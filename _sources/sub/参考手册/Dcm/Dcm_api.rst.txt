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
   TRUE

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
   TRUE

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
   TRUE

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
   TRUE

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

DsdInternal_HandleIndication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType DsdInternal_HandleIndication(uint8 protocolId, const Dcm_DsdServiceRequestNotificationType *notification, uint8 notificationNum)

Called by DsdInternal_RxIndication do serviceRequest notification indication.

**Sync/Async**
   TRUE

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
     - protocolId
     - current protocol Id
   * - [in]
     - notification
     - the reuqest notification
   * - [in]
     - notificationNum
     - the number of request notification

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

DsdInternal_CheckServiceCondition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType DsdInternal_CheckServiceCondition(uint16 ConnectionId, uint16 *servIndex, Dcm_NegativeResponseCodeType *errorCode)

Called by DsdInternal_RxIndication to check Service condition.

**Sync/Async**
   TRUE

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
     - ConnectionId
     - current connection Id
   * - [out]
     - servIndex
     - service configuration index
   * - [out]
     - errorCode
     - the nrc to send

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

DsdInternal_CheckSubServiceCondition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType DsdInternal_CheckSubServiceCondition(uint8 protocolId, uint16 servIndex, Dcm_NegativeResponseCodeType *errorCode, uint16 *subServIndex)

Called by DsdInternal_RxIndication to check subService condition.

**Sync/Async**
   TRUE

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
     - protocolId
     - current protocol Id
   * - [in]
     - servIndex
     - the configuration index of service
   * - [out]
     - errorCode
     - the nrc to send
   * - [out]
     - subServIndex
     - the configuration index

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

DsdInternal_SecurityEventReport
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL void DsdInternal_SecurityEventReport(Dcm_NegativeResponseCodeType ErrorCode)

Called by DsdInternal_SendResponse to report IdsM security events.

**Sync/Async**
   TRUE

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
     - ErrorCode
     - the nrc to send

**Return type**
   void

DsdInternal_CheckServiceAuth
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType DsdInternal_CheckServiceAuth(uint16 ConnectionId, const Dcm_DsdServiceType *DcmDsdServicePtr, Dcm_NegativeResponseCodeType *errorCode)

check service authentication, security and session

**Sync/Async**
   TRUE

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
     - ConnectionId
     - the current connection id
   * - [in]
     - DcmDsdServicePtr
     - the service configuration
   * - [out]
     - errorCode
     - the possible errorCode

**Return type**
   Std_ReturnType

DsdInternal_HandleTransmit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL void DsdInternal_HandleTransmit(uint8 ProtocolId, Dcm_NegativeResponseCodeType errorCode)

prepare for actual transmission

**Sync/Async**
   TRUE

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
     - ProtocolId
     - the current protocol id
   * - [in]
     - errorCode
     - the input errorCode

**Return type**
   void

DsdInternal_RxIndication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void DsdInternal_RxIndication(uint8 protocolId)

Called by Dcm_TpRxIndication to check service request validity.

**Sync/Async**
   TRUE

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
     - protocolId
     - current protocol Id

**Return type**
    void

DsdInternal_HandleConfirmation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void DsdInternal_HandleConfirmation(uint8 protocolId, Dcm_ConfirmationStatusType confirmationStatus)

Called by DslInternal_SetStateIdle do serviceRequest notification confirmation.

**Sync/Async**
   TRUE

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
     - protocolId
     - current protocol Id
   * - [in]
     - confirmationStatus
     - curruent confirmation status

**Return type**
   void

DsdInternal_SendResponse
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void DsdInternal_SendResponse(uint8 ProtocolId, Dcm_NegativeResponseCodeType errorCode)

This function sends diagnostic response.

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - 
     - ProtocolId
     - 
   * - [in]
     - errorCode
     - The NRC error code

**Return type**
   void

DsdInternal_CheckService
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType DsdInternal_CheckService(uint8 protocolId, uint16 *servIndex, uint8 *Sid)

Called by DsdInternal_RxIndication to check service validity and output configuration index.

**Sync/Async**
   TRUE

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
     - protocolId
     - current protocol Id
   * - [out]
     - servIndex
     - the configuration index
   * - [in]
     - Sid
     - the requested ServiceId(if have)

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

DsdInternal_CheckSubService
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType DsdInternal_CheckSubService(uint8 protocolId, uint16 servIndex, uint16 *subServIndex, uint8 *SubServiceId)

Called by DsdInternal_RxIndication to check subService validity and output configuration index.

**Sync/Async**
   TRUE

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
     - protocolId
     - current protocol Id
   * - [in]
     - servIndex
     - the configuration index of service
   * - [out]
     - subServIndex
     - the configuration index
   * - [in]
     - SubServiceId
     - the requested subServiceId(if have)

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

DslInternal_CheckProtocolWithSameBuffer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType DslInternal_CheckProtocolWithSameBuffer(const Dcm_DslProtocolRowType *protocolRow)

This function checks whether the protocol shares a buffer with other protocols and those protocols are idle or not.

**Sync/Async**
   TRUE

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
     - protocolRow
     - the input protocolRow

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - all protocols that share the same buffer with the input protocol are idle
   * - E_NOT_OK
     - at least one protocol that share the same buffer with the input protocol is not idle

DslInternal_FindProtocolRowByTxPduId
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType DslInternal_FindProtocolRowByTxPduId(PduIdType Id, uint8 *ProtocolId, uint16 *connectionId)

This function searches for matched protocol and connection Id by txPduId.

**Sync/Async**
   TRUE

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
     - Id
     - Identification of the I-PDU.
   * - 
     - ProtocolId
     - 
   * - [out]
     - connectionId
     - the matched connectionId (under the protocol)

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Succesfully find the matched one
   * - E_NOT_OK
     - Fail to find any mathced one

DslInternal_CheckIdle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL boolean DslInternal_CheckIdle(uint8 protocolId)

This function checks whether all the current State of running protocol except input protocol are idle or not.

**Sync/Async**
   TRUE

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
     - protocolId
     - the input protocolId

**Return type**
   DCM_LOCAL boolean

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - TRUE
     - All protocols are idle
   * - FALSE
     - at least one protocol is not idle

DslInternal_RxCheckParam
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL uint8 DslInternal_RxCheckParam(PduIdType id, const PduInfoType *info, PduLengthType *bufferSizePtr, uint8 apiId)

This function checks common params and initialization status for callbacks.

**Sync/Async**
   TRUE

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
     - bufferSizePtr
     - Available receive buffer in the receiving module. This parameter will be used to compute the Block Size (BS) in the transport protocol module.
   * - [in]
     - apiId
     - The Id of the api

**Return type**
   DCM_LOCAL uint8

DslInternal_CopyTxDataCheckParam
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL uint8 DslInternal_CopyTxDataCheckParam(PduIdType id, const PduInfoType *info, PduLengthType *availableDataPtr)

This function checks params for copyTxData.

**Sync/Async**
   TRUE

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
     - Provides the destination buffer (SduDataPtr) and the number of bytes to be copied (SduLength). If not enough transmit data is available, no data is copied by the upper layer module and BUFREQ_E_BUSY is returned. The lower layer module may retry the call. An SduLength of 0 can be used to indicate state changes in the retry parameter or to query the current amount of available data in the upper layer module. In this case, the Sdu DataPtr may be a NULL_PTR.
   * - [in]
     - availableDataPtr
     - Indicates the remaining number of bytes that are available in the upper layer module's Tx buffer. availableDataPtr can be used by TP modules that support dynamic payload lengths (e.g. FrIsoTp) to determine the size of the following CFs.

**Return type**
   DCM_LOCAL uint8

DslInternal_RxProcessRequest
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL void DslInternal_RxProcessRequest(PduIdType id, uint8 protocolId, uint16 connectionId)

This function do internal process for tpRxIndication.

**Sync/Async**
   TRUE

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
     - protocolId
     - current protocol id
   * - [in]
     - connectionId
     - current connection id

**Return type**
   void

DslInternal_HandleFullComMode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL void DslInternal_HandleFullComMode(uint16 connectionId)

This function do internal process for fullComMode entered.

**Sync/Async**
   TRUE

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
     - current connection id

**Return type**
   void

DslInternal_HandleTxDataCopy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL BufReq_ReturnType DslInternal_HandleTxDataCopy(uint16 connectionId, const PduInfoType *info)

This function do internal process for copyTxData when sduLength > 0.

**Sync/Async**
   TRUE

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
     - current connection id
   * - 
     - info
     - 

**Return type**
   DCM_LOCAL BufReq_ReturnType

DslInternal_HandleStartOfReception
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL BufReq_ReturnType DslInternal_HandleStartOfReception(PduIdType id, uint16 connectionId, PduLengthType TpSduLength, const PduInfoType *info)

This function handle startOfReception when the buffer is enough for storing data.

**Sync/Async**
   TRUE

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
     - input pduId
   * - [in]
     - connectionId
     - current connection id
   * - [in]
     - TpSduLength
     - total request data length
   * - [in]
     - info
     - the input pduInfo

**Return type**
   DCM_LOCAL BufReq_ReturnType

DslInternal_HandleTpTxConfirmation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL void DslInternal_HandleTpTxConfirmation(uint8 protocolId)

This function handle tpTxConfirmation when the result is E_OK and condition check succeeds.

**Sync/Async**
   TRUE

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
     - protocolId
     - current protocol id

**Return type**
   void

DslInternal_DefaultToNonDefault
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType DslInternal_DefaultToNonDefault(uint8 ProtocolId)

This function sets from default session to non-default session.

**Sync/Async**
   TRUE

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
     - ProtocolId
     - current protocol id

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - the switch is succeeds
   * - DCM_E_PENDING
     - the switch is pending

DslInternal_PosRespTxDataCopy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL BufReq_ReturnType DslInternal_PosRespTxDataCopy(uint8 protocolId, const PduInfoType *info)

This handle copyTxData for positive response.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - 
     - protocolId
     - 
   * - [inout]
     - info
     - input pduInfo

**Return type**
   DCM_LOCAL BufReq_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - BUFREQ_OK
     - copy is successful
   * - BUFREQ_E_NOT_OK
     - copy is not successful

DslInternal_NegRespTxDataCopy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL BufReq_ReturnType DslInternal_NegRespTxDataCopy(uint8 protocolId, const PduInfoType *info)

This handle copyTxData for negative response.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - 
     - protocolId
     - 
   * - [inout]
     - info
     - input pduInfo

**Return type**
   DCM_LOCAL BufReq_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - BUFREQ_OK
     - copy is successful
   * - BUFREQ_E_NOT_OK
     - copy is not successful

DslInternal_ProcessCopyRxData
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL BufReq_ReturnType DslInternal_ProcessCopyRxData(PduIdType id, const PduInfoType *info, uint8 protocolId)

This process actual copy of copyRxData.

**Sync/Async**
   TRUE

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
     - input pduId
   * - [in]
     - info
     - input pduInfo
   * - [in]
     - protocolId
     - current protocol id

**Return type**
   DCM_LOCAL BufReq_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - BUFREQ_OK
     - copy is successful
   * - BUFREQ_E_NOT_OK
     - copy is not successful

Dcm_CopyTxDataCheckRoe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL boolean Dcm_CopyTxDataCheckRoe(PduIdType id, uint8 *ProtocolId, uint16 *connectionId)

check copyTxData for Roe protocol

**Sync/Async**
   TRUE

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
     - input pduId
   * - 
     - ProtocolId
     - 
   * - [out]
     - connectionId
     - the matched connection id

**Return type**
   DCM_LOCAL boolean

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - TRUE
     - it is an Roe response
   * - FALSE
     - it is not an Roe response

DslInternal_SessionInit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void DslInternal_SessionInit(void)

initialize the session to default status

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant


**Return type**
   void

DslInternal_SecurityInit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void DslInternal_SecurityInit(void)

initialize the security to default status

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant


**Return type**
   void

DslInternal_ProtocolInit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void DslInternal_ProtocolInit(void)

initialize the protocolCtrl to initial status

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant


**Return type**
   void

DslInternal_SetSecurityLevel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void DslInternal_SetSecurityLevel(Dcm_SecLevelType SecurityLevel)

This function sets the security level.

**Sync/Async**
   TRUE

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
     - SecurityLevel
     - The requested sercurity level

**Return type**
   void

DslInternal_ResetToDefaultSession
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void DslInternal_ResetToDefaultSession(boolean Immediate)

This function resets to default session.

**Sync/Async**
   TRUE

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
     - Immediate
     - whether the request is immediately effective

**Return type**
   void

DslInternal_SetSesCtrlType
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType DslInternal_SetSesCtrlType(uint8 ProtocolId, Dcm_SesCtrlType SesCtrlType)

This function sets the session.

**Sync/Async**
   TRUE

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
     - ProtocolId
     - the current protocolId
   * - [in]
     - SesCtrlType
     - the requested session

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - DCM_E_PENDING
     - Request was pending

DslInternal_FindProtocolRowByRxPduId
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType DslInternal_FindProtocolRowByRxPduId(PduIdType Id, uint8 *ProtocolId, uint16 *connectionId)

This function searches for matched protocol and connection Id by RxPduId.

**Sync/Async**
   TRUE

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
     - Id
     - Identification of the I-PDU.
   * - 
     - ProtocolId
     - 
   * - [out]
     - connectionId
     - the matched connectionId (under the protocol)

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Succesfully find the matched one
   * - E_NOT_OK
     - Fail to find any mathced one

DslInternal_SetDiagnosticState
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void DslInternal_SetDiagnosticState(uint16 ConnectionId, Dcm_DiagnosticStateType diagnosticState)

This function sets the current diagnosticState and notify ComM.

**Sync/Async**
   TRUE

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
     - ConnectionId
     - the current connection id
   * - [in]
     - diagnosticState
     - the current diagnostic State

**Return type**
   void

DslInternal_SetStateIdle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void DslInternal_SetStateIdle(uint8 protocolId, const Dcm_ConfirmationStatusType *confirmationStatus, boolean immediateHandle, boolean reachDsp)

This function sets the protocol State to idle.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant for different protocolId

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - protocolId
     - the current protocol id
   * - [in]
     - confirmationStatus
     - the final confirmation status
   * - [in]
     - immediateHandle
     - whether to handle supplier/manufacturer confirmation immediately or asynchronously
   * - [in]
     - reachDsp
     - whether to call DspInternal_DcmConfirmation

**Return type**
   void

DslInternal_InitChannelQueuedRequestCtrl
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void DslInternal_InitChannelQueuedRequestCtrl(uint8 index)

This function initialize the queued request ctrl status.

**Sync/Async**
   TRUE

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
     - index
     - the requested index of queued request ctrl

**Return type**
   void

DslInternal_StopProtocol
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType DslInternal_StopProtocol(uint8 ProtocolId)

This function stops the target protocol.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant for different protocolId

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - ProtocolId
     - the stopped protocol Id

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

DslInternal_ProcessTransmit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void DslInternal_ProcessTransmit(uint8 ProtocolId)

This function actually sends the data.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant for different protocolId

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - 
     - ProtocolId
     - 

**Return type**
   void

DslInternal_PagedBufferInit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void DslInternal_PagedBufferInit(Dcm_ProtocolCtrlType *protocolCtrlPtr)

This function initialize pagedBuffer vars.

**Sync/Async**
   TRUE

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
     - protocolCtrlPtr
     - the target protocolCtrlPtr

**Return type**
   void

DspInternal_handleDTCRoe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void DspInternal_handleDTCRoe(Dem_UdsStatusByteType DTCStatusOld, Dem_UdsStatusByteType DTCStatusNew)

Called by Dcm_DemTriggerOnDTCStatus to process roeEvent related to DTC.

**Sync/Async**
   TRUE

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
     - DTCStatusOld
     - DTC status before change
   * - [in]
     - DTCStatusNew
     - DTC status after change

**Return type**
   void

DspInternal_DcmConfirmation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void DspInternal_DcmConfirmation(uint8 protocolId, uint16 connectionId)

Called by DslInternal_SetStateIdle to notify Dsp for confirmation.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant for different protocolId

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - protocolId
     - current protocol Id
   * - [in]
     - connectionId
     - current connection Id

**Return type**
    void

DspInternal_handleDTCRoe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void DspInternal_handleDTCRoe(Dem_UdsStatusByteType DTCStatusOld, Dem_UdsStatusByteType DTCStatusNew)

Called by Dcm_DemTriggerOnDTCStatus to process roeEvent related to DTC.

**Sync/Async**
   TRUE

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
     - DTCStatusOld
     - DTC status before change
   * - [in]
     - DTCStatusNew
     - DTC status after change

**Return type**
   void

Dcm_Init
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Dcm_Init(const Dcm_ConfigType *ConfigPtr)

Service for basic initialization of DCM module.

**Sync/Async**
   TRUE

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
   TRUE

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
   TRUE

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
   TRUE

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
   TRUE

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
   TRUE

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
   TRUE

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
   TRUE

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
   TRUE

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
   TRUE

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
   TRUE

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
   TRUE

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
   TRUE

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
   TRUE

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
   TRUE

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
   TRUE

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
   TRUE

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
   TRUE

**Reentrancy**
   Reentrant


**Return type**
   void

DcmInternal_CheckP2Timer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL void DcmInternal_CheckP2Timer(void)

called to check P2Timer

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant


**Return type**
   void

DcmInternal_CheckP4Timer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL void DcmInternal_CheckP4Timer(void)

called to check P4Timer

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant


**Return type**
   void

