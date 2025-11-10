提供给Dcm的函数(Functions provided to Dcm)
----------------------------------------------------------
Dem_SetDTCFilterByExtendedDataRecordNumber
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_SetDTCFilterByExtendedDataRecordNumber(uint8 ClientId, Dem_DTCFormatType DTCFormat, uint8 ExtendedDataRecordNumber)

Sets the DTC Filter based on a given extended data record on the primary fault memory. The server selects all DTCs that have a matching extended data record.

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
     - Unique client id, assigned to the instance of the calling module
   * - [in]
     - DTCFormat
     - Defines the DTC format of the requested data. Valid selections are DEM_DTC_FORMAT_UDS and DEM_DTC_FORMAT_OBD_3BYTE.
   * - [in]
     - ExtendedDataRecordNumber
     - the extended data record number the filter is set for. Valid values are within the range of 0x01 and 0xFD.

**Return type**
  Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - DTC filter for requested extended data record successfully set.
   * - E_NOT_OK
     - Indicates an invalid extended data record number was selected.

Dem_SetDTCFilterByReadinessGroup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_SetDTCFilterByReadinessGroup(uint8 ClientID, Dem_DTCFormatType DTCFormat, Dem_EventOBDReadinessGroupType ReadinessGroupNumber)

Sets the DTC Filter based on a given DTC readiness group on the primary fault memory. The server selects all DTCs that have this DTC readiness group configured.

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
   * - 
     - ClientID
     - 
   * - [in]
     - DTCFormat
     - Defines the DTC format of the requested data. Valid selections are DEM_DTC_FORMAT_UDS and DEM_DTC_FORMAT_OBD_3BYTE.
   * - [in]
     - ReadinessGroupNumber
     - Specifies the DTC readiness group number defined by SAE J1979-DA.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - DTC filter for requested DTC readiness group successfully set.
   * - E_NOT_OK
     - Indicates an invalid DTC readiness group was selected.

Dem_DcmGetInfoTypeValue08
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_DcmGetInfoTypeValue08(Dcm_OpStatusType OpStatus, uint8 *Iumprdata08, uint8 *Iumprdata08BufferSize)

Service is used for requesting IUMPR data according to InfoType $08. This interface is derived from the prototype <Module>_GetInfotypeValueData() defined by the Dcm. Therefore Dcm_OpStatusType and Std_ReturnType are contained. API is needed in OBD-relevant ECUs only. API Availability: This API will be available only if ({ecuc(Dem/DemGeneral.DemOBDSupport)} != DEM_OBD_NO_OBD_SUPPORT)

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
     - OpStatus
     - Only DCM_INITIAL will appear, because this API behaves synchronous.
   * - [out]
     - Iumprdata08
     - Buffer containing the number of data elements (as defined in ISO-15031-5) and contents of InfoType $08. The buffer is provided by the Dcm.
   * - [inout]
     - Iumprdata08BufferSize
     - The maximum number of data bytes that can be written to the Iumprdata08 Buffer. When the function returns, the value is updated with the actual number of data bytes that are written to the Iumprdata08BufferSize.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Always E_OK is returned.

Dem_DcmGetInfoTypeValue0B
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_DcmGetInfoTypeValue0B(Dcm_OpStatusType OpStatus, uint8 *Iumprdata0B, uint8 *Iumprdata0BBufferSize)

Service is used for requesting IUMPR data according to InfoType $0B. This interface is derived from the prototype <Module>_GetInfotypeValueData() defined by the Dcm. Therefore Dcm_OpStatusType and Std_ReturnType are contained. API is needed in OBD-relevant ECUs only. API Availability: This API will be available only if ({ecuc(Dem/DemGeneral.DemOBDSupport)} != DEM_OBD_NO_OBD_SUPPORT)

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
     - OpStatus
     - Only DCM_INITIAL will appear, because this API behaves synchronous.
   * - [out]
     - Iumprdata0B
     - Buffer containing the number of data elements (as defined in ISO-15031-5) and contents of InfoType $0B. The buffer is provided by the Dcm.
   * - [inout]
     - Iumprdata0BBufferSize
     - The maximum number of data bytes that can be written to the Iumprdata0B Buffer. When the function returns, the value is updated with the actual number of data bytes that are written to the Iumprdata0BBufferSize.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Always E_OK is returned.

