====================
StbM
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

   * - 2025/2/24
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
-------------------------------------------------------------------------------------------

.. 如果没有就不存在该章节，或为None

.. list-table::
   :widths: 10 10 30 10
   :header-rows: 1

   * - 编号(Number)
     - 分类(Classification)
     - 标题(Title)
     - 版本(Version)
   * - 1
     - Autosar
     - AUTOSAR_FO_RS_TimeSync.pdf
     - R23-11
   * - 2
     - Autosar
     - AUTOSAR_FO_PRS_TimeSyncProtocol.pdf
     - R23-11
   * - 3
     - Autosar
     - AUTOSAR_CP_SWS_SynchronizedTimeBaseManager.pdf
     - R23-11

术语与简写 Terms and Abbreviations
====================================================================


术语 Terms
------------------------------------------------------------------------------

.. :align: center   表格内容居中(Table contents are centered)

.. list-table::
   :widths: 10 40
   :header-rows: 1

   * - 术语(Terms)
     - 解释(Explanation)

   * - Current Time Tuple
     - 当前时间元组，包含全局时间的本地实例和本地虚拟时间(Current time tuple, including the local instance of global time and local virtual time)

   * - Disciplined HW Clock
     - 一种可以调整其速率和偏移量的硬件时钟(A hardware clock whose rate and offset can be adjusted)

   * - Global Time
     - 由全局时间主机提供的时间(Time provided by the global time master)

   * - Local Instance of the Global Time
     - 基于本地虚拟时间结合从全局时间主机接收到的时间元组推导出的本地时间(Local time derived based on local virtual time combined with the time tuple received from the global time master)

   * - Main Time Tuple
     - 用来计算推导全局时间本地实例的时间对(A pair of times used to calculate and derive the local instance of global time)

   * - Notification Time Base Customer
     - 当发生如下事件时，时间基客户端将会被同步时间管理器通知：(The time base customer will be notified by the synchronized time manager when the following events occur:)
       时间基状态发生了变化（例如，时间基发生了超时）(The time base status changes (for example, the time base times out))
       时间基准值已经达到了用户预先设定的一个值(The time base value has reached a value preset by the user)

   * - Offset Correction
     - 补偿时间偏移所需的偏移值(The offset value required to compensate for time offset)

   * - Offset Correction by Jump
     - 在时间同步时应用的一个偏移值，这是值将补偿本地全局时间与从时间主站接收到的全局时间值之间的时差(An offset value applied during time synchronization, which will compensate for the time difference between the local global time and the global time value received from the time master)

   * - Offset Correction by Rate Adaption
     - 除了速率校准之外还会应用速率偏差校准，这样可以让本地时间平滑的向全局时间过渡(In addition to rate correction, rate deviation correction will also be applied, which can make the local time smoothly transition to the global time)

   * - Rate Correction
     - 速率校准(Rate correction)

   * - Rate Deviation
     - 表示目标时钟频率和参考时钟频率之间相差了多少(Indicates the difference between the target clock frequency and the reference clock frequency)

   * - Time Base Customer
     - 同步时间管理器支持下述3种时基客户(The synchronized time manager supports the following three types of time base customers)
       活跃客户(Active customers)、
       触发客户(Trigger customers)、
       通知客户(Notification customers)

简写 Abbreviations
-------------------------------------------------------------------------------

.. 缩写词英文全称中文解释

.. list-table::
   :widths: 10 20 30
   :header-rows: 1


   * - 简写(Abbreviation)
     - 全称(Full name)
     - 解释(Explanation)

   * - DET
     - Default Error Tracer
     - 默认错误检测模块

   * - ECU
     - Electronic Control Unit
     - 电子控制器单元

   * - PDU
     - Protocol Data Unit
     - 协议数据单元

   * - StbM
     - Synchronized Time-Base Manager
     - 同步时基管理

   * - <Bus>TSyn
     - A bus specific Time Synchronization Provider module
     - 基于特定总线的时间同步模块

   * - CanTSyn
     - Time Synchronization Provider module for CAN
     - 基于CAN总线的时间同步提供者

   * - EthTSyn
     - Time Synchronization Provider module for Ethernet
     - 基于以太网总线的时间同步提供者

   * - TG
     - Time Gateway
     - 时间网关

   * - TS
     - Time Slave
     - 时间从机

   * - TM
     - Time Master
     - 时间主机

   * - TD
     - Time Domain
     - 时间域

   * - TL
     - Local Instance of the Global Time
     - 全局时间的本地实例

   * - TV
     - Virtual Local Time
     - 虚拟本地时间

   * - Rrc
     - Rate (correction) as derived by rate measurement
     - 速率校正值

   * - Roc
     - Rate offset as derived by Offset Correction by Rate Adaption
     - 通过速率自适应的偏移校正得出的速率偏移值


