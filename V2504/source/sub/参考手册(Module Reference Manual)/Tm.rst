Tm
#################################

:strong:`缩写词注解 (Abbreviation Notes):`

.. list-table::
   :widths: 34 33 33
   :header-rows: 1

   * - 缩写词 (Abbreviation)
     - 解释/描述 (Explanation/Description)
     - 中文解释 (Chinese explanation)
   * - nop
     - No Operation
     - 无操作 (No operation)


简介 (Introduction)
=================================

Tm在AutoSAR软件层级架构如下图：

Tm in AutoSAR software layer architecture is as follows:

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/Tm/image1.png
   :alt: Tm在AutoSAR软件层级架构图 (TM in AutoSAR Software Hierarchical Architecture Diagram)
   :name: Tm在AutoSAR软件层级架构图 (TM in AutoSAR Software Hierarchical Architecture Diagram)
   :align: center


如图所示Tm模块位于系统服务，所有层都可以使用系统服务。Tm模块可以越过一个软件层来访问GPT，而GPT不能与其他MCAL模块直接产生交互。复杂驱动和ECU抽象层与GPT存在交互，但不受Tm模块影响。

As shown in the figure, the Tm module is located in the system service layer, and all layers can use the system services. The Tm module can access GPT across one software layer, whereas GPT cannot directly interact with other MCAL modules. Complex drivers and ECU abstraction layers have interactions with GPT but are not affected by the Tm module.

参考资料 (Reference materials)
------------------------------------------

[1] AUTOSAR_EXP_LayeredSoftwareArchitecture.pdf，R19-11

[2] AUTOSAR_SWS_TimeService.PDF，R19-11

功能描述 (Function Description)
===========================================

Tm功能 (TM Function)
----------------------------------

Tm功能介绍 (TM Function Introduction)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Tm模块通过直接访问GPT硬件，经过一定转换后给其他BSW模块提供接口从而可以初始化一个时钟，随时获取其经过时间，或者可以主动忙碌等待一段时间。并可以对时钟进行偏移等操作。

The Tm module provides interfaces to other BSW modules for initializing a clock, obtaining elapsed time at any time, or actively busy-waiting for a period. It can also perform offset operations on the clock by directly accessing GPT hardware after certain transformations.

Tm功能实现 (TM Function Implementation)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

不同种类的时钟，也称为“Tm预定义时钟”，在硬件的和配置支持下存在。每一个预定义时钟都有一个预定义的tick duration（最小单位记录时长）和一个预定义的字节数（物理范围）。这些预定义时钟是基于GPT预定义时钟的，这是GPT驱动提供的自由运行的硬件时钟。

Different types of clocks, also referred to as "Tm predefined clocks," exist with hardware and configuration support. Each predefined clock has a predefined tick duration (minimum unit record duration) and a predefined byte count (physical range). These predefined clocks are based on the GPT predefined clock, which is a free-running hardware clock provided by the GPT driver.

共有以下四种预定义时钟：Tm_PredefTimer1us16bitType，

The following four predefined clocks are available: Tm_PredefTimer1us16bitType,

Tm_PredefTimer1us24bitType，Tm_PredefTimer1us32bitType，

Tm_PredefTimer100us32bitType。（前一项为tick duration，后一项为字节大小）。那么，Tm提供的服务也都支持这四种时钟。相关服务有：Tm_ResetTimer…,Tm_GetTimeSpan…, Tm_ShiftTimer…, Tm_SyncTimer…,Tm_BusyWait…。注意100us不支持BusyWait。

Tm_PredefTimer100us32bitType. (The preceding item is tick duration, the latter item is byte size). So, all services provided by Tm also support these four clocks. Related services include: Tm_ResetTimer…, Tm_GetTimeSpan…, Tm_ShiftTimer…, Tm_SyncTimer…, Tm_BusyWait…. Note that 100us does not support BusyWait.

源文件描述 (Source file description)
===============================================

.. centered:: **表 Tm组件文件描述 (Table Tm Component File Description)**

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 文件 (Files)
     - 说明 (Description)
   * - Tm.c
     - 包含需要使用的宏定义，内部变量，内部函数，全局函数。 (Contains the macros needed for use, internal variables, internal functions, and global functions.)
   * - Tm.h
     - 包含需要使用的宏定义，类型定义，配置结构体声明，外部函数声明。 (Contain macro definitions, type definitions, configuration structure declarations, and external function declarations.)
   * - Tm_Cfg.h
     - 包含配置宏定义。 (Include configuration macro definitions.)




