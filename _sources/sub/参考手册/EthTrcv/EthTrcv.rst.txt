====================
EthTrcv
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
     - AUTOSAR_SWS_EthernetTransceiverDriver.pdf
     - R23-11

   * - 2
     - Autosar
     - AUTOSAR_SWS_ECUStateManager.pdf
     - R23-11

   * - 3
     - Autosar
     - AUTOSAR_SWS_EthernetInterface.pdf
     - R23-11


术语与简写 Terms and Abbreviations
============================================================

术语 Terms
----------------------------------------------------
.. :align: center   表格内容居中(Table contents are centered)

None

简写 Abbreviations
----------------------------------------------------

.. list-table::
   :widths: 10 20 30
   :header-rows: 1

   * - 简写(Abbreviation)
     - 全称(Full name)
     - 解释(Explanation)

   * - EC
     - Ethernet controller
     - 以太网控制器

   * - ET
     - Ethernet transceiver
     - 以太网收发器

   * - Eth
     - Ethernet Controller Driver
     - 以太网控制器驱动

   * - EthIf
     - Ethernet Interface
     - 以太网接口

   * - EthTrcv
     - Ethernet Transceiver Driver
     - 以太网收发器驱动

   * - MCG
     - Module Configuration Generator
     - 模块配置生成器

   * - MII
     - Media Independent Interface
     - 媒体独立接口

   * - PLCA
     - Physical Layer Collision Avoidance
     - 物理层碰撞避免

   * - P2P
     - Point-to-Point
     - 链路层协议

   * - TO
     - Transmit Opportunity
     - 发送机会


简介 Introduction
==============================

在AUTOSAR分层软件体系结构中，EthTrcv属于微控制器抽象层， 它是一个以太网收发器的驱动模块。

In the AUTOSAR layered software architecture, EthTrcv belongs to the Microcontroller Abstraction Layer, and it is a driver module for the Ethernet transceiver.

EthTrcv模块的主要任务是向上层（以太网接口）提供独立于硬件的接口，因为包括多个相同的收发器，

The main task of the EthTrcv module is to provide a hardware-independent interface to the upper layer (Ethernet Interface). Since multiple identical transceivers are included,

所以对于所有的收发器来说，接口应该统一，这样上层（以太网接口）可以以统一的方式访问底层总线系统。

the interface shall be unified for all transceivers, so that the upper layer (Ethernet Interface) can access the underlying bus system in a unified manner.

.. figure:: ../../../_static/参考手册/EthTrcv/image1.png
   :name: EthTrcv_arch
   :align: center

   EthTrcv模块层次图 (EthTrcv Module Layer Diagram)


功能描述 Functional Description
============================================================

模式设置功能 Mode Setting Function
--------------------------------------------------------------------------------------------------------

以设置收发器的状态为例，上层EthIf调用设置收发器状态的API，EthTrcv通过对芯片的寄存器的值进行修改，从而到达修改收发器状态的目的。

Taking setting the state of the transceiver as an example: the upper layer EthIf calls the API for setting the transceiver state, and EthTrcv modifies the value of the chip's register, so as to achieve the purpose of modifying the transceiver state.

唤醒检测功能 Wakeup Detection Function
--------------------------------------------------------------------------------------------------------

以太网收发器驱动程序应支持唤醒取决于配置参数EthTrcvWakeUpSupport，要么根本不支持(ETHTRCV_WAKEUP_NOT_SUPPORTED)，或通过中断(ETHTRCV_WAKEUP_BY_INTERRUPT)，或通过轮询(ETHTRCV_WAKEUP_BY_POLLING)。

The Ethernet Transceiver Driver shall support wakeup depending on the configuration parameter EthTrcvWakeUpSupport: it either does not support wakeup at all (ETHTRCV_WAKEUP_NOT_SUPPORTED), or supports it via interrupt (ETHTRCV_WAKEUP_BY_INTERRUPT),or supports it via polling (ETHTRCV_WAKEUP_BY_POLLING).

如果以太网收发器驱动程序检测到唤醒，它会将收发器硬件提供的唤醒原因映射到EcuM定义的唤醒事件。

If the Ethernet Transceiver Driver detects a wakeup, it maps the wakeup reason provided by the transceiver hardware to the wakeup event defined by EcuM.

以太网收发器驱动程序将支持以下场景：

The Ethernet Transceiver Driver shall support the following scenarios:

1.休眠的ECU 和休眠的总线 -> 通过EthTrcv_Init唤醒检测（在开机期间调用）

1.Dormant ECU and dormant bus -> Wakeup detection via EthTrcv_Init (called during power-on)


2.唤醒的ECU 和休眠的总线 -> 通过EthTrcv_MainFunction或唤醒中断处理程序唤醒检测（由EcuM中的CheckWakeup检查）

2.Awake ECU and dormant bus -> Wakeup detection via EthTrcv_MainFunction or wakeup interrupt handler (checked by CheckWakeup in EcuM)



特性 Features
----------------------------------------------------

不支持变体功能 Variant function is not supported


集成 Integration
==============================

