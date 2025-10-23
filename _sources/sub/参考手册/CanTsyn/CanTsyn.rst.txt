====================
CanTsyn
====================


文档信息 Document Information
============================================================

版本历史 Version History
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

参考文档 References
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


术语与简写 Terms and Abbreviations
====================================================================


术语 Terms
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


简写 Abbreviations
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

简介 Introduction
===================================================
CanTSyn 在 AutoSAR 软件层级架构如下图， 其所属于时间同步栈。

The software layer architecture of StbM in AutoSAR is shown in the figure below. It belongs to the time synchronization stack.

.. figure:: ../../../_static/参考手册/CanTSyn/CanTSyn_In_AutoSAR.png
   :alt: CanTSyn在AUTOSAR中的位置(Position of CanTSyn in AUTOSAR))
   :name: CanTSyn_fig_arch
   :align: center

   CanTSyn 在 AUTOSAR 中的位置 (Position of CanTSyn in AUTOSAR)


本文中描述CanTSyn，StbM负责管理时间域，给CanTSyn提供接口用来更新同步时间，给其他用户提供接口用来获取/通知同步时间。CanTSyn负责Can总线上的时间同步。

As described in this document, CanTSyn works with StbM. StbM is responsible for managing the time domain, providing an interface for CanTSyn to update the synchronized time, and providing interfaces for other users to get/notify the synchronized time. CanTSyn is responsible for time synchronization over the CAN bus.


功能描述 Functional Description
===============================================================
.. 本章节仅描述模块支持的功能大致情况，不宜做细致描述；更加细致的描述在配置章节，结合配置，从集成角度描述

CanTSyn模块和StbM模块息息相关，StbM模块提供了时间同步的功能和时钟实例，但不负责在各个总线内的时间分发任务。那么CanTSyn模块就处理了在CAN总线发放时间信息的任务。

The CanTSyn module is closely related to the StbM module. The StbM module provides time synchronization function and clock instances but is not responsible for the task of time distribution on individual buses. Therefore, the CanTSyn module handles the task of distributing time information on the CAN bus.

仅仅通过广播的方式把时间信息从Time Masters发送到Time Slaves会导致时间不精准，这是因为CAN总线传输仲裁机制以及BSW的延迟。

Simply broadcasting time information from Time Masters to Time Slaves may lead to inaccuracies due to the CAN bus arbitration mechanism and BSW latency. 

具体实现上我们通过以下的两步算法来尽可能消除这样的延迟：

In practice, this latency is minimized by implementing the following two-step algorithm:

第一步：发送方（Time Master）首先记录当前的同步时间（SYNC）以及本地时间(T0VLT)并在第一个广播信息（所谓的SYNC信息）里，把同步好的时间的秒部分（SYNCSEC）作为内容发送。

Step 1: The sender (Time Master) first records the current synchronized time (SYNC) and the local time (T0VLT), and in the first broadcast message (the SYNC message), sends the seconds part of the synchronized time (SYNCSEC). 

发送方在收到 “CAN transmit confirmation”时记录时间戳来得到信息实际发送的时间点（T1VLT）。接收方（Time Slave）收到信息 “CAN receive indication”时记录时间戳来检测信息实际收到的时间点（T2VLT）。

The sender records the timestamp Upon receiving "CAN transmit confirmation" to get the actual transmission time of the message (T1VLT). The receiver (Time Slave) records the timestamp upon receiving "CAN receive indication" to detect the actual time the message was received (T2VLT).

第二步：在第二个同步信息（所谓的FUP（follow-up）信息）里，发送方发送T4作为内容，T4为SYNC消息准备发送和实际发送的时间差（T1VLT-T0VLT）加上T0SYNCNS（同步时间的纳秒部分）（T4=T0SYNCNS+(T1VLT-T0VLT)）。对于发送方来说，此时T0SYNCSEC+T4就为同步时间。Time Slave现在从SYNC和FUP消息里获取了足够的信息，再加上先前记录的时间戳T2VLT，就可以确定更加确切的时间信息。接收方将(T0SYNCSEC+T4)和T2VLT时间对信息传给StbM, StbM即可计算同步时间，完成一次Time Master和Time Slave之间的时间同步。

