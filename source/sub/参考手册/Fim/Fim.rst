===================
Fim
===================



文档信息 Document Information
================================================================

版本历史 Version History
------------------------------------------------------------------------------------------------------------

.. list-table::
   :widths: 10 10 10 10 20
   :header-rows: 1

   * - 日期(Date)
     - 作者(Author)
     - 版本(Version)
     - 状态(Status)
     - 说明(Description)

   * - 2025/02/21
     - li.feng
     - V0.1
     - 发布(Release)
     - 首次发布(First release)

   * - 2025/04/04
     - li.feng
     - V1.0
     - 发布(Release)
     - 正式发布(Official release)

参考文档 References
------------------------------------------------------------------------------------------------------------

.. list-table::
   :widths: 10 10 30 10
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
     - AUTOSAR_CP_SWS_FunctionInhibitionManager.pdf
     - R23-11 
   * - 3
     - Autosar
     - AUTOSAR_CP_SWS_DiagnosticEventManager.pdf
     - R23-11 
   * - 4
     - Autosar
     - AUTOSAR_CP_SRS_FunctionInhibitionManager.pdf
     - R23-11 

术语与简写 Terms and Abbreviations
================================================================

术语 Terms
------------------------------------------------------------------------------------------------------------
.. :align: center   表格内容居中(Table contents are centered)


.. list-table::
   :widths: 15 40
   :header-rows: 1

   * - 术语(Terms)
     - 解释(Explanation)

   * - Monitor Status
     - 事件状态:“监视器状态”是由Dem根据监视器的报告值计算的状态.(Event state: “Monitor status” refers to the state that is calculated by Dem according to report value of monitor.)

   * - Diagnostic Event
     - 诊断事件:“诊断事件”是Dem提供给特定诊断监视器功能的标识符,用于报告错误.(Diagnostic event: “Diagnostic event” is an identifier provided by Dem to the specific diagnostic monitor for reporting an error.)

   * - Summarized Event
     - 汇总事件：汇总事件由多个单个诊断事件组成.(Summarized event: Composed of multiple single diagnostic events.)

   * - Function Identifier
     - 唯一功能标识符.(Unique function identifier.)
   
   * - Function Identifier permission state
     - FID许可状态:FID权限状态包含由其FID表示的功能是否可以执行的信息.(FID permission state: FID permission state includes the information about whether the functions indicated by FID can be executed.)

   * - Monitored Component
     - 监控组件:“监控组件”是Dem提供给特定被监控组件(硬件组件或信号)的标识符.(Monitored component: “Monitored component” is an identifier that is provided by Dem to the specific monitored component (hardware component or signal).)

简写 Abbreviations
------------------------------------------------------------------------------------------------------------

.. list-table::
   :widths: 10 20 30
   :header-rows: 1

   * - 简写(Abbreviation)
     - 全称(Full name)
     - 解释(Explanation)

   * - Activity state
     - The activity state is the status of a software component being executed
     - 正在执行的软件组件的状态.

   * - FID
     - Function Identifier
     - 功能ID.

   * - FiM
     - Function Inhibition Manager
     - 功能抑制管理

   * - Inhibition Condition
     - The relation between one FID, an inhibition mask and the status of a Dem event/component.
     - 抑制条件

   * - MIL
     - Malfunction Indication Light
     - 故障指示灯

   * - Permission state
     - The permission state contains the information whether a functionality, represented by its FID, can be executed or whether it shall not run
     - 功能许可状态

   * - Dem
     - Diagnostic Event Manage
     - 诊断事件管理





简介 Introduction
================================================================

如图FiM模块位于系统服务层,主要供SWC(应用软件组件使用),一个SWC里面有多个功能,每个功能都对应一个FID,当SWC中的事件状态发生改变,SWC会报告给DEM,FiM会通过轮训/触发来获取DEM的事件状态,然后根据配置的事件和功能的映射关系来决定功能的禁用与否,功能对应的SWC会访问FiM来获取该功能是否要禁用.