DslInternal_ProcessPreemption
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType DslInternal_ProcessPreemption(uint8 curProtocolId, uint8 targetProtocolId)

This function process protocol preemption.

**Sync/Async**
   TRUE

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
     - curProtocolId
     - the current running protocol Id
   * - [in]
     - targetProtocolId
     - the preempted protocol id

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

DcmInternal_ProcessQueuedRequest
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL void DcmInternal_ProcessQueuedRequest(uint8 protocolId)

This function process queueud request.

**Sync/Async**
   TRUE

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
     - protocolId
     - the input protocol Id

**Return type**
   void

DcmInternal_DispatchService
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL void DcmInternal_DispatchService(uint8 protocolId)

This function calls service interpreter.

**Sync/Async**
   TRUE

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
     - protocolId
     - the input protocol Id

**Return type**
   void

DcmInternal_HandlePreemption
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType DcmInternal_HandlePreemption(uint8 protocolId)

This function handles preemption.

**Sync/Async**
   TRUE

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
     - protocolId
     - the input protocol Id

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

DcmInternal_HandleRequestCallback
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType DcmInternal_HandleRequestCallback(uint8 protocolId)

This function handles request callbacks.

**Sync/Async**
   TRUE

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
     - protocolId
     - the input protocol Id

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

DcmInternal_HandleConfirmation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL void DcmInternal_HandleConfirmation(uint8 protocolId, const Dcm_DsdServiceRequestNotificationType *notification, uint8 notificationNum)

This function handles manufacturer/supplier notification confirmation.

**Sync/Async**
   TRUE

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
     - protocolId
     - the input protocol Id
   * - [in]
     - notification
     - the notification container
   * - [in]
     - notificationNum
     - the number of notification container

**Return type**
   void

DcmInternal_HandleServiceReturn
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL void DcmInternal_HandleServiceReturn(Std_ReturnType result, uint8 protocolId, Dcm_NegativeResponseCodeType errorCode)

This function deal with service function return value.

**Sync/Async**
   TRUE

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
     - result
     - the service result
   * - [in]
     - protocolId
     - the current protocol id
   * - [in]
     - errorCode
     - nrc returned by service

**Return type**
   void

DcmInternal_PrepareRxIndication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType DcmInternal_PrepareRxIndication(uint8 protocolId)

This function setup pre-conditions for rxIndication.

**Sync/Async**
   TRUE

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
     - protocolId
     - the current protocol id

**Return type**
   Std_ReturnType

DcmInternal_Memcpy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void DcmInternal_Memcpy(uint8 *dest, const uint8 *src, uint32 size)

Dcm internal memory copy function.

**Sync/Async**
   TRUE

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
     - dest
     - the output data
   * - [in]
     - src
     - the input data
   * - [in]
     - size
     - the input data size

**Return type**
   void

DcmInternal_Memset
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void DcmInternal_Memset(uint8 *dest, uint8 data, uint32 size)

Dcm internal memory set function.

**Sync/Async**
   TRUE

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
     - dest
     - the output data
   * - [in]
     - data
     - the input data
   * - [in]
     - size
     - date size to set

**Return type**
   void

DcmInternal_ProcessRequest
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void DcmInternal_ProcessRequest(void)

called by Dcm_MainFunction to process pending requests

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant


**Return type**
   void

DcmInternal_ProgCtrlInit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void DcmInternal_ProgCtrlInit(void)

called to initialize programing condition

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant


**Return type**
   void

DcmInternal_GetMetaDataSATA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void DcmInternal_GetMetaDataSATA(uint8 protocolId, uint16 *sourceAddress, uint16 *targetAddress)

get the SATA accorgding to protocolId

**Sync/Async**
   TRUE

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
     - protocolId
     - the input protocolId
   * - [out]
     - sourceAddress
     - the current sourceAddress
   * - [out]
     - targetAddress
     - the current targetAddress

**Return type**
   void

DcmInternal_DecreaseTimer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    boolean DcmInternal_DecreaseTimer(uint32 *timer)

deals with timer to decrease counter

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant for different timer

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - timer
     - the input timer

**Return type**
   boolean

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - TRUE
     - timeout occurs
   * - FALSE
     - timeout does not occur

DcmInternal_CheckTimer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void DcmInternal_CheckTimer(void)

called by Dcm_MainFunction to check timers

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant


**Return type**
   void

DcmInternal_CancelJobs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType DcmInternal_CancelJobs(uint8 ProtocolId)

called to cancel jobs for the input protocol

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant for different protocolId

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - ProtocolId
     - the input protocolId

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

DcmInternal_FindSessionIndex
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType DcmInternal_FindSessionIndex(Dcm_SesCtrlType session, uint8 *sessionIndex)

called to find configured session Index

**Sync/Async**
   TRUE

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
     - session
     - the input sessionId
   * - [out]
     - sessionIndex
     - the configuration index

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

DcmInternal_FindSecurityIndex
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void DcmInternal_FindSecurityIndex(Dcm_SecLevelType security, uint8 *securityIndex)

called to find configured security Index

**Sync/Async**
   TRUE

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
     - security
     - input security level
   * - [out]
     - securityIndex
     - configuration index

**Return type**
   void

DcmInternal_SetProgConditions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType DcmInternal_SetProgConditions(Dcm_OpStatusType OpStatus)

called to set the programing condition

**Sync/Async**
   TRUE

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
     - OpStatus
     - Indicates the current operation status

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

DcmInternal_TransformArray_u16
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void DcmInternal_TransformArray_u16(uint8 *dest, uint16 src, Dcm_EndiannessType endianness)

called to transform uint16 data to uint8_N

**Sync/Async**
   TRUE

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
     - dest
     - the dest buffer
   * - [in]
     - src
     - the input data
   * - [in]
     - endianness
     - the configured endianness

**Return type**
   void

DcmInternal_TransformArray_u24
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void DcmInternal_TransformArray_u24(uint8 *dest, uint32 src, Dcm_EndiannessType endianness)

called to transform uint24 data to uint8_N

**Sync/Async**
   TRUE

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
     - dest
     - the dest buffer
   * - [in]
     - src
     - the input data
   * - [in]
     - endianness
     - the configured endianness

**Return type**
   void

DcmInternal_TransformArray_u32
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void DcmInternal_TransformArray_u32(uint8 *dest, uint32 src, Dcm_EndiannessType endianness)

called to transform uint32 data to uint8_N

**Sync/Async**
   TRUE

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
     - dest
     - the dest buffer
   * - [in]
     - src
     - the input data
   * - [in]
     - endianness
     - the configured endianness

**Return type**
   void

DcmInternal_TransformArray_u64
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void DcmInternal_TransformArray_u64(uint8 *dest, uint64 src, Dcm_EndiannessType endianness)

called to transform uint64 data to uint8_N

**Sync/Async**
   TRUE

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
     - dest
     - the dest buffer
   * - [in]
     - src
     - the input data
   * - [in]
     - endianness
     - the configured endianness

**Return type**
   void

DcmInternal_ProcessRxIndication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void DcmInternal_ProcessRxIndication(void)

called to asynchronously deal with rxIndication

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant


**Return type**
   void

DcmInternal_ProcessTxConfirmation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void DcmInternal_ProcessTxConfirmation(void)

called to asynchronously deal with txConfirmation

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant


**Return type**
   void

DcmInternal_SetActiveDiagnostic
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void DcmInternal_SetActiveDiagnostic(boolean active)

Allows to notify ComM the current DiagnosticState for all connections.

**Sync/Async**
   TRUE

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
     - notify ComM the active or inactive diagnosticState

**Return type**
   void

Dcm_OBD0x02_ReadPid
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_OBD0x02_ReadPid(Dcm_MsgContextType *pMsgContext)

Called by Dcm_OBD0x02 to read pid.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

Dcm_OBD0x02_ReadPidData
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_OBD0x02_ReadPidData(Dcm_MsgContextType *pMsgContext, uint8 pid, uint8 *offset)

read pid data

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [in]
     - pid
     - The requested pid
   * - [inout]
     - offset
     - Current offset

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

Dcm_OBD0x09_FindVehInfo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_OBD0x09_FindVehInfo(uint8 infoType, uint8 *vehInfoIndex)

Called by Dcm_OBD0x09 to find vehInfo index.

**Sync/Async**
   TRUE

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
     - infoType
     - input infoType
   * - [out]
     - vehInfoIndex
     - the configured vehInfo index

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

Dcm_OBD0x01_ReadAvailabilityPid
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_OBD0x01_ReadAvailabilityPid(uint8 Pid, uint8 *mixPid, uint8 availPidIndex, Dcm_MsgLenType *BufSize, uint8 *DestBuffer)

read availability Pid

**Sync/Async**
   TRUE

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
     - Pid
     - input pid
   * - [inout]
     - mixPid
     - Start as 0 for OBD request or NULL_PTR for UDS request, bit 1 is set for availability Id, bit 2 is set for non-availability ones.
   * - [in]
     - availPidIndex
     - the index of availability pid
   * - [inout]
     - BufSize
     - When the function is called this parameter contains the maximum number of data bytes that can be written to the buffer. The function returns the actual number of written data bytes in this parameter.
   * - [out]
     - DestBuffer
     - The output data

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

Dcm_OBD0x01_ReadPidData
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_OBD0x01_ReadPidData(uint8 pidIndex, uint8 *mixPid, Dcm_MsgLenType *BufSize, uint8 *DestBuffer)

read Pid Data

**Sync/Async**
   TRUE

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
     - pidIndex
     - input pid configuration index
   * - [inout]
     - mixPid
     - Start as 0 for OBD request or NULL_PTR for UDS request, bit 1 is set for availability Id, bit 2 is set for non-availability ones.
   * - [inout]
     - BufSize
     - When the function is called this parameter contains the maximum number of data bytes that can be written to the buffer. The function returns the actual number of written data bytes in this parameter.
   * - [out]
     - DestBuffer
     - The output data

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

Dcm_OBD0x01_ProcessPidData
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_OBD0x01_ProcessPidData(const Dcm_DspPidType *DcmDspPidPtr, Dcm_MsgLenType *BufSize, uint8 *DestBuffer)

process Pid Data

**Sync/Async**
   TRUE

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
     - DcmDspPidPtr
     - input pid configuration
   * - [inout]
     - BufSize
     - When the function is called this parameter contains the maximum number of data bytes that can be written to the buffer. The function returns the actual number of written data bytes in this parameter.
   * - [out]
     - DestBuffer
     - The output data

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

Dcm_OBD0x06_ReadAvailabilityMid
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_OBD0x06_ReadAvailabilityMid(uint8 mid, uint8 *mixMid, Dcm_MsgLenType *BufSize, uint8 *DestBuffer)

read availability Mid

**Sync/Async**
   TRUE

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
     - mid
     - input mid
   * - [inout]
     - mixMid
     - Start as 0 for OBD request or NULL_PTR for UDS request, bit 1 is set for availability Id, bit 2 is set for non-availability ones.
   * - [inout]
     - BufSize
     - When the function is called this parameter contains the maximum number of data bytes that can be written to the buffer. The function returns the actual number of written data bytes in this parameter.
   * - [out]
     - DestBuffer
     - The output data

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

Dcm_OBD0x06_ReadMidData
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_OBD0x06_ReadMidData(uint8 mid, uint8 *mixMid, uint8 numberOfTIDs, Dcm_MsgLenType *BufSize, uint8 *DestBuffer)

read Mid Data

**Sync/Async**
   TRUE

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
     - mid
     - input mid
   * - [inout]
     - mixMid
     - Start as 0 for OBD request or NULL_PTR for UDS request, bit 1 is set for availability Id, bit 2 is set for non-availability ones.
   * - [in]
     - numberOfTIDs
     - number of TIDs
   * - [inout]
     - BufSize
     - When the function is called this parameter contains the maximum number of data bytes that can be written to the buffer. The function returns the actual number of written data bytes in this parameter.
   * - [out]
     - DestBuffer
     - The output data

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

Dcm_OBD0x06_ProcessMidData
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_OBD0x06_ProcessMidData(uint8 mid, uint8 numberOfTIDs, Dcm_MsgLenType *BufSize, uint8 *DestBuffer)

process Mid Data

**Sync/Async**
   TRUE

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
     - mid
     - input mid
   * - [in]
     - numberOfTIDs
     - number of TIDs
   * - [inout]
     - BufSize
     - When the function is called this parameter contains the maximum number of data bytes that can be written to the buffer. The function returns the actual number of written data bytes in this parameter.
   * - [out]
     - DestBuffer
     - The output data

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

Dcm_OBD0x08_ReadAvailabilityTid
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_OBD0x08_ReadAvailabilityTid(uint8 tid, uint8 *MixTid, uint8 availTidIndex, Dcm_MsgLenType *BufSize, uint8 *DestBuffer)

read availability Tid

**Sync/Async**
   TRUE

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
     - tid
     - input tid
   * - 
     - MixTid
     - 
   * - [in]
     - availTidIndex
     - the index of availability tid
   * - [inout]
     - BufSize
     - When the function is called this parameter contains the maximum number of data bytes that can be written to the buffer. The function returns the actual number of written data bytes in this parameter.
   * - [out]
     - DestBuffer
     - The output data

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

Dcm_OBD0x08_ReadTidData
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_OBD0x08_ReadTidData(uint8 tidIndex, uint8 *MixTid, Dcm_MsgLenType *BufSize, uint8 *DestBuffer, uint8 *InBuffer, Dcm_MsgLenType InBufferSize, Dcm_NegativeResponseCodeType *ErrorCode)

read Tid Data

**Sync/Async**
   TRUE

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
     - tidIndex
     - input tid configuration index
   * - 
     - MixTid
     - 
   * - [inout]
     - BufSize
     - When the function is called this parameter contains the maximum number of data bytes that can be written to the buffer. The function returns the actual number of written data bytes in this parameter.
   * - [out]
     - DestBuffer
     - The output data
   * - [in]
     - InBuffer
     - the input data
   * - [in]
     - InBufferSize
     - the size of input data
   * - [out]
     - ErrorCode
     - nrc to send

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

Dcm_OBD0x09_ReadAvailabilityVehInfo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_OBD0x09_ReadAvailabilityVehInfo(uint8 infoType, uint8 availInfoTypeIndex, uint8 *MixInfoType, Dcm_MsgLenType *BufSize, uint8 *DestBuffer)

read availability vehInfo

**Sync/Async**
   TRUE

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
     - infoType
     - input infoType
   * - [in]
     - availInfoTypeIndex
     - input availability infoType index
   * - [inout]
     - MixInfoType
     - Start as 0 for OBD request or NULL_PTR for UDS request, bit 1 is set for availability Id, bit 2 is set for non-availability ones.
   * - [inout]
     - BufSize
     - When the function is called this parameter contains the maximum number of data bytes that can be written to the buffer. The function returns the actual number of written data bytes in this parameter.
   * - [out]
     - DestBuffer
     - The output data

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

Dcm_OBD0x09_ReadVehInfoData
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_OBD0x09_ReadVehInfoData(Dcm_ExtendedOpStatusType OpStatus, uint8 vehInfoIndex, uint8 *MixInfoType, Dcm_MsgLenType *BufSize, uint8 *DestBuffer, Dcm_NegativeResponseCodeType *ErrorCode)

read vehInfo Data

**Sync/Async**
   TRUE

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
     - OpStatus
     - current operation status
   * - [in]
     - vehInfoIndex
     - input vehInfo index
   * - [inout]
     - MixInfoType
     - Start as 0 for OBD request or NULL_PTR for UDS request, bit 1 is set for availability Id, bit 2 is set for non-availability ones.
   * - [inout]
     - BufSize
     - When the function is called this parameter contains the maximum number of data bytes that can be written to the buffer. The function returns the actual number of written data bytes in this parameter.
   * - [out]
     - DestBuffer
     - The output data
   * - [out]
     - ErrorCode
     - nrc to send

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful
   * - DCM_E_PENDING
     - Request was pending

Dcm_OBD0x09_ProcessVehInfoData
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_OBD0x09_ProcessVehInfoData(Dcm_ExtendedOpStatusType OpStatus, const Dcm_DspVehInfoType *vehInfo, uint8 *MixInfoType, Dcm_MsgLenType *BufSize, uint8 *DestBuffer, Dcm_NegativeResponseCodeType *ErrorCode)

process vehInfo Data

**Sync/Async**
   TRUE

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
     - OpStatus
     - current operation status
   * - [in]
     - vehInfo
     - input vehInfo configuration
   * - [inout]
     - MixInfoType
     - Start as 0 for OBD request or NULL_PTR for UDS request, bit 1 is set for availability Id, bit 2 is set for non-availability ones.
   * - [inout]
     - BufSize
     - When the function is called this parameter contains the maximum number of data bytes that can be written to the buffer. The function returns the actual number of written data bytes in this parameter.
   * - [out]
     - DestBuffer
     - The output data
   * - [out]
     - ErrorCode
     - nrc to send

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful
   * - DCM_E_PENDING
     - Request was pending

Dcm_OBD0x08_ReadTid
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dcm_OBD0x08_ReadTid(uint8 tid, uint8 *InBuffer, Dcm_MsgLenType InBufferSize, uint8 *DestBuffer, Dcm_MsgLenType *BufSize, Dcm_NegativeResponseCodeType *ErrorCode)

Called by OBD 0x08 and UDS 0x31 to read the tidData.

