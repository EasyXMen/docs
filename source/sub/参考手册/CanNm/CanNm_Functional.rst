功能描述（Functional Description）
========================================

特性（Features）
-------------------------

AUTOSAR CanNm基于分散的直接网络管理策略，这意味着每个网络节点仅根据在通信系统内接收和/或发送报文，执行自给自足的活动。

AUTOSAR CanNm is based on a decentralized direct network management strategy, which means that each network node performs self-sufficient activities only based on receiving and/or sending messages within the communication system.

AUTOSAR CanNm协调算法基于周期性的NM数据包，集群中的所有节点都通过广播传输接收这些数据包。接收到NM数据包表明发送节点要保持NM集群处于唤醒状态。如果任何节点准备好进入总线睡眠模式，它将停止发送NM数据包，但是只要接收到来自其他节点的NM数据包，它就会推迟过渡到总线睡眠模式。如果在专用计时器超时前都未接收到NM数据包，则每个节点都会启动到总线休眠模式的转换。CanNm通过状态机切换和各状态定时器管理来完成协调算法。

The AUTOSAR CanNm coordination algorithm is based on periodic NM data packets, which all nodes in the cluster receive through broadcast transmission. Receiving an NM data packet indicates that the sending node intends to keep the NM cluster in an awake state. If any node is ready to enter the bus sleep mode, it will stop sending NM data packets. However, it will postpone the transition to the bus sleep mode as long as it receives NM data packets from other nodes. If no NM data packets are received before a dedicated timer expires, each node will initiate the transition to the bus sleep mode. CanNm completes the coordination algorithm through state machine switching and the management of timers for each state.

通道状态管理功能（Channel Status Management Function）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

从网络管理集群中单个节点的角度来看，AUTOSAR CanNm状态机包含算法所需的状态、切换和触发。通道的状态切换在触发切换后的下一个主函数中处理，且每当模式切换完成后通过API将状态通知到上层节点（NmIf）。

From the perspective of a single node in the network management cluster, the AUTOSAR CanNm state machine includes the states, transitions, and triggers required by the algorithm. The state transition of the channel is handled in the next main function after the transition is triggered, and the state is notified to the upper-layer node (NmIf) through the API whenever the mode transition is completed.

AUTOSAR CanNm状态机包含三种操作模式（Mode）。

The AUTOSAR CanNm state machine includes three operating modes.

- Network Mode 网络模式
- Prepare Bus-Sleep Mode 总线预睡眠模式
- Bus-Sleep Mode 总线睡眠模式

.. figure:: ../../../_static/参考手册/CanNm/CanNmStateMachine.png
   :alt: CanNmStackMachine
   :align: center

   CanNm Stack Machine

网络模式（Network Mode）
******************************

网络模式包含以下三个子状态（State）：

Network Mode includes the following three sub-states (State):

- Rpeate Message State 重复报文状态
- Normal Operation State 正常运行状态
- Ready Sleep State 准备睡眠状态

重复报文状态（Repeat Message State）
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

当节点配置为Passive Mode的节点，意味着该节点只能接受报文而不能传输任何报文，关于Passive Mode具体的将在下面章节中进行说明。
对于非Passive Mode的节点，Repeat Message State可确保从Bus-Sleep或Prepare Bus-Sleep到Network Mode的任何过渡对于网络上的其他节点都是可见的。此外，它确保所有节点在CanNmRepeatMessageTime（配置参数）内保持活动状态。当CanNmRepeatMessageTime配置为0，表示未配置Repeat Message State。这意味着Repeat Message State是瞬态的，在进入后立即离开，因此无法保证启动稳定性，并且无法执行节点检测过程。当CanNmRepeatMessageTime超时后，节点将离开Repeat Message State而切至其他状态。若当前网络状态为请求，切换到Normal Operation State，若当前网络状态为释放，切换到Ready SleepState。
当非Passive Mode的节点从Bus-SleepMode, Prepare-Bus-Sleep Mode，Normal Operation State或Ready Sleep State进入Repeat Message State时，传输功能应该被重启，为了防止总线数据爆发，降低负载，每次进入Repeat Message State时，都要延迟CanNmMsgCycleOffset（配置参数）段时间后，再开始传输数据，若配置CanNmImmediateNmTransmissions并且网络被请求则不需要延迟CanNmMsgCycleOffset时间。


