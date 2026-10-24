====================
CanTsyn
====================


文档信息(Document Information)
============================================================

版本历史(Version History)
--------------------------------------------------------------------------------------------------------

.. list-table::
   :widths: 10 10 10 10 20
   :header-rows: 1

   * - 日期(Date)
     - 作者(Author)
     - 版本(Version)
     - 状态(Status)
     - 说明(Description)

   * - 2025/3/2
     - xiongfei.shi
     - V0.1
     - 发布(Release)
     - 首次发布(First release)

   * - 2025/04/04
     - xiongfei.shi
     - V1.0
     - 发布(Release)
     - 正式发布(Official release)

   * - 2026/01/15
     - caihong.liu
     - V1.1
     - 增加
     - 补充3.0版本特性描述

参考文档(References)
--------------------------------------------------------------------------------------------------------

.. list-table::
   :widths: 10 10 30 10
   :header-rows: 1

   * - 编号(Number)
     - 分类(Classification)
     - 标题(Title)
     - 版本(Version)
   * - 1
     - Autosar
     - AUTOSAR_CP_SWS_TimeSyncOverCAN.pdf
     - R23-11
   * - 2
     - Autosar
     - AUTOSAR_CP_SWS_SynchronizedTimeBaseManager.pdf
     - R23-11


术语与简写(Terms and Abbreviations)
====================================================================


术语(Terms)
--------------------------------------------------------------------------------------------------------

.. :align: center   表格内容居中(Table contents are centered)

.. list-table::
   :widths: 10 40
   :header-rows: 1

   * - 术语(Terms)
     - 解释(Explanation)

   * - Global Time Domain
     - 全局时间域(Global Time Domain)

   * - Global Time Master
     - 全域时间主控(Global Time Master)

   * - Debounce Time
     - 同一PDU两条发送消息的最小间隔(Minimum Interval between Two Transmissions of the Same PDU)

   * - SYNC message
     - 时间同步消息(Time synchronization message)

   * - FUP message
     - 后续消息(Subsequent Message)


简写(Abbreviations)
--------------------------------------------------------------------------------------------------------
.. list-table::
   :widths: 10 20 30
   :header-rows: 1


   * - 简写(Abbreviation)
     - 全称(Full name)
     - 解释(Explanation)

   * - <Bus>TSyn
     - A bus specific Time Synchronization module
     - 特定总线时间同步模块

   * - CanTSyn
     - Time Synchronization module for CAN
     - CAN 时间同步模块

   * - CRC
     - Cyclic Redundancy Checksum
     - 循环冗余检验

   * - DET
     - Default Error Tracer
     - 默认错误跟踪器

   * - DLC
     - Data Length Code
     - 数据长度代码

   * - StbM
     - Synchronized Time-Base Manager
     - 同步的时间基管理

   * - TS
     - Time Slave
     - 时间从属

   * - Timesync
     - Time Synchronization
     - 时间同步

简介(Introduction)
===================================================
  CanTSyn 在 AutoSAR 软件层级架构如下图， 其所属于时间同步栈。

  The software layer architecture of StbM in AutoSAR is shown in the figure below. It belongs to the time synchronization stack.

  .. figure:: /_static/参考手册(Module_Reference_Manual)/CanTSyn/CanTSyn_In_AutoSAR.png
    :alt: CanTSyn在AUTOSAR中的位置(Position of CanTSyn in AUTOSAR))
    :name: CanTSyn_fig_arch
    :align: center

  CanTSyn 在 AUTOSAR 中的位置 (Position of CanTSyn in AUTOSAR)


  本文中描述CanTSyn，StbM负责管理时间域，给CanTSyn提供接口用来更新同步时间，给其他用户提供接口用来获取/通知同步时间。CanTSyn负责Can总线上的时间同步。

  As described in this document, CanTSyn works with StbM. StbM is responsible for managing the time domain, providing an interface for CanTSyn to update the synchronized time, and providing interfaces for other users to get/notify the synchronized time. CanTSyn is responsible for time synchronization over the CAN bus.


