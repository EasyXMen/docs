====================
CanIf
====================



文档信息(Document Information)
========================================

版本历史(Version History)
------------------------------------

.. list-table::
   :widths: 10 10 10 10 20
   :header-rows: 1

   * - 日期(Date)
     - 作者(Author)
     - 版本(Version)
     - 状态(Status)
     - 说明(Description)
   * - 2025/3/3
     - miao.wang
     - V0.1
     - 发布(Release)
     - 首次发布(First release)
   * - 2025/04/04
     - miao.wang
     - V1.0
     - 发布(Release)
     - 正式发布(Official release)


参考文档(References)
------------------------------------

.. list-table::
   :widths: 10 10 30 10
   :header-rows: 1

   * - 编号(Number)
     - 分类(Classification)
     - 标题(Title)
     - 版本(Version)
   * - 1
     - Autosar
     - AUTOSAR_CP_SRS_CAN.pdf
     - R23-11
   * - 2
     - Autosar
     - AUTOSAR_CP_SWS_CANInterface.pdf
     - R23-11


术语与简写(Terms and Abbreviations)
==========================================

术语(Terms)
-----------------------
   .. :align: center   表格内容居中

.. list-table::
   :widths: 10 40
   :header-rows: 1

   * - 术语(Term)
     - 解释(Explanation)

   * - CAN Hardware Unit
     - 一个CAN物理单元包含一个或多个相同类型的CAN控制器(A CAN physical unit contains one or more CAN controllers of the same type)
   * - CanIf Receive L-PDU
     - CanIf接收的"由下至上"的PDU(The "bottom-up" PDU received by CanIf)

   * - CanIf Transmit L-PDU
     - CanIf发送的"由上至下"的PDU(The "top-down" PDU sent by CanIf)

简写(Abbreviations)
------------------------

.. list-table::
   :widths: 10 20 30
   :header-rows: 1

   * - 简写(Abbreviation)
     - 全称(Full name)
     - 解释(Explanation)

   * - CanDrv
     - CAN Driver module
     - CAN控制器驱动模块

   * - CAN FD
     - CAN with Flexible Data-Rate
     - 相比传统CAN，其波特率及负载都更高

   * - CanIf
     - CAN Interface module
     - CAN接口模块

   * - CanTrcv
     - CAN Transceiver Driver module
     - CAN收发器驱动模块

   * - HOH
     - CAN hardware object handle
     - CAN硬件抽象单元(HRH+HTH)

   * - HRH
     - CAN hardware receive handle
     - CAN驱动层接收硬件单元的抽象

   * - HTH
     - CAN hardware transmit handle
     - CAN驱动层发送硬件单元的抽象

   * - DET
     - Default Error Tracer
     - 开发错误检测


简介(Introduction)
============================

CanIf模块将底层不同的Can驱动，CanTrcv驱动抽象化，方便上层模块统一通过CanIf模块进行访问。

The CanIf module abstracts different underlying Can and CanTrcv drivers, facilitating unified access by upper-layer modules through the CanIf module.

在AUTOSAR架构中，其上层模块主要为PduR，CanTp，J1939Tp，CanNm，CanSm等。

In the AUTOSAR architecture, the upper-layer modules mainly include PduR, CanTp, J1939Tp, CanNm, CanSm, etc.

CanIf主要功能包含L-PDU的接收指示，L-PDU的发送及发送确认等通信功能，
以及Can Controller/Trcv的模式控制，波特率切换，睡眠唤醒等其它功能栈功能。

The main functions of CanIf include communication functions such as L-PDU reception indication, L-PDU transmission and transmission confirmation,as well as CAN controller/Trcv management, covering mode control, baud rate switching, and sleep/wake-up capabilities.

.. figure:: /_static/参考手册(Module_Reference_Manual)/CanIf/image1.png
   :name: CanIf_arch
   :align: center

   CanIf模块层次图

   CanIf Module Hierarchy Diagram

CanIf模块处于AUTOSAR架构中的通信硬件抽象层，其下层模块为CanDrv/CanTrcv驱动模块，
上层模块可能为PduR，CanTp，CanNm，CanSM，EcuM，Xcp，J1939Tp，J1939Nm，CDD。

The CanIf module resides in the communication hardware abstraction layer of the AUTOSAR architecture. Its lower-layer modules are the CanDrv/CanTrcv drivers, and its upper-layer modules may include PduR, CanTp, CanNm, CanSM, EcuM, Xcp, J1939Tp, J1939Nm, and CDD.

CanIf实现了与上下层模块间基于PDU的发送/接收，实现了对硬件单元模式的控制以及模式切换通知，
实现了对睡眠/唤醒机制的支持。

CanIf implements PDU-based transmission/reception with upper- and lower-layer modules, realizes the control over hardware unit modes and mode switch notifications, and supports the sleep/wake-up mechanism.


.. 功能描述章节
.. include:: CanIf_Functional.rst


集成(Integration)
=======================

文件列表(File List)
--------------------------