Dem_DcmReadDataOfPID01
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_DcmReadDataOfPID01(uint8 *PID01value)

Service to report the value of PID $01 computed by the Dem. API is needed in OBD-relevant ECUs only. API Availability: This API will be available only if ({ecuc(Dem/DemGeneral.DemOBDSupport)} != DEM_OBD_NO_OBD_SUPPORT)

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
     - Buffer containing the contents of PID $01 computed by the Dem. The buffer is provided by the Dcm with the appropriate size, i.e. during configuration, the Dcm identifies the required size from the largest PID in order to configure a PIDBuffer.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Always E_OK is returned, as E_NOT_OK will never appear.

Dem_DcmReadDataOfPID1C
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_DcmReadDataOfPID1C(uint8 *PID1Cvalue)

Service to report the value of PID $1C computed by the Dem. API is needed in OBD-relevant ECUs only. API Availability: This API will be available only if ({ecuc(Dem/DemGeneral.DemOBDSupport)} != DEM_OBD_NO_OBD_SUPPORT)

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
     - PID1Cvalue
     - Buffer containing the contents of PID $1C computed by the Dem. The value of PID$1C is configuration within DemOBDCompliancy. The buffer is provided by the Dcm with the appropriate size, i.e. during configuration, the Dcm identifies the required size from the largest PID in order to configure a PIDBuffer.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Always E_OK is returned, as E_NOT_OK will never appear.

Dem_DcmReadDataOfPID21
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_DcmReadDataOfPID21(uint8 *PID21value)

Service to report the value of PID $21 computed by the Dem. API is needed in OBD-relevant ECUs only. API Availability: This API will be available only if ({ecuc(Dem/DemGeneral.DemOBDSupport)} != DEM_OBD_NO_OBD_SUPPORT)

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
     - Buffer containing the contents of PID $21 computed by the Dem. The value of PID$21 is configuration within DemOBDCompliancy. The buffer is provided by the Dcm with the appropriate size, i.e. during configuration, the Dcm identifies the required size from the largest PID in order to configure a PIDBuffer.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Always E_OK is returned, as E_NOT_OK will never appear.

Dem_DcmReadDataOfPID30
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_DcmReadDataOfPID30(uint8 *PID30value)

Service to report the value of PID $30 computed by the Dem. API is needed in OBD-relevant ECUs only. API Availability: This API will be available only if ({ecuc(Dem/DemGeneral.DemOBDSupport)} != DEM_OBD_NO_OBD_SUPPORT)

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
     - PID30value
     - Buffer containing the contents of PID $30 computed by the Dem. The value of PID$30 is configuration within DemOBDCompliancy. The buffer is provided by the Dcm with the appropriate size, i.e. during configuration, the Dcm identifies the required size from the largest PID in order to configure a PIDBuffer.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Always E_OK is returned, as E_NOT_OK will never appear.

Dem_DcmReadDataOfPID31
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_DcmReadDataOfPID31(uint8 *PID31value)

Service to report the value of PID $31 computed by the Dem. API is needed in OBD-relevant ECUs only. API Availability: This API will be available only if ({ecuc(Dem/DemGeneral.DemOBDSupport)} == DEM_OBD_MASTER_ECU)

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
     - PID31value
     - Buffer containing the contents of PID $31 computed by the Dem. The value of PID$31 is configuration within DemOBDCompliancy. The buffer is provided by the Dcm with the appropriate size, i.e. during configuration, the Dcm identifies the required size from the largest PID in order to configure a PIDBuffer.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Always E_OK is returned, as E_NOT_OK will never appear.

Dem_DcmReadDataOfPID41
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_DcmReadDataOfPID41(uint8 *PID41value)

Service to report the value of PID $41 computed by the Dem. API is needed in OBD-relevant ECUs only. API Availability: This API will be available only if ({ecuc(Dem/DemGeneral.DemOBDSupport)} == DEM_OBD_MASTER_ECU)

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
     - PID41value
     - Buffer containing the contents of PID $41 computed by the Dem. The value of PID$41 is configuration within DemOBDCompliancy. The buffer is provided by the Dcm with the appropriate size, i.e. during configuration, the Dcm identifies the required size from the largest PID in order to configure a PIDBuffer.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Always E_OK is returned, as E_NOT_OK will never appear.

