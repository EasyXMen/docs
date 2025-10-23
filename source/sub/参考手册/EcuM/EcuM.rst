===================
EcuM
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
   * - 2024/11/20
     - Jian.Jiang
     - V0.1
     - 发布（Release）
     - 首次发布（First release）
   * - 2025/04/04
     - Jian.Jiang
     - V1.0
     - 发布（Release）
     - 正式发布（Official release）

参考文档（Reference Document）
----------------------------------

.. list-table::
   :widths: 10 15 25 10
   :header-rows: 1

   * - 编号（Number）
     - 分类（Classification）
     - 标题（Title）
     - 版本（Version）
   * - 1
     - Autosar
     - AUTOSAR_CP_EXP_ModeManagementGuide.pdf
     - R23-11
   * - 2
     - Autosar
     - AUTOSAR_CP_SRS_ModeManagement.pdf
     - R23-11 
   * - 3
     - Autosar
     - AUTOSAR_CP_SWS_ECUStateManager.pdf
     - R23-11 


术语与简写（Terms and Abbreviations）
========================================


术语（Term）
--------------------------
   .. :align: center   表格内容居中

.. list-table::
   :widths: 10 40
   :header-rows: 1

   * - 术语（Term）
     - 解释（Explanation）

   * - Mode
     - 模式是车辆中运行的各种状态机（不仅仅是 ECU 管理器）的一组特定状态，与特定实体、应用程序或整个车辆相关
       
       A mode is a set of specific states of various state machines (not just the ECU manager) running in the vehicle, which is related to a specific entity, application, or the entire vehicle.

   * - Phase
     - ECU 管理器操作和事件的逻辑或时间组合，例如启动、启动、关闭、休眠……阶段可以由子阶段组成，如果子阶段主要存在以将执行的操作序列分组为逻辑单元，则通常称为序列。
       
       A logical or temporal combination of ECU manager operations and events, such as startup, boot, shutdown, sleep... A phase can consist of sub - phases, and if a sub - phase mainly exists to group the sequence of operations performed into logical units, it is usually called a sequence.

   * - Shutdown Target
     - 在 ECU 进入休眠状态、断电或重置之前，必须将其关闭。因此，SLEEP、OFF 和 RESET 是有效的关闭目标。通过选择关闭目标，应用程序可以将其对下次关闭后 ECU 行为的期望传达给 ECU 管理器模块。
       
       Before the ECU enters the sleep state, powers off, or resets, it must be shut down. Therefore, SLEEP, OFF, and RESET are valid shutdown targets. By selecting a shutdown target, the application can convey its expectations for the ECU's behavior after the next shutdown to the ECU manager module.

   * - Phase
     - ECU 管理器操作和事件的逻辑或时间组合，例如启动、启动、关闭、休眠……阶段可以由子阶段组成，如果子阶段主要存在以将执行的操作序列分组为逻辑单元，则通常称为序列。
       
       A logical or temporal combination of ECU manager operations and events, such as startup, boot, shutdown, sleep... A phase can consist of sub - phases, and if a sub - phase mainly exists to group the sequence of operations performed into logical units, it is usually called a sequence.

   * - Wakeup Event
     - 导致唤醒的物理事件。CAN 消息或切换 IO 线可以是唤醒事件。同样，内部 SW 表示（例如中断）也可以称为唤醒事件。
       
       A physical event that causes wakeup. A CAN message or a switched IO line can be a wakeup event. Similarly, an internal software representation (such as an interrupt) can also be called a wakeup event.

   * - Wakeup Reason
     - 导致唤醒的物理事件。CAN 消息或切换 IO 线可以是唤醒事件。同样，内部 SW 表示（例如中断）也可以称为唤醒事件。   
       
       A physical event that causes wakeup. A CAN message or a switched IO line can be a wakeup event. Similarly, an internal software representation (such as an interrupt) can also be called a wakeup event.
  

简写（Abbreviation）
-------------------------

