功能描述(Functional Description)
===================================================================================================


公共特性(Public Features)
---------------------------------------------------------------------------------------------------


多核多分区功能(Multi-core and Multi-partition Features)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- TcpIp模块支持多核单分区部署，即每个核上最多只能部署一个分区。

- 由TcpIpCtrl/TcpIpEthIfCtrlRef所关联的EthIfController所在分区，来决定TcpIp所部署的所有分区。


.. only:: doc_pbs

   PBS功能(PBS Features)
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   - TcpIp模块支持多变体配置。

     The TcpIp module supports multi-variant configurations.

   - 支持TcpIpLocalAddr中Type、Domain等配置变体，以及子容器TcpIpAddrAssignment和TcpIpStaticIpAddressConfig。

     Support configuration variants such as Type and Domain in TcpIpLocalAddr, as well as the sub-containers TcpIpAddrAssignment and TcpIpStaticIpAddressConfig.


Memmap功能(Memmap Features)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Memmap文件是动态的。存在
  TCPIP_START_SEC_CONST_UNSPECIFIED、TCPIP_STOP_SEC_CONST_UNSPECIFIED、
  TCPIP_START_SEC_CONFIG_DATA_8、TCPIP_STOP_SEC_CONFIG_DATA_8、
  TCPIP_START_SEC_CONFIG_DATA_16、TCPIP_STOP_SEC_CONFIG_DATA_16、
  TCPIP_START_SEC_CONFIG_DATA_32、TCPIP_STOP_SEC_CONFIG_DATA_32、
  TCPIP_START_SEC_CONFIG_DATA_UNSPECIFIED、TCPIP_STOP_SEC_CONFIG_DATA_UNSPECIFIED、
  TCPIP_START_SEC_VAR_CLEARED_8、TCPIP_STOP_SEC_VAR_CLEARED_8、
  TCPIP_START_SEC_VAR_CLEARED_16、TCPIP_STOP_SEC_VAR_CLEARED_16、
  TCPIP_START_SEC_VAR_CLEARED_32、TCPIP_STOP_SEC_VAR_CLEARED_32、
  TCPIP_START_SEC_VAR_CLEARED_PTR、TCPIP_STOP_SEC_VAR_CLEARED_PTR、
  TCPIP_START_SEC_VAR_CLEARED_UNSPECIFIED、TCPIP_STOP_SEC_VAR_CLEARED_UNSPECIFIED、
  TCPIP_START_SEC_VAR_INIT_UNSPECIFIED、TCPIP_STOP_SEC_VAR_INIT_UNSPECIFIED、
  TCPIP_START_SEC_VAR_CLONE_8、TCPIP_STOP_SEC_VAR_CLONE_8、
  TCPIP_START_SEC_VAR_CLEARED_{{ n }}_8 [#f1]_、TCPIP_STOP_SEC_VAR_CLEARED_{{ n }}_8 [#f1]_、
  TCPIP_START_SEC_VAR_CLEARED_{{ n }}_32 [#f1]_、TCPIP_STOP_SEC_VAR_CLEARED_{{ n }}_32 [#f1]_、
  TCPIP_START_SEC_VAR_CLEARED_{{ n }}_PTR [#f1]_、TCPIP_STOP_SEC_VAR_CLEARED_{{ n }}_PTR [#f1]_、
  TCPIP_START_SEC_VAR_CLEARED_{{ n }}_UNSPECIFIED [#f1]_、TCPIP_STOP_SEC_VAR_CLEARED_{{ n }}_UNSPECIFIED [#f1]_、
  TCPIP_START_SEC_CODE、TCPIP_STOP_SEC_CODE。

  The Memmap files are dynamic.

.. rubric:: 说明

.. [#f1] n 为TcpIp所部署的分区名称。


独占区功能(Exclusive Area Features)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
None.


模块特性(Module Features)
---------------------------------------------------------------------------------------------------


System Scalability功能介绍(Introduction to System Scalability Function)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

根据不同的应用情况，TcpIp模块的功能(对IP协议的支持情况)分为三个等级。因开发需求，目前只支持IPv4，因此只支持SC1功能。

According to different application scenarios, the functions of the TcpIp module (support for IP protocols) are divided into three levels. Due to development requirements, only IPv4 is supported currently, so only the SC1 function is supported.


Internet Protocol Version 4功能介绍(Introduction to Internet Protocol Version 4 Function)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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


IP Based Protocols功能介绍(Introduction to IP Based Protocols Function)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

TLS（传输层安全协议）是一种位于传输层和应用层之间的安全通信协议，用于在网络上传输数据时提供机密性、完整性和身份认证。
在建立连接时，客户端和服务器通过 握手过程（Handshake） 协商出加密算法、会话密钥，并验证双方身份。
握手完成后，所有应用层数据都会被加密传输，从而防止窃听和篡改。

- 支持版本：TLS1.2、TLS 1.3
- 支持TLS Client和Server
- 支持签名算法：RSA ECDSA
- 支持秘钥交换算法：RSA ECDHE（X25519）
- 支持对称加密算法：AES-CBC AES-GCM
- 不支持TLS Alert Protocol
- 不支持TLS 1.2 Hello Request和TLS 1.3 Hello Retry Request
- 不支持Client Certificate和Certificate Request
- 不支持证书链验证
- 不支持PSK和0-RTT
- 不支持的extension：encrypt then mac，record size limit

TLS (Transport Layer Security) is a cryptographic protocol that operates between the transport and application layers, ensuring confidentiality, integrity, and authentication for data transmitted over the network.
During the handshake phase, the client and server negotiate cipher suites, exchange keys, and authenticate each other.
Once the handshake is complete, all subsequent application data is encrypted to prevent eavesdropping or tampering.

- Supported version: TLS1.2, TLS 1.3
- Support TLS Client and Server
- Supported signature algorithm: RSA ECDSA
- Supported key exchange algorithm: RSA ECDHE (X25519)
- Supported symmetric algorithm: AES-CBC, AES-GCM
- TLS Alert Protocol is not supported
- TLS 1.2 Hello Request and TLS 1.3 Hello Retry Request are not supported
- Client Certificate and Certificate Request are not supported
- Certificate chain validation is not supported
- PSK and 0-RTT are not supported
- Unsupported extensions: encrypt-then-MAC, record size limit

IKE（Internet Key Exchange）协议建立在 Internet 安全联盟和密钥管理协议 ISAKMP 定义的框架上，是基于 UDP（User Datagram Protocol）的应用层协议。
它为 IPSec 提供了自动协商密钥、建立 IPSec 安全联盟的服务，能够简化 IPSec 的配置和维护工作。

- 支持版本：IKEv2
- 支持身份认证方式：PSK
- 支持完整性校验算法：HMAC_SHA2_256
- 支持对称加密算法：AES-CBC
- 支持密钥交换算法：ECDHE（X25519）

IKE (Internet Key Exchange) is an application-layer protocol based on UDP (User Datagram Protocol) and built on the framework defined by ISAKMP (Internet Security Association and Key Management Protocol).
It provides IPSec with automatic key negotiation and services for establishing IPSec security associations, simplifying IPSec configuration and maintenance.

- Supported version: IKEv2
- Supported authentication method: PSK
- Supported integrity algorithm: HMAC_SHA2_256
- Supported symmetric algorithm: AES-CBC
- Supported key exchange algorithm: ECDHE (X25519)

IPsec（Internet Protocol Security）是一组在 IP 层提供加密、认证、防篡改和重放保护的安全协议。
它可以保护主机、网络或 VPN 之间的数据通信安全。

- 支持模式：传输模式（Transport Mode）
- 支持服务：认证头（AH）

IPsec (Internet Protocol Security) is a suite of security protocols that provides encryption, authentication, anti-tampering, and anti-replay protection at the IP layer.
It can protect data communication security between hosts, networks, or VPNs.

- Supported mode: Transport Mode
- Supported service: Authentication Header (AH)

TCP/IP Stack state handling功能介绍(Introduction to TCP/IP Stack State Handling Function)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
