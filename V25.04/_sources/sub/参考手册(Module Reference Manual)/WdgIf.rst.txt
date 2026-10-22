WdgIf
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
     - 应用程序接口 (Application Programming Interface)
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
     - 看门狗管理器 (Watchdog Manager)
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
     - The Motor Industry SoftwareReliability Association
     - 电机工业软件可靠性协会 (Association for Reliability of Electrical Machinery Software)
   * - TCL
     - Tool Confidence Level
     - 工具置信度等级 (Tool confidence level)
   * - SEOOC
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

WdgIf是AUTOSAR的一个基础软件模块，WdgIf模块为访问Watchdog Driver提供统一的服务，包括看门狗启动和模式切换等。

WdgIf is a basic software module of AUTOSAR, providing unified services for accessing the Watchdog Driver, including watchdog startup and mode switching.

ORIENTAIS WDG使用静态配置和动态管理将其功能集成到相关对象中。对象之间的相互调用是通过相关接口实现的。ORIENTAIS WDG设计目标是为了设计一个安全的看门狗管理和实体监督协议栈，遵循ISO26262:2018功能安全所约束条件，目前ORIENTAIS WDG现已通过 TÜV Rheinland的ISO 26262 ASIL D的产品认证。ORIENTAIS WDG的架构如下图所示，其中WdgIf位于板载设备抽象层。

ORIENTAIS WDG integrates its functionalities into relevant objects through static configuration and dynamic management. Inter-object calls are realized via corresponding interfaces. The design goal of ORIENTAIS WDG is to create a secure watchdog and entity supervision protocol stack. It adheres to the conditions constrained by ISO26262:2018 functional safety, and currently, ORIENTAIS WDG has passed the TÜV Rheinland ISO 26262 ASIL D product certification. The architecture of ORIENTAIS WDG is shown in the following diagram, where WdgIf resides in the board-level device abstraction layer.

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/WdgIf/image1.png
   :alt: ORIENTAIS-WDG协议栈软件架构 (ORIENTAIS-WDG Protocol Stack Software Architecture)
   :name: ORIENTAIS-WDG协议栈软件架构 (ORIENTAIS-WDG Protocol Stack Software Architecture)
   :align: center


参考资料 (Reference materials)
------------------------------------------

[1] AUTOSAR_SWS_WatchdogInterface.pdf，R19-11

[2] AUTOSAR_SWS_WatchdogDriver.pdf, R19-11

[3] AUTOSAR_SWS_BSWModeManager.pdf, R19-11

[4] AUTOSAR_SWS_DefaultErrorTracer.pdf, R19-11

功能描述 (Function Description)
===========================================

WdgIf功能 (WdgIf Function)
----------------------------------------

WdgIf功能介绍 (Function Introduction for WdgIf)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

WdgIf模块为Watchdog看门狗协议栈的中间层，提供了对底层看门狗驱动程序的服务的统一访问，如模式切换和设置触发条件。Watchdog结构层次如下图所示。 (The WdgIf module serves as the middle layer for the Watchdog watchdog protocol stack, providing unified access to services of underlying watchdog drivers, such as mode switching and setting trigger conditions. The structure hierarchy of the Watchdog is shown in the following figure.)

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/WdgIf/image2.png
   :alt: Watchdog层次结构图(Diagram Watchdog Hierarchy)
   :name: Watchdog层次结构图(Diagram Watchdog Hierarchy)
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

WdgIf功能实现 (WdgIf functionality implementation)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

WdgIf实现WdgM对多Watchdog Driver的管理，将WdgM的指令下发到对应的Watchdog Driver。

WdgIf implements the management of multiple Watchdog Drivers, sending WdgM instructions to the corresponding Watchdog Driver.

WdgIf接口不能为Wdg Driver增加功能。除此之外，WdgIf不会从看门狗属性中抽象出来，比如看门狗模式切换或者设置窗口模式以及超时时间等，其不隐藏底层看门狗驱动程序和看门狗硬件的任何功能。

The WdgIf interface cannot add functionality to the Wdg Driver. Additionally, WdgIf does not abstract away any watchdog properties such as switching watchdog modes, setting window mode, or timeout values; it does not hide any functionalities of the underlying watchdog driver or hardware.

源文件描述 (Source file description)
===============================================