**Sync/Async**
   TRUE

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
     - tid
     - Target TID
   * - [in]
     - InBuffer
     - the input data
   * - [in]
     - InBufferSize
     - the size of input data
   * - [out]
     - DestBuffer
     - address to output Pid data
   * - [inout]
     - BufSize
     - When the function is called this parameter contains the maximum number of data bytes that can be written to the buffer. The function returns the actual number of written data bytes in this parameter.
   * - 
     - ErrorCode
     - 

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was unsuccessful

Dcm_OBD0x01
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dcm_OBD0x01(Dcm_ExtendedOpStatusType OpStatus, Dcm_MsgContextType *pMsgContext, Dcm_NegativeResponseCodeType *ErrorCode)

The service interpreter for OBD 0x01.

**Sync/Async**
   Depending on Application

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
     - OpStatus
     - Indicates the current operation status
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful
   * - DCM_E_PENDING
     - Request is not yet finished
   * - DCM_E_FORCE_RCRRP
     - Application requests the transmission of a response Response Pending (NRC 0x78)

Dcm_OBD0x01_ReadPid
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dcm_OBD0x01_ReadPid(Dcm_ExtendedOpStatusType OpStatus, uint8 Pid, uint8 *DestBuffer, Dcm_MsgLenType *BufSize, uint8 *mixPid)

Called by OBD 0x01 and UDS 0x22 to read the PidData.

**Sync/Async**
   Depending on Application

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
     - OpStatus
     - Indicates the current operation status
   * - [in]
     - Pid
     - Target PID
   * - [out]
     - DestBuffer
     - address to output Pid data
   * - [inout]
     - BufSize
     - When the function is called this parameter contains the maximum number of data bytes that can be written to the buffer. The function returns the actual number of written data bytes in this parameter.
   * - [inout]
     - mixPid
     - Start as 0 for OBD request or NULL_PTR for UDS request, bit 1 is set for availability Id, bit 2 is set for non-availability ones.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - DCM_E_PENDING
     - Request is not yet finished
   * - E_NOT_OK
     - Request was unsuccessful

Dcm_OBD0x02
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dcm_OBD0x02(Dcm_ExtendedOpStatusType OpStatus, Dcm_MsgContextType *pMsgContext, Dcm_NegativeResponseCodeType *ErrorCode)

The service interpreter for OBD 0x02.

**Sync/Async**
   TRUE

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
     - OpStatus
     - Indicates the current operation status
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

Dcm_OBD0x03
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dcm_OBD0x03(Dcm_ExtendedOpStatusType OpStatus, Dcm_MsgContextType *pMsgContext, Dcm_NegativeResponseCodeType *ErrorCode)

The service interpreter for OBD 0x02.

**Sync/Async**
   TRUE

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
     - OpStatus
     - Indicates the current operation status
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

Dcm_OBD0x04
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dcm_OBD0x04(Dcm_ExtendedOpStatusType OpStatus, Dcm_MsgContextType *pMsgContext, Dcm_NegativeResponseCodeType *ErrorCode)

The service interpreter for OBD 0x04.

**Sync/Async**
   Depending on Application

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
     - OpStatus
     - Indicates the current operation status
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful
   * - DCM_E_PENDING
     - Request is not yet finished

Dcm_OBD0x06
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dcm_OBD0x06(Dcm_ExtendedOpStatusType OpStatus, Dcm_MsgContextType *pMsgContext, Dcm_NegativeResponseCodeType *ErrorCode)

The service interpreter for OBD 0x06.

**Sync/Async**
   TRUE

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
     - OpStatus
     - Indicates the current operation status
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

Dcm_OBD0x06_ReadMid
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dcm_OBD0x06_ReadMid(uint8 mid, uint8 *DestBuffer, Dcm_MsgLenType *BufSize, uint8 *mixMid)

Called by OBD 0x06 and UDS 0x22 to read the midData.

**Sync/Async**
   TRUE

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
     - mid
     - Target MID
   * - [out]
     - DestBuffer
     - address to output Pid data
   * - [inout]
     - BufSize
     - When the function is called this parameter contains the maximum number of data bytes that can be written to the buffer. The function returns the actual number of written data bytes in this parameter.
   * - [inout]
     - mixMid
     - Start as 0 for OBD request or NULL_PTR for UDS request, bit 1 is set for availability Id, bit 2 is set for non-availability ones.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was unsuccessful

Dcm_OBD0x07
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dcm_OBD0x07(Dcm_ExtendedOpStatusType OpStatus, Dcm_MsgContextType *pMsgContext, Dcm_NegativeResponseCodeType *ErrorCode)

The service interpreter for OBD 0x07.

**Sync/Async**
   Depending on Application

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
     - OpStatus
     - Indicates the current operation status
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful
   * - DCM_E_PENDING
     - Request is not yet finished

Dcm_OBD0x08
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dcm_OBD0x08(Dcm_ExtendedOpStatusType OpStatus, Dcm_MsgContextType *pMsgContext, Dcm_NegativeResponseCodeType *ErrorCode)

The service interpreter for OBD 0x08.

**Sync/Async**
   TRUE

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
     - OpStatus
     - Indicates the current operation status
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

Dcm_OBD0x08_ReadTid
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dcm_OBD0x08_ReadTid(uint8 tid, uint8 *InBuffer, Dcm_MsgLenType InBufferSize, uint8 *DestBuffer, Dcm_MsgLenType *BufSize, Dcm_NegativeResponseCodeType *ErrorCode)

Called by OBD 0x08 and UDS 0x31 to read the tidData.

**Sync/Async**
   TRUE

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
     - tid
     - Target TID
   * - [in]
     - InBuffer
     - the input data
   * - [in]
     - InBufferSize
     - the size of input data
   * - [out]
     - DestBuffer
     - address to output Pid data
   * - [inout]
     - BufSize
     - When the function is called this parameter contains the maximum number of data bytes that can be written to the buffer. The function returns the actual number of written data bytes in this parameter.
   * - 
     - ErrorCode
     - 

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was unsuccessful

Dcm_OBD0x08_FindTid
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dcm_OBD0x08_FindTid(uint8 tid, uint8 *tidIndex)

Called by OBD 0x08 and UDS 0x31 to find the configured tid index.

**Sync/Async**
   TRUE

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
     - tid
     - Target TID
   * - [out]
     - tidIndex
     - the configured tid index

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was unsuccessful

Dcm_OBD0x09
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dcm_OBD0x09(Dcm_ExtendedOpStatusType OpStatus, Dcm_MsgContextType *pMsgContext, Dcm_NegativeResponseCodeType *ErrorCode)

The service interpreter for OBD 0x09.

**Sync/Async**
   Depending on Application

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
     - OpStatus
     - Indicates the current operation status
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful
   * - DCM_E_PENDING
     - Request is not yet finished

Dcm_OBD0x09_ReadVehInfo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dcm_OBD0x09_ReadVehInfo(Dcm_ExtendedOpStatusType OpStatus, uint8 infoType, uint8 *DestBuffer, Dcm_MsgLenType *BufSize, uint8 *MixInfoType, Dcm_NegativeResponseCodeType *ErrorCode)

Called by OBD 0x09 and UDS 0x22 to read the vehInfo data.

**Sync/Async**
   Depending on Application

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
     - OpStatus
     - Indicates the current operation status
   * - [in]
     - infoType
     - Target infoType
   * - [out]
     - DestBuffer
     - address to output Pid data
   * - [inout]
     - BufSize
     - When the function is called this parameter contains the maximum number of data bytes that can be written to the buffer. The function returns the actual number of written data bytes in this parameter.
   * - [inout]
     - MixInfoType
     - Start as 0 for OBD request or NULL_PTR for UDS request, bit 1 is set for availability Id, bit 2 is set for non-availability ones.
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was unsuccessful
   * - DCM_E_PENDING
     - Request is not yet finished

Dcm_OBD0x0A
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dcm_OBD0x0A(Dcm_ExtendedOpStatusType OpStatus, Dcm_MsgContextType *pMsgContext, Dcm_NegativeResponseCodeType *ErrorCode)

The service interpreter for OBD 0x0A.

**Sync/Async**
   Depending on Application

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
     - OpStatus
     - Indicates the current operation status
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful
   * - DCM_E_PENDING
     - Request is not yet finished

Dcm_OBD_GetFilteredDTC
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dcm_OBD_GetFilteredDTC(uint8 ClientId, uint8 DTCStatusMask, Dem_DTCOriginType DTCOrigin, uint8 *DestBuffer, uint16 *NumberOfFilteredDTC)

Called by OBD 0x03, 0x07, 0x0A to get filtered DTC.

**Sync/Async**
   Depending on Application

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
     - ClientId
     - Dem ClientId
   * - [in]
     - DTCStatusMask
     - Status-byte mask for DTC status-byte filtering
   * - [in]
     - DTCOrigin
     - used to select the source memory the DTCs shall be read from
   * - [out]
     - DestBuffer
     - address to output DTC
   * - [out]
     - NumberOfFilteredDTC
     - the number of output DTC

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was unsuccessful
   * - DCM_E_PENDING
     - Request is not yet finished

Dcm_OBD_FindPid
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dcm_OBD_FindPid(uint8 Pid, uint8 ServiceId, uint8 *PidIndex)

Called by OBD 0x01, 0x02 to find the pid in the configuration.

**Sync/Async**
   TRUE

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
     - Pid
     - Target Pid
   * - [in]
     - ServiceId
     - Actual OBD service ID
   * - [out]
     - PidIndex
     - Pid index in the configuration

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Pid index found
   * - E_NOT_OK
     - Pid is not configured

Dcm_OBD_isAvailability
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    boolean Dcm_OBD_isAvailability(uint8 Id, uint8 *AvailIdIndex)

Called by OBD 0x01, 0x02, 0x06, 0x08, 0x09 to check is this Id an availabilityId and find which availableIdIndex it belongs to.

**Sync/Async**
   TRUE

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
     - Id
     - OBD ID (pid/mid/testId)
   * - [out]
     - AvailIdIndex
     - the availableIndex this id belongs to (if it is an availability id)

**Return type**
   boolean

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - TRUE
     - it is an availability Id, and availIdIndex is found
   * - FALSE
     - it is not an availability Id

Dcm_UDS0x10_HandleForBoot
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x10_HandleForBoot(uint8 protocolId, Dcm_ExtendedOpStatusType OpStatus, uint8 session, Dcm_DspSessionForBootType sessionForBoot, Dcm_NegativeResponseCodeType *ErrorCode)

handle session change related to boot

**Sync/Async**
   Depending on Session Type and current session level

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
     - protocolId
     - the current protocol Id
   * - [in]
     - OpStatus
     - Indicates the current operation status
   * - [in]
     - session
     - the requested session
   * - [in]
     - sessionForBoot
     - the configuration of session related to boot
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was unsuccessful
   * - DCM_E_PENDING
     - Request is not yet finished
   * - DCM_E_FORCE_RCRRP
     - Application request the transmission of a response Response Pending (NRC 0x78)

Dcm_UDS0x10_ProcessSetProg
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x10_ProcessSetProg(uint8 protocolId, Dcm_ExtendedOpStatusType OpStatus, uint8 session, Dcm_DspSessionForBootType sessionForBoot, Dcm_NegativeResponseCodeType *ErrorCode)

process setProgCondition

**Sync/Async**
   Depending on Session Type and current session level

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
     - protocolId
     - the current protocol Id
   * - [in]
     - OpStatus
     - Indicates the current operation status
   * - [in]
     - session
     - the requested session
   * - [in]
     - sessionForBoot
     - the configuration of session related to boot
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was unsuccessful
   * - DCM_E_PENDING
     - Request is not yet finished
   * - DCM_E_FORCE_RCRRP
     - Application request the transmission of a response Response Pending (NRC 0x78)

Dcm_UDS0x10_CheckTimer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Dcm_UDS0x10_CheckTimer(void)

Called by Dcm_MainFunction/DcmInternal_CheckTimer to deal with session timer.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant


**Return type**
   void

Dcm_UDS0x10_CheckSession
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dcm_UDS0x10_CheckSession(const Dcm_SesCtrlType *session, uint8 sessionNum, Dcm_NegativeResponseCodeType *ErrorCode)

Called by DsdInternal_RxIndication to check general service/subService session and most of th UDS services to check did, rid, memory, etc. session.

**Sync/Async**
   TRUE

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
     - session
     - the required session
   * - [in]
     - sessionNum
     - the required session num
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

Dcm_UDS0x10_SessionChange
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Dcm_UDS0x10_SessionChange(void)

Called by Dcm_TpTxConfirmation for 0x10 service postivie response confirmation and ResetToDefaultSession to change the session.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant


**Return type**
   void

DcmInternal_FindResetIndex
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL void DcmInternal_FindResetIndex(uint8 subFunction, uint8 *resetIndex)

Called by UDS 0x11 to find the configured DcmReset index for the requested subfunction, this function is guaranteed to be successful as there will be configuration validation rules.

**Sync/Async**
   TRUE

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
     - subFunction
     - the requested subfunction
   * - [out]
     - resetIndex
     - the requested subfunction's reset configuration Index

**Return type**
   void

Dcm_UDS0x14_PrepareClear
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x14_PrepareClear(Dcm_ExtendedOpStatusType OpStatus, uint8 clientId, uint8 *reqData, Dcm_NegativeResponseCodeType *ErrorCode)

prepare clear DTC by select and check clear conditions

**Sync/Async**
   Depending on Dem

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
     - OpStatus
     - Indicates the current operation status
   * - [in]
     - clientId
     - the configured dem client id
   * - [in]
     - reqData
     - the requested data
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was unsuccessful
   * - DCM_E_PENDING
     - Request is not yet finished

Dcm_UDS0x14_ProcessClear
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x14_ProcessClear(uint8 clientId, Dcm_NegativeResponseCodeType *ErrorCode)

process clearDTC

**Sync/Async**
   Depending on Dem

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
     - clientId
     - the configured dem client id
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was unsuccessful
   * - DCM_E_PENDING
     - Request is not yet finished

Dcm_UDS0x19_01
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x19_01(uint8 clientId, Dcm_MsgContextType *pMsgContext, Dcm_NegativeResponseCodeType *ErrorCode)

The service interpreter for UDS 0x19 subfunction 0x01.

**Sync/Async**
   Depending on Dem

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
     - clientId
     - the Dem clientId
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful
   * - DCM_E_PENDING
     - Request is not yet finished

Dcm_UDS0x19_02_0A
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x19_02_0A(uint8 clientId, Dcm_MsgContextType *pMsgContext, Dcm_NegativeResponseCodeType *ErrorCode)

The service interpreter for UDS 0x19 subfunction 0x02 and 0x0A.

**Sync/Async**
   Depending on Dem

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
     - clientId
     - the Dem clientId
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful
   * - DCM_E_PENDING
     - Request is not yet finished

Dcm_UDS0x19_02_0A_Prepare
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x19_02_0A_Prepare(uint8 clientId, Dcm_MsgContextType *pMsgContext, Dcm_NegativeResponseCodeType *ErrorCode)

prepare for processing sunfunction 0x2/0xA

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
     - clientId
     - the Dem clientId
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

Dcm_UDS0x19_02_0A_Process
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x19_02_0A_Process(uint8 clientId, Dcm_MsgContextType *pMsgContext)

process sunfunction 0x2/0xA

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
     - clientId
     - the Dem clientId
   * - [in]
     - oldPagedBufferStarted
     - whether the page buffer is started or not
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [out]
     - offset
     - The resulting offset

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

Dcm_UDS0x19_03
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x19_03(uint8 clientId, Dcm_MsgContextType *pMsgContext, Dcm_NegativeResponseCodeType *ErrorCode)

The service interpreter for UDS 0x19 subfunction 0x03.

**Sync/Async**
   Depending on Dem

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
     - clientId
     - the Dem clientId
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful
   * - DCM_E_PENDING
     - Request is not yet finished

Dcm_UDS0x19_03_Prepare
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x19_03_Prepare(uint8 clientId, Dcm_MsgContextType *pMsgContext, Dcm_NegativeResponseCodeType *ErrorCode)

prepare for processing sunfunction 0x3

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
     - clientId
     - the Dem clientId
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

Dcm_UDS0x19_04
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x19_04(Dcm_OpStatusType OpStatus, uint8 clientId, Dcm_MsgContextType *pMsgContext, Dcm_NegativeResponseCodeType *ErrorCode)

The service interpreter for UDS 0x19 subfunction 0x04.

**Sync/Async**
   Depending on Dem

**Reentrancy**
   Reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - 
     - OpStatus
     - 
   * - [in]
     - clientId
     - the Dem clientId
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful
   * - DCM_E_PENDING
     - Request is not yet finished

Dcm_UDS0x19_04_Prepare
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x19_04_Prepare(Dcm_OpStatusType OpStatus, uint8 clientId, Dcm_MsgContextType *pMsgContext, boolean *disabled, Dcm_NegativeResponseCodeType *ErrorCode)

prepare for processing sunfunction 0x4

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
     - OpStatus
     - current operation status
   * - [in]
     - clientId
     - the Dem clientId
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [out]
     - disabled
     - set to TRUE when Dem_DisableDTCRecordUpdate return E_OK
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

Dcm_UDS0x19_06
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x19_06(Dcm_OpStatusType OpStatus, uint8 clientId, Dcm_MsgContextType *pMsgContext, Dcm_NegativeResponseCodeType *ErrorCode)

The service interpreter for UDS 0x19 subfunction 0x06.

**Sync/Async**
   Depending on Dem

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
     - OpStatus
     - current operation status
   * - [in]
     - clientId
     - the Dem clientId
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful
   * - DCM_E_PENDING
     - Request is not yet finished

