功能描述 Functional Description
==============================================================

特性 Features
------------------------------------------------------------------------------------------------

AUTOSAR UdpNm基于分散的直接网络管理策略，这意味着每个网络节点仅根据在通信系统内接收和/或发送报文，执行自给自足的活动。

AUTOSAR UdpNm is based on a decentralized direct network management strategy, which means that each network node performs self-sufficient activities based solely on the messages it receives and/or transmits within the communication system.

AUTOSAR UdpNm协调算法基于周期性的NM数据包，集群中的所有节点都通过广播传输接收这些数据包。接收到NM数据包表明发送节点要保持NM集群处于唤醒状态。如果任何节点准备好进入总线睡眠模式，它将停止发送NM数据包，但是只要接收到来自其他节点的NM数据包，它就会推迟过渡到总线睡眠模式。如果在专用计时器超时前都未接收到NM数据包，则每个节点都会启动到总线休眠模式的转换。UdpNm通过状态机切换和各状态定时器管理来完成协调算法

The AUTOSAR UdpNm coordination algorithm is based on periodic NM packets, which are received via broadcast by all nodes in the cluster. The reception of an NM packet indicates that the sending node wants to keep the NM cluster awake. If any node is ready to enter the bus-sleep mode, it stops sending NM packets but postpones the transition to bus-sleep mode as long as it receives NM packets from other nodes. If no NM packets are received before a dedicated timer expires, each node initiates the transition to the bus-sleep mode. UdpNm accomplishes this coordination algorithm through state machine switches and the management of various state timers.


通道状态管理功能 Channel State Management Function
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

从网络管理集群中单个节点的角度来看，AUTOSAR UdpNm状态机包含算法所需的状态、切换和触发。通道的状态切换在触发切换后的下一个主函数中处理，且每当模式切换完成后通过API将状态通知到上层节点(NmIf)。

From the perspective of a single node in the network management cluster, the AUTOSAR UdpNm state machine contains the states, switches, and triggers required by the algorithm. Channel state switches are processed in the next main function after a switch is triggered, and whenever a mode switch is completed, the state is notified to the upper layer module (NmIf) via an API.

AUTOSAR UdpNm状态机包含三种操作模式(Mode)：

The AUTOSAR UdpNm state machine consists of three operating modes:

- Network Mode(网络模式)
- Prepare Bus-Sleep Mode(总线预睡眠模式)
- Bus-Sleep Mode(总线睡眠模式)


.. figure:: ../../../_static/参考手册/UdpNm/UdpNmStateMachine.png
   :alt: UdpNmStackMachine
   :align: center

   UdpNm Stack Machine

网络模式 Network Mode
****************************************************************************************************************

网络模式包含以下三个子状态(State)：

The Network Mode contains the following three sub-states:

- Repeat Message State(重复报文状态)
- Normal Operation State(正常运行状态)
- Ready Sleep State(准备睡眠状态)

重复报文状态 Repeat Message State
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

当节点配置为Passive Mode的节点，意味着该节点只能接受报文而不能传输任何报文，关于Passive Mode具体的将在下面章节中进行说明。

When a node is configured in Passive Mode, it means that the node can only receive messages and cannot transmit any messages. Passive Mode will be explained in more detail in a later section.

对于非Passive Mode的节点，Repeat Message State可确保从Bus-Sleep或Prepare Bus-Sleep到Network Mode的任何过渡对于网络上的其他节点都是可见的。此外，它确保所有节点在UdpNmRepeatMessageTime(配置参数)内保持活动状态。当UdpNmRepeatMessageTime配置为0，表示未配置Repeat Message State。这意味着Repeat Message State是瞬态的，在进入后立即离开，因此无法保证启动稳定性，并且无法执行节点检测过程。当UdpNmRepeatMessageTime超时后，节点将离开Repeat Message State而切至其他状态。若当前网络状态为请求，切换到Normal Operation State，若当前网络状态为释放，切换到Ready Sleep State。

For nodes not in Passive Mode, the Repeat Message State ensures that any transition from Bus-Sleep or Prepare Bus-Sleep to Network Mode is visible to other nodes on the network. Furthermore, it ensures that all nodes remain active within the UdpNmRepeatMessageTime (a configuration parameter). If UdpNmRepeatMessageTime is configured to 0, it indicates that the Repeat Message State is not configured. This means that the Repeat Message State is transient and is exited immediately upon entry. Consequently, startup stability cannot be guaranteed, and the node detection procedure cannot be performed. When UdpNmRepeatMessageTime expires, the node will leave the Repeat Message State and transition to another state. If the current network state is "requested", it switches to the Normal Operation State. If the current network state is "released", it switches to the Ready Sleep State.

