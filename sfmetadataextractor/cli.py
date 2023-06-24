"""This module provides the sfmetadataextractor CLI."""
# sfmetadataextractor/cli.py

from typing import Optional

import typer

from sfmetadataextractor import __app_name__, __version__
from sfmetadataextractor.extractor import Extractor


app = typer.Typer()


@app.command(name="extract")
def extract_metadata(inputFile: str =  typer.Option(
                                            ...,
                                            "--inputFile",
                                            "-i",
                                            help="The input metadata file to process."), 
                    outputFile: str = typer.Option(
                                            ...,
                                            "--outputFile",
                                            "-o",
                                            help="The output file with the metadata extracted."),
                    MetadataTypes: str = typer.Option(
                                            ...,
                                            "--MetadataTypes",
                                            "-m",
                                            help="Comma-separated list of metadataTypes to be extracted, for example: ApexClass,CustomObject"),
                    ):
    """Extract selected metadata types from Salesforce Metadata WSDL file."""
    typer.echo(f"Extracting metadata from {inputFile}") 
    extractorhandler= Extractor(inputFile,outputFile,MetadataTypes)
    extractorhandler.extract()
    typer.echo(f"{MetadataTypes} metadata types extracted successfully and saved in {outputFile}")
     
    


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
    return






