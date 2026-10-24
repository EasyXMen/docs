类型定义(Type Definitions)
---------------------------
.. 如果没有就不存在该章节，或为None

.. list-table:: 
   :widths: 15 5 20
   :header-rows: 1

   * - Type Name
     - Type
     - Description

   * - Dcm_ProtocolCtrlType
     - struct ProtocolCtrlType
     - Dcm protocol control type.

   * - Dcm_ConfirmationHandleType
     - struct ConfirmationHandleType
     - Dcm confirmation info type.

   * - Dcm_SessionCtrlType
     - struct SessionCtrlType
     - Dcm session control unit.

   * - Dcm_SecurityCtrlType
     - struct SecurityCtrlType
     - Dcm security control unit.

   * - Dcm_StateType
     - enum
     - Dcm State enum.

   * - Dcm_CommStateType
     - enum
     - Dcm ComM State.

   * - Dcm_DiagnosticStateType
     - enum
     - Dcm diagnostic State.

   * - Dcm_ActiveDiagnosticType
     - enum
     - active diagnostic status enum

   * - Dcm_ProgConditionsType
     - struct ProgConditionsType
     - Used in Dcm_SetProgConditions() to allow the integrator to store relevant information prior to jumping to bootloader jump due to ECUReset request.

   * - Dcm_MsgItemType
     - uint8
     - Base type for diagnostic message item.

   * - Dcm_MsgType
     -  Dcm_MsgItemType
     - Base type for diagnostic message (request, positive or negative response)

   * - Dcm_MsgLenType
     - uint32
     - Length of diagnostic message (request, positive or negative response). The maximum length is dependent of the underlying transport protocol/media.

   * - Dcm_MsgAddInfoType
     - struct MsgAddInfoType
     - Additional information on message request.

   * - Dcm_IdContextType
     - uint8
     - This message context identifier can be used to determine the relation between request and response confirmation.

   * - Dcm_MsgContextType
     - struct MsgContextType
     - This data structure contains all information which is necessary to process a diagnostic message from request to response and response confirmation.

   * - Dcm_ExtendedOpStatusType
     - uint8
     - extended operation status enum

   * - Dcm_StatusType
     - enum
     - Base item type to transport status information.

   * - Dcm_CommunicationModeType
     - enum
     - communication mode enum

   * - Dcm_ReturnReadMemoryType
     - enum
     - Return values of Callout Dcm_ReadMemory.

   * - Dcm_ReturnWriteMemoryType
     - enum
     - Return type of callout Dcm_WriteMemory.

   * - Dcm_EcuStartModeType
     - enum
     - Allows the DCM to know if a diagnostic response shall be sent in the case of a jump from bootloader.

   * - Dcm_DsdServiceRequestNotificationConfirmationFncType
     - Std_ReturnType*
     - The function confirms to the app the successful transmission or a transmission error of a diagnostic service.

   * - Dcm_DsdServiceRequestNotificationIndicationFncType
     - Std_ReturnType*
     - The function indicates to the app that a service is about to be executed and allows the application to reject the execution of the service request.

   * - Dcm_DsdServiceRequestNotificationType
     - struct DsdServiceRequestNotificationType
     - service notification callouts

   * - Dcm_ServiceRoleType
     - struct ServiceRoleType
     - authenticationRow type

   * - Dcm_DspSecurityCompareKeyFncType
     - Std_ReturnType*
     - Request to application for asynchronous comparing key.

   * - Dcm_DspSecurityGetSeedFncType
     - Std_ReturnType*
     - Request to application for asynchronous provision of seed value.

   * - Dcm_DspSecurityGetAttemptCounterFncType
     - Std_ReturnType*
     - Read the attempt counter for a specific security level from the application.

   * - Dcm_DspSecuritySetAttemptCounterFncType
     - Std_ReturnType*
     - Set the attempt counter for a specific security level in the application.

   * - Dcm_DspSecurityRowType
     - struct DspSecurityRowType
     - DcmDspSecurityRow configuration.

   * - Dcm_DspSessionRowType
     - struct DspSessionRowType
     - DcmDspSessionRow Configuration.

   * - Dcm_ServcieFncType
     - Std_ReturnType*
     - Function prototype for service entry, named by parameter SidTabFnc.

   * - Dcm_ModeRuleFncType
     - Std_ReturnType*
     - general mode rule function

   * - Dcm_DsdSubServiceType
     - struct DsdSubServiceType
     - DcmDsdSubService Configuration.

   * - Dcm_DsdServiceType
     - struct DsdServiceType
     - DcmDsdService Configuration.

   * - Dcm_DsdServiceTableType
     - struct DsdServiceTableType
     - DcmDsdServiceTable Configuration.

   * - Dcm_DslCallbackDCMRequestServiceFncType
     - Std_ReturnType*
     - This function allows the application to examine the environment conditions and enable/disable further processing of the protocol for StartProtocol and informs the application of the protocol stop for StopProtocol.

   * - Dcm_DslCallbackDCMRequestServiceType
     - struct DslCallbackDCMRequestServiceType
     - CallbackDCMRequestService Configuration.

   * - Dcm_DslProtocolRxType
     - struct DslProtocolRxType
     - DcmDslProtocolRx Configuration.

   * - Dcm_ComCtrlFncType
     - Std_ReturnType*
     - general communication control function

   * - Dcm_DslMainConnectionType
     - struct DslMainConnectionType
     - mainConnection configuration

   * - Dcm_DslProtocolRowType
     - struct DslProtocolRowType
     - This container contains the configuration of one particular diagnostic protocol used in Dcm.

   * - Dcm_DspAuthenticationConnectionType
     - struct DspAuthenticationConnectionType
     - DcmDspAuthenticationConnection Configuration.

   * - Dcm_DspAuthenticationTransmitCertificateType
     - struct DspAuthenticationTransmitCertificateType
     - DcmDspAuthenticationTransmitCertificate Configuration.

   * - Dcm_DspAuthenticationRowType
     - struct DspAuthenticationRowType
     - DcmDspAuthenticationRow Configuration.

   * - Dcm_DspAuthenticationType
     - struct DspAuthenticationType
     - DcmDspAuthentication Configuration.

   * - Dcm_DspClearDTCCheckFncType
     - Std_ReturnType*
     - Callout function for condition check, manufacturer / supplier specific checks on the groupOf DTC, which is requested to clear.

   * - Dcm_DspClearDTCType
     - struct DspClearDTCType
     - DcmDspClearDTC Configuration.

   * - Dcm_DspComControlAllChannelType
     - struct DspComControlAllChannelType
     - DcmDspComControlAllChannel Configuration.

   * - Dcm_DspComControlSpecificChannelType
     - struct DspComControlSpecificChannelType
     - DcmDspComControlSpecificChannel Configuration.

   * - Dcm_DspComControlSubNodeType
     - struct DspComControlSubNodeType
     - DcmDspComControlSubNode Configuration.

   * - Dcm_DspComControlType
     - struct DspComControlType
     - DcmDspComControl Configuration.

   * - Dcm_DspCommonAuthorizationType
     - struct DspCommonAuthorizationType
     - DcmDspCommonAuthorization Configuration.

   * - Dcm_DspControlDTCSettingType
     - struct DspControlDTCSettingType
     - DcmDspControlDTCSetting Configuration.

   * - Dcm_DspDataConditionCheckReadFncType
     - Std_ReturnType*
     - DcmDspDataConditionCheckRead function prototype.

   * - Dcm_DspDataEcuSignalType
     - Std_ReturnType*
     - EcuSignal function prototype.

   * - Dcm_DspDataFreezeCurrentStateFncType
     - Std_ReturnType*
     - DcmDspDataFreezeCurrentState function prototype.

   * - Dcm_DspDataGetScalingInfoFncType
     - Std_ReturnType*
     - DcmDspDataGetScalingInfo function prototype.

   * - Dcm_DspDataReadDataLengthFncType
     - Std_ReturnType*
     - DcmDspDataReadDataLength function prototype.

   * - Dcm_DspDataReadEcuSignalType
     - Std_ReturnType*
     - ReadEcuSignal function prototype.

   * - Dcm_DspDataReadFncType
     - Std_ReturnType*
     - DcmDspDataRead function prototype.

   * - Dcm_DspPidDataReadFncType
     - Std_ReturnType*
     - DcmDspPidDataRead function prototype.

   * - Dcm_DspDataResetToDefaultFncType
     - Std_ReturnType*
     - DcmDspDataResetToDefault function prototype.

   * - Dcm_DspDataReturnControlToEcuFncType
     - Std_ReturnType*
     - DcmDspDataReturnControlToEcu function prototype.

   * - Dcm_DspDataShortTermAdjustmentFncType
     - Std_ReturnType*
     - DcmDspDataShortTermAdjustment function prototype.

   * - Dcm_DspDataWriteFncType
     - Std_ReturnType*
     - DcmDspDataWrite function prototype.

   * - Dcm_DspDataCfgType
     - struct DspDataCfgType
     - DcmDspData Configuration.

   * - Dcm_DspDidSignalType
     - struct DspDidSignalType
     - DcmDspDidSignal Configuration.

   * - Dcm_DspDidReadFncType
     - Std_ReturnType*
     - General didRead function prototype, used when DidUsePort is not DCM_USE_DATA_ELEMENT_SPECIFIC_INTERFACES.

   * - Dcm_DspDidWriteFncType
     - Std_ReturnType*
     - General didWrite function prototype, used when DidUsePort is not DCM_USE_DATA_ELEMENT_SPECIFIC_INTERFACES.

   * - Dcm_DspDidType
     - struct DspDidType
     - DcmDspDid Configuration.

   * - Dcm_DspDidControlType
     - struct DspDidControlType
     - didControl Configuration

   * - Dcm_DspDidReadWriteType
     - struct DspDidReadWriteType
     - DcmDspDidReadWrite Configuration.

   * - Dcm_DspDidInfoType
     - struct DspDidInfoType
     - DcmDspDidInfo Configuration.

   * - Dcm_DspDidRangeIsDidAvailableFncType
     - Std_ReturnType*
     - DcmDspDidRangeIsDidAvailable function prototype.

   * - Dcm_DspDidRangeReadDataLengthFncType
     - Std_ReturnType*
     - DcmDspDidRangeReadDataLength function prototype.

   * - Dcm_DspDidRangeReadDidFncType
     - Std_ReturnType*
     - DcmDspDidRangeReadDid function prototype.

   * - Dcm_DspDidRangeWriteDidFncType
     - Std_ReturnType*
     - DcmDspDidRangeWriteDid function prototype.

   * - Dcm_DspDidRangeType
     - struct DspDidRangeType
     - DcmDspDidRange Configuration.

   * - Dcm_DspEcuResetRowType
     - struct DspEcuResetRowType
     - DcmDspEcuResetRow Configuration.

   * - Dcm_DspMemoryRangeInfoType
     - struct DspMemoryRangeInfoType
     - DcmDspRead/WriteMemoryRangeInfo Configuration.

   * - Dcm_DspMemoryIdInfoType
     - struct DspMemoryIdInfoType
     - DcmDspMemoryIdInfo Configuration.

   * - Dcm_DspMemoryType
     - struct DspMemoryType
     - DcmDspMemory Configuration.

   * - Dcm_DspPidService01Type
     - struct DspPidService01Type
     - DcmDspDidService01 Configuration.

   * - Dcm_DspPidDataType
     - struct DspPidDataType
     - PidData Configuration.

   * - Dcm_DspPidType
     - struct DspPidType
     - DcmDspPid Configuration.

   * - Dcm_RequestControlFncType
     - Std_ReturnType*
     - RequestControl function type.

   * - Dcm_DspRequestControlType
     - struct DspRequestControlType
     - DcmDspRequestControl Configuration.

   * - Dcm_DspRoutineFncType
     - Std_ReturnType*
     - general routine request function type

   * - Dcm_DspRoutineSignalType
     - struct DspRoutineSignalType
     - DcmDspRoutineSignal Configuration.

   * - Dcm_DspRoutineSubType
     - struct DspRoutineSubType
     - DcmDspStart/Stop/RequestResultsRoutine Configuration.

   * - Dcm_DspRoutineType
     - struct DspRoutineType
     - DcmDspRoutine Configuration.

   * - Dcm_DspVehInfoDataReadFncType
     - Std_ReturnType*
     - VehInfoDataRead function type.

   * - Dcm_DspVehInfoDataType
     - struct DspVehInfoDataType
     - vehInfoData Configuration

   * - Dcm_DspVehInfoType
     - struct DspVehInfoType
     - DcmDspVehInfo Configuration.

   * - Dcm_QueuedRequestCtrlType
     - struct QueuedRequestCtrlType
     - QueuedRequest control unit.

   * - Dcm_EndiannessType
     - enum
     - Endianness enum.

   * - Dcm_DspSessionForBootType
     - enum
     - SessionForBoot enum.

   * - Dcm_DcmDsdAddressingFormatType
     - enum
     - service request addressing format

   * - Dcm_DslProtocolTransType
     - enum
     - The transmission type of the protocol.

   * - Dcm_DslProtocolRxAddrType
     - enum
     - The protocolRxAddr enum.

   * - Dcm_DspDataType
     - enum
     - DspDataType Enum.

   * - Dcm_DspDataUsePortType
     - enum
     - DspDataUsePort Enum.

   * - Dcm_DspDidUsePortType
     - enum
     - DidUsePort Enum.

   * - Dcm_DspDidControlMaskType
     - enum
     - controlMask Enum

   * - Dcm_ResponseToEcuResetType
     - enum
     - DcmDspResponseToEcuReset Enum.

   * - Dcm_DspPidServiceType
     - enum
     - DcmDspPidServiceType Enum.

   * - Dcm_ConditionType
     - enum
     - DcmCondition Enum.

   * - Dcm_PendingRequestStateType
     - enum
     - QueuedRequest State enum.

   * - Dcm_AuthenticationCtrlType
     - struct AuthenticationCtrlType
     - authentication ctrl structure type

   * - Dcm_WhiteListType
     - struct WhiteListType
     - whitelist structure type

   * - Dcm_AuthenticateInfoType
     - struct AuthenticateInfoType
     - authentication info structure type

   * - Dcm_KeyMCertInfoType
     - struct KeyMCertInfoType
     - KeyM Certificate info structure type.

   * - Dcm_AuthenticationStateType
     - enum
     - authentication State enum

   * - Dcm_AuthenticateStatusType
     - enum
     - authentication status enum
      
   * - Dcm_SchedulerType
     - struct SchedulerType
     - UDS 0x2A scheduler manager structure type.

   * - Dcm_RoutineStatusType
     - enum
     - Routine current status

   * - Dcm_DDDIDDefineType
     - struct DDDIDDefineType
     - dynamically defined did definition structure

   * - Dcm_DDDIDType
     - struct DDDIDType
     - dynamically defined did structure

   * - Dcm_TransferDataType
     - struct TransferDataType
     - UDS 0x36 transfer data management unit.

   * - Dcm_RoeCtrlType
     - struct RoeCtrlType
     - Dcm roe control unit.

   * - Dcm_DDDIDStatusType
     - enum
     - DDDID status enum.

   * - Dcm_TransferStatusType
     - enum
     - UDS 0x36 transfer status enum.

   * - Dcm_RoeEventType
     - enum
     - UDS roe event status enum.

   * - Dcm_RoeStatusType
     - enum
     - UDS roe current status.

   * - Dcm_RoeEventWindowTimeType
     - enum
     - UDS roe windowtime enum.

   * - Dcm_DidType
     - enum
     - Dcm did type enum.

   * - Dcm_AuthenticateProcessStatusTypes
     - enum
     - authentication process status enum