当非Passive Mode的节点从Bus-Sleep Mode, Prepare-Bus-Sleep Mode，Normal Operation State或Ready Sleep State进入Repeat Message State时，传输功能应该被重启，为了防止总线数据爆发，降低负载，每次进入Repeat Message State时，都要延迟UdpNmMsgCycleOffset(配置参数)段时间后，再开始传输数据，若配置UdpNmImmediateNmTransmissions并且网络被请求则不需要延迟UdpNmMsgCycleOffset时间。

When a non-Passive Mode node enters the Repeat Message State from Bus-Sleep Mode, Prepare-Bus-Sleep Mode, Normal Operation State, or Ready Sleep State, the transmission function shall be restarted. To prevent a burst of data on the bus and to reduce the load, a delay of UdpNmMsgCycleOffset (a configuration parameter) is introduced each time the Repeat Message State is entered before data transmission begins. However, if UdpNmImmediateNmTransmissions is configured and the network is requested, the UdpNmMsgCycleOffset delay is not necessary.

正常运行状态 Normal Operation State
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Normal Operation State可确保只要需要网络功能，任何节点都可以使NM集群保持唤醒状态。当处于Normal Operation State，节点按照UdpNmMsgCycleTime周期发送报文，当网络释放后，UdpNm进入Ready Sleep state。

The Normal Operation State ensures that any node can keep the NM cluster awake as long as network functionality is required. While in the Normal Operation State, the node sends messages periodically according to UdpNmMsgCycleTime. When the network is released, UdpNm enters the Ready Sleep state.

准备睡眠状态 Ready Sleep State
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Ready Sleep State可确保NM群集中的任何节点都在等待过渡到Prepare Bus-Sleep Mode。

The Ready Sleep State ensures that any node in the NM cluster is waiting to transition to the Prepare Bus-Sleep Mode. 

当进入Ready Sleep State，本节点就不再传输数据。当节点接收到其他节点传输的报文时，会将NM-Timeout定时器重置，当NM-Timeout定时器超时且处于Ready Sleep State时，网络管理进入Prepare Bus-Sleep Mode。其中NM-Timeout定时器的时间是由UdpNmTimeoutTime(配置参数)决定的。

Upon entering the Ready Sleep State, the local node stops transmitting data. When the node receives a message transmitted by another node, it resets the NM-Timeout timer. When the NM-Timeout timer expires and the node is in the Ready Sleep State, the network management enters the Prepare Bus-Sleep Mode. The duration of the NM-Timeout timer is determined by UdpNmTimeoutTime (a configuration parameter).

总线预睡眠模式 Prepare Bus-Sleep Mode
******************************************************************************************************************************

Prepare Bus Sleep state目的是确保所有节点都有时间在进入总线休眠状态之前停止其网络活动，使总线活动平静下来，最后在“准备总线睡眠模式”下总线上没有任何活动。

The purpose of the Prepare Bus Sleep state is to ensure that all nodes have time to stop their network activities before entering the bus-sleep state, allowing bus activity to quiet down. Ultimately, there shall be no activity on the bus in the "Prepare Bus-Sleep Mode".

当本节点进入Prepare Bus-Sleep Mode，UdpNmWaitBusSleepTime(配置参数)定时器被启动，当UdpNmWaitBusSleepTime定时器超时，当前状态将由Prepare Bus-Sleep Mode切换至Bus-Sleep Mode。

When the local node enters the Prepare Bus-Sleep Mode, the UdpNmWaitBusSleepTime (a configuration parameter) timer is started. When the UdpNmWaitBusSleepTime timer expires, the current state switches from Prepare Bus-Sleep Mode to Bus-Sleep Mode.

如果在Prepare Bus-Sleep Mode接收到其他节点传输的网络管理报文时，当前UdpNm状态将由Prepare Bus-Sleep Mode切换至Network Mode， 默认情况下，将进入Repeat Message State。

If a network management message from another node is received in the Prepare Bus-Sleep Mode, the current UdpNm state will switch from Prepare Bus-Sleep Mode to Network Mode, and by default, will enter the Repeat Message State.

如果在Prepare Bus-Sleep Mode接收到网络请求时，当前状态将由Prepare Bus-Sleep Mode切换至Network Mode， 默认情况下，将进入Repeat Message State。如果UdpNmImmediateRestartEnabled(配置参数)被设置为TRUE，那么在这种情况下会立刻触发一次传输，这样做的理由是：集群中的其他节点仍处于Prepare Bus-Sleep Mode，在这种特殊情况下，应避免过渡到Bus-Sleep Mode，并应尽快恢复总线通信。由于UdpNm中网络管理PDU的传输偏移导致，处于Repeat Message State的第一个网络管理PDU的传输可能会大大延迟。为了避免延迟重新启动网络可以立即请求发送网络管理PDU。

