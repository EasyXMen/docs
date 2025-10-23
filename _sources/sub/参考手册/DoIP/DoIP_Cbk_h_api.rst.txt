
DoIP_SoAdTpCopyTxData
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    BEGIN_C_DECLS BufReq_ReturnType DoIP_SoAdTpCopyTxData(PduIdType soadTxPduId, const PduInfoType *pduInfoPtr, const RetryInfoType *retry, PduLengthType *availableDataPtr)

This function is called to acquire the transmit data of an I-PDU segment (N-PDU).Each call to this function provides the next part of the I-PDU data unless retry->TpDataState is TP_DATARETRY.

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
     - soadTxPduId
     - Identification of the transmitted I-PDU.
   * - [in]
     - pduInfoPtr
     - Provides the destination buffer (SduDataPtr) and the number of bytes to be copied (SduLength).
   * - [in]
     - retry
     - This parameter is used to acknowledge transmitted data or toretransmit data after transmission problems.
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

DoIP_SoAdTpTxConfirmation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void DoIP_SoAdTpTxConfirmation(PduIdType soadTxPduId, Std_ReturnType result)

Returns the version information of this module.

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
     - soadTxPduId
     - Identification of the transmitted I-PDU.
   * - [in]
     - result
     - E_OK: The PDU was transmitted. E_NOT_OK: Transmission of the PDU failed.

**Return type**
   void

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - None
     - 

DoIP_SoAdTpCopyRxData
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    BufReq_ReturnType DoIP_SoAdTpCopyRxData(PduIdType soadRxPduId, const PduInfoType *pduInfoPtr, PduLengthType *bufferSizePtr)

This function is called to provide the received data of an I-PDU segment (N-PDU) to the upper layer.

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
     - soadRxPduId
     - Identification of the received I-PDU.
   * - [in]
     - pduInfoPtr
     - Provides the source buffer (SduDataPtr) and the number of bytes to be copied (SduLength).
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

DoIP_SoAdTpStartOfReception
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    BufReq_ReturnType DoIP_SoAdTpStartOfReception(PduIdType soadRxPduId, const PduInfoType *pduInfoPtr, PduLengthType sduLen, PduLengthType *bufferSizePtr)

This function is called at the start of receiving an N-SDU. The N-SDU might be fragmented into multiple N-PDUs (FF with one or more following CFs) or might consist of a single N-PDU (SF).

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
     - soadRxPduId
     - Identification of the I-PDU.
   * - [in]
     - pduInfoPtr
     - Pointer to a PduInfoType structure containing the payload data (without protocol information) and payload length of the first frame or single frame of a transport protocol I-PDU reception..
   * - [in]
     - sduLen
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
     - Connection has been accepted. bufferSizePtr indicates the available receive buffer; reception is continued.
   * - BUFREQ_E_NOT_OK
     - Connection has been rejected; reception is aborted. bufferSizePtr remains unchanged.
   * - BUFREQ_E_OVFL
     - No buffer of the required length can be provided; reception is aborted. bufferSizePtr remains unchanged.

DoIP_SoAdTpRxIndication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void DoIP_SoAdTpRxIndication(PduIdType soadRxPduId, Std_ReturnType result)

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
     - soadRxPduId
     - Identification of the received I-PDU.
   * - [in]
     - result
     - E_OK: The PDU was received. E_NOT_OK: Reception of the PDU failed.

**Return type**
   void

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - None.
     - 

DoIP_SoAdIfRxIndication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void DoIP_SoAdIfRxIndication(PduIdType soadRxPduId, const PduInfoType *pduInfoPtr)

Indication of a received I-PDU from a lower layer communication interface module.

**Sync/Async**
   TRUE

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
     - soadRxPduId
     - Identification of the received I-PDU.
   * - [in]
     - pduInfoPtr
     - Contains the length (SduLength) of the received PDU, a pointer to a buffer (SduDataPtr) containing the PDU, and the MetaData related to this PDU.

**Return type**
   void

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - None.
     - 

DoIP_SoAdIfTxConfirmation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void DoIP_SoAdIfTxConfirmation(PduIdType soadTxPduId, Std_ReturnType result)

The lower layer communication interface module confirms the transmission of an I-PDU.

**Sync/Async**
   TRUE

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
     - soadTxPduId
     - ID of the I-PDU that has been transmitted.
   * - [in]
     - result
     - Result of the transmission.

**Return type**
   void

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - None.
     - 

DoIP_SoConModeChg
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void DoIP_SoConModeChg(SoAd_SoConIdType soConId, SoAd_SoConModeType mode)

Notification about a SoAd socket connection state change, e.g. socket connection gets online.

**Sync/Async**
   TRUE

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
     - soConId
     - socket connection index specifying the socket connection with the mode change.
   * - [in]
     - mode
     - new mode.

**Return type**
   void

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - None.
     - 

DoIP_LocalIpAddrAssignmentChg
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void DoIP_LocalIpAddrAssignmentChg(SoAd_SoConIdType soConId, TcpIp_IpAddrStateType state)

This function gets called by the SoAd if an IP address assignment related to a socket connection changes.

**Sync/Async**
   TRUE

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
     - soConId
     - socket connection index specifying the socket connection where the IP address assigment has changed
   * - [in]
     - state
     - state of IP address assignment.

**Return type**
   void

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - None.
     - 

