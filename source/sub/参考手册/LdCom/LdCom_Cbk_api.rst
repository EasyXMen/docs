回调函数 Callback Function
------------------------------------------------------------------

      
提供的服务 Services
------------------------------------------------------------------
LdCom_CopyTxData
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    BufReq_ReturnType LdCom_CopyTxData(PduIdType id, const PduInfoType *info, const RetryInfoType *retry, PduLengthType *availableDataPtr)

Requests transmission of a signal.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant for different Ids. Non reentrant for the same Id.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - id
     - Identification of the transmitted I-PDU..
   * - [in]
     - info
     - Provides the destination buffer (SduDataPtr) and the number of bytes to be copied (SduLength).
   * - [in]
     - retry
     - This parameter is used to acknowledge transmitted data or to retransmit data after transmission problems.
   * - [out]
     - availableDataPtr
     - Indicates the remaining number of bytes that are available in the upper layer module's Tx buffer.

**Return type**
   BufReq_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - BUFREQ_OK
     - Data has been copied to the transmit buffer completely as requested.
   * - BUFREQ_E_BUSY
     - Request could not be fulfilled, because the required amount of Tx data is not available. The lower layer module may retry this call later on. No data has been copied.
   * - BUFREQ_E_NOT_OK
     - Data has not been copied. Request failed.

LdCom_TpTxConfirmation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void LdCom_TpTxConfirmation(PduIdType id, Std_ReturnType result)

This function is called after the I-PDU has been transmitted on its network, the result indicates whether the transmission was successful or not.

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
     - id
     - Identification of the transmitted I-PDU.
   * - [in]
     - result
     - E_OK: The PDU was transmitted. E_NOT_OK: Transmission of the PDU failed.

**Return type**
   void


LdCom_StartOfReception
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    BufReq_ReturnType LdCom_StartOfReception(PduIdType id, const PduInfoType *info, PduLengthType TpSduLength, PduLengthType *bufferSizePtr)

This function is called at the start of receiving an N-SDU..

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
     - id
     - Identification of the I-PDU.
   * - [in]
     - info
     - Pointer to a PduInfoType structure containing the payload data (without protocol information) and payload length of the first frame or single frame of a transport protocol I-PDU reception, and the MetaData related to this PDU. If neither first/single frame data nor MetaData are available, this parameter is set to NULL_PTR..
   * - [in]
     - TpSduLength
     - Total length of the N-SDU to be received.
   * - [out]
     - bufferSizePtr
     - Available receive buffer in the receiving module. This parameter will be used to compute the Block Size (BS) in the transport protocol module.

**Return type**
   BufReq_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - BUFREQ_OK
     - Connection has been accepted. bufferSizePtr indicates the available receive buffer; reception is continued. If no buffer of the requested size is available, a receive buffer size of 0 shall be indicated by bufferSizePtr.
   * - BUFREQ_E_NOT_OK
     - Connection has been rejected; reception is aborted. bufferSizePtr remains unchanged.
   * - BUFREQ_E_OVFL
     - No buffer of the required length can be provided; reception is aborted. bufferSizePtr remains unchanged.

LdCom_CopyRxData
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    BufReq_ReturnType LdCom_CopyRxData(PduIdType id, const PduInfoType *info, PduLengthType *bufferSizePtr)

This function is called to provide the received data of an I-PDU segment (N-PDU) to the upper layer. Each call to this function provides the next part of the I-PDU data. The size of the remaining buffer is written to the position indicated by bufferSizePtr.

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
     - id
     - Identification of the received I-PDU.
   * - [in]
     - info
     - Provides the source buffer (SduDataPtr) and the number of bytes to be copied(SduLength). An SduLength of 0 can be used to query the current amount of available buffer in the upper layer module. In this case, the SduDataPtr may be a NULL_PTR.
   * - [out]
     - bufferSizePtr
     - Available receive buffer after data has been copied.

**Return type**
   BufReq_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - BUFREQ_OK
     - Data copied successfully.
   * - BUFREQ_E_NOT_OK
     - Data was not copied because an error occurred.

LdCom_TpRxIndication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void LdCom_TpRxIndication(PduIdType id, Std_ReturnType result)

Called after an I-PDU has been received via the TP API, the result indicates whether the transmission was successful or not.

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
     - id
     - Identification of the received I-PDU
   * - [in]
     - result
     - E_OK: The PDU was received. E_NOT_OK: Reception of the PDU failed.

**Return type**
   void


LdCom_RxIndication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void LdCom_RxIndication(PduIdType RxPduId, const PduInfoType *PduInfoPtr)

Indication of a received PDU from a lower layer communication interface module.

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
     - ID of the received PDU.
   * - [in]
     - PduInfoPtr
     - Contains the length (SduLength) of the received PDU, a pointer to a buffer (SduDataPtr) containing the PDU, and the MetaData related to this PDU.

**Return type**
   void


LdCom_TxConfirmation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void LdCom_TxConfirmation(PduIdType TxPduId, Std_ReturnType result)

The lower layer communication interface module confirms the transmission of an IPDU, or the failure to transmit a PDU.

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
     - ID of the PDU that has been transmitted.
   * - [in]
     - result
     - E_OK: The PDU was transmitted. E_NOT_OK: Transmission of the PDU failed.

**Return type**
   void


LdCom_TriggerTransmit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType LdCom_TriggerTransmit(PduIdType TxPduId, PduInfoType *PduInfoPtr)

Copy the upper layer module(called module) data to be used the lower layer module transmission.

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
     - ID of the SDU that is requested to be transmitted.
   * - [inout]
     - PduInfoPtr
     - Contains a pointer to a buffer (SduDataPtr) to where the SDU data shall be copied, and the available buffer size in SduLengh.On return, the service will indicate the length of the copied SDU data in SduLength.

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