.. list-table::
   :widths: 15 20 25
   :header-rows: 1


   * - 简写（Abbreviation）
     - 全称（Full name）
     - 解释（Explanation）

   * - BswM
     - Basic Software Mode Manager
     - 基础软件模式管理器

   * - Dem
     - Diagnostic Event Manager
     - 诊断事件管理器

   * - Det
     - Default Error Tracer
     - 默认错误追踪器

   * - Mcu
     - Microcontroller Unit
     - 微控制器单元

   * - Os
     - Operating System
     - 操作系统


简介（Introduction）
==============================

EcuM主要用于管理ECU状态的模块，它管理ECU的运行状态，并控制ECU的启动、关闭、休眠、唤醒等操作。具体来说，EcuM模块主要完成以下功能：

EcuM is a module mainly used to manage the ECU state. It manages the operating state of the ECU and controls operations such as ECU startup, shutdown, sleep, and wake - up. Specifically, the EcuM module mainly accomplishes the following functions:

   * 初始化和取消初始化OS、SchM和BswM以及一些基本软件驱动模块。
   
     Initialize and deinitialize the OS, SchM, BswM, and some basic software driver modules.

   * 根据请求将 ECU 配置为休眠和关机。

     Configure the ECU to sleep and shut down according to requests.

   * 管理 ECU 上的所有唤醒事件。

     Manage all wake - up events on the ECU.

.. figure:: ../../../_static/参考手册/EcuM/EcuM层次图.png
   :alt: EcuM模块层次图
   :name: fig_EcuMarch
   :align: center

   EcuM层次图

   EcuM Hierarchy Diagram


如图 :ref:`fig_EcuMarch` 所示，EcuM模块处于AUTOSAR架构中的系统服务层，它与 SchM、BswM、Os、Mcu 等模块直接相连，与这些模块结合起来，完成ECU的启动、关闭、休眠等操作。

As shown in Figure :ref:`fig_EcuMarch`, the EcuM module is located in the system service layer of the AUTOSAR architecture. It is directly connected to modules such as SchM, BswM, Os, and Mcu, and works together with these modules to complete operations such as ECU startup, shutdown, and sleep.


功能描述（Functional Description）
==========================================

模块初始化功能（Module Initialization Function）
-----------------------------------------------------------

模块初始化功能介绍（Introduction to Module Initialization Function）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
上电时，EcuM负责基础软件模块(包含MCAL)的初始化（结合BswM），然后启动Os。

When powered on, EcuM is responsible for initializing the basic software modules (including MCAL) (in conjunction with BswM) and then starting the Os.


模块初始化功能集成（Integration of Module Initialization Function）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
针对模块初始化工作需要通过EcuM配置实现，初始化列表中的项限定于Autosar中的模块注1 初始化
列表分为EcuMDriverInitListZero、EcuMDriverInitListOne、EcuMDriverRestartList；其中
EcuMDriverInitListZero与EcuMDriverInitListOne两者都在Os启动前进行初始化，意味这这些
模块的初始化不能使用Os的任何接口，其中EcuMDriverInitListZero不能使用Post-build为配置
参数的模块初始化；两者的初始化列表示例如下图

The module initialization work needs to be implemented through EcuM configuration. The items in the initialization list are limited to the modules specified in Autosar [Note 1]. The initialization lists are divided into EcuMDriverInitListZero, EcuMDriverInitListOne, and EcuMDriverRestartList; among them, both EcuMDriverInitListZero and EcuMDriverInitListOne are initialized before the Os starts, which means that the initialization of these modules cannot use any interfaces of the Os. Besides, EcuMDriverInitListZero cannot use the module initialization with Post-build as configuration parameters. Examples of the initialization lists of the two are as shown in the following figure.

  .. figure:: ../../../_static/参考手册/EcuM/DriverInitialization.png
     :alt: EcuM模块初始化列表
     :name: fig_EcuM00
     :align: center

     DriverInitialization


睡眠唤醒功能（Sleep/Wake-up Function）
------------------------------------------------------------

睡眠唤醒功能介绍（Introduction to Sleep/Wake-up Function）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

对于车机系统中，休眠唤醒是最常见的功能，也是AutoSar中最基础的功能，它主要完成ECU的休眠、唤醒等操作。
在AUTOSAR中，休眠唤醒主要通过EcuM来配置实现的。ECU一般休眠方式有三种：