功能描述(Functional Description)
===============================================================
.. 本章节仅描述模块支持的功能大致情况，不宜做细致描述；更加细致的描述在配置章节，结合配置，从集成角度描述

  CanTSyn模块和StbM模块息息相关，StbM模块提供了时间同步的功能和时钟实例，但不负责在各个总线内的时间分发任务。那么CanTSyn模块就处理了在CAN总线发放时间信息的任务。

  The CanTSyn module is closely related to the StbM module. The StbM module provides time synchronization function and clock instances but is not responsible for the task of time distribution on individual buses. Therefore, the CanTSyn module handles the task of distributing time information on the CAN bus.

  仅仅通过广播的方式把时间信息从Time Masters发送到Time Slaves会导致时间不精准，这是因为CAN总线传输仲裁机制以及BSW的延迟。

  Simply broadcasting time information from Time Masters to Time Slaves may lead to inaccuracies due to the CAN bus arbitration mechanism and BSW latency. 

  具体实现上我们通过以下的两步算法来尽可能消除这样的延迟：

  In practice, this latency is minimized by implementing the following two-step algorithm:

    第一步：发送方(Time Master)首先记录当前的同步时间(SYNC)以及本地时间(T0VLT)并在第一个广播信息(所谓的SYNC信息)里，把同步好的时间的秒部分(SYNCSEC)作为内容发送。

    Step 1: The sender (Time Master) first records the current synchronized time (SYNC) and the local time (T0VLT), and in the first broadcast message (the SYNC message), sends the seconds part of the synchronized time (SYNCSEC). 

    发送方在收到 “CAN transmit confirmation”时记录时间戳来得到信息实际发送的时间点(T1VLT)。接收方(Time Slave)收到信息 “CAN receive indication”时记录时间戳来检测信息实际收到的时间点(T2VLT)。

    The sender records the timestamp Upon receiving "CAN transmit confirmation" to get the actual transmission time of the message (T1VLT). The receiver (Time Slave) records the timestamp upon receiving "CAN receive indication" to detect the actual time the message was received (T2VLT).

    第二步：在第二个同步信息(所谓的FUP(follow-up)信息)里，发送方发送T4作为内容，T4为SYNC消息准备发送和实际发送的时间差(T1VLT-T0VLT)加上T0SYNCNS(同步时间的纳秒部分)(T4=T0SYNCNS+(T1VLT-T0VLT))。对于发送方来说，此时T0SYNCSEC+T4就为同步时间。Time Slave现在从SYNC和FUP消息里获取了足够的信息，再加上先前记录的时间戳T2VLT，就可以确定更加确切的时间信息。接收方将(T0SYNCSEC+T4)和T2VLT时间对信息传给StbM, StbM即可计算同步时间，完成一次Time Master和Time Slave之间的时间同步。

    Step 2: In the second synchronization message (the FUP, or follow-up, message), the sender transmits T4 as the content. T4 is the difference between the intended and actual transmission time of the SYNC message (T1VLT - T0VLT), plus the nanoseconds part of the synchronized time (T0SYNCNS). Thus, T4 = T0SYNCNS + (T1VLT - T0VLT). For the sender, the synchronized time at this point is T0SYNCSEC + T4. Time Slave now has obtained sufficient information from the SYNC and FUP messages, and along with its previously recorded timestamp T2VLT, it can determine a more precise time. The receiver passes the time pair information, (T0SYNCSEC + T4) and T2VLT, to StbM. StbM can then calculate the synchronized time, completing the time synchronization cycle between Time Master and Time Slave.

公共特性(Public Features)
----------------------------

多核多分区功能(Multi-core and Multi-partition Features)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  - CanTSyn模块无分区配置参数，从CanTSynPort关联的CanIfController获取分区分布，使用Can硬件时钟时要考虑硬件是否支持跨分区访问

  The CanTSyn module has no dedicated partition configuration parameters; it acquires the partition distribution from the CanIfController associated with the CanTSynPort. When using a CAN hardware clock, it is necessary to consider whether the hardware supports cross-partition access.
    
  - CanTSynGlobalTimeDomin引用的CanIfCcontroller分区，为各个 port 定义全局变量分配到相应的分区及定义MainFunction。

  Based on the partition of the CanIfController referenced by CanTSynGlobalTimeDomain, global variables are defined for each port and allocated to their respective partitions, and the MainFunction is defined accordingly.

