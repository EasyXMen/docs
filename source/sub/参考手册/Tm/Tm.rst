===================
Tm
===================



文档信息（Document Information）
=======================================

版本历史（Version History）
-----------------------------------

.. list-table::
   :widths: 10 10 10 10 20
   :header-rows: 1

   * - 日期（Date）
     - 作者（Author）
     - 版本（Version）
     - 状态（Status）
     - 说明（Description）
   * - 2025/01/24
     - xudong.guan
     - V0.1
     - 发布（Release）
     - 首次发布（First release）
   * - 2025/04/04
     - xudong.guan
     - V1.0
     - 发布（Release）
     - 正式发布（Official release）

参考文档（Reference Document）
----------------------------------

.. list-table::
   :widths: 10 10 30 10
   :header-rows: 1

   * - 编号（Number）
     - 分类（Classification）
     - 标题（Title）
     - 版本（Version）
   * - 1
     - Autosar
     - AUTOSAR_CP_SRS_TimeService.pdf
     - R23-11
   * - 2
     - Autosar
     - AUTOSAR_CP_SWS_TimeService.pdf
     - R23-11 

术语与简写（Terms and Abbreviations）
========================================

术语（Term）
--------------
   .. :align: center   表格内容居中

.. list-table::
   :widths: 15 40
   :header-rows: 1

   * - 术语（Term）
     - 解释（Explanation）

   * - GPT Predef Timer
     - GPT Predef Timer是由GPT driver提供的自由运行的向上计数器。哪些GPT Predef Timer可用取决于硬件（时钟、硬件定时器、预分频器、定时器寄存器宽度等）和配置。GPT Predef Timer具有预定义的物理时间单位和范围
       
       A GPT Predef Timer is a free running up counter provided by the GPT driver. Which GPT Predef Timer(s) are available depends on hardware (clock, hardware timers, prescaler, width of timer register, ...) and configuration. A GPT Predef Timer has predefined physical time unit and range.

   * - Time Service Predef Timer
     - Time Service Predef Timer是具有预定义物理时间单位和范围的自由运行向上计数器。其硬件定时器功能基于对应的GPT Predef Timer实现。Time Service模块会为每个Predef Timer提供一组API services。用户可实例化任意数量的定时器（仅受可用内存限制），且各定时器实例的使用完全相互独立。
       
       A Time Service Predef Timer is a free running up counter with predefined physical time unit and range. The hardware timer functionality is based on the corresponding GPT Predef Timer. For each Predef Timer a set of API services is provided by the Time Service module. The user can instantiate any timers (only limited by available memory) and can use the instances completely independently of each other.

   * - Timer instance
     - timer instance是API数据类型Tm_PredefTimer...bitType的数据对象，这意味着它是Time Service Predef Timer在用户软件层面的实例化产物。用户可实例化任意数量的定时器（仅受可用内存限制）。通过API services提供的方法，各timer instance的使用可完全相互独立。
       
       A timer instance is a data object of an API data type Tm_PredefTimer...bitType, this means it is an instantiation of a Time Service Predef Timer on user software level. The user can instantiate any timers (only limited by available memory). The timer instances can be used completely independently of each other by methodes provided as API services.

   * - Reference time
     - reference time是为每个timer instance存储的时间值。它是API数据类型Tm_PredefTimer...bitType中一个与实现相关的元素。
       
       The reference time is a time value stored for each timer instance. It’s an implementation specific element of the API data types Tm_PredefTimer...bitType.

简写（Abbreviation）
-----------------------

.. list-table::
   :widths: 10 20 30
   :header-rows: 1


   * - 简写（Abbreviation）
     - 全称（Full name）
     - 解释（Explanation）

   * - GPT
     - General Purpose Timer
     - 通用定时器模块，提供高精度定时功能，提供接口作为Tm模块获取时间来源基础。
       The general-purpose timer module provides high-precision timing functions and offers interfaces as the basis for the Tm module to obtain time sources.

   * - nop
     - No operation
     - 无操作。