If a network request is received in the Prepare Bus-Sleep Mode, the current state will switch from Prepare Bus-Sleep Mode to Network Mode, and by default, will enter the Repeat Message State. If UdpNmImmediateRestartEnabled (a configuration parameter) is set to TRUE, a transmission will be triggered immediately in this case. The rationale for this is that other nodes in the cluster are still in the Prepare Bus-Sleep Mode, and in this specific situation, the transition to Bus-Sleep Mode shall be avoided, and bus communication shall be restored as quickly as possible. Due to the transmission offset of the network management PDU in UdpNm, the transmission of the first network management PDU in the Repeat Message State can be significantly delayed.  To avoid a delayed network restart, a request to send the network management PDU can be made immediately.

总线睡眠模式 Bus-Sleep Mode
******************************************************************************************************************************

Bus-Sleep state的目的是在不交换任何消息时降低节点的功耗。将通信控制器切换到睡眠模式，激活相应的唤醒机制，最后将功耗降低到总线睡眠模式下的适当水平。

The purpose of the Bus-Sleep state is to reduce the power consumption of the node when no messages are being exchanged. This is achieved by switching the communication controller to a sleep mode, activating the appropriate wake-up mechanisms, and finally reducing power consumption to a level suitable for the bus-sleep mode.

当UdpNm处于Bus-Sleep Mode接收到网络管理报文时，此时UdpNm不会切换至Network Mode，而是通知Nm模块，由上层模块做决策。

When UdpNm is in Bus-Sleep Mode and receives a network management message, it does not switch to Network Mode. Instead, it notifies the Nm module, and the upper-layer module makes the decision.

当UdpNm处于Bus-Sleep Mode接收到被动请求或网络请求时，当前状态将由Bus-Sleep Mode切换至Network Mode， 默认情况下，将进入Repeat Message State。

When UdpNm is in Bus-Sleep Mode and receives a passive request or a network request, the current state switches from Bus-Sleep Mode to Network Mode, and by default, will enter the Repeat Message State.

AUTOSAR NM 报文格式 AUTOSAR NM Message Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

AUTOSAR NM 报文有特定的格式要求，NM报文总长度视总线特性而定，受总线MTU限制。报文数据段格式如图：

AUTOSAR NM messages have a specific format requirement. The total length of an NM message depends on the bus characteristics and is limited by the bus MTU. The format of the message data segment is as follows:

.. figure:: ../../../_static/参考手册/Nm/NM_message_layout_example.png
   :alt: Nm报文格式图(Nm Message Format Diagram)
   :align: center

   NM message layout example

1.Control Bit Vector(CBV)：长度为一字节的可选字段，根据配置可以处于NM报文第一、二字节或者不使用。FlexRay总线仅可处于第一字节或不使用。该字节信息如下图

1.Control Bit Vector (CBV): An optional one-byte field that, depending on the configuration, can be located in the first or second byte of the NM message, or not used at all. For the FlexRay bus, it can only be in the first byte or not used. This byte contains information as shown in the figure below.

.. figure:: ../../../_static/参考手册/Nm/CBV_layout.png
   :alt: CBV排版图(CBV Layout Diagram)
   :align: center

   CBV layout

2.Source Node ID (SNI)：长度为一字节的可选字段，根据配置可以处于NM报文第一、二字节或者不使用。FlexRay总线仅可处于第二字节或不使用。该字节数据根据通道配置决定。

2.Source Node ID (SNI): An optional one-byte field that, depending on the configuration, can be located in the first or second byte of the NM message, or not used at all. For the FlexRay bus, it can only be in the second byte or not used. The data in this byte is determined by the channel configuration.

3.User Data of n Bytes：若干字节的可选字段，CBV和SNI之外的字节都为User Data部分。该字段包含两部分，即User data和PNC bit Vector，这两部分均为根据配置决定是否支持，若同时支持则严格要求ser data和PNC bit Vector各自的字节必须连续

3.User Data of n Bytes: An optional field of several bytes. Any bytes other than the CBV and SNI are part of the User Data. This field consists of two parts: User data and the PNC bit Vector. Support for both parts is determined by the configuration. If both are supported, it is strictly required that the bytes for the user data and the PNC bit Vector are contiguous.

