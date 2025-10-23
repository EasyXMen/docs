接口描述（Interface Description）
========================================

类型定义（Type Definitions）
-------------------------------------

.. list-table:: 
   :widths: 15 5 20
   :header-rows: 1

   * - Type Name
     - Type
     - Description

   * - Fee_ConfigType
     - struct
     - Configuration data structure of the Fee module
      
提供的服务（Provided services）
------------------------------------------------

Fee_Init
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Fee_Init(const Fee_ConfigType *ConfigPtr)

Service to initialize the FEE module.

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
     - ConfigPtr
     - Pointer to the selected configuration set 

**Return type**
   void


Fee_SetMode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Fee_SetMode(MemIf_ModeType Mode)

Function to switch the mode of the underlying Flash Driver.

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
     - Mode
     - Desired mode for the underlying flash driver 

**Return type**
   void


Fee_Read
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Fee_Read(uint16 BlockNumber, uint16 BlockOffset, uint8 *DataBufferPtr, uint16 Length)

Service to initiate a read job.

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
     - BlockNumber
     - Number of logical block, also denoting start address of that block in flash memory 
   * - [in]
     - BlockOffset
     - Read address offset inside the block 
   * - [out]
     - DataBufferPtr
     - Pointer to data buffer 
   * - [in]
     - Length
     - Number of bytes to read 

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

Fee_Write
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Fee_Write(uint16 BlockNumber, const uint8 *DataBufferPtr)

Service to initiate a write job.

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
     - BlockNumber
     - Number of logical block, also denoting start address of that block in Flash EEPROM 
   * - [in]
     - DataBufferPtr
     - Pointer to data buffer 

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

Fee_Cancel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Fee_Cancel(void)

Service to call the cancel function of the underlying flash driver.

**Sync/Async**
   Asynchronous

**Reentrancy**
   Non Reentrant


**Return type**
   void


Fee_GetStatus
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    MemIf_StatusType Fee_GetStatus(void)

Service to return the status.

**Sync/Async**
   Synchronous

**Reentrancy**
   Non Reentrant


**Return type**
   MemIf_StatusType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - MEMIF_UNINIT
     - The FEE module has not been initialized 
   * - MEMIF_IDLE
     - The FEE module is currently idle 
   * - MEMIF_BUSY
     - The FEE module is currently busy 
   * - MEMIF_BUSY_INTERNAL
     - The FEE module is busy with internal management operations. 

Fee_GetJobResult
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    MemIf_JobResultType Fee_GetJobResult(void)

Service to query the result of the last accepted job issued by the upper layer software.

**Sync/Async**
   Synchronous

**Reentrancy**
   Non Reentrant


**Return type**
   MemIf_JobResultType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - MEMIF_JOB_OK
     - The last job has been finished successfully 
   * - MEMIF_JOB_PENDING
     - The last job is waiting for execution or currently being executed 
   * - MEMIF_JOB_CANCELED
     - The last job has been canceled (which means it failed) 
   * - MEMIF_JOB_FAILED
     - The last job has not been finished successfully (it failed) 
   * - MEMIF_BLOCK_INCONSISTENT
     - The requested block is inconsistent, it may contain corrupted data 
   * - MEMIF_BLOCK_INVALID
     - The requested block has been invalidated, the requested read operation can not be performed 

Fee_InvalidateBlock
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Fee_InvalidateBlock(uint16 BlockNumber)

Service to invalidate a logical block.

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
     - BlockNumber
     - Number of logical block, also denoting start address of that block in flash memory 

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

Fee_GetVersionInfo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Fee_GetVersionInfo(Std_VersionInfoType *VersionInfoPtr)

Service to return the version information of the FEE module.

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
     - VersionInfoPtr
     - Pointer to standard version information structure 

**Return type**
   void


Fee_EraseImmediateBlock
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Fee_EraseImmediateBlock(uint16 BlockNumber)

