
类型定义 Type Definitions
------------------------------------------------------------------------

.. 如果没有就不存在该章节，或为None

.. list-table::
   :widths: 10 3 20
   :header-rows: 1

   * - Type Name
     - Type
     - Description

   * - CanTSyn_ConfigType
     - struct
     - This is the base type for the configuration of the Time Synchronization over CAN.

   * - CanTSyn_TransmissionModeType
     - enum
     - Handles the enabling and disabling of the transmission mode.


提供的服务 Services
------------------------------------------------------------------------

CanTSyn_Init
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void CanTSyn_Init(const CanTSyn_ConfigType *configPtr)

This function initializes the Time Synchronization over CAN.

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
     - Pointer to selected configuration structure

**Return type**
   void



CanTSyn_GetVersionInfo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void CanTSyn_GetVersionInfo(Std_VersionInfoType *versioninfoPtr)

This service returns the version information of this module.

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
     - versioninfoPtr
     - See Std_VersionInfoType

**Return type**
   void


CanTSyn_SetTransmissionMode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void CanTSyn_SetTransmissionMode(uint8 CtrlIdx, CanTSyn_TransmissionModeType Mode)

This API is used to turn on and off the TX capabilities of the CanTSyn.

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
     - CtrlIdx
     - Index of the CAN channel
   * - [in]
     - Mode
     - CANTSYN_TX_OFF CANTSYN_TX_ON

**Return type**
   void
