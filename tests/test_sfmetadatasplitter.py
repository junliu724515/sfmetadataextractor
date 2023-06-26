"""Unit tests for sfmetadataextractor.cli"""
import os
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
    result = runner.invoke(cli.app, ["extract --help"])
    # assert result.exit_code == 0
    print(result.stdout)
    assert f"Flow,PermissionSet,CustomObject,CustomField,RecordType metadata types extracted successfully and saved in output\n" in result.stdout


def teardown_function():
    """remove the output file"""
    os.remove("output.wsdl")
