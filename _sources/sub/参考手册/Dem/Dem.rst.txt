===================
Dem
===================



文档信息(Document Information)
=======================================

版本历史(Version History)
-----------------------------------

.. list-table::
   :widths: 10 10 10 10 20
   :header-rows: 1

   * - 日期(Date)
     - 作者(Author)
     - 版本(Version)
     - 状态(Status)
     - 说明(Description)
   * - 2024/11/16
     - peng.wu
     - V0.1
     - 发布(Release)
     - 首次发布(First release)
   * - 2025/04/04
     - peng.wu
     - V1.0
     - 发布(Release)
     - 正式发布(Official release)


参考文档(References)
----------------------------------

.. list-table::
   :widths: 10 12 28 10
   :header-rows: 1

   * - 编号(Number)
     - 分类(Classification)
     - 标题(Title)
     - 版本(Version)
   * - 1
     - Autosar
     - AUTOSAR_CP_SWS_DefaultErrorTracer.pdf
     - R23-11
   * - 2
     - Autosar
     - AUTOSAR_CP_SWS_DiagnosticCommunicationManager.pdf
     - R23-11
   * - 3
     - Autosar
     - AUTOSAR_CP_SWS_DiagnosticEventManager.pdf
     - R23-11
   * - 4
     - Autosar
     - AUTOSAR_CP_SWS_RTE.pdf
     - R23-11
   * - 5
     - Autosar
     - AUTOSAR_FO_TR_Glossary.pdf
     - R23-11
   * - 6
     - Autosar
     - AUTOSAR_CP_SWS_BSWGeneral.pdf
     - R23-11
   * - 7
     - Autosar
     - AUTOSAR_FO_RS_Diagnostics.pdf
     - R23-11
   * - 8
     - Autosar
     - AUTOSAR_CP_SRS_BSWGeneral.pdf
     - R23-11
   * - 9
     - ISO
     - 17356-3.pdf
     - -
   * - 10
     - SAE
     - J1979.pdf
     - -
   * - 11
     - ISO
     - 14229.pdf
     - -


术语与简写(Terms and Abbreviations)
========================================


术语(Terms)
------------------------


.. list-table::
   :widths: 10 40
   :header-rows: 1

   * - 术语(Term)
     - 解释(Explanation)

   * - Aging
     - 老化，在达到一定操作循环的条件后从存储空间中移除(Aging: Removal from storage space after reaching a certain number of operation cycle conditions)

   * - Aging Counter
     - 老化计数器 (Aging Counter)

   * - Application Layer
     - SWC应用层 (SWC Application Layer)

   * - Debounce counter
     - 计数去抖计数器 (Debounce counter)

   * - Dem-internal data value
     - Dem内部数据 (Dem-internal data value)

   * - Diagnostic Channel
     - 诊断仪与ECU的通道，通常指不同的诊断协议，适应不同的总线 (The channel between the diagnostic tool and the ECU, usually referring to different diagnostic protocols adapted to different buses)

   * - Displacement
     - 根据策略用需要存储的更重要的事件替换最不重要的事件 (Replacing the least important event with a more important event that needs to be stored, according to a strategy)

   * - DTC group
     - DTC分组 (DTC group)

   * - DtcGroupAllDtcs
     - DTC全组 (DtcGroupAllDtcs)

   * - Event debouncing
     - 事件去抖 (Event debouncing)

   * - Event confirmation
     - 事件确认(Bit3：CDTC) (Event confirmation (Bit3: CDTC))

   * - Event memory
     - 一个事件存储器由多个事件存储器条目组成 (An event memory consists of multiple event memory entries)

   * - Event memory entry
     - 事件存储器条目 (Event memory entry)

   * - Event memory overflow indication
     - 事件存储器溢出指引 (Event memory overflow indication)

   * - Event related data
     - 事件相关数据(冻结帧、扩展数据) (Event related data (Freeze frame, Extended data))

   * - Event status byte
     - ISO 14229-1 [1] 中定义的状态字节，基于事件级别 (Status byte defined in ISO 14229-1 [1], based on event level)

   * - Extended data record
     - 扩展数据 (Extended data record)

   * - External Diagnostic Tool
     - 外部诊断仪 (External Diagnostic Tool)

   * - Failure counter
     - 故障计数器 (Failure counter)

   * - Fault Detection Counter
     - ISO 和 FDC-API 中使用的 sint8 值 (Fault Detection Counter: sint8 value used in ISO and FDC-API)

   * - Freeze frame
     - 冻结帧 (Freeze frame)

   * - Healing
     - 处理一段时间/几个运行周期内报告的通过后关闭警告指示器 (Turning off the warning indicator after a pass is reported over a period of time/several operation cycles)

   * - Internal Diagnostic Tool
     - 处于总线网络上的Dcm客户端，作用与外部诊断仪相同，但是位于车辆内部 (Dcm client on the bus network, serving the same function as an external diagnostic tool but located inside the vehicle)

   * - Monitor
     - 监视器 (Monitor)

   * - Operating cycle
     - 操作循环 (Operating cycle)

   * - UDS Service
     - UDS服务 (UDS Service)

简写(Abbreviations)
---------------------------

.. list-table::
   :widths: 15 20 25
   :header-rows: 1


   * - 简写(Abbreviation)
     - 全称(Full name) 
     - 解释(Explanation)

   * - BSW
     - Basic Software
     - 基础软件

   * - CDD
     - Complex Device Driver
     - 复杂驱动
   * - CRC
     - Cyclic Redundancy Checkcrc
     - 校验模块
   * - Dcm
     - Diagnostic Communication Manager
     - 诊断通信模块
   * - Dem
     - Diagnostic Event Manager
     - 诊断故障管理模块
   * - Det
     - Default Error Tracer
     - 错误跟踪模块
   * - DID
     - Data Identifier
     - 数据ID
   * - DTC
     - Diagnostic Trouble Code
     - 诊断故障码
   * - DTR
     - Diagnostic Test Result
     - 诊断测试结果
   * - DYC 
     - OBD Term: Driving Cycle
     - (OBD Term)驾驶循环
   * - ECU
     - Electronic Control Unit
     - 电控单元
   * - EcuM
     - Electronic Control Unit Manager
     - 电控单元管理模块
   * - FDC
     - Fault Detection Counter
     - 故障检测计数值
   * - Fim
     - Function Inhibition Manager
     - 功能抑制管理模块
   * - FMI
     - Failure Mode Indicator (SAE J1939)
     - 失败模式灯
   * - FTB
     - Failure Type Byte
     - 失败类型字节
   * - HW
     - Hardware
     - 硬件
   * - ID
     - Identification/Identifier
     - 识别号
   * - ISO
     - International Standardization Organization
     - 国际标准组织
   * - IUMPR
     - In Use Monitoring Performance Ratio (OBD Term)
     - 故障检测率
   * - J1939Dcm
     - SAEJ1939 Diagnostic Communication ManagerJ1939
     - 诊断通信管理模块
   * - MIL
     - Malfunction Indicator Light (SAE J1979) or Lamp (SAE J1939)
     - 故障灯
   * - NVRAM
     - Non volatile RAM
     - 非易失存储
   * - OBD
     - On-Board-Diagnostics
     - 车上诊断
   * - OC
     - Occurrence Count (SAE J1939)
     - 发生计数器
   * - OEM
     - Original Equipment Manufacturer (Automotive Manufacturer)
     - 整车厂
   * - OS
     - Operating System
     - 操作系统
   * - PID
     - Parameter Identification (SAE J1587 or SAE J1979)
     - 参数识别号
   * - PTO
     - Power Take Off
     - 电源下电
   * - RAM
     - Random Access Memory
     - 易失储存
   * - ROM
     - Read-only Memory
     - 只读存储
   * - RTE
     - Runtime Environment
     - 运行时环境
   * - SPN
     - Suspect Parameter Number (SAE J1939)
     - 参数编号
   * - SSCP
     - synchronous server call point
     - 同步调用点
   * - SW
     - Software
     - 软件
   * - SW-C
     - Software Component
     - 软件组件
   * - UDS
     - Unified Diagnostic Services
     - 统一诊断服务
   * - VOBD
     - Vehicle On-Board-Diagnostic
     - 车载诊断
   * - WUC
     - OBD Term: Warm up cycle (OBD Term)
     - 暖机循环
   * - WIR
     - Warning Indicator Request
     - 警告灯请求
   * - WWH-OBD
     - World Wide Harmonized On-Board-Diagnostic
     - 全球统一车载诊断系统

简介(Introduction)
===========================


服务组件Diagnostic Event Manager (Dem)负责处理和存储诊断事件(错误)和相关数据。
此外，Dem向Dcm/J939Dcm提供故障信息(例如，从事件存储器中读取所有存储的dtc)，并且
为应用层和其他BSW模块提供接口。

The service component Diagnostic Event Manager (Dem) is responsible for processing and storing diagnostic events (errors) and related data. In addition, Dem provides fault information to Dcm/J1939Dcm (for example, reading all stored DTCs from the event memory) and offers interfaces for the application layer and other BSW modules.

模块架构如图 :ref:`Dem_AUTOSAR_Arch` 所示，Dem模块按照ISO-14229-1、ISO-15031-5和
SAE-J1939-73等规范实现UDS、OBD和J1939的诊断事件管理及存储功能。
具体实现为：DTC状态管理、冻结帧与扩展数据存储、去抖、恢复与老化、替换等功能。
用户可以通过Dcm或J1939Dcm(J1939事件)中的服务读取或清除事件及其相关数据。
此外，Dem中所有事件及其相关数据的非易失性存储都依赖于NvM。

The module architecture is shown in *DemArchitecture in AUTOSAR*. The Dem module implements the diagnostic event management and storage functions for UDS, OBD, and J1939 in accordance with specifications such as ISO-14229-1, ISO-15031-5, and SAE-J1939-73. The specific implementations include: DTC status management, freeze frame and extended data storage, debouncing, recovery and aging, replacement, etc. Users can read or clear events and their related data through services in Dcm or J1939Dcm (for J1939 events). In addition, the non-volatile storage of all events and their related data in Dem depends on NvM.

.. figure:: ../../../_static/参考手册/Dem/Dem_AUTOSAR_Architecture.png
   :alt: Dem模块层次图 (Dem Module Hierarchy Diagram)
   :name: Dem_AUTOSAR_Arch
   :align: center

   DemArchitecture in AUTOSAR