通信调度功能 Communication Scheduling Function
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

UdpNm提供周期性网络管理报文发送功能：该功能根据配置项UdpPassiveModeEnabled决定是否启用，当UdpPassiveModeEnabled为TRUE意为启动Udp模块启动被动模式，仅接收报文并不主动参加网络管理；该功能也可动态的被诊断通信控制服务启停。

UdpNm provides a function for the periodic transmission of network management messages. This function is enabled or disabled based on the UdpPassiveModeEnabled configuration item. When UdpPassiveModeEnabled is TRUE, it means that the Udp module is in passive mode, only receiving messages but not actively participating in network management. This function can also be dynamically started and stopped by diagnostic communication control services.

UdpNm提供配置项UdpMsgCycleTime作为常规的报文周期，提供UdpMsgCycleOffset、UdpImmediateNmTransmissions、UdpBusLoadReductionEnabled作为网络管理报文发送方向上特殊场景的附加属性。

UdpNm provides UdpMsgCycleTime as the regular message cycle, and UdpMsgCycleOffset, UdpImmediateNmTransmissions, and UdpBusLoadReductionEnabled as additional attributes for special scenarios in network management message transmission.

如果一个NM PDU被成功接收，下层(例如.SoAd )通过函数调用UdpNm_SoAdIfRxIndication通知Udp。Udp根据PduId匹配相应的通道配置，如是否支持CBV，若支持则根据CBV字节位置逐bit解析、若使能PN则处理PNC Bit Vector字段、重置NM-Timeout计时器等

If an NM PDU is successfully received, the lower layer (e.g.,  SoAd) notifies Udp via the function call UdpNm_SoAdIfRxIndication. Udp then matches the PduId to the corresponding channel configuration to determine, for example, whether CBV is supported. If supported, it parses the CBV byte bit by bit. If PN is enabled, it processes the PNC Bit Vector field and resets the NM-Timeout timer, etc.

快速发送 Immediate Transmission
******************************************************************************************************************************

快速发送机制根据配置参数UdpNmImmediateNmTransmissions决定。该改参数为0时意为不启动；当该参数配置大于0时意为快速发送的报文次数，需要再配置UdpNmImmediateNmCycleTime作为快速发送时报文发送周期。

The immediate transmission mechanism is determined by the UdpNmImmediateNmTransmissions configuration parameter. A value of 0 for this parameter means that the mechanism is not activated. If the parameter is configured to be greater than 0, it indicates the number of messages to be sent immediately. In this case, UdpNmImmediateNmCycleTime must also be configured as the message transmission cycle for immediate transmission.

快速发送机制仅作用于Repeat Message State阶段，当通道被主动请求第一次进入网络模式时，或UdpNmPnHandleMultipleNetworkRequests为TRUE且有网络请求时，进入Repeat Message State触发快速发送UdpNmImmediateNmTransmissions次网络管理报文。当快速发送次数结束时，恢复常规的发送周期。

The immediate transmission mechanism is only active during the Repeat Message State. When a channel is actively requested to enter the Network Mode for the first time, or when UdpNmPnHandleMultipleNetworkRequests is TRUE and there is a network request, the node enters the Repeat Message State and triggers the immediate transmission of UdpNmImmediateNmTransmissions network management messages. After the immediate transmissions are complete, the regular transmission cycle is resumed.

报文失败重发 Message Retransmission on Failure
******************************************************************************************************************************

报文发送失败为UdpNm的可选机制，因为UdpNm通道状态切换为异步处理，且以太网需要链路层连接，因此可能造成网络管理报文发送时，通道状态未切换导致发送被拒绝。

Message retransmission on failure is an optional mechanism in UdpNm. Since UdpNm channel state switches are handled asynchronously and Ethernet requires a link-layer connection, it is possible that when a network management message is to be sent, the channel state has not yet switched, leading to the transmission being rejected.

失败重发存在两种触发场景：

There are two scenarios that can trigger a retransmission:

1.UdpNmImmediateNmTransmissions大于0，确保快速发送次数均能成功发送

1.When UdpNmImmediateNmTransmissions is greater than 0, ensure that all immediate transmissions are successful. 

快速发送阶段，每当SoAd_IfTransmit返回E_NOT_OK时，则在后续每次主函数中调用一次SoAd_IfTransmit直到返回E_OK并递减快速发送次数，直到完成全部次数快速发送。最坏情况若存在某次报文始终无法成功发送，则在离开Repeat Message State关闭快速发送时一并停掉重发功能。

