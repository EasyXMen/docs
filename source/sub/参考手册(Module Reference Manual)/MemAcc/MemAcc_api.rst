类型定义
--------

.. list-table:: 
   :widths: 15 5 20
   :header-rows: 1

   * - Type Name
     - Type
     - Description

   * - MemAcc_AddressAreaIdType
     - uint16
     - Unique address area ID type @range 0..0xFFFF.

   * - MemAcc_AddressType
     - uint32
     - Logical memory address type @range 0..0xFFFFFFFF.

   * - MemAcc_LengthType
     - uint32
     - Job length type @range 0..0xFFFFFFFF.

   * - MemAcc_DataType
     - uint8
     - General data type @range 0..0xFF.

   * - MemAcc_HwIdType
     - uint32
     - Type for the unique numeric identifiers of all Mem hardware instances used for hardware specific requests @range 0..0xFFFFFFFF.

   * - MemAcc_MemoryInfoType
     - struct MemAcc_MemoryInfoTypeTag
     - This structure contains information of Mem device characteristics.

   * - MemAcc_JobInfoType
     - struct MemAcc_JobInfoTypeTag
     - This structure contains information the current processing state of the MemAcc module.

   * - MemAcc_MemJobResultType
     - enum
     - Asynchronous job result type.

   * - MemAcc_JobResultType
     - enum
     - Asynchronous job result type.

   * - MemAcc_JobStatusType
     - enum
     - Asynchronous job status type.

   * - MemAcc_JobType
     - enum
     - Type for asynchronous jobs.

   * - MemAcc_MemAddressType
     -  MemAcc_AddressType
     - Physical memory device address type @range 0..0xFFFFFFFF.

   * - MemAcc_MemConfigType
     - void
     - Memory driver configuration structure type @range NA.

   * - MemAcc_MemDataType
     - uint8
     - General data type @range 0..0xFF.

   * - MemAcc_MemInstanceIdType
     - uint32
     - Memory driver instance ID type @range 0..0xFFFFFFFF.

   * - MemAcc_MemLengthType
     -  MemAcc_LengthType
     - Physical memory device length type @range NA.

   * - MemAcc_MemHwServiceIdType
     - uint32
     - Index type for Mem driver hardware specific service table @range 0..0xFFFFFFFF.

   * - MemAcc_MemInitFuncType
     - void*
     - Function pointer for the Mem_Init service for the invocation of the Mem driver API via function pointer interface.

   * - MemAcc_MemDeInitFuncType
     - void*
     - Function pointer for the Mem_DeInit service for the invocation of the Mem driver API via function pointer interface.

   * - MemAcc_MemGetJobResultFuncType
     -  MemAcc_MemJobResultType
     - Function pointer for the Mem_JobResultType service for the invocation of the Mem driver API via function pointer interface.

   * - MemAcc_MemSuspendFuncType
     - void*
     - Function pointer for the Mem_Suspend service for the invocation of the Mem driver API via function pointer interface.

   * - MemAcc_MemResumeFuncType
     - void*
     - Function pointer for the Mem_Resume service for the invocation of the Mem driver API via function pointer interface.

   * - MemAcc_MemPropagateErrorFuncType
     - void*
     - Function pointer for the Mem_PropagateError service for the invocation of the Mem driver API via function pointer interface.

   * - MemAcc_MemReadFuncType
     - Std_ReturnType*
     - Function pointer for the Mem_Read service for the invocation of the Mem driver API via function pointer interface.

   * - MemAcc_MemWriteFuncType
     - Std_ReturnType*
     - Function pointer for the Mem_Write service for the invocation of the Mem driver API via function pointer interface.

   * - MemAcc_MemEraseFuncType
     - Std_ReturnType*
     - Function pointer for the Mem_Erase service for the invocation of the Mem driver API via function pointer interface.

   * - MemAcc_MemBlankCheckFuncType
     - Std_ReturnType*
     - Function pointer for the Mem_BlankCheck service for the invocation of the Mem driver API via function pointer interface.

   * - MemAcc_MemHwSpecificServiceFuncType
     - Std_ReturnType*
     - Function pointer for the Mem_HwSpecificService function for the invocation of the Mem driver API via function pointer interface.

   * - MemAcc_MemMainFuncType
     - void*
     - Function pointer for the Mem_MainFunction service for the invocation of the Mem driver API via function pointer interface.



