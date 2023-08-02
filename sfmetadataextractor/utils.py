"""This module provides the sfmetadataextractor common functions."""
# sfmetadataextractor/utils.py

# Forming the namespace for XML elements
NS = "{http://www.w3.org/2001/XMLSchema}"
NS_WSDL = "{http://schemas.xmlsoap.org/wsdl/}"

def get_attrib_value(element, attrib, prefix_len=0) -> str:
    """Helper function to extract the attribute value from an element's attribute."""
    val = element.attrib.get(attrib)
    if val and len(val) > prefix_len:
        return val[prefix_len:]
    return ''


def write_to_file(out_file: str, contents: bytes) -> None:
    """Write the extracted data to a file."""
    with open(out_file, 'wb') as file:
        file.write(contents)
