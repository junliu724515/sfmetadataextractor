from typer.testing import CliRunner

from xml.etree.ElementTree import fromstring
from sfmetadataextractor import __app_name__, __version__, cli
from sfmetadataextractor.extractor import get_base_name, get_element_name, get_type_name, Extractor


runner = CliRunner()

def test_version():
    result = runner.invoke(cli.app, ["--version"])
    assert result.exit_code == 0
    assert f"{__app_name__} v{__version__}\n" in result.stdout

def test_get_base_name():
    assert get_base_name(fromstring("<element base=\"tns:ExampleBase\"/>")) == "ExampleBase"

def test_get_element_name():
    assert get_element_name(fromstring("<element element=\"tns:ExampleElement\"/>")) == "ExampleElement"

def test_get_type_name():
    assert get_type_name(fromstring("<element type=\"tns:ExampleType\"/>")) == "ExampleType"
