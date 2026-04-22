CanNm
#################################

:strong:`缩写词注解 (Abbreviation Notes):`

.. list-table::
   :widths: 34 33 33
   :header-rows: 1

   * - 缩写词 (Abbreviation)
     - 解释/描述 (Explanation/Description)
     - 中文解释 (Chinese explanation)
   * - API
     - Application ProgrammingInterface
     - 应用程序接口 (API)
   * - BSWM
     - Basic Software Manager
     - 基础软件模式管理 (Basic software model management)
   * - CanIf
     - Can Interface
     - Can接口模块 (Can interface module)
   * - DEM
     - Diagnostic Event Manager
     - 诊断事件管理模块 (Diagnostic event management module)
   * - DET
     - Default Error Tracer
     - 默认错误检测模块 (Default error detection module)
   * - NM
     - Network Management
     - 网络管理 (network management)
   * - PDU
     - Protocol Data Unit
     - 协议数据单元 (protocol data unit)
   * - SDU
     - Service Data Unit
     - 服务数据单元 (service data unit)
   * - PNI
     - Partial NetworkInformation
     - 部分网络信息 (Some network information)
   * - PN
     - Partial Network
     - 部分网络 (Partial network)
   * - PNC
     - Partial Network Cluster
     - 部分网络集群 (Partial network cluster)
   * - ERA
     - External Request Array
     - 外部请求集合 (External request collection)
   * - EIRA
     - External and InternalRequest Array
     - 外部和内部请求集合 (Collection of external and internal requests)
   * - CanNm
     - Can Network Management
     - Can网络管理 (Can network management)
   * - CBV
     - Control Bit Vector
     - 控制位向量 (control bit vector)
   * - CWU
     - Car Wakeup
     - 车辆唤醒 (vehicle wake up)
         

简介 (Introduction)
=================================


CanNm模块的核心功能是协调网络正常运行和总线睡眠模式之间的转换，除此之外，还提供了可选功能，例如检测当前节点或检测其他所有节点是否准备休眠等。

The core function of the CanNm module is to coordinate the transition between normal network operation and bus sleep mode. In addition, it also provides optional functions, such as detecting the current node or detecting whether all other nodes are ready to sleep.

CanNm提供网络管理接口（Nm）和CanIf模块之间的适配。CanNm通过调用CanIf模块的发送API来传输数据，并提供接收API给CanIf用于接收下层网络管理报文。Nm模块调用CanNm模块API来更改CanNm的当前状态机状态，CanNm的状态机模式切换需要通知给Nm模块。

CanNm provides adaptation between the network management interface (Nm) and the CanIf module.CanNm transmits data by calling the sending API of the CanIf module, and provides the receiving API to CanIf for receiving lower-layer network management messages.The Nm module calls the CanNm module API to change the current state machine state of CanNm. The state machine mode switching of CanNm needs to be notified to the Nm module.

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/CanNm/image1.png
   :alt: CanNm在AUTOSAR中的位置(The position of CanNm in AUTOSAR)
   :name: CanNm在AUTOSAR中的位置(The position of CanNm in AUTOSAR)
   :align: center

CanNm模块的主要功能为：

The main functions of the CanNm module are:

1、协调网络正常运行和总线睡眠模式之间的转换

Coordinate the transition between normal network operation and bus sleep mode

2、可选功能

Optional functions

(1)检测远程睡眠指令功能

Detect remote sleep command function

(2)用户数据功能

User data function

(3)被动模式功能

Passive mode function

(4)NM PDU Rx指示功能

NM PDU Rx indication function

(5)状态变化通知功能

Status change notification function

(6)通讯控制功能

Communication control function

(7)NM协调器同步支持功能

NM coordinator synchronization support function

(8)减负载功能

Load reduction function

3、局部联网功能

Local networking function

4、车辆唤醒功能

Vehicle wake-up function

参考资料 (References)
---------------------------------

[1] AUTOSAR_SWS\_ CANInterface.pdf，R19-11

[2] AUTOSAR_SWS_CANNetworkManagement.pdf，R19-11

[3] AUTOSAR_SWS_PDURouter.pdf，R19-11

[4] AUTOSAR_SWS_NetworkManagementInterface.pdf，R19-11

[5]AUTOSAR_SWS_COMManager.pdf，R19-11

功能描述 (Function description)
===========================================

AUTOSAR CanNm基于分散的直接网络管理策略，这意味着每个网络节点仅根据在通信系统内接收和/或发送报文，执行自给自足的活动。

AUTOSAR CanNm is based on a decentralized direct network management strategy, which means that each network node only performs self-sufficient activities based on receiving and/or sending messages within the communication system.

AUTOSAR CanNm协调算法基于周期性的NM数据包，集群中的所有节点都通过广播传输接收这些数据包。接收到NM数据包表明发送节点要保持NM集群处于唤醒状态。如果任何节点准备好进入总线睡眠模式，它将停止发送NM数据包，但是只要接收到来自其他节点的NM数据包，它就会推迟过渡到总线睡眠模式。如果在专用计时器超时前都未接收到NM数据包，则每个节点都会启动到总线休眠模式的转换。CanNm通过状态机切换和各状态定时器管理来完成协调算法。

The AUTOSAR CanNm coordination algorithm is based on periodic NM packets, which are received by all nodes in the cluster via broadcast transmission.Receiving an NM packet indicates that the sending node wants to keep the NM cluster awake.If any node is ready to enter bus sleep mode, it will stop sending NM packets, but it will postpone transition to bus sleep mode as long as it receives NM packets from other nodes.If no NM packet is received before the dedicated timer expires, each node initiates a transition to bus sleep mode.CanNm completes the coordination algorithm through state machine switching and timer management of each state.

状态机切换 (State machine switching)
-----------------------------------------------

模式介绍 (Mode introduction)
========================================

首先介绍AUTOSAR CanNm协调算法的三种操作模式：

First, we introduce the three operating modes of the AUTOSAR CanNm coordination algorithm:

- Network Mode 网络模式

Network Mode network mode

- Prepare Bus-Sleep Mode准备总线睡眠模式

Prepare Bus-Sleep Mode prepare bus sleep mode

- Bus-Sleep Mode总线睡眠模式

Bus-Sleep Mode bus sleep mode

当本节点的操作模式发生变化的时候，需要通知上层Nm。

When the operating mode of this node changes, the upper layer Nm needs to be notified.

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/CanNm/image2.png
   :alt: CanNm状态机(CanNm state machine)
   :name: CanNm状态机(CanNm state machine)
   :align: center

Network Mode
============================

Network Mode下包括三种内部状态：

Network Mode includes three internal states:

- Repeat Message State重复消息状态

Repeat Message State Repeat message state

- Normal Operation State正常运行状态

Normal Operation StateNormal operating state

- Ready Sleep State就绪睡眠状态

Ready Sleep State ready sleep state

下面对这三种状态分别说明：

These three states are explained below:

1. Repeat Message State

当节点配置为Passive Mode的节点，意味着该节点只能接受报文而不能传输任何报文，关于Passive Mode具体的将在下面章节中进行说明。

When a node is configured as a Passive Mode node, it means that the node can only accept packets but cannot transmit any packets. The details of Passive Mode will be explained in the following chapters.

对于非Passive Mode的节点，Repeat Message State可确保从Bus-Sleep或Prepare Bus-Sleep到Network Mode的任何过渡对于网络上的其他节点都是可见的。此外，它确保所有节点在CanNmRepeatMessageTime（配置参数）内保持活动状态。当CanNmRepeatMessageTime配置为0，表示未配置Repeat Message State。这意味着Repeat Message State是瞬态的，在进入后立即离开，因此无法保证启动稳定性，并且无法执行节点检测过程。当CanNmRepeatMessageTime超时后，节点将离开Repeat Message State而切至其他状态。若当前网络状态为请求，切换到Normal Operation State，若当前网络状态为释放，切换到Ready SleepState。

For nodes that are not in Passive Mode, Repeat Message State ensures that any transition from Bus-Sleep or Prepare Bus-Sleep to Network Mode is visible to other nodes on the network.Additionally, it ensures that all nodes remain active for the duration of CanNmRepeatMessageTime (configuration parameter).When CanNmRepeatMessageTime is configured as 0, it means that Repeat Message State is not configured.This means that the Repeat Message State is transient and leaves immediately after entering, so startup stability cannot be guaranteed and the node detection process cannot be performed.When CanNmRepeatMessageTime times out, the node will leave Repeat Message State and switch to other states.If the current network state is Request, switch to Normal Operation State. If the current network state is Release, switch to Ready SleepState.

当非Passive Mode的节点从Bus-SleepMode, Prepare-Bus-Sleep Mode，Normal Operation State或Ready Sleep State进入Repeat Message State时，传输功能应该被重启，为了防止总线数据爆发，降低负载，每次进入Repeat Message State时，都要延迟CanNmMsgCycleOffset（配置参数）段时间后，再开始传输数据，若配置CanNmImmediateNmTransmissions并且网络被请求则不需要延迟CanNmMsgCycleOffset时间。

When a non-Passive Mode node enters Repeat Message State from Bus-SleepMode, Prepare-Bus-Sleep Mode, Normal Operation State or Ready Sleep State, the transmission function should be restarted. In order to prevent bus data bursts and reduce the load, each time it enters Repeat MessageState, it is necessary to delay the CanNmMsgCycleOffset (configuration parameter) for a period of time before starting to transmit data. If CanNmImmediateNmTransmissions is configured and the network is requested, there is no need to delay the CanNmMsgCycleOffset time.

2. Normal Operation State

Normal Operation State可确保只要需要网络功能，任何节点都可以使NM集群保持唤醒状态。当处于Normal Operation State，节点按照CanNmMsgCycleTime周期发送报文，当网络释放后，CanNm进入ReadySleep state。

Normal Operation State ensures that any node can keep the NM cluster awake as long as network functionality is required.When in the Normal Operation State, the node sends messages according to the CanNmMsgCycleTime cycle. When the network is released, CanNm enters the ReadySleep state.

3. Ready Sleep State

Ready Sleep State可确保NM群集中的任何节点都在等待过渡到Prepare Bus-Sleep Mode。

Ready Sleep State ensures that any node in the NM cluster is waiting to transition to Prepare Bus-Sleep Mode.

当进入Ready Sleep State，本节点就不再发送网络管理报文。当节点接收到其他节点传输的网络管理报文时，会将NM-Timeout定时器重置，当NM-Timeout定时器超时且处于Ready Sleep State时，网络管理进入Prepare Bus-Sleep Mode。其中NM-Timeout定时器的时间是由CanNmTimeoutTime（配置参数）决定的。

When entering the Ready Sleep State, this node will no longer send network management messages.When a node receives a network management message transmitted by another node, it will reset the NM-Timeout timer. When the NM-Timeout timer times out and is in the Ready Sleep State, the network management enters Prepare Bus-Sleep Mode.The time of the NM-Timeout timer is determined by CanNmTimeoutTime (configuration parameter).

Prepare Bus Sleep Mode
======================================

Prepare Bus Sleep state目的是确保所有节点都有时间在进入总线休眠状态之前停止其网络活动，使总线活动平静下来，最后在“准备总线睡眠模式”下总线上没有任何活动。

The purpose of Prepare Bus Sleep state is to ensure that all nodes have time to stop their network activities before entering bus sleep state, allowing bus activity to calm down, and finally there is no activity on the bus in "Prepare Bus Sleep Mode".

当本节点进入Prepare Bus-Sleep Mode，CanNmWaitBusSleepTime（配置参数）定时器被启动，当CanNmWaitBusSleepTime定时器超时，当前状态将由Prepare Bus-Sleep Mode切换至Bus-Sleep Mode。

When this node enters Prepare Bus-Sleep Mode, the CanNmWaitBusSleepTime (configuration parameter) timer is started. When the CanNmWaitBusSleepTime timer times out, the current state will be switched from Prepare Bus-Sleep Mode to Bus-Sleep Mode.

如果在Prepare Bus-Sleep Mode接收到其他节点传输的网络管理报文时，当前CanNm状态将由Prepare Bus-Sleep Mode切换至Network Mode，默认情况下，将进入Repeat Message State。

If network management messages transmitted by other nodes are received in Prepare Bus-Sleep Mode, the current CanNm state will be switched from Prepare Bus-Sleep Mode to Network Mode. By default, it will enter Repeat Message State.

如果在Prepare Bus-Sleep Mode接收到网络请求时，当前状态将由Prepare Bus-Sleep Mode切换至Network Mode，默认情况下，将进入Repeat Message State。如果CanNmImmediateRestartEnabled（配置参数）被设置为TRUE，那么在这种情况下会立刻触发一次传输，这样做的理由是：集群中的其他节点仍处于Prepare Bus-Sleep Mode，在这种特殊情况下，应避免过渡到Bus-Sleep Mode，并应尽快恢复总线通信。由于CanNm中网络管理PDU的传输偏移导致，处于Repeat Message State的第一个网络管理PDU的传输可能会大大延迟。为了避免延迟重新启动网络可以立即请求发送网络管理PDU。

If a network request is received in Prepare Bus-Sleep Mode, the current state will be switched from Prepare Bus-Sleep Mode to Network Mode. By default, it will enter Repeat Message State.If CanNmImmediateRestartEnabled (configuration parameter) is set to TRUE, then in this case a transfer will be triggered immediately. The reason for this is that other nodes in the cluster are still in Prepare Bus-Sleep Mode. In this special case, the transition to Bus-Sleep Mode should be avoided and bus communication should be restored as soon as possible.Due to the transmission offset of the network management PDU in CanNm, the transmission of the first network management PDU in the Repeat Message State may be greatly delayed.To avoid delays in restarting the network a Network Management PDU can be requested immediately.

Bus-Sleep Mode
==============================

Bus-Sleep state的目的是在不交换任何消息时降低节点的功耗。将通信控制器切换到睡眠模式，激活相应的唤醒机制，最后将功耗降低到总线睡眠模式下的适当水平。

The purpose of Bus-Sleep state is to reduce the power consumption of nodes when no messages are exchanged.Switch the communication controller to sleep mode, activate the corresponding wake-up mechanism, and finally reduce the power consumption to the appropriate level in bus sleep mode.

当CanNm处于Bus-Sleep Mode接收到网络管理报文时，此时CanNm不会切换至Network Mode，而是通知Nm模块，由上层模块做决策。

When CanNm is in Bus-Sleep Mode and receives network management messages, CanNm will not switch to Network Mode at this time, but will notify the Nm module and let the upper module make decisions.

当CanNm处于Bus-Sleep Mode接收到被动请求或网络请求时，当前状态将由Bus-Sleep Mode切换至Network Mode，默认情况下，将进入Repeat Message State。

