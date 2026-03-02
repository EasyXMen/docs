====================
TcpIp
====================

文档信息 Document Information
============================================================

版本历史 Version History
------------------------------------------------------------------------------------------------------

.. list-table::
   :widths: 10 10 10 10 20
   :header-rows: 1

   * - 日期(Date)
     - 作者(Author)
     - 版本(Version)
     - 状态(Status)
     - 说明(Description)

   * - 2024/3/3
     - miao.wang
     - V0.1
     - 发布(Release)
     - 首次发布(First release)

   * - 2025/04/04
     - miao.wang
     - V1.0
     - 发布(Release)
     - 正式发布(Official release)


参考文档 References
---------------------------------------------------------------------------------------

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
     - AUTOSAR_SWS_TCPIP.pdf
     - R23-11


术语与简写 Terms and Abbreviations
====================================================================

.. 术语 Terms
.. -------------------------------------------------

简写 Abbreviations
------------------------------------------------------------

.. list-table::
   :widths: 10 20 30
   :header-rows: 1

   * - 简写(Abbreviation)
     - 全称(Full name)
     - 解释(Explanation)
   * - ARP
     - Address Resolution Protocol
     - 地址解析协议
   * - DHCP
     - Dynamic Host Configuration Protocol
     - 动态主机配置协议
   * - ICMP
     - Internet Control Message Protocol
     - 以太网控制消息协议
   * - IP
     - Internet Protocol
     - 以太网协议
   * - MTU
     - Maximum Transmission Unit
     - 最大传输单元
   * - TCP
     - Transmission Control Protocol
     - 传输控制协议
   * - UDP
     - User Datagram Protocol
     - 用户数据报协议
   * - TCP/IP
     - A family of communication protocols used in computer networks
     - TCP/IP协议簇
   * - LwIP
     - A Lightweight TCP/IP stack
     - 一种轻量级TCP/IP协议栈



简介 Introduction
==================================

在AUTOSAR架构中，TcpIp模块介于SoAd模块和EthIf模块之间，TcpIp模块软件的设计是在遵循AUTOSAR R23-11规范的情况下，基于lwip代码开发而来。

In the AUTOSAR architecture, the TcpIp module is located between the SoAd module and the EthIf module.The software design of the TcpIp module is developed based on the lwip code while complying with the AUTOSAR R23-11 specification.

由于开发需求(暂时只实现IPv4)，AUTOSAR规范本身存在的一些问题，以及lwip实现的功能情况，TcpIp模块代码并未完全实现AUTOSAR规范所有功能。

Due to development requirements (only IPv4 is implemented temporarily), certain issues existing in the AUTOSAR specification itself, and the functional implementation status of lwip,the TcpIp module code does not fully implement all functions specified in the AUTOSAR specification.

TcpIp模块的主要功能为：

The main functions of the TcpIp module are as follows:

1.为上层模块提供TCP、UDP数据报的收发接口(TCP涉及链接)；

1.Provide upper-layer modules with interfaces for sending and receiving TCP and UDP datagrams (TCP involves connections);

2.基于IP数据报实现TCP/UDP数据报的封装、解析；

2.Implement encapsulation and parsing of TCP/UDP datagrams based on IP datagrams;

3.实现IP数据报收发所需要的DHCP、ICMP、ARP、AUTO-IP协议功能；

3.Implement the functions of DHCP, ICMP, ARP, and AUTO-IP protocols required for sending and receiving IP datagrams;

4.基于以太网数据报实现IP/ARP数据报的封装、解析。

4.Implement encapsulation and parsing of IP/ARP datagrams based on Ethernet datagrams.

.. figure:: ../../../_static/参考手册/TcpIp/image1.png
   :name: TcpIp_arch
   :align: center

   TcpIp模块层次图 (TcpIp Module Layer Diagram)


功能描述 Functional Description
==========================================================

System Scalability功能介绍 Introduction to System Scalability Function
---------------------------------------------------------------------------------------------------------------------------------------

根据不同的应用情况，TcpIp模块的功能(对IP协议的支持情况)分为三个等级。因开发需求，目前只支持IPv4，因此只支持SC1功能。

According to different application scenarios, the functions of the TcpIp module (support for IP protocols) are divided into three levels. Due to development requirements, only IPv4 is supported currently, so only the SC1 function is supported.

.. figure:: ../../../_static/参考手册/TcpIp/image2.png
   :name: scalability
   :align: center

   TcpIp模块功能等级 (TcpIp Module Function Levels)

Internet Protocol Version 4功能介绍 Introduction to Internet Protocol Version 4 Function
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