When a node is configured as a Passive Mode node, it means that the node can only receive messages and cannot transmit any messages. The details of Passive Mode will be explained in the following chapters.
For nodes that are not in Passive Mode, the Repeat Message State ensures that any transition from Bus-Sleep or Prepare Bus-Sleep to Network Mode is visible to other nodes on the network. In addition, it ensures that all nodes remain active within the CanNmRepeatMessageTime (a configuration parameter). When CanNmRepeatMessageTime is configured as 0, it indicates that the Repeat Message State is not configured. This means the Repeat Message State is transient and will exit immediately after entering, so start-up stability cannot be guaranteed and the node detection process cannot be executed. When CanNmRepeatMessageTime times out, the node will leave the Repeat Message State and switch to another state. If the current network state is "request", it will switch to the Normal Operation State; if the current network state is "release", it will switch to the Ready Sleep State.
When a non-Passive Mode node enters the Repeat Message State from Bus-Sleep Mode, Prepare-Bus-Sleep Mode, Normal Operation State, or Ready Sleep State, the transmission function should be restarted. To prevent bus data bursts and reduce load, each time entering the Repeat Message State, data transmission should start after a delay of CanNmMsgCycleOffset (a configuration parameter). However, if CanNmImmediateNmTransmissions is configured and the network is requested, there is no need to delay for the CanNmMsgCycleOffset time.

正常运行状态（Normal Operation State）
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Normal Operation State可确保只要需要网络功能，任何节点都可以使NM集群保持唤醒状态。当处于Normal Operation State，节点按照CanNmMsgCycleTime周期发送报文，当网络释放后，CanNm进入ReadySleep state。

The Normal Operation State ensures that any node can keep the NM cluster awake as long as network functionality is required. When in the Normal Operation State, the node sends messages at intervals of CanNmMsgCycleTime. Once the network is released, CanNm enters the Ready Sleep state.

准备睡眠状态（Ready Sleep State）
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Ready Sleep State可确保NM群集中的任何节点都在等待过渡到Prepare Bus-Sleep Mode。
当进入Ready Sleep State，本节点就不再发送网络管理报文。当节点接收到其他节点传输的网络管理报文时，会将NM-Timeout定时器重置，当NM-Timeout定时器超时且处于Ready Sleep State时，网络管理进入Prepare Bus-Sleep Mode。其中NM-Timeout定时器的时间是由CanNmTimeoutTime（配置参数）决定的。

The Ready Sleep State ensures that any node in the NM cluster is waiting to transition to the Prepare Bus-Sleep Mode.
When entering the Ready Sleep State, the node stops sending network management messages. When the node receives network management messages transmitted by other nodes, it resets the NM-Timeout timer. When the NM-Timeout timer expires while the node is in the Ready Sleep State, the network management enters the Prepare Bus-Sleep Mode. The duration of the NM-Timeout timer is determined by the CanNmTimeoutTime (a configuration parameter).

总线预睡眠模式（Prepare Bus-Sleep Mode）
******************************************************

Prepare Bus Sleep state目的是确保所有节点都有时间在进入总线休眠状态之前停止其网络活动，使总线活动平静下来，最后在“准备总线睡眠模式”下总线上没有任何活动。
当本节点进入Prepare Bus-Sleep Mode，CanNmWaitBusSleepTime（配置参数）定时器被启动，当CanNmWaitBusSleepTime定时器超时，当前状态将由Prepare Bus-Sleep Mode切换至Bus-Sleep Mode。
如果在Prepare Bus-Sleep Mode接收到其他节点传输的网络管理报文时，当前CanNm状态将由Prepare Bus-Sleep Mode切换至Network Mode，默认情况下，将进入Repeat Message State。
如果在Prepare Bus-Sleep Mode接收到网络请求时，当前状态将由Prepare Bus-Sleep Mode切换至Network Mode，默认情况下，将进入Repeat Message State。如果CanNmImmediateRestartEnabled（配置参数）被设置为TRUE，那么在这种情况下会立刻触发一次传输，这样做的理由是：集群中的其他节点仍处于Prepare Bus-Sleep Mode，在这种特殊情况下，应避免过渡到Bus-Sleep Mode，并应尽快恢复总线通信。由于CanNm中网络管理PDU的传输偏移导致，处于Repeat Message State的第一个网络管理PDU的传输可能会大大延迟。为了避免延迟重新启动网络可以立即请求发送网络管理PDU。

The purpose of the Prepare Bus Sleep state is to ensure that all nodes have time to stop their network activities before entering the bus sleep state, so as to calm down the bus activities. Finally, there will be no activity on the bus in the "Prepare Bus Sleep Mode".
When the local node enters the Prepare Bus-Sleep Mode, the CanNmWaitBusSleepTime (configuration parameter) timer is started. When the CanNmWaitBusSleepTime timer expires, the current state will switch from Prepare Bus-Sleep Mode to Bus-Sleep Mode.
If a network management message transmitted by another node is received in the Prepare Bus-Sleep Mode, the current CanNm state will switch from Prepare Bus-Sleep Mode to Network Mode, and by default, it will enter the Repeat Message State.
If a network request is received in the Prepare Bus-Sleep Mode, the current state will switch from Prepare Bus-Sleep Mode to Network Mode, and by default, it will enter the Repeat Message State. If CanNmImmediateRestartEnabled (configuration parameter) is set to TRUE, a transmission will be triggered immediately in this case. The reason for doing this is that other nodes in the cluster are still in the Prepare Bus-Sleep Mode. In this special case, the transition to Bus-Sleep Mode should be avoided, and bus communication should be restored as soon as possible. Due to the transmission offset of the network management PDU in CanNm, the transmission of the first network management PDU in the Repeat Message State may be significantly delayed. To avoid delaying the restart of the network, the transmission of the network management PDU can be requested immediately.

