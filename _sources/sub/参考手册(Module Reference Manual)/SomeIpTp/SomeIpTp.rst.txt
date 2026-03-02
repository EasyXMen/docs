===================
SomeIpTp
===================



文档信息 Document Information
============================================================

版本历史 Version History
------------------------------------------------------------------------------------------------

.. list-table::
   :widths: 10 10 5 5 30
   :header-rows: 1

   * - 日期(Date)
     - 作者(Author)
     - 版本(Version)
     - 状态(Status)
     - 说明(Description)

   * - 2025/04/03
     - jianyu.yang
     - V0.1
     - 发布(Release)
     - 首次发布(First release)
   * - 2025/04/04
     - jianyu.yang
     - V1.0
     - 发布(Release)
     - 正式发布(Official release)

参考文档 References
--------------------------------------------------------------------------------------------------

.. list-table::
   :widths: 5 10 35 10
   :header-rows: 1

   * - 编号(Number)
     - 分类(Classification)
     - 标题(Title)
     - 版本(Version)
   * - 1
     - Autosar
     - AUTOSAR_CP_SWS_BSWGeneral.pdf
     - R23-11
   * - 2
     - Autosar
     - AUTOSAR_CP_SRS_BSWGeneral.pdf
     - R23-11 
   * - 3
     - Autosar
     - AUTOSAR_CP_EXP_LayeredSoftwareArchitecture.pdf
     - R23-11
   * - 4
     - Autosar
     - AUTOSAR_FO_RS_SOMEIPProtocol.pdf
     - R23-11 
   * - 5
     - Autosar
     - AUTOSAR_FO_PRS_SOMEIPProtocol.pdf
     - R23-11
   * - 6
     - Autosar
     - AUTOSAR_CP_SWS_PDURouter.pdf
     - R23-11
   * - 7
     - Autosar
     - AUTOSAR_CP_SWS_SOMEIPTransportProtocol.pdf
     - R23-11 


术语与简写 Terms and Abbreviations
====================================================================


术语 Terms
----------------------------------------------------------------------------------------------------
.. :align: center   表格内容居中(Table contents are centered)


.. list-table::
   :widths: 10 40
   :header-rows: 1

   * - 术语(Terms)
     - 解释(Explanation)

   * - SOME/IP
     - 可扩展的面向服务中间件(Scalable service-oriented middleware)


简写 Abbreviations
----------------------------------------------------------------------------------------------------

.. list-table::
   :widths: 10 20 30
   :header-rows: 1


   * - 简写(Abbreviation)
     - 全称(Full name)
     - 解释(Explanation)
   * - SOME/IP TP
     - SOME/IP Transport Layer
     - SOME/IP传输层
   * - UDP
     - User Datagram Protocol
     - 用户数据报协议


简介 Introduction
==================================

SOME/IP TP为使用UDP发送长度大于1400字节的SOME/IP报文提供了可能。在发送端，SOME/IP TP将原始数据进行分段，插入TP报头后分段发送出去。在接收端，SOME/IP TP利用TP报头将接收的分段进行重组，传递给上层用户。

SOME/IP TP makes it possible to send SOME/IP messages with a length greater than 1400 bytes using UDP. On the sending end, SOME/IP TP segments the original data, inserts a TP header, and then sends the segments. On the receiving end, SOME/IP TP uses the TP header to reassemble the received segments and delivers them to upper-layer users.

.. figure:: ../../../_static/参考手册/SomeIpTp/SomeIpTp_layer.png
   :alt: SomeIpTp模块层次图 (SomeIpTp Module Layer Diagram)
   :name: SomeIpTp_fig_arch
   :align: center

   SomeIpTp模块层次图 (SomeIpTp Module Layer Diagram)


如图 :ref:`SomeIpTp_fig_arch`  SomeIpTp模块通过和PduR模块进行交互，进行数据的接收和发送。

As shown in Figure :ref:`SomeIpTp_fig_arch`  , the SomeIpTp module interacts with the PduR module to receive and send data.



功能描述 Functional Description
==========================================================


特性 Features
----------------------------------------------------------------------------------------------
.. _my_anchor_someIpTp_feature:

.. only:: doc_pbs

  变体 Variant
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  模块不支持变体

  The module does not support variants


SOME/IP TP 怎么工作 How SOME/IP TP Works
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

SOME/IP TP 发送与接收 SOME/IP TP Sending and Receiving
******************************************************************************************************************************************************************************************************

SOME/IP TP为使用UDP发送长度大于1400字节的SOME/IP报文提供了可能。在发送端，SOME/IP TP将原始数据进行分段，插入TP报头后分段发送出去。在接收端，SOME/IP TP利用TP报头将接收的分段进行重组，传递给上层用户。

SOME/IP TP makes it possible to send SOME/IP messages with a length greater than 1400 bytes using UDP. On the sending end, SOME/IP TP segments the original data, inserts a TP header, and then sends the segments. On the receiving end, SOME/IP TP uses the TP header to reassemble the received segments and delivers them to upper-layer users.

.. figure:: ../../../_static/参考手册/SomeIpTp/SomeIpTp_segment.png
   :alt: SomeIpTp分片 (SomeIpTp Fragmentation)
   :name: SomeIpTp_segment_fig_arch
   :align: center

   SomeIpTp分片 (SomeIpTp Fragmentation)