静态文件(Static Files)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - 文件(File)
     - 描述(Description)

   * - CanIf.h
     - 声明CanIf模块的全部外部接口(除了回调函数)，以及配置文件中的全局变量 (Declares all CanIf module external interfaces (excluding callbacks) and global variables in the configuration file)

   * - CanIf.c
     - 作为CanIf模块的核心文件，实现CanIf模块全部对外接口，以及实现CanIf模块功能所必须的local函数，local宏定义，local变量定义(Core implementation file containing all external interfaces and required local functions/macros/variables for CanIf functionality)

   * - CanIf_Types.h
     - 定义CanIf模块外部/内部类型，包括AUTOSAR标准定义的类型 (Defines CanIf module external/internal types including AUTOSAR-standardized types)

   * - CanIf_Internal.h
     - 声明CanIf模块内部功能所必须的local函数，local宏定义，local变量 (Declares local functions, macros and variables necessary for the internal functions)

   * - CanIf_Internal.c
     - 实现CanIf模块内部功能所必须的local函数，local宏定义，local变量 (Implements local functions, macros and variables necessary for the internal functions)

   * - CanIf_DetError.h
     - 声明CanIf模块DET错误检测功能的函数接口 (Declares DET error detection interfaces)

   * - CanIf_DetError.c
     - 实现CanIf模块DET错误检测功能的函数接口 (Implements DET error detection interfaces)

   * - CanIf_CanTrcv.h
     - 声明CanIf模块提供给CanTrcv模块的回调函数 (Declares callback functions for CanTrcv interaction)

   * - CanIf_Can.h
     - 声明CanIf模块提供给Can模块的回调函数 (Declares callback functions for CAN interaction)

   * - CanIf_Cbk.h
     - 包含CanIf模块全部回调函数的声明 (Contains declarations of all CanIf callback functions)

   * - CanIf_MemMap.h
     - 声明CanIf模块内存布局 (Defines memory mapping configuration for CanIf module)

