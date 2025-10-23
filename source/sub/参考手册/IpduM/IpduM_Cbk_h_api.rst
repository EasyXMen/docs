


      
提供的服务 Services
------------------------------------------------------------------
IpduM_RxIndication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void IpduM_RxIndication(PduIdType RxPduId, const PduInfoType *PduInfoPtr)

Indication of a received I-PDU from a lower layer communication interface module.

**Sync/Async**
   TRUE

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
     - RxPduId
     - ID of the received I-PDU.
   * - [in]
     - PduInfoPtr
     - Contains the length of the received I-PDU and a pointer to a buffer (SduDataPtr) containing the I-PDU.

**Return type**
   void


IpduM_TxConfirmation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void IpduM_TxConfirmation(PduIdType TxPduId, Std_ReturnType result)

The lower layer communication interface module confirms the transmission of an I-PDU.

**Sync/Async**
   TRUE

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
     - ID of the I-PDU that has been transmitted.
   * - [in]
     - result
     - result of confirmation.

**Return type**
   void


IpduM_TriggerTransmit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType IpduM_TriggerTransmit(PduIdType TxPduId, PduInfoType *PduInfoPtr)

The lower layer communication interface module confirms the transmission of an I-PDU.

**Sync/Async**
   TRUE

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
     - ID of the I-PDU that has been transmitted.
   * - [inout]
     - PduInfoPtr
     - Contains a pointer to a buffer (SduDataPtr) to where the SDU data shall be copied, and the available buffer size in SduLengh.On return, the service will indicate the length of the copied SDU data in SduLength.

**Return type**
   Std_ReturnType


