
CanIf_ConfirmPnAvailability
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void CanIf_ConfirmPnAvailability(uint8 TransceiverId)

This service indicates that the transceiver is running in PN communication mode referring to the corresponding CAN transceiver with the abstract CanIf TransceiverId.

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
     - Abstract CanIf TransceiverId, which is assigned to a CAN transceiver, which was checked for PN availability.

**Return type**
    void


CanIf_ClearTrcvWufFlagIndication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void CanIf_ClearTrcvWufFlagIndication(uint8 TransceiverId)

This service indicates that the transceiver has cleared the WufFlag referring to the corresponding CAN transceiver with the abstract CanIf TransceiverId.

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
     - Abstract CanIf TransceiverId, which is assigned to a CAN transceiver, for which this function was called.

**Return type**
   void


CanIf_CheckTrcvWakeFlagIndication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void CanIf_CheckTrcvWakeFlagIndication(uint8 TransceiverId)

This service indicates that the check of the transceiver’s wake-up flag has been finished by the corresponding CAN transceiver with the abstract CanIf TransceiverId. This indication is used to cope with the asynchronous transceiver communication.

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
     - Abstract CanIf TransceiverId, which is assigned to a CAN transceiver, for which this function was called.

**Return type**
   void


CanIf_TrcvModeIndication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void CanIf_TrcvModeIndication(uint8 TransceiverId, CanTrcv_TrcvModeType TransceiverMode)

This service indicates a transceiver state transition referring to the corresponding CAN transceiver with the abstract CanIf TransceiverId.

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
     - Abstract CanIf TransceiverId, which is assigned to a CAN transceiver, which state has been transitioned.
   * - [in]
     - TransceiverMode
     - Mode to which the CAN transceiver transitioned.

**Return type**
   void