提供的服务
-----------
MemAcc_Det_ReportError
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    MEMACC_LOCAL_INLINE void MemAcc_Det_ReportError(uint8 ApiId, uint8 ErrorId)

Report Develop Error.

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
     - ApiId
     - Specifies which API reported the error
   * - [in]
     - ErrorId
     - Specify which error was reported

**Return type**
   MEMACC_LOCAL_INLINE void


MemAcc_BurstFlagEnable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    MEMACC_LOCAL_INLINE boolean MemAcc_BurstFlagEnable(uint8 flag, uint8 type)

Check whether the flag is on.

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
     - flag
     - The check flag
   * - [in]
     - type
     - The reqeust type

**Return type**
   MEMACC_LOCAL_INLINE boolean


MemAcc_Init
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void MemAcc_Init(const MemAcc_ConfigType *configPtr)

Initialization function - initializes all variables and sets the module state to initialized.

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
     - configPtr
     - Pointer to configuration set

**Return type**
   void


MemAcc_DeInit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void MemAcc_DeInit(void)

Deinitialize module. If there are still access jobs pending, they are immediately terminated and the module state is set to unitialized. Therefore, MemAcc must be re-initialized before it will accept any new job requests after this service is processed.

**Sync/Async**
   Synchronous

**Reentrancy**
   Non Reentrant


**Return type**
   void


MemAcc_GetVersionInfo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void MemAcc_GetVersionInfo(Std_VersionInfoType *versionInfoPtr)

Service to return the version information of the MemAcc module.

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
     - versionInfoPtr
     - Pointer to where to store the version information of this module

**Return type**
   void


MemAcc_GetJobResult
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    MemAcc_JobResultType MemAcc_GetJobResult(MemAcc_AddressAreaIdType addressAreaId)

Returns the consolidated job result of the address area referenced by addressAreaId.

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
     - addressAreaId
     - Numeric identifier of address area

**Return type**
    MemAcc_JobResultType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - MEMACC_OK
     - The last MemAcc job was finished successfully
   * - MEMACC_FAILED
     - The last MemAcc job resulted in an unspecific failure and the job was not completed
   * - MEMACC_INCONSISTENT
     - The results of the last MemAcc job didn't meet the expected result
   * - MEMACC_CANCELED
     - The last MemAcc job was canceled
   * - MEMACC_ECC_UNCORRECTED
     - The last memory operation returned an uncorrectable ECC error
   * - MEMACC_ECC_CORRECTED
     - The last memory operation returned a correctable ECC error

MemAcc_GetJobStatus
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    MemAcc_JobStatusType MemAcc_GetJobStatus(MemAcc_AddressAreaIdType addressAreaId)

Returns the status of the MemAcc job referenced by addressAreaId.

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
     - addressAreaId
     - Numeric identifier of address area

**Return type**
    MemAcc_JobStatusType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - MEMACC_JOB_IDLE
     - Job processing was completed or no job currently pending
   * - MEMACC_JOB_PENDING
     - A job is currently being processed

MemAcc_GetMemoryInfo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType MemAcc_GetMemoryInfo(MemAcc_AddressAreaIdType addressAreaId, MemAcc_AddressType address, MemAcc_MemoryInfoType *memoryInfoPtr)

This service extern FUNCtion retrieves the physical memory device information of a specific address area. It can be used by an upper layer to get all necessary information to align the start address and trim the length for erase/write jobs.

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
     - addressAreaId
     - Numeric identifier of address area
   * - [in]
     - address
     - Address in logical address space from which corresponding memory device information shall be retrieved
   * - [out]
     - memoryInfoPtr
     - Destination memory pointer to store the memory device information

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The requested addressAreaId and address are valid
   * - E_NOT_OK
     - The requested addressAreaId and address are invalid