As shown in picture, the FiM module is in system service layer for providing SWC (used by application software component). One SWC contains multiple functions. Each function corresponds to one FID; when the event status of SWC changes, SWC will make report to DEM, FiM will get the event status of DEM through polling/trigger, then determine whether disable the function based on configured event and mapping relationship of function, and the corresponding SWC of function Access FiM to see if this feature needs disabling

.. figure:: ../../../_static/参考手册/FiM/FiM_architecture.png
   :alt: FiM架构层次图 (FiM Architecture Hierarchy Diagram)
   :name: FiM_arch
   :align: center

   FiM架构层次图 (FiM Architecture Hierarchy Diagram)

如图 :ref:`FiM_Relationship` 所示,接口的详细内容请参考“接口描述”章节.

As shown in the figure :ref:`FiM_Relationship` , please see the 'Interface Description' chapter for details about interface

.. figure:: ../../../_static/参考手册/FiM/FiM_Relationship.png
   :alt: FiM模块接口关系图 (FiM Module Interface Relationship Diagram)
   :name: FiM_Relationship
   :align: center

   FiM_Relationship

功能描述 Functional Description
================================================================

特性 Features
------------------------------------------------------------------------------------------------------------

模块初始化 Module initialization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Dem和FiM的初始化顺序如下:

The initialization sequence of Dem and FiM is as follows:

1.Dem_PreInit,Dem预初始化

1.Dem_PreInit, Dem pre-initialization

2.非易失性存储器数据需可用

2.Non-volatile memory data should be available

3.FiM初始化(设置内部变量);初始化后,FiM尚不能使用

3.FiM initialization (set internal variables); FiM cannot be used yet after initialization

4.DEM初始化:进行内部DEM初始化,并使用FiM_DemInit最终初始化FiM

4.DEM initialization: Conduct internal DEM initialization and use FiM_DemInit to finally initialize FiM

FiM_GetFunctionPermission在FiM完整初始化之前(FiM_DemInit)调用需要返回E_NOT_OK

Before the full initialization of FiM (FiM_DemInit),  return E_NOT-OK for calling FiM_GetFunctionalPermission


FID唯一性 FID Uniqueness
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

每一个功能在FiM模块中都会对应一个唯一的FID,该FID的作用是管理功能的禁用与否,SWC正是通过FID来访问FiM,并知道功能是否被禁用对事件具有不同依赖性的两个不同功能决不能具有相同的FunctionId,用户需要确保不同功能使用不同的FID,FID的值由工具保证唯一性

In the FiM module, each function corresponds to a unique FID, which is used for managing whether the function is disabled or not. SWC accesses FiM through FID and knows whether the function is disabled Two different functions with different dependencies on events shall not have the same FunctionalId. Users need to ensure that different FIDs are used for different functions, and the unique FID value is ensured by tool

FID的抑制源 Inhibition Source of FID
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

FID是否抑制受到DEM中的组件(Component),事件(event)和汇总事件(Summarized Event)的状态的控制

FID inhibition is controlled by the states of components, events, and Summarized Event in DEM

其中汇总事件是由多个单个诊断事件组成,汇总事件是多个诊断事件的代表,当与汇总事件相关联的事件被报告给FiM时

To be specific, the Summarized Event is composed of several individual diagnostic events, and represents several diagnostic events. When the events associated with the Summarized Event are reported to FiM

FiM需要能够一并处理与该汇总事件相关联的所有FID的禁止条件

FiM should be able to handle all FID prohibition conditions linked with the Summarized Event together


事件,组件与FID的对应关系 Correspondence of Event, Component and FID
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1.一个FID可以对应多个event,代表多个event都会对FID代表的功能进行抑制控制,而这种控制关系是只要有一个event达到功能抑制的条件,不管其它event的状态都会对对应功能抑制

1.A FID can correspond to many events. The representation of several event inhibits and controls the function represented by the FID. Such control relationship can inhibit the corresponding functions, as long as one event reaches the condition of functional suppression, whatever the state of other events

2.一个event可对应多个FID,代表一个事件会影响到多个功能的抑制。

2.One event can correspond to several FIDs. The representation of one event will affect the inhibition of multiple functions.

