
类型定义（Type definition）
---------------------------------
.. 如果没有就不存在该章节，或为None

None

      
提供的服务（Provided services）
--------------------------------------
Dem_GetVersionInfo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Dem_GetVersionInfo(Std_VersionInfoType *versionInfo)

Returns the version information of this module. API Availability: This API will be available only if ({ecuc(Dem/DemGeneral.DemVersionInfoApi)} == true)

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


Dem_PreInit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Dem_PreInit(const Dem_ConfigType *ConfigPtr)

Initializes the internal states necessary to process events reported by BSW-modules.

**Sync/Async**
   Synchronous

**Reentrancy**
   Non Reentrant


**Return type**
   void


Dem_Init
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Dem_Init(const Dem_ConfigType *ConfigPtr)

Initializes or reinitializes this module.

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
     - ConfigPtr
     - Pointer to the configuration set in VARIANT-POST-BUILD.

**Return type**
   void


Dem_Shutdown
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Dem_Shutdown(void)

Shuts down this module.

**Sync/Async**
   Synchronous

**Reentrancy**
   Non Reentrant


**Return type**
   void


Dem_ClearDTC
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_ClearDTC(uint8 ClientId)

Clears single DTCs, as well as groups of DTCs.

**Sync/Async**
   Asynchronous

**Reentrancy**
   Reentrant for different ClientIds, non reentrant for the same ClientId.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - ClientId
     - Unique client id, assigned to the instance of the calling module.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - DTC successfully cleared
   * - E_NOT_OK
     - No DTC selected
   * - DEM_WRONG_DTC
     - Selected DTC value in selected format does not exist or clearing is restricted by configuration to group of all DTCs only.
   * - DEM_WRONG_DTCORIGIN
     - Selected DTCOrigin does not exist
   * - DEM_CLEAR_FAILED
     - DTC clearing failed
   * - DEM_CLEAR_BUSY
     - Another client is currently clearing DTCs. The requested operation will not be started and the caller shall try again at a later moment.
   * - DEM_CLEAR_MEMORY_ERROR
     - An error occurred during erasing a memory location (e.g. if DemClearDTCBehavior is set to DEM_CLRRESP_NON-VOLATILE_FINISH and erasing of non-volatile-block failed).
   * - DEM_PENDING
     - Clearing the DTCs is currently in progress. The caller shall call this function again at a later moment.
   * - DEM_BUSY
     - A different Dem_SelectDTC dependent operation according to SWS_Dem_01253 of this client is currently in progress.

Dem_ClearPrestoredFreezeFrame
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_ClearPrestoredFreezeFrame(Dem_EventIdType EventId)

Clears a prestored freeze frame of a specific event. This API can only be used through the RTE and therefore no declaration is exported via

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant for different EventIds. Non reentrant for the same EventId.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - EventId
     - Identification of an event by assigned EventId.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Clear prestored freeze frame was successful
   * - E_NOT_OK
     - Clear prestored freeze frame failed

Dem_GetComponentFailed
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_GetComponentFailed(Dem_ComponentIdType ComponentId, boolean *ComponentFailed)

Gets the failed status of a DemComponent.

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
     - ComponentId
     - Identification of a DemComponent
   * - [out]
     - ComponentFailed
     - TRUE: failed FALSE: not failed

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - getting "ComponentFailed" was successful
   * - E_NOT_OK
     - getting "ComponentFailed" was not successful

Dem_GetDTCSelectionResult
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_GetDTCSelectionResult(uint8 ClientId)

Provides information if the last call to Dem_SelectDTC has selected a valid DTC or group of DTCs.

**Sync/Async**
   Asynchronous

**Reentrancy**
   Reentrant for different ClientIds, non reentrant for the same ClientId.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - ClientId
     - Unique client id, assigned to the instance of the calling module.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The DTC select parameter check is successful and the requested DTC or group of DTC in the selected origin is selected for further operations.
   * - E_NOT_OK
     - No DTC selected
   * - DEM_WRONG_DTC
     - Selected DTC value in selected format does not exist
   * - DEM_WRONG_DTCORIGIN
     - Selected DTCOrigin does not exist
   * - DEM_PENDING
     - Checking the SelectDTC parameters is currently in progress. The caller shall call this function again later.
   * - DEM_BUSY
     - A different Dem_SelectDTC dependent operation according to SWS_Dem_01253 of this client is currently in progress.

Dem_GetDTCSelectionResultForClearDTC
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_GetDTCSelectionResultForClearDTC(uint8 ClientId)

Provides information if the last call to Dem_SelectDTC has selected a valid DTC or group of DTCs, respecting the settings if the Dem shall clear only all DTCs.

**Sync/Async**
   Asynchronous

**Reentrancy**
   Reentrant for different ClientIds, non reentrant for the same ClientId.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - ClientId
     - Unique client id, assigned to the instance of the calling module.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The DTC select parameter check is successful and the requested DTC or group of DTC in the selected origin is selected for further operations.
   * - E_NOT_OK
     - No DTC selected
   * - DEM_WRONG_DTC
     - Selected DTC value in selected format does not exist
   * - DEM_WRONG_DTCORIGIN
     - Selected DTCOrigin does not exist
   * - DEM_PENDING
     - Checking the SelectDTC parameters is currently in progress. The caller shall call this function again later.
   * - DEM_BUSY
     - A different Dem_SelectDTC dependent operation according to SWS_Dem_01253 of this client is currently in progress.

Dem_GetEventUdsStatus
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_GetEventUdsStatus(Dem_EventIdType EventId, Dem_UdsStatusByteType *UDSStatusByte)

