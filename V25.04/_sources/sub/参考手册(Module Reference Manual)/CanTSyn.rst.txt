CanTSyn
#################################

:strong:`缩写词注解 (Abbreviation Notes):`

.. list-table::
   :widths: 34 33 33
   :header-rows: 1

   * - 缩写词 (Abbreviation)
     - 解释/描述 (Explanation/Description)
     - 中文解释 (Chinese explanation)
   * - (G)TD
     - (Global) Time Domain
     - （全局）时间域 ((Global) Time Domain)
   * - (G)TM
     - (Global)Time Master
     - （全局）时间主控 ((Global) Time Controller)
   * - <Bus>TSyn
     - A bus specific TimeSynchronization module
     - 特定总线时间同步模块 (Specific Bus Time Synchronization Module)
   * - CAN
     - Controller Area Network
     - 控制器区域网络 (Controller Area Network)
   * - CanTSyn
     - Time Synchronizationmodule for CAN
     - CAN时间同步模块 (CAN Time Synchronization Module)
   * - CRC
     - Cyclic RedundancyChecksum
     - 循环冗余检验 (Cyclic Redundancy Check)
   * - DebounceTime
     - Minimum gap between twoTx messages with the samePDU
     - 同一PDU两条发送消息的最小间隔 (Minimum interval for sending two messages on the same PDU)
   * - DEM
     - Diagnostic Event Manager
     - 诊断事件管理 (Event Management)
   * - DET
     - Default Error Tracer
     - 默认错误跟踪器 (Default Error Tracker)
   * - DLC
     - Data Length Code
     - 数据长度代码 (Data length code)
   * - FUPmessage
     - Follow-Up message
     - 后续消息 (Subsequent updates)
   * - OFNSmessage
     - Offset adjustment message
     - 偏移调整消息 (Offset adjustment message)
   * - OFSmessage
     - Offset Synchronizationmessage
     - 偏移同步消息 (Offset Synchronized Messages)
   * - StbM
     - Synchronized Time-BaseManager
     - 同步的时间基管理 (Synchronized time base management)
   * - SYNCmessage
     - Time Synchronizationmessage
     - 时间同步消息 (Time synchronization messages)
   * - TG
     - Time Gateway
     - 时间网关 (Time Gateway)
   * - Timesync
     - Time Synchronization
     - 时间同步 (Time synchronization)
   * - TS
     - Time Slave
     - 时间从属 (Time subordinates)
   * - TSD
     - Time Sub-domain
     - 时间子域 (Time subdomain)




简介 (Introduction)
=================================

CanTSyn在AutoSAR软件层级架构如下图，其所属于时间同步栈。

As shown in the figure below, CanTSyn is located in the AUTOSAR software layered architecture and belongs to the time synchronization stack.

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/CanTSyn/image1.png
   :alt: CanTSyn所在AutoSAR软件架构 (CanTSyn in AutoSAR software architecture)
   :name: CanTSyn所在AutoSAR软件架构 (CanTSyn in AutoSAR software architecture)
   :align: center


本文中描述CanTSyn，StbM负责管理时间域，给CanTSyn提供接口用来更新同步时间，给其他用户提供接口用来获取/通知同步时间。CanTSyn负责Can总线上的时间同步。

This article describes CanTSyn, where StbM is responsible for managing the time domain, providing interfaces to CanTSyn for updating synchronization time and to other users for obtaining/notifying synchronization time. CanTSyn is in charge of time synchronization on the CAN bus.

参考资料 (Reference materials)
------------------------------------------

[1] AUTOSAR_SWS_TimeSyncOverCAN.pdf，R19-11

[2] AUTOSAR_SWS_SynchronizedTimeBaseManager.pdf，R19-11

[3] AUTOSAR_EXP_LayeredSoftwareArchitecture.pdf，R19-11

功能描述 (Function Description)
===========================================

CanTSyn功能 (CanTSyn Function)
--------------------------------------------

CanTSyn功能介绍 (Introduction to CanTSyn Function)
==============================================================

CanTSyn模块和StbM模块息息相关，StbM模块提供了时间同步的功能和时钟实例的指针，但不负责在各个总线内的时间分发任务。那么CanTSyn模块就处理了在CAN总线发放时间信息的任务。

The CanTSyn module and the StbM module are closely related. The StbM module provides time synchronization functionality and clock instance pointers, but it is not responsible for distributing time across various buses. Therefore, the CanTSyn module handles the task of disseminating time information on the CAN bus.