.. only:: doc_pbs

   PBS功能(PBS Features)
   ~~~~~~~~~~~~~~~~~~~~~~~~
   - 支持同一个时间域配置不同的SYNC报文DataIDList进行CRC校验。
    
   Support configuring different SYNC message DataIDLists under the same time domain for CRC checksum.

   - 支持同一个时间域下配置不同的FUP报文DataIDList进行CRC校验。

   Support configuring different FUP message DataIDLists under the same time domain for CRC checksum.

   - 支持同一个时间域配置不同的时间同步角色，且相应角色的参数均可配置为不同值。

   Support configuring different time synchronization roles under the same time domain, and the parameters for each role can be configured with different values.

Memmap功能(Memmap Features)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  memmap文件是动态的。存在CANTSYN_START_SEC_CODE、CANTSYN_STOP_SEC_CODE、CANTSYN_START_SEC_CODE_FAST、CANTSYN_STOP_SEC_CODE_FAST、CANTSYN_START_SEC_CONFIG_DATA_32、CANTSYN_STOP_SEC_CONFIG_DATA_32、CANTSYN_START_SEC_CONFIG_DATA_UNSPECIFIED、CANTSYN_STOP_SEC_CONFIG_DATA_UNSPECIFIED、CANTSYN_START_SEC_VAR_CLEARED_GLOBAL_8、CANTSYN_STOP_SEC_VAR_CLEARED_GLOBAL_8、CANTSYN_START_SEC_VAR_CLEARED_GLOBAL_PTR、CANTSYN_STOP_SEC_VAR_CLEARED_GLOBAL_PTR、CANTSYN_START_SEC_CONST_PTR、CANTSYN_STOP_SEC_CONST_PTR、CANTSYN_START_SEC_VAR_CLEARED_GLOBAL_UNSPECIFIED、CANTSYN_STOP_SEC_VAR_CLEARED_GLOBAL_UNSPECIFIED、CANTSYN_START_SEC_VAR_CLEARED_{{PartitionName}}_UNSPECIFIED、CANTSYN_STOP_SEC_VAR_CLEARED_{{PartitionName}}_UNSPECIFIED 字段。

  The memmap file is dynamic. There are CANTSYN_START_SEC_CODE、CANTSYN_STOP_SEC_CODE、CANTSYN_START_SEC_CODE_FAST、CANTSYN_STOP_SEC_CODE_FAST、CANTSYN_START_SEC_CONFIG_DATA_32、CANTSYN_STOP_SEC_CONFIG_DATA_32、CANTSYN_START_SEC_CONFIG_DATA_UNSPECIFIED、CANTSYN_STOP_SEC_CONFIG_DATA_UNSPECIFIED、CANTSYN_START_SEC_VAR_CLEARED_GLOBAL_8、CANTSYN_STOP_SEC_VAR_CLEARED_GLOBAL_8、CANTSYN_START_SEC_VAR_CLEARED_GLOBAL_PTR、CANTSYN_STOP_SEC_VAR_CLEARED_GLOBAL_PTR、CANTSYN_START_SEC_CONST_PTR、CANTSYN_STOP_SEC_CONST_PTR、CANTSYN_START_SEC_VAR_CLEARED_GLOBAL_UNSPECIFIED、CANTSYN_STOP_SEC_VAR_CLEARED_GLOBAL_UNSPECIFIED、CANTSYN_START_SEC_VAR_CLEARED_{{PartitionName}}_UNSPECIFIED、CANTSYN_STOP_SEC_VAR_CLEARED_{{PartitionName}}_UNSPECIFIED fields.

独占区功能(Exclusive Area Features)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  None.

模块特性(Module Features)
------------------------------------------------------------------------------------------------------

消息格式(Message Format)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  CanTSyn的协议格式即支持标准CAN模式也支持扩展CAN模式。

  The protocol format of CanTSyn supports both standard CAN and extended CAN modes.