简介 Introduction
==================================

StbM（Synchronization TimeBase Manager，时间同步管理器），负责在分布式车载系统中实现时间同步，确保相关模块在同一时间基准下运行。时间同步支持多种同步协议，这部分主要在<bus>TSyn模块中实现，StbM对这些模块进行统一的抽象和管理，对上提供服务。StbM在AutoSAR中软件层级架构如下图。

StbM (Synchronization TimeBase Manager) is responsible for implementing time synchronization in distributed in-vehicle systems to ensure that related modules run under the same time base. Time synchronization supports multiple synchronization protocols, which are mainly implemented in the <bus>TSyn module. StbM provides unified abstraction and management for these modules and offers services to the upper layer. The software layer architecture of StbM in AutoSAR is as follows.

.. figure:: ../../../_static/参考手册/StbM/StbM_IN_AUTOSAR.png
   :alt: StbM在AUTOSAR中的位置 (Position of StbM in AUTOSAR)
   :align: center

   StbM在AUTOSAR中的位置 (Position of StbM in AUTOSAR)

本文主要描述StbM，给CanTSyn, EthTSyn提供接口用来更新同步时间，以及给其他用户提供接口用来获取/通知同步时间。

This document mainly describes StbM, which provides interfaces for CanTSyn and EthTSyn to update synchronization time, and provides interfaces for other users to obtain/notify synchronization time.


功能描述 Functional Description
==========================================================
.. 本章节仅描述模块支持的功能大致情况，不宜做细致描述；更加细致的描述在配置章节，结合配置，从集成角度描述

StbM 的主要功能包括两个方面， 一是使上层应用间的时间可以同步， 二是提供绝对时间值。

The main functions of StbM include two aspects: one is to enable time synchronization between upper-layer applications, and the other is to provide absolute time values.

特性 Features
---------------------------------------------------

.. only:: doc_pbs

  变体 Variant
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    .. 支持PBS的模块，必须具有本章节，以功能为导向描述模块级别的变体支持情况
    .. 主要功能必须描述，比较偏尽量描述（不强制）

  支持将同一个同步时间基配置为全局时间基或者非全局时间基（StbMIsSystemWideGlobalTimeMaster属性）。

  Support configuring the same synchronized time base as a global time base or a non-global time base (StbMIsSystemWideGlobalTimeMaster attribute).


全局时间基 Global Time Base
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
由于不同的硬件时钟，速率可能会有偏差，这将会导致使用不同硬件时钟的应用，各自的时间会有偏差，为了消除这种偏差，StbM会将一个主节点的时间基作为全局的时间基，并将所有其他节点的时间同步到这一节点，以达成时间同步的目的。

Due to the possible rate deviation of different hardware clocks, applications using different hardware clocks will have time deviations. To eliminate this deviation, StbM will take the time base of a master node as the global time base,and synchronize the time of all other nodes to this node to achieve time synchronization.

状态变化通知功能 Status Change Notification Function
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
StbM允许客户注册回调函数，StbM将跟踪用户通过掩码配置的状态位，当这些状态位有变化时StbM将通过回调函数通知用户。

StbM allows customers to register callback functions. StbM will track the status bits configured by the user through a mask, and notify the user through the callback function when these status bits change.

定时功能 Timing Function
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
StbM实现了定时器功能，允许用户设置定时任务，当时间到达用户设定的时间值时，StbM将通过回调函数触发用户设定的任务。

StbM implements a timer function, allowing users to set timing tasks. When the time reaches the time value set by the user, StbM will trigger the task set by the user through a callback function.

时间记录功能 Time Recording Function
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
时间记录功能将记录StbM发生同步事件的时间点的数据快照，供用户获取用于验证本地时间精度等目的。

The time recording function will record data snapshots of the time points when synchronization events occur in StbM, for users to obtain for purposes such as verifying local time accuracy.