When CanNm is in Bus-Sleep Mode and receives a passive request or a network request, the current state will be switched from Bus-Sleep Mode to Network Mode. By default, it will enter Repeat Message State.

PDU格式 (PDU format)
----------------------------------

网络管理的报文有特定的格式要求，报文数据段格式如图：

Network management messages have specific format requirements. The format of the message data segment is as follows:

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/CanNm/image3.png
   :alt: NM PDU默认格式(NM PDU default format)
   :name: NM PDU默认格式(NM PDU default format)
   :align: center

其中CBV（ControlBitVector）字节对应的bit位标识如下

The bit identifier corresponding to the CBV (ControlBitVector) byte is as follows:

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/CanNm/image4.png
   :alt: CBV格式(CBV format)
   :name: CBV格式(CBV format)
   :align: center

对于CBV中的bit说明如下：

The bit description in CBV is as follows:

Bit 0重复消息请求

Bit 0 Repeat message request

0：未请求进入Repeat Message State

0: No request to enter Repeat Message State

1：请求进入Repeat Message State

1: Request to enter Repeat Message State

Bit 1,2：保留位，当配置项CanNmCoordinatorEnabled使能时，该位等于配置的CanNmCoordinatorId的值

Bit 1,2: Reserved bits. When the configuration item CanNmCoordinatorEnabled is enabled, this bit is equal to the value of the configured CanNmCoordinatorId.

| Bit 3 NM协调器休眠位
| 0：主协调器不要求启动同步休眠
| 1：主协调员请求启动同步休眠

| Bit 3 NM coordinator sleep bit
| 0: The main coordinator does not require synchronous hibernation to be started
| 1: The main coordinator requests to start synchronous hibernation

| Bit 4主动唤醒位
| 0：节点尚未唤醒网络
| 1：节点唤醒了网络

| Bit 4 active wake-up bit
| 0: The node has not yet woken up the network
| 1: The node wakes up the network

Bit 6局部网络信息位（PNI）

Bit 6 Partial Network Information Bit (PNI)

| 0：NM消息不包含局部网络请求信息
| 1：NM消息包含局部网络请求信息,该位由配置决定，运行阶段不改变

| 0: NM message does not contain local network request information
| 1: The NM message contains local network request information. This bit is determined by the configuration and does not change during the running phase.

Bit5 Bit7为保留位

Bit5 Bit7 are reserved bits

NmPdu中的UserData可以通过CanNm的配置引用EcuC中的Pdu。未使用的情况下默认全0xFF，通过Nm的接口去抓取当前接收与发送的UserData。

UserData in NmPdu can reference Pdu in EcuC through the configuration of CanNm.If not used, the default value is 0xFF. Use the Nm interface to capture the currently received and sent UserData.

可选功能 (optional features)
----------------------------------------

CanNm可以通过使能配置参数来使用以下可选功能。

CanNm can use the following optional features by enabling configuration parameters.

检测远程睡眠指令功能 (Detect remote sleep command function)
=================================================================

远程睡眠指示应用于一种情况，当处于NormalOperation State的节点发现集群中的所有其他节点都准备睡眠，但处于Normal Operation State状态的节点仍将保持总线苏醒。为了避免这种情况，可以使能远程睡眠指示功能。

The remote sleep indication should be used in a situation when a node in Normal Operation State finds that all other nodes in the cluster are preparing to sleep, but the node in Normal Operation State will still keep the bus awake.To avoid this situation, the remote sleep indication function can be enabled.

如果当前CanNm状态为Normal Operation State，并且在CanNmRemoteSleepIndTime（配置参数）定时器内未收到其他节点发送的网络管理报文，则通知上层Nm模块集群内的其他节点均已准备睡眠。

If the current CanNm state is Normal Operation State and no network management messages are received from other nodes within the CanNmRemoteSleepIndTime (configuration parameter) timer, the upper Nm module is notified that other nodes in the cluster are ready to sleep.

如果CanNm已通知上层Nm模块，而在Normal Operation State或Ready Sleep State下又收到了网络管理报文，或者CanNm从Normal Operation State切换至Repeat Message State，CanNm需要通知上层Nm模块集群中的某些节点不再准备睡眠。

If CanNm has notified the upper Nm module and receives a network management message in Normal Operation State or Ready Sleep State, or CanNm switches from Normal Operation State to Repeat Message State, CanNm needs to notify the upper Nm module that some nodes in the cluster are no longer ready to sleep.

用户数据功能 (User data function)
===========================================

使用CanNmUserDataEnabled开关（配置参数）对NM用户数据的支持进行静态配置。

Use the CanNmUserDataEnabled switch (configuration parameter) to statically configure NM user data support.

当用户数据功能使能，可以调用CanNm_SetUserData，该函数可以设置总线上接下来发送的NM数据包的NM用户数据。也可以调用CanNm_GetUserData，该函数可以提供包含在最近接收到的NM PDU的有效载荷中的NM用户数据。

When the user data function is enabled, CanNm_SetUserData can be called. This function can set the NM user data of the next NM data packet sent on the bus.CanNm_GetUserData can also be called, which provides the NM user data contained in the payload of the most recently received NM PDU.

如果CanNmComUserDataSupport（配置参数）配置为使能，CanNm将在每次请求发送相应的NM消息之前从引用的NM I-PDU收集NM用户数据，并将用户数据与其他NM字节合并。此时就不能再通过CanNm_SetUserData函数设置用户数据。

If CanNmComUserDataSupport (configuration parameter) is configured to be enabled, CanNm will collect NM user data from the referenced NM I-PDU and merge the user data with other NM bytes before each request to send the corresponding NM message.At this time, user data can no longer be set through the CanNm_SetUserData function.

被动模式功能 (Passive mode functionality)
===================================================

在被动模式下，节点仅接收NM消息，但不发送任何NM消息。被动模式应使用CanNmPassiveModeEnabled开关（配置参数）进行静态配置。

In passive mode, the node only receives NM messages but does not send any NM messages.Passive mode should be statically configured using the CanNmPassiveModeEnabled switch (configuration parameter).

NM PDU Rx指示功能 (NM PDU Rx indication function)
=============================================================

若CanNmPduRxIndicationEnabled（配置参数）使能，在成功接收NM PDU时，CanNm应通过调用Nm_PduRxIndication通知上层。

If CanNmPduRxIndicationEnabled (configuration parameter) is enabled, CanNm should notify the upper layer by calling Nm_PduRxIndication when successfully receiving NM PDU.

状态变化通知功能 (Status change notification function)
==============================================================

如果CanNmStateChangeIndEnabled（配置参数）使能，则CanNm需要将CanNm状态的所有更改通知上层Nm。

If CanNmStateChangeIndEnabled (configuration parameter) is enabled, CanNm needs to notify the upper Nm of all changes in CanNm state.

通讯控制功能 (Communication control function)
=======================================================

使用CanNmComControlEnabled开关（配置参数），可以静态配置通信控制。当CanNm_DisableCommunication函数被调用，CanNm模块NM报文的传输能力将被停止，直到调用CanNm_EnableCommunication，CanNm的nm报文传输能力被恢复。

Communication control can be configured statically using the CanNmComControlEnabled switch (configuration parameter).When the CanNm_DisableCommunication function is called, the CanNm module's NM message transmission capability will be stopped until CanNm_EnableCommunication is called, and CanNm's nm message transmission capability is restored.

当CanNm_DisableCommunication函数被调用，CanNm的NM-Timeout定时器将被停止，调用函数CanNm_EnableCommunication，NM-Timeout定时器将被恢复。若一直未调用CanNm_EnableCommunication，CanNm会一直处在Ready Sleep State中无法进入休眠状态，在这种情况下，AutoSar规定，当网络被释放后，CanNm将从Ready Sleep State切换至Prepare Bus-Sleep Mode。

When the CanNm_DisableCommunication function is called, CanNm's NM-Timeout timer will be stopped. Calling the function CanNm_EnableCommunication, the NM-Timeout timer will be restored.If CanNm_EnableCommunication has not been called, CanNm will always be in Ready Sleep State and cannot enter sleep state. In this case, AutoSar stipulates that when the network is released, CanNm will switch from Ready Sleep State to Prepare Bus-Sleep Mode.

NM协调器同步支持功能 (NM coordinator synchronization support function)
=============================================================================

当有多个协调器连接到同一条总线时，在CBV中，NmCoordinatorSleepReady位用于指示主协调器请求启动关闭，有关CBV的概念见2.2章。

When multiple coordinators are connected to the same bus, in CBV, the NmCoordinatorSleepReady bit is used to instruct the main coordinator to request startup shutdown. For the concept of CBV, see Chapter 2.2.

当CanNm处于网络模式，接收网络管理报文的CBV中NmCoordinatorSleepReady=1，则CanNm通知上层协调睡眠功能被请求。

When CanNm is in network mode and NmCoordinatorSleepReady=1 in the CBV of the received network management message, CanNm notifies the upper layer that the coordination sleep function is requested.

当CanNm已通知上层协调睡眠功能被请求，接收网络管理报文的CBV中NmCoordinatorSleepReady=0，则CanNm通知上层协调睡眠功能请求被取消。

When CanNm has notified the upper layer that the coordination sleep function is requested, and NmCoordinatorSleepReady=0 in the CBV of the received network management message, CanNm notifies the upper layer that the coordination sleep function request is cancelled.

减负载功能 (Load shedding function)
==============================================

当CanNmBusLoadReductionEnabled参数配置为TRUE时，CanNm应该支持总线负载降低机制，当从其他状态进入Repeat Message State状态时，关闭总线负载降低机制，当从其他状态进入Normal Operation State状态时，打开总线负载降低机制。

When the CanNmBusLoadReductionEnabled parameter is configured as TRUE, CanNm should support the bus load reduction mechanism. When entering the Repeat Message State from other states, the bus load reduction mechanism is turned off. When entering the Normal Operation State from other states, the bus load reduction mechanism is turned on.

当总线负载降低机制启动后，CanNm_RxIndication()被调用后，使用CanNmMsgReducedTime参数重装CanNm Message Cycle Timer，当总线负载降低机制启动后，当成功发送NM PDU后，用CanNmMsgCycleTime参数重装CanNm Message Cycle Timer。

When the bus load reduction mechanism is started, after CanNm_RxIndication() is called, use the CanNmMsgReducedTime parameter to reload the CanNm Message Cycle Timer. When the bus load reduction mechanism is started, when the NM PDU is successfully sent, use the CanNmMsgCycleTime parameter to reload the CanNm Message Cycle Timer.

PN功能 (PN function)
==================================

Autosar4.x版本开始支持PN功能，Pn功能的目的是基于功能划分网络，形成局域网；这种功能的划分由整车设计完成，对于各节点只需要关心自身存在的网段。只有在CanNmGlobalPnSupport(配置参数)和各通道下的CanNmPnEnabled(配置参数)使能的情况下，Pn功能才能正常工作。

Autosar4.x version begins to support the PN function. The purpose of the Pn function is to divide the network based on functions to form a local area network. This division of functions is completed by the vehicle design, and each node only needs to care about its own network segment.The Pn function can only work properly when CanNmGlobalPnSupport (configuration parameter) and CanNmPnEnabled (configuration parameter) under each channel are enabled.

如果CanNmPnEnabled(配置参数)为FALSE，则CanNm将执行正常的Rx指示处理，并且应禁用Pn功能。如果CanNmPnEnabled为TRUE，接收到的NM-PDU CBV中的PNI位为0，则CanNm模块应执行常规的Rx指示处理，从而省去了Pn功能的扩展。如果CanNmPnEnabled为TRUE并且接收到的NM-PDU CBV中的PNI位为1，则CanNm模块处理NM-PDU的Pn信息。

If CanNmPnEnabled (configuration parameter) is FALSE, CanNm will perform normal Rx indication processing and the Pn functionality should be disabled.If CanNmPnEnabled is TRUE and the PNI bit in the received NM-PDU CBV is 0, the CanNm module should perform conventional Rx indication processing, thereby eliminating the need for extension of the Pn function.If CanNmPnEnabled is TRUE and the PNI bit in the received NM-PDU CBV is 1, the CanNm module processes the Pn information of the NM-PDU.

如果CanNmPnEnabled为TRUE，则CanNm模块应将CBV中发送的PNI位的值设置为1，要使用Pn，则必须使用CBV。

If CanNmPnEnabled is TRUE, the CanNm module shall set the value of the PNI bit sent in CBV to 1. To use Pn, CBV must be used.

如果CanNmPnEnabled为FALSE，则CanNm模块应将CBV中已发送的PNI位的值始终设置为0。

If CanNmPnEnabled is FALSE, the CanNm module shall always set the value of the sent PNI bit in the CBV to 0.

Pn信息的位置位于网络管理报文的用户数据部分中，具体的位置通过CanNmPnInfoOffset和CanNmPnInfoLength来确定。

The location of the Pn information is located in the user data part of the network management message, and the specific location is determined by CanNmPnInfoOffset and CanNmPnInfoLength.

例如当CanNmPnInfoOffset = 3，CanNmPnInfoLength =2，代表NM消息只有字节3和字节4包含PN请求信息。

For example, when CanNmPnInfoOffset = 3 and CanNmPnInfoLength =2, it means that only bytes 3 and 4 of the NM message contain PN request information.

PN过滤 (PN filter)
--------------------------------

PNC是Partial Network Cluster的缩写，它是指为了在车辆网络中支持一个或多个车辆功能而由多个ECU构成的集群。PNC的编号我们称为PNC ID，范围8~63，整车网络统一编号，关于PNC id与CanNmPdu映射关系说明：PNC ID对应CanNmPdu中的一个bit，例如PNC ID=8，对应CanNmPduByte1的bit0；PNC ID=63，对应Byte7的bit7；PNC ID对应的bit数值为1，则表示当前PN网络被请求，为0则表示网络释放。

PNC is the abbreviation of Partial Network Cluster, which refers to a cluster composed of multiple ECUs in order to support one or more vehicle functions in the vehicle network.The number of PNC is called PNC ID, ranging from 8 to 63. It is a unified number for the entire vehicle network. Regarding the mapping relationship between PNC id and CanNmPdu, the PNC ID corresponds to a bit in CanNmPdu. For example, PNC ID=8 corresponds to bit0 of CanNmPduByte1; PNC ID=63 corresponds to bit7 of Byte7; the bit value corresponding to the PNC ID is 1, which means the current PN network is requested, and 0 means the network is released.

通过配置参数CanNmPnFilterMaskByte，CanNm可以检测到哪个PN与ECU相关，而哪个与PN不相关。

By configuring the parameter CanNmPnFilterMaskByte, CanNm can detect which PN is related to the ECU and which is not related to the PN.

CanNmPnFilterMaskByte的每个位具有以下含义：

