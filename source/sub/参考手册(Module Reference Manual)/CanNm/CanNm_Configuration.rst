配置(Configuration)
===============================

基础配置(Basic Configuration)
--------------------------------

- CanNmGlobalConfig需要配置CanNmMainFunctionPeriod，单位为毫秒(ms)。作为CanNm主函数的运行周期，所有的计时器都在每次主函数中递减一次。

  The CanNmGlobalConfig requires configuration of the CanNmMainFunctionPeriod in milliseconds (ms). This period defines the execution cycle of the CanNm main function, during which all managed timers are decremented once.

.. figure:: ../../../_static/参考手册/CanNm/CanNmGlobalConfig基础配置.png
   :alt: CanNmGlobalConfig基础配置(CanNmGlobalConfig Basic Configuration)
   :align: center
   
   CanNmGlobalConfig基础配置
   
   CanNmGlobalConfig Basic Configuration

- CanNmChannelConfig中为该通道配置基础的运行参数，包括报文发送周期、自动流转状态的持续时间、引用ComM的Channel配置。

  The CanNmChannelConfig configures basic channel parameters, including the message transmission period, the duration for automatic state transitions, and a reference to the ComM Channel configuration.

.. figure:: ../../../_static/参考手册/CanNm/CanNmChannelConfig基础配置.png
   :alt: CanNmChannelConfig基础配置(CanNmChannelConfig Basic Configuration)
   :align: center
   
   CanNmChannelConfig基础配置
   
   CanNmChannelConfig Basic Configuration

- 每个CanNmChannelConfig需要创建CanNmRxPdu和CanNmTxPdu。CanNmRxPdu可以创建多个，CanNmTxPdu仅一个。

  Each CanNmChannelConfig must define one CanNmTxPdu and may define multiple CanNmRxPdus.

.. figure:: ../../../_static/参考手册/CanNm/CanNmPdu基础配置.png
   :alt: CanNmPdu基础配置(CanNmPdu Basic Configuration)
   :align: center
   
   CanNmPdu基础配置
   
   CanNmPdu Basic Configuration

- 每个容器引用的Pdu需要绑定在CanIf模块，根据收发防线配置到CanIfInitCfg/CanIfRxPduCfg和CanIfInitCfg/CanIfTxPduCfg

  Each container's referenced PDU must be bound to the CanIf module. Based on its transmission or reception direction, it is then defined in either CanIfInitCfg/CanIfTxPduCfg or CanIfInitCfg/CanIfRxPduCfg.

.. figure:: ../../../_static/参考手册/CanNm/CanIfPdu基础配置.png
   :alt: CanIfPdu基础配置(CanIfPdu Basic Configuration)
   :align: center
   
   CanIfPdu基础配置
   
   CanIfPdu Basic Configuration

UserData
--------------

- 启动CanNm的UserData功能需要在Nm模块勾选NmGlobalFeatre/NmUserDataEnabled，将默认勾选所有<Bus>NmUserDataEnabled

  To enable the CanNm UserData feature, select NmGlobalFeature/NmUserDataEnabled in the Nm module. This action automatically enables all corresponding <Bus>NmUserDataEnabled configurations by default.

.. figure:: ../../../_static/参考手册/CanNm/NmUserDataEnabled.png
   :alt: NmUserDataEnabled
   :align: center
   
   NmUserDataEnabled

- 此时CanNmComUserDataSupport未勾选则启动API方式通过Nm模块透传设置网络管理报文UserData字段

  If CanNmComUserDataSupport is disabled, the API method is used to directly set the NM PDU's UserData field through the Nm module via pass-through.

.. figure:: ../../../_static/参考手册/CanNm/CanNmUserData.png
   :alt: CanNmUserData
   :align: center
   
   CanNmUserData