时间偏差校准 Time Deviation Correction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
如果开启了时间偏差校准功能，StbM将通过速率校准和偏移校准来减小本地时间和全局时间之间的偏差。StbM管理一个主时间组，这个主时基组用来作为其他从节点时间同步的基准，主时间组由TG和TV组成，TG是全局时间，TV是虚拟本地时间，TG的来源为总线同步模块设置的时间和当前的TV通过时间校正计算而得出的时间，TV的来源是本地的硬件时钟，包括GPT,OS和EthTSyn三种。

If the time deviation correction function is enabled, StbM will reduce the deviation between local time and global time through rate correction and offset correction. StbM manages a main time group, which is used as the reference for time synchronization of other slave nodes.The main time group consists of TG and TV. TG is the global time, and TV is the virtual local time. The source of TG is the time set by the bus synchronization module and the time derived from the current TV through time correction calculation. The source of TV is the local hardware clock, including GPT, OS, and EthTSyn.

时间校正计算包括偏移校正和速率校正，偏移校正包括跳跃校正和速率适应。速率校正，在单位时间不停计算时间差，以得出不同时钟间的速率偏差，而偏移校正是根据本地的时间，速率的偏差以及接受到的时间计算得出的时间来覆盖主时间组。表示成公式为TL = TGSync + (TV - TVSync) * r。其中的跳跃校正为当StbM接收到时间值时，主时间组的值直接更新为接收到的时间。

Time correction calculation includes offset correction and rate correction. Offset correction includes jump correction and rate adaptation. Rate correction continuously calculates the time difference per unit time to derive the rate deviation between different clocks, while offset correction overwrites the main time group based on the local time,rate deviation, and the time calculated from the received time. It is expressed as a formula: TL = TGSync + (TV - TVSync) * r. The jump correction is that when StbM receives a time value, the value of the main time group is directly updated to the received time.

速率适应的偏移校正，则是在一段时间内逐渐校正调整偏移值。

Offset correction with rate adaptation gradually corrects and adjusts the offset value over a period of time.


偏差 Deviation
------------------------------------------------------------------

1.不再支持偏移时间基

1.Offset time base is no longer supported

2.不支持备用时钟功能

2.Standby clock function is not supported

3.不支持时间验证功能

3.Time verification function is not supported

4.不支持时间新鲜度功能

4.Time freshness function is not supported

5.不支持Disciplined HW Clock

5.Disciplined HW Clock is not supported

6.不支持同步时间的NVM存储机制

6.NVM storage mechanism for synchronized time is not supported

7.不支持时间基的克隆

7.Time base cloning is not supported


扩展 Extension
------------------------------------------------------------------

None


集成 Integration
========================================

文件列表 File List
------------------------------------------------------------------

静态文件 Static Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - 文件(File)
     - 描述(Description)

   * - StbM.h
     - StbM模块头文件，包含了API函数的声明(Header file of the StbM module, including declarations of API functions)

   * - StbM_Internal.h
     - StbM模块头文件，包含了内部数据类型定义(Header file of the StbM module, including definitions of internal data types)

   * - StbM_Types.h
     - StbM模块头文件，包含了外部数据类型定义(Header file of the StbM module, including definitions of external data types)

   * - StbM.c
     - StbM模块源文件，包含了API函数的实现(Source file of the StbM module, including implementations of API functions)

动态文件 Dynamic Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - 文件(File)
     - 描述(Description)

   * - StbM_MemMap.h
     - StbM模块的内存映射(Memory mapping of the StbM module)

   * - StbM_Cfg.h
     - 定义StbM模块预编译时用到的配置参数(Defines configuration parameters used in the pre-compilation of the StbM module)

   * - StbM_Cfg.c
     - StbM Pre-Compile 配置源文件(Pre-Compile configuration source file of StbM)

   * - StbM_PBcfg.c
     - StbM Post-Build 配置源文件(Post-Build configuration source file of StbM)

   * - StbM_Callout.c
     - 用户自定义的回调函数实现(Implementation of user-defined callback functions)

   * - StbM_External.h
     - 用户自定义回调函数声明(Declarations of user-defined callback functions)


错误处理 Error Handling
----------------------------------------------------------------------------------------