Step 2: In the second synchronization message (the FUP, or follow-up, message), the sender transmits T4 as the content. T4 is the difference between the intended and actual transmission time of the SYNC message (T1VLT - T0VLT), plus the nanoseconds part of the synchronized time (T0SYNCNS). Thus, T4 = T0SYNCNS + (T1VLT - T0VLT). For the sender, the synchronized time at this point is T0SYNCSEC + T4. Time Slave now has obtained sufficient information from the SYNC and FUP messages, and along with its previously recorded timestamp T2VLT, it can determine a more precise time. The receiver passes the time pair information, (T0SYNCSEC + T4) and T2VLT, to StbM. StbM can then calculate the synchronized time, completing the time synchronization cycle between Time Master and Time Slave.

特性 Features
------------------------------------------------------------------------------------------------------

.. only:: doc_pbs

  变体 Variant
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  .. 支持PBS的模块，必须具有本章节，以功能为导向描述模块级别的变体支持情况
  .. 主要功能必须描述，比较偏尽量描述（不强制）

  - 支持同一个时间域配置不同的SYNC报文DataIDList进行CRC校验。
  - Support configuring different SYNC message DataIDLists under the same time domain for CRC checksum.
  - 支持同一个时间域下配置不同的FUP报文DataIDList进行CRC校验。
  - Support configuring different FUP message DataIDLists under the same time domain for CRC checksum.
  - 支持同一个时间域配置不同的时间同步角色，且相应角色的参数均可配置为不同值。
  - Support configuring different time synchronization roles under the same time domain, and the parameters for each role can be configured with different values.

消息格式 Message Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
CanTSyn的协议格式即支持标准CAN模式也支持扩展CAN模式。

The protocol format of CanTSyn supports both standard CAN and extended CAN modes.


时间同步主站 Time Synchronization Master
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
CanTSyn支持配置为时间主站，将时间同步给同网络下的其他时间从站。

CanTSyn can be configured as a Time Master to synchronize time with other Time Slaves on the same network.

时间同步从站 Time Synchronization Slave
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
CanTSyn支持配置为时间从站，接受同网络下的时间主机的同步消息，将自己的时间与主站同步。

CanTSyn can be configured as a Time Slave to receive synchronization messages from the Time Master on the same network and synchronize its own time with the master's time.


偏差 Deviation
--------------------------------------------------------------------

.. 有序列表示例

1.不再支持偏移时间的同步，配置中删除CanTSynGlobalTimeOfsDataIDList配置项和CanTSynGlobalTimeOfnsDataIDList配置项

1.Synchronization of offset time is no longer supported; the CanTSynGlobalTimeOfsDataIDList and CanTSynGlobalTimeOfnsDataIDList configuration items have been removed.

2.不支持CAN的硬件时间戳

2.CAN hardware timestamps are not supported.

3.不支持时间验证功能

3.Time verification function is not supported

4.不支持数据完整性检查功能(ICV)

4.The data integrity check function (ICV) is not supported.


扩展 Extension
--------------------------------------------------------------------
None


集成 Integration
========================================

文件列表 File List
--------------------------------------------------------------------

静态文件 Static Files
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


动态文件 Dynamic Files
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

   * - CanTSyn_PBcfg.c
     - CanTSyn Post-Build 配置源文件(Post-Build configuration source file of CanTSyn)


错误处理 Error Handling
------------------------------------------------------------------------

开发错误 Development Errors
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

产品错误 Product Errors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

None

运行时错误 Runtime Errors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

None


接口描述 Interface Description
==============================================================

