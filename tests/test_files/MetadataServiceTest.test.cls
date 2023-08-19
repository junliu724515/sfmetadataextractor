
@IsTest
public class MetadataServiceTest {

  private class WebServiceMockImpl implements WebServiceMock
  {
    public void doInvoke(
            Object stub, Object request, Map<String, Object> response,
            String endpoint, String soapAction, String requestName,
            String responseNS, String responseName, String responseType)
    {
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
    }
  }

  @IsTest
  private static void coverGeneratedCodeCRUDOperations()
  {
    // Null Web Service mock implementation
    System.Test.setMock(WebServiceMock.class, new WebServiceMockImpl());
    // Only required to workaround a current code coverage bug in the platform
    MetadataService metaDataService = new MetadataService();
    // Invoke operations
    Test.startTest();
    MetadataService.MetadataPort metaDataPort = new MetadataService.MetadataPort();
    Test.stopTest();
  }

  @IsTest
  private static void coverGeneratedCodeFileBasedOperations1()
  {
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
  }

  @IsTest
  private static void coverGeneratedCodeFileBasedOperations2()
  {
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
  }

  @IsTest
  private static void coverGeneratedCodeTypes()
  {
    // Reference types
    Test.startTest();
    new MetadataService();
    new MetadataService.SharingReason();
    new MetadataService.FlowDecision();
    new MetadataService.PermissionSetTabSetting();
    new MetadataService.FlowElementReferenceOrValue();
    new MetadataService.FlowWaitEventOutputParameter();
    new MetadataService.CallOptions_element();
    new MetadataService.SaveResult();
    new MetadataService.ReadResult();
    new MetadataService.PermissionSetUserPermission();
    new MetadataService.MktDataModelFieldAttributes();
    new MetadataService.ExtendedErrorDetails();
    new MetadataService.SharingRecalculation();
    new MetadataService.readMetadataResponse_element();
    new MetadataService.upsertMetadata_element();
    new MetadataService.FlowStageStepInputParameter();
    new MetadataService.MktDataLakeFieldAttributes();
    new MetadataService.ValueTypeField();
    new MetadataService.FlowAssignmentItem();
    new MetadataService.RunTestsResult();
    new MetadataService.FlowOutputFieldAssignment();
    new MetadataService.PermissionSetFlowAccess();
    new MetadataService.FlowApexPluginCallOutputParameter();
    new MetadataService.RetrieveResult();
    new MetadataService.FlowVisibilityRule();
    new MetadataService.UpsertResult();
    new MetadataService.renameMetadata_element();
    new MetadataService.DeployDetails();
    new MetadataService.FlowStageStepEntryActionInputParameter();
    new MetadataService.CustomObject();
    new MetadataService.FlowCollectionMapItem();
    new MetadataService.PicklistValue();
    new MetadataService.cancelDeployResponse_element();
    new MetadataService.FlowMetadataValue();
    new MetadataService.ValueSettings();
    new MetadataService.ProfileObjectPermissions();
    new MetadataService.PermissionSetObjectPermissions();
    new MetadataService.DeployMessage();
    new MetadataService.MktDataModelAttributes();
    new MetadataService.FlowWait();
    new MetadataService.FlowStage();
    new MetadataService.FlowWaitEventInputParameter();
    new MetadataService.ArticleTypeChannelDisplay();
    new MetadataService.SessionHeader_element();
    new MetadataService.checkRetrieveStatus_element();
    new MetadataService.SearchLayouts();
    new MetadataService.FlowScreenFieldInputParameter();
    new MetadataService.retrieve_element();
    new MetadataService.Package_x();
    new MetadataService.FlowStageStep();
    new MetadataService.DeleteResult();
    new MetadataService.deployRecentValidationResponse_element();
    new MetadataService.PackageTypeMembers();
    new MetadataService.FlowCondition();
    new MetadataService.deployRecentValidation_element();
    new MetadataService.FlowScreenRule();
    new MetadataService.DebuggingHeader_element();
    new MetadataService.FlowCollectionSortOption();
    new MetadataService.PermissionSetApexPageAccess();
    new MetadataService.DescribeMetadataObject();
    new MetadataService.DeployOptions();
    new MetadataService.FlowChoice();
    new MetadataService.FieldSet();
    new MetadataService.DescribeMetadataResult();
    new MetadataService.AllOrNoneHeader_element();
    new MetadataService.describeMetadata_element();
    new MetadataService.listMetadata_element();
    new MetadataService.FlowChoiceUserInput();
    new MetadataService.ProfileSearchLayouts();
    new MetadataService.PermissionSetFieldPermissions();
    new MetadataService.PermissionSetCustomMetadataTypeAccess();
    new MetadataService.PermissionSetExternalDataSourceAccess();
    new MetadataService.RunTestSuccess();
    new MetadataService.RetrieveRequest();
    new MetadataService.FlowConnector();
    new MetadataService.deleteMetadataResponse_element();
    new MetadataService.LogInfo();
    new MetadataService.CodeLocation();
    new MetadataService.ListMetadataQuery();
    new MetadataService.PermissionSetApplicationVisibility();
    new MetadataService.CompactLayout();
    new MetadataService.SharedTo();
    new MetadataService.FlowCollectionProcessor();
    new MetadataService.FlowRecordLookup();
    new MetadataService.FlowDynamicChoiceSet();
    new MetadataService.WebLink();
    new MetadataService.Flow();
    new MetadataService.FlowRecordDelete();
    new MetadataService.FlowRecordRollback();
    new MetadataService.FlowSubflowInputAssignment();
    new MetadataService.ArticleTypeTemplate();
    new MetadataService.FlowWaitEvent();
    new MetadataService.AsyncResult();
    new MetadataService.FlowOrchestratedStage();
    new MetadataService.FlowTransformValue();
    new MetadataService.ValueSetValuesDefinition();
    new MetadataService.FlowAssignment();
    new MetadataService.RetrieveMessage();
    new MetadataService.checkRetrieveStatusResponse_element();
    new MetadataService.FlowStageStepExitActionOutputParameter();
    new MetadataService.createMetadataResponse_element();
    new MetadataService.FlowStageStepEntryActionOutputParameter();
    new MetadataService.HistoryRetentionPolicy();
    new MetadataService.Index();
    new MetadataService.FlowFormula();
    new MetadataService.MktDataLakeAttributes();
    new MetadataService.CodeCoverageResult();
    new MetadataService.deploy_element();
    new MetadataService.RecordTypePicklistValue();
    new MetadataService.FlowApexPluginCall();
    new MetadataService.ListView();
    new MetadataService.FlowScreenFieldOutputParameter();
    new MetadataService.DeployResult();
    new MetadataService.FlowCoverageResult();
    new MetadataService.FlowCoverageWarning();
    new MetadataService.retrieveResponse_element();
    new MetadataService.readMetadata_element();
    new MetadataService.FlowActionCallOutputParameter();
    new MetadataService.ValueSet();
    new MetadataService.IndexField();
    new MetadataService.FlowInputValidationRule();
    new MetadataService.FlowStageStepExitActionInputParameter();
    new MetadataService.FlowRecordCreate();
    new MetadataService.updateMetadataResponse_element();
    new MetadataService.upsertMetadataResponse_element();
    new MetadataService.FlowScreenField();
    new MetadataService.PermissionSetRecordTypeVisibility();
    new MetadataService.FlowConstant();
    new MetadataService.cancelDeploy_element();
    new MetadataService.RunTestFailure();
    new MetadataService.createMetadata_element();
    new MetadataService.ValidationRule();
    new MetadataService.DescribeValueTypeResult();
    new MetadataService.describeMetadataResponse_element();
    new MetadataService.PermissionSetCustomPermissions();
    new MetadataService.FlowDataTypeMapping();
    new MetadataService.checkDeployStatus_element();
    new MetadataService.describeValueTypeResponse_element();
    new MetadataService.FlowActionCallInputParameter();
    new MetadataService.FlowTextTemplate();
    new MetadataService.FlowRule();
    new MetadataService.checkDeployStatusResponse_element();
    new MetadataService.FlowRecordUpdate();
    new MetadataService.FlowScreen();
    new MetadataService.PermissionSetApexClassAccess();
    new MetadataService.FileProperties();
    new MetadataService.FlowScreenRuleAction();
    new MetadataService.FlowTransformValueAction();
    new MetadataService.FlowRecordFilter();
    new MetadataService.FlowScheduledPath();
    new MetadataService.deleteMetadata_element();
    new MetadataService.listMetadataResponse_element();
    new MetadataService.FlowSubflowOutputAssignment();
    new MetadataService.FlowActionCall();
    new MetadataService.deployResponse_element();
    new MetadataService.ListViewFilter();
    new MetadataService.describeValueType_element();
    new MetadataService.FlowStageStepAssignee();
    new MetadataService.RecordType();
    new MetadataService.FlowStart();
    new MetadataService.PermissionSetCustomSettingAccess();
    new MetadataService.LookupFilter();
    new MetadataService.PicklistEntry();
    new MetadataService.FlowLoop();
    new MetadataService.CodeCoverageWarning();
    new MetadataService.DebuggingInfo_element();
    new MetadataService.FlowApexPluginCallInputParameter();
    new MetadataService.FlowStageStepOutputParameter();
    new MetadataService.FieldSetItem();
    new MetadataService.Error();
    new MetadataService.FlowStep();
    new MetadataService.FlowInputFieldAssignment();
    new MetadataService.updateMetadata_element();
    new MetadataService.FlowSchedule();
    new MetadataService.renameMetadataResponse_element();
    new MetadataService.CancelDeployResult();
    new MetadataService.CustomField();
    new MetadataService.FlowSubflow();
    new MetadataService.FlowTransform();
    new MetadataService.FlowVariable();
    new MetadataService.BusinessProcess();
    new MetadataService.MetadataPort();
    new MetadataService.ReadSharingReasonResult();
    new MetadataService.readSharingReasonResponse_element();
    new MetadataService.ReadCustomObjectResult();
    new MetadataService.readCustomObjectResponse_element();
    new MetadataService.ReadPicklistValueResult();
    new MetadataService.readPicklistValueResponse_element();
    new MetadataService.ReadFieldSetResult();
    new MetadataService.readFieldSetResponse_element();
    new MetadataService.ReadCompactLayoutResult();
    new MetadataService.readCompactLayoutResponse_element();
    new MetadataService.ReadWebLinkResult();
    new MetadataService.readWebLinkResponse_element();
    new MetadataService.ReadFlowResult();
    new MetadataService.readFlowResponse_element();
    new MetadataService.ReadIndexResult();
    new MetadataService.readIndexResponse_element();
    new MetadataService.ReadListViewResult();
    new MetadataService.readListViewResponse_element();
    new MetadataService.ReadValidationRuleResult();
    new MetadataService.readValidationRuleResponse_element();
    new MetadataService.ReadRecordTypeResult();
    new MetadataService.readRecordTypeResponse_element();
    new MetadataService.ReadCustomFieldResult();
    new MetadataService.readCustomFieldResponse_element();
    new MetadataService.ReadBusinessProcessResult();
    new MetadataService.readBusinessProcessResponse_element();

    Test.stopTest();
   }