提供的服务(Services)
---------------------------------------------
Dcm_ComM_NoComModeEntered
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Dcm_ComM_NoComModeEntered(uint8 NetworkId)

This call informs the Dcm module about a ComM mode change to COMM_NO_COMMUNICATION.

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - NetworkId
     - Identifier of the network concerned by the mode change

**Return type**
    void

Dcm_ComM_SilentComModeEntered
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Dcm_ComM_SilentComModeEntered(uint8 NetworkId)

This call informs the Dcm module about a ComM mode change to COMM_SILENT_COMMUNICATION.

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - NetworkId
     - Identifier of the network concerned by the mode change

**Return type**
   void

Dcm_ComM_FullComModeEntered
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Dcm_ComM_FullComModeEntered(uint8 NetworkId)

This call informs the Dcm module about a ComM mode change to COMM_FULL_COMMUNICATION.

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - NetworkId
     - Identifier of the network concerned by the mode change

**Return type**
   void

Dcm_DemTriggerOnDTCStatus
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dcm_DemTriggerOnDTCStatus(uint32 DTC, Dem_UdsStatusByteType DTCStatusOld, Dem_UdsStatusByteType DTCStatusNew)

Triggers on changes of the UDS status byte. Allows to trigger on ROE Event for subservice On DTCStatusChanged.

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - DTC
     - This is the DTC the change trigger is assigned to.
   * - [in]
     - DTCStatusOld
     - DTC status before change
   * - [in]
     - DTCStatusNew
     - DTC status after change