In the in-vehicle system, sleep and wake-up is the most common function and also the most basic function in AutoSar, which mainly completes operations such as ECU sleep and wake-up.
In AUTOSAR, sleep and wake-up are mainly configured and implemented through EcuM. There are generally three ECU sleep modes:

   * Mcu休眠，EcuM进入Halt模式，通过外设中断唤醒；
  
     Mcu sleep: EcuM enters Halt mode and is woken up by a peripheral interrupt;

   * Mcu处于低功耗，还能运行简单循环逻辑，EcuM进入Poll模式，通过外设中断唤醒或周期事件唤醒；

     Mcu is in low power consumption and can still run simple loop logic: EcuM enters Poll mode and is woken up by a peripheral interrupt or a periodic event;

   * Mcu掉电，由外部设备检测到唤醒事件直接给Mcu供电

     Mcu power-off: An external device detects a wake-up event and directly supplies power to the Mcu.

Sleep Phase
**************

上述前两个方式在EcuM中属于SLEEP阶段，都是通过控制Mcu进入低功耗模式来使Mcu暂停，
需要调用EcuM的API: EcuM_GoDownHaltPoll来进入，对应的处理流程如下图

The first two modes mentioned above belong to the SLEEP phase in EcuM, which make the Mcu pause by controlling it to enter a low-power mode.
It is necessary to call EcuM's API: EcuM_GoDownHaltPoll to enter, and the corresponding processing flow is as shown in the following figure.

  .. figure:: ../../../_static/参考手册/EcuM/SLEEPPhaseGeneral.png
    :alt: EcuM模块休眠流程
    :name: fig_EcuM01
    :align: center

    Sleep Phase General

其中GoSleep Sequence 解析流程如下图：

The parsing process of the GoSleep Sequence is shown in the following figure:

  .. figure:: ../../../_static/参考手册/EcuM/EcuMGoSleepSequence.png
    :alt: GoSleep Sequence
    :name: fig_EcuM02
    :align: center

    EcuM Go Sleep Sequence

Shutdown Phase
**************************

对于Mcu掉电，在EcuM中处于Shutdown阶段，有BswM执行相应逻辑后进入该阶段，对应的处理流程如下图：

For the Mcu power-off, it is in the Shutdown phase in EcuM. This phase is entered after BswM executes the corresponding logic, and the corresponding processing flow is as shown in the following figure: 

  .. figure:: ../../../_static/参考手册/EcuM/ShutdownPhaseGeneral.png
    :alt: EcuM Shutdown Phase
    :name: fig_EcuM03
    :align: center

    Shutdown Phase General

流程中的OffPreOS Sequence分解后如下图：

The decomposed OffPreOS Sequence in the flow is as shown in the following figure:

  .. figure:: ../../../_static/参考手册/EcuM/OffPreOSSequence.png
    :alt: OffPreOS Sequence
    :name: fig_EcuM04
    :align: center

    Off PreOS Sequence

流程中的OffPostOS Sequence分解后如下图：

The decomposed OffPostOS Sequence in the flow is as shown in the following figure:

  .. figure:: ../../../_static/参考手册/EcuM/OffPostOSSequence.png
    :alt: OffPostOS Sequence
    :name: fig_EcuM05
    :align: center

    Off PostOS Sequence

唤醒以及验证流程（Wake-up and Verification Process）
***********************************************************

在EcuM中对于每个唤醒源Wakeup Source的状态与对应的描述如下表所示：

In EcuM, the status and corresponding descriptions of each wake-up source (Wakeup Source) are as shown in the following table:

  .. list-table:: 
     :widths: 10 30
     :header-rows: 1

     * - 唤醒源状态（Wake-up Source Status）
       - 状态描述（Status Description）

     * - NONE
       - 唤醒事件未检测到，或者已经被清除
         
         No wake-up event detected, or it has been cleared

     * - PENDING
       - 唤醒事件检测到，但是还未验证
         
         Wake-up event detected, but not yet verified

     * - VALIDATED
       - 唤醒事件检测到，并且已经验证成功
         
         Wake-up event detected and successfully verified

     * - EXPIRED
       - 唤醒事件检测到，但是已经校验超时
         
         Wake-up event detected, but verification has timed out

