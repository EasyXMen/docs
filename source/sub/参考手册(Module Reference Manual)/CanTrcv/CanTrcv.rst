========================
CanTrcv
========================


文档信息 Document Information
==================================

历史版本 Version History
----------------------------------------------------------

.. list-table::
   :widths: 10 10 10 10 10
   :header-rows: 1

   * - 日期(Date)
     - 作者(Author)
     - 版本(Version)
     - 状态(Status)
     - 说明(Description)

   * - 2025/4/2
     - Zhijia.Zou
     - V0.1
     - 发布(Release)
     - 首次发布(First release)

   * - 2025/04/04
     - Zhijia.Zou
     - V1.0
     - 发布(Release)
     - 正式发布(Official release)


参考文档 Reference Document
----------------------------------------------------------

.. list-table::
   :widths: 10 20 30 10
   :header-rows: 1

   * - 编号(Number)
     - 分类(Classification)
     - 标题(Title)
     - 版本(Version)
   * - 1
     - Autosar
     -  AUTOSAR_SWS_CanTransceiverDriver.pdf
     - R23-11
   * - 2
     - Autosar
     - AUTOSAR_SRS_CAN.pdf
     - R23-11

术语与简写 Terms and Abbreviations
==================================

术语 Terms
----------------------------------------------------------
None

简写 Abbreviations
----------------------------------------------------------
None

简介 Introduction
==================================

CanTrcv功能介绍 CanTrcv Function Introduction
----------------------------------------------------------

CAN收发器驱动程序模块负责处理ECU上的CAN收发器硬件芯片，并将CAN总线上使用的信号电平调整为微控制器可以识别的逻辑(数字)信号电平。此外，收发器还能检测到电气故障，如线路问题、地面偏移或长主导信号的传输。

The CAN Transceiver Driver module is responsible for handling the CAN transceiver hardware chip on the ECU and adjusting the signal level used on the CAN bus to a logic (digital) signal level recognizable by the microcontroller. In addition, the transceiver can detect electrical faults, such as line problems, ground offsets, or the transmission of long dominant signals.

根据CAN收发器与微控制器的接口，驱动程序模块可以标记由外部端口pin记录的探测错误或由SPI总线记录的检测错误；特定CAN收发器支持电源控制，并通过CAN总线唤醒。有些CAN收发器具备特定功能，如系统基础芯片(SBC)，它除了CAN基本功能之外，还实现了电源控制和高级监控，并通过SPI总线和MCU进行访问。部分网络唤醒是CAN系统中的一种状态，其中一些节点处于低功耗模式，而其他节点正在通信。这减少了整个网络的功耗。在低功耗模式下，节点被预先定义的唤醒帧唤醒。支持选择性唤醒的收发器除了普通收发器提供的唤醒模式(Wakeup Pattern)外，还可以通过唤醒帧(Wakeup Frame)来唤醒。

According to the interface between the CAN transceiver and the microcontroller, the driver module can flag detection errors recorded by external port pins or detection errors recorded by the SPI bus; specific CAN transceivers support power control and can wake up through the CAN bus. Some CAN transceivers have specific functions, such as System Basis Chips (SBCs), which, in addition to the basic CAN functions, also implement power control and advanced monitoring, and are accessed by the MCU through the SPI bus. Partial network wakeup is a state in the CAN system where some nodes are in low-power mode while other nodes are communicating. This reduces the power consumption of the entire network. In low-power mode, nodes are woken up by pre-defined Wakeup Frame. Transceivers that support selective wakeup can be woken up by Wakeup Frame in addition to the Wakeup Pattern provided by ordinary transceivers.

CanTrcv功能实现 CanTrcv Function Implementation
--------------------------------------------------------------------

CAN收发器驱动程序的目标是指定适合CAN收发器设备的接口和行为和抽象CAN收发器硬件；它为上层提供了一个独立于硬件的接口；它通过使用MCAL层的API接口访问CAN收发器硬件，从ECU布局中抽象出来。

The goal of the CAN Transceiver Driver is to specify interfaces and behaviors suitable for CAN transceiver devices and abstract the CAN transceiver hardware; it provides a hardware-independent interface for the upper layer; it accesses the CAN transceiver hardware by using the API interface of the MCAL layer, abstracting away from the ECU layout.

