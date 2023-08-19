"""Unit tests for sfmetadataextractor.cli"""
import os
import filecmp
from xml.etree.ElementTree import fromstring
from typer.testing import CliRunner

from sfmetadataextractor import __app_name__, __version__, cli
from sfmetadataextractor.utils import get_attrib_value

runner = CliRunner()


def test_version():
    """Test version"""
    result = runner.invoke(cli.app, ["--version"])
    assert result.exit_code == 0
    assert f"{__app_name__} v{__version__}\n" in result.stdout


def test_get_base_name():
    """test remove the tns: prefix from the base attribute"""
    assert get_attrib_value(fromstring(
        "<element base=\"tns:ExampleBase\"/>"), "base", 4) == "ExampleBase"


def test_get_element_name():
    """test get attribute value"""
    assert get_attrib_value(fromstring(
        "<element element=\"tns:ExampleElement\"/>"), "element") == "tns:ExampleElement"


def test_extractor():
    """test extractor"""
    result = runner.invoke(cli.app,
                           ["extract", "-i", "test_files/Metadata-test.wsdl", "-o", "output.wsdl", "-m", "Flow"])
    assert result.exit_code == 0
    # print(result.stdout)
    assert f"Flow metadata types extracted successfully and saved in output.wsdl\n" in result.stdout
    f1 = "output.wsdl"
    f2 = "test_files/output-test.wsdl"
    assert filecmp.cmp(f1, f2, shallow=True) == True
    os.remove("output.wsdl")


def test_extensionMapping():
    """test extractor"""
    result = runner.invoke(cli.app, ["extensionMap", "-i", "test_files/Metadata-test.wsdl", "-o", "mapping.json"])
    assert result.exit_code == 0
    # print(result.stdout)
    assert f"Metadata extensions extracted successfully and saved in mapping.json\n" in result.stdout
    f1 = "mapping.json"
    f2 = "test_files/mapping-test.json"
    with open(f1, 'r') as file1, open(f2, 'r') as file2:
        assert file1.readlines() == file2.readlines(), "Files content is not the same"
    os.remove("mapping.json")


def test_patch():
    """test extractor"""
    result = runner.invoke(cli.app, ["patch", "-e", "test_files/mapping-test.json", "-i",
                                     "test_files/MetadataServiceImported-test.cls", "-o", "MetadataService.cls", "-a",
                                     "58.0"])
    assert result.exit_code == 0
    # print(result.stdout)
    assert f"test_files/MetadataServiceImported-test.cls class has been patched successfully and saved in MetadataService.cls\n" in result.stdout
    with open('MetadataService.cls', 'r') as file1, open('test_files/MetadataService-test.cls', 'r') as file2:
        assert file1.readlines() == file2.readlines(), "Files content is not the same"
    os.remove("MetadataService.cls")


def test_generate_unit_tests():
    """test unit tests generation"""
    result = runner.invoke(cli.app, ["generateUnitTests", "-i", "test_files/MetadataService-test.cls", "-o",
                                     "MetadataServiceTest.cls"])
    assert result.exit_code == 0
    # print(result.stdout)
    assert f"Unit tests generated successfully and saved in MetadataServiceTest.cls\n" in result.stdout
    with open('MetadataServiceTest.cls', 'r') as file1, open('test_files/MetadataServiceTest.test.cls', 'r') as file2:
        assert file1.readlines() == file2.readlines(), "Files content is not the same"
    os.remove("MetadataServiceTest.cls")
