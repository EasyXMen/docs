提供给J1939Dcm的函数（Functions provided to J1939Dcm）
-------------------------------------------------------------------
Dem_J1939DcmSetDTCFilter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_J1939DcmSetDTCFilter(Dem_J1939DcmDTCStatusFilterType DTCStatusFilter, Dem_DTCKindType DTCKind, Dem_DTCOriginType DTCOrigin, uint8 ClientId, Dem_J1939DcmLampStatusType *LampStatus)

The function sets the DTC filter for a specific node and returns the composite lamp status of the filtered DTCs.

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
     - DTCStatusFilter
     - The following types are available: DEM_J1939DTC_ACTIVE DEM_J1939DTC_PREVIOUSLY_ACTIVE DEM_J1939DTC_PENDING DEM_J1939DTC_PERMANENT DEM_J1939DTC_CURRENTLY_ACTIVE
   * - [in]
     - DTCKind
     - Defines the functional group of DTCs to be reported (e.g. all DTC, OBD-relevant DTC)
   * - [in]
     - DTCOrigin
     - This parameter is used to select the source memory the DTCs shall be read/cleared from.
   * - [in]
     - ClientId
     - ClientId to address the J1939 event memory
   * - [out]
     - LampStatus
     - Receives the lamp status returned by this function. If the return value of the function is other than DEM_FILTERED_OK this parameter does not contain valid data.

**Return type**
    Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Operation successful
   * - E_NOT_OK
     - Filter could not be set

Dem_J1939DcmGetNumberOfFilteredDTC
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_J1939DcmGetNumberOfFilteredDTC(uint16 *NumberOfFilteredDTC, uint8 ClientId)

Gets the number of currently filtered DTCs set by the function Dem_J1939DcmSetDTCFilter.

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
   * - [out]
     - NumberOfFilteredDTC
     - The number of DTCs matching the defined status mask.
   * - [in]
     - ClientId
     - ClientId to address the J1939 event memory

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Operation successful
   * - E_NOT_OK
     - Operation successful and result pending.

Dem_J1939DcmGetNextFilteredDTC
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_J1939DcmGetNextFilteredDTC(uint32 *J1939DTC, uint8 *OccurenceCounter, uint8 ClientId)

Gets the next filtered J1939 DTC.

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
   * - [out]
     - J1939DTC
     - Receives the J1939DTC value. If the return value of the function is other than DEM_FILTERED_OK this parameter does not contain valid data.
   * - [out]
     - OccurenceCounter
     - This parameter receives the corresponding occurrence counter. If the return value of the function call is other than DEM_FILTERED_OK this parameter does not contain valid data.
   * - [in]
     - ClientId
     - ClientId to address the J1939 event memory

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Operation successful
   * - DEM_NO_SUCH_ELEMENT
     - The requested element is not available
   * - DEM_PENDING
     - Operation successful and result pending.
   * - DEM_BUFFER_TOO_SMALL
     - The provided buffer is too small

Dem_J1939DcmFirstDTCwithLampStatus
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Dem_J1939DcmFirstDTCwithLampStatus(uint8 ClientId)

The function sets the filter to the first applicable DTC for the DM31 response for a specific node.

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
     - ClientId to address the J1939 event memory

**Return type**
   void


Dem_J1939DcmGetNextDTCwithLampStatus
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_J1939DcmGetNextDTCwithLampStatus(Dem_J1939DcmLampStatusType *LampStatus, uint32 *J1939DTC, uint8 *OccurenceCounter, uint8 ClientId)

Gets the next filtered J1939 DTC for DM31 including current LampStatus.

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
     - LampStatus
     - Receives the lamp status returned by this function. If the return value of the function is other than DEM_FILTERED_OK this parameter does not contain valid data.
   * - [out]
     - J1939DTC
     - Receives the J1939DTC value. If the return value of the function is other than DEM_FILTERED_OK this parameter does not contain valid data.
   * - [out]
     - OccurenceCounter
     - This parameter receives the corresponding occurrence counter. If the return value of the function call is other than DEM_FILTERED_OK this parameter does not contain valid data.
   * - [in]
     - ClientId
     - ClientId to address the J1939 event memory

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Operation successful
   * - DEM_NO_SUCH_ELEMENT
     - The requested element is not available
   * - DEM_PENDING
     - Operation successful and result pending.
   * - DEM_BUFFER_TOO_SMALL
     - The provided buffer is too small

Dem_J1939DcmClearDTC
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_J1939DcmClearDTC(Dem_J1939DcmSetClearFilterType DTCTypeFilter, Dem_DTCOriginType DTCOrigin, uint8 ClientId)

Clears the status of all event(s) related to the specified DTC(s), as well as all associated event memory entries for these event(s).

**Sync/Async**
   Asynchronous

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
     - DTCTypeFilter
     - Defines the type of DTCs to be cleared.
   * - [in]
     - DTCOrigin
     - This parameter is used to select the source memory the DTCs shall be read/cleared from.
   * - [in]
     - ClientId
     - ClientId to address the J1939 event memory

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

Dem_J1939DcmSetFreezeFrameFilter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_J1939DcmSetFreezeFrameFilter(Dem_J1939DcmSetFreezeFrameFilterType FreezeFrameKind, uint8 ClientId)

The function sets the FreezeFrame filter for a specific node.

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
     - FreezeFrameKind
     - The following types are available: DEM_J1939DCM_FREEZEFRAME DEM_J1939DCM_EXPANDED_FREEZEFRAME DEM_J1939DCM_SPNS_IN_EXPANDED_FREEZEFRAME
   * - [in]
     - ClientId
     - ClientId to address the J1939 event memory

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Operation successful
   * - E_NOT_OK
     - Filter could not be set

