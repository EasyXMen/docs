
CanIf_TriggerTransmit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType CanIf_TriggerTransmit(PduIdType TxPduId, PduInfoType *PduInfoPtr)

Within this API, the upper layer module (called module) shall check whether the available data fits into the buffer size reported by PduInfoPtr->SduLength. If it fits, it shall copy its data into the buffer provided by PduInfoPtr->SduDataPtr and update the length of the actual copied data in PduInfoPtr->SduLength. If not, it returns E_NOT_OK without changing PduInfoPtr.

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant for different PduIds. Non reentrant for the same PduId.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - TxPduId
     - ID of the SDU that is requested to be transmitted.
   * - [inout]
     - PduInfoPtr
     - Contains a pointer to a buffer (SduDataPtr) to where the SDU data shall be copied, and the available buffer size in SduLengh. On return, the service will indicate the length of the copied SDU data in SduLength.

**Return type**
    Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - SDU has been copied and SduLength indicates the number of copied bytes.
   * - E_NOT_OK
     - No SDU data has been copied. PduInfoPtr must not be used since it may contain a NULL pointer or point to invalid data.

CanIf_TxConfirmation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void CanIf_TxConfirmation(PduIdType CanTxPduId)

This service confirms a previously successfully processed transmission of a CAN TxPDU.

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
     - CanTxPduId
     - L-PDU handle of CAN L-PDU successfully transmitted.

**Return type**
   void


CanIf_RxIndication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void CanIf_RxIndication(const Can_HwType *Mailbox, const PduInfoType *PduInfoPtr)

This service indicates a successful reception of a received CAN Rx L-PDU to the CanIf after passing all filters and validation checks.

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
     - Mailbox
     - Identifies the HRH and its corresponding CAN Controller.
   * - [in]
     - PduInfoPtr
     - Pointer to the received L-PDU.

**Return type**
   void


CanIf_ControllerBusOff
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void CanIf_ControllerBusOff(uint8 ControllerId)

This service indicates a Controller BusOff event referring to the corresponding CAN Controller with the abstract CanIf ControllerId.

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
     - ControllerId
     - Abstract CanIf ControllerId which is assigned to a CAN controller, where a BusOff occured.

**Return type**
   void


CanIf_ControllerModeIndication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void CanIf_ControllerModeIndication(uint8 ControllerId, Can_ControllerStateType ControllerMode)

This service indicates a controller state transition referring to the corresponding CAN controller with the abstract CanIf ControllerId.

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
     - ControllerId
     - Abstract CanIf ControllerId which is assigned to a CAN controller, which state has been transitioned.
   * - [in]
     - ControllerMode
     - Mode to which the CAN controller transitioned.

**Return type**
   void