开发错误 Development Errors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 20 10 30
   :header-rows: 1

   * - Error code
     - Value[hex]
     - Description

   * - STBM_E_PARAM
     - 0x0A
     - API called with invalid parameters.

   * - STBM_E_UNINIT
     - 0x0B
     - API called while StbM is not initialized.

   * - STBM_E_PARAM_POINTER
     - 0x10
     - API called with invalid pointer in parameter list.

   * - STBM_E_INIT_FAILED
     - 0x11
     - STbM_Init initialization failed.

   * - STBM_E_SERVICE_NOT_SUPPORTED
     - 0x12
     - API not supported with current configuration.

   * - STBM_E_PARAM_TIMESTAMP
     - 0x25
     - API called with invalid timestamp.

   * - STBM_E_PARAM_USERDATA
     - 0x26
     - API called with invalid user data.

   * - STBM_E_INVALID_PARTITION
     - 0xF0
     - API called in invalid partition.

   * - STBM_E_ALREADY_INITIALIZED
     - 0xF1
     - StbM_Init has already been initialized.


产品错误 Product Errors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

None

运行时错误 Runtime Errors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

None

接口描述 Interface Description
==============================================================

.. 目前能够自动生成的有类型定义，普通函数，回调函数。
.. 有些模块的API来自多个头文件，需要自行裁剪合并
.. 引用接口描述。来自于code->doxygen->xml->rst
.. 引用接口描述。 From code->doxygen->xml->rst

.. include:: StbM_h_api.rst
.. include:: StbM_Internal_h_api.rst
.. include:: StbM_Types_h_api.rst


配置函数 Configuration function
----------------------------------------------------------------------------------------

.. 可选的章节，根据模块实际情况确定
.. 格式同提供的服务

StbM_MainFunction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void StbM_MainFunction(void)

This function needs to be called periodically to perform the AUTOSAR StbM activities.

**Sync/Async**
   Asynchronous

**Reentrancy**
   Reentrant (Reentrant for different partitions. Non reentrant for the same partition.)


**Return type**
   void


StatusNotificationCallback<TimeBase>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType StatusNotificationCallback<TimeBase>(StbM_TimeBaseNotificationType eventNotification)

The callback notifies the customers, when a <TimeBase> related event occurs, which is enabled by the notification mask

**Sync/Async**
   Synchronous

**Reentrancy**
   Non Reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - eventNotification
     - Holds the notification bits for the different Time Base related events

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - successfull
   * - E_NOT_OK
     - failed


<Customer>_TimeNotificationCallback<TimeBase>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType <Customer>_TimeNotificationCallback<TimeBase>(StbM_TimeDiffType deviationTime)

This callback notifies the <Customer>, when a Time Base reaches the time value set by StbM_StartTimer for the <TimeBase>

**Sync/Async**
   Synchronous

**Reentrancy**
   Non Reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - deviationTime
     - Difference time value when callback is called by StbM

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - successfull
   * - E_NOT_OK
     - failed


SyncTimeRecordBlockCallback<TimeBase>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType SyncTimeRecordBlockCallback<TimeBase>(const StbM_SyncRecordTableBlockType* syncRecordTableBlock)

Provides a recorded snapshot data block of the measurement data table belonging to the Synchronized Time Base

**Sync/Async**
   Synchronous

**Reentrancy**
   Non Reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - syncRecordTableBlock
     - Block of the table

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Table access done
   * - E_NOT_OK
     - Table contains no data or access invalid


SWC服务组件封装 SWC Service Component Encapsulation
----------------------------------------------------------------------------

以下类型和接口可以封装至SWC生成完整的服务组件，可以与应用通过端口连接，没有列出的部分StbM底层暂时不支持。

The following types and interfaces can be encapsulated into SWC to generate a complete service component, which can be connected to applications through ports. The unlisted parts are temporarily not supported by the StbM bottom layer.


CS接口封装 CS Interface Encapsulation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

注：下面提到的<UserModule>和<UserPort>分别为用户SWC的名字和对应端口名，在与StbM服务组件端口连接后适用。

Note: <UserModule> and <UserPort> mentioned below are the name of the user SWC and the corresponding port name, which are applicable after connecting to the StbM service component port.

Rte_Call_<UserModule>_<UserPort>_GetMasterConfig