Each bit of CanNmPnFilterMaskByte has the following meaning:

0 PN请求与本ECU无关。如果接收的NM PDU中将该位置设置为1，也无法使ECU的通讯栈处于唤醒状态，因为该位的请求与本ECU是无关的。

0 PN request has nothing to do with this ECU.If this bit is set to 1 in the received NM PDU, the ECU's communication stack cannot be awakened because the request for this bit has nothing to do with this ECU.

1PN请求与本ECU有关。如果已在接收的NM-PDU中将该位置设置为1，则ECU的通信堆栈将保持唤醒状态。

The 1PN request is related to this ECU.If this bit has been set to 1 in the received NM-PDU, the ECU's communication stack will remain awake.

如果至少有一位与本ECU相关的PN请求，那么这条Nm PDU对于CanNm来说就是有用的，需要进行处理，如果没有一位与本ECU相关的PN请求，那么这条NM PDU将被忽略。

If there is at least one PN request related to this ECU, then this Nm PDU is useful to CanNm and needs to be processed. If there is no PN request related to this ECU, then this NM PDU will be ignored.

ERA与EIRA (ERA and EIRA)
---------------------------------------

ERA是指ECU外部的PN请求的聚合，当CanNmPnEraCalcEnabled使能(配置参数)，表示支持ERA功能。而EIRA是指ECU内部和外部Pn请求的聚合，当CanNmPnEiraCalcEnabled使能(配置参数)，表示支持EIRA功能。

ERA refers to the aggregation of PN requests outside the ECU. When CanNmPnEraCalcEnabled is enabled (configuration parameter), it indicates that the ERA function is supported.EIRA refers to the aggregation of ECU internal and external Pn requests. When CanNmPnEiraCalcEnabled is enabled (configuration parameter), it indicates that the EIRA function is supported.

ERA是在网关节点才使用，此时没有内部的请求，只有不同的Channel对Pn的外部请求，ERA会为每个channel的每个PN位都设置一个监测的定时器，当CanNmPnResetTime(配置参数)时间内未请求PN，则将该PN的请求状态设置为未请求，每次请求状态有变化的时候都会通知上层PduR，由PduR模块进行转发。

ERA is only used at the gateway node. At this time, there are no internal requests, only external requests for Pn from different channels. ERA will set a monitoring timer for each PN bit of each channel. When the PN is not requested within the CanNmPnResetTime (configuration parameter) time, the request status of the PN is set to not requested. Each time the request status changes, the upper layer PduR will be notified, and the PduR module will forward it.

EIRA体现了当前节点与网络上其他节点对某一个PNC的请求与释放情况；EIRA不区分物理Channel，只针对不同的PN。EIRA会为每个PN位都设置一个监测的定时器，当CanNmPnResetTime(配置参数)时间内未请求PN，则将该PN的请求状态设置为未请求，每次请求状态有变化的时候都会通知上层PduR，由PduR模块进行转发。

EIRA reflects the request and release of a certain PNC by the current node and other nodes on the network; EIRA does not distinguish between physical channels and only targets different PNs.EIRA will set a monitoring timer for each PN bit. When the PN is not requested within the CanNmPnResetTime (configuration parameter) time, the request status of the PN will be set to not requested. Each time the request status changes, the upper layer PduR will be notified and forwarded by the PduR module.

自发传输 (spontaneous transmission)
-----------------------------------------------

如果网络被请求并且CanNmPnHandleMultipleNetworkRequest（配置参数）设置为TRUE，无论CanNm处于Ready Sleep State，Normal Operation State或Repeat Message State，CanNm应更改为或重新启动为Repeat Message State。并且，CanNm会传输CanNmImmediateNmTransmissions（配置参数）数量的报文，其中第一条报文立即传输，其他报文按CanNmImmediateNmCycleTime传输（配置参数）。

If a network is requested and CanNmPnHandleMultipleNetworkRequest (configuration parameter) is set to TRUE, CanNm should change to or restart to Repeat Message State whether CanNm is in Ready Sleep State, Normal Operation State or Repeat Message State.Moreover, CanNm will transmit the number of messages CanNmImmediateNmTransmissions (configuration parameter), of which the first message is transmitted immediately, and other messages are transmitted according to CanNmImmediateNmCycleTime (configuration parameter).

车辆唤醒功能 (Vehicle wake-up function)
=================================================

当CanNmCarWakeUpRxEnabled（配置参数）使能时，车辆唤醒功能被启用，目前暂时没有使用场景。如果任何接收到的NM-PDU中的Car Wakeup位为1，都会通知上层Nm。

When CanNmCarWakeUpRxEnabled (configuration parameter) is enabled, the vehicle wake-up function is enabled, and there is currently no usage scenario.If the Car Wakeup bit in any received NM-PDU is 1, the upper layer Nm will be notified.

当CanNmCarWakeUpRxEnabled（配置参数）使能，CanNmCarWakeUpFilterEnabled（配置参数）也使能时，只有收到NodeId等于CanNmCarWakeUpFilterNodeId的报文时，才会通知上层。

When CanNmCarWakeUpRxEnabled (configuration parameter) is enabled and CanNmCarWakeUpFilterEnabled (configuration parameter) is also enabled, the upper layer will be notified only when a message with NodeId equal to CanNmCarWakeUpFilterNodeId is received.

源文件描述 (Source file description)
===============================================

CanNm组件文件描述 (CanNm component file description)
==============================================================

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 文件 (document)
     - 说明 (illustrate)
   * - CanNm_Cfg.h
     - 定义CanNm模块预编译时用到的配置参数。 (Define the configuration parameters used when precompiling the CanNm module.)
   * - CanNm_Cfg.c
     - 定义CanNm模块生成的配置参数。 (Define the configuration parameters generated by the CanNm module.)
   * - CanNm.h
     - CanNm模块头文件，包含了API函数的扩展声明并定义了配置的数据结构。 (The CanNm module header file contains extended declarations of API functions and defines the configured data structure.)
   * - CanNm.c
     - CanNm模块源文件，包含了API函数的实现。 (CanNm module source file contains the implementation of API functions.)
   * - CanNm_Cbk.h
     - 包含CanNm供CanIf调用的API函数的声明 (Contains the declaration of the API function called by CanNm for CanIf)
   * - CanNm_Internal.h
     - 包含CanNm内部的变量和数据结构的定义 (Contains the definition of variables and data structures inside CanNm)
   * - CanNm_MemMap.h
     - CanNm编译抽象文件 (CanNm compiles abstract files)
         
         
         
.. figure:: ../../_static/参考手册(Module_Reference_Manual)/CanNm/image5.png
   :alt: CanNm组件文件交互关系图(CanNm component file interaction diagram)
   :name: CanNm组件文件交互关系图(CanNm component file interaction diagram)
   :align: center

API接口 (API interface)
=====================================

类型定义 (type definition)
--------------------------------------

CanNm_ConfigType类型定义 (CanNm_ConfigType type definition)
=======================================================================

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 名称 (name)
     - CanNm_ConfigType
   * - 类型 (type)
     - Structure
   * - 范围 (scope)
     - --
   * - 描述 (describe)
     - 此类型应包含容器CanNm_GlobalConfig及其子容器的参数。 (This type should contain the parameters of the container CanNm_GlobalConfig and its subcontainers.)
         
         
         
输入函数描述 (Enter function description)
---------------------------------------------------
.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 输入模块 (Input module)
     - API
   * - Det
     - Det_ReportError
   * - Nm
     - Nm_CarWakeUpIndication
   * - \
     - Nm_CoordReadyToSleepCancellation
   * - \
     - Nm_CoordReadyToSleepIndication
   * - \
     - Nm_PduRxIndication
   * - \
     - Nm_RemoteSleepCancellation
   * - \
     - Nm_RemoteSleepIndication
   * - \
     - Nm_StateChangeNotification
   * - \
     - Nm_TxTimeoutException
   * - \
     - Nm_RepeatMessageIndication
   * - \
     - Nm_BusSleepMode
   * - \
     - Nm_NetworkMode
   * - \
     - Nm_NetworkStartIndication
   * - \
     - Nm_PrepareBusSleepMode
   * - PduR
     - PduR_CanNmRxIndication
   * - \
     - PduR_CanNmTriggerTransmit
   * - \
     - PduR_CanNmTxConfirmation
   * - CanIf
     - CanIf_Transmit
   * - CanSM
     - CanSM_TxTimeoutException
         
         
         
静态接口函数定义 (Static interface function definition)
---------------------------------------------------------------

CanNm_Init函数定义 (CanNm_Init function definition)
===============================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function name:)
     - CanNm_Init
     - \
     - \
   * - 函数原型： (Function prototype:)
     - void CanNm_Init(
     - \
     - \
   * - \
     - constCanNm_ConfigType\* CanNmConfigPtr
     - \
     - \
   * - \
     - )
     - \
     - \
   * - 服务编号： (Service number:)
     - 0x00
     - \
     - \
   * - 同步/异步： (Sync/Asynchronous:)
     - 同步 (synchronous)
     - \
     - \
   * - 是否可重入： (Is it reentrant:)
     - 不可重入 (Not reentrant)
     - \
     - \
   * - 输入参数： (Input parameters:)
     - CanNmConfigPtr
     - 值域： (range:)
     - 指向初始化结构体的指针 (Pointer to initialization structure)
   * - 输入输出参数: (Input and output parameters:)
     - 无 (none)
     - \
     - \
   * - 输出参数： (Output parameters:)
     - 无 (none)
     - \
     - \
   * - 返回值： (Return value:)
     - 无 (none)
     - \
     - \
   * - 功能概述： (Function overview:)
     - 初始化完整的CanNm模块，即初始化在配置时激活的所有通道。 (Initialize the complete CanNm module, that is, initialize all channels activated during configuration.)
     - \
     - \
         
         
         
CanNm_DeInit函数定义 (CanNm_DeInit function definition)
===================================================================
.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 函数名称： (Function name:)
     - CanNm_DeInit
   * - 函数原型： (Function prototype:)
     - void CanNm_DeInit (
   * - \
     - void
   * - \
     - )
   * - 服务编号： (Service number:)
     - 0x10
   * - 同步/异步： (Sync/Asynchronous:)
     - 同步 (synchronous)
   * - 是否可重入： (Is it reentrant:)
     - 不可重入 (Not reentrant)
   * - 输入参数： (Input parameters:)
     - 无 (none)
   * - 输入输出参数: (Input and output parameters:)
     - 无 (none)
   * - 输出参数： (Output parameters:)
     - 无 (none)
   * - 返回值： (Return value:)
     - 无 (none)
   * - 功能概述： (Function overview:)
     - 反初始化CanNm模块 (Deinitialize the CanNm module)
         
         
         
CanNm_PassiveStartUp函数定义 (CanNm_PassiveStartUp function definition)
===================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function name:)
     - CanNm_PassiveStartUp
     - \
     - \
   * - 函数原型： (Function prototype:)
     - Std_ReturnTypeCanNm_PassiveStartUp(
     - \
     - \
   * - \
     - NetworkHandleTypenmChannelHandle
     - \
     - \
   * - \
     - )
     - \
     - \
   * - 服务编号： (Service number:)
     - 0x01
     - \
     - \
   * - 同步/异步： (Sync/Asynchronous:)
     - 非同步 (asynchronous)
     - \
     - \
   * - 是否可重入： (Is it reentrant:)
     - 可重入（同一通道不可重入） (Reentrant (the same channel cannot be reentrant))
     - \
     - \
   * - 输入参数： (Input parameters:)
     - nmChannelHandle
     - 值域： (range:)
     - NM通道Id (NM channel ID)
   * - 输入输出参数: (Input and output parameters:)
     - 无 (none)
     - \
     - \
   * - 输出参数： (Output parameters:)
     - 无 (none)
     - \
     - \
   * - 返回值： (Return value:)
     - E_OK:被动启动CanNm网络管理成功 (E_OK: Passively started CanNm network management successfully)
     - \
     - \
   * - \
     - E_NOT_OK:被动启动CanNm网络管理失败 (E_NOT_OK: Passive start of CanNm network management failed)
     - \
     - \
   * - 功能概述： (Function overview:)
     - 被动启动CanNm模块 (Passively start the CanNm module)
     - \
     - \
         
         
         
CanNm_NetworkRequest函数定义 (CanNm_NetworkRequest function definition)
===================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function name:)
     - CanNm_NetworkRequest
     - \
     - \
   * - 函数原型： (Function prototype:)
     - Std_ReturnTypeCanNm_NetworkRequest(
     - \
     - \
   * - \
     - NetworkHandleTypenmChannelHandle
     - \
     - \
   * - \
     - )
     - \
     - \
   * - 服务编号： (Service number:)
     - 0x02
     - \
     - \
   * - 同步/异步： (Sync/Asynchronous:)
     - 非同步 (asynchronous)
     - \
     - \
   * - 是否可重入： (Is it reentrant:)
     - 可重入（同一通道不可重入） (Reentrant (the same channel cannot be reentrant))
     - \
     - \
   * - 输入参数： (Input parameters:)
     - nmChannelHandle
     - 值域： (range:)
     - NM通道Id (NM channel ID)
   * - 输入输出参数: (Input and output parameters:)
     - 无 (none)
     - \
     - \
   * - 输出参数： (Output parameters:)
     - 无 (none)
     - \
     - \
   * - 返回值： (Return value:)
     - E_OK: 请求被接受 (E_OK: Request accepted)
     - \
     - \
   * - \
     - E_NOT_OK:请求被拒绝 (E_NOT_OK: Request rejected)
     - \
     - \
   * - 功能概述： (Function overview:)
     - 由于 ECU需要在总线上通信，因此请求网络 (Since the ECU needs to communicate on the bus, it requests the network)
     - \
     - \
         
         
         
CanNm_NetworkRelease函数定义 (CanNm_NetworkRelease function definition)
===================================================================================


.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function name:)
     - CanNm_NetworkRelease
     - \
     - \
   * - 函数原型： (Function prototype:)
     - Std_ReturnTypeCanNm_NetworkRelease(
     - \
     - \
   * - \
     - NetworkHandleTypenmChannelHandle
     - \
     - \
   * - \
     - )
     - \
     - \
   * - 服务编号： (Service number:)
     - 0x03
     - \
     - \
   * - 同步/异步： (Sync/Asynchronous:)
     - 非同步 (asynchronous)
     - \
     - \
   * - 是否可重入： (Is it reentrant:)
     - 可重入（同一通道不可重入） (Reentrant (the same channel cannot be reentrant))
     - \
     - \
   * - 输入参数： (Input parameters:)
     - nmChannelHandle
     - 值域： (range:)
     - NM通道Id (NM channel ID)
   * - 输入输出参数: (Input and output parameters:)
     - 无 (none)
     - \
     - \
   * - 输出参数： (Output parameters:)
     - 无 (none)
     - \
     - \
   * - 返回值： (Return value:)
     - E_OK: 请求被接受 (E_OK: Request accepted)
     - \
     - \
   * - \
     - E_NOT_OK:请求被拒绝 (E_NOT_OK: Request rejected)
     - \
     - \
   * - 功能概述： (Function overview:)
     - 由于ECU不需要在总线上通信，因此释放网络 (Since the ECU does not need to communicate on the bus, freeing up the network)
     - \
     - \
         
         
         