以上唤醒状态转换流程如下图：

The above wake-up status transition process is shown in the following figure:

  .. figure:: ../../../_static/参考手册/EcuM/WakeupSourceStatus.png
    :alt: EcuM Wakeup Source Status
    :name: fig_EcuM06
    :align: center

    Wakeup Source Status

以上状态的变化通过API(BswM_EcuM_CurrentWakeup)来通知BswM, BswM可以通过收到的通知来做一些其他的逻辑操作（通过集成配置实现）。

The changes in the above states are notified to BswM through the API (BswM_EcuM_CurrentWakeup). BswM can perform some other logical operations based on the received notifications (implemented through integrated configuration).

ECU 管理器模块最多可以管理 32 个唤醒源，每个唤醒源占32位数据的1位，其中有5个为系统默认如下表所示：

The ECU Manager module can manage a maximum of 32 wake-up sources, with each wake-up source occupying 1 bit of a 32-bit data. Among them, 5 are system defaults as shown in the following table:

  .. list-table:: 
     :widths: 10 30 30
     :header-rows: 1

     * - 唤醒源（Wake-up Sources）
       - 唤醒源的值 （Value of Wake-up Source）
       - 描述（Description）

     * - ECUM_WKSOURCE_POWER
       - 0x01
       - 电源循环（位 0）
         
         Power cycle (bit 0)

     * - ECUM_WKSOURCE_RESET
       - 0x02
       - 硬件复位（位 1）。如果 Mcu 驱动程序无法区分电源循环和复位原因，则这应为默认唤醒源。
         
         Hardware reset (bit 1). If the Mcu driver cannot distinguish between power cycles and reset causes, this shall be the default wake-up source.

     * - ECUM_WKSOURCE_INTERNAL_RESET
       - 0x04
       - µC 的内部复位（位 2） 内部复位通常仅复位 µC 核心，而不会复位外设或内存控制器。确切的行为取决于硬件。此源也可能表示未处理的异常。
         
         Internal reset of the µC (bit 2). Internal reset usually only resets the µC core, not peripherals or memory controllers. The exact behavior depends on the hardware. This source may also indicate an unhandled exception.

     * - ECUM_WKSOURCE_INTERNAL_WDG
       - 0x08
       - 由内部看门狗复位（位 3）
         
         Reset by internal watchdog (bit 3)

     * - ECUM_WKSOURCE_EXTERNAL_WDG
       - 0x10
       - 如果硬件支持检测，则由外部看门狗（位 4）复位
         
         Reset by external watchdog if hardware supports detection (bit 4)

EcuM可以通过配置来EcuMCheckWakeupTimeout、EcuMValidationTimeout来使能唤醒验证，唤醒验证流程序列图如下图：

EcuM can enable wake-up verification by configuring EcuMCheckWakeupTimeout and EcuMValidationTimeout. The sequence diagram of the wake-up verification process is as shown in the following figure:

  .. figure:: ../../../_static/参考手册/EcuM/WakeupValidationSequence.png
    :alt: EcuM Wakeup Validation Sequence
    :name: fig_EcuM07
    :align: center

    Wakeup Validation Sequence


睡眠唤醒功能实现（Implementation of Sleep/Wake-up Function）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

EcuM 管理器模块提供以下接口来确定这些唤醒源的状态：

The EcuM manager module provides the following interfaces to determine the status of these wake-up sources:

  * EcuM_GetPendingWakeupEvents 
  * EcuM_GetValidatedWakeupEvents 
  * EcuM_GetExpiredWakeupEvents

EcuM通过以下接口操纵唤醒源的状态 : 

EcuM manipulates the status of wake-up sources through the following interfaces:

  * EcuM_ClearWakeupEvent 
  * EcuM_SetWakeupEvent 
  * EcuM_ValidateWakeupEvent 
  * EcuM_CheckWakeup 
  * EcuM_DisableWakeupSources 
  * EcuM_EnableWakeupSources 
  * EcuM_StartWakeupSources 
  * EcuM_StopWakeupSources

多核（Multi-core）
-----------------------------------------------