时间同步主站(Time Synchronization Master)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  CanTSyn支持配置为时间主站，将时间同步给同网络下的其他时间从站。

  CanTSyn can be configured as a Time Master to synchronize time with other Time Slaves on the same network.

时间同步从站(Time Synchronization Slave)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  CanTSyn支持配置为时间从站，接受同网络下的时间主机的同步消息，将自己的时间与主站同步。

  CanTSyn can be configured as a Time Slave to receive synchronization messages from the Time Master on the same network and synchronize its own time with the master's time.

支持硬件时间戳(Hardware Timestamp Support)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  CanTSyn模块支持使用CAN硬件时间戳功能来获取发送和接收时间戳，从而提高时间同步的精度。前提需要使用支持时间戳功能的CAN控制器，并在配置中启用硬件时间戳支持选项。

  The CanTSyn module supports the use of the CAN hardware timestamping function to obtain transmission and reception timestamps, thereby improving the accuracy of time synchronization. The prerequisite is to use a CAN controller that supports the timestamping function and to enable the hardware timestamping support option in the configuration.

安全时间同步(Secure Time Synchronization)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  安全时间同步通过为 Follow_Up 报文添加附加的认证信息来实现。安全认证信息主要包括两个部分：新鲜度值（Freshness Value，FV）和完整性校验值（Integrity Check Value，ICV）。

  Secure time synchronization is achieved by adding additional authentication information to the Follow_Up message. The security authentication information primarily consists of two parts: the Freshness Value (FV) and the Integrity Check Value (ICV). 

  在获取 FV 和生成/验证 ICV 的过程中，若获取失败或者验证失败则会跳过处理并报告相应的安全事件。

  During the process of obtaining the FV and generating or verifying the ICV, if acquisition or verification fails, the processing is skipped and the corresponding security event is reported.

新鲜度值(Freshness Value)
******************************
  首先，每个 Timebase 都至少配置一个新鲜度值（Freshness Value，FV）。

  First, each Timebase is configured with at least one Freshness Value (FV).

  FV 指向一个单调递增的计数机制，用于确保该时间基准的新鲜性，即保证被接收的时间信息在时间顺序上不发生回退，从而防止旧时间信息被重放使用。
  该单调递增机制可以通过独立的消息计数器（Freshness Counter）实现，也可以通过时间戳值（Freshness Timestamp）来实现。

  The FV points to a monotonically increasing counting mechanism used to ensure the freshness of the time base, guaranteeing that the received time information does not regress in chronological order to prevent the replay of old time information. This monotonic mechanism can be implemented through an independent Message Counter (Freshness Counter) or via a Freshness Timestamp.

  FV 在StbM中进行管理和维护：

  FV is managed and maintained within the StbM:

    1. 发送 Follow_Up 报文时，会根据配置通过指定的 API 从 StbM 获取当前 Timebase 对应的 FV，并将其附加在 Follow_Up 报文。

    When transmitting a Follow_Up message, the FV corresponding to the current Timebase is obtained from the StbM via the specified API based on the configuration and attached to the Follow_Up message.

    2. 接收端在处理收到的 Follow_Up 报文时，从 StbM 获取当前 Timebase 对应的 FV，并将其构建 ICV 生成报文进行完整性校验。

    When the receiver processes the incoming Follow_Up message, it obtains the FV corresponding to the current Timebase from the StbM and uses it to construct the ICV generation message for integrity verification.

  若 FV 获取失败则跳过 ICV 的计算和附加过程，会向 Follow_Up 报文中写入标志位标识该消息不具备认证能力。

  If FV acquisition fails, the ICV calculation and attachment process is skipped, and a flag is written into the Follow_Up message to indicate that the message does not possess authentication capability.