CanTrcv在访问到硬件，发现唤醒事件之后，也可以通过回调接口通知到上层CanIf/EcuM从而使BSW能处理这些唤醒事件。

After the CanTrcv accesses the hardware and detects a wakeup event, it can also notify the upper-layer CanIf/EcuM through a callback interface, so that the BSW can handle these wakeup events.

偏差 Deviations
----------------------------------------------------------

None

扩展 Extensions
----------------------------------------------------------

None

集成 Integration
==================================

文件列表 File List
----------------------------------------------------------

文件结构图 File Structure Diagram
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../../../_static/参考手册/CanTrcv/CanTrcv文件结构图.png


静态文件 Static Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 5 10 
   :header-rows: 1

   * - 文件(File)
     - 说明(Description)

   * - CanTrcv.c
     - 包含需要使用的宏定义，内部变量，内部函数，全局函数。(Contains macro definitions, internal variables, internal functions, and global functions that need to be used.)

   * - CanTrcv_Driver.c
     - 包含需要使用的关于硬件的宏定义，内部变量，内部函数。(Contains macro definitions related to hardware, internal variables, and internal functions that need to be used.)

   * - CanTrcv_Driver.h
     - 包含需要使用的关于硬件的宏定义，类型定义，内部函数声明。(Contains macro definitions related to hardware, type definitions, and internal function declarations that need to be used.)

   * - CanTrcv_Types.h
     - 包含需要使用的类型定义。(Contains type definitions that need to be used.)

   * - CanTrcv.h
     - 包含需要使用的宏定义，类型定义，配置结构体声明，外部函数声明。(Contains macro definitions, type definitions, configuration structure declarations, and external function declarations that need to be used.)

动态文件 Dynamic Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 5 10 
   :header-rows: 1

   * - 文件(File)
     - 说明(Description)

   * - CanTrcv_Cfg.h
     - 生成CanTrcv模块配置相关的宏定义。(Generates macro definitions related to the CanTrcv module configuration.)

   * - CanTrcv_Cfg.c
     - 生成CanTrcv模块配置相关的结构体。(Generates structures related to the CanTrcv module configuration.)

   * - CanTrcv_MemMap.h
     - CanTrcv模块的内存映射。(Memory mapping of the CanTrcv module.)

错误处理 Error Handling
----------------------------------------------------------

开发错误 Development Errors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 5 10 20
   :header-rows: 1

   * - Error code
     - Value[hex]
     - Description

   * - CANTRCV_E_INVALID_TRANSCEIVER
     - 0x01
     - API called with wrong parameter for the CAN transceiver

   * - CANTRCV_E_PARAM_POINTER
     - 0x02
     - API called with null pointer parameter

   * - CANTRCV_E_UNINIT
     - 0x0B
     - API service used without initialization

   * - CANTRCV_E_TRCV_NOT_STANDBY
     - 0x15
     - API service called in wrong transceiver operation mode (STANDBY expected)

   * - CANTRCV_E_TRCV_NOT_NORMAL
     - 0x16
     - API service called in wrong transceiver operation mode (NORMAL expected)

   * - CANTRCV_E_PARAM_TRCV_WAKEUP_MODE
     - 0x17
     - API service called with invalid parameter for Trcv WakeupMode

   * - CANTRCV_E_PARAM_TRCV_OPMODE
     - 0x18
     - API service called with invalid parameter for Op Mode

   * - CANTRCV_E_BAUDRATE_NOT_SUPPORTED
     - 0x19
     - Configured baud rate is not supported by the transceiver

   * - CANTRCV_E_INIT_FAILED
     - 0x1A
     - Module initialization has failed, e.g. CanTrcv_Init() called with an invalid pointer in postbuild.

运行时错误 Runtime Errors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 5 10 20
   :header-rows: 1

   * - Error code
     - Value[hex]
     - Description

   * - CANTRCV_E_NO_TRCV_CONTROL
     - 0x1A
     - No/incorrect communication to transceiver.

.. include:: CanTrcv_h.rst