在多核架构中，EcuM必须在每个核心存在一个实例。有一个指定的主核心，其中引导加载
程序通过 EcuM_Init 启动主EcuM。主EcuM启动一些驱动程序，确定构建后配置，并启动
所有剩余核心及其所有从EcuM。每个 EcuM 现在启动核心本地操作系统和所有核心本地BswM。
多核架构中，EcuM的分部如下图所示：

In a multi-core architecture, the EcuM must have an instance in each core. There is a designated main core, where the boot loader starts the main EcuM through EcuM_Init. The main EcuM starts some drivers, determines the post-build configuration, and starts all remaining cores and all their slave EcuMs. Each EcuM now starts the core-local operating system and all core-local BswMs.
The distribution of EcuM in the multi-core architecture is shown in the following figure:

  .. figure:: ../../../_static/参考手册/EcuM/MultiCore.png
    :alt: EcuM 多核分布
    :name: fig_EcuM08
    :align: center

    Multi Core

EcuM 模式处理（EcuM Mode Handling）
---------------------------------------------------------

ECU 状态管理器为 SW-C 提供接口，以便选择性地请求和释放模式 RUN 和 POST_RUN。
EcuMFlex 仲裁 SW-C 发出的请求和释放，并将结果传播给 BswM。EcuM 和 BswM 之间
的合作是必要的，因为只有 BswM 才能决定何时转换到不同的模式。由于 EcuM 没有自己
的状态机，EcuM 依赖于 BswM 进行的状态转换。因此，EcuM 不请求状态。此外，它会通
知 BswM 所有请求的当前仲裁情况。当 RTE 执行了属于某种模式的所有 Runnable 时，
BswM 会收到通知。如图所示EcuM模式处理机构。

The ECU State Manager provides interfaces for SW-C to selectively request and release the RUN and POST_RUN modes.
EcuMFlex arbitrates the requests and releases issued by SW-C and propagates the results to BswM. Cooperation between EcuM and BswM is necessary because only BswM can decide when to transition to a different mode. Since EcuM does not have its own state machine, it relies on state transitions performed by BswM. Therefore, EcuM does not request states. Furthermore, it notifies BswM of the current arbitration status of all requests. When the RTE has executed all Runnables belonging to a certain mode, BswM will be notified. The EcuM mode handling mechanism is as shown in the figure.

  .. figure:: ../../../_static/参考手册/EcuM/ModeHandling.png
    :alt: EcuM 模式处理
    :name: fig_EcuM09
    :align: center

    Mode Handling

.. only:: doc_pbs

  变体（Variants）
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  - 支持OS启动后支持模块初始化
  
    Support module initialization after OS startup
  
  - 支持唤醒源配置
  
    Support wake-up source configuration

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
   
   * - EcuM.h
     - PB配置数据结构，以及外部接口声明
       
       PB configuration data structure and external interface declarations

   * - EcuM_Cbk.h
     - EcuM回调函数声明
       
       EcuM callback function declarations

   * - EcuM_Externals.h
     - EcuM模块中所有callout函数声明
       
       Declarations of all callout functions in the EcuM module

   * - EcuM_Internal.h
     - 定义所有内部数据结构，以及内部接口声明
       
       Defines all internal data structures and internal interface declarations

   * - EcuM_MemMap.h
     - EcuM代码、变量所用的MemMap段
       
       MemMap segments used by EcuM code and variables

   * - EcuM_Types.h
     - EcuM通用宏定义以及类型定义
       
       EcuM general macro definitions and type definitions

   * - EcuM.c
     - RUN/POST_RUN 仲裁、EcuM通用函数定义
       
       RUN/POST_RUN arbitration and EcuM general function definitions

   * - EcuM_AlarmClock.c
     - 包含当alarm存在时，设置alarm的API集合
       
       Contains a collection of APIs for setting alarms when alarms exist

   * - EcuM_Shutdown.c
     - 所有SHUTDOWN阶段API定义
       
       All SHUTDOWN phase API definitions

   * - EcuM_Sleep.c
     - 所有SLEEP阶段API定义
       
       All SLEEP phase API definitions

   * - EcuM_StartUp.c
     - 所有STARTUP阶段API定义
       
       All STARTUP phase API definitions

   * - EcuM_Up.c
     - 所有UP阶段API定义
       
       All UP phase API definitions

