===================
SoAd
===================
.. 标题标识符“===”的长度必须要大于其内容的长度，否则会报错，其他标题亦是如此


文档信息 Document Information
============================================================

版本历史 Version History
--------------------------------------------------------------------------------------------------------

.. list-table::
   :widths: 10 10 10 10 20
   :header-rows: 1

   * - 日期(Date)
     - 作者(Author)
     - 版本(Version)
     - 状态(Status)
     - 说明(Description)

   * - 2025/3/5
     - fupeng.yu
     - V0.1
     - 发布(Release)
     - 首次发布(First release)

   * - 2025/04/04
     - fupeng.yu
     - V1.0
     - 发布(Release)
     - 正式发布(Official release)

参考文档 References
--------------------------------------------------------------------------------------------------------

.. list-table::
   :widths: 10 10 30 10
   :header-rows: 1

   * - 编号(Number)
     - 分类(Classification)
     - 标题(Title)
     - 版本(Version)
   * - 1
     - Autosar
     - AUTOSAR_CP_SRS_Ethernet.pdf
     - R23-11
   * - 2
     - Autosar
     - AUTOSAR_CP_SWS_SocketAdaptor.pdf
     - R23-11 


术语与简写 Terms and Abbreviations
====================================================================


术语 Terms
--------------------------------------------------------------------------------------------------------
.. :align: center   表格内容居中(Table contents are centered)


