.. list-table:: 
   :widths: 15 5 20
   :header-rows: 1

   * - Type Name
     - Type
     - Description

   * - PduR_PBConfigIdType
     - uint16
     - Identification of the post-build configuration.

   * - PduR_RoutingPathGroupIdType
     - uint16
     - Identification of a Routing group.

   * - PduR_QueueDepthType
     - uint8
     - PduR queue depth type.

   * - PduR_BufferPoolSizeType
     - uint8
     - PduR buffer pool size type.

   * - PduR_BufferIndexType
     - uint16
     - PduR buffer index type.

   * - PduR_RoutingPathGroupType
     - struct
     - PduR route path group type.

   * - PduR_BufferPoolType
     - struct
     - PduR buffer pool type.

   * - PduR_QueueCfgType
     - struct
     - PduR queue configuration type.

   * - PduR_DefaultValueType
     - struct
     - PduR path default value type.

   * - PduR_SrcPduType
     - struct
     - PduR src pdu type.

   * - PduR_DestPduType
     - struct
     - PduR dest pdu type.

   * - PduR_RoutingPathType
     - struct
     - PduR route path type.

   * - PduR_RoutingTableType
     - struct
     - PduR route table type.

   * - PduR_PBConfigType
     - struct
     - The root struct configuration parameters of PduR.

   * - PduR_ModuleCancelReceiveApiType
     - Std_ReturnType func(PduIdType)
     - PduRCancelReceive function prototype.

   * - PduR_ModuleIfTpCancelTransmitApiType
     - Std_ReturnType func(PduIdType)
     - PduRCancelTransmit function prototype.

   * - PduR_ModuleTriggertransmitApiType
     - Std_ReturnType func(PduIdType, PduInfoType*)
     - PduRTriggertransmit function prototype.

   * - PduR_ModuleIfTransmitApiType
     - Std_ReturnType func(PduIdType, const PduInfoType*)
     - PduRTransmit function prototype.

   * - PduR_ModuleTxConfirmationApiType
     - void func(PduIdType, Std_ReturnType)
     - PduRTxConfirmation function prototype.

   * - PduR_ModuleIfRxIndicationApiType
     - void func(PduIdType, const PduInfoType*)
     - PduRRxIndication function prototype.

   * - PduR_ModuleTpTransmitApiType
     - Std_ReturnType func(PduIdType, const PduInfoType*)
     - PduRTpTransmit function prototype.

   * - PduR_ModuleCopyTxDataApiType
     - BufReq_ReturnType func(PduIdType, const PduInfoType*, const RetryInfoType*, PduLengthType*)
     - PduRCopyTxData function prototype.

   * - PduR_ModuleTpTxConfirmationApiType
     - void func(PduIdType, Std_ReturnType)
     - PduRTpTxConfirmation function prototype.

   * - PduR_ModuleStartOfReceptionApiType
     - BufReq_ReturnType func(PduIdType, const PduInfoType*, PduLengthType, PduLengthType*)
     - PduRStartOfReception function prototype.

   * - PduR_ModuleCopyRxDataApiType
     - BufReq_ReturnType func(PduIdType, const PduInfoType*, PduLengthType*)
     - PduRCopyRxData function prototype.

   * - PduR_ModuleTpRxIndicationApiType
     - void func(PduIdType, Std_ReturnType)
     - PduRTpRxIndication function prototype.

   * - PduR_BswModuleType
     - struct
     - PduR Module configuration type.

   * - PduR_BufferType
     - struct
     - PduRTxBuffer design.

   * - PduR_QueueRuntimeType
     - struct
     - PduR queue runtime type.