.. 目前能够自动生成的有类型定义，普通函数，回调函数。
.. 有些模块的API来自多个头文件，需要自行裁剪合并
.. 引用接口描述。来自于code->doxygen->xml->rst
.. 引用接口描述。 From code->doxygen->xml->rst

.. include:: CanTSyn_h_api.rst
.. include:: CanTSyn_Cbk_h_api.rst
.. include:: CanTSyn_Internal_h_api.rst


配置函数 Configuration function
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

依赖的服务 Applicable Services
----------------------------------------------------------------------------------------

.. - 本章节暂时无法自动化生成，需在第八章最后部分手动copy
.. - 接口有几种类型，根据实际情况选择，没有的章节就不写，格式都一样

强制接口 Compulsory interface
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


可选接口 Optional Interface
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


配置接口 Configuration Interfaces
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. 可选的章节，根据模块实际情况确定
.. 格式同强制接口

None


配置 Configuration
====================================

1.各CanTSynGlobalTimeDomain的CanTSynGlobalTimeDomainId是唯一的，不能出现相同。

1.CanTSynGlobalTimeDomainId for each CanTSynGlobalTimeDomain must be unique.

2.如果使能了CRC校验，那么相同CanTSynGlobalTimeDomainId的Master和Slave的CanTSynGlobalTimeSyncDataIDList、CanTSynGlobalTimeFupDataIDListElement配置项必须相同，否则校验不过。

2.If CRC checksum is enabled, CanTSynGlobalTimeSyncDataIDList and CanTSynGlobalTimeFupDataIDListElement configuration items must be identical for the Master and Slave within the same CanTSynGlobalTimeDomainId; otherwise, the check will fail.

.. figure:: ../../../_static/参考手册/CanTSyn/CanTSyn_1.png
   :alt: CanTSyn_1
   :align: center

配置主函数周期。 

Configure the main function period.

Master配置

Master Configuration

BSW部分

BSW Part

导入萃取文件前

Before Importing the Extraction File

注意：萃取文件更新步骤参考下文SWC部分

Note: For the steps to update the extraction file, refer to the SWC part below.

.. figure:: ../../../_static/参考手册/CanTSyn/CanTSyn_2.png
   :alt: CanTSyn_2
   :align: center

右键新增一个时间域。 

Right-click to add a new time domain.

.. figure:: ../../../_static/参考手册/CanTSyn/CanTSyn_3.png
   :alt: CanTSyn_3
   :align: center

1.配置CanTSynGlobalTimeDomainId时间域的ID。（主从时间域ID必须一致才可进行同步，用于划分不同的同步局域网）

1.Configure the time domain ID CanTSynGlobalTimeDomainId. (The Master and Slave time domain IDs must be identical for synchronization. This is used to create separate synchronization networks.)

2.关联时间基。

2.Associate the time base.

3.关联CAN控制器。

3.Associate the CAN controller.

.. figure:: ../../../_static/参考手册/CanTSyn/CanTSyn_3.png
   :alt: CanTSyn_3
   :align: center

1.设置CanTSynCyclicMsgResumeTime时间，指从立即发送恢复到循环发送所需要的时间。

1.Set CanTSynCyclicMsgResumeTime, which specifies the time required to transition from immediate transmission back to cyclic transmission.

2.设置CanTSynGlobalTimeDebounceTime，指SYNC报文和FU报文之间的时间间隔。

2.Set CanTSynGlobalTimeDebounceTime, which specifies the time interval between the SYNC and FUP messages.

3.CanTSynGlobalTimeTxCrcSecured可选择支持或不支持CRC校验。（CRC校验会校验报文中的sequenceID，DomainID等信息）此处选择不支持。注意：若选择支持，则需要配置CanTSynGlobalTimeFupDataIDList和CanTSynGlobalTimeSyncDataIDList。

3.Set CanTSynGlobalTimeTxCrcSecured to either enable or disable CRC checksum. (CRC checksum checks information in the message such as the sequence ID and Domain ID). Here, it is set to disabled. Note: If enabled, CanTSynGlobalTimeFupDataIDList and CanTSynGlobalTimeSyncDataIDList must be configured.

