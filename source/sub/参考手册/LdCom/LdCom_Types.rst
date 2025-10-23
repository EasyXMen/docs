
.. list-table:: 
   :widths: 15 5 20
   :header-rows: 1

   * - Type Name
     - Type
     - Description

   * - LdComTpTxConfirmationFuncPtrType
     - void*
     - Define callback function types of notifications for TP transmission confirmation.

   * - LdComRxStartOfReceptionFuncPtrType
     - BufReq_ReturnType*
     - Define callback function start of reception for reception.

   * - LdComRxCopyRxDataFuncPtrType
     - BufReq_ReturnType*
     - Define callback function of copy data of reception for receive.

   * - LdComTpRxIndicationFuncPtrType
     - void*
     - Define callback function of notifications for TP receive.

   * - LdComTxConfirmationFuncPtrType
     - void*
     - Define callback function types of notifications for IF transmission confirmation.

   * - LdComRxIndicationFuncPtrType
     - void*
     - Define callback function of notifications for IF receive.

   * - LdComTriggerTransmitFuncPtrType
     - Std_ReturnType*
     - Define callback function for trigger transmit.

   * - LdCom_IPduType
     - struct LdCom_IPduTypeTag
     - Contains the configuration parameters of the IPdu inside LdCom.

   * - LdCom_ConfigType
     - struct LdCom_ConfigTypeTag
     - The root struct configuration parameters of LdCom.

