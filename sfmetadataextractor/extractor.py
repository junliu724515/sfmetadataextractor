import xml.etree.ElementTree as ET
import typer

# Forming the namespace for XML elements
ns = "{http://www.w3.org/2001/XMLSchema}"
ns_wsdl = "{http://schemas.xmlsoap.org/wsdl/}"


def get_type_name(element: object) -> str:
    """Helper function to extract the type name from an element's 'type' attribute."""
    return element.attrib['type'][4:]


def get_element_name(element: object) -> str:
    """Helper function to extract the element name from an element's attribute."""
    return element.attrib['element'][4:]

def get_base_name(element: object) -> str:
    """Helper function to extract the base name from an element's attribute."""
    return element.attrib['base'][4:]


def extract_metadata(metadata_root: str, root_node: object, elements: dict) -> dict:
    """Function to extract metadata from XML."""
    # Searching for complexType and simpleType XML elements
    for element_type in ["complexType", "simpleType"]:
        root_element = root_node.find(
            f".//{ns}{element_type}[@name='{metadata_root}']")
        if root_element is not None:
            break

    # If root_element is still None, it was not found in root_node.
    # We might raise an exception or handle this case appropriately here.
    if root_element is not None:
        elements[metadata_root] = root_element
        # get the extension elements under the complex types
        sequence_elements = root_element.findall(f".//{ns}element")
        if sequence_elements:
            for sequence_element in sequence_elements:
                type_name = get_type_name(sequence_element)
                if 'tns' in sequence_element.attrib['type'] and type_name not in elements:
                    extract_metadata(type_name, root_node, elements)

        # get the extension elements under the complex types
        extension = root_element.find(f".//{ns}extension")
        if extension is not None:
            extension_name = get_base_name(extension)
            extract_metadata(extension_name, root_node, elements)

        return elements
    else:
        raise typer.BadParameter(
            "Could not find metadata type " + metadata_root)


def extract_messages(root_node: object, messages: dict, elements: dict) -> dict:
    """Function to extract messages from XML."""
    message_elements = root_node.findall(f".//{ns_wsdl}message")
    for message in message_elements:
        messages[message.attrib['name']] = message
        extract_message_elements(message, root_node, elements)
    return messages

# find all the complex or simple types under the current message_node


def extract_message_elements(message_node: object, root_node: object, elements: dict) -> dict:
    """Function to extract message elements from XML."""
    message_elements = message_node.findall(f".//{ns_wsdl}part")

    for message_element in message_elements:
        element_name = get_element_name(message_element)

        if element_name not in elements:
            element = root_node.find(f".//{ns}element[@name='{element_name}']")
            elements[element_name] = element

            for child_element in element.findall(f'.//{ns}element'):
                type_name = child_element.attrib['type']

                if 'tns' in type_name:
                    type_name = get_type_name(child_element)
                    extract_metadata(type_name, root_node, elements)
    return elements


def write_to_fileile(out_file: str, root_node: object, elements: dict, messages: dict):
    with open(out_file, 'wb') as f:
        contents = f"""<?xml version="1.0" encoding="UTF-8"?>
<definitions targetNamespace="http://soap.sforce.com/2006/04/metadata" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns="http://schemas.xmlsoap.org/wsdl/" xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/" xmlns:tns="http://soap.sforce.com/2006/04/metadata">
<types>
<xsd:schema elementFormDefault="qualified" targetNamespace="http://soap.sforce.com/2006/04/metadata">"""
        for element in elements.values():
            contents += ET.tostring(element).decode()
        contents += """</xsd:schema>
                   </types>
                   """
        for message in messages.values():
            contents += ET.tostring(message).decode()
        contents += f"""{ET.tostring(root_node.find(f".//{ns_wsdl}portType")).decode()}
        {ET.tostring(root_node.find(f".//{ns_wsdl}binding")).decode()}"""

        # rename Metadata to MetadataPort
        port_node = root_node.find(f".//{ns_wsdl}port")
        port_node.set('name', 'MetadataPort')
        contents += f"""{ET.tostring(root_node.find(f".//{ns_wsdl}service")).decode()}
        </definitions>"""
        f.write(contents.encode())


class Extractor:
    """
    The Extractor class handles the extraction process. It parses an input XML file, 
    extracts the necessary data, and writes it to an output file.
    """
    def __init__(self, input_file: str, out_file: str, metadataTypes: str) -> None:
        self.out_file = out_file
        self.root_node = ET.parse(input_file).getroot()
        self.metadataTypes = metadataTypes.split(",")
        self.elements = dict()
        self.messages = dict()

    def extract(self) -> None:
        """Method to perform the extraction process."""
        for metadataType in self.metadataTypes:
            extract_metadata(metadataType, self.root_node, self.elements)
        extract_messages(self.root_node, self.messages, self.elements)
        write_to_fileile(self.out_file, self.root_node, self.elements, self.messages)
