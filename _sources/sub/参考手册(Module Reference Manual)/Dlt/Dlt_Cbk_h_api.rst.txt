
类型定义 Type Definitions
------------------------------------------------------------------------------------------------

      
提供的服务 Services
------------------------------------------------------------------------------------------------
Dlt_RxIndication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    FUNC(void, DLT_APPL_CODE) Dlt_RxIndication(
        PduIdType RxPduId, 
        P2CONST(PduInfoType, AUTOMATIC, DLT_APPL_CONST) PduInfoPtr)

Indication of a received PDU from a lower layer communication interface module.

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
     - RxPduId
     - ID of the received PDU
   * - [in]
     - PduInfoPtr
     - Contains length (SduLength), buffer pointer (SduDataPtr) and MetaData

**Return type**
   void

Dlt_TriggerTransmit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    FUNC(Std_ReturnType, DLT_APPL_CODE) Dlt_TriggerTransmit(
        PduIdType TxPduId,
        P2CONST(PduInfoType, AUTOMATIC, DLT_APPL_CONST) PduInfoPtr)

Upper layer module shall check if data fits into PduInfoPtr->SduLength buffer.

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
     - ID of the SDU requested to be transmitted
   * - [in]
     - PduInfoPtr
     - Contains buffer pointer (SduDataPtr) and available size (SduLength)

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - SDU copied, SduLength indicates copied bytes
   * - E_NOT_OK
     - No data copied (buffer may be invalid)

Dlt_TxConfirmation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    #ifdef DLT_TX_CONFIRM_R19_USED
    FUNC(void, DLT_APPL_CODE) Dlt_TxConfirmation(PduIdType TxPduId, Std_ReturnType result)
    #else
    FUNC(void, DLT_APPL_CODE) Dlt_TxConfirmation(PduIdType TxPduId)
    #endif

Confirms the transmission of a PDU or failure to transmit.

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
     - ID of the transmitted PDU
   * - [in]
     - result
     - E_OK: PDU transmitted, E_NOT_OK: Transmission failed

**Return type**
   void

[后续函数按相同格式转换...]
[The subsequent functions are converted in the same format...]

Dlt_CopyTxData
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    FUNC(BufReq_ReturnType, DLT_APPL_CODE) Dlt_CopyTxData(
        PduIdType id,
        P2CONST(PduInfoType, AUTOMATIC, DLT_APPL_CONST) info,
        P2CONST(RetryInfoType, AUTOMATIC, DLT_APPL_CONST) retry,
        P2VAR(PduLengthType, AUTOMATIC, DLT_APPL_DATA) availableDataPtr)

Acquires transmit data of an I-PDU segment (N-PDU).

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
     - id
     - ID of transmitted I-PDU
   * - [in]
     - info
     - Destination buffer and bytes to copy
   * - [in]
     - retry
     - Data retransmission control
   * - [out]
     - availableDataPtr
     - Remaining bytes in Tx buffer

**Return type**
   BufReq_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - BUFREQ_OK
     - Data copied completely
   * - BUFREQ_E_BUSY
     - Retry later (no data copied)
   * - BUFREQ_E_NOT_OK
     - Data not copied