总线睡眠模式（Bus-Sleep Mode）
*****************************************

Bus-Sleep state的目的是在不交换任何消息时降低节点的功耗。将通信控制器切换到睡眠模式，激活相应的唤醒机制，最后将功耗降低到总线睡眠模式下的适当水平。
当CanNm处于Bus-Sleep Mode接收到网络管理报文时，此时CanNm不会切换至Network Mode，而是通知Nm模块，由上层模块做决策。
当CanNm处于Bus-Sleep Mode接收到被动请求或网络请求时，当前状态将由Bus-Sleep Mode切换至Network Mode，默认情况下，将进入Repeat Message State。

The purpose of the Bus-Sleep state is to reduce the power consumption of the node when no messages are being exchanged. The communication controller is switched to sleep mode, the corresponding wake-up mechanism is activated, and finally the power consumption is reduced to an appropriate level in the bus sleep mode.
When CanNm is in Bus-Sleep Mode and receives a network management message, CanNm will not switch to Network Mode at this time; instead, it will notify the Nm module, and the upper-layer module will make the decision.
When CanNm is in Bus-Sleep Mode and receives a passive request or a network request, the current state will switch from Bus-Sleep Mode to Network Mode, and by default, it will enter the Repeat Message State.

AUTOSAR NM 报文格式（AUTOSAR NM Message Format）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

AUTOSAR NM 报文有特定的格式要求，NM报文总长度视总线特性而定，受总线MTU限制。报文数据段格式如图：

AUTOSAR NM messages have specific format requirements. The total length of an NM message depends on the characteristics of the bus and is limited by the bus MTU. The format of the message data segment is as shown in the figure:

.. figure:: ../../../_static/参考手册/Nm/NM_message_layout_example.png
   :alt: Nm报文格式图
   :align: center

   NM message layout example

- Control Bit Vector(CBV)：长度为一字节的可选字段，根据配置可以处于NM报文第一、二字节或者不使用。FlexRay总线仅可处于第一字节或不使用。该字节信息如下图
    
   Control Bit Vector (CBV): an optional field with a length of one byte, which can be located in the first or second byte of the NM message or not used at all according to the configuration. For the FlexRay bus, it can only be in the first byte or not used. The information of this byte is as shown in the following figure.

.. figure:: ../../../_static/参考手册/Nm/CBV_layout.png
   :alt: CBV排版图
   :align: center

   CBV layout

- Source Node ID (SNI)：长度为一字节的可选字段，根据配置可以处于NM报文第一、二字节或者不使用。FlexRay总线仅可处于第二字节或不使用。该字节数据根据通道配置决定。
    
   Source Node ID (SNI): an optional field with a length of one byte, which can be located in the first or second byte of the NM message or not used at all according to the configuration. For the FlexRay bus, it can only be in the second byte or not used. The data of this byte is determined by the channel configuration.

- User Data of n Bytes：若干字节的可选字段，CBV和SNI之外的字节都为User Data部分。该字段包含两部分，即User data和PNC bit Vector，这两部分均为根据配置决定是否支持，若同时支持则严格要求ser data和PNC bit Vector各自的字节必须连续
    
   User Data of n Bytes: an optional field consisting of several bytes. All bytes except those of CBV and SNI belong to the User Data part. This field includes two parts, namely User data and PNC bit Vector. Both parts are configurable in terms of whether they are supported. If both are supported, it is strictly required that the respective bytes of User data and PNC bit Vector must be continuous.

通信调度功能（Communication scheduling function）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

CanNm提供周期性网络管理报文发送功能：该功能根据配置项CanNmPassiveModeEnabled决定是否启用，当CanNmPassiveModeEnabled为TRUE意为启动CanNm模块启动被动模式，仅接收报文并不主动参加网络管理；该功能也可动态的被诊断通信控制服务启停。
CanNm提供配置项CanNmMsgCycleTime作为常规的报文周期，提供CanNmMsgCycleOffset、CanNmImmediateNmTransmissions、CanNmBusLoadReductionEnabled作为网络管理报文发送方向上特殊场景的附加属性。

CanNm provides the function of sending periodic network management messages: This function is enabled or disabled according to the configuration item CanNmPassiveModeEnabled. When CanNmPassiveModeEnabled is TRUE, it means that the CanNm module starts the passive mode, in which it only receives messages and does not actively participate in network management; This function can also be dynamically started or stopped by the diagnostic communication control service.
CanNm provides the configuration item CanNmMsgCycleTime as the regular message cycle, and provides CanNmMsgCycleOffset, CanNmImmediateNmTransmissions, and CanNmBusLoadReductionEnabled as additional attributes for special scenarios in the sending direction of network management messages.