MemAcc_GetProcessedLength
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    MemAcc_LengthType MemAcc_GetProcessedLength(MemAcc_AddressAreaIdType addressAreaId)

Returns the accumulated number of bytes that have already been processed in the current job.

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
     - addressAreaId
     - Numeric identifier of address area

**Return type**
    MemAcc_LengthType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - uint32/uint64
     - 

MemAcc_GetJobInfo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void MemAcc_GetJobInfo(MemAcc_AddressAreaIdType addressAreaId, MemAcc_JobInfoType *jobInfoPtr)

Returns detailed information about the current memory job like memory device ID, job type, job, processing state or job result, address area as well as address and length. In case no job is pending on the referenced address area, the function returns the information of the last job.

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
     - addressAreaId
     - Numeric identifier of address area
   * - [out]
     - jobInfoPtr
     - Structure pointer to return the detailed processing information of the current job

**Return type**
   void


MemAcc_ActivateMem
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType MemAcc_ActivateMem(MemAcc_AddressType headerAddress, MemAcc_HwIdType hwId)

Dynamic activation and initialization of a Mem driver referenced by hwId and headerAddress.

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
     - headerAddress
     - Physical start address of Mem driver header structure
   * - [in]
     - hwId
     - Unique numeric memory driver identifier

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Mem driver activation successful
   * - E_NOT_OK
     - Mem driver activation failed

MemAcc_DeactivateMem
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType MemAcc_DeactivateMem(MemAcc_HwIdType hwId, MemAcc_AddressType headerAddress)

Dynamic deactivation of a Mem driver referenced by hwId and headerAddress.

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
     - hwId
     - Unique numeric memory driver identifier
   * - [in]
     - headerAddress
     - Physical start address of Mem driver header structure

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Mem driver deactivation successful
   * - E_NOT_OK
     - Mem driver deactivation failed

MemAcc_Cancel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void MemAcc_Cancel(MemAcc_AddressAreaIdType addressAreaId)

Triggers a cancel operation of the pending job for the address area referenced by the address AreaId. Cancelling affects only jobs in pending state. For any other states, the request will be ignored.

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
     - addressAreaId
     - Numeric identifier of address area

**Return type**
   void


MemAcc_Read
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType MemAcc_Read(MemAcc_AddressAreaIdType addressAreaId, MemAcc_AddressType sourceAddress, MemAcc_DataType *destinationDataPtr, MemAcc_LengthType length)

Triggers a read job to copy data from the source address into the referenced destination data buffer.

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
     - addressAreaId
     - Numeric identifier of address area
   * - [in]
     - sourceAddress
     - Read address in logical address space
   * - [out]
     - destinationDataPtr
     - Destination memory pointer to store the read data
   * - [in]
     - length
     - Read length in bytes (aligned to read page size)

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The requested job has been accepted by the module
   * - E_NOT_OK
     - The requested job has not been accepted by the module
   * - E_MEM_SERVICE_NOT_AVAIL
     - The underlying Mem driver service extern FUNCtion is not available

MemAcc_Write
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType MemAcc_Write(MemAcc_AddressAreaIdType addressAreaId, MemAcc_AddressType targetAddress, const MemAcc_DataType *sourceDataPtr, MemAcc_LengthType length)

Triggers a write job to store the passed data to the provided address area with given address and length.

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
     - addressAreaId
     - Numeric identifier of address area
   * - [in]
     - targetAddress
     - Write address in logical address space
   * - [in]
     - sourceDataPtr
     - Source data pointer (aligned to BufferAlignmentValue)
   * - [in]
     - length
     - Write length in bytes (aligned to page size)

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The requested job has been accepted by the module
   * - E_NOT_OK
     - The requested job has not been accepted by the module
   * - E_MEM_SERVICE_NOT_AVAIL
     - The underlying Mem driver service extern FUNCtion is not available

MemAcc_Erase
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType MemAcc_Erase(MemAcc_AddressAreaIdType addressAreaId, MemAcc_AddressType targetAddress, MemAcc_LengthType length)