完整性校验值(Integrity Check Value)
***********************************************************
  ICV 指的是密码学函数的计算结果，用于确保能够检测到对消息的未授权修改。该密码学函数可以采用任意一种密码学原语，并结合相应的密码密钥来实现。

  ICV refers to the calculation result of a cryptographic function, used to ensure that unauthorized modifications to the message can be detected. This cryptographic function can employ any cryptographic primitive and be implemented in combination with a corresponding cryptographic key.

  对应于接收端的 ICV 的使用是可选的。为了在多个时间观测单元之间实现较大的灵活性，相关配置会决定如何处理带有 ICV 的报文。

  The use of ICV on the receiver side is optional. To achieve greater flexibility across multiple time observation units, relevant configurations determine how messages with ICV are processed.

  如果接收端不启用 ICV 校验，则可能仅使用接收到的数值，而不对 ICV 本身进行验证。

  If the receiver does not enable ICV verification, it may only use the received values without verifying the ICV itself.

  ICV 的计算和验证算法由 Csm 模块负责实现：

  The ICV calculation and verification algorithms are implemented by the Csm module:

    1. 发送端在发送 Follow_Up 报文时，在获取 FV 后，构造用于生成 ICV 的数据后调用 Csm 提供的 API 来计算 ICV，并将其附加在 Follow_Up 报文的认证 TLV 中。

    When the transmitter sends a Follow_Up message, after obtaining the FV, it constructs the data for ICV generation and calls the API provided by the Csm to calculate the ICV, attaching it to the authentication TLV of the Follow_Up message.

    2. 接收端在处理收到的 Follow_Up 报文时，提取出 ICV，同样需要先获取 FV 后构造用于验证 ICV 的数据调用 Csm 提供的 API 来验证 ICV 的正确性。

    When the receiver processes the received Follow_Up message, it extracts the ICV; similarly, it must first obtain the FV and construct the data for ICV verification, then call the API provided by the Csm to verify the correctness of the ICV.

  构造的数据范围从 Follow_Up 报文起一个起始字节直到 FV 字段的末尾字节，并不包括 ICV 字段本身。

  The range of the constructed data starts from a beginning byte of the Follow_Up message to the end byte of the FV field, excluding the ICV field itself.

  若配置上选择使用截取的 FV，当构造校验数据时使用完整的 FV，但是实际发送的 Follow_Up 报文中填充截取后的 FV。

  If the configuration selects the use of a truncated FV, the full FV is used when constructing the verification data, but the truncated FV is filled into the actually transmitted Follow_Up message.

时间记录(Time Recording)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  为时间同步系统能够在运行过程中检测主从节点之间的时间偏差、识别时间同步劣化或异常情况，并从全系统视角判断是否建立了可信的一致时间基准，因此引入Time Validation特性。

  The Time Validation feature is introduced to enable the time synchronization system to detect time deviations between master and slave nodes during operation, identify time synchronization degradation or anomalies, and determine from a system-wide perspective whether a trusted and consistent time base has been established.

  TimeSync 模块需要能够采集时间同步状态信息，并将这些信息提供给应用（即Validator SWC），以支持 Time Validation 功能的实现。Time Slave、Time Master 以及 Time Gateway 会从相应的 TimeSync 模块中收集时间同步过程的相关信息，例如：基于其本地的全局时间实例（通过使用 SyncLocal Time Tuple）、时间同步报文的接收时间戳、时间同步报文中的全局时间信息等，来计算时间偏差和其他相关指标。

  The TimeSync module must be able to collect time synchronization status information and provide this information to the application (i.e., Validator SWC) to support the implementation of the Time Validation function. Time Slave, Time Master, and Time Gateway will collect information related to the time synchronization process from the corresponding TimeSync modules—for example, based on their local global time instances (by using SyncLocal Time Tuple), reception timestamps of time synchronization messages, and global time information within time synchronization messages—to calculate time deviations and other relevant metrics.

  CanTSyn 模块通过 StbM 各个接口将各个阶段的时间同步信息传递到 StbM。

  The CanTSyn module passes time synchronization information from each stage to the StbM through various StbM interfaces.

偏差(Deviation)
--------------------------------------------------------------------
  None
  
.. 有序列表示例

  1. 不再支持偏移时间的同步，配置中删除CanTSynGlobalTimeOfsDataIDList配置项和CanTSynGlobalTimeOfnsDataIDList配置项

  Synchronization of offset time is no longer supported; the CanTSynGlobalTimeOfsDataIDList and CanTSynGlobalTimeOfnsDataIDList configuration items have been removed.

  2. 不支持时间验证功能

  Time verification function is not supported

