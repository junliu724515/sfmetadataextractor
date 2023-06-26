"""This module provides the sfmetadataextractor CLI."""
# sfmetadataextractor/cli.py

from typing import Optional

import typer

from sfmetadataextractor import __app_name__, __version__, extractor

app = typer.Typer()

@app.command(name="extract")
def extract_metadata(input_file: str = typer.Option(
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
    extractorhandler = extractor.ExtractorHandler(input_file, output_file, metadata_types)
    extractorhandler.extract()
    typer.echo(
        f"{metadata_types} metadata types extracted successfully and saved in {output_file}")


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
    return