如果一个NM PDU被成功接收，下层(例如. CanIf )通过函数调用CanNm_RxIndication通知CanNm。CanNm根据PduId匹配相应的通道配置，如是否支持CBV，若支持则根据CBV字节位置逐bit解析、若使能PN则处理PNC Bit Vector字段、重置NM-Timeout计时器等

If an NM PDU is successfully received, the lower layer (e.g., CanIf) notifies CanNm through the function call CanNm_RxIndication. CanNm matches the corresponding channel configuration based on the PduId, such as whether CBV is supported. If supported, it parses bit by bit according to the position of the CBV byte; if PN is enabled, it processes the PNC Bit Vector field; and it resets the NM-Timeout timer, etc.

快速发送（Quick transmission）
**********************************************

快速发送机制根据配置参数CanNmImmediateNmTransmissions决定。该改参数为0时意为不启动；当该参数配置大于0时意为快速发送的报文次数，需要再配置CanNmImmediateNmCycleTime作为快速发送时报文发送周期。
快速发送机制仅作用于Repeat Message State阶段，当通道被主动请求第一次进入网络模式时，或CanNmPnHandleMultipleNetworkRequests为TRUE且有网络请求时，进入Repeat Message State触发快速发送CanNmImmediateNmTransmissions次网络管理报文。当快速发送次数结束时，恢复常规的发送周期。

The quick transmission mechanism is determined by the configuration parameter CanNmImmediateNmTransmissions. When this parameter is 0, it means the mechanism is not activated; when the parameter is configured to be greater than 0, it indicates the number of messages to be sent in quick transmission, and in this case, CanNmImmediateNmCycleTime needs to be configured as the message sending cycle during quick transmission.
The quick transmission mechanism only takes effect in the Repeat Message State phase. When a channel is actively requested to enter the network mode for the first time, or when CanNmPnHandleMultipleNetworkRequests is TRUE and there is a network request, the node enters the Repeat Message State and triggers the quick transmission of network management messages for CanNmImmediateNmTransmissions times. When the quick transmission count is completed, the regular sending cycle is restored.

总线负载降低（Bus load reduction）
******************************************

当同一总线上的ECU被同时唤醒时，将同时进入Repeat Message状态并开始发送网络管理报文，将造成总线负载在瞬间提高，为此提供CanNmMsgCycleOffset使ECU首次发送报文时延迟一段时间，该参数数值基于网络集群大小，以便于各个ECU配置不同的数值。因此必须有一种机制，可以独立于网络管理集群的大小来降低总线负载。
总线负载降低为CanNm的可选功能：当CanNmBusLoadReductionEnabled参数配置为TRUE时，CanNm应该支持总线负载降低机制。该机制仅使能在Normal Opeation State，通过配置参数CanNmMsgReducedTime和不断切换报文发送周期计时器以实现该机制。

When ECUs on the same bus are woken up simultaneously, they will all enter the Repeat Message state and start sending network management messages, which will cause an instantaneous increase in bus load. To address this, CanNmMsgCycleOffset is provided to delay the first message transmission of ECUs by a certain period. The value of this parameter is based on the size of the network cluster, allowing different values to be configured for each ECU. Therefore, a mechanism must exist to reduce bus load independently of the size of the network management cluster.
Bus load reduction is an optional function of CanNm: when the CanNmBusLoadReductionEnabled parameter is configured as TRUE, CanNm should support the bus load reduction mechanism. This mechanism is only enabled in the Normal Operation State and is implemented through the configuration parameter CanNmMsgReducedTime and the continuous switching of message transmission cycle timers.

当总线负载降低机制启动后，CanNm_RxIndication()被调用后（接收到报文），使用CanNmMsgReducedTime参数重装内部的报文发送计时器，当成功发送NM-PDU后（CanIf_Transmit返回E_OK），用CanNmMsgCycleTime参数重装内部的报文发送计时器。
CanNmMsgReducedTime参数数值要求： CanNmMsgCycleTime/2 < CanNmMsgReducedTime < CanNmMsgCycleTime。因此最终实现一个网络集群中仅有CanNmMsgReducedTime数值最小的两个节点交替发送网络管理报文。

When the bus load reduction mechanism is activated, after CanNm_RxIndication() is called (upon receiving a message), the internal message transmission timer is reloaded with the CanNmMsgReducedTime parameter. When the NM-PDU is successfully transmitted (CanIf_Transmit returns E_OK), the internal message transmission timer is reloaded with the CanNmMsgCycleTime parameter.
Requirements for the value of CanNmMsgReducedTime: CanNmMsgCycleTime/2 < CanNmMsgReducedTime < CanNmMsgCycleTime. Therefore, the final implementation ensures that only the two nodes with the smallest CanNmMsgReducedTime values in a network cluster alternately send network management messages.