4.设置同步报文的发送周期CanTSynGlobalTimeTxPeriod。

4.Set the transmission period for synchronization messages CanTSynGlobalTimeTxPeriod.

导入萃取文件后

After Importing the Extraction File

完成更新萃取文件后，按照以下步骤生成RTE

After updating the extraction file, follow the steps below to generate the RTE.

.. figure:: ../../../_static/参考手册/CanTSyn/CanTSyn_4.png
   :alt: CanTSyn_4
   :align: center

首先打开ECUC模块，在上图位置添加之前在SWC新增的应用组件。 

First, open the ECUC module and add the application component previously created in the SWC, as shown in the figure above.

.. figure:: ../../../_static/参考手册/CanTSyn/CanTSyn_5.png
   :alt: CanTSyn_5
   :align: center

右键ECUC模块，同步一下模块。

Right-click the ECUC module and synchronize the module.

.. figure:: ../../../_static/参考手册/CanTSyn/CanTSyn_6.png
   :alt: CanTSyn_6
   :align: center

点金同步RTE/OS。 

Click to synchronize RTE/OS.

.. figure:: ../../../_static/参考手册/CanTSyn/CanTSyn_7.png
   :alt: CanTSyn_7
   :align: center

.. figure:: ../../../_static/参考手册/CanTSyn/CanTSyn_8.png
   :alt: CanTSyn_8
   :align: center

生成RTE文件和APP文件。

Generate the RTE and APP files.

SWC部分

SWC Part

作为主时钟，需要将自己的本地时间基信息发送到总线上，在这之前需要设置主时钟关联的时间基。因此需要走SWC，通过StbM的服务组件设置时间基。

As a master clock, it needs to send its local time base information to the bus. Before doing so, the time base associated with the master clock must be set. Therefore, this is done through SWC by setting the time base via the StbM service component.

.. figure:: ../../../_static/参考手册/CanTSyn/CanTSyn_9.png
   :alt: CanTSyn_9
   :align: center

如上图所示，在Application Component处右键新增一个应用组件。

As shown in the figure above, right-click on Application Component to add a new application component.

.. figure:: ../../../_static/参考手册/CanTSyn/CanTSyn_10.png
   :alt: CanTSyn_10
   :align: center

对该APP组件进行命名。 

Name this APP component.

.. figure:: ../../../_static/参考手册/CanTSyn/CanTSyn_11.png
   :alt: CanTSyn_11
   :align: center

右键新增一个客户端Port。

Right-click to add a new client Port.

.. figure:: ../../../_static/参考手册/CanTSyn/CanTSyn_12.png
   :alt: CanTSyn_12
   :align: center

选中CanTSyn关联的时间基。 

Select the time base associated with CanTSyn.

.. figure:: ../../../_static/参考手册/CanTSyn/CanTSyn_13.png
   :alt: CanTSyn_13
   :align: center

点击上图所示Runnable Entity List。

Click Runnable Entity List, as shown in the figure above.

.. figure:: ../../../_static/参考手册/CanTSyn/CanTSyn_14.png
   :alt: CanTSyn_14
   :align: center

New一个Init Runnable。

Create a new Init Runnable.

.. figure:: ../../../_static/参考手册/CanTSyn/CanTSyn_15.png
   :alt: CanTSyn_15
   :align: center

.. figure:: ../../../_static/参考手册/CanTSyn/CanTSyn_16.png
   :alt: CanTSyn_16
   :align: center

选择Access Points中的SetGlobalTime。 

Select SetGlobalTime from the Access Points.

.. figure:: ../../../_static/参考手册/CanTSyn/CanTSyn_17.png
   :alt: CanTSyn_17
   :align: center

.. figure:: ../../../_static/参考手册/CanTSyn/CanTSyn_18.png
   :alt: CanTSyn_18
   :align: center

如上图所示开启图形界面。 