Gets the current UDS status byte assigned to the DTC for the event.

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
     - EventId
     - Identification of an event by assigned EventId.
   * - [out]
     - UDSStatusByte
     - UDS DTC status byte of the requested event (refer to chapter "Status bit
                              support"). If the return value of the function call is E_NOT_OK, this parameter does not contain valid data.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - get of event status was successful
   * - E_NOT_OK
     - get of event status failed

Dem_GetMonitorStatus
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_GetMonitorStatus(Dem_EventIdType EventID, Dem_MonitorStatusType *MonitorStatus)

Gets the current monitor status for an event.

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
   * - 
     - EventID
     - 
   * - [out]
     - MonitorStatus
     - Monitor status byte of the requested event. If the return value of the function call is E_NOT_OK, this parameter does not contain valid data.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - get monitor status was successful
   * - E_NOT_OK
     - get the monitor status failed

Dem_GetDebouncingOfEvent
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_GetDebouncingOfEvent(Dem_EventIdType EventId, Dem_DebouncingStateType *DebouncingState)

Gets the debouncing status of an event. This function shall not be used for EventId with native debouncing within their functions. It is rather for EventIds using debouncing within the Dem.

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
     - EventId
     - Identification of an event by assigned EventId.
   * - [out]
     - DebouncingState
     - Bit 0 Temporarily Defective (corresponds to 0 < FDC < 127) Bit 1 finally Defective (corresponds to FDC = 127) Bit 2 temporarily healed (corresponds to -128 < FDC < 0) Bit 3 Test complete (corresponds to FDC = -128 or FDC = 127) Bit 4 DTR Update (= Test complete && Debouncing complete && enable conditions / storage conditions fulfilled)

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - get of debouncing status per event state successful
   * - E_NOT_OK
     - get of debouncing per event state failed

Dem_GetDTCOfEvent
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_GetDTCOfEvent(Dem_EventIdType EventId, Dem_DTCFormatType DTCFormat, uint32 *DTCOfEvent)

Gets the DTC of an event.

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
     - EventId
     - Identification of an event by assigned EventId.
   * - [in]
     - DTCFormat
     - Defines the output-format of the requested DTC value.
   * - [out]
     - DTCOfEvent
     - Receives the DTC value in respective format returned by this function. If the return value of the function is other than E_OK this parameter does not contain valid data.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - get of DTC was successful
   * - E_NOT_OK
     - the call was not successful
   * - DEM_E_NO_DTC_AVAILABLE
     - there is no DTC configured in the requested format

Dem_GetDTCSuppression
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_GetDTCSuppression(uint8 ClientId, boolean *SuppressionStatus)

Returns the suppression status of a specific DTC. API Availability: This API will be available only if ({ecuc(Dem/DemGeneral.DemSuppressionSupport)} == DEM_DTC_SUPPRESSION)

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
     - ClientId
     - Unique client id, assigned to the instance of the calling module
   * - [out]
     - SuppressionStatus
     - Defines whether the respective DTC is suppressed (TRUE) or enabled (FALSE).

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Operation was successful.
   * - E_NOT_OK
     - Dem_SelectDTC was not called.
   * - DEM_WRONG_DTC
     - No valid DTC or DTC group selected.
   * - DEM_WRONG_DTCORIGIN
     - Wrong DTC origin selected.
   * - DEM_PENDING
     - The requested value is calculated asynchronously and currently not available. The caller can retry later.
   * - DEM_BUSY
     - A different Dem_SelectDTC dependent operation according to SWS_Dem_01253 of this client is currently in progress.

Dem_GetEventAvailable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_GetEventAvailable(Dem_EventIdType EventId, boolean *AvailableStatus)

Get the Event availability.

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
     - EventId
     - Identification of an event by assigned EventId.
   * - [out]
     - AvailableStatus
     - TRUE if the event is available. FALSE if the event is not available.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Event availability has been obtained.
   * - E_NOT_OK
     - Event availability cannot be obtained.

Dem_GetFaultDetectionCounter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_GetFaultDetectionCounter(Dem_EventIdType EventId, sint8 *FaultDetectionCounter)

Gets the fault detection counter of an event. This API can only be used through the RTE, and therefore no declaration is exported via

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
     - EventId
     - Identification of an event by assigned EventId.
   * - [out]
     - FaultDetectionCounter
     - This parameter receives the Fault Detection Counter information of the requested EventId. If the return value of the function call is other than E_OK this parameter does not contain valid data. -128dec...127dec PASSED...FAILED according to ISO 14229-1

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - request was successful
   * - E_NOT_OK
     - request failed
   * - DEM_E_NO_FDC_AVAILABLE
     - there is no fault detection counter available for the requested event

Dem_GetIndicatorStatus
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_GetIndicatorStatus(uint8 IndicatorId, Dem_IndicatorStatusType *IndicatorStatus)

Gets the indicator status derived from the UDS status. API Availability: This API will be available only if ({ecuc(Dem/DemGeneral/DemEventMemorySet/DemIndicator)} != NULL)

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
     - IndicatorId
     - Number of indicator
   * - [out]
     - IndicatorStatus
     - Status of the indicator, like off, on, or blinking.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Operation was successful
   * - E_NOT_OK
     - Operation failed

Dem_GetEventFreezeFrameDataEx
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_GetEventFreezeFrameDataEx(Dem_EventIdType EventId, uint8 RecordNumber, uint16 DataId, uint8 *DestBuffer, uint16 *BufSize)

Gets the data of a freeze frame by event.

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
     - EventId
     - Identification of an event by assigned EventId.
   * - [in]
     - RecordNumber
     - This parameter is a unique identifier for a freeze frame record as defined in ISO14229-1. 0xFF means most recent freeze frame record is returned. 0x00 is only supported if the Dem module supports WWH-OBD (refer to DemOBDSupport)
   * - [in]
     - DataId
     - This parameter specifies the DID (ISO14229-1) that shall be copied to the destination buffer.
   * - [out]
     - DestBuffer
     - This parameter contains a byte pointer that points to the buffer, to which the freeze frame data record shall be written to. The format is raw hexadecimal values and contains no header-information.
   * - [inout]
     - BufSize
     - When the function is called this parameter contains the maximum number of data bytes that can be written to the buffer. The function returns the actual number of written data bytes in this parameter.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Operation was successful
   * - E_NOT_OK
     - Operation could not be performed
   * - DEM_NO_SUCH_ELEMENT
     - The requested event data is not currently stored (but the request was valid) OR The requested record number is not supported by the event OR The requested DID is not supported by the freeze frame.
   * - DEM_BUFFER_TOO_SMALL
     - The provided buffer size is too small.

Dem_GetEventExtendedDataRecordEx
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_GetEventExtendedDataRecordEx(Dem_EventIdType EventId, uint8 RecordNumber, uint8 *DestBuffer, uint16 *BufSize)

Gets the data of an extended data record by event.

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
     - EventId
     - Identification of an event by assigned EventId.
   * - [in]
     - RecordNumber
     - Identification of requested Extended data record. Valid values are between 0x01 and 0xEF as defined in ISO14229-1.
   * - [out]
     - DestBuffer
     - This parameter contains a byte pointer that points to the buffer, to which the extended data data record shall be written to. The format is raw hexadecimal values and contains no header-information.
   * - [inout]
     - BufSize
     - When the function is called this parameter contains the maximum number of data bytes that can be written to the buffer. The function returns the actual number of written data bytes in this parameter.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Operation was successful
   * - E_NOT_OK
     - Operation could not be performed
   * - DEM_NO_SUCH_ELEMENT
     - The requested event data is not currently stored (but the request was valid) OR The requested record number is not supported by the event.
   * - DEM_BUFFER_TOO_SMALL
     - The provided buffer size is too small.

Dem_GetEventMemoryOverflow
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_GetEventMemoryOverflow(uint8 ClientId, Dem_DTCOriginType DTCOrigin, boolean *OverflowIndication)

Gets the event memory overflow indication status.

**Sync/Async**
   Synchronous

**Reentrancy**
   Re-entrant for different ClientIDs, Non re-entrant for same ClientId.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - ClientId
     - DemClientID identifying the DemEventMemorySet indicating in which event memory the overflow has occurred.
   * - [in]
     - DTCOrigin
     - If the Dem supports more than one event memory this parameter is used to select the source memory the overflow indication shall be read from.
   * - [out]
     - OverflowIndication
     - This parameter returns TRUE if the according event memory was overflowed, otherwise it returns FALSE.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Operation was successful
   * - E_NOT_OK
     - Operation failed or is not supported

Dem_GetNumberOfEventMemoryEntries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_GetNumberOfEventMemoryEntries(uint8 ClientId, Dem_DTCOriginType DTCOrigin, uint8 *NumberOfEventMemoryEntries)

Returns the number of entries currently stored in the requested event memory.

**Sync/Async**
   Synchronous

**Reentrancy**
   Re-entrant for different ClientIDs, Non re-entrant for same ClientId.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - ClientId
     - DemClientID identifying the DemEventMemorySet to which the requested event memory belongs to.
   * - [in]
     - DTCOrigin
     - If the Dem supports more than one event memory this parameter is used to select the source memory the overflow indication shall be read from.
   * - [out]
     - NumberOfEventMemoryEntries
     - Number of entries currently stored in the requested event memory.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Operation was successful
   * - E_NOT_OK
     - Operation failed

Dem_ResetEventDebounceStatus
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_ResetEventDebounceStatus(Dem_EventIdType EventId, Dem_DebounceResetStatusType DebounceResetStatus)

Control the internal debounce counter/timer by BSW modules and SW-Cs. The event qualification will not be affected by these debounce state changes. This API is available for BSW modules as soon as Dem_PreInit has been completed (refer to SWS_Dem_00438 and SWS_Dem_00167).

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant for different EventIds. Non reentrant for the same EventId.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - EventId
     - Identification of an event by assigned EventId.
   * - [in]
     - DebounceResetStatus
     - Freeze or reset the internal debounce counter/timer of the specified event.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Operation was successful
   * - E_NOT_OK
     - Operation failed

Dem_ResetEventStatus
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_ResetEventStatus(Dem_EventIdType EventId)

Resets the event failed status. This API can only be used through the RTE and therefore no declaration is exported via

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant for different EventIds. Non reentrant for the same EventId.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - EventId
     - Identification of an event by assigned EventId.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request to reset the event status was successful accepted.
   * - E_NOT_OK
     - Request to reset the event status failed or is not allowed, because the event is already tested in this operation cycle.

Dem_ResetMonitorStatus
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_ResetMonitorStatus(Dem_EventIdType EventId)

Resets the monitor failed status.

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant for different EventIds. Non reentrant for the same EventId.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - EventId
     - Identification of an event by assigned EventId.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request to reset the monitor status was successful and accepted.
   * - E_NOT_OK
     - Request to reset the monitor status failed or is not allowed.

Dem_RestartOperationCycle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_RestartOperationCycle(uint8 OperationCycleId)

Sets an operation cycle state. This API can only be used through the RTE and therefore no declaration is exported via

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
     - OperationCycleId
     - Identification of operation cycle, like power cycle, driving cycle.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - set of operation cycle was accepted and will be handled asynchronously
   * - E_NOT_OK
     - set of operation cycle was rejected

Dem_PrestoreFreezeFrame
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_PrestoreFreezeFrame(Dem_EventIdType EventId)

Captures the freeze frame data for a specific event. This API can only be used through the RTE and therefore no declaration is exported via

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant for different EventIds. Non reentrant for the same EventId.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - EventId
     - Identification of an event by assigned EventId.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Freeze frame prestorage was successful
   * - E_NOT_OK
     - Freeze frame prestorage failed

Dem_SelectDTC
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_SelectDTC(uint8 ClientId, uint32 DTC, Dem_DTCFormatType DTCFormat, Dem_DTCOriginType DTCOrigin)

Selects a DTC or DTC group as target for further operations.

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant for different EventIds. Non reentrant for the same EventId.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - ClientId
     - Unique client id, assigned to the instance of the calling module.
   * - [in]
     - DTC
     - Defines the DTC in respective format that is selected. If the DTC fits to a DTC group number, the DTC group is selected.
   * - [in]
     - DTCFormat
     - Defines the input-format of the provided DTC value.
   * - [in]
     - DTCOrigin
     - The event memory of the requested DTC or group of DTC.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - DTC successfully selected.
   * - DEM_BUSY
     - Another Dem_SelectDTC or Dem_SelectDTC dependent operation of this client is currently in progress.

Dem_SetComponentAvailable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_SetComponentAvailable(Dem_ComponentIdType ComponentId, boolean AvailableStatus)

Set the availability of a specific DemComponent.

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
     - ComponentId
     - Identification of a DemComponent.
   * - [in]
     - AvailableStatus
     - This parameter specifies whether the respective Component shall be available (TRUE) or not (FALSE).

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Operation was successful
   * - E_NOT_OK
     - Operation failed

Dem_SetDTCSuppression
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_SetDTCSuppression(uint8 ClientId, boolean SuppressionStatus)

Set the suppression status of a specific DTC. API Availability: This API will be available only if ({ecuc(Dem/DemGeneral.DemSuppressionSupport)} == DEM_DTC_SUPPRESSION)

**Sync/Async**
   Asynchronous

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
     - ClientId
     - Unique client id, assigned to the instance of the calling module
   * - [in]
     - SuppressionStatus
     - This parameter specifies whether the respective DTC shall be disabled (TRUE) or enabled (FALSE).

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The status of the DTC is correctly provided in the DTCStatus parameter.
   * - E_NOT_OK
     - No DTC selected.
   * - DEM_WRONG_DTC
     - Selected DTC value in selected format does not exist.
   * - DEM_WRONG_DTCORIGIN
     - Selected DTCOrigin does not exist.
   * - DEM_PENDING
     - The requested value is calculated asynchronously and currently not available. The caller can retry later.
   * - DEM_BUSY
     - A different Dem_SelectDTC dependent operation according to SWS_Dem_01253 of this client is currently in progress.

Dem_SetEnableCondition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_SetEnableCondition(uint8 EnableConditionID, boolean ConditionFulfilled)

Sets an enable condition. API Availability: This API will be available only if ({ecuc(Dem/DemGeneral/DemEnableCondition)} != NULL)

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
     - EnableConditionID
     - This parameter identifies the enable condition.
   * - [in]
     - ConditionFulfilled
     - This parameter specifies whether the enable condition assigned to the EnableConditionID is fulfilled (TRUE) or not fulfilled (FALSE).

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - In case the enable condition could be set successfully the API call returns E_OK.
   * - E_NOT_OK:If
     - the setting of the enable condition failed the return value of the function is E_NOT_OK.

Dem_SetEventAvailable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_SetEventAvailable(Dem_EventIdType EventId, boolean AvailableStatus)

Set the available status of a specific Event.

**Sync/Async**
   Asynchronous

**Reentrancy**
   Reentrant for different EventIds. Non reentrant for the same EventId.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - EventId
     - Identification of an event by assigned EventId.
   * - [in]
     - AvailableStatus
     - This parameter specifies whether the respective Event shall be available (TRUE) or not (FALSE).

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request to set the availability status was successful.
   * - E_NOT_OK
     - Request to set the availability status not accepted.

Dem_SetEventConfirmationThresholdCounter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_SetEventConfirmationThresholdCounter(Dem_EventIdType EventId, uint8 FailureCycleCounterThreshold)

Set the failure confirmation threshold of an event.

**Sync/Async**
   Asynchronous

**Reentrancy**
   Reentrant for different EventIds. Non reentrant for the same EventId.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - EventId
     - Identification of an event by assigned EventId.
   * - [in]
     - FailureCycleCounterThreshold
     - Failure cycle counter threshold of event to be set.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Change of threshold was successful.
   * - E_NOT_OK
     - Threshold cannot be changed as DemEventConfirmationThresholdCounterAdaptable is set to FALSE for this event.

Dem_SetEventStatus
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_SetEventStatus(Dem_EventIdType EventId, Dem_EventStatusType EventStatus)

Called by SW-Cs or BSW modules to report monitor status information to the Dem. BSW modules calling Dem_SetEventStatus can safely ignore the return value. This API will be available only if ({Dem/DemConfigSet/DemEventParameter/DemEventReportingType} == STANDARD_REPORTING)

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant for different EventIds. Non reentrant for the same EventId.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - EventId
     - Identification of an event by assigned EventId.
   * - [in]
     - EventStatus
     - Monitor test result

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - set of event status was successful
   * - E_NOT_OK
     - Event status setting or processing failed or could not be accepted.

Dem_SetEventStatusWithMonitorData
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_SetEventStatusWithMonitorData(Dem_EventIdType EventId, Dem_EventStatusType EventStatus, Dem_MonitorDataType monitorData0, Dem_MonitorDataType monitorData1)

This API will be available only if ({Dem/DemConfigSet/DemEventParameter/DemEventReportingType} == STANDARD_REPORTING_WITH_MONITOR_DATA)

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant for different EventIds. Non reentrant for the same EventId.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - EventId
     - Identification of an event by assigned EventId.
   * - [in]
     - EventStatus
     - Monitor test result
   * - [in]
     - monitorData0
     - -
   * - [in]
     - monitorData1
     - -

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - set of event status was successful
   * - E_NOT_OK
     - Event status setting or processing failed or could not be accepted.

Dem_SetStorageCondition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_SetStorageCondition(uint8 StorageConditionID, boolean ConditionFulfilled)

Sets a storage condition.API Availability: This API will be available only if ({ecuc(Dem/DemGeneral/DemStorageCondition)} != NULL)

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
     - StorageConditionID
     - This parameter identifies the storage condition.
   * - [in]
     - ConditionFulfilled
     - This parameter specifies whether the storage condition assigned to the StorageConditionID is fulfilled (TRUE) or not fulfilled (FALSE).

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - In case the storage condition could be set successfully the API call returns E_OK.
   * - E_NOT_OK:If
     - the setting of the storage condition failed the return value of the function is E_NOT_OK.

Dem_SetWIRStatus
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_SetWIRStatus(Dem_EventIdType EventId, boolean WIRStatus)

Sets the WIR status bit via failsafe SW-Cs. This API can only be used through the RTE and therefore no declaration is exported via

**Sync/Async**
   Asynchronous

**Reentrancy**
   Reentrant for different EventIds. Non reentrant for the same EventId.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - EventId
     - Identification of an event by assigned EventId. The Event Number is configured in the DEM. Min.: 1 (0: Indication of no Event or Failure) Max.:Result of configuration of Event Numbers in DEM (Max is either 255 or 65535)
   * - [in]
     - WIRStatus
     - Requested status of event related WIR-bit (regarding to the current status of function inhibition) WIRStatus = TRUE -> WIR-bit shall be set to "1" WIRStatus = FALSE -> WIR-bit shall be set to "0"

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request to set the WIR status was successful.
   * - E_NOT_OK
     - Request to set the WIR status was not accepted (e.g. disabled controlDTCSetting) and should be repeated.

Dem_GetTranslationType
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Dem_DTCTranslationFormatType Dem_GetTranslationType(uint8 ClientId)

Gets the supported DTC formats of the ECU.The supported formats are configured via Dem TypeOfDTCSupported.

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant for different ClientIds, non reentrant for the same ClientId.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - ClientId
     - Unique client id, assigned to the instance of the calling module.

**Return type**
    Dem_DTCTranslationFormatType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - Dem_DTCTranslationFormatType
     - Returns the configured DTC translation format. A combination of different DTC formats is not possible.
   * - DEM_DTC_TRANSLATION_ISO15031_6
     - ISO15031-6 DTC format/SAE J2012-DA_DTCFormat_00 DTC format
   * - DEM_DTC_TRANSLATION_ISO14229_1
     - ISO14229-1 DTC format
   * - DEM_DTC_TRANSLATION_SAEJ1939_73
     - SAEJ1939-73 DTC format
   * - DEM_DTC_TRANSLATION_ISO11992_4
     - ISO11992-4 DTC format
   * - DEM_DTC_TRANSLATION_J2012DA_FORMAT_04
     - SAE_J2012-DA_DTCFormat_04 DTC format

Dem_GetDTCStatusAvailabilityMask
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_GetDTCStatusAvailabilityMask(uint8 ClientId, Dem_UdsStatusByteType *DTCStatusMask, Dem_DTCOriginType DTCOrigin)

Gets the DTC Status availability mask of the selected fault memory.

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant for different ClientIds, non reentrant for the same ClientId.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - ClientId
     - Unique client id, assigned to the instance of the calling module.
   * - [out]
     - DTCStatusMask
     - DTCStatusMask The value DTCStatusMask indicates the supported DTC status bits from the Dem. All supported information is indicated by setting the corresponding status bit to 1. See ISO14229-1.
   * - [in]
     - DTCOrigin
     - This parameter selects the event memory the DTCStatus AvailabilityMask is requested for. Only the values DEM_DTC_ORIGIN_PRIMARY_MEMORY and DEM_DTC_ORIGIN_USERDEFINED_MEMORY_<Name> are valid.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - get of DTC status mask was successful
   * - E_NOT_OK
     - get of DTC status mask failed

Dem_GetStatusOfDTC
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_GetStatusOfDTC(uint8 ClientId, uint8 *DTCStatus)

Gets the status of a DTC. For large configurations and DTC-calibration, the interface behavior can be asynchronous (splitting the DTC-search into segments). The DTCs of OBD Events Suppression shall be reported as Dem_WRONG_DTC.

**Sync/Async**
   Asynchronous

**Reentrancy**
   Reentrant for different ClientIds, non reentrant for the same ClientId.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - ClientId
     - Unique client id, assigned to the instance of the calling module.
   * - [in]
     - DTCStatus
     - This parameter receives the status information of the requested DTC. It follows the format as defined in ISO14229-1 If the return value of the function call is other than DEM_FILTERED_OK this parameter does not contain valid data.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The status of the DTC is correctly provided in the DTCStatus parameter.
   * - E_NOT_OK
     - No DTC selected
   * - DEM_WRONG_DTC
     - Selected DTC value in selected format does not exist
   * - DEM_WRONG_DTCORIGIN
     - Selected DTCOrigin does not exist
   * - DEM_PENDING
     - Retrieving the DTC status is currently in progress. The caller shall call this function again at a later moment.
   * - DEM_NO_SUCH_ELEMENT
     - Selected DTC does not have an assigned DTC status.
   * - DEM_BUSY
     - A different Dem_SelectDTC dependent operation according to SWS_Dem_01253 of this client is currently in progress.

Dem_GetSeverityOfDTC
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_GetSeverityOfDTC(Dem_DTCSeverityType *DTCSeverity, uint8 ClientId)

Gets the severity of the requested DTC. For large configurations and DTC-calibration, the interface behavior can be asynchronous (splitting the DTC-search into segments).

**Sync/Async**
   Asynchronous

**Reentrancy**
   Reentrant for different ClientIds, non reentrant for the same ClientId.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [out]
     - DTCSeverity
     - This parameter contains the DTCSeverity according to ISO 14229-1.
   * - [in]
     - ClientId
     - Unique client id, assigned to the instance of the calling module.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The DTC severity is correctly provided in the DTCSeverity parameter.
   * - E_NOT_OK
     - No DTC selected
   * - DEM_WRONG_DTC
     - Selected DTC value in selected format does not exist
   * - DEM_WRONG_DTCORIGIN
     - Selected DTCOrigin does not exist
   * - DEM_PENDING
     - Retrieving the DTC status is currently in progress. The caller shall call this function again at a later moment.
   * - DEM_NO_SUCH_ELEMENT
     - Selected DTC does not have an assigned DTC status.
   * - DEM_BUSY
     - A different Dem_SelectDTC dependent operation according to SWS_Dem_01253 of this client is currently in progress.

Dem_GetFunctionalUnitOfDTC
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_GetFunctionalUnitOfDTC(uint8 ClientId, uint8 *DTCFunctionalUnit)

Gets the functional unit of the requested DTC.

**Sync/Async**
   Asynchronous

**Reentrancy**
   Reentrant for different ClientIds, non reentrant for the same ClientId.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - ClientId
     - Unique client id, assigned to the instance of the calling module.
   * - [out]
     - DTCFunctionalUnit
     - Functional unit value of this DTC

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The DTC functional unit is provided in the parameter DTCFunctionalUnit.
   * - E_NOT_OK
     - No DTC selected
   * - DEM_WRONG_DTC
     - Selected DTC value in selected format does not exist
   * - DEM_WRONG_DTCORIGIN
     - Selected DTCOrigin does not exist
   * - DEM_PENDING
     - Retrieving the DTC status is currently in progress. The caller shall call this function again at a later moment.
   * - DEM_NO_SUCH_ELEMENT
     - Selected DTC does not have an assigned DTC status.
   * - DEM_BUSY
     - A different Dem_SelectDTC dependent operation according to SWS_Dem_01253 of this client is currently in progress.

Dem_SetDTCFilter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_SetDTCFilter(uint8 ClientId, uint8 DTCStatusMask, Dem_DTCFormatType DTCFormat, Dem_DTCOriginType DTCOrigin, boolean FilterWithSeverity, Dem_DTCSeverityType DTCSeverityMask, boolean FilterForFaultDetectionCounter)

Sets the DTC Filter. The server shall perform a bit-wise logical AND-ing operation between the parameter DTCStatusMask and the current UDS status in the server. In addition to the DTCStatus AvailabilityMask, the server shall return all DTCs for which the result of the AND-ing operation is non-zero [i.e. (statusOfDTC & DTCStatusMask) != 0]. The server shall process only the DTC Status bits that it is supporting. OBD Events Suppression shall be ignored for this computation. If no DTCs within the server match the masking criteria specified in the client request, no DTC or status information shall be provided following the DTCStatusAvailabilityMask byte in the positive response message (((statusOfDTC & DTCStatusMask) != 0) && ((severity & DTCSeverityMask) != 0)) == TRUE.

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant for different ClientIds, non reentrant for the same ClientId.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - ClientId
     - Unique client id, assigned to the instance of the calling module.
   * - [in]
     - DTCStatusMask
     - Status-byte mask for DTC status-byte filtering Values: 0x00: Autosar-specific value to deactivate the status-byte filtering (different meaning than in ISO 14229-1) to report all supported DTCs (used for service 0x19 subfunctions 0x0A/0x15) 0x01..0xFF: Status-byte mask according to ISO 14229-1 DTCStatusMask (handed over by Dcm from service request directly) to filter for DTCs with at least one status bit set matching this status-byte mask
   * - [in]
     - DTCFormat
     - Defines the output-format of the requested DTC values for the sub-sequent API calls. If passed value does not fit to Configuration, the DET error DEM_E_WRONG_CONFIGURATION shall be reported, e.g. if DTCFormat "DEM_DTC_FORMAT_OBD" is passed, but OBD is not supported per configuration.
   * - [in]
     - DTCOrigin
     - If the Dem supports more than one event memory this parameter is used to select the source memory the DTCs shall be read from. If passed value does not fit to Configuration, the DET error DEM_E_WRONG_CONFIGURATION shall be reported.
   * - [in]
     - FilterWithSeverity
     - This flag defines whether severity information (ref. to parameter below) shall be used for filtering. This is to allow for coexistence of DTCs with and without severity information. TRUE: severity information is used for filtering. FALSE: severity information is not used for filtering.
   * - [in]
     - DTCSeverityMask
     - Contains the DTCSeverityMask according to ISO14229-1.
   * - [in]
     - FilterForFaultDetectionCounter
     - This flag defines whether the fault detection counter information shall be used for filtering. This is to allow for coexistence of DTCs with and without fault detection counter information. If fault detection counter information is filter criteria, only those DTCs with a fault detection counter value between 1 and 0x7E shall be reported. Remark: If the event does not use the debouncing inside Dem, then the Dem must request this information via GetFaultDetectionCounter. TRUE: fault detection counter is used for filtering. FALSE: fault detection counter is not used for filtering.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Filter was successfully set.
   * - E_NOT_OK
     - Indicates a wrong DTCOrigin or DTCFormat

Dem_GetNumberOfFilteredDTC
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_GetNumberOfFilteredDTC(uint8 ClientId, uint16 *NumberOfFilteredDTC)

Gets the number of a filtered DTC.

**Sync/Async**
   Asynchronous

**Reentrancy**
   Reentrant for different ClientIds, non reentrant for the same ClientId.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - ClientId
     - Unique client id, assigned to the instance of the calling module.
   * - [out]
     - NumberOfFilteredDTC
     - The number of DTCs matching the defined status mask.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Getting number of filtered DTCs was successful
   * - E_NOT_OK
     - No DTC filter set
   * - DEM_PENDING
     - Retrieving the DTC status is currently in progress. The caller shall call this function again at a later moment.

Dem_GetNextFilteredDTC
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_GetNextFilteredDTC(uint8 ClientId, uint32 *DTC, uint8 *DTCStatus)

Gets the next filtered DTC matching the filter criteria. For UDS services, the interface has an asynchronous behavior, because a large number of DTCs has to be processed.

**Sync/Async**
   Asynchronous

**Reentrancy**
   Reentrant for different ClientIds, non reentrant for the same ClientId.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - ClientId
     - Unique client id, assigned to the instance of the calling module.
   * - [out]
     - DTC
     - Receives the DTC value in respective format of the filter returned by this function. If the return value of the function is other than DEM_FILTERED_OK this parameter does not contain valid data.
   * - [out]
     - DTCStatus
     - This parameter receives the status information of the requested DTC. It follows the format as defined in ISO14229-1 If the return value of the function call is other than DEM_FILTERED_OK this parameter does not contain valid data.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Returned next filtered element
   * - E_NOT_OK
     - No DTC filter set
   * - DEM_NO_SUCH_ELEMENT
     - No further element matching the filter criteria found
   * - DEM_PENDING
     - The requested operation is currently in progress. The caller shall call this function again at a later moment. Note that according to SWS_Dem_00653 this return value is not always allowed.

Dem_GetNextFilteredDTCAndFDC
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_GetNextFilteredDTCAndFDC(uint8 ClientId, uint32 *DTC, sint8 *DTCFaultDetectionCounter)

Gets the next filtered DTC and its associated Fault Detection Counter (FDC) matching the filter criteria. The interface has an asynchronous behavior, because a large number of DTCs has to be processed and the FDC might be received asynchronously from a SW-C, too.

**Sync/Async**
   Asynchronous

**Reentrancy**
   Reentrant for different ClientIds, non reentrant for the same ClientId.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - ClientId
     - Unique client id, assigned to the instance of the calling module.
   * - [out]
     - DTC
     - Receives the DTC value in respective format of the filter returned by this function. If the return value of the function is other than DEM_FILTERED_OK this parameter does not contain valid data.
   * - [out]
     - DTCFaultDetectionCounter
     - This parameter receives the Fault Detection Counter information of the requested DTC. If the return value of the function call is other than DEM_FILTERED_OK this parameter does not contain valid data. -128dec...127dec PASSED...FAILED according to ISO 14229-1

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Returned next filtered element
   * - E_NOT_OK
     - No DTC filter set
   * - DEM_NO_SUCH_ELEMENT
     - No further element matching the filter criteria found
   * - DEM_PENDING
     - The requested operation is currently in progress. The caller shall call this function again at a later moment.

Dem_GetNextFilteredDTCAndSeverity
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_GetNextFilteredDTCAndSeverity(uint8 ClientId, uint32 *DTC, uint8 *DTCStatus, Dem_DTCSeverityType *DTCSeverity, uint8 *DTCFunctionalUnit)

Gets the next filtered DTC and its associated Severity matching the filter criteria. The interface has an asynchronous behavior, because a large number of DTCs has to be processed.

**Sync/Async**
   Asynchronous

**Reentrancy**
   Reentrant for different ClientIds, non reentrant for the same ClientId.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - ClientId
     - Unique client id, assigned to the instance of the calling module.
   * - [out]
     - DTC
     - Receives the DTC value in respective format of the filter returned by this function. If the return value of the function is other than DEM_FILTERED_OK this parameter does not contain valid data.
   * - 
     - DTCStatus
     - 
   * - 
     - DTCSeverity
     - 
   * - 
     - DTCFunctionalUnit
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
     - Returned next filtered element
   * - E_NOT_OK
     - No DTC filter set
   * - DEM_NO_SUCH_ELEMENT
     - No further element matching the filter criteria found
   * - DEM_PENDING
     - The requested operation is currently in progress. The caller shall call this function again at a later moment.

Dem_SetFreezeFrameRecordFilter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_SetFreezeFrameRecordFilter(uint8 ClientId, Dem_DTCFormatType DTCFormat)

Sets a freeze frame record filter.

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant for different ClientIds, non reentrant for the same ClientId.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - ClientId
     - Unique client id, assigned to the instance of the calling module.
   * - [in]
     - DTCFormat
     - Defines the output-format of the requested DTC values

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Filter is accepted
   * - E_NOT_OK
     - Wrong filter selected

Dem_GetNextFilteredRecord
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_GetNextFilteredRecord(uint8 ClientId, uint32 *DTC, uint8 *RecordNumber)

Gets the next freeze frame record number and its associated DTC stored in the event memory. The interface has an asynchronous behavior, because NvRAM access might be required.

**Sync/Async**
   Asynchronous

**Reentrancy**
   Reentrant for different ClientIds, non reentrant for the same ClientId.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - ClientId
     - Unique client id, assigned to the instance of the calling module.
   * - [out]
     - DTC
     - DTC Receives the DTC value in respective format of the filter returned by this function. If the return value of the function is other than E_OK this parameter does not contain valid data.
   * - [out]
     - RecordNumber
     - Freeze frame record number of the reported DTC (relative addressing). If the return value of the function is other than E_OK this parameter does not contain valid data.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Returned next filtered element
   * - DEM_NO_SUCH_ELEMENT
     - No further element (matching the filter criteria) found
   * - DEM_PENDING
     - The requested value is calculated asynchronously and currently not available. The caller can retry later. Only used by asynchronous interfaces.

Dem_GetDTCByOccurrenceTime
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_GetDTCByOccurrenceTime(uint8 ClientId, Dem_DTCRequestType DTCRequest, uint32 *DTC)

Gets the DTC by occurrence time. There is no explicit parameter for the DTC-origin as the origin always is DEM_DTC_ORIGIN_PRIMARY_MEMORY.

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant for different ClientIds, non reentrant for the same ClientId.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - ClientId
     - Unique client id, assigned to the instance of the calling module.
   * - [in]
     - DTCRequest
     - This parameter defines the request type of the DTC.
   * - [out]
     - DTC
     - DTC Receives the DTC value in respective format of the filter returned by this function. If the return value of the function is other than E_OK this parameter does not contain valid data.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - get of DTC was successful
   * - E_NOT_OK
     - the call was not successful
   * - DEM_NO_SUCH_ELEMENT
     - The requested element is not stored

Dem_DisableDTCRecordUpdate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_DisableDTCRecordUpdate(uint8 ClientId)

Disables the event memory update of a specific DTC (only one at one time).

**Sync/Async**
   Asynchronous

**Reentrancy**
   Reentrant for different ClientIds, non reentrant for the same ClientId.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - ClientId
     - Unique client id, assigned to the instance of the calling module.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Event memory update successfully disabled
   * - E_NOT_OK
     - No DTC selected
   * - DEM_WRONG_DTC
     - Selected DTC value in selected format does not exist or a group of DTC was selected
   * - DEM_WRONG_DTCORIGIN
     - Selected DTCOrigin does not exist
   * - DEM_PENDING
     - Disabling the DTC record update is currently in progress. The caller shall call this function again at a later moment.
   * - DEM_BUSY
     - A different Dem_SelectDTC dependent operation according to SWS_Dem_01253 of this client is currently in progress.

Dem_EnableDTCRecordUpdate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_EnableDTCRecordUpdate(uint8 ClientId)

Enables the event memory update of the DTC disabled by

**Sync/Async**
   Asynchronous

**Reentrancy**
   Reentrant for different ClientIds, non reentrant for the same ClientId.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - ClientId
     - Unique client id, assigned to the instance of the calling module.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - DTC record successfully updated.
   * - E_NOT_OK
     - No DTC selected.

Dem_GetSizeOfExtendedDataRecordSelection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_GetSizeOfExtendedDataRecordSelection(uint8 ClientId, uint32 *SizeOfExtendedDataRecord)

Gets the size of Extended Data Record by DTC selected by the call of Dem_SelectExtended DataRecord.

**Sync/Async**
   Asynchronous

**Reentrancy**
   Reentrant for different ClientIds, non reentrant for the same ClientId.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - ClientId
     - Unique client id, assigned to the instance of the calling module.
   * - [out]
     - SizeOfExtendedDataRecord
     - Size of the requested extended data record(s) including record number. The format for a single ExtendedDataRecord is: {RecordNumber, data[1], ..., data[N]}

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Size returned successfully
   * - E_NOT_OK
     - selection function is not called.
   * - DEM_PENDING
     - The requested value is calculated asynchronously and currently not available. The caller can retry later.
   * - DEM_WRONG_DTC
     - DTC value not existing
   * - DEM_WRONG_DTCORIGIN
     - Wrong DTC origin
   * - DEM_NO_SUCH_ELEMENT
     - Record number is not supported by configuration and therefore invalid

Dem_GetSizeOfFreezeFrameSelection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_GetSizeOfFreezeFrameSelection(uint8 ClientId, uint32 *SizeOfFreezeFrame)

Gets the size of Extended Data Record by DTC selected by the call of Dem_SelectExtended DataRecord.

**Sync/Async**
   Asynchronous

**Reentrancy**
   Reentrant for different ClientIds, non reentrant for the same ClientId.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - ClientId
     - Unique client id, assigned to the instance of the calling module.
   * - [out]
     - SizeOfFreezeFrame
     - Number of bytes in the requested freeze frame record.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Size returned successfully
   * - E_NOT_OK
     - selection function is not called.
   * - DEM_PENDING
     - The requested value is calculated asynchronously and currently not available. The caller can retry later.
   * - DEM_WRONG_DTC
     - DTC value not existing
   * - DEM_WRONG_DTCORIGIN
     - Wrong DTC origin
   * - DEM_NO_SUCH_ELEMENT
     - Record number is not supported by configuration and therefore invalid

Dem_GetNextExtendedDataRecord
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_GetNextExtendedDataRecord(uint8 ClientId, uint8 *DestBuffer, uint16 *BufSize)

Gets extended data record for the DTC selected by Dem_SelectExtendedDataRecord. The function stores the data in the provided DestBuffer.

**Sync/Async**
   Asynchronous

**Reentrancy**
   Reentrant for different ClientIds, non reentrant for the same ClientId.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - ClientId
     - Unique client id, assigned to the instance of the calling module.
   * - [out]
     - DestBuffer
     - This parameter contains a byte pointer that points to the buffer, to which the extended data record shall be written to. The format is: {ExtendedDataRecordNumber, data[0], data[1], ..., data[n]}
   * - [inout]
     - BufSize
     - When the function is called this parameter contains the maximum number of data bytes that can be written to the buffer. The function returns the actual number of written data bytes in this parameter.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Size and buffer successfully returned.
   * - E_NOT_OK
     - selection function is not called.
   * - DEM_BUFFER_TOO_SMALL
     - provided buffer size too small.
   * - DEM_PENDING
     - The requested value is calculated asynchronously and currently not available. The caller can retry later.
   * - DEM_WRONG_DTC
     - DTC value not existing
   * - DEM_WRONG_DTCORIGIN
     - Wrong DTC origin
   * - DEM_NO_SUCH_ELEMENT
     - Found no (further) element matching the filter criteria

Dem_GetNextFreezeFrameData
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_GetNextFreezeFrameData(uint8 ClientId, uint8 *DestBuffer, uint16 *BufSize)

Gets extended data record for the DTC selected by Dem_SelectExtendedDataRecord. The function stores the data in the provided DestBuffer.

**Sync/Async**
   Asynchronous

**Reentrancy**
   Reentrant for different ClientIds, non reentrant for the same ClientId.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - ClientId
     - Unique client id, assigned to the instance of the calling module.
   * - [out]
     - DestBuffer
     - This parameter contains a byte pointer that points to the buffer, to which the freeze frame data record shall be written to. The format is: {RecordNumber, NumOfDIDs, DID[1], data[1], ..., DID[N], data[N]}
   * - [inout]
     - BufSize
     - When the function is called this parameter contains the maximum number of data bytes that can be written to the buffer. The function returns the actual number of written data bytes in this parameter.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Size and buffer successfully returned.
   * - E_NOT_OK
     - selection function is not called.
   * - DEM_BUFFER_TOO_SMALL
     - provided buffer size too small.
   * - DEM_PENDING
     - The requested value is calculated asynchronously and currently not available. The caller can retry later.
   * - DEM_WRONG_DTC
     - DTC value not existing
   * - DEM_WRONG_DTCORIGIN
     - Wrong DTC origin
   * - DEM_NO_SUCH_ELEMENT
     - Found no (further) element matching the filter criteria

Dem_SelectExtendedDataRecord
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_SelectExtendedDataRecord(uint8 ClientId, uint8 ExtendedDataNumber)

Sets the filter to be used by Dem_GetNextExtendedDataRecord and Dem_GetSizeOfExtendedDataRecordSelection.

**Sync/Async**
   Asynchronous

**Reentrancy**
   Reentrant for different ClientIds, non reentrant for the same ClientId.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - ClientId
     - Unique client id, assigned to the instance of the calling module.
   * - [in]
     - ExtendedDataNumber
     - Identification/Number of requested extended data record. For primary fault memory the value of 0xFE is explictely allowed to request all regulated emissions OBD DTC extended data records. The value of 0xFF is explicitely allowed in all fault memories to retrieve the data of all extended datal records.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Extended data record successfully selected.
   * - DEM_WRONG_DTC
     - Selected DTC value in selected format does not exist.
   * - DEM_WRONG_DTCORIGIN
     - Selected DTCOrigin does not exist.
   * - DEM_PENDING
     - Selecting the extended data record is currently in progress. The caller shall call this function again at a later moment.
   * - DEM_BUSY
     - A different Dem_SelectDTC dependent operation according to SWS_Dem_01253 of this client is currently in progress.

Dem_SelectFreezeFrameData
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_SelectFreezeFrameData(uint8 ClientId, uint8 RecordNumber)

Sets the filter to be used by Dem_GetNextFreezeFrameData and Dem_GetSizeOfFreezeFrame Selection.

**Sync/Async**
   Asynchronous

**Reentrancy**
   Reentrant for different ClientIds, non reentrant for the same ClientId.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - ClientId
     - Unique client id, assigned to the instance of the calling module.
   * - [in]
     - RecordNumber
     - Unique identifier for a snapshot record as defined in ISO 14229-1. The value 0xFF is a placeholder referencing all snapshot records of the addressed DTC. The value 0x00 indicates the DTC-specific WWH-OBD snapshot record.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Freeze frame data successfully selected.
   * - DEM_WRONG_DTC
     - Selected DTC value in selected format does not exist.
   * - DEM_WRONG_DTCORIGIN
     - Selected DTCOrigin does not exist.
   * - DEM_PENDING
     - Selecting the freeze frame is currently in progress. The caller shall call this function again at a later moment.
   * - DEM_BUSY
     - A different Dem_SelectDTC dependent operation according to SWS_Dem_01253 of this client is currently in progress.

Dem_GetNumberOfFreezeFrameRecords
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_GetNumberOfFreezeFrameRecords(uint8 ClientId, uint16 *NumberOfFilteredRecords)

This function returns the number of all freeze frame records currently stored in the primary event memory.

**Sync/Async**
   Asynchronous

**Reentrancy**
   Reentrant for different ClientIds, non reentrant for the same ClientId.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - ClientId
     - Unique client id, assigned to the instance of the calling module.
   * - [out]
     - NumberOfFilteredRecords
     - Number of all freeze frame records currently stored in the primary event memory.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Returned correctly the number of freeze frame records
   * - DEM_PENDING
     - The requested value is calculated asynchronously and currently not available. The caller can retry later

Dem_DisableDTCSetting
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_DisableDTCSetting(uint8 ClientId)

Disables the DTC setting for all DTCs assigned to the DemEventMemorySet of the addressed client.

**Sync/Async**
   Asynchronous

**Reentrancy**
   Reentrant for different ClientIds, non reentrant for the same ClientId.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - ClientId
     - Unique client id, assigned to the instance of the calling module.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Returned next filtered element
   * - DEM_PENDING
     - The requested operation is currently in progress. The caller shall call this function again at a later moment.

Dem_EnableDTCSetting
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_EnableDTCSetting(uint8 ClientId)

(Re)-Enables the DTC setting for all DTCs assigned to the DemEventMemorySet of the addressed client.

**Sync/Async**
   Asynchronous

**Reentrancy**
   Reentrant for different ClientIds, non reentrant for the same ClientId.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - ClientId
     - Unique client id, assigned to the instance of the calling module.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The operation was successful;
   * - DEM_PENDING
     - The started operation is currently in progress. The caller shall call this function again at a later moment.

Dem_SetEventDisabled
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_SetEventDisabled(Dem_EventIdType EventId)

Service for reporting the event as disabled to the Dem for the PID $41 computation. API is needed in OBD-relevant ECUs only. API Availability: This API will be available only if ({ecuc(Dem/DemGeneral.DemOBDSupport)} != DEM_OBD_NO_OBD_SUPPORT)

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant for different EventIds. Non reentrant for the same EventId.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - EventId
     - Identification of an event by assigned EventId.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - set of event to disabled was successfull.
   * - E_NOT_OK
     - set of event disabled failed

Dem_RepIUMPRFaultDetect
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_RepIUMPRFaultDetect(Dem_RatioIdType RatioID)

Service for reporting that faults are possibly found because all conditions are fullfilled. API is needed in OBD-relevant ECUs only API Availability: This API will be available only if ({ecuc(Dem/DemGeneral.DemOBDSupport)} != DEM_OBD_NO_OBD_SUPPORT)

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant for different EventIds. Non reentrant for the same EventId.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - RatioID
     - Ratio Identifier reporting that a respective monitor could have found a fault only used when interface option "API" is selected

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - report of IUMPR result was successfully reported

Dem_SetIUMPRDenCondition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_SetIUMPRDenCondition(Dem_IumprDenomCondIdType ConditionId, Dem_IumprDenomCondStatusType ConditionStatus)

In order to communicate the status of the (additional) denominator conditions among the OBD relevant ECUs, the API is used to forward the condition status to a Dem of a particular ECU. API is needed in OBD-relevant ECUs only. API Availability: This API will be available only if ({ecuc(Dem/DemGeneral.DemOBDSupport)} != DEM_OBD_NO_OBD_SUPPORT)

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
     - ConditionId
     - Identification of a IUMPR denominator condition ID (General Denominator, Cold start, EVAP, 500mi).
   * - [in]
     - ConditionStatus
     - Status of the IUMPR denominator condition (Not-reached, reached, not reachable / inhibited)

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - set of IUMPR denominator condition was successful
   * - E_NOT_OK
     - set of IUMPR denominator condition failed or could not be accepted.

Dem_GetIUMPRDenCondition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_GetIUMPRDenCondition(Dem_IumprDenomCondIdType ConditionId, Dem_IumprDenomCondStatusType *ConditionStatus)

In order to communicate the status of the (additional) denominator conditions among the OBD relevant ECUs, the API is used to forward the condition status to a Dem of a particular ECU. API is needed in OBD-relevant ECUs only. API Availability: This API will be available only if ({ecuc(Dem/DemGeneral.DemOBDSupport)} != DEM_OBD_NO_OBD_SUPPORT)

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
     - ConditionId
     - Identification of a IUMPR denominator condition ID (General Denominator, Cold start, EVAP, 500mi).
   * - [in]
     - ConditionStatus
     - Status of the IUMPR denominator condition (Not-reached, reached, not reachable / inhibited)

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - get of IUMPR denominator condition status was successful
   * - E_NOT_OK
     - get of condition status failed

Dem_RepIUMPRDenRelease
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_RepIUMPRDenRelease(Dem_RatioIdType RatioID)

Service is used to release a denominator of a specific monitor. API is needed in OBD-relevant ECUs only API Availability: This API will be available only if ({ecuc(Dem/DemGeneral.DemOBDSupport)} != DEM_OBD_NO_OBD_SUPPORT)

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
     - RatioID
     - Ratio Identifier reporting that specific denominator is released (for physical reasons

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - report of IUMPR denominator status was successfully reported
   * - E_NOT_OK
     - report of IUMPR denominator status was not successfully reported

Dem_SetPtoStatus
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_SetPtoStatus(boolean PtoStatus)

API is needed in OBD-relevant ECUs only API Availability: This API will be available only if ({ecuc(Dem/DemGeneral.DemOBDSupport)} != DEM_OBD_NO_OBD_SUPPORT)

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
     - PtoStatus
     - sets the status of the PTO (TRUE==active; FALSE==inactive)

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Returns E_OK when the new PTO-status has been adopted by the Dem
   * - E_NOT_OK
     - returns E_NOT_OK in all other cases.

Dem_ReadDataOfPID01
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_ReadDataOfPID01(uint8 *PID01value)

Service to report the value of PID $01 computed by the Dem. API is needed in OBD relevant ECUs only.

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
   * - [out]
     - PID01value
     - Buffer containing the contents of PID $01 computed by the Dem. The buffer is provided by the application with the size of 4 bytes.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - Always
     - E_OK is returned, as E_NOT_OK will never appear.

Dem_GetDataOfPID21
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_GetDataOfPID21(uint8 *PID21value)

Service to get the value of PID $21 from the Dem by a software component. API is needed in OBD-relevant ECUs only. API Availability: This API will be available only if ({ecuc(Dem/DemGeneral/DemGeneral OBD.DemOBDCentralizedPID21Handling)} == true) && ({ecuc(Dem/DemGeneral.DemOBDSupport)} == DEM_OBD_MASTER_ECU)

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
   * - [out]
     - PID21value
     - Content of PID $21 as raw hex value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - Always
     - E_OK is returned, as E_NOT_OK will never appear.

Dem_SetDataOfPID21
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_SetDataOfPID21(const uint8 *PID21value)

Service to set the value of PID $21 in the Dem by a software component. API is needed in OBD-relevant ECUs only. API Availability: This API will be available only if ({ecuc(Dem/DemGeneral.DemOBDSupport)} != DEM_OBD_NO_OBD_SUPPORT)

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
     - PID21value
     - Buffer containing the contents of PID $21. The buffer is provided by the Dcm with the appropriate size, i.e. during configuration, the Dcm identifies the required size from the largest PID in order to configure a PIDBuffer.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - Always
     - E_OK is returned, as E_NOT_OK will never appear.

Dem_SetDataOfPID31
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_SetDataOfPID31(const uint8 *PID31value)

Service to set the value of PID $31 in the Dem by a software component. API is needed in OBD-relevant ECUs only. API Availability: This API will be available only if ({ecuc(Dem/DemGeneral.DemOBDSupport)} != DEM_OBD_NO_OBD_SUPPORT)

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
     - PID31value
     - Buffer containing the contents of PID $31. The buffer is provided by the Dcm with the appropriate size, i.e. during configuration, the Dcm identifies the required size from the largest PID in order to configure a PIDBuffer.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - Always
     - E_OK is returned, as E_NOT_OK will never appear.

Dem_SetDataOfPID4D
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_SetDataOfPID4D(const uint8 *PID4Dvalue)

Service to set the value of PID $4D in the Dem by a software component. API is needed in OBD-relevant ECUs only. API Availability: This API will be available only if ({ecuc(Dem/DemGeneral.DemOBDSupport)} != DEM_OBD_NO_OBD_SUPPORT)

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
     - PID4Dvalue
     - Buffer containing the contents of PID $4D. The buffer is provided by the Dcm with the appropriate size, i.e. during configuration, the Dcm identifies the required size from the largest PID in order to configure a PIDBuffer.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - Always
     - E_OK is returned, as E_NOT_OK will never appear.

Dem_SetDataOfPID4E
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_SetDataOfPID4E(const uint8 *PID4Evalue)

Service to set the value of PID $4E in the Dem by a software component. API is needed in OBD-relevant ECUs only. API Availability: This API will be available only if ({ecuc(Dem/DemGeneral.DemOBDSupport)} != DEM_OBD_NO_OBD_SUPPORT)

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
     - PID4Evalue
     - Buffer containing the contents of PID $4E. The buffer is provided by the Dcm with the appropriate size, i.e. during configuration, the Dcm identifies the required size from the largest PID in order to configure a PIDBuffer.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - Always
     - E_OK is returned, as E_NOT_OK will never appear.

Dem_GetCycleQualified
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_GetCycleQualified(uint8 OperationCycleId, boolean *isQualified)

Returns the qualification state of the dependent operation cycle. API Availability: This API will be available only if any of the ({ecuc(Dem/DemGeneral/DemOperationCycle.DemLeadingCycleRef)} != NULL)

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
     - OperationCycleId
     - Identification of a configured DemOperationCycle.
   * - [out]
     - isQualified
     - TRUE: The dependent operation cylcle is qualified. FALSE: The qualification conditions of the dependent operation cylcle have not been met.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - Always
     - E_OK is returned, as E_NOT_OK will never appear.

Dem_SetCycleQualified
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_SetCycleQualified(uint8 OperationCycleId)

Sets a dependent operation cycle as qualified, so it may be processed along with its leading cycle.

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
     - OperationCycleId
     - Identification of a configured DemOperationCycle.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - Always
     - E_OK is returned.

Dem_GetDTCSeverityAvailabilityMask
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_GetDTCSeverityAvailabilityMask(uint8 ClientId, Dem_DTCSeverityType *DTCSeverityMask)

Gets the DTC Severity availability mask.

**Sync/Async**
   Synchronous

**Reentrancy**
   Re-entrant for different ClientIDs, Non re-entrant for same ClientId.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - ClientId
     - Unique client id, assigned to the instance of the calling module.
   * - [out]
     - DTCSeverityMask
     - DTCSeverityMask The value DTCSeverityMask indicates the supported DTC severity bits from the Dem. All supported information is indicated by setting the corresponding status bit to 1. See ISO14229-1.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - get of DTC severity mask was successful
   * - E_NOT_OK
     - get of DTC severity mask failed

Dem_GetB1Counter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_GetB1Counter(uint16 *B1Counter)

Service to report the value of the B1 counter computed by the Dem. API is needed in WWH-OBD relevant ECUs only.

**Sync/Async**
   Synchronous

**Reentrancy**
   Re-entrant for different ClientIDs, Non re-entrant for same ClientId.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [out]
     - B1Counter
     - Buffer containing the B1 counter. The buffer is provided by the application with the size of 2 bytes.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - Always
     - E_OK is returned, as E_NOT_OK will never appear.

Dem_SetDTR
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_SetDTR(uint16 DTRId, sint32 TestResult, sint32 LowerLimit, sint32 UpperLimit, Dem_DTRControlType Ctrlval)

Reports a DTR result with lower and upper limit. The internal eventstatus serves as master whether the DTR values are forwarded or ignored, also taking the DTRUpdateKind into account. The EventId that is related to the DTR is assigned per configuration (and derived from ServiceNeeds). Processing takes enable/storage conditions into account. API is needed in OBD-relevant ECUs only. API Availability: This API will be available only if ({ecuc(Dem/DemGeneral.DemOBDSupport)} != DEM_OBD_NO_OBD_SUPPORT)

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant for different DTRIds. Non reentrant for the same DTRId.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - DTRId
     - Identification of a DTR element by assigned DTRId.
   * - [in]
     - TestResult
     - Test result of DTR
   * - [in]
     - LowerLimit
     - Lower limit of DTR
   * - [in]
     - UpperLimit
     - Upper limit of DTR
   * - [in]
     - Ctrlval
     - Control value of the DTR to support its interpretation Dem-internally.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Report of DTR result successful
   * - E_NOT_OK
     - Report of DTR result failed

Dem_MainFunction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Dem_MainFunction(void)

Processes all not event based Dem internal functions.

**Sync/Async**
   Synchronous

**Reentrancy**
   Non reentrant


**Return type**
   void


Dem_SatellitePreInit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Dem_SatellitePreInit(void)

Dem_SatellitePreInit is called directly for pre-initialization in case of single partition, or executed by the corresponding partition in case of multiple partitions.

**Sync/Async**
   Synchronous

**Reentrancy**
   Non reentrant


**Return type**
   void


Dem_SatelliteInit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Dem_SatelliteInit(void)

Dem_SatelliteInit is called directly for initialization in case of single partition, or executed by the corresponding partition in case of multiple partitions.

**Sync/Async**
   Synchronous

**Reentrancy**
   Non reentrant


**Return type**
   void


Dem_SatelliteMainFunction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Dem_SatelliteMainFunction(void)

Cyclic DemSatellite timer task. Processes all time debounce of satellite.

**Sync/Async**
   Synchronous

**Reentrancy**
   Non reentrant


**Return type**
   void