**Return type**
    Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - this value is always returned.

Dcm_Init
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Dcm_Init(const Dcm_ConfigType *ConfigPtr)

Service for basic initialization of DCM module.

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - ConfigPtr
     - Pointer to configuration set in Variant Post-Build.

**Return type**
   void

Dcm_GetVersionInfo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Dcm_GetVersionInfo(Std_VersionInfoType *versionInfo)

Returns the version information of this module.

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [out]
     - versionInfo
     - Pointer to where to store the version information of this module.

**Return type**
   void

Dcm_GetVin
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dcm_GetVin(uint8 *Data)

Function to get the VIN (as defined in SAE J1979-DA)

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [out]
     - Data
     - Pointer to where to store the VIN

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The Data pointer has been filled with valid VIN
   * - E_NOT_OK
     - The default VIN will be used in the DoIP

Dcm_BndMWriteBlockFinish
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Dcm_BndMWriteBlockFinish(BndM_BlockIdType BlockId, BndM_ResultType result)

Called by BndM to indicate that a block write operation has finished.

**Sync/Async**
   Synchronous

**Reentrancy**
   Non Reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - BlockId
     - the requested blockId
   * - [in]
     - result
     - the result of the request

**Return type**
   void

Dcm_SetDeauthenticatedRole
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dcm_SetDeauthenticatedRole(uint16 connectionId, Dcm_AuthenticationRoleType deauthenticatedRole)