  @IsTest
  private static void elfMissingGetRecordsTest() { // elf patch
    Test.startTest();
    new MetadataService.ReadSharingReasonResult().getRecords();
    new MetadataService.ReadCustomObjectResult().getRecords();
    new MetadataService.ReadPicklistValueResult().getRecords();
    new MetadataService.ReadFieldSetResult().getRecords();
    new MetadataService.ReadCompactLayoutResult().getRecords();
    new MetadataService.ReadWebLinkResult().getRecords();
    new MetadataService.ReadFlowResult().getRecords();
    new MetadataService.ReadIndexResult().getRecords();
    new MetadataService.ReadListViewResult().getRecords();
    new MetadataService.ReadValidationRuleResult().getRecords();
    new MetadataService.ReadRecordTypeResult().getRecords();
    new MetadataService.ReadCustomFieldResult().getRecords();
    new MetadataService.ReadBusinessProcessResult().getRecords();

    Test.stopTest();
  }

   @IsTest
   private static void elfMissingGetResultTest() { // elf patch
     Test.startTest();
     new MetadataService.readSharingReasonResponse_element().getResult();
     new MetadataService.readCustomObjectResponse_element().getResult();
     new MetadataService.readPicklistValueResponse_element().getResult();
     new MetadataService.readFieldSetResponse_element().getResult();
     new MetadataService.readCompactLayoutResponse_element().getResult();
     new MetadataService.readWebLinkResponse_element().getResult();
     new MetadataService.readFlowResponse_element().getResult();
     new MetadataService.readIndexResponse_element().getResult();
     new MetadataService.readListViewResponse_element().getResult();
     new MetadataService.readValidationRuleResponse_element().getResult();
     new MetadataService.readRecordTypeResponse_element().getResult();
     new MetadataService.readCustomFieldResponse_element().getResult();
     new MetadataService.readBusinessProcessResponse_element().getResult();

     Test.stopTest();

   }

}