.. centered:: **表 WdgIf组件文件描述 (Description of WdgIf Component File)**

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 文件 (Files)
     - 说明 (Description)
   * - WdgIf.c
     - WdgIf源文件 (Source File)
   * - WdgIf.h
     - WdgIf头文件 (WdgIf header file)
   * - WdgIf.MemMep.h
     - WdgIf的内存映射定义 (The memory-mapped definition of WdgIf)
   * - WdgIf\_Types.h
     - WdgIf的数据类型定义 (The data types definition of WdgIf)




.. figure:: ../../_static/参考手册(Module_Reference_Manual)/WdgIf/image3.png
   :alt: WdgIf组件文件交互关系图 (WdgIf Component File Interaction Diagram)
   :name: WdgIf组件文件交互关系图 (WdgIf Component File Interaction Diagram)
   :align: center


API接口 (API Interface)
=====================================

类型定义 (Type definition)
--------------------------------------

WdgIf_ModeType类型定义 (WdgIf_ModeType Type Definition)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 名称 (Name)
     - WdgIf_ModeType
   * - 类型 (Type)
     - Enumeration
   * - 范围 (Range)
     - WDGIF_OFF_MODE = 0
   * - 
     - WDGIF_SLOW_MODE = 1
   * - 
     - WDGIF_FAST_MODE = 2
   * - 描述 (Description)
     - 用于WdgIf模块内部模式切换的数据类型 (Data types for mode switching within the WdgIf module)




输入函数描述 (Describe the input function:)
-----------------------------------------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 输入模块 (Input Module)
     - API
   * - Wdg
     - Wdg_SetMode
   * - Wdg
     - Wdg_SetTriggerCondition
   * - Det
     - Det_ReportError




静态接口函数定义 (Static interface function definition)
---------------------------------------------------------------

WdgIf_SetMode函数定义 (The WdgIf_SetMode function defines)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - WdgIf_SetMode
     - 
     - 
   * - 函数原型： (Function prototype:)
     - Std_ReturnType WdgIf_SetMode
     - 
     - 
   * - 
     - (
     - 
     - 
   * - 
     - uint8 DeviceIndex,
     - 
     - 
   * - 
     - WdgIf_ModeType WdgMode
     - 
     - 
   * - 
     - );
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x01
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
     - DeviceIndex：看门狗驱动程序实例的标识符索引 (DeviceIndex：Identifier index of the watchdog driver instance)
     - 值域： (Domain:)
     - 0-255
   * - 
     - WdgMode：看门狗驱动程序的模式 (WdgMode：Watchdog driver mode)
     - 值域： (Domain:)
     - WDGIF_OFF_MODEWDGIF_SLOW_MODE
   * - 
     - 
     - 
     - WDGIF_FAST_MODE
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无
     - 
     - 
   * - 返回值： (Return Value:)
     - E_OK：API接口请求成功 (E_OK: API interface request successful)
     - 
     - 
   * - 
     - E_NOT_OK：API接口请求失败 (E_NOT_OK: API interface request failed)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 将服务API接口WdgIf_SetMode映射到相应的看门狗驱动程序的服务Wdg_SetMode (Map the service API interface WdgIf_SetMode to the corresponding watchdog driver service Wdg_SetMode.)
     - 
     - 




WdgIf_SetTriggerCondition函数定义 (The WdgIf_SetTriggerCondition function defines)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - WdgIf_SetTriggerCondition
     - 
     - 
   * - 函数原型： (Function prototype:)
     - void WdgIf_SetTriggerCondition
     - 
     - 
   * - 
     - (
     - 
     - 
   * - 
     - uint8 DeviceIndex,
     - 
     - 
   * - 
     - uint16 Timeout
     - 
     - 
   * - 
     - );
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
     - DeviceIndex：看门狗驱动程序实例的标识符索引 (DeviceIndex：Identifier index of the watchdog driver instance)
     - 值域： (Domain:)
     - 0-255
   * - 
     - Timeout：设置触发计数器的超时时间值 (Timeout：Set the timeout value for triggering the counter)
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
     - 无
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 将服务API接口WdgIf_SetTriggerCondition映射到相应的看门狗驱动程序的服务Wdg_SetTriggerCondition (Map the service API interface WdgIf_SetTriggerCondition to the corresponding watchdog driver service Wdg_SetTriggerCondition.)
     - 
     - 




WdgIf_GetVersionInfo函数定义 (The WdgIf_GetVersionInfo function definition)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - WdgIf_GetVersionInfo
     - 
     - 
   * - 函数原型： (Function prototype:)
     - void WdgIf_GetVersionInfo
     - 
     - 
   * - 
     - (
     - 
     - 
   * - 
     - Std_VersionInfoType \*versioninfo
     - 
     - 
   * - 
     - );
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
     - 获取WdgIf模块版本信息。需宏开启该功能 (Get version information of the WdgIf module. This feature requires a macro to be enabled.)
     - 
     - 