During the immediate transmission phase, whenever SoAd_IfTransmit returns E_NOT_OK, SoAd_IfTransmit is called once in each subsequent main function until it returns E_OK, at which point the count of immediate transmissions is decremented until all have been sent. In the worst-case scenario, if a message can never be sent successfully, the retransmission function is stopped when the immediate transmission phase is exited upon leaving the Repeat Message State.

2.UdpNmRetryFirstMessageRequest配置为TRUE，确保进入网络模式的首帧报文一定成功发送

2.When UdpNmRetryFirstMessageRequest is configured to TRUE, ensure that the first message upon entering the Network Mode is successfully sent. 

当通道状态第一次切换到网络模式时，根据配置决定是否确保首帧发送成功。若调用SoAd_IfTransmit返回E_NOT_OK，则在后续每次主函数中调用一次SoAd_IfTransmit直到返回E_OK。最坏情况若SoAd_IfTransmit始终返回E_NOT_OK，则若通道状态进入Normal Opeartion State时仍可在后续主函数中触发发送，若进入Ready Sleep State停止网络管理报文发送功能时一并停掉重发功能。

When the channel state first switches to the Network Mode, the configuration determines whether to ensure the successful transmission of the first frame. If SoAd_IfTransmit returns E_NOT_OK, SoAd_IfTransmit is called once in each subsequent main function until it returns E_OK. In the worst-case scenario, if SoAd_IfTransmit consistently returns E_NOT_OK, the transmission can still be triggered in a subsequent main function if the channel state enters the Normal Operation State. If it enters the Ready Sleep State, the network management message transmission function is stopped, and the retransmission function is also stopped.


UdpNm附加功能 UdpNm Additional Functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

检测远程睡眠指示 Remote Sleep Indication Detection
******************************************************************************************************************************************************************

远程睡眠指示应用于一种情况，当处于Normal Operation State的节点发现集群中的所有其他节点都准备睡眠，但处于Normal Operation State状态的节点仍将保持总线苏醒。为了避免这种情况，可以使能远程睡眠指示功能。

Remote sleep indication is used in a situation where a node in the Normal Operation State detects that all other nodes in the cluster are ready to sleep, but the node in the Normal Operation State would otherwise keep the bus awake. To avoid this, the remote sleep indication function can be enabled.

如果当前UdpNm状态为Normal Operation State，并且在UdpNmRemoteSleepIndTime(配置参数)定时器内未收到其他节点发送的网络管理报文，则通知上层Nm模块集群内的其他节点均已准备睡眠。

If the current UdpNm state is Normal Operation State and no network management messages have been received from other nodes within the UdpNmRemoteSleepIndTime (a configuration parameter) timer, the upper-layer Nm module is notified that all other nodes in the cluster are ready to sleep.

如果UdpNm已通知上层Nm模块，而在Normal Operation State或Ready Sleep State下又收到了网络管理报文，或者UdpNm从Normal Operation State切换至Repeat Message State，UdpNm需要通知上层Nm模块集群中的某些节点不再准备睡眠。

If UdpNm has already notified the upper-layer Nm module, and a network management message is received in the Normal Operation State or Ready Sleep State, or if UdpNm switches from the Normal Operation State to the Repeat Message State, UdpNm needs to notify the upper-layer Nm module that some nodes in the cluster are no longer ready to sleep.

用户数据 User Data
******************************************************************************************************************************

使用UdpNmUserDataEnabled开关(配置参数)对NM用户数据的支持进行静态配置。

Support for NM user data is statically configured using the UdpNmUserDataEnabled switch (a configuration parameter). 

当用户数据功能使能，可以调用UdpNm_SetUserData，该函数可以设置总线上接下来发送的NM数据包的NM用户数据。也可以调用UdpNm_GetUserDat，该函数可以提供包含在最近接收到的NM PDU的有效载荷中的NM用户数据。

When the user data function is enabled, UdpNm_SetUserData can be called to set the NM user data for the next NM packet to be sent on the bus. UdpNm_GetUserData can also be called to retrieve the NM user data contained in the payload of the most recently received NM PDU. 

如果UdpNmComUserDataSupport(配置参数)配置为使能，UdpNm将在每次请求发送相应的NM消息之前从引用的NM I-PDU收集NM用户数据，并将用户数据与其他NM字节合并。此时就不能再通过UdpNm_SetUserData函数设置用户数据。

If UdpNmComUserDataSupport (a configuration parameter) is enabled, UdpNm will collect the NM user data from the referenced NM I-PDU before each request to send the corresponding NM message and will merge the user data with the other NM bytes. In this case, the UdpNm_SetUserData function can no longer be used to set the user data.