扩展(Extension)
--------------------------------------------------------------------
  None

集成(Integration)
========================================

文件列表(File List)
--------------------------------------------------------------------

静态文件(Static Files)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - 文件(File)
     - 描述(Description)

   * - CanTSyn.h
     - 包含需要使用的宏定义，类型定义，配置结构体声明，外部函数声明(Contains macro definitions, type definitions, configuration structure declarations, and external function declarations that need to be used)

   * - CanTSyn_Cbk.h
     - 包含需要使用的宏定义，类型定义，配置结构体声明，外部回调函数声明(Contains macro definitions, type definitions, configuration structure declarations, and external callback function declarations that need to be used)

   * - CanTSyn_Internal.h
     - 包含需要使用的内部宏定义，内部类型定义，外部数据声明和外部函数声明(Contains internal macro definitions, internal type definitions, external data declarations, and external function declarations that need to be used)

   * - CanTSyn.c
     - 包含需要使用的宏定义，内部变量，内部函数，全局函数(Contains macro definitions, internal variables, internal functions, and global functions that need to be used)


动态文件(Dynamic Files)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - 文件(File)
     - 描述(Description)

   * - CanTSyn_MemMap.h
     - CanTSyn模块的内存映射(Memory mapping of the CanTrcv module)

   * - CanTSyn_Cfg.h
     - 定义CanTSyn模块预编译时用到的配置参数(Defines configuration parameters used in the pre-compilation of the CanTSyn module)

   * - CanTSyn_Cfg.c
     - CanTSyn Pre-Compile 配置源文件(Pre-Compile configuration source file of CanTSyn)

   * - CanTSyn_PBcfg.h
     - 包含CanTSyn模块内部宏定义和PB配置的数据类型定义(Contains internal macro definitions of the CanTSyn module and data type definitions for post-build configuration)

   * - CanTSyn_PBcfg.c
     - CanTSyn Post-Build 配置源文件(Post-Build configuration source file of CanTSyn)

错误处理(Error Handling)
------------------------------------------------------------------------

开发错误(Development Errors)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. list-table::
   :widths: 20 10 30
   :header-rows: 1

   * - Error code
     - Value[hex]
     - Description

   * - CANTSYN_E_INVALID_PDUID
     - 0x01
     - API service called with wrong PDU or SDU

   * - CANTSYN_E_UNINIT
     - 0x02
     - API service used in un-initialized state

   * - CANTSYN_E_NULL_POINTER
     - 0x03
     - A pointer is NULL

   * - CANTSYN_E_INIT_FAILED
     - 0x04
     - CanTSyn initialization failed

   * - CANTSYN_E_PARAM
     - 0x05
     - API called with invalid parameter

   * - CANTSYN_E_INV_CTRL_IDX
     - 0x06
     - Invalid Controller index

   * - CANTSYN_E_INVALID_PARTITION
     - 0xF0
     - CanTSyn accessed by wrong partition

   * - CANTSYN_E_ALREADY_INITIALIZED
     - 0xF1
     - CanTSyn has initialized

产品错误(Product Errors)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  None

运行时错误(Runtime Errors)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  None

接口描述(Interface Description)
==============================================================

.. 目前能够自动生成的有类型定义，普通函数，回调函数。
.. 有些模块的API来自多个头文件，需要自行裁剪合并
.. 引用接口描述。来自于code->doxygen->xml->rst
.. 引用接口描述。 From code->doxygen->xml->rst

.. include:: CanTSyn_h_api.rst
.. include:: CanTSyn_Cbk_h_api.rst
.. include:: CanTSyn_Internal_h_api.rst


配置函数(Configuration function)
----------------------------------------------------------------------------------------

.. 可选的章节，根据模块实际情况确定
.. 格式同提供的服务

CanTSyn_MainFunction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void CanTSyn_MainFunction(void)

This function needs to be called periodically to perform the AUTOSAR CanTSyn activities.

