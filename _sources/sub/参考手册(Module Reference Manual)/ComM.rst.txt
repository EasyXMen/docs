ComM
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
     - 应用程序接口 (Application Programming Interface)
   * - BswM
     - Basic Software Manager
     - 基础软件管理模块 (Basic Software Management Module)
   * - BusSM
     - Bus State Manger
     - 与总线相关的状态管理模块 (State management module related to the bus)
   * - CanSM
     - Can State Manger
     - Can总线状态管理模块 (CAN Bus Status Management Module)
   * - DET
     - Default Error Tracer
     - 默认错误检测模块 (Default error detection module)
   * - NM
     - Network Management
     - 网络管理 (Network Management)
   * - PDU
     - Protocol Data Unit
     - 协议数据单元 (Protocol Data Unit)
   * - PN
     - Partial Network
     - 部分网络 (Part of the network)
   * - PNC
     - Partial Network Cluster
     - 部分网络集群 (Part of Network Clusters)
   * - ERA
     - External Request Array
     - 外部请求集合 (External Request Collection)
   * - EIRA
     - External and InternalRequest Array
     - 外部和内部请求集合 (External and internal request collections)
   * - ComM
     - Communication Manager
     - 通讯管理模块 (Communication Management Module)
   * - DCM
     - Diagnostic CommunicationManager
     - 诊断通讯管理模块 (Diagnostic Communication Management Module)
   * - BusNm
     - Bus Network Management
     - 与总线相关的网络管理模块 (Network management module related to buses)
   * - NvM
     - Non-Volatile Manager
     - 非易失性管理器 (Non-volatile Manager)




简介 (Introduction)
=================================

ComM（COM Manage，通信管理）模块是一个资源管理器，它封装了对基础通信服务的控制。ComM模块控制与通信相关的基础软件模块，它收集来自通信请求者的总线通信访问请求，并进行协调。

ComM (COM Manage, Communication Management) module is a resource manager that encapsulates the control of fundamental communication services. The ComM module controls basic software modules related to communication; it collects bus communication access requests from communication requestors and coordinates them.

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/ComM/image1.png
   :alt: ComM在AUTOSAR中的位置 (The position of ComM in AUTOSAR)
   :name: ComM在AUTOSAR中的位置 (The position of ComM in AUTOSAR)
   :align: center


ComM模块的目的是：

The purpose of the ComM module is:

为用户简化总线通信栈的使用，包括简化的网络管理处理。

To simplify the use of the bus communication stack for users, including simplified network management processing.

协调一个ECU上多个独立软件组件的总线通信栈的可用性(允许发送和接收信号)。

Ensure the availability of bus communication stacks on an ECU for multiple independent software components (enabling sending and receiving signals).

提供一个API来禁用发送信号，以防止ECU(主动地)唤醒通信总线。

Provide an API to disable sending signals to prevent the ECU (actively) from waking up the communication bus.

通过为每个通道实现通道状态机来控制ECU的多个通信总线通道。

Control multiple communication bus channels of the ECU by implementing channel state machines for each channel.

提供迫使ECU保持总线唤醒的“无通讯”模式的可能性。

Provide the possibility of forcing the ECU to maintain bus wake-up in "no communication" mode.

通过分配请求的通信模式所需的所有资源来简化资源管理。

Simplify resource management by allocating all resources required for the communication mode requested.

参考资料 (Reference materials)
------------------------------------------

[1] AUTOSAR_SWS_COMManager.pdf

[2] AUTOSAR_SWS_NetworkManagementInterface.pdf

[3] AUTOSAR_SWS_BSWModeManager.pdf

[4] AUTOSAR_SWS_ECUStateManager.pdf

[5] AUTOSAR_SWS_DiagnosticCommunicationManager.pdf

[6] AUTOSAR_SWS_COM.pdf

功能描述 (Function Description)
===========================================

Channel与PNC状态管理功能 (Channel and PNC Status Management Function)
------------------------------------------------------------------------------

AUTOSAR中，通过ComM系统服务实现对通信状态的管理。用户上电唤醒时通过主动请求通信FULL_COMMUNICATION或被动唤醒通知，用户休眠时请求NO_COMMUNICATION释放通信，ComM接收到请求后通过相应总线的SM模块和NM模块实现对总线通信状态的切换。用户无需再与各个通信总线的状态管理模块和网络管理模块进行交互。一个用户可以对应多个通道和多个PNC。当用户请求FULL_COMMUNICATION来请求通信时，该用户对应的所有channel和PNC都需要切换为FULL_COMMUNICATION的状态。在发生被动唤醒时，例如由ECUM发出的唤醒请求或者由网络管理模块发出的重启通信请求，对应的channel和PNC需要切换为FULL_COMMUNICATION的状态。ComM为每个channel和每个PNC都提供一个独立的状态机。

In AUTOSAR, the ComM system services are used to manage communication status. When users are powered on and awakened, they can request FULL_COMMUNICATION actively or receive passive wake-up notifications. During user dormancy, they request NO_COMMUNICATION to release communication. Upon receiving these requests, ComM switches the bus communication state through corresponding SM and NM modules. Users no longer need to interact with individual communication bus status management modules and network management modules. A single user can correspond to multiple channels and PNCs. When a user requests FULL_COMMUNICATION, all associated channels and PNCs must switch to this state. In passive wake-up scenarios, such as when woken up by ECUM or when a restart communication request is issued by the network management module, corresponding channels and PNCs need to change to the FULL_COMMUNICATION state. ComM provides an independent state machine for each channel and each PNC.

ComM模块实现了PNC(局域网络集群)管理功能，在ComM中可配置PNC，并且该PNC可以被通道和用户所引用，每个PNC在总线上使用NM用户数据中位向量中的专用位位置。如果节点上的本地ComM用户请求了PNC，则该节点会将NM用户数据中的相应位设置为1。如果不再请求PNC，节点将NM用户数据中的相应位设置为0。BusNm收集并聚集PNC的NM用户数据，并通过以下方式提供状态：通过COM信号向ComM发送COM位向量。ComM通过信号的内容，更新PNC状态机的状态。

The ComM module implements the PNC (Local Network Cluster) management function. In ComM, PNC can be configured and referenced by channels and users. Each PNC uses a dedicated bit position in the NM user data middle vector on the bus. If a local ComM user on the node requests a PNC, the node sets the corresponding bit in the NM user data to 1. If the request for PNC is no longer needed, the node sets the corresponding bit to 0. BusNm collects and aggregates the NM user data of PNCs and provides status through the following method: by sending COM位向量 via the COM signal to ComM. ComM updates the state of the PNC state machine based on the content of the signal.

PNC可以设置为网关类型和非网关类型，网关类型主要用于当局域网连接到一个以上的通道时，需要进行协调，通道可以配置为Active（主动）类型和Passive（被动）类型，Passive类型存在于当被动协调通道连接到多个PNC网关。如果启用了ComM的PNC网关功能（ComMPNCGatewayEnabled =true）可以将映射到此网关的ComM通道设置为主动或被动类型（COMM_GATEWAY_TYPE_ACTIVE或COMM_GATEWAY_TYPE_PASSIVE）。如果ComM通道映射到两个不同的PNC网关，则只有一个网关主动协调此通道，而另一个则被动协调。这意味着，PNC网关始终映射到至少一个ComM通道类型为主动，并且可以映射到一个或多个ComM通道类型为被动。当PNC只要有一个Active通道收到ERA中为请求，则Passive通道发送当前PNC为请求的Nm Pdu；当前Gateway 的PNC中所有Active通道收到ERA标识PNC为释放状态，发送当前PNC为释放的Nm Pdu；这种表现可以简单理解为Gateway 从Active 通道向Passive转发ERA PNC信息。

PNC can be set as gateway type and non-gateway type. Gateway type is mainly used when a local network connects to more than one channel, requiring coordination. Channels can be configured as Active (active) types and Passive (passive) types. Passive type exists when a passive coordinated channel is connected to multiple PNC gateways. If the ComM PNC gateway function is enabled (ComMPNCGatewayEnabled = true), the ComM channels mapped to this gateway can be set as active or passive types (COMM_GATEWAY_TYPE_ACTIVE or COMM_GATEWAY_TYPE_PASSIVE). If a ComM channel is mapped to two different PNC gateways, only one gateway actively coordinates this channel while the other passively coordinates. This means that PNC gateways always map to at least one ComM channel type as active and can map to one or more ComM channels types as passive. When PNC has at least one Active channel receiving an ERA request for a PDU, Passive channels send current PNC requests for Nm PDUs; when all Active channels in the current Gateway PNC receive an ERA indicating that PNC is in release state, they send current PNC releases for Nm PDUs; this behavior can be simply understood as the Gateway actively forwarding ERA information from active channels to passive ones.

Channel状态机 (Channel State Machine)
==================================================

ComM为每个通道都实现了一个状态机，ComM通道有三个主要状态，分别为COMM_NO_COMMUNICATION、COMM_SILENT_COMMUNICATION、COMM_FULL_COMMUNICATION，其中COMM_SILENT_COMMUNICATION状态用于网络管理内部状态同步，用户不可请求。COMM_NO_COMMUNICATI-

CommM implements a state machine for each channel. CommM channels have three main states: COMM_NO_COMMUNICATION, COMM_SILENT_COMMUNICATION, and COMM_FULL_COMMUNICATION.其中COMM_SILENT_COMMUNICATION state is used for internal state synchronization in network management and is not requestable by users. COMM_NO CommunICATI-

ON内部包含COMM_NO_COM_NO_PENDING_REQUEST和COMM_NO_CO-

ON contains COMM_NO_COM_NO_PENDING_REQUEST and COMM_NO_CO-

M_REQUEST_PENDING两个子状态，COMM_FULL_COMMUNICATION内部包含COMM_FULL_COM_NETWORK_REQUESTED和COMM_FULL_COM\_-

Two sub-states, M_REQUEST_PENDING, with COMM_FULL_COMMUNICATION containing COMM_FULL_COM_NETWORK_REQUESTED and COMM_FULL_COM-_-_

