====================
CanNm
====================

文档信息（Document Information）
=====================================

版本历史（Version History）
---------------------------------

.. list-table::
   :widths: 10 10 10 10 20
   :header-rows: 1

   * - 日期（Date）
     - 作者（Author）
     - 版本（Version）
     - 状态（Status）
     - 说明（Description）
   * - 2025/2/22
     - caihong.liu
     - V0.1
     - 发布（Release）
     - 首次发布（First release）
   * - 2025/04/04
     - caihong.liu
     - V1.0
     - 发布（Release）
     - 正式发布（Official release）

参考文档（Reference Document）
-------------------------------------

.. list-table::
   :widths: 10 10 30 10
   :header-rows: 1

   * - 编号（Number）
     - 分类（Classification）
     - 标题（Title）
     - 版本（Version）
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

术语与简写（Terms and Abbreviations）
============================================

术语（Term）
------------------

.. list-table::
   :widths: 10 40
   :header-rows: 1

   * - 术语（Term）
     - 解释（Explanation）

   * - NM-PDU
     - 指数据包中传输的有效载荷，包括NM用户数据以及控制位向量和源节点标识符。
        
       Refers to the payload transmitted in the data packet, including NM user data, control bit vectors, and source node identifiers.

   * - PDU transmission ability is disabled
     - 这意味着NM-PDU传输已经被CanNm_DisableCommunication服务禁用。
        
       This means that the NM-PDU transmission has been disabled by the CanNm_DisableCommunication service.

   * - Repeat Message Request Bit Indication
     - CanNm_RxIndication在接收到的NM-PDU的CBV字节中找到Repeat Message Request比特位为TRUE。
      
       CanNm_RxIndication finds that the Repeat Message Request bit in the CBV byte of the received NM-PDU is TRUE.

   * - Top-level PNC coordinator
     - ECU作为顶层的PNC协调器，负责在所有分配的通道上进行主动协调的PNC。该ECU具有启用的PNC网关功能。顶层PNC协调器触发这些PNC的同步PNC停机，如果网络中没有其他ECU请求它们，如果同步PNC停机被启用。
      
       As the top-level PNC coordinator, the ECU is responsible for actively coordinating PNCs across all assigned channels. This ECU has the PNC gateway function enabled. The top-level PNC coordinator triggers the synchronous PNC shutdown of these PNCs if no other ECUs in the network request them and if the synchronous PNC shutdown is enabled.

   * - Intermediate PNC coordinator
     - 一个ECU作为中间的PNC协调器，为那些在至少一个通道上被动协调的PNC提供协调。该ECU具有启用的PNC网关功能。如果同步PNC关断被启用，中间PNC协调器将同步PNC关断转发给被动协调的PNC的主动协调通道。
      
       An ECU acts as an intermediate PNC coordinator, providing coordination for those PNCs that are passively coordinated on at least one channel. This ECU has the PNC gateway function enabled. If the synchronous PNC shutdown is enabled, the intermediate PNC coordinator will forward the synchronous PNC shutdown to the actively coordinated channels of the passively coordinated PNCs.

   * - PNC leaf node
     - 一个PNC叶子节点是一个ECU，它在网络中完全不充当PNC协调器。它与通常的NM消息一样处理PN关机消息。
      
       A PNC leaf node is an ECU that does not act as a PNC coordinator at all in the network. It processes PN shutdown messages in the same way as regular NM messages.

   * - PN shutdown message
     - 顶层PNC协调器发送PN关断消息，以指示整个PN拓扑的同步PNC关断。一个PN关断消息作为NM消息，在控制比特向量中具有PNSR位，对于一个同步关断设置为" 1 "表示的所有PNC。
      
       The top-level PNC coordinator sends a PN shutdown message to indicate the synchronous PNC shutdown of the entire PN topology. A PN shutdown message, acting as an NM message, has the PNSR bit in the control bit vector, which is set to "1" for all PNCs indicating a synchronous shutdown.
     
   * - Immediate Transmission Confirmation
     - 每一个NM PDU传输请求都被直接看作是由总线确认的，不需要进行超时处理。这种机制可用于总线系统，其中总线流量设计为每次传输都将始终在总线上发送。
      
       Every NM PDU transmission request is directly regarded as being acknowledged by the bus, and no timeout processing is required. This mechanism can be used in bus systems where the bus traffic is designed such that each transmission will always be sent on the bus.

简写（Abbreviation）
---------------------------

.. list-table::
   :widths: 10 20 30
   :header-rows: 1


   * - 简写（Abbreviation）
     - 全称（Full name）
     - 解释（Explanation）

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


简介（Introduction）
============================

AUTOSAR CanNm是一个仅是现在Can总线的硬件独立协议模块，CanNm模块的核心功能是协调网络正常运行和总线睡眠模式之间的转换，还提供了可选功能，例如检测当前节点或检测其他所有节点是否准备休眠等。
CanNm提供网络管理接口（Nm）和CanIf模块之间的适配。CanNm通过调用CanIf模块的发送API来传输数据，并提供接收API给CanIf用于接收下层网络管理报文。Nm模块调用CanNm模块API来更改CanNm的当前状态机状态，CanNm的状态机模式切换需要通知给Nm模块。

AUTOSAR CanNm is a hardware-independent protocol module that is only applicable to the current CAN bus. The core function of the CanNm module is to coordinate the transition between the normal operation of the network and the bus sleep mode. It also provides optional functions, such as detecting whether the current node or all other nodes are ready to sleep.
CanNm provides adaptation between the Network Management interface (Nm) and the CanIf module. CanNm transmits data by calling the transmission API of the CanIf module and provides a reception API to the CanIf for receiving lower-layer network management messages. The Nm module calls the CanNm module API to change the current state machine state of CanNm, and the state machine mode switching of CanNm needs to be notified to the Nm module.

.. figure:: ../../../_static/参考手册/CanNm/模块层次图.png
   :alt: CanNm 在 AUTOSAR中 的位置
   :align: center

   CanNm在AUTOSAR中的位置
   
   The position of CanNm in AUTOSAR

.. 功能描述章节
.. include:: CanNm_Functional.rst

.. 集成描述章节
.. include:: CanNm_Integration.rst

.. 引用接口描述。来自于code->doxygen->latex->rst
.. include:: CanNm_api.rst
 
.. 引用配置描述章节
.. include:: CanNm_Configuration.rst