.. list-table::
   :widths: 10 40
   :header-rows: 1

   * - 函数名称：(Function Name:)
     - Rte_Call_<UserModule>_<UserPortName>_GetMasterConfig

   * - 运行实体函数定义：(Runtime Entity Function Definition:)
     - 详见接口描述章节的StbM_GetMasterConfig(See StbM_GetMasterConfig in the interface description chapter)

   * - 变体：(Variant:)
     - Name=StbMSynchronizedTimeBase.SHORT-NAME

   * - 生成条件：(Generation Condition:)
     - 1. StbMSynchronizedTimeBase/StbMIsSystemWideGlobalTimeMaster == TRUE
       And
       2. StbMSynchronizedTimeBaseIdentifier < 128

   * - 端口类型：(Port Type:)
     - Provided Port

   * - 从属端口：(Dependent Port:)
     - GlobalTime_Master_{Name}


Rte_Call_<UserModule>_<UserPort>_SetGlobalTime

.. list-table::
   :widths: 10 40
   :header-rows: 1

   * - 函数名称：(Function Name:)
     - Rte_Call_<UserModule>_<UserPortName>_SetGlobalTime

   * - 运行实体函数定义：(Runtime Entity Function Definition:)
     - 详见接口描述章节的StbM_SetGlobalTime(See StbM_SetGlobalTime in the interface description chapter)

   * - 变体：(Variant:)
     - Name=StbMSynchronizedTimeBase.SHORT-NAME

   * - 生成条件：(Generation Condition:)
     - 1. StbMSynchronizedTimeBase/StbMIsSystemWideGlobalTimeMaster == TRUE
       And
       2. StbMSynchronizedTimeBaseIdentifier < 128

   * - 端口类型：(Port Type:)
     - Provided Port

   * - 从属端口：(Dependent Port:)
     - GlobalTime_Master_{Name}

Rte_Call_<UserModule>_<UserPort>_SetRateCorrection

.. list-table::
   :widths: 10 40
   :header-rows: 1

   * - 函数名称：(Function Name:)
     - Rte_Call_<UserModule>_<UserPortName>_SetRateCorrection

   * - 运行实体函数定义：(Runtime Entity Function Definition:)
     - 详见接口描述章节的StbM_SetRateCorrection(See StbM_SetRateCorrection in the interface description chapter)

   * - 变体：(Variant:)
     - Name=StbMSynchronizedTimeBase.SHORT-NAME

   * - 生成条件：(Generation Condition:)
     - 1. StbMSynchronizedTimeBase/StbMIsSystemWideGlobalTimeMaster == TRUE
       And
       2. StbMSynchronizedTimeBaseIdentifier < 128

   * - 端口类型：(Port Type:)
     - Provided Port

   * - 从属端口：(Dependent Port:)
     - GlobalTime_Master_{Name}

Rte_Call_<UserModule>_<UserPort>_SetUserData

.. list-table::
   :widths: 10 40
   :header-rows: 1

   * - 函数名称：(Function Name:)
     - Rte_Call_<UserModule>_<UserPortName>_SetUserData

   * - 运行实体函数定义：(Runtime Entity Function Definition:)
     - 详见接口描述章节的StbM_SetUserData(See StbM_SetUserData in the interface description chapter)

   * - 变体：(Variant:)
     - Name=StbMSynchronizedTimeBase.SHORT-NAME

   * - 生成条件：(Generation Condition:)
     - 1. StbMSynchronizedTimeBase/StbMIsSystemWideGlobalTimeMaster == TRUE
       And
       2. StbMSynchronizedTimeBaseIdentifier < 128

   * - 端口类型：(Port Type:)
     - Provided Port

   * - 从属端口：(Dependent Port:)
     - GlobalTime_Master_{Name}

Rte_Call_<UserModule>_<UserPort>_TriggerTimeTransmission

.. list-table::
   :widths: 10 40
   :header-rows: 1

   * - 函数名称：(Function Name:)
     - Rte_Call_<UserModule>_<UserPortName>_TriggerTimeTransmission

   * - 运行实体函数定义：(Runtime Entity Function Definition:)
     - 详见接口描述章节的StbM_TriggerTimeTransmission(See StbM_TriggerTimeTransmission in the interface description chapter)

   * - 变体：(Variant:)
     - Name=StbMSynchronizedTimeBase.SHORT-NAME

   * - 生成条件：(Generation Condition:)
     - 1. StbMSynchronizedTimeBase/StbMIsSystemWideGlobalTimeMaster == TRUE
       And
       2. StbMSynchronizedTimeBaseIdentifier < 128

   * - 端口类型：(Port Type:)
     - Provided Port

   * - 从属端口：(Dependent Port:)
     - GlobalTime_Master_{Name}

Rte_Call_<UserModule>_<UserPort>_UpdateGlobalTime

