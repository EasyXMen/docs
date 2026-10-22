
类型定义
--------
.. 如果没有就不存在该章节，或为None

None

      
提供的服务
-----------
EthIf_RxIndication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void EthIf_RxIndication(uint8 CtrlIdx, Eth_FrameType FrameType, boolean IsBroadcast, const uint8 *PhysAddrPtr, const Eth_DataType *DataPtr, uint16 DataLen, TimeTupleType *IngressTimeTuplePtr, Eth_BufIdxType RxHandleId)

Receive indication of an Ethernet frame which was received by the indexed controller.

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
     - Index of the physical Ethernet controller within the context of the Ethernet Interface.
   * - [in]
     - FrameType
     - Frame type of received Ethernet frame.
   * - [in]
     - IsBroadcast
     - parameter to indicate a broadcast frame.
   * - [in]
     - PhysAddrPtr
     - Pointer to Physical source address (MAC address in network byte order) of received Ethernet frame.
   * - [in]
     - DataPtr
     - Pointer to payload of received Ethernet frame.
   * - [in]
     - DataLen
     - Length (bytes) of the payload in received frame.
   * - [in]
     - IngressTimeTuplePtr
     - Pointer to ingress timestamp provided as time tuple.
   * - [in]
     - RxHandleId
     - Unique receive handle id provided by the Ethernet Driver, to identify the ingress queue element per hysical Ethernet controller.

**Return type**
   void


EthIf_RxIndication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void EthIf_RxIndication(uint8 CtrlIdx, Eth_FrameType FrameType, boolean IsBroadcast, const uint8 *PhysAddrPtr, const Eth_DataType *DataPtr, uint16 DataLen)

Receive indication of an Ethernet frame which was received by the indexed controller.

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
     - Index of the physical Ethernet controller within the context of the Ethernet Interface.
   * - [in]
     - FrameType
     - Frame type of received Ethernet frame.
   * - [in]
     - IsBroadcast
     - parameter to indicate a broadcast frame.
   * - [in]
     - PhysAddrPtr
     - Pointer to Physical source address (MAC address in network byte order) of received Ethernet frame.
   * - [in]
     - DataPtr
     - Pointer to payload of received Ethernet frame.
   * - [in]
     - DataLen
     - Length (bytes) of the payload in received frame.

**Return type**
   void


EthIf_TxConfirmation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void EthIf_TxConfirmation(uint8 CtrlIdx, Eth_BufIdxType BufIdx, Std_ReturnType Result)

Confirms frame transmission by the indexed controller.

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
     - Index of the physical Ethernet controller within the context of the Ethernet Interface.
   * - [in]
     - BufIdx
     - Index of the transmitted buffer.
   * - [in]
     - Result
     - E_OK: The transmission was successful, E_NOT_OK: The transmission failed.

**Return type**
   void


EthIf_TxConfirmation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void EthIf_TxConfirmation(uint8 CtrlIdx, Eth_BufIdxType BufIdx)

Confirms frame transmission by the indexed controller.

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
     - Index of the physical Ethernet controller within the context of the Ethernet Interface.
   * - [in]
     - BufIdx
     - Index of the transmitted buffer.

**Return type**
   void


EthIf_CtrlModeIndication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void EthIf_CtrlModeIndication(uint8 CtrlIdx, Eth_ModeType CtrlMode)

Called asynchronously when mode has been read out.

**Sync/Async**
   Synchronous

**Reentrancy**
   Non Reentrant for the same CtrlIdx, reentrant for different

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - CtrlIdx
     - Index of the physical Ethernet controller within the context of the Ethernet Interface.
   * - [in]
     - CtrlMode
     - Notified Ethernet controller mode.

**Return type**
   void


EthIf_TrcvModeIndication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void EthIf_TrcvModeIndication(uint8 TrcvIdx, Eth_ModeType TrcvMode)

Called asynchronously when a mode change has been read out.

**Sync/Async**
   Synchronous

**Reentrancy**
   Non Reentrant for the same CtrlIdx, reentrant for different

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - TrcvIdx
     - Index of the Ethernet transceiver within the context of the Ethernet Interface.
   * - [in]
     - TrcvMode
     - Notified Ethernet transceiver mode.

**Return type**
   void


EthIf_SwitchPortModeIndication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void EthIf_SwitchPortModeIndication(uint8 SwitchIdx, uint8 SwitchPortIdx, Eth_ModeType PortMode)

The EthIf shall determine the expected notifications based on the EthSwtPort configuration. In case the EthSwtPort references an EthTrcv the EthIf expects a notification from the EthTrcv via API

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
     - SwitchIdx
     - Index of the switch.
   * - [in]
     - SwitchPortIdx
     - Index of the port at the addressed switch.
   * - [in]
     - PortMode
     - Notified Ethernet Switch port mode.

**Return type**
   void


EthIf_SleepIndication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void EthIf_SleepIndication(uint8 TrcvIdx)

This API is called by the corresponding EthTrcv, if a sleep indication was detected on the network.

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
     - TrcvIdx
     - Index of the Ethernet transceiver within the context of the Ethernet Interface.

**Return type**
   void