Dem依赖关系如图 :ref:`Dem_Relationship` 所示，接口的详细内容请参考“接口描述”章节。

The dependencies of Dem are shown in *Demrelationship*. For detailed information about the interfaces, please refer to the "Interface Description" chapter.

.. figure:: ../../../_static/参考手册/Dem/Dem_Relationship.png
   :alt: Dem模块接口关系图
   :name: Dem_Relationship
   :align: center

   Demrelationship


功能描述(Functional Description)
==========================================


特性(Features)
-----------------------

.. only:: doc_pbs
  
  变体(Variants)
  ~~~~~~~~~~~~~~~~~~~~~
.. 支持PBS的模块，必须具有本章节，以功能为导向描述模块级别的变体支持情况
.. 主要功能必须描述，比较偏尽量描述(不强制)

  - DTC值允许在不同变体下使用不同值
  
    DTC values allow the use of different values under different variants
	
  - 事件使能状态在不同变体下使用使能或不使能
  
    The event enable status uses enabled or disabled under different variants
  
  - 事件在同操作循环下failed后允许pass条件在不同变体下使用使能或不使能
  
    After an event fails in the same operation cycle, the allow-pass condition uses enabled or disabled under different variants
	
  - 事件CDTC门限值在不同变体下使用不同值
  
    The event CDTC threshold uses different values under different variants
	
  - DTC组允许在不同变体下使用不同值
    
	DTC groups allow the use of different values under different variants

  - 故障灯行为在不同变体下使用不同值

   The malfunction indicator lamp behavior uses different values under different variants

 - 事件使能状态在不同变体下使用使能或不使能

   The event enable status uses enabled or disabled under different variants

 - 事件在同操作循环下failed后允许pass条件在不同变体下使用使能或不使能

   After an event fails in the same operation cycle, the allow-pass condition uses enabled or disabled under different variants

 - 事件CDTC门限值在不同变体下使用不同值

   The event CDTC threshold uses different values under different variants

 - DTC组允许在不同变体下使用不同值

   DTC groups allow the use of different values under different variants

 - 故障灯行为在不同变体下使用不同值

   The malfunction indicator lamp behavior uses different values under different variants



主卫星功能(Main Satellite Function)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
对于单分区操作系统，Dem主分区提供了服务组件的AUTOSAR接口。
对于多分区操作系统，支持一个Dem主分区和多个卫星分区，每一个Dem分区都提供独有的服务接口。
Dem主分区和卫星分区都运行在可信分区中。Dem的核间通讯采用了共享内存的内部数据进行交换，对受保护内存部分的写访问必须在可信任的分区中。

For a single-partition operating system, the Dem main partition provides the AUTOSAR interface of the service component.
For a multi-partition operating system, one Dem main partition and multiple satellite partitions are supported, and each Dem partition provides a unique service interface.
Both the Dem main partition and satellite partitions run in trusted partitions. The inter-core communication of Dem uses internal data in shared memory for exchange, and write access to the protected memory part must be in the trusted partition.

.. list-table::
   :widths: 10 25
   :header-rows: 1

   * - 功能(Function)
     - 描述(Description)
   
   * - Dem主分区(Dem Main Partition)
     - 作为Dem模块的核心文件，实现Dem模块全部对外接口，以及实现Dem模块功能所必须的local函数，local宏定义，local变量定义。(As the core file of the Dem module, it implements all external interfaces of the Dem module, as well as the local functions, local macro definitions, and local variable definitions necessary for realizing the functions of the Dem module)

   * - Dem卫星分区(Dem Satellite Partition)
     - 主要在本地执行去抖动操作(基于计数器和时间的去抖动)，以及管理分区的监控状态。(Mainly performs debouncing operations locally (counter-based and time-based debouncing) and manages the monitoring status of the partition)


初始化功能(Initialization Function)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
对于单分区操作系统，初始化流程按照AUOTOSAR规范中要求的执行。
对于多分区操作系统，首先在主分区中执行预初始化(Dem_MasterPreInit)加载配置数据，然后预初始化卫星
分区并更新分区的监控状态(Dem_SatellitePreInit)，此时主分区以及卫星分区的状态都为PREINITIALIZED
(预初始化)，分配给各个卫星的事件也可以使用Dem_SetEventStatus向Dem报告监视结果，并在第一个
Dem_Mainfunction调用中排队处理。

For a single-partition operating system, the initialization process is executed in accordance with the requirements specified in the AUTOSAR standard.
For a multi-partition operating system, first, the pre-initialization (Dem_MasterPreInit) is performed in the main partition to load configuration data, and then the satellite partitions are pre-initialized and their monitoring status is updated (Dem_SatellitePreInit). At this point, both the main partition and the satellite partitions are in the PREINITIALIZED state. The events assigned to each satellite can also use Dem_SetEventStatus to report monitoring results to Dem, which will be queued for processing in the first call of Dem_Mainfunction.


当NvM读取完Dem的存储数据后，将Dem所有功能全部初始化(Dem_MasterInit)，然后初始化各个卫星
(Dem_SatelliteInit)，此时主分区以及卫星分区的状态都为INITIALIZED(已初始化)。
若系统已经调用Dem_Shutdown之后，Dem_MasterInit接口还可以用于重新初始化主分区。

After NvM finishes reading the stored data of Dem, all functions of Dem are fully initialized (Dem_MasterInit), and then each satellite is initialized (Dem_SatelliteInit). At this time, both the main partition and the satellite partitions are in the INITIALIZED state.
If the system has called Dem_Shutdown, the Dem_MasterInit interface can still be used to re-initialize the main partition.



诊断事件报告(Diagnostic Event Reporting)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
诊断事件是指在一个SWC或BSW模块中的监控的结果，报告的状态可以是Failed、Passed、PreFailed或PrePassed，
SWC与BSW通过Dem_SetEventStatus向Dem报告事件及其状态并存入Dem内部队列中，在下一个Dem_MainFunction中
处理队列中的事件，包括处理内部Memory Entry空间分配以及事件DTC状态切换等，并且将事件及其相关状态和数据
放入对应的Memory Entry中。

A diagnostic event refers to the monitoring result within a SWC or BSW module. The reported status can be Failed, Passed, PreFailed, or PrePassed.
SWCs and BSW modules report events and their status to Dem via the Dem_SetEventStatus API, which are stored in Dem's internal queue. In the next Dem_MainFunction cycle, the queued events are processed. This processing includes handling the allocation of internal Memory Entry space, switching the event DTC status, and placing the event along with its associated status and data into the corresponding Memory Entry.


去抖功能(Debounce Function)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
当报告事件状态为PREPASSED(或PREFAILED)时，需要进行去抖处理来确认事件的状态为PASSED或FAILED。去抖可分为
基于计数去抖和基于时间去抖。当报告的事件状态为PREFAILED或PREPASSED时，在Dem_MainFunction中的内部函数
Dem_DebounceCounterCalculate/Dem_DebounceTimeCalculate里开始根据配置进行计数，当报告PREFAILED或
PREPASSED状态的事件的计数值/超时值达到配置的阈值时，事件状态将被确认为FAILED或PASSED。

When the reported event status is PREPASSED (or PREFAILED), debounce processing is required to confirm the event status as PASSED or FAILED. Debouncing can be categorized into counter-based debouncing and time-based debouncing. When an event is reported with PREFAILED or PREPASSED status, the internal functions Dem_DebounceCounterCalculate and Dem_DebounceTimeCalculate within Dem_MainFunction begin counting according to the configuration. When the count value or timeout value for the event reporting PREFAILED or PREPASSED status reaches the configured threshold, the event status is confirmed as FAILED or PASSED.


DTC状态管理(DTC Status Management)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
每个事件都支持一个DTC状态，分为8个Bit状态位，Dem初始化时，会将每个配置的事件的DTC状态进行初始化，
当SWC或BSW报告事件后，将通过Dem_MainFunction中异步执行计算。

Each event supports a DTC status, which consists of 8 status bits. During Dem initialization, the DTC status for each configured event is initialized. After an event is reported by a SWC or BSW module, the status bit calculations are performed asynchronously within the Dem_MainFunction.


.. list-table::
   :widths: 5 15 10 20
   :header-rows: 1

   * - 位(Bit)
     - 名称(Name)
     - 缩写(Abbreviation)
     - 说明(Description)
   
   * - Bit 0
     - TesetFailed
     - TF
     - 表示最近一次测试的测试结果(Indicates the test result of the most recent test)

   * - Bit 1
     - TestFailedThisOperationCycle
     - TFTOC
     - 在开启的操作循环内，事件是否被判定为失败(Indicates whether the event has been judged as failed within the current operation cycle)

   * - Bit 2
     - PendingDTC
     - PDTC
     - 在过去或当前的操作循环中，如果事件被判定为失败，并且自从报告了失败结果以来，它的整个周期内都没有测试通过(Indicates that the event was judged as failed in a past or current operation cycle and has not passed the test throughout its entire cycle since the failure was reported)

   * - Bit 3
     - ComfirmedDTC
     - CDTC
     - 表示事件已被确认且被存储(Indicates that the event has been confirmed and stored)

   * - Bit 4
     - TestNotCompleteSinceLastClear
     - TNCSLC
     - 自故障存储已被清除后事件是否已被确认(通过或失败)(Indicates whether the event has been confirmed (passed or failed) since the fault memory was last cleared)

   * - Bit 5
     - TestFailedSinceLastClear
     - TFSLC
     - 自从上次清除故障后该事件是否被标记为失败(Indicates whether the event has been marked as failed since the fault memory was last cleared)

   * - Bit 6
     - TestNotCompleteThisOperationCycle
     - TNCTOC
     - 事件在开启的操作循环内是否已经被确认(通过或失败)(Indicates whether the event has been confirmed (passed or failed) within the current operation cycle)

   * - Bit 7
     - WarnningIndicator
     - WIR
     - 表示出此事件的warning indicator是否激活(Indicates whether the warning indicator for this event is activated)


冻结帧和扩展数据(Freeze Frame and Extended Data)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
ISO-14229-1规定了两种类型的诊断事件相关数据：冻结帧与扩展数据。数据可以以冻结帧和扩展数据的形式与每个DTC一起存储。

ISO-14229-1 specifies two types of diagnostic event-related data: freeze frame and extended data. Data can be stored together with each DTC in the form of freeze frames and extended data.