报文失败重发（Message failure retransmission）
****************************************************

报文发送失败为CanNm的可选机制，因为Can通道状态切换为异步处理，因此可能造成网络管理报文发送时，通道状态未切换导致发送被CanIf拒绝。
失败重发存在两种触发场景：

The message transmission failure is an optional mechanism of CanNm. Since the state switching of the Can channel is processed asynchronously, it may cause the transmission to be rejected by CanIf due to the channel state not being switched when sending network management messages.
There are two trigger scenarios for failure retransmission:

- CanNmImmediateNmTransmissions大于0，确保快速发送次数均能成功发送

  If CanNmImmediateNmTransmissions is greater than 0, it ensures that all quick transmission attempts can be sent successfully.

快速发送阶段，每当CanIf_Transmit返回E_NOT_OK时，则在后续每次主函数中调用一次CanIf_Transmit直到返回E_OK并递减快速发送次数，直到完成全部次数快速发送。最坏情况若存在某次报文始终无法成功发送，则在离开Repeat Message State关闭快速发送时一并停掉重发功能。

During the quick transmission phase, whenever CanIf_Transmit returns E_NOT_OK, CanIf_Transmit will be called once in each subsequent main function until it returns E_OK, and the number of quick transmissions will be decremented until all quick transmissions are completed. In the worst-case scenario, if a certain message cannot be sent successfully all the time, the retransmission function will be stopped when exiting the Repeat Message State and turning off the quick transmission.

- CanNmRetryFirstMessageRequest配置为TRUE，确保进入网络模式的首帧报文一定成功发送

  If CanNmRetryFirstMessageRequest is configured as TRUE, it ensures that the first frame message entering the network mode is successfully sent.

当通道状态第一次切换到网络模式时，根据配置决定是否确保首帧发送成功。若调用CanIf_Transmit返回E_NOT_OK，则在后续每次主函数中调用一次CanIf_Transmit直到返回E_OK。最坏情况若CanIf_Transmit始终返回E_NOT_OK，则若通道状态进入Normal Opeartion State时仍可在后续主函数中触发发送，若进入Ready Sleep State停止网络管理报文发送功能时一并停掉重发功能。

When the channel state switches to Network Mode for the first time, whether to ensure the successful transmission of the first frame is determined according to the configuration. If calling CanIf_Transmit returns E_NOT_OK, CanIf_Transmit will be called once in each subsequent main function until it returns E_OK. In the worst-case scenario, if CanIf_Transmit always returns E_NOT_OK, transmission can still be triggered in subsequent main functions when the channel state enters the Normal Operation State; if the channel state enters the Ready Sleep State and the network management message transmission function is stopped, the retransmission function will be stopped together.

CanNm附加功能（CanNm Additional Functions）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

检测远程睡眠指示（Detection of remote sleep indication）
****************************************************************

远程睡眠指示应用于一种情况，当处于NormalOperation State的节点发现集群中的所有其他节点都准备睡眠，但处于Normal Operation State状态的节点仍将保持总线苏醒。为了避免这种情况，可以使能远程睡眠指示功能。
如果当前CanNm状态为Normal Operation State，并且在CanNmRemoteSleepIndTime（配置参数）定时器内未收到其他节点发送的网络管理报文，则通知上层Nm模块集群内的其他节点均已准备睡眠。
如果CanNm已通知上层Nm模块，而在Normal Operation State或Ready Sleep State下又收到了网络管理报文，或者CanNm从Normal Operation State切换至Repeat Message State，CanNm需要通知上层Nm模块集群中的某些节点不再准备睡眠。

The remote sleep indication applies to a situation where a node in the Normal Operation State detects that all other nodes in the cluster are ready to sleep, but the node in the Normal Operation State will still keep the bus awake. To avoid this situation, the remote sleep indication function can be enabled.
If the current CanNm state is Normal Operation State and no network management messages sent by other nodes are received within the CanNmRemoteSleepIndTime (a configuration parameter) timer, the upper-layer Nm module will be notified that all other nodes in the cluster are ready to sleep.
If CanNm has notified the upper-layer Nm module, but receives a network management message again in the Normal Operation State or Ready Sleep State, or if CanNm switches from the Normal Operation State to the Repeat Message State, CanNm needs to notify the upper-layer Nm module that some nodes in the cluster are no longer ready to sleep.

用户数据（User Data）
*****************************************************

使用CanNmUserDataEnabled开关（配置参数）对NM用户数据的支持进行静态配置。
当用户数据功能使能，可以调用CanNm_SetUserData（CanNmComUserDataSupport为FALSE），该函数可以设置总线上接下来发送的NM数据包的NM用户数据。也可以调用CanNm_GetUserData，该函数可以提供包含在最近接收到的NM PDU的有效载荷中的NM用户数据。
如果CanNmComUserDataSupport（配置参数）配置为使能，CanNm将在每次请求发送相应的NM消息之前从引用的NM I-PDU收集NM用户数据，并将用户数据与其他NM字节合并。此时就不能再通过CanNm_SetUserData函数设置用户数据。