READY_SLEEP两个子状态。ComM通道状态机如下图所示。

READY_SLEEP two sub-states. ComM channel state machine is shown as follows.

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/ComM/image2.png
   :alt: ComM通道状态机 (Comm Channel State Machine)
   :name: ComM通道状态机 (Comm Channel State Machine)
   :align: center

PNC状态机 (PNC State Machine)
==========================================

ComM为每个PNC（局域网集群）实现一个状态机，每个PNC都有其自己的状态，通过配置映射，PNC的状态与channel的状态有关。ComM用户可以请求和释放PNC，系统通道节点上所有PNC的状态通过网络管理报文进行交换。每个PNC在总线上使用网络管理报文用户数据中位向量中的专用位位置。如果该节点上的本地ComM用户请求了PNC，则该节点会将网络管理用户数据中的相应位设置为1。如果该PNC不再被请求，节点将网络管理用户数据中的相应位设置为0。BusNm收集并聚合PNC的网络管理用户数据，并通过COM位向量通过COM信号将状态提供给ComM。

ComM implements a state machine for each PNC (Local Area Network Cluster), and each PNC has its own state. Through configuration mapping, the state of a PNC is related to the channel's state. ComM users can request and release PNCs; the states of all PNCs on the system channel nodes are exchanged via network management messages. Each PNC uses a dedicated bit position in the user data field of network management messages for its presence on the bus. If a local ComM user requests a PNC at that node, the node sets the corresponding bit in the network management user data to 1. If the PNC is no longer requested, the node sets the corresponding bit in the network management user data to 0. BusNm collects and aggregates the network management user data of PNCs and provides the state via the COM bit vector through COM signals to ComM.

在每个系统通道上，每个PNC在网络管理用户数据中使用相同的位位置。ComM使用两种类型的位向量EIRA和ERA进行PNC状态信息交换。EIRA体现了当前节点与网络上其他节点对某一个PNC的请求与释放情况；EIRA不区分物理通道，只针对不同的PN，ERA则是在网关节点才使用，用于表示不同的通道对Pn的外部请求。ComM PNC有两个主要状态，分别为COMM_PNC_NO_C-

On each system channel, every PNC uses the same bit position in the network management user data. ComM utilizes two types of bit vectors, EIRA and ERA, for exchanging PNC status information. EIRA represents the current node's request and release conditions regarding a specific PNC with other nodes on the network; it does not differentiate physical channels but targets different PN instead. ERA is used only at gateway nodes to indicate external requests for different channels pertaining to Pn. ComM PNC has two primary states, namely COMM_PNC_NO_C-

OMMUNICATION、COMM_PNC_FULL_COMMUNICATION。COMM_PNC_F-

ULL_COMMUNICATION 内部有COMM_PNC_PREPARE_SLEEP，COMM_P-

ULL_COMMUNICATION includes COMM_PNC_PREPARE_SLEEP, COMM_P-

NC_READY_SLEEP和COMM_PNC_REQUESTED三个子状态。ComM PNC的状态机如下图所示。

NC_READY_SLEEP and COMM_PNC_REQUESTED three sub-states. ComM PNC's state machine is shown in the following figure.

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/ComM/image3.png
   :alt: ComM PNC状态机 (Comm PNC State Machine)
   :name: ComM PNC状态机 (Comm PNC State Machine)
   :align: center


注：当前版本使用 Nm_UpdateIRA 接口替代 Com_SendSignal 进行 IRA 的更新。

Note: The current version uses the Nm_UpdateIRA interface to replace Com_SendSignal for updating IRA.

功能抑制 (Function inhibition)
------------------------------------------

功能抑制是ComM中的扩展功能，ComM释放了功能抑制的接口与配置，功能抑制以通道为单位，各通道内的功能抑制相互独立。功能抑制分为唤醒抑制与无通信抑制。

Functional inhibition is an extended feature of ComM, which releases the interfaces and configurations for functional inhibition. Functional inhibition operates on a channel basis, with each channel's functional inhibition being independent from others. It is divided into wake-up inhibition and no-communication inhibition.

唤醒抑制：表现为通道处于COMM_NO_COMMUNICATION或COMM_SILENT_COMMUNICATION状态时忽略User对通道的FULL_COMMUNICATION请求，但通道的被动唤醒功能不受影响，当全局配置项打开的情况下，唤醒抑制可以通过API来控制。

Wake-up Suppression: Refers to ignoring the User's FULL_COMMUNICATION request for the channel when it is in COMM_NO_COMMUNICATION or COMM_SILENT_COMMUNICATION state, but the channel's passive wake-up function remains unaffected. Wake-up suppression can be controlled via API when the global configuration item is enabled.

NoCom抑制：表现为限制通道切换到COMM_FULL_COMMUNICATION与COMM_SILENT_COMMUNICATION状态，当全局配置项打开的情况下，NoCom抑制也可以通过API来控制。

NoCom Inhibition: Manifests as restricting channel switching to COMM_FULL_COMMUNICATION and COMM_SILENT_COMMUNICATION states. When the global configuration item is enabled, NoCom inhibition can also be controlled via API.

managed通道与managing通道 (managed channel and managing channel)
---------------------------------------------------------------------------

一个通道可以被配置为managed通道和managing通道，即被其他通道管理的通道和管理其他通道的通道。一个通道为managed通道还是managing通道是由配置参数ComMManageReference来决定的，如果通道1通过配置项ComMManageReference引用了通道2，那么，通道1为managed通道，通道2为managing通道。其中managed通道的ComMNmVariant（配置参数）为LIGHT，managing通道的ComMNmVariant为FULL。

A channel can be configured as both a managed channel and a managing channel, i.e., a channel that is managed by other channels and a channel that manages other channels. Whether a channel is a managed channel or a managing channel is determined by the configuration parameter ComMManageReference. If Channel 1 references Channel 2 via the configuration item ComMManageReference, then Channel 1 is a managed channel, and Channel 2 is a managing channel. Among them, the managed channel's ComMNmVariant (configuration parameter) is LIGHT, while the managing channel's ComMNmVariant is FULL.

如果一个managed通道被用户主动或ECUM被动唤醒请求FULL_COMMUNICATION ，那么它的managing通道也需要请求FULL_COMMUNICATION。当一个managing通道想要切换到NO_COMMUNICATION的时候，一定需要它的managed通道都没有请求FULL_COMMUNICATION时才能切换状态。

If a managed channel is actively or passively awakened by a user to request FULL_COMMUNICATION, its managing channel also needs to request FULL_COMMUNICATION. When a managing channel wants to switch to NO_COMMUNICATION, it must wait until its managed channels have not requested FULL_COMMUNICATION before switching the state.

多核分布 (Multi-core Distribution)
----------------------------------------------

ComM 支持多分区（多核）分布，每一个通道和用户都支持被分配给特定的分区，通过配置项ComMChannelPartitionRef 和 ComMUserEcucPartitionRef 来实现。使能多分区功能，要确保 ComMMultiplePartitionEnabled 设置为TRUE。

ComM supports multi-partition (multi-core) distribution, with each channel and user supporting allocation to a specific partition through configuration items ComMChannelPartitionRef and ComMUserEcucPartitionRef. To enable the multi-partition feature, ensure that ComMMultiplePartitionEnabled is set to TRUE.

在使能多分区功能后，所有与通道和用户相关的 API 如ComM_CommunicationAllowed 或 ComM_RequestComMode 等，均只允许在对应通道或用户所在的分区上下文中被调用。

After enabling the multi-partition feature, all APIs related to channels and users such as ComM_CommunicationAllowed or ComM_RequestComMode are only allowed to be called in the context of the partition where the corresponding channel or user is located.

通道和它关联的用户可以分布在不同的分区上，ComM 使用全局共享变量进行分区间的信息交换，包括 PNC 相关的功能也是如此。

Channels and their associated users can be distributed across different partitions, with ComM using global shared variables for information exchange between partitions, including PNC-related functionalities as well.

每一个通道的主函数会被对应分区的任务所调度，这部分内容由 SchM 实现。

The main function of each channel is scheduled by tasks corresponding to partitions, and this part is implemented by SchM.

如果ComM 被同时分布到不同的核上，则 ComM 所使用的变量所在的内存分区不能启用缓存机制。

If ComM is distributed across multiple cores, the memory partition used by the variables accessed by ComM cannot enable caching mechanisms.

源文件描述 (Source file description)
===============================================

.. centered:: **表 ComM组件文件描述 (Table ComponentM Component File Description)**

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 文件 (Files)
     - 说明 (Description)
   * - ComM_BusSM.h
     - ComM与BusSm交互API声明 (Comm and BusSm Interaction API Declaration)
   * - ComM_BswM.h
     - ComM与BswM交互API声明 (Comm and BswM Interaction API Declaration)
   * - ComM_Ch.c
     - ComM 通道管理模块内部实现 (Comm channel management module internal implementation)
   * - ComM_Ch.h
     - ComM 通道管理模块内部接口声明 (Comm Channel Management Module Internal Interface Declaration)
   * - ComM_Dcm.h
     - ComM与Dcm交互API声明 (Comm and Dcm Interact API Declaration)
   * - ComM_EcuM.h
     - ComM与EcuM交互API声明 (Comm and EcuM Interaction API Declaration)
   * - ComM_Internal.h
     - ComM内部公共接口声明 (Internal Public Interface Declaration for ComM)
   * - ComM_Nm.h
     - ComM与NmIf交互API声明 (Comm and NmIf Interaction API Declaration)
   * - ComM_Pnc.h
     - ComM 部分网络管理模块内部实现 (ComM Part of Network Management Module Internal Implementation)
   * - ComM_Pnc.c
     - ComM 部分网络管理模块内部实现 (ComM Part of Network Management Module Internal Implementation)
   * - ComM.c
     - ComM源文件，包含了API函数的实现 (Source file for Comm, contains implementations of API functions)
   * - ComM.h
     - ComM头文件，包含了API函数的声明 (Comm header file, contains the declarations of API functions)
   * - ComM_Types.h
     - ComM 头文件，包含了模块类型定义 (Comm header file, contains module type definitions)
   * - ComM_Version.h
     - ComM 头文件，包含了版本信息 (Comm header file, contains version information)
   * - ComM_Cfg.h
     - ComM配置头文件，涉及配置项宏开关 (Configuration header file for Comm, involving configuration item macro switches)
   * - ComM_Cfg.c
     - ComM配置C文件，包含多分区情况下的配置常量定义 (Configuration file for ComM, includes constant definitions for multi-partition scenarios)
   * - ComM_Gent.c
     - ComM 与通道有关的主函数入口实现 (Comm related main function entry implementation)
   * - ComM_PBCfg.h
     - ComM 配置头文件，包含全局配置声明和相关类型定义 (Comm configuration header file, containing global configuration declarations and related type definitions)
   * - ComM_PBCfg.c
     - ComM 配置C文件，包含全局配置定义 (Comm Configuration C file, contains global configuration definitions)
   * - ComM_Com.h
     - ComM 配置头文件，包含PNC接收信号的回调函数声明 (Comm configuration header file, contains declarations of PNC receiving signal callback functions)
   * - ComM_Com.c
     - ComM 配置C文件，包含PNC接收信号的回调函数实现 (Comm configuration C file, includes implementation of PNC receive signal callback functions)
   * - ComM_MemMap.h
     - ComM 的内存映射抽象说明 (The memory-mapped abstraction of ComM)