Sets a new role used in deauthenticated state for that connection. The set role is valid until the connection switches into authenticated state or the ECU is reset.

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - connectionId
     - Unique connection identifier identifiying the connection for which a deauthenticated roles is set.
   * - [in]
     - deauthenticatedRole
     - New deauthenticated role that is assigned to that connection

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - this value is always returned.

Dcm_GetSecurityLevel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dcm_GetSecurityLevel(Dcm_SecLevelType *SecLevel)

This function provides the active security level value.

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [out]
     - SecLevel
     - Active Security Level value Conversion formula to calculate SecurityLevel out of tester requested SecurityAccessType parameter: SecurityLevel = (SecurityAccessType + 1) / 2 Content of SecurityAccessType is according to "securityAccessType" parameter of SecurityAccess request

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - this value is always returned.

Dcm_GetSesCtrlType
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dcm_GetSesCtrlType(Dcm_SesCtrlType *SesCtrlType)

This function provides the active session control type value.

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [out]
     - SesCtrlType
     - Active Session Control Type value Content is according to "diagnosticSessionType" parameter of DiagnosticSessionControl request

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - this value is always returned.

Dcm_ResetToDefaultSession
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dcm_ResetToDefaultSession(void)

The call to this function allows the application to reset the current session to Default session. Example: Automatic termination of an extended diagnostic session upon exceeding of a speed limit.

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant


**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - this value is always returned.

Dcm_SetActiveDiagnostic
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dcm_SetActiveDiagnostic(boolean active)

Allows to activate and deactivate the call of ComM_DCM_ActiveDiagnostic() function.

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - active
     - If false Dcm shall not call ComM_DCM_ActiveDiagnostic(). If true Dcm will call ComM_DCM_ActiveDiagnostic().

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - this value is always returned.

Dcm_StartOfReception
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    BufReq_ReturnType Dcm_StartOfReception(PduIdType id, const PduInfoType *info, PduLengthType TpSduLength, PduLengthType *bufferSizePtr)

This function is called at the start of receiving an N-SDU. The N-SDU might be fragmented into multiple N-PDUs (FF with one or more following CFs) or might consist of a single N-PDU (SF). If the service is successful and BUFREQ_OK is returned, the service provides the currently available maximum buffer size. This function might be called in interrupt context.

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - id
     - Identification of the I-PDU.
   * - [in]
     - info
     - Pointer to a PduInfoType structure containing the payload data (without protocol information) and payload length of the first frame or single frame of a transport protocol I-PDU reception, and the MetaData related to this PDU. If neither first/single frame data nor MetaData are available, this parameter is set to NULL_PTR.
   * - [in]
     - TpSduLength
     - Total length of the N-SDU to be received.
   * - [out]
     - bufferSizePtr
     - Available receive buffer in the receiving module. This parameter will be used to compute the Block Size (BS) in the transport protocol module.