The support for NM user data is statically configured using the CanNmUserDataEnabled switch (a configuration parameter).
When the user data function is enabled, CanNm_SetUserData (with CanNmComUserDataSupport set to FALSE) can be called. This function can set the NM user data for the next NM data packet to be sent on the bus. Additionally, CanNm_GetUserData can be called, which provides the NM user data contained in the payload of the most recently received NM PDU.
If CanNmComUserDataSupport (a configuration parameter) is configured to be enabled, CanNm will collect NM user data from the referenced NM I-PDU before each request to send the corresponding NM message, and merge the user data with other NM bytes. In this case, the user data can no longer be set through the CanNm_SetUserData function.

被动模式（Passive Mode）
*******************************************

在被动模式下，节点仅接收NM消息，但不发送任何NM消息。被动模式应使用CanNmPassiveModeEnabled开关（配置参数）进行静态配置。

In passive mode, a node only receives NM messages but does not send any NM messages. Passive mode shall be statically configured using the CanNmPassiveModeEnabled switch (a configuration parameter).

NM-Pdu接收（Reception of NM-PDU）
**************************************

若CanNmPduRxIndicationEnabled（配置参数）使能，在成功接收NM PDU时，CanNm应通过调用Nm_PduRxIndication通知上层。

If the CanNmPduRxIndicationEnabled (configuration parameter) is enabled, CanNm shall notify the upper layer by calling Nm_PduRxIndication upon successful reception of an NM PDU.

状态改变通知（State change notification）
******************************************

如果CanNmStateChangeIndEnabled（配置参数）使能，则CanNm需要将CanNm状态的所有更改通知上层Nm。

If the CanNmStateChangeIndEnabled (configuration parameter) is enabled, CanNm needs to notify the upper-layer Nm of all changes in the CanNm state.

通信控制（Communication Control）
******************************************

使用CanNmComControlEnabled开关（配置参数），可以静态配置通信控制。当CanNm_DisableCommunication函数被调用，CanNm模块NM报文的传输能力将被停止，直到调用CanNm_EnableCommunication，CanNm的nm报文传输能力被恢复。

Communication control can be statically configured using the CanNmComControlEnabled switch (a configuration parameter). When the CanNm_DisableCommunication function is called, the NM message transmission capability of the CanNm module will be stopped. The NM message transmission capability of CanNm will be restored until CanNm_EnableCommunication is called.

.. hint::

   网络释放时，CanNm_DisableCommunication和CanNm_EnableCommunication成对使用。

   When the network is released, CanNm_DisableCommunication and CanNm_EnableCommunication are used in pairs.
   
   当CanNm_DisableCommunication函数被调用，CanNm的NM-Timeout定时器将被停止，调用函数CanNm_EnableCommunication，NM-Timeout定时器将被恢复。因此在CanNm_EnableCommunication尚未调用前，若释放网络，通道状态将停留在ReadySleep状态，休眠将被阻塞，需要在CanNm_EnableCommunication调用后才可进入Prepare-Bus-Sleep模式。

   When the CanNm_DisableCommunication function is called, the NM-Timeout timer of CanNm will be stopped. When the CanNm_EnableCommunication function is called, the NM-Timeout timer will be restored. Therefore, if the network is released before CanNm_EnableCommunication is called, the channel state will remain in the ReadySleep state, and hibernation will be blocked. The system can only enter the Prepare-Bus-Sleep mode after CanNm_EnableCommunication is called.

协调同步（Coordinated synchronization）
************************************************

当有多个协调器连接到同一条总线时，在CBV中，NmCoordinatorSleepReady位用于指示主协调器请求启动关闭。
当CanNm处于网络模式，接收网络管理报文的CBV中NmCoordinatorSleepReady=1，则CanNm通知上层协调睡眠功能被请求。
当CanNm已通知上层协调睡眠功能被请求，接收网络管理报文的CBV中NmCoordinatorSleepReady=0，则CanNm通知上层协调睡眠功能请求被取消。

When multiple coordinators are connected to the same bus, in the CBV, the NmCoordinatorSleepReady bit is used to indicate that the main coordinator requests to initiate a shutdown.
When CanNm is in network mode and the NmCoordinatorSleepReady bit in the CBV of the received network management message is set to 1, CanNm notifies the upper layer that the coordinated sleep function is requested.
When CanNm has notified the upper layer that the coordinated sleep function is requested, and the NmCoordinatorSleepReady bit in the CBV of the received network management message is set to 0, CanNm notifies the upper layer that the request for the coordinated sleep function is cancelled.

