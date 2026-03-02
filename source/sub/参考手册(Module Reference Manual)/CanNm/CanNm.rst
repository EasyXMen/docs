====================
CanNm
====================

文档信息(Document Information)
=====================================

版本历史(Version History)
---------------------------------

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

参考文档(References)
-------------------------------------

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

术语与简写(Terms and Abbreviations)
============================================

术语(Terms)
------------------

.. list-table::
   :widths: 10 40
   :header-rows: 1

   * - 术语(Term)
     - 解释(Explanation)

   * - NM-PDU
     - 指数据包中传输的有效载荷，包括NM用户数据以及控制位向量和源节点标识符 (Network Management Protocol Data Unit containing NM user data, Control Bit Vector and source node identifier)

   * - PDU transmission ability is disabled
     - 这意味着NM-PDU传输已经被CanNm_DisableCommunication服务禁用 (Indicates NM-PDU transmission was disabled via CanNm_DisableCommunication service)

   * - Repeat Message Request Bit Indication
     - CanNm_RxIndication在接收到的NM-PDU的CBV字节中找到Repeat Message Request比特位为TRUE (CanNm_RxIndication detects TRUE state of Repeat Message Request bit in CBV byte of received NM-PDU)

   * - Top-level PNC coordinator
     - ECU作为顶层的PNC协调器，负责在所有分配的通道上进行主动协调的PNC。该ECU具有启用的PNC网关功能。顶层PNC协调器触发这些PNC的同步PNC停机，如果网络中没有其他ECU请求它们，如果同步PNC停机被启用 (ECU serving as the top-level PNC coordinator, responsible for actively coordinating PNCs across all assigned channels. This ECU has PNC gateway functionality enabled. It triggers synchronous PNC shutdown when no other ECUs require these PNCs and when synchronous shutdown is enabled)

   * - Intermediate PNC coordinator
     - 一个ECU作为中间的PNC协调器，为那些在至少一个通道上被动协调的PNC提供协调。该ECU具有启用的PNC网关功能。如果同步PNC关断被启用，中间PNC协调器将同步PNC关断转发给被动协调的PNC的主动协调通道 (ECU functioning as an intermediate PNC coordinator that provides coordination for passively-managed PNCs on at least one channel. It forwards synchronous shutdown commands to active channels when enabled)

   * - PNC leaf node
     - 一个PNC叶子节点是一个ECU，它在网络中完全不充当PNC协调器。它与通常的NM消息一样处理PN关机消息 (Non-coordinating ECU that processes PN shutdown messages like regular NM messages)

   * - PN shutdown message
     - 顶层PNC协调器发送PN关断消息，以指示整个PN拓扑的同步PNC关断。一个PN关断消息作为NM消息，在控制比特向量中具有PNSR位，对于一个同步关断设置为" 1 "表示的所有PNC (Synchronized shutdown command broadcast by top-level coordinator via NM message with PNSR bit=1 in CBV for all PNCs)

   * - Immediate Transmission Confirmation
     - 每一个NM PDU传输请求都被直接看作是由总线确认的，不需要进行超时处理。这种机制可用于总线系统，其中总线流量设计为每次传输都将始终在总线上发送 (Transmission mechanism where NM-PDU transmissions are treated as immediately confirmed by the bus without timeout monitoring. Applicable in time-triggered bus systems with guaranteed transmission slots)

简写(Abbreviations)
---------------------------

.. list-table::
   :widths: 10 20 30
   :header-rows: 1


   * - 简写(Abbreviation)
     - 全称(Full name)
     - 解释(Explanation)

   * - CanIf
     - Can Interface
     - Can 接口模块缩写

   * - CanNm
     - Can Network Management
     - Can 网络管理模块缩写

   * - CBV
     - Control Bit Vector
     - NM-PDU中控制位向量

   * - CWU
     - Car Wakeup
     - 车辆唤醒

   * - ERA
     - External Request Array
     - 外部PNC请求数组

   * - EIRA
     - External and Internal Request Array
     - 外部和内部PNC请求数组

   * - LSduR
     - Linklayer SDU Router
     - 链路层Sdu Router

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


简介(Introduction)
============================

AUTOSAR CanNm是一个仅是现在Can总线的硬件独立协议模块，CanNm模块的核心功能是协调网络正常运行和总线睡眠模式之间的转换，还提供了可选功能，例如检测当前节点或检测其他所有节点是否准备休眠等。

AUTOSAR CanNm is a hardware-independent protocol module designed specifically for CAN buses. Its core function is to manage transitions between normal network operation and bus sleep mode. It also offers optional features, such as detecting if the current node or all other nodes are ready for sleep.

CanNm提供网络管理接口(Nm)和CanIf模块之间的适配。CanNm通过调用CanIf模块的发送API来传输数据，并提供接收API给CanIf用于接收下层网络管理报文。Nm模块调用CanNm模块API来更改CanNm的当前状态机状态，CanNm的状态机模式切换需要通知给Nm模块。

CanNm adapts between the Network Management (Nm) interface and the CanIf module. It transmits messages by calling CanIf's transmit API and provides a receive API for CanIf to handle incoming network management messages. The Nm module calls CanNm APIs to change its state machine state, and CanNm notifies the Nm module of any state machine mode transitions.

.. figure:: ../../../_static/参考手册/CanNm/模块层次图.png
   :alt: CanNm 在 AUTOSAR中 的位置(Position of CanNm in AUTOSAR)
   :align: center

   CanNm在AUTOSAR中的位置
   
   Position of CanNm in AUTOSAR

.. 功能描述章节
.. include:: CanNm_Functional.rst

.. 集成描述章节
.. include:: CanNm_Integration.rst

.. 引用接口描述。来自于code->doxygen->latex->rst
.. include:: CanNm_api.rst
 
.. 引用配置描述章节
.. include:: CanNm_Configuration.rst