IP协议是整个TCP/IP协议的核心，UDP、TCP、ICMP等协议都是基于IP来传送协议数据。IP协议是一种不可靠，尽最大努力，无连接的网络层协议。除了实现最基本的IP数据报的收发外，还需要完成IP数据报(长度较大)的分片和重组功能。

The IP protocol is the core of the entire TCP/IP protocol suite. Protocols such as UDP, TCP, and ICMP all transmit protocol data based on IP. The IP protocol is an unreliable, best-effort, connectionless network-layer protocol. In addition to implementing the basic sending and receiving of IP datagrams, it is also necessary to complete the fragmentation and reassembly functions for IP datagrams (with large lengths).

ARP协议，译作地址解析协议，ARP只适用于IPv4，在以太网中ARP数据报封装在以太网帧中进行发送。ARP协议的基本功能是使用目标主机的IP地址，查询其对应的MAC地址，以保证底层链路上数据报通信的进行。为了实现在网络接口中物理地址与IP地址间的转换，ARP协议中引入了缓存表的概念(记录了一条一条的<IP地址，MAC地址>对)。

The ARP protocol, translated as Address Resolution Protocol, is only applicable to IPv4. In Ethernet, ARP datagrams are encapsulated in Ethernet frames for transmission.The basic function of the ARP protocol is to use the IP address of the target host to query its corresponding MAC address, so as to ensure the transmission of datagrams on the underlying link.To realize the conversion between physical addresses and IP addresses in network interfaces, the ARP protocol introduces the concept of a cache table (which records <IP address, MAC address> pairs one by one).

AUTOIP协议是一个不用服务器来获取IP地址方法的协议，而DHCP需要一个服务器。一个配置了AUTOIP的主机将会得到一个高16 位为0xa9fe的IP地址(即169.254.xxx.xxx)。

The AUTOIP protocol is a protocol that obtains an IP address without a server, whereas DHCP requires a server.A host configured with AUTOIP will obtain an IP address whose upper 16 bits are 0xa9fe (i.e., 169.254.xxx.xxx).

IP协议完成了数据报在各个主机之间的递交，但是它并不完美，正如前面所说，它提供的是一种无连接的不可靠的数据报交付，协议本身不提供任何错误检验与恢复机制。

The IP protocol completes the delivery of datagrams between various hosts, but it is not perfect. As mentioned earlier,it provides a connectionless and unreliable datagram delivery service, and the protocol itself does not provide any error checking and recovery mechanisms.

为了弥补IP协议的缺陷，出现了ICMP协议。ICMP协议用于在主机、路由器之间传递控制消息(如数据报错误信息、网络状况信息、主机状况信息等)。ICMP协议配合IP协议完成数据报的递交，提高数据报递交的有效性，但是ICMP协议报文有着自己的组织结构，且ICMP报文是被封装在IP数据报中发送的。此外，ping命令，其本质上就是发送一个ICMP回送请求报文。

To make up for the shortcomings of the IP protocol, the ICMP protocol was introduced. The ICMP protocol is used to transmit control messages (such as datagram error information, network status information, host status information, etc.) between hosts and routers. The ICMP protocol cooperates with the IP protocol to complete the delivery of datagrams and improve the effectiveness of datagram delivery. However, ICMP protocol messages have their own organizational structure, and ICMP messages are encapsulated in IP datagrams for transmission. In addition, the ping command essentially sends an ICMP echo request message.

IP Based Protocols功能介绍 Introduction to IP Based Protocols Function
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

TcpIp模块维护一个本端IP地址表，每个本端IP地址的配置参见配置TcpIpLocalAddr，主要实现IP地址由何种方式分配，每个TcpIpLocalAddr有唯一的ID号(TcpIpAddrId)表示。

The TcpIp module maintains a local IP address table. The configuration of each local IP address refers to the configuration of TcpIpLocalAddr,which mainly specifies how the IP address is assigned. Each TcpIpLocalAddr is represented by a unique ID (TcpIpAddrId).

虽然按AUTOSAR标准，可支持N个本端IP地址关联到同一个硬件Controller，但限于LwIP功能实现，我们目前只支持每个TcpIpCtrl只能被一个单播(TCPIP_UNICAST)TcpIpLocalAddr关联。

Although according to the AUTOSAR standard, N local IP addresses can be associated with the same hardware Controller, limited by the functional implementation of LwIP,currently we only support that each TcpIpCtrl can be associated with only one unicast (TCPIP_UNICAST) TcpIpLocalAddr.