3.一个FID可以对应多个组件,代表一个FID对应的功能被多个组件所使用,只要有一个组件状态达到功能禁止的条件,那么该功能就被禁止

3.A FID can correspond to several components. The functions corresponding to one FID represented are used by several components. However, the function will be disabled, as long as one component reaches the condition of function prohibition

如图 :ref:`FIM-EVENT-COMPONENT` 是Event和FID关系示意:

The figure :ref:`FIM-EVENT-COMPONENT` is the schematic diagram of the relationship between Event and FID:

.. figure:: ../../../_static/参考手册/FiM/FIM-EVENT-COMPONENT.png
   :alt: FID-Event映射关系 (FID-Event mapping relationship)
   :name: FIM-EVENT-COMPONENT
   :align: center

   FIM-EVENT-COMPONENT

FID的抑制条件 Inhibition Conditions of FID
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

每一个DEM事件和FID都有一个对应的掩码,掩码有以下四种类型

Each DEM event and FID has a corresponding mask in the following four types

.. list-table::
   :widths: 10 20 
   :header-rows: 1

   * - 掩码(Mask)
     - 解释(Explanation)    

   * - Inhitbit if failed
     - 如果某个DEM事件最近一次的测试失败,那么如果与DEM事件关联的FID的掩码为Inhitbit if failed,则FID对应功能被禁止(When the most recent test of one DEM event fails, if the mask of FID linked with DEM event is Inhitbit if failed, the corresponding function of the FID will be disabled)

   * - Inhibit if tested
     - 如果某个DEM事件当前操作周期测试完成,那么如果与DEM事件关联的FID的掩码为Inhibit if tested,则FID对应功能被禁止(When the current operation cycle test of one DEM event is completed, if the mask of FID linked with the DEM event is Inhibit if tested, the corresponding function of the FID will be disabled)

   * - Inhibit if not tested
     - 如果某个DEM事件当前操作周期未完成测试,那么如果与DEM事件关联的FID的掩码为Inhibit if tested,则FID对应功能被禁止(When the current operation cycle test of one DEM event is not completed, if the mask of FID linked with the DEM event is Inhibit if tested, the corresponding function of the FID will be disabled)

   * - Inhibit if tested and failed
     - 如果某个DEM事件当前操作周期完成测试并且测试失败,那么如果与DEM事件关联的FID的掩码为Inhibit if tested,则FID对应功能被禁止(When the current operation cycle test of one DEM event is completed and test fails, if the mask of FID linked with the DEM event is Inhibit if tested, the corresponding function of the FID will be disabled)

根据事件真实的状态和掩码信息计算抑制状态。当状态与掩码匹配时，功能抑制。当状态与掩码不匹配时，功能取消抑制

Calculate the inhibition state based on the true state of the event and mask information. When the state matches the mask, the function inhibition will be enabled. When the state does not match the mask, the function inhibition will be cancelled.

使用 FID - DemComponentId - inhibition configuration来计算FID的允许状态当组件变化为 FAILED时,功能需要抑制

When FID DemWidgetId inhibition configuration is used to calculate the allowed state of FID, if the component changes to FAILED, the function needs inhibiting

配置工程师应在编译时提供处理FiM模块中功能和事件的依赖关系所需的每个FID的抑制条件

During compilation, the configuration engineer should provide the inhibition conditions for each FID required to handle the dependencies between functions and events in the FiM module


FIM支持轮询和触发 Polling and Triggering Supported by FIM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

FiM支持轮询和触发来获取DEM事件的状态

FiM supports polling and triggering to get the status of DEM events

1.轮询

1.Polling

在FiM_MainFunction里面通过轮询所有的FID及其对应的事件状态来计算FID的抑制状态

Calculate the inhibition state of FID by polling all FIDs and their corresponding event statuses in FiM_MainFunction

2.触发

2.Triggering

在DEM中通过调用FiM提供的FiM_DemTriggerOnComponentStatus/FiM_DemTriggerOnMonitorStatus来触发对应FID运抑制状态的计算