.. list-table::
   :widths: 10 25
   :header-rows: 1

   * - 功能(Function)
     - 说明(Description)
   
   * - 冻结帧(Freeze Frame)
     - 包括一个或多个DID(数据标识符)，每个DID又包括一个或多个数据元素。冻结帧在事件确认期间的可配置时间点进行收集和存储，通常会多次存储。(Consists of one or more DIDs (Data Identifiers), each of which contains one or more data elements. Freeze frames are collected and stored at configurable time points during event confirmation and are typically stored multiple times)

   * - 扩展数据(Extended Data)
     - 包括一个或多个数据元素，通常用于统计数值(Consists of one or more data elements, typically used for statistical values)

SWC与BSW报告事件时，Dem根据配置DemExtendedDataRecordTrigger与DemFreezeFrameRecordTrigger决定在哪种条件下获取实时
扩展数据与冻结帧，并且与事件一同存入buffer中。接着在Dem_MainFunction中等待事件的Memory Entry分配完成后，将数据存储到其中。

When an SWC or BSW module reports an event, Dem determines under which conditions to acquire real-time extended data and freeze frames based on the configurations of DemExtendedDataRecordTrigger and DemFreezeFrameRecordTrigger. This data is stored in a buffer together with the event. Subsequently, during the Dem_MainFunction execution, after the Memory Entry allocation for the event is completed, the data is stored into it.


恢复与老化功能(Recovery and Aging Functions)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 10 25
   :header-rows: 1

   * - 功能(Function)
     - 说明(Description)
   
   * - 诊断事件的恢复(Recovery of Diagnostic Events)
     - 某事件已经报告了故障，在经过后续操作循环监测下没有继续报告故障，满足恢复条件，则认为事件已经恢复(If an event has reported a fault and no further faults are reported during subsequent operation cycle monitoring, and the recovery conditions are met, the event is considered recovered)

   * - 诊断事件的老化(Aging of Diagnostic Events)
     - 在当前事件满足恢复条件并且在经过后续操作循环监测下没有继续报告故障，满足老化条件，则开始老化处理(If the current event meets the recovery conditions and no further faults are reported during subsequent operation cycle monitoring, and the aging conditions are met, aging processing is initiated)

恢复：指事件在当前操作循环报告状态为FAILED并且置位了DTC状态位Bit7，后续的操作循环中此事件仅报告了PASSED状态，并在
Dem_OperationCycleRestart中开始执行恢复处理，若在某一个操作循环开启时满足恢复条件则将DTC状态位Bit7清除。恢复条件由
配置中DemIndicatorHealingCycleCounterThreshold的值决定。

Recovery: This refers to a situation where an event reports a FAILED status in the current operation cycle and DTC status bit Bit7 is set. In subsequent operation cycles, if the event only reports a PASSED status, recovery processing begins in Dem_OperationCycleRestart. If the recovery conditions are met at the start of an operation cycle, DTC status bit Bit7 is cleared. The recovery conditions are determined by the value of DemIndicatorHealingCycleCounterThreshold in the configuration.

老化：指事件满足恢复条件并且后续的操作循环中事件继续仅报告PASSED状态，在内部函数Dem_OperationCycleEnd中进行老化处
理，若在某一个操作循环关闭时满足老化条件则将清除DTC状态位Bit3、Bit5，并且删除此事件所有相关的数据，老化条件由配置中
DemAgingCycleCounterThreshold的值决定。若配置DemStatusBitHandlingTestFailedSinceLastClear允许清除Bit5，清除时
机由配置中DemAgingCycleCounterThresholdForTFSLC的值决定。

Aging: This refers to a situation where an event meets the recovery conditions and continues to report only a PASSED status in subsequent operation cycles. Aging processing is performed in the internal function Dem_OperationCycleEnd. If the aging conditions are met at the end of an operation cycle, DTC status bits Bit3 and Bit5 are cleared, and all data related to this event is deleted. The aging conditions are determined by the value of DemAgingCycleCounterThreshold in the configuration. If the configuration item DemStatusBitHandlingTestFailedSinceLastClear allows clearing Bit5, the clearing timing is determined by the value of DemAgingCycleCounterThresholdForTFSLC in the configuration.


替换功能(Replacement Function)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
诊断事件的替换功能是指若在配置中配置的事件数量大于配置的存储数量，则最不重要的、已经存在的事件的Memory Entry被需要
存储的新事件的Memory Entry取代。
若SWC或BSW向Dem报告了尚未存储新的事件，且此时Dem内部分配的Memory Entry已经达到了配置中的最大值，则在内部函数
Dem_EventDisplacementProcess中进行替换处理。执行替换处理后，Dem将把“最不重要”的事件相关的数据删除，更新此事件相关
的DTC状态。此外，AutoSAR规定事件替换只能由高优先级事件替换低优先级事件。
以下是事件替换的三种策略介绍：

The replacement function for diagnostic events means that if the number of configured events exceeds the configured storage capacity, the Memory Entry of the least important existing event is replaced by the Memory Entry of the new event that needs to be stored.
If an SWC or BSW module reports a new, not yet stored event to Dem, and the internally allocated Memory Entries in Dem have reached the configured maximum, replacement processing is performed in the internal function Dem_EventDisplacementProcess. After replacement processing, Dem deletes the data related to the "least important" event and updates the DTC status associated with that event. Furthermore, AUTOSAR stipulates that event replacement can only occur where a higher-priority event replaces a lower-priority event.
The following introduces three strategies for event replacement:

.. list-table::
   :widths: 5 30
   :header-rows: 1

  
   * - 策略(Strategy)
     - 解释(Explanation)
   
   * - DEM_DISPLACEMENT_NONE
     - 不执行替换(No replacement is performed)

   * - DEM_DISPLACEMENT_FULL
     - 优先寻找Passive状态的事件，若所有已存储的事件状态都为Active，则按照Occurrence(故障产生的时间最长)来找到将被新事件替换的旧事件。(Active/Passive：事件的DTC状态是否为Failed/Passed)(Priority is given to finding events in the Passive state. If all stored events are in the Active state, the old event to be replaced by the new event is identified based on Occurrence (the event with the longest time since the fault occurred). (Active/Passive: Indicates whether the DTC status of the event is Failed/Passed))

   * - DEM_DISPLACEMENT_PRIO_OCC
     - 先寻找Priority最低的事件，若所有已存储的旧事件的Priority相同，则按照Occurrence(故障产生的时间最长)来找到将被新事件替换的旧事件(First, the event with the lowest Priority is sought. If all stored old events have the same Priority, the old event to be replaced by the new event is identified based on Occurrence (the one with the longest time since the fault occurred))


事件存储管理功能(Event Storage Management Function)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
诊断事件的相关数据可以通过NvM模块读写存储单元中的数据，上电初始化时调用Dem_NvMMemoryInit将NvM读取的admin、entry数据
更新到Dem模块中，在下电时调用Dem_NvmShutdown将Dem的数据写入存储单元。如果不使用AUTOSAR NvM模块，则必须提供一个兼容的
存储功能替代品，以便使用与非易失性数据管理相关的功能。
Dem只会触发少量的NvM写操作，所以ECU在运行时通常只存储变化不频繁的数据，如果需要多次触发NvM的写频率，则需要通过配置项
(Dem/DemConfigSet/DemDTC/DemNvStorageStrategy)，使能Dem立即写功能。

The relevant data of diagnostic events can be read from and written to the storage unit via the NvM module. During power-on initialization, Dem_NvMMemoryInit is called to update the admin and entry data read by NvM into the Dem module. During power-off, Dem_NvmShutdown is called to write the Dem data into the storage unit. If the AUTOSAR NvM module is not used, a compatible alternative storage function must be provided to utilize features related to non-volatile data management.
Dem triggers only a minimal number of NvM write operations. Therefore, the ECU typically stores only infrequently changing data during operation. If it is necessary to trigger NvM write operations more frequently, the Dem immediate write function must be enabled via the configuration item (Dem/DemConfigSet/DemDTC/DemNvStorageStrategy).


操作循环功能(Operation Cycle Function)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
每个事件都分配给一个操作循环，只有当相应的操作循环已启动时，才可以向Dem报告事件，一个操作循环可以通过函数
Dem_OperationCycleSetReStart启动和停止。Dem在初始化时只设置对应操作循环的flag初始值，以及使能操作循环
的接口，并且重启操作循环会调用很多DTC的回调接口，所以操作循环的启动和停止功能是在主函数中异步执行的。

Each event is assigned to an operation cycle. Events can only be reported to the Dem module if their corresponding operation cycle is active (started). An operation cycle can be started and stopped through the function Dem_OperationCycleSetReStart. During initialization, Dem only sets the initial value of the flag for the corresponding operation cycle and enables the interface of the operation cycle. Moreover, restarting the operation cycle will call many DTC callback interfaces, so the start and stop functions of the operation cycle are executed asynchronously in the main function.


使能条件功能(Enable Condition Function)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
使能条件被定义为一组分配给特定条件的参数。只要这个条件没有得到满足，事件报告(参考Dem_SetEventStatus)就无效，因此不会被接受。
调用Dem_EnableConditionInit激活使能条件后，在主函数中调用Dem_EnableConditionTask异步执行使能条件的功能。

An enable condition is defined as a set of parameters assigned to a specific logical state. As long as this condition is not met, event reports (refer to Dem_SetEventStatus) are invalid and will not be accepted.
After calling Dem_EnableConditionInit to activate an enable condition, the functionality of the enable condition is executed asynchronously by calling Dem_EnableConditionTask in the main function.


存储条件功能(Storage Condition Function)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
存储条件被定义为一组分配给特定条件的参数。只要这个条件没有得到满足，Dem模块就不会将事件存储到事件存储器中。
调用Dem_StorageConditionInit初始化存储条件的状态以及激活存储条件的功能。

A storage condition is defined as a set of parameters assigned to a specific logical state. As long as this condition is not met, the Dem module will not store the event in the event memory.
Call Dem_StorageConditionInit to initialize the status of the storage condition and activate its functionality.


J1939功能 J1939(Function)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Dem模块能够支持J1939协议栈，支持J1939定义的特定冻结帧，每个DTC可以被单独配置为支持冻结帧和/或扩展冻结帧。
Lamp支持Malfunction Indicator Lamp(MIL), Red Stop Lamp(RSL), Amber Warning Lamp(AWL), Protect Lamp(PL),
这些Lamp的行为支持：闪烁、持续闪烁、持续、快闪和慢闪等。
调用函数Dem_J1939DcmClearDTC可以清除与指定的J1939 DTC相关的所有事件的状态，以及这些事件的所有关联事件内存条目。