UDP称为用户数据报协议，是一种无连接的、不可靠的传输协议。

UDP, known as User Datagram Protocol, is a connectionless and unreliable transport protocol.

UDP只是简单地完成数据从一个进程到另一个进程的交付，它没有提供任何流量控制机制，收到的报文也没有确认；

UDP simply completes the delivery of data from one process to another. It does not provide any flow control mechanism, and there is no acknowledgment for received messages;

在差错控制上，只提供了一种简单的差错控制方法，即校验和计算，当UDP收到的报文校验和计算不成功时，它将丢弃掉这个报文。

In terms of error control, it only provides a simple error control method, namely checksum calculation. When the checksum calculation of a received UDP message fails, the message will be discarded.

UDP使用网络层的IP协议来发送报文。

UDP uses the IP protocol at the network layer to send messages.

TCP称为传输控制协议，是一种面向连接的、可靠的、基于字节流的传输层协议。为了保证传输的可靠性、高效性，TCP提供了一系列的机制，例如握手机制、正面确认、超时重传、以及各种定时机制等。

TCP, known as Transmission Control Protocol, is a connection-oriented, reliable, byte-stream-based transport layer protocol.
To ensure the reliability and efficiency of transmission, TCP provides a series of mechanisms,such as a handshake mechanism, positive acknowledgment, timeout retransmission, and various timing mechanisms.

AUTOSAR标准中涉及的机制(TCP配置 )有：超时重传；慢启动与拥塞避免；快速重传与快速恢复；NAGLE算法；保活机制；收发窗口机制；定时机制。

The mechanisms involved in the AUTOSAR standard (TCP configuration) include: timeout retransmission; slow start and congestion avoidance; fast retransmission and fast recovery; NAGLE algorithm; keep-alive mechanism; send and receive window mechanisms; timing mechanisms.

DHCP使用UDP进行报文的传输。通过同DHCP服务器的交互，设备可以获得一个有效的IP地址，使得它可以在特定网络环境下运行。目前不支持DHCPv4和DHCPv6功能。

DHCP uses UDP for message transmission. Through interaction with a DHCP server, a device can obtain a valid IP address, enabling it to operate in a specific network environment. Currently, DHCPv4 and DHCPv6 functions are not supported.

TCP/IP Stack state handling功能介绍 Introduction to TCP/IP Stack State Handling Function
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

TcpIp的状态指的是每个Controller的状态，分为
TCPIP_STATE_OFFLINE、
TCPIP_STATE_STARTUP、
TCPIP_STATE_OFFLINE、
TCPIP_STATE_ONHOLD、
TCPIP_STATE_SHUTDOWN五种状态，
其中TCPIP_STATE_STARTUP和TCPIP_STATE_SHUTDOWN为中间过渡状态。

The state of TcpIp refers to the state of each Controller, which is divided into five states:
TCPIP_STATE_OFFLINE，
TCPIP_STATE_STARTUP，
TCPIP_STATE_OFFLINE，
TCPIP_STATE_ONHOLD，
and TCPIP_STATE_SHUTDOWN.
Among them, TCPIP_STATE_STARTUP and TCPIP_STATE_SHUTDOWN are intermediate transition states.

.. only:: doc_pbs

特性 Features
--------------------------------------------------

支持变体功能 Support variant function
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

支持TcpIpLocalAddr中Type、Domain等配置变体，以及子容器TcpIpAddrAssignment和TcpIpStaticIpAddressConfig。

Support configuration variants such as Type and Domain in TcpIpLocalAddr, as well as the sub-containers TcpIpAddrAssignment and TcpIpStaticIpAddressConfig.

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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - 文件(File)
     - 描述(Description)

   * - TcpIp.h
     - 声明TcpIp模块的全部外部接口(除了回调函数)，以及配置文件中的全局变量。(Declares all external interfaces of the TcpIp module (except callback functions) and global variables in the configuration file.)

   * - TcpIp.c
     - 作为TcpIp模块的核心文件，实现TcpIp模块全部对外接口， 以及实现TcpIp模块功能所必须的local函数，local宏定义，local变量定义。(Serves as the core file of the TcpIp module, implementing all external interfaces of the TcpIp module, as well as local functions, local macros, and local variable definitions necessary for implementing the functions of the TcpIp module.)
      
   * - TcpIp_Types.h
     - 定义TcpIp模块外部/内部类型，包括AUTOSAR标准定义的类型。(Defines external/internal types of the TcpIp module, including types defined by the AUTOSAR standard.)

   * - TcpIp_Internal.h
     - 声明TcpIp模块内部功能所必须的local函数，local宏定义，local变量。(Declares local functions, local macros, and local variables necessary for the internal functions of the TcpIp module.)

   * - TcpIp_Internal.c
     - 实现TcpIp模块内部功能所必须的local函数，local宏定义，local变量。(Implements local functions, local macros, and local variables necessary for the internal functions of the TcpIp module.)

   * - TcpIp_DetError.h
     - 声明TcpIp模块DET错误检测功能的函数接口。(Declares the function interfaces for the DET error detection function of the TcpIp module.)

   * - TcpIp_DetError.c
     - 实现TcpIp模块DET错误检测功能的函数接口。(Implements the function interfaces for the DET error detection function of the TcpIp module.)

   * - TcpIp_MemMap.h
     - 声明TcpIp模块内存布局。(Declares the memory mapping of the TcpIp module.)