Dem_DcmReadDataOfPID4D
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_DcmReadDataOfPID4D(uint8 *PID4Dvalue)

Service to report the value of PID $4D computed by the Dem. API is needed in OBD-relevant ECUs only. API Availability: This API will be available only if ({ecuc(Dem/DemGeneral.DemOBDSupport)} == DEM_OBD_MASTER_ECU)

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
     - PID4Dvalue
     - Buffer containing the contents of PID $4D computed by the Dem. The value of PID$4D is configuration within DemOBDCompliancy. The buffer is provided by the Dcm with the appropriate size, i.e. during configuration, the Dcm identifies the required size from the largest PID in order to configure a PIDBuffer.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Always E_OK is returned, as E_NOT_OK will never appear.

Dem_DcmReadDataOfPID4E
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_DcmReadDataOfPID4E(uint8 *PID4Evalue)

Service to report the value of PID $4E computed by the Dem. API is needed in OBD-relevant ECUs only. API Availability: This API will be available only if ({ecuc(Dem/DemGeneral.DemOBDSupport)} == DEM_OBD_MASTER_ECU)

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
     - PID4Evalue
     - Buffer containing the contents of PID $4E computed by the Dem. The value of PID$4E is configuration within DemOBDCompliancy. The buffer is provided by the Dcm with the appropriate size, i.e. during configuration, the Dcm identifies the required size from the largest PID in order to configure a PIDBuffer.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Always E_OK is returned, as E_NOT_OK will never appear.

Dem_DcmReadDataOfPID91
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_DcmReadDataOfPID91(uint8 *PID91value)

Service to report the value of PID $91 computed by the Dem. API is needed in OBD-relevant ECUs only. API Availability: This API will be available only if ({ecuc(Dem/DemGeneral.DemOBDSupport)} == DEM_OBD_MASTER_ECU)

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
     - PID91value
     - Buffer containing the contents of PID $91 computed by the Dem. The value of PID$91 is configuration within DemOBDCompliancy. The buffer is provided by the Dcm with the appropriate size, i.e. during configuration, the Dcm identifies the required size from the largest PID in order to configure a PIDBuffer.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Always E_OK is returned, as E_NOT_OK will never appear.

Dem_DcmReadDataOfOBDFreezeFrame
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_DcmReadDataOfOBDFreezeFrame(uint8 PID, uint8 DataElementIndexOfPID, uint8 *DestBuffer, uint16 *BufSize)

Gets data element per PID and index of the most important freeze frame being selected for the output of service $02. The function stores the data in the provided DestBuffer. API is needed in OBD-relevant ECUs only. API Availability: This API will be available only if ({ecuc(Dem/DemGeneral.DemOBDSupport)} != DEM_OBD_NO_OBD_SUPPORT)

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
     - PID
     - This parameter is an identifier for a PID as defined in ISO15031-5.
   * - [in]
     - DataElementIndexOfPID
     - Data element index of this PID according to the Dcm configuration of service $02. It is zero-based and consecutive, and ordered by the data element positions (configured in Dcm, refer to SWS_Dem_00597).
   * - [inout]
     - DestBuffer
     - This parameter contains a byte pointer that points to the buffer, to which the data element of the PID shall be written to. The format is raw hexadecimal values and contains no header-information.
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
     - Freeze frame data was successfully reported
   * - E_NOT_OK
     - Freeze frame data was not successfully reported

Dem_DcmGetDTCOfOBDFreezeFrame
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_DcmGetDTCOfOBDFreezeFrame(uint8 FrameNumber, uint32 *DTC, Dem_DTCFormatType DTCFormat)

Gets DTC by freeze frame record number. API is needed in OBD-relevant ECUs only. API Availability: This API will be available only if ({ecuc(Dem/DemGeneral.DemOBDSupport)} != DEM_OBD_NO_OBD_SUPPORT)

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
     - FrameNumber
     - Unique identifier for a freeze frame record as defined in ISO 15031-5. The value 0x00 indicates the complete OBD freeze frame. Other values are reserved for future functionality
   * - [out]
     - DTC
     - Diagnostic Trouble Code in ODB format. If the return value of the function is other than E_OK this parameter does not contain valid data.
   * - [in]
     - DTCFormat
     - Output format of the DTC value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - operation was successful
   * - E_NOT_OK
     - no DTC available