.. figure:: ../../_static/参考手册(Module_Reference_Manual)/Tm/image2.png
   :alt: Tm组件文件交互关系图 (Tm Component File Interactions Diagram)
   :name: Tm组件文件交互关系图 (Tm Component File Interactions Diagram)
   :align: center

API接口 (API Interface)
=====================================

类型定义 (Type definition)
--------------------------------------

Tm_PredefTimer1us16bitType类型定义 (Tm_PredefTimer1us16bitType type definition)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 名称 (Name)
     - Tm_PredefTimer1us16bitType
   * - 类型 (Type)
     - Structure
   * - 范围 (Range)
     - 无
   * - 描述 (Description)
     - Tm模块预定义1us16bit时钟的数据结构体，存放参考时间。 (The Tm module predefines a data structure for 1us 16-bit clock, storing the reference time.)




Tm_PredefTimer1us24bitType类型定义 (Definition of Tm_PredefTimer1us24bitType type)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 名称 (Name)
     - Tm_PredefTimer1us24bitType
   * - 类型 (Type)
     - Structure
   * - 范围 (Range)
     - 无
   * - 描述 (Description)
     - Tm模块预定义1us24bit时钟的数据结构体，存放参考时间。 (The Tm module predefined data structure for 1us 24-bit clock data, storing reference time.)




Tm_PredefTimer1us32bitType类型定义 (Tm_PredefTimer1us32bitType type definition)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 名称 (Name)
     - Tm_PredefTimer1us32bitType
   * - 类型 (Type)
     - Structure
   * - 范围 (Range)
     - 无
   * - 描述 (Description)
     - Tm模块预定义1us32bit时钟的数据结构体，存放参考时间。 (The Tm module predefines a data structure for 1us 32-bit clock, storing reference time.)




Tm_PredefTimer100us32bitType类型定义 (Tm_PredefTimer100us32bitType type definition)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 名称 (Name)
     - Tm_PredefTimer100us32bitType
   * - 类型 (Type)
     - Structure
   * - 范围 (Range)
     - 无
   * - 描述 (Description)
     - Tm模块预定义100us32bit时钟的数据结构体，存放参考时间。 (The TM module predefines a data structure for 100us 32-bit clock, storing reference time.)




输入函数描述 (Describe the input function:)
-----------------------------------------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 输入模块 (Input Module)
     - API
   * - Gpt
     - Gpt_GetPredefTimerValue
   * - Det
     - Det_ReportError
   * - 
     - Det_ReportRuntimeError




静态接口函数定义 (Static interface function definition)
---------------------------------------------------------------