动态文件 Dynamic Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - 文件(File)
     - 描述(Description)

   * - TcpIp_CfgTypes.h
     - 定义PB/PC配置参数结构体类型，以及内部运行时结构体类型。(Defines the structure types of PB/PC configuration parameters and internal runtime structure types.)

   * - TcpIp_Cfg.h
     - 定义TcpIp模块PC配置的宏定义。(Defines macros for the PC configuration of the TcpIp module.)

   * - TcpIp_Cfg.c
     - 定义TcpIp模块PC配置的结构体参数。(Defines the structure parameters for the PC configuration of the TcpIp module)

   * - TcpIp_PBcfg.h
     - 定义TcpIp模块PB配置的宏定义。(Defines macros for the PB configuration of the TcpIp module.)

   * - TcpIp_PBcfg.c
     - 定义TcpIp模块PB配置的结构体参数。(Defines the structure parameters for the PB configuration of the TcpIp module)

   * - TcpIp_SocketOwner.h
     - 定义为上层SocketOwner提供的接口函数。(Defines interface functions provided for the upper-layer SocketOwner.)

   * - lwipopts.h
     - lwIp协议栈配置文件。(Configuration file for the lwIP protocol stack.)


错误处理 Error Handling
------------------------------------------------------------------------------------------

开发错误 Development Errors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. list-table::
   :widths: 20 10 30
   :header-rows: 1

   * - Error code
     - Value[hex]
     - Description
   * - TCPIP_E_UNINIT
     - 0x01
     - API service called before initializing the module
   * - TCPIP_E_PARAM_POINTER
     - 0x02
     - API service called with NULL pointer
   * - TCPIP_E_INV_ARG
     - 0x03
     - Invalid argument
   * - TCPIP_E_NOBUFS
     - 0x04
     - No buffer space available
   * - TCPIP_E_MSGSIZE
     - 0x07
     - Message too long
   * - TCPIP_E_PROTOTYPE
     - 0x08
     - Protocol wrong type for socket
   * - TCPIP_E_ADDRINUSE
     - 0x09
     - Address already in use
   * - TCPIP_E_ADDRNOTAVAIL
     - 0x0A
     - Can't assign requested address
   * - TCPIP_E_ISCONN
     - 0x0B
     - Socket is already connected
   * - TCPIP_E_NOTCONN
     - 0x0C
     - Socket is not connected
   * - TCPIP_E_NOPROTOOPT
     - 0x0D
     - Protocol not available
   * - TCPIP_E_AFNOSUPPORT
     - 0x0E
     - Address family not supported by protocol family
   * - TCPIP_E_INIT_FAILED
     - 0x0F
     - Invalid configuration set selection

产品错误 Product Errors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
None

运行时错误 Runtime Errors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 20 10 30
   :header-rows: 1

   * - Error code
     - Value[hex]
     - Description
   * - TCPIP_E_TIMEDOUT
     - 0x01
     - Operation timed out
   * - TCPIP_E_CONNREFUSED
     - 0x02
     - Connection refused
   * - TCPIP_E_HOSTUNREACH
     - 0x03
     - No route to host
   * - TCPIP_E_PACKETTOBIG
     - 0x04
     - Path does not support frame size
   * - TCPIP_E_DADCONFLICT
     - 0x05
     - Duplicate IP Address detected



接口描述 Interface Description
==============================================================

.. include:: TcpIp_h_api.rst



配置 Configuration
--------------------------------------------------------------------------------

System Scalability功能 System Scalability Function
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

根据配置项TcpIpGeneral->TcpIpScalabilityClass实现TcpIp功能等级的配置，目前工具固定配置为SC1，不可改。