SOMEIP-TP协议在原有的SOMEIP协议中改造了MessageType区域的构造(增加了TP-Flag位)，并扩展了4个字节(分为Offset，Res，M区域)用于控制传输TP报文。SomeIpTp模块完成TP相关位的填充和解析，以支持大数据传输。

The SOMEIP-TP protocol modifies the structure of the MessageType field in the original SOMEIP protocol (adding a TP-Flag bit) and extends 4 bytes (divided into Offset, Res, and M fields) to control the transmission of TP messages. The SomeIpTp module completes the filling and parsing of TP-related bits to support large data transmission.

.. figure:: ../../../_static/参考手册/SomeIpTp/SomeIpTp_header.png
   :alt: SomeIpTp报文格式 (SomeIpTp Message Format)
   :name: SomeIpTp_header_fig_arch
   :align: center

   SomeIpTp报文格式 (SomeIpTp Message Format)

偏差 Deviation
--------------------------------------------------------------------
.. 有序列表示例

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
   
   * - SomeIpTp.h
     - SomeIpTp模块头文件，通过加载该头文件访问SomeIpTp公开的函数和数据类型(SomeIpTp module header file; access the public functions and data types of SomeIpTp by including this header file)

   * - SomeIpTp_Internal.h
     - SomeIpTp模块内部使用的宏，运行时变量类型定义头文件。(Header file for macros used internally by the SomeIpTp module and definitions of runtime variable types.)

   * - SomeIpTp_Types.h
     - SomeIpTp模块类型定义头文件(SomeIpTp module type definition header file)

   * - SomeIpTp.c
     - SomeIpTp模块实现源文件，各API实现在该文件中(SomeIpTp module implementation source file; various APIs are implemented in this file)

动态文件 Dynamic Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - 文件(File)
     - 描述(Description)
   
   * - SomeIpTp_Cfg.h
     - 用于定义SomeIpTp模块预编译时用到的宏(Used to define macros used during pre-compilation of the SomeIpTp module)

   * - SomeIpTp _Cfg.c
     - 配置参数源文件，包含各个配置项的定义(Configuration parameter source file, containing definitions of various configuration items)

   * - SomeIpTp_MemMap.h
     - SomeIpTp模块函数和变量存储位置定义文件(File defining the storage locations of functions and variables of the SomeIpTp module)


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

   * - SOMEIPTP_E_UNINIT
     - 0x01
     - SOME/IP TP module not initialized

   * - SOMEIPTP_E_PARAM_POINTER
     - 0x02
     - Null pointer has been passed as an argument

   * - SOMEIPTP_E_PARAM
     - 0x03
     - Unknown parameter has been passed

   * - SOMEIPTP_E_INIT_FAILED
     - 0x04
     - Invalid configuration set selection


产品错误 Product Errors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
None

运行时错误 Runtime Errors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. list-table:: 
   :widths: 20 10 30
   :header-rows: 1

   * - SOMEIPTP_E_MESSAGE_TYPE
     - 0x04
     - The TP-Flag (of Message Type) was set to '0'

   * - SOMEIPTP_E_INCONSISTENT_SEQUENCE
     - 0x05
     - Inconsistent subsequent segment received

   * - SOMEIPTP_E_INCONSISTENT_HEADER
     - 0x06
     - Inconsistent header received

   * - SOMEIPTP_E_DISASSEMBLY_INTERRUPT
     - 0x07
     - Disassembly Interrupt due to the upper layer

   * - SOMEIPTP_E_ASSEMBLY_INTERRUPT
     - 0x08
     - Assembly Interrupt due to the upper layer


接口描述 Interface Description
==============================================================

.. include:: SomeIpTp_h_api.rst
.. include:: SomeIpTp_Types_h_api.rst


配置 Configuration
=================================================


接收端配置 Receiver Configuration
------------------------------------------------------------------------------------------------------------------------------
SomeIpTpRxNSdu及其子容器用于配置SomIpTp模块对接收到的分片进行组装的配置。

SomeIpTpRxNSdu and its sub-containers are used to configure the SomIpTp module for the assembly of received fragments.

.. figure:: ../../../_static/参考手册/SomeIpTp/SomeIpTp_Rx.png
   :alt: SomeIpTp接收端 (SomeIpTp Receiver)
   :name: SomeIpTp_rx_fig_arch
   :align: center

   SomeIpTp接收端NSdu的配置 (Configuration of SomeIpTp Receiver NSdu)


发送端配置 Transmitter Configuration
------------------------------------------------------------------------------------------------------------------------------
SomeIpTpTxNSdu及其子容器用于配置SomIpTp模块对收到的上层的NSdu的发送请求，将其进行分片后发送的配置。

SomeIpTpTxNSdu and its sub-containers are used to configure the SomIpTp module to process the NSdu transmission requests received from the upper layer, fragment the NSdu, and then send the fragments.

.. figure:: ../../../_static/参考手册/SomeIpTp/SomeIpTp_Tx.png
   :alt: SomeIpTp发送端 (SomeIpTp Transmitter)
   :name: SomeIpTp_tx_fig_arch
   :align: center

   SomeIpTp发送端NSdu的配置 (Configuration of SomeIpTp Transmitter NSdu)
