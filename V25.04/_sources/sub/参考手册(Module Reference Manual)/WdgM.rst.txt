WdgM
#################################

:strong:`缩写词注解 (Abbreviation Notes):`

.. list-table::
   :widths: 34 33 33
   :header-rows: 1

   * - 缩写词 (Abbreviation)
     - 解释/描述 (Explanation/Description)
     - 中文解释 (Chinese explanation)
   * - API
     - Application ProgrammingInterface
     - 应用编程接口 (Application Programming Interface)
   * - HW
     - Hardware
     - 硬件 (Hardware)
   * - SW
     - Software
     - 软件 (Software)
   * - WDG
     - Watchdog
     - 看门狗 (Watch Dog)
   * - WdgM
     - Watchdog Manager
     - 看门狗管理器看门狗管理器 (Watchdog Manager Watchdog Manager)
   * - WdgIf
     - Watchdog Interface
     - 看门狗接口 (Watchdog Interface)
   * - SE
     - Supervision Entity
     - 监督实体 (Supervised Entity)
   * - CP
     - CheckPoint
     - 监控点 (Monitoring Point)
   * - DEM
     - Diagnostic Event Manager
     - 诊断事件管理器 (Diagnostic Event Manager)
   * - DET
     - Default Error Tracer
     - 开发错误跟踪器 (Develop error tracker)
   * - 
     - 
     - 默认错误跟踪器 (Default Error Tracker)
   * - OS
     - Operating System
     - 操作系统 (Operating System)
   * - BSW
     - Basic Software
     - 基础软件 (Basic software)
   * - MCU
     - Microcontroller Unit
     - 微控制器 (Microcontroller)
   * - MPU
     - Memory Protection Unit
     - 内存保护单元 (Memory Protection Unit)
   * - STM
     - System Timer
     - 系统定时器 (System Timer)
   * - GTM
     - Generic Timer Module
     - 通用定时器模块 (General Timer Module)
   * - MCAL
     - Microcontroller AbstractionLayer
     - 微控制器抽象层 (Microcontroller Abstraction Layer)
   * - MISRA
     - The Motor Industry Software
     - 电机工业软件可靠性协会 (Association for Reliability of Electrical Machinery Software)
   * - 
     - Reliability Association
     - 
   * - TCL
     - Tool Confidence Level
     - 工具置信度等级 (Tool confidence level)
   * - SEooC
     - Safety Element out of Context
     - 无运用场景的安全组件 (Security components without applied scenarios)






简介 (Introduction)
=================================

看门狗硬件实际上是一个特殊的定时器，当定时周期到达时，会发出溢出脉冲，从而引起整个板子的复位。在程序中使用时需要适当的插入一些看门狗定时器复位指令，从而保证程序正常运行时看门狗不溢出。当程序运行出现异常情况时，看门狗会因为长时间未运行复位指令引起定时器超时，从而产生溢出脉冲，通过RESET 引脚对硬件进行复位。

Watchdog hardware is actually a special timer that sends an overflow pulse to reset the entire board when the timing period arrives. In program usage, appropriate watchdog timer reset instructions need to be inserted to ensure that the watchdog does not overflow during normal program execution. When abnormal conditions occur in program

运行出现异常情况时，看门狗会因为长时间未运行复位指令引起定时器超时，从而产生溢出脉冲，通过RESET 引脚对硬件进行复位。

Watchdog will generate an overflow pulse due to the timeout of the timer caused by the long absence of reset instructions when abnormal conditions occur in program execution, thereby resetting the hardware through the RESET pin.

WDG协议栈是 AUTOSAR 标准里的基本基础软件之一。其原理是 WDG 运行期间如果不定时喂狗，WDG 就会使系统复位，这就保证整个系统良好运行，不会出现死循环、死锁或者某个程序一直占用资源不释放的情况。WDG 可提供给用户自己设置的在不喂狗的情况下最大的不复位时间，可设置多种模式，如果硬件支持，可设置进入睡眠模式。

The WDG protocol stack is one of the basic software components in the AUTOSAR standard. Its principle is that if the WDG is not fed during its operation, it will reset the system, ensuring the entire system runs well without getting stuck in an infinite loop, deadlocks, or programs holding onto resources indefinitely. Users can set the maximum time before a reset occurs when not feeding the WDG, with multiple modes available to set. If hardware supports it, sleep mode can be configured.

WdgM是AUTOSAR的一个基础软件模块，WdgM能够监督程序的执行并触发硬件看门狗。ORIENTAIS WDG使用静态配置和动态管理将其功能集成到相关对象中。对象之间的相互调用是通过相关接口实现的。ORIENTAIS WDG设计目标是为了设计一个安全的看门狗管理和实体监督协议栈，遵循ISO26262:2018功能安全所约束条件，目前ORIENTAIS WDG现已通过 TÜV Rheinland的ISO 26262 ASIL D的产品认证。ORIENTAIS WDG的架构如下图所示，其中WdgM位于系统服务层。

WdgM is a basic software module in AUTOSAR, capable of supervising the execution of programs and triggering hardware watchdogs. ORIENTAIS WDG integrates its functionalities into relevant objects through static configuration and dynamic management. Inter-object calls are realized via related interfaces. The design goal of ORIENTAIS WDG is to develop a secure watchdog management and entity supervision protocol stack, adhering to the conditions set by ISO26262:2018 functional safety. Currently, ORIENTAIS WDG has been certified for ISO 26262 ASIL D products by TÜV Rheinland. The architecture of ORIENTAIS WDG is shown in the following figure, with WdgM located in the system service layer.

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/WdgM/image1.png
   :alt: 1‑1 ORIENTAIS WDG架构框图(ORIENTAIS WDG Architecture Diagram)
   :name: 1‑1 ORIENTAIS WDG架构框图(ORIENTAIS WDG Architecture Diagram)
   :align: center

参考资料 (Reference materials)
------------------------------------------

[1] AUTOSAR_SWS_WatchdogManager.pdf, R19-11

[2] AUTOSAR_SWS_WatchdogInterface.pdf, R19-11

[3] AUTOSAR_SWS_WatchdogDriver.pdf, R19-11

[4] AUTOSAR_SWS_DiagnosticEventManager.pdf, R19-11

[5] AUTOSAR_SWS_DefaultErrorTracer.pdf, R19-11

功能描述 (Function Description)
===========================================

WdgM功能 (WdgM Function)
--------------------------------------

WdgM功能介绍 (WdgM Feature Introduction)
====================================================

WdgM模块为Watchdog看门狗协议栈的顶层，为用户提供API应用的接口。WdgM通过WdgIf来改变看门狗的模式，并用于向Wdg Driver报告触发硬件看门狗的条件。Watchdog结构层次如下图所示。

The WdgM module is the top layer of the Watchdog watchdog protocol stack, providing API application interfaces to users. WdgM uses WdgIf to change the watchdog mode and reports conditions that trigger the hardware watchdog to the Wdg Driver. The structure hierarchy of the Watchdog is shown in the following diagram.

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/WdgM/image2.png
   :alt: Watchdog层次结构图 (Watchdog Hierarchy Diagram)
   :name: Watchdog层次结构图 (Watchdog Hierarchy Diagram)
   :align: center


.. centered:: **表 Watchdog层次结构说明 (Table Watchdog Hierarchy Description)**

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 层次 (Levels)
     - 作用 (Function)
   * - WdgM
     - WdgM模块为Watchdog的顶层，为用户提供API应用的接口 (The WdgM module is the top layer of Watchdog, providing users with API application interfaces.)
   * - WdgIf
     - WdgM管理多个Watchdog Driver的中间抽象层。 (WdgM is an intermediate abstraction layer for managing multiple Watchdog Driver instances.)
   * - Wdg
     - Watchdog的底层硬件驱动 (The underlying hardware driver of Watchdog)




WdgM可配置多种运行Mode模式，每个Mode包含数个Supervision Entity (SE)，每个SE包含多个Checkpoint (CP)。根据对CP之间的时间差、CP执行顺序的关注，分为Alive Supervision，Deadline Supervision，Logical Supervision。 Logical Supervision 可以再细分为Internal Logical Supervision和External Logical Supervision。Internal Logical Supervision即所有涉及的CP，均在同SE；External Logical Supervision，即所有CP至少存在于两个不同的SE。WdgM引入Local Status和Global Status两种状态，其中Local Status和所属SE的各种监督结果相关，而Global Status则和当前模式下所有活动的Local Status相关。WdgM通过监督算法对状态计算决定是否要触发硬件看门狗。

WdgM can configure multiple运行Mode modes, each mode containing several Supervision Entity (SE), and each SE containing multiple Checkpoint (CP). According to the attention on the time difference between CPs or the order of CP execution, it is divided into Alive Supervision, Deadline Supervision, and Logical Supervision. Logical Supervision can further be细分为Internal Logical Supervision and External Logical Supervision. Internal Logical Supervision refers to all involved CPs being within the same SE; External Logical Supervision means that all CPs exist in at least two different SEs. WdgM introduces two states: Local Status and Global Status, where Local Status is related to various supervision results of the corresponding SE, while Global Status relates to all active Local Status under the current mode. WdgM decides whether to trigger the hardware watchdog through a supervision algorithm for state computation.