动态文件（Dynamic Files）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - 文件（File）
     - 描述（Description）
   
   * - EcuM_Callout_Stubs.c
     - EcuM callout函数定义
       
       EcuM callout function definitions

   * - EcuM_Cfg.c
     - EcuM 的配置参数 
       
       Configuration parameters of EcuM

   * - EcuM_Cfg.h
     - 一些控制宏以及宏参数定义
       
       Some control macros and macro parameter definitions

   * - EcuM_Generated_Types.h
     - 依赖配置生成的宏定义、数据结构等
       
       Configuration-dependent generated macro definitions, data structures, etc.

   * - EcuM_Lcfg.c
     - 定义链接配置运行时变量以及内部接口定义
       
       Defines link configuration runtime variables and internal interface definitions

   * - EcuM_PBcfg.c
     - Post-Build 配置参数定义
       
       Post-Build configuration parameter definitions

   * - EcuM_PBcfg.h
     - 全局Post-Build 配置参数声明
       
       Global Post-Build configuration parameter declarations

   * - Rte_EcuM_Type.h
     - 外部参数类型定义
       
       External parameter type definitions

   * - SchM_EcuM.h
     - 定义关键区域保护以及mainfunction声明
       
       Defines critical section protection and main function declarations


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

   * - ECUM_E_UNINIT
     - 0x00
     - A service was called prior to initialization

   * - ECUM_E_SERVICE_DISABLED
     - 0x01
     - A function was called which was disabled by configuration

   * - ECUM_E_NULL_POINTER
     - 0x02
     - A invalid pointer was passed as an argument

   * - ECUM_E_INVALID_PAR
     - 0x03
     - A parameter was invalid (unspecific)

   * - ECUM_E_STATE_PAR_OUT_OF_RANGE
     - 0x04
     - A state, passed as an argument to a service, was out of range (specific parameter test)

   * - ECUM_E_UNKNOWN_WAKEUP_SOURCE
     - 0x05
     - An unknown wakeup source was passed as a parameter to an API

   * - ECUM_E_INIT_FAILED
     - 0x06
     - The initialization failed

   * - ECUM_E_RAM_CHECK_FAILED
     - 0x07
     - The RAM check during wakeup failed

   * - ECUM_E_CONFIGURATION_DATA_INCONSISTENT
     - 0x08
     - Postbuild configuration data is inconsistent

   * - ECUM_E_MULTIPLE_RUN_REQUESTS
     - 0x09
     - On multiple requests by the same ID for requestRun()

   * - ECUM_E_MISMATCHED_RUN_RELEASE
     - 0x10
     - On releasing without a matching request for releaseRun

   * - ECUM_E_CALL_OS_FAILED
     - 0x11
     - Call to OS_Start failed 

   * - ECUM_E_REINIT
     - 0x13
     - Reinit EcuM module


运行时错误（Runtime error）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. list-table:: 
   :widths: 20 10 30
   :header-rows: 1

   * - Error code
     - Value[hex]
     - Description

   * - ECUM_E_WAKEUP_TIMEOUT
     - 0x12
     - After a wake up, no wake up event was set in the given time (see EcuMCheckWakeupTimeout)


.. include:: EcuM_api.rst

配置（configuration）
==================================

初始化其他模块配置（Initialization of Other Module Configurations）
---------------------------------------------------------------------

EcuM初始化其他模块分为三种 EcuMDriverInitListOne, EcuMDriverInitListZero, EcuMDriverInitListBswM, 
前两个是对Mcu以及Mcal以及Det和Dem的初始化，在EcuM初始化时就会被执行，后一个对基础软件的初始化，由BswM模块完成。

EcuM initializes other modules in three types: EcuMDriverInitListOne, EcuMDriverInitListZero, and EcuMDriverInitListBswM. The first two are for initializing Mcu, Mcal, Det, and Dem, which will be executed during EcuM initialization. The last one is for initializing basic software, which is completed by the BswM module.

初始化内容通过配置EcuMDriverInitItem来指定，具体配置说明如下表：

The initialization content is specified by configuring EcuMDriverInitItem, and the specific configuration description is as shown in the following table:

