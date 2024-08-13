# sfmetadataextractor

This is a python command line tool to split/extract components from Salesforce metadata wsdl file

Blog Post: https://jmcloudservices.com/blog/a-python-tool-to-upgrade-apex-wrapper-salesforce-metadata-api

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/YOUTUBE_VIDEO_ID_HERE/0.jpg)](https://www.youtube.com/watch?v=4cC4WUGKTYc)

---

[![CI/CD Pipeline](https://github.com/junliu724515/sfmetadataextractor/actions/workflows/release.yml/badge.svg?style=for-the-badge&logo=github)](https://github.com/junliu724515/sfmetadataextractor/actions/workflows/release.yml)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/junliu724515/sfmetadataextractor.svg?include_prereleases)
![GitHub issues](https://img.shields.io/github/issues/junliu724515/sfmetadataextractor)



## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

---

## Installation

Option 1: Install from whl file (Recommended)

Download the latest whl file from the release page and run the following command
```bash
pip install sfmetadataextractor-v0.1.3-py3-none-any.whl
```

Option 2: Install from source code 

Clone/Build/Install this repository:
```bash
git clone https://github.com/junliu724515/sfmetadataextractor.git

cd sfmetadataextractor/

python -m pip install . (In the project folder)

```

## Uninstallation

```bash
 pip uninstall sfmetadataextractor
```

**Note:** This project requires [Python](https://www.python.org/).

---

## Usage

**1.** Command to extract metadata component:

```bash
sfmetadataextractor extract --help
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

sfmetadataextractor extract -i metadata.wsdl -o metadata_extracted.wsdl -m ApexClass,CustomObject
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
   
sfmetadataextractor extensionMap -i metadata.wsdl -o extension_mapping.json
```

**3.** Command to patch apex class with extension mapping file:

Reason to patch: The WSDL file may use an inheritance model that is not directly supported by the generated Apex code. 
                 This can lead to issues where the generated code does not correctly reflect the structure and relationships defined in the WSDL. 
                 So we need to patch the class using the extension_mapping.json file

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

sfmetadataextractor patch -e extension_mapping.json -i MetadataServiceImported.cls -o MetadataService.cls -a 61.0
```

**4.** Command to generate unit tests:

```bash
Usage: sfmetadataextractor generateUnitTests [OPTIONS]

Options:
  -i, --inputFile TEXT   The input apex class.  [required]
  -o, --outputFile TEXT  The output unit test class file.  [required]
  --help                 Show this message and exit.


Example:

sfmetadataextractor generateUnitTests -i MetadataService.cls -o MetadataServiceTest.cls
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

