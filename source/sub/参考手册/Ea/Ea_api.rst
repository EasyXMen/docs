
类型定义 Type Definitions
--------------------------------------------------------------------------------

.. list-table:: 
   :widths: 15 5 20
   :header-rows: 1

   * - Type Name
     - Type
     - Description

   * - Ea_ConfigType
     - struct
     - Configuration data structure of the Ea module
      

      
提供的服务 Services
--------------------------------------------------------------------------------
Ea_Det_ReportError
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    EA_LOCAL_INLINE void Ea_Det_ReportError(uint8 ApiId, uint8 ErrorId)

Report Develop Error.

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
     - ApiId
     - Specifies which API reported the error.
   * - [in]
     - ErrorId
     - Specify which error was reported.

**Return type**
   EA_LOCAL_INLINE void


Ea_Det_ReportRunTimeError
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    EA_LOCAL_INLINE void Ea_Det_ReportRunTimeError(uint8 ApiId, uint8 ErrorId)

Report Running Time Error.

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
     - ApiId
     - Specifies which API reported the error.
   * - [in]
     - ErrorId
     - Specify which error was reported.

**Return type**
   EA_LOCAL_INLINE void


Ea_Init
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Ea_Init(const Ea_ConfigType *ConfigPtr)

Initializes the EEPROM abstraction module.

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


Ea_Read
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Ea_Read(uint16 BlockNumber, uint16 BlockOffset, uint8 *DataBufferPtr, uint16 Length)

Reads Length bytes of block BlockNumber at offset BlockOffset into the buffer DataBufferPtr.

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
     - BlockNumber
     - Number of logical block, also denoting start address of that block in EEPROM.
   * - [in]
     - BlockOffset
     - Read address offset inside the block(read offset within block)
   * - [out]
     - DataBufferPtr
     - Pointer to data buffer
   * - [in]
     - Length
     - Number of bytes to read(Length of read job)

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

Ea_Write
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Ea_Write(uint16 BlockNumber, const uint8 *DataBufferPtr)

Writes the contents of the DataBufferPtr to the block BlockNumber.

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
     - BlockNumber
     - Number of logical block, also denoting start address of that block in EEPROM
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

Ea_Cancel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Ea_Cancel(void)

Cancels the ongoing asynchronous operation.

**Sync/Async**
   FALSE

**Reentrancy**
   Non Reentrant


**Return type**
   void


Ea_GetStatus
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    MemIf_StatusType Ea_GetStatus(void)

Service to return the status.

**Sync/Async**
   TRUE

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
     - The EA module has not been initialized
   * - MEMIF_IDLE
     - The EA module is currently idle
   * - MEMIF_BUSY
     - The EA module is currently busy
   * - MEMIF_BUSY_INTERNAL
     - The EA module is busy with internal management operations.

Ea_GetJobResult
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    MemIf_JobResultType Ea_GetJobResult(void)

Service to return the job result.

**Sync/Async**
   TRUE

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

Ea_InvalidateBlock
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Ea_InvalidateBlock(uint16 BlockNumber)

Invalidates the block BlockNumber.

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
     - BlockNumber
     - Number of logical block, also denoting start address of that block in EEPROM

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
     - - only if DET is enabled: The requested job has not been accepted by the EA module.

Ea_GetVersionInfo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Ea_GetVersionInfo(Std_VersionInfoType *VersionInfoPtr)

Service to get the version information of EA module.

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
     - VersionInfoPtr
     - Pointer to standard version information structure

**Return type**
   void


Ea_EraseImmediateBlock
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Ea_EraseImmediateBlock(uint16 BlockNumber)

Erases the block BlockNumber.

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
     - - only if DET is enabled: The requested job has not been accepted by the EA module.

Ea_JobEndNotification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Ea_JobEndNotification(void)

Service to report to this module the successful end of an asynchronous operation.

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant


**Return type**
   void