.. list-table::
   :widths: 10 40
   :header-rows: 1

   * - 函数名称：(Function Name:)
     - Rte_Call_<UserModule>_<UserPortName>_UpdateGlobalTime

   * - 运行实体函数定义：(Runtime Entity Function Definition:)
     - 详见接口描述章节的StbM_UpdateGlobalTime(See StbM_UpdateGlobalTime in the interface description chapter)

   * - 变体：(Variant:)
     - Name=StbMSynchronizedTimeBase.SHORT-NAME

   * - 生成条件：(Generation Condition:)
     - 1. StbMSynchronizedTimeBase/StbMIsSystemWideGlobalTimeMaster == TRUE
       And
       2. StbMSynchronizedTimeBaseIdentifier < 128

   * - 端口类型：(Port Type:)
     - Provided Port

   * - 从属端口：(Dependent Port:)
     - GlobalTime_Master_{Name}


Rte_Call_<UserModule>_<UserPort>_GetCurrentTime

.. list-table::
   :widths: 10 40
   :header-rows: 1

   * - 函数名称：(Function Name:)
     - Rte_Call_<UserModule>_<UserPortName>_GetCurrentTime

   * - 运行实体函数定义：(Runtime Entity Function Definition:)
     - 详见接口描述章节的StbM_GetCurrentTime(See StbM_GetCurrentTime in the interface description chapter)

   * - 变体：(Variant:)
     - Name=StbMSynchronizedTimeBase.SHORT-NAME

   * - 生成条件：(Generation Condition:)
     - StbMSynchronizedTimeBaseIdentifier < 128

   * - 端口类型：(Port Type:)
     - Provided Port

   * - 从属端口：(Dependent Port:)
     - GlobalTime_Slave_{Name}


Rte_Call_<UserModule>_<UserPort>_GetRateDeviation

.. list-table::
   :widths: 10 40
   :header-rows: 1

   * - 函数名称：(Function Name:)
     - Rte_Call_<UserModule>_<UserPortName>_GetRateDeviation

   * - 运行实体函数定义：(Runtime Entity Function Definition:)
     - 详见接口描述章节的StbM_GetRateDeviation(See StbM_GetRateDeviation in the interface description chapter)

   * - 变体：(Variant:)
     - Name=StbMSynchronizedTimeBase.SHORT-NAME

   * - 生成条件：(Generation Condition:)
     - StbMSynchronizedTimeBaseIdentifier < 128

   * - 端口类型：(Port Type:)
     - Provided Port

   * - 从属端口：(Dependent Port:)
     - GlobalTime_Slave_{Name}


Rte_Call_<UserModule>_<UserPort>_GetSyncTimeRecordHead

.. list-table::
   :widths: 10 40
   :header-rows: 1

   * - 函数名称：(Function Name:)
     - Rte_Call_<UserModule>_<UserPortName>_GetSyncTimeRecordHead

   * - 运行实体函数定义：(Runtime Entity Function Definition:)
     - 详见接口描述章节的StbM_GetSyncTimeRecordHead(See StbM_GetSyncTimeRecordHead in the interface description chapter)

   * - 变体：(Variant:)
     - Name=StbMSynchronizedTimeBase.SHORT-NAME

   * - 生成条件：(Generation Condition:)
     - 1. StbMSynchronizedTimeBaseIdentifier < 128
       And
       2. StbMSynchronizedTimeBase/StbMIsSystemWideGlobalTimeMaster == FALSE
       And
       3. StbMGeneral/StbMTimeRecordingSupport == True

   * - 端口类型：(Port Type:)
     - Provided Port

   * - 从属端口：(Dependent Port:)
     - GlobalTime_Slave_{Name}


Rte_Call_<UserModule>_<UserPort>_GetTimeBaseStatus

.. list-table::
   :widths: 10 40
   :header-rows: 1

   * - 函数名称：(Function Name:)
     - Rte_Call_<UserModule>_<UserPortName>_GetTimeBaseStatus

   * - 运行实体函数定义：(Runtime Entity Function Definition:)
     - 详见接口描述章节的StbM_GetTimeBaseStatus(See StbM_GetTimeBaseStatus in the interface description chapter)

   * - 变体：(Variant:)
     - Name=StbMSynchronizedTimeBase.SHORT-NAME

   * - 生成条件：(Generation Condition:)
     - StbMSynchronizedTimeBaseIdentifier < 128

   * - 端口类型：(Port Type:)
     - Provided Port

   * - 从属端口：(Dependent Port:)
     - GlobalTime_Slave_{Name}