- 若CanNmComUserDataSupport勾选，则屏蔽掉API，使能ComSignal形式设置网络管理报文UserData字段。此时需要配置CanNmUserDataTxPdu，该容器每个通道仅可配置一个。需要在PduR配置PduRRoutingPath将该Pdu配置到PduRDestPdu，并配置ComSignal以及相应的Pdu到PduRSrcPdu

  If CanNmComUserDataSupport is enabled, the API method is disabled and the ComSignal mechanism is used to set the NM PDU's UserData field. This requires configuration of a CanNmUserDataTxPdu container (limited to one per channel). In PduR, configure a PduRRoutingPath to route this PDU to a PduRDestPdu, and map the corresponding ComSignal and its source PDU to a PduRSrcPdu.
  
.. figure:: ../../../_static/参考手册/CanNm/CanNmUserDataTxPdu.png
   :alt: CanNmUserDataTxPdu
   :align: center
   
   CanNmUserDataTxPdu

快速发送(Fast Transmission)
----------------------------------

快速发送机制需要先配置CanNmImmediateNmTransmission决定快速发送的次数，当CanNmImmediateNmTransmission > 0时才可配置CanNmImmediateNmCycleTime报文的快速发送周期

The fast transmission mechanism first requires configuring CanNmImmediateNmTransmission to determine the maximum count of fast transmissions. CanNmImmediateNmTransmission > 0 is the prequisite for configuring the fast transmission cycle of CanNmImmediateNmCycleTime messages.

.. figure:: ../../../_static/参考手册/CanNm/CanNmImmediateNmTransmission.png
   :alt: CanNmImmediateNmTransmission
   :align: center
   
   CanNmImmediateNmTransmission

总线负载降低(Reduction of Bus Load)
---------------------------------------

- 使用总线负载降低机制首先需要在CanNmGlobalConfig勾选CanNmBusLoadReductionEnabled
   
  To enable the bus load reduction mechanism, first ensure that CanNmBusLoadReductionEnabled is selected in the CanNmGlobalConfig.

.. figure:: ../../../_static/参考手册/CanNm/CanNmGlobalConfig负载降低.png
   :alt: CanNmGlobalConfig负载降低(CanNmGlobalConfig load reduction)
   :align: center
   
   CanNmGlobalConfig负载降低
   
   CanNmGlobalConfig load reduction

- 然后在CanNmChannelConfig中勾选CanNmBusLoadReductionActive后配置CanNmMsgReducedTime

  Then enable CanNmBusLoadReductionActive in CanNmChannelConfig and configure CanNmMsgReducedTime

.. figure:: ../../../_static/参考手册/CanNm/CanNmChannelConfig负载降低.png
   :alt: CanNmChannelConfig负载降低(CanNmChannelConfig load reduction)
   :align: center
   
   CanNmChannelConfig负载降低
   
   (CanNmChannelConfig load reduction)

车辆唤醒 Vehicle Wake-up
------------------------------------------

车辆唤醒功能是通过在接收到的网络管理报文中检测UserData字段中指定bit触发。

The vehicle wake-up function is triggered by detecting a specified bit in the UserData field of an incoming Network Management (Nm) message.

首先需要勾选CanNmChannelConfig/CanNmCarWakeUpRxEnabled，在配置CanNmCarWakeUpBitPosition和CanNmCarWakeUpBytePosition。

First, enable CanNmChannelConfig/CanNmCarWakeUpRxEnabled; then set the values for CanNmCarWakeUpBitPosition and CanNmCarWakeUpBytePosition.

若要启动过滤功能则勾选CanNmChannelConfig/CanNmCarWakeUpFilterNodeId，并填写指定的NodeId到CanNmCarWakeUpFilterNodeId

To enable the filtering function, enable CanNmChannelConfig/CanNmCarWakeUpFilterNodeId, and fill in the specified NodeId into CanNmCarWakeUpFilterNodeId.

.. figure:: ../../../_static/参考手册/CanNm/CanNmCarWakeUp.png
   :alt: CanNmCarWakeUp
   :align: center
   
   CanNmCarWakeUp