.. figure:: ../../_static/参考手册(Module_Reference_Manual)/ComM/image4.png
   :alt: ComM组件静态文件交互关系图 (Comm Component Static File Interaction Diagram)
   :name: ComM组件静态文件交互关系图 (Comm Component Static File Interaction Diagram)
   :align: center

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/ComM/image5.png
   :alt: ComM组件静态文件交互关系图1 (Comm Component Static File Interaction Diagram)
   :name: ComM组件静态文件交互关系图1 (Comm Component Static File Interaction Diagram)
   :align: center

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/ComM/image6.png
   :alt: ComM组件静态文件交互关系图2 (Comm Component Static File Interaction Diagram)
   :name: ComM组件静态文件交互关系图2 (Comm Component Static File Interaction Diagram)
   :align: center


API接口 (API Interface)
=====================================

类型定义 (Type definition)
--------------------------------------

ComM_InitStatusType类型定义 (Comm_InitStatusType type definition)
=============================================================================

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 名称 (Name)
     - ComM_InitStatusType
   * - 类型 (Type)
     - Enumeration
   * - 范围 (Range)
     - COMM_UNINIT 未初始化 (UNINITIALIZED)
   * - 
     - COMM_INIT 初始化成功 (COMM_INIT Initialization successful)
   * - 描述 (Description)
     - 表示ComM初始化状态 (Indicates CommM Initialization State)




ComM_PNCModeType类型定义 (CommPNCModeType type definition)
======================================================================

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 名称 (Name)
     - ComM_PNCModeType
   * - 类型 (Type)
     - Enumeration
   * - 范围 (Range)
     - COMM_PNC_REQUESTED
   * - 
     - PNC处于被请求模式 (PNC is in requested mode)
   * - 
     - COMM_PNC\_PREPARE_SLEEP
   * - 
     - PNC处于prepare sleep模式 (PNC is in prepare sleep mode.)
   * - 
     - COMM_PNC_READY_SLEEP
   * - 
     - PNC处于ready sleep模式 (PNC is in ready sleep mode.)
   * - 
     - COMM_PNC_NO_COMMUNICATION
   * - 
     - PNC处于无通信模式 (PNC is in no communication mode.)
   * - 
     - COMM_PNC_REQUESTED_WITH_WAKEUP_REQUEST
   * - 
     - PNC是由本地ComM用户请求的 (PNC is requested by local ComM users.)
   * - 描述 (Description)
     - 表示PNC状态机的状态 (Show PNC state machine states)




ComM_StateType类型定义 (Comm_StateType Type Definition)
===================================================================

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 名称 (Name)
     - ComM_StateType
   * - 类型 (Type)
     - uint8
   * - 范围 (Range)
     - COMM_NO_COM_NO_PENDING_REQUEST
   * - 
     - COMM_NO_COM_REQUEST_PENDING
   * - 
     - COMM_FULL_COM_NETWORK_REQUESTED
   * - 
     - COMM_FULL_COM_READY_SLEEP
   * - 
     - COMM_SILENT_COM
   * - 描述 (Description)
     - 通信状态机通信状态与通信状态的状态和子状态 (Communication state machine communication states and their states and sub-states)




ComM_ModeType类型定义 (CommModeType type definition)
================================================================

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 名称 (Name)
     - ComM_ModeType
   * - 类型 (Type)
     - uint8
   * - 范围 (Range)
     - COMM_NO_COMMUNICATION
   * - 
     - COMM_SILENT_COMMUNICATION
   * - 
     - COMM_FULL_COMMUNICATION COMM_FULL\_
   * - 
     - COMMUNICATION_WITH_WAKEUP_REQUEST
   * - 描述 (Description)
     - 通信管理器的当前模式（状态机的主要状态） (The current mode of the communication manager (main states of the state machine))




ComM_UserHandleType类型定义 (Comm_UserHandleType type definition)
=============================================================================

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 名称 (Name)
     - ComM_UserHandleType
   * - 类型 (Type)
     - uint8
   * - 范围 (Range)
     - 0..254 (255 是保留的，用于 COMM_NOT_USED_USER_ID)
   * - 描述 (Description)
     - UserId的类型 (The type of UserId)




ComM_ConfigType类型定义 (Comm_ConfigType Type Definition)
=====================================================================

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 名称 (Name)
     - ComM_ConfigType
   * - 类型 (Type)
     - Structure
   * - 范围 (Range)
     -
   * - 描述 (Description)
     - ComM模块配置数据 (Comm module configuration data)




输入函数描述 (Describe the input function:)
-----------------------------------------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 输入模块 (Input Module)
     - API
   * - Det
     - Det_ReportError
   * - Nm
     - Nm_PassiveStartUp
   * - 
     - Nm_NetworkRequest
   * - 
     - Nm_NetworkRelease
   * - 
     - Nm_PduRxIndication
   * - 
     - Nm_PrepareBusSleepMode
   * - 
     - Nm_UpdateIRA
   * - Dcm
     - Dcm_ComM_NoComModeEntered
   * - 
     - Dcm_ComM_SilentComModeEntered
   * - 
     - Dcm_ComM_FullComModeEntered
   * - BswM
     - BswM_ComM_CurrentMode
   * - 
     - BswM_ComM_CurrentPNCMode
   * - 
     - BswM_ComM_InitiateReset
   * - NvM
     - NvM_ReadBlock
   * - 
     - NvM_WriteBlock
   * - 
     - NvM_GetErrorStatus
   * - <BusSM>
     - <BusSM>_GetCurrentComMode
   * - 
     - <BusSM>_RequestComMode
   * - CanIf
     - CanIf_Transmit
   * - CanSM
     - CanSM_TxTimeoutException
   * - Com
     - Com_ReceiveSignal
   * - 
     - Com_SendSignal




静态接口函数定义 (Static interface function definition)
---------------------------------------------------------------