Rte_Call_<UserModule>_<UserPort>_GetTimeLeap

.. list-table::
   :widths: 10 40
   :header-rows: 1

   * - 函数名称：(Function Name:)
     - Rte_Call_<UserModule>_<UserPortName>_GetTimeLeap

   * - 运行实体函数定义：(Runtime Entity Function Definition:)
     - 详见接口描述章节的StbM_GetTimeLeap(See StbM_GetTimeLeap in the interface description chapter)

   * - 变体：(Variant:)
     - Name=StbMSynchronizedTimeBase.SHORT-NAME

   * - 生成条件：(Generation Condition:)
     - StbMSynchronizedTimeBaseIdentifier < 128

   * - 端口类型：(Port Type:)
     - Provided Port

   * - 从属端口：(Dependent Port:)
     - GlobalTime_Slave_{Name}


Rte_Call_<UserModule>_<UserPort>_StartTimer

.. list-table::
   :widths: 10 40
   :header-rows: 1

   * - 函数名称：(Function Name:)
     - Rte_Call_<UserModule>_<UserPortName>_StartTimer

   * - 运行实体函数定义：(Runtime Entity Function Definition:)
     - 详见接口描述章节的StbM_StartTimer(See StbM_StartTimer in the interface description chapter)

   * - 变体：(Variant:)
     - TimeBase = StbMSynchronizedTimeBase.SHORT-NAME
       Customer = StbMSynchronizedTimeBase/StbMNotificationCustomer.SHORT-NAME

   * - 生成条件：(Generation Condition:)
     - StbMSynchronizedTimeBaseIdentifier < 128

   * - 端口类型：(Port Type:)
     - Provided Port

   * - 从属端口：(Dependent Port:)
     - StartTimer_{TimeBase}_{Customer}


依赖的服务 Applicable Services
--------------------------------------------------------------------------------------------------------------

.. - 本章节暂时无法自动化生成，需在第八章最后部分手动copy
.. - 接口有几种类型，根据实际情况选择，没有的章节就不写，格式都一样

强制接口 Compulsory interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. 可选的章节，根据模块实际情况确定

None

可选接口 Optional Interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

   * - GetApplicationID
     - Os.h
     - Get application ID.

   * - EthIf_GetCurrentTimeTuple
     - EthIf.h
     - Returns a time tuple value out of the HW registers according to the capability of the HW.

   * - Gpt_GetTimeElapsed
     - Gpt.h
     - This service gets the number of ticks between the current tick value and a previously read tick value.

   * - GetCounterValue
     - Os.h
     - This service reads the current count value of a counter.

   * - Gpt_StartTimer
     - Gpt.h
     - Starts a timer channel.

   * - SyncScheduleTable
     - Os.h
     - This service provides the schedule table with a synchronization count and start synchronization.


配置接口 Configuration Interfaces
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. 可选的章节，根据模块实际情况确定
.. 格式同强制接口

None


配置 Configuration
====================================

StbMGeneral
------------------------------------------------------

StbMGptTimerRef
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1.该配置项选中的Gpt时钟必须是独占的，不能同时被时间基使用。

1.The Gpt clock selected in this configuration item must be exclusive and cannot be used by the time base at the same time.

2.该配置项选中的Gpt时钟需要在Mcal层将时钟周期配置为1微妙，并且将其定时中断函数配置为StbM_TimerCallback()。

2.The Gpt clock selected in this configuration item needs to configure the clock period to 1 microsecond in the Mcal layer, and configure its timing interrupt function to StbM_TimerCallback().

3.该配置项只能配置一个Gpt定时器，该定时器Mcal如果不支持跨核调用的话，那么创建的定时任务需要和该定时器需要配置在同一个核上。

3.Only one Gpt timer can be configured in this configuration item. If the Mcal of this timer does not support cross-core calls, the created timing task needs to be configured on the same core as the timer.


StbMSynchronizedTimeBase
------------------------------------------------------------------------------------------------------------

StbMStoreTimebaseNonVolatile
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1.当前还不支持此功能，因此该配置使能与否都无影响。

1.This function is not currently supported, so whether this configuration is enabled has no effect.