被动模式 Passive Mode
**************************************************************************************************************************

在被动模式下，节点仅接收NM消息，但不发送任何NM消息。被动模式应使用UdpNmPassiveModeEnabled开关(配置参数)进行静态配置。

In passive mode, the node only receives NM messages but does not send any NM messages. Passive mode shall be statically configured using the UdpNmPassiveModeEnabled switch (a configuration parameter).

NM-Pdu接收 NM-Pdu Reception
**************************************************************************************************************************

若UdpNmPduRxIndicationEnabled(配置参数)使能，在成功接收NM PDU时，UdpNm应通过调用Nm_PduRxIndication通知上层

If UdpNmPduRxIndicationEnabled (a configuration parameter) is enabled, UdpNm shall notify the upper layer by calling Nm_PduRxIndication upon the successful reception of an NM PDU.

状态改变通知 State Change Notification
************************************************************************************************************************************************

如果UdpNmStateChangeIndEnabled(配置参数)使能，则UdpNm需要将UdpNm状态的所有更改通知上层Nm。

If UdpNmStateChangeIndEnabled (a configuration parameter) is enabled, UdpNm needs to notify the upper layer Nm of all changes to the UdpNm state.

通信控制 Communication Control
************************************************************************************************************************************************

使用UdpNmComControlEnabled开关(配置参数)，可以静态配置通信控制。当UdpNm_DisableCommunication函数被调用，UdpNm模块NM报文的传输能力将被停止，直到调用UdpNm_EnableCommunication，UdpNm的nm报文传输能力被恢复。

Communication control can be statically configured using the UdpNmComControlEnabled switch (a configuration parameter). When the UdpNm_DisableCommunication function is called, the NM message transmission capability of the UdpNm module is stopped until UdpNm_EnableCommunication is called, at which point the NM message transmission capability of UdpNm is restored.

.. hint::

   网络释放时，UdpNm_DisableCommunication和UdpNm_EnableCommunication成对使用。

   When the network is released, UdpNm_DisableCommunication and UdpNm_EnableCommunication are used in pairs. 
   
   当UdpNm_DisableCommunication函数被调用，UdpNm的NM-Timeout定时器将被停止，调用函数UdpNm_EnableCommunication，NM-Timeout定时器将被恢复。因此在UdpNm_EnableCommunication尚未调用前，若释放网络，通道状态将停留在ReadySleep状态，休眠将被阻塞，需要在UdpNm_EnableCommunication调用后才可进入Prepare-Bus-Sleep模式。

   When the UdpNm_DisableCommunication function is called, the NM-Timeout timer of UdpNm is stopped. When the UdpNm_EnableCommunication function is called, the NM-Timeout timer is restored. Therefore, if the network is released before U-dpNm_EnableCommunication is called, the channel state will remain in the ReadySleep state, and sleep will be blocked. The node can only enter the Prepare-Bus-Sleep mode after UdpNm_EnableCommunication is called.

协调同步 Coordination Synchronization
************************************************************************************************************************************************

当有多个协调器连接到同一条总线时，在CBV中，NmCoordinatorSleepReady位用于指示主协调器请求启动关闭。

When multiple coordinators are connected to the same bus, the NmCoordinatorSleepReady bit in the CBV is used to indicate that the master coordinator is requesting to initiate a shutdown.

当UdpNm处于网络模式，接收网络管理报文的CBV中NmCoordinatorSleepReady=1，则UdpNm通知上层协调睡眠功能被请求。

When UdpNm is in network mode and receives a network management message with NmCoordinatorSleepReady=1 in the CBV, UdpNm notifies the upper layer that the coordinated sleep function has been requested.

当UdpNm已通知上层协调睡眠功能被请求，接收网络管理报文的CBV中NmCoordinatorSleepReady=0，则UdpNm通知上层协调睡眠功能请求被取消。

When UdpNm has already notified the upper layer that the coordinated sleep function has been requested and then receives a network management message with NmCoordinatorSleepReady=0 in the CBV, UdpNm notifies the upper layer that the coordinated sleep function request has been canceled.

车辆唤醒 Car Wake-up
******************************************************************************************************************************

当UdpNmCarWakeUpRxEnabled(配置参数)使能时，车辆唤醒功能被启用，目前暂时没有使用场景。如果任何接收到的NM-PDU中的Car Wakeup位为1，都会通知上层Nm。

When UdpNmCarWakeUpRxEnabled (a configuration parameter) is enabled, the vehicle wake-up function is enabled. There are currently no use cases for this. If the Car Wakeup bit in any received NM-PDU is 1, the upper layer Nm will be notified.

