# sfmetadataextractor

This is a python command line tool to split/extract components from Salesforce metadata wsdl file

Blog Post: https://jmcloudservices.com/blog/a-python-tool-to-upgrade-apex-wrapper-salesforce-metadata-api
---

![Build and Test](https://github.com/junliu724515/sfmetadataextractor/blob/beta/test/.github/workflows/release.yml/badge.svg)
![GitHub issues](https://github.com/junliu724515/sfmetadataextractor.svg)

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

---

## Installation

**1.** Clone/Build/Install this repository:

```bash
git clone https://github.com/junliu724515/sfmetadataextractor.git

cd sfmetadataextractor/

python -m pip install . (In the project folder)

```

## Uninstallation

```bash
 pip uninstall sfmetadataextractor
```

**2.** Navigate to the project directory:

The following files are included in this project:

- README.md
- setup.py
- sfmetadataextractor/__init__.py
- sfmetadataextractor/__main__.py
- sfmetadataextractor/class_patch.py
- sfmetadataextractor/cli.py
- sfmetadataextractor/extension_mapping.py
- sfmetadataextractor/extractor.py
- sfmetadataextractor/utils.py
- tests/__init__.py
- tests/test_sfmetadatasplitter.py

**Note:** This project requires [Python](https://www.python.org/).

---

## Usage

**1.** Command to extract metadata component:

```bash
python sfmetadataextractor extract --help
  Usage: python sfmetadataextractor extract [OPTIONS]

  Extract selected metadata types from Salesforce Metadata WSDL file.

Options:
  -i, --inputFile TEXT      The input metadata wsdl file to process.
                            [required]
  -o, --outputFile TEXT     The output wsdl file with the metadata extracted.
                            [required]
  -m, --MetadataTypes TEXT  Comma-separated list of metadataTypes to be
                            extracted, for example: ApexClass,CustomObject
                            [required]
  --help                    Show this message and exit.


Example

    python sfmetadataextractor extract -i metadata.wsdl -o metadata_extracted.wsdl -m ApexClass,CustomObject
```

**2.** Command to create an extension mapping file for apex class patching:

```bash
Usage: python sfmetadataextractor extensionMap [OPTIONS]

  Extract metadata extensions from Salesforce Metadata WSDL file.

Options:
  -i, --inputFile TEXT   The input metadata wsdl file to process.  [required]
  -o, --outputFile TEXT  The output metadata extension mapping file.
                         [required]
  --help                 Show this message and exit.

Example:
   python sfmetadataextractor extensionMap -i metadata.wsdl -o extension_mapping.json
```

**3.** Command to patch apex class with extension mapping file:

```bash
Usage: python sfmetadataextractor patch [OPTIONS]

  Patch apex class with the metadata extensions.

Options:
  -e, --extensionMapFile TEXT  The extention map file to read all metadata
                               extensions for the patching  [required]
  -i, --inputFile TEXT         The input apex class file to process.
                               [required]
  -o, --outputFile TEXT        The output apex patched file.  [required]
  -a, --apiVersion TEXT        api version to be used for the patching, for
                               example: 58.0  [required]
  --help                       Show this message and exit.
  
Example:
   python sfmetadataextractor patch -e extension_mapping.json -i MetadataServiceImported.cls -o MetadataService.cls -a 58.0
```

**4.** Command to generate unit tests:

```bash
Usage: sfmetadataextractor generateUnitTests [OPTIONS]

Options:
  -i, --inputFile TEXT   The input apex class.  [required]
  -o, --outputFile TEXT  The output unit test class file.  [required]
  --help                 Show this message and exit.


Example:
   python sfmetadataextractor generateUnitTests -i MetadataService.cls -o MetadataServiceTest.cls

```

For more details, Please refer to the --help command or my blog post https://jmcloudservices.com/blog/a-python-tool-to-upgrade-apex-wrapper-salesforce-metadata-api.


**Features**
- Feature 1: Extract the components selected from Salesforce Metadata wsdl file.
- Feature 2: Generate extension mapping file, that is required for patching the apex class generated from wsdl file from feature 1.
- Feature 3: Patch the apex class generated with the mapping file and generate unit tests.

**Contributing**
- I welcome contributions from the community! Please read our contributing guidelines before submitting a pull request.

License
This project is licensed under the MIT License. See LICENSE for more details.

Contact
For questions or feedback, please reach out to jun.liu@jmcloudservices.com.