StbMLocalTimeClock
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1.注意： **StbMLocalTimeHardware** 的配置需要注意该StbM将被哪个<Bus>TSyn模块关联，那么此处配置的硬件时钟需要在Mcal上将其配置为和<Bus>TSyn模块在同一个核上。

1.For the configuration of **StbMLocalTimeHardware** , attention should be paid to which <Bus>TSyn module the StbM will be associated with. Then, the hardware clock configured here needs to be configured on the same core as the <Bus>TSyn module in Mcal.

2.如果该StbM将被多个不同核上的<Bus>TSyn模块关联，那么此处配置的硬件时钟需要在Mcal上将其配置为允许多核访问。

2.If the StbM will be associated with <Bus>TSyn modules on multiple different cores, the hardware clock configured here needs to be configured to allow multi-core access in Mcal.

Rte_StbM_Types.h文件生成 Generation of Rte_StbM_Types.h File
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

请参考《ORIENTAIS Configurator for EasyXMen V25.10 使用指南.pdf》的3.6.3章节服务封装使用步骤内容。

Please refer to the content of the service encapsulation usage steps in Chapter 3.6.3 of "ORIENTAIS Configurator for EasyXMen V25.10 User Manual .pdf".

多分区部署 Multi-Partition Deployment
------------------------------------------------------------------------------------------------------------

1.配置项 **StbMEcucPartitionRef** 确定纯本地时间基运行在哪个分区上，同步时间基运行于哪个分区由其被关联的<Bus>TSyn模块决定，在单分区系统上不需要配置该参数。

1.The configuration item **StbMEcucPartitionRef** determines which partition the pure local time base runs on. The partition where the synchronized time base runs is determined by the <Bus>TSyn module it is associated with. This parameter does not need to be configured in a single-partition system.

以下是相关配置的用例

The following are use cases for related configurations.

配置一个基础的时间基，提供给CanTSyn使用。

Configure a basic time base for CanTSyn to use.

.. figure:: ../../../_static/参考手册/StbM/StbM_1.png
   :alt: StbM_1
   :align: center

如上图所示，需要配置StbM的主函数周期，这里配置为10ms。黄色部分指分区信息，勾选后表示StbM是多分区的，否则为单分区。下拉框选中的分区指默认分区，当StbM配置的任意时间基没有被任何时间同步TSP模块关联后，StbM配置为该分区。

As shown in the figure above, it is necessary to configure the main function period of StbM, which is configured as 10ms here. The yellow part refers to partition information. Checking it means that StbM is multi-partition; otherwise, it is single-partition. The partition selected in the drop-down box refers to the default partition. When any time base configured by StbM is not associated with any time synchronization TSP module, StbM is configured as this partition.

.. figure:: ../../../_static/参考手册/StbM/StbM_2.png
   :alt: StbM_2
   :align: center

在StbMSynchronizedTimeBase处右键新建一个时间基。

Right-click on StbMSynchronizedTimeBase to create a new time base.

.. figure:: ../../../_static/参考手册/StbM/StbM_3.png
   :alt: StbM_3
   :align: center

StbMNotificationInterface配置为NO_NOTIFICATION。时间基标识StbMSynchronizedTimeBaseIdentifier配置为0（用于时间同步的时间基StbMSynchronizedTimeBaseIdentifier范围为0-15，如果是纯本地时间基则为32-127。偏移时间基已经被移除）。

StbMNotificationInterface is configured as NO_NOTIFICATION. The time base identifier StbMSynchronizedTimeBaseIdentifier is configured as 0 (The range of StbMSynchronizedTimeBaseIdentifier for the time base used for time synchronization is 0-15, and 32-127 for the pure local time base. The offset time base has been removed).

.. figure:: ../../../_static/参考手册/StbM/StbM_4.png
   :alt: StbM_4
   :align: center

新增一个StbMLocalTimeClock，关联本地的一个时钟源。除了EthTSynGlobalTimeDomain之外，都需要配置StbMClockFrequency和StbMClockPrescaler进行分频。注意：分频系数需要和所关联的硬件时钟源匹配。此处选择的是GPT，分频系数为1/50000000。

Add a new StbMLocalTimeClock and associate it with a local clock source. Except for EthTSynGlobalTimeDomain, it is necessary to configure StbMClockFrequency and StbMClockPrescaler for frequency division. Note: The frequency division factor needs to match the associated hardware clock source. The selected one here is GPT, and the frequency division factor is 1/50000000.