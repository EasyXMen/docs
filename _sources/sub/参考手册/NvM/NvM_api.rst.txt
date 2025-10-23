类型定义（Type definition）
--------------------------------------
.. list-table:: 
   :widths: 15 5 20
   :header-rows: 1

   * - Type Name
     - Type
     - Description

   * - NvM_InitBlockCallbackType
     - Std_ReturnType*
     - A pointer to initial callback function.

   * - NvM_SingleBlockCallbackType
     - Std_ReturnType*
     - A pointer to single block callback function.

   * - NvM_ReadRamBlockFromNvmCallbackType
     - Std_ReturnType*
     - A pointer to copy ram to ram mirror read callback function.

   * - NvM_WriteRamBlockToNvmCallbackType
     - Std_ReturnType*
     - A pointer to copy ram to ram mirror write callback function.

   * - NvM_MultiBlockCallbackType
     - void*
     - A pointer to multi block callback function.

   * - NvM_BlockCRCType
     - enum
     - Defines CRC data width for the NVRAM block.

   * - NvM_BlockManagementType
     - enum
     - Defines the block management type for the NVRAM block.

   * - NvM_MultiBlockRequestType
     - enum
     - Type of multitasking request.

   * - NvM_ServiceIdType
     - enum
     - Service Type Indicates the Id of a function service.



提供的服务（Provided services）
--------------------------------------------
NvM_JobEndNotification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    BEGIN_C_DECLS void NvM_JobEndNotification(void)

Function to be used by the underlying memory abstraction to signal end of job without error.

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant


**Return type**
    void


NvM_JobErrorNotification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void NvM_JobErrorNotification(void)

Function to be used by the underlying memory abstraction to signal end of job with error.

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant


**Return type**
   void

NvM_Init
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void NvM_Init(const NvM_ConfigType *ConfigPtr)

Service for resetting all internal variables.

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
     - ConfigPtr
     - Pointer to the selected configuration set

**Return type**
   void


NvM_GetVersionInfo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void NvM_GetVersionInfo(Std_VersionInfoType *VersionInfo)

Service to get the version information of the NvM module.

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
     - VersionInfo
     - Pointer to where to store the version information of this module

**Return type**
   void


NvM_GetErrorStatus
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType NvM_GetErrorStatus(NvM_BlockIdType BlockId, NvM_RequestResultType *RequestResultPtr)

Service to read the block dependent error/status information.

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
     - BlockId
     - The block identifier uniquely identifies one NVRAM block descriptor
   * - [out]
     - RequestResultPtr
     - Pointer to where to store the request result

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The block dependent error/status information was read successfully
   * - E_NOT_OK
     - An error occured

NvM_SetRamBlockStatus
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType NvM_SetRamBlockStatus(NvM_BlockIdType BlockId, boolean BlockChanged)

Service for setting the RAM block status of a permanent RAM block or the status of the explicit synchronization of a NVRAM block.

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
     - BlockId
     - The block identifier uniquely identifies one NVRAM block descriptor
   * - [in]
     - BlockChanged
     - TRUE : Validate the RAM block and mark block as changed

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The status of the permanent RAM block or the explicit synchronization was changed as requested
   * - E_NOT_OK
     - An error occurred

NvM_CancelWriteAll
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void NvM_CancelWriteAll(void)

Service to cancel a running NvM_WriteAll request.

**Sync/Async**
   FALSE

**Reentrancy**
   Non Reentrant


**Return type**
   void


NvM_ReadAll
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void NvM_ReadAll(void)

Initiates a multi block read request.

**Sync/Async**
   FALSE

**Reentrancy**
   Non Reentrant


**Return type**
   void


NvM_WriteAll
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void NvM_WriteAll(void)

Initiates a multi block write request.

**Sync/Async**
   FALSE

**Reentrancy**
   Non Reentrant


**Return type**
   void


NvM_FirstInitAll
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void NvM_FirstInitAll(void)

The function initiates a multi block first initialization request.

**Sync/Async**
   FALSE

**Reentrancy**
   Non Reentrant


**Return type**
   void


NvM_WritePRAMBlock
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType NvM_WritePRAMBlock(NvM_BlockIdType BlockId)

Service to copy the data of the permanent RAM block to its corresponding NV block.

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
     - BlockId
     - The block identifier uniquely identifies one NVRAM block descriptor.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - request has been accepted
   * - E_NOT_OK
     - request has not been accepted

NvM_RestorePRAMBlockDefaults
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType NvM_RestorePRAMBlockDefaults(NvM_BlockIdType BlockId)