Tm_GetVersionInfo函数定义 (The Tm_GetVersionInfo function definition)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称: (Function Name:)
     - Tm_GetVersionInfo
     - 
     - 
   * - 函数原型: (Function prototype:)
     - FUNC(void,Tm_CODE)
     - 
     - 
   * - 
     - Tm_GetVersionInfo(Std_VersionInfoType\*VersionInfoPtr )
     - 
     - 
   * - 服务编号: (Service Number:)
     - 0x1
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 是 (Is)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - 无
     - 值域： (Domain:)
     - 无
   * - 输入输出参数: (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - VersionInfoPtr：版本信息 (VersionInfoPtr：Version Information)
     - 
     - 
   * - 返回值： (Return Value:)
     - 无
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 获取Tm模块版本信息 (Get Tm Module Version Information)
     - 
     - 




Tm_ResetTimer1us16bit函数定义 (The_tm_ResetTimer1us16bit_function_definition)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称: (Function Name:)
     - Tm_ResetTimer1us16bit
     - 
     - 
   * - 函数原型: (Function prototype:)
     - FUNC(Std_ReturnType,Tm_CODE)
     - 
     - 
   * - 
     - Tm_ResetTimer1us16bit(Tm_PredefTimer1us16bitType\*TimerPtr )
     - 
     - 
   * - 服务编号: (Service Number:)
     - 0x2
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 仅在不同时钟实例下可重入 (Only reentrant when not in simultaneous clock instances)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - 无
     - 值域： (Domain:)
     - 无
   * - 输入输出参数: (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - TimerPtr：时钟实例 (TimerPtr：Clock Instance)
     - 
     - 
   * - 返回值： (Return Value:)
     - Std_ReturnType：E_OK:GPT驱动成功，无开发错误。 (Std_ReturnType：E_OK:GPT driver succeeded, no development errors.)
     - 
     - 
   * - 
     - E_NOT_OK:GPT驱动失败，或有开发错误。 (E_NOT_OK: GPT Driver Failure, or Developer Error.)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 重置时钟。 (Reset clock.)
     - 
     - 




Tm_GetTimeSpan1us16bit函数定义 (The definition of Tm_GetTimeSpan1us16bit function)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称: (Function Name:)
     - Tm_GetTimeSpan1us16bit
     - 
     - 
   * - 函数原型: (Function prototype:)
     - FUNC(Std_ReturnType,Tm_CODE)
     - 
     - 
   * - 
     - Tm_GetTimeSpan1us16bit( constTm_PredefTimer1us16bitType\*TimerPtr,uint16\*TimeSpanPtr )
     - 
     - 
   * - 服务编号: (Service Number:)
     - 0x3
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 是 (Is)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - TimerPtr：时钟实例 (TimerPtr：Clock Instance)
     - 值域： (Domain:)
     - 无
   * - 输入输出参数: (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - TimeSpanPtr：时段 (TimeSpanPtr：Duration)
     - 
     - 
   * - 返回值： (Return Value:)
     - Std_ReturnType：E_OK:GPT驱动成功，无开发错误。 (Std_ReturnType：E_OK:GPT driver succeeded, no development errors.)
     - 
     - 
   * - 
     - E_NOT_OK:GPT驱动失败，或有开发错误。 (E_NOT_OK: GPT Driver Failure, or Developer Error.)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 获取时段。 (Get the time slot.)
     - 
     - 




Tm_ShiftTimer1us16bit函数定义 (Tm_ShiftTimer1us16bit function definition)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称: (Function Name:)
     - Tm_ShiftTimer1us16bit
     - 
     - 
   * - 函数原型: (Function prototype:)
     - FUNC(void,Tm_CODE)
     - 
     - 
   * - 
     - Tm_ShiftTimer1us16bit(Tm_PredefTimer1us16bitType\*TimerPtr, uint16TimeValue )
     - 
     - 
   * - 服务编号: (Service Number:)
     - 0x4
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 仅在不同时钟实例时是 (Only applicable when not simultaneously clock instances.)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - TimerValue：要平移的参考时间 (TimerValue：Time to translateoreferring to the reference time for translation)
     - 值域： (Domain:)
     - 0-0xFFFF
   * - 输入输出参数: (Input Output Parameters:)
     - TimerPtr：时钟实例 (TimerPtr：Clock Instance)
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无
     - 
     - 
   * - 返回值： (Return Value:)
     - 无
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 平移时间。 (Shift time.)
     - 
     - 




Tm_SyncTimer1us16bit函数定义 (The definition of Tm_SyncTimer1us16bit function)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称: (Function Name:)
     - Tm_SyncTimer1us16bit
     - 
     - 
   * - 函数原型: (Function prototype:)
     - FUNC(void,Tm_CODE)
     - 
     - 
   * - 
     - Tm_SyncTimer1us16bit(Tm_PredefTimer1us16bitType\*TimerDstPtr,constTm_PredefTimer1us16bitType\*TimerSrcPtr )
     - 
     - 
   * - 服务编号: (Service Number:)
     - 0x5
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 仅在不同目标时钟实例时是 (Only when different target clock instances.)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - TimerSrcPtr：原时钟 (TimerSrcPtr：original clock)
     - 值域： (Domain:)
     - 无
   * - 输入输出参数: (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - TimerDstPtr：目标时钟 (TimerDstPtr：Target Clock)
     - 
     - 
   * - 返回值： (Return Value:)
     - 无
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 同步时间。 (Synchronize time.)
     - 
     - 




Tm_BusyWait1us16bit函数定义 (Tm_BusyWait1us16bit function definition)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称: (Function Name:)
     - Tm_BusyWait1us16bit
     - 
     - 
   * - 函数原型: (Function prototype:)
     - FUNC(Std_ReturnType,Tm_CODE)
     - 
     - 
   * - 
     - Std_ReturnTypeTm_BusyWait1us16bit( uint8WaitingTimeMin )
     - 
     - 
   * - 服务编号: (Service Number:)
     - 0x6
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 是 (Is)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - WaitingTimeMin：最少等待时间（单位为微秒） (WaitingTimeMin：Minimum waiting time（unit in microseconds）)
     - 值域： (Domain:)
     - 0-256
   * - 输入输出参数: (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无
     - 
     - 
   * - 返回值： (Return Value:)
     - Std_ReturnType：E_OK:GPT驱动成功，无开发错误。 (Std_ReturnType：E_OK:GPT driver succeeded, no development errors.)
     - 
     - 
   * - 
     - E_NOT_OK:GPT驱动失败，或有开发错误。 (E_NOT_OK: GPT Driver Failure, or Developer Error.)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 轮询忙碌等待，保证最小等待时间。 (Polling busy wait, guarantee minimal waiting time.)
     - 
     - 




Tm_ResetTimer1us24bit函数定义 (Tm_ResetTimer1us24bit function definition)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称: (Function Name:)
     - Tm_ResetTimer1us24bit
     - 
     - 
   * - 函数原型: (Function prototype:)
     - FUNC(Std_ReturnType,Tm_CODE)
     - 
     - 
   * - 
     - Tm_ResetTimer1us24bit(Tm_PredefTimer1us24bitType\*TimerPtr )
     - 
     - 
   * - 服务编号: (Service Number:)
     - 0x7
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 仅在不同时钟实例下可重入 (Only reentrant when not in simultaneous clock instances)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - 无
     - 值域： (Domain:)
     - 无
   * - 输入输出参数: (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - TimerPtr：时钟实例 (TimerPtr：Clock Instance)
     - 
     - 
   * - 返回值： (Return Value:)
     - Std_ReturnType：E_OK:GPT驱动成功，无开发错误。 (Std_ReturnType：E_OK:GPT driver succeeded, no development errors.)
     - 
     - 
   * - 
     - E_NOT_OK:GPT驱动失败，或有开发错误。 (E_NOT_OK: GPT Driver Failure, or Developer Error.)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 重置时钟。 (Reset clock.)
     - 
     - 




Tm_GetTimeSpan1us24bit函数定义 (The definition of Tm_GetTimeSpan1us24bit function)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称: (Function Name:)
     - Tm\_GetTimeSpan1us24bit
     - 
     - 
   * - 函数原型: (Function prototype:)
     - FUNC(Std_ReturnType,Tm_CODE)
     - 
     - 
   * - 
     - Tm_GetTimeSpan1us24bit( constTm_PredefTimer1us24bitType\*TimerPtr,uint32\*TimeSpanPtr )
     - 
     - 
   * - 服务编号: (Service Number:)
     - 0x8
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 是 (Is)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - TimerPtr：时钟实例 (TimerPtr：Clock Instance)
     - 值域： (Domain:)
     - 无
   * - 输入输出参数: (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - TimeSpanPtr：时段 (TimeSpanPtr：Duration)
     - 
     - 
   * - 返回值： (Return Value:)
     - Std_ReturnType：E_OK:GPT驱动成功，无开发错误。 (Std_ReturnType：E_OK:GPT driver succeeded, no development errors.)
     - 
     - 
   * - 
     - E_NOT_OK:GPT驱动失败，或有开发错误。 (E_NOT_OK: GPT Driver Failure, or Developer Error.)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 获取时段。 (Get the time slot.)
     - 
     - 




Tm_ShiftTimer1us24bit函数定义 (Tm_ShiftTimer1us24bit function definition)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称: (Function Name:)
     - Tm_ShiftTimer1us24bit
     - 
     - 
   * - 函数原型: (Function prototype:)
     - FUNC(void,Tm_CODE)
     - 
     - 
   * - 
     - Tm_ShiftTimer1us24bit(Tm_PredefTimer1us24bitType\*TimerPtr, uint32TimeValue )
     - 
     - 
   * - 服务编号: (Service Number:)
     - 0x9
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 仅在不同时钟实例时是 (Only applicable when not simultaneously clock instances.)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - TimerValue：要平移的参考时间 (TimerValue：Time to translateoreferring to the reference time for translation)
     - 值域： (Domain:)
     - 0-0xFFFFFF
   * - 输入输出参数: (Input Output Parameters:)
     - TimerPtr：时钟实例 (TimerPtr：Clock Instance)
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无
     - 
     - 
   * - 返回值： (Return Value:)
     - 无
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 平移时间。 (Shift time.)
     - 
     - 




Tm_SyncTimer1us24bit函数定义 (Tm_SyncTimer1us24bit function definition)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称: (Function Name:)
     - Tm_SyncTimer1us24bit
     - 
     - 
   * - 函数原型: (Function prototype:)
     - FUNC(void,Tm_CODE)
     - 
     - 
   * - 
     - Tm_SyncTimer1us24bit(Tm_PredefTimer1us24bitType\*TimerDstPtr,constTm_PredefTimer1us24bitType\*TimerSrcPtr )
     - 
     - 
   * - 服务编号: (Service Number:)
     - 0xa
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 仅在不同目标时钟实例时是 (Only when different target clock instances.)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - TimerSrcPtr：原时钟 (TimerSrcPtr：original clock)
     - 值域： (Domain:)
     - 无
   * - 输入输出参数: (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - TimerDstPtr：目标时钟 (TimerDstPtr：Target Clock)
     - 
     - 
   * - 返回值： (Return Value:)
     - 无
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 同步时间。 (Synchronize time.)
     - 
     - 




Tm_BusyWait1us24bit函数定义 (The definition of Tm_BusyWait1us24bit function)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称: (Function Name:)
     - Tm_BusyWait1us24bit
     - 
     - 
   * - 函数原型: (Function prototype:)
     - FUNC(Std_ReturnType,Tm_CODE)
     - 
     - 
   * - 
     - Std_ReturnTypeTm_BusyWait1us24bit( uint8WaitingTimeMin )
     - 
     - 
   * - 服务编号: (Service Number:)
     - 0xb
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 是 (Is)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - WaitingTimeMin：最少等待时间（单位为微秒） (WaitingTimeMin：Minimum waiting time（unit in microseconds）)
     - 值域： (Domain:)
     - 0-256
   * - 输入输出参数: (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无
     - 
     - 
   * - 返回值： (Return Value:)
     - Std_ReturnType：E_OK:GPT驱动成功，无开发错误。 (Std_ReturnType：E_OK:GPT driver succeeded, no development errors.)
     - 
     - 
   * - 
     - E_NOT_OK:GPT驱动失败，或有开发错误。 (E_NOT_OK: GPT Driver Failure, or Developer Error.)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 轮询忙碌等待，保证最小等待时间。 (Polling busy wait, guarantee minimal waiting time.)
     - 
     - 




Tm_ResetTimer1us32bit函数定义 (The function definition for Tm_ResetTimer1us32bit is)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称: (Function Name:)
     - Tm_ResetTimer1us32bit
     - 
     - 
   * - 函数原型: (Function prototype:)
     - FUNC(Std_ReturnType,Tm_CODE)
     - 
     - 
   * - 
     - Tm_ResetTimer1us32bit(Tm_PredefTimer1us32bitType\*TimerPtr )
     - 
     - 
   * - 服务编号: (Service Number:)
     - 0xc
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 仅在不同时钟实例下可重入 (Only reentrant when not in simultaneous clock instances)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - 无
     - 值域： (Domain:)
     - 无
   * - 输入输出参数: (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - TimerPtr：时钟实例 (TimerPtr：Clock Instance)
     - 
     - 
   * - 返回值： (Return Value:)
     - Std_ReturnType：E_OK:GPT驱动成功，无开发错误。 (Std_ReturnType：E_OK:GPT driver succeeded, no development errors.)
     - 
     - 
   * - 
     - E_NOT_OK:GPT驱动失败，或有开发错误。 (E_NOT_OK: GPT Driver Failure, or Developer Error.)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 重置时钟。 (Reset clock.)
     - 
     - 




Tm_GetTimeSpan1us32bit函数定义 (The definition of Tm_GetTimeSpan1us32bit function)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称: (Function Name:)
     - Tm\_GetTimeSpan1us32bit
     - 
     - 
   * - 函数原型: (Function prototype:)
     - FUNC(Std_ReturnType,Tm_CODE)
     - 
     - 
   * - 
     - Tm_GetTimeSpan1us32bit( constTm_PredefTimer1us32bitType\*TimerPtr,uint32\*TimeSpanPtr )
     - 
     - 
   * - 服务编号: (Service Number:)
     - 0xd
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 是 (Is)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - TimerPtr：时钟实例 (TimerPtr：Clock Instance)
     - 值域： (Domain:)
     - 无
   * - 输入输出参数: (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - TimeSpanPtr：时段 (TimeSpanPtr：Duration)
     - 
     - 
   * - 返回值： (Return Value:)
     - Std_ReturnType：E_OK:GPT驱动成功，无开发错误。 (Std_ReturnType：E_OK:GPT driver succeeded, no development errors.)
     - 
     - 
   * - 
     - E_NOT_OK:GPT驱动失败，或有开发错误。 (E_NOT_OK: GPT Driver Failure, or Developer Error.)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 获取时段。 (Get the time slot.)
     - 
     - 




Tm_ShiftTimer1us32bit函数定义 (Function definition for Tm_ShiftTimer1us32bit)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称: (Function Name:)
     - Tm_ShiftTimer1us32bit
     - 
     - 
   * - 函数原型: (Function prototype:)
     - FUNC(void,Tm_CODE)
     - 
     - 
   * - 
     - Tm_ShiftTimer1us32bit(Tm_PredefTimer1us32bitType\*TimerPtr, uint32TimeValue )
     - 
     - 
   * - 服务编号: (Service Number:)
     - 0xe
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 仅在不同时钟实例时是 (Only applicable when not simultaneously clock instances.)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - TimerValue：要平移的参考时间 (TimerValue：Time to translateoreferring to the reference time for translation)
     - 值域： (Domain:)
     - 0-0xFFFFFFFF
   * - 输入输出参数: (Input Output Parameters:)
     - TimerPtr：时钟实例 (TimerPtr：Clock Instance)
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无
     - 
     - 
   * - 返回值： (Return Value:)
     - 无
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 平移时间。 (Shift time.)
     - 
     - 




Tm_SyncTimer1us32bit函数定义 (The definition of Tm_SyncTimer1us32bit function)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称: (Function Name:)
     - Tm_SyncTimer1us32bit
     - 
     - 
   * - 函数原型: (Function prototype:)
     - FUNC(void,Tm_CODE)
     - 
     - 
   * - 
     - Tm_SyncTimer1us32bit(Tm_PredefTimer1us32bitType\*TimerDstPtr,constTm_PredefTimer1us32bitType\*TimerSrcPtr )
     - 
     - 
   * - 服务编号: (Service Number:)
     - 0xf
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 仅在不同目标时钟实例时是 (Only when different target clock instances.)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - TimerSrcPtr：原时钟 (TimerSrcPtr：original clock)
     - 值域： (Domain:)
     - 无
   * - 输入输出参数: (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - TimerDstPtr：目标时钟 (TimerDstPtr：Target Clock)
     - 
     - 
   * - 返回值： (Return Value:)
     - 无
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 同步时间。 (Synchronize time.)
     - 
     - 




Tm_BusyWait1us32bit函数定义 (Tm_BusyWait1us32bit function definition)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称: (Function Name:)
     - Tm_BusyWait1us32bit
     - 
     - 
   * - 函数原型: (Function prototype:)
     - FUNC(Std_ReturnType,Tm_CODE)
     - 
     - 
   * - 
     - Std_ReturnTypeTm_BusyWait1us32bit( uint8WaitingTimeMin )
     - 
     - 
   * - 服务编号: (Service Number:)
     - 0x10
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 是 (Is)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - WaitingTimeMin：最少等待时间（单位为微秒） (WaitingTimeMin：Minimum waiting time（unit in microseconds）)
     - 值域： (Domain:)
     - 0-256
   * - 输入输出参数: (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无
     - 
     - 
   * - 返回值： (Return Value:)
     - Std_ReturnType：E_OK:GPT驱动成功，无开发错误。 (Std_ReturnType：E_OK:GPT driver succeeded, no development errors.)
     - 
     - 
   * - 
     - E_NOT_OK:GPT驱动失败，或有开发错误。 (E_NOT_OK: GPT Driver Failure, or Developer Error.)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 轮询忙碌等待，保证最小等待时间。 (Polling busy wait, guarantee minimal waiting time.)
     - 
     - 




Tm_ResetTimer100us32bit函数定义 (Tm_ResetTimer100us32bit function definition)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称: (Function Name:)
     - Tm_ResetTimer100us32bit
     - 
     - 
   * - 函数原型: (Function prototype:)
     - FUNC(Std_ReturnType,Tm_CODE)
     - 
     - 
   * - 
     - Tm_ResetTimer100us32bit(Tm_PredefTimer100us32bitType\*TimerPtr )
     - 
     - 
   * - 服务编号: (Service Number:)
     - 0x11
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 仅在不同时钟实例下可重入 (Only reentrant when not in simultaneous clock instances)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - 无
     - 值域： (Domain:)
     - 无
   * - 输入输出参数: (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - TimerPtr：时钟实例 (TimerPtr：Clock Instance)
     - 
     - 
   * - 返回值： (Return Value:)
     - Std_ReturnType：E_OK:GPT驱动成功，无开发错误。 (Std_ReturnType：E_OK:GPT driver succeeded, no development errors.)
     - 
     - 
   * - 
     - E_NOT_OK:GPT驱动失败，或有开发错误。 (E_NOT_OK: GPT Driver Failure, or Developer Error.)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 重置时钟。 (Reset clock.)
     - 
     - 




Tm_GetTimeSpan100us32bit函数定义 (The definition of Tm_GetTimeSpan100us32bit function)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称: (Function Name:)
     - Tm\_GetTimeSpan100us32bit
     - 
     - 
   * - 函数原型: (Function prototype:)
     - FUNC(Std_ReturnType,Tm_CODE)
     - 
     - 
   * - 
     - Tm_GetTimeSpan100us32bit( constTm_PredefTimer100us32bitType\*TimerPtr,uint32\*TimeSpanPtr )
     - 
     - 
   * - 服务编号: (Service Number:)
     - 0x12
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 是 (Is)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - TimerPtr：时钟实例 (TimerPtr：Clock Instance)
     - 值域： (Domain:)
     - 无
   * - 输入输出参数: (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - TimeSpanPtr：时段 (TimeSpanPtr：Duration)
     - 
     - 
   * - 返回值： (Return Value:)
     - Std_ReturnType：E_OK:GPT驱动成功，无开发错误。 (Std_ReturnType：E_OK:GPT driver succeeded, no development errors.)
     - 
     - 
   * - 
     - E_NOT_OK:GPT驱动失败，或有开发错误。 (E_NOT_OK: GPT Driver Failure, or Developer Error.)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 获取时段。 (Get the time slot.)
     - 
     - 




Tm_ShiftTimer100us32bit函数定义 (Tm_ShiftTimer100us32bit function definition)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称: (Function Name:)
     - Tm_ShiftTimer100us32bit
     - 
     - 
   * - 函数原型: (Function prototype:)
     - FUNC(void,Tm_CODE)
     - 
     - 
   * - 
     - Tm_ShiftTimer100us32bit(Tm_PredefTimer100us32bitType\*TimerPtr, uint32TimeValue )
     - 
     - 
   * - 服务编号: (Service Number:)
     - 0x13
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 仅在不同时钟实例时是 (Only applicable when not simultaneously clock instances.)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - TimerValue：要平移的参考时间 (TimerValue：Time to translateoreferring to the reference time for translation)
     - 值域： (Domain:)
     - 0-0xFFFFFFFF
   * - 输入输出参数: (Input Output Parameters:)
     - TimerPtr：时钟实例 (TimerPtr：Clock Instance)
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无
     - 
     - 
   * - 返回值： (Return Value:)
     - 无
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 平移时间。 (Shift time.)
     - 
     - 




Tm_SyncTimer100us32bit函数定义 (The definition of Tm_SyncTimer100us32bit function)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称: (Function Name:)
     - Tm_SyncTimer100us32bit
     - 
     - 
   * - 函数原型: (Function prototype:)
     - FUNC(void,Tm_CODE)
     - 
     - 
   * - 
     - Tm_SyncTimer100us32bit(Tm_PredefTimer100us32bitType\*TimerDstPtr,constTm_PredefTimer100us32bitType\*TimerSrcPtr )
     - 
     - 
   * - 服务编号: (Service Number:)
     - 0x14
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 仅在不同目标时钟实例时是 (Only when different target clock instances.)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - TimerSrcPtr：原时钟 (TimerSrcPtr：original clock)
     - 值域： (Domain:)
     - 无
   * - 输入输出参数: (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - TimerDstPtr：目标时钟 (TimerDstPtr：Target Clock)
     - 
     - 
   * - 返回值： (Return Value:)
     - 无
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 同步时间。 (Synchronize time.)
     - 
     - 




Tm_GetTimeSpan1ms32bit函数定义 (The definition of Tm_GetTimeSpan1ms32bit function)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称: (Function Name:)
     - Tm\_GetTimeSpan1ms32bit
     - 
     - 
   * - 函数原型: (Function prototype:)
     - FUNC(Std_ReturnType,Tm_CODE)
     - 
     - 
   * - 
     - Tm_GetTimeSpan1ms32bit( constTm_PredefTimer100us32bitType\*TimerPtr,uint32\*TimeSpanPtr )
     - 
     - 
   * - 服务编号: (Service Number:)
     - 0x12
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 是 (Is)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - TimerPtr：时钟实例 (TimerPtr：Clock Instance)
     - 值域： (Domain:)
     - 无
   * - 输入输出参数: (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - TimeSpanPtr：时段 (TimeSpanPtr：Duration)
     - 
     - 
   * - 返回值： (Return Value:)
     - Std_ReturnType：E_OK:GPT驱动成功，无开发错误。 (Std_ReturnType：E_OK:GPT driver succeeded, no development errors.)
     - 
     - 
   * - 
     - E_NOT_OK:GPT驱动失败，或有开发错误。 (E_NOT_OK: GPT Driver Failure, or Developer Error.)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 获取时段。 (Get the time slot.)
     - 
     - 




可配置函数定义 (Configurable Function Definition)
----------------------------------------------------------

无。

None.

配置 (Configure)
==============================

配置列表 (Configuration List)
----------------------------------------------------------

.. centered:: **表 属性描述 (Table Properties Description)**

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - UI名称 (UI Name)
     - 该配置项在配置工具界面显示的名称 (The name of this configuration item as displayed in the configuration tool interface)
   * - 取值范围 (Range)
     - 该配置项允许的取值区间 (The configurable item allows value ranges.)
   * - 默认取值 (Default value)
     - 该配置项默认的配置值 (The default configuration value for this option)
   * - 参数描述 (Parameter Description)
     - 该配置项在标准的AUTOSAR_EcucParamDef.arxml文件中的描述 (This configuration item's description in the standard AUTOSAR_EcucParamDef.arxml file.)
   * - 依赖关系 (Dependencies)
     - 该配置项与其他模块或配置项的关系 (The configuration item's relationship with other modules or configuration items)




TmGeneral
-------------------------

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/Tm/image3.png
   :alt: TmGeneral工具配置 (TmGeneral Tool Configuration)
   :name: TmGeneral工具配置 (TmGeneral Tool Configuration)
   :align: center


.. centered:: **表 TmGeneral配置描述 (Table TmGeneral Configuration Description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - TmDevErrorDetect
     - 取值范围 (Range)
     - True/False
     - 默认取值 (Default value)
     - False
   * - 
     - 参数描述 (Parameter Description)
     - 开关开发错误检测和报告。 (Enable error detection and reporting for switch development.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - TmEnablePredefTimer100us32bit
     - 取值范围 (Range)
     - True/False
     - 默认取值 (Default value)
     - False
   * - 
     - 参数描述 (Parameter Description)
     - 开关100us32bit时钟相关功能。 (Disable 100us 32-bit Clock Related Function.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - TmEnablePredefTimer1us16bit
     - 取值范围 (Range)
     - True/False
     - 默认取值 (Default value)
     - False
   * - 
     - 参数描述 (Parameter Description)
     - 开关1us16bit时钟相关功能。 (Disable 1us 16-bit Clock Related Function.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - TmEnablePredefTimer1us24bit
     - 取值范围 (Range)
     - True/False
     - 默认取值 (Default value)
     - False
   * - 
     - 参数描述 (Parameter Description)
     - 开关1us24bit时钟相关功能。 (Enable 1us 24-bit Clock Related Function.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - TmEnablePredefTimer1us32bit
     - 取值范围 (Range)
     - True/False
     - 默认取值 (Default value)
     - False
   * - 
     - 参数描述 (Parameter Description)
     - 开关1us32bit时钟相关功能。 (Enable 1us 32-bit Clock Related Function.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - TmVersionInfoApi
     - 取值范围 (Range)
     - True/False
     - 默认取值 (Default value)
     - False
   * - 
     - 参数描述 (Parameter Description)
     - 开关获取版本信息接口。 (Interface for acquiring version information.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