简介（Introduction）
==============================
如图所示Tm模块位于系统服务，所有层都可以使用系统服务。Tm模块可以越过一个软件层来访问GPT，而GPT不能与其他MCAL模块直接产生交互。

As shown in the figure, the Tm module is located in the system services, and all layers can use the system services. The Tm module can access GPT across a software layer, while GPT cannot directly interact with other MCAL modules.

复杂驱动和ECU抽象层与GPT存在交互，但不受Tm模块影响。

Complex drivers and the ECU Abstraction Layer interact with GPT, but are not affected by the Tm module.

.. figure:: ../../../_static/参考手册/Tm/Tm_ArchitectureFig.png
   :alt: Tm架构层次图
   :name: fig_arch
   :align: center

   Tm架构层次图

   Tm Architecture Hierarchy Diagram

功能描述（Functional Description）
==========================================

特性（Features）
-------------------------

Tm功能介绍（Introduction to Tm Functions）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Tm模块通过直接访问GPT硬件，经过一定转换后给其他BSW模块提供接口从而可以初始化一个时钟，随时获取其经过时间，或者可以主动忙碌等待一段时间，并可以对时钟进行偏移等操作。

The Tm module directly accesses GPT hardware, and after certain conversions, provides interfaces for other BSW modules to initialize a clock, obtain its elapsed time at any time, actively wait for a period of time in a busy state, and perform operations such as offsetting the clock.

不同种类的时钟，也称为“Tm预定义时钟”，在硬件的和配置支持下存在。每一个预定义时钟都有一个预定义的tick duration（最小单位记录时长）和一个预定义的字节数（物理范围）。这些预定义时钟是基于GPT预定义时钟的，这是GPT驱动提供的自由运行的硬件时钟。

Different types of clocks, also known as "Tm predefined clocks", exist with hardware and configuration support. Each predefined clock has a predefined tick duration (minimum unit recording time) and a predefined number of bytes (physical range). These predefined clocks are based on GPT predefined clocks, which are free - running hardware clocks provided by the GPT driver.

共有以下四种预定义时钟：Tm_PredefTimer1us16bitType，Tm_PredefTimer1us24bitType，Tm_PredefTimer1us32bitType，Tm_PredefTimer100us32bitType。（前一项为tick duration，后一项为字节大小）。

There are four predefined clocks in total: Tm_PredefTimer1us16bitType, Tm_PredefTimer1us24bitType, Tm_PredefTimer1us32bitType, and Tm_PredefTimer100us32bitType. (The first part is the tick duration, and the latter part is the byte size).

那么，Tm提供的服务也都支持这四种时钟。相关服务有：Tm_ResetTimer…, Tm_GetTimeSpan…, Tm_ShiftTimer…, Tm_SyncTimer…, Tm_BusyWait…。注意100us不支持BusyWait。

Then, the services provided by Tm also support these four clocks. The related services include: Tm_ResetTimer…, Tm_GetTimeSpan…, Tm_ShiftTimer…, Tm_SyncTimer…, Tm_BusyWait… It should be noted that 100us does not support BusyWait.

集成（Integration）
============================

文件列表（File List）
----------------------------------

静态文件（Static Files）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - 文件（File）
     - 描述（Description）
   
   * - Tm.c
     - Tm模块源码文件，包含需要使用的宏定义，内部变量，内部函数，全局函数。
       
       Source code files of the Tm module, including macros, internal variables, internal functions, and global functions that need to be used.

   * - Tm.h
     - Tm模块头文件，包含需要使用的宏定义，类型定义，配置结构体声明，外部函数声明。
       
       Header file of the Tm module, including macros, type definitions, configuration structure declarations, and external function declarations that need to be used.

   * - Tm_MemMep.h
     - Tm的内存映射定义文件。
       
       Memory mapping definition file of the Tm module.