The configuration of the TcpIp function level is implemented according to the configuration item TcpIpGeneral->TcpIpScalabilityClass. Currently, the tool fixes the configuration to SC1, which cannot be modified.

因为SC1只支持基于IPv4协议实现的功能，所以关于IPv6的配置(配置时，忽略所有IPv6相关配置项)、API等都不支持。

Since SC1 only supports functions implemented based on the IPv4 protocol, configurations (all IPv6-related configuration items are ignored during configuration), APIs, etc., related to IPv6 are not supported.

Internet Protocol Version 4功能 Internet Protocol Version 4 Function
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: ../../../_static/参考手册/TcpIp/image3.png
   :name: TcpIp_TcpIpIpV4General
   :align: center

   TcpIpIpV4General


该部分的功能主要体现在TcpIpIpV4General的配置Container中，涉及的配置参数及功能如下：

The functions of this part are mainly reflected in the configuration Container of TcpIpIpV4General. The involved configuration parameters and their functions are as follows:

1.TcpIpArpEnabled：是否使能ARP功能；

1.TcpIpArpEnabled: Whether to enable the ARP function;

2.TcpIpAutoIpEnabled：是否使能AUTOIP功能(未实现)；

2.TcpIpAutoIpEnabled: Whether to enable the AUTOIP function (not implemented);

3.TcpIpDhcpClientEnabled：是否使能DHCP客户端功能(未实现)；

3.TcpIpDhcpClientEnabled: Whether to enable the DHCP client function (not implemented);

4.TcpIpIcmpEnabled：是否使能ICMP功能；

4.TcpIpIcmpEnabled: Whether to enable the ICMP function;

5.TcpIpIpV4Enabled：是否使能IPv4功能；

5.TcpIpIpV4Enabled: Whether to enable the IPv4 function;

6.TcpIpLocalAddrIpv4EntriesMax：限制TcpIpLocalAddr配置项(IPv4)的总数目；

6.TcpIpLocalAddrIpv4EntriesMax: Limits the total number of TcpIpLocalAddr configuration items (for IPv4);

7.TcpIpPathMtuDiscoveryEnabled：是否使能MTU发现机制(未实现)。

7.TcpIpPathMtuDiscoveryEnabled: Whether to enable the MTU discovery mechanism (not implemented).

我们根据AUTOSAR配置，转化成lwIP的配置(工具生成lwipopts.h文件)，进而实现功能的可配置性。

We convert the AUTOSAR configuration into the configuration of lwIP (the tool generates the lwipopts.h file), thereby realizing the configurability of functions.


.. figure:: ../../../_static/参考手册/TcpIp/image4.png
   :name: TcpIp_TcpIpIpFragmentationConfig
   :align: center

   TcpIpIpFragmentationConfig


IPv4：该部分的功能主要体现在IPv4接收数据报的重组功能上，TcpIpIpConfig->TcpIpIpV4Config->TcpIpIpFragmentationConfig的配置Container中，涉及的配置参数及功能如下：

IPv4: The functions of this part are mainly reflected in the reassembly function of received IPv4 datagrams, and the configuration Container of TcpIpIpConfig->TcpIpIpV4Config->TcpIpIpFragmentationConfig. The involved configuration parameters and their functions are as follows:

1.TcpIpIpFragmentationRxEnabled：是否使能接收重组功能；

1.TcpIpIpFragmentationRxEnabled: Whether to enable the receive reassembly function;

2.TcpIpIpNumFragments：每个IP数据报最多的分片数目(在TcpIpIpFragmentationRxEnabled使能的情况下)；

2.TcpIpIpNumFragments: The maximum number of fragments for each IP datagram (when TcpIpIpFragmentationRxEnabled is enabled);

3.TcpIpIpFragmentationRxEnabled：并行处理多少IP数据报的接收重组(在TcpIpIpFragmentationRxEnabled使能的情况下)；

3.TcpIpIpFragmentationRxEnabled: The number of IP datagrams for which receive reassembly is processed in parallel (when TcpIpIpFragmentationRxEnabled is enabled);

4.TcpIpIpReassTimeout：重组超时时间(在TcpIpIpFragmentationRxEnabled使能的情况下)。

4.TcpIpIpReassTimeout: The reassembly timeout period (when TcpIpIpFragmentationRxEnabled is enabled).


.. figure:: ../../../_static/参考手册/TcpIp/image5.png
   :name: TcpIp_TcpIpArpConfig
   :align: center

   TcpIpArpConfig


ARP：该部分的功能体现在TcpIpIpConfig->TcpIpIpV4Config->TcpIpArpConfig的配置Container中，涉及的配置参数及功能如下：

