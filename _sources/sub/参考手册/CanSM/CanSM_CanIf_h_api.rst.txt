
提供的服务（Provided services）
------------------------------------
CanSM_ControllerBusOff
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void CanSM_ControllerBusOff(uint8 ControllerId)

This callback function notifies the CanSM about a bus-off event on a certain CAN controller, which needs to be considered with the specified bus-off recovery handling for the impacted CAN network.

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant (only for different CanControllers)

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - ControllerId
     - CAN controller, which detected a bus-off event

**Return type**
    void


CanSM_ControllerModeIndication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void CanSM_ControllerModeIndication(uint8 ControllerId, Can_ControllerStateType ControllerMode)

This callback shall notify the CanSM module about a CAN controller mode change.

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant (only for different CAN controllers)

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - ControllerId
     - CAN controller, whose mode has changed
   * - [in]
     - ControllerMode
     - Notified CAN controller mode

**Return type**
   void


CanSM_TransceiverModeIndication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void CanSM_TransceiverModeIndication(uint8 TransceiverId, CanTrcv_TrcvModeType TransceiverMode)

This callback shall notify the CanSM module about a CAN transceiver mode change.

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant for different CAN Transceivers

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - TransceiverId
     - CAN transceiver, whose mode has changed
   * - [in]
     - TransceiverMode
     - Notified CAN transceiver mode

**Return type**
   void


CanSM_TxTimeoutException
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void CanSM_TxTimeoutException(NetworkHandleType Channel)

This function shall notify the CanSM module, that the CanNm has detected for the affected partial CAN network a tx timeout exception, which shall be recovered within the respective network state machine of the CanSM module.

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
     - Channel
     - Affected CAN network

**Return type**
   void


CanSM_ClearTrcvWufFlagIndication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void CanSM_ClearTrcvWufFlagIndication(uint8 Transceiver)

This callback function shall indicate the CanIf_ClearTrcvWufFlag API process end for the notified CAN Transceiver.

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant for different CAN Transceivers

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - Transceiver
     - Requested Transceiver

**Return type**
   void


CanSM_CheckTransceiverWakeFlagIndication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void CanSM_CheckTransceiverWakeFlagIndication(uint8 Transceiver)

This callback function indicates the CanIf_CheckTrcvWakeFlag API process end for the notified CAN Transceiver.

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant for different CAN Transceivers

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - Transceiver
     - Requested Transceiver

**Return type**
   void


CanSM_ConfirmPnAvailability
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void CanSM_ConfirmPnAvailability(uint8 TransceiverId)

This callback function indicates that the transceiver is running in PN communication mode.

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
     - TransceiverId
     - CAN transceiver, which was checked for PN availability

**Return type**
   void