Dcm_UDS0x19_06_Prepare
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x19_06_Prepare(Dcm_OpStatusType OpStatus, uint8 clientId, Dcm_MsgContextType *pMsgContext, boolean *disabled, Dcm_NegativeResponseCodeType *ErrorCode)

prepare for processing sunfunction 0x4

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
     - OpStatus
     - current operation status
   * - [in]
     - clientId
     - the Dem clientId
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [out]
     - disabled
     - set to TRUE when Dem_DisableDTCRecordUpdate return E_OK
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

Dcm_UDS0x19_0D
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x19_0D(uint8 clientId, Dcm_MsgContextType *pMsgContext, Dcm_NegativeResponseCodeType *ErrorCode)

The service interpreter for UDS 0x19 subfunction 0x0D.

**Sync/Async**
   Depending on Dem

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
     - clientId
     - the Dem clientId
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful
   * - DCM_E_PENDING
     - Request is not yet finished

Dcm_UDS0x19_0E
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x19_0E(uint8 clientId, Dcm_MsgContextType *pMsgContext, Dcm_NegativeResponseCodeType *ErrorCode)

The service interpreter for UDS 0x19 subfunction 0x0E.

**Sync/Async**
   Depending on Dem

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
     - clientId
     - the Dem clientId
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful
   * - DCM_E_PENDING
     - Request is not yet finished

Dcm_UDS0x19_ProcessSubFunction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x19_ProcessSubFunction(Dcm_OpStatusType OpStatus, uint8 protocolId, Dcm_NegativeResponseCodeType *ErrorCode)

process subFunction of 0x19

**Sync/Async**
   Depending on Dem

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
     - OpStatus
     - current operation status
   * - [in]
     - protocolId
     - current protocol id
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful
   * - DCM_E_PENDING
     - Request is not yet finished

Dcm_UDS0x19_PostProcess
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x19_PostProcess(uint8 protocolId, Std_ReturnType subFunctionResult, Dcm_NegativeResponseCodeType *ErrorCode)

deal with subFunction process result

**Sync/Async**
   Depending on Dem

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
     - protocolId
     - current protocol id
   * - [in]
     - subFunctionResult
     - the result of Dcm_UDS0x19_ProcessSubFunction
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful
   * - DCM_E_PENDING
     - Request is not yet finished

Dcm_UDS0x19_HandleTotalLength
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x19_HandleTotalLength(Dcm_MsgContextType *pMsgContext, Dcm_NegativeResponseCodeType *ErrorCode)

deal with total response length

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
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [out]
     - ErrorCode
     - nrc to send

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

Dcm_UDS0x22_RangeDidHandle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x22_RangeDidHandle(Dcm_ExtendedOpStatusType OpStatus, uint16 ConnectionId, uint16 Did, uint16 RangeDidIndex, uint8 *DestBuffer, Dcm_MsgLenType *BufSize, Dcm_NegativeResponseCodeType *ErrorCode)

This function gets the configured did index, also applying to rangeDid and OBDDid.

**Sync/Async**
   Depending on Application

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
     - OpStatus
     - Indicates the current operation status
   * - [in]
     - ConnectionId
     - the current connectionid
   * - [in]
     - Did
     - the input did
   * - [in]
     - RangeDidIndex
     - the input range did index
   * - [out]
     - DestBuffer
     - address to output the did data
   * - [inout]
     - BufSize
     - When the function is called this parameter contains the maximum number of data bytes that can be written to the buffer. The function returns the actual number of written data bytes in this parameter.
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was unsuccessful
   * - DCM_E_PENDING
     - Request is not yet finished

Dcm_UDS0x22_RangeDidReadData
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x22_RangeDidReadData(Dcm_ExtendedOpStatusType OpStatus, uint16 Did, const Dcm_DspDidRangeType *DcmDspDidRangeCfg, uint8 *DestBuffer, Dcm_MsgLenType *BufSize, Dcm_NegativeResponseCodeType *ErrorCode)

This function reads data of range did.

**Sync/Async**
   Depending on Application

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
     - OpStatus
     - Indicates the current operation status
   * - [in]
     - Did
     - the input did
   * - [in]
     - DcmDspDidRangeCfg
     - the DcmDspDidRange Configuration
   * - [out]
     - DestBuffer
     - the pointer for result
   * - [inout]
     - BufSize
     - When the function is called this parameter contains the maximum number of data bytes that can be written to the buffer. The function returns the actual number of written data bytes in this parameter.
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was unsuccessful
   * - DCM_E_PENDING
     - Request is not yet finished

Dcm_UDS0x22_OBDDidHandle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x22_OBDDidHandle(Dcm_ExtendedOpStatusType OpStatus, uint16 Did, uint8 *DestBuffer, Dcm_MsgLenType *BufSize, Dcm_NegativeResponseCodeType *ErrorCode)

This function deals with obd did to get data.

**Sync/Async**
   Depending on Application

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
     - OpStatus
     - Indicates the current operation status
   * - [in]
     - Did
     - the input did
   * - [out]
     - DestBuffer
     - address to output the did data
   * - [inout]
     - BufSize
     - When the function is called this parameter contains the maximum number of data bytes that can be written to the buffer. The function returns the actual number of written data bytes in this parameter.
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was unsuccessful
   * - DCM_E_PENDING
     - Request is not yet finished

Dcm_UDS0x22_GetDidLength
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x22_GetDidLength(uint16 Did, uint16 ConnectionId, Dcm_MsgLenType *DataLength, Dcm_NegativeResponseCodeType *ErrorCode)

This function gets the did length to read for pagedBuffer functionality.

**Sync/Async**
   Depending on Application

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
     - Did
     - the input did
   * - [in]
     - ConnectionId
     - the current connection id
   * - [out]
     - DataLength
     - The data length of the did
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was unsuccessful
   * - DCM_E_PENDING
     - Request is not yet finished
   * - DCM_E_FORCE_RCRRP
     - Application request the transmission of a response Response Pending (NRC 0x78)

Dcm_UDS0x22_ReadDidPostProcess
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x22_ReadDidPostProcess(uint8 protocolId, Std_ReturnType readResult, uint16 index, Dcm_MsgContextType *pMsgContext, Dcm_NegativeResponseCodeType *ErrorCode)

This function handles the result of read Did and deal with pagedBuffer initialization.

**Sync/Async**
   Depending on Application

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
     - protocolId
     - the current protocol id
   * - [in]
     - readResult
     - the result of read did
   * - [in]
     - index
     - the index of the requested did
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was unsuccessful
   * - DCM_E_PENDING
     - Request is not yet finished
   * - DCM_E_FORCE_RCRRP
     - Application request the transmission of a response Response Pending (NRC 0x78)