动态文件（Dynamic Files）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - 文件（File）
     - 描述（Description）

   * - Tm_Cfg.h
     - Tm模块配置头文件，包含配置宏定义。
       
       Configuration header file of the Tm module, including configuration macro definitions.

错误处理（Error handling）
--------------------------------

开发错误（Development errors）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. list-table:: 
   :widths: 20 10 30
   :header-rows: 1

   * - Error code
     - Value[hex]
     - Description

   * - TM_E_PARAM_POINTER
     - 0x01
     - 调用API服务的时候传入了非法（例如空指针）的指针。
       
       An illegal pointer (such as a null pointer) was passed when calling the API service.

   * - TM_E_PARAM_VALUE
     - 0x02
     - 调用API服务的时候传入了非法的参数。
       
       An illegal parameter was passed when calling the API service.

产品错误（Product Errors）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

None

运行时错误（Runtime error）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   - TM_E_HARDWARE_TIMER
   - 0x03
   - 访问底层硬件计时器（GPT Predef Timer）失败。

     Failed to access the underlying hardware timer (GPT Predef Timer).


接口描述（Interface Description）
=======================================

.. include:: Tm_h_api.rst


依赖的服务（Dependent Services）
------------------------------------------------

强制接口（Mandatory Interfaces）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 10 5 30
   :header-rows: 1

   * - API Function
     - Header File
     - Description

   * - Det_ReportRuntimeError
     - Det.h
     - Service to report runtime errors. If a callout has been configured then this callout shall be called.

   * - Gpt_GetPredefTimerValue
     - Gpt.h
     - Delivers the current value of the desired GPT Predef Timer.

可选接口（Optional Interfaces）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 10 5 30
   :header-rows: 1

   * - API Function
     - Header File
     - Description

   * - Det_ReportError
     - Det.h
     - Service to report development errors

服务封装（Service Encapsulation）
-----------------------------------------------------
Tm无服务封装接口。

The Tm module has no service encapsulation interfaces.

配置（Configuration）
============================


基础配置说明（Basic Configuration Description）
-----------------------------------------------------

开发错误检测开关（Development Error Detection Switch）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Tm模块提供TmDevErrorDetection开关，用于控制是否开启Tm模块的开发错误检测功能。

The Tm module provides the TmDevErrorDetection switch, which is used to control whether to enable the development error detection function of the Tm module.

.. figure:: ../../../_static/参考手册/Tm/Tm_cfg_det.png
   :alt: Tm配置-开发错误检测开关
   :name: fig_cfg_det
   :align: center

   Tm配置图-开发错误检测

   Tm Configuration Diagram - Development Error Detection


预定时器接口使能开关（Predefined Timer Interface Enable Switches）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Tm模块支持4种预定时器，分别是1us16bit，1us24bit,1us32bit和100us32bit，并提供相应的开关来控制是否使能相应的定时器接口。

The Tm module supports 4 types of predefined timers, namely 1us16bit, 1us24bit, 1us32bit, and 100us32bit, and provides corresponding switches to control whether to enable the corresponding timer interfaces.

.. figure:: ../../../_static/参考手册/Tm/Tm_cfg_predefTimer.png
   :alt: Tm配置-预定时器接口使能开关
   :name: fig_cfg_predefTimer
   :align: center

   Tm配置图-预定时器接口使能开关

   Tm Configuration Diagram - Predefined Timer Interface Enable Switches

版本获取开关（Version Acquisition Switch）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Tm模块提供版本获取开关，用于控制是否获取版本号。

The Tm module provides a version acquisition switch to control whether to obtain the version number.

.. figure:: ../../../_static/参考手册/Tm/Tm_cfg_version.png
   :alt: Tm配置-版本获取开关
   :name: fig_cfg_version
   :align: center

   Tm配置图-版本获取开关

   Tm Configuration Diagram - Version Acquisition Switch


