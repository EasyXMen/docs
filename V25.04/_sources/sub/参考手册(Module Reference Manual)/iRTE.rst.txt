iRTE
#################################

:strong:`缩写词注解 (Abbreviation Notes):`

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 序号 (Serial Number)
     - 缩略词 (Abbreviations)
     - 英文全名 (Full English Name)
     - 中文解释 (Translate the given Chinese text into English.)
   * - \
     - iRTE
     - i-Soft Runtime Environment
     - 普华基础模块运行时环境 (PricewaterhouseCoopers Basic Module Runtime Environment)
   * - \
     - BSW
     - Basic Software
     - 基础软件 (Basic software)
   * - \
     - BSWMD
     - Basic Software Module Description
     - 基础软件模块描述 (Description of Basic Software Modules)
   * - \
     - ECU
     - Electronic Control Unit
     - 电子控制单元 (Electronic Control Unit)
   * - \
     - AUTOSAR
     - Automotive Open System Architecture
     - 汽车开放系统架构 (Automotive Open Systems Architecture)
   * - \
     - C/S
     - Client-server communication
     - 客户端服务器通信 (Client-server communication)
   * - \
     - ECUC
     - AUTOSAR ECU Configuration
     - AUTOSAR ECU配置 (AUTOSAR ECU Configuration)
   * - \
     - IOC
     - Inter-OsApplication Communication
     - 跨Os应用通信 (Cross-OS application communication)
   * - \
     - API
     - Application Programming Interface
     - 应用程序编程接口 (Application Programming Interface)
   * - \
     - SchM
     - Schedule Manager
     - 调度管理 (Scheduling Management)
         
简介 (Introduction)
=================================

iRte是适配普华BSW实现需求的BSW模块间通信接口层，与应用无交互，主要包括SchM模块。基于ECU为多核BSW架构提供运行时环境：

iRte is the BSW module communication interface layer adapted for the requirements of PuHua BSW, with no interaction with applications, mainly including the SchM module. Based on ECU, it provides a runtime environment for a multi-core BSW architecture:

生成TASK函数，负责映射到Task的周期BswEntity的运行调度；

Generate the TASK function, responsible for mapping to Task's periodic BswEntity scheduling;

提供BSW间C/S通信接口；

Provide BSW inter-C/S communication interface;

为BSW数据一致性保护提供独占区接口；

Provide an exclusive zone interface for preserving data consistency for BSW;

参考资料 (References materials)
---------------------------------

[1] AUTOSAR_TPS_SystemTemplate.pdf，R19-11

[2] AUTOSAR_SWS_RTE.pdf，R19-11

[3] AUTOSAR_EXP_LayeredSoftwareArchitecture.pdf，R19-11

[4] AUTOSAR_TPS_BSWModuleDescriptionTemplate，R19-11

[5] AUTOSAR_SWS_OS.pdf，R19-11

[6] AUTOSAR_TR_Methodology.pdf，R19-11

[7] AUTOSAR_EXP_VFB.pdf，R19-11

[8] AUTOSAR_SWS_COM.pdf，R19-11

[9] AUTOSAR_SWS_LargeDataCOM.pdf，R19-11
         
功能描述 (Function Description)
===========================================

SchM功能描述 (SchM Function Description)
----------------------------------------------------

SchM功能支撑普华BSW的实现，与应用无交互，工程配置、集成时客户无需额外关注。

