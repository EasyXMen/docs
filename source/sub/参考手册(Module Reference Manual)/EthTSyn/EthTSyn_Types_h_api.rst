
类型定义 Type Definitions
-------------------------------------------------------------------------
.. 如果没有就不存在该章节，或为None

.. list-table::
   :widths: 15 5 20
   :header-rows: 1

   * - Type Name
     - Type
     - Description

   * - EthTSyn_CrcFlagsRxValidatedCfgType
     - 
     - 

   * - EthTSyn_CrcSecuredType
     - enum
     - This represents the configuration of whether or not CRC is supported.

   * - EthTSyn_CrcValidatedType
     - enum
     - Definition of whether or not validation of the CRC takes place.

   * - EthTSyn_RxIcvVerificationType
     - enum
     - Definition of whether or not ICV verification shall be supported.

   * - EthTSyn_PortRoleType
     - enum
     - This type shall define the role of a port during time synchronization process.

   * - EthTSyn_CriptographySelection
     - enum
     - This type shall define Symmetric or asymmetric cryptography selection for the ICV generation.

   * - EthTSyn_CryptoProcessingType
     - enum
     - Define the encryption and decryption process, synchronous or asynchronous.

   * - EthTSyn_PdelayTXStatusType
     - enum
     - Enumeration defining the status of Pdelay Delay Measurement Requester during pdelay measurement.

   * - EthTSyn_PdelayRXStatusType
     - enum
     - Enumeration defining the status of Pdelay Delay Measurement Receiver during pdelay measurement.

   * - EthTSyn_SyncStatusType
     - enum
     - Enumeration defining the status of a port during synchronization process.

   * - EthTSyn_TransmissionModeType
     - enum
     - Enumeration defining the mode of transmission for Ethernet Time Synchronization.

   * - EthTSyn_CrcTimeFlagsTxSecuredCfgType
     - struct
     - This type shall Determine whether the CRC verification is enabled for each specific field under the sub-TLV.

   * - EthTSyn_GlobalTimeSlaveCfgType
     - struct
     - This type shall define the configuration of the time slave.

   * - EthTSyn_PdelayConfigCfgType
     - struct
     - Configuration structure for propagation delay measurement in Ethernet Time Synchronization.

   * - EthTSyn_GlobalTimeMasterCfgType
     - struct
     - This type shall define the configuration of the time master.

   * - EthTSyn_PortRoleCfgType
     - struct
     - This type shall define the configuration of role of a port during the synchronization process.

   * - EthTSyn_ICVRxPduType
     - struct
     - Structure for ICV-related RX PDU data handling.

   * - EthTSyn_TxCsmJobType
     - struct
     - Define information about the Csm job of generation.

   * - EthTSyn_RxCsmJobType
     - struct
     - Define information about the Csm job of verification.

   * - EthTSyn_GlobalTimeTxIcvGenerationType
     - struct
     - This type shall define the configuration of ICV generation.

   * - EthTSyn_GlobalTimeRxIcvVerificationType
     - struct
     - Configuration structure for ICV (Integrity Check Value) verification in Ethernet Time Synchronization.

   * - EthTSyn_AuthenticatedFieldInofoType
     - struct
     - Structure describing the Time Authenticated Field for ICV processing.

   * - EthTSyn_CircularBufferType
     - struct
     - Structure defining parameters of a circular buffer used for ICV data storage.

   * - EthTSyn_ICVGenarationAndVerificationType
     - struct
     - Structure defining runtime variables related to ICV (Integrity Check Value).

   * - EthTSyn_PortConfigCfgType
     - struct
     - Configuration structure for a port under a time domain.

   * - EthTSyn_GlobalTimeFollowUpDataIDListElementCfgType
     - struct
     - Structure defining a single data ID used for CRC calculation or message authentication.

   * - EthTSyn_GlobalTimeFollowUpDataIDListCfgType
     - struct
     - Structure defining the list of data IDs used for CRC calculation or message authentication.

   * - EthTSyn_GlobalTimeDomainCfgType
     - struct
     - This type shall define the configuration of a time domain.

   * - EthTSyn_TimeStampType
     - struct
     - Structure defining the format of a global timestamp.

   * - EthTSyn_PdelayResponderTimestampType
     - struct
     - Structure defining ingress and egress timestamps during Pdelay measurement.

   * - EthTSyn_SyncEgressTupleType
     - struct
     - Structure defining the egress time tuple type, including global and local time.

   * - EthTSyn_RateRatioType
     - struct
     - Structure for parameters related to rate ratio calculation in Ethernet Time Synchronization.

   * - EthTSyn_PortType
     - struct
     - Runtime variable structure for an Ethernet Time Synchronization port.

   * - EthTSyn_ConfigType
     - struct
     - Main configuration structure for the Ethernet Time Synchronization module.


      
提供的服务
-----------