当UdpNmCarWakeUpRxEnabled(配置参数)使能，UdpNmCarWakeUpFilterEnabled(配置参数)也使能时，只有收到NodeId等于UdpNmCarWakeUpFilterNodeId的报文时，才会通知上层。

When UdpNmCarWakeUpRxEnabled (a configuration parameter) is enabled and UdpNmCarWakeUpFilterEnabled (a configuration parameter) is also enabled, the upper layer will be notified only when a message with a NodeId equal to UdpNmCarWakeUpFilterNodeId is received.

PNC
******************

Autosar4.x版本开始支持PN功能，Pn功能的目的是基于功能划分网络，形成局域网；这种功能的划分由整车设计完成，对于各节点只需要关心自身存在的网段。只有在UdpGlobalPnSupport(配置参数)和各通道下的UdpPnEnabled(配置参数)使能的情况下，Pn功能才能正常工作。

Starting with Autosar4.x, the PN function is supported. The purpose of the PN function is to partition the network based on the function, forming local area networks. This function partitioning is handled by the overall vehicle design; individual nodes only need to be concerned with their own network segments. The PN function can work correctly only when UdpGlobalPnSupport (a configuration parameter) and UdpPnEnabled (a configuration parameter) for each channel are enabled.

如果UdpPnEnabled(配置参数)为FALSE，则Udp将执行常规的Rx处理，并且应禁用Pn功能。如果UdpPnEnabled为TRUE，接收到的NM-PDU CBV中的PNI位为0，则Udp模块应执行常规的Rx处理，从而省去了Pn功能的扩展。如果UdpPnEnabled为TRUE并且接收到的NM-PDU CBV中的PNI位为1，则Udp模块处理NM-PDU的Pn信息。

If UdpPnEnabled (a configuration parameter) is FALSE, Udp will perform regular Rx processing, and the PN function shall be disabled. If UdpPnEnabled is TRUE and the PNI bit in the CBV of a received NM-PDU is 0, the Udp module shall perform regular Rx processing, thus bypassing the extensions of the PN function. If UdpPnEnabled is TRUE and the PNI bit in the CBV of a received NM-PDU is 1, the Udp module processes the PN information of the NM-PDU.

如果UdpPnEnabled为TRUE，则必须使用CBV，且发送报文时应将CBV中发送的PNI位的值设置为1；如果UdpPnEnabled为FALSE，若使用CBV，则发送报文时应将CBV中的PNI位的值始终设置为0。

If UdpPnEnabled is TRUE, the CBV must be used, and the value of the PNI bit sent in the CBV shall be set to 1 when transmitting a message. If UdpPnEnabled is FALSE and the CBV is used, the value of the PNI bit in the CBV shall always be set to 0 when transmitting a message.

PNC是Partial Network Cluster的缩写，它是指为了在车辆网络中支持一个或多个车辆功能而由多个ECU构成的集群。PNC的编号我们称为PNC ID，范围8~63，整车网络统一编号，关于PNC id与UdpPdu映射关系说明：PNC ID对应UdpPdu中的一个bit，例如PNC ID=8，对应UdpPduByte1的bit0；PNC ID=63，对应Byte7的bit7；PNC ID对应的bit数值为1，则表示当前PN网络被请求，为0则表示网络释放。

PNC is an abbreviation for Partial Network Cluster, which refers to a cluster of multiple ECUs that support one or more vehicle functions in a vehicle network. The number of a PNC is called the PNC ID, which ranges from 8 to 63 and is uniformly numbered throughout the vehicle network. The mapping relationship between the PNC ID and the UdpPdu is as follows: The PNC ID corresponds to one bit in the UdpPdu. For example, PNC ID=8 corresponds to bit0 of UdpPduByte1; PNC ID=63 corresponds to bit7 of Byte7. If the bit corresponding to the PNC ID has a value of 1, it indicates that the current PN network is requested; a value of 0 indicates that the network is released.

Pn信息的位置位于网络管理报文的用户数据部分中，具体的位置根据Nm模块配置决定：NmPncBitVectorOffset和NmPncBitVectorLength。

The location of the PN information is in the user data portion of the network management message. The specific location is determined by the Nm module configuration: NmPncBitVectorOffset and NmPncBitVectorLength. 

例如当NmPncBitVectorOffset = 3，NmPncBitVectorLength = 2，代表NM报文只有字节3和字节4包含PN请求信息。

For example, when NmPncBitVectorOffset = 3 and NmPncBitVectorLength = 2, it means that only byte 3 and byte 4 of the NM message contain PN request information.

