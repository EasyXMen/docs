接口描述（Interface Description）
==========================================

类型定义（Type Definitions）
---------------------------------------------
.. include:: PduR_Types_h_api.rst

None

      
提供的服务（Provided Services）
------------------------------------------------
PduR_Init
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void PduR_Init(const PduR_PBConfigType *ConfigPtr)

Initializes the PDU Router.

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
     - ConfigPtr
     - Pointer to Post build configuration data.

**Return type**
   void


PduR_GetVersionInfo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void PduR_GetVersionInfo(Std_VersionInfoType *versionInfo)

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
   * - [out]
     - versionInfo
     - Pointer to where to store the version information of this module.

**Return type**
   void


PduR_GetConfigurationId
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    PduR_PBConfigIdType PduR_GetConfigurationId(void)

Returns the unique identifier of the post-build time configuration of the PDU Router.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant


**Return type**
   PduR_PBConfigIdType


PduR_EnableRouting
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void PduR_EnableRouting(PduR_RoutingPathGroupIdType id)

Enables a routing path group.

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
     - Identification of the routing path group. Routing path groups are defined in the PDU router configuration.

**Return type**
   void


PduR_DisableRouting
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void PduR_DisableRouting(PduR_RoutingPathGroupIdType id, boolean initialize)

Disables a routing path group.

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
     - Identification of the routing path group. Routing path groups are defined in the PDU router configuration.
   * - [in]
     - initialize
     - true : initialize single buffers to the default value false : retain current value of single buffers

**Return type**
   void


PduR_Transmit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType PduR_Transmit(PduIdType TxPduId, const PduInfoType *PduInfoPtr)

Requests transmission of a PDU.

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
     - Identifier of the PDU to be transmitted
   * - [in]
     - PduInfoPtr
     - Length of and pointer to the PDU data and pointer to MetaData.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Transmit request has been accepted.
   * - E_NOT_OK
     - Transmit request has not been accepted.

PduR_CancelTransmit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType PduR_CancelTransmit(PduIdType TxPduId)

Requests cancellation of an ongoing transmission of a PDU in a lower layer communication module.

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
     - Identifier of the PDU to be transmitted

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Cancellation was executed successfully by the destination module.
   * - E_NOT_OK
     - Cancellation was rejected by the destination module.

PduR_CancelReceive
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType PduR_CancelReceive(PduIdType RxPduId)

Requests cancellation of an ongoing reception of a PDU in a lower layer transport protocol module.

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
     - RxPduId
     - Identification of the PDU to be cancelled.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Cancellation was executed successfully by the destination module.
   * - E_NOT_OK
     - Cancellation was rejected by the destination module.

PduR_IfRxIndication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void PduR_IfRxIndication(PduIdType RxPduId, const PduInfoType *PduInfoPtr)

Indication of a received PDU from a lower layer communication interface module.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant for different PduIds. Non reentrant for the same PduId

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


PduR_IfTxConfirmation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void PduR_IfTxConfirmation(PduIdType TxPduId, Std_ReturnType result)

The lower layer communication interface module confirms the transmission of a PDU, or the failure to transmit a PDU.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant for different PduIds. Non reentrant for the same PduId

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
     - E_OK : The PDU was transmitted. E_NOT_OK : Transmission of the PDU failed.

**Return type**
   void


PduR_IfTriggerTransmit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType PduR_IfTriggerTransmit(PduIdType TxPduId, PduInfoType *PduInfoPtr)

Within this API, the upper layer module (called module) shall check whether the available data fits into the buffer size reported by PduInfoPtr->SduLength. If it fits, it shall copy its data into the buffer provided by PduInfoPtr->SduDataPtr and update the length of the actual copied data in PduInfoPtr->SduLength. If not, it returns E_NOT_OK without changing PduInfoPtr.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant for different PduIds. Non reentrant for the same PduId

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

PduR_TpCopyRxData
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    BufReq_ReturnType PduR_TpCopyRxData(PduIdType id, const PduInfoType *info, PduLengthType *bufferSizePtr)

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
     - Provides the source buffer (SduDataPtr) and the number of bytes to be copied (SduLength). An SduLength of 0 can be used to query the current amount of available buffer in the upper layer module. In this case, the SduDataPtr may be a NULL_PTR.
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
     - Data copied successfully
   * - BUFREQ_E_NOT_OK
     - Data was not copied because an error occurred.

PduR_TpRxIndication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void PduR_TpRxIndication(PduIdType id, Std_ReturnType result)

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
     - Identification of the received I-PDU.
   * - [in]
     - result
     - E_OK : The PDU was received. E_NOT_OK : Reception of the PDU failed.

**Return type**
   void


PduR_TpStartOfReception
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    BufReq_ReturnType PduR_TpStartOfReception(PduIdType id, const PduInfoType *info, PduLengthType TpSduLength, PduLengthType *bufferSizePtr)

This function is called at the start of receiving an N-SDU. The N-SDU might be fragmented into multiple N-PDUs (FF with one or more following CFs) or might consist of a single N-PDU (SF). The service shall provide the currently available maximum buffer size when invoked with TpSdu Length equal to 0.

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
     - Pointer to a PduInfoType structure containing the payload data (without protocol information) and payload length of the first frame or single frame of a transport protocol I-PDU reception, and the MetaData related to this PDU. If neither first/single frame data nor MetaData are available, this parameter is set to NULL_PTR.
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

PduR_TpCopyTxData
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    BufReq_ReturnType PduR_TpCopyTxData(PduIdType id, const PduInfoType *info, const RetryInfoType *retry, PduLengthType *availableDataPtr)

This function is called to acquire the transmit data of an I-PDU segment (N-PDU). Each call to this function provides the next part of the I-PDU data unless retry->TpDataState is TP_DATARETRY. In this case the function restarts to copy the data beginning at the offset from the current position indicated by retry->TxTpDataCnt. The size of the remaining data is written to the position indicated by availableDataPtr.

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
     - info
     - Provides the destination buffer (SduDataPtr) and the number of bytes to be copied (SduLength). If not enough transmit data is available, no data is copied by the upper layer module and BUFREQ_E_BUSY is returned. The lower layer module may retry the call. An SduLength of 0 can be used to indicate state changes in the retry parameter or to query the current amount of available data in the upper layer module. In this case, the Sdu DataPtr may be a NULL_PTR.
   * - [in]
     - retry
     - This parameter is used to acknowledge transmitted data or to retransmit data after transmission problems. If the retry parameter is a NULL_PTR, it indicates that the transmit data can be removed from the buffer immediately after it has been copied. Otherwise, the retry parameter must point to a valid RetryInfoType element. If TpDataState indicates TP_CONFPENDING, the previously copied data must remain in the TP buffer to be available for error recovery. TP_DATACONF indicates that all data that has been copied before this call is confirmed and can be removed from the TP buffer. Data copied by this API call is excluded and will be confirmed later. TP_DATARETRY indicates that this API call shall copy previously copied data in order to recover from an error. In this case TxTpDataCnt specifies the offset in bytes from the current data copy position.
   * - [out]
     - availableDataPtr
     - Indicates the remaining number of bytes that are available in the upper layer module's Tx buffer. availableDataPtr can be used by TP modules that support dynamic payload lengths (e.g. FrIsoTp) to determine the size of the following CFs.

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

PduR_TpTxConfirmation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void PduR_TpTxConfirmation(PduIdType id, Std_ReturnType result)

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
     - E_OK : The PDU was transmitted. E_NOT_OK : Transmission of the PDU failed.

**Return type**
   void