Dem_DcmGetAvailableOBDMIDs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_DcmGetAvailableOBDMIDs(uint8 Obdmid, uint32 *Obdmidvalue)

Reports the value of a requested "availability-OBDMID" to the DCM upon a Service $06 request. Derived from that the tester displays the supported tests a mechanic can select from. API is needed in OBD-relevant ECUs only. API Availability: This API will be available only if ({ecuc(Dem/DemGeneral.DemOBDSupport)} != DEM_OBD_NO_OBD_SUPPORT)

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
     - Obdmid
     - Availablity OBDMID ($00,$20, $40...)
   * - [out]
     - Obdmidvalue
     - Bit coded information on the support of OBDMIDs.

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

Dem_DcmGetNumTIDsOfOBDMID
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_DcmGetNumTIDsOfOBDMID(uint8 Obdmid, uint8 *numberOfTIDs)

Gets the number of TIDs per (functional) OBDMID. This can be used by the DCM to iteratively request for OBD/TID result data within a loop from 0....numberOfTIDs-1 API is needed in OBD-relevant ECUs only. API Availability: This API will be available only if ({ecuc(Dem/DemGeneral.DemOBDSupport)} != DEM_OBD_NO_OBD_SUPPORT)

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
     - Obdmid
     - OBDMID subject of the request to identify the number of assigned TIDs
   * - [out]
     - numberOfTIDs
     - Number of assigned TIDs for the requested OBDMID. Used as loop value for the DCM to retrieve all OBD/TID result data.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - get number of TIDs successful
   * - E_NOT_OK
     - get number of TIDs failed

Dem_DcmGetDTRData
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_DcmGetDTRData(uint8 Obdmid, uint8 TIDindex, uint8 *TIDvalue, uint8 *UaSID, uint16 *Testvalue, uint16 *Lowlimvalue, uint16 *Upplimvalue)

Reports a DTR data along with TID-value, UaSID, test result with lower and upper limit. API is needed in OBD-relevant ECUs only. API Availability: This API will be available only if ({ecuc(Dem/DemGeneral.DemOBDSupport)} != DEM_OBD_NO_OBD_SUPPORT)

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
     - Obdmid
     - Identification of a DTR element by assigned DTRId.
   * - [in]
     - TIDindex
     - Index of the TID within the DEM. Runs from 0 to "numberOfTIDs" obtained in the call to
   * - [out]
     - TIDvalue
     - TID to be put on the tester reponse
   * - [out]
     - UaSID
     - UaSID to be put on the tester reponse
   * - [out]
     - Testvalue
     - Latest test result
   * - [out]
     - Lowlimvalue
     - Lower limit value associated to the latest test result
   * - [out]
     - Upplimvalue
     - Upper limit value associated to the latest test result

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

Dem_DcmGetInfoTypeValue79
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_DcmGetInfoTypeValue79(Dcm_OpStatusType OpStatus, uint8 *DataValueBuffer, uint8 *DataValueBufferSize)

Service to report the value of monitor activity denominator PID computed by the Dem. API is needed in OBD-relevant ECUs only. API Availability: This API will be available only if: ({ecucDem/DemGeneral.DemOBDSupport)} != DEM_OBD_NO_OBD_SUPPORT)

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
     - OpStatus
     - OpStatus "Only DCM_INITIAL will appear, because this API behaves synchronous."
   * - [out]
     - DataValueBuffer
     - Buffer containing the contents of the monitor activity denominator. The buffer is provided by the caller with the appropriate size.
   * - [inout]
     - DataValueBufferSize
     - The maximum number of data bytes that can be written to the DataValueBuffer. When the function returns, the value is updated with the actual number of data bytes that are written to the Data ValueBuffer.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Always E_OK is returned

Dem_DcmReadDataOfPIDF501
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_DcmReadDataOfPIDF501(uint8 *PIDF501value)

Function to report the value of PID 0xF501 computed by the Dem. API is needed in OBD-relevant ECUs only. API Availability: This API will be available only if: ({ecucDem/DemGeneral.DemOBDSupport)} != DEM_OBD_NO_OBD_SUPPORT)

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
     - PIDF501value
     - Buffer containing the contents of the PID 0xF501. The buffer is provided by the Dcm with the appropriate size.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Always E_OK is returned

