
类型定义 Type Definitions
--------------------------------------------------------------------------------
.. 如果没有就不存在该章节，或为None

.. list-table::
   :widths: 15 5 20
   :header-rows: 1

   * - Type Name
     - Type
     - Description

   * - EthSM_NetworkModeStateType
     - enum
     - This type shall define the states of the network mode state machine.



提供的服务 Services
--------------------------------------------------------------------------------
EthSM_Init
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void EthSM_Init(void)

This function initialize the EthSM.

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant (Reentrant for different partitions. Non reentrant for the same partition.)

**Return type**
   void


EthSM_GetVersionInfo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void EthSM_GetVersionInfo(Std_VersionInfoType *versioninfo)

This service puts out the version information of this module.

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
     - versioninfo
     - Pointer where to put out the version information.

**Return type**
   void


EthSM_RequestComMode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthSM_RequestComMode(NetworkHandleType NetworkHandle, ComM_ModeType ComM_Mode)

Handles the communication mode and sets the Ethernet network active or passive.

**Sync/Async**
   Asynchronous

**Reentrancy**
   Reentrant (only for different Ethernet controllers)

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - NetworkHandle
     - Handle of destinated communication network for request
   * - [in]
     - ComM_Mode
     - Requested communication mode

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Controller mode request has been accepted
   * - E_NOT_OK
     - Controller mode request has not been accepted

EthSM_GetCurrentComMode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthSM_GetCurrentComMode(NetworkHandleType NetworkHandle, ComM_ModeType *ComM_ModePtr)

This service shall put out the current communication mode of a Ethernet network.

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
     - NetworkHandle
     - Network handle whose current communication mode shall be put out
   * - [out]
     - ComM_ModePtr
     - Pointer where to put out the current communication mode

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Service accepted
   * - E_NOT_OK
     - Service denied

EthSM_CtrlModeIndication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void EthSM_CtrlModeIndication(uint8 CtrlIdx, Eth_ModeType CtrlMode)

Called when mode has been read out.

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant (only for different Ethernet controllers)

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - CtrlIdx
     - Ethernet Interface Controller whose mode has changed
   * - [in]
     - CtrlMode
     - Notified Ethernet Interface Controller mode

**Return type**
   void


EthSM_TrcvLinkStateChg
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void EthSM_TrcvLinkStateChg(uint8 CtrlIdx, EthTrcv_LinkStateType TransceiverLinkState)

This service is called by the Ethernet Interface to report a transceiver link state change.

**Sync/Async**
   Synchronous (only for different Ethernet controllers)

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
     - CtrlIdx
     - Index of the Ethernet controller within the context of the Ethernet Interface
   * - [in]
     - TransceiverLinkState
     - Actual transceiver link state of the specific network handle

**Return type**
   void