Calculation of the corresponding FID operation inhibition state will be triggered in DEM by calling FiM_DemTriggerOn componentStatus/FiM_DemTriggerOnMonitorStatus provided by FiM

FiM模块应通过同步响应传入的权限查询来确保对功能的即时控制。FiM模块可以通过将权限状态存储为状态变量或在权限查询时计算事件状态来实现这种行为。通过匹配计数器来记录信息,大于0时为抑制

The FiM module should ensure immediate control over functionality by synchronously responding to incoming permission queries. The FiM module can realize such behavior by storing permission states as state variables or calculating event statuses  during permission queries.Information is recorded by matching the counter. Inhibition is enabled when it is greater than 0.




支持FID的使能/失能 Support of FID Enabling/Disabling
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

使用FiM_SetFunctionAvailable不使能FID,则请求FiM_GetFunctionPermission时返回FALSE

If FID is not enabled via FiM_SetFunctionalAvailable, then return to FALSE when requesting FiM_GetFunctionalPermission

.. only:: doc_pbs

  变体 Variant
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  1.支持功能抑制配置不同的抑制源和抑制条件

  1.Support the configuration of function inhibition with different inhibition sources and conditions

偏差 Deviation
------------------------------------------------------------------------------------------------------------

None

扩展 Extension
------------------------------------------------------------------------------------------------------------

None


集成 Integration
================================================================

文件列表 File List
------------------------------------------------------------------------------------------------------------

静态文件 Static Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - 文件(File)
     - 描述(Description)
   
   * - FiM.h
     - FiM模块源码文件,包含需要使用的宏定义,内部变量,内部函数,全局函数.(FiM module source code file, containing macro definitions, internal variables, internal functions, and global functions, all of which will be used.)

   * - FiM_OptMacros.h
     - FiM实现文件,包含FiM功能的宏开关.(FiM implementation file, containing macro switches for FiM functionality)

   * - FiM_Dem.h
     - 与DEM相关API的声明文件.(Declaration file of DEM-related APIs)

   * - Tm_MemMep.h
     - FiM的内存映射定义文件.(Memory mapping definition file of FiM)
   
   * - FiM_Types.h
     - FiM的内存定义文件.(Memory definition file of FiM.)

   * - FiM.c
     - FiM的功能实现文件.(Implementation file for the FiM functionality)
     
动态文件 Dynamic Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - 文件(File)
     - 描述(Description)

   * - FiM_Cfg.h
     - FiM模块PC配置宏定义.(PC configuration macro definition of FiM module.)

   * - FiM_Lcfg.c
     - FiM模块非PB配置数据变量定义.(Definition of non-PB configuration data variables of FiM module)

   * - FiM_Lcfg.h
     - FiM模块非PB配置数据变量声明、宏定义.(Variable declaration and macro definition of non-PB configuration data of FiM module.)

   * - FiM_PBcfg.c
     - FiM模块PB配置数据变量定义.(Definition of PB configuration data variables of FiM module.)

   * - FiM_PBcfg.h
     - FiM模块PB配置数据变量声明.(Declaration of PB configuration data variables of FiM module.)
     
   * - Rte_FiM_Type.h
     - FiM模块实现数据类型定义.(Definition of realization data type of FiM module.)

错误处理 Error Handling
------------------------------------------------------------------------------------------------------------

开发错误 Development Errors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. list-table:: 
   :widths: 20 10 30
   :header-rows: 1

   * - Error code
     - Value[hex]
     - Description

   * - FIM_E_NO_ERROR
     - 0x0u
     - API function called with no det error

   * - FIM_E_UNINIT
     - 0x01u
     - API function called with a parameter value, which is not allowed by active configuration

   * - FIM_E_FID_OUT_OF_RANGE
     - 0x02u
     - FiM_GetFunctionPermission called with wrong FID

   * - FIM_E_EVENTID_OUT_OF_RANGE
     - 0x03u
     - Dem calls FiM with invalid EventId

   * - FIM_E_PARAM_POINTER
     - 0x04u
     - API is invoked with NULL Pointer

   * - FIM_E_INIT_FAILED
     - 0x05u
     - Invalid configuration set selection

   * - FIM_E_COMPONENT_OUT_OF_RANGE
     - 0x09u
     - Dem calls FiM with invalid ComponentId 

   * - FIM_E_PARTITION_ERROR
     - 0x0Au
     - partition error