**Sync/Async**
   Asynchronous

**Reentrancy**
   Reentrant (Reentrant for different partitions. Non reentrant for the same partition.)

**Return type**
   void

依赖的服务(Applicable Services)
----------------------------------------------------------------------------------------

.. - 本章节暂时无法自动化生成，需在第八章最后部分手动copy
.. - 接口有几种类型，根据实际情况选择，没有的章节就不写，格式都一样

强制接口(Compulsory interface)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. 可选的章节，根据模块实际情况确定

.. list-table::
   :widths: 10 5 30
   :header-rows: 1

   * - API Function
     - Header File
     - Description

   * - StbM_GetCurrentTime
     - StbM.h
     - Returns a time value(Local Time Base derived from Global Time Base) in standard format.

   * - StbM_GetTimeBaseUpdateCounter
     - StbM.h
     - Get the time base update counter value, that indicates a Time Base update to the Timesync Modules.

   * - StbM_GetTimeBaseStatus
     - StbM.h
     - Returns detailed status information for a Synchronized(or Pure Local) Time Base.

   * - StbM_GetCurrentVirtualLocalTime
     - StbM.h
     - Returns the Virtual Local Time of the referenced Time Base..

   * - CanIf_Transmit
     - CanIf.h
     - Requests transmission of a PDU.


可选接口(Optional Interface)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. 可选的章节，根据模块实际情况确定
.. 格式同强制接口

.. list-table::
   :widths: 10 5 30
   :header-rows: 1

   * - API Function
     - Header File
     - Description

   * - Det_ReportError
     - Det.h
     - Service to report development errors.

   * - Crc_CalculateCRC8H2F
     - Crc.h
     - Calculate CRC value.

   * - GetApplicationID
     - Os.h
     - Get application ID.


配置接口(Configuration Interfaces)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. 可选的章节，根据模块实际情况确定
.. 格式同强制接口

  None

配置(Configuration)
====================================
  1. 各CanTSynGlobalTimeDomain的CanTSynGlobalTimeDomainId是唯一的，不能出现相同。

  CanTSynGlobalTimeDomainId for each CanTSynGlobalTimeDomain must be unique.

  2. 如果使能了CRC校验，那么相同CanTSynGlobalTimeDomainId的Master和Slave的CanTSynGlobalTimeSyncDataIDList、CanTSynGlobalTimeFupDataIDListElement配置项必须相同，否则校验不过。

  If CRC checksum is enabled, CanTSynGlobalTimeSyncDataIDList and CanTSynGlobalTimeFupDataIDListElement configuration items must be identical for the Master and Slave within the same CanTSynGlobalTimeDomainId; otherwise, the check will fail.

完整性校验值发送端配置描述(Transmitter ICV Config Description)
----------------------------------------------------------------------------------------
  1. 为 CanTSynGlobalTimeMaster 添加子容器 CanTSynGlobalTimeTxIcvGeneration 用于配置完整性校验值发送端的相关参数：

  Add a sub-container CanTSynGlobalTimeTxIcvGeneration to CanTSynGlobalTimeMaster for configuring the relevant parameters of the Integrity Check Value transmitter side:

  .. figure:: /_static/参考手册(Module_Reference_Manual)/CanTSyn/CanTSynGlobalTimeTxIcvGeneration.png
    :alt: CanTSyn发送端ICV配置
    :align: center

  CanTSyn发送端ICV配置(CanTSyn Transmitter ICV Configuration)

  2. 其中 CanTSynIcvGenerationFvIdRef 需要引用 StbMFreshnessValue 的配置：

  Where CanTSynIcvGenerationFvIdRef needs to reference the StbMFreshnessValue configuration:

  .. figure:: /_static/参考手册(Module_Reference_Manual)/EthTSyn/StbMFreshnessValue.png
    :alt: CanTSyn引用 FV 配置
    :align: center

  CanTSyn引用 FV 配置(CanTSyn Reference FV Configuration)

  3. 其中 CanTSynIcvGenerationJobRef 需要引用 CsmJob 的配置：

  Where CanTSynIcvGenerationJobRef needs to reference the CsmJob configuration:

  .. figure:: /_static/参考手册(Module_Reference_Manual)/EthTSyn/CsmJobs.png
    :alt: CanTSyn引用 CsmJob 配置
    :align: center

  CanTSyn引用 CsmJob 配置(CanTSyn Reference CsmJob Configuration)

