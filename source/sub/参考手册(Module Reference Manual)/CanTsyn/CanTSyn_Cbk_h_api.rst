
类型定义 Type Definitions
------------------------------------------------------------------------
.. 如果没有就不存在该章节，或为None

None


提供的服务 Services
------------------------------------------------------------------------

CanTSyn_RxIndication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

   void CanTSyn_RxIndication(PduIdType RxPduId, const PduInfoType *PduInfoPtr)

Indication of a received PDU from a lower layer communication interface module.

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant(Reentrant for different PduIds. Non reentrant for the same PduId.)

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - RxPduId
     - ID of the received PDU.
   * - [in]
     - PduInfoPtr
     - Contains the length (SduLength) of the received PDU, a pointer to a buffer (SduDataPtr) containing the PDU, and the MetaData related to this PDU.

**Return type**
    void


CanTSyn_TxConfirmation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void CanTSyn_TxConfirmation(PduIdType TxPduId, Std_ReturnType result)

The lower layer communication interface module confirms the transmission of a PDU, or the failure to transmit a PDU.

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant(Reentrant for different PduIds. Non reentrant for the same PduId.)

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - TxPduId
     - ID of the PDU that has been transmitted.
   * - [in]
     - result
     - E_OK: The PDU was transmitted. E_NOT_OK: Transmission of the PDU failed.

**Return type**
   void
