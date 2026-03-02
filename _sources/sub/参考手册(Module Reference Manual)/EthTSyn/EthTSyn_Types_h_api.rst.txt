
类型定义 Type Definitions
-------------------------------------------------------------------------
.. 如果没有就不存在该章节，或为None

.. list-table:: 
   :widths: 15 5 20
   :header-rows: 1

   * - Type Name
     - Type
     - Description

   * - EthTSyn_CrcTimeFlagsTxSecuredCfgType
     - struct EthTSyn_CrcTimeFlagsTxSecuredCfgTypeTag
     - This type shall Determine whether the CRC verification is enabled for each specific field under the sub-TLV.

   * - EthTSyn_CrcFlagsRxValidatedCfgType
     -  EthTSyn_CrcTimeFlagsTxSecuredCfgType
     - This type shall Determine whether the CRC verification is enabled for each specific field under the sub-TLV. 

   * - EthTSyn_GlobalTimeSlaveCfgType
     - struct EthTSyn_GlobalTimeSlaveCfgTypeTag
     - This type shall define the configuration of the time slave.

   * - EthTSyn_PdelayConfigCfgType
     - struct EthTSyn_PdelayConfigCfgTypeTag
     - This type shall define the configuration of the propagation delay.

   * - EthTSyn_GlobalTimeMasterCfgType
     - struct EthTSyn_GlobalTimeMasterCfgTypeTag
     - This type shall define the configuration of the time master.

   * - EthTSyn_PortRoleCfgType
     - struct EthTSyn_PortRoleCfgTypeTag
     - This type shall define the configuration of role of a port during the synchronization process.

   * - EthTSyn_PortRoleType
     - enum EthTSyn_PortRoleTypeTag
     - This type shall define the role of a port during time synchronization process.

   * - EthTSyn_PortConfigCfgType
     - struct EthTSyn_PortConfigCfgTypeTag
     - This type shall define the configuration of the port under a time domain.

   * - EthTSyn_GlobalTimeFollowUpDataIDListElementCfgType
     - struct EthTSyn_GlobalTimeFollowUpDataIDListElementCfgTypeTag
     - This type shall define the data ID,which is used for CRC caculation or message authentication.

   * - EthTSyn_GlobalTimeFollowUpDataIDListCfgType
     - struct EthTSyn_GlobalTimeFollowUpDataIDListCfgTypeTag
     - This type shall define the list of  data ID,which is used for CRC caculation or message authentication.

   * - EthTSyn_GlobalTimeDomainCfgType
     - struct EthTSyn_GlobalTimeDomainCfgTypeTag
     - This type shall define the configuration of a time domain.

   * - EthTSynMessageType
     - uint8
     - This definition specifies the types of messages that the EthTSyn module sends and receives.

   * - EthTSyn_PdelayTXStatusType
     - enum EthTSyn_PdelayTXStatusTypeTag
     - This type shall define the status of Pdelay Delay Measurement Requester during pdelay measurement.

   * - EthTSyn_PdelayRXStatusType
     - enum EthTSyn_PdelayRXStatusTypeTag
     - This type shall define the  status of Pdelay Delay Measurement Receiver during pdelay measurement.

   * - EthTSyn_SyncStatusType
     - enum EthTSyn_SyncStatusTypeTag
     - This type shall define the status of a port during synchronization process.

   * - EthTSyn_TransmissionModeType
     - enum EthTSyn_TransmissionModeTypeTag
     - This type shall define the mode of transmission.

   * - EthTSyn_TimeStampType
     - struct EthTSyn_TimeStampTypeTag
     - This type shall define the format of global timestamp.

   * - EthTSyn_PdelayResponderTimestampType
     - struct EthTSyn_PdelayResponderTimestampTypeTag
     - This type shall define the type of ingress timestamp and egress timestamp during pdelay measurement.

   * - EthTSyn_SyncEgressTupleType
     - struct EthTSyn_SyncEgressTupleTypeTag
     - This type shall define the type of egress time tuple,which includes the global and local time.

   * - EthTSyn_PortType
     - struct EthTSyn_PortTypeTag
     - This type shall define the runtime variable of a port.

   * - EthTSyn_ConfigType
     - struct EthTSyn_ConfigTypeTag
     - This type shall define the configuration of EthTSyn.

   * - EthTSyn_PortRoleTypeTag
     - enum
     - This type shall define the role of a port during time synchronization process.

   * - EthTSyn_PdelayTXStatusTypeTag
     - enum
     - This type shall define the status of Pdelay Delay Measurement Requester during pdelay measurement.

   * - EthTSyn_PdelayRXStatusTypeTag
     - enum
     - This type shall define the  status of Pdelay Delay Measurement Receiver during pdelay measurement.

   * - EthTSyn_SyncStatusTypeTag
     - enum
     - This type shall define the status of a port during synchronization process.

   * - EthTSyn_TransmissionModeTypeTag
     - enum
     - This type shall define the mode of transmission.