The Dem module can support the J1939 protocol stack and the specific freeze frames defined by J1939. Each DTC can be individually configured to support freeze frames and/or extended freeze frames.
The supported lamp types include Malfunction Indicator Lamp (MIL), Red Stop Lamp (RSL), Amber Warning Lamp (AWL), and Protect Lamp (PL).
The supported lamp behaviors include: flashing, continuous flashing, steady illumination, fast flashing, and slow flashing, among others.
Calling the function Dem_J1939DcmClearDTC clears the status of all events associated with the specified J1939 DTC, as well as all associated event memory entries for these events.


Clear DTC功能(Clear DTC Function)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
不同客户端可通过调用Dem_ClearDTC清除DTC相关的所有事件的状态、关联事件内存条目等。清除过程是在主函数中异步执行的，
当一个清除操作正在进行时：

Different clients can clear the status of all events related to a DTC, along with their associated event memory entries, by calling Dem_ClearDTC. The clearing process is executed asynchronously in the main function.
When a clearing operation is in progress:

 #. 来自不同客户端的清除请求会收到DEM_CLEAR_BUSY响应

    Clearing requests from different clients will receive a DEM_CLEAR_BUSY response.

 #. 来自同一客户端的清除请求会收到DEM_CLEAR_PENDING响应
  
    Clearing requests from the same client will receive a DEM_CLEAR_PENDING response.


偏差(Deviation)
------------------------
.. 有序列表示例

 #. 诊断事件依赖以及组件可用性(Diagnostic Event Dependencies and Component Availability)

   AUTOSAR规范中的7.3.6章节(事件依赖关系)，7.3.7章节(组件可用性)暂未实现。

   The functionalities described in AUTOSAR specification chapters 7.3.6 (Event Dependencies) and 7.3.7 (Component Availability) are currently not implemented.

 #. DTC组合事件(DTC Combination Events)

   暂不支持DTC组合事件，Dem/DemGeneral/DemEventCombinationSupport配置项暂不支持配置，默认值为DEM_EVCOMB_DISABLED。

   DTC combination events are not currently supported. The configuration parameter Dem/DemGeneral/DemEventCombinationSupport is not configurable and defaults to DEM_EVCOMB_DISABLED.

 #. 依赖操作周期(Dependent Operation Cycles)

   暂不支持依赖操作周期功能，Dem/DemGeneral/DemOperationCycle/DemLeadingCycleRef配置项暂不支持配置，设置该参数时，
   操作周期被视为依赖操作周期。每当参数未设置时，操作周期被视为“普通”操作周期。

   Dependent operation cycle functionality is not currently supported. The configuration parameter Dem/DemGeneral/DemOperationCycle/DemLeadingCycleRef is not configurable. When this parameter is set, the operation cycle is treated as a dependent operation cycle. When the parameter is not set, the operation cycle is considered a "normal" operation cycle.

 #. DemRatio功能(DemRatio Function)

   暂不支持DemRatio功能，Dem/DemGeneral/DemRatio暂不支持配置。

   The DemRatio function is not currently supported, and the Dem/DemGeneral/DemRatio parameter is not configurable.

 #. OBD相关功能(OBD-Related Functions)

   AUTOSAR规范中的7.9章节的ODB相关功能暂未实现。

   OBD-related functions specified in Chapter 7.9 of the AUTOSAR specification are not yet implemented.

 #. Replacement诊断事件(Replacement Diagnostic Events)

   AUTOSAR规范中的7.6章节中的replacement功能暂未实现，Dem/DemGeneral/DemStorageCondition/
   DemStorageConditionReplacementEventRef配置项暂不支持配置。

   The replacement function described in Chapter 7.6 of the AUTOSAR specification is not yet implemented. The configuration parameter Dem/DemGeneral/DemStorageCondition/DemStorageConditionReplacementEventRef is not currently configurable.

 #. J1939 Readiness功能(J1939 Readiness Function)

   AUTOSAR规范中的7.10.5章节中的Readiness功能只实现了Dem_J1939DcmReadDiagnosticReadiness1，其余Readiness功能暂未实现。

   Among the Readiness functions in Chapter 7.10.5 of the AUTOSAR specification, only Dem_J1939DcmReadDiagnosticReadiness1 has been implemented. The remaining Readiness functions are not yet available.

 #. 多事件触发(Multiple Event Triggers)

   每当报告一个配置的事件时将触发其他事件。暂不实现。

   The feature to trigger other events upon reporting a configured event, which is not currently implemented.


扩展(Extension)
-----------------------------------------
#. Dem与NvM Block的同步功能(Synchronization Function between Dem and NvM Block)

   诊断事件的同步功能指的是Dem一键在DemNvRamBlockId下创建reference关系，同时在NvM模块生成相应的NvMBlock。同步功能会根据
   Dem的配置自动计算Dem所需Block的长度与个数。选择同步功能会自动在NvM模块创建相应的NvMBlock。Dem支持event分开存储，
   会创建 DemMaxNumberEventEntryPrimary + DemMaxNumberEventEntryPermanent个NvMBlock，每个NvMBlock用来单独存放发生
   故障的event状态信息、扩展数据、冻结帧数据等。

   The synchronization function for diagnostic events allows Dem to create a reference relationship under DemNvRamBlockId with one click, while simultaneously generating the corresponding NvMBlock in the NvM module. This function automatically calculates the length and number of Blocks required by Dem based on its configuration. Selecting the synchronization function will automatically create the corresponding NvMBlock in the NvM module. Dem supports separate storage of events and will create (DemMaxNumberEventEntryPrimary + DemMaxNumberEventEntryPermanent) NvMBlocks. Each NvMBlock is used to individually store the status information, extended data, freeze frame data, etc., of a faulted event.

#. Dem模块的可选功能(Optional Functions of the Dem Module)

   在Dem_OptMacros.h文件中，定义了一些可选功能的宏定义，例如使用C标准库的memcpy功能，使用NvM轮询功能，清除时在一个主函数
   周期内需要扫描的事件数目，使用用户定义的同步功能等。用户可根据实际应用场景，在此文件中设置宏定义开关，打开对应的功能。

   In the Dem_OptMacros.h file, macro definitions for some optional functions are defined, such as using the C standard library's memcpy function, using the NvM polling function, the number of events that need to be scanned within one main function cycle during clearing, and using user-defined synchronization functions. Users can set the macro definition switches in this file according to their actual application scenarios to enable the corresponding functions.


集成(Integration)
============================

初始化(Initialization)
---------------------------
#. Dem单分区或无分区(Dem Single Partition or No Partition)

   集成时需要EcuM与BswM进行分步初始化，预初始化和初始化流程如下：1、首先调用Dem_PreInit进行预初始化；2、初始化存储栈，调用NvM_ReadAll；
   3、等NvM_ReadAll结束(多块通知结果不为PENDING)后调用Dem_Init。

   During integration, EcuM and BswM are required to perform step-by-step initialization. The pre-initialization and initialization process is as follows: 1. First, call Dem_PreInit for pre-initialization; 2. Initialize the storage stack and call NvM_ReadAll; 3. After NvM_ReadAll completes (the multi-block notification result is not PENDING), call Dem_Init.

#. Dem多分区(Dem Multiple Partitions)

   需要EcuM与BswM进行不同分区的预初始化和初始化。(注意：Dem多分区初始化情况下会调用GetCurrentApplicationID接口，该接口需要OS启动后才能调用)
   如诊断测试工程中，配置了分区0(主分区master分区)和分区1，预初始化和初始化流程如下：1、首先进行分区0(主分区master分区)的预初始化，调用Dem_PreInit；
   2、在主分区初始化完成后调用其他分区上卫星分区的预初始化Dem_SatellitePreInit接口；3、初始化存储栈，调用NvM_ReadAll，等NvM_ReadAll结束(多块通知结果不为PENDING)
   后调用Dem分区0(主分区master分区)初始化Dem_Init；4、在主分区初始化完成后，调用其他分区上卫星分区的初始化Dem_SatelliteInit接口。

   EcuM and BswM are required to perform pre-initialization and initialization for different partitions. (Note: In the case of Dem multi-partition initialization, the GetCurrentApplicationID interface is called, which can only be invoked after the OS has started.) For example, in a diagnostic test project where Partition 0 (master partition) and Partition 1 are configured, the pre-initialization and initialization process is as follows: 1. First, perform pre-initialization for Partition 0 (master partition) by calling Dem_PreInit; 2. After the master partition initialization is complete, call the Dem_SatellitePreInit interface for pre-initialization of satellite partitions on other partitions; 3. Initialize the storage stack, call NvM_ReadAll, and after NvM_ReadAll completes (the multi-block notification result is not PENDING), call Dem_Init for Dem Partition 0 (master partition); 4. After the master partition initialization is complete, call the Dem_SatelliteInit interface for initialization of satellite partitions on other partitions.


文件列表(File List)
-------------------------------