**Return type**
   BufReq_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - BUFREQ_OK
     - Connection has been accepted. bufferSizePtr indicates the available receive buffer; reception is continued. If no buffer of the requested size is available, a receive buffer size of 0 shall be indicated by bufferSizePtr.
   * - BUFREQ_E_NOT_OK
     - Connection has been rejected; reception is aborted. bufferSizePtr remains unchanged.
   * - BUFREQ_E_OVFL
     - No buffer of the required length can be provided; reception is aborted. bufferSizePtr remains unchanged.

Dcm_CopyRxData
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    BufReq_ReturnType Dcm_CopyRxData(PduIdType id, const PduInfoType *info, PduLengthType *bufferSizePtr)

This function is called to provide the received data of an I-PDU segment (N-PDU) to the upper layer. Each call to this function provides the next part of the I-PDU data. The size of the remaining buffer is written to the position indicated by bufferSizePtr. This function might be called in interrupt context.

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - id
     - Identification of the received I-PDU.
   * - [in]
     - info
     - Provides the source buffer (SduDataPtr) and the number of bytes to be copied (SduLength). An SduLength of 0 can be used to query the current amount of available buffer in the upper layer module. In this case, the SduDataPtr may be a NULL_PTR.
   * - [out]
     - bufferSizePtr
     - Available receive buffer after data has been copied.

**Return type**
   BufReq_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - BUFREQ_OK
     - Data copied successfully
   * - BUFREQ_E_NOT_OK
     - Data was not copied because an error occurred.

Dcm_TpRxIndication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Dcm_TpRxIndication(PduIdType id, Std_ReturnType result)

