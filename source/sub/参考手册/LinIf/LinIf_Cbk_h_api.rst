
LinIf_WakeupConfirmation
------------------------------

.. code::

    void LinIf_WakeupConfirmation(EcuM_WakeupSourceType WakeupSource)

The LIN Driver or LIN Transceiver Driver will call this function to report the wake up source after the successful wakeup detection during CheckWakeup or after power on by bus.

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
     - WakeupSource
     - Source device, which initiated the wakeup event: LIN controller or LIN transceiver.

**Return type**
   void


LinIf_HeaderIndication
------------------------------

.. code::

    Std_ReturnType LinIf_HeaderIndication(NetworkHandleType Channel, Lin_PduType *PduPtr)

The LIN Driver will call this function to report a received LIN header.This function is only applicable for LIN slave nodes.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant for different Channels.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - Channel
     - Identification of the LIN channel.
   * - [inout]
     - PduPtr
     - Pointer to PDU providing the received PID and pointer to the SDU data buffer as in parameter. Upon return, the length, checksum type and frame response type are received as out parameter. If the frame response type is LIN_FRAMERESPONSE_TX, then the SDU data buffer contains the transmission data.

**Return type**
   Std_ReturnType


LinIf_RxIndication
------------------------------

.. code::

    void LinIf_RxIndication(NetworkHandleType Channel, uint8 *Lin_SduPtr)

The LIN Driver will call this function to report a successfully received response and provides the reception data to the LIN Interface. This function is only applicable for LIN slave nodes.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant for different Channels.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - Channel
     - Identification of the LIN channel.
   * - [in]
     - Lin_SduPtr
     - pointer to a shadow buffer or memory mapped LIN Hardware receive buffer where the current SDU is stored. This pointer is only valid if the response is received.

**Return type**
   void


LinIf_TxConfirmation
------------------------------

.. code::

    void LinIf_TxConfirmation(NetworkHandleType Channel)

The LIN Driver will call this function to report a successfully transmitted response. This function is only applicable for LIN slave nodes.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant for different Channels.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - Channel
     - Identification of the LIN channel.

**Return type**
   void


LinIf_LinErrorIndication
------------------------------

.. code::

    void LinIf_LinErrorIndication(NetworkHandleType Channel, Lin_SlaveErrorType ErrorStatus)

The LIN Driver will call this function to report a detected error event during header or response processing This function is only applicable for LIN slave nodes.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant for different Channels.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - Channel
     - Identification of the LIN channel.
   * - [in]
     - ErrorStatus
     - Type of detected error.

**Return type**
   void