可配置函数定义 (Configurable Function Definition)
----------------------------------------------------------

TriggerConditionFunction函数定义 (TriggerConditionFunction function definition)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - TriggerConditionFunction
     - 
     - 
   * - 函数原型： (Function prototype:)
     - void TriggerConditionFunction
     - 
     - 
   * - 
     - (
     - 
     - 
   * - 
     - uint8 DeviceIndex,
     - 
     - 
   * - 
     - uint16 Timeout
     - 
     - 
   * - 
     - );
     - 
     - 
   * - 服务编号： (Service Number:)
     - 无
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
     - DeviceIndex：看门狗驱动程序实例的标识符索引 (DeviceIndex：Identifier index of the watchdog driver instance)
     - 值域： (Domain:)
     - 0-255
   * - 
     - Timeout：设置触发计数器的超时时间值 (Timeout：Set the timeout value for triggering the counter)
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
     - 无
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 用于设置触发器计数器的超时值(毫秒)，可能不用于外部看门狗设备 (Timeout value (ms) for setting trigger counter, may not be used for external watchdog devices)
     - 
     - 




SetModeFunction函数定义 (SetModeFunction function definition)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - SetModeFunction
     - 
     - 
   * - 函数原型： (Function prototype:)
     - Std_ReturnTypeSetModeFunction
     - 
     - 
   * - 
     - (
     - 
     - 
   * - 
     - uint8 DeviceIndex,
     - 
     - 
   * - 
     - WdgIf_ModeType WdgMode
     - 
     - 
   * - 
     - );
     - 
     - 
   * - 服务编号： (Service Number:)
     - 无
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
     - DeviceIndex：看门狗驱动程序实例的标识符索引 (DeviceIndex：Identifier index of the watchdog driver instance)
     - 值域： (Domain:)
     - 0-255
   * - 
     - WdgMode：看门狗驱动程序的模式 (WdgMode：Watchdog driver mode)
     - 值域： (Domain:)
     - WDGIF_OFF_MODEWDGIF_SLOW_MODE
   * - 
     - 
     - 
     - WDGIF_FAST_MODE
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无
     - 
     - 
   * - 返回值： (Return Value:)
     - E_OK：API接口请求成功 (E_OK: API interface request successful)
     - 
     - 
   * - 
     - E_NOT_OK：API接口请求失败 (E_NOT_OK: API interface request failed)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 用于设置看门狗的工作模式，包括WDGIF_OFF_MODE、 (To set the watchdog operation mode, including WDGIF_OFF_MODE,)
     - 
     - 
   * - 
     - WDGIF_FAST_MODE和WDGIF_SLOW_MODE。对于外部看门狗设备，WDGIF_FAST_MODE和WDGIF_SLOW_MODE可能合并为正常模式。 (WDGIF_FAST_MODE and WDGIF_SLOW_MODE. For external watchdog devices, WDGIF_FAST_MODE and WDGIF_SLOW_MODE may be combined into normal mode.)
     - 
     - 




配置 (Configure)
==============================

WdgIfGeneral配置 (WdgIfGeneral Configuration)
-----------------------------------------------------------

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/WdgIf/image4.png
   :alt: WdgIf模块的General容器配置图 (The General container configuration diagram of WdgIf module)
   :name: WdgIf模块的General容器配置图 (The General container configuration diagram of WdgIf module)
   :align: center


.. centered:: **表 WdgIf模块的General容器配置表 (Table for General Container Configuration of WdgIf Module)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - WdgIfDevErrorDetect
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
   * - WdgIfVersionInfoApi
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
   * - WdgIfHeaderFileInclusion
     - 取值范围 (Range)
     - 下拉选项或勾选 (Dropdown options or check boxes)
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 包含所用C回调声明的WdgIf模块所包含的头文件名称 (Name of the header file that includes the C callback declarations in the WdgIf module)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 依赖于Wdg驱动程序模块的配置 (Dependent on the configuration of the Wdg Driver Module)
     - 
     - 




WdgIfInternalDevice配置 (Configurations of WdgIfInternalDevice)
-----------------------------------------------------------------------------

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/WdgIf/image5.png
   :alt: WdgIf模块内部看门狗设备的配置图 (The configuration diagram of the WdgIf module internal watchdog device)
   :name: WdgIf模块内部看门狗设备的配置图 (The configuration diagram of the WdgIf module internal watchdog device)
   :align: center