静态文件(Static Files)
~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - 文件(File)
     - 描述(Description)

   * - Dem_Cbk.h
     - Dem模块与NvM交互的外部接口函数声明(Declaration of external interface functions for interaction between Dem module and NvM)

   * - Dem_Dcm.h
     - Dem模块与Dcm交互的外部接口函数声明(Declaration of external interface functions for interaction between Dem module and Dcm)

   * - Dem_J1939Dcm.h
     - Dem模块与J1939Dcm交互的外部接口函数声明(Declaration of external interface functions for interaction between Dem module and J1939Dcm)

   * - Dem_OptMacros.h
     - Dem模块可选功能宏定义(Macro definitions for optional functions of Dem module)

   * - Dem_Types.h
     - Dem模块标准类型定义(Standard type definitions for Dem module)

   * - Dem.h
     - Dem模块外部接口函数声明(Declaration of external interface functions for Dem module)

   * - Dem_APIImplementation.h
     - Dem模块外部接口函数实现(Implementation of external interface functions for Dem module)

   * - Dem_ClearDTC.h
     - Dem模块清除DTC相关功能函数实现(Implementation of functions related to DTC clearing in Dem module)

   * - Dem_Client.h
     - Dem模块客户端相关功能函数实现(Implementation of functions related to client in Dem module)

   * - Dem_DataElement.h
     - Dem模块原始数据获取相关功能函数实现(Implementation of functions related to raw data acquisition in Dem module)

   * - Dem_DcmAPIImplementation.h
     - Dem模块与Dcm相关的外部接口函数实现(Implementation of external interface functions related to Dcm in Dem module)

   * - Dem_Debounce.h
     - Dem模块去抖相关功能函数实现(Implementation of functions related to debouncing in Dem module)

   * - Dem_Dtc.h
     - Dem模块DTC处理相关功能函数实现(Implementation of functions related to DTC processing in Dem module)

   * - Dem_DtcInterface.h
     - Dem模块DTC处理相关功能函数声明(Declaration of functions related to DTC processing in Dem module)

   * - Dem_EnableCondition.h
     - Dem模块使能条件处理相关功能函数实现(Implementation of functions related to enable condition processing in Dem module)

   * - Dem_Error.h
     - Dem模块错误处理相关功能函数实现(Implementation of functions related to error handling in Dem module)

   * - Dem_Event.h
     - Dem模块事件处理相关功能函数实现(Implementation of functions related to event processing in Dem module)

   * - Dem_EventInterface.h
     - Dem模块事件处理相关功能函数声明(Declaration of functions related to event processing in Dem module)

   * - Dem_ExtendedData.h
     - Dem模块扩展数据处理相关功能函数实现(Implementation of functions related to extended data processing in Dem module)

   * - Dem_FreezeFrame.h
     - Dem模块冻结帧处理相关功能函数实现(Implementation of functions related to freeze frame processing in Dem module)

   * - Dem_Indicator.h
     - Dem模块故障灯处理相关功能函数实现(Implementation of functions related to malfunction indicator processing in Dem module)

   * - Dem_InitState.h
     - Dem模块初始化状态处理相关功能函数实现(Implementation of functions related to initialization state processing in Dem module)

   * - Dem_Int.h
     - Dem模块内部宏定义(Internal macro definitions for Dem module)

   * - Dem_J1939.h
     - Dem模块与J1939Dcm相关的外部接口函数实现以及J1939相关功能函数实现(Implementation of external interface functions related to J1939Dcm and functions related to J1939 in Dem module)

   * - Dem_Master.h
     - Dem模块主星处理相关功能函数实现(Implementation of functions related to master processing in Dem module)

   * - Dem_MasterInterface.h
     - Dem模块主星处理相关功能函数声明(Declaration of functions related to master processing in Dem module)

   * - Dem_MasterSatelliteCom.h
     - Dem模块主卫星通信处理相关功能函数实现(Implementation of functions related to master-satellite communication processing in Dem module)

   * - Dem_Mem.h
     - Dem模块数据存储处理相关功能函数实现(Implementation of functions related to data storage processing in Dem module)

   * - Dem_MemInterface.h
     - Dem模块数据存储处理相关功能函数声明(Declaration of functions related to data storage processing in Dem module)

   * - Dem_MemMap.h
     - Dem模块内存映射定义(Memory map definitions for Dem module)

   * - Dem_Obd.h
     - Dem模块OBD处理相关功能函数实现(Implementation of functions related to OBD processing in Dem module)

   * - Dem_OperationCycle.h
     - Dem模块操作循环处理相关功能函数实现(Implementation of functions related to operation cycle processing in Dem module)

   * - Dem_PreStore.h
     - Dem模块预存储冻结帧处理相关功能函数实现(Implementation of functions related to pre-storage freeze frame processing in Dem module)

   * - Dem_Queue.h
     - Dem模块队列处理相关功能函数实现(Implementation of functions related to queue processing in Dem module)

   * - Dem_Satellite.h
     - Dem模块卫星处理相关功能函数实现(Implementation of functions related to satellite processing in Dem module)

   * - Dem_SatelliteInterface.h
     - Dem模块卫星处理相关功能函数声明(Declaration of functions related to satellite processing in Dem module)

   * - Dem_StorageCondition.h
     - Dem模块存储条件处理相关功能函数实现(Implementation of functions related to storage condition processing in Dem module)

   * - Dem.c
     - Dem模块源码文件入口(Main source file for the Dem module)


动态文件(Dynamic Files)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - 文件(File)
     - 描述(Description)

   * - Dem_Cfg.h
     - Dem模块PC配置宏定义(PC configuration macro definitions for the Dem module)

   * - Dem_Lcfg.c
     - Dem模块非PB配置数据变量定义(Definition of non-PB configuration data variables for the Dem module)

   * - Dem_Lcfg.h
     - Dem模块非PB配置数据变量声明、宏定义(Declaration of non-PB configuration data variables and macro definitions for the Dem module)

   * - Dem_PBcfg.c
     - Dem模块PB配置数据变量定义(Definition of PB configuration data variables for the Dem module)

   * - Dem_PBcfg.h
     - Dem模块PB配置数据变量声明(Declaration of PB configuration data variables for the Dem module)

   * - Rte_Dem_Type.h
     - Dem模块实现数据类型定义(Definition of implementation data types for the Dem module)


错误处理(Error Handling)
--------------------------------

开发错误(Development Errors)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. list-table:: 
   :widths: 20 10 30
   :header-rows: 1

   * - Error code
     - Value[hex]
     - Description

   * - DEM_E_NO_ERROR
     - 0x0u
     - API function called with no det error

   * - DEM_E_WRONG_CONFIGURATION
     - 0x10u
     - API function called with a parameter value, which is not allowed by active configuration

   * - DEM_E_PARAM_POINTER
     - 0x11u
     - API function called with a NULL pointer

   * - DEM_E_PARAM_DATA
     - 0x12u
     - API function called with wrong parameter value

   * - DEM_E_PARAM_LENGTH
     - 0x13u
     - API function called with wrong length parameter value

   * - DEM_E_INIT_FAILED
     - 0x14u
     - Dem initialisation failed

   * - DEM_E_UNINIT
     - 0x20u
     - API function called before the Dem module has been full initialized or after the Dem module has been shut down

   * - DEM_E_WRONG_CONDITION
     - 0x40u
     - Required conditions for the respective API call are not fulfilled

   * - DEM_E_INVALID_OBDMID
     - 0x50u
     - Dem_DcmGetAvailableOBDMIDs called with invalid OBDMID


运行时错误(Runtime Errors)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: 
   :widths: 20 10 30
   :header-rows: 1

   * - Error code
     - Value[hex]
     - Description

   * - DEM_E_UDS_STATUS_PROCESSING_FAILED
     - 0x21u
     - The UDS status corresponding to a changed monitor status could not be processed

   * - DEM_E_NODATAAVAILABLE
     - 0x30u
     - No valid data for data element available by SW-C or BSW call

.. 引用接口描述。来自于code->doxygen->latex->rst
.. include:: Dem_h_api.rst
.. include:: Dem_Cbk_h_api.rst
.. include:: Dem_Dcm_h_api.rst
.. include:: Dem_J1939Dcm_h_api.rst


依赖的服务(Dependent Services)
-----------------------------------------

可选接口(Optional Interfaces)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 10 5 30
   :header-rows: 1

   * - API Function
     - Header File
     - Description

   * - Dcm_DemTriggerOnDTCStatus 
     - Dcm_Dem.h
     - Triggers on changes of the UDS status byte. Allowsto trigger on ROE Event for subservice On DTCStatusChanged.

   * - Det_ReportError 
     - Det.h
     - Service to report development errors.

   * - FiM_DemInit
     - FiM_Dem.h
     - This service re-initializes the FIM.

   * - FiM_DemTriggerOnComponentStatus
     - FiM_Dem.h
     - Triggers on changes of the component failed status.

   * - FiM_DemTriggerOnMonitorStatus
     - FiM_Dem.h
     - This service is provided to be called by the Dem in order to inform the Fim about monitor status changes.

   * - J1939Dcm_DemTriggerOnDTCStatus
     - J1939Dcm_Dem.h
     - Trigger for DM01 message that a UDS status change has happened.

   * - NvM_GetErrorStatus
     - NvM.h
     - Service to read the block dependent error/status information.

   * - NvM_ReadBlock
     - NvM.h
     - Service to copy the data of the NV block to its corresponding RAM block.

   * - NvM_SetRamBlockStatus
     - NvM.h
     - Service for setting the RAM block status of a permanent RAM block or the status of the explicit synchronization of a NVRAM block.

   * - NvM_WriteBlock
     - NvM.h
     - Service to copy the data of the RAM block to its corresponding NV block.


配置接口(Configure Interfaces)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 10 5 30
   :header-rows: 1

   * - API Function
     - Header File
     - Description

   * - <Module>_DemInitMonitorFor<EventName> 
     - Dem_Lcfg.h
     - Inits the diagnostic monitor of a specific event. There is one separate callback per event (if configured), if no port interface is provided by the Dem.

   * - <Module>_DemTriggerOnComponentStatus
     - Dem_Callback.h
     - Triggers on changes of the DemComponent failed status.

   * - <Module>_ClearDtcNotification
     - Dem_Callback.h
     - Called by the Dem when performing a clear DTC operation.

   * - <Module>_DemGeneralTriggerOnMonitorStatus
     - Dem_Callback.h
     - Triggers on changes of the monitor status. Called synchronously in context of event status reporting.

   * - <Module>_DemGeneralTriggerOnEventUdsStatus
     - Dem_Lcfg.h
     - Triggers on changes of the UDS DTC status byte.

   * - <Module>_DemTriggerOnEventUdsStatus
     - Dem_Callback.h
     - Triggers on changes of the UDS DTC status byte.

   * - <Module>_DemTriggerOnDTCStatus
     - Dem_Lcfg.h
     - Triggers on changes of the UDS status byte.

   * - <Module>_DemTriggerOnMonitorStatus
     - Dem_Lcfg.h
     - Triggers on changes of the monitor status. Called synchronously in context of event status reporting.

   * - <Module>_DemTriggerOnEventData
     - Dem_Lcfg.h
     - Triggers on changes of the event related data in the event memory.

   * - <Module>_DemClearEventAllowed<ForCondition>
     - Dem_Lcfg.h
     - Triggers on DTC-deletion, which is not allowed if the out-parameter returns False. There is one
       separate callback per condition, which can be assigned to one or several events, if no port
       interface is provided by the Dem. Parameter "Allowed" will be unchanged in case E_NOT_OK is returned.

   * - <Module>_DemRead<DataElement>
     - Dem_Callback.h
     - Requests the current value of the data element. There is one separate callback per data element, if no port interface is provided by the Dem.

   * - <Module>_DemGetFaultDetectionCounter<ForEvent>
     - Dem_Lcfg.h
     - Gets the current fault detection counter value. There is one c-callback per event using monitor-internal debouncing, if no port interface is provided by the Dem.


