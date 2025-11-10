====================
UdpNm
====================

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

   * - 2025/2/22
     - caihong.liu
     - V0.1
     - 发布(Release)
     - 首次发布(First release)

   * - 2025/04/04
     - caihong.liu
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
     - AUTOSAR_FO_PRS_NetworkManagementProtocol.pdf
     - R23-11
   * - 2
     - Autosar
     - AUTOSAR_CP_SWS_NetworkManagementInterface.pdf
     - R23-11
   * - 3
     - Autosar
     - AUTOSAR_FO_RS_NetworkManagement.pdf
     - R23-11
   * - 4
     - Autosar
     - AUTOSAR_CP_TPS_ECUConfiguration.pdf
     - R23-11


术语与简写 Terms and Abbreviations
====================================================================

术语 Terms
--------------------------------------------------------------------------------------------------------

.. list-table::
   :widths: 10 40
   :header-rows: 1

   * - 术语(Terms)
     - 解释(Explanation)

   * - NM PDU
     - 指数据包中传输的有效载荷，包括NM用户数据以及控制位向量和源节点标识符。(The payload transmitted within a data packet, which includes NM user data, the Control Bit Vector, and the Source Node Identifier.)

   * - NM Packet
     - 指一个以太网帧：除了有效载荷部分的网管传输数据( PDU )外，还包含一个IP和一个UDP报头。(An Ethernet frame that, in addition to the network management transmission data (PDU) of the payload section, also contains an IP and a UDP header.)

   * - NM Message
     - 在NM算法的方法论内转移的任何单一信息项。(Any single item of information transferred within the methodology of the NM algorithm.)

   * - Bus-Off state
     - 指没有电缆连接到以太网HW的情况。(The state where no cable is connected to the Ethernet HW.)

   * - PDU transmission ability is disabled
     - 这意味着NM-PDU传输已经被UdpNm_DisableCommunication服务禁用。(This means that NM-PDU transmission has been disabled by the UdpNm_DisableCommunication service.)

   * - Repeat Message Request Bit Indication
     - UdpNm_SoAdIfRxIndication在接收到的NM-PDU的CBV字节中找到Repeat Message Request比特位为TRUE。(UdpNm_SoAdIfRxIndication finds the Repeat Message Request bit to be TRUE in the CBV byte of a received NM-PDU.)

   * - Top-level PNC coordinator
     - ECU作为顶层的PNC协调器，负责在所有分配的通道上进行主动协调的PNC。该ECU具有启用的PNC网关功能。顶层PNC协调器触发这些PNC的同步PNC停机，如果网络中没有其他ECU请求它们，如果同步PNC停机被启用。(An ECU acting as a top-level PNC coordinator, which is responsible for the active coordination of PNC on all its assigned channels. This ECU has the PNC gateway function enabled. The top-level PNC coordinator triggers a synchronized PNC shutdown for these PNCs if no other ECU in the network requests them and if synchronized PNC shutdown is enabled.)

   * - Intermediate PNC coordinator
     - 一个ECU作为中间的PNC协调器，为那些在至少一个通道上被动协调的PNC提供协调。该ECU具有启用的PNC网关功能。如果同步PNC关断被启用，中间PNC协调器将同步PNC关断转发给被动协调的PNC的主动协调通道。(An ECU acting as an intermediate PNC coordinator, which provides coordination for those PNCs that are passively coordinated on at least one channel. This ECU has the PNC gateway function enabled. If synchronized PNC shutdown is enabled, the intermediate PNC coordinator will forward the synchronized PNC shutdown to the actively coordinating channels of the passively coordinated PNCs.)
     
   * - PNC leaf node
     - 一个PNC叶子节点是一个ECU，它在网络中完全不充当PNC协调器。它与通常的NM消息一样处理PN关机消息。(A PNC leaf node is an ECU that does not act as a PNC coordinator at all within the network. It handles PN shutdown messages like regular NM messages.)

   * - PN shutdown message
     - 顶层PNC协调器发送PN关断消息，以指示整个PN拓扑的同步PNC关断。一个PN关断消息作为NM消息，在控制比特向量中具有PNSR位，对于一个同步关断设置为" 1 "表示的所有PNC。(A PN shutdown message is sent by a top-level PNC coordinator to indicate a synchronized PNC shutdown for the entire PN topology. A PN shutdown message is an NM message with the PNSR bit in the Control Bit Vector set to "1" for all PNCs for which a synchronized shutdown is indicated.)

简写 Abbreviations
--------------------------------------------------------------------------------------------------------

.. list-table::
   :widths: 10 20 30
   :header-rows: 1


   * - 简写(Abbreviation)
     - 全称(Full name)
     - 解释(Explanation)

   * - API
     - Application Programming Interface
     - 应用程序接口

   * - EthIf
     - Ethernet Interface
     - 以太网接口

   * - UdpNm
     - UDP Network Management
     - Udp 网络管理模块缩写

   * - CBV
     - Control Bit Vector
     - NM-PDU中控制位向量

   * - CWU
     - Car Wakeup
     - 车辆唤醒

   * - SduR
     - Service Data Unit
     - 服务数据单元

   * - NM
     - Network Management
     - 网络管理

   * - PNC
     - Partial Network Cluster
     - 部分网络簇

   * - PNI
     - Partial Network Information
     - 部分网络信息

   * - PNL
     - Partial Network Learning
     - 部分网络学习

   * - SNI
     - Source Node Identifier
     - 源节点标识符

   * - UDP
     - User Datagram Protocol
     - 用户数据包协议

   * - TCP/IP
     - A family of communication protocols used in computer networks
     - 计算机网络中使用的一簇通信协议

简介 Introduction
====================================================================

UdpNm模块的核心功能是协调网络正常运行和总线睡眠模式之间的转换，除此之外，还提供了可选功能，例如检测当前节点或检测其他所有节点是否准备休眠等。

The core function of the UdpNm module is to coordinate the transition between normal network running and bus-sleep mode. In addition, it provides optional functions, such as detecting whether the local node or all other nodes are ready to sleep.

UdpNm提供网络管理接口(Nm)和TCP/IP协议栈之间的适配。UdpNm通过调用SoAd模块的发送API来传输数据，并提供接收API给SoAd用于接收下层网络管理报文。Nm模块调用UdpNm模块API来更改UdpNm的当前状态机状态，UdpNm的状态机模式切换需要通知给Nm模块。

UdpNm provides the adaptation between the Network Management interface (Nm) and the TCP/IP protocol stack. UdpNm transmits data by calling the transmission APIs of the SoAd module and provides reception APIs for SoAd to receive network management messages from the lower layers. The Nm module calls the APIs of the UdpNm module to change the current state machine state of UdpNm, and state machine mode switches in the UdpNm module need to be notified to the Nm module.

.. figure:: ../../../_static/参考手册/UdpNm/ComStack.png
   :alt: Autosar通信栈 (Autosar Communication Stack)
   :align: center

   Autosar通信栈 (Autosar Communication Stack)

.. 功能描述章节
.. include:: UdpNm_Functional.rst

.. 集成描述章节
.. include:: UdpNm_Integration.rst

.. 引用接口描述。来自于code->doxygen->latex->rst
.. 引用接口描述。 From code->doxygen->latex->rst
.. include:: UdpNm_api.rst

.. 引用配置描述章节
.. include:: UdpNm_Configuration.rst