Dcm_UDS0x22_ReadDidPrepare
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x22_ReadDidPrepare(Dcm_ExtendedOpStatusType OpStatus, #if(STD_ON==DCM_PAGEDBUFFER_ENABLED) uint8 protocolId, #endif Dcm_MsgContextType *pMsgContext, Dcm_NegativeResponseCodeType *ErrorCode)

This function setup the initial read status and iterate over requested did.

**Sync/Async**
   Depending on Application

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
     - OpStatus
     - Indicates the current operation status
   * - [in]
     - protocolId
     - the current protocol id
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was unsuccessful
   * - DCM_E_PENDING
     - Request is not yet finished
   * - DCM_E_FORCE_RCRRP
     - Application request the transmission of a response Response Pending (NRC 0x78)

Dcm_UDS0x22_HandleDidStatus
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL void Dcm_UDS0x22_HandleDidStatus(Std_ReturnType result, uint16 did, uint16 index, Dcm_MsgContextType* pMsgContext, uint32* offset, Dcm_MsgLenType* bufSize)

This function sets did status

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
     - result
     - the previous result
   * - [in]
     - did
     - the requested did
   * - [in]
     - index
     - the current reading index
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [inout]
     - offset
     - the current offset of the response buffer
   * - [out]
     - bufSize
     - the current available buffer size and resulting data size

**Return type**
   void

Dcm_UDS0x22_ReadDid
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x22_ReadDid(Dcm_ExtendedOpStatusType OpStatus, uint16 index, Dcm_MsgContextType *pMsgContext, uint32 *offset, Dcm_NegativeResponseCodeType *ErrorCode)

This function reads the data of a did.

**Sync/Async**
   Depending on Application

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
     - OpStatus
     - Indicates the current operation status
   * - [in]
     - index
     - the index of the requested did
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [inout]
     - offset
     - the current offset of the response buffer
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was unsuccessful
   * - DCM_E_PENDING
     - Request is not yet finished
   * - DCM_E_FORCE_RCRRP
     - Application request the transmission of a response Response Pending (NRC 0x78)

Dcm_UDS0x22_ReadDidProcess
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x22_ReadDidProcess(Dcm_ExtendedOpStatusType OpStatus, uint16 connectionId, uint16 did, Dcm_DidType didType, uint16 didIndex, uint8 *DestBuffer, Dcm_MsgLenType *bufSize, Dcm_NegativeResponseCodeType *ErrorCode)

This function reads a did based on is type (regular/range/OBD)

**Sync/Async**
   Depending on Application

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
     - OpStatus
     - Indicates the current operation status
   * - [in]
     - connectionId
     - the current connection id
   * - [in]
     - did
     - the requested did
   * - [in]
     - didType
     - the type of the requested did
   * - [in]
     - didIndex
     - the index of the requested did
   * - [inout]
     - DestBuffer
     - output buffer
   * - [inout]
     - bufSize
     - When the function is called this parameter contains the maximum number of data bytes that can be written to the buffer. The function returns the actual number of written data bytes in this parameter.
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was unsuccessful
   * - DCM_E_PENDING
     - Request is not yet finished
   * - DCM_E_FORCE_RCRRP
     - Application request the transmission of a response Response Pending (NRC 0x78)

Dcm_UDS0x23_PostReadMemory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x23_PostReadMemory(Dcm_ReturnReadMemoryType readMemoryResult, Dcm_NegativeResponseCodeType *ErrorCode)

This function handles the result of read memory.

**Sync/Async**
   Depends on Application

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
     - readMemoryResult
     - the result of read memory
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was unsuccessful
   * - DCM_E_PENDING
     - Request is not yet finished
   * - DCM_E_FORCE_RCRRP
     - Application request the transmission of a response Response Pending (NRC 0x78)

Dcm_UDS0x24_GetScalingInfo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x24_GetScalingInfo(uint16 didIndex, uint16 *offset, Dcm_ExtendedOpStatusType OpStatus, Dcm_MsgContextType *pMsgContext, Dcm_NegativeResponseCodeType *ErrorCode)

This function handles getScailingInfo callout.

**Sync/Async**
   Depending on Application

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
     - didIndex
     - the index of did
   * - [inout]
     - offset
     - The current offset of target buffer
   * - [in]
     - OpStatus
     - current operation status
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was unsuccessful
   * - DCM_E_PENDING
     - Request is not yet finished

Dcm_UDS0x27_RequestSeed
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x27_RequestSeed(Dcm_ExtendedOpStatusType OpStatus, uint8 securityIndex, uint8 securityLevel, Dcm_MsgContextType *pMsgContext, Dcm_NegativeResponseCodeType *ErrorCode)

This function deal with request seed subfunction.

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
     - OpStatus
     - current operation status
   * - [in]
     - securityIndex
     - the requested security row configuration
   * - [in]
     - securityLevel
     - the requested security level
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was unsuccessful

Dcm_UDS0x27_SendKey
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x27_SendKey(Dcm_ExtendedOpStatusType OpStatus, uint8 securityIndex, uint8 securityLevel, Dcm_MsgContextType *pMsgContext, Dcm_NegativeResponseCodeType *ErrorCode)

This function deal with send key subfunction.

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
     - OpStatus
     - current operation status
   * - [in]
     - securityIndex
     - the requested security row configuration
   * - [in]
     - securityLevel
     - the requested security level
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was unsuccessful

Dcm_UDS0x27_RequestSeedProcess
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x27_RequestSeedProcess(Dcm_ExtendedOpStatusType OpStatus, uint8 securityLevel, Dcm_MsgContextType *pMsgContext, const Dcm_DspSecurityRowType *securityRow, Dcm_NegativeResponseCodeType *ErrorCode)

This function deal with request seed callout.

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
     - OpStatus
     - current operation status
   * - [in]
     - securityLevel
     - the requested security level
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [in]
     - securityRow
     - the requested security row configuration
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was unsuccessful

Dcm_UDS0x27_GetAttemptCounterProcess
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x27_GetAttemptCounterProcess(Std_ReturnType currentResult, uint8 index, Dcm_OpStatusType OpStatus, boolean *finish)

This function deal with getAttemptCounter callout.

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
     - currentResult
     - the result of previous operation
   * - [in]
     - index
     - the requested security row configuration index
   * - [in]
     - OpStatus
     - current operation status
   * - [inout]
     - finish
     - whether the whole process if finished

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was unsuccessful

Dcm_UDS0x28_ReEnableCommunication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL void Dcm_UDS0x28_ReEnableCommunication(void)

This function switchs the communication modes and enables all coomunication.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant


**Return type**
   void

Dcm_UDS0x28_TxConfirmationExtHandle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL void Dcm_UDS0x28_TxConfirmationExtHandle(uint8 controlType, uint8 communicationType, uint16 nodeIdentificationNumber)

This function handels txConfirmation of extended address subfunction.

**Sync/Async**
   TRUE

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
     - controlType
     - the requested cotrolType
   * - [in]
     - communicationType
     - the requested communicationType
   * - [in]
     - nodeIdentificationNumber
     - the requested nodeIdentiferNumber

**Return type**
   void

Dcm_UDS0x28_FindSubNode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x28_FindSubNode(uint16 nodeIdentificationNumber, Dcm_NegativeResponseCodeType *ErrorCode)

This function finds matched subNode cfg based on input nodeId.

**Sync/Async**
   TRUE

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
     - nodeIdentificationNumber
     - the requested nodeIdentiferNumber
   * - [out]
     - ErrorCode
     - the nrc to send

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was unsuccessful

Dcm_UDS0x29_AuthenticateStore
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL void Dcm_UDS0x29_AuthenticateStore(void)

called to store the current authentication State

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant


**Return type**
   void

Dcm_UDS0x29_SetNrc
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL void Dcm_UDS0x29_SetNrc(Dcm_NegativeResponseCodeType *ErrorCode)

called to set to configured nrc (if have)

**Sync/Async**
   TRUE

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
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   void

Dcm_UDS0x29_SetDeAuthenticateRole
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL void Dcm_UDS0x29_SetDeAuthenticateRole(uint16 connectionId)

called to set authentication role

**Sync/Async**
   TRUE

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
     - the current connectionId

**Return type**
   void

Dcm_UDS0x29_ClearWhiteList
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL void Dcm_UDS0x29_ClearWhiteList(uint16 connectionId)

This function clears the white list.

**Sync/Async**
   TRUE

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
     - the current connectionId

**Return type**
   void

Dcm_UDS0x29_0x00
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x29_0x00(uint16 ConnectionId, Dcm_MsgContextType *pMsgContext, Dcm_NegativeResponseCodeType *ErrorCode)

The service interpreter for UDS 0x29 subfunction 0x00.

**Sync/Async**
   TRUE

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
     - ConnectionId
     - the current connection id
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

Dcm_UDS0x29_KeyMAsyncCheck
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x29_KeyMAsyncCheck(Dcm_NegativeResponseCodeType *ErrorCode)

Checkes KeyM asynchronous result and set errorCode accordingly.

**Sync/Async**
   TRUE

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
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

Dcm_UDS0x29_Challenge
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x29_Challenge(uint16 ConnectionId, Dcm_MsgContextType *pMsgContext, Dcm_NegativeResponseCodeType *ErrorCode)

This function deals with challenge and output accordingly.

**Sync/Async**
   Asynchronous

**Reentrancy**
   Reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - 
     - ConnectionId
     - 
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful
   * - DCM_E_PENDING
     - Request was not yet finished

Dcm_UDS0x29_HandleCsmGenerateResult
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x29_HandleCsmGenerateResult(uint16 ConnectionId, Dcm_MsgContextType *pMsgContext, Dcm_NegativeResponseCodeType *ErrorCode)

This function deals with Csm Generate asynchronous result.

**Sync/Async**
   Asynchronous

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
     - ConnectionId
     - the current connection Id
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful
   * - DCM_E_PENDING
     - Request was not yet finished

Dcm_UDS0x29_HandleCsmSignatureResult
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x29_HandleCsmSignatureResult(uint16 ConnectionId, Dcm_MsgContextType *pMsgContext, Dcm_NegativeResponseCodeType *ErrorCode)

This function deals with Csm Signature asynchronous result.

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
     - ConnectionId
     - the current connection Id
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

Dcm_UDS0x29_01_02
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x29_01_02(Dcm_ExtendedOpStatusType OpStatus, uint16 ConnectionId, Dcm_MsgContextType *pMsgContext, Dcm_NegativeResponseCodeType *ErrorCode)

The service interpreter for UDS 0x29 subfunction 0x01 or 0x02.

**Sync/Async**
   FALSE

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
     - OpStatus
     - Indicates the current operation status
   * - [in]
     - ConnectionId
     - the current connection Id
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful
   * - DCM_E_PENDING
     - Request was not yet finished

Dcm_UDS0x29_01_02_InitialHandle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x29_01_02_InitialHandle(uint16 ConnectionId, Dcm_MsgContextType *pMsgContext, Dcm_NegativeResponseCodeType *ErrorCode)

Handle UDS 0x29 subfunction 0x01 or 0x02 when opStatus is DCM_INITIAL.

**Sync/Async**
   Asynchronous

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
     - ConnectionId
     - the current connection Id
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful
   * - DCM_E_PENDING
     - Request was not yet finished

Dcm_UDS0x29_0x03_getlist
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x29_0x03_getlist(Dcm_KeyMCertInfoType Dcm_KeyMCertInfo, uint8 *DataPtr, uint8 *DataLength, Dcm_NegativeResponseCodeType *ErrorCode)

gets the specific lists

**Sync/Async**
   FALSE

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
     - Dcm_KeyMCertInfo
     - the input cerfication info
   * - [out]
     - DataPtr
     - the dest buffer
   * - [out]
     - DataLength
     - the total data length
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful
   * - DCM_E_PENDING
     - Request was not yet finished

Dcm_UDS0x29_0x03_whitelist
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x29_0x03_whitelist(uint16 ConnectionId, Dcm_NegativeResponseCodeType *ErrorCode)

gets the white lists

**Sync/Async**
   FALSE

**Reentrancy**
   Reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - 
     - ConnectionId
     - 
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful
   * - DCM_E_PENDING
     - Request was not yet finished

Dcm_UDS0x29_0x03_Update
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x29_0x03_Update(uint16 ConnectionId, Dcm_NegativeResponseCodeType *ErrorCode)

updates the authentication State

**Sync/Async**
   FALSE

**Reentrancy**
   Reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - 
     - ConnectionId
     - 
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful
   * - DCM_E_PENDING
     - Request was not yet finished

Dcm_UDS0x29_0x03
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x29_0x03(Dcm_ExtendedOpStatusType OpStatus, uint16 ConnectionId, Dcm_MsgContextType *pMsgContext, Dcm_NegativeResponseCodeType *ErrorCode)

The service interpreter for UDS 0x29 subfunction 0x03.

**Sync/Async**
   FALSE

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
     - OpStatus
     - Indicates the current operation status
   * - 
     - ConnectionId
     - 
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful
   * - DCM_E_PENDING
     - Request was not yet finished

Dcm_UDS0x29_0x04
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x29_0x04(Dcm_OpStatusType OpStatus, Dcm_MsgContextType *pMsgContext, Dcm_NegativeResponseCodeType *ErrorCode)

The service interpreter for UDS 0x29 subfunction 0x04.

**Sync/Async**
   Asynchronous

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
     - OpStatus
     - Indicates the current operation status
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful
   * - DCM_E_PENDING
     - Request was not yet finished

Dcm_UDS0x29_0x04_KeyMProcess
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x29_0x04_KeyMProcess(KeyM_CertDataType *certData, uint16 CertId, Dcm_NegativeResponseCodeType *ErrorCode)

Handles interaction with KeyM for UDS 0x29 subfunction 0x04.

**Sync/Async**
   Asynchronous

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
     - certData
     - the input certData
   * - [in]
     - CertId
     - the input certificate evaluation id
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful
   * - DCM_E_PENDING
     - Request was not yet finished

Dcm_UDS0x29_0x04_ConditionCheck
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x29_0x04_ConditionCheck(Dcm_MsgContextType *pMsgContext, Dcm_NegativeResponseCodeType *ErrorCode, uint16 *TransmitCertificateRef)

check conditions for subfunction 0x04

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
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.
   * - [out]
     - TransmitCertificateRef
     - The configured cerficateRef

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

Dcm_UDS0x29_0x08
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x29_0x08(Dcm_MsgContextType *pMsgContext, Dcm_NegativeResponseCodeType *ErrorCode)

The service interpreter for UDS 0x29 subfunction 0x08.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

Dcm_UDS0x29_RoleCheck
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x29_RoleCheck(uint16 ConnectionId, const uint8 *RoleRef, uint8 RoleNum)

checks whether the role is validated

**Sync/Async**
   TRUE

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
     - ConnectionId
     - the current connection Id
   * - [in]
     - RoleRef
     - the input role ref
   * - [in]
     - RoleNum
     - the number of role ref

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

Dcm_UDS0x29_WhiteListCheck
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x29_WhiteListCheck(uint16 ConnectionId, Dcm_MsgLenType CheckLength)

checks whether the service is in white list

**Sync/Async**
   TRUE

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
     - ConnectionId
     - the current connection Id
   * - [in]
     - CheckLength
     - the input check length

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

Dcm_UDS0x29_DidWhiteListCheck
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x29_DidWhiteListCheck(uint16 ConnectionId, uint16 RecDid)

checks whether the did is in white list

**Sync/Async**
   TRUE

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
     - ConnectionId
     - the current connection Id
   * - [in]
     - RecDid
     - the input did

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

Dcm_UDS0x29_RidWhiteListCheck
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x29_RidWhiteListCheck(uint16 ConnectionId)

checks whether the rid is in white list

**Sync/Async**
   TRUE

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
     - ConnectionId
     - the current connection Id

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

Dcm_UDS0x2A_SchedulerInit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL void Dcm_UDS0x2A_SchedulerInit(Dcm_SchedulerType *schedulerPtr)

Called by UDS 0x2A to initialize the scheduler.

**Sync/Async**
   TRUE

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
     - schedulerPtr
     - the scheduler ptr

**Return type**
   void

Dcm_UDS0x2A_ConditionCheck
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x2A_ConditionCheck(Dcm_MsgContextType *pMsgContext, Dcm_NegativeResponseCodeType *ErrorCode)

check conditions for UDS 0x2A

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
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

Dcm_UDS0x2A_HandleDid
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x2A_HandleDid(Dcm_ExtendedOpStatusType OpStatus, Dcm_MsgContextType *pMsgContext, uint16 connectionId, Dcm_NegativeResponseCodeType *ErrorCode)

handle did read for UDS 0x2A

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
     - OpStatus
     - current operation status
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - 
     - connectionId
     - 
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

Dcm_UDS0x2A_HandleDidConditionCheck
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x2A_HandleDidConditionCheck(uint16 didIndex, Dcm_ExtendedOpStatusType OpStatus, Dcm_NegativeResponseCodeType *ErrorCode)

handles did conditionCheck callout

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
     - didIndex
     - the reuqested did index
   * - [in]
     - OpStatus
     - current operation status
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

Dcm_UDS0x2A_DidReadPrepare
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x2A_DidReadPrepare(uint16 connectionId, uint16 didIndex, Dcm_ExtendedOpStatusType OpStatus, uint16 *dataLength, Dcm_NegativeResponseCodeType *ErrorCode)

prepare for dynamic did read

**Sync/Async**
   Depends on Application

**Reentrancy**
   Reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - 
     - connectionId
     - 
   * - [in]
     - didIndex
     - the reuqested did index
   * - [in]
     - OpStatus
     - current operation status
   * - [out]
     - dataLength
     - the dataLength of dynamic did
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful
   * - DCM_E_PENDING
     - Request is not yet finished

Dcm_UDS0x2A_SetScheduler
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x2A_SetScheduler(uint16 didIndex, uint16 connectionId, uint16 dataLength, Dcm_MsgContextType *pMsgContext, Dcm_NegativeResponseCodeType *ErrorCode)

setup scheduler for requested periodic read

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
     - didIndex
     - the reuqested did index
   * - 
     - connectionId
     - 
   * - [out]
     - dataLength
     - the dataLength of dynamic did
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

Dcm_UDS0x2A_SetNonStopScheduler
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x2A_SetNonStopScheduler(Dcm_SchedulerType *schedulerPtr, uint16 didIndex, uint16 connectionId, uint8 transMode, uint16 dataLength)

setup scheduler for requested periodic read for nonStop subfunction

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
     - schedulerPtr
     - the previously found schedulerPtr
   * - [in]
     - didIndex
     - the reuqested did index
   * - 
     - connectionId
     - 
   * - [in]
     - transMode
     - the requested transMode
   * - [in]
     - dataLength
     - the dataLength of dynamic did

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

Dcm_UDS0x2A_MainFunctionHandle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL void Dcm_UDS0x2A_MainFunctionHandle(Dcm_SchedulerType *schedulerPtr)

handle a operating scheduler

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
     - schedulerPtr
     - the target scheduler

**Return type**
   void

Dcm_UDS0x2A_PeriodicSend
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x2A_PeriodicSend(uint16 connIndex)

prepare data and send periodic data

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
     - connIndex
     - the current connection index
   * - [in]
     - schedulerPtr
     - the current scheduler pointer

**Return type**
   void

Dcm_UDS0x2C_ConditionCheck
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x2C_ConditionCheck(uint16 connectionId, Dcm_MsgContextType *pMsgContext, Dcm_NegativeResponseCodeType *ErrorCode, uint16 *didIndex)

General condition checks for UDS 0x2C.

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
     - current connection id
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.
   * - [out]
     - didIndex
     - The index of requested did

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

Dcm_UDS0x2C_01
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x2C_01(uint16 connectionId, Dcm_MsgContextType *pMsgContext, uint16 DDDIDIndex, const Dcm_DspDidInfoType *DcmDspDidInfoPtr, Dcm_NegativeResponseCodeType *ErrorCode)

The service interpreter for UDS 0x2C subfunction 0x01.

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
     - current connection id
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [in]
     - DDDIDIndex
     - DDDID index for reqeusted did
   * - [in]
     - DcmDspDidInfoPtr
     - the DcmDspDidInfo configuration
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

Dcm_UDS0x2C_02
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x2C_02(Dcm_MsgContextType *pMsgContext, uint16 DDDIDIndex, const Dcm_DspDidInfoType *DcmDspDidInfoPtr, Dcm_NegativeResponseCodeType *ErrorCode)

The service interpreter for UDS 0x2C subfunction 0x02.

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
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [in]
     - DDDIDIndex
     - DDDID index for reqeusted did
   * - [in]
     - DcmDspDidInfoPtr
     - the DcmDspDidInfo configuration
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

Dcm_UDS0x2C_02_ConditionCheck
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x2C_02_ConditionCheck(Dcm_MsgContextType *pMsgContext, const Dcm_DspDidInfoType *DcmDspDidInfoPtr, Dcm_MsgLenType *SourceElementsNum, Dcm_NegativeResponseCodeType *ErrorCode)

general condition check for UDS 0x2C, subFunction 0x2

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
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [in]
     - DcmDspDidInfoPtr
     - the DcmDspDidInfo configuration
   * - [out]
     - SourceElementsNum
     - the requestged source element number
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

Dcm_UDS0x2C_03
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x2C_03(Dcm_MsgLenType reqDataLen, uint16 DDDIDIndex)

The service interpreter for UDS 0x2C subfunction 0x03.

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
     - reqDataLen
     - the request data length
   * - [in]
     - DDDIDIndex
     - DDDID index for reqeusted did

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

Dcm_UDS0x2E_ConditionCheck
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x2E_ConditionCheck(Dcm_MsgContextType *pMsgContext, uint16 *did, uint16 *didIndex, Dcm_DidType *didType, Dcm_NegativeResponseCodeType *ErrorCode)

General condition checks for UDS 0x2E.

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
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [out]
     - did
     - The requested did
   * - [out]
     - didIndex
     - The index of requested did
   * - [out]
     - didType
     - The type of requested did
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

Dcm_UDS0x2E_SecureCoding
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x2E_SecureCoding(boolean *secureCoding, Dcm_MsgContextType *pMsgContext, uint16 did, uint16 didIndex, Dcm_NegativeResponseCodeType *ErrorCode)

process secure coding for UDS 0x2E

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
     - secureCoding
     - whether the requested did is configured to be secure coding did
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [in]
     - did
     - The requested did
   * - [in]
     - didIndex
     - The index of requested did
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

Dcm_UDS0x2E_WriteDspDataSignal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x2E_WriteDspDataSignal(const uint8 *reqData, Dcm_MsgLenType reqDataLen, const Dcm_DspDidType *DcmDspDidCfg, Dcm_ExtendedOpStatusType OpStatus, #if(STD_ON==DCM_DYN_DATA) boolean isDynamic, #endif Dcm_NegativeResponseCodeType *ErrorCode)

process dspData write for signal

**Sync/Async**
   Depends on Application

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
     - reqData
     - the requested data
   * - [inout]
     - reqDataLen
     - the requested data length
   * - [in]
     - DcmDspDidCfg
     - the configuration of requested did
   * - [in]
     - OpStatus
     - current operation status
   * - [in]
     - isDynamic
     - whether the requested did is a dynamic one
   * - [out]
     - ErrorCode
     - nrc to send

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful
   * - DCM_E_PENDING
     - Request is not yet finished

Dcm_UDS0x2E_NvMSignalHandle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x2E_NvMSignalHandle(NvM_BlockIdType blockId, Dcm_ExtendedOpStatusType OpStatus, uint8 *data, Dcm_NegativeResponseCodeType *ErrorCode)

handle signal that use nvm block to write

**Sync/Async**
   Asynchronous

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
     - blockId
     - the configured nvm block id
   * - [in]
     - OpStatus
     - current operation status
   * - [in]
     - data
     - data to be written
   * - [out]
     - ErrorCode
     - nrc to send

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful
   * - DCM_E_PENDING
     - Request is not yet finished

Dcm_UDS0x2F_ConditionCheck
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x2F_ConditionCheck(Dcm_MsgContextType *pMsgContext, Dcm_NegativeResponseCodeType *ErrorCode, uint16 *didIndex, boolean *isDynamic)

called to check conditions for UDS 0x2F

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.
   * - [out]
     - didIndex
     - the target did configuration index if condition check passes
   * - [out]
     - isDynamic
     - whether the did is dynamic

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

Dcm_UDS0x2F_FindDidControl
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x2F_FindDidControl(uint16 did, const Dcm_DspDidType **didCfg, const Dcm_DspDidControlType **didControlCfg, uint16 *didIndex, Dcm_NegativeResponseCodeType *ErrorCode)

find did and did control configuration based on input did

**Sync/Async**
   TRUE

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
     - did
     - the requested did
   * - [out]
     - didCfg
     - the requested did configuration
   * - [out]
     - didControlCfg
     - the requested did control configuration
   * - [out]
     - didIndex
     - the configuration index of the did
   * - [out]
     - ErrorCode
     - the nrc to send

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

Dcm_UDS0x2F_CheckTotalLength
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x2F_CheckTotalLength(const Dcm_DspDidType *didCfg, const Dcm_DspDidControlType *didControlCfg, Dcm_MsgContextType *pMsgContext, boolean *isDynamic, Dcm_NegativeResponseCodeType *ErrorCode)

check to totalLength of request

**Sync/Async**
   TRUE

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
     - didCfg
     - the requested did configuration
   * - [in]
     - didControlCfg
     - the requested did control configuration
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [out]
     - isDynamic
     - is the requested did dynamic
   * - [out]
     - ErrorCode
     - nrc to send

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

Dcm_UDS0x2F_ControlRestore
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL void Dcm_UDS0x2F_ControlRestore(uint16 didIndex, const Dcm_DspDidControlType *didControlCfg)

restore io control

**Sync/Async**
   TRUE

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
     - didIndex
     - the requested did configuration index
   * - [in]
     - didControlCfg
     - the requested did control configuration

**Return type**
   void

Dcm_UDS0x2F_ControlHandle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x2F_ControlHandle(Dcm_ExtendedOpStatusType OpStatus, Dcm_MsgContextType *pMsgContext, uint16 didIndex, const Dcm_DspDidControlType *didControlCfg, boolean isDynamic, Dcm_NegativeResponseCodeType *ErrorCode)

process io control including cmer and ioCtrlParam

**Sync/Async**
   TRUE

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
     - OpStatus
     - current operation status
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [in]
     - didIndex
     - the requested did configuration index
   * - [in]
     - didControlCfg
     - the requested did control configuration
   * - [in]
     - isDynamic
     - is the requested did dynamic
   * - [out]
     - ErrorCode
     - nrc to send

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful
   * - DCM_E_PENDING
     - Request is not yet finished

Dcm_UDS0x2F_HandleCMER
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x2F_HandleCMER(uint16 signalIndex, uint16 didIndex, const Dcm_DspDidControlType *didControlCfg, boolean isDynamic, Dcm_MsgContextType *pMsgContext, Dcm_MsgLenType *stateSize, uint16 *maskOffset)

process CMER

**Sync/Async**
   TRUE

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
     - signalIndex
     - signal index
   * - [in]
     - didIndex
     - the requested did configuration index
   * - [in]
     - didControlCfg
     - the requested did control configuration
   * - [in]
     - isDynamic
     - is the requested did dynamic
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [out]
     - stateSize
     - the requested state size
   * - [inout]
     - maskOffset
     - the current maskOffset

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - this signal shall be processed
   * - E_NOT_OK
     - this signal shall be skipped

Dcm_UDS0x2F_HandleIoControl
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x2F_HandleIoControl(uint8 *reqData, Dcm_ExtendedOpStatusType OpStatus, const Dcm_DspDataCfgType *DcmDspDataCfg, uint8 ioCtrlParam, uint16 stateOffset, Dcm_MsgLenType stateSize, const uint8 *controlMaskPtr, Dcm_NegativeResponseCodeType *ErrorCode)

process ioCtrlParam

**Sync/Async**
   TRUE

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
     - reqData
     - requested data
   * - [in]
     - OpStatus
     - current operation status
   * - [in]
     - DcmDspDataCfg
     - DcmDspData configuration
   * - [in]
     - ioCtrlParam
     - requested ioCtrl Parameter
   * - [in]
     - stateOffset
     - requested state offset
   * - [in]
     - stateSize
     - requested state size
   * - [in]
     - controlMaskPtr
     - requested controlMask pointer
   * - [out]
     - ErrorCode
     - nrc to send

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

Dcm_UDS0x31_FindRoutineIndex
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x31_FindRoutineIndex(uint16 rid, uint16 *routineIndex, Dcm_NegativeResponseCodeType *ErrorCode)

find the configured rid index

**Sync/Async**
   TRUE

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
     - rid
     - the input rid
   * - [out]
     - routineIndex
     - the configuration index
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

Dcm_UDS0x31_HandleOBDRID
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x31_HandleOBDRID(Dcm_MsgContextType *pMsgContext, uint16 *totalLength, Dcm_NegativeResponseCodeType *ErrorCode)

process OBD type rid

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [inout]
     - totalLength
     - the total length of the response
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

Dcm_UDS0x31_SecureCoding
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x31_SecureCoding(Dcm_ExtendedOpStatusType OpStatus, uint16 routineIndex, Dcm_MsgContextType *pMsgContext, Dcm_NegativeResponseCodeType *ErrorCode)

process secure coding rid

**Sync/Async**
   TRUE

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
     - OpStatus
     - Indicates the current operation status
   * - [in]
     - routineIndex
     - target routine index
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

Dcm_UDS0x31_SecureCodingInitial
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x31_SecureCodingInitial(Dcm_MsgContextType *pMsgContext, uint16 routineIndex)

handle secure coding for DCM_INITIAL opstatus

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [in]
     - routineIndex
     - target routine index

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

Dcm_UDS0x31_SecureCodingPending
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x31_SecureCodingPending(uint8 *resData)

handle secure coding for DCM_PENDING opstatus

**Sync/Async**
   TRUE

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
     - resData
     - The output data

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

Dcm_UDS0x31_SecureCodingFinish
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x31_SecureCodingFinish(uint8 *resData)

finish secure coding

**Sync/Async**
   TRUE

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
     - resData
     - The output data

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

Dcm_UDS0x31_HandleSubFunction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x31_HandleSubFunction(Dcm_ExtendedOpStatusType OpStatus, uint8 protocolId, uint16 routineIndex, uint8 subFunction, const Dcm_DspRoutineSubType **routineSub, Dcm_NegativeResponseCodeType *ErrorCode)

handle UDS 0x31 subfunctions, check condition

**Sync/Async**
   TRUE

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
     - OpStatus
     - current operation status
   * - [in]
     - protocolId
     - the current protocolId
   * - [in]
     - routineIndex
     - routine configuration index
   * - [in]
     - subFunction
     - the requested subfunction
   * - [out]
     - routineSub
     - the requested subConfiguration of routine
   * - [out]
     - ErrorCode
     - nrc to send

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

Dcm_UDS0x31_CheckRoutineCommonAuth
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x31_CheckRoutineCommonAuth(const Dcm_DspCommonAuthorizationType *commonAuthorization, Dcm_NegativeResponseCodeType *ErrorCode)

check routine common authroization

**Sync/Async**
   TRUE

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
     - commonAuthorization
     - routine configuration index
   * - [out]
     - ErrorCode
     - nrc to send

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

Dcm_UDS0x31_HandleRegularRID
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x31_HandleRegularRID(Dcm_ExtendedOpStatusType OpStatus, Dcm_MsgContextType *pMsgContext, uint16 routineIndex, uint16 *totalLength, Dcm_NegativeResponseCodeType *ErrorCode)

process regular type rid

**Sync/Async**
   TRUE

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
     - OpStatus
     - current operation status
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [in]
     - routineIndex
     - current routine configuration index
   * - [out]
     - totalLength
     - the total length of the response
   * - [out]
     - ErrorCode
     - nrc to send

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

Dcm_UDS0x31_RoutineCallout
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x31_RoutineCallout(Dcm_ExtendedOpStatusType OpStatus, Dcm_MsgContextType *pMsgContext, const Dcm_DspRoutineSubType *routineSub, uint16 routineIndex, uint16 *totalLength, Dcm_NegativeResponseCodeType *ErrorCode)

process routine callout

**Sync/Async**
   TRUE

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
     - OpStatus
     - current operation status
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [in]
     - routineSub
     - the requested subConfiguration of routine
   * - [in]
     - routineIndex
     - the routine configuration index
   * - [out]
     - totalLength
     - the total length of the response
   * - [out]
     - ErrorCode
     - nrc to send

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

Dcm_UDS0x31_InSignalCheck
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x31_InSignalCheck(Dcm_MsgLenType reqDataLen, const Dcm_DspRoutineSubType *routineSub, Dcm_NegativeResponseCodeType *ErrorCode)

check inSignal request length

**Sync/Async**
   TRUE

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
     - reqDataLen
     - request data length
   * - [in]
     - routineSub
     - the requested subConfiguration of routine
   * - [out]
     - ErrorCode
     - nrc to send

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

Dcm_UDS0x31_OutSignalCheck
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x31_OutSignalCheck(const Dcm_DspRoutineSubType *routineSub, uint16 currentDataLength, uint16 *totalLength, Dcm_NegativeResponseCodeType *ErrorCode)

check outSignal response length

**Sync/Async**
   TRUE

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
     - routineSub
     - the requested subConfiguration of routine
   * - [in]
     - currentDataLength
     - current response data length
   * - [out]
     - totalLength
     - the response length
   * - [out]
     - ErrorCode
     - nrc to send

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

Dcm_UDS0x34_ConditionCheck
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x34_ConditionCheck(Dcm_MsgContextType *pMsgContext, uint32 *memoryAddress, uint32 *memorySize, uint8 *memoryIdentifier, Dcm_NegativeResponseCodeType *ErrorCode)

check general conditions for UDS 0x34

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [out]
     - memoryAddress
     - the requested memoryAddress
   * - [out]
     - memorySize
     - the requested memorySize
   * - [out]
     - memoryIdentifier
     - the configured memoryIdentifier
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

Dcm_UDS0x35_ConditionCheck
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x35_ConditionCheck(Dcm_MsgContextType *pMsgContext, uint32 *memoryAddress, uint32 *memorySize, uint8 *memoryIdentifier, Dcm_NegativeResponseCodeType *ErrorCode)

check general conditions for UDS 0x35

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [out]
     - memoryAddress
     - the requested memoryAddress
   * - [out]
     - memorySize
     - the requested memorySize
   * - [out]
     - memoryIdentifier
     - the configured memoryIdentifier
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

Dcm_UDS0x36_ConditionCheck
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x36_ConditionCheck(Dcm_MsgContextType *pMsgContext, uint64 *dataLength, Dcm_NegativeResponseCodeType *ErrorCode)

check general conditions for UDS 0x36

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [out]
     - dataLength
     - the data length of the following operations
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

Dcm_UDS0x36_HandleTransfer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x36_HandleTransfer(Dcm_ExtendedOpStatusType OpStatus, uint64 *dataLength, Dcm_MsgContextType *pMsgContext, Dcm_NegativeResponseCodeType *ErrorCode)

handle actual data transfer

**Sync/Async**
   TRUE

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
     - OpStatus
     - Indicates the current operation status
   * - [inout]
     - dataLength
     - the data length of the following operations
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful
   * - DCM_E_PENDING
     - Request is not yet finished
   * - DCM_E_FORCE_RCRRP
     - Application requests the transmission of a response Response Pending (NRC 0x78)

Dcm_UDS0x36_CheckSequence
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x36_CheckSequence(Dcm_MsgLenType reqDataLen, uint8 blockSequenceCounter, Dcm_NegativeResponseCodeType *ErrorCode)

check the transfer sequence such as previous service request and block sequence counter

**Sync/Async**
   TRUE

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
     - reqDataLen
     - the request data length
   * - [in]
     - blockSequenceCounter
     - requested block sequence counter
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

Dcm_UDS0x36_ProcessRead
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x36_ProcessRead(Dcm_ExtendedOpStatusType OpStatus, uint64 dataLength, Dcm_MsgContextType *pMsgContext, Dcm_NegativeResponseCodeType *ErrorCode)

process data transfer of read

**Sync/Async**
   TRUE

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
     - OpStatus
     - Indicates the current operation status
   * - [in]
     - dataLength
     - the data length of the following operations
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful
   * - DCM_E_PENDING
     - Request is not yet finished
   * - DCM_E_FORCE_RCRRP
     - Application requests the transmission of a response Response Pending (NRC 0x78)

Dcm_UDS0x36_ProcessWrite
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x36_ProcessWrite(Dcm_ExtendedOpStatusType OpStatus, uint64 dataLength, Dcm_MsgContextType *pMsgContext, Dcm_NegativeResponseCodeType *ErrorCode)

process data transfer of write

**Sync/Async**
   TRUE

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
     - OpStatus
     - Indicates the current operation status
   * - [in]
     - dataLength
     - the data length of the following operations
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful
   * - DCM_E_PENDING
     - Request is not yet finished
   * - DCM_E_FORCE_RCRRP
     - Application requests the transmission of a response Response Pending (NRC 0x78)

Dcm_UDS0x38_ConvertToU64
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL uint64 Dcm_UDS0x38_ConvertToU64(uint8 *data, uint8 size)

This function coverts data to uint64.

**Sync/Async**
   TRUE

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
     - data
     - the input uint8_N data
   * - [in]
     - size
     - the size of the data

**Return type**
   DCM_LOCAL uint64

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - the
     - result data

Dcm_UDS0x38_CheckCondition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x38_CheckCondition(Dcm_MsgContextType *pMsgContext, uint8 *dataFormatIdentifier, uint64 *fileSizeUncompressed, uint64 *fileSizeCompressed, Dcm_NegativeResponseCodeType *ErrorCode)

check general conditions for UDS 0x38

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [out]
     - dataFormatIdentifier
     - requested dataFormatIdentifier
   * - [out]
     - fileSizeUncompressed
     - requested fileSizeUncompressed
   * - [out]
     - fileSizeCompressed
     - requested fileSizeCompressed
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

Dcm_UDS0x38_HandleModeOfOperation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x38_HandleModeOfOperation(Dcm_ExtendedOpStatusType OpStatus, Dcm_MsgContextType *pMsgContext, uint8 modeOfOperation, uint8 dataFormatIdentifier, uint64 *fileSizeUncompressed, uint64 *fileSizeCompressed, uint64 *maxNumberOfBlockLength, uint64 *dirInfoLength, Dcm_NegativeResponseCodeType *ErrorCode)

check general conditions for UDS 0x38

**Sync/Async**
   TRUE

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
     - OpStatus
     - Indicates the current operation status
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [in]
     - modeOfOperation
     - requested modeOfOperation
   * - [in]
     - dataFormatIdentifier
     - requested dataFormatIdentifier
   * - [inout]
     - fileSizeUncompressed
     - requested fileSizeUncompressed
   * - [inout]
     - fileSizeCompressed
     - requested fileSizeCompressed
   * - [out]
     - maxNumberOfBlockLength
     - output maxNumberOfBlockLength
   * - [out]
     - dirInfoLength
     - output dirInfoLength
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful
   * - DCM_E_PENDING
     - Request is not yet finished
   * - DCM_E_FORCE_RCRRP
     - Application requests the transmission of a response Response Pending (NRC 0x78)

Dcm_UDS0x38_NonDeleteFileMode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x38_NonDeleteFileMode(uint8 modeOfOperation, uint64 fileSizeUncompressed, uint64 *maxNumberOfBlockLength, Dcm_MsgContextType *pMsgContext, Dcm_NegativeResponseCodeType *ErrorCode)

handle modeOfOperation that is not DeleteFile

**Sync/Async**
   TRUE

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
     - modeOfOperation
     - requested modeOfOperation
   * - [in]
     - fileSizeUncompressed
     - requested fileSizeUncompressed
   * - [out]
     - maxNumberOfBlockLength
     - output maxNumberOfBlockLength
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

Dcm_UDS0x3D_CheckCondition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x3D_CheckCondition(Dcm_MsgContextType *pMsgContext, uint8 *memoryIdentifier, uint32 *memoryAddress, uint32 *memorySize, Dcm_NegativeResponseCodeType *ErrorCode)

check general conditions for UDS 0x3D

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [out]
     - memoryIdentifier
     - the configured memoryIdentifier
   * - [out]
     - memoryAddress
     - the requested memoryAddress
   * - [out]
     - memorySize
     - the requested memorySize
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

Dcm_UDS0x85_ConditionCheck
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x85_ConditionCheck(Dcm_MsgContextType *pMsgContext, Dcm_NegativeResponseCodeType *ErrorCode)

check general conditions for UDS 0x85

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

Dcm_UDS0x86_SetEvent
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x86_SetEvent(Dcm_ProtocolType protocolType, Dcm_RoeEventType roeEvent, Dcm_RoeEventWindowTimeType eventWindowTime, Dcm_NegativeResponseCodeType *ErrorCode)

called to set the roeEvent to Dcm_RoeCtrl

**Sync/Async**
   TRUE

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
     - protocolType
     - current protocolType
   * - [in]
     - roeEvent
     - the input roeEvent
   * - [in]
     - eventWindowTime
     - the input event window time
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

Dcm_UDS0x86_MainFunction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL void Dcm_UDS0x86_MainFunction(void)

called by Dcm_UDS0x86_CheckTimer to act as the roe scheduler

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant


**Return type**
   void

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - void
     - 

Dcm_UDS0x86_ConditionCheck
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x86_ConditionCheck(Dcm_MsgContextType *pMsgContext, Dcm_RoeEventWindowTimeType *eventWindowTime, Dcm_NegativeResponseCodeType *ErrorCode)

general condition check for UDS 0x86

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [out]
     - eventWindowTime
     - the requested event window time
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

Dcm_UDS0x86_SubFunctionCheck
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x86_SubFunctionCheck(Dcm_MsgLenType reqDataLen, uint8 subFunction, Dcm_NegativeResponseCodeType *ErrorCode)

general checks for subfunction

**Sync/Async**
   TRUE

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
     - reqDataLen
     - the requested data length
   * - [in]
     - subFunction
     - the requested subFunction
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

Dcm_UDS0x86_01
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x86_01(uint8 protocolId, Dcm_RoeCtrlType *roeCtrlPtr, Dcm_MsgContextType *pMsgContext, Dcm_RoeEventWindowTimeType eventWindowTime, Dcm_NegativeResponseCodeType *ErrorCode)

service interpreter for subFunction 0x1

**Sync/Async**
   TRUE

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
     - protocolId
     - the current protocolId
   * - [in]
     - roeCtrlPtr
     - the roe control Unit pointer
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [in]
     - eventWindowTime
     - the requested eventWindowTime
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

Dcm_UDS0x86_03
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x86_03(uint8 protocolId, Dcm_RoeCtrlType *roeCtrlPtr, Dcm_MsgContextType *pMsgContext, Dcm_RoeEventWindowTimeType eventWindowTime, Dcm_NegativeResponseCodeType *ErrorCode)

service interpreter for subFunction 0x3

**Sync/Async**
   TRUE

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
     - protocolId
     - the current protocolId
   * - [in]
     - roeCtrlPtr
     - the roe control Unit pointer
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [in]
     - eventWindowTime
     - the requested eventWindowTime
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

Dcm_UDS0x86_04
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL void Dcm_UDS0x86_04(Dcm_MsgContextType *pMsgContext)

service interpreter for subFunction 0x4

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.

**Return type**
   void

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

Dcm_UDS0x86_06
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL void Dcm_UDS0x86_06(void)

service interpreter for subFunction 0x6

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant


**Return type**
   void

Dcm_UDS0x86_08
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x86_08(uint8 protocolId, Dcm_RoeCtrlType *roeCtrlPtr, Dcm_MsgContextType *pMsgContext, Dcm_RoeEventWindowTimeType eventWindowTime, Dcm_NegativeResponseCodeType *ErrorCode)

service interpreter for subFunction 0x8

**Sync/Async**
   TRUE

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
     - protocolId
     - the current protocolId
   * - [in]
     - roeCtrlPtr
     - the roe control Unit pointer
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [in]
     - eventWindowTime
     - the requested eventWindowTime
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

Dcm_UDS0x86_Store
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL void Dcm_UDS0x86_Store(uint8 subFunction, Dcm_RoeEventWindowTimeType eventWindowTime, Dcm_MsgContextType *pMsgContext)

store roe info to NvM

**Sync/Async**
   TRUE

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
     - subFunction
     - the requested subFunction
   * - [in]
     - eventWindowTime
     - the requested eventWindowTime
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.

**Return type**
   void

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

Dcm_UDS0x86_HandleSubFunction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x86_HandleSubFunction(uint8 protocolId, Dcm_RoeCtrlType *roeCtrlPtr, Dcm_MsgContextType *pMsgContext, Dcm_RoeEventWindowTimeType eventWindowTime, Dcm_NegativeResponseCodeType *ErrorCode)

handle different subFunctions

**Sync/Async**
   TRUE

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
     - protocolId
     - the current protocolId
   * - [in]
     - roeCtrlPtr
     - the roe control Unit pointer
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [in]
     - eventWindowTime
     - the requested eventWindowTime
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

Dcm_UDS0x86_SetRoeStatus
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL void Dcm_UDS0x86_SetRoeStatus(Dcm_RoeStatusType RoeStatus)

set all roeStatus

**Sync/Async**
   TRUE

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
     - RoeStatus
     - the current roeStatus

**Return type**
   void

Dcm_UDS0x86_getRoePduIdAndProtocolId
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL void Dcm_UDS0x86_getRoePduIdAndProtocolId(Dcm_ProtocolType protocolType, PduIdType *roePduId, uint8 *protocolId)

get roe PduId and protocolId based on requested protocolType

**Sync/Async**
   TRUE

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
     - protocolType
     - the requested protocolType
   * - [out]
     - roePduId
     - the matched roePduId
   * - [out]
     - protocolId
     - the matched roe protocolId

**Return type**
   void

Dcm_UDS0x86_CheckService
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS0x86_CheckService(Dcm_ProtocolType protocolType, Dcm_RoeCtrlType *roeCtrl, uint8 *reqData, Dcm_MsgLenType reqDataLen, Dcm_NegativeResponseCodeType *ErrorCode)

check Service and subService for requested response service

**Sync/Async**
   TRUE

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
     - protocolType
     - the requested protocolType
   * - [in]
     - roeCtrl
     - the matched roeCtrl unit
   * - [in]
     - reqData
     - the requested service data
   * - [in]
     - reqDataLen
     - the requested service data len
   * - [out]
     - ErrorCode
     - the nrc to be sent

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful



Dcm_UDS0x86_TriggerServiceRequest
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Dcm_UDS0x86_TriggerServiceRequest(Dcm_RoeCtrlType *roeCtrlPtr)

called when DTC Status change or did written to trigger established service request

**Sync/Async**
   TRUE

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
     - roeCtrlPtr
     - the related roeCtrl unit

**Return type**
   void

Dcm_UDS_CheckMemoryCondition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS_CheckMemoryCondition(const Dcm_DspMemoryType *MemoryCfg, uint8 AddAndLenFid, Dcm_MsgLenType byteNumber, uint8 *addByteNumber, uint8 *LenByteNumber, Dcm_NegativeResponseCodeType *ErrorCode)

Verify memory request condition such as addAndLengthformatId and request length.

**Sync/Async**
   TRUE

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
     - MemoryCfg
     - the target memory configuration ptr
   * - [in]
     - AddAndLenFid
     - the requested address and length format id
   * - [in]
     - byteNumber
     - the requested byte number
   * - [out]
     - addByteNumber
     - the number of byte of address
   * - [out]
     - LenByteNumber
     - the number of byte of memory length
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was unsuccessful

Dcm_UDS_CheckMemoryRangeCheck
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS_CheckMemoryRangeCheck(const Dcm_DspMemoryType *MemoryCfg, uint8 memoryAccess, uint32 MemoryAddress, uint32 MemorySize, uint8 *MemoryIdentifier, const Dcm_DspMemoryRangeInfoType **targetMemoryInfo)

Verify requested memory is within the configuration.

**Sync/Async**
   TRUE

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
     - MemoryCfg
     - the target memory configuration ptr
   * - [in]
     - memoryAccess
     - read/write memory access
   * - [in]
     - MemoryAddress
     - the requested address
   * - [in]
     - MemorySize
     - the requested size
   * - [out]
     - MemoryIdentifier
     - configured memory Id
   * - [out]
     - targetMemoryInfo
     - the configured memory range info

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was unsuccessful

Dcm_UDS_FindMemoryRange
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS_FindMemoryRange(uint32 MemoryAddress, uint32 MemorySize, const Dcm_DspMemoryRangeInfoType *memoryInfo, uint16 infoNum, const Dcm_DspMemoryRangeInfoType **targetMemoryInfo)

find requested memory range info within the configuration

**Sync/Async**
   TRUE

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
     - MemoryAddress
     - the requested address
   * - [in]
     - MemorySize
     - the requested size
   * - [in]
     - memoryInfo
     - memoryInfo to search from
   * - [in]
     - infoNum
     - the number of memoryInfo
   * - [out]
     - targetMemoryInfo
     - the configured memory range info

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was unsuccessful

Dcm_UDS_CheckMemoryAuth
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS_CheckMemoryAuth(const Dcm_DspMemoryRangeInfoType *memoryRangeInfo, Dcm_NegativeResponseCodeType *ErrorCode)

check target memory range session/security/modeRule

**Sync/Async**
   TRUE

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
     - memoryRangeInfo
     - the requested memoryRangeInfo
   * - [out]
     - ErrorCode
     - the nrc to send

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was unsuccessful

Dcm_UDS_SignalHandleNvM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS_SignalHandleNvM(Dcm_ExtendedOpStatusType OpStatus, const Dcm_DspDataCfgType *dspData, uint8 *DestBuffer)

Calls NvM APIs to read data from nvm block.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - 
     - OpStatus
     - 
   * - 
     - dspData
     - 
   * - 
     - DestBuffer
     - 

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was unsuccessful

Dcm_UDS_SignalHandleDefault
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS_SignalHandleDefault(Dcm_ExtendedOpStatusType OpStatus, const Dcm_DspDataCfgType *dspData, uint8 *DestBuffer, uint16 *DataLength, Dcm_NegativeResponseCodeType *ErrorCode)

read data from signal using callouts(CS/SR/Callout)

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - 
     - OpStatus
     - 
   * - 
     - dspData
     - 
   * - 
     - DestBuffer
     - 
   * - 
     - DataLength
     - 
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was unsuccessful

Dcm_UDS_DynDidDefinedDID
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS_DynDidDefinedDID(Dcm_ExtendedOpStatusType OpStatus, uint16 ConnectionId, uint16 DDDIdIndex, uint8 index, Dcm_MsgLenType* offset, uint8* DestBuffer, Dcm_MsgLenType* BufSize, #if (STD_ON == DCM_DDDID_CHECK_SOURCE) boolean* checkFail, #endif, Dcm_NegativeResponseCodeType* ErrorCode);

prepare for reading dynamic did

**Sync/Async**
   Depending on Application

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
     - OpStatus
     - Indicates the current operation status
   * - [in]
     - ConnectionId
     - the current connection
   * - [in]
     - DDDIdIndex
     - the index of the dynamic defined did
   * - [in]
     - index
     - the index of the dynamic defined source did
   * - [inout]
     - offset
     - the input and resulting offset
   * - [out]
     - DestBuffer
     - the did's output data
   * - [inout]
     - BufSize
     - When the function is called this parameter contains the maximum number of data bytes that can be written to the buffer. The function returns the actual number of written data bytes in this parameter.
   * - [out]
     - checkFail
     - whether the source did check fails
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was unsuccessful
   * - DCM_E_PENDING
     - Request is not yet finished
   * - DCM_E_FORCE_RCRRP
     - Application request the transmission of a response Response Pending (NRC 0x78)

Dcm_UDS_DynDidDefinedDIDHandle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS_DynDidDefinedDIDHandle(Dcm_ExtendedOpStatusType OpStatus, uint16 DDDIdIndex, uint8 index, Dcm_MsgLenType *offset, uint8 *DestBuffer, Dcm_MsgLenType *BufSize, Dcm_NegativeResponseCodeType *ErrorCode)

read dynamic did that is defined by source did

**Sync/Async**
   Depending on Application

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
     - OpStatus
     - Indicates the current operation status
   * - [in]
     - DDDIdIndex
     - the index of the dynamic defined did
   * - [in]
     - index
     - the index of the dynamic defined source did
   * - [inout]
     - offset
     - the input and resulting offset
   * - [out]
     - DestBuffer
     - the did's output data
   * - [inout]
     - BufSize
     - When the function is called this parameter contains the maximum number of data bytes that can be written to the buffer. The function returns the actual number of written data bytes in this parameter.
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was unsuccessful
   * - DCM_E_PENDING
     - Request is not yet finished
   * - DCM_E_FORCE_RCRRP
     - Application request the transmission of a response Response Pending (NRC 0x78)

Dcm_UDS_DynDidDefinedAdd
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    DCM_LOCAL Std_ReturnType Dcm_UDS_DynDidDefinedAdd(Dcm_ExtendedOpStatusType OpStatus, uint16 DDDIdIndex, uint8 index, Dcm_MsgLenType *offset, uint8 *DestBuffer, Dcm_MsgLenType *BufSize, Dcm_NegativeResponseCodeType *ErrorCode)

read dynamic did that is defined by memory address and memory size

**Sync/Async**
   Depending on Application

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
     - OpStatus
     - Indicates the current operation status
   * - [in]
     - DDDIdIndex
     - the index of the dynamic defined did
   * - [in]
     - index
     - the index of the dynamic defined source did
   * - 
     - offset
     - 
   * - [out]
     - DestBuffer
     - the did's output data
   * - [inout]
     - BufSize
     - When the function is called this parameter contains the maximum number of data bytes that can be written to the buffer. The function returns the actual number of written data bytes in this parameter.
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was unsuccessful
   * - DCM_E_PENDING
     - Request is not yet finished
   * - DCM_E_FORCE_RCRRP
     - Application request the transmission of a response Response Pending (NRC 0x78)

Dcm_UDS0x10
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dcm_UDS0x10(Dcm_ExtendedOpStatusType OpStatus, Dcm_MsgContextType *pMsgContext, Dcm_NegativeResponseCodeType *ErrorCode)

The service interpreter for UDS 0x10.

**Sync/Async**
   Depending on Session Type and current session level

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
     - OpStatus
     - Indicates the current operation status
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful
   * - DCM_E_PENDING
     - Request is not yet finished
   * - DCM_E_FORCE_RCRRP
     - Application requests the transmission of a response Response Pending (NRC 0x78)

Dcm_UDS0x10_CheckTimer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Dcm_UDS0x10_CheckTimer(void)

Called by Dcm_MainFunction/DcmInternal_CheckTimer to deal with session timer.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant


**Return type**
   void

Dcm_UDS0x10_SessionChange
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Dcm_UDS0x10_SessionChange(void)

Called by Dcm_TpTxConfirmation for 0x10 service postivie response confirmation and ResetToDefaultSession to change the session.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant


**Return type**
   void

Dcm_UDS0x10_CheckSession
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dcm_UDS0x10_CheckSession(const Dcm_SesCtrlType *session, uint8 sessionNum, Dcm_NegativeResponseCodeType *ErrorCode)

Called by DsdInternal_RxIndication to check general service/subService session and most of th UDS services to check did, rid, memory, etc. session.

**Sync/Async**
   TRUE

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
     - session
     - the required session
   * - [in]
     - sessionNum
     - the required session num
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

Dcm_UDS0x11
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dcm_UDS0x11(Dcm_ExtendedOpStatusType OpStatus, Dcm_MsgContextType *pMsgContext, Dcm_NegativeResponseCodeType *ErrorCode)

The service interpreter for UDS 0x11.

**Sync/Async**
   Depending on Configuration DcmSendRespPendOnRestart

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
     - OpStatus
     - Indicates the current operation status
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful
   * - DCM_E_PENDING
     - Request is not yet finished
   * - DCM_E_FORCE_RCRRP
     - Application requests the transmission of a response Response Pending (NRC 0x78)

Dcm_UDS0x14
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dcm_UDS0x14(Dcm_ExtendedOpStatusType OpStatus, Dcm_MsgContextType *pMsgContext, Dcm_NegativeResponseCodeType *ErrorCode)

The service interpreter for UDS 0x14.

**Sync/Async**
   Depending on Dem

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
     - OpStatus
     - Indicates the current operation status
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful
   * - DCM_E_PENDING
     - Request is not yet finished

Dcm_UDS0x19
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dcm_UDS0x19(Dcm_ExtendedOpStatusType OpStatus, Dcm_MsgContextType *pMsgContext, Dcm_NegativeResponseCodeType *ErrorCode)

The service interpreter for UDS 0x19.

**Sync/Async**
   Depending on Dem

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
     - OpStatus
     - Indicates the current operation status
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful
   * - DCM_E_PENDING
     - Request is not yet finished

Dcm_UDS0x22
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dcm_UDS0x22(Dcm_ExtendedOpStatusType OpStatus, Dcm_MsgContextType *pMsgContext, Dcm_NegativeResponseCodeType *ErrorCode)

The service interpreter for UDS 0x22.

**Sync/Async**
   Depending on Application

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
     - OpStatus
     - Indicates the current operation status
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful
   * - DCM_E_PENDING
     - Request is not yet finished
   * - DCM_E_FORCE_RCRRP
     - Application requests the transmission of a response Response Pending (NRC 0x78)

Dcm_UDS0x23
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dcm_UDS0x23(Dcm_ExtendedOpStatusType OpStatus, Dcm_MsgContextType *pMsgContext, Dcm_NegativeResponseCodeType *ErrorCode)

The service interpreter for UDS 0x23.

**Sync/Async**
   Depending on Application

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
     - OpStatus
     - Indicates the current operation status
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful
   * - DCM_E_PENDING
     - Request is not yet finished
   * - DCM_E_FORCE_RCRRP
     - Application request the transmission of a response Response Pending (NRC 0x78)

Dcm_UDS0x24
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dcm_UDS0x24(Dcm_ExtendedOpStatusType OpStatus, Dcm_MsgContextType *pMsgContext, Dcm_NegativeResponseCodeType *ErrorCode)

The service interpreter for UDS 0x24.

**Sync/Async**
   Depending on Application

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
     - OpStatus
     - Indicates the current operation status
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful
   * - DCM_E_PENDING
     - Request is not yet finished

Dcm_UDS0x27
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dcm_UDS0x27(Dcm_ExtendedOpStatusType OpStatus, Dcm_MsgContextType *pMsgContext, Dcm_NegativeResponseCodeType *ErrorCode)

The service interpreter for UDS 0x27.

**Sync/Async**
   Depending on Application

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
     - OpStatus
     - Indicates the current operation status
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful
   * - DCM_E_PENDING
     - Request is not yet finished

Dcm_UDS0x27_CheckSecurity
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dcm_UDS0x27_CheckSecurity(const Dcm_SecLevelType *security, uint8 securityNum, Dcm_NegativeResponseCodeType *ErrorCode)

This function checks whether the current security State is supported.

**Sync/Async**
   TRUE

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
     - security
     - the requested security
   * - [in]
     - securityNum
     - the requested security number
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

Dcm_UDS0x27_CheckTimer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Dcm_UDS0x27_CheckTimer(void)

This function checks the security timer and decrease counter.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant


**Return type**
   void

Dcm_UDS0x27_SetAttemptCounter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Dcm_UDS0x27_SetAttemptCounter(Dcm_OpStatusType OpStatus, uint8 securityIndex, uint8 attemptCounter)

This function calls the SetAttemptCounterFnc and actually sets the attemptCounter.

**Sync/Async**
   TRUE

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
     - OpStatus
     - Indicates the current operation status
   * - [in]
     - securityIndex
     - the cofigured securityRow index
   * - [in]
     - attemptCounter
     - the input attemptCounter to set

**Return type**
   void

Dcm_UDS0x27_GetAttemptCounter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Dcm_UDS0x27_GetAttemptCounter(void)

This function is called by Dcm_MainFunction to process the getAttemptCounter.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant


**Return type**
   void

Dcm_UDS0x27_SetAttemptCounterHandle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Dcm_UDS0x27_SetAttemptCounterHandle(void)

This function is called by Dcm_MainFunction to process the setAttemptCounter.

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant


**Return type**
   void

Dcm_UDS0x31
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dcm_UDS0x31(Dcm_ExtendedOpStatusType OpStatus, Dcm_MsgContextType *pMsgContext, Dcm_NegativeResponseCodeType *ErrorCode)

The service interpreter for UDS 0x31.

**Sync/Async**
   Depending on Application

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
     - OpStatus
     - Indicates the current operation status
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful
   * - DCM_E_PENDING
     - Request is not yet finished

Dcm_UDS0x34
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dcm_UDS0x34(Dcm_ExtendedOpStatusType OpStatus, Dcm_MsgContextType *pMsgContext, Dcm_NegativeResponseCodeType *ErrorCode)

The service interpreter for UDS 0x34.

**Sync/Async**
   Depending on Application

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
     - OpStatus
     - Indicates the current operation status
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful
   * - DCM_E_PENDING
     - Request is not yet finished

Dcm_UDS0x35
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dcm_UDS0x35(Dcm_ExtendedOpStatusType OpStatus, Dcm_MsgContextType *pMsgContext, Dcm_NegativeResponseCodeType *ErrorCode)

The service interpreter for UDS 0x35.

**Sync/Async**
   Depending on Application

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
     - OpStatus
     - Indicates the current operation status
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful
   * - DCM_E_PENDING
     - Request is not yet finished

Dcm_UDS0x37
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dcm_UDS0x37(Dcm_ExtendedOpStatusType OpStatus, Dcm_MsgContextType *pMsgContext, Dcm_NegativeResponseCodeType *ErrorCode)

The service interpreter for UDS 0x37.

**Sync/Async**
   Depending on Application

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
     - OpStatus
     - Indicates the current operation status
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful
   * - DCM_E_PENDING
     - Request is not yet finished

Dcm_UDS0x38
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dcm_UDS0x38(Dcm_ExtendedOpStatusType OpStatus, Dcm_MsgContextType *pMsgContext, Dcm_NegativeResponseCodeType *ErrorCode)

The service interpreter for UDS 0x38.

**Sync/Async**
   Depending on Application

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
     - OpStatus
     - Indicates the current operation status
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful
   * - DCM_E_PENDING
     - Request is not yet finished
   * - DCM_E_FORCE_RCRRP
     - Application requests the transmission of a response Response Pending (NRC 0x78)

Dcm_UDS0x85
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dcm_UDS0x85(Dcm_ExtendedOpStatusType OpStatus, Dcm_MsgContextType *pMsgContext, Dcm_NegativeResponseCodeType *ErrorCode)

The service interpreter for UDS 0x85.

**Sync/Async**
   Depending on Dem

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
     - OpStatus
     - Indicates the current operation status
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful
   * - DCM_E_PENDING
     - Request is not yet finished

Dcm_UDS0x85_EnableDTCSetting
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Dcm_UDS0x85_EnableDTCSetting(void)

enables the DTC setting (session change or 85 req)

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant


**Return type**
   void

Dcm_UDS0x85_MainFunction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Dcm_UDS0x85_MainFunction(void)

enables the DTC setting when mode rule fails

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant


**Return type**
   void

Dcm_UDS0x86
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dcm_UDS0x86(Dcm_ExtendedOpStatusType OpStatus, Dcm_MsgContextType *pMsgContext, Dcm_NegativeResponseCodeType *ErrorCode)

The service interpreter for UDS 0x86.

**Sync/Async**
   TRUE

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
     - OpStatus
     - Indicates the current operation status
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

Dcm_UDS0x2A
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dcm_UDS0x2A(Dcm_ExtendedOpStatusType OpStatus, Dcm_MsgContextType *pMsgContext, Dcm_NegativeResponseCodeType *ErrorCode)

The service interpreter for UDS 0x2A.

**Sync/Async**
   Depending on Application

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
     - OpStatus
     - Indicates the current operation status
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful
   * - DCM_E_PENDING
     - Request is not yet finished

Dcm_UDS0x2A_MainFunction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Dcm_UDS0x2A_MainFunction(void)

Called by Dcm_MainFunction to deal with 2A scheduler counter and message sending.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant


**Return type**
   void

Dcm_UDS0x2A_StatusChangeHandle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Dcm_UDS0x2A_StatusChangeHandle(void)

Called by UDS 0x10, 0x29 and 0x27 to notify the session/security/authenticationState change so as to check the access right again. Stop the periodic transmission if access right is lost.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant


**Return type**
   void

Dcm_UDS0x2C
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dcm_UDS0x2C(Dcm_ExtendedOpStatusType OpStatus, Dcm_MsgContextType *pMsgContext, Dcm_NegativeResponseCodeType *ErrorCode)

The service interpreter for UDS 0x2C.

**Sync/Async**
   TRUE

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
     - OpStatus
     - Indicates the current operation status
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

Dcm_UDS0x2E
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dcm_UDS0x2E(Dcm_ExtendedOpStatusType OpStatus, Dcm_MsgContextType *pMsgContext, Dcm_NegativeResponseCodeType *ErrorCode)

The service interpreter for UDS 0x2E.

**Sync/Async**
   Depending on Application

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
     - OpStatus
     - Indicates the current operation status
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful
   * - DCM_E_PENDING
     - Request is not yet finished

Dcm_UDS0x2E_WriteDspData
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dcm_UDS0x2E_WriteDspData(Dcm_ExtendedOpStatusType OpStatus, const Dcm_DspDidType *DcmDspDidCfg, const uint8 *reqData, Dcm_MsgLenType reqDataLen, Dcm_NegativeResponseCodeType *ErrorCode)

Called to write did data.

**Sync/Async**
   Depending on Application

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
     - OpStatus
     - Indicates the current operation status
   * - [in]
     - DcmDspDidCfg
     - the DcmDspDid configuration
   * - [in]
     - reqData
     - the requested data to write
   * - [in]
     - reqDataLen
     - the requested data length to write
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful
   * - DCM_E_PENDING
     - Request is not yet finished

Dcm_UDS0x2E_Init
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Dcm_UDS0x2E_Init(void)

Called by Dcm_Init to initialize secure coding did offset.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant


**Return type**
   void

Dcm_UDS0x2F
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dcm_UDS0x2F(Dcm_ExtendedOpStatusType OpStatus, Dcm_MsgContextType *pMsgContext, Dcm_NegativeResponseCodeType *ErrorCode)

The service interpreter for UDS 0x2F.

**Sync/Async**
   Depending on Application

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
     - OpStatus
     - Indicates the current operation status
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful
   * - DCM_E_PENDING
     - Request is not yet finished

Dcm_UDS0x2F_StatusChangeHandle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Dcm_UDS0x2F_StatusChangeHandle(void)

Called by UDS 0x2F and 0x10 to notify session/security/authenticationState change and call returnControlToEcu accordingly if it is no long supported in current status.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant


**Return type**
   void

Dcm_UDS_CheckMemory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dcm_UDS_CheckMemory(const Dcm_DspMemoryType *MemoryCfg, uint8 AddAndLenFid, Dcm_MsgLenType byteNumber, uint8 *reqData, uint8 *MemoryIdentifier, uint32 *MemoryAddress, uint32 *MemorySize, uint8 memoryAccess, Dcm_NegativeResponseCodeType *ErrorCode)

Called by UDS 0x2C, 0x3D, 0x23, 0x34, 0x35 to check whether the input memoryAdd and memorySize is valid.

**Sync/Async**
   TRUE

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
     - MemoryCfg
     - the target memory configuration ptr
   * - [in]
     - AddAndLenFid
     - the requested address and length format id
   * - [in]
     - byteNumber
     - the requested address and length format id
   * - [in]
     - reqData
     - the input request data
   * - [out]
     - MemoryIdentifier
     - the configured memoryIdentifier (if available)
   * - [out]
     - MemoryAddress
     - the extracted memoryAddress from input data
   * - [out]
     - MemorySize
     - the extracted MemorySize from input data
   * - 
     - memoryAccess
     - 
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was unsuccessful

Dcm_UDS_SetBlockLength
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Dcm_UDS_SetBlockLength(uint32 BlockLength, uint8 *ResData, Dcm_MsgLenType *ResDataLen)

Called by UDS 0x34, 0x35 to set the lengthFormatIdentifier and blockLength to resData accordingly.

**Sync/Async**
   TRUE

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
     - BlockLength
     - the input blockLength
   * - [out]
     - ResData
     - the output data
   * - [out]
     - ResDataLen
     - the response data length

**Return type**
   void

Dcm_UDS0x36
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dcm_UDS0x36(Dcm_ExtendedOpStatusType OpStatus, Dcm_MsgContextType *pMsgContext, Dcm_NegativeResponseCodeType *ErrorCode)

The service interpreter for UDS 0x36.

**Sync/Async**
   Depending on Application

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
     - OpStatus
     - Indicates the current operation status
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful
   * - DCM_E_PENDING
     - Request is not yet finished
   * - DCM_E_FORCE_RCRRP
     - Application requests the transmission of a response Response Pending (NRC 0x78)

Dcm_UDS_InitTransferData
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Dcm_UDS_InitTransferData(Dcm_TransferStatusType transferStatus, uint8 memoryIdentifier, uint32 memoryAddress, uint32 blockLength, uint32 memorySize)

Called by UDS 0x34, 0x35 and 0x37 to initialize transferData status.

**Sync/Async**
   TRUE

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
     - transferStatus
     - current transfer status
   * - [in]
     - memoryIdentifier
     - configured memory id
   * - [in]
     - memoryAddress
     - input memory address
   * - [in]
     - blockLength
     - max blockLength returned by callout
   * - [in]
     - memorySize
     - input memory size

**Return type**
   void

Dcm_UDS0x3D
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dcm_UDS0x3D(Dcm_ExtendedOpStatusType OpStatus, Dcm_MsgContextType *pMsgContext, Dcm_NegativeResponseCodeType *ErrorCode)

The service interpreter for UDS 0x3D.

**Sync/Async**
   Depending on Application

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
     - OpStatus
     - Indicates the current operation status
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful
   * - DCM_E_PENDING
     - Request is not yet finished
   * - DCM_E_FORCE_RCRRP
     - Application requests the transmission of a response Response Pending (NRC 0x78)

Dcm_UDS0x3E
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dcm_UDS0x3E(Dcm_ExtendedOpStatusType OpStatus, Dcm_MsgContextType *pMsgContext, Dcm_NegativeResponseCodeType *ErrorCode)

The service interpreter for UDS 0x3E.

**Sync/Async**
   TRUE

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
     - OpStatus
     - Indicates the current operation status
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

Dcm_UDS_CheckReadWriteDid
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dcm_UDS_CheckReadWriteDid(uint16 ConnectionId, uint16 Did, const Dcm_DspDidReadWriteType *DcmDspDidReadWrite, Dcm_NegativeResponseCodeType *ErrorCode)

Called by UDS 0x22, 0x24, 0x2A, 0x2C and 0x2E to check whether this did is supported to read/write in the current session/security/mode/authenticationState.

**Sync/Async**
   TRUE

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
     - ConnectionId
     - the current connectionId
   * - [in]
     - Did
     - the input did
   * - [out]
     - DcmDspDidReadWrite
     - did's read/write configuration
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was unsuccessful

Dcm_UDS_FindDid
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dcm_UDS_FindDid(uint16 Did, Dcm_DidType *didType, uint16 *DidIndex, Dcm_NegativeResponseCodeType *ErrorCode)

This function gets the configured did index, also applying to rangeDid and OBDDid.

**Sync/Async**
   TRUE

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
     - Did
     - the input did
   * - [out]
     - didType
     - the type of did
   * - [out]
     - DidIndex
     - the did configuration index
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was unsuccessful

Dcm_UDS_SignalHandle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dcm_UDS_SignalHandle(Dcm_ExtendedOpStatusType OpStatus, uint16 DidIndex, uint8 *DestBuffer, uint16 *DataLength, Dcm_NegativeResponseCodeType *ErrorCode)

Called by UDS 0x22/0x2A/0x2F to read data in did's signals.

**Sync/Async**
   Depending on Application

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
     - OpStatus
     - Indicates the current operation status
   * - [in]
     - DidIndex
     - the input did index
   * - [out]
     - DestBuffer
     - address to output the signal data
   * - [out]
     - DataLength
     - the data length of did (only for dynamic ones)
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was unsuccessful
   * - DCM_E_PENDING
     - Request is not yet finished

Dcm_UDS_DidReadHandle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dcm_UDS_DidReadHandle(Dcm_ExtendedOpStatusType OpStatus, uint16 DidIndex, uint8 *DestBuffer, Dcm_MsgLenType *BufSize, Dcm_NegativeResponseCodeType *ErrorCode)

Called by UDS 0x22 to read data in did's signals.

**Sync/Async**
   Depending on Application

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
     - OpStatus
     - Indicates the current operation status
   * - [in]
     - DidIndex
     - the input did index
   * - [out]
     - DestBuffer
     - address to output the signal data
   * - [inout]
     - BufSize
     - When the function is called this parameter contains the maximum number of data bytes that can be written to the buffer. The function returns the actual number of written data bytes in this parameter.
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was unsuccessful
   * - DCM_E_PENDING
     - Request is not yet finished

Dcm_UDS_DynDidHandle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dcm_UDS_DynDidHandle(Dcm_ExtendedOpStatusType OpStatus, uint16 ConnectionId, uint16 DDDIdIndex, uint8 *DestBuffer, Dcm_MsgLenType *BufSize, #if(STD_ON==DCM_DDDID_CHECK_SOURCE) boolean *checkFail, #endif Dcm_NegativeResponseCodeType *ErrorCode)

Called by UDS 0x22 and 0x2A to read data of a dynamic did.

**Sync/Async**
   Depending on Application

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
     - OpStatus
     - Indicates the current operation status
   * - [in]
     - ConnectionId
     - the current connection
   * - [in]
     - DDDIdIndex
     - the index of the dynamic defined did
   * - [out]
     - DestBuffer
     - the did's output data
   * - [inout]
     - BufSize
     - When the function is called this parameter contains the maximum number of data bytes that can be written to the buffer. The function returns the actual number of written data bytes in this parameter.
   * - [out]
     - checkFail
     - whether the source did check fails
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was unsuccessful
   * - DCM_E_PENDING
     - Request is not yet finished
   * - DCM_E_FORCE_RCRRP
     - Application request the transmission of a response Response Pending (NRC 0x78)

Dcm_UDS0x86_Init
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Dcm_UDS0x86_Init(void)

called by Dcm_Init to initialize roe status, only apply for nvm stored roe data

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant


**Return type**
   void

Dcm_UDS0x86_TriggerServiceRequest
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Dcm_UDS0x86_TriggerServiceRequest(Dcm_RoeCtrlType *roeCtrlPtr)

called when DTC Status change or did written to trigger established service request

**Sync/Async**
   TRUE

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
     - roeCtrlPtr
     - the related roeCtrl unit

**Return type**
   void

Dcm_UDS0x86_CheckTimer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Dcm_UDS0x86_CheckTimer(void)

called by Dcm_MainFunction to check scheduler rate

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant


**Return type**
   void

Dcm_UDS0x28
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dcm_UDS0x28(Dcm_ExtendedOpStatusType OpStatus, Dcm_MsgContextType *pMsgContext, Dcm_NegativeResponseCodeType *ErrorCode)

The service interpreter for UDS 0x28.

**Sync/Async**
   TRUE

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
     - OpStatus
     - Indicates the current operation status
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

Dcm_UDS0x28_TxConfirmation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Dcm_UDS0x28_TxConfirmation(uint16 ConnectionId)

This function switch the comMode and calls the releated function when txConfirmation.

**Sync/Async**
   TRUE

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
     - ConnectionId
     - the current connectionId

**Return type**
   void

Dcm_UDS0x28_SessionChange
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Dcm_UDS0x28_SessionChange(void)

This function is called when session is changed and it enables the communication accordingly.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant


**Return type**
   void

Dcm_UDS0x28_MainFunction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Dcm_UDS0x28_MainFunction(void)

This function is called by Dcm_MainFunction when UDS 0x28 is configured with modeRule, it checks whether the mode rule is no longer effective and enables the communication again.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant


**Return type**
   void

Dcm_UDS0x29
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dcm_UDS0x29(Dcm_ExtendedOpStatusType OpStatus, Dcm_MsgContextType *pMsgContext, Dcm_NegativeResponseCodeType *ErrorCode)

The service interpreter for UDS 0x29.

**Sync/Async**
   TRUE

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
     - OpStatus
     - Indicates the current operation status
   * - [inout]
     - pMsgContext
     - Message-related information for one diagnostic protocol identifier. The pointers in pMsgContext shall point behind the SID.
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

Dcm_UDS0x29_Init
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Dcm_UDS0x29_Init(void)

This function initialize the variables used by UDS 0x29.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant


**Return type**
   void

Dcm_UDS0x29_MainFunction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Dcm_UDS0x29_MainFunction(void)

called by Dcm_MainFunction to handle timer

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant


**Return type**
   void

Dcm_UDS0x29_AuthenticationCheck
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dcm_UDS0x29_AuthenticationCheck(uint16 ConnectionId, const uint8 *subRoleRef, uint8 subRoleRefNum, Dcm_NegativeResponseCodeType *ErrorCode)

called by DsdInternal_RxIndication to verify service and subfunction authentication

**Sync/Async**
   TRUE

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
     - ConnectionId
     - the current connection
   * - [in]
     - subRoleRef
     - the input role ref
   * - [in]
     - subRoleRefNum
     - the number of input role ref
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request was successful
   * - E_NOT_OK
     - Request was not successful

Dcm_UDS0x29_SetDeAuthenticate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Dcm_UDS0x29_SetDeAuthenticate(uint16 ConnectionId)

This function switches the authenticationStatus to DCM_DEAUTHENTICATED and restore status accordingly.

**Sync/Async**
   TRUE

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
     - ConnectionId
     - the current connectionId

**Return type**
   void

Dcm_UDS0x29_SetAuthenticationCtrlOn
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Dcm_UDS0x29_SetAuthenticationCtrlOn(uint16 ConnectionId)

This function is called by Dcm_TpTxConfirmation to actually set the authenticationState on.

**Sync/Async**
   TRUE

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
     - ConnectionId
     - the current connection Id

**Return type**
   void

Dcm_UDS0x29_SetAuthenticationCtrlOff
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Dcm_UDS0x29_SetAuthenticationCtrlOff(uint16 ConnectionId)

This function is called by Dcm_StartOfReception to actually set the authenticationState off.

**Sync/Async**
   TRUE

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
     - ConnectionId
     - the current connection Id

**Return type**
   void

Dcm_UDS0x29_DidAuthenticationCheck
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dcm_UDS0x29_DidAuthenticationCheck(uint16 ConnectionId, uint16 Did, const Dcm_DspDidReadWriteType *didReadWrite, const Dcm_DspDidControlType *didControl, Dcm_NegativeResponseCodeType *ErrorCode)

called by UDS 0x22, 0x24, 0x2A, 0x2C, 0x2E, 0x2F to check did authentication

**Sync/Async**
   TRUE

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
     - ConnectionId
     - the current connection
   * - [in]
     - Did
     - the input did
   * - [in]
     - didReadWrite
     - the input did read/write info
   * - [in]
     - didControl
     - the input did control info
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType

Dcm_UDS0x29_RidAuthenticationCheck
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dcm_UDS0x29_RidAuthenticationCheck(uint16 ConnectionId, uint16 RoutineCfgIdx, Dcm_NegativeResponseCodeType *ErrorCode)

called by UDS 0x31 to check rid authentication

**Sync/Async**
   TRUE

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
     - ConnectionId
     - the current connection
   * - [in]
     - RoutineCfgIdx
     - the target rid configuration index
   * - [out]
     - ErrorCode
     - If the operation <Module>_<DiagnosticService> returns value E_NOT_OK, the Dcm module shall send a negative response with NRC code equal to the parameter ErrorCode parameter value.

**Return type**
   Std_ReturnType