CanNm_DisableCommunication函数定义 (CanNm_DisableCommunication function definition)
===============================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function name:)
     - CanNm_DisableCommunication
     - \
     - \
   * - 函数原型： (Function prototype:)
     - Std_ReturnTypeCanNm_DisableCommunication(
     - \
     - \
   * - \
     - NetworkHandleTypenmChannelHandle
     - \
     - \
   * - \
     - )
     - \
     - \
   * - 服务编号： (Service number:)
     - 0x0c
     - \
     - \
   * - 同步/异步： (Sync/Asynchronous:)
     - 非同步 (asynchronous)
     - \
     - \
   * - 是否可重入： (Is it reentrant:)
     - 可重入(仅限不同通道) (Reentrant (different channels only))
     - \
     - \
   * - 输入参数： (Input parameters:)
     - nmChannelHandle
     - 值域： (range:)
     - NM通道Id (NM channel ID)
   * - 输入输出参数: (Input and output parameters:)
     - 无 (none)
     - \
     - \
   * - 输出参数： (Output parameters:)
     - 无 (none)
     - \
     - \
   * - 返回值： (Return value:)
     - E_OK: 请求成功 (E_OK: Request successful)
     - \
     - \
   * - \
     - E_NOT_OK:请求关闭通信失败 (E_NOT_OK: Request to close communication failed)
     - \
     - \
   * - 功能概述： (Function overview:)
     - 用于ISO14229的28服务，关闭通信 (28 service for ISO14229, communication closed)
     - \
     - \
         
         
         
CanNm_EnableCommunication函数定义 (CanNm_EnableCommunication function definition)
=============================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function name:)
     - CanNm_EnableCommunication
     - \
     - \
   * - 函数原型： (Function prototype:)
     - Std_ReturnTypeCanNm_EnableCommunication(
     - \
     - \
   * - \
     - NetworkHandleTypenmChannelHandle
     - \
     - \
   * - \
     - )
     - \
     - \
   * - 服务编号： (Service number:)
     - 0x0d
     - \
     - \
   * - 同步/异步： (Sync/Asynchronous:)
     - 非同步 (asynchronous)
     - \
     - \
   * - 是否可重入： (Is it reentrant:)
     - 可重入（同一通道不可重入） (Reentrant (the same channel cannot be reentrant))
     - \
     - \
   * - 输入参数： (Input parameters:)
     - nmChannelHandle
     - 值域： (range:)
     - NM通道Id (NM channel ID)
   * - 输入输出参数: (Input and output parameters:)
     - 无 (none)
     - \
     - \
   * - 输出参数： (Output parameters:)
     - 无 (none)
     - \
     - \
   * - 返回值： (Return value:)
     - E_OK: 请求成功 (E_OK: Request successful)
     - \
     - \
   * - \
     - E_NOT_OK:请求使能通信失败 (E_NOT_OK: Request to enable communication failed)
     - \
     - \
   * - 功能概述： (Function overview:)
     - 用于ISO14229的28服务，使能通信 (28 services for ISO14229, enabling communication)
     - \
     - \
         
         
         
CanNm_SetUserData函数定义 (CanNm_SetUserData function definition)
=============================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function name:)
     - CanNm_SetUserData
     - \
     - \
   * - 函数原型： (Function prototype:)
     - Std_ReturnTypeCanNm_SetUserData(
     - \
     - \
   * - \
     - NetworkHandleTypenmChannelHandle
     - \
     - \
   * - \
     - const uint8\*nmUserDataPtr
     - \
     - \
   * - \
     - )
     - \
     - \
   * - 服务编号： (Service number:)
     - 0x04
     - \
     - \
   * - 同步/异步： (Sync/Asynchronous:)
     - 同步 (synchronous)
     - \
     - \
   * - 是否可重入： (Is it reentrant:)
     - 不同通道可重入 (Different channels can re-entry)
     - \
     - \
   * - 输入参数： (Input parameters:)
     - nmChannelHandle
     - 值域： (range:)
     - NM通道Id (NM channel ID)
   * - \
     - nmUserDataPtr
     - 值域： (range:)
     - 指向要设置的用户数据的指针 (Pointer to the user data to set)
   * - 输入输出参数: (Input and output parameters:)
     - 无 (none)
     - \
     - \
   * - 输出参数： (Output parameters:)
     - 无 (none)
     - \
     - \
   * - 返回值： (Return value:)
     - E_OK:设置用户数据成功 (E_OK: Setting user data successfully)
     - \
     - \
   * - \
     - E_NOT_OK：设置用户数据失败 (E_NOT_OK: Failed to set user data)
     - \
     - \
   * - 功能概述： (Function overview:)
     - 设置总线上接下来发送的NM消息的用户数据 (Set the user data for the next NM message sent on the bus)
     - \
     - \
         
         
         
CanNm_GetUserData函数定义 (CanNm_GetUserData function definition)
=============================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function name:)
     - CanNm_GetUserData
     - \
     - \
   * - 函数原型： (Function prototype:)
     - Std_ReturnTypeCanNm_GetUserData(
     - \
     - \
   * - \
     - NetworkHandleTypenmChannelHandle
     - \
     - \
   * - \
     - uint8\*nmUserDataPtr
     - \
     - \
   * - \
     - )
     - \
     - \
   * - 服务编号： (Service number:)
     - 0x05
     - \
     - \
   * - 同步/异步： (Sync/Asynchronous:)
     - 同步 (synchronous)
     - \
     - \
   * - 是否可重入： (Is it reentrant:)
     - 可重入 (reentrant)
     - \
     - \
   * - 输入参数： (Input parameters:)
     - nmChannelHandle
     - 值域： (range:)
     - 请求获取用户数据的通道 (Channel to request user data)
   * - 输入输出参数: (Input and output parameters:)
     - 无 (none)
     - \
     - \
   * - 输出参数: (Output parameters:)
     - nmUserDataPtr
     - 值域： (range:)
     - 指向用于输出用户数据的内存的指针 (Pointer to memory used to output user data)
   * - 返回值： (Return value:)
     - E_OK:请求用户数据成功 (E_OK: Requesting user data successfully)
     - \
     - \
   * - \
     - E_NOT_OK:请求用户数据失败 (E_NOT_OK: Requesting user data failed)
     - \
     - \
   * - 功能概述： (Function overview:)
     - 从最近收到的NMPDU中获取用户数据 (Get user data from the most recently received NMPDU)
     - \
     - \
         
         
         
CanNm_Transmit函数定义 (CanNm_Transmit function definition)
=======================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function name:)
     - CanNm_Transmit
     - \
     - \
   * - 函数原型： (Function prototype:)
     - Std_ReturnTypeCanNm_Transmit(
     - \
     - \
   * - \
     - PduIdTypeTxPduId,
     - \
     - \
   * - \
     - constPduInfoType\*PduInfoPtr
     - \
     - \
   * - \
     - )
     - \
     - \
   * - 服务编号： (Service number:)
     - 0x49
     - \
     - \
   * - 同步/异步： (Sync/Asynchronous:)
     - 同步 (synchronous)
     - \
     - \
   * - 是否可重入： (Is it reentrant:)
     - 对不同的TxPduId可重入 (Reentrant for different TxPduIds)
     - \
     - \
   * - 输入参数： (Input parameters:)
     - TxPduId
     - 值域： (range:)
     - 要发送的Pdu的Id (Id of the Pdu to be sent)
   * - \
     - PduInfoPtr
     - 值域： (range:)
     - 要发送的数据长度和数据指针 (Data length and data pointer to be sent)
   * - 输入输出参数: (Input and output parameters:)
     - 无 (none)
     - \
     - \
   * - 输出参数： (Output parameters:)
     - 无 (none)
     - \
     - \
   * - 返回值： (Return value:)
     - E_OK：成功接收传输请求 (E_OK: Transfer request successfully received)
     - \
     - \
   * - \
     - E_NOT_OK：传输请求被拒绝 (E_NOT_OK: Transfer request rejected)
     - \
     - \
   * - 功能概述： (Function overview:)
     - 请求发送一帧NM报文 (Request to send a frame of NM message)
     - \
     - \
         
         
         
CanNm_GetNodeIdentifier函数定义 (CanNm_GetNodeIdentifier function definition)
=========================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function name:)
     - CanNm_GetNodeIdentifier
     - \
     - \
   * - 函数原型： (Function prototype:)
     - Std_ReturnTypeCanNm_GetNodeIdentifier(
     - \
     - \
   * - \
     - NetworkHandleTypenmChannelHandle,
     - \
     - \
   * - \
     - uint8\*nmNodeIdPtr
     - \
     - \
   * - \
     - )
     - \
     - \
   * - 服务编号： (Service number:)
     - 0x06
     - \
     - \
   * - 同步/异步： (Sync/Asynchronous:)
     - 同步 (synchronous)
     - \
     - \
   * - 是否可重入： (Is it reentrant:)
     - 可重入 (reentrant)
     - \
     - \
   * - 输入参数： (Input parameters:)
     - nmChannelHandle
     - 值域： (range:)
     - 获取NodeId的通道号 (Get the channel number of NodeId)
   * - 输入输出参数: (Input and output parameters:)
     - 无 (none)
     - \
     - \
   * - 输出参数： (Output parameters:)
     - nmNodeIdPtr
     - 值域： (range:)
     - 指向存储NodeId的变量的指针 (Pointer to the variable storing the NodeId)
   * - 返回值： (Return value:)
     - E_OK: 获取成功 (E_OK: Obtained successfully)
     - \
     - \
   * - \
     - E_NOT_OK:获取失败 (E_NOT_OK: Failed to obtain)
     - \
     - \
   * - 功能概述： (Function overview:)
     - 获取最近接收到的NM报文中的节点标识符 (Get the node identifier in the recently received NM message)
     - \
     - \
         
         
         
CanNm_GetLocalNodeIdentifier函数定义 (CanNm_GetLocalNodeIdentifier function definition)
===================================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function name:)
     - CanNm_GetLocalNodeIdentifier
     - \
     - \
   * - 函数原型： (Function prototype:)
     - Std_ReturnTypeCanNm_GetLocalNodeIdentifier(
     - \
     - \
   * - \
     - NetworkHandleTypenmChannelHandle,
     - \
     - \
   * - \
     - uint8\*nmNodeIdPtr
     - \
     - \
   * - \
     - )
     - \
     - \
   * - 服务编号： (Service number:)
     - 0x07
     - \
     - \
   * - 同步/异步： (Sync/Asynchronous:)
     - 同步 (synchronous)
     - \
     - \
   * - 是否可重入： (Is it reentrant:)
     - 可重入 (reentrant)
     - \
     - \
   * - 输入参数： (Input parameters:)
     - nmChannelHandle
     - 值域： (range:)
     - 获取NodeId的通道号 (Get the channel number of NodeId)
   * - 输入输出参数: (Input and output parameters:)
     - 无 (none)
     - \
     - \
   * - 输出参数： (Output parameters:)
     - nmNodeIdPtr
     - 值域： (range:)
     - 指向存储NodeId的变量的指针 (Pointer to the variable storing the NodeId)
   * - 返回值： (Return value:)
     - E_OK: 获取成功 (E_OK: Obtained successfully)
     - \
     - \
   * - \
     - E_NOT_OK:获取失败 (E_NOT_OK: Failed to obtain)
     - \
     - \
   * - 功能概述： (Function overview:)
     - 获取配置的该通道的本地节点标识符 (Get the configured local node identifier for this channel)
     - \
     - \
         
         
         
CanNm_RepeatMessageRequest函数定义 (CanNm_RepeatMessageRequest function definition)
===============================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function name:)
     - CanNm_RepeatMessageRequest
     - \
     - \
   * - 函数原型： (Function prototype:)
     - Std_ReturnTypeCanNm_RepeatMessageRequest(
     - \
     - \
   * - \
     - NetworkHandleTypenmChannelHandle
     - \
     - \
   * - \
     - )
     - \
     - \
   * - 服务编号： (Service number:)
     - 0x08
     - \
     - \
   * - 同步/异步： (Sync/Asynchronous:)
     - 非同步 (asynchronous)
     - \
     - \
   * - 是否可重入： (Is it reentrant:)
     - 可重入（同一通道不可重入） (Reentrant (the same channel cannot be reentrant))
     - \
     - \
   * - 输入参数： (Input parameters:)
     - nmChannelHandle
     - 值域： (range:)
     - 需要置位Repeat MessageRequest Bit的通道 (Channels that need to set the Repeat MessageRequest Bit)
   * - 输入输出参数: (Input and output parameters:)
     - 无 (none)
     - \
     - \
   * - 输出参数： (Output parameters:)
     - 无 (none)
     - \
     - \
   * - 返回值： (Return value:)
     - E_OK：设置成功 (E_OK: Setting successful)
     - \
     - \
   * - \
     - E_NOT_OK：设置重复标志位失败或未配置此网络。 (E_NOT_OK: Failed to set the duplicate flag or this network is not configured.)
     - \
     - \
   * - 功能概述： (Function overview:)
     - 为总线上接下来发送的NMPDU设置重复消息请求位 (Set the repeat message request bit for the next NMPDU sent on the bus)
     - \
     - \
         
         
         
CanNm_GetPduData函数定义 (CanNm_GetPduData function definition)
===========================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function name:)
     - CanNm_GetPduData
     - \
     - \
   * - 函数原型： (Function prototype:)
     - Std_ReturnTypeCanNm_GetPduData(
     - \
     - \
   * - \
     - NetworkHandleTypenmChannelHandle,
     - \
     - \
   * - \
     - uint8\*nmPduDataPtr
     - \
     - \
   * - \
     - )
     - \
     - \
   * - 服务编号： (Service number:)
     - 0x0a
     - \
     - \
   * - 同步/异步： (Sync/Asynchronous:)
     - 同步 (synchronous)
     - \
     - \
   * - 是否可重入： (Is it reentrant:)
     - 可重入 (reentrant)
     - \
     - \
   * - 输入参数： (Input parameters:)
     - nmChannelHandle
     - 值域： (range:)
     - NM通道Id (NM channel ID)
   * - 输入输出参数: (Input and output parameters:)
     - 无 (none)
     - \
     - \
   * - 输出参数： (Output parameters:)
     - nmPduDataPtr
     - 值域： (range:)
     - 获取到的NMPdu数据要被存放的地址 (The address where the obtained NMPdu data is to be stored.)
   * - 返回值： (Return value:)
     - E_OK: 获取成功 (E_OK: Obtained successfully)
     - \
     - \
   * - \
     - E_NOT_OK:获取数据失败或未配置此网络 (E_NOT_OK: Failed to obtain data or this network is not configured)
     - \
     - \
   * - 功能概述： (Function overview:)
     - 从最近接收到的NMPDU中获取整个PDU数据 (Get the entire PDU data from the most recently received NMPDU)
     - \
     - \
         
         
         