Service to erase a logical block.

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
     - BlockNumber
     - Number of logical block, also denoting start address of that block in EEPROM. 

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

Fee_MainFunction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code:: 

   void Fee_MainFunction(void)

Service to handle the requested read/write/erase jobs and the internal management operations.

**Sync/Async**
   Synchronous

**Reentrancy**
   Non Reentrant

**Parameters**

**Return type**
   void


回调函数（Callback Function）
-----------------------------------------------------

Fee_JobEndNotification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

   void Fee_JobEndNotification(void)

Service to report to this module the successful end of an asynchronous operation.

**Sync/Async**
   Synchronous

**Reentrancy**
   Non Reentrant


**Return type**
   void


依赖的服务（Dependent Services）
----------------------------------------------------------


强制接口（Mandatory Interface）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 10 5 30
   :header-rows: 1

   * - API Function
     - Header File
     - Description

   * - Det_ReportRuntimeError 
     - Det.h
     - Service to report runtime errors. If a callout has been configured then this callout shall be called.

   * - MemAcc_Cancel
     - MemAcc.h
     - Triggers a cancel operation of the pending job for the address area referenced by the addressAreaId. 
       Cancelling affects only jobs in pending state. For any other states, the request will be ignored.


   * - MemAcc_Compare (draft)
     - MemAcc.h
     - Triggers a job to compare the passed data to the memory content of the provided address area.
       The job terminates, if all bytes matched or a difference was detected. The result of this service
       can be retrieved using the MemAcc_GetJobResult() API. If the compare operation determined a mismatch,
       the result code is MEMACC_INCONSISTENT.


   * - MemAcc_Erase
     - MemAcc.h
     - Triggers an erase job of the given area.Triggers an erase job of the given area defined by targetAddress
       and length. The result of this service can be retrieved using the Mem_GetJobResult API. If the erase
       operation was successful, the result of the job is MEM_JOB_OK. If the erase operation failed, e.g. due to
       a hardware issue, the result of the job is MEM_JOB_FAILED.


   * - MemAcc_GetJobResult
     - MemAcc.h
     - Returns the consolidated job result of the address area referenced by addressAreaId.


   * - MemAcc_Read
     - MemAcc.h
     - Triggers a read job to copy data from the source address into the referenced destination data buffer.
       The result of this service can be retrieved using the MemAcc_GetJobResult API. If the read operation
       was successful, the result of the job is MEMACC_OK. If the read operation failed, the result of the
       job is either MEMACC_FAILED in case of a general error or MEMACC_ECC_CORRECTED/MEMACC_ECC_UNCORRECTED
       in case of a correctable/uncorrectable ECC error.


   * - MemAcc_Write
     - MemAcc.h
     - Triggers a write job to store the passed data to the provided address area with given address and length.
       The result of this service can be retrieved using the MemAcc_GetJobResult API. If the write operation was
       successful, the job result is MEMACC_OK. If there was an issue writing the data, the result is MEMACC_FAILED.


可选接口（Optional Interfaces）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 10 5 30
   :header-rows: 1

   * - Det_ReportError
     - .h
     - Service to report development errors.

   * - MemAcc_BlankCheck
     - MemAcc.h
     - Checks if the passed address space is blank, i.e. erased and writeable. The result of this service can be
       retrieved using the MemAcc_GetJobResult API. If the address area defined by targetAddress and length is
       blank, the result is MEMACC_OK, otherwise the result is MEMACC_INCONSISTENT.


配置函数（Configuration Functions）
-------------------------------------------

NvM_JobEndNotification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 10 5 30
   :header-rows: 1

   * - NvM_JobEndNotification
     - NvM_Cbk.h
     - Function to be used by the underlying memory abstraction to signal end of job without error.

   * - NvM_JobErrorNotification
     - NvM_Cbk.h
     - Function to be used by the underlying memory abstraction to signal end of job with error.