Service to restore the default data to its corresponding permanent RAM block.

**Sync/Async**
   FALSE

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
     - The block identifier uniquely identifies one NVRAM block descriptor

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - request has been accepted
   * - E_NOT_OK
     - request has not been accepted

NvM_SetDataIndex
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType NvM_SetDataIndex(NvM_BlockIdType BlockId, uint8 DataIndex)

Service for setting the DataIndex of a dataset NVRAM block.

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
     - BlockId
     - The block identifier uniquely identifies one NVRAM block descriptor
   * - [in]
     - DataIndex
     - Index of a dataset NVRAM block

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The index position was set successfully
   * - E_NOT_OK
     - An error occurred

NvM_GetDataIndex
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType NvM_GetDataIndex(NvM_BlockIdType BlockId, uint8 *DataIndexPtr)

Service for getting the currently set DataIndex of a dataset NVRAM block.

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
     - BlockId
     - The block identifier uniquely identifies one NVRAM block descriptor
   * - [out]
     - DataIndexPtr
     - Pointer to where to store the current dataset index (0..255)

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The index position has been retrieved successfully
   * - E_NOT_OK
     - An error occurred

NvM_ReadPRAMBlock
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType NvM_ReadPRAMBlock(NvM_BlockIdType BlockId)

Service to copy the data of the NV block to its corresponding permanent RAM block.

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
     - BlockId
     - The block identifier uniquely identifies one NVRAM block descriptor

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - request has been accepted
   * - E_NOT_OK
     - request has not been accepted

NvM_ReadBlock
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType NvM_ReadBlock(NvM_BlockIdType BlockId, void *NvM_DstPtr)

Service to copy the data of the NV block to its corresponding RAM block.

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
     - BlockId
     - The block identifier uniquely identifies one NVRAM block descriptor
   * - [in]
     - NvM_DstPtr
     - Pointer to the RAM data block

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - request has been accepted
   * - E_NOT_OK
     - request has not been accepted

NvM_WriteBlock
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType NvM_WriteBlock(NvM_BlockIdType BlockId, const void *NvM_SrcPtr)

Service to copy the data of the RAM block to its corresponding NV block.

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
     - BlockId
     - The block identifier uniquely identifies one NVRAM block descriptor
   * - [in]
     - NvM_SrcPtr
     - Pointer to the RAM data block

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - request has been accepted
   * - E_NOT_OK
     - request has not been accepted

NvM_RestoreBlockDefaults
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType NvM_RestoreBlockDefaults(NvM_BlockIdType BlockId, void *NvM_DestPtr)

Service to restore the default data to its corresponding RAM block.

**Sync/Async**
   FALSE

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
     - The block identifier uniquely identifies one NVRAM block descriptor
   * - [in]
     - NvM_DestPtr
     - Pointer to the RAM data block

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - request has been accepted
   * - E_NOT_OK
     - request has not been accepted

NvM_CancelJobs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType NvM_CancelJobs(NvM_BlockIdType BlockId)

Service to cancel all jobs pending for a NV block.

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
     - BlockId
     - The block identifier uniquely identifies one NVRAM block descriptor

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The job was successfully removed from queue
   * - E_NOT_OK
     - The job could not be found in the queue

NvM_ValidateAll
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void NvM_ValidateAll(void)

Initiates a multi block validation request.

**Sync/Async**
   FALSE

**Reentrancy**
   Non Reentrant


**Return type**
   void


NvM_SetBlockProtection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType NvM_SetBlockProtection(NvM_BlockIdType BlockId, boolean ProtectionEnabled)

Service for setting/resetting the write protection for a NV block.

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
     - BlockId
     - The block identifier uniquely identifies one NVRAM block descriptor
   * - [in]
     - ProtectionEnabled
     - TRUE : Write protection shall be enabled FALSE: Write protection shall be disabled

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The block was enabled/disabled as requested
   * - E_NOT_OK
     - An error occurred

NvM_InvalidateNvBlock
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType NvM_InvalidateNvBlock(NvM_BlockIdType BlockId)

Service to invalidate a NV block.

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
     - BlockId
     - The block identifier uniquely identifies one NVRAM block descriptor

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - request has been accepted
   * - E_NOT_OK
     - request has not been accepted

NvM_EraseNvBlock
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType NvM_EraseNvBlock(NvM_BlockIdType BlockId)

Service to erase a NV block.

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
     - BlockId
     - The block identifier uniquely identifies one NVRAM block descriptor

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - request has been accepted
   * - E_NOT_OK
     - request has not been accepted