ComM_Init函数定义 (Comm_Init function definition)
=============================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - ComM_Init
     - 
     - 
   * - 函数原型： (Function prototype:)
     - void ComM_Init(constComM_ConfigType\*ConfigPtr)
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x01
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 不可重入 (Non-reentrant)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - ConfigPtr
     - 值域： (Domain:)
     - 指向post-build配置数据的指针 (Pointer to post-build configuration data)
   * - 输入输出参数: (Input Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 返回值： (Return Value:)
     - 无 (None)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 完成对ComM模块的初始化处理，重新启动内部状态机 (Complete the initialization of the ComM module and restart the internal state machine.)
     - 
     - 




ComM_DeInit函数定义 (CommDeInit function definition)
================================================================

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - ComM_DeInit
   * - 函数原型： (Function prototype:)
     - void ComM_DeInit (
   * - 
     - void
   * - 
     - )
   * - 服务编号： (Service Number:)
     - 0x02
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
   * - 是否可重入： (Is Reentrant:)
     - 不可重入 (Non-reentrant)
   * - 输入参数： (Input parameters:)
     - 无 (None)
   * - 输入输出参数: (Input Output Parameters:)
     - 无 (None)
   * - 输出参数： (Output Parameters:)
     - 无 (None)
   * - 返回值： (Return Value:)
     - 无 (None)
   * - 功能概述： (Function Overview:)
     - 反初始化ComM模块 (Uninitialize ComM module)




ComM_GetStatus函数定义 (The Comm_GetStatus function definition)
===========================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - ComM_GetStatus
     - 
     - 
   * - 函数原型： (Function prototype:)
     - Std_ReturnTypeComM_GetStatus(
     - 
     - 
   * - 
     - ComM_InitStatusType\*Status
     - 
     - 
   * - 
     - )
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x03
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 不可重入 (Non-reentrant)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - 无 (None)
     - 
     - 
   * - 输入输出参数: (Input Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - Status
     - 值域： (Domain:)
     - 初始化状态 (Initialization state)
   * - 返回值： (Return Value:)
     - E_OK:初始化状态成功返回 (E_OK: Initialization status successful return)
     - 
     - 
   * - 
     - E_NOT_OK:初始化状态成功失败 (E_NOT_OK: Initialization status success failure)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 返回ComM的初始化状态。 (Return to ComM's initial state.)
     - 
     - 




ComM_GetInhibitionStatus函数定义 (The Comm_GetInhibitionStatus function definition)
===============================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - ComM_GetInhibitionStatus
     - 
     - 
   * - 函数原型： (Function prototype:)
     - Std_ReturnTypeComM_GetInhibitionStatus(
     - 
     - 
   * - 
     - NetworkHandleTypeChannel,
     - 
     - 
   * - 
     - ComM_InhibitionStatusType\*Status
     - 
     - 
   * - 
     - )
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x04
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 不可重入 (Non-reentrant)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - Channel
     - 值域： (Domain:)
     - ComM的通道Id (Comm's channel Id)
   * - 输入输出参数: (Input Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - State
     - 值域： (Domain:)
     - ComM通道的抑制状态 (The inhibition state of the ComM channel)
   * - 返回值： (Return Value:)
     - E_OK：成功返回抑制状态 (E_OK: Suppressed state on success)
     - 
     - 
   * - 
     - E_NOT_OK：抑制状态返回失败 (E_NOT_OK: Suppressed state return failure)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 返回ComM通道的抑制状态。 (Return the抑制状态of the ComM channel.)
     - 
     - 




ComM_RequestComMode函数定义 (Comm_RequestComMode function definition)
=================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - ComM_RequestComMode
     - 
     - 
   * - 函数原型： (Function prototype:)
     - Std_ReturnTypeComM_RequestComMode(
     - 
     - 
   * - 
     - ComM_UserHandleTypeUser,
     - 
     - 
   * - 
     - ComM_ModeTypeComMode
     - 
     - 
   * - 
     - )
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x05
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 可重入 (Reentrant)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - User
     - 值域： (Domain:)
     - 请求模式的用户的Id (The Id of the users in request mode)
   * - 
     - ComMode
     - 值域： (Domain:)
     - COMM_FULL_COMMUNICATIONCOMM_NO_COMMUNICATION
   * - 输入输出参数: (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无
     - 
     - 
   * - 返回值： (Return Value:)
     - E_OK:成功切换到新模式 (E_OK: Successfully switched to the new mode)
     - 
     - 
   * - 
     - E_NOT_OK:更改新模式失败 (E_NOT_OK: Failed to change new mode)
     - 
     - 
   * - 
     - COMM_E_MODE_LIMITATION:由于模式抑制，不能更改模式。 (COMM_E_MODE_LIMITATION: Due to mode suppression, the mode cannot be changed.)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 用户对通信模式的请求。 (Requests for communication modes from users.)
     - 
     - 




ComM_GetMaxComMode函数定义 (The Comm_GetMaxCommMode function definition)
====================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - ComM_GetMaxComMode
     - 
     - 
   * - 函数原型： (Function prototype:)
     - Std_ReturnTypeComM_GetMaxComMode(
     - 
     - 
   * - 
     - ComM_UserHandleTypeUser,
     - 
     - 
   * - 
     - ComM_ModeType\*ComMode
     - 
     - 
   * - 
     - )
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x06
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 可重入 (Reentrant)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - User
     - 值域： (Domain:)
     - 用户的Id (User's ID)
   * - 输入输出参数: (Input Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - ComMode
     - 值域： (Domain:)
     - 获取的通信模式 (Acquired communication mode)
   * - 返回值： (Return Value:)
     - E_OK:成功返回允许的通信模式最大值 (E_OK: Success returns the maximum allowable communication mode value)
     - 
     - 
   * - 
     - E_NOT_OK:返回允许的通信模式最大值失败 (E_NOT_OK: Failed to return the maximum allowed communication mode value)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 查询相应用户最大允许的通信模式。 (Query the maximum allowed communication mode for the corresponding user.)
     - 
     - 




ComM_GetRequestedComMode函数定义 (The Comm_GetRequestedComMode function definition)
===============================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - ComM_GetRequestedComMode
     - 
     - 
   * - 函数原型： (Function prototype:)
     - Std_ReturnTypeComM_GetRequestedComMode(
     - 
     - 
   * - 
     - ComM_UserHandleTypeUser,
     - 
     - 
   * - 
     - ComM_ModeType\*ComMode
     - 
     - 
   * - 
     - )
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x07
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 可重入 (Reentrant)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - User
     - 值域： (Domain:)
     - 用户的Id (User's ID)
   * - 输入输出参数: (Input Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - ComMode
     - 值域： (Domain:)
     - 请求的通信模式 (Request communication mode)
   * - 返回值： (Return Value:)
     - E_OK:成功返回请求的通信模式 (E_OK: Successful return of requested communication mode)
     - 
     - 
   * - 
     - E_NOT_OK:请求的通信模式返回失败 (E_NOT_OK: The communication mode request failed)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 查询对应用户当前请求的通信模式。 (Query the communication mode for the corresponding user's current request.)
     - 
     - 




ComM_GetCurrentComMode函数定义 (The Comm_GetCurrentComMode function definition)
===========================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - ComM\_GetCurrentComMode
     - 
     - 
   * - 函数原型： (Function prototype:)
     - Std_ReturnTypeComM\_GetCurrentComMode(
     - 
     - 
   * - 
     - ComM_UserHandleTypeUser,
     - 
     - 
   * - 
     - ComM_ModeType\*ComMode
     - 
     - 
   * - 
     - )
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x08
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 可重入 (Reentrant)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - User
     - 值域： (Domain:)
     - 用户的Id (User's ID)
   * - 输入输出参数: (Input Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - ComMode
     - 值域： (Domain:)
     - 获取当前的通信模式 (Get the current communication mode)
   * - 返回值： (Return Value:)
     - E_OK:从BusSM返回通讯模式成功 (E_OK: Communication mode switch succeeded as returned by BusSM)
     - 
     - 
   * - 
     - E_NOT_OK:从BusSM返回通讯模式失败 (E_NOT_OK: Communication mode failure from BusSM)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 查询当前通信模式。 (Query current communication mode.)
     - 
     - 




ComM_PreventWakeUp函数定义 (Comm_PreventWakeUp function definition)
===============================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - ComM\_PreventWakeUp
     - 
     - 
   * - 函数原型： (Function prototype:)
     - Std_ReturnTypeComM\_PreventWakeUp(
     - 
     - 
   * - 
     - NetworkHandleTypeChannel,
     - 
     - 
   * - 
     - booleanStatus
     - 
     - 
   * - 
     - )
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x09
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 不可重入 (Non-reentrant)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - Channel
     - 值域： (Domain:)
     - Channel的Id (Channel's Id)
   * - 
     - Status
     - 值域： (Domain:)
     - 是否开启唤醒抑制功能 (Is wake-up inhibition function enabled?)
   * - 输入输出参数: (Input Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 返回值： (Return Value:)
     - E_OK:成功地更改了通道的唤醒状态 (E_OK: Successfully changed the channel's wake-up state)
     - 
     - 
   * - 
     - E_NOT_OK:唤醒状态更改失败，例如ComMEcuGroupClassification禁用了该功能 (E_NOT_OK: Failed to change wake-up state, for example, ComMEcuGroupClassification disabled this feature)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 更改相应通道的抑制状态COMM_NO_WAKEUP (Change the inhibit state of the corresponding channel to COMM_NO_WAKEUP)
     - 
     - 




ComM_LimitChannelToNoComMode函数定义 (The function definition for ComM_LimitChannelToNoComMode)
===========================================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - ComM_LimitChannelToNoComMode
     - 
     - 
   * - 函数原型： (Function prototype:)
     - Std_ReturnTypeComM\_LimitChannelToNoComMode(
     - 
     - 
   * - 
     - NetworkHandleTypeChannel,
     - 
     - 
   * - 
     - booleanStatus
     - 
     - 
   * - 
     - )
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x0b
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 不可重入 (Non-reentrant)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - Channel
     - 值域： (Domain:)
     - Channel的Id (Channel's Id)
   * - 
     - Status
     - 值域： (Domain:)
     - TRUE：使能COMM_NO_COMMUNICATION更改为更高的通信模式。 (TRUE: Enable COMM_NO_COMMUNICATION to be changed to a higher communication mode.)
   * - 
     - 
     - 
     - FALSE：禁止COMM_NO_COMMUNICATION更改为更高的通信模式。 (FALSE: prohibit COMM_NO_COMMUNICATION from being changed to a higher communication mode.)
   * - 输入输出参数: (Input Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 返回值： (Return Value:)
     - E_OK:成功地改变了通道的抑制状态 (E_OK: Successfully changed the channel's inhibition state)
     - 
     - 
   * - 
     - E_NOT_OK:改变通道的抑制状态失败，例如ComMEcuGroupClassification禁用该功能 (E_NOT_OK: Failed to change the suppress state of the channel, e.g., ComMEcuGroupClassification disable this feature)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 更改channel对应通道的禁止状态，以便从COMM_NO_COMMUNICATION更改为更高的通信模式。 (Change the prohibition status of the corresponding channel to allow it to be switched from COMM_NO_COMMUNICATION to a higher communication mode.)
     - 
     - 




ComM_LimitECUToNoComMode函数定义 (The function definition for ComM_LimitECUToNoComMode)
===================================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - ComM_LimitECUToNoComMode
     - 
     - 
   * - 函数原型： (Function prototype:)
     - Std_ReturnTypeComM_LimitECUToNoComMode(
     - 
     - 
   * - 
     - booleanStatus
     - 
     - 
   * - 
     - )
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x0c
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 不可重入 (Non-reentrant)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - Status
     - 值域： (Domain:)
     - TRUE：使能COMM_NO_COMMUNICATION更改为更高的通信模式。 (TRUE: Enable COMM_NO_COMMUNICATION to be changed to a higher communication mode.)
   * - 
     - 
     - 
     - FALSE：禁止COMM_NO_COMMUNICATION更改为更高的通信模式。 (FALSE: prohibit COMM_NO_COMMUNICATION from being changed to a higher communication mode.)
   * - 输入输出参数: (Input Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 返回值： (Return Value:)
     - E_OK:ECU成功地改变了通道的抑制状态 (E_OK: The ECU successfully changed the channel's inhibit status)
     - 
     - 
   * - 
     - E_NOT_OK:ECU改变通道的抑制状态失败，例如ComMEcuGroupClassification禁用该功能 (E_NOT_OK: Failed to change the抑制状态 of ECU channel, for example, ComMEcuGroupClassification disables this function)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 更改ECU的禁止状态（对于所有的通道），以便从COMM_NO_COMMUNICATION更改为更高的通信模式。 (Modify the prohibition status of ECU (for all channels) to change from COMM_NO_COMMUNICATION to a higher communication mode.)
     - 
     - 




ComM_ReadInhibitCounter函数定义 (The Comm_ReadInhibitCounter function definition)
=============================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - ComM_ReadInhibitCounter
     - 
     - 
   * - 
     - Std_ReturnType   ComM_ReadInhibitCounter (
     - 
     -
   * - 函数原型： (Function prototype:)
     - uint16* CounterValue
     - 
     -
   * - 
     - )
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x0d
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 可重入 (Reentrant)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - 无 (None)
     - 
     - 
   * - 输入输出参数: (Input Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - CounterValue
     - 值域： (Domain:)
     - 被拒绝的COMM_FULL_COMMUNICATION用户请求的数量。 (The number of rejected COMM_FULL_COMMUNICATION user requests.)
   * - 
     - E_OK：成功返回抑制计数器 (E_OK: Success returns suppression counter)
     - 
     -
   * - 
     - E_NOT_OK：抑制计数器返回失败 (E_NOT_OK: Counter suppression failed)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 这个函数获取被拒绝的COMM_FULL_COMMUNICATION用户请求的数量。 (This function retrieves the number of rejected COMM_FULL_COMMUNICATION user requests.)
     - 
     - 




ComM_ResetInhibitCounter函数定义 (The Comm_ResetInhibitCounter function definition)
===============================================================================================

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - ComM_ResetInhibitCounter
   * - 函数原型： (Function prototype:)
     - Std_ReturnType ComM_ResetInhibitCounter (
   * - 
     - void
   * - 
     - )
   * - 服务编号： (Service Number:)
     - 0x0e
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
   * - 是否可重入： (Is Reentrant:)
     - 可重入 (Reentrant)
   * - 输入参数： (Input parameters:)
     - 无 (None)
   * - 输入输出参数: (Input Output Parameters:)
     - 无 (None)
   * - 输出参数： (Output Parameters:)
     - 无 (None)
   * - 返回值： (Return Value:)
     - E_OK：重置了被拒绝的COMM_FULL_COMMUNICATION的数量 (E_OK: Reset the count of rejected COMM_FULL_COMMUNICATION)
   * - 
     - E_NOT_OK：重置失败 (E_NOT_OK: Reset Failed)
   * - 功能概述： (Function Overview:)
     - 这个函数重置被拒绝的COMM_FULL_COMMUNICATION用户请求的数量。 (This function resets the count of rejected COMM_FULL_Communication user requests.)




ComM_SetECUGroupClassification函数定义 (The Comm_SetECUGroupClassification function defines)
========================================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - ComM_SetECUGroupClassification
     - 
     - 
   * - 函数原型： (Function prototype:)
     - Std_ReturnTypeComM\_SetECUGroupClassification(
     - 
     - 
   * - 
     - ComM_InhibitionStatusTypeStatus
     - 
     - 
   * - 
     - )
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x0f
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 不可重入 (Non-reentrant)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - Status
     - 值域： (Domain:)
     - 设置的模式禁止状态 (Disabled mode set)
   * - 输入输出参数: (Input Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 返回值： (Return Value:)
     - E_OK:ECU成功地修改了ComMEcuGroupClassification的值 (E_OK: The ECU successfully modified the value of ComMEcuGroupClassification)
     - 
     - 
   * - 
     - E_NOT_OK:ComMEcuGroupClassification的值修改失败 (E_NOT_OK: Modification of the value for ComMEcuGroupClassification failed)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 设置ComMEcuGroupClassification的值 (Set the value of ComMEcuGroupClassification)
     - 
     - 




ComM_GetVersionInfo函数定义 (The CommM_GetVersionInfo function definition)
======================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - ComM_GetVersionInfo
     - 
     - 
   * - 函数原型： (Function prototype:)
     - voidComM_GetVersionInfo(
     - 
     - 
   * - 
     - Std\_VersionInfoType\*Versioninfo
     - 
     - 
   * - 
     - )
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x10
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 可重入 (Reentrant)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - 无 (None)
     - 
     - 
   * - 输入输出参数: (Input Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - Versioninfo
     - 值域： (Domain:)
     - 指向存储版本信息的位置 (Point to where version information is stored)
   * - 返回值： (Return Value:)
     - 无 (None)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 获取版本信息 (Get Version Information)
     - 
     - 




ComM_Nm_NetworkStartIndication函数定义 (Comm_Nm_NetworkStartIndication function definition)
=======================================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - ComM_Nm_NetworkStartIndication
     - 
     - 
   * - 函数原型： (Function prototype:)
     - voidComM_Nm_NetworkStartIndication(
     - 
     - 
   * - 
     - NetworkHandleTypeChannel
     - 
     - 
   * - 
     - )
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x15
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 异步 (Asynchronous)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 可重入 (Reentrant)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - Channel
     - 值域： (Domain:)
     - ComM的通道Id (Comm's channel Id)
   * - 输入输出参数: (Input Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 返回值： (Return Value:)
     - 无 (None)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 指示在总线睡眠模式下已收到NM消息，这表示网络中的某些节点已进入网络模式。 (Indication received in bus sleep mode indicates that some nodes in the network have entered network mode.)
     - 
     - 




ComM_Nm_NetworkMode函数定义 (Comm_Nm_NetworkMode function definition)
=================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - ComM_Nm_NetworkMode
     - 
     - 
   * - 函数原型： (Function prototype:)
     - voidComM_Nm_NetworkMode(
     - 
     - 
   * - 
     - NetworkHandleTypeChannel
     - 
     - 
   * - 
     - )
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x18
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 异步 (Asynchronous)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 可重入 (Reentrant)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - Channel
     - 值域： (Domain:)
     - ComM的通道Id (Comm's channel Id)
   * - 输入输出参数: (Input Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 返回值： (Return Value:)
     - 无 (None)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 通知网络管理已进入网络模式。 (Notify network management that network mode has entered.)
     - 
     - 




ComM_Nm_PrepareBusSleepMode函数定义 (The function definition for ComM_Nm_PrepareBusSleepMode)
=========================================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - ComM_Nm_PrepareBusSleepMode
     - 
     - 
   * - 函数原型： (Function prototype:)
     - voidComM_Nm_PrepareBusSleepMode(
     - 
     - 
   * - 
     - NetworkHandleTypeChannel
     - 
     - 
   * - 
     - )
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x19
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 异步 (Asynchronous)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 可重入 (Reentrant)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - Channel
     - 值域： (Domain:)
     - ComM的通道Id (Comm's channel Id)
   * - 输入输出参数: (Input Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 返回值： (Return Value:)
     - 无 (None)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 通知网络管理已进入PrepareBus-Sleep模式。 (Notification: Network management has entered PrepareBus-Sleep mode.)
     - 
     - 




ComM_Nm_BusSleepMode函数定义 (CommNm_BusSleepMode function definition)
==================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - ComM_Nm_BusSleepMode
     - 
     - 
   * - 函数原型： (Function prototype:)
     - voidComM_Nm_BusSleepMode(
     - 
     - 
   * - 
     - NetworkHandleTypeChannel
     - 
     - 
   * - 
     - )
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x1a
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 异步 (Asynchronous)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 可重入 (Reentrant)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - Channel
     - 值域： (Domain:)
     - ComM的通道Id (Comm's channel Id)
   * - 输入输出参数: (Input Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 返回值： (Return Value:)
     - 无 (None)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 通知网络管理已进入Bus-Sleep模式。 (Notification: Network management has entered Bus-Sleep mode.)
     - 
     - 




ComM_Nm_RestartIndication函数定义 (Function definition for ComM_Nm_RestartIndication)
=================================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - ComM\_Nm\_RestartIndication
     - 
     - 
   * - 函数原型： (Function prototype:)
     - voidComM\_Nm\_RestartIndication(
     - 
     - 
   * - 
     - NetworkHandleTypeChannel
     - 
     - 
   * - 
     - )
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x1b
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 异步 (Asynchronous)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 可重入 (Reentrant)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - Channel
     - 值域： (Domain:)
     - ComM的通道Id (Comm's channel Id)
   * - 输入输出参数: (Input Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 返回值： (Return Value:)
     - 无 (None)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 如果NmIf已开始关闭协调总线，并且并非所有协调总线都已指示总线处于睡眠状态，并且至少在协调总线之一上重新启动了NM，则NM接口应在已经指示总线睡眠状态的通道使用nmNetworkHandle调用回调函数ComM_Nm_RestartIndication。 (If NmIf has begun closing the coordination bus, and not all coordination buses have instructed the bus to enter sleep mode, and NM has been restarted on at least one of the coordination buses, then the NM interface should use nmNetworkHandle to call the callback function ComM_Nm_RestartIndication on the channel that has already instructed the bus to sleep.)
     - 
     - 




ComM_DCM_ActiveDiagnostic函数定义 (TheComm_DCM_ActiveDiagnosticfunctiondefinition)
==============================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - ComM_DCM_ActiveDiagnostic
     - 
     - 
   * - 函数原型： (Function prototype:)
     - voidComM_DCM_ActiveDiagnostic(
     - 
     - 
   * - 
     - NetworkHandleTypeChannel
     - 
     - 
   * - 
     - )
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x1f
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 可重入 (Reentrant)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - Channel
     - 值域： (Domain:)
     - ComM的通道Id (Comm's channel Id)
   * - 输入输出参数: (Input Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 返回值： (Return Value:)
     - 无 (None)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - DCM诊断开始的指示。 (DCM diagnosis initiation instructions.)
     - 
     - 




ComM_DCM_InactiveDiagnostic函数定义 (Comm_DCM_InactiveDiagnostic function definition)
=================================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - ComM_DCM_InactiveDiagnostic
     - 
     - 
   * - 函数原型： (Function prototype:)
     - voidComM_DCM_InactiveDiagnostic(
     - 
     - 
   * - 
     - NetworkHandleTypeChannel
     - 
     - 
   * - 
     - )
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x20
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 可重入 (Reentrant)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - Channel
     - 值域： (Domain:)
     - ComM的通道Id (Comm's channel Id)
   * - 输入输出参数: (Input Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 返回值： (Return Value:)
     - 无 (None)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - DCM诊断结束的指示。 (Indication of DCM diagnosis completion.)
     - 
     - 




ComM_EcuM_WakeUpIndication函数定义 (Function definition for ComM_EcuM_WakeUpIndication)
===================================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - ComM_EcuM_WakeUpIndication
     - 
     - 
   * - 函数原型： (Function prototype:)
     - voidComM_EcuM_WakeUpIndication(
     - 
     - 
   * - 
     - NetworkHandleTypeChannel
     - 
     - 
   * - 
     - )
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x2a
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 可重入 (Reentrant)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - Channel
     - 值域： (Domain:)
     - ComM的通道Id (Comm's channel Id)
   * - 输入输出参数: (Input Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 返回值： (Return Value:)
     - 无 (None)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 在相应通道上的唤醒通知。 (Wake-up notifications on the corresponding channels.)
     - 
     - 




ComM_EcuM_PNCWakeUpIndication函数定义 (The CommEcuM_PNCWakeUpIndication function definition)
========================================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - ComM_EcuM_PNCWakeUpIndication
     - 
     - 
   * - 函数原型： (Function prototype:)
     - voidComM_EcuM_PNCWakeUpIndication(
     - 
     - 
   * - 
     - PNCHandleTypePNCid
     - 
     - 
   * - 
     - )
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x37
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 可重入 (Reentrant)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - PNCid
     - 值域： (Domain:)
     - 局域网集群的Id (Cluster ID of Local Network)
   * - 输入输出参数: (Input Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 返回值： (Return Value:)
     - 无 (None)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 在相应pnc上的唤醒通知。 (Wake-up notifications on the corresponding pnc.)
     - 
     - 




ComM_CommunicationAllowed函数定义 (The CommCommunicationAllowed function definition)
================================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - ComM_CommunicationAllowed
     - 
     - 
   * - 函数原型： (Function prototype:)
     - voidComM_CommunicationAllowed(
     - 
     - 
   * - 
     - NetworkHandleTypeChannel,
     - 
     - 
   * - 
     - boolean Allowed
     - 
     - 
   * - 
     - )
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x35
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 异步 (Asynchronous)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 不可重入 (Non-reentrant)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - Channel
     - 值域： (Domain:)
     - ComM的通道Id (Comm's channel Id)
   * - 
     - Allowed
     - 值域： (Domain:)
     - 是否允许通信 (Is communication allowed?)
   * - 输入输出参数: (Input Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 返回值： (Return Value:)
     - 无 (None)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 当允许通信时，EcuM或BswM应向ComM指示。 (When communication is allowed, EcuM or BswM shall indicate to ComM.)
     - 
     - 




ComM_BusSM_ModeIndication函数定义 (Comm_BusSM_ModeIndication function definition)
=============================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - ComM_BusSM_ModeIndication
     - 
     - 
   * - 函数原型： (Function prototype:)
     - voidComM_BusSM_ModeIndication(
     - 
     - 
   * - 
     - NetworkHandleTypeChannel,
     - 
     - 
   * - 
     - ComM_ModeTypeComMode
     - 
     - 
   * - 
     - )
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x33
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 异步 (Asynchronous)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 可重入 (Reentrant)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - Channel
     - 值域： (Domain:)
     - ComM的通道Id (Comm's channel Id)
   * - 
     - ComMode
     - 值域： (Domain:)
     - 通信模式 (Communication mode)
   * - 输入输出参数: (Input Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 返回值： (Return Value:)
     - 无 (None)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 由相应的BusSM通知实际总线模式。 (Notify the actual bus mode via the corresponding BusSM.)
     - 
     - 




ComM_BusSM_BusSleepMode函数定义 (Comm_BusSM_BusSleepMode function definition)
=========================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - ComM_BusSM_BusSleepMode
     - 
     - 
   * - 函数原型： (Function prototype:)
     - voidComM_BusSM_BusSleepMode(
     - 
     - 
   * - 
     - NetworkHandleTypeChannel
     - 
     - 
   * - 
     - )
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x34
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 可重入 (Reentrant)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - Channel
     - 值域： (Domain:)
     - ComM的通道Id (Comm's channel Id)
   * - 输入输出参数: (Input Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 返回值： (Return Value:)
     - E_OK: 请求被接受 (E_OK: The request has been accepted.)
     - 
     - 
   * - 
     - E_NOT_OK:请求被拒绝 (E_NOT_OK: Request rejected)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 通知相应的总线状态管理器实际的总线模式为“Bus-Sleep”。 (Notify the corresponding bus status manager that the actual bus mode is "Bus-Sleep".)
     - 
     - 
   * - 
     - 仅适用于LIN从节点。 (Only for LIN slave nodes.)
     - 
     - 




ComM_COMCbk\_<sn>函数定义 (ComM_COMCbk\<sn> Function Definition)
============================================================================

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - ComM_COMCbk\_<sn>
   * - 函数原型： (Function prototype:)
     - void ComM_COMCbk\_<sn> (
   * - 
     - void
   * - 
     - )
   * - 服务编号： (Service Number:)
     - 0x36
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
   * - 是否可重入： (Is Reentrant:)
     - 不可重入 (Non-reentrant)
   * - 输入参数： (Input parameters:)
     - 无 (None)
   * - 输入输出参数: (Input Output Parameters:)
     - 无 (None)
   * - 输出参数： (Output Parameters:)
     - 无 (None)
   * - 返回值： (Return Value:)
     - 无 (None)
   * - 功能概述： (Function Overview:)
     - 在COM中更新EIRA或ERA时调用此回调。 (This callback is invoked when updating EIRA or ERA in COM.)




ComM_MainFunction函数定义 (Definition of ComM_MainFunction function)
================================================================================

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - ComM_MainFunction
   * - 函数原型： (Function prototype:)
     - void ComM_MainFunction\_<ComMChannel.ShortName> (
   * - 
     - void
   * - 
     - )
   * - 服务编号： (Service Number:)
     - 0x60
   * - 功能概述： (Function Overview:)
     - ComM 模块后台主处理函数。 需被后台主循环或 OS 的 task调用 (Comm module backend main processing function. Needs to be called by the backend main loop or an OS task.)




可配置函数定义 (Configurable Function Definition)
----------------------------------------------------------

无。

None.

SWC服务组件封装 (SWC Service Component Packaging)
-----------------------------------------------------------

以下类型和接口可以封装至SWC生成完整的服务组件，可以与应用通过端口连接，没有列出的部分暂时不支持。

The following types and interfaces can be encapsulated into SWC to generate complete service components, which can be connected to the application via ports. Parts not listed are currently unsupported.

实现数据类型封装 (Implement data type encapsulation)
============================================================

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 类型名及定义引用 (Type Name and Definition Reference)
     - 生成条件 (Generate Conditions)
   * - ComM_ModeType
     - 无 (None)
   * - ComM_UserHandleType
     - 无 (None)
   * - ComM_UserHandleArrayType\_{channel_name}
     - 无 (None)




SR接口封装 (SR Interface Encapsulation)
===================================================

ComM_CurrentChannelRequest
------------------------------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - ComM_CurrentChannelRequest\_{channel_name}
   * - 功能描述 (Function Description)
     - Array of ComMUserIdentifier, that currently holdFULL_COM requests for this channel.
   * - 变体： (Variants:)
     - channel_name ={ecuc(ComM/ComMConfigSet/ComMChannel.SHORT-NAME)}
   * - 生成条件： (Generate conditions:)
     - ComMFullCommRequestNotificationEnabled is true
   * - 输入参数： (Input parameters:)
     - ComM_UserHandleArrayType\_{channel_name}
   * - 从属端口： (Subordinate Port:)
     - ComM_CR




CS接口封装 (CS Interface Packaging)
===============================================

Rte_Call_ComM_ComM_UserRequest_GetCurrentComMode
----------------------------------------------------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Rte_Call_ComM_ComM_UserRequest_GetCurrentComMode
   * - 运行实体函数定义： (Definition of running entity function:)
     - 详见4.3.9 (See 4.3.9)
   * - 变体： (Variants:)
     - 无 (None)
   * - 生成条件： (Generate conditions:)
     - 无 (None)
   * - 端口类型： (Port Type:)
     - Provided Port
   * - 从属端口： (Subordinate Port:)
     - ComM_UserRequest




Rte_Call_ComM_ComM_UserRequest_GetMaxComMode
------------------------------------------------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Rte_Call_ComM_ComM_UserRequest_GetMaxComMode
   * - 运行实体函数定义： (Definition of running entity function:)
     - 详见4.3.7 (See 4.3.7)
   * - 变体： (Variants:)
     - 无 (None)
   * - 生成条件： (Generate conditions:)
     - 无 (None)
   * - 端口类型： (Port Type:)
     - Provided Port
   * - 从属端口： (Subordinate Port:)
     - ComM_UserRequest




Rte_Call_ComM_ComM_UserRequest_RequestComMode
-------------------------------------------------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Rte_Call_ComM_ComM_UserRequest_RequestComMode
   * - 运行实体函数定义： (Definition of running entity function:)
     - 详见4.3.6 (See 4.3.6)
   * - 变体： (Variants:)
     - 无 (None)
   * - 生成条件： (Generate conditions:)
     - 无 (None)
   * - 端口类型： (Port Type:)
     - Provided Port
   * - 从属端口： (Subordinate Port:)
     - ComM_UserRequest




Rte_Call_ComM_ComM_ChannelLimitation_GetInhibitionStatus
------------------------------------------------------------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Rte_Call_ComM_ComM_ChannelLimitation_GetInhibitionStatus
   * - 运行实体函数定义： (Definition of running entity function:)
     - 详见4.3.5 (See 4.3.5)
   * - 变体： (Variants:)
     - 无 (None)
   * - 生成条件： (Generate conditions:)
     - ComMModeLimitationEnabled is TRUE
   * - 端口类型： (Port Type:)
     - Provided Port
   * - 从属端口： (Subordinate Port:)
     - ComM_ChannelLimitation




Rte_Call_ComM_ComM_ChannelLimitation_LimitChannelToNoComMode
----------------------------------------------------------------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Rte\_Call_ComM_ComM_ChannelLimitation_LimitChannelToNoComMode
   * - 运行实体函数定义： (Definition of running entity function:)
     - 详见4.3.11 (See 4.3.11)
   * - 变体： (Variants:)
     - 无 (None)
   * - 生成条件： (Generate conditions:)
     - ComMModeLimitationEnabled andComMResetAfterForcingNoComm open
   * - 端口类型： (Port Type:)
     - Provided Port
   * - 从属端口： (Subordinate Port:)
     - ComM_ChannelLimitation




Rte_Call_ComM_ComM_ChannelWakeup_PreventWakeUp
--------------------------------------------------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Rte_Call_ComM_ComM_ChannelWakeup_PreventWakeUp
   * - 运行实体函数定义： (Definition of running entity function:)
     - 详见4.3.10 (See 4.3.10)
   * - 变体： (Variants:)
     - 无 (None)
   * - 生成条件： (Generate conditions:)
     - ComMWakeupInhibitionEnabled open
   * - 端口类型： (Port Type:)
     - Provided Port
   * - 从属端口： (Subordinate Port:)
     - ComM_ChannelWakeup




Rte_Call_ComM_ComM_ECUModeLimitation_LimitECUToNoComMode
------------------------------------------------------------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Rte_Call_ComM_ComM_ECUModeLimitation_LimitECUToNoComMode
   * - 运行实体函数定义： (Definition of running entity function:)
     - 详见4.3.12 (See 4.3.12)
   * - 变体： (Variants:)
     - 无 (None)
   * - 生成条件： (Generate conditions:)
     - ComMModeLimitationEnabled andComMResetAfterForcingNoComm open
   * - 端口类型： (Port Type:)
     - Provided Port
   * - 从属端口： (Subordinate Port:)
     - ComM_ECUModeLimitation




Rte_Call_ComM_ComM_ECUModeLimitation_ReadInhibitCounter
-----------------------------------------------------------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Rte_Call_ComM_ComM_ECUModeLimitation_ReadInhibitCounter
   * - 运行实体函数定义： (Definition of running entity function:)
     - 详见4.3.13 (See 4.3.13)
   * - 变体： (Variants:)
     - 无 (None)
   * - 生成条件： (Generate conditions:)
     - ComMModeLimitationEnabled enable andComMGlobalNvMBlockDescriptor configured
   * - 端口类型： (Port Type:)
     - Provided Port
   * - 从属端口： (Subordinate Port:)
     - ComM_ECUModeLimitation




Rte_Call_ComM_ComM_ECUModeLimitation_ResetInhibitCounter
------------------------------------------------------------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Rte_Call_ComM_ComM_ECUModeLimitation_ResetInhibitCounter
   * - 运行实体函数定义： (Definition of running entity function:)
     - 详见4.3.14 (See 4.3.14)
   * - 变体： (Variants:)
     - 无 (None)
   * - 生成条件： (Generate conditions:)
     - ComMModeLimitationEnabled enable andComMGlobalNvMBlockDescriptor configured
   * - 端口类型： (Port Type:)
     - Provided Port
   * - 从属端口： (Subordinate Port:)
     - ComM_ECUModeLimitation




模式转换接口封装 (Interface Encapsulation for Mode Conversion)
======================================================================

ComM_CurrentMode
--------------------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 接口名称： (Interface Name:)
     - UM\_{user_name}_currentMode
   * - 变体： (Variants:)
     - user_name ={ecuc(ComM/ComMConfigSet/ComMUser.SHORT-NAME)}
   * - 生成条件： (Generate conditions:)
     - 无 (None)
   * - 模式组： (Pattern Group:)
     - currentMode
   * - 端口类型： (Port Type:)
     - Provided Port
   * - 从属端口： (Subordinate Port:)
     - ComM_UM




配置 (Configure)
==============================

ComMGeneral
---------------------------

.. centered:: **表  ComMGeneral属性描述 (Table  ComMGeneral Property Description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - ComM0PNCVectorAvoidance
     - 取值范围 (Range)
     - TRUE,FALSE
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 如果启用了ComMPNCGatewayEnabled，此参数将避免发送0-PNC-Vectors。（暂不支持） (If ComMPNCGatewayEnabled is enabled, this parameter will avoid sending 0-PNC-Vectors. (Not yet supported))
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - ComMPNCGatewayEnabled启用 (EnableComMPNCGateway)
     - 
     - 
   * - ComMDevErrorDetect
     - 取值范围 (Range)
     - true, false
     - 默认取值 (Default value)
     - false
   * - 
     - 参数描述 (Parameter Description)
     - 打开或关闭开发错误检测和通知。 (Enable or disable development error detection and notifications.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无 (None)
     - 
     - 
   * - ComMDirectUserMapping
     - 取值范围 (Range)
     - TRUE,FALSE
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 如果此参数设置为true，配置工具将自动为每个ComMPNC 创建一个ComMUser，并为每个ComMChannel 创建一个ComMUser。 (If this parameter is set to true, the configuration tool will automatically create a ComMUser for each ComMPNC and a ComMUser for each ComMChannel.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无 (None)
     - 
     - 
   * - ComMEcuGroupClassification
     - 取值范围 (Range)
     - 0..255
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 定义模式抑制是否影响ECU。 (Does pattern suppression affect the ECU?)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 至少在启用/允许唤醒抑制的情况下，应以非易失性方式存储（在复位期间必须保持该值）。可以在运行时使用ComM_SetECUGroupClassification()进行更改，因此默认值只能设置一次（第一次ECU 初始化）。 (At least when wake-up suppression is enabled/permitted, it should be stored in a non-volatile manner (and this value must be retained during reset). It can be changed at runtime using ComM_SetECUGroupClassification(), so the default value can only be set once (on the first ECU initialization).)
     - 
     - 
   * - ComMModeLimitationEnabled
     - 取值范围 (Range)
     - TRUE,FALSE
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 如果应启用模式限制功能，则为true。 (If the mode limit function should be enabled, then it is true.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无 (None)
     - 
     - 
   * - ComMPncGatewayEnabled
     - 取值范围 (Range)
     - TRUE,FALSE
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 如果应启用PNC网关，则为true。 (If PNC Gateway should be enabled, then true.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无 (None)
     - 
     - 
   * - ComMPNCPrepareSleepTimer
     - 取值范围 (Range)
     - 0..63
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - PNC 状态机应在COMM_PNC_PREPARE_SLEEP中等待的时间（以秒为单位）。 (The time (in seconds) that the PNC state machine should wait in COMM_PNC_PREPARE_SLEEP.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - #CanNm:(CanNmPnResetTime +ComMPNCPrepareSleepTimer)< CanNmTimeoutTime
     - 
     - 
   * - 
     - 
     - # FrNm:(FrNmPnResetTime +ComMPNCPrepareSleepTimer)< (
     - 
     - 
   * - 
     - 
     - (FrNmReadySleepCnt+1) \*FrNmRepetitionCycle\*“一个 FlexRay周期的持续时间”）
     - 
     - 
   * - 
     - 
     - # UdpNm:(UdpNmPnResetTime +ComMPNCPrepareSleepTimer)< UdpNmTimeoutTime
     - 
     - 
   * - ComMPNCSupport
     - 取值范围 (Range)
     - TRUE,FALSE
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 启用或禁用对PNC网络的支持。 (Enable or disable support for PNC network.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无 (None)
     - 
     - 
   * - ComMResetAfterForcingNoComm
     - 取值范围 (Range)
     - TRUE,FALSE
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 由于活动模式限制为“无通信”模式，ComM应在进入“无通信”模式后执行复位。 (Due to the activity mode limit being "No Communication" mode, ComM should execute a reset after entering the "No Communication" mode.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无 (None)
     - 
     - 
   * - ComMSynchronousWakeUp
     - 取值范围 (Range)
     - TRUE,FALSE
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 如果为真，一个通道的唤醒将导致所有通道的唤醒 (If true, waking one channel will cause all channels to wake up.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无 (None)
     - 
     - 
   * - ComMVersionInfoApi
     - 取值范围 (Range)
     - true, false
     - 默认取值 (Default value)
     - false
   * - 
     - 参数描述 (Parameter Description)
     - 获取版本信息的预处理开关 (Preprocessing switch for getting version information)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无 (None)
     - 
     - 
   * - ComMWakeupInhibitionEnabled
     - 取值范围 (Range)
     - TRUE,FALSE
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 如果唤醒抑制功能启用，则为True。 (If the wake-up inhibition function is enabled, then True.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无 (None)
     - 
     - 
   * - ComMMultiplePartitionEnabled
     - 取值范围 (Range)
     - TRUE,FALSE
     - 默认取值 (Default value)
     - FALSE
   * - 
     - 参数描述 (Parameter Description)
     - 启用/禁用多分区功能 (Enable/Disable Multi-Partition Function)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无 (None)
     - 
     - 
   * - ComMGlobalNvMBlockDescriptor
     - 取值范围 (Range)
     - Reference to[ NvMBlockDescriptor]
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 源自NvM配置 (Originated from NvM configuration)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无 (None)
     - 
     - 




ComMConfigSet
-----------------------------

.. centered:: **表 ComMConfigSet属性描述 (Table ComMConfigSet Property Description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - ComMPNCEnabled
     - 取值范围 (Range)
     - TRUE,FALSE
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 定义在此配置设置中是否启用部分网络。 (Define whether partial networking is enabled in this configuration setting.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 依赖于ComMPNCSupport使能 (Enable ComMPNCSupportdependency)
     - 
     - 





ComMChannel
===========================


.. centered:: **表 ComMChannel属性描述 (Table ComMChannel Property Description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - ComMBusType
     - 取值范围 (Range)
     - Enumeration
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 标识通道的总线类型。 (Specify the bus type for the identifier channel.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无 (None)
     - 
     - 
   * - ComMCDDBusPrefix
     - 取值范围 (Range)
     - String
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 用于 API 调用 CDD的前缀。 (Prefix for API call CDD.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 仅当ComMBusType等于COMM_BUS_TYPE_CDD时适用。 (Only applicable when ComMBusType equals COMM_BUS_TYPE_CDD.)
     - 
     - 
   * - ComMChannelId
     - 取值范围 (Range)
     - 0..255
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 对应通道的通道标识号。 (The channel identifier number for the corresponding channel.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 应与网络管理的通道id和总线接口协调。 (Should coordinate with the channel ID and bus interface of network management.)
     - 
     - 
   * - ComMFullCommRequestNotificationEnabled
     - 取值范围 (Range)
     - TRUE,FALSE
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 定义是否为此通道提供可选SenderReceiver端口的接口ComM_CurrentChannelRequest。 (Define the interface ComM_CurrentChannelRequest to indicate whether optional SenderReceiver ports are provided for this channel.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 应存储为非易失性（重置期间必须保留值）。 (Should be stored as non-volatile (values must be retained during reset).)
     - 
     - 
   * - ComMMainFunctionPeriod
     - 取值范围 (Range)
     - 0..65535
     - 默认取值 (Default value)
     - 0.02
   * - 
     - 参数描述 (Parameter Description)
     - 指定必须触发MainFunction的周期(以秒为单位)。 (Specify the周期 (in seconds) that must trigger MainFunction.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无 (None)
     - 
     - 
   * - ComMNoCom
     - 取值范围 (Range)
     - TRUE,FALSE
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - NoCom抑制功能的默认值 (The default value of NoCom抑制功能)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - ComMModeLimitationEnabled使能 (CommModeLimitationEnabled Enable)
     - 
     - 
   * - ComMNoWakeUpInhibitionNvmStorage
     - 取值范围 (Range)
     - TRUE,FALSE
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 如果此参数设置为“true”，则信道的NoWakeUp禁止状态应（以某种实现特定方式）存储在ComMGlobalNvmBlockDescriptor指向的块中。 (If this parameter is set to "true", the NoWakeUp disabled state of the channel should (in some implementation-specific manner) be stored in the block pointed to by ComMGlobalNvmBlockDescriptor.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 如果该参数设置为true，则必须在（现有的，即多重性1）ComMGlobalNvmBlockDescriptor中给出一个有效的 Nvm块引用，指向一个足够大的Nvm 块。 (If this parameter is set to true, a valid NVM block reference pointing to an adequate NVM block must be provided in (the existing, i.e., multiplicity 1) ComMGlobalNvmBlockDescriptor.)
     - 
     - 
   * - ComMNoWakeup
     - 取值范围 (Range)
     - TRUE,FALSE
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - NoWakeup抑制功能的默认值 (Default value of NoWakeup Inhibition功能)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 应存储为非易失性（重置期间必须保留值）。 (Should be stored as non-volatile (values must be retained during reset).)
     - 
     - 
   * - ComMPNCGatewayType
     - 取值范围 (Range)
     - Enumeration
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 标识 ComMChannel的PNC网络网关行为。 (Indicate the PNC network gateway behavior for ComMChannel.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 参数不得用于受管通道（不得设置为COMM_GATEWAY_TYPE_ACTIVE或COMM_GATEWAY_TYPE_PASSIVE）。 (Parameters shall not be used for managed channels (shall not be set as COMM_GATEWAY_TYPE_ACTIVE or COMM_GATEWAY_TYPE_PASSIVE).)
     - 
     - 
   * - ComMChannelPartitionRef
     - 取值范围 (Range)
     - Reference to [EcucPartition ]
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 根据ComMChannel被分配到的分区，引用EcucPartition。 (Based on the partition assigned to ComMChannel, reference EcucPartition.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无 (None)
     - 
     - 
   * - ComMManageReference
     - 取值范围 (Range)
     - Reference to [ComMChannel ]
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 表示managing通道和managed通道之间的引用。 (Represent references between managing channels and managed channels.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 不能配置ComMPncGatewayType，managedchannel对应的ComMNmVariant要求为LIGHT，managingchannel对应的ComMNmVariant要求为FULL (Cannot configure ComMPncGatewayType, managedchannel requires ComMNmVariant to be LIGHT, managingchannel requires ComMNmVariant to be FULL)
     - 
     - 




ComMNetworkManagement
-------------------------------------

.. centered:: **表  ComMNetworkManagement属性描述 (Table  ComMNetworkManagement Property Description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - ComMNmLightTimeout
     - 取值范围 (Range)
     - 0..255
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 定义离开COMM_FULL_COMMUNICATION子状态COMM_FULL_COM_READY_SLEEP的超时时间(以秒为单位)。 (Define the timeout duration (in seconds) for leaving the COMM_FULL_COMMUNICATION sub-state COMM_FULL_COM_READY_SLEEP.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 仅在将 ComMNmVariant配置为 ComMLight时使用 (Use only when ComMNmVariant is configured as ComMLight.)
     - 
     - 
   * - ComMNmVariant
     - 取值范围 (Range)
     - Enumeration
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 定义网络管理的功能。应与NM 配置协调。 (Define the functions of network management. Should coordinate with NM configuration.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 如果 ComMBusType =COMM_BUS_TYPE_INTERNAL，ComMNmVariant应为 NONE。 (If ComMBusType = COMM_BUS_TYPE_INTERNAL, ComMNmVariant should be NONE.)
     - 
     - 
   * - 
     - 
     - 对于managed通道，ComMNmVariant应为 LIGHT。 (For managed channels, ComMNmVariant should be LIGHT.)
     - 
     - 
   * - 
     - 
     - 对于managing通道，ComMNmVariant应为FULL。 (For managing channels, ComMNmVariant should be FULL.)
     - 
     - 
   * - ComMPNCNmRequest
     - 取值范围 (Range)
     - TRUE,FALSE
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 如果此参数等于真，则每次由于PNC 状态机更改为COMM_PNC_REQUESTED而请求 FULL通信时，应使用 API调用Nm_NetworkRequest。 (If this parameter is true, then an API call to Nm_NetworkRequest should be made using the API every time FULL communication is requested due to the PNC state machine changing to COMM_PNC_REQUESTED.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 只有当 ComMNmVariant为 FULL时才可以将ComMPNCNmRequest设置为 TRUE。 (Only set ComMPNCNmRequest to TRUE when ComMNmVariant is FULL.)
     - 
     - 




ComMUserPerChannel
----------------------------------

.. centered:: **表  ComMUserPerChannel属性描述 (Table  ComMUserPerChannel Property Description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - ComMUserChannel
     - 取值范围 (Range)
     - Reference to [ComMUser ]
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 对与此通道用户对应的ComMUser 的引用。 (Reference to the ComMUser corresponding to this channel user.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无 (None)
     - 
     - 




ComMPNC 
========================

.. centered:: **表 ComMPnc属性描述 (Table ComMPnc Property Description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - ComMPNCId
     - 取值范围 (Range)
     - 8..63
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - PNC标识号。 (PNC Identifier.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无 (None)
     - 
     - 
   * - ComMChannelPerPNC
     - 取值范围 (Range)
     - Reference to [ComMChannel ]
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 对这个PNC所需的ComMChannel的引用。 (Reference to the ComMChannel required for this PNC.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无 (None)
     - 
     - 
   * - ComMPNCEthIfSwitchPortGroupRef
     - 取值范围 (Range)
     - Reference to [EthIfSwitchPortGroup]
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 引用与此 PNC对应的PortGroups 。 (Reference the PortGroups corresponding to this PNC.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无 (None)
     - 
     - 
   * - ComMUserPerPNC
     - 取值范围 (Range)
     - Reference to [ComMUser ]
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 这个PNC对应的ComMUsers的引用。 (The reference to ComMUsers corresponding to this PNC.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无 (None)
     - 
     - 




ComMPNCComSignal
--------------------------------

.. centered:: **表 ComMPNCComSignal属性描述 (Table ComMPNCComSignal Property Description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - ComMPNCComSignalKind
     - 取值范围 (Range)
     - Enumeration
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 指示此 PNCComSignal是代表 EIRA 还是 ERAPNC 信息。 (Indicate whether this PNCComSignal represents EIRA or ERAPNC information.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无 (None)
     - 
     - 
   * - ComMPNCComSignalChannelRef
     - 取值范围 (Range)
     - Reference to [ComMChannel ]
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 参考ComMChannel，用于确定该PNCComSignal应是主动还是被动（通过ComMChannel 的参数ComMPNCGatewayType）。 (Refer to ComMChannel for determining whether this PNCComSignal should be active or passive (based on the parameters of ComMChannel, specifically ComMPNCGatewayType).)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - ComMPNCGatewayEnabled使能 (ComMPNCGatewayEnabled Enabled)
     - 
     - 
   * - ComMPNCComSignalRef
     - 取值范围 (Range)
     - Reference to [ComSignal ]
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 参考ComSignal，用于传输PN通道请求信息。 (Refer to ComSignal for transmitting PN channel request information.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无 (None)
     - 
     - 




ComMUser
========================

.. centered:: **表 ComMUser属性描述 (Table ComMUser Property Description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - ComMUserIdentifier
     - 取值范围 (Range)
     - 0..254
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 指代系统中指定请求通信模式的用户所需的标识符。 (Identifiers required for users specifying request communication modes in the reference system.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - EcuMUser：用户的概念与ECU状态管理器规范中的请求者概念非常相似。这两个参数应在配置过程中协调一致。 (EcuMUser: The concept of a user in this context is very similar to the requester concept in the ECU State Manager specification. These two parameters should be coordinated during the configuration process.)
     - 
     - 
   * - ComMUserModeNotification
     - 取值范围 (Range)
     - TRUE,FALSE
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 打开或关闭用户模式通知。 (Turn on or off user mode notifications.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无 (None)
     - 
     - 
   * - ComMUserEcucPartitionRef
     - 取值范围 (Range)
     - Reference to [EcucPartition ]
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 表示在哪个“EcucPartition”中执行请求者。当分区停止时，通信请求将在ComM中取消，以避免由于分区停止而导致总线保持唤醒的情况。 (Indicate in which "EcucPartition" the request is to be executed. When the partition stops, the communication request will be canceled in ComM to avoid keeping the bus awake due to the partition stop.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无 (None)
     - 
     - 