CanNm_GetState函数定义 (CanNm_GetState function definition)
=======================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function name:)
     - CanNm_GetState
     - \
     - \
   * - 函数原型： (Function prototype:)
     - Std_ReturnTypeCanNm_GetState(
     - \
     - \
   * - \
     - NetworkHandleTypenmChannelHandle,
     - \
     - \
   * - \
     - Nm_StateType\*nmStatePtr,
     - \
     - \
   * - \
     - Nm_ModeType\*nmModePtr
     - \
     - \
   * - \
     - )
     - \
     - \
   * - 服务编号： (Service number:)
     - 0x0b
     - \
     - \
   * - 同步/异步： (Sync/Asynchronous:)
     - 同步 (synchronous)
     - \
     - \
   * - 是否可重入： (Is it reentrant:)
     - 可重入 (reentrant)
     - \
     - \
   * - 输入参数： (Input parameters:)
     - nmChannelHandle
     - 值域： (range:)
     - NM通道Id (NM channel ID)
   * - 输入输出参数: (Input and output parameters:)
     - 无 (none)
     - \
     - \
   * - 输出参数： (Output parameters:)
     - nmStatePtr
     - 值域： (range:)
     - 存放CanNm状态的地址 (The address where CanNm status is stored)
   * - \
     - nmModePtr
     - 值域： (range:)
     - 存放CanNm模式的地址 (Store the address of CanNm mode)
   * - 返回值： (Return value:)
     - E_OK: 获取成功 (E_OK: Obtained successfully)
     - \
     - \
   * - \
     - E_NOT_OK:获取失败 (E_NOT_OK: Failed to obtain)
     - \
     - \
   * - 功能概述： (Function overview:)
     - 获取CanNm当前的状态和模式 (Get the current status and mode of CanNm)
     - \
     - \
         
         
         
CanNm_GetVersionInfo函数定义 (CanNm_GetVersionInfo function definition)
===================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function name:)
     - CanNm_GetVersionInfo
     - \
     - \
   * - 函数原型： (Function prototype:)
     - voidCanNm_GetVersionInfo(
     - \
     - \
   * - \
     - Std\_VersionInfoType\*Versioninfo
     - \
     - \
   * - \
     - )
     - \
     - \
   * - 服务编号： (Service number:)
     - 0xf1
     - \
     - \
   * - 同步/异步： (Sync/Asynchronous:)
     - 同步 (synchronous)
     - \
     - \
   * - 是否可重入： (Is it reentrant:)
     - 可重入 (reentrant)
     - \
     - \
   * - 输入参数： (Input parameters:)
     - 无 (none)
     - \
     - \
   * - 输入输出参数: (Input and output parameters:)
     - 无 (none)
     - \
     - \
   * - 输出参数： (Output parameters:)
     - versioninfo
     - 值域： (range:)
     - 指向存储版本信息的buffer的地址 (Address pointing to the buffer where version information is stored)
   * - 返回值： (Return value:)
     - 无 (none)
     - \
     - \
   * - 功能概述： (Function overview:)
     - 获取版本信息 (Get version information)
     - \
     - \
         
         
         
CanNm_RequestBusSynchronization函数定义 (CanNm_RequestBusSynchronization function definition)
=========================================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function name:)
     - CanNm_RequestBusSynchronization
     - \
     - \
   * - 函数原型： (Function prototype:)
     - Std_ReturnTypeCanNm_RequestBusSynchronization(
     - \
     - \
   * - \
     - NetworkHandleTypenmChannelHandle
     - \
     - \
   * - \
     - )
     - \
     - \
   * - 服务编号： (Service number:)
     - 0xc0
     - \
     - \
   * - 同步/异步： (Sync/Asynchronous:)
     - 非同步 (asynchronous)
     - \
     - \
   * - 是否可重入： (Is it reentrant:)
     - 不可重入 (Not reentrant)
     - \
     - \
   * - 输入参数： (Input parameters:)
     - nmChannelHandle
     - 值域： (range:)
     - NM通道Id (NM channel ID)
   * - 输入输出参数: (Input and output parameters:)
     - 无 (none)
     - \
     - \
   * - 输出参数： (Output parameters:)
     - 无 (none)
     - \
     - \
   * - 返回值： (Return value:)
     - E_OK: 请求成功 (E_OK: Request successful)
     - \
     - \
   * - \
     - E_NOT_OK:请求失败 (E_NOT_OK: Request failed)
     - \
     - \
   * - 功能概述： (Function overview:)
     - 请求总线同步 (Request bus synchronization)
     - \
     - \
         
         
         
CanNm_CheckRemoteSleepIndication函数定义 (CanNm_CheckRemoteSleepIndication function definition)
===========================================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function name:)
     - CanNm_CheckRemoteSleepIndication
     - \
     - \
   * - 函数原型： (Function prototype:)
     - Std_ReturnTypeCanNm_CheckRemoteSleepIndication(
     - \
     - \
   * - \
     - NetworkHandleTypenmChannelHandle,
     - \
     - \
   * - \
     - boolean\*nmRemoteSleepIndPtr
     - \
     - \
   * - \
     - )
     - \
     - \
   * - 服务编号： (Service number:)
     - 0xd0
     - \
     - \
   * - 同步/异步： (Sync/Asynchronous:)
     - 同步 (synchronous)
     - \
     - \
   * - 是否可重入： (Is it reentrant:)
     - 可重入 (reentrant)
     - \
     - \
   * - 输入参数： (Input parameters:)
     - nmChannelHandle
     - 值域： (range:)
     - NM通道Id (NM channel ID)
   * - 输入输出参数: (Input and output parameters:)
     - 无 (none)
     - \
     - \
   * - 输出参数： (Output parameters:)
     - nmRemoteSleepIndPtr
     - 值域： (range:)
     - 检测是否发生远程睡眠通知结果存储地址 (Detect whether remote sleep notification result storage address occurs)
   * - 返回值： (Return value:)
     - E_OK: 检查成功 (E_OK: Check successful)
     - \
     - \
   * - \
     - E_NOT_OK:获取指示失败 (E_NOT_OK: Failed to obtain instructions)
     - \
     - \
   * - 功能概述： (Function overview:)
     - 检查是否发生远程睡眠通知 (Check if remote sleep notification occurs)
     - \
     - \
         
         
         
CanNm_SetSleepReadyBit函数定义 (CanNm_SetSleepReadyBit function definition)
=======================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function name:)
     - CanNm_SetSleepReadyBit
     - \
     - \
   * - 函数原型： (Function prototype:)
     - Std_ReturnTypeCanNm\_SetSleepReadyBit(
     - \
     - \
   * - \
     - NetworkHandleTypenmChannelHandle,
     - \
     - \
   * - \
     - booleannmSleepReadyBit
     - \
     - \
   * - \
     - )
     - \
     - \
   * - 服务编号： (Service number:)
     - 0x17
     - \
     - \
   * - 同步/异步： (Sync/Asynchronous:)
     - 同步 (synchronous)
     - \
     - \
   * - 是否可重入： (Is it reentrant:)
     - 不同通道可重入 (Different channels can re-entry)
     - \
     - \
   * - 输入参数： (Input parameters:)
     - nmChannelHandle
     - 值域： (range:)
     - NM通道Id (NM channel ID)
   * - \
     - nmSleepReadyBit
     - 值域： (range:)
     - Sleep ReadyBit要设置的的值 (Sleep ReadyBit value to be set)
   * - 输入输出参数: (Input and output parameters:)
     - 无 (none)
     - \
     - \
   * - 输出参数： (Output parameters:)
     - 无 (none)
     - \
     - \
   * - 返回值： (Return value:)
     - E_OK: 设置成功 (E_OK: Setup successful)
     - \
     - \
   * - \
     - E_NOT_OK:设置失败 (E_NOT_OK: Setting failed)
     - \
     - \
   * - 功能概述： (Function overview:)
     - 在控制位向量中设置NM协调器睡眠就绪位 (Set the NM coordinator sleep ready bit in the control bit vector)
     - \
     - \
         
         
         
CanNm_TxConfirmation函数定义 (CanNm_TxConfirmation function definition)
===================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function name:)
     - CanNm_TxConfirmation
     - \
     - \
   * - 函数原型： (Function prototype:)
     - voidCanNm_TxConfirmation(
     - \
     - \
   * - \
     - PduIdType TxPduId
     - \
     - \
   * - \
     - )
     - \
     - \
   * - 服务编号： (Service number:)
     - 0x40
     - \
     - \
   * - 同步/异步： (Sync/Asynchronous:)
     - 同步 (synchronous)
     - \
     - \
   * - 是否可重入： (Is it reentrant:)
     - 不同PduId可重入 (Different PduId can be re-entrant)
     - \
     - \
   * - 输入参数： (Input parameters:)
     - TxPduId
     - 值域： (range:)
     - 发送成功的PduId (Send successful PduId)
   * - 输入输出参数: (Input and output parameters:)
     - 无 (none)
     - \
     - \
   * - 输出参数： (Output parameters:)
     - 无 (none)
     - \
     - \
   * - 返回值： (Return value:)
     - 无 (none)
     - \
     - \
   * - 功能概述： (Function overview:)
     - 底层通信模块确认成功发送报文 (The underlying communication module confirms that the message was successfully sent)
     - \
     - \
         
         
         
CanNm_RxIndication函数定义 (CanNm_RxIndication function definition)
===============================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function name:)
     - CanNm_RxIndication
     - \
     - \
   * - 函数原型： (Function prototype:)
     - voidCanNm_RxIndication(
     - \
     - \
   * - \
     - PduIdTypeRxPduId,
     - \
     - \
   * - \
     - constPduInfoType\*PduInfoPtr
     - \
     - \
   * - \
     - )
     - \
     - \
   * - 服务编号： (Service number:)
     - 0x42
     - \
     - \
   * - 同步/异步： (Sync/Asynchronous:)
     - 同步 (synchronous)
     - \
     - \
   * - 是否可重入： (Is it reentrant:)
     - 不同PduId可重入 (Different PduId can be re-entrant)
     - \
     - \
   * - 输入参数： (Input parameters:)
     - RxPduId
     - 值域： (range:)
     - 接收报文的PduId (PduId of received message)
   * - \
     - PduInfoPtr
     - 值域： (range:)
     - 接收报文的长度和指向报文的指针 (The length of the received message and the pointer to the message)
   * - 输入输出参数: (Input and output parameters:)
     - 无 (none)
     - \
     - \
   * - 输出参数： (Output parameters:)
     - 无 (none)
     - \
     - \
   * - 返回值： (Return value:)
     - 无 (none)
     - \
     - \
   * - 功能概述： (Function overview:)
     - 底层通信模块调用该函数通知CanNm接收到NM报文 (The underlying communication module calls this function to notify CanNm that it has received the NM message.)
     - \
     - \
         
         
         
CanNm_ConfirmPnAvailability函数定义 (CanNm_ConfirmPnAvailability function definition)
=================================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function name:)
     - CanNm_ConfirmPnAvailability
     - \
     - \
   * - 函数原型： (Function prototype:)
     - voidCanNm_ConfirmPnAvailability(
     - \
     - \
   * - \
     - NetworkHandleTypenmChannelHandle
     - \
     - \
   * - \
     - )
     - \
     - \
   * - 服务编号： (Service number:)
     - 0x16
     - \
     - \
   * - 同步/异步： (Sync/Asynchronous:)
     - 同步 (synchronous)
     - \
     - \
   * - 是否可重入： (Is it reentrant:)
     - 可重入（仅限不同channel） (Reentrant (only different channels))
     - \
     - \
   * - 输入参数： (Input parameters:)
     - nmChannelHandle
     - 值域： (range:)
     - NM通道Id (NM channel ID)
   * - 输入输出参数: (Input and output parameters:)
     - 无 (none)
     - \
     - \
   * - 输出参数： (Output parameters:)
     - 无 (none)
     - \
     - \
   * - 返回值： (Return value:)
     - E_OK: 设置成功 (E_OK: Setup successful)
     - \
     - \
   * - \
     - E_NOT_OK:设置失败 (E_NOT_OK: Setting failed)
     - \
     - \
   * - 功能概述： (Function overview:)
     - 在指定的NMchannel上启用PN滤波功能 (Enable PN filtering function on the specified NMchannel)
     - \
     - \
         
         
         
CanNm_TriggerTransmit函数定义 (CanNm_TriggerTransmit function definition)
=====================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function name:)
     - CanNm_TriggerTransmit
     - \
     - \
   * - \
     - Std_ReturnType CanNm_TriggerTransmit (
     - \
     - \
   * - \
     - PduIdType TxPduId,
     - \
     - \
   * - \
     - PduInfoType* PduInfoPtr
     - \
     - \
   * - \
     - )
     - \
     - \
   * - 服务编号： (Service number:)
     - 0x41
     - \
     - \
   * - 同步/异步： (Sync/Asynchronous:)
     - 同步 (synchronous)
     - \
     - \
   * - 是否可重入： (Is it reentrant:)
     - 不同PduId可重入 (Different PduId can be re-entrant)
     - \
     - \
   * - 输入参数： (Input parameters:)
     - TxPduId
     - 值域： (range:)
     - 发送PduId (SendPduId)
   * - 输入输出参数: (Input and output parameters:)
     - PduInfoPtr
     - 值域： (range:)
     - 下层模块提供的用于存储发送数据的buffer地址和buffer大小。返回时将实际拷贝的数据长度赋值给sduLength。 (The buffer address and buffer size provided by the lower module for storing sent data.When returning, assign the actual copied data length to sduLength.)
   * - 输出参数： (Output parameters:)
     - 无 (none)
     - \
     - \
   * - \
     - E_OK: 从CanNm获取数据成功 (E_OK: Obtaining data from CanNm successfully)
     - \
     - \
   * - \
     - E_NOT_OK: 从CanNm获取数据失败 (E_NOT_OK: Failed to get data from CanNm)
     - \
     - \
   * - 功能概述： (Function overview:)
     - 下层模块在发送数据时调用该函数从CanNm获取要发送的数据 (The lower module calls this function to obtain the data to be sent from CanNm when sending data.)
     - \
     - \
         
         
         