ARP: The functions of this part are reflected in the configuration Container of TcpIpIpConfig->TcpIpIpV4Config->TcpIpArpConfig. The involved configuration parameters and their functions are as follows:

1.TcpIpArpNumGratuitousARPonStartup：当获取到IP地址对外广播自己的<IP地址，MAC地址>，该参数为广播的次数，因基于LwIP实现(固定为1次，不可改配置)；

1.TcpIpArpNumGratuitousARPonStartup: When an IP address is obtained, the <IP address, MAC address> of the host is broadcast to the outside. This parameter specifies the number of broadcasts. Due to the implementation based on LwIP (fixed to 1 time, which cannot be modified in configuration);

2.TcpIpArpPacketQueueEnabled：是否使能ARP在未获取目的MAC地址之前缓存请求发送的IP报；

2.TcpIpArpPacketQueueEnabled: Whether to enable ARP to cache IP packets that request to be sent before obtaining the destination MAC address;

3.TcpIpArpTableEntryTimeout：ARP缓存表(Entry)的生存时间(超时则从缓存表中移除该Entry)；

3.TcpIpArpTableEntryTimeout: The lifetime of an entry in the ARP cache table (the entry will be removed from the cache table when it times out);

4.TcpIpArpTableSizeMax：ARP缓存表的Size(即Entry的数目)。

4.TcpIpArpTableSizeMax: The size of the ARP cache table (i.e., the number of entries).


.. figure:: ../../../_static/参考手册/TcpIp/image6.png
   :name: TcpIp_TcpIpIcmpConfig
   :align: center

   TcpIpIcmpConfig


ICMP：该部分的功能体现在TcpIpIpConfig->TcpIpIpV4Config->TcpIpIcmpConfig的配置Container中，涉及的配置参数及功能如下：

ICMP: The functions of this part are reflected in the configuration Container of TcpIpIpConfig->TcpIpIpV4Config->TcpIpIcmpConfig. The involved configuration parameters and their functions are as follows:

1.TcpIpIcmpTtl：ICMP数据报Ttl参数(该参数封装在IP报首部)；

1.TcpIpIcmpTtl: The Ttl parameter of the ICMP datagram (this parameter is encapsulated in the header of the IP packet);

2.TcpIpIcmpMsgHandler(包含参数TcpIpIcmpMsgHandlerHeaderFileName和TcpIpIcmpMsgHandlerName)：主要是配置ICMP报文的接收函数，TcpIp接收到ICMP报文时调用该配置API传递给上层模块。该功能未实现，在工具上对该配置Container进行了限制(无法添加)。

2.TcpIpIcmpMsgHandler (including parameters TcpIpIcmpMsgHandlerHeaderFileName and TcpIpIcmpMsgHandlerName): It is mainly used to configure the receiving function for ICMP messages. When the TcpIp module receives an ICMP message, it calls this configured API to pass the message to the upper-layer module. This function is not implemented, and restrictions have been imposed on this configuration Container in the tool (cannot be added).

3.TcpIp模块除了在lwip代码中实现部分ICMP常用功能，还为上层模块提供ICMPv4数据报发送接口TcpIp_IcmpTransmit。但未实现ICMP数据报上传上层模块的功能(参见配置TcpIpIcmpMsgHandler说明)。

3.In addition to implementing some common ICMP functions in the lwIP code, the TcpIp module also provides the upper-layer module with the ICMPv4 datagram sending interface TcpIp_IcmpTransmit. However, the function of uploading ICMP datagrams to the upper-layer module is not implemented (see the description of configuring TcpIpIcmpMsgHandler).

IP Based Protocols功能 IP Based Protocols Function
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: ../../../_static/参考手册/TcpIp/image7.png
   :name: TcpIp_TcpIpAddrAssignment
   :align: center

   TcpIpAddrAssignment


每个TcpIpLocalAddr配置Container中，主要实现了IP地址的分配机制TcpIpAddrAssignment(考虑到目前标准的不完善以及代码实现的复杂性，暂只支持配置一个IP分配机制)。其中，

In each TcpIpLocalAddr configuration Container, the main function is to implement the IP address assignment mechanism TcpIpAddrAssignment (considering the current imperfection of the standard and the complexity of code implementation, only one IP assignment mechanism can be configured temporarily). Among them,

1.TcpIpAssignmentLifetime用以实现分配永久IP的功能未实现(暂无该需求)；

1.The function of TcpIpAssignmentLifetime for implementing permanent IP assignment is not implemented (no such requirement currently);

