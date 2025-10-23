
类型定义 Type Definitions
--------------------------------------------------------------------------------

.. list-table:: 
   :widths: 15 5 20
   :header-rows: 1

   * - Type Name
     - Type
     - Description

   * - Eep_62_AddressType
     - uint32
     - Used as address offset from the configured EEPROM base address to access a certain EEPROM memory area @range NA.

   * - Eep_62_LengthType
     - uint16
     - Specifies the number of bytes to read/write/erase/compare @range NA.

   * - Eep_62_RuntimeType
     - struct Eep_62_RuntimeTypeTag
     - Prototype of EEprom driver routine.

   * - Eep_62_RequestJobType
     - enum
     - Define EEPROM module request job type.


      
提供的服务 Services
--------------------------------------------------------------------------------
Eep_Det_ReportError
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    EEP_62_LOCAL_INLINE void Eep_Det_ReportError(uint8 ApiId, uint8 ErrorId)

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
   EEP_62_LOCAL_INLINE void


Eep_Det_ReportRunTimeError
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    EEP_62_LOCAL_INLINE void Eep_Det_ReportRunTimeError(uint8 ApiId, uint8 ErrorId)

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
   EEP_62_LOCAL_INLINE void


Eep_62_CheckPartition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    EEP_62_LOCAL_INLINE boolean Eep_62_CheckPartition(void)

Check satellite partition current id.

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant


**Return type**
   EEP_62_LOCAL_INLINE boolean


Eep_62_Init
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Eep_62_Init(const Eep_62_ConfigType *ConfigPtr)

Service for EEPROM initialization.

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
     - Pointer to configuration set

**Return type**
   void


Eep_62_SetMode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Eep_62_SetMode(uint8 deviceIndex, MemIf_ModeType Mode)

Sets the mode.

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
     - deviceIndex
     - The used device index
   * - [in]
     - Mode
     - MEMIF_MODE_SLOW: Slow read access / normal SPI access. MEMIF_MODE_FAST: Fast read access / SPI burst access.

**Return type**
   void


Eep_62_Read
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Eep_62_Read(uint8 deviceIndex, Eep_62_AddressType EepromAddress, uint8 *DataBufferPtr, Eep_62_LengthType Length)

Reads from EEPROM.

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
     - deviceIndex
     - The used device index
   * - [in]
     - EepromAddress
     - Address offset in EEPROM (will be added to the EEPROM base address). Min.: 0 Max.: EEP_SIZE - 1
   * - [out]
     - DataBufferPtr
     - Pointer to destination data buffer in RAM
   * - [in]
     - Length
     - Number of bytes to read Min.: 1 Max.: EEP_SIZE - Eeprom Address

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - read command has been accepted
   * - E_NOT_OK
     - read command has not been accepted

Eep_62_Write
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Eep_62_Write(uint8 deviceIndex, Eep_62_AddressType EepromAddress, const uint8 *DataBufferPtr, Eep_62_LengthType Length)

Writes from EEPROM.

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
     - deviceIndex
     - The used device index
   * - [in]
     - EepromAddress
     - Address offset in EEPROM (will be added to the EEPROM base address). Min.: 0 Max.: EEP_SIZE - 1
   * - [in]
     - DataBufferPtr
     - Pointer to source data
   * - [in]
     - Length
     - Number of bytes to read Min.: 1 Max.: EEP_SIZE - Eeprom Address

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - write command has been accepted
   * - E_NOT_OK
     - write command has not been accepted

Eep_62_Erase
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Eep_62_Erase(uint8 deviceIndex, Eep_62_AddressType EepromAddress, Eep_62_LengthType Length)

Service for erasing EEPROM sections.

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
     - deviceIndex
     - The used device index
   * - [in]
     - EepromAddress
     - Address offset in EEPROM. Min.: 0 Max.: EEP_SIZE - 1
   * - [in]
     - Length
     - Number of bytes to read Min.: 1 Max.: EEP_SIZE - Eeprom Address

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - erase command has been accepted
   * - E_NOT_OK
     - erase command has not been accepted

Eep_62_Compare
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Eep_62_Compare(uint8 deviceIndex, Eep_62_AddressType EepromAddress, const uint8 *DataBufferPtr, Eep_62_LengthType Length)

Compares a data block in EEPROM with an EEPROM block in the memory.

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
     - deviceIndex
     - The used device index
   * - [in]
     - EepromAddress
     - Address offset in EEPROM (will be added to the EEPROM base address). Min.: 0 Max.: EEP_SIZE - 1
   * - [in]
     - DataBufferPtr
     - Pointer to data buffer (compare data)
   * - [in]
     - Length
     - Number of bytes to read Min.: 1 Max.: EEP_SIZE - Eeprom Address

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - compare command has been accepted
   * - E_NOT_OK
     - compare command has not been accepted

Eep_62_Cancel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Eep_62_Cancel(uint8 deviceIndex)

Cancels a running job.

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant


**Return type**
   void


Eep_62_GetStatus
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    MemIf_StatusType Eep_62_GetStatus(uint8 deviceIndex)

Returns the EEPROM status.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant


**Return type**
   MemIf_StatusType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - MEMIF_UNINIT
     - The module has not been initialized
   * - MEMIF_IDLE
     - The module is currently idle
   * - MEMIF_BUSY
     - The module is currently busy
   * - MEMIF_BUSY_INTERNAL
     - The module is busy with internal management operations.

Eep_62_GetJobResult
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    MemIf_JobResultType Eep_62_GetJobResult(uint8 deviceIndex)

This service returns the result of the last job.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant


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
     - The requested block has been invalidated, the requested read operation can not be

Eep_62_GetVersionInfo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Eep_62_GetVersionInfo(Std_VersionInfoType *versioninfo)

Service to get the version information of this module.

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
     - versioninfo
     - Pointer to where to store the version information of this module.

**Return type**
   void
   
Eep_62_JobEndNotification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    BEGIN_C_DECLS void Eep_62_JobEndNotification(void)

This callback function provided by the module user is called when a job has been completed with a positive result.

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant


**Return type**
    void


Eep_62_JobErrorNotification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Eep_62_JobErrorNotification(void)

This callback function provided by the module user is called when a job has been canceled or finished with negative result.

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant


**Return type**
   void