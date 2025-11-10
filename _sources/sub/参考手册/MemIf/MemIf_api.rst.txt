类型定义(Type Definitions)
-------------------------------------------

.. list-table:: 
   :widths: 15 5 20
   :header-rows: 1

   * - Type Name
     - Type
     - Description

   * - MemIf_StatusType
     - enum
     - Denotes the current status of the underlying abstraction module and device drive.

   * - MemIf_JobResultType
     - enum
     - Denotes the result of the last job.

   * - MemIf_ModeType
     - enum
     - Denotes the mode type of the lower layer.(Reserved for compatibility with older versions of Mcal)


提供的服务(Services)
-------------------------------------------------
MemIf_Read
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType MemIf_Read(uint16 DeviceIndex, uint16 BlockNumber, uint16 BlockOffset, uint8 *DataBufferPtr, uint16 Length)

Invokes the "Read" function of the underlying memory abstraction module selected by the parameter DeviceIndex.

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
     - DeviceIndex
     - index number of device
   * - [in]
     - BlockNumber
     - number of logic block
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
     - The requested job has not been accepted by the module.

MemIf_Write
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType MemIf_Write(uint16 DeviceIndex, uint16 BlockNumber, const uint8 *DataBufferPtr)

Invokes the "Write" function of the underlying memory abstraction module selected by the parameter DeviceIndex.

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
     - DeviceIndex
     - index number of device
   * - [in]
     - BlockNumber
     - number of logic block
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
     - The requested job has not been accepted by the module.

MemIf_Cancel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void MemIf_Cancel(uint16 DeviceIndex)

Invokes the "Cancel" function of the underlying memory abstraction module selected by the parameter DeviceIndex.

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
     - DeviceIndex
     - index number of device

**Return type**
   void


MemIf_GetJobResult
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    MemIf_JobResultType MemIf_GetJobResult(uint16 DeviceIndex)

Invokes the "GetJobResult" function of the underlying memory abstraction module selected by the parameter DeviceIndex.

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
     - DeviceIndex
     - index number of device

**Return type**
    MemIf_JobResultType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - MEMIF_JOB_OK
     - The job has been finished successfully
   * - MEMIF_JOB_FAILED
     - The job has not been finished successfully
   * - MEMIF_JOB_PENDING
     - The job has not yet been finished.
   * - MEMIF_JOB_CANCELED
     - The job has been canceled.
   * - MEMIF_BLOCK_INCONSISTENT
     - 1. The requested block is inconsistent, it may contain corrupted data.
   * - MEMIF_BLOCK_INVALID
     - The requested block has been marked as invalid, the requested operation can not be performed.

MemIf_InvalidateBlock
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType MemIf_InvalidateBlock(uint16 DeviceIndex, uint16 BlockNumber)

Invokes the "InvalidateBlock" function of the underlying memory abstraction module selected by the parameter DeviceIndex.

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
     - DeviceIndex
     - index number of device
   * - [in]
     - BlockNumber
     - number of logic block

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
     - The requested job has not been accepted by the module.

MemIf_EraseImmediateBlock
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType MemIf_EraseImmediateBlock(uint16 DeviceIndex, uint16 BlockNumber)

Invokes the "EraseImmediateBlock" function of the underlying memory abstraction module selected by the parameter DeviceIndex.

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
     - DeviceIndex
     - index number of device
   * - [in]
     - BlockNumber
     - number of logic block

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
     - The requested job has not been accepted by the module.

MemIf_GetStatus
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    MemIf_StatusType MemIf_GetStatus(uint16 DeviceIndex)

Invokes the "GetStatus" function of the underlying memory abstraction module selected by the parameter DeviceIndex.

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
     - DeviceIndex
     - index number of device

**Return type**
    MemIf_StatusType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - MEMIF_UNINIT
     - The underlying abstraction module or device driver has not been initialized (yet).
   * - MEMIF_IDLE
     - The underlying abstraction module or device driver is currently idle.
   * - MEMIF_BUSY
     - The underlying abstraction module or device driver is currently busy.
   * - MEMIF_BUSY_INTERNAL
     - The underlying abstraction module is busy with internal management operations. The underlying device driver can be busy or idle.

MemIf_GetVersionInfo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void MemIf_GetVersionInfo(Std_VersionInfoType *VersionInfoPtr)

Returns version information.

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
     - Pointer to standard version information structure.

**Return type**
   void



