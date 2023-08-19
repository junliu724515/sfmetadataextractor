import textwrap


class generateTests:
    """This class generate unit test class for MetadataService.cls"""

    def __init__(self, input_file: str, output_file: str) -> None:
        self.input_file = input_file
        self.output_file = output_file
        self.class_names = []
        self.class_names_with_get_records = []
        self.class_names_with_get_results = []

    def generate(self):
        """Generate unit test class for MetadataService.cls"""
        self.read_input_file()
        self.write_new_file()

    def read_input_file(self) -> None:
        with open(self.input_file, 'r') as file:
            while True:
                line = file.readline()
                trimmed_line = line.strip()
                if 'public class' in trimmed_line and 'MetadataService' not in trimmed_line:
                    self.class_names.append(trimmed_line.split(' ')[2])
                if 'implements IReadResult' in trimmed_line:
                    self.class_names_with_get_records.append(trimmed_line.split(' ')[2])
                if 'implements IReadResponseElement' in trimmed_line:
                    self.class_names_with_get_results.append(trimmed_line.split(' ')[2])
                if not line:
                    break

    def write_new_file(self) -> None:

        with open(self.output_file, 'w') as file:
            cover_generated_code_types = "".join(
                ["new MetadataService." + class_name + "();\n                        " for class_name in
                 self.class_names])
            elf_missing_get_records = "".join(
                ["new MetadataService." + class_name + "().getRecords();\n                        " for class_name in
                 self.class_names_with_get_records])
            elf_missing_get_results = "".join(
                ["new MetadataService." + class_name + "().getResult();\n                         " for class_name in
                 self.class_names_with_get_results])
            test_class_code = textwrap.dedent(f"""
                    @IsTest
                    public class MetadataServiceTest {{
                    
                      private class WebServiceMockImpl implements WebServiceMock
                      {{
                        public void doInvoke(
                                Object stub, Object request, Map<String, Object> response,
                                String endpoint, String soapAction, String requestName,
                                String responseNS, String responseName, String responseType)
                        {{
                          if(request instanceof MetadataService.retrieve_element)
                            response.put('response_x', new MetadataService.retrieveResponse_element());
                          else if(request instanceof MetadataService.checkDeployStatus_element)
                            response.put('response_x', new MetadataService.checkDeployStatusResponse_element());
                          else if(request instanceof MetadataService.listMetadata_element)
                            response.put('response_x', new MetadataService.listMetadataResponse_element());
                          else if(request instanceof MetadataService.checkRetrieveStatus_element)
                            response.put('response_x', new MetadataService.checkRetrieveStatusResponse_element());
                          else if(request instanceof MetadataService.describeMetadata_element)
                            response.put('response_x', new MetadataService.describeMetadataResponse_element());
                          else if(request instanceof MetadataService.deploy_element)
                            response.put('response_x', new MetadataService.deployResponse_element());
                          else if(request instanceof MetadataService.updateMetadata_element)
                            response.put('response_x', new MetadataService.updateMetadataResponse_element());
                          else if(request instanceof MetadataService.renameMetadata_element)
                            response.put('response_x', new MetadataService.renameMetadataResponse_element());
                          else if(request instanceof  MetadataService.cancelDeploy_element)
                            response.put('response_x', new MetadataService.cancelDeployResponse_element());
                          else if(request instanceof  MetadataService.deleteMetadata_element)
                            response.put('response_x', new MetadataService.deleteMetadataResponse_element());
                          else if(request instanceof  MetadataService.upsertMetadata_element)
                            response.put('response_x', new MetadataService.upsertMetadataResponse_element());
                          else if(request instanceof  MetadataService.createMetadata_element)
                            response.put('response_x', new MetadataService.createMetadataResponse_element());
                          else if(request instanceof  MetadataService.deployRecentValidation_element)
                            response.put('response_x', new MetadataService.deployRecentValidationResponse_element());
                          else if(request instanceof MetadataService.describeValueType_element)
                            response.put('response_x', new MetadataService.describeValueTypeResponse_element());
                          else if(request instanceof MetadataService.checkRetrieveStatus_element)
                            response.put('response_x', new MetadataService.checkRetrieveStatusResponse_element());
                          return;
                        }}
                      }}
                    
                      @IsTest
                      private static void coverGeneratedCodeCRUDOperations()
                      {{
                        // Null Web Service mock implementation
                        System.Test.setMock(WebServiceMock.class, new WebServiceMockImpl());
                        // Only required to workaround a current code coverage bug in the platform
                        MetadataService metaDataService = new MetadataService();
                        // Invoke operations
                        Test.startTest();
                        MetadataService.MetadataPort metaDataPort = new MetadataService.MetadataPort();
                        Test.stopTest();
                      }}
                    
                      @IsTest
                      private static void coverGeneratedCodeFileBasedOperations1()
                      {{
                        // Null Web Service mock implementation
                        System.Test.setMock(WebServiceMock.class, new WebServiceMockImpl());
                        // Only required to workaround a current code coverage bug in the platform
                        MetadataService metaDataService = new MetadataService();
                        // Invoke operations
                        Test.startTest();
                        MetadataService.MetadataPort metaDataPort = new MetadataService.MetadataPort();
                        metaDataPort.retrieve(null);
                        metaDataPort.checkDeployStatus(null, false);
                        metaDataPort.listMetadata(null, null);
                        metaDataPort.describeMetadata(null);
                        metaDataPort.deploy(null, null);
                        metaDataPort.checkDeployStatus(null, false);
                        metaDataPort.updateMetadata(null);
                        metaDataPort.renameMetadata(null, null, null);
                        metaDataPort.cancelDeploy(null);
                        Test.stopTest();
                      }}
                    
                      @IsTest
                      private static void coverGeneratedCodeFileBasedOperations2()
                      {{
                        // Null Web Service mock implementation
                        System.Test.setMock(WebServiceMock.class, new WebServiceMockImpl());
                        // Only required to workaround a current code coverage bug in the platform
                        MetadataService metaDataService = new MetadataService();
                        // Invoke operations
                        Test.startTest();
                        MetadataService.MetadataPort metaDataPort = new MetadataService.MetadataPort();
                        metaDataPort.deleteMetadata(null, null);
                        metaDataPort.upsertMetadata(null);
                        metaDataPort.createMetadata(null);
                        metaDataPort.deployRecentValidation(null);
                        metaDataPort.describeValueType(null);
                        metaDataPort.checkRetrieveStatus(null, null);
                        Test.stopTest();
                      }}
                      
                      @IsTest
                      private static void coverGeneratedCodeTypes()
                      {{
                        // Reference types
                        Test.startTest();
                        new MetadataService();
                        {cover_generated_code_types}
                        Test.stopTest();
                       }}
                       
                      @IsTest
                      private static void elfMissingGetRecordsTest() {{ // elf patch
                        Test.startTest();
                        {elf_missing_get_records}
                        Test.stopTest();
                      }}
                      
                       @IsTest
                       private static void elfMissingGetResultTest() {{ // elf patch
                         Test.startTest();
                         {elf_missing_get_results}   
                         Test.stopTest();
                       
                       }}
                       
                    }}
             """)
            file.write(test_class_code)
