配置（configuration）
===============================

基础配置（Basic configuration）
--------------------------------

- CanNmGlobalConfig需要配置CanNmMainFunctionPeriod，单位为毫秒（ms）。作为CanNm主函数的运行周期，所有的计时器都在每次主函数中递减一次。

  The CanNmGlobalConfig needs to configure CanNmMainFunctionPeriod, with the unit being milliseconds (ms). As the running cycle of the CanNm main function, all timers are decremented once in each main function execution.

.. figure:: ../../../_static/参考手册/CanNm/CanNmGlobalConfig基础配置.png
   :alt: CanNmGlobalConfig基础配置
   :align: center
   
   CanNmGlobalConfig基础配置

- CanNmChannelConfig中为该通道配置基础的运行参数，包括报文发送周期、自动流转状态的持续时间、引用ComM的Channel配置。

  In CanNmChannelConfig, basic operating parameters are configured for the channel, including the message transmission period, the duration of automatic state transition, and the Channel configuration referencing ComM.

.. figure:: ../../../_static/参考手册/CanNm/CanNmChannelConfig基础配置.png
   :alt: CanNmChannelConfig基础配置
   :align: center
   
   CanNmChannelConfig基础配置

- 每个CanNmChannelConfig需要创建CanNmRxPdu和CanNmTxPdu。CanNmRxPdu可以创建多个，CanNmTxPdu仅一个。

  Each CanNmChannelConfig needs to create CanNmRxPdu and CanNmTxPdu. Multiple CanNmRxPdus can be created, while only one CanNmTxPdu is allowed.

.. figure:: ../../../_static/参考手册/CanNm/CanNmPdu基础配置.png
   :alt: CanNmPdu基础配置
   :align: center
   
   CanNmPdu基础配置

- 每个容器引用的Pdu需要绑定在CanIf模块，根据收发防线配置到CanIfInitCfg/CanIfRxPduCfg和CanIfInitCfg/CanIfTxPduCfg

  The Pdu referenced by each container needs to be bound to the CanIf module, and configured to CanIfInitCfg/CanIfRxPduCfg and CanIfInitCfg/CanIfTxPduCfg according to the receiving and sending directions.

.. figure:: ../../../_static/参考手册/CanNm/CanIfPdu基础配置.png
   :alt: CanIfPdu基础配置
   :align: center
   
   CanIfPdu基础配置

UserData
--------------

- 启动CanNm的UserData功能需要在Nm模块勾选NmGlobalFeatre/NmUserDataEnabled，将默认勾选所有<Bus>NmUserDataEnabled

  To enable the UserData function of CanNm, you need to check NmGlobalFeature/NmUserDataEnabled in the Nm module, which will by default check all <Bus>NmUserDataEnabled.

.. figure:: ../../../_static/参考手册/CanNm/NmUserDataEnabled.png
   :alt: NmUserDataEnabled
   :align: center
   
   NmUserDataEnabled

- 此时CanNmComUserDataSupport未勾选则启动API方式通过Nm模块透传设置网络管理报文UserData字段

  If CanNmComUserDataSupport is not checked at this time, the API mode will be enabled to transparently transmit and set the UserData field of the network management message through the Nm module.

.. figure:: ../../../_static/参考手册/CanNm/CanNmUserData.png
   :alt: CanNmUserData
   :align: center
   
   CanNmUserData

- 若CanNmComUserDataSupport勾选，则屏蔽掉API，使能ComSignal形式设置网络管理报文UserData字段。此时需要配置CanNmUserDataTxPdu，该容器每个通道仅可配置一个。需要在PduR配置PduRRoutingPath将该Pdu配置到PduRDestPdu，并配置ComSignal以及相应的Pdu到PduRSrcPdu

  If CanNmComUserDataSupport is checked, the API will be blocked, and the ComSignal form will be enabled to set the UserData field of the network management message. In this case, CanNmUserDataTxPdu needs to be configured, and only one such container can be configured per channel. It is necessary to configure the PduRRoutingPath in PduR to map this Pdu to PduRDestPdu, and configure the ComSignal as well as the corresponding Pdu to PduRSrcPdu.
  
.. figure:: ../../../_static/参考手册/CanNm/CanNmUserDataTxPdu.png
   :alt: CanNmUserDataTxPdu
   :align: center
   
   CanNmUserDataTxPdu

快速发送（Fast transmission）
----------------------------------

快速发送机制需要先配置CanNmImmediateNmTransmission决定快速发送的次数，当CanNmImmediateNmTransmission > 0时才可配置CanNmImmediateNmCycleTime报文的快速发送周期

The fast transmission mechanism first requires configuring CanNmImmediateNmTransmission to determine the number of fast transmissions. Only when CanNmImmediateNmTransmission > 0 can the fast transmission cycle of CanNmImmediateNmCycleTime messages be configured.

.. figure:: ../../../_static/参考手册/CanNm/CanNmImmediateNmTransmission.png
   :alt: CanNmImmediateNmTransmission
   :align: center
   
   CanNmImmediateNmTransmission

总线负载降低（Reduction of bus load）
---------------------------------------

- 使用总线负载降低机制首先需要在CanNmGlobalConfig勾选CanNmBusLoadReductionEnabled
   
  To use the bus load reduction mechanism, you first need to check CanNmBusLoadReductionEnabled in CanNmGlobalConfig

.. figure:: ../../../_static/参考手册/CanNm/CanNmGlobalConfig负载降低.png
   :alt: CanNmGlobalConfig负载降低
   :align: center
   
   CanNmGlobalConfig负载降低

- 然后在CanNmChannelConfig中勾选CanNmBusLoadReductionActive后配置CanNmMsgReducedTime

  Then check CanNmBusLoadReductionActive in CanNmChannelConfig and configure CanNmMsgReducedTime

.. figure:: ../../../_static/参考手册/CanNm/CanNmChannelConfig负载降低.png
   :alt: CanNmChannelConfig负载降低
   :align: center
   
   CanNmChannelConfig负载降低

车辆唤醒（Vehicle wake-up）
------------------------------------------

车辆唤醒功能是通过在接收到的网络管理报文中检测UserData字段中指定bit触发。
首先需要勾选CanNmChannelConfig/CanNmCarWakeUpRxEnabled，在配置CanNmCarWakeUpBitPosition和CanNmCarWakeUpBytePosition。
若要启动过滤功能则勾选CanNmChannelConfig/CanNmCarWakeUpFilterNodeId，并填写指定的NodeId到CanNmCarWakeUpFilterNodeId

The vehicle wake-up function is triggered by detecting the specified bit in the UserData field of the received network management message.
First, you need to check CanNmChannelConfig/CanNmCarWakeUpRxEnabled, and then configure CanNmCarWakeUpBitPosition and CanNmCarWakeUpBytePosition.
To enable the filtering function, check CanNmChannelConfig/CanNmCarWakeUpFilterNodeId, and fill in the specified NodeId into CanNmCarWakeUpFilterNodeId.

.. figure:: ../../../_static/参考手册/CanNm/CanNmCarWakeUp.png
   :alt: CanNmCarWakeUp
   :align: center
   
   CanNmCarWakeUp
