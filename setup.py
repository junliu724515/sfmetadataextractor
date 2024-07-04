from setuptools import setup, find_packages

setup(
    name="sfmetadataextractor",
    version="0.1.2-beta.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "sfmetadataextractor=sfmetadataextractor.cli:main",
        ],
    },
    install_requires=[
        "typer"
    ],
    author="Jun Liu",
    author_email="jun.liu@jmcloudservices.com",
    description="A tool for extracting metadata from Salesforce WSDL files.",
    url="https://github.com/junliu724515/sfmetadataextractor",
)