Dem_J1939DcmGetNextFreezeFrame
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_J1939DcmGetNextFreezeFrame(uint32 *J1939DTC, uint8 *OccurenceCounter, uint8 *DestBuffer, uint16 *BufSize, uint8 ClientId)

Gets next freeze frame data. The function stores the data in the provided DestBuffer.

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
   * - [out]
     - J1939DTC
     - Receives the J1939DTC value. If the return value of the function is other than DEM_FILTERED_OK this parameter does not contain valid data.
   * - [out]
     - OccurenceCounter
     - This parameter receives the corresponding occurrence counter. If the return value of the function call is other than DEM_FILTERED_OK this parameter does not contain valid data.
   * - [inout]
     - DestBuffer
     - This parameter contains a byte pointer that points to the buffer, to swhich the freeze frame data record shall be written to.
   * - [inout]
     - BufSize
     - When the function is called this parameter contains the maximum number of data bytes that can be written to the buffer. The function returns the actual number of writtens data bytes in Dest Buffer
   * - [in]
     - ClientId
     - ClientId to address the J1939 event memory

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Operation successful
   * - DEM_NO_SUCH_ELEMENT
     - The requested element is not available
   * - DEM_PENDING
     - Operation successful and result pending.
   * - DEM_BUFFER_TOO_SMALL
     - The provided buffer is too small

Dem_J1939DcmGetNextSPNInFreezeFrame
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_J1939DcmGetNextSPNInFreezeFrame(uint32 *SPNSupported, uint8 *SPNDataLength, uint8 ClientId)

Gets next SPN.

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
   * - [out]
     - SPNSupported
     - This parameter contains the next SPN in the ExpandedFreezeFrame
   * - 
     - SPNDataLength
     - 
   * - [in]
     - ClientId
     - ClientId to address the J1939 event memory

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Operation successful
   * - DEM_NO_SUCH_ELEMENT
     - The requested element is not available
   * - DEM_PENDING
     - Operation successful and result pending.

Dem_J1939DcmSetRatioFilter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_J1939DcmSetRatioFilter(uint16 *IgnitionCycleCounter, uint16 *OBDMonitoringConditionsEncountered, uint8 ClientId)

The function sets the Ratio filter for a specific node and returns the corresponding Ignition Cycle Counter and General Denominator.

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
     - IgnitionCycleCounter
     - Ignition Cycle Counter
   * - [out]
     - OBDMonitoringConditionsEncountered
     - OBD Monitoring Conditions Encountered
   * - [in]
     - ClientId
     - ClientId to address the J1939 event memory

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Operation successful
   * - E_NOT_OK
     - Filter could not be set

Dem_J1939DcmGetNextFilteredRatio
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_J1939DcmGetNextFilteredRatio(uint32 *SPN, uint16 *Numerator, uint16 *Denominator, uint8 ClientId)

Gets the next filtered Ratio.

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
     - SPN
     - Receives the SPN of the applicaple system monitor. If the return value of the function is other than DEM_FILTERED_OK this parameter does not contain valid data.
   * - [out]
     - Numerator
     - Receives the Numerator of the applicable system monitor. If the return value of the function is other than DEM_FILTERED_OK this parameter does not contain valid data.
   * - [out]
     - Denominator
     - Receives the Denominator of the applicable system monitor. If the return value of the function is other than DEM_FILTERED_OK this parameter does not contain valid data.
   * - [in]
     - ClientId
     - ClientId to address the J1939 event memory

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Operation successful
   * - DEM_NO_SUCH_ELEMENT
     - The requested element is not available
   * - DEM_PENDING
     - Operation successful and result pending.
   * - DEM_BUFFER_TOO_SMALL
     - The provided buffer is too small

Dem_J1939DcmReadDiagnosticReadiness1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_J1939DcmReadDiagnosticReadiness1(Dem_J1939DcmDiagnosticReadiness1Type *DataValue, uint8 ClientId)

Service to report the value of Diagnostic Readiness 1 (DM05) computed by the Dem.

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
     - DataValue
     - Buffer of 8 bytes containing the contents of Diagnostic Readiness1 (DM05) computed by the Dem.
   * - [in]
     - ClientId
     - ClientId to address the J1939 event memory

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Operation successful
   * - E_NOT_OK
     - Operation failed

Dem_J1939DcmReadDiagnosticReadiness2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_J1939DcmReadDiagnosticReadiness2(Dem_J1939DcmDiagnosticReadiness2Type *DataValue, uint8 ClientId)

Service to report the value of Diagnostic Readiness 2 (DM21) computed by the Dem.

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
     - DataValue
     - Buffer of 8 bytes containing the contents of Diagnostic Readiness2 (DM21) computed by the Dem.
   * - [in]
     - ClientId
     - ClientId to address the J1939 event memory

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Operation successful
   * - E_NOT_OK
     - Operation failed

Dem_J1939DcmReadDiagnosticReadiness3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_J1939DcmReadDiagnosticReadiness3(Dem_J1939DcmDiagnosticReadiness3Type *DataValue, uint8 ClientId)

Service to report the value of Diagnostic Readiness 3 (DM26) computed by the Dem.

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
     - DataValue
     - Buffer of 8 bytes containing the contents of Diagnostic Readiness3 (DM26) computed by the Dem.
   * - [in]
     - ClientId
     - ClientId to address the J1939 event memory

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Operation successful
   * - E_NOT_OK
     - Operation failed