接收 Reception
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

当通道使能UdpNmPnEnabled为TRUE，且CBV中PNI为1，则需要对PNC Bit Vector字段进行过滤。

When UdpNmPnEnabled for a channel is TRUE and the PNI in the CBV is 1, the PNC Bit Vector field needs to be filtered. 

过滤操作由Nm模块完成，通过提供PNC bit vector字段起始地址调用Nm_PncBitVectorRxIndication接口，根据返回值RelevantPncRequestDetected判断接收到的报文是否与该通道相关，若相关则属于过滤通过，可以对报文进行后续处理。若过滤不通过则丢弃本次接收到的报文，不做任何处理。

The filtering operation is performed by the Nm module. The Nm_PncBitVectorRxIndication interface is called with the starting address of the PNC bit vector field. Based on the return value RelevantPncRequestDetected, it is determined whether the received message is relevant to the channel. If it is relevant, it passes the filter and can be further processed. If it does not pass the filter, the received message is discarded without any processing.

当通道使能UdpNmPnEnabled为TRUE，且CBV中PNI为0，视为过滤失败则丢弃本次接收到的报文，不做任何处理。

When UdpNmPnEnabled for a channel is TRUE and the PNI in the CBV is 0, it is considered a filter failure, and the received message is discarded without any processing.

当过滤失败时，若配置项UdpNmAllNmMessagesKeepAwake为TRUE则也可进行后续处理而不丢弃报文。

In the case of a filter failure, if the UdpNmAllNmMessagesKeepAwake configuration item is TRUE, the message can still be further processed instead of being discarded.

当通道使能UdpNmPnEnabled为FALSE，则不进行过滤，对报文进行后续处理而不丢弃报文。

When UdpNmPnEnabled for a channel is FALSE, no filtering is performed, and the message is further processed without being discarded.

发送 Transmission
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

如果网络被请求并且UdpNmPnHandleMultipleNetworkRequests(配置参数)设置为TRUE，无论UdpNm处于Ready Sleep State，Normal Operation State或Repeat Message State，UdpNm应更改为或重新启动为Repeat Message State。并且，UdpNm会传输UdpNmImmediateNmTransmissions(配置参数)数量的报文，其中第一条报文立即传输，其他报文按UdpNmImmediateNmCycleTime传输(配置参数)。

If the network is requested and UdpNmPnHandleMultipleNetworkRequests (a configuration parameter) is set to TRUE, regardless of whether UdpNm is in the Ready Sleep State, Normal Operation State, or Repeat Message State, UdpNm shall change to or restart in the Repeat Message State. Furthermore, UdpNm will transmit a number of messages equal to UdpNmImmediateNmTransmissions (a configuration parameter), with the first message being transmitted immediately and the others being transmitted according to UdpNmImmediateNmCycleTime (a configuration parameter).

当通道使能UdpNmPnEnabled为TRUE，每次发送网络管理报文时，提供PNC bit vector字段起始地址调用Nm_PncBitVectorTxIndication接口以填充该字段。

When UdpNmPnEnabled for a channel is TRUE, each time a network management message is sent, the Nm_PncBitVectorTxIndication interface is called with the starting address of the PNC bit vector field to fill that field.

.. only:: doc_pbs

多变体支持 Multi-variant Support
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

UdpNm 支持在不同变体中：

UdpNm supports in different variants:

1.支持报文发送前的不同的偏移周期

1.Supports different offset periods before message transmission

2.支持配置不同的节点ID

2.Supports the configuration of different node IDs

3.支持配置是否启用PNC功能

3.Supports the configuration of whether to enable the PNC function

4.支持不同的NM-Pdu收发路径

4.Supports different NM-PDU reception and transmission paths

偏差 Deviation
------------------------------------------------
.. 有序列表示例

1.不支持 Dynamic PNC-to-channel-mapping。

1.Dynamic PNC-to-channel-mapping is not supported.

2.不支持 Pnc shutdown

2.PNC shutdown is not supported.

扩展 Extension
----------------------------------------------------

1.UdpNmRetryFirstMessageRequest配置参数影响范围扩大

1.The scope of the UdpNmRetryFirstMessageRequest configuration parameter has been expanded. 

   该配置不仅限于BusSleep Mode主动唤醒时确保首帧发送成功，作用范围增大到任意方式导致进入网络模式都将确保首帧成功发送

   This configuration is no longer limited to ensuring the successful transmission of the first frame upon an active wake-up from BusSleep Mode. Its scope has been extended to ensure the successful transmission of the first frame regardless of how the node enters network mode.