.. centered:: **表 WdgIf模块内部看门狗设备的配置表 (Table for Configuration of Watchdog Device within Module WdgIf)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - WdgIfDeviceIndex
     - 取值范围 (Range)
     - 0…65535
     - 默认取值 (Default value)
     - 0
   * -
     - 参数描述 (Parameter Description)
     - 表示看门狗接口ID，以便被看门狗管理器引用 (Indicate watchdog interface ID for reference by the watchdog manager)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 依赖于Wdg驱动程序的配置 (Dependent on Wdg driver configuration)
     - 
     - 
   * - TriggerConditionFunction
     - 取值范围 (Range)
     - 字符串（函数名称） (String (function name))
     - 默认取值 (Default value)
     - NULL_PTR
   * - 
     - 参数描述 (Parameter Description)
     - 该参数是用于设置触发器计数器的超时值(毫秒)，可能不用于外部看门狗设备 (This parameter is used to set the timeout value (in milliseconds) for the trigger counter, and may not be applicable for external watchdog devices.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 依赖于Wdg驱动程序的配置 (Dependent on Wdg driver configuration)
     - 
     - 
   * - SetModeFunction
     - 取值范围 (Range)
     - 字符串（函数名称） (String (function name))
     - 默认取值 (Default value)
     - NULL_PTR
   * - 
     - 参数描述 (Parameter Description)
     - 该参数为看门狗模式，包括WDGIF_OFF_MODE(0)、WDGIF_FAST_MODE(1)和WDGIF_SLOW_MODE(2)。对于外部看门狗设备，WDGIF_FAST_MODE和WDGIF_SLOW_MODE可能合并为正常模式
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 依赖于Wdg驱动程序的配置 (Dependent on Wdg driver configuration)
     - 
     - 
   * - WdgIfDriverRef
     - 取值范围 (Range)
     - 下拉选项或引用 (Dropdown options or citation)
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 引用底层设备Wdg驱动程序的索引 (Reference index of underlying device Wdg driver program)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 依赖于Wdg驱动程序的配置 (Dependent on Wdg driver configuration)
     - 
     - 




WdgIfExternalDevice配置 (Configuration of WdgIfExternalDevice)
----------------------------------------------------------------------------

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/WdgIf/image6.png
   :alt: WdgIf模块外部看门狗设备的配置图 (Configuration diagram of the WdgIf Module External Watchdog Device)
   :name: WdgIf模块外部看门狗设备的配置图 (Configuration diagram of the WdgIf Module External Watchdog Device)
   :align: center


.. centered:: **表 WdgIf模块外部看门狗设备的配置表 (Table for External Watchdog Device Configuration of WdgIf Module)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - WdgIfDeviceIndex
     - 取值范围 (Range)
     - 0…65535
     - 默认取值 (Default value)
     - 0
   * -
     - 参数描述 (Parameter Description)
     - 表示看门狗接口ID，以便被看门狗管理器引用 (Indicate watchdog interface ID for reference by the watchdog manager)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 依赖于Wdg驱动程序的配置 (Dependent on Wdg driver configuration)
     - 
     - 
   * - TriggerConditionFunction
     - 取值范围 (Range)
     - 字符串（函数名称） (String (function name))
     - 默认取值 (Default value)
     - NULL_PTR
   * - 
     - 参数描述 (Parameter Description)
     - 该参数是用于设置触发器计数器的超时值(毫秒)，可能不用于外部看门狗设备 (This parameter is used to set the timeout value (in milliseconds) for the trigger counter, and may not be applicable for external watchdog devices.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 依赖于Wdg驱动程序的配置 (Dependent on Wdg driver configuration)
     - 
     - 
   * - SetModeFunction
     - 取值范围 (Range)
     - 字符串（函数名称） (String (function name))
     - 默认取值 (Default value)
     - NULL_PTR
   * - 
     - 参数描述 (Parameter Description)
     - 该参数为看门狗模式，包括WDGIF_OFF_MODE(0)、WDGIF_FAST_MODE(1)和WDGIF_SLOW_MODE(2)。对于外部看门狗设备，WDGIF_FAST_MODE和WDGIF_SLOW_MODE可能合并为正常模式
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 依赖于Wdg驱动程序的配置 (Dependent on Wdg driver configuration)
     - 
     - 