配置(Configuration)
===========================

主卫星分区 Master-Satellite(Partition)
------------------------------------------------

如图 :ref:`DemMasterEcucPartitionRef` 所示，在Dem/DemGeneral/DemMasterEcucPartitionRef配置master Partition。

As shown in DemMasterEcucPartitionRef, configure the master Partition in Dem/DemGeneral/DemMasterEcucPartitionRef.

.. figure:: ../../../_static/参考手册/Dem/DemMasterEcucPartitionRef.png
   :alt: DemMasterEcucPartitionRef配置图(DemMasterEcucPartitionRef Configuration Diagram)
   :name: DemMasterEcucPartitionRef
   :align: center

   DemMasterEcucPartitionRef

如图 :ref:`DemEventEcucPartitionRef` 所示，在每一个event下可以配置对应的Partition。

As shown in DemEventEcucPartitionRef Config, the corresponding Partition can be configured under each event.

.. figure:: ../../../_static/参考手册/Dem/DemEventEcucPartitionRef.png
   :alt: DemEventEcucPartitionRef配置图(DemEventEcucPartitionRef Configuration Diagram)
   :name: DemEventEcucPartitionRef
   :align: center

   DemEventEcucPartitionRef Config

所关联的partition必需在如图 :ref:`EcuCPartition` 中配置已配置。

The associated partition must be configured as shown in EcuCPartition Config.

.. figure:: ../../../_static/参考手册/Dem/EcuCPartition.png
   :alt: EcuCPartition配置图(EcuCPartition Configuration Diagram)
   :name: EcuCPartition
   :align: center

   EcuCPartition Config


扩展数据(Extended Data)
----------------------------------------------
首先需要先配置数据元素类型，如图 :ref:`DemDataElementClass` 所示，在Dem/DemGeneral/DemDataElementClass
容器下可创建子容器，可配置数据元素长度、内部数据元素、数据元素的访问方式等配置。

First, it is necessary to configure the data element type. As shown in :ref:`DemDataElementClass`, sub-containers can be created under the Dem/DemGeneral/DemDataElementClass container, where configurations such as the length of data elements, internal data elements, and the access method of data elements can be set.

.. figure:: ../../../_static/参考手册/Dem/DemDataElementClass.png
   :alt: DemDataElementClass配置图(DemDataElementClass Configuration Diagram)
   :name: DemDataElementClass
   :align: center

   DemDataElementClass Config

其中内部元素包含FailedCycles、AGINGCTR_UPCNT、AGINGCTR_DOWNCNT、CURRENT_FDC、OCC1~OCC6、OVFLIND、SI30等。

The internal elements include FailedCycles, AGINGCTR_UPCNT, AGINGCTR_DOWNCNT, CURRENT_FDC, OCC1~OCC6, OVFLIND, SI30, etc.

.. figure:: ../../../_static/参考手册/Dem/DemInternalDataElement.png
   :alt: DemInternalDataElement配置图(DemInternalDataElement Configuration Diagram)
   :name: DemInternalDataElement
   :align: center

   DemInternalDataElement Config

配置的数据元素，在DemExtendedDataRecordClass中关联，如图:ref:`DemExtendedDataRecordClass` 所示，在Dem/DemGeneral/
DemExtendedDataRecordClass容器下可创建子容器，配置扩展数据号、扩展数据存储触发方式、是否允许更新扩展数据、扩展数据索引等配置。

The configured data elements are associated in DemExtendedDataRecordClass. As shown in :ref:`DemExtendedDataRecordClass`, sub-containers can be created under the Dem/DemGeneral/DemExtendedDataRecordClass container to configure settings such as the extended data number, extended data storage trigger mode, whether to allow updating extended data, and extended data index.

.. figure:: ../../../_static/参考手册/Dem/DemExtendedDataRecordClass.png
   :alt: DemExtendedDataRecordClass配置图(DemExtendedDataRecordClass Configuration Diagram)
   :name: DemExtendedDataRecordClass
   :align: center

   DemExtendedDataRecordClass Config

配置的DemExtendedDataRecordClass，在DemExtendedDataClass中关联，在Dem/DemGeneral/DemExtendedDataClasss容器下可创建子容器，
如图:ref:`DemExtendedDataClass` 所示。

The configured DemExtendedDataRecordClass is associated in DemExtendedDataClass. Sub-containers can be created under the Dem/DemGeneral/DemExtendedDataClass container, as shown in :ref:`DemExtendedDataClass`.

.. figure:: ../../../_static/参考手册/Dem/DemExtendedDataClass.png
   :alt: DemExtendedDataClass配置图(DemExtendedDataClass Configuration Diagram)
   :name: DemExtendedDataClass
   :align: center

   DemExtendedDataClass Config

上述中配置的DemExtendedDataRecordClass需要在DemDTCAttributes中关联，然后给DemEventParameter中使用。
详细参考诊断事件参数配置。

The DemExtendedDataRecordClass configured as mentioned above needs to be associated in DemDTCAttributes and then used in DemEventParameter.
For details, please refer to the configuration of diagnostic event parameters.

冻结帧(Freeze Frame)
------------------------
若配置冻结帧，需要先配置Did，如图 :ref:`DemDidClass` 所示，在Dem/DemGeneral/DemDidClass
容器下可创建子容器，配置Did标识、数据元素索引等配置。

If freeze frames are to be configured, the DID must first be configured. As shown in :ref:`DemDidClass`, sub-containers can be created under the Dem/DemGeneral/DemDidClass container to configure settings such as the DID identifier and data element index.

.. figure:: ../../../_static/参考手册/Dem/DemDidClass.png
   :alt: DemDidClass配置图(DemDidClass Configuration Diagram)
   :name: DemDidClass
   :align: center

   DemDidClass Config

配置的Did可在DemFreezeFrameClass中关联，如图:ref:`DemFreezeFrameClass` 所示，在Dem/DemGeneral/
DemFreezeFrameClass容器下可创建子容器，关联Did配置。

The configured DID can be associated in DemFreezeFrameClass. As shown in :ref:`DemFreezeFrameClass`, sub-containers can be created under the Dem/DemGeneral/DemFreezeFrameClass container to associate with the DID configuration.

.. figure:: ../../../_static/参考手册/Dem/DemFreezeFrameClass.png
   :alt: DemFreezeFrameClass配置图(DemFreezeFrameClass Configuration Diagram)
   :name: DemFreezeFrameClass
   :align: center

   DemFreezeFrameClass Config

配置DemFreezeFrameRecordClass，如图:ref:`DemFreezeFrameRecordClass` 所示，在Dem/DemGeneral/
DemFreezeFrameRecordClass容器下可创建子容器，配置冻结帧ID、冻结帧存储触发方式、允许更新冻结帧等配置。

Configure DemFreezeFrameRecordClass. As shown in :ref:`DemFreezeFrameRecordClass`, sub-containers can be created under the Dem/DemGeneral/DemFreezeFrameRecordClass container to configure settings such as freeze frame ID, freeze frame storage trigger mode, and permission to update freeze frames.

.. figure:: ../../../_static/参考手册/Dem/DemFreezeFrameRecordClass.png
   :alt: DemFreezeFrameRecordClass配置图(DemFreezeFrameRecordClass Configuration Diagram)
   :name: DemFreezeFrameRecordClass
   :align: center

   DemFreezeFrameRecordClass Config

配置的DemFreezeFrameRecordClass，在DemFreezeFrameRecNumClass中关联，如图:ref:`DemFreezeFrameRecNumClass` 所示，
在Dem/DemGeneral/DemFreezeFrameRecNumClass容器下可创建子容器，关联配置的DemFreezeFrameRecordClass。

The configured DemFreezeFrameRecordClass is associated in DemFreezeFrameRecNumClass. As shown in :ref:`DemFreezeFrameRecNumClass`, sub-containers can be created under the Dem/DemGeneral/DemFreezeFrameRecNumClass container to associate with the configured DemFreezeFrameRecordClass.

.. figure:: ../../../_static/参考手册/Dem/DemFreezeFrameRecNumClass.png
   :alt: DemFreezeFrameRecNumClass配置图(DemFreezeFrameRecNumClass Configuration Diagram)
   :name: DemFreezeFrameRecNumClass
   :align: center

   DemFreezeFrameRecNumClass Config

上述中配置的DemFreezeFrameRecNumClass需要在DemDTCAttributes中关联，然后给DemEventParameter中使用。
详细参考诊断事件参数配置。

The DemFreezeFrameRecNumClass configured as mentioned above needs to be associated in DemDTCAttributes and then used in DemEventParameter.
For details, please refer to the configuration of diagnostic event parameters.

诊断事件参数(Diagnostic Event Parameters)
-----------------------------------------------------
在Dem/DemConfigSet/DemEventParameter容器下创建子容器，如图 :ref:`DemEventParameter` 所示，
可配置指定组件内的优先级、Bit3置位阈值、诊断事件的ID 、事件种类、Dem事件的报告行为、DTC索引、
操作循环索引、DemEnableConditionGroup索引、DemStorageConditionGroup索引等参数。

Create a sub-container under the Dem/DemConfigSet/DemEventParameter container, as shown in :ref:`DemEventParameter`. Parameters such as the priority within the specified component, the Bit3 set threshold, the ID of the diagnostic event, the event type, the reporting behavior of the Dem event, the DTC index, the operation cycle index, the DemEnableConditionGroup index, and the DemStorageConditionGroup index can be configured.

.. figure:: ../../../_static/参考手册/Dem/DemEventParameter.png
   :alt: DemEventParameter配置图(DemEventParameter Configuration Diagram)
   :name: DemEventParameter
   :align: center

   DemEventParameter Config

在DemEventParameter中关联的DTC如图 :ref:`DemDTC` 所示，可配置DTC功能单元、DTCSeverity、
DTC值、存储策略、DTC属性索引、OBD DTC索引等。

The DTC associated in DemEventParameter is shown in :ref:`DemDTC`, where configurations such as DTC functional unit, DTC Severity, DTC value, storage strategy, DTC attribute index, and OBD DTC index can be made.

.. figure:: ../../../_static/参考手册/Dem/DemDTC.png
   :alt: DemDTC配置图(DemDTC Configuration Diagram)
   :name: DemDTC
   :align: center

   DemDTC Config