产品错误 Product Errors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
None



.. include:: Fim_api.rst



依赖的服务 Applicable Services
------------------------------------------------------------------------------------------------------------

可选接口 Optional Interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 10 5 30
   :header-rows: 1

   * - API Function
     - Header File
     - Description

   * - Det_ReportError
     - Det.h
     - Service to report development errors

服务封装 Service Encapsulation
------------------------------------------------------------------------------------------------------------

None

配置 Configuration
================================================================


FiMConfigSetup配置 Configuration of FiMConfigSetup
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

该配置包含了三个子容器用于描述FIM模块,如图 :ref:`FiMConfigSetup`

This configuration contains three sub-containers for describing the FIM module, as shown in the figure :ref:`FiMConfigSetup`

.. figure:: ../../../_static/参考手册/FiM/FiMConfigSetup.png
   :alt: FiMConfigSetup配置图 (FiMConfigSetup Configuration Diagram)
   :name: FiMConfigSetup
   :align: center

   FiMConfigSetup



1.FiMFiDs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

FiM管理功能的抑制,每一个功能都会被分配一个唯一的FiD,给FiM添加FiD需要鼠标右键点击FiMFID,如下图 :ref:`FiMFID_add`:

Inhibition of FiM management function. Each function is assigned a unique FiD,To add FiD to FiM, right click FiMFID, as shown below :ref:`FiMFID_add`:

.. figure:: ../../../_static/参考手册/FiM/FiMFID_add.png
   :alt: FiMFID_add配置图 (FiMFID_add Configuration Diagram)
   :name: FiMFID_add
   :align: center

   FiMFID_add


创建好iMFiD后FiMFIDs的文件夹下面就会显示该FID,左键点击该FID的名称,在右面就会出现该FID的配置选项,其中包含Fid的编号和分区,FiM支持多分区,FiMFIDEcucPartitionRef为该功能所在的分区索引而FiMFIDEcucPartitionRef的选项请参考EcuC配置参考文档,如下图 :ref:`FiMFiDs`:

After creating iMFiD, the FID will be displayed by the FiMFIDs folder. Left click the name of the FID, and the configuration options for the FID will appear on the right. It includes Fid numbers and partitions; FiM supports multiple partitions.FiMFIDEcucPartitionRef is the index of the area that includes such function. For the options of FiMFIDEcucPartitionRef, refer to the EcuC configuration reference document, as shown in the following figure :ref:`FiMFiDs`:

.. figure:: ../../../_static/参考手册/FiM/FiMFiDs.png
   :alt: FiMFiDs配置图 (FiMFiDs Configuration Diagram)
   :name: FiMFiDs
   :align: center

   FiMFiDs

2.FiMInhibitionConfigurations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

在FiMInhibitionConfigurations可添加多个FiMInhibitionConfiguration_x,通过右键点击FiMInhibitionConfigurations即可添加

Several FiMInhibitionConfiguration-x can be added in FiMInhibitionConfiguration by right clicking the FiMInhibitionConfiguration

如下图 :ref:`FiMInhibitionConfiguration_add` 所示:

As shown in the following figure :ref:`FiMInhibitionConfiguration_add` :

.. figure:: ../../../_static/参考手册/FiM/FiMInhibitionConfiguration_add.png
   :alt: FiMInhibitionConfiguration_add配置图 (FiMInhibitionConfiguration_add Configuration Diagram)
   :name: FiMInhibitionConfiguration_add
   :align: center

   FiMInhibitionConfiguration_add


FiMInhibitionConfiguration容器包含FID和事件/组件之间的关系,由FIM的特性可知,一个FID可以映射到多个事件,DEM组件,和汇总事件,为了描述这种关系所以有了该容器由FiM的特性可知,FID-Event/Component的映射会有一个唯一的FiMInhInhibitionMask,而一个FID可以映射多个Event/Component,所以一个FID和与其有关系的Event/Component可能存在1到4种FiMInhInhibitionMask.