.. list-table:: 
   :widths: 20 30
   :header-rows: 1

   * - UI名称（UI Names）
     - 使用说明（Instructions for Use）

   * - EcuMModuleParameter
     - 配置参数类型， VOID无参数，NULL_PTR传入空指针，POSTBUILD_PTR传对应模块的配置参数指针
       
       The type of configuration parameter. VOID means no parameter, NULL_PTR means passing a null pointer, and POSTBUILD_PTR means passing the configuration parameter pointer of the corresponding module.

   * - EcuMModuleService
     - 指定调用的函数， 例如： Init, PreInit, Start 等函数。
       
       Specify the function to be called, such as: Init, PreInit, Start and other functions.
       
   * - EditModuleService
     - 使能是否可以手动修改配置EcuMModuleService，由用户手动填入服务函数名称。
       
       Enable whether the configuration of EcuMModuleService can be modified manually, and the user manually enters the service function name.

   * - EcuMModulePbConfigName
     - 配置当EcuMModuleParameter选择POSTBUILD_PTR时，对应模块的配置参数名称。
       
       Configure the name of the configuration parameter of the corresponding module when EcuMModuleParameter selects POSTBUILD_PTR.

   * - EditPbConfigName
     - 使能是否可以手动修改配置EcuMModulePbConfigName，由用户手动填入配置参数名称。
       
       Enable whether the configuration of EcuMModulePbConfigName can be modified manually, and the user manually enters the configuration parameter name.

   * - IncludeHeaderFile
     - 配置包含的对应初始化模块的头文件。
       
       Configure the header file of the corresponding initialization module to be included.

   * - EditHeaderFile
     - 使能是否可以手动修改配置IncludeHeaderFile，由用户手动填入配置头文件名称。
       
       Enable whether the configuration of IncludeHeaderFile can be modified manually, and the user manually enters the configuration header file name.

   * - EcuMEcucCoreDefinitionRef
     - 在多核的情况下，配置需要在不同核上初始化的内容，如果一个容器中存在该配置，那么该容器其他的EcuMDriverInitItem都需要配置该项。
       
       In the case of multi-core, configure the content that needs to be initialized on different cores. If this configuration exists in a container, other EcuMDriverInitItems in the container need to be configured with this item.

   * - EcuMModuleRef
     - 在当前工程下配置需要EcuM初始化的模块。
       
       Configure the modules that need to be initialized by EcuM in the current project.


休眠唤醒配置（Sleep/Wake-up Configuration）
-------------------------------------------------

休眠配置（Sleep Configuration）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. 首先配置默认的下电方式，有三种方式： EcuMShutdownTargetOff、EcuMShutdownTargetReset、EcuMShutdownTargetSleep；当配置为EcuMShutdownTargetReset或EcuMShutdownTargetSleep时，就需要配置复位模式或者睡眠模式。具体配置如下图：

   First, configure the default power-off mode. There are three modes: EcuMShutdownTargetOff, EcuMShutdownTargetReset, and EcuMShutdownTargetSleep. When configured as EcuMShutdownTargetReset or EcuMShutdownTargetSleep, it is necessary to configure the reset mode or sleep mode. The specific configuration is as shown in the following figure:

   .. figure:: ../../../_static/参考手册/EcuM/DefaultSleepConfig.png
      :alt: 默认睡眠配置
      :name: fig_EcuM10
      :align: center

      Default Sleep Config

2. 配置休眠模式，通过EcuMSleepModeSuspend配置决定是Halt还是Poll, 配置EcuMSleepModeMcuModeRef选择控制Mcu的模式， 配置EcuMWakeupSourceMask选择在该sleep模式下唤醒的源。具体配置如下图：

   Configure the sleep mode. Determine whether it is Halt or Poll through the EcuMSleepModeSuspend configuration. Configure EcuMSleepModeMcuModeRef to select the mode for controlling the Mcu. Configure EcuMWakeupSourceMask to select the wake-up sources in this sleep mode. The specific configuration is as shown in the following figure:

   .. figure:: ../../../_static/参考手册/EcuM/SleepModeConfig.png
      :alt: 睡眠模式配置
      :name: fig_EcuM11
      :align: center

      Sleep Mode Config