2.TcpIpAssignmentMethod项可根据需求选择何种分配方式(DHCP/AUTO-IP/STATIC等)；

2.The TcpIpAssignmentMethod item allows selecting the assignment method (DHCP/AUTO-IP/STATIC, etc.) according to requirements;

3.TcpIpAssignmentPriority分配方式优先级，用于配置了多个TcpIpAddrAssignment时(目前不支持)；

3.TcpIpAssignmentPriority is the priority of the assignment method, which is used when multiple TcpIpAddrAssignment configurations are set (not supported currently);

4.TcpIpAssignmentTrigger用于配置IP分配是自动还是手动方式，自动方式是当调用TcpIp_RequestComMode请求TCPIP_STATE_ONLINE时自动通过配置的IP分配机制请求IP分配，手动方式需要上层模块通过调用TcpIp_RequestIpAddrAssignment，TcpIp_ReleaseIpAddrAssignment来请求IP的分配和释放。

4.TcpIpAssignmentTrigger is used to configure whether IP assignment is automatic or manual. In the automatic mode, when TcpIp_RequestComMode is called to request TCPIP_STATE_ONLINE, IP assignment is automatically requested through the configured IP assignment mechanism. In the manual mode, the upper-layer module needs to call TcpIp_RequestIpAddrAssignment and TcpIp_ReleaseIpAddrAssignment to request IP assignment and release respectively.

当TcpIpAssignmentMethod配置为TCPIP_STATIC方式时，才可选择是否配置TcpIpStaticIpAddressConfig (当TcpIpAssignmentTrigger配置为TCPIP_AUTOMATIC时，必须配置；当配置为TCPIP_MANUAL时，可配可不配，当未配置时，调用TcpIp_RequestIpAddrAssignment请求IP分配时，IP地址参数不能为空)。当IP地址状态改变时，调用Up_LocalIpAddrAssignmentChg通知上层模块。

When TcpIpAssignmentMethod is configured as TCPIP_STATIC, you can choose whether to configure TcpIpStaticIpAddressConfig  (When TcpIpAssignmentTrigger is configured as TCPIP_AUTOMATIC, configuration is mandatory; When configured as TCPIP_MANUAL, configuration is optional. If not configured, the IP address parameter cannot be empty when TcpIp_RequestIpAddrAssignment is called to request IP assignment). When the IP address state changes, Up_LocalIpAddrAssignmentChg is called to notify the upper-layer module.


.. figure:: ../../../_static/参考手册/TcpIp/image8.png
   :name: TcpIp_TcpIpUdpConfig
   :align: center

   TcpIpUdpConfig


UDP的配置参数只有TcpIpUdpTtl，该信息封装在相应IP报的首部。TcpIp为上层模块提供接口TcpIp_UdpTransmit来发送UDP报文，当收到UDP接收报文时，通过调用Up_RxIndication(一般为SoAd_RxIndication)传递给上层。

The only configuration parameter for UDP is TcpIpUdpTtl, and this information is encapsulated in the header of the corresponding IP packet. The TcpIp module provides the interface TcpIp_UdpTransmit for the upper-layer module to send UDP messages. When a UDP receive message is received, it is passed to the upper layer by calling Up_RxIndication (generally SoAd_RxIndication).


TcpIp模块除了为上层模块提供了发送接口TcpIp_TcpTransmit，收到TCP报文通过调用Up_RxIndication(一般为SoAd_RxIndication)传递给上层外，还涉及，

In addition to providing the upper-layer module with the sending interface TcpIp_TcpTransmit, and passing received TCP messages to the upper layer by calling Up_RxIndication (generally SoAd_RxIndication), the TcpIp module also involves the following:

1.作为客户端的链接接口TcpIp_TcpConnect

1.TcpIp_TcpConnect: The connection interface used as a client;

2.作为服务端进入监听模式(等待客户端发起链接请求)接口TcpIp_TcpListen

2.TcpIp_TcpListen: The interface for the server to enter the listening mode (waiting for connection requests initiated by the client);

3.增大接收窗口的接口TcpIp_TcpReceived(上层模块接收到数据需要调用该接口来释放TcpIp模块中TCP的接收窗口)

3.TcpIp_TcpReceived: The interface for increasing the receive window (the upper-layer module needs to call this interface to release the TCP receive window in the TcpIp module after receiving data).


.. figure:: ../../../_static/参考手册/TcpIp/image9.png
   :name: TcpIp_TcpIpTcpConfig
   :align: center

   TcpIpTcpConfig


通过配置TcpIpTcpConfig(Container)的各个配置参数来说明TCP的功能实现：