The FiMInhibitionConfiguration container contains the relationships between FIDs and events/components. It can be learned by the characteristics of FIMs that one FID can be mapped to multiple events, DEM components, and Summarized Event. The container was created in order to describe these relationships It can be learned by the characteristics of FiM that the mapping of FID Event/Component will have a unique FiMInhInhibitionMask, and a FID can map several Event/Components,Therefore, one FID and its related Event/Component may have 1 to 4 FiMInhInhibitionMasks

而FiMInhibitionConfiguration以此为基础,描述出某个FID的其中一种FiMInhInhibitionMask下所有的Event,Component和汇总事件,所以FiMInhibitionConfigurations下

On the basis of the above, FiMInhibitionConfiguration describes all Events, Components, and Summarized Events under one of the FiMInhInhibitionMasks of one FID. Therefore, under FiMInhibitionConfiguration

所以一个FID最大有四种FiMInhibitionConfiguration,如图 :ref:`FiMInhibitionConfiguration` :

Therefore, one FID can have at most 4 FiMInhibitionConfiguration options, as shown in the figure :ref:`FiMInhibitionConfiguration` :

.. figure:: ../../../_static/参考手册/FiM/FiMInhibitionConfiguration.png
   :alt: FiMInhibitionConfiguration配置图 (FiMInhibitionConfiguration Configuration Diagram)
   :name: FiMInhibitionConfiguration
   :align: center

   FiMInhibitionConfiguration



1.FiMInhFunctionIdRef

该配置后面的选项框里面包含了所有的FID的名称,每一个FID都有一个或多个FiMInhibitionConfiguration

The option box behind this configuration contains the names of all FIDs. Each FID has one or more FiMInhibitionConfiguration

一个FiMInhibitionConfiguration只能对应一个FID

One FiMInhibitionConfiguration can only correspond to one FID

2.FiMInhInhibitionMask

抑制掩码,特性里面有四种掩码的选项,一个FiMInhibitionConfiguration对应一个掩码

Inhibition mask; there are four mask options in the feature; one FiMInhibitionConfiguration corresponds to one mask

3.FiMInhComponentRef

该配置下面包含了该FID和FiMInhInhibitionMask组合下的所有和该FID有关系的组件。

This configuration includes all components related to such FID under the combination of this FID and FiMInhInhibitionMask.

如下图 :ref:`FiMInhComponentRef_add` 点击红框中的按钮添加FID对应的选项,其中的DemComponent_x是DEM所配置的

As shown in the figure below: ref: ` FiMInhWidgetRef_dedd ` Click the button in the red box to add the option corresponding to FID. In particular, DemWidget-x is configured by DEM

.. figure:: ../../../_static/参考手册/FiM/FiMInhComponentRef_add.png
   :alt: FiMInhComponentRef_add配置图 (FiMInhComponentRef_add Configuration Diagram)
   :name: FiMInhComponentRef_add
   :align: center

   FiMInhComponentRef_add

4.FiMInhEventRef

该配置下面包含了该FID和FiMInhInhibitionMask组合下的所有和该FID有关系的事件(Event)。

This configuration contains all events related to such FID under the combination of this FID and FiMInhInhibitionMask.

填方法同FiMInhComponentRef

The filling method is the same as FiMInhComponentRef

5.FiMInhSumRef

该配置下面包含了该FID和FiMInhInhibitionMask组合下的所有和该FID有关系的汇总事件(Sum Event)。

This configuration contains all Sum Events related to such FID under the combination of this FID and FiMInhInhibitionMask.

填方法同FiMInhComponentRef

The filling method is the same as FiMInhComponentRef


3.FiMSummaryEvents
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

FiMSummaryEvents里面包含了所有的汇总事件,每一个汇总事件都是由多个单个事件组成

FiMSummaryEvents contains all Sum Events, each of which also contains several individual events

FiMSummaryEvents主要是配置汇总事件和汇总事件所包含的单个事件

