"""This module provides the sfmetadataextractor CLI."""
# sfmetadataextractor/cli.py

from typing import Optional

import typer

from sfmetadataextractor import __app_name__, __version__, class_patch, extension_mapping, extractor, generate_tests

app = typer.Typer()


@app.command(name="extract")
def extract_metadata(
        input_file: str = typer.Option(
            ...,
            "--inputFile",
            "-i",
            help="The input metadata wsdl file to process."),
        output_file: str = typer.Option(
            ...,
            "--outputFile",
            "-o",
            help="The output wsdl file with the metadata extracted."),
        metadata_types: str = typer.Option(
            ...,
            "--MetadataTypes",
            "-m",
            help="Comma-separated list of metadataTypes to be extracted, "
                 + "for example: ApexClass,CustomObject"),
):
    """Extract selected metadata types from Salesforce Metadata WSDL file."""
    if 'wsdl' not in input_file.lower():
        typer.echo("Input file must be a Salesforce Metadata WSDL file.")
        raise typer.Exit()
    typer.echo(f"Extracting metadata from {input_file}")
    extractor_handler = extractor.ExtractorHandler(input_file, output_file, metadata_types)
    extractor_handler.extract()
    typer.echo(
        f"{metadata_types} metadata types extracted successfully and saved in {output_file}")


# wrote a patch command using class_patch.py
@app.command(name="patch")
def patch_metadata(
        extension_map_file: str = typer.Option(
            ...,
            "--extensionMapFile",
            "-e",
            help="The extention map file to read all metadata extensions for the patching"),
        input_file: str = typer.Option(
            ...,
            "--inputFile",
            "-i",
            help="The input apex class file to process."),
        output_file: str = typer.Option(
            ...,
            "--outputFile",
            "-o",
            help="The output apex patched file."),
        api_version: str = typer.Option(
            ...,
            "--apiVersion",
            "-a",
            help="api version to be used for the patching, for example: 58.0"),
):
    """Patch apex class with the metadata extensions."""
    typer.echo(f"Patching apex class in {input_file}")
    class_patch_handler = class_patch.ClassPatch(extension_map_file, input_file, output_file, api_version)
    class_patch_handler.patch()
    typer.echo(
        f"{input_file} class has been patched successfully and saved in {output_file}")


@app.command(name="extensionMap")
def extension_map(
        input_file: str = typer.Option(
            ...,
            "--inputFile",
            "-i",
            help="The input metadata wsdl file to process."),
        output_file: str = typer.Option(
            ...,
            "--outputFile",
            "-o",
            help="The output metadata extension mapping file."),
):
    """Extract metadata extensions from Salesforce Metadata WSDL file."""
    if 'wsdl' not in input_file.lower():
        typer.echo("Input file must be a Salesforce Metadata WSDL file.")
        raise typer.Exit()
    typer.echo(f"Extracting metadata extensions from {input_file}")
    mapping_handler = extension_mapping.ExtensionMapping(input_file, output_file)
    mapping_handler.map()
    typer.echo(
        f"Metadata extensions extracted successfully and saved in {output_file}")

@app.command(name="generateUnitTests")
def generate_unit_test(
        input_file: str = typer.Option(
            ...,
            "--inputFile",
            "-i",
            help="The input apex class."),
        output_file: str = typer.Option(
            ...,
            "--outputFile",
            "-o",
            help="The output unit test class file."),
):
    typer.echo(f"Generating unit tests for {input_file}")
    generate_tests_handler = generate_tests.generateTests(input_file, output_file)
    generate_tests_handler.generate()
    typer.echo(
        f"Unit tests generated successfully and saved in {output_file}")

def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()


@app.callback()
def main(
        version: Optional[bool] = typer.Option(
            None,
            "--version",
            "-v",
            help="Show the application's version and exit.",
            callback=_version_callback,
            is_eager=True,
        )
) -> None:
    """cli main entry point."""
    # return