其中DTC属性索引如图:ref:`DemDTCAttributes` 所示，可以配置老化阈值、Bit5老化阈值、DTC优先级、
故障分类、扩展数据索引、冻结帧索引、冻结帧号、冻结帧号索引、对DemJ1939FreezeFrameClass的引用、对
DemJ1939FreezeFrameClass的引用、存储地址等参数。

The DTC attribute index is shown in :ref:`DemDTCAttributes`, where parameters such as aging threshold, Bit5 aging threshold, DTC priority, fault classification, extended data index, freeze frame index, freeze frame number, freeze frame number index, reference to DemJ1939FreezeFrameClass, and storage address can be configured.

.. figure:: ../../../_static/参考手册/Dem/DemDTCAttributes.png
   :alt: DemDTCAttributes配置图(DemDTCAttributes Configuration Diagram)
   :name: DemDTCAttributes
   :align: center

   DemDTCAttributes Config

在DemEventParameter中关联的DemEnableConditionGroupRef，如图 :ref:`DemEnableConditionGroup` 所示，
可关联使能条件索引。

The DemEnableConditionGroupRef associated in DemEventParameter, as shown in :ref:`DemEnableConditionGroup`, can be linked to the enable condition index.

.. figure:: ../../../_static/参考手册/Dem/DemEnableConditionGroup.png
   :alt: DemEnableConditionGroup配置图(DemEnableConditionGroup Configuration Diagram)
   :name: DemEnableConditionGroup
   :align: center

   DemEnableConditionGroup Config

如图 :ref:`DemEnableCondition` 所示，可配置使能条件Id、使能条件状态等。

As shown in :ref:`DemEnableCondition`, the enable condition ID, enable condition status, etc. can be configured.

.. figure:: ../../../_static/参考手册/Dem/DemEnableCondition.png
   :alt: DemEnableCondition配置图(DemEnableCondition Configuration Diagram)
   :name: DemEnableCondition
   :align: center

   DemEnableCondition Config

在DemEventParameter中关联的DemStorageConditionGroupRef，如图 :ref:`DemStorageConditionGroup` 所示，
可关联存储条件索引。

The DemStorageConditionGroupRef associated in DemEventParameter, as shown in :ref:`DemStorageConditionGroup`, can be linked to the storage condition index.

.. figure:: ../../../_static/参考手册/Dem/DemStorageConditionGroup.png
   :alt: DemStorageConditionGroup配置图(DemStorageConditionGroup Configuration Diagram)
   :name: DemStorageConditionGroup
   :align: center

   DemStorageConditionGroup Config

如图 :ref:`DemStorageCondition` 所示，可配置存储条件Id、存储条件状态等。

As shown in :ref:`DemStorageCondition`, the storage condition ID, storage condition status, etc. can be configured.

.. figure:: ../../../_static/参考手册/Dem/DemStorageCondition.png
   :alt: DemStorageCondition配置图(DemStorageCondition Configuration Diagram)
   :name: DemStorageCondition
   :align: center

   DemStorageCondition Config

在DemEventParameter中关联的DemOperationCycleRef，可关联操作循环索引，
如图 :ref:`DemOperationCycle` 所示，DemOperationCycleId根据添加的数量自动增加。

The DemOperationCycleRef associated in DemEventParameter can be linked to the operation cycle index. As shown in :ref:`DemOperationCycle`, the DemOperationCycleId increases automatically according to the number of additions.

.. figure:: ../../../_static/参考手册/Dem/DemOperationCycle.png
   :alt: DemOperationCycle配置图(DemOperationCycle Configuration Diagram)
   :name: DemOperationCycle
   :align: center

   DemOperationCycle Config

在DemEventParameter中每个事件的回调接口可创建对应的子容器，选择是否配置回调接口。
如图 :ref:`DemCallbackClearEventAllowed` 所示，可配置ClearEventAllowed回调接口。

For each event in DemEventParameter, a corresponding sub-container can be created for the callback interface, allowing selection of whether to configure the callback.
As shown in :ref:`DemCallbackClearEventAllowed`, the ClearEventAllowed callback interface can be configured.

.. figure:: ../../../_static/参考手册/Dem/DemCallbackClearEventAllowed.png
   :alt: DemCallbackClearEventAllowed配置图(DemCallbackClearEventAllowed Configuration Diagram)
   :name: DemCallbackClearEventAllowed
   :align: center

   DemCallbackClearEventAllowed Config

如图 :ref:`DemCallbackEventDataChanged` 所示，可配置EventDataChanged回调接口。

As shown in :ref:`DemCallbackEventDataChanged`, the EventDataChanged callback interface can be configured.

.. figure:: ../../../_static/参考手册/Dem/DemCallbackEventDataChanged.png
   :alt: DemCallbackEventDataChanged配置图(DemCallbackEventDataChanged Configuration Diagram)
   :name: DemCallbackEventDataChanged
   :align: center

   DemCallbackEventDataChanged Config

如图 :ref:`DemCallbackEventUdsStatusChanged` 所示，可配置EventUdsStatusChanged回调接口。

As shown in :ref:`DemCallbackEventUdsStatusChanged`, the EventUdsStatusChanged callback interface can be configured.

.. figure:: ../../../_static/参考手册/Dem/DemCallbackEventUdsStatusChanged.png
   :alt: DemCallbackEventUdsStatusChanged配置图(DemCallbackEventUdsStatusChanged Configuration Diagram)
   :name: DemCallbackEventUdsStatusChanged
   :align: center

   DemCallbackEventUdsStatusChanged Config

如图 :ref:`DemCallbackInitMForE` 所示，可配置InitMonitorForEvent回调接口。

As shown in :ref:`DemCallbackInitMForE`, the InitMonitorForEvent callback interface can be configured.

.. figure:: ../../../_static/参考手册/Dem/DemCallbackInitMForE.png
   :alt: DemCallbackInitMForE配置图(DemCallbackInitMForE Configuration Diagram)
   :name: DemCallbackInitMForE
   :align: center

   DemCallbackInitMForE Config

如图 :ref:`DemCallbackMonitorStatusChanged` 所示，可配置MonitorStatusChanged回调接口。

As shown in :ref:`DemCallbackMonitorStatusChanged`, the MonitorStatusChanged callback interface can be configured.

.. figure:: ../../../_static/参考手册/Dem/DemCallbackMonitorStatusChanged.png
   :alt: DemCallbackMonitorStatusChanged配置图(DemCallbackMonitorStatusChanged Configuration Diagram)
   :name: DemCallbackMonitorStatusChanged
   :align: center

   DemCallbackMonitorStatusChanged Config

如图 :ref:`DemIndicatorAttribute` 所示，可配置指示器的行为、Indicator的失败循环次数、恢复循环次数、Indicator索引等。

As shown in :ref:`DemIndicatorAttribute`, configurations such as the behavior of the indicator, the number of failure cycles of the Indicator, the number of recovery cycles, and the Indicator index can be made.

.. figure:: ../../../_static/参考手册/Dem/DemIndicatorAttribute.png
   :alt: DemIndicatorAttribute配置图(DemIndicatorAttribute Configuration Diagram)
   :name: DemIndicatorAttribute
   :align: center

   DemIndicatorAttribute Config


去抖功能(Debounce Function)
-------------------------------------------
如图 :ref:`DemDebounceAlgorithmClass` 所示，在Dem/DemConfigSet/DemEventParameter/DemDebounceAlgorithmClass
容器下可创建子容器关联基于计数/时间、或者监控内部(DemDebounceMonitorInternal)的去抖配置，在对应的子容器中关联配置好的
去抖功能即可。

As shown in :ref:`DemDebounceAlgorithmClass`, sub-containers can be created under the Dem/DemConfigSet/DemEventParameter/DemDebounceAlgorithmClass container to associate debounce configurations based on counter/time, or monitor internal (DemDebounceMonitorInternal). The configured debounce function can then be associated in the corresponding sub-container.

.. figure:: ../../../_static/参考手册/Dem/DemDebounceAlgorithmClass.png
   :alt: DemDebounceAlgorithmClass配置图(DemDebounceAlgorithmClass Configuration Diagram)
   :name: DemDebounceAlgorithmClass
   :align: center

   DemDebounceAlgorithmClass Config

若关联基于计数的去抖功能，如图 :ref:`DemDebounceCounterBasedClass` 所示，在Dem/DemConfigSet/
DemDebounceCounterBasedClass容器下可创建多个基于计数去抖的子容器，可配置去抖行为、计算counter的步长、触发fail/pass的阈值、
Jump-up/Jump-down的值、是否存储去抖计数等参数。

If associating a count-based debounce function, as shown in :ref:`DemDebounceCounterBasedClass`, multiple count-based debounce sub-containers can be created under the Dem/DemConfigSet/DemDebounceCounterBasedClass container. Parameters such as debounce behavior, step size for counter calculation, thresholds for triggering fail/pass, Jump-up/Jump-down values, and whether to store the debounce count can be configured.

.. figure:: ../../../_static/参考手册/Dem/DemDebounceCounterBasedClass.png
   :alt: DemDebounceCounterBasedClass配置图(DemDebounceCounterBasedClass Configuration Diagram)
   :name: DemDebounceCounterBasedClass
   :align: center

   DemDebounceCounterBasedClass Config

若关联基于时间的去抖功能，如图 :ref:`DemDebounceTimeBasedClass` 所示，在Dem/DemConfigSet/DemDebounceTimeBasedClass
容器下可创建多个基于时间去抖的子容器，可配置去抖行为、触发fail/pass的阈值、分配事件内存条目和捕获冻结帧的阈值等参数。

If associating a time-based debounce function, as shown in :ref:`DemDebounceTimeBasedClass`, multiple time-based debounce sub-containers can be created under the Dem/DemConfigSet/DemDebounceTimeBasedClass container. Parameters such as debounce behavior, thresholds for triggering fail/pass, and thresholds for allocating event memory entries and capturing freeze frames can be configured.

.. figure:: ../../../_static/参考手册/Dem/DemDebounceTimeBasedClass.png
   :alt: DemDebounceTimeBasedClass配置图(DemDebounceTimeBasedClass Configuration Diagram)
   :name: DemDebounceTimeBasedClass
   :align: center

   DemDebounceTimeBasedClass Config