FiMSummaryEvents is mainly used for configuring Sum Events and individual events included in the Sum Events

右键点击FiMSummaryEvents添加汇总事件,如下图 :ref:`FiMSummaryEvents` :

Right click FiMSummaryEvents to add Sum Events, as shown in the following figure :ref:`FiMSummaryEvents` :

.. figure:: ../../../_static/参考手册/FiM/FiMSummaryEvents.png
   :alt: FiMSummaryEvents配置图 (FiMSummaryEvents Configuration Diagram)
   :name: FiMSummaryEvents
   :align: center

   FiMSummaryEvents

然后点击创建的汇总事件条目弹出右面的创作出对汇总事件内的单个事件进行添加或删除 :ref:`FiMSummaryEvents_add` 。

Then click the created Sum Event entry to pop up the 'Create' option on the right to add or delete individual events within the Sum Even :ref:`FiMSummaryEvents_add` .

.. figure:: ../../../_static/参考手册/FiM/FiMSummaryEvents_add.png
   :alt: FiMSummaryEvents_add配置图 (FiMSummaryEvents_add Configuration Diagram)
   :name: FiMSummaryEvents_add
   :align: center

   FiMSummaryEvents_add


FiMGeneral配置 FiMGeneral Configuration
------------------------------------------------------------------------------------------------------------------------------------------------------------------

FiMAvailabilitySupport
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

该参数用于设置指定的FID是否支持功能禁用

This parameter is used for setting whether the specified FID supports feature disabling

true:支持

true: Support

false:不支持

false: No support

.. figure:: ../../../_static/参考手册/FiM/FiMAvailabilitySupport.png
   :alt: FiMAvailabilitySupport配置图 (FiMAvailabilitySupport Configuration Diagram)
   :name: FiMAvailabilitySupport
   :align: center

   FiMAvailabilitySupport

FiMDevErrorDetect
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

打开或关闭开发错误检测和通知.

Enable or disable the development error detection and notifications

True:开启检测和通知功能.

True: Enable detection and notification functions.

false:关闭检测和通知功能

false: Disable detection and notification functions


.. figure:: ../../../_static/参考手册/FiM/FiMDevErrorDetect.png
   :alt: FiMDevErrorDetect配置图 (FiMDevErrorDetect Configuration Diagram)
   :name: FiMDevErrorDetect
   :align: center

   FiMDevErrorDetect


FiMEventUpdateTriggeredByDem
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

指定FIM获取EventIds状态的方式.

Specify How FIMs Get the EventIds Status

TRUE: DEM通知FIM监视器状态的变化.

TRUE: DEM notifies FIM of the monitor status changes

FALSE: FIM轮询从DEM模块周期性或按需监视状态.

FALSE: The FIM polling monitors the status periodically or based on demand from the DEM module

.. figure:: ../../../_static/参考手册/FiM/FiMEventUpdateTriggeredByDem.png
   :alt: FiMEventUpdateTriggeredByDem配置图 (FiMEventUpdateTriggeredByDem Configuration Diagram)
   :name: FiMEventUpdateTriggeredByDem
   :align: center

   FiMEventUpdateTriggeredByDem

FiMMainFunctionPeriod
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

周期任务的执行时间 Execution Time of Cycle Task

.. figure:: ../../../_static/参考手册/FiM/FiMMainFunctionPeriod.png
   :alt: FiMMainFunctionPeriod配置图 (FiMMainFunctionPeriod Configuration Diagram)
   :name: FiMMainFunctionPeriod
   :align: center

   FiMMainFunctionPeriod

FiMMaxEventsPerFidInhibitionConfiguration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

指定单个FiMInhibitionConfiguration中抑制事件的最大总数,为Event,Component和汇总事件的总和

Specify the max. total number of inhibited events in a single FiMInhibitionConfiguration, which is the sum of Events, Components, and Summarized Events

.. figure:: ../../../_static/参考手册/FiM/FiMMaxEventsPerFidInhibitionConfiguration.png
   :alt: FiMMaxEventsPerFidInhibitionConfiguration配置图 (FiMMaxEventsPerFidInhibitionConfiguration Configuration Diagram)
   :name: FiMMaxEventsPerFidInhibitionConfiguration
   :align: center

   FiMMaxEventsPerFidInhibitionConfiguration

    