Open the graphical interface, as shown in the figure above.

.. figure:: ../../../_static/参考手册/CanTSyn/CanTSyn_19.png
   :alt: CanTSyn_19
   :align: center

双击ECU_ComPosition。 

Double-click ECU_Composition.

.. figure:: ../../../_static/参考手册/CanTSyn/CanTSyn_20.png
   :alt: CanTSyn_20
   :align: center

实例化TSyn_App。 

Instantiate TSyn_App.

.. figure:: ../../../_static/参考手册/CanTSyn/CanTSyn_21.png
   :alt: CanTSyn_21
   :align: center

再次右键ECU_ComPosition打开图形化界面。 

Right-click ECU_Composition again to open the graphical interface.

.. figure:: ../../../_static/参考手册/CanTSyn/CanTSyn_22.png
   :alt: CanTSyn_22
   :align: center

在空白处右键选择连接模式。 

Right-click in the empty area and select the connection mode.

.. figure:: ../../../_static/参考手册/CanTSyn/CanTSyn_23.png
   :alt: CanTSyn_23
   :align: center

将StbM组件和TSynApp组件连接。 

Connect the StbM component and the TSynApp component.

.. figure:: ../../../_static/参考手册/CanTSyn/CanTSyn_24.png
   :alt: CanTSyn_24
   :align: center

双击SysTem进入映射界面。 

Double-click System to enter the mapping interface.

.. figure:: ../../../_static/参考手册/CanTSyn/CanTSyn_25.png
   :alt: CanTSyn_25
   :align: center

将ECU_Composition左键拖入ECU下，完成映射。 

Drag ECU_Composition with the left mouse button under the ECU to complete the mapping.

.. figure:: ../../../_static/参考手册/CanTSyn/CanTSyn_26.png
   :alt: CanTSyn_26
   :align: center

点击上方箭头处进行校验。在下方箭头处查看是否有报错。若无报错，则可按照下图进行萃取。 

Click the arrow at the top to perform verification. Check the area indicated by the arrow below for any errors. If there are no errors, proceed with extraction as shown in the figure below.

.. figure:: ../../../_static/参考手册/CanTSyn/CanTSyn_27.png
   :alt: CanTSyn_27
   :align: center

如上图所示，在ECU处右键创建萃取文件。 

As shown in the figure above, right-click the ECU to create the extraction file.

.. figure:: ../../../_static/参考手册/CanTSyn/CanTSyn_28.png
   :alt: CanTSyn_28
   :align: center

替换到原有工程下的萃取文件。 

Replace the existing extraction file in the project directory.

Slave配置

Slave Configuration

.. figure:: ../../../_static/参考手册/CanTSyn/CanTSyn_29.png
   :alt: CanTSyn_29
   :align: center

CanTSynGlobalTimeDomain配置与Master一致。区别在于需要设置的是CanTSynGlobalTimeSlave。

The CanTSynGlobalTimeDomain configuration is the same as that of the Master. The difference is that CanTSynGlobalTimeSlave needs to be configured.

.. figure:: ../../../_static/参考手册/CanTSyn/CanTSyn_30.png
   :alt: CanTSyn_30
   :align: center

1.设置FU报文的接收超时。指在这个时间内必须收到FU报文，否则丢弃。

1.Set the reception timeout for FUP messages. This means that the FUP message must be received within this time; otherwise, it is discarded.

2.设置CanTSynGlobalTimeSequenceCounterJumpWidth，指报文中的序列号SequenceCounter允许跳变的最大值，即可接受的最大丢帧数。

2.Set CanTSynGlobalTimeSequenceCounterJumpWidth, which specifies the maximum allowed jump for SequenceCounter in the message, i.e., the maximum number of acceptable lost frames.

3.由于不设置CRC校验，因此CanTSynRxCrcValidated需要设置为CRC_IGNORED。

3.Since CRC checksum is not being used, CanTSynRxCrcValidated must be set to CRC_IGNORED.