文件列表 File List
----------------------------------------------------

静态文件 Static Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - 文件(File)
     - 描述(Description)

   * - EthTrcv.h
     - 声明EthTrcv模块的全部外部接口（除了回调函数），以及配置文件中的全局变量。(Declares all external interfaces of the EthTrcv module (except callback functions) and global variables in the configuration file.)

   * - EthTrcv.c
     - 作为EthTrcv模块的核心文件，实现EthTrcv模块全部对外接口，以及实现EthTrcv模块功能所必须的local函数，local宏定义，local变量定义。(Serves as the core file of the EthTrcv module; implements all external interfaces of the EthTrcv module, as well as local functions, local macros, and local variable definitions necessary for implementing the functions of the EthTrcv module.)

   * - EthTrcv_Types.h
     - 定义EthTrcv模块外部/内部类型，包括AUTOSAR标准定义的类型。(Defines external/internal types of the EthTrcv module, including types defined by the AUTOSAR standard.)

   * - EthTrcv_Internal.h
     - 声明EthTrcv模块内部功能所必须的local函数，local宏定义，local变量。(Declares local functions, local macros, and local variables necessary for the internal functions of the EthTrcv module.)

   * - EthTrcv_Internal.c
     - 实现EthTrcv模块内部功能所必须的local函数，local宏定义，local变量。(Implements local functions, local macros, and local variables necessary for the internal functions of the EthTrcv module.)

   * - EthTrcv_DetError.h
     - 声明EthTrcv模块DET错误检测功能的函数接口。(Declares the function interfaces for the DET error detection function of the EthTrcv module.)

   * - EthTrcv_DetError.c
     - 实现EthTrcv模块DET错误检测功能的函数接口。(Implements the function interfaces for the DET error detection function of the EthTrcv module.)

   * - EthTrcv_Cbk.h
     - 包含EthTrcv模块全部回调函数的声明。(Contains declarations of all callback functions of the EthTrcv module.)

   * - EthTrcv_MemMap.h
     - 声明EthTrcv模块内存布局。(Declares the memory layout of the EthTrcv module.)

动态文件 Dynamic Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - 文件(File)
     - 描述(Description)

   * - EthTrcv_CfgTypes.h
     - 定义PB/PC配置参数结构体类型，以及内部运行时结构体类型。(Defines the structure types of PB/PC configuration parameters and internal runtime structure types.)

   * - EthTrcv_Cfg.h
     - 定义EthTrcv模块PC配置的宏定义。(Defines the macros for the PC configuration of the EthTrcv module.)

   * - EthTrcv_Cfg.c
     - 定义EthTrcv模块PC配置的结构体参数。(Defines the structure parameters for the PC configuration of the EthTrcv module.)

   * - EthTrcv_PBcfg.h
     - 定义EthTrcv模块PB配置的宏定义。(Defines the macros for the PB configuration of the EthTrcv module.)

   * - EthTrcv_PBcfg.c
     - 定义EthTrcv模块PB配置的结构体参数。(Defines the structure parameters for the PB configuration of the EthTrcv module.)


错误处理 Error Handling
----------------------------------------------------

开发错误 Development Errors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 20 10 30
   :header-rows: 1

   * - Error code
     - Value[hex]
     - Description

   * - ETHTRCV_E_INV_TRCV_IDX
     - 0x01
     - Invalid transceiver index

   * - ETHTRCV_E_UNINIT
     - 0x02
     - EthTrcv module was not initialized

   * - ETHTRCV_E_PARAM_POINTER
     - 0x03
     - Invalid pointer in parameter list

   * - ETHTRCV_E_NOT_SUPPORTED
     - 0x04
     - Functionality is not supported

产品错误 Product Errors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
None

运行时错误 Runtime Errors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 20 10 30
   :header-rows: 1

   * - Error code
     - Value[hex]
     - Description

   * - ETHTRCV_E_MDI_COMMUNICATION
     - 0x04
     - Failure or incorrect communication mode

接口描述 Interface Description
============================================================

.. 目前能够自动生成的有类型定义，普通函数，回调函数。
.. 有些模块的API来自多个头文件，需要自行裁剪合并
.. 引用接口描述。来自于code->doxygen->xml->rst
.. 引用接口描述。 From code->doxygen->xml->rst
.. include:: EthTrcv_h_api.rst


配置 Configuration
----------------------------------------------------

EthTrcv模块全局通用配置

Global General Configuration of the EthTrcv Module

.. figure:: ../../../_static/参考手册/EthTrcv/image2.png
   :name: EthTrcv_EthTrcvGeneral
   :align: center

   EthTrcvGeneral

1. 收发器是否应支持唤醒，取决于配置项EthTrcvWakeUpSupport。

1. Whether the transceiver shall support wakeup depends on the configuration item EthTrcvWakeUpSupport.

EthTrcv模块收发器配置

Transceiver Configuration of the EthTrcv Module

.. figure:: ../../../_static/参考手册/EthTrcv/image3.png
   :name: EthTrcv_EthTrcvConfig
   :align: center

   EthTrcvConfig