车辆唤醒（Vehicle wake-up）
************************************

当CanNmCarWakeUpRxEnabled（配置参数）使能时，车辆唤醒功能被启用，目前暂时没有使用场景。如果任何接收到的NM-PDU中的Car Wakeup位为1，都会通知上层Nm。
当CanNmCarWakeUpRxEnabled（配置参数）使能，CanNmCarWakeUpFilterEnabled（配置参数）也使能时，只有收到NodeId等于CanNmCarWakeUpFilterNodeId的报文时，才会通知上层。

When the CanNmCarWakeUpRxEnabled (configuration parameter) is enabled, the vehicle wake-up function is activated, but there are currently no application scenarios for it. If the Car Wakeup bit in any received NM-PDU is 1, the upper-layer Nm will be notified.
When both CanNmCarWakeUpRxEnabled (configuration parameter) and CanNmCarWakeUpFilterEnabled (configuration parameter) are enabled, the upper layer will only be notified when a message with a NodeId equal to CanNmCarWakeUpFilterNodeId is received.

PNC
******************

Autosar4.x版本开始支持PN功能，Pn功能的目的是基于功能划分网络，形成局域网；这种功能的划分由整车设计完成，对于各节点只需要关心自身存在的网段。只有在CanNmGlobalPnSupport(配置参数)和各通道下的CanNmPnEnabled(配置参数)使能的情况下，Pn功能才能正常工作。
如果CanNmPnEnabled(配置参数)为FALSE，则CanNm将执行常规的Rx处理，并且应禁用Pn功能。如果CanNmPnEnabled为TRUE，接收到的NM-PDU CBV中的PNI位为0，则CanNm模块应执行常规的Rx处理，从而省去了Pn功能的扩展。如果CanNmPnEnabled为TRUE并且接收到的NM-PDU CBV中的PNI位为1，则CanNm模块处理NM-PDU的Pn信息。

The PN function has been supported since the Autosar 4.x version. The purpose of the PN function is to divide the network based on functions to form local area networks; this functional division is completed by the vehicle design, and each node only needs to care about the network segment it belongs to. The PN function can work normally only when CanNmGlobalPnSupport (a configuration parameter) and CanNmPnEnabled (a configuration parameter) under each channel are enabled.
If CanNmPnEnabled (the configuration parameter) is FALSE, CanNm will perform regular Rx processing, and the PN function shall be disabled. If CanNmPnEnabled is TRUE and the PNI bit in the received NM-PDU CBV is 0, the CanNm module shall perform regular Rx processing, thus omitting the extension of the PN function. If CanNmPnEnabled is TRUE and the PNI bit in the received NM-PDU CBV is 1, the CanNm module processes the PN information of the NM-PDU.

如果CanNmPnEnabled为TRUE，则必须使用CBV，且发送报文时应将CBV中发送的PNI位的值设置为1；如果CanNmPnEnabled为FALSE，若使用CBV，则发送报文时应将CBV中的PNI位的值始终设置为0。

If CanNmPnEnabled is TRUE, the CBV must be used, and the value of the PNI bit sent in the CBV shall be set to 1 when sending a message; if CanNmPnEnabled is FALSE, and if the CBV is used, the value of the PNI bit in the CBV shall always be set to 0 when sending a message.

PNC是Partial Network Cluster的缩写，它是指为了在车辆网络中支持一个或多个车辆功能而由多个ECU构成的集群。PNC的编号我们称为PNC ID，范围8~63，整车网络统一编号，关于PNC id与CanNmPdu映射关系说明：PNC ID对应CanNmPdu中的一个bit，例如PNC ID=8，对应CanNmPduByte1的bit0；PNC ID=63，对应Byte7的bit7；PNC ID对应的bit数值为1，则表示当前PN网络被请求，为0则表示网络释放。

PNC is the abbreviation of Partial Network Cluster, which refers to a cluster composed of multiple ECUs to support one or more vehicle functions in the vehicle network. The number of PNC is called PNC ID, with a range of 8 to 63, and it is uniformly numbered in the vehicle network. The description of the mapping relationship between PNC ID and CanNmPdu is as follows: A PNC ID corresponds to a bit in CanNmPdu. For example, PNC ID = 8 corresponds to bit 0 of CanNmPduByte1; PNC ID = 63 corresponds to bit 7 of Byte7; if the bit value corresponding to the PNC ID is 1, it indicates that the current PN network is requested; if it is 0, it indicates that the network is released.

Pn信息的位置位于网络管理报文的用户数据部分中，具体的位置根据Nm模块配置决定：NmPncBitVectorOffset和NmPncBitVectorLength。
例如当NmPncBitVectorOffset = 3，NmPncBitVectorLength = 2，代表NM报文只有字节3和字节4包含PN请求信息。