SchM functionality supports the realization of PuHua BSW and does not interact with applications. Customers do not need additional attention during engineering configuration and integration.

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 功能分类 (Function Classification)
     - 功能点描述 (Feature Description)
   * - 独占区功能 (Exclusive Area Function)
     - 为BSW提供独占区接口，用于数据一致性保护 (Provide exclusive area interfaces for BSW for data consistency protection.)
   * - BswEvent
     - BswTimingEvent：周期事件，激活BSW MainFunction函数 (BswTimingEvent：periodic event, activate BSW MainFunction function)
   * - BswEvent
     - BswBackgroundEvent：不定周期事件 (BswBackgroundEvent：Non-periodic event)
   * - CS通信 (CS Communication)
     - 通信域：同分区，同核不同分区，不同核不同分区 (Communication Domain: Same Zone, Same Core Different Zone, Different Core Different Zone)
   * - CS通信 (CS Communication)
     - 支持CS同步/异步通信 (Support CS Synchronous/Automatic Communication)
   * - MainFunction的调度 (Scheduling of MainFunction)
     - 支持周期TASK，按各BSW模块MainFunction的配置周期进行调度 (Support periodicity for TASK, scheduling based on the configuration cycle of each BSW module's MainFunction.)
   * - 生命周期 (Lifecycle)
     - 支持对每个分区开启/关闭，激活/关闭周期TASK。 (Support enabling/disabling per-partition and activating/deactivating periodic TASKs.)
         
API描述 (API Description)
=======================================

SchM
--------------------

SchM实现AUTOSAR BSW模块MainFunction主函数的调度，为BSW模块提供独占区接口服务，为BSW模块间实现跨分区函数调用提供CS接口。

SchM schedules the MainFunction of AUTOSAR BSW modules, provides exclusive area interface services for BSW modules, and offers CS interfaces for cross-partition function calls between BSW modules.

所有SchM接口均与应用无关，只适配普华BSW的实现逻辑。故只列出实现的接口清单，不对其进行详细描述。

All SchM interfaces are application-independent and are only adapted to the implementation logic of PuHua BSW. Hence, only the list of implemented interfaces is provided without detailed descriptions.

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 功能分类 (Function Classification)
     - 接口名 (Interface Name)
   * - 生成周期函数 (Generate periodic functions)
     - SchM_Init
   * - 生成周期函数 (Generate periodic functions)
     - SchM_Start
   * - 生成周期函数 (Generate periodic functions)
     - SchM_StartTiming
   * - 生成周期函数 (Generate periodic functions)
     - SchM_Deinit
   * - 独占区 (Exclusive Zone)
     - SchM_Enter
   * - 独占区 (Exclusive Zone)
     - SchM_Exit
   * - CS同步通信 (CS Synchronization Communication)
     - SchM_Call
         
iRTE配置 (iRTE Configuration)
===========================================

主要涉及三类配置：

Mainly involves three types of configurations:

通用配置页面：AUTOSAR标准定义的配置项；

General Configuration Page: Configuration items defined by AUTOSAR standards;

iRTE-OS同步配置功能；

iRTE-OS Synchronized Configuration Function;

Update Bswmd All。

其中通用配置页面的内容会被iRTE-OS同步功能填充，一般不需要或进行少量手动调整即可。

The content of the general configuration page will be filled by the iRTE-OS synchronization function, and generally does not require or only requires minimal manual adjustments.

通用配置页面 (General Configuration Page)
---------------------------------------------------

RteOsInteraction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/iRTE/image1.png
   :alt: 通用配置页面-RteOsInteraction (General Configuration Page-RteOsInteraction)
   :name: 通用配置页面-RteOsInteraction (General Configuration Page-RteOsInteraction)
   :align: center


.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 描述 (Description)
     - 描述 (Description)
     - 描述 (Description)
   * - RteExpectedActivationOffset
     - 取值范围 (Range)
     - [0 .. INF]
     - 默认取值 (Default value)
     - 无
   * - RteExpectedActivationOffset
     - 参数描述 (Parameter Description)
     - OsAlarm激活偏移时间（S）
     - OsAlarm激活偏移时间（S）
     - OsAlarm激活偏移时间（S）
   * - RteExpectedActivationOffset
     - 依赖关系 (Dependencies)
     - RteActivationOsAlarmRef关联OsAlarm时才需配置 (RteActivationOsAlarmRef should be configured only when associated with OsAlarm.)
     - RteActivationOsAlarmRef关联OsAlarm时才需配置 (RteActivationOsAlarmRef should be configured only when associated with OsAlarm.)
     - RteActivationOsAlarmRef关联OsAlarm时才需配置 (RteActivationOsAlarmRef should be configured only when associated with OsAlarm.)
   * - RteExpectedTickDuration
     - 取值范围 (Range)
     - [0 .. INF]
     - 默认取值 (Default value)
     - 无
   * - RteExpectedTickDuration
     - 参数描述 (Parameter Description)
     - OsAlarm激活周期（S）
     - OsAlarm激活周期（S）
     - OsAlarm激活周期（S）
   * - RteExpectedTickDuration
     - 依赖关系 (Dependencies)
     - RteActivationOsAlarmRef关联OsAlarm时才需配置 (RteActivationOsAlarmRef should be configured only when associated with OsAlarm.)
     - RteActivationOsAlarmRef关联OsAlarm时才需配置 (RteActivationOsAlarmRef should be configured only when associated with OsAlarm.)
     - RteActivationOsAlarmRef关联OsAlarm时才需配置 (RteActivationOsAlarmRef should be configured only when associated with OsAlarm.)
   * - RteActivationOsAlarmRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - RteActivationOsAlarmRef
     - 参数描述 (Parameter Description)
     - 关联OsAlarm (AssociateOsAlarm)
     - 关联OsAlarm (AssociateOsAlarm)
     - 关联OsAlarm (AssociateOsAlarm)
   * - RteActivationOsAlarmRef
     - 依赖关系 (Dependencies)
     - 依赖于OS模块中OsAlarm的配置 (Dependent on the configuration of OsAlarm in the OS module)
     - 依赖于OS模块中OsAlarm的配置 (Dependent on the configuration of OsAlarm in the OS module)
     - 依赖于OS模块中OsAlarm的配置 (Dependent on the configuration of OsAlarm in the OS module)
   * - RteActivationOsTaskRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - RteActivationOsTaskRef
     - 参数描述 (Parameter Description)
     - 关联OsTask (Associate OsTask)
     - 关联OsTask (Associate OsTask)
     - 关联OsTask (Associate OsTask)
   * - RteActivationOsTaskRef
     - 依赖关系 (Dependencies)
     - 依赖于OS模块中OsTask的配置 (Dependent on the configuration of OsTask in the OS module)
     - 依赖于OS模块中OsTask的配置 (Dependent on the configuration of OsTask in the OS module)
     - 依赖于OS模块中OsTask的配置 (Dependent on the configuration of OsTask in the OS module)

RteBswModuleInstance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/iRTE/image2.png
   :alt: 通用配置页面-RteBswModuleInstance (General Configuration Page-RteBswModuleInstance)
   :name: 通用配置页面-RteBswModuleInstance (General Configuration Page-RteBswModuleInstance)
   :align: center



.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 描述 (Description)
     - 描述 (Description)
     - 描述 (Description)
   * - RteBswImplementationRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - RteBswImplementationRef
     - 参数描述 (Parameter Description)
     - 关联BswImplementation (Associate BswImplementation)
     - 关联BswImplementation (Associate BswImplementation)
     - 关联BswImplementation (Associate BswImplementation)
   * - RteBswImplementationRef
     - 依赖关系 (Dependencies)
     - 依赖于BSW的bswmd.arxml文件 (Dependent on BSW, the bswmd.arxml file)
     - 依赖于BSW的bswmd.arxml文件 (Dependent on BSW, the bswmd.arxml file)
     - 依赖于BSW的bswmd.arxml文件 (Dependent on BSW, the bswmd.arxml file)
         
RteBswEventToTaskMapping
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/iRTE/image3.png
   :alt: 通用配置页面-RteBswEventToTaskMapping (General Configuration Page-RteBswEventToTaskMapping)
   :name: 通用配置页面-RteBswEventToTaskMapping (General Configuration Page-RteBswEventToTaskMapping)
   :align: center



.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 描述 (Description)
     - 描述 (Description)
     - 描述 (Description)
   * - RteBswPositionInTask
     - 取值范围 (Range)
     - 0 .. 65535
     - 默认取值 (Default value)
     - 无
   * - RteBswPositionInTask
     - 参数描述 (Parameter Description)
     - BswSchedulableEntity在OsTask里的执行位置 (The execution position of BswSchedulableEntity in OsTask)
     - BswSchedulableEntity在OsTask里的执行位置 (The execution position of BswSchedulableEntity in OsTask)
     - BswSchedulableEntity在OsTask里的执行位置 (The execution position of BswSchedulableEntity in OsTask)
   * - RteBswPositionInTask
     - 依赖关系 (Dependencies)
     - 无
     - 无
     - 无
   * - RteBswServerQueueLength
     - 取值范围 (Range)
     - 0 .. 65535
     - 默认取值 (Default value)
     - 无
   * - RteBswServerQueueLength
     - 参数描述 (Parameter Description)
     - CS server队列长度 (CS server queue length)
     - CS server队列长度 (CS server queue length)
     - CS server队列长度 (CS server queue length)
   * - RteBswServerQueueLength
     - 依赖关系 (Dependencies)
     - 无
     - 无
     - 无
   * - RteBswEventRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - RteBswEventRef
     - 参数描述 (Parameter Description)
     - 关联RteEvent (Associated RteEvent)
     - 关联RteEvent (Associated RteEvent)
     - 关联RteEvent (Associated RteEvent)
   * - RteBswEventRef
     - 依赖关系 (Dependencies)
     - BSW模块描述arxml文件中RteBswEvent的配置 (BSW module description for configuration of RteBswEvent in arxml files)
     - BSW模块描述arxml文件中RteBswEvent的配置 (BSW module description for configuration of RteBswEvent in arxml files)
     - BSW模块描述arxml文件中RteBswEvent的配置 (BSW module description for configuration of RteBswEvent in arxml files)
   * - RteBswMappedToTaskRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - RteBswMappedToTaskRef
     - 参数描述 (Parameter Description)
     - 关联OsTask (Associate OsTask)
     - 关联OsTask (Associate OsTask)
     - 关联OsTask (Associate OsTask)
   * - RteBswMappedToTaskRef
     - 依赖关系 (Dependencies)
     - OS模块中OsTask的配置 (Configuration of OsTask in the OS Module)
     - OS模块中OsTask的配置 (Configuration of OsTask in the OS Module)
     - OS模块中OsTask的配置 (Configuration of OsTask in the OS Module)
   * - RteBswUsedOsEventRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - RteBswUsedOsEventRef
     - 参数描述 (Parameter Description)
     - 关联OsEvent (Associate OsEvent)
     - 关联OsEvent (Associate OsEvent)
     - 关联OsEvent (Associate OsEvent)
   * - RteBswUsedOsEventRef
     - 依赖关系 (Dependencies)
     - OS模块中OsEvent的配置 (Configuration of OsEvent in the OS Module)
     - OS模块中OsEvent的配置 (Configuration of OsEvent in the OS Module)
     - OS模块中OsEvent的配置 (Configuration of OsEvent in the OS Module)
   * - RteBswUsedOsAlarmRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - RteBswUsedOsAlarmRef
     - 参数描述 (Parameter Description)
     - 关联OsAlarm (AssociateOsAlarm)
     - 关联OsAlarm (AssociateOsAlarm)
     - 关联OsAlarm (AssociateOsAlarm)
   * - RteBswUsedOsAlarmRef
     - 依赖关系 (Dependencies)
     - OS模块中OsAlarm的配置 (Configuration of OsAlarm in the OS Module)
     - OS模块中OsAlarm的配置 (Configuration of OsAlarm in the OS Module)
     - OS模块中OsAlarm的配置 (Configuration of OsAlarm in the OS Module)

RteBswExclusiveAreaImpl
^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/iRTE/image4.png
   :alt: 通用配置页面-RteBswExclusiveAreaImpl (General Configuration Page-RteBswExclusiveAreaImpl)
   :name: 通用配置页面-RteBswExclusiveAreaImpl (General Configuration Page-RteBswExclusiveAreaImpl)
   :align: center



.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 描述 (Description)
     - 描述 (Description)
     - 描述 (Description)
   * - RteExclusiveAreaImplMechanism
     - 取值范围 (Range)
     - ALL_INTERRUPT_BLOCKING
     - 默认取值 (Default value)
     - 无
   * - RteExclusiveAreaImplMechanism
     - 取值范围 (Range)
     - NONE
     - 默认取值 (Default value)
     - 无
   * - RteExclusiveAreaImplMechanism
     - 取值范围 (Range)
     - OS_INTERRUPT_BLOCKING
     - 默认取值 (Default value)
     - 无
   * - RteExclusiveAreaImplMechanism
     - 取值范围 (Range)
     - OS_RESOURCE
     - 默认取值 (Default value)
     - 无
   * - RteExclusiveAreaImplMechanism
     - 取值范围 (Range)
     - OS_SPINLOCK
     - 默认取值 (Default value)
     - 无
   * - RteExclusiveAreaImplMechanism
     - 参数描述 (Parameter Description)
     - 独占区的实现机制选择 (The implementation mechanism for exclusivity zones)
     - 独占区的实现机制选择 (The implementation mechanism for exclusivity zones)
     - 独占区的实现机制选择 (The implementation mechanism for exclusivity zones)
   * - RteExclusiveAreaImplMechanism
     - 依赖关系 (Dependencies)
     - 无
     - 无
     - 无
   * - RteBswExclusiveAreaOsResourceRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - RteBswExclusiveAreaOsResourceRef
     - 参数描述 (Parameter Description)
     - 关联OsResource (Associate OsResource)
     - 关联OsResource (Associate OsResource)
     - 关联OsResource (Associate OsResource)
   * - RteBswExclusiveAreaOsResourceRef
     - 依赖关系 (Dependencies)
     - RteExclusiveAreaImplMechanism配置为OS_RESOURCE时 (Configure RteExclusiveAreaImplMechanism as OS_RESOURCE)
     - RteExclusiveAreaImplMechanism配置为OS_RESOURCE时 (Configure RteExclusiveAreaImplMechanism as OS_RESOURCE)
     - RteExclusiveAreaImplMechanism配置为OS_RESOURCE时 (Configure RteExclusiveAreaImplMechanism as OS_RESOURCE)
   * - RteBswExclusiveAreaOsSpinlockRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - RteBswExclusiveAreaOsSpinlockRef
     - 参数描述 (Parameter Description)
     - 关联OsSpinlock (Associate OsSpinlock)
     - 关联OsSpinlock (Associate OsSpinlock)
     - 关联OsSpinlock (Associate OsSpinlock)
   * - RteBswExclusiveAreaOsSpinlockRef
     - 依赖关系 (Dependencies)
     - RteExclusiveAreaImplMechanism配置为OS_SPINLOCK时 (Configure RteExclusiveAreaImplMechanism as OS_SPINLOCK when)
     - RteExclusiveAreaImplMechanism配置为OS_SPINLOCK时 (Configure RteExclusiveAreaImplMechanism as OS_SPINLOCK when)
     - RteExclusiveAreaImplMechanism配置为OS_SPINLOCK时 (Configure RteExclusiveAreaImplMechanism as OS_SPINLOCK when)
   * - RteBswExclusiveAreaRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - RteBswExclusiveAreaRef
     - 参数描述 (Parameter Description)
     - BSW模块描述arxml中ExclusiveArea (BSW Module Description arxml ExclusiveArea)
     - BSW模块描述arxml中ExclusiveArea (BSW Module Description arxml ExclusiveArea)
     - BSW模块描述arxml中ExclusiveArea (BSW Module Description arxml ExclusiveArea)
   * - RteBswExclusiveAreaRef
     - 依赖关系 (Dependencies)
     - BSW模块描述arxml文件中ExclusiveArea的配置 (BSW Module Describes Configuration in arxml File for ExclusiveArea)
     - BSW模块描述arxml文件中ExclusiveArea的配置 (BSW Module Describes Configuration in arxml File for ExclusiveArea)
     - BSW模块描述arxml文件中ExclusiveArea的配置 (BSW Module Describes Configuration in arxml File for ExclusiveArea)

Bswmd文件更新(BSWMD file update)
--------------------------------------

基于BSW模块的设计，工具可更新全部或单个模块描述文件，用来描述BSW模块在接口层面、BswEntity调度的需求，作为iRte的输入生成代码。

Based on the BSW module design, the tool can update all or individual module description files to describe the BSW module's requirements at the interface level and the scheduling needs of BswEntity as input for generating code.

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/iRTE/image5.png
   :alt: 更新全部Bswmd文件 (Update all Bswmd files)
   :name: 更新全部Bswmd文件 (Update all Bswmd files)
   :align: center



.. figure:: ../../_static/参考手册(Module_Reference_Manual)/iRTE/image6.png
   :alt: 更新单个模块Bswmd文件 (Update individual module Bswmd file)
   :name: 更新单个模块Bswmd文件 (Update individual module Bswmd file)
   :align: center


iRTE-OS同步配置 (iRTE-OS Synchronized Configuration)
----------------------------------------------------------------

基于BSW的模块描述文件（Bswmd文件），根据模型需求自动配置OS模块。自动配置分两种：

Module description files (Bswmd files) based on BSW, automatically configure OS modules according to model requirements. Automatic configuration is divided into two types:

与iRTE实现相关，OS必须按实现需求进行配置且客户不能修改；

Regarding iRTE implementation, the OS must be configured according to the implementation requirements and customers cannot modify it;

为客户提供配置Demo，简化客户手动配置工作量，客户根据应用场景在自动配置的基础上进行少量调整、适配；

Provide configuration demos for customers to simplify their manual configuration efforts, allowing them to make minor adjustments and adaptations based on their specific use cases on top of the automatic configurations.

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/iRTE/image7.png
   :alt: iRTE-OS自动配置 (iRTE-OS Auto Configuration)
   :name: iRTE-OS自动配置 (iRTE-OS Auto Configuration)
   :align: center


iRTE生成和集成 (iRTE Generation and Integration)
===========================================================

工具开发流程概述 (Overview of Tool Development Process)
---------------------------------------------------------------

完成除OS和iRTE之外的所有BSW模块配置；

Complete the configuration of all BSW modules except OS and iRTE;

补充必要的OS信息如OS核数；

Add necessary OS information such as the number of OS cores;

更新全部BSW模块的模块描述文件；

Update all BSW modules' module description files;

手动配置章节4中的配置内容，或通过iRTE-OS同步功能自动生成推荐Demo配置（iRTE模块和OS模块）；

Manually configure the content as described in Chapter 4, or automatically generate the recommended Demo configuration (iRTE module and OS module) through the iRTE-OS synchronization feature;

如果选用了iRTE-OS同步功能，需要基于自动生成的推荐OS、iRTE Demo配置，结合使用场景进行调整适配；

If the iRTE-OS synchronization feature is selected, adjustments and adaptations need to be made based on the auto-generated recommended OS and iRTE Demo configurations in conjunction with the usage scenario.

先生成iRTE代码，后生成OS代码（全工程生成顺序为其它BSW→iRTE→OS）；

Generate iRTE code first, then generate OS code (the full engineering generation order is other BSW → iRTE → OS);

iRTE文件结构 (iRTE File Structure)
----------------------------------------------

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/iRTE/image8.png
   :alt: iRTE文件结构 (iRTE File Structure)
   :name: iRTE文件结构 (iRTE File Structure)
   :align: center



.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 文件名 (Filename)
     - 描述 (Description)
   * - SchM.c
     - 包含如下几部分内容： 生命周期函数定义；  定义Os_Task，填充其内容； (Contents as follows: Event Lifecycle Definition; Define Os_Task and Fill Its Content;)
   * - SchM<Mip>.c
     - SchM接口实现 (Implementation of SchM Interface)
   * - SchM<Mip>.h
     - SchM接口声明； BswSchduleEntity和BswCalledEntity原型声明； (SchM interface declaration; prototype declarations for BswSchduleEntity and BswCalledEntity;)
   * - SchM<Mip>_Type.h
     - BSW模块使用的数据类型定义； (Data types defined for the BSW module;)
   * - SchM.h
     - 声明生命周期函数； (Declare lifecycle functions;)
   * - SchM_Internal.h
     - 定义SchM内部公共函数； (Define internal public functions of SchM;)
   * - SchM_Type.h
     - 定义SchM内部使用数据类型； (Define data types for use within SchM;)
   * - Rte_Main.h
     - Bsw模块固定引用； (Bsw module fixed reference;)

集成(Integrate)
---------------------

按照5.1章节完成工程的配置，生成所有BSW（包括OS、iRTE、MCAL）动态配置代码后，基于芯片、编译器搭建代码工程，集成BSW静态代码以及工具生成的动态代码，手动集成Application代码，基于内存布局需求、以及BSW的MemMap进行链接文件设计，整体进行编译、链接。

After completing the configuration of the project according to Chapter 5.1, generate all BSW (including OS, iRTE, MCAL) dynamic configuration codes. Based on the chip and compiler, set up the code engineering, integrate BSW static codes and dynamically generated codes by tools, manually integrate Application code, design link files based on memory layout requirements and BSW MemMap, and perform overall compilation and linking.