3. 配置复位模式，只需要配置EcuMResetModeId即可，具体配置如下图：

   Configure the reset mode. It is only necessary to configure EcuMResetModeId. The specific configuration is as shown in the following figure:

   .. figure:: ../../../_static/参考手册/EcuM/ResetModeConfig.png
      :alt: 复位模式配置
      :name: fig_EcuM12
      :align: center

      Reset Mode Config


唤醒配置（Wake-up Configuration）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

通过配置EcuMWakeupSource来配置EcuM唤醒源，具体配置如下图：

Configure the EcuM wake-up source by configuring EcuMWakeupSource. The specific configuration is as shown in the following figure:

.. figure:: ../../../_static/参考手册/EcuM/WakeupSourceConfig.png
   :alt: 唤醒源配置
   :name: fig_EcuM13
   :align: center

   Wakeup Source Config

唤醒源配置说明如下表：

The description of the wake-up source configuration is as shown in the following table:

.. list-table:: 
   :widths: 20 30
   :header-rows: 1

   * - UI名称（UI Name）
     - 使用说明（Instructions for Use）

   * - EcuMCheckWakeupTimeout
     - 用于配置唤醒源的检测超时时间，单位为s，默认为0，表示不检测超时
       
       Used to configure the detection timeout period for the wake-up source, in seconds. The default value is 0, indicating that timeout detection is not performed.

   * - EcuMValidationTimeout
     - 用于配置唤醒源的有效验证超时时间，单位为s，默认为0，表示不检测超时
       
       Used to configure the valid validation timeout period for the wake-up source, in seconds. The default value is 0, indicating that timeout detection is not performed.
  
   * - EcuMWakeupSourceId
     - 用户可配置的唤醒源ID，从5起开始配置
       
       User-configurable wake-up source ID, starting from 5.

   * - EcuMWakeupSourcePolling
     - 当此EcuMWakeupSource被EcuMSleepMode->EcuMWakeupSourceMask引用，且EcuMSleepMode->EcuMSleepModeSuspend配置为FALSE（POLL模式），则此项EcuMWakeupSourcePolling应该配置为TRUE，表示以轮询的方式检测唤醒源
       
       When this EcuMWakeupSource is referenced by EcuMSleepMode->EcuMWakeupSourceMask and EcuMSleepMode->EcuMSleepModeSuspend is configured as FALSE (POLL mode), this EcuMWakeupSourcePolling should be configured as TRUE, indicating that the wake-up source is detected in a polling manner.

   * - EcuMComMChannelRef
     - 当配置此项后，当唤醒源检测到后，会调用ComM_EcuM_WakeUpIndication通知EcuMComMChannelRef引用的ComMChannel
       
       After configuring this item, when a wake-up source is detected, ComM_EcuM_WakeUpIndication will be called to notify the ComMChannel referenced by EcuMComMChannelRef.

   * - EcuMComMPNCRef
     - 当配置此项后，当唤醒源检测到后，会调用ComM_EcuM_PNCWakeUpIndication通知EcuMComMPNCRef引用的ComMPnc
       
       After configuring this item, when a wake-up source is detected, ComM_EcuM_PNCWakeUpIndication will be called to notify the ComMPnc referenced by EcuMComMPNCRef.

   * - EcuMResetReasonRef
     - MCU 驱动程序检测到的复位原因到唤醒源的映射
       
       Mapping from the reset reason detected by the MCU driver to the wake-up source.


多核配置（Multi-core Configuration）
----------------------------------------------

系统是属于多核时，需要通过配置EcuMPartitionRef将EcuM也配置成多核，该配置引用的是分区配置，
只能选择每个核中的一个分区来关联。然后需要配置互斥锁供EcuM使用，具体配置如下图：

When the system is multi-core, it is necessary to configure EcuM as multi-core by configuring EcuMPartitionRef. This configuration refers to the partition configuration, and only one partition in each core can be selected for association. Then, it is necessary to configure a mutex for EcuM to use. The specific configuration is as shown in the following figure:

.. figure:: ../../../_static/参考手册/EcuM/PartitionConfig.png
   :alt: 多核配置
   :name: fig_EcuM14
   :align: center

   Partition Config