The location of Pn information is in the user data part of the network management message, and the specific location is determined by the configuration of the Nm module: NmPncBitVectorOffset and NmPncBitVectorLength.
For example, when NmPncBitVectorOffset = 3 and NmPncBitVectorLength = 2, it means that only byte 3 and byte 4 of the NM message contain PN request information.

接收（Reception）
^^^^^^^^^^^^^^^^^^^^^^^^^^

当通道使能CanNmPnEnabled为TRUE，且CBV中PNI为1，则需要对PNC Bit Vector字段进行过滤。
过滤操作由Nm模块完成，通过提供PNC bit vector字段起始地址调用Nm_PncBitVectorRxIndication接口，根据返回值RelevantPncRequestDetected判断接收到的报文是否与该通道相关，若相关则属于过滤通过，可以对报文进行后续处理。若过滤不通过则丢弃本次接收到的报文，不做任何处理。

When the channel has CanNmPnEnabled set to TRUE and the PNI in the CBV is 1, filtering of the PNC Bit Vector field is required.
The filtering operation is performed by the Nm module. It calls the Nm_PncBitVectorRxIndication interface by providing the starting address of the PNC bit vector field. Based on the return value RelevantPncRequestDetected, it is determined whether the received message is related to the channel. If it is related, the filtering is passed, and subsequent processing can be performed on the message. If the filtering fails, the received message is discarded without any processing.

当通道使能CanNmPnEnabled为TRUE，且CBV中PNI为0，视为过滤失败则丢弃本次接收到的报文，不做任何处理。

When the channel has CanNmPnEnabled set to TRUE and the PNI in the CBV is 0, it is regarded as a filtering failure, and the received message will be discarded without any processing.

当过滤失败时，若配置项CanNmAllNmMessagesKeepAwake为TRUE则也可进行后续处理而不丢弃报文。

When the filtering fails, if the configuration item CanNmAllNmMessagesKeepAwake is set to TRUE, subsequent processing can also be performed without discarding the message.

当通道使能CanNmPnEnabled为FALSE，则不进行过滤，对报文进行后续处理而不丢弃报文。

When the channel has CanNmPnEnabled set to FALSE, no filtering is performed, and subsequent processing is carried out on the message without discarding it.

发送（Transmit）
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

如果网络被请求并且CanNmPnHandleMultipleNetworkRequests（配置参数）设置为TRUE，无论CanNm处于Ready Sleep State，Normal Operation State或Repeat Message State，CanNm应更改为或重新启动为Repeat Message State。并且，CanNm会传输CanNmImmediateNmTransmissions（配置参数）数量的报文，其中第一条报文立即传输，其他报文按CanNmImmediateNmCycleTime传输（配置参数）。

If the network is requested and the CanNmPnHandleMultipleNetworkRequests (configuration parameter) is set to TRUE, CanNm shall switch to or restart the Repeat Message State regardless of whether it is in the Ready Sleep State, Normal Operation State, or Repeat Message State. In addition, CanNm will transmit a number of messages equal to the value of CanNmImmediateNmTransmissions (configuration parameter), where the first message is transmitted immediately, and the other messages are transmitted according to CanNmImmediateNmCycleTime (configuration parameter).

当通道使能CanNmPnEnabled为TRUE，每次发送网络管理报文时，提供PNC bit vector字段起始地址调用Nm_PncBitVectorTxIndication接口以填充该字段。
When the channel has CanNmPnEnabled set to TRUE, each time a network management message is sent, the starting address of the PNC bit vector field is provided to call the Nm_PncBitVectorTxIndication interface to populate this field.

.. only:: doc_pbs
 
  多变体支持（Multi-variant support）
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  
    CanNm 支持在不同变体中：
  
    CanNm supports in different variants:
  
  - 支持报文发送前的不同的偏移周期
  
     Support different offset periods before message transmission
  
  - 支持配置不同的总线负载降低计时器
  
     Support configuring different bus load reduction timers
  
  - 支持配置不同的节点ID
  
     Support configuring different node IDs
  
  - 支持配置是否启用PNC功能，以及含PNC的报文发送超时计时器
  
     Support configuring whether to enable the PNC function and the timeout timer for sending messages containing PNC.
  
  - 支持不同的NM-Pdu收发路径
  
     Support different NM-Pdu sending and receiving paths


偏差（Deviation）
----------------------
.. 有序列表示例

#. 不支持 Dynamic PNC-to-channel-mapping。

   Dynamic PNC-to-channel mapping is not supported.

#. 不支持 Pnc shutdown

   Pnc shutdown is not supported.


扩展
-------------

#. 添加配置项CanNmRetryFirstMessageRequest（Add the configuration item CanNmRetryFirstMessageRequest）  

   该配置以实现当通道唤醒时，Can通道状态尚未进入FULL_COM，导致CanNm首帧报文未能及时发送

   This configuration is implemented to address the issue where the CanNm first frame message fails to be sent in a timely manner because the Can channel status has not yet entered FULL_COM when the channel is awakened.