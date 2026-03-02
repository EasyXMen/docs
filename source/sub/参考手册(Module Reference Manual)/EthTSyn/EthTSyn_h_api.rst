



提供的服务 Services
------------------------------------------------------------------
EthTSyn_Init
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void EthTSyn_Init(const EthTSyn_ConfigType *configPtr)

This function initializes the Time Synchronization over Ethernet.

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
     - Pointer to the selected configuration set.

**Return type**
   void


EthTSyn_GetVersionInfo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void EthTSyn_GetVersionInfo(Std_VersionInfoType *versioninfo)

Returns the version information of this module.

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
     - versioninfo
     - Pointer to the memory location holding the version information of the module.

**Return type**
   void


EthTSyn_SetTransmissionMode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void EthTSyn_SetTransmissionMode(uint8 ctrlIdx, EthTSyn_TransmissionModeType mode)

This API is used to turn on and off the TX capabilities of the EthTSyn.

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
     - ctrlIdx
     - Index of the Ethernet controller.
   * - [in]
     - mode
     - the mode of Transmission.

**Return type**
   void


EthTSyn_RxIndication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void EthTSyn_RxIndication(uint8 ctrlIdx, Eth_FrameType frameType, boolean isBroadcast, const uint8 *physAddrPtr, const uint8 *dataPtr, uint16 lenByte)

By this API service the EthTSyn gets an indication and the data of a received frame.

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
     - ctrlIdx
     - Index of the Ethernet controller.
   * - [in]
     - frameType
     - frame type of received Ethernet frame
   * - [in]
     - isBroadcast
     - parameter to indicate a broadcast frame
   * - [in]
     - physAddrPtr
     - pointer to Physical source address (MAC address in network byte
   * - [in]
     - dataPtr
     - Pointer to payload of the received Ethernet frame (i.e. Ethernet header is not provided).
   * - [in]
     - lenByte
     - Length of received data.

**Return type**
   void


EthTSyn_TxConfirmation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void EthTSyn_TxConfirmation(uint8 ctrlIdx, Eth_BufIdxType bufIdx, Std_ReturnType result)

Confirms the transmission of an Ethernet frame.

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
     - ctrlIdx
     - Index of the Ethernet controller within the context of the Ethernet Interface.
   * - [in]
     - bufIdx
     - Index of the buffer resource.
   * - [in]
     - result
     - E_OK: The transmission was successful, E_NOT_OK: The transmission failed.

**Return type**
   void


EthTSyn_TrcvLinkStateChg
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void EthTSyn_TrcvLinkStateChg(uint8 ctrlIdx, EthTrcv_LinkStateType trcvLinkState)

Allows resetting state machine in case of unexpected Link loss to avoid inconsistent Sync and Follow_Up sequences.

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
     - ctrlIdx
     - Index of the Ethernet controller within the context of the Ethernet Interface.
   * - [in]
     - trcvLinkState
     - ETHTRCV_LINK_STATE_DOWN ETHTRCV_LINK_STATE_ACTIVE

**Return type**
   void


EthTSyn_MainFunction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void EthTSyn_MainFunction(uint8 portIndex)

Main function for cyclic call/resp.Sync, Follow_Up and Pdelay_Req transmissions.

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
     - portIndex
     - Index of the configured Port.

**Return type**
   void