监督算法 (Supervise algorithms)
===========================================

监督模块实现了看门狗WDG的监控功能，也是WDG的主要功能。

The supervision module implements the watchdog WDG's monitoring function and is also the main function of WDG.

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/WdgM/image3.png
   :alt: 看门狗监督示意图 (Watchdog Supervision Diagram)
   :name: 看门狗监督示意图 (Watchdog Supervision Diagram)
   :align: center


看门狗WDG在用户选择的特定模式下工作，每种模式有多个监督实体组成，相应的全局监督状态也是由每个监督实体的局部监督状态计算出来的。每一个监督实体都包括几个活动监督（Alive Supervision）、期限监督（Deadline Supervision）和逻辑监督（Logical Supervision）。该监督实体的相应局部监督状态也从相应的活动监督、期限监督和逻辑监督的所有结果中计算出来。

The Watchdog WDG works in a specific mode chosen by the user, where multiple supervisory entities form each mode. The corresponding global supervisory state is computed from the local supervisory states of each supervisory entity. Each supervisory entity includes several active supervision (Alive Supervision), deadline supervision (Deadline Supervision), and logical supervision (Logical Supervision). The local supervisory state of the supervisory entity is computed from all results of the respective active supervision, deadline supervision, and logical supervision.

用户可以通过ORIENTAIS配置工具设置不同的模式，其中包含不同的监督机制和检查点，以适应不同的环境。这个模块用于在不同模式之间切换。

Users can configure different modes using the ORIENTAIS configuration tool, which includes various supervision mechanisms and checkpoints to adapt to different environments. This module is used for switching between different modes.

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/WdgM/image4.png
   :alt: 基本原则和算法示意图 (Basic principles and algorithm schematic diagram)
   :name: 基本原则和算法示意图 (Basic principles and algorithm schematic diagram)
   :align: center


模式切换改变被监督实体的监督参数。当模式发生变化时，被监督实体的监督参数的变化遵循以下规则：

Switching modes alters the supervision parameters of the supervised entity. When the mode changes, the changes in the supervision parameters of the supervised entity follow these rules:

- 如果当前的全局监督状态是WDGM_GLOBAL_STATUS_OK或WDGM_GLOBAL_STATUS_FAILED，那么每个监督实体激活新模式（作为参数传递给函数WdgM_SetMode），函数WdgM_ChangeSEStatus应当保留SE的当前状态，以及该监督实体（SE）中活动监督、期限监督和内部逻辑监督的状态。

If the current global supervision status is WDGM_GLOBAL_STATUS_OK or WDGM_GLOBAL_STATUS_FAILED, then for each supervisory entity (activated in a new mode passed as a parameter to the WdgM_SetMode function), the WdgM_ChangeSEStatus function should retain the SE's current state as well as the states of active supervision, term supervision, and internal logic supervision within that supervisory entity (SE).

- 如果当前的全局监督状态是WDGM_GLOBAL_STATUS_OK或WDGM_GLOBAL_STATUS_FAILED，则对于在新模式下停用的每个监督实体（传递给函数WdgM_SetMode作为参数），函数WdgM_SetMode将监督实体的状态更改为WDGM_GLOBAL_STATUS_DEACTIVATED；确定活动监督、期限监督和逻辑监督的结果予以纠正；还应将其失败的引用循环计数器清除为0；将其所有的活动监督、期限监督和逻辑监督的状态设置为默认值。

If the current global supervision status is WDGM_GLOBAL_STATUS_OK or WDGM_GLOBAL_STATUS_FAILED, for each supervision entity disabled in the new mode (passed as a parameter to the WdgM_SetMode function), the WdgM_SetMode function will change the state of the supervision entity to WDGM_GLOBAL_STATUS_DEACTIVATED; ensure that the results of active supervision, term supervision, and logical supervision are corrected; also clear its failed reference cycle counter to 0; set the states of all active supervision, term supervision, and logical supervision to default values.

- 如果当前的全局监督状态不是WDGM_GLOBAL_STATUS_OK或WDGM_GLOBAL_STATUS_FAILED，则WdgM_SetMode函数将返回而不做任何操作。

If the current global supervision status is not WDGM_GLOBAL_STATUS_OK or WDGM_GLOBAL_STATUS_FAILED, the WdgM_SetMode function will return without performing any operations.

模式切换也会改变看门狗触发的参数。当模式改变时，看门狗触发参数的变化遵循以下规则：

Switching modes also changes the parameters that trigger the watchdog. When the mode changes, the watchdog trigger parameters follow the following rules:

- 如果调用函数WdgM_SetMode，看门狗管理器模块将通过调用WdgIf_SetMode服务将配置的看门狗模式（mode）参数应用到每一个看门狗设备。

If the function WdgM_SetMode is called, the watchdog manager module will apply the configured watchdog mode parameter to each watchdog device by calling the WdgIf_SetMode service.

- 对于每个看门狗实例，看门狗模式应该静态配置并由参数WdgMWatchdogMode表示。

For each watchdog instance, the watchdog mode should be statically configured and represented by the parameter WdgMWatchdogMode.

源文件描述 (Source file description)
===============================================

.. centered:: **表 WdgM组件文件描述 (Table WdgM Component File Description)**

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 文件 (Files)
     - 说明 (Description)
   * - WdgM.c
     - WdgM源文件 (Source file)
   * - WdgM.h
     - WdgM头文件 (WdgM Header File)
   * - WdgM_CfgType.h
     - WdgM配置类型头文件 (WDGM Configuration Type Header File)
   * - WdgM.MemMep.h
     - WdgM的内存映射定义 (The memory mapping definition of WdgM)
   * - WdgM_Type.h
     - WdgM的数据类型定义 (Definition of data types for WdgM.)




.. figure:: ../../_static/参考手册(Module_Reference_Manual)/WdgM/image5.png
   :alt: WdgM组件文件交互关系图 (Component File Interactions Diagram for WdgM Module)
   :name: WdgM组件文件交互关系图 (Component File Interactions Diagram for WdgM Module)
   :align: center

API接口 (API Interface)
=====================================

类型定义 (Type definition)
--------------------------------------

WdgM_LocalStatusType类型定义 (WdgM_LocalStatusType Type Definition)
===============================================================================

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 名称 (Name)
     - WdgM_LocalStatusType
   * - 类型 (Type)
     - Enumeration
   * - 范围 (Range)
     - WDGM_LOCAL_STATUS_OK = 0
   * - 
     - WDGM_LOCAL_STATUS_FAILED = 1
   * - 
     - WDGM_LOCAL_STATUS_EXPIRED = 2
   * - 
     - WDGM_LOCAL_STATUS_DEACTIVATED = 3
   * - 描述 (Description)
     - 用于描述WdgM模块内部局部状态的数据类型 (Data types used to describe the internal local state of the WdgM module)




WdgM_GlobalStatusType类型定义 (WdgM_GlobalStatusType Type Definition)
=================================================================================

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 名称 (Name)
     - WdgM_GlobalStatusType
   * - 类型 (Type)
     - Enumeration
   * - 范围 (Range)
     - WDGM_GLOBAL_STATUS_OK = 0
   * - 
     - WDGM_GLOBAL_STATUS_FAILED = 1
   * - 
     - WDGM_GLOBAL_STATUS_EXPIRED = 2
   * - 
     - WDGM_GLOBAL_STATUS_STOPPED = 2
   * - 
     - WDGM_GLOBAL_STATUS_DEACTIVATED = 3
   * - 描述 (Description)
     - 用于描述WdgM模块全局状态的数据类型 (Data type used for describing the global state of the WdgM module)




输入函数描述 (Describe the input function:)
-----------------------------------------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 输入模块 (Input Module)
     - API
   * - Det
     - Det_ReportRuntimeError
   * - Det
     - Det_ReportError
   * - OS
     - GetElapsedValue
   * - WdgIf
     - WdgIf_SetMode
   * - WdgIf
     - WdgIf_SetTriggerCondition
   * - BswM
     - BswM_WdgM_RequestPartitionReset
   * - Dem
     - Dem_SetEventStatus
   * - Mcu
     - Mcu_PerformReset




静态接口函数定义 (Static interface function definition)
---------------------------------------------------------------

WdgM_Init函数定义 (The WdgM_Init function definition)
=================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - WdgM_Init
     - 
     - 
   * - 函数原型： (Function prototype:)
     - void WdgM_Init(const WdgM_ConfigType\*ConfigPtr);
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x00
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 不可重入 (Non-reentrant)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - ConfigPtr：传入配置生成的WdgM_Config指针 (ConfigPtr：Pointer to WdgM_Config for configuration generation)
     - 值域： (Domain:)
     - 无
   * - 输入输出参数： (Input Output Parameters:)
     - 无
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
     - 完成对WdgM模块的初始化处理 (Complete initialization handling for WdgM module)
     - 
     - 