FiMMaxFiMInhibitionConfigurations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

指定FiMInhibitionConfigurations的最大总数,即其中FiMInhibitionConfiguration的个数

Specify the max. total number of FiMInhibitionConfiguration, that is, the number of FiMInhibitionConfiguration in it

.. figure:: ../../../_static/参考手册/FiM/FiMMaxFiMInhibitionConfigurations.png
   :alt: FiMMaxFiMInhibitionConfigurations配置图 (FiMMaxFiMInhibitionConfigurations Configuration Diagram)
   :name: FiMMaxFiMInhibitionConfigurations
   :align: center

   FiMMaxFiMInhibitionConfigurations


FiMMaxInputEventsPerSummaryEvents
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


指定每个汇总事件中的单个事件的总数,即FiMSummaryEvent_x下面可添加的事件的总数

Specify the total number of individual events in each Summarized Event, i.e. the total number of events that can be added under FiMSummaryEvent-x

.. figure:: ../../../_static/参考手册/FiM/FiMMaxInputEventsPerSummaryEvents.png
   :alt: FiMMaxInputEventsPerSummaryEvents配置图 (FiMMaxInputEventsPerSummaryEvents Configuration Diagram)
   :name: FiMMaxInputEventsPerSummaryEvents
   :align: center

   FiMMaxInputEventsPerSummaryEvents


FiMMaxSumEventsPerFidInhibitionConfiguration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

指定FiMInhibitionConfiguration中汇总事件的最大总数。FiMInhSumRef容器下可添加的事件总数

Specify the max. total number of Summarized Events in FiMInhibitionConfiguration. Total events that can be added under FiMInhSumRef container

.. figure:: ../../../_static/参考手册/FiM/FiMMaxSumEventsPerFidInhibitionConfiguration.png
   :alt: FiMMaxSumEventsPerFidInhibitionConfiguration配置图 (FiMMaxSumEventsPerFidInhibitionConfiguration Configuration Diagram)
   :name: FiMMaxSumEventsPerFidInhibitionConfiguration
   :align: center

   FiMMaxSumEventsPerFidInhibitionConfiguration

FiMMaxSummaryEvents
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

指定可配置的汇总事件的最大数目,即FiMSummaryEvents容器下FiMSummaryEvent的总数

Specify the max. number of configurable Summary Events, which is the total number of FiMSummaryEvents in the FiMSummaryEvents container

.. figure:: ../../../_static/参考手册/FiM/FiMMaxSummaryEvents.png
   :alt: FiMMaxSummaryEvents配置图 (FiMMaxSummaryEvents Configuration Diagram)
   :name: FiMMaxSummaryEvents
   :align: center

   FiMMaxSummaryEvents

FiMVersionInfoApi
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

打开或关闭获取版本信息的API

Open or close to get the API of version information

.. figure:: ../../../_static/参考手册/FiM/FiMVersionInfoApi.png
   :alt: FiMVersionInfoApi配置图 (FiMVersionInfoApi Configuration Diagram)
   :name: FiMVersionInfoApi
   :align: center

   FiMVersionInfoApi

FiMMaxComponentsPerFidInhibitionConfiguration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

指定FiMInhibitionConfiguration中Component的最大总数,即FiMInhComponentRef容器下,可添加的Component的总数

Specify the max. total number of Components in FiMInhibitionConfiguration, that is, the total number of Components that can be added under the FiMInhWidgetRef container

.. figure:: ../../../_static/参考手册/FiM/FiMMaxComponentsPerFidInhibitionConfiguration.png
   :alt: FiMMaxComponentsPerFidInhibitionConfiguration配置图 (FiMMaxComponentsPerFidInhibitionConfiguration Configuration Diagram)
   :name: FiMMaxComponentsPerFidInhibitionConfiguration
   :align: center

   FiMMaxComponentsPerFidInhibitionConfiguration