动态文件(Dynamic Files)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - 文件(File)
     - 描述(Description)
   * - CanIf_CfgTypes.h
     - 定义PB/PC配置参数结构体类型，以及内部运行时结构体类型 (Defines PB/PC configuration parameter structure types and internal runtime structure types)

   * - CanIf_Cfg.h
     - 定义CanIf模块PC配置的宏定义 (Defines macros for CanIf module's PC configuration)

   * - CanIf_Cfg.c
     - 定义CanIf模块PC配置的结构体参数 (Defines structure parameters for CanIf module's PC configuration)

   * - CanIf_PBcfg.h
     - 定义CanIf模块PB配置的宏定义 (Defines macros for CanIf module's PB configuration)

   * - CanIf_PBcfg.c
     - 定义CanIf模块PB配置的结构体参数 (Defines structure parameters for CanIf module's PB configuration)

错误处理(Error Handling)
----------------------------------

开发错误(Development Errors)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. list-table::
   :widths: 20 10 30
   :header-rows: 1

   * - Error code
     - Value[Hex]
     - Description

   * - CANIF_E_PARAM_CANID
     - 0x0A
     - API service called with invalid CAN ID

   * - CANIF_E_PARAM_HOH
     - 0x0C
     - API service called with invalid hardware object

   * - CANIF_E_PARAM_LPDU
     - 0x0D
     - API service called with invalid PDU ID

   * - CANIF_E_PARAM_CONTROLLERID
     - 0x0F
     - API service called with invalid controller ID

   * - CANIF_E_PARAM_WAKEUPSOURCE
     - 0x10
     - API service called with invalid wakeup source

   * - CANIF_E_PARAM_TRCV
     - 0x11
     - API service called with invalid transceiver ID

   * - CANIF_E_PARAM_TRCVMODE
     - 0x12
     - API service called with invalid transceiver mode

   * - CANIF_E_PARAM_TRCVWAKEUPMODE
     - 0x13
     - API service called with invalid transceiver wakeup mode

   * - CANIF_E_PARAM_POINTER
     - 0x14
     - API service called with invalid pointer

   * - CANIF_E_PARAM_CTRLMODE
     - 0x15
     - API service called with invalid controller mode

   * - CANIF_E_PARAM_PDU_MODE
     - 0x16
     - API service called with invalid PDU mode

   * - CANIF_E_PARAM_CAN_ERROR
     - 0x17
     - API services called with invalid parameter

   * - CANIF_E_UNINIT
     - 0x1E
     - API service used without module initialization

   * - CANIF_E_INVALID_TXPDUID
     - 0x32
     - Transmit PDU ID invalid

   * - CANIF_E_INVALID_RXPDUID
     - 0x3C
     - Receive PDU ID invalid

   * - CANIF_E_INIT_FAILED
     - 0x50
     - CAN Interface initialisation failed

产品错误(Product Errors)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
None

运行时错误(Runtime Errors)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 20 10 30
   :header-rows: 1

   * - Error code
     - Value[Hex]
     - Description

   * - CANIF_E_INVALID_DATA_LENGTH
     - 0x3D
     - Failed Data Length Check

   * - CANIF_E_DATA_LENGTH_MISMATCH
     - 0x3E
     - Data Length

   * - CANIF_E_STOPPED
     - 0x46
     - Transmit requested on offline PDU channel

   * - CANIF_E_TXPDU_LENGTH_EXCEEDED
     - 0x5A
     - Message length was exceeding the maximum length


接口描述(Interface Description)
=========================================

.. 目前能够自动生成的有类型定义，普通函数，回调函数。
.. 有些模块的API来自多个头文件，需要自行裁剪合并
.. 引用接口描述。来自于code->doxygen->xml->rst
.. include:: CanIf_h_api.rst

.. include:: CanIf_Can_h_api.rst

.. include:: CanIf_CanTrcv_h_api.rst

配置(Configuration)
------------------------------

1.(Tx Data Path)
----------------------

配置数据发送路径，需要引用上层EcuC的Pdu和下层CanDrv的CanController，
并逐层配置CanIfTxPduCfg、CanIfBufferCfg、CanIfHthCfg、CanIfCtrlCfg。

To configure the data transmission path, reference the Pdu of the upper-layer EcuC and the CanController of the lower-layer CanDrv, then configure CanIfTxPduCfg, CanIfBufferCfg, CanIfHthCfg, and CanIfCtrlCfg layer by layer.

.. figure:: /_static/参考手册(Module_Reference_Manual)/CanIf/image2.png
   :name: CanIf_CanIfTxPduCfg
   :align: center

   CanIfTxPduCfg

.. figure:: /_static/参考手册(Module_Reference_Manual)/CanIf/image3.png
   :name: CanIf_CanIfBufferCfg
   :align: center

   CanIfBufferCfg

.. figure:: /_static/参考手册(Module_Reference_Manual)/CanIf/image4.png
   :name: CanIf_Pdu
   :align: center

   EcuC Pdu

如图，

As shown in the figure,

 - 配置项CanIfTxPduCfg/CanIfTxPduRef，向上关联了EcuC的Pdu

   The configuration item CanIfTxPduCfg/CanIfTxPduRef references the Pdu of the upper-layer EcuC.

 - 配置项CanIfTxPduCfg/CanIfTxPduBufferRef，向下关联了CanIfBufferCfg

   The configuration item CanIfTxPduCfg/CanIfTxPduBufferRef references the lower-layer CanIfBufferCfg.


.. figure:: /_static/参考手册(Module_Reference_Manual)/CanIf/image5.png
   :name: CanIf_CanIfHthCfg
   :align: center

   CanIfHthCfg

.. figure:: /_static/参考手册(Module_Reference_Manual)/CanIf/image6.png
   :name: CanIf_CanIfCtrlCfg
   :align: center

   CanIfCtrlCfg

如图，

As shown in the figure,

 - 配置项CanIfBufferCfg/CanIfBufferHthRef，向下关联了CanIfHthCfg

   The configuration item CanIfBufferCfg/CanIfBufferHthRef references the lower-layer CanIfHthCfg.

 - 配置项CanIfHthCfg/CanIfHthCanCtrlIdRef，向下关联了CanIfCtrlCfg

   The configuration item CanIfHthCfg/CanIfHthCanCtrlIdRef references the lower-layer CanIfCtrlCfg.

2.(Rx Data Path)
----------------------

配置数据接收路径，需要引用上层EcuC的Pdu和下层CanDrv的CanController，
并逐层配置CanIfTxPduCfg、CanIfHrhCfg、CanIfCtrlCfg。

To configure the data reception path, reference the Pdu of the upper-layer EcuC and the CanController of the lower-layer CanDrv, and configure CanIfTxPduCfg, CanIfHrhCfg, and CanIfCtrlCfg layer by layer.

.. figure:: /_static/参考手册(Module_Reference_Manual)/CanIf/image7.png
   :name: CanIf_CanIfRxPduCfg
   :align: center

   CanIfRxPduCfg

.. figure:: /_static/参考手册(Module_Reference_Manual)/CanIf/image8.png
   :name: CanIf_CanIfHrhCfg
   :align: center

   CanIfHrhCfg

如图，

As shown in the figure,

 - 配置项CanIfRxPduCfg/CanIfRxPduRef，向上关联了EcuC的Pdu

   The configuration item CanIfRxPduCfg/CanIfRxPduRef references the Pdu of the upper-layer EcuC.

 - 配置项CanIfRxPduCfg/CanIfRxPduHrhIdRef，向下关联了CanIfHrhCfg

   The configuration item CanIfRxPduCfg/CanIfRxPduHrhIdRef references the lower-layer CanIfHrhCfg.

 - 配置项CanIfHrhCfg/CanIfHrhCanCtrlIdRef，向下关联了CanIfCtrlCfg

   The configuration item CanIfHrhCfg/CanIfHrhCanCtrlIdRef references the lower-layer CanIfCtrlCfg.