WdgM_DeInit函数定义 (WDGM_DeInit function definition)
=================================================================

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - WdgM_DeInit
   * - 函数原型： (Function prototype:)
     - void WdgM_DeInit(void);
   * - 服务编号： (Service Number:)
     - 0x01
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
   * - 是否可重入： (Is Reentrant:)
     - 不可重入 (Non-reentrant)
   * - 输入参数： (Input parameters:)
     - 无
   * - 输入输出参数： (Input Output Parameters:)
     - 无
   * - 输出参数： (Output Parameters:)
     - 无
   * - 返回值： (Return Value:)
     - 无
   * - 功能概述： (Function Overview:)
     - 完成对WdgM模块的反初始化处理 (Complete the反初始化processing for WdgM module)




WdgM_GetVersionInfo函数定义 (The function definition for WdgM_GetVersionInfo)
=========================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - WdgM_GetVersionInfo
     - 
     - 
   * - 函数原型： (Function prototype:)
     - voidWdgM_GetVersionInfo(Std_VersionInfoType\*versioninfo);
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x02
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 不可重入 (Non-reentrant)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - 无
     - 
     - 
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - Versioninfo：保存版本信息的结构体地址 (Versioninfo：The address of the structure for saving version information.)
     - 值域： (Domain:)
     - 无
   * - 返回值： (Return Value:)
     - 无
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 获取WdgM模块版本信息。需宏开启该功能 (Get version information of WdgM module. Requires macro enable this feature.)
     - 
     - 