仅仅通过广播的方式把时间信息从Time Masters发送到Time Slaves会导致时间不精准，这是因为CAN总线传输仲裁机制以及BSW的延迟。

Simply broadcasting time information from Time Masters to Time Slaves via radio would result in inaccuracies, due to the CAN bus transmission arbitration mechanism and BSW delays.

CanTSyn功能实现 (CanTSyn Function Implementation)
=============================================================

我们通过以下的两步算法来尽可能消除这样的延迟：

We eliminate such delays through the following two-step algorithm:

发送方（Time Master）首先记录当前的同步时间（SYNC）以及本地时间(T0VLT)并在第一个广播信息（所谓的SYNC信息）里，把同步好的时间的秒部分（SYNCSEC）作为内容发送。发送方在收到“CAN transmit confirmation”时记录时间戳来得到信息实际发送的时间点（T1VLT）。

The sender (Time Master) first records the current synchronization time (SYNC) and local time (T0VLT), and in the first broadcast message (referred to as the SYNC information), sends the second part of the synchronized time (SYNCSEC) as content. The sender records a timestamp upon receiving "CAN transmit confirmation" to obtain the actual transmission time point (T1VLT).

接收方（Time Slave）收到信息 “CAN receive indication”时记录时间戳来检测信息实际收到的时间点（T2VLT）。

Record a timestamp when the receiver (Time Slave) receives the information "CAN receive indication" to detect the actual time point (T2VLT) of receipt.

在第二个广播信息（所谓的FUP（follow-up）信息）里，发送方发送T4作为内容，T4为SYNC消息准备发送和实际发送的时间差（T1VLT-T0VLT）加上T0SYNCNS（同步时间的纳秒部分）（T4=T0SYNCNS+(T1VLT-T0VLT)）。对于发送方来说，此时T0SYNCSEC+T4就为同步时间。

In the second broadcast message (so-called FUP (follow-up) message), the sender sends T4 as content, where T4 is the difference between the time prepared to send and the actual sending of a SYNC message (T1VLT-T0VLT) plus T0SYNCNS (nanoseconds part of the synchronization time) (T4=T0SYNCNS+(T1VLT-T0VLT)). For the sender, at this point, T0SYNCSEC+T4 is the synchronization time.

Time Slave现在从SYNC和FUP消息里获取了足够的信息，再加上先前记录的时间戳T2VLT，就可以确定更加确切的时间信息。接收方获取当前的时间戳为T3VLT，再减去T2VLT，我们就将FUP及SYNC消息中的传输延迟包含在内，再加上T0SYNCSEC+T4（Master的同步时间），我们就得到最终的同步时间T5=T0SYNCSEC+T4+（T3VLT-T2VLT）。

