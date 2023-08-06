"""Generate a mapping of file extensions to file types from the SF Metadata API"""
import xml.etree.ElementTree as ET
import json
import typer

from sfmetadataextractor.utils import NS, get_attrib_value

class ExtensionMapping:
    """ExtensionMapping class generates mapping file of metadata extensions. It parses an input XML file"""
    def __init__(self, input_file: str, out_file: str) -> None:
        self.out_file = out_file
        self.root_node = ET.parse(input_file).getroot()
        self.elements = []
        self.extensions = {}

    def map(self) -> None:
        """Method to perform the mapping process."""
        for element_type in ["complexType", "simpleType"]:
            elements = self.root_node.findall(f".//{NS}{element_type}")
            self.elements.extend(elements)
        for element in self.elements:
            self.traverse_metadata(element)
        self.create_extension_map_file()

    def traverse_metadata(self, element) -> None:
        """Function to extract metadata from XML."""
        # Searching for complexType and simpleType XML elements

        if element is None:
            raise typer.BadParameter(
                "Could not find metadata type MetadataExtension")
        metadata_name = get_attrib_value(element, "name")

        # Traverse extension elements
        extension = element.find(f".//{NS}extension")
        if extension is not None:
            # Remove the tns: prefix from the base attribute
            extension_name = get_attrib_value(extension, "base", 4)
            self.extensions[metadata_name] = extension_name

    def create_extension_map_file(self) -> None:
        """Function to create extension mapping file."""
        with open(self.out_file, 'w', encoding='utf-8') as file:
            json.dump(self.extensions, file, indent=4)  # pretty-printing
