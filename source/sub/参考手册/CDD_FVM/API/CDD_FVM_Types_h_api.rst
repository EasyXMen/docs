
类型定义 Type Definitions
---------------------------------

.. list-table:: 
   :widths: 15 5 20
   :header-rows: 1

   * - Type Name
     - Type
     - Description

   * - CDD_FVM_StateType
     -  enum CDD_FVM_StateTag
     - Define the initialization state of the FVM module.

   * - CDD_FVM_ModeType
     - enum CDD_FVM_ModeTag
     - Define the mode of the FVM module.

   * - CDD_FVM_PduType
     - enum CDD_FVM_PduTag
     - Define the type of the API.

   * - CDD_FVM_TxFreshnessConfigType
     - struct CDD_FVM_TxFreshnessConfigTag
     - Define the configuration of the freshness value in Tx mode.

   * - CDD_FVM_RxFreshnessConfigType
     - struct CDD_FVM_RxFreshnessConfigTag
     - Define the configuration of the freshness value in Rx mode.

   * - CDD_FVM_TxSingleFreshnessCounterConfigType
     - struct CDD_FVM_TxSingleFreshnessCounterConfigTag
     - Define a single counter send configuration.

   * - CDD_FVM_RxSingleFreshnessCounterConfigType
     - struct CDD_FVM_RxSingleFreshnessCounterConfigTag
     - Define a single counter receive configuration.

   * - CDD_FVM_SyncMsgCtrlPudType
     - struct CDD_FVM_SyncMsgCtrlPudTag
     - Define the PDU corresponding to the synchronization message.

   * - CDD_FVM_FreshnessCounterConfigType
     - struct CDD_FVM_FreshnessCounterConfigTag
     - Define the configuration of the freshness counter.

   * - CDD_FVM_MultipleFreshnessValueStructureType
     - struct CDD_FVM_MultipleFreshnessValueStructureTag
     - Define the structure of the freshness value in the multiple freshness value mode.

   * - CDD_FVM_SlaveSyncMsgPduType
     - struct CDD_FVM_SlaveSyncMsgPduTag
     - Define the configuration of the PDU corresponding to the synchronization message from the slave ECU.

   * - CDD_FVM_SlaveECUSyncConfigType
     - struct CDD_FVM_SlaveECUSyncConfigTag
     - Define slave ECU configurations related to synchronization.

   * - CDD_FVM_TxMultipleFreshnessTruncatedCounterConfigType
     - struct CDD_FVM_TxMultipleFreshnessTruncatedCounterConfigTag
     - Define the configuration in Tx Multiple Freshness Truncated Counter mode.

   * - CDD_FVM_RxMultipleFreshnessTruncatedCounterConfigType
     - struct CDD_FVM_RxMultipleFreshnessTruncatedCounterConfigTag
     - Define the configuration in Rx Multiple Freshness Truncated Counter mode.

   * - CDD_FVM_MasterSyncMsgPduType
     - struct CDD_FVM_MasterSyncMsgPduTag
     - Define the configuration of the PDU corresponding to the synchronization message from the master ECU.

   * - CDD_FVM_MasterConfigType
     - struct CDD_FVM_MasterConfigTag
     - Define master ECU configurations related to synchronization.

   * - CDD_FVM_ConfigType
     - struct CDD_FVM_ConfigTag
     - Define configuration data structure of FVM module.

   * - CDD_FVM_StateTag
     - enum
     - Define the initialization state of the FVM module.

   * - CDD_FVM_ModeTag
     - enum
     - Define the mode of the FVM module.

   * - CDD_FVM_PduTag
     - enum
     - Define the type of the API.