完整性校验值接收端配置描述(Receiver ICV Config Description)
----------------------------------------------------------------------------------------
  1. 为 CanTSynGlobalTimeSlave 添加子容器 CanTSynGlobalTimeRxIcvVerification 用于配置完整性校验值接受端的相关参数：

  Add a sub-container CanTSynGlobalTimeRxIcvVerification to CanTSynGlobalTimeSlave for configuring the relevant parameters of the Integrity Check Value receiver side:

  .. figure:: /_static/参考手册(Module_Reference_Manual)/CanTSyn/CanTSynGlobalTimeRxIcvVerification.png
    :alt: CanTSyn接收端ICV配置
    :align: center

  CanTSyn接收端ICV配置(CanTSyn Receiver ICV Configuration)

  2. 其中 CanTSynIcvVerificationFvIdRef 需要引用 StbMFreshnessValue 的配置同于发送端

  Where CanTSynIcvVerificationFvIdRef needs to reference the StbMFreshnessValue configuration, the same as the transmitter side.

  3. 其中 CanTSynIcvVerificationJobRef 需要引用 CsmJob 的配置同于发送端

  Where CanTSynIcvVerificationJobRef needs to reference the CsmJob configuration, the same as the transmitter side.

Can硬件时钟使能(CAN Hardware Clock Enable)
----------------------------------------------------------------------------------------
  1. 当 Can 硬件支持时间戳功能时，可以通过配置使能 CanTSynHardwareTimeStampSupport 选项来使能硬件时间戳功能.

  When the CAN hardware supports the timestamping function, the hardware timestamping function can be enabled by configuring the CanTSynHardwareTimeStampSupport option.

  .. figure:: /_static/参考手册(Module_Reference_Manual)/CanTSyn/CanTSynHardwareTimeStampSupport.png
    :alt: CanTSynHardwareTimeStampSupport配置
    :align: center

  CanTSynHardwareTimeStampSupport配置(CanTSynHardwareTimeStampSupport Configuration)

  2. 同时，需要在 CanIf 中配置 CanIfGlobalTimeSupport 选项来使能全局时间支持。（该配置项使能依赖于 CanIfPublicCtrlDrvVersion，功能较旧的控制器不支持硬件时钟）

  Meanwhile, the CanIfGlobalTimeSupport option needs to be configured in the CanIf to enable global time support. (The enablement of this configuration item depends on CanIfPublicCtrlDrvVersion; controllers with older functionality do not support the hardware clock.)

  .. figure:: /_static/参考手册(Module_Reference_Manual)/CanTSyn/CanIfGlobalTimeSupport.png
    :alt: CanIfGlobalTimeSupport配置
    :align: center

  CanIfGlobalTimeSupport配置(CanIfGlobalTimeSupport Configuration)

时间记录配置描述(Time Recording Config Description)
----------------------------------------------------------------------------------------
  1. CanTSyn 需要使能 CanTSynTimeValidationSupport 和 CanTSynEnableTimeValidation 两个配置选项：

  CanTSyn needs to enable two configuration options: CanTSynTimeValidationSupport and CanTSynEnableTimeValidation:

  .. figure:: /_static/参考手册(Module_Reference_Manual)/CanTSyn/CanTSynEnableTimeValidation.png
    :alt: CanTSynEnableTimeValidation配置
    :align: center

  CanTSynEnableTimeValidation配置(CanTSynEnableTimeValidation Configuration)

  2. StbM 需要为 Timebase 配置 StbMTimeValidation:

  StbM needs to configure StbMTimeValidation for the Timebase:

  .. figure:: /_static/参考手册(Module_Reference_Manual)/EthTSyn/StbMTimeRecording.png
    :alt: StbMTimeRecording配置
    :align: center

  StbMTimeRecording配置(StbMTimeRecording Configuration)