CanNm_MainFunction函数定义 (CanNm_MainFunction function definition)
===============================================================================

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 函数名称： (Function name:)
     - CanNm_MainFunction
   * - 函数原型： (Function prototype:)
     - void CanNm_MainFunction(
   * - \
     - void
   * - \
     - )
   * - 服务编号： (Service number:)
     - 0x13
   * - 功能概述： (Function overview:)
     - CanNm模块周期调度函数 (CanNm module periodic scheduling function)
         
         
         
可配置函数定义 (Configurable function definition)
----------------------------------------------------------

无。

none.

配置 (Configuration)
==================================

CanNmGlobalConfig
---------------------------------

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/CanNm/image6.png
   :alt: CanNmGlobalConfig容器配置图(CanNmGlobalConfig container configuration diagram)
   :name: CanNmGlobalConfig容器配置图(CanNmGlobalConfig container configuration diagram)
   :align: center

.. centered:: **表 CanNmGlobalConfig属性描述 (Table CanNmGlobalConfig property description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI name)
     - 描述 (describe)
     - \
     - \
     - \
   * - CanNmBusLoadReductionEnabled
     - 取值范围 (Value range)
     - STD_ON,STD_OFF
     - 默认取值 (Default value)
     - 无 (none)
   * - \
     - 参数描述 (Parameter description)
     - 预处理器开关，用于启用总线减负载支持 (Preprocessor switch to enable bus load shedding support)
     - \
     - \
   * - \
     - 依赖关系 (Dependencies)
     - 如果CanNmPassiveModeEnabled== true 或CanNmGlobalPnSupport==true，那么CanNmBusLoadReductionEnabled= false (If CanNmPassiveModeEnabled== true or CanNmGlobalPnSupport==true, then CanNmBusLoadReductionEnabled= false)
     - \
     - \
   * - CanNmBusSynchronizationEnabled
     - 取值范围 (Value range)
     - STD_ON,STD_OFF
     - 默认取值 (Default value)
     - 无 (none)
   * - \
     - 参数描述 (Parameter description)
     - 预处理器开关，用于启用总线同步支持，此功能仅适用于网关节点 (Preprocessor switch to enable bus synchronization support, this feature is only available for gateway nodes)
     - \
     - \
   * - \
     - 依赖关系 (Dependencies)
     - 如果（CanNmPassiveModeEnabled==False），那么等于（NmBusSynchronizationEnabled）否则等于（False）
     - \
     - \
   * - CanNmComControlEnabled
     - 取值范围 (Value range)
     - STD_ON,STD_OFF
     - 默认取值 (Default value)
     - 无 (none)
   * - \
     - 参数描述 (Parameter description)
     - 预处理器开关，用于启用通信控制支持 (Preprocessor switch to enable communication control support)
     - \
     - \
   * - \
     - 依赖关系 (Dependencies)
     - 如果（CanNmPassiveModeEnabled==False），那么等于（NmComControlEnabled）否则等于（False）
     - \
     - \
   * - CanNmComUserDataSupport
     - 取值范围 (Value range)
     - STD_ON,STD_OFF
     - 默认取值 (Default value)
     - 无 (none)
   * - \
     - 参数描述 (Parameter description)
     - 用于启用Com用户数据的预处理器开关 (Preprocessor switch for enabling Com user data)
     - \
     - \
   * - \
     - 依赖关系 (Dependencies)
     - 如果CanNmPassiveModeEnabled== True则CanNmComUserDataSupport= False (If CanNmPassiveModeEnabled== True then CanNmComUserDataSupport= False)
     - \
     - \
   * - CanNmCoordinatorSyncSupport
     - 取值范围 (Value range)
     - STD_ON,STD_OFF
     - 默认取值 (Default value)
     - 无 (none)
   * - \
     - 参数描述 (Parameter description)
     - 启用/禁用协调器同步支持。 (Enable/disable coordinator synchronization support.)
     - \
     - \
   * - \
     - 依赖关系 (Dependencies)
     - 如果将CanNmPassiveModeEnabled设置为TRUE，则必须将CanNmCoordinatorSyncSupport设置为FALSE。 (If CanNmPassiveModeEnabled is set to TRUE, CanNmCoordinatorSyncSupport must be set to FALSE.)
     - \
     - \
   * - CanNmDevErrorDetect
     - 取值范围 (Value range)
     - true, false
     - 默认取值 (Default value)
     - false
   * - \
     - 参数描述 (Parameter description)
     - 打开或关闭开发错误检测 (Turn development error detection on or off)
     - \
     - \
   * - \
     - 依赖关系 (Dependencies)
     - 无 (none)
     - \
     - \
   * - CanNmGlobalPnSupport
     - 取值范围 (Value range)
     - STD_ON,STD_OFF
     - 默认取值 (Default value)
     - 无 (none)
   * - \
     - 参数描述 (Parameter description)
     - 用于全局启用部分网络支持的预处理器开关。 (Preprocessor switch for globally enabling partial network support.)
     - \
     - \
   * - \
     - 依赖关系 (Dependencies)
     - 无 (none)
     - \
     - \
   * - CanNmImmediateRestartEnabled
     - 取值范围 (Value range)
     - STD_ON,STD_OFF
     - 默认取值 (Default value)
     - 无 (none)
   * - \
     - 参数描述 (Parameter description)
     - 预处理器开关，用于在准备总线休眠模式下根据总线通信请求启用NMPDU立即传输 (Preprocessor switch to enable immediate transmission of NMPDU upon bus communication request in prepare bus sleep mode)
     - \
     - \
   * - \
     - 依赖关系 (Dependencies)
     - 如果定义了CanNmPassiveModeEnabled，则不能定义它 (Cannot define CanNmPassiveModeEnabled if it is defined)
     - \
     - \
   * - CanNmImmediateTxconfEnabled
     - 取值范围 (Value range)
     - STD_ON,STD_OFF
     - 默认取值 (Default value)
     - 无 (none)
   * - \
     - 参数描述 (Parameter description)
     - 启用/禁用立即发送确认。 (Enable/disable sending confirmation immediately.)
     - \
     - \
   * - \
     - 依赖关系 (Dependencies)
     - 如果CanNmPasiveModeEnabled已启用，则不应启用CanNmImmediateTxconfEnabled。 (CanNmImmediateTxconfEnabled should not be enabled if CanNmPasiveModeEnabled is enabled.)
     - \
     - \
   * - CanNmMainFunctionPeriod
     - 取值范围 (Value range)
     - 0.001..0.255
     - 默认取值 (Default value)
     - 无 (none)
   * - \
     - 参数描述 (Parameter description)
     - 各个实例的CanNm_MainFunction的调用周期，以秒为单位指定。 (The calling period of CanNm_MainFunction of each instance, specified in seconds.)
     - \
     - \
   * - \
     - 依赖关系 (Dependencies)
     - 取值需要大于0 (The value needs to be greater than 0)
     - \
     - \
   * - CanNmPassiveModeEnabled
     - 取值范围 (Value range)
     - STD_ON,STD_OFF
     - 默认取值 (Default value)
     - 无 (none)
   * - \
     - 参数描述 (Parameter description)
     - 预处理器开关，用于支持被动模式 (Preprocessor switch to support passive mode)
     - \
     - \
   * - \
     - 依赖关系 (Dependencies)
     - 依赖于NmIf模块的NmPassiveModeEnabled (Depends on NmPassiveModeEnabled of NmIf module)
     - \
     - \
   * - CanNmPduRxIndicationEnabled
     - 取值范围 (Value range)
     - STD_ON,STD_OFF
     - 默认取值 (Default value)
     - 无 (none)
   * - \
     - 参数描述 (Parameter description)
     - 用于启用PDURx指示的预处理器开关 (Preprocessor switch to enable PDURx indication)
     - \
     - \
   * - \
     - 依赖关系 (Dependencies)
     - 依赖于NmIf模块的NmPduRxIndicationEnabled (Depends on NmPduRxIndicationEnabled of NmIf module)
     - \
     - \
   * - CanNmPnEiraCalcEnabled
     - 取值范围 (Value range)
     - STD_ON,STD_OFF
     - 默认取值 (Default value)
     - FALSE
   * - \
     - 参数描述 (Parameter description)
     - 指定CanNm是否计算内部外部请求的PN请求信息（EIRA）
     - \
     - \
   * - \
     - 依赖关系 (Dependencies)
     - 仅当CanNmGlobalPnSupport== true时可配置 (Configurable only when CanNmGlobalPnSupport== true)
     - \
     - \
   * - CanNmPnResetTime
     - 取值范围 (Value range)
     - 0.001~65.535
     - 默认取值 (Default value)
     - 无 (none)
   * - \
     - 参数描述 (Parameter description)
     - 以秒为单位指定重置定时器的运行时间。该复位时间对EIRA和ERA中的PN请求复位有效。每个通道的值应该相同。因此它是一个全局配置参数 (Specifies the time in seconds for the reset timer to run.This reset time is valid for PN request reset in EIRA and ERA.The value should be the same for each channel.Therefore it is a global configuration parameter)
     - \
     - \
   * - \
     - 依赖关系 (Dependencies)
     - 仅当CanNmGlobalPnSupport== true时可配置 (Configurable only when CanNmGlobalPnSupport== true)
     - \
     - \
   * - \
     - \
     - CanNmPnResetTime>CanNmMsgCycleTime
     - \
     - \
   * - \
     - \
     - CanNmPnResetTime<CanNmTimeoutTime
     - \
     - \
   * - CanNmRemoteSleepIndEnabled
     - 取值范围 (Value range)
     - STD_ON,STD_OFF
     - 默认取值 (Default value)
     - 无 (none)
   * - \
     - 参数描述 (Parameter description)
     - 预处理器开关，支持远程睡眠指示，此功能仅适用于网关节点 (Preprocessor switch to support remote sleep indication, this feature is only available for gateway nodes)
     - \
     - \
   * - \
     - 依赖关系 (Dependencies)
     - 如果（CanNmPassiveModeEnabled==False），那么等于（NmComControlEnabled）否则等于（False）
     - \
     - \
   * - CanNmStateChangeIndEnabled
     - 取值范围 (Value range)
     - STD_ON,STD_OFF
     - 默认取值 (Default value)
     - 无 (none)
   * - \
     - 参数描述 (Parameter description)
     - 用于启用CanNM状态更改通知的预处理器开关 (Preprocessor switch to enable CanNM state change notifications)
     - \
     - \
   * - \
     - 依赖关系 (Dependencies)
     - 依赖于NmStateChangeIdEnabled (Depends on NmStateChangeIdEnabled)
     - \
     - \
   * - CanNmUserDataEnabled
     - 取值范围 (Value range)
     - STD_ON,STD_OFF
     - 默认取值 (Default value)
     - 无 (none)
   * - \
     - 参数描述 (Parameter description)
     - 预处理器开关，用于支持用户数据 (Preprocessor switch to support user data)
     - \
     - \
   * - \
     - 依赖关系 (Dependencies)
     - 依赖于NmUserDataEnabled (Depends on NmUserDataEnabled)
     - \
     - \
   * - CanNmVersionInfoApi
     - 取值范围 (Value range)
     - STD_ON,STD_OFF
     - 默认取值 (Default value)
     - 无 (none)
   * - \
     - 参数描述 (Parameter description)
     - 启用或者禁用版本获取API (Enable or disable version acquisition API)
     - \
     - \
   * - \
     - 依赖关系 (Dependencies)
     - 无 (none)
     - \
     - \
   * - CanNmPnEiraRxNSduRef
     - 取值范围 (Value range)
     - Reference to [ Pdu]
     - 默认取值 (Default value)
     - 无 (none)
   * - \
     - 参数描述 (Parameter description)
     - 引用COM-Stack中Pdu。CanNm只需要一个SduRef，因为EIRA是所有以太网通道上的聚合。 (Reference Pdu in COM-Stack.CanNm only requires one SduRef since EIRA is aggregated on all Ethernet channels.)
     - \
     - \
   * - \
     - 依赖关系 (Dependencies)
     - 仅当CanNmPnEiraCalcEnabled==true时可配，引用的PDU需要在PDUR中进行关联 (Configurable only when CanNmPnEiraCalcEnabled==true, the referenced PDU needs to be associated in the PDUR)
     - \
     - \
         

CanNmChannelConfig
==================================

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/CanNm/image7.png
   :alt: CanNmChannelConfig容器配置图(CanNmChannelConfig container configuration diagram)
   :name: CanNmChannelConfig容器配置图(CanNmChannelConfig container configuration diagram)
   :align: center