WdgM_SetMode函数定义 (WdgM_SetMode function definition)
===================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - WdgM_SetMode
     - 
     - 
   * - 函数原型： (Function prototype:)
     - Std_ReturnTypeWdgM_SetMode(WdgM_ModeType Mode);
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x03
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 不可重入 (Non-reentrant)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - Mode：运行模式 (Mode：Run Mode)
     - 值域： (Domain:)
     - 0-255
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无
     - 
     - 
   * - 返回值： (Return Value:)
     - E_OK：API接口请求被接受 (E_OK: The API interface request has been accepted)
     - 
     - 
   * - 
     - E_NOT_OK：API接口请求被拒绝 (E_NOT_OK: The API interface request was rejected.)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 切换Watchdog的工作模式 (Switch Watchdog's operating mode)
     - 
     - 




WdgM_GetMode函数定义 (The WdgM_GetMode function definition)
=======================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - WdgM_GetMode
     - 
     - 
   * - 函数原型： (Function prototype:)
     - Std_ReturnTypeWdgM_GetMode(WdgM_ModeType \*Mode);
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x0B
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 不可重入 (Non-reentrant)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - 无
     - 
     - 
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - Mode：指向当前Mode编号的指针 (Pointer to the current Mode number)
     - 值域： (Domain:)
     - 无
   * - 返回值： (Return Value:)
     - E_OK：返回当前Mode编号成功 (E_OK: Successfully returned current Mode number)
     - 
     - 
   * - 
     - E_NOT_OK：返回当前Mode编号失败 (E_NOT_OK: Return current Mode number failure)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 获取当前被激活的Mode编号 (Get the number of the currently activated Mode)
     - 
     - 




WdgM_CheckpointReached函数定义 (The WdgM_CheckpointReached function definition)
===========================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - WdgM_CheckpointReached
     - 
     - 
   * - 函数原型： (Function prototype:)
     - Std_ReturnType WdgM_CheckpointReached
     - 
     - 
   * - 
     - (
     - 
     - 
   * - 
     - WdgM_SupervisedEntityIdType SEID,
     - 
     - 
   * - 
     - WdgM_CheckpointIdType CheckpointID
     - 
     - 
   * - 
     - );
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x0E
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 不可重入 (Non-reentrant)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - SEID：当前程序运行到的SE编号 (SEID: The SE ID of the current program execution)
     - 值域： (Domain:)
     - 0-65535
   * - 
     - CheckpointID：当前程序运行到某SE的CP编号 (CheckpointID：The CP number of the current program execution in a SE)
     - 值域： (Domain:)
     - 0-65535
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无
     - 
     - 
   * - 返回值： (Return Value:)
     - E_OK：API接口请求被接受 (E_OK: The API interface request has been accepted)
     - 
     - 
   * - 
     - E_NOT_OK：API接口请求被拒绝 (E_NOT_OK: The API interface request was rejected.)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 程序运行到某SE对应的Checkpoint (The program runs to the Checkpoint corresponding to certain SE)
     - 
     - 




WdgM_GetLocalStatus函数定义 (The WdgM_GetLocalStatus function definition)
=====================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - WdgM_GetLocalStatus
     - 
     - 
   * - 函数原型： (Function prototype:)
     - Std_ReturnType WdgM_GetLocalStatus
     - 
     - 
   * - 
     - (
     - 
     - 
   * - 
     - WdgM_SupervisedEntityIdType SEID,
     - 
     - 
   * - 
     - WdgM_LocalStatusType \*Status
     - 
     - 
   * - 
     - );
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x0C
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 不可重入 (Non-reentrant)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - SEID：监督实体的标识符ID (SEID: Identifier ID for Supervising Entity)
     - 值域： (Domain:)
     - 0-65535
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - Status：指向SE的LocalStatus的指针 (Status：Pointer to LocalStatus pointing to SE)
     - 值域： (Domain:)
     - 无
   * - 返回值： (Return Value:)
     - E_OK：API接口请求被接受 (E_OK: The API interface request has been accepted)
     - 
     - 
   * - 
     - E_NOT_OK：API接口请求被拒绝 (E_NOT_OK: The API interface request was rejected.)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 获取某SEID对应的局部状态（LocalStatus）
     - 
     - 




WdgM_GetGlobalStatus函数定义 (The function definition for WdgM_GetGlobalStatus)
===========================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - WdgM_GetGlobalStatus
     - 
     - 
   * - 函数原型： (Function prototype:)
     - Std_ReturnType WdgM_GetGlobalStatus
     - 
     - 
   * - 
     - (
     - 
     - 
   * - 
     - WdgM_GlobalStatusType \*Status
     - 
     - 
   * - 
     - );
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x0D
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 不可重入 (Non-reentrant)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - 无
     - 
     - 
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - Status：指向SE的LocalStatus的指针 (Status：Pointer to LocalStatus pointing to SE)
     - 值域： (Domain:)
     - 无
   * - 返回值： (Return Value:)
     - E_OK：API接口请求被接受 (E_OK: The API interface request has been accepted)
     - 
     - 
   * - 
     - E_NOT_OK：API接口请求被拒绝 (E_NOT_OK: The API interface request was rejected.)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 获取全局状态（Global Status）
     - 
     - 




WdgM_PerformReset函数定义 (The WdgM_PerformReset function definition)
=================================================================================

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - WdgM_PerformReset
   * - 函数原型： (Function prototype:)
     - void WdgM_PerformReset(void);
   * - 服务编号： (Service Number:)
     - 0x0F
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
   * - 是否可重入： (Is Reentrant:)
     - 不可重入 (Non-reentrant)
   * - 输入参数： (Input parameters:)
     - 无
   * - 输入输出参数： (Input Output Parameters:)
     - 无
   * - 输出参数： (Output Parameters:)
     - 无
   * - 返回值： (Return Value:)
     - 无
   * - 功能概述： (Function Overview:)
     - 执行Watchdog复位操作 (Perform Watchdog Reset Operation)




WdgM_GetFirstExpiredSEID函数定义 (The WdgM_GetFirstExpiredSEID function definition)
===============================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - WdgM_GetFirstExpiredSEID
     - 
     - 
   * - 函数原型： (Function prototype:)
     - Std_ReturnType WdgM_GetFirstExpiredSEID
     - 
     - 
   * - 
     - (
     - 
     - 
   * - 
     - WdgM_SupervisedEntityIdType \*SEID
     - 
     - 
   * - 
     - );
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x10
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 不可重入 (Non-reentrant)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - 无
     - 
     - 
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - SEID：指向SEID的指针 (SEID：Pointer to SEID)
     - 值域： (Domain:)
     - 无
   * - 返回值： (Return Value:)
     - E_OK：返回SEID成功 (E_OK: Successfully returned SEID)
     - 
     - 
   * - 
     - E_NOT_OK：返回SEID失败 (E_NOT_OK: Failed to return SEID)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 获取第一次出现Local_Status_Expired的SE编号 (Get the SE number on first occurrence of Local_Status_Expired)
     - 
     - 




WdgM_MainFunction函数定义 (Definition of WdgM_MainFunction function)
================================================================================

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - WdgM_MainFunction
   * - 函数原型： (Function prototype:)
     - void WdgM_MainFunction(void);
   * - 服务编号： (Service Number:)
     - 0x08
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
   * - 是否可重入： (Is Reentrant:)
     - 不可重入 (Non-reentrant)
   * - 输入参数： (Input parameters:)
     - 无
   * - 输入输出参数： (Input Output Parameters:)
     - 无
   * - 输出参数： (Output Parameters:)
     - 无
   * - 返回值： (Return Value:)
     - 无
   * - 功能概述： (Function Overview:)
     - WdgM主函数，主函数依次判断得到Local status和GlobalStatus，并据此给出相应的故障处理 (Main function, the main function sequentially determines the Local status and GlobalStatus, and provides corresponding fault handling based on this.)




可配置函数定义 (Configurable Function Definition)
----------------------------------------------------------

无。

None.

SWC服务组件封装 (SWC Service Component Packaging)
-----------------------------------------------------------

以下类型和接口可以封装至SWC生成完整的服务组件，可以与应用通过端口连接，没有列出的部分WdgM底层暂时不支持。

The following types and interfaces can be encapsulated into SWC to generate complete service components, which can be connected to the application via ports. The underlying WdgM temporarily does not support the unlisted parts.

实现数据类型封装 (Implement data type encapsulation)
============================================================

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 类型名及定义引用 (Type Name and Definition Reference)
     - 生成条件 (Generate Conditions)
   * - WdgM_SupervisedEntityIdType
     - 无
   * - WdgM_CheckpointIdType
     - 无
   * - WdgM_Mode
     - 无
   * - WdgM_LocalStatusType
     - 无
   * - WdgM_GlobalStatusType
     - 无
   * - WdgM_ModeType
     - 无




.. _实现数据类型封装-1:

.. _Implementing Data Type Encapsulation-1:

实现数据类型封装 (Implement data type encapsulation)
============================================================

注：下面提到的<UserModule>和<UserPortName>分别为用户SWC的名字和对应端口名，在与WdgM服务组件端口连接后适用。

Note: The <UserModule> and <UserPortName> mentioned below refer to the name of the user SWC and its corresponding port name, applicable after connecting with the WdgM service component port.

Rte_Call_WdgM_LocalSupervision\_{SupervisedEntityCheckpointName}_CheckpointReached
--------------------------------------------------------------------------------------------------

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Rte_Call_WdgM_LocalSupervision\_{SupervisedEntityCheckpointName}_CheckpointReached
     - 
     - 
   * - 函数定义： (Function definition:)
     - Std_ReturnTypeRte_Call_WdgM_LocalSupervision\_{SupervisedEntityCheckpointName}_CheckpointReached(WdgM_SupervisedEntityIdTypeSEID,
     - 
     - 
   * - 
     - WdgM_CheckpointIdType CheckpointID);
     - 
     - 
   * - 服务编号： (Service Number:)
     - N/A
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - N/A
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - N/A
     - 
     - 
   * - 输入参数： (Input parameters:)
     - SEID：被监管实体的标识描述符 (SEID: Identifier Descriptor of Regulated Entity)
     - 值域： (Domain:)
     - 0 -65535
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - Status：给定被监督实体的监督状态 (Status: The supervisory status of the given supervised entity)
     - 值域： (Domain:)
     - 0 -65535
   * - 返回值： (Return Value:)
     - Std_ReturnType：
     - 
     - 
   * - 
     - E_OK： 成功 (E_OK: Success)
     - 
     - 
   * - 
     - E_NOT_OK： 失败 (E_NOT_OK: Failure)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 指示看门狗管理器已到达被监督实体内的检查点； (Indication that the watchdog manager has reached a checkpoint within the supervised entity;)
     - 
     - 
   * - 
     - 该端口为SWC提供一个监督实体检查点的监督接口； (This port provides a monitoring interface for SWC to supervise entity check points;)
     - 
     - 
   * - 变体： (Variants:)
     - SupervisedEntityCheckpointName =
     - 
     - 
   * - 
     - {ecuc(WdgM/WdgMGeneral/WdgMSupervisedEntity.SHORT-NAME)}\_{
     - 
     - 
   * - 
     - ecuc(WdgM/WdgMGeneral/WdgMSupervisedEntity/WdgMCheckpoint.
     - 
     - 
   * - 
     - SHORT-NAME)}
     - 
     - 
   * - 生成条件： (Generate conditions:)
     - {ecuc(WdgM/WdgMGeneral/WdgMSupervisedEntity/WdgMSupervisedEntityId.value)}
     - 
     - 
   * - 
     - ecuc{WdgM/WdgMGeneral/WdgMSupervisedEntity/Wdg
     - 
     - 
   * - 
     - MCheckpoint/WdgMCheckpointId}
     - 
     - 
   * - 端口类型： (Port Type:)
     - Require Port
     - 
     - 
   * - 从属端口： (Subordinate Port:)
     - localSupervision\_{SupervisedEntityCheckpointName}
     - 
     - 




Rte_Call_WdgM_LocalSupervisonStatus\_{SupervisedEntityName}_GetLocalStatus
------------------------------------------------------------------------------------------

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Rte_Call_WdgM_LocalSupervisonStatus\_{SupervisedEntityName}_GetLocalStatus
     - 
     - 
   * - 函数定义： (Function definition:)
     - Std_ReturnTypeRte_Call_WdgM_LocalSupervisonStatus\_{SupervisedEntityName}_GetLocalStatus(WdgM_SupervisedEntityIdTypeSEID,
     - 
     - 
   * - 
     - WdgM_LocalStatusType \*Status);
     - 
     - 
   * - 服务编号： (Service Number:)
     - N/A
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - N/A
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - N/A
     - 
     - 
   * - 输入参数： (Input parameters:)
     - SEID：被监管实体的标识描述符 (SEID: Identifier Descriptor of Regulated Entity)
     - 值域： (Domain:)
     - 0 -65535
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - Status：给定被监督实体的监督状态 (Status: The supervisory status of the given supervised entity)
     - 值域： (Domain:)
     - 0 -65535
   * - 返回值： (Return Value:)
     - Std_ReturnType：
     - 
     - 
   * - 
     - E_OK： 成功 (E_OK: Success)
     - 
     - 
   * - 
     - E_NOT_OK： 失败 (E_NOT_OK: Failure)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 返回单个被监督实体的监督状态； (Return the supervision status of individual supervised entities;)
     - 
     - 
   * - 
     - 该端口为SWC提供一个被监督实体的监督状态接口； (This port provides an interface for the supervised entity's supervision status for SWC;)
     - 
     - 
   * - 变体： (Variants:)
     - SupervisedEntityName =
     - 
     - 
   * - 
     - {ecuc(WdgM/WdgMGeneral/WdgMSupervisedEntity.SHORT-NAME)}
     - 
     - 
   * - 生成条件： (Generate conditions:)
     - {ecuc(WdgM/WdgMGeneral/WdgMSupervisedEntity/WdgMSupervisedEntityId.value)}
     - 
     - 
   * - 端口类型： (Port Type:)
     - Require Port
     - 
     - 
   * - 从属端口： (Subordinate Port:)
     - LocalSupervisonStatus\_{SupervisedEntityName}
     - 
     - 




Rte_Call_WdgM_GlobalSupervision_GetFirstExpiredSEID
-------------------------------------------------------------------

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Rte_Call_WdgM_GlobalSupervision_GetFirstExpiredSEID
     - 
     - 
   * - 函数定义： (Function definition:)
     - Std_ReturnTypeRte_Call_WdgM_GlobalSupervision_GetFirstExpiredSEID
     - 
     - 
   * - 
     - (WdgM_SupervisedEntityIdType\*SEID);
     - 
     - 
   * - 服务编号： (Service Number:)
     - N/A
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - N/A
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - N/A
     - 
     - 
   * - 输入参数： (Input parameters:)
     - 无
     - 
     - 
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - SEID：被监管实体的标识描述符 (SEID: Identifier Descriptor of Regulated Entity)
     - 值域： (Domain:)
     - 0 -65535
   * - 返回值： (Return Value:)
     - Std_ReturnType：
     - 
     - 
   * - 
     - E_OK： 成功 (E_OK: Success)
     - 
     - 
   * - 
     - E_NOT_OK： 失败 (E_NOT_OK: Failure)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 返回第一个到达状态WDGM_LOCAL_STATUS_EXPIRED的SEID； (Return the SEID that first reaches the state WDGM_LOCAL_STATUS_EXPIRED;)
     - 
     - 
   * - 
     - 该端口提供WdgM的全局监督接口； (This port provides the global supervision interface for WdgM;)
     - 
     - 
   * - 变体： (Variants:)
     - 无
     - 
     - 
   * - 生成条件： (Generate conditions:)
     - 无
     - 
     - 
   * - 端口类型： (Port Type:)
     - Require Port
     - 
     - 
   * - 从属端口： (Subordinate Port:)
     - GlobalSupervision
     - 
     - 




Rte_Call_WdgM_GlobalSupervision_GetMode
-------------------------------------------------------

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Rte_Call_WdgM_GlobalSupervision_GetFirstExpiredSEID
     - 
     - 
   * - 函数定义： (Function definition:)
     - Std_ReturnTypeRte_Call_WdgM_GlobalSupervision_GetMode
     - 
     - 
   * - 
     - (WdgM_ModeType \*Mode);
     - 
     - 
   * - 服务编号： (Service Number:)
     - N/A
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - N/A
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - N/A
     - 
     - 
   * - 输入参数： (Input parameters:)
     - 无
     - 
     - 
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - Mode：看门狗管理器的当前工作模式 (Mode: Current Working Mode of Watchdog Manager)
     - 值域： (Domain:)
     - 0 - 255
   * - 返回值： (Return Value:)
     - Std_ReturnType：
     - 
     - 
   * - 
     - E_OK： 成功 (E_OK: Success)
     - 
     - 
   * - 
     - E_NOT_OK： 失败 (E_NOT_OK: Failure)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 返回看门狗管理器当前工作模式； (Return the current operating mode of the watchdog manager;)
     - 
     - 
   * - 
     - 该端口提供WdgM的全局监督接口； (This port provides the global supervision interface for WdgM;)
     - 
     - 
   * - 变体： (Variants:)
     - 无
     - 
     - 
   * - 生成条件： (Generate conditions:)
     - 无
     - 
     - 
   * - 端口类型： (Port Type:)
     - Require Port
     - 
     - 
   * - 从属端口： (Subordinate Port:)
     - GlobalSupervision
     - 
     - 




Rte_Call_WdgM_GlobalSupervision_PerformReset
------------------------------------------------------------

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Rte_Call_WdgM_GlobalSupervision_PerformReset
     - 
     - 
   * - 函数定义： (Function definition:)
     - Std_ReturnTypeRte_Call_WdgM_GlobalSupervision_PerformReset
     - 
     - 
   * - 
     - (WdgM_ModeType \*Mode);
     - 
     - 
   * - 服务编号： (Service Number:)
     - N/A
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - N/A
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - N/A
     - 
     - 
   * - 输入参数： (Input parameters:)
     - 无
     - 
     - 
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - Mode：看门狗管理器的当前工作模式 (Mode: Current Working Mode of Watchdog Manager)
     - 值域： (Domain:)
     - 0 - 255
   * - 返回值： (Return Value:)
     - Std_ReturnType：
     - 
     - 
   * - 
     - E_OK： 成功 (E_OK: Success)
     - 
     - 
   * - 
     - E_NOT_OK： 失败 (E_NOT_OK: Failure)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 返回看门狗管理器当前工作模式； (Return the current operating mode of the watchdog manager;)
     - 
     - 
   * - 
     - 通知Watchdog Manager复位看门狗； (Notify Watchdog Manager to reset the watchdog;)
     - 
     - 
   * - 
     - 该端口提供WdgM的全局监督接口； (This port provides the global supervision interface for WdgM;)
     - 
     - 
   * - 变体： (Variants:)
     - 无
     - 
     - 
   * - 生成条件： (Generate conditions:)
     - 无
     - 
     - 
   * - 端口类型： (Port Type:)
     - Require Port
     - 
     - 
   * - 从属端口： (Subordinate Port:)
     - GlobalSupervision
     - 
     - 




Rte_Call_WdgM_GlobalSupervision_GetGlobalStatus
---------------------------------------------------------------

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Rte_Call_WdgM_GlobalSupervision_GetGlobalStatus
     - 
     - 
   * - 函数定义： (Function definition:)
     - Std_ReturnTypeRte_Call_WdgM_GlobalSupervision_GetGlobalStatus
     - 
     - 
   * - 
     - (WdgM_GlobalStatusType \*Status);
     - 
     - 
   * - 服务编号： (Service Number:)
     - N/A
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - N/A
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - N/A
     - 
     - 
   * - 输入参数： (Input parameters:)
     - 无
     - 
     - 
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - Status：Watchdog Manager全局监控状态 (Status: Global Monitoring Status of Watchdog Manager)
     - 值域： (Domain:)
     - 0 -65535
   * - 返回值： (Return Value:)
     - Std_ReturnType：
     - 
     - 
   * - 
     - E_OK： 成功 (E_OK: Success)
     - 
     - 
   * - 
     - E_NOT_OK： 失败 (E_NOT_OK: Failure)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 返回看门狗管理器的全局监控状态； (Return the global monitoring state of the watchdog manager;)
     - 
     - 
   * - 
     - 该端口提供WdgM的全局监督接口； (This port provides the global supervision interface for WdgM;)
     - 
     - 
   * - 变体： (Variants:)
     - 无
     - 
     - 
   * - 生成条件： (Generate conditions:)
     - 无
     - 
     - 
   * - 端口类型： (Port Type:)
     - Require Port
     - 
     - 
   * - 从属端口： (Subordinate Port:)
     - GlobalSupervision
     - 
     - 




Rte_Call_WdgM_GlobalSupervision_SetMode
-------------------------------------------------------

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Rte_Call_WdgM_GlobalSupervision_SetMode
     - 
     - 
   * - 函数定义： (Function definition:)
     - Std_ReturnTypeRte_Call_WdgM_GlobalSupervision_SetMode
     - 
     - 
   * - 
     - (WdgM_ModeType Mode);
     - 
     - 
   * - 服务编号： (Service Number:)
     - N/A
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - N/A
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - N/A
     - 
     - 
   * - 输入参数： (Input parameters:)
     - Mode：已配置的看门狗管理模式之一 (Mode：One of the configured watchdog management modes.)
     - 值域： (Domain:)
     - 0 - 255
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - Status：Watchdog Manager全局监控状态 (Status: Global Monitoring Status of Watchdog Manager)
     - 值域： (Domain:)
     - 0 -65535
   * - 返回值： (Return Value:)
     - Std_ReturnType：
     - 
     - 
   * - 
     - E_OK： 成功 (E_OK: Success)
     - 
     - 
   * - 
     - E_NOT_OK： 失败 (E_NOT_OK: Failure)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 设置看门狗的当前工作模式； (Set the current working mode of the watchdog;)
     - 
     - 
   * - 
     - 该端口提供WdgM的全局监督接口； (This port provides the global supervision interface for WdgM;)
     - 
     - 
   * - 变体： (Variants:)
     - 无
     - 
     - 
   * - 生成条件： (Generate conditions:)
     - 无
     - 
     - 
   * - 端口类型： (Port Type:)
     - Require Port
     - 
     - 
   * - 从属端口： (Subordinate Port:)
     - GlobalSupervision
     - 
     - 




模式转换接口封装 (Interface Encapsulation for Mode Conversion)
======================================================================

WdgM_LocalMode\_{SupervisedEntityName} 
-------------------------------------------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 接口名称： (Interface Name:)
     - WdgM_LocalMode\_{SupervisedEntityName}
   * - 变体： (Variants:)
     - SupervisedEntityName ={ecuc(WdgM/WdgMGeneral/WdgMSupervisedEntity/WdgMSupervisedEntityId.SHORT-NAME)}
   * - 生成条件： (Generate conditions:)
     - 无
   * - 模式组： (Pattern Group:)
     - SupervisedEntityName
   * - 端口类型： (Port Type:)
     - Provided Port
   * - 从属端口： (Subordinate Port:)
     - modeSwitchPort_WdgMLocalMode\_{SupervisedEntityName}




WdgM_GlobalMode
-------------------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 接口名称： (Interface Name:)
     - WdgM_GlobalMode
   * - 变体： (Variants:)
     - 无
   * - 生成条件： (Generate conditions:)
     - 无
   * - 模式组： (Pattern Group:)
     - 无
   * - 端口类型： (Port Type:)
     - Provided Port
   * - 从属端口： (Subordinate Port:)
     - modeSwitchPort_WdgMGlobalMode




配置 (Configure)
==============================

主要介绍WdgM模块的配置参数，列举配置项在配置界面显示的名称，对应的标准、可能的取值、默认的取值、参数描述及依赖关系，旨在指导用户如何使用配置工具进行WdgM模块参数的配置。

Mainly introduce the configuration parameters of the WdgM module, listing the names of configuration items as displayed in the configuration interface, corresponding standards, possible values, default values, parameter descriptions, and dependencies, aiming to guide users on how to configure the parameters of the WdgM module using the configuration tool.

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




WdgMGeneral配置 (WdgMGeneral Configuration)
---------------------------------------------------------

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/WdgM/image6.png
   :alt: WdgM模块的General容器配置图 (The General container configuration diagram of WdgM module)
   :name: WdgM模块的General容器配置图 (The General container configuration diagram of WdgM module)
   :align: center


.. centered:: **表 WdgM模块的General配置属性描述 (Description of General Configuration Properties for WdgM Module)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - WdgMDevErrorDetect
     - 取值范围 (Range)
     - STD_ON,STD_OFF
     - 默认取值 (Default value)
     - STD_OFF
   * -
     - 参数描述 (Parameter Description)
     - 是否开启配置出错检测。若开启，一旦检测到配置出错，则代码停留在故障出错位置。量产用代码，需关闭该配置。 (Is configuration error detection enabled? If enabled, the code will halt at the position of the detected error. This configuration should be disabled for production code.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 依赖于DET模块的配置 (Dependent on the configuration of DET module)
     - 
     - 
   * - WdgMImmediateReset
     - 取值范围 (Range)
     - STD_ON,STD_OFF
     - 默认取值 (Default value)
     - STD_OFF
   * - 
     - 参数描述 (Parameter Description)
     - Global statusStopped状态时，是否调用Mcu_PerformReset执行立即复位操作。 (Global statusStopped status, whether to call Mcu_PerformReset to execute an immediate reset operation.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 依赖于复位机制 (Dependent on reset mechanisms)
     - 
     - 
   * - WdgMOffModeEnabled
     - 取值范围 (Range)
     - STD_ON,STD_OFF
     - 默认取值 (Default value)
     - STD_OFF
   * - 
     - 参数描述 (Parameter Description)
     - 是否允许WatchdogDriver配置为OffMode模式。 (Is WatchdogDriver allowed to be configured in OffMode mode.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 依赖于Wdg底层设备驱动程序 (Dependent on the underlying device driver of Wdg)
     - 
     - 
   * - WdgMVersionInfoApi
     - 取值范围 (Range)
     - STD_ON,STD_OFF
     - 默认取值 (Default value)
     - STD_OFF
   * - 
     - 参数描述 (Parameter Description)
     - 是否在编译时，查看配置文件，源文件的版本信息是否一致 (Is it necessary to check if the version information of the configuration file and source files is consistent during compilation?)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - FIRST_EXPIRED_SEID
     - 取值范围 (Range)
     - 0...4294967295
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - 保存在此区域的数据在热复位后不得擦除或复位。热复位是指复位操作时电源正常。监管实体ID占用2字节。 (The data saved in this area shall not be erased or reset after a warm reset. A warm reset refers to a reset operation with normal power supply. The regulatory authority ID occupies 2 bytes.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 依赖于内存保护 (Dependent on memory protection)
     - 
     - 
   * - FIRST_EXPIRED_INVERSE_SEID
     - 取值范围 (Range)
     - 0...4294967295
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - 保存在此区域的数据在热复位后不得擦除或复位。热复位是指复位操作时电源正常。监管实体ID占用2字节。 (The data saved in this area shall not be erased or reset after a warm reset. A warm reset refers to a reset operation with normal power supply. The regulatory authority ID occupies 2 bytes.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 依赖于内存保护 (Dependent on memory protection)
     - 
     - 




WdgMSupervisedEntity配置 (WdgMSupervisedEntity Configuration)
===========================================================================

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/WdgM/image7.png
   :alt: WdgM监督实体配置 (WdgM Supervision Entity Configuration)
   :name: WdgM监督实体配置 (WdgM Supervision Entity Configuration)
   :align: center


.. centered:: **表 WdgM模块的监督实体配置属性描述 (Description of Supervision Entity Configuration Properties for WdgM Module)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - WdgMSupervisedEntityId
     - 取值范围 (Range)
     - ...65535
     - 默认取值 (Default value)
     - 1
   * - 
     - 参数描述 (Parameter Description)
     - 该参数应包含被监督实体的唯一标识符。 (This parameter should contain a unique identifier for the supervised entity.)
     - 
     - 
   * - 
     - 
     - 备注： (Note:)
     - 
     - 
   * - 
     - 
     - 不同的WdgM监督实体不能有相同的WdgM监督实体ID (Different WdgM monitoring entities cannot have the same WdgM monitoring entity ID)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - WdgMInternalTransitionId
     - 取值范围 (Range)
     - 0...65535
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - 用于描述外部逻辑监督ID (To describe external logical supervision ID)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - WdgMOsApplicationRef
     - 取值范围 (Range)
     - 引用或下拉选项 (Copy or Pull-down Options)
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 对操作系统应用程序的可选引用。 (Optional references to operating system applications.)
     - 
     - 
   * - 
     - 
     - 注意，当相应的受监督实体到达 (Note, when the corresponding supervised entity arrives,)
     - 
     - 
   * - 
     - 
     - WDGM_LOCAL_STATUS_FAILED时，看门狗管理器模块将触发该操作系统应用程序的分区重新启动。 (When WDGM_LOCAL_STATUS_FAILED occurs, the watchdog manager module will trigger a reboot of the partition for the operating system application.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 依赖于操作系统 (Dependent on the operating system)
     - 
     - 
   * - WdgMInternalCheckpointInitialRef
     - 取值范围 (Range)
     - 引用或下拉选项 (Copy or Pull-down Options)
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 用于实现对这个监督实体的初始检查点的引用 (To refer to the initial checkpoint for this supervised entity)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 依赖于监控点的配置 (Dependent on the configuration of monitoring points)
     - 
     - 
   * - WdgMInternallCheckpointFinalRef
     - 取值范围 (Range)
     - 引用或下拉选项 (Copy or Pull-down Options)
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 用于实现对这个监督实体的最终检查点的引用 (Reference for the final checkpoint of implementing this supervised entity)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - WdgMPartitionResetCallBack
     - 取值范围 (Range)
     - True或False (True or False)
     - 默认取值 (Default value)
     - False
   * - 
     - 参数描述 (Parameter Description)
     - 用户为WdgM多分区重置定义的回调接口开关 (Callback interface switch defined by users for WdgM multi-part reset)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - WdgMEcucPartitionRef
     - 
     - 
   * - WdgMEcucPartitionRef
     - 取值范围 (Range)
     - 引用或下拉选项 (Copy or Pull-down Options)
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 表示被监督实体在该“EcucPartition”中执行 (Indicate that the supervised entity executes in this "EcucPartition")
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - BswMPartitionRef
     - 
     - 
   * - WdgMOSCounter
     - 取值范围 (Range)
     - 引用或下拉选项 (Copy or Pull-down Options)
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - WdgM用于对SE执行Deadline监督的操作系统计数器 (WdgM is used for performing deadline supervision on SE using operating system counters.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - OsCounter
     - 
     - 




WdgMCheckpoints配置 (WDGMCheckpoints Configuration)
=================================================================

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/WdgM/image8.png
   :alt: WdgM监督实体配置1 (WdgM Supervision Entity Configuration)
   :name: WdgM监督实体配置1 (WdgM Supervision Entity Configuration)
   :align: center


.. centered:: **表 WdgM模块的监控点配置属性描述 (Configuration property description for monitoring points of WdgM module)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - WdgMCheckpointId
     - 取值范围 (Range)
     - 0...65535
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - 参数用于实现应包含检查点的唯一标识符 (Parameters for implementing unique identifiers that should include checkpoints)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 




WdgMInternalTransition配置 (WdgMInternalTransition Configuration)
===============================================================================

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/WdgM/image9.png
   :alt: WdgM模块的内部转换配置 (Internal conversion configuration of WdgM module)
   :name: WdgM模块的内部转换配置 (Internal conversion configuration of WdgM module)
   :align: center


.. centered:: **表 WdgM模块的内部转换配置属性描述 (Internal Conversion Configuration Properties Description for WdgM Module)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - WdgMInternalTransitionSourceRef
     - 取值范围 (Range)
     - 引用或下拉选项 (Copy or Pull-down Options)
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 参数用于对给定监督实体内部转换的源检查点的引用 (Parameters for referring to the source checkpoint internal transformation within a given supervised entity)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 依赖于监控点的配置 (Dependent on the configuration of monitoring points)
     - 
     - 
   * - WdgMInternalTransitionDestRef
     - 取值范围 (Range)
     - 引用或下拉选项 (Copy or Pull-down Options)
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 参数用于对给定监督实体内部转换的目标检查点的引用 (Parameters are used for referencing target checkpoints within the given supervised entity for internal transformation.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 依赖于监控点的配置 (Dependent on the configuration of monitoring points)
     - 
     - 




WdgMWatchdog配置 (WatchdogConfiguration)
======================================================

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/WdgM/image10.png
   :alt: WdgM驱动接口挂接配置 (WdgM Driver Interface Mount Configuration)
   :name: WdgM驱动接口挂接配置 (WdgM Driver Interface Mount Configuration)
   :align: center


.. centered:: **表 WdgM模块的驱动接口挂接配置属性描述 (Description of attributes for driver interface attachment configuration of WdgM module)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - WdgMWatchdogName
     - 取值范围 (Range)
     - 字符串：uint8 [] (String: uint8[])
     - 默认取值 (Default value)
     - NULL_PTR
   * - 
     - 参数描述 (Parameter Description)
     - 参数必须包含看门狗实例索引的符号名称 (The parameters must include the symbolic name of the watchdog instance index.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - WdgMWatchdogDeviceRef
     - 取值范围 (Range)
     - 引用或下拉选项 (Copy or Pull-down Options)
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 对Watchdog接口的一个设备容器的引用。在被引用的容器WdgIfDevice中，参数WdgIfDeviceIndex包含了Index参数，WdgM必须使用这个参数来调用WdgIf_SetTriggerCondition来调用这个Watchdog实例。 (A reference to a device container for the Watchdog interface. In the referenced container WdgIfDevice, the parameter WdgIfDeviceIndex contains the Index parameter, which must be used by WdgM to call WdgIf_SetTriggerCondition to call this Watchdog instance.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 依赖于WdgIf的配置 (Dependent on the configuration of WdgIf)
     - 
     - 




WdgMConfigSet配置 (WdgMConfigSet Configuration)
-------------------------------------------------------------

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/WdgM/image11.png
   :alt: WdgM配置集的设置 (Configuration settings for WdgM configuration sets)
   :name: WdgM配置集的设置 (Configuration settings for WdgM configuration sets)
   :align: center


.. centered:: **表 WdgM模块的ConfigSet配置属性描述 (Description of ConfigSet Configuration Property for WdgM Module)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - WdgMInitialMode
     - 取值范围 (Range)
     - 引用或下拉选项 (Copy or Pull-down Options)
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 软件看门狗管理模块初始化后的状态 (The state after initialization of the software watchdog management module)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 




WdgMDemEventParameterRefs配置 (WdgMDemEventParameterRefs Configuration)
=====================================================================================

容器用于引用DemEventParameter元素，该元素应使用API Dem_ReportErrorStatus API调用，以防发生相应的错误。EventId取自引用的DemEventParameter的DemEventId值。标准化错误在容器中提供，可以通过供应商特定的错误引用进行扩展。

Containers are used to reference the DemEventParameter element, which should be invoked using the API Dem_ReportErrorStatus to call for an appropriate error. EventId is taken from the DemEventId value of the referenced DemEventParameter. Standardized errors are provided within the container and can be extended through vendor-specific error references.

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/WdgM/image12.png
   :alt: WdgM模块的DEM事件参数配置 (Configuration of DEM Event Parameters for WdgM Module)
   :name: WdgM模块的DEM事件参数配置 (Configuration of DEM Event Parameters for WdgM Module)
   :align: center


.. centered:: **表 WdgM模块的Dem配置属性描述 (Description of Dem Configuration Properties for WdgM Module)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - WDGM_E_SET_MODEWDGM_E_SET_MODE
     - 取值范围 (Range)
     - 0...65535
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - 参考DemEventParameter，当错误“看门狗驱动程序的模式切换到失败”已经发生时应发出。 (Refer to DemEventParameter when an error "mode switch failed for watchdog driver" has occurred.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - WDGM_E_SUPERVISION
     - 取值范围 (Range)
     - 0...65535
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - 当错误“监督失败，看门狗复位将发生”时，将发出 (When the error "Supervision failure, watchdog reset will occur" occurs, a)
     - 
     - 
   * - 
     - 
     - DemEventParameter引用已经发生。 (DemEventParameter Reference Has Been Made.)
     - 
     - 
   * - 
     - 
     - 备注：全局监管状态已达到 (Note: Global regulatory status has reached)
     - 
     - 
   * - 
     - 
     - WDGM_GLOBAL_STATUS_STOPPED
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 依赖于WdgIf的配置 (Dependent on the configuration of WdgIf)
     - 
     - 




WdgMMode-OffMode配置 (WdgMMode-Off Mode Configuration)
====================================================================

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/WdgM/image13.png
   :alt: WdgM关闭模式OffMode的配置 (Configure WdgM in OffMode mode)
   :name: WdgM关闭模式OffMode的配置 (Configure WdgM in OffMode mode)
   :align: center


.. centered:: **表 WdgM模块的OffsetMode配置属性描述 (The OffsetMode configuration property description for Module WdgM module)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - WdgMExpiredSupervisionCycleTol
     - 取值范围 (Range)
     - 0...65535
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - 这个参数应使用定义了一个值，用来固定在全局监控状态达到过期状态后，延迟阻塞看门狗触发的监控周期数量。 (This parameter should be set to a value that defines the number of monitoring cycles to delay the watchdog trigger after the global monitoring state reaches an expired state.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - WdgMModeId
     - 取值范围 (Range)
     - 0...65535
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - 此参数固定模式的标识符。例如，这个标识符作为参数传递给WdgM_SetMode服务。 (This parameter identifier for fixed mode. For example, this identifier is passed as a parameter to the WdgM_SetMode service.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - WdgMSupervisionCycle
     - 取值范围 (Range)
     - 0...65535
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - 该参数定义了主函数WdgM_MainFunction的调度周期。 (This parameter defines the scheduling period of the main function WdgM_MainFunction.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 




WdgMMode-OffMode-Trigger配置 (WdgMMode-OffMode-Trigger Configuration)
-----------------------------------------------------------------------------------

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/WdgM/image14.png
   :alt: WdgM触发硬件看门狗的配置 (Configure WdgM to trigger hardware watchdog)
   :name: WdgM触发硬件看门狗的配置 (Configure WdgM to trigger hardware watchdog)
   :align: center


.. centered:: **表 WdgM模块的OffsetMode-Trigger配置属性描述 (The OffsetMode-Trigger configuration property description for Table WdgM module)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - WdgMTriggerConditionValue
     - 取值范围 (Range)
     - 0...65535
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - 这个参数应该包含这个看门狗传递给 (This parameter should include what the watchdog passes.)
     - 
     - 
   * - 
     - 
     - WdgIf_SetTriggerCondition的值。 (The value of WdgIf_SetTriggerCondition.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - WdgMWatchdogMode
     - 取值范围 (Range)
     - 引用或下拉选项 (Copy or Pull-down Options)
     - 默认取值 (Default value)
     - WDGIF_OFF_MODE
   * - 
     - 参数描述 (Parameter Description)
     - 该参数包含看门狗模式，应使用代表在此看门狗管理模式下引用的看门狗。 (This parameter contains watchdog mode and should be used with a watchdog that is referenced in this watchdog management mode.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 依赖于WdgIf和Wdg的配置 (Dependent on the configuration of WdgIf and Wdg.)
     - 
     - 
   * - WdgMTriggerWatchdogRef
     - 取值范围 (Range)
     - 0...65535
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - 该参数是对配置看门狗的引用 (This parameter is a reference to the configuration watchdog.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 




WdgMMode-FastMode配置 (WdgMMode-FastMode Configuration)
=====================================================================

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/WdgM/image15.png
   :alt: WdgM关闭模式FastMode的配置 (Close Mode FastMode Configuration)
   :name: WdgM关闭模式FastMode的配置 (Close Mode FastMode Configuration)
   :align: center


.. centered:: **表 WdgM模块的FastMode配置属性描述 (Description of the FastMode configuration property for WdgM module)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - WdgMExpiredSupervisionCycleTol
     - 取值范围 (Range)
     - 0...65535
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - 这个参数应使用定义了一个值，用来固定在全局监控状态达到过期状态后，延迟阻塞看门狗触发的监控周期数量。 (This parameter should be set to a value that defines the number of monitoring cycles to delay the watchdog trigger after the global monitoring state reaches an expired state.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - WdgMModeId
     - 取值范围 (Range)
     - 0...65535
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - 此参数固定模式的标识符。例如，这个标识符作为参数传递给WdgM_SetMode服务。 (This parameter identifier for fixed mode. For example, this identifier is passed as a parameter to the WdgM_SetMode service.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - WdgMSupervisionCycle
     - 取值范围 (Range)
     - 0...65535
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - 该参数定义了主函数WdgM_MainFunction的调度周期。 (This parameter defines the scheduling period of the main function WdgM_MainFunction.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 




WdgMMode-FastMode-AliveSupervision
--------------------------------------------------

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/WdgM/image16.png
   :alt: WdgM活性监督的配置 (Configuration of WdgM Active Supervision)
   :name: WdgM活性监督的配置 (Configuration of WdgM Active Supervision)
   :align: center


.. centered:: **表 WdgM模块的FastMode-AliveSupervision配置属性描述 (The FastMode-AliveSupervision configuration property description for Table WdgM module)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - WdgMAliveSupervisionId
     - 取值范围 (Range)
     - 0...65535
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - 用于描述活性监督的唯一标识符 (Unique identifier for describing active supervision)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - WdgMExpectedAliveIndications
     - 取值范围 (Range)
     - 0...65535
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - 该参数包含根据对应的SE定义的监督周期的参考数量中Checkpoint的预期存活指示的数量。 (This parameter indicates the expected number of Checkpoints that are intended to survive in the reference count of supervision cycles according to the corresponding SE definition.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - WdgMMaxMargin
     - 取值范围 (Range)
     - 0...65535
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - 此参数包含Checkpoint的活性指示的数量，这些活性指示是可接受的，可以附加到相应的监督参考周期内的预期活性指示。 (This parameter contains the number of active indicators for Checkpoints, which are acceptable and can be attached to the expected active indicators within the corresponding supervised reference cycle.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 依赖于OS操作系统 (Dependent on OS operating system)
     - 
     - 
   * - WdgMMinMargin
     - 取值范围 (Range)
     - 0...65535
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - 此参数包含Checkpoint的活性指示的数量，这些活性指示在相应的监督参考周期内可以从预期的活性指示中错过。 (This parameter contains the number of checkpoint liveness indicators, which can miss the expected liveness indicators within the corresponding supervisory reference period.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 依赖于监控点的配置 (Dependent on the configuration of monitoring points)
     - 
     - 
   * - WdgMSupervisionReferenceCycle
     - 取值范围 (Range)
     - 0...65535
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - 该参数应包含活性监督机制根据对应的SE进行活性指示计数检查时所参考的监测周期数。 (This parameter should contain the monitoring cycle number referenced by the active supervision mechanism for active indicator counting checks corresponding to the SE.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - WdgMAliveSupervisionCheckpointRef
     - 取值范围 (Range)
     - 引用或下拉选项 (Copy or Pull-down Options)
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 指被监管单位内部应被监管的Checkpoint监控点 (Indications within the regulated entities that should be monitored by Checkpoints.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 




WdgMMode-FastMode-DeadlineSupervision
-----------------------------------------------------

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/WdgM/image17.png
   :alt: WdgM期限监督的配置 (Configuration for Term Supervision)
   :name: WdgM期限监督的配置 (Configuration for Term Supervision)
   :align: center


.. centered:: **表 WdgM模块的FastMode-DeadlineSupervision配置属性描述 (The FastMode-DeadlineSupervision configuration property description for Table WdgM module)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - WdgMEnableTimeoutDetection
     - 取值范围 (Range)
     - STD_OFF，STD_ON
     - 默认取值 (Default value)
     - STD_OFF
   * -
     - 参数描述 (Parameter Description)
     - 是否开启配置超时检测。若开启，一旦检测到期限监督发生超市，则触发看门狗的复位功能。 (Is configuration timeout detection enabled? If enabled, the watchdog reset function will be triggered once a timeout supervision exceeds the detected period.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - WdgMDeadlineSupervisionId
     - 取值范围 (Range)
     - 0...65535
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - 用于描述期限监督的唯一标识符 (Unique identifier for describing term supervision)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - WdgMDeadlineMax
     - 取值范围 (Range)
     - 0...65535
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - 此参数包含超过该期限的最长时间跨度 (This parameter includes the longest time span exceeding the deadline.)
     - 
     - 
   * - 
     - 
     - 备注：单位为秒 (Note: Units in seconds)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - WdgMDeadlineMin
     - 取值范围 (Range)
     - 0...65535
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - 此参数包含最短的时间跨度，超过该时间跨度就认为满足了最后期限。 (This parameter contains the shortest time span, beyond which the deadline is considered satisfied.)
     - 
     - 
   * - 
     - 
     - 备注：单位为秒 (Note: Units in seconds)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 依赖于监控点的配置 (Dependent on the configuration of monitoring points)
     - 
     - 
   * - WdgMDeadlineStartRef
     - 取值范围 (Range)
     - 引用或下拉选项 (Copy or Pull-down Options)
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 用于实现对期限监督的开始Checkpoint监控点的引用 (Reference for the beginning Checkpoint monitoring point for implementing term supervision)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - WdgMDeadlineStopRef
     - 取值范围 (Range)
     - 引用或下拉选项 (Copy or Pull-down Options)
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 用于实现对期限监督的终止Checkpoint监控点的引用 (Reference for checkpoint monitoring to achieve term supervision termination)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 




WdgMMode-FastMode-ExternalLogicalSupervision
------------------------------------------------------------

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/WdgM/image18.png
   :alt: WdgM外部逻辑监督的配置 (Configuration of External Logical Supervision)
   :name: WdgM外部逻辑监督的配置 (Configuration of External Logical Supervision)
   :align: center


.. centered:: **表 WdgM模块的FastMode-ExternalLogicalSupervision配置属性描述 (Configuration property description for FastMode-ExternalLogicalSupervision of WdgM module)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - WdgMExternalLogicalSupervisionId
     - 取值范围 (Range)
     - 0...65535
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - 用于描述外部逻辑监督的唯一标识符 (Unique identifier for describing external logical supervision)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - WdgMExternalCheckpointInitialRef
     - 取值范围 (Range)
     - 引用或下拉选项 (Copy or Pull-down Options)
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 用于实现对这个外部图的初始Checkpoint监控点的引用 (For the initial checkpoint reference of this external graph)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - WdgMExternalCheckpointFinalRef
     - 取值范围 (Range)
     - 引用或下拉选项 (Copy or Pull-down Options)
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 用于实现对这个外部图的最终Checkpoint监控点的引用 (To reference the final checkpoint for monitoring this external graph)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 




.. figure:: ../../_static/参考手册(Module_Reference_Manual)/WdgM/image19.png
   :alt: WdgM外部逻辑监督外部转换的配置 (External Logic Supervision of External Conversion Configuration)
   :name: WdgM外部逻辑监督外部转换的配置 (External Logic Supervision of External Conversion Configuration)
   :align: center


.. centered:: **表 WdgM模块的FastMode-ExternalTransition配置属性描述 (Description of the FastMode-ExternalTransition configuration property for WdgM module)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - WdgMExternalTransitionSourceRef
     - 取值范围 (Range)
     - 0...65535
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - 用于实现对外部迁移的源Checkpoint监控点的引用 (Reference for Checkpoint for monitoring source for external migration)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - WdgMExternalTransitionDestRef
     - 取值范围 (Range)
     - 0...65535
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - 用于实现对外部迁移的目标Checkpoint监控点的引用 (Reference for the Checkpoint Monitor used to achieve external migration goals)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 




WdgMMode-FastMode-LocalStatusParams
---------------------------------------------------

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/WdgM/image20.png
   :alt: WdgM局部监督状态参数的配置 (Configuration of local supervision state parameters WdgM)
   :name: WdgM局部监督状态参数的配置 (Configuration of local supervision state parameters WdgM)
   :align: center


.. centered:: **表 WdgM模块的FastMode-LocalStatusParameter配置属性描述 (Configuration property description for FastMode-LocalStatusParameter of WdgM module)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - WdgMFailedAliveSupervisionRefCycleTol
     - 取值范围 (Range)
     - 0...65535
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - 该参数应包含对该监督实体的不正确/失败的有效监督的可接受的参考周期数量 (This parameter should contain the acceptable reference cycle number for valid supervision of an incorrect/failure supervision entity.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - WdgMLocalStatusSupervisedEntityRef
     - 取值范围 (Range)
     - 引用或下拉选项 (Copy or Pull-down Options)
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 这是对监督实体的引用，其中本地状态参数被指定 (This is a reference to a supervising entity where local state parameters are specified.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 




WdgMMode-FastMode-WdgMTrigger
---------------------------------------------

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/WdgM/image21.png
   :alt: WdgM触发参数的配置 (Configuration of WdgM Trigger Parameters)
   :name: WdgM触发参数的配置 (Configuration of WdgM Trigger Parameters)
   :align: center


.. centered:: **表 WdgM模块的FastMode-Trigger配置属性描述 (The FastMode-Trigger configuration property description for Module WdgM)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - WdgMTriggerConditionValue
     - 取值范围 (Range)
     - 0...65535
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - 这个参数应该包含这个看门狗传递给 (This parameter should include what the watchdog passes.)
     - 
     - 
   * - 
     - 
     - WdgIf_SetTriggerCondition的值。 (The value of WdgIf_SetTriggerCondition.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - WdgMWatchdogMode
     - 取值范围 (Range)
     - 引用或下拉选项 (Copy or Pull-down Options)
     - 默认取值 (Default value)
     - WDGIF_FAST_MODE
   * - 
     - 参数描述 (Parameter Description)
     - 该参数包含看门狗模式，应使用代表在此看门狗管理模式下引用的看门狗。 (This parameter contains watchdog mode and should be used with a watchdog that is referenced in this watchdog management mode.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 依赖于WdgIf和Wdg的配置 (Dependent on the configuration of WdgIf and Wdg.)
     - 
     - 
   * - WdgMTriggerWatchdogRef
     - 取值范围 (Range)
     - 0...65535
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - 该参数是对配置看门狗的引用 (This parameter is a reference to the configuration watchdog.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 




WdgMMode-SlowMode配置 (WdgMMode_SlowMode Configuration)
=====================================================================

备注：与FastMode的描述保持一致。

Note: Consistent with the description of FastMode.
