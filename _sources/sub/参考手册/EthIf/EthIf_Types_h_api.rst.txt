
类型定义 Type Definitions
--------------------------------------------------------------------------------
.. 如果没有就不存在该章节，或为None

.. list-table::
   :widths: 15 5 20
   :header-rows: 1

   * - Type Name
     - Type
     - Description

   * - EthIf_StateType
     - enum EthIf_StateTag
     - state of EthIf

   * - EthIf_CtrlRefTrcvType
     - enum EthIf_CtrlRefTrcvTag
     - Type of ethernet hardware refercecd by controller.

   * - EthIf_MeasurementIdxType
     - uint8
     -

   * - EthIf_SwitchPortGroupIdxType
     - uint8
     - Definition of configurable interface <User>_TrcvLinkStateChg.

   * - EthIfULRxIndicationFuncType
     - void*
     - Definition of configurable interface <User>_RxIndication.

   * - EthIfULTxConfirmationFuncType
     - void*
     - Definition of configurable interface.

   * - EthIfTrcvLinkStateChgFuncType
     - void*
     - Definition of configurable interface <User>_TrcvLinkStateChg.

   * - EthIf_EthDriverApiType
     - struct EthIf_EthDriverApiTag
     - Api Type of Ethernet Driver.

   * - EthIf_ControllerCfgType
     - struct EthIf_ControllerCfgTag
     - EthIfController Configuration type.

   * - EthIf_FrameOwnerCfgType
     - struct EthIf_FrameOwnerCfgTag
     - EthIfFrameOwner Configuration type.

   * - EthIf_SwitchCfgType
     - struct EthIf_SwitchCfgTag
     - EthIfSwitch Configuration type.

   * - EthIf_TrcvCfgType
     - struct EthIf_TrcvCfgTag
     - EthIfTransceiver Configuration type.

   * - EthIf_PhysControllerType
     - struct EthIf_PhysControllerTag
     - EthIfPhysicalController Configuration type.

   * - EthIf_PortGroupSemanticType
     - enum EthIf_PortGroupSemanticTag
     - Sementic type of EthIfSwitchPortGroup.

   * - EthIf_EthSwtPortCfgType
     - struct EthIf_EthSwtPortCfgTag
     - EthSwitchPort Configuration type.

   * - EthIf_PortGroupType
     - struct EthIf_PortGroupTag
     - EthIfPortGroup Configuration type.

   * - EthIf_ConfigType
     - struct EthIf_ConfigTag
     - EthIf Configuration type.

   * - EthIf_StateTag
     - enum
     - state of EthIf

   * - EthIf_CtrlRefTrcvTag
     - enum
     - Type of ethernet hardware refercecd by controller.

   * - EthIf_PortGroupSemanticTag
     - enum
     - Sementic type of EthIfSwitchPortGroup.