若关联监控内部(DemDebounceMonitorInternal)的去抖功能，如图 :ref:`DemDebounceMonitorInternal` 所示，
在Dem/DemConfigSet/DemEventParameter/DemDebounceAlgorithmClass/DemDebounceMonitorInternal容器下创建DemCallbackGetFDC
子容器，可选择是否配置回调接口。

If associating the monitor internal (DemDebounceMonitorInternal) debounce function, as shown in :ref:`DemDebounceMonitorInternal`, a DemCallbackGetFDC sub-container can be created under the Dem/DemConfigSet/DemEventParameter/DemDebounceAlgorithmClass/DemDebounceMonitorInternal container, and you can choose whether to configure the callback interface.

.. figure:: ../../../_static/参考手册/Dem/DemDebounceMonitorInternal.png
   :alt: DemDebounceMonitorInternal配置图(DemDebounceMonitorInternal Configuration Diagram)
   :name: DemDebounceMonitorInternal
   :align: center

   DemDebounceMonitorInternal Config


J939功能 J1939(Functionality)
--------------------------------------------------
在Dem/DemGeneral/DemGeneralJ1939容器中，如图 :ref:`DemGeneralJ1939` 所示，可勾选使能对应的功能配置。

In the Dem/DemGeneral/DemGeneralJ1939 container, as shown in :ref:`DemGeneralJ1939`, you can check to enable the corresponding function configurations.

.. figure:: ../../../_static/参考手册/Dem/DemGeneralJ1939.png
   :alt: DemGeneralJ1939配置图(DemGeneralJ1939 Configuration Diagram)
   :name: DemGeneralJ1939
   :align: center

   DemGeneralJ1939 Config

在Dem/DemGeneral/DemGeneralJ1939/DemSPNClass容器中，创建子容器，如图 :ref:`DemSPNClass` 所示，
可配置SPN标识符，并关联数据元素。

In the Dem/DemGeneral/DemGeneralJ1939/DemSPNClass container, create a sub-container. As shown in :ref:`DemSPNClass`, you can configure the SPN identifier and associate data elements.

.. figure:: ../../../_static/参考手册/Dem/DemSPNClass.png
   :alt: DemSPNClass配置图(DemSPNClass Configuration Diagram)
   :name: DemSPNClass
   :align: center

   DemSPNClass Config

在Dem/DemGeneral/DemGeneralJ1939/DemJ1939FreezeFrameClass容器中，创建子容器，如图 :ref:`DemJ1939FreezeFrameClass` 所示，
可关联配置的DemSPNClass。

In the Dem/DemGeneral/DemGeneralJ1939/DemJ1939FreezeFrameClass container, create a sub-container. As shown in :ref:`DemJ1939FreezeFrameClass`, the configured DemSPNClass can be associated.

.. figure:: ../../../_static/参考手册/Dem/DemJ1939FreezeFrameClass.png
   :alt: DemJ1939FreezeFrameClass配置图(DemJ1939FreezeFrameClass Configuration Diagram)
   :name: DemJ1939FreezeFrameClass
   :align: center

   DemJ1939FreezeFrameClass Config

还可在Dem/DemGeneral/DemGeneralJ1939/DemCallbackJ1939DTCStatusChanged 容器中，创建子容器，
如图 :ref:`DemCallbackJ1939DTCStatusChanged` 所示，可配置回调接口。

Additionally, a sub-container can be created in the Dem/DemGeneral/DemGeneralJ1939/DemCallbackJ1939DTCStatusChanged container. As shown in :ref:`DemCallbackJ1939DTCStatusChanged`, the callback interface can be configured.

.. figure:: ../../../_static/参考手册/Dem/DemCallbackJ1939DTCStatusChanged.png
   :alt: DemCallbackJ1939DTCStatusChanged配置图(DemCallbackJ1939DTCStatusChanged Configuration Diagram)
   :name: DemCallbackJ1939DTCStatusChanged
   :align: center

   DemCallbackJ1939DTCStatusChanged Config

上述中配置的DemJ1939FreezeFrameClass需要在DemDTCAttributes中关联，然后给DemEventParameter中使用。详细参考诊断事件参数配置。

The DemJ1939FreezeFrameClass configured above needs to be associated in DemDTCAttributes and then used in DemEventParameter. For details, please refer to the diagnostic event parameter configuration.


诊断事件存储功能(Diagnostic Event Storage Function)
----------------------------------------------------------
在Dem/DemGeneral/DemEventMemorySet 容器中，如图 :ref:`DemEventMemorySet` 所示，配置可存储在永久存储器中的事件的最大数量、
DTC支持的类型(ISO11992_4、ISO14229_1、ISO15031_6、SAEJ1939_73、SAE_J2012_DA_DTCFORMAT_04)、关联的指示灯MIL、RSL、AWL、PL等。

In the Dem/DemGeneral/DemEventMemorySet container, as shown in :ref:`DemEventMemorySet`, configure parameters such as the maximum number of events that can be stored in permanent memory, the DTC types supported (ISO11992_4, ISO14229_1, ISO15031_6, SAEJ1939_73, SAE_J2012_DA_DTCFORMAT_04), and associated indicator lamps including MIL, RSL, AWL, PL, etc.

.. figure:: ../../../_static/参考手册/Dem/DemEventMemorySet.png
   :alt: DemEventMemorySet配置图(DemEventMemorySet Configuration Diagram)
   :name: DemEventMemorySet
   :align: center

   DemEventMemorySet Config

在Dem/DemGeneral/DemEventMemorySet/DemClearDTCNotification 子容器中，如图 :ref:`DemClearDTCNotification` 所示，
可配置清除DTC的回调接口以及清除时机。

In the Dem/DemGeneral/DemEventMemorySet/DemClearDTCNotification sub-container, as shown in :ref:`DemClearDTCNotification`, the callback interface for clearing DTCs and the clearing timing can be configured.

.. figure:: ../../../_static/参考手册/Dem/DemClearDTCNotification.png
   :alt: DemClearDTCNotification配置图(DemClearDTCNotification Configuration Diagram)
   :name: DemClearDTCNotification
   :align: center

   DemClearDTCNotification Config

在Dem/DemGeneral/DemEventMemorySet/DemIndicator 子容器中，如图 :ref:`DemIndicator` 所示，可配置指示灯ID。

In the Dem/DemGeneral/DemEventMemorySet/DemIndicator sub-container, as shown in :ref:`DemIndicator`, the indicator lamp ID can be configured.

.. figure:: ../../../_static/参考手册/Dem/DemIndicator.png
   :alt: DemIndicator配置图(DemIndicator Configuration Diagram)
   :name: DemIndicator
   :align: center

   DemIndicator Config

在Dem/DemGeneral/DemEventMemorySet/DemPrimaryMemory 子容器中，如图 :ref:`DemPrimaryMemory` 所示，
可配置用于UDS服务0x19正向响应的掩码、替换策略、触发事件存储的方式、存储在主内存中的最大事件数、OCC计算方式、快照号计算方式等。

In the Dem/DemGeneral/DemEventMemorySet/DemPrimaryMemory sub-container, as shown in :ref:`DemPrimaryMemory`, configurations can be made such as the mask for UDS service 0x19 positive response, replacement strategy, method for triggering event storage, maximum number of events stored in primary memory, OCC calculation method, and snapshot number calculation method.

.. figure:: ../../../_static/参考手册/Dem/DemPrimaryMemory.png
   :alt: DemPrimaryMemory配置图(DemPrimaryMemory Configuration Diagram)
   :name: DemPrimaryMemory
   :align: center

   DemPrimaryMemory Config

以及关联的DTC组，如图 :ref:`DemGroupOfDTC` 所示。

and the associated DTC group, as shown in :ref:`DemGroupOfDTC`.

.. figure:: ../../../_static/参考手册/Dem/DemGroupOfDTC.png
   :alt: DemGroupOfDTC配置图(DemGroupOfDTC Configuration Diagram)
   :name: DemGroupOfDTC
   :align: center

   DemGroupOfDTC Config

还可在Dem/DemGeneral/DemEventMemorySet/DemUserDefinedMemory 子容器中，如图 :ref:`DemUserDefinedMemory` 所示，
可配置用户定义的事件存储功能。

Additionally, in the Dem/DemGeneral/DemEventMemorySet/DemUserDefinedMemory sub-container, as shown in :ref:`DemUserDefinedMemory`, user-defined event storage functions can be configured.

.. figure:: ../../../_static/参考手册/Dem/DemUserDefinedMemory.png
   :alt: DemUserDefinedMemory配置图(DemUserDefinedMemory Configuration Diagram)
   :name: DemUserDefinedMemory
   :align: center

   DemUserDefinedMemory Config

当Dem需要永久存储event状态信息、内部数据时，需要与NvM进行交互，可在Dem/DemGeneral/DemNvRamBlockId 下通过同步功能创建reference关系。
如图 :ref:`DemNvRamBlockId` 所示，

When Dem needs to permanently store event status information and internal data, it needs to interact with NvM. A reference relationship can be created through the synchronization function under Dem/DemGeneral/DemNvRamBlockId.
As shown in :ref:`DemNvRamBlockId`,

.. figure:: ../../../_static/参考手册/Dem/DemNvRamBlockId.png
   :alt: DemNvRamBlockId配置图(DemNvRamBlockId Configuration Diagram)
   :name: DemNvRamBlockId
   :align: center

   DemNvRamBlockId Config

右键点击DemNvRamBlockId 容器，点击同步功能，如图 :ref:`DemNvRamBlockIdSYNC` 所示。

Right-click on the DemNvRamBlockId container and click on the synchronization function, as shown in :ref:`DemNvRamBlockIdSYNC`.

.. figure:: ../../../_static/参考手册/Dem/DemNvRamBlockIdSYNC.png
   :alt: DemNvRamBlockIdSYNC配置图(DemNvRamBlockIdSYNC Configuration Diagram)
   :name: DemNvRamBlockIdSYNC
   :align: center

   DemNvRamBlockIdSYNC Config

或者右键点击BSW中的Dem模块，点击同步功能，如图 :ref:`DemSYNCModule` 所示，

Alternatively, right-click on the Dem module in BSW and click on the synchronization function, as shown in :ref:`DemSYNCModule`.

.. figure:: ../../../_static/参考手册/Dem/DemSYNCModule.png
   :alt: DemSYNCModule配置图(DemSYNCModule Configuration Diagram)
   :name: DemSYNCModule
   :align: center

   DemSYNCModule Config