Triggers an erase job of the given area. Triggers an erase job of the given area defined by targetAddress and length.

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
     - addressAreaId
     - Numeric identifier of address area
   * - [in]
     - targetAddress
     - Erase address in logical address space
   * - [in]
     - length
     - Erase length in bytes (aligned to sector size)

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The requested job has been accepted by the module
   * - E_NOT_OK
     - The requested job has not been accepted by the module
   * - E_MEM_SERVICE_NOT_AVAIL
     - The underlying Mem driver service extern FUNCtion is not available

MemAcc_Compare
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType MemAcc_Compare(MemAcc_AddressAreaIdType addressAreaId, MemAcc_AddressType sourceAddress, const MemAcc_DataType *dataPtr, MemAcc_LengthType length)

Triggers a job to compare the passed data to the memory content of the provided address area.

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
     - addressAreaId
     - Numeric identifier of address area
   * - [in]
     - sourceAddress
     - Compare address in logical address space
   * - [in]
     - dataPtr
     - Pointer to user data which shall be compared to data in memory
   * - [in]
     - length
     - Compare length in bytes

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The requested job has been accepted by the module
   * - E_NOT_OK
     - The requested job has not been accepted by the module
   * - E_MEM_SERVICE_NOT_AVAIL
     - The underlying Mem driver service extern FUNCtion is not available

MemAcc_BlankCheck
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType MemAcc_BlankCheck(MemAcc_AddressAreaIdType addressAreaId, MemAcc_AddressType targetAddress, MemAcc_LengthType length)

Checks if the passed address space is blank.

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
     - addressAreaId
     - Numeric identifier of address area
   * - [in]
     - targetAddress
     - Blank check address in logical address space
   * - [in]
     - length
     - Blank check length in bytes

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The requested job has been accepted by the module
   * - E_NOT_OK
     - The requested job has not been accepted by the module
   * - E_MEM_SERVICE_NOT_AVAIL
     - The underlying Mem driver service extern FUNCtion is not available

MemAcc_HwSpecificService
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType MemAcc_HwSpecificService(MemAcc_AddressAreaIdType addressAreaId, MemAcc_HwIdType hwId, MemAcc_MemHwServiceIdType hwServiceId, MemAcc_DataType *dataPtr, MemAcc_LengthType *lengthPtr)

Triggers a hardware specific job request referenced by hwServiceId.

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
     - addressAreaId
     - Numeric identifier of address area
   * - [in]
     - hwId
     - Unique numeric memory driver identifier
   * - [in]
     - hwServiceId
     - Array index pointing to the hardware specific service extern FUNCtion pointer
   * - [inout]
     - dataPtr
     - Data pointer pointing to the job buffer
   * - [inout]
     - lengthPtr
     - Size pointer of the data passed by dataPtr

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The requested job has been accepted by the module
   * - E_NOT_OK
     - The requested job has not been accepted by the module
   * - E_MEM_SERVICE_NOT_AVAIL
     - The underlying Mem driver service extern FUNCtion is not available

MemAcc_RequestLock
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType MemAcc_RequestLock(MemAcc_AddressAreaIdType addressAreaId, MemAcc_AddressType address, MemAcc_LengthType length, void *lockNotificationFctPtr)

Request lock of an address area for exclusive access.

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
     - addressAreaId
     - Numeric identifier of address area
   * - [in]
     - address
     - Logical start address of the address area to identify the Mem driver to be locked
   * - [in]
     - length
     - Length of the address area to identify the Mem driver to be locked
   * - [in]
     - lockNotificationFctPtr
     - Pointer to address area lock notification callback extern FUNCtion

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The requested job has been accepted by the module
   * - E_NOT_OK
     - The requested job has not been accepted by the module

MemAcc_ReleaseLock
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType MemAcc_ReleaseLock(MemAcc_AddressAreaIdType addressAreaId, MemAcc_AddressType address, MemAcc_LengthType length)

Release access lock of provided address area.

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
     - addressAreaId
     - Numeric identifier of address area
   * - [in]
     - address
     - Logical start address to identify lock area
   * - [in]
     - length
     - Length to identify lock area

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The requested job has been accepted by the module
   * - E_NOT_OK
     - The requested job has not been accepted by the module