The functional implementation of TCP is illustrated by configuring each configuration parameter in TcpIpTcpConfig (Container):

1.TcpIpTcpCongestionAvoidanceEnabled：拥塞避免功能(固定使能)；

1.TcpIpTcpCongestionAvoidanceEnabled: Congestion avoidance function (enabled by default);

2.TcpIpTcpFastRecoveryEnabled：快速恢复功能(固定使能)；

2.TcpIpTcpFastRecoveryEnabled: Fast recovery function (enabled by default);

3.TcpIpTcpFastRetransmitEnabled：快速重传功能(固定使能)；

3.TcpIpTcpFastRetransmitEnabled: Fast retransmission function (enabled by default);

4.TcpIpTcpFinWait2Timeout：客户端发送FIN并收到服务端ACK后进入FIN_WAIT_2状态，在该状态下等待服务器端发送FIN的时间；

4.TcpIpTcpFinWait2Timeout: After the client sends a FIN and receives an ACK from the server, it enters the FIN_WAIT_2 state. This parameter is the time to wait for the server to send a FIN in this state;

5.TcpIpTcpKeepAliveEnabled：是否使能TCP保活机制；

5.TcpIpTcpKeepAliveEnabled: Whether to enable the TCP keep-alive mechanism;

6.TcpIpTcpKeepAliveInterval：(在TcpIpTcpKeepAliveEnabled使能前提下才有效)保活探测报文的发送间隔时间；

6.TcpIpTcpKeepAliveInterval: (Effective only when TcpIpTcpKeepAliveEnabled is enabled) The interval for sending keep-alive probe messages;

7.TcpIpTcpKeepAliveProbesMax：(在TcpIpTcpKeepAliveEnabled使能前提下才有效)保活探测报文的发送最大次数；

7.TcpIpTcpKeepAliveProbesMax: (Effective only when TcpIpTcpKeepAliveEnabled is enabled) The maximum number of keep-alive probe messages to be sent;

8.TcpIpTcpKeepAliveTime：(在TcpIpTcpKeepAliveEnabled使能前提下才有效)TCP最后一次通信，与第一次保活探测报文发送的时间间隔；

8.TcpIpTcpKeepAliveTime: (Effective only when TcpIpTcpKeepAliveEnabled is enabled) The time interval between the last TCP communication and the first keep-alive probe message;

9.TcpIpTcpMaxRtx：TCP报文最大重传次数(LwIP最大支持13次)；

9.TcpIpTcpMaxRtx: The maximum number of retransmissions for TCP messages (lwIP supports a maximum of 13 times);

10.TcpIpTcpMsl：TCP客户端在TIME_WAIT状态下需要等待2×MSL时间才能切换到CLOSED状态；

10.TcpIpTcpMsl: The TCP client needs to wait for 2×MSL time in the TIME_WAIT state before switching to the CLOSED state;

11.TcpIpTcpNagleEnabled：糊涂窗口避免功能(固定使能)；

11.TcpIpTcpNagleEnabled: Silly window avoidance function (enabled by default);

12.TcpIpTcpReceiveWindowMax：接收窗口最大值；

12.TcpIpTcpReceiveWindowMax: The maximum value of the receive window;

13.TcpIpTcpRetransmissionTimeout：超时重传的超时时间，不支持(LWIP中重传超时RTT是根据网络状况动态计算的，不是固定配置值)；

13.TcpIpTcpRetransmissionTimeout: The timeout period for timeout retransmission (not supported; the retransmission timeout RTT in LWIP is dynamically calculated based on network conditions, not a fixed configuration value);

14.TcpIpTcpSlowStartEnabled：慢启动功能(固定使能)；

14.TcpIpTcpSlowStartEnabled: Slow start function (enabled by default);

15.TcpIpTcpSynMaxRtx：链接请求重传最大次数(LwIP最大支持13次)；

15.TcpIpTcpSynMaxRtx: The maximum number of retransmissions for connection requests (lwIP supports a maximum of 13 times);

16.TcpIpTcpSynReceivedTimeout：服务端收到SYN后，回复SYN/ACK，进入到SYN_RCVD状态，在该状态等待客户端回复ACK的时间；

16.TcpIpTcpSynReceivedTimeout: After the server receives a SYN, it replies with a SYN/ACK and enters the SYN_RCVD state. This parameter is the time to wait for the client to reply with an ACK in this state;

17.TcpIpTcpTtl：该信息封装在相应IP报首部。

17.TcpIpTcpTtl: This information is encapsulated in the header of the corresponding IP packet.