Called after an I-PDU has been received via the TP API, the result indicates whether the transmission was successful or not. This function might be called in interrupt context.

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - id
     - Identification of the received I-PDU.
   * - [in]
     - result
     - Result of the reception.

**Return type**
   void

Dcm_CopyTxData
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    BufReq_ReturnType Dcm_CopyTxData(PduIdType id, const PduInfoType *info, const RetryInfoType *retry, PduLengthType *availableDataPtr)

This function is called to acquire the transmit data of an I-PDU segment (N-PDU). Each call to this function provides the next part of the I-PDU data. The size of the remaining data is written to the position indicated by availableDataPtr. This function might be called in interrupt context.

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - id
     - Identification of the transmitted I-PDU.
   * - [in]
     - info
     - Provides the destination buffer (SduDataPtr) and the number of bytes to be copied (SduLength). If not enough transmit data is available, no data is copied by the upper layer module and BUFREQ_E_BUSY is returned. The lower layer module may retry the call. An SduLength of 0 can be used to indicate state changes in the retry parameter or to query the current amount of available data in the upper layer module. In this case, the Sdu DataPtr may be a NULL_PTR.
   * - [in]
     - retry
     - currently not being used
   * - [out]
     - availableDataPtr
     - Indicates the remaining number of bytes that are available in the upper layer module's Tx buffer. availableDataPtr can be used by TP modules that support dynamic payload lengths (e.g. FrIsoTp) to determine the size of the following CFs.

**Return type**
   BufReq_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - BUFREQ_OK
     - Data has been copied to the transmit buffer completely as requested.
   * - BUFREQ_E_BUSY
     - Request could not be fulfilled, because the required amount of Tx data is not available. The lower layern module may retry this call later on. No data has been copied.
   * - BUFREQ_E_NOT_OK
     - Data has not been copied. Request failed.

Dcm_TpTxConfirmation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Dcm_TpTxConfirmation(PduIdType id, Std_ReturnType result)

This function is called after the I-PDU has been transmitted on its network, the result indicates whether the transmission was successful or not. This function might be called in interrupt context.

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - id
     - Identification of the transmitted I-PDU.
   * - [in]
     - result
     - Result of the transmission of the I-PDU.

**Return type**
   void

Dcm_TxConfirmation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Dcm_TxConfirmation(PduIdType TxPduId, Std_ReturnType result)

The lower layer communication interface module confirms the transmission of a PDU, or the failure to transmit a PDU. This function might be called in interrupt context.

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - TxPduId
     - ID of the PDU that has been transmitted.
   * - [in]
     - result
     - E_OK : The PDU was transmitted. E_NOT_OK: Transmission of the PDU failed.

**Return type**
   void

Dcm_CsmAsyncJobFinished
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dcm_CsmAsyncJobFinished(uint32 jobId, Crypto_ResultType result)

Can be called from Csm upon finishing an asynchronous job processing. The integrator will configure this name as callback function within the Csm ECUC configuration for asynchronous jobs. Only one such callback is available, the Dcm detects the job that has finished by evaluating the job parameter.

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - jobId
     - JobId provided by the Csm, indicating the job that has finished.
   * - [in]
     - result
     - Return value of the asynchronous job

**Return type**
   Std_ReturnType

Dcm_KeyMAsyncCertificateVerifyFinished
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dcm_KeyMAsyncCertificateVerifyFinished(KeyM_CertificateIdType CertID, KeyM_CertificateStatusType Result)

Can be called from Key upon finishing an asynchronous certificate verification. The integrator will configure this name as callback function within the KeyM ECUC configuration for asynchronous jobs. Only one such callback is available, the Dcm detects the certificate that has finished by evaluating the certId parameter.

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - CertID
     - Certificate identifier that has finished the verification
   * - [in]
     - Result
     - Return value of the asynchronous job

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - this value is always returned

Dcm_SatelliteMainFunction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Dcm_SatelliteMainFunction(void)

Scheduled by SchM, running on different cores to deal with transmission for different controller.

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant


**Return type**
   void




