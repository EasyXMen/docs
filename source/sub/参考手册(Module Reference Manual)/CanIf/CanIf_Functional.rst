功能描述(Functional Description)
===================================================================================================
.. 本章节仅描述模块支持的功能大致情况，不宜做细致描述；更加细致的描述在配置章节，结合配置，从集成角度描述


公共特性(Public Features)
---------------------------------------------------------------------------------------------------


多核多分区功能(Multi-core and Multi-partition Features)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- CanIf模块支持多核多分区部署，由配置项CanIfPublicCfg/CanIfEcucPartitionRef决定CanIf可被部署的所有分区。

  The CanIf module supports multi-core, multi-partition deployment, and the configuration options CanIfPublicCfg/CanIfEcucPartitionRef determine all partitions to which CanIf can be deployed.

- 由CanIfCtrlCfg/CanIfCtrlPartitionRef决定每个CanIf控制器所在分区。

  The partition in which each CanIf controller resides is determined by CanIfCtrlCfg/CanIfCtrlPartitionRef.

- 由CanIfTrcvCfg/CanIfTrcvPartitionRef决定每个CanIf收发器所在分区。

  The partition in which each CanIf transceiver resides is determined by CanIfTrcvCfg/CanIfTrcvPartitionRef.


.. only:: doc_pbs

   PBS功能(PBS Features)
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   - CanIf模块支持多变体配置。

     The CanIf module supports multi-variant configurations.

   - 支持容器CanIfTxPduCfg、CanIfRxPduCfg、CanIfHthCfg、CanIfHrhCfg、CanIfBufferCfg的数量和属性变体。

     The number and attribute variants of the CanIfTxPduCfg, CanIfRxPduCfg, CanIfHthCfg, CanIfHrhCfg, and CanIfBufferCfg containers are supported.

   - 不支持容器CanIfCtrlDrvCfg、CanIfCtrlCfg、CanIfTrcvDrvCfg、CanIfTrcvCfg的数量和属性变体。

     The number and attribute variants of the CanIfCtrlDrvCfg, CanIfCtrlCfg, CanIfTrcvDrvCfg, and CanIfTrcvCfg containers are not supported.