.. list-table::
   :widths: 10 40
   :header-rows: 1

   * - 术语(Terms)
     - 解释(Explanation)

   * - AUTOSAR Connetor
     - SoAd（Socket Adaptor）充当不同PDU（协议数据单元）源/供应者与TCP/IP协议栈之间以及TCP/IP协议栈与不同PDU接收者/消费者之间的（解）复用器。术语AUTOSAR连接器指的是PDU的源/供应者或接收者/消费者。(SoAd (Socket Adaptor) serves as a (solution) multiplexer between different PDU (Protocol Data Unit) sources/providers and the TCP/IP protocol stack, as well as between the TCP/IP protocol stack and different PDU receivers/consumers.)  The term AUTOSAR connector refers to the source/supplier or receiver/consumer of PDU.)

   * - TCP socket connection
     - TCP传输协议的套接字连接

   * - UDP socket connection(UDP socket connection)
     - UDP传输协议的套接字连接

   * - IF-PDU(IF-PDU is the PDU sent/received via SoAd's IF-API)
     - IF-PDU是通过SoAd的IF-API发送/接收的PDU

   * - TP-PDU(TP-PDU is the PDU sent/received via SoAd's TP-API)
     - TP-PDU是通过SoAd的TP-API发送/接收的PDU

简写 Abbreviations
--------------------------------------------------------------------------------------------------------

.. list-table::
   :widths: 10 20 30
   :header-rows: 1


   * - 简写(Abbreviation)
     - 全称(Full name)
     - 解释(Explanation)

   * - ARP
     - Address Resolution Protocol
     - 地址解析协议

   * - DEM
     - Diagnostic Event Manager
     - 诊断事件管理器

   * - DET
     - Default Error Tracer
     - 默认错误跟踪

   * - DHCPv4
     - Dynamic Host Configuration Protocol
     - 动态主机配置协议

   * - DHCPv6
     - Dynamic Host Configuration Protocol for Internet Protocol Version 6
     - IPv6版的动态主机配置协议

   * - DoIP
     - Diagnostics over IP
     - IP的诊断

   * - HTTP
     - HyperText Transfer Protocol
     - 超文本传输协议

   * - IANA
     - Internet Assigned Numbers Authority
     - 互联网分配号码机构

   * - ICMPv4
     - Internet Control Message Protocol
     - Internet v4控制消息协议

   * - ICMPv6
     - Internet Control Message Protocol for Internet Protocol Version 6
     - Internet v6控制消息协议

   * - IETF
     - Internet Engineering Task Force
     - 互联网工程任务组

   * - IP
     - Internet Protocol
     - 互联网协议

   * - IPv4
     - Internet Protocol version 4
     - 互联网协议版本4

   * - IPv6
     - Internet Protocol version 6
     - 互联网协议版本6

   * - NDP
     - Neighbor Discovery Protocol
     - IPv6邻居发现协议

   * - Sd
     - Service Discovery
     - 服务发现

   * - TCP
     - Transmission Control Protocol
     - 传输控制协议

   * - TCP/IP
     - A family of communication protocols used in computer networks
     - 计算机网络中使用的通信协议家族

   * - TLS
     - Transport Layer Security
     - 安全传输层协议

   * - TP
     - Transport Protocol
     - 传输协议

   * - UDP
     - User Datagram Protocol
     - 用户数据报协议

   * - UdpNm
     - AUTOSAR UDP Network Management
     - AUTOSAR UDP网络管理

简介 Introduction
===================================================


SoAd 作为“通信桥梁”将上层基于 I-PDU 的通信，与下层基于 Socket 的TCP/UDP 通信连接起来。同时实现基于 Socket Connection 的连接控制，以及I-PDU 与 Socket Connection 的路由控制，并为上层提供相应接口。

SoAd, as the "communication bridge", connects the I-PDU-based upper layer communication and Socket-based lower layer TCP/UDP communication. It can also realize the connection control based on Socket Connection, as well as routing control between I-PDU and Socket Connection, and provide corresponding interfaces for the upper layer.

.. figure:: ../../../_static/参考手册/SoAd/SoAd_Autosar_Architecture.png
   :alt: SoAd模块在AUTOSAR架构中的位置 (Position of SoAd Module in AUTOSAR Architecture)
   :name: SoAd_Autosar_Architecture
   :align: center

   SoAd Architecture in AUTOSAR


如图 :ref:`SoAd_Autosar_Architecture` 所示，SoAd模块处于AUTOSAR架构中的通信服务层，其下层模块为TcpIp模块，上层模块为PduR,Sd,DoIP,UDPNm。

As shown in the figure :ref:`SoAd_Autosar_Architecture` , the SoAd module is in the communication service layer of the AUTOSAR architecture. Its lower and upper layer modules are the TcpIp module, and the PduR, Sd, DoIP, UDPNm.



功能描述 Functional Description
==========================================================


特性 Features
--------------------------------------------------------------------------------------------

.. only:: doc_pbs

  变体（Multi-variant support） Variant (Multi-variant support)
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  SoAd 模块支持PduRoute，SocketConnectionGroup,SocketRoute中一些配置项的配置的变体

  The SoAd module supports PduRoute, SocketConnectGroup, and variants of some configuration items in SocketRoute

Socket Connections 功能 Function of Socket Connections
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

为了实现上层 PDUs 与下层 Sockets 之前的通信映射， SoAd 模块定义了 Socket Connection 的概念。一个 Socket Connection 表示一个本端 socket（本端 IP 和本端 Port）与远端 socket（远端 IP 和远端 Port）的链接，以及该链接基于的传 输协议（UDP/TCP），是否使用 PDU Header，是否需求 buffer，传输协议相关参数等。

The SoAd module defines the concept of Socket Connection to realize the communication mapping between upper level PDUs and lower level Sockets. A Socket Connection indicates the linkage between a local socket (local IP and local Port) and a remote socket (remote IP and remote Port), the transmission protocol (UDP/TCP) on which the linkage is based, and that whether PDU headers are used, and whether buffers and transmission protocol-related parameters are required.

每个 Socket Connection 的模式根据 SoAd_SoConModeType 定义分为三种：SOAD_SOCON_ONLINE、 SOAD_SOCON_RECONNECT、SOAD_SOCON_OFFLINE。

By the definition of SoAd_SoConModeType, each Socket Connection can be divided into: SOAD_SOCON_ONLINE,  SOAD_SOCON_RECONNECT and SOAD_SOCON_OFFLINE.

1.Socket Connection Open：

当我们需要使能通信时，首先需要开启相应的 Socket Connections。开启的方式分为两种：手动方式（需上层模块调用 SoAd_OpenSoCon）、自动方式。初始化之后，每个 Socket Connection 都处于 SOAD_SOCON_OFFLINE 模式，执行Open 操作时根据每个 Socket Connection 的配置属性，其模式切换路线分两种：

To enable communication, open the corresponding Socket Connections first. There are two ways to enable it: Manual mode (calling SoAd_openSoCon by the upper layer) and automatic mode. After initialization, each Socket Connection will be under SOAD_SOCON_OFFLINE mode. When Open operation is executed, the mode switching line can be divided into two kinds based on the configuration attribute of each Socket Connection:

SOAD_SOCON_OFFLINE→SOAD_SOCON_ONLINE；SOAD_SOCON_OFFLINE→SOAD_SOCON_RECONNECT→SOAD_SOCON_ONLINE。只有当处于 SOAD_SOCON_ONLINE 模式时才能通过该 SocketConnection 发送/接收数据（属于 UDP 的 Socket Connection 可以在SOAD_SOCON_RECONNECT 模式下响应 SoAd_RxIndication，在该 API 中先切换到 SOAD_SOCON_ONLINE 模式，再执行数据接收处理）。

SOAD_SOCON_OFFLINE→SOAD_SOCON_ONLINE; SOAD_SOCON_OFFLINE→SOAD_SOCON_RECONNECT→SOAD_SOCON_ONLINE. Data be sent/received through this SocketConnection only under SOAD_SOCON_ONLINE (Socket Connection that belongs to UDP can respond to SoAd_rxCondition in SOAD_SOCON-CONNECT mode, switch to SOAD_SOCON-ONLINE mode in this API first, and then receive and process data).

2.Socket Connection Close：

Socket Connection 的关闭分为主动请求关闭（上层模块调用 SoAd_CloseSoCon），以及异常关闭，如下层模块检测到错误事件，通过SoAd_TcpIpEvent 通知到 SoAd 模块； UDP 报文接收超时； TP PDU 收发过程中出现错误/取消等。只有在执行主动请求关闭时， Socket Connection 的模式才能切换到 SOAD_SOCON_OFFLINE，别的情况都切换到SOAD_SOCON_RECONNECT 模式。

The closing Socket Connection can be further divided into active request closing (calling SoAd_ClosseSoCon by upper layer module) and abnormal closing. Upon detecting an error event, the lower layer module will notify the SoAd module through SoAd_TcpIpEvent; UDP packet reception timeout; errors/cancellations occur during the transmission and receiving process of TP PDUs. While executing active request closing, Socket Connection mode will be switched to SOAD_SOCON_OFFLINE but to SOAD_SOCON_RECONNECT mode under other circumstances.

3.Socket Connection Open/Close Sequence Remarks：

Socket Connection 的开启及关闭是异步的，任务队列只能缓存两个不同的任务请求，多余的任务根据策略进行舍弃或者撤销（revoke）队列中的任务。

The opening and closing of Socket Connection are asynchronous. The task queue can only cache two different task requests. Excess tasks will be discarded or revoked from the tasks in the queue according to the strategy.

4.Notifications：

当 Socket Connection 的模式切换时，可以通过调用<Up>_SoConModeChg()函数通知上层模块。

Switch the mode of Socket Connection after notifying the upper layer module by calling <Up>_SoConModeChg() function.

当 Socket Connection 关联的 IP 地址（本端）状态切换时，可以通过调<Up>_LocalIpAddrAssignmentChg()函数通知上层。

Switch the status of the IP address (local) linked with Socket Connection after notifying the upper layer by calling <Up>_LocalIpAddrAssignmentChg() function.


PDU Transmission 功能 Function of PDU Transmission
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

SoAd 通过 PDU route(SoAdPduRoute, SoAdPduRouteDest)将 PDU 映射到socket connection，进而通过其关联的 UDP/TCP Socket 进行发送。SoAd 提供 IF、TP 两种 PDU 发送方式。

SoAd maps PDUs to socket connections through PDU route (SoAdPduRoute, SoAdPduRouteDest), and then sends them via the linked UDP/TCP sockets. SoAd supports PDU sending by IF and TP.

1.PDU Transmission via IF-API：

对于数据长度较小的 PDU，通常使用 IF 发送方式。在 SoAd 中支持 IF PDU的 1： n 路由发送。

For PDUs with smaller data lengths, IF transmission is generally used. 1: n routing transmission for IF PDU is supported in SoAd.

2.PDU Transmission via IF-API and nPduUdpTxBuffer：

当 Socket Connection（UDP 类型）关联的所有发送 PDU 都是“IF”类型,使能PDU Header，其关联的 SoAdPduRouteDests 至少有一个 SoAdTxUdpTriggerMode配置为 TRIGGER_NEVER 模式。SoAd 将使能该 Socket Connection 的nPduUdpTxBuffer 机制。

When all PDU sending linked with Socket Connection (UDP type) is of "IF" type and PDU Header is enabled, the linked SoAdPduRouteDests must have at least one SoAdTxUdpTriggerMode that is configured as TRIGGER_NEVER mode. SoAd will enable the nPduUdpTxBuffer mechanism of this Socket Connection.

nPduUdpTxBuffer 机制，能够将多个 IF PDU 封装在一个 UDP 报文中进行统一发送，以达到节省带宽的目的。

The nPduUdpTxBuffer mechanism can encapsulate several IF PDUs into one UDP packet for unified transmission, in order to save bandwidth.

3.PDU Transmission via IfRoutingGroupTransmit API：

SoAd 支持上层模块（通常为 Sd 模块），通过 Trigger Transmit 方式请求RoutingGroup 关联的部分或者所有 IF PDUs 的发送。

SoAd supports upper level modules (Sd modules in general) to request the sending of part or all IF PDUs linked with RoutingGroup through Trigger Transmit.

上面提到的部分 IF PDUs 指的是关联到某一特定 Socket Connection 的 PDUs。

Some IF PDUs above refer to the PDUs linked with a specific Socket Connection.

4.PDU Transmission via TP-API：

对于上层模块数据长度较大的 PDU，通常通过 TP 方式进行发送。TP 发送不支持 PDU 的 1： n 路由。

PDUs with longer data lengths in upper level modules are generally sent through TP. TP transmission does not support 1: n routing of PDU.


PDU Header option 功能 Function of PDU Header option
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

SoAd 支持 PDU Header 功能， PDU Header 由 4 字节的 Header ID,4 字节的PDU 数据长度组成（大端字节序）。当 Socket Connection 关联到多个接收 PDU，以及需要用到 nPduUdpTxBuffer 机制等情况时，都需要 PDU Header 功能的支持。

SoAd supports PDU Header function. PDU Header consists of a 4-byte Header ID and a 4-byte PDU data length (big endian byte order). PDU Header is required, when Socket Connection links with several receiving PDUs and requires nPduUdpTxBuffer mechanism.

PDU Reception 功能 Function of PDU Reception
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PDU 的接收，在 SoAd 中通过 Socket Route (SoAdSocketRoute,SoAdSocketRouteDest)来实现，将通过 UDP/TCP Socket 获取的报文映射到 PDUs。当前 Socket Route 仅支持 1： 1 路由（即一个 SoAdSocketRoute 只能包含一个SoAdSocketRouteDest），但需注意的是一个 Socket Connection 可以关联多个SoAdSocketRoute。SoAd 与上层模块 PDU 接收同样有两种方式： IF 接收、 TP 接收。

In SoAd, PDUs is received through Socket Route (SoAdSocketRoute, SoAdSocketRouteDest) and is  mapped by the message obtained through UDP/TCP Socket. At present, Socket Route only supports 1:1 routing (i.e. one SoAdSocketRoute can only contain one SoAdSocketRouteDest). However, a Socket Connection can be linked with multiple SoAdSocketRoutes. There are two receiving methods for SoAd and upper layer module PDU: IF and TP.

Best Match Algorithm 功能 Function of Best Match Algorithm
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

该最佳匹配算法是根据提供的 remote address（IP 和 Port）从 SocketConnection Group 中选择出最佳匹配的 Socket Connection。

The best matching algorithm is the most matched Socket Connection selected from the SocketConnection Group based on the provided remote address (IP and Port).


Message Acceptance Policy 功能 Function of Message Acceptance Policy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

该功能用于接收远端节点（remote nodes）发送报文的过滤。当该功能使能时， Socket Connection 只能接收指定的某个/某些远端节点发送来的报文。当该功能不使能时， Socket Connection 将接收所有远端节点发送来的报文。

This function is used for filtering the messages sent by remote nodes. After this function is enabled, Socket Connection can receive messages from the designated one or some remote nodes only. If this function is not enabled, Socket Connection can receive the messages from all remote nodes.


TP PDU Cancelation 功能 Function of TP PDU Cancelation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

TP PDU 的传输支持中途取消，分为接收取消和发送取消。

The transmission of TP PDU can be cancelled in the middle way and can be further divided into receiving cancellation and sending cancellation.


Disconnection and recovery 功能 Function of Disconnection and recovery
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

在 SoAd_MainFunction 中，将会对需要断开连接的 Socket Connection 进行连接关闭，其关闭后 Socket Connection 状态分为两种情况：SOAD_SOCON_OFFLINE 和 SOAD_SOCON_RECONNECT。对于处于 SOAD_SOCON_RECONNECT 状态的 Socket Connection， SoAd 将会自动尝试恢复连接。

In SoAd_SainFunction, the Socket Connection that needs to be disconnected will be closed. After being closed, the Socket Connection status will have two conditions: SOAD_SOCON_OFFLINE and SOAD_SOCON_RECONNECT.For Socket Connection under the status of SOAD_SOCON_RECONNECT, SoAd will try to recover connection automatically.


Routing Groups 功能 Function of Routing Groups
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

SoAd 支持对每个 Routing Group 的使能状态进行控制，进而控制各 RoutingGroup 关联的 SoAdPduRouteDest 或者 SoAdSocketRouteDest。只有当 RouteDest处于使能状态时，才能执行新 PDU 的收发。

SoAd can control the enabling status of each Routing Group, thereby controlling the SoAdPduRouteDest or SoAdSocketRouteDest linked with each Routing Group. The new PDU cannot be sent or received until RouteDest is enabled.



Buffer handling 功能 Function of Buffer handling
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

在 SoAd 的报文收发过程中，有些情况下需要用到合适的 buffer 来缓存需要发送的数据及接收到的数据。

When the messages in SoAd are sent or received, appropriate buffers are needed in some cases to cache the data that needs sending and receiving.



偏差 Deviation
--------------------------------------------------------------------
None



扩展 Extension
--------------------------------------------------------------------
None

集成 Integration
========================================

文件列表 File List
--------------------------------------------------------------------

静态文件 Static Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - 文件(File)
     - 描述(Description)

   * - SoAd.h
     - 实现SoAd模块全部外部接口的声明（除了回调函数），以及配置文件中全局变量的声明。(Declares all external interfaces of the SoAd module (except for callback functions) and the global variables in the configuration file.)

   * - SoAd_Internal.h
     - 实现SoAd模块内部的数据类型和宏定义，还有接口的声明。(Declares the realization of data types and macro definitions within the SoAd module, as well as interface.)

   * - SoAd_Types.h
     - 实现外部/内部类型的定义，包括 AUTOSAR 标准定义的类型，以及 PB/PC 配置参数结构体类型，以及内部运行时结构体类型。(Implements definitions of external/internal types, including types defined by AUTOSAR standards, PB/PC configuration parameter structure types, and internal runtime structure types.)

   * - SoAd_Cbk.h
     - 实现 SoAd 模块全部回调函数的声明。(Implements the declaration of all callback functions of the SoAd module)

   * - SoAd.c
     - 作为 SoAd 模块的核心文件，实现 SoAd 模块全部对外接口，以及实现 SoAd 模块功能所必须的 local 函数， local 宏定义， local 变量定义。(As the core file of SoAd module, it can realize all external interfaces of SoAd module, as well as all local functions, local macro definitions and local variable definitions which are required for realizing SoAd module function.)

动态文件 Dynamic Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - 文件(File)
     - 描述(Description)

   * - SoAd_Cfg.h
     - 定义 SoAd 模块 PC 配置的宏定义。(Defines the macro definitions for SoAd module PC configuration.)

   * - SoAd_Cfg.c
     - 定义 SoAd 模块 PC 配置的结构体参数。(Defines the structural parameters for SoAd module PC configuration.)

   * - SoAd_PBcfg.h
     - 声明 SoAd 模块 PB 配置的结构体。(Declares the structure of the SoAd module PB configuration.)

   * - SoAd_PBcfg.c
     - 定义 SoAd 模块 PB 配置的结构体参数。(Defines the structural parameters for the PB configuration of the SoAd module.)

错误处理 Error Handling
--------------------------------------------------------------------



开发错误 Development Errors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. list-table:: 
   :widths: 20 10 30
   :header-rows: 1

   * - Error code
     - Value[hex]
     - Description

   * - SOAD_E_NOTINIT
     - 0x01
     - API service called before initializing the module

   * - SOAD_E_PARAM_POINTER
     - 0x02
     - API service called with NULL pointer

   * - SOAD_E_INV_ARG
     - 0x03
     - Invalid argument

   * - SOAD_E_INV_PDUID
     - 0x06
     - Invalid PDU ID

   * - SOAD_E_INV_SOCKETID
     - 0x07
     - Invalid socket address

   * - SOAD_E_INIT_FAILED
     - 0x08
     - Invalid configuration set selection

   * - SOAD_E_INVALID_PARTITION
     - 0x80
     - Invalid partition ID

产品错误 Product Errors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
None

运行时错误 Runtime Errors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. list-table:: 
   :widths: 20 10 30
   :header-rows: 1

   * - Error code
     - Value[hex]
     - Description

   * - SOAD_E_NOBUFS
     - 0x04
     - No buffer space available

   * - SOAD_E_INV_PDUHEADER_ID
     - 0x05
     - Unknown PduHeader ID

   * - SOAD_E_TCP_AUTOCONNECT_FAILED
     - 0x10
     - Automatic TCP connection failed

接口描述 Interface Description
==============================================================

类型定义 Type Definitions
--------------------------------------------------------------------------------------------
.. include:: SoAd_Types_h_api.rst

      
提供的服务 Services
--------------------------------------------------------------------------------------------
.. include:: SoAd_h_api.rst

回调函数 Callback Function
--------------------------------------------------------------------------------------------
.. include:: SoAd_Cbk_h_api.rst


依赖的服务 Applicable Services
--------------------------------------------------------------------------------------------

强制接口 Compulsory interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. list-table::
   :widths: 10 5 30
   :header-rows: 1

   * - API Function
     - Header File
     - Description

   * - Det_ReportRuntimeError 
     - Det.h
     - Service to report runtime errors. If a callout has been configured then this callout shall be called.

   * - TcpIp_<Up>GetSocket 
     - TcpIp.h
     - By this API service the TCP/IP stack is requested to allocate a new socket. Note: Each accepted incoming TCP connection also allocates a socket resource.

   * - TcpIp_Bind 
     - TcpIp.h
     - By this API service the TCP/IP stack is requested to bind a UDP or TCP socket to a local resource.

   * - TcpIp_ChangeParameter 
     - TcpIp.h
     - By this API service the TCP/IP stack is requested to change a parameter of a socket. E.g. the Nagle algorithm may be controlled by this API.

   * - TcpIp_Close
     - TcpIp.h
     - By this API service the TCP/IP stack is requested to close the socket and release all related resources.


   * - TcpIp_GetCtrlIdx
     - TcpIp.h
     - TcpIp_GetCtrlIdx returns the index of the controller related to LocalAddrId.

   * - TcpIp_GetIpAddr
     - TcpIp.h
     - Obtains the local IP address actually used by Local AddrId, the netmask and default router

   * - TcpIp_GetPhysAddr
     - TcpIp.h
     - Obtains the physical source address used by the EthIf controller implicitly specified via LocalAddrId.

   * - TcpIp_GetRemotePhysAddr
     - TcpIp.h
     - TcpIp_GetRemotePhysAddr queries the IP/physical address translation table specified by CtrlIdx and returns the physical address related to the IP address specified by IpAddrPtr. In case no physical address can be retrieved and parameter initRes is TRUE, address resolution for the specified IP address is initiated on the local network.

   * - TcpIp_ReleaseIpAddrAssignment 
     - TcpIp.h
     - By this API service the local IP address assignment for the IP address specified by LocalAddrId shall be released.

   * - TcpIp_RequestComMode
     - TcpIp.h
     - By this API service the TCP/IP stack is requested to change the TcpIp state of the communication network identified by EthIf controller index.

   * - TcpIp_RequestIpAddrAssignment
     - TcpIp.h
     - By this API service the local IP address assignment for the IP address specified by LocalAddrId shall be initiated.

   * - TcpIp_TcpConnect
     - TcpIp.h
     - By this API service the TCP/IP stack is requested to establish a TCP connection to the configured peer.

   * - TcpIp_TcpListen
     - TcpIp.h
     - By this API service the TCP/IP stack is requested to listen on the TCP socket specified by the socket identifier.

   * - TcpIp_TcpReceived
     - TcpIp.h
     - By this API service the reception of socket data is confirmed to the TCP/IP stack.

   * - TcpIp_TcpTransmit
     - TcpIp.h
     - This service requests transmission of data via TCP to a remote node. The transmission of the data is decoupled.

   * - TcpIp_UdpTransmit
     - TcpIp.h
     - This service transmits data via UDP to a remote node. The transmission of the data is immediately performed with this function call by forwarding it to EthIf.


可选接口 Optional Interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 10 5 30
   :header-rows: 1

   * - API Function
     - Header File
     - Description

   * - Det_ReportError 
     - Det.h
     - Service to report development errors.

   * - PduR_SoAdTpCopyRxData
     - PduR_SoAd.h
     - This function is called to provide the received data of an I-PDU segment (N-PDU) to the upper layer. Each call to this function provides the next part of the I-PDU data. The size of the remaining buffer is written to the position indicated by bufferSizePtr.

   * - TcpIp_DhcpReadOption
     - TcpIp.h
     - By this API service the TCP/IP stack retrieves DHCP option data identified by parameter option for already received DHCP options.


   * - TcpIp_DhcpV6ReadOption
     - TcpIp.h
     - By this API service the TCP/IP stack retrieves DHCPv6 option data identified by parameter option for already received DHCPv6 options.

   * - TcpIp_DhcpV6WriteOption
     - TcpIp.h
     - By this API service the TCP/IP stack writes the DHCPv6 option data identified by parameter option.

   * - TcpIp_DhcpWriteOption 
     - TcpIp.h
     - By this API service the TCP/IP stack writes the DHCP option data identified by parameter option.

配置接口 Configuration Interfaces
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. list-table::
   :widths: 10 5 30
   :header-rows: 1

   * - API Function
     - Header File
     - Description

   * - <Up>_[SoAd][If]RxIndication 
     - PduR_SoAd.h/UdpNm.h/Sd.h/DoIP_Cbk.h/XcpOnEth_Cbk.h/CDD_Cbk.h
     - Indication of a received PDU from a lower layer communication interface module.

   * - <Up>_[SoAd][If]TriggerTransmit 
     - PduR_SoAd.h
     - Within this API, the upper layer module (called module) shall check whether the available data fits into the buffer size reported by PduInfoPtr->SduLength.

   * - <Up>_[SoAd][If]TxConfirmation 
     - PduR_SoAd.h/UdpNm.h
     - The lower layer communication interface module confirms the transmission of a PDU, or the failure to transmit a PDU.

   * - <Up>_[SoAd][Tp]StartOfReception 
     - PduR_SoAd.h/DoIP_Cbk.h
     - This function is called at the start of receiving an N-SDU. The N-SDU might be fragmented into multiple N-PDUs (FF with one or more following CFs) or might consist of a single N-PDU (SF). The service shall provide the currently available maximum buffer size when invoked with TpSdu Length equal to 0.

   * - <Up>_[SoAd][Tp]CopyRxData
     - PduR_SoAd.h/DoIP_Cbk.h
     - This function is called to provide the received data of an I-PDU segment (N-PDU) to the upper layer. Each call to this function provides the next part of the I-PDU data. The size of the remaining buffer is written to the position indicated by bufferSizePtr.

   * - <Up>_[SoAd][Tp]RxIndication
     - PduR_SoAd.h/DoIP_Cbk.h
     - Called after an I-PDU has been received via the TP API, the result indicates whether the transmission was successful or not.

   * - <Up>_[SoAd][Tp]CopyTxData
     - PduR_SoAd.h/DoIP_Cbk.h
     - This function is called to acquire the transmit data of an I-PDU segment (N-PDU). Each call to this function provides the next part of the I-PDU data unless retry->TpDataState is TP_DATARETRY.

   * - <Up>_[SoAd][Tp]TxConfirmation
     - PduR_SoAd.h/DoIP_Cbk.h
     - This function is called after the I-PDU has been transmitted on its network, the result indicates whether the transmission was successful or not.

   * - <Up>_SoConModeChg
     - PduR_SoAd.h/DoIP_Cbk.h/Sd.h
     - Notification about a SoAd socket connection state change, e.g. socket connection gets online

   * - <Up>_LocalIpAddrAssignmentChg
     - PduR_SoAd.h/DoIP_Cbk.h/Sd.h
     - This function gets called by the SoAd if an IP address assignment related to a socket connection changes (i.e. new address assigned or assigned address becomes invalid).

配置 Configuration
====================================

SoAd Socket Connection
--------------------------------------------------------------

.. figure:: ../../../_static/参考手册/SoAd/SoAdSocketConnectionGroup.png
   :name: SoAd_SoAdSocketConnectionGroup
   :align: center

   SoAdSocketConnectionGroup

SoAd模块的Socket Connection是在SoAdSocketConnectionGroup中配置的,SoAdSocketConnectionGroup配置了该Socket Connection的端口，是否自动连接，PduHeader是否使能，是否通知上层Ip地址分配变化和连接模式改变，TP接收缓存大小的配置等。而SoAdSocketConnection中配置了远端的IP和端口，在SoAdSocketConnectionGroup中还要配置该连接是UDP还是TCP连接

The Socket Connection of the SoAd module is configured in the SoAdSocketconnectionGroup, which comes with the port for the Socket Connection, in order to realize automatic connection, enabling of PduHeader, and the upper layer is notified of the changes on IP address allocation and connection mode, and the configuration of TP receiving cache size.The remote IP and port are configured in SoAdSocketConnection. In SoAdSocketConnection Group, configure the specific connection (UDP or TCP).

发送PDU Send PDU
--------------------------------------------------------------

.. figure:: ../../../_static/参考手册/SoAd/SoAdPduRouteDest.png
   :name: SoAd_SoAdPduRouteDest
   :align: center

   SoAdPduRouteDest

上层发送PDU 是在SoAdPduRoute中配置的，可以配置该PDU路由（SoAdPduRouteDest）到不同的SocketConnection中让后将其发出,SoAdPduRouteDest还可以选择关联RoutingGroup，通过RoutingGroup控制该PDU的发送。

The PDU sending by upper layer is configured in SoAdPduRoute. The PDU can be routed (SoAdPduRouteDest) to different SocketConnections for sending. SoAdPduRouteDest can also be linked with RoutingGroup to control PDU sending.

接收PDU Receive PDU
--------------------------------------------------------------

.. figure:: ../../../_static/参考手册/SoAd/SoAdSocketRouteDest.png
   :name: SoAd_SoAdSocketRouteDest
   :align: center

   SoAdSocketRouteDest

接收PDU在SoAdSocketRoute配置，通过SocketConnection接收的报文转化为PDU后，把该PDU通知给上层模块，可以将加收的PDU通过SoAdSocketRouteDest配置后路由到多个上层模块中

Receive the configuration of PDU in SoAdSocketRoute; after converting the received message into PDU through SocketConnection, notify the upper layer module of the PDU. The received PDU can be routed to several upper layer modules through SoAdSocketRouteDest configuration


