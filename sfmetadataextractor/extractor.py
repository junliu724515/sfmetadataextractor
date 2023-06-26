"""This module provides the Metadata extractor."""
# sfmetadataextractor/extractor.py

import xml.etree.ElementTree as ET
import typer

from sfmetadataextractor.utils import NS_WSDL, NS, get_attrib_value, write_to_file

class ExtractorHandler:
    """
    The Extractor class handles the extraction process. It parses an input XML file, 
    extracts the necessary data, and writes it to an output file.
    """

    def __init__(self, input_file: str, out_file: str, metadata_types: str) -> None:
        self.out_file = out_file
        self.root_node = ET.parse(input_file).getroot()
        self.metadata_types = metadata_types.split(",")
        self.elements = {}
        self.messages = {}

    def extract(self) -> None:
        """Method to perform the extraction process."""
        for metadata_type in self.metadata_types:
            self.traverse_metadata(metadata_type)
        self.traverse_messages()
        self.write_to_file()

    def traverse_metadata(self, metadata_root: str) -> dict:
        """Function to extract metadata from XML."""
        # Searching for complexType and simpleType XML elements
        for element_type in ["complexType", "simpleType"]:
            root_element = self.root_node.find(
                f".//{NS}{element_type}[@name='{metadata_root}']")
            if root_element is not None:
                break

        # If root_element is still None, it was not found in root_node.
        # We might raise an exception or handle this case appropriately here.
        if root_element is not None:
            self.elements[metadata_root] = root_element
            # get the extension elements under the complex types
            sequence_elements = root_element.findall(f".//{NS}element")
            if sequence_elements:
                for sequence_element in sequence_elements:
                    type_name = get_attrib_value(sequence_element, "type")
                    if 'tns' in type_name:
                        # remove the tns: prefix from the type attribute
                        type_name = get_attrib_value(
                            sequence_element, "type", 4)
                        if type_name not in self.elements:
                            # if the type name is not in elements, we need to traverse it
                            self.traverse_metadata(type_name)

            # get the extension elements under the complex types
            extension = root_element.find(f".//{NS}extension")
            if extension is not None:
                # remove the tns: prefix from the base attribute
                extension_name = get_attrib_value(extension, "base", 4)
                self.traverse_metadata(extension_name)
            return self.elements
        else:
            raise typer.BadParameter(
                "Could not find metadata type " + metadata_root)

    def traverse_messages(self) -> dict:
        """Function to extract messages from XML."""
        message_elements = self.root_node.findall(f".//{NS_WSDL}message")
        for message in message_elements:
            self.messages[message.attrib['name']] = message
            self.traverse_message_elements(message)
        return self.messages

    # find all the complex or simple types under the current message_node
    def traverse_message_elements(self, message_node: object) -> dict:
        """Function to extract message elements from XML."""
        message_elements = message_node.findall(f".//{NS_WSDL}part")

        for message_element in message_elements:
            # remove the tns: prefix from the element attribute
            element_name = get_attrib_value(message_element, "element", 4)

            if element_name not in self.elements:
                element = self.root_node.find(
                    f".//{NS}element[@name='{element_name}']")
                self.elements[element_name] = element

                for child_element in element.findall(f'.//{NS}element'):
                    type_name = get_attrib_value(child_element, "type")
                    if 'tns' in type_name:
                        # remove the tns: prefix from the type attribute
                        type_name = get_attrib_value(child_element, "type", 4)
                        if type_name not in self.elements:
                            self.traverse_metadata(type_name)
        return self.elements

    def write_to_file(self):
        """Method to write the extracted data to a file. write the contents to a file in the format required by the Metadata API"""
        contents = f"""<?xml version="1.0" encoding="UTF-8"?>
    <definitions targetNamespace="http://soap.sforce.com/2006/04/metadata" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns="http://schemas.xmlsoap.org/wsdl/" xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/" xmlns:tns="http://soap.sforce.com/2006/04/metadata">
    <types>
    <xsd:schema elementFormDefault="qualified" targetNamespace="http://soap.sforce.com/2006/04/metadata">"""
        for element in self.elements.values():
            contents += ET.tostring(element).decode()
        contents += """</xsd:schema>
                    </types>
                    """
        for message in self.messages.values():
            contents += ET.tostring(message).decode()
        contents += f"""{ET.tostring(self.root_node.find(f".//{NS_WSDL}portType")).decode()}
            {ET.tostring(self.root_node.find(f".//{NS_WSDL}binding")).decode()}"""

        # rename Metadata to MetadataPort
        port_node = self.root_node.find(f".//{NS_WSDL}port")
        port_node.set('name', 'MetadataPort')
        contents += f"""{ET.tostring(self.root_node.find(f".//{NS_WSDL}service")).decode()}
            </definitions>"""
        write_to_file(self.out_file, contents.encode())