.. centered:: **表 CanNmChannelConfig属性描述 (Table CanNmChannelConfig property description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI name)
     - 描述 (describe)
     - \
     - \
     - \
   * - \
     - 取值范围 (Value range)
     - STD_ON,STD_OFF
     - 默认取值 (Default value)
     - FALSE
   * - CanNmActiveWakeupBitEnabled
     - 参数描述 (Parameter description)
     - 在CanNm模块中启用/禁用处理Active   Wakeup Bit (Enable/disable handling of Active Wakeup Bit in CanNm module)
     - \
     - \
   * - \
     - 依赖关系 (Dependencies)
     - 此参数仅在CanNmPassiveModeEnabled为False时可配置 (This parameter is only configurable when CanNmPassiveModeEnabled is False)
     - \
     - \
   * - \
     - 取值范围 (Value range)
     - STD_ON,STD_OFF
     - 默认取值 (Default value)
     - FALSE
   * - \
     - 参数描述 (Parameter description)
     - 指定   CanNm 是否丢弃不相关的   NM PDU。 (Specifies whether CanNm discards irrelevant NM PDUs.)
     - \
     - \
   * - \
     - 依赖关系 (Dependencies)
     - 仅当   CanNmPnEiraCalcEnabled == true 或CanNmPnEraCalcEnabled   == true时有效 (Only valid when CanNmPnEiraCalcEnabled == true or CanNmPnEraCalcEnabled == true)
     - \
     - \
   * - \
     - 取值范围 (Value range)
     - STD_ON,STD_OFF
     - 默认取值 (Default value)
     - 无 (none)
   * - CanNmBusLoadReductionActive
     - 参数描述 (Parameter description)
     - 该参数定义了各自NM通道的总线减负载功能是否启用。 (This parameter defines whether the bus load shedding function of the respective NM channel is enabled.)
     - \
     - \
   * - \
     - 依赖关系 (Dependencies)
     - 如果CanNmBusLoadReductionEnabled   == false则CanNmBusLoadReductionActive   = false (If CanNmBusLoadReductionEnabled == false then CanNmBusLoadReductionActive = false)
     - \
     - \
   * - \
     - 取值范围 (Value range)
     - 0..7
     - 默认取值 (Default value)
     - 无 (none)
   * - CanNmCarWakeUpBitPosition
     - 参数描述 (Parameter description)
     - 指定CWU在NM   PDU中的Bit位置。 (Specify the bit position of the CWU in the NM PDU.)
     - \
     - \
   * - \
     - 依赖关系 (Dependencies)
     - 仅当   CanNmCarWakeUpRxEnabled == TRUE 时可用 (Only available when CanNmCarWakeUpRxEnabled == TRUE)
     - \
     - \
   * - \
     - 取值范围 (Value range)
     - 0..7
     - 默认取值 (Default value)
     - 无 (none)
   * - CanNmCarWakeUpBytePosition
     - 参数描述 (Parameter description)
     - 指定CWU在NM   PDU中的Byte位置。 (Specify the byte position of the CWU in the NM PDU.)
     - \
     - \
   * - \
     - 依赖关系 (Dependencies)
     - 仅当   CanNmCarWakeUpRxEnabled == TRUE 时可用，CanNmCarWakeupBytePosition   ≥ 启用的系统字节数   (CBV,NID)
     - \
     - \
   * - \
     - 取值范围 (Value range)
     - STD_ON,STD_OFF
     - 默认取值 (Default value)
     - 无 (none)
   * - CanNmCarWakeUpFilterEnabled
     - 参数描述 (Parameter description)
     - 如果支持CWU过滤，则仅NM   PDU中具有源节点标识符CanNmCarWakeUpFilterNodeId的CWU位被视为CWU请求。 (If CWU filtering is supported, only the CWU bits in the NM PDU with the source node identifier CanNmCarWakeUpFilterNodeId are considered CWU requests.)
     - \
     - \
   * - \
     - 依赖关系 (Dependencies)
     - CanNmCarWakeUpRxEnabled=TRUE
     - \
     - \
   * - \
     - 取值范围 (Value range)
     - 0~255
     - 默认取值 (Default value)
     - 无 (none)
   * - CanNmCarWakeUpFilterNodeId
     - 参数描述 (Parameter description)
     - CWU过滤的源节点标识符。如果支持CWU过滤，则只有具有源节点标识符CanNmCarWakeUpFilterNodeId的NM   PDU中的CWU位被视为CWU请求 (Source node identifier for CWU filtering.If CWU filtering is supported, only the CWU bits in the NM PDU with the source node identifier CanNmCarWakeUpFilterNodeId are considered CWU requests)
     - \
     - \
   * - \
     - 依赖关系 (Dependencies)
     - CanNmCarWakeUpFilterEnabled=TRUE
     - \
     - \
   * - \
     - 取值范围 (Value range)
     - STD_ON,STD_OFF
     - 默认取值 (Default value)
     - FALSE
   * - CanNmCarWakeUpRxEnabled
     - 参数描述 (Parameter description)
     - 启用或禁用在接收的NM   PDU中支持CarWakeUp  bit评估 (Enable or disable support for CarWakeUp bit evaluation in received NM PDUs)
     - \
     - \
   * - \
     - 依赖关系 (Dependencies)
     - 依赖于NmIf模块的NmCarWakeUpRxEnabled (NmCarWakeUpRxEnabled which depends on NmIf module)
     - \
     - \
   * - \
     - 取值范围 (Value range)
     - 0.001..65.535
     - 默认取值 (Default value)
     - 无 (none)
   * - \
     - 参数描述 (Parameter description)
     - 定义用于CanNmImmediateNmTransmissions   NM PDU 立即传输的循环时间，以秒为单位。 (Defines the cycle time, in seconds, for CanNmImmediateNmTransmissions NM PDU immediate transmission.)
     - \
     - \
   * - \
     - 依赖关系 (Dependencies)
     - 此参数仅在以下情况下有效CanNmImmediateNmTransmissions>1。 (This parameter is only valid if CanNmImmediateNmTransmissions>1.)
     - \
     - \
   * - \
     - 取值范围 (Value range)
     - 0..255
     - 默认取值 (Default value)
     - 无 (none)
   * - \
     - 参数描述 (Parameter description)
     - 定义应立即传输的NM   PDU的数量。如果该值为零，则不会立即发送   NM PDU。立即传输   NM PDU 的循环时间由   CanNmImmediateNmCycleTime 定义。 (Defines the number of NM PDUs that should be transmitted immediately.If the value is zero, the NM PDU is not sent immediately.The cycle time for immediate transmission of NM PDUs is defined by CanNmImmediateNmCycleTime.)
     - \
     - \
   * - CanNmImmediateNmTransmissions
     - \
     - 如果   CanNmImmediateRestartEnabled = true 那么 (if CanNmImmediateRestartEnabled = true then)
     - \
     - \
   * - \
     - 依赖关系 (Dependencies)
     - CanNmImmediateNmTransmissions   = 0如果   CanNmPnHandleMultipleNetworkRequests == True" 那么 (CanNmImmediateNmTransmissions = 0 if CanNmPnHandleMultipleNetworkRequests == True" then)
     - \
     - \
   * - \
     - \
     - "CanNmImmediateNmTransmissions   > 0
     - \
     - \
   * - \
     - 取值范围 (Value range)
     - 0~65.535
     - 默认取值 (Default value)
     - 无 (none)
   * - CanNmMsgCycleOffset
     - 参数描述 (Parameter description)
     - 周期性传输节点中的时间偏移。它决定了传输的启动延迟。以秒为单位指定 (Time offset in periodic transmission nodes.It determines the startup delay of the transfer.Specified in seconds)
     - \
     - \
   * - \
     - 依赖关系 (Dependencies)
     - 参数值<CanMsgCycleTime此参数仅在CanNmPassiveModeEnabled为False时有效 (Parameter value <CanMsgCycleTime This parameter is only valid when CanNmPassiveModeEnabled is False)
     - \
     - \
   * - \
     - 取值范围 (Value range)
     - 0.001~65.535
     - 默认取值 (Default value)
     - 无 (none)
   * - CanNmMsgCycleTime
     - 参数描述 (Parameter description)
     - NM   PDU的周期以秒为单位。它确定周期性速率，并且是传输调度的基础。 (The period of NM PDU is in seconds.It determines the periodic rate and is the basis for transmission scheduling.)
     - \
     - \
   * - \
     - 依赖关系 (Dependencies)
     - 当“CanNmPassiveModeEnabled”为“False”时，此参数才有效。 (This parameter is only valid when "CanNmPassiveModeEnabled" is "False".)
     - \
     - \
   * - \
     - 取值范围 (Value range)
     - 0.001~65.535
     - 默认取值 (Default value)
     - 无 (none)
   * - \
     - 参数描述 (Parameter description)
     - 减负载的周期传输时间，以秒为单位。 (Cycle transfer time for load shedding, in seconds.)
     - \
     - \
   * - \
     - \
     - 0,5 * CanNmMsgCycleTime ≤   CanNmMsgReducedTime < CanNmMsgCycleTime
     - \
     - \
   * - CanNmMsgReducedTime
     - \
     - 此参数仅在以下情况下有效 (This parameter is only valid when)
     - \
     - \
   * - \
     - 依赖关系· (Dependencies ·)
     - CanNmBusLoadReductionEnabled ==   True 和CanNmBusLoadReductionActive == True   和 (CanNmBusLoadReductionEnabled == True and CanNmBusLoadReductionActive == True and)
     - \
     - \
   * - \
     - \
     - CanNmPassiveModeEnabled == False
     - \
     - \
   * - \
     - \
     - 否则不使用此参数。 (Otherwise this parameter is not used.)
     - \
     - \
   * - \
     - 取值范围 (Value range)
     - 0.001~65.535
     - 默认取值 (Default value)
     - 无 (none)
   * - \
     - 参数描述 (Parameter description)
     - 当使用部分网络并定义此超时时，CanNm   会监控   NM-PDU 在此传输超时时间内成功传输，否则提供错误通知。 (When using a partial network and defining this timeout, CanNm monitors for successful transmission of NM-PDUs within this transmission timeout and provides an error notification otherwise.)
     - \
     - \
   * - \
     - 依赖关系 (Dependencies)
     - CanNmMsgTimeoutTime   < CanNmMsgCycleTime此参数仅在   CanNmPassiveModeEnabled 和 CanNmImmediateTxConfEnabled   设置为   FALSE 且   CanNmPnEnabled 设置为 TRUE 时有效。 (CanNmMsgTimeoutTime < CanNmMsgCycleTime This parameter is only valid when CanNmPassiveModeEnabled and CanNmImmediateTxConfEnabled are set to FALSE and CanNmPnEnabled is set to TRUE.)
     - \
     - \
   * - \
     - 取值范围 (Value range)
     - FSLSE/TRUE
     - 默认 (default)
     - 无 (none)
   * - \
     - 参数描述 (Parameter description)
     - 是否使能节点检测功能 (Whether to enable node detection function)
     - \
     - \
   * - \
     - 依赖关系 (Dependencies)
     - 仅当CanNmNodeIdEnabled设置为TRUE时有效如果CanNmPassiveModeEnabled==True，则CanNmNodeDetectionEnabled=False (Only valid when CanNmNodeIdEnabled is set to TRUE If CanNmPassiveModeEnabled==True, then CanNmNodeDetectionEnabled=False)
     - \
     - \
   * - \
     - 取值范围 (Value range)
     - 0~255
     - 默认取值 (Default value)
     - 无 (none)
   * - CanNmNodeId
     - 参数描述 (Parameter description)
     - 本地节点标志符 (local node identifier)
     - \
     - \
   * - \
     - 依赖关系 (Dependencies)
     - 此参数仅在   CanNmNodeIdEnabled == True 时有效 (This parameter is only valid when CanNmNodeIdEnabled == True)
     - \
     - \
   * - CanNmNodeIdEnabled
     - 取值范围 (Value range)
     - true,   false
     - 默认取值 (Default value)
     - true
   * - \
     - 参数描述 (Parameter description)
     - 用于启用源节点标识符的预处理器开关。 (Preprocessor switch to enable source node identifiers.)
     - \
     - \
   * - \
     - 依赖关系 (Dependencies)
     - Equal(NmNodeIdEnabled)
     - \
     - \
   * - \
     - \
     - CANNM_PDU_BYTE_0
     - \
     - \
   * - \
     - 取值范围 (Value range)
     - CANNM_PDU_BYTE_1
     - 默认取值 (Default value)
     - 无 (none)
   * - \
     - \
     - CANNM_PDU_OFF
     - \
     - \
   * - CanNmPduCbvPosition
     - 参数描述 (Parameter description)
     - 定义NM   PDU内控制位向量的位置。参数的值表示NM   PDU中控制位向量的位置（CanNmPduByte0表示字节0，CanNmPduByte1表示字节1，CanNmPduOff表示源节点标识符不是NM   PDU的一部分）
     - \
     - \
   * - \
     - \
     - 如果CanNmNodeDetectionEnabled==   true，那么CanNmPduCbvPosition！=   CANNM_PDU_OFF (If CanNmNodeDetectionEnabled== true, then CanNmPduCbvPosition!= CANNM_PDU_OFF)
     - \
     - \
   * - \
     - 依赖关系 (Dependencies)
     - 如果（CANNM_PDU_CBV_POSITION！=   CANNM_PDU_OFF&&CANNM_PDU_NID_POSITION！=   CANNM_PDU_OFF）则CANNM_PDU_CBV_POSITION！=   CANNM_PDU_NID_POSITION
     - \
     - \
   * - \
     - \
     - 如果（CANNM_PDU_CBV_POSITION！=   CANNM_PDU_OFF&&CANNM_PDU_NID_POSITION==CANNM_PDU_OFF）则CANNM_PDU_CBV_POSITION=CANNM_PDU_BYTE0
     - \
     - \
   * - \
     - \
     - CANNM_PDU_BYTE_0
     - \
     - \
   * - \
     - 取值范围 (Value range)
     - CANNM_PDU_BYTE_1
     - 默认取值 (Default value)
     - 无 (none)
   * - \
     - \
     - CANNM_PDU_OFF
     - \
     - \
   * - CanNmPduNidPosition
     - 参数描述 (Parameter description)
     - 定义NM   PDU中源节点标识的位置。该参数的值表示NM   PDU中源节点标识的位置 (Defines the position of the source node identifier in the NM PDU.The value of this parameter indicates the position of the source node identifier in the NM PDU.)
     - \
     - \
   * - \
     - \
     - 如果CanNmNodeIdEnabled==   true，那么CanNmPduNidPosition！=   CANNM_PDU_OFF (If CanNmNodeIdEnabled== true, then CanNmPduNidPosition!= CANNM_PDU_OFF)
     - \
     - \
   * - \
     - 依赖关系 (Dependencies)
     - 如果（CANNM_PDU_NID_POSITION！=   CANNM_PDU_OFF&& CANNM_PDU_CBV_POSITION！=   CANNM_PDU_OFF）则CANNM_PDU_NID_POSITION！=   CANNM_PDU_CBV_POSITION
     - \
     - \
   * - \
     - \
     - 如果（CANNM_PDU_NID_POSITION！=   CANNM_PDU_OFF&& CANNM_PDU_CBV_POSITION== CANNM_PDU_OFF）则CANNM_PDU_NID_POSITION=   CANNM_PDU_BYTE0
     - \
     - \
   * - \
     - 取值范围 (Value range)
     - STD_ON,STD_OFF
     - 默认取值 (Default value)
     - 无 (none)
   * - CanNmPnEnabled
     - 参数描述 (Parameter description)
     - 使能或者禁用PN (Enable or disable PN)
     - \
     - \
   * - \
     - 依赖关系 (Dependencies)
     - 仅当   CanNmGlobalPnSupport == true 时有效,同时需要配置CanNmPnInfo (Only valid when CanNmGlobalPnSupport == true, and CanNmPnInfo needs to be configured.)
     - \
     - \
   * - \
     - 取值范围 (Value range)
     - STD_ON,STD_OFF
     - 默认取值 (Default value)
     - FALSE
   * - CanNmPnEraCalcEnabled
     - 参数描述 (Parameter description)
     - 指定CanNm是否计算外部请求的PN请求信息 (Specifies whether CanNm calculates PN request information for external requests)
     - \
     - \
   * - \
     - 依赖关系 (Dependencies)
     - 仅当   CanNmGlobalPnSupport == true 时有效 (Only valid when CanNmGlobalPnSupport == true)
     - \
     - \
   * - \
     - 取值范围 (Value range)
     - STD_ON,STD_OFF
     - 默认取值 (Default value)
     - FALSE
   * - CanNmPnHandleMultipleNetworkRequests
     - 参数描述 (Parameter description)
     - 指定CanNm是否执行从网络模式到重复消息状态（true）或不（false）的附加转换
     - \
     - \
   * - \
     - 依赖关系 (Dependencies)
     - 仅当   CanNmGlobalPnSupport == true 时有效 (Only valid when CanNmGlobalPnSupport == true)
     - \
     - \
   * - \
     - 取值范围 (Value range)
     - 0.001~65.535
     - 默认取值 (Default value)
     - 无 (none)
   * - CanNmRemoteSleepIndTime
     - 参数描述 (Parameter description)
     - 远程睡眠指示超时。它定义了需要多长时间才能识别所有其他节点已准备好进入睡眠状态 (Remote sleep indication timed out.It defines how long it takes to recognize that all other nodes are ready to sleep)
     - \
     - \
   * - \
     - 依赖关系 (Dependencies)
     - CanNmRemoteSleepIndTime≥   CanNmMsgCycleTime且CanNmRemoteSleepIndTime仅在CanNmRemoteSleepIndEnabled   = true时是必需的 (CanNmRemoteSleepIndTime ≥ CanNmMsgCycleTime and CanNmRemoteSleepIndTime is only required if CanNmRemoteSleepIndEnabled = true)
     - \
     - \
   * - \
     - 取值范围 (Value range)
     - 0~65.535
     - 默认取值 (Default value)
     - 无 (none)
   * - \
     - 参数描述 (Parameter description)
     - 重复消息状态超时。它以秒为单位定义了NM应该停留在重复消息状态的时间 (Duplicate message status timeout.It defines how long in seconds the NM should stay in duplicate message state)
     - \
     - \
   * - \
     - 依赖关系 (Dependencies)
     - CanNmRepeatMessageTime=n*CanNmMsgCycleTime;CanNmRepeatMessageTime>CanNmImmediateNmTransmissions   \*CanNmImmediateNmCycleTime
     - \
     - \
   * - \
     - 取值范围 (Value range)
     - FALSE/TRUE
     - 默认取值 (Default value)
     - 无 (none)
   * - CanNmRepeatMsgIndEnabled
     - 参数描述 (Parameter description)
     - 是否使能RepeatMessageRequest位已被收到的通知 (Whether to enable notification that the RepeatMessageRequest bit has been received)
     - \
     - \
   * - \
     - 依赖关系 (Dependencies)
     - 计算公式=如果（CanNmPassiveModeEnabled==False）则等于（NmRepeatMsgIndEnabled）否则等于（False）
     - \
     - \
   * - \
     - 取值范围 (Value range)
     - STD_ON,STD_OFF
     - 默认取值 (Default value)
     - 无 (none)
   * - CanNmStayInPbsEnabled
     - 参数描述 (Parameter description)
     - 如果禁用此参数，则在   CanNmWaitBusSleepTime 后离开Prepare Bus-Sleep 模式。如果启用此参数，则只有在   ECU 断电或任何重新启动原因适用时才能离开   Prepare BusSleep 模式。 (If this parameter is disabled, Prepare Bus-Sleep mode is left after CanNmWaitBusSleepTime.If this parameter is enabled, Prepare BusSleep mode can only be left when the ECU is powered off or any restart reason applies.)
     - \
     - \
   * - \
     - 取值范围 (Value range)
     - 0.002~65.535
     - 默认取值 (Default value)
     - 无 (none)
   * - \
     - \
     - NM   PDU的网络超时。它表示在转换到 (Network timeout for NM PDU.It means that when converting to)
     - \
     - \
   * - CanNmTimeoutTime
     - 参数描述 (Parameter description)
     - Prepare Bus-Sleep 模式启动之前，NM需要停留在 (Before the Prepare Bus-Sleep mode is started, the NM needs to stay in)
     - \
     - \
   * - \
     - \
     - ReadySleep状态的时间 (ReadySleep state time)
     - \
     - \
   * - \
     - 依赖关系 (Dependencies)
     - CanNmTimeoutTime >   CanNmMsgCycleTime
     - \
     - \
   * - \
     - 取值范围 (Value range)
     - 0.001~65.535
     - 默认取值 (Default value)
     - 无 (none)
   * - CanNmWaitBusSleepTime
     - 参数描述 (Parameter description)
     - 表示在转换到总线休眠模式之前，NM应停留在准备总线休眠模式的时间，以秒为单位 (Indicates the time, in seconds, that the NM should stay in ready bus sleep mode before transitioning to bus sleep mode.)
     - \
     - \
   * - \
     - 依赖关系 (Dependencies)
     - 它应该对群集中的所有节点都是相等的。它应该足够长，使所有Tx缓冲区都为空，如果   CanNmStayInPbsEnabled 被禁用，这个参数应该是强制性的。 (它应该对群集中的所有节点都是相等的。It should be long enough so that all Tx buffers are empty, this parameter should be mandatory if CanNmStayInPbsEnabled is disabled.)
     - \
     - \
   * - \
     - 取值范围 (Value range)
     - Reference to [ ComMChannel ]
     - 默认取值 (Default value)
     - 无 (none)
   * - CanNmComMNetworkHandleRef
     - 参数描述 (Parameter description)
     - 此引用指向由ComMChannel定义的唯一通道，并提供对ComMChannelId中唯一通道索引值的访问 (This reference points to the unique channel defined by ComMChannel and provides access to the unique channel index value in ComMChannelId)
     - \
     - \
   * - \
     - 依赖关系 (Dependencies)
     - 无 (none)
     - \
     - \
   * - \
     - 取值范围 (Value range)
     - Reference to [ Pdu ]
     - 默认取值 (Default value)
     - 无 (none)
   * - CanNmPnEraRxNSduRef
     - 参数描述 (Parameter description)
     - 参考COM堆栈中的Pdu。每个CanNm通道都需要SduRef，因为每个channel都会报告ERA (Refer to Pdu in COM stack.SduRef is required for each CanNm channel because each channel reports ERA)
     - \
     - \
   * - \
     - 依赖关系 (Dependencies)
     - 仅当   CanNmPnEraCalcEnabled == true 时有效，引用的PDU需要在PDUR中进行关联 (Only valid when CanNmPnEraCalcEnabled == true, the referenced PDU needs to be associated in the PDUR)
     - \
     - \
         
         