Memmap功能(Memmap Features)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Memmap文件是动态的。存在
  CANIF_START_SEC_CONFIG_DATA_8、CANIF_STOP_SEC_CONFIG_DATA_8、
  CANIF_START_SEC_CONFIG_DATA_16、CANIF_STOP_SEC_CONFIG_DATA_16、
  CANIF_START_SEC_CONFIG_DATA_32、CANIF_STOP_SEC_CONFIG_DATA_32、
  CANIF_START_SEC_CONFIG_DATA_PTR、CANIF_STOP_SEC_CONFIG_DATA_PTR、
  CANIF_START_SEC_CONFIG_DATA_UNSPECIFIED、CANIF_STOP_SEC_CONFIG_DATA_UNSPECIFIED、
  CANIF_START_SEC_VAR_CLEARED_8、CANIF_STOP_SEC_VAR_CLEARED_8、
  CANIF_START_SEC_VAR_CLEARED_16、CANIF_STOP_SEC_VAR_CLEARED_16、
  CANIF_START_SEC_VAR_CLEARED_32、CANIF_STOP_SEC_VAR_CLEARED_32、
  CANIF_START_SEC_VAR_CLEARED_PTR、CANIF_STOP_SEC_VAR_CLEARED_PTR、
  CANIF_START_SEC_VAR_CLEARED_UNSPECIFIED、CANIF_STOP_SEC_VAR_CLEARED_UNSPECIFIED、
  CANIF_START_SEC_VAR_CLEARED_{{ n }}_8 [#f1]_、CANIF_STOP_SEC_VAR_CLEARED_{{ n }}_8 [#f1]_、
  CANIF_START_SEC_VAR_CLEARED_{{ n }}_PTR [#f1]_、CANIF_STOP_SEC_VAR_CLEARED_{{ n }}_PTR [#f1]_、
  CANIF_START_SEC_VAR_CLEARED_{{ n }}_UNSPECIFIED [#f1]_、CANIF_STOP_SEC_VAR_CLEARED_{{ n }}_UNSPECIFIED [#f1]_、
  CANIF_START_SEC_CODE、CANIF_STOP_SEC_CODE。

  The Memmap files are dynamic.

.. rubric:: 说明

.. [#f1] n 为CanIfPublicCfg/CanIfEcucPartitionRef中配置的分区名称。


独占区功能(Exclusive Area Features)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
None.


模块特性(Module Features)
---------------------------------------------------------------------------------------------------


模式控制功能(Mode Control Function)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


模式控制功能介绍(Introduction)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. CanIf模块的状态机控制，包括未初始化和已初始化状态，除了CanIf_Init 和CanIf_GetVersionInfo之外，都需要在已初始化状态下才能正常调用。

   The state machine control of the CanIf module includes UNINITIALIZED and INITIALIZED states. With the exception of CanIf_Init and CanIf_GetVersionInfo, all other API functions require the module to be in the INITIALIZED state for proper operation.

#. Controller模式控制，分为STOPPED，STARTED，SLEEP三种，只有在START状态下Controller才能正常通信。

   The Controller supports three modes: STOPPED, STARTED, and SLEEP. Normal communication is possible only when the Controller is in the STARTED state.

#. Trcv模式控制，分为NORMAL，STANDBY，SLEEP三种，只有在NORMAL状态下Trcv才能正常通信。

   Trcv supports three modes: NORMAL, STANDBY, and SLEEP. Normal communication is possible only when Trcv is in the NORMAL state.

#. Controller的Pdu模式控制，分为OFFLINE，TX_OFFLINE，TX_OFFLINE_ACTIVE，ONLINE四种，
   ONLINE模式下允许正常收发通信，TX_OFFLINE模式下只能接收不能发送，
   TX_OFFLINE_ACTIVE模式下允许接收和虚拟发送，OFFLINE模式下不允许收发通信。

   The Controller supports four PDU modes: OFFLINE, TX_OFFLINE, TX_OFFLINE_ACTIVE, and ONLINE.
   In the ONLINE mode, both transmission and reception are allowed; in the TX_OFFLINE mode, only reception is allowed and transmission is not permitted; in the TX_OFFLINE_ACTIVE mode, reception and virtual transmission are allowed; in the OFFLINE mode, both transmission and reception are not allowed.


模式控制功能实现(Implementation)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. 上电之后CanIf处于CANIF_UNINIT状态，正确调用CanIf_Init(参数为CanIf模块PB配置参数指针)之后状态切换到CANIF_INITED。

   After power-on, CanIf is in the CANIF_UNINIT state. Upon successful execution of CanIf_Init—which takes a pointer to the post-build (PB) configuration data as its parameter—the module transitions to the CANIF_INITED state.

#. CanIf_Init初始化之后，Controller模式为STOPPED，调用接口CanIf_SetControllerMode切换Controller模式， 调用CanIf_GetControllerMode获取当前Controller模式。当Controller发生BusOff事件时，Controller模式切换到STOPPED。

   After CanIf_Init has been executed, the Controller mode is STOPPED. Use CanIf_SetControllerMode to change the Controller mode and CanIf_GetControllerMode to query the current mode. When a BusOff event occurs, the Controller mode switches to STOPPED.

#. 调用CanIf_SetTrcvMode切换Trcv模式，调用CanIf_GetTrcvMode获取Trcv当前模式。

   Call CanIf_SetTrcvMode to switch the Trcv mode and CanIf_GetTrcvMode to obtain the current Trcv mode.

#. CanIf_Init初始化之后，Pdu模式为OFFLINE，调用CanIf_SetPduMode切换Pdu模式，
   调用CanIf_GetPduMode获取当前Controller的Pdu模式。
   其中TX_OFFLINE_ACTIVE模式需要在配置项CanIfTxOfflineActiveSupport使能时才支持。
   当Controller发生BusOff事件时，Pdu模式切换到TX_OFFLINE。

   After CanIf_Init has been executed, the PDU mode defaults to OFFLINE. Use CanIf_SetPduMode to change the mode and CanIf_GetPduMode to query the current Controller PDU mode. The TX_OFFLINE_ACTIVE mode requires the CanIfTxOfflineActiveSupport configuration parameter to be enabled. Upon a BusOff event, the PDU mode transitions to TX_OFFLINE.


TxPdu发送功能(TxPdu Transmission Function)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


TxPdu发送功能介绍(Introduction)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

当模块初始化成功，Controller模式及其Pdu模式，Trcv模式均处于允许发送状态时，可通过CanIf两种发送机制来发送L-Pdu:

When the module is successfully initialized and the Controller, PDU, and Trcv modes all enter a transmit-enabled state, L-PDUs can be sent using either of the two transmission mechanisms provided by CanIf:

- 方式一：上层模块调用CanIf_Transmit请求TxPdu的发送，发送时机由上层决定；

  Method 1: The upper-layer module calls CanIf_Transmit to request the transmission of TxPdu. The transmission timing is determined by the upper layer.

- 方式二：下层驱动调用CanIf_TriggerTransmit请求TxPdu的发送数据，发送时机由下层决定；

  Method 2: The lower-layer driver calls CanIf_TriggerTransmit to request TxPDU data for transmission. The transmission timing is determined by the lower layer.

TxPdu发送成功后，下层驱动调用CanIf_TxConfirmation进行发送确认。

Upon successful transmission of the TxPDU, the lower-layer driver calls CanIf_TxConfirmation for transmission confirmation.


TxPdu发送功能实现(Implementation)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

当上层模块调用CanIf_Transmit请求TxPdu发送，并传入L-PDU的SDU及可能存在的MetaData数据时，
CanIf根据Static/Dynamic CanId策略计算出该TxPdu当前对应的CanId，调用Can_Write由配置的HTH进行发送。

When the upper-layer module calls CanIf_Transmit to request a TxPDU transmission and passes in the SDU of the L-PDU and associated MetaData, CanIf calculates the corresponding CanId of the TxPdu according to the Static/Dynamic CanId strategy, and calls Can_Write to initiate transmission through the configured HTH.

CAN总线通常不支持TriggerTransmit进行发送，该机制通常用于LIN总线。

The CAN bus generally does not support transmission via TriggerTransmit; this mechanism is typically used for the LIN bus.

当驱动层TxPdu发送成功后，调用CanIf_TxConfirmation，CanIf调用<User_TxConfirmation>通知上层模块。

Upon successful transmission of a TxPDU by the driver layer, it calls CanIf_TxConfirmation, and CanIf then invokes <User_TxConfirmation> to notify the upper-layer module.

对于TxPdu发送，可以配置TxBuffer机制(CanIfBufferSize>0)来降低因发送邮箱BUSY而导致丢帧的概率。
需注意的是配置项CanIfBufferSize决定该HTH最多缓存的不同TxPdu帧数，对于每个TxPdu最多只能缓存一帧。

To mitigate frame loss due to busy transmit mailboxes, the Tx Buffer mechanism can be enabled by setting CanIfBufferSize greater than 0. Note that the configuration parameter CanIfBufferSize determines the maximum number of different TxPdu frames the HTH can buffer, with a limit of one frame buffered per TxPDU.


RxPdu接收功能(RxPdu Reception Function)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


RxPdu接收功能介绍(Introduction)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

当模块初始化成功，Controller模式及其Pdu模式，Trcv模式均处于允许接收状态时，将从驱动层接收到的报文，传递到上层模块。

When the module is successfully initialized and the Controller, PDU, and Trcv modes all enter a receive-enabled state, any messages received from the driver layer will be passed up to the upper-layer module.


RxPdu接收功能实现(Implementation)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

当驱动层邮箱收到报文后，调用CanIf_RxIndication将接收数据传递到CanIf模块，CanIf通过接收的HRH以及CanId，
查询匹配到接收RxPdu，调用关联上层模块的<User_RxIndication>将接收RxPdu数据传递给上层模块。

When a message is received in the driver layer's mailbox, it invokes CanIf_RxIndication to deliver the data to the CanIf module. Using the received HRH and CanId, CanIf looks up the matching Rx PDU and then calls the corresponding <User_RxIndication> callback to pass the received data to the associated upper-layer module.

RxPdu上层模块由配置项CanIfRxPduUserRxIndicationUL决定，<User_RxIndication>由配置项CanIfRxPduUserRxIndicationName决定。

The upper-layer module for an RxPdu is determined by the configuration item CanIfRxPduUserRxIndicationUL, while <User_RxIndication> is determined by CanIfRxPduUserRxIndicationName.


睡眠唤醒功能(Sleep and Wake-up Function)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


睡眠唤醒功能介绍(Introduction)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

上层模块可以通过CanIf来将Controller/Trcv设置为SLEEP模式，支持Controller/Trcv唤醒源检测，Controller/Trcv唤醒确认，Trcv唤醒原因获取，Trcv唤醒标志位检测/清除，Trcv唤醒模式设置。

The upper-layer module can set the Controller/Trcv to SLEEP mode through CanIf. CanIf supports Controller/Trcv wake-up source detection, Controller/Trcv wake-up confirmation, Trcv wake-up reason retrieval, Trcv wake-up flag detection/clearance, and Trcv wake-up mode setting.


睡眠唤醒功能实现(Implementation)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

CanIf提供CanIf_SetControllerMode/CanIf_SetTrcvMode来设置Controller/Trcv的模式(包含SLEEP模式)，
当发生唤醒事件后可通过调用CanIf_CheckWakeup来检测是否由Controller/Trcv导致的唤醒事件，
可通过CanIf_CheckValidation来检测唤醒成功确认(唤醒确认条件为接收到任意Pdu/NM Pdu，
参见配置项CanIfPublicWakeupCheckValidByNM是否勾选)。

CanIf provides CanIf_SetControllerMode/CanIf_SetTrcvMode to set the mode of Controller/Trcv (including SLEEP mode). When a wake-up event occurs, CanIf_CheckWakeup can be called to detect whether the event is caused by the Controller/Trcv. CanIf_CheckValidation can be used to confirm the wake-up (a wake-up is confirmed upon receipt of any Pdu/NM Pdu, see whether the configuration item CanIfPublicWakeupCheckValidByNM is checked).


偏差(Deviation)
---------------------------------------------------------------------------------------------------

None


扩展(Expansion)
---------------------------------------------------------------------------------------------------

None