Time Slave now obtains sufficient information from SYNC and FUP messages, along with the previously recorded timestamp T2VLT, to determine more accurate time information. The receiver acquires the current timestamp as T3VLT, then subtracts T2VLT from it, thereby including the transmission delay in the FUP and SYNC messages. Adding T0SYNCSEC + T4 (Master's synchronization time), we obtain the final synchronization time T5 = T0SYNCSEC + T4 + (T3VLT - T2VLT).

至此，Time Master和Time Slave完成时间同步。

So far, Time Master and Time Slave have completed time synchronization.

以下图片显示了CAN时间同步机制：

The following image shows the CAN time synchronization mechanism:

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/CanTSyn/image2.png
   :alt: Can时间同步算法 (Can Time Synchronization Algorithms)
   :name: Can时间同步算法 (Can Time Synchronization Algorithms)
   :align: center


源文件描述 (Source file description)
===============================================

.. centered:: **表 CanTSyn组件文件描述 (Table Description for CanTSyn Component File)**

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 文件 (Files)
     - 说明 (Description)
   * - CanTSyn.c
     - 包含需要使用的宏定义，内部变量，内部函数，全局函数。 (Contains the macros needed for use, internal variables, internal functions, and global functions.)
   * - CanTSyn.h
     - 包含需要使用的宏定义，类型定义，配置结构体声明，外部函数声明。 (Contain macro definitions, type definitions, configuration structure declarations, and external function declarations.)
   * - CanTSyn_Cbk.h
     - 包含需要使用的宏定义，类型定义，配置结构体声明，外部回调函数声明。 (Contains macro definitions, type definitions, configuration structure declarations, and external callback function declarations.)
   * - CanTSyn_Cfg.h
     - 包含配置宏定义。 (Include configuration macro definitions.)
   * - CanTSyn_Cfg.c
     - 包含配置参数结构体。 (Contain configuration parameter structure.)
   * - CanTSyn_MemMap.h
     - CanTSyn模块的内存映射。 (Memory mapping of the CanTSyn module.)


.. figure:: ../../_static/参考手册(Module_Reference_Manual)/CanTSyn/image3.png
   :alt: CanTSyn组件文件交互关系图 (Component File Interactions Diagram for CanTSyn)
   :name: CanTSyn组件文件交互关系图 (Component File Interactions Diagram for CanTSyn)
   :align: center

API接口 (API Interface)
=====================================

类型定义 (Type definition)
--------------------------------------

CanTSyn_ConfigType类型定义 (CanTSyn_ConfigType Type Definition)
===========================================================================

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 名称 (Name)
     - CanTSyn_ConfigType
   * - 类型 (Type)
     - Structure
   * - 范围 (Range)
     - 无
   * - 描述 (Description)
     - 配置参数结构体类型定义 (Definition of configuration parameter structure type)




CanTSyn_TransmissionModeType类型定义 (CanTSyn_TransmissionModeType Type Definition)
===============================================================================================

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 名称 (Name)
     - CanTSyn_TransmissionModeType
   * - 类型 (Type)
     - Enumeration
   * - 范围 (Range)
     - CANTSYN_TX_OFF
   * - 
     - CANTSYN_TX_ON
   * - 描述 (Description)
     - 传输模式 (Transmission mode)




输入函数描述 (Describe the input function:)
-----------------------------------------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 输入模块 (Input Module)
     - API
   * - Crc
     - Crc_CalculateCRC8H2F
   * - Det
     - Det_ReportError
   * - CanIf
     - CanIf_Transmit
   * - StbM
     - StbM_BusGetCurrentTime
   * - 
     - StbM_BusSetGlobalTime
   * - 
     - StbM_GetCurrentVirtualLocalTime
   * - 
     - StbM_GetOffset
   * - 
     - StbM_GetTimeBaseStatus
   * - 
     - StbM_GetTimeBaseUpdateCounter




静态接口函数定义 (Static interface function definition)
---------------------------------------------------------------

CanTSyn_GetVersionInfo函数定义 (The CanTSyn_GetVersionInfo function definition)
===========================================================================================

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - CanTSyn_GetVersionInfo
   * - 函数原型： (Function prototype:)
     - void CanTSyn_GetVersionInfo (
   * - 
     - Std_VersionInfoType\* versioninfo
   * - 
     - )
   * - 服务编号： (Service Number:)
     - 0x02
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
   * - 是否可重入： (Is Reentrant:)
     - 否 (No)
   * - 输入参数： (Input parameters:)
     - 无 (None)
   * - 输入输出参数： (Input Output Parameters:)
     - 无 (None)
   * - 输出参数： (Output Parameters:)
     - versionInfoPtr：版本信息 (versionInfoPtr: Version Information)
   * - 返回值： (Return Value:)
     - 无 (None)
   * - 功能概述： (Function Overview:)
     - 获取CanTSyn模块版本信息 (Get CanTSyn Module Version Information)




CanTSyn_Init函数定义 (The CanTSyn_Init function defines)
====================================================================

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - CanTSyn_Init
     - 
     - 
     - 
   * - 函数原型： (Function prototype:)
     - void CanTSyn_Init(
     - 
     - 
     - 
   * - 
     - constCanTSyn_ConfigType\*configPtr
     - 
     - 
     - 
   * - 
     - )
     - 
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x01
     - 
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 否 (No)
     - 
     - 
     - 
   * - 输入参数： (Input parameters:)
     - configPtr
     - 值域： (Domain:)
     - 配置结构指针 (Pointer to configuration structure)
     - 
   * - 输入输出参数： (Input Output Parameters:)
     - 无 (None)
     - 
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无 (None)
     - 
     - 
     - 
   * - 返回值： (Return Value:)
     - 无 (None)
     - 
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 初始化模块。 (Initialize module.)
     - 
     - 
     - 




CanTSyn_SetTransmissionMode函数定义 (The CanTSyn_SetTransmissionMode function defines)
==================================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - CanTSyn_SetTransmissionMode
     - 
     - 
   * - 函数原型： (Function prototype:)
     - voidCanTSyn_SetTransmissionMode(
     - 
     - 
   * - 
     - uint8 CtrlIdx,
     - 
     - 
   * - 
     - CanTSyn_TransmissionModeTypeMode
     - 
     - 
   * - 
     - )
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
     - 否 (No)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - CtrlIdx
     - 值域： (Domain:)
     - CAN通道序号 (CAN Channel Number)
   * - 
     - Mode
     - 值域： (Domain:)
     - CANTSYN_TX_OFFCANTSYN_TX_ON
   * - 输入输出参数： (Input Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 返回值： (Return Value:)
     - 无 (None)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 开关发送消息功能。 (Disable message sending function.)
     - 
     - 




CanTSyn_RxIndication函数定义 (The CanTSyn_RxIndication function definition)
=======================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - CanTSyn_RxIndication
     - 
     - 
   * - 函数原型： (Function prototype:)
     - voidCanTSyn_RxIndication(
     - 
     - 
   * - 
     - PduIdTypeRxPduId,
     - 
     - 
   * - 
     - constPduInfoType\*PduInfoPtr
     - 
     - 
   * - 
     - )
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x42
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 对于不同的PDU可重入，否则不可。 (For different PDUs reentrancy is allowed, otherwise not.)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - RxPduId
     - 值域： (Domain:)
     - 收到的PDU Id (Received PDU ID)
   * - 
     - PduInfoPtr
     - 值域： (Domain:)
     - 数据信息指针 (Data information pointer)
   * - 输入输出参数： (Input Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 返回值： (Return Value:)
     - 无 (None)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 提示从下层模块收到PDU。 (Received PDU from lower module.)
     - 
     - 




CanTSyn_TxConfirmation函数定义 (The CanTSyn_TxConfirmation function defines)
========================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - CanTSyn_TxConfirmation
     - 
     - 
   * - 函数原型： (Function prototype:)
     - voidCanTSyn_TxConfirmation(
     - 
     - 
   * - 
     - PduIdType TxPduId,
     - 
     - 
   * - 
     - Std_ReturnTyperesult
     - 
     - 
   * - 
     - )
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x40
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 对于不同的PDU可重入，否则不可。 (For different PDUs reentrancy is allowed, otherwise not.)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - RxPduId
     - 值域： (Domain:)
     - 收到的PDU Id (Received PDU ID)
   * - 
     - result
     - 值域： (Domain:)
     - E_OK：成功发送。E_NOT_Ok：发送失败 (E_OK：Success sent. E_NOT_Ok：Send failed.)
   * - 输入输出参数： (Input Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 返回值： (Return Value:)
     - 无 (None)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 下层模块确认发送成功或失败。 (Lower-level modules confirm sending success or failure.)
     - 
     - 




CanTSyn_MainFunction函数定义 (CanTSyn_MainFunction function definition)
===================================================================================

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - CanTSyn_MainFunction
   * - 函数原型： (Function prototype:)
     - void CanTSyn_MainFunction (
   * - 
     - void
   * - 
     - )
   * - 服务编号： (Service Number:)
     - 0x06
   * - 功能概述： (Function Overview:)
     - 模块主函数，循环调用，发送时间同步消息。 (Main function of the module, loops to send time synchronization messages.)




可配置函数定义 (Configurable Function Definition)
----------------------------------------------------------

无。

None.

配置 (Configure)
==============================

.. centered:: **配置列表 (Configuration List)**

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




CanTSynGeneral
------------------------------

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/CanTSyn/image4.png
   :alt: CanTSynGeneral 工具配置 (CanTSynGeneral Tool Configuration)
   :name: CanTSynGeneral 工具配置 (CanTSynGeneral Tool Configuration)
   :align: center


.. centered:: **表 CanTSynGeneral配置描述 (Table CanTSynGeneral Configuration Description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - CanTSynDevErrorDetect
     - 取值范围 (Range)
     - True、False
     - 默认取值 (Default value)
     - FALSE
   * - 
     - 
     - 
     - 
     - 
   * - 
     - 参数描述 (Parameter Description)
     - 开关错误检测和通知。 (Switch error detection and notification.)
     - 
     -
   * - 
     - 依赖关系 (Dependencies)
     - 无 (None)
     - 
     - 
   * - CanTSynMainFunctionPeriod
     - 取值范围 (Range)
     - 0..INF
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 主函数调度周期。 (Main function scheduling period.)
     - 
     -
   * - 
     - 依赖关系 (Dependencies)
     - 无 (None)
     - 
     - 
   * - CanTSynVersionInfoApi
     - 取值范围 (Range)
     - True、False
     - 默认取值 (Default value)
     - FALSE
   * - 
     - 参数描述 (Parameter Description)
     - 开关获取版本信息接口。 (Interface for acquiring version information.)
     - 
     -
   * - 
     - 依赖关系 (Dependencies)
     - 无 (None)
     - 
     - 
   * - CanTSynR19CbkVersion
     - 取值范围 (Range)
     - True、False
     - 默认取值 (Default value)
     - FALSE
   * - 
     - 参数描述 (Parameter Description)
     - 选择CanTSyn回调函数为 R19版本（默认为 4.2.2 版本）。 (Choose CanTSyn callback function for version R19 (default is version 4.2.2).)
     - 
     -
   * - 
     - 依赖关系 (Dependencies)
     - 无 (None)
     - 
     - 
   * - CanTSynMultiplePartitionEnabled
     - 取值范围 (Range)
     - True、False
     - 默认取值 (Default value)
     - FALSE
   * - 
     - 参数描述 (Parameter Description)
     - 是否支持多分区。 (Does it support multiple partitions.)
     - 
     -
   * - 
     - 依赖关系 (Dependencies)
     - 无 (None)
     - 
     - 




CanTSynGlobalTimeDomain
---------------------------------------

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/CanTSyn/image5.png
   :alt: CanTSynGlobalTimeDomain 工具配置 (CanTSynGlobalTimeDomain Tool Configuration)
   :name: CanTSynGlobalTimeDomain 工具配置 (CanTSynGlobalTimeDomain Tool Configuration)
   :align: center


.. centered:: **表 CanTSynGlobalTimeDomain配置描述 (Table CanTSynGlobalTimeDomain Configuration Description)**

.. list-table::
   :widths: 15 15 14 14 14 14 14
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
     - 
     - 
   * - CanTSynGlobalTimeDomainId
     - 取值范围 (Range)
     - 0..31
     - 
     - 默认取值 (Default value)
     - 
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 时间域ID。 (Time-domain ID.)
     - 
     - 
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无 (None)
     - 
     - 
     - 
     - 
   * - CanTSynUseExtendedMsgFormat
     - 取值范围 (Range)
     - True、False
     - 
     - 默认取值 (Default value)
     - 
     - False
   * - 
     - 参数描述 (Parameter Description)
     - 是否使用时间同步扩展格式（仅CANFD）。 (Is time synchronization extended format (only for CANFD) used?)
     - 
     - 
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无 (None)
     - 
     - 
     - 
     - 
   * - CanTSynSynchronizedTimeBaseRef
     - 取值范围 (Range)
     - reference
     - 
     - 默认取值 (Default value)
     - 
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 引用需要的时间基。 (Reference the time base required.)
     - 
     - 
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - StbMSynchronizedTimeBase
     - 
     - 
     - 
     - 
   * - CanTSynGlobalTimeCanIfRef
     - 取值范围 (Range)
     - reference
     - 默认取值 (Default value)
     - 
     - 
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 这表示该时间域关联的哪一个CanIfCtrlCfg。用于确定开启多分区时，本时间域关联的是哪一个分区。 (This indicates which CanIfCtrlCfg is associated with this time domain. Used to determine which partition this time domain is associated with when multiple partitions are enabled.)
     - 
     - 
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - CanIfCtrlCfg
     - 
     - 
     - 
     - 




CanTSynGlobalTimeSyncDataIDList
===============================================

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/CanTSyn/image6.png
   :alt: CanTSynGlobalTimeSyncDataIDList工具配置 (CanTSynGlobalTimeSyncDataIDList Tool Configuration)
   :name: CanTSynGlobalTimeSyncDataIDList工具配置 (CanTSynGlobalTimeSyncDataIDList Tool Configuration)
   :align: center


CanTSynGlobalTimeSyncDataIDListElement
------------------------------------------------------

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/CanTSyn/image7.png
   :alt: CanTSynGlobalTimeSyncDataIdListElement工具配置 (CanTSynGlobalTimeSyncDataIdListElement Tool Configuration)
   :name: CanTSynGlobalTimeSyncDataIdListElement工具配置 (CanTSynGlobalTimeSyncDataIdListElement Tool Configuration)
   :align: center


.. centered:: **表 CanTSynGlobalTimeSyncDataIdListElement配置描述 (Table CanTSynGlobalTimeSyncDataIdListElement Configuration Description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - CanTSynGlobalTimeSyncDataIDListIndex
     - 取值范围 (Range)
     - 0..15
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 用于CRC计算和信息校验SYNC报文的DataIDList的Index。 (The Index of DataIDList for CRC calculation and information validation in SYNC message.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 不可配，自动根据顺序生成。 (Unmatchable, automatically generated in order.)
     - 
     - 
   * - CanTSynGlobalTimeSyncDataIDListValue
     - 取值范围 (Range)
     - 0..255
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 用于CRC计算和信息校验SYNC报文的DataIDList的值。 (Values for DataIDList used for CRC calculation and information verification of SYNC messages.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无 (None)
     - 
     - 




CanTSynGlobalTimeFupDataIDList
==============================================

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/CanTSyn/image8.png
   :alt: CanTSynGlobalTimeFupDataIdList工具配置 (Tool Configuration for CanTSynGlobalTimeFupDataIdList)
   :name: CanTSynGlobalTimeFupDataIdList工具配置 (Tool Configuration for CanTSynGlobalTimeFupDataIdList)
   :align: center


CanTSynGlobalTimeFupDataIDListElement
-----------------------------------------------------

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/CanTSyn/image9.png
   :alt: CanTSynGlobalTimeFupDataIdListElement工具配置 (CanTSynGlobalTimeFupDataIdListElement Tool Configuration)
   :name: CanTSynGlobalTimeFupDataIdListElement工具配置 (CanTSynGlobalTimeFupDataIdListElement Tool Configuration)
   :align: center


.. centered:: **表 CanTSynGlobalTimeFupDataIdListElement配置描述 (Table CanTSynGlobalTimeFupDataIdListElement Configuration Description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - CanTSynGlobalTimeFupDataIDListIndex
     - 取值范围 (Range)
     - 0..15
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 用于CRC计算和信息校验FUP报文的DataIDList的Index。 (Index for DataIDList used in CRC calculation and information validation for FUP message.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 不可配，自动根据顺序生成。 (Unmatchable, automatically generated in order.)
     - 
     - 
   * - CanTSynGlobalTimeFupDataIDListValue
     - 取值范围 (Range)
     - 0..255
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 用于CRC计算和信息校验SYNC报文的DataIDList的值。 (Values for DataIDList used for CRC calculation and information verification of SYNC messages.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无 (None)
     - 
     - 




CanTSynGlobalTimeOfsDataIDList
==============================================

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/CanTSyn/image10.png
   :alt: CanTSynGlobalTimeOfsDataIdList工具配置 (CanTSynGlobalTimeOfDayConfig Data ID List Tool Configuration)
   :name: CanTSynGlobalTimeOfsDataIdList工具配置 (CanTSynGlobalTimeOfDayConfig Data ID List Tool Configuration)
   :align: center


CanTSynGlobalTimeOfsDataIDListElement
-----------------------------------------------------

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/CanTSyn/image11.png
   :alt: CanTSynGlobalTimeOfsDataIdListElement工具配置 (CanTSynGlobalTimeOfsDataIdListElement Tool Configuration)
   :name: CanTSynGlobalTimeOfsDataIdListElement工具配置 (CanTSynGlobalTimeOfsDataIdListElement Tool Configuration)
   :align: center


.. centered:: **表 CanTSynGlobalTimeOfsDataIdListElement配置描述 (Table CanTSynGlobalTimeOfsDataIdListElement Configuration Description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - CanTSynGlobalTimeOfsDataIDListIndex
     - 取值范围 (Range)
     - 0..15
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 用于CRC计算和信息校验OFS报文的DataIDList的Index。 (The Index for DataIDList used in CRC calculation and information validation of OFS messages.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 不可配，自动根据顺序生成。 (Unmatchable, automatically generated in order.)
     - 
     - 
   * - CanTSynGlobalTimeOfsDataIDListValue
     - 取值范围 (Range)
     - 0..255
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 用于CRC计算和信息校验OFS报文的DataIDList的值。 (Values for DataIDList used for CRC calculation and information validation of OFS messages.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无 (None)
     - 
     - 




CanTSynGlobalTimeOfnsDataIDList
===============================================

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/CanTSyn/image12.png
   :alt: CanTSynGlobalTimeOfnsDataIdList工具配置 (Tool Configuration for CanTSynGlobalTime Ofns Data Id List)
   :name: CanTSynGlobalTimeOfnsDataIdList工具配置 (Tool Configuration for CanTSynGlobalTime Ofns Data Id List)
   :align: center


CanTSynGlobalTimeOfnsDataIDListElement
------------------------------------------------------

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/CanTSyn/image13.png
   :alt: CanTSynGlobalTimeOfnsDataIdListElement工具配置 (CanTSynGlobalTimeOfnsDataIdListElement Tool Configuration)
   :name: CanTSynGlobalTimeOfnsDataIdListElement工具配置 (CanTSynGlobalTimeOfnsDataIdListElement Tool Configuration)
   :align: center


.. centered:: **表 CanTSynGlobalTimeOfnsDataIdListElement配置描述 (Table CanTSynGlobalTimeOfnsDataIdListElement Configuration Description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - CanTSynGlobalTimeOfnsDataIDListIndex
     - 取值范围 (Range)
     - 0..15
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 用于CRC计算和信息校验OFNS报文的DataIDList的Index。 (Index for DataIDList used in CRC calculation and information verification of OFNS messages.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 不可配，自动根据顺序生成。 (Unmatchable, automatically generated in order.)
     - 
     - 
   * - CanTSynGlobalTimeOfnsDataIDListValue
     - 取值范围 (Range)
     - 0..255
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 用于CRC计算和信息校验OFNS报文的DataIDList的值。 (Values for DataIDList used for CRC calculation and information verification of OFNS messages.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无 (None)
     - 
     - 




CanTSynGlobalTimeMaster
=======================================

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/CanTSyn/image14.png
   :alt: CanTSynGlobalTimeMaster工具配置 (CanTSynGlobalTimeMaster Tool Configuration)
   :name: CanTSynGlobalTimeMaster工具配置 (CanTSynGlobalTimeMaster Tool Configuration)
   :align: center


.. centered:: **表 CanTSynGlobalTimeMaster配置描述 (Table CanTSynGlobalTimeMaster Configuration Description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - CanTSynCyclicMsgResumeTime
     - 取值范围 (Range)
     - 0..INF
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 在立即传输之后，间隔多久发送第一帧常规循环时间同步报文。单位：秒。 (How long after immediate transfer is the first frame of regular cyclic time synchronization message sent. Unit: seconds.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无 (None)
     - 
     - 
   * - CanTSynGlobalTimeDebounceTime
     - 取值范围 (Range)
     - 0..INF
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - SYNC消息和FUP消息之间以及OFS和OFNS消息之间的发送间隔时间。 (The time interval between the sending of SYNC messages and FUP messages, as well as between OFS and OFNS messages.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无 (None)
     - 
     - 
   * - CanTSynGlobalTimeTxCrcSecured
     - 取值范围 (Range)
     - CRC_SUPPORTED/CRC_NOT_SUPPORTED
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 发送报文的CRC校验支持形式。 (Support for CRC check on sent messages.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 当其为CRC_SUPPORTED时，若CanTSynGlobalTimeDomainId为0-15，则需配置CanTSynGlobalTimeSyncDataIDList和CanTSynGlobalTimeFupDataIDList；若CanTSynGlobalTimeDomainId为16-31，则需配置CanTSynGlobalTimeOfsDataIDList和CanTSynGlobalTimeOfnsDataIDList。 (When CRC_SUPPORTED is enabled, if CanTSynGlobalTimeDomainId is 0-15, configure CanTSynGlobalTimeSyncDataIDList and CanTSynGlobalTimeFupDataIDList; if CanTSynGlobalTimeDomainId is 16-31, configure CanTSynGlobalTimeOfsDataIDList and CanTSynGlobalTimeOfnsDataIDList.)
     - 
     - 
   * - CanTSynGlobalTimeTxPeriod
     - 取值范围 (Range)
     - 0..INF
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 同步报文发送周期。 (Sync message sending period.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无 (None)
     - 
     - 
   * - CanTSynImmediateTimeSync
     - 取值范围 (Range)
     - True、False
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 开关在主函数中对StbM_GetTimeBaseUpdateCounter()的周期调用。 (The switch is called periodically in the main function for StbM_GetTimeBaseUpdateCounter().)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无 (None)
     - 
     - 
   * - CanTSynMasterConfirmationTimeout
     - 取值范围 (Range)
     - 0..INF
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 发送时间同步消息之后的确认等待超时。 (Timeout during confirmation wait after sending time synchronization message.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无 (None)
     - 
     - 




CanTSynGlobalTimeMasterPdu
------------------------------------------

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/CanTSyn/image15.png
   :alt: CanTSynGlobalTimeMasterPdu工具配置 (CanTSynGlobalTimeMasterPdu Tool Configuration)
   :name: CanTSynGlobalTimeMasterPdu工具配置 (CanTSynGlobalTimeMasterPdu Tool Configuration)
   :align: center


.. centered:: **表 CanTSynGlobalTimeMasterPdu配置描述 (Table CanTSynGlobalTimeMasterPdu Configuration Description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - CanTSynGlobalTimePduRef
     - 取值范围 (Range)
     - Reference
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 发送时间同步消息所用的pdu引用。 (Reference PDU for sending time synchronization messages.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - Pdu
     - 
     - 




CanTSynGlobalTimeSlave
======================================

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/CanTSyn/image16.png
   :alt: CanTSynGlobalTimeSlave工具配置 (CanTSynGlobalTimeSlave Tool Configuration)
   :name: CanTSynGlobalTimeSlave工具配置 (CanTSynGlobalTimeSlave Tool Configuration)
   :align: center


.. centered:: **表 CanTSynGlobalTimeSlave配置描述 (Table CanTSynGlobalTimeSlave Configuration Description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - CanTSynGlobalTimeFollowUpTimeout
     - 取值范围 (Range)
     - 0..INF
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 等待Follow_Up报文的超时时间。 (Timeout duration for waiting for the Follow_Up message.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无 (None)
     - 
     - 
   * - CanTSynGlobalTimeSequenceCounterJumpWidth
     - 取值范围 (Range)
     - 1..15
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 两帧SYNC或OFS消息之间的最大SequenceCounter差。 (The maximum difference in SequenceCounter between two frames of SYNC or OFS messages.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无 (None)
     - 
     - 
   * - CanTSynRxCrcValidated
     - 取值范围 (Range)
     - CRC_IGNORED/CRC_NOT_VALIDATED/
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 
     - CRC_OPTIONAL/
     - 
     - 
   * - 
     - 
     - CRC_VALIDATED
     - 
     - 
   * - 
     - 参数描述 (Parameter Description)
     - 接收报文的CRC校验支持形式。 (Support for CRC checksum on received messages.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 当其为CRC_OPTIONAL或CRC_VALIDATED时，若CanTSynGlobalTimeDomainId为0-15，则需配置CanTSynGlobalTimeSyncDataIDList和CanTSynGlobalTimeFupDataIDList；若CanTSynGlobalTimeDomainId为16-31，则需配置CanTSynGlobalTimeOfsDataIDList和CanTSynGlobalTimeOfnsDataIDList。 (When CanTSynGlobalTimeDomainId is 0-15 and CRC_OPTIONAL or CRC_VALIDATED, configure CanTSynGlobalTimeSyncDataIDList and CanTSynGlobalTimeFupDataIDList; when CanTSynGlobalTimeDomainId is 16-31, configure CanTSynGlobalTimeOfsDataIDList and CanTSynGlobalTimeOfnsDataIDList.)
     - 
     - 




CanTSynGlobalTimeSlavePdu
-----------------------------------------

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/CanTSyn/image17.png
   :alt: CanTSynGlobalTimeSlavePdu工具配置 (CanTSynGlobalTimeSlavePdu Tool Configuration)
   :name: CanTSynGlobalTimeSlavePdu工具配置 (CanTSynGlobalTimeSlavePdu Tool Configuration)
   :align: center


.. centered:: **表 CanTSynGlobalTimeSlavePdu配置描述 (Table CanTSynGlobalTimeSlavePdu Configuration Description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - CanTSynGlobalTimePduRef
     - 取值范围 (Range)
     - Reference
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 接收报文所用的pdu引用。 (Reference PDU for received messages.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - Pdu
     - 
     - 