CanNmRxPdu
--------------------------

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/CanNm/image8.png
   :alt: CanNmRxPdu容器配置图(CanNmRxPdu container configuration diagram)
   :name: CanNmRxPdu容器配置图(CanNmRxPdu container configuration diagram)
   :align: center

.. centered:: **表  CanNmRxPdu属性描述 (Table CanNmRxPdu attribute description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI name)
     - 描述 (describe)
     - \
     - \
     - \
   * - CanNmRxPduId
     - 取值范围 (Value range)
     - 0 .. 65535
     - 默认取值 (Default value)
     - CANNM_RX_PDU_index(x)
   * - \
     - 参数描述 (Parameter description)
     - 此参数定义与此CanNm 通道关联的CanIf L-PDU 范围的Rx PDU ID。 (This parameter defines the Rx PDU ID of the CanIf L-PDU range associated with this CanNm channel.)
     - \
     - \
   * - \
     - 依赖关系 (Dependencies)
     - 配置的PDU顺序 (Configured PDU sequence)
     - \
     - \
   * - CanNmRxPduRef
     - 取值范围 (Value range)
     - Reference to [ Pdu]
     - 默认取值 (Default value)
     - 无 (none)
   * - \
     - 参数描述 (Parameter description)
     - 对此 CanNm通道使用的全局 PDU的引用。 (A reference to the global PDU used by this CanNm channel.)
     - \
     - \
   * - \
     - 依赖关系 (Dependencies)
     - 依赖于ECUC里面配置的PDU,与CanNmTxPduRef、CanNmTxUserDataPduRef不能相同 (Depends on the PDU configured in ECUC, which cannot be the same as CanNmTxPduRef and CanNmTxUserDataPduRef.)
     - \
     - \
         
         

CanNmTxPdu
--------------------------

仅当 CanNmPassiveModeEnabled 为 false 时，此容器的配置有效。

This container's configuration is only valid when CanNmPassiveModeEnabled is false.

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/CanNm/image9.png
   :alt: CanNmTxPdu容器配置图(CanNmTxPdu container configuration diagram)
   :name: CanNmTxPdu容器配置图(CanNmTxPdu container configuration diagram)
   :align: center

.. centered:: **表  CanNmTxPdu属性描述 (Table CanNmTxPdu attribute description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI name)
     - 描述 (describe)
     - \
     - \
     - \
   * - CanNmTxConfirmationPduId
     - 取值范围 (Value range)
     - 0 .. 65535
     - 默认取值 (Default value)
     - CANNM_TX_PDU_index(x)
   * - \
     - 参数描述 (Parameter description)
     - 下层的TxConfirmation使用的TxPdu的ID。 (The ID of the TxPdu used by the underlying TxConfirmation.)
     - \
     - \
   * - \
     - 依赖关系 (Dependencies)
     - 配置的PDU顺序 (Configured PDU sequence)
     - \
     - \
   * - CanNmTxPduRef
     - 取值范围 (Value range)
     - Reference to [ Pdu]
     - 默认取值 (Default value)
     - 无 (none)
   * - \
     - 参数描述 (Parameter description)
     - 引用AUTOSARECU配置规范中描述的全局PDU结构中的PDU。CanNm模块将使用此参考来导出PDUID。 (References the PDU in the global PDU structure described in the AUTOSARECU configuration specification.The CanNm module will use this reference to export the PDUID.)
     - \
     - \
   * - \
     - 依赖关系 (Dependencies)
     - 依赖于ECUC里面配置的PDU，与CanNmRxPduRef、CanNmTxUserDataPduRef不能相同 (Depends on the PDU configured in ECUC, which cannot be the same as CanNmRxPduRef and CanNmTxUserDataPduRef.)
     - \
     - \
         
         

CanNmUserDataTxPdu
----------------------------------

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/CanNm/image10.png
   :alt: CanNmUserDataTxPdu容器配置图(CanNmUserDataTxPdu container configuration diagram)
   :name: CanNmUserDataTxPdu容器配置图(CanNmUserDataTxPdu container configuration diagram)
   :align: center

.. centered:: **表 CanNmUserDataTxPdu属性描述 (Table CanNmUserDataTxPdu attribute description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI name)
     - 描述 (describe)
     - \
     - \
     - \
   * - CanNmTxUserDataPduId
     - 取值范围 (Value range)
     - 0 .. 65535
     - 默认取值 (Default value)
     - CANNM_USER_TX\_PDU_index(x)
   * - \
     - 参数描述 (Parameter description)
     - 此参数定义NM用户数据I-PDU的HandleID。 (This parameter defines the HandleID of the NM user data I-PDU.)
     - \
     - \
   * - \
     - 依赖关系 (Dependencies)
     - 配置的PDU顺序 (Configured PDU sequence)
     - \
     - \
   * - CanNmTxUserDataPduRef
     - 取值范围 (Value range)
     - Reference to [ Pdu]
     - 默认取值 (Default value)
     - 无 (none)
   * - \
     - 参数描述 (Parameter description)
     - 在全局PDU集合中引用NMUser Data I-PDU。 (Reference the NMUser Data I-PDU in the global PDU collection.)
     - \
     - \
   * - \
     - 依赖关系 (Dependencies)
     - 依赖于ECUC里面配置的PDU，与CanNmRxPduRef、CanNmTxPduRef不能相同,该PDU需要在PDUR模块中有引用 (Depends on the PDU configured in ECUC, which cannot be the same as CanNmRxPduRef and CanNmTxPduRef. This PDU needs to be referenced in the PDUR module)
     - \
     - \
         

CanNmPnInfo
===========================

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/CanNm/image11.png
   :alt: CanNmPnInfo容器配置图(CanNmPnInfo container configuration diagram)
   :name: CanNmPnInfo容器配置图(CanNmPnInfo container configuration diagram)
   :align: center

.. centered:: **表 CanNmPnInfo属性描述 (Table CanNmPnInfo property description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI name)
     - 描述 (describe)
     - \
     - \
     - \
   * - CanNmPnInfoLength
     - 取值范围 (Value range)
     - 1 .. 7
     - 默认取值 (Default value)
     - 无 (none)
   * - \
     - 参数描述 (Parameter description)
     - 指定NM消息中PN请求信息的长度。 (Specifies the length of the PN request information in the NM message.)
     - \
     - \
   * - \
     - 依赖关系 (Dependencies)
     - 仅当CanNmGlobalPnSupport== true 时有效 (Only valid when CanNmGlobalPnSupport== true)
     - \
     - \
   * - CanNmPnInfoOffset
     - 取值范围 (Value range)
     - 1 .. 7
     - 默认取值 (Default value)
     - 无 (none)
   * - \
     - 参数描述 (Parameter description)
     - 指定NM消息中PN请求信息的偏移量。 (Specifies the offset of the PN request information in the NM message.)
     - \
     - \
   * - \
     - 依赖关系 (Dependencies)
     - 仅当CanNmGlobalPnSupport== true 时有效 (Only valid when CanNmGlobalPnSupport== true)
     - \
     - \
         

CanNmPnFilterMaskByte
--------------------------------------

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/CanNm/image12.png
   :alt: CanNmPnFilterMaskByte容器配置图(CanNmPnFilterMaskByte container configuration diagram)
   :name: CanNmPnFilterMaskByte容器配置图(CanNmPnFilterMaskByte container configuration diagram)
   :align: center

.. centered:: **表 CanNmPnFilterMaskByte属性描述 (Table CanNmPnFilterMaskByte property description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI name)
     - 描述 (describe)
     - \
     - \
     - \
   * - CanNmPnFilterMaskByteIndex
     - 取值范围 (Value range)
     - 0 .. 6
     - 默认取值 (Default value)
     - 无 (none)
   * - \
     - 参数描述 (Parameter description)
     - 过滤掩码字节的索引。指定过滤掩码字节数组中的位置 (Index of filter mask bytes.Specifies the position in the filter mask byte array)
     - \
     - \
   * - \
     - 依赖关系 (Dependencies)
     - 仅当CanNmGlobalPnSupport== true时有效CanNmPnFilterMaskByteIndex<CanNmPnInfoLength (Only valid when CanNmGlobalPnSupport== trueCanNmPnFilterMaskByteIndex<CanNmPnInfoLength)
     - \
     - \
   * - CanNmPnFilterMaskByteValue
     - 取值范围 (Value range)
     - 0 .. 255
     - 默认取值 (Default value)
     - 无 (none)
   * - \
     - 参数描述 (Parameter description)
     - 用于配置过滤掩码字节的参数。 (Parameters used to configure filter mask bytes.)
     - \
     - \
   * - \
     - 依赖关系 (Dependencies)
     - 仅当CanNmGlobalPnSupport== true 时有效 (Only valid when CanNmGlobalPnSupport== true)
     - \
     - \
