========================
EthTSyn
========================
.. 标题标识符“===”的长度必须要大于其内容的长度，否则会报错，其他标题亦是如此
.. The length of the title identifier "===" must be greater than the length of its content; otherwise, an error will occur. The same applies to other titles.


文档信息 Document Information
==================================================================

版本历史 Version History
------------------------------------------------------------------------------------------------------------------

.. list-table::
   :widths: 10 10 10 10 20
   :header-rows: 1

   * - 日期(Date)
     - 作者(Author)
     - 版本(Version)
     - 状态(Status)
     - 说明(Description)

   * - 2025/2/27
     - shuangyang.fu
     - V0.1
     - 发布(Release)
     - 首次发布(First release)

   * - 2025/04/04
     - shuangyang.fu
     - V1.0
     - 发布(Release)
     - 正式发布(Official release)


参考文档 References
------------------------------------------------------------------------------------------------------------------

.. list-table::
   :widths: 10 10 30 10
   :header-rows: 1

   * - 编号(Number)
     - 分类(Classification)
     - 标题(Title)
     - 版本(Version)

   * - 1
     - Autosar
     - AUTOSAR_SWS_SynchronizedTimeBaseManager.pdf
     - R23-11
   * - 2
     - Autosar
     - AUTOSAR_SWS_SynchronizedTimeBaseManager.pdf
     - R24-11
   * - 3
     - Autosar
     - AUTOSAR_PRS_TimeSyncProtocol.pdf
     - R23-11
   * - 4
     - Autosar
     - AUTOSAR_PRS_TimeSyncProtocol.pdf
     - R24-11
   * - 5
     - Autosar
     - AUTOSAR_SWS_TimeSyncOverEthernet.pdf
     - R23-11
   * - 6
     - Autosar
     - AUTOSAR_SWS_TimeSyncOverEthernet.pdf
     - R24-11
   * - 7
     - IEEE
     - IEEE Std 802.1AS-2011.pdf
     - 2011


术语与简写 Terms and Abbreviations
==================================================================


术语 Terms
------------------------------------------------------------------------------------------------------------------
.. :align: center   表格内容居中(Table contents are centered)


.. list-table::
   :widths: 10 40
   :header-rows: 1

   * - 术语(Terms)
     - 解释(Explanation)

   * - PTP
     - 一种高精度时间同步协议,可以到达亚微秒级精度(A high-precision time synchronization protocol that can achieve sub-microsecond accuracy)

简写 Abbreviations
------------------------------------------------------------------------------------------------------------------

.. list-table::
   :widths: 10 20 30
   :header-rows: 1


   * - 简写(Abbreviation)
     - 全称(Full name)
     - 解释(Explanation)

   * - STBM
     - SynchronizedTimeBaseManager
     - 同步时基管理

   * - <Bus>TSyn
     - A bus specific Time Synchronization Provider module
     - 总线特定的时间同步提供程序模块

   * - Follow_Up
     - Time transport message (Follow-Up)
     - 时间传输消息(后续)

   * - ETH
     - Ethernet
     - 以太网

   * - EthTSyn
     - Time Synchronization Provider module for Ethernet
     - Eth提供的时间同步程序模块

   * - SYNC
     - Time synchronization message
     - 时间同步消息

简介 Introduction
=================================

EthTSyn模块负责确保以太网同步时间信息的采集和分发。它与StbM交互,并为StbM提供所有特定于以太网的功能。EthTSyn主要功能包括测量以太网消息之间的延迟和不同时基之前的时间同步。

The EthTSyn module is responsible for ensuring the collection and distribution of Ethernet synchronized time information. It interacts with StbM and provides all Ethernet-specific functions for StbM. The main functions of EthTSyn include measuring the delay between Ethernet messages and time synchronization before different time bases.

.. figure:: ../../../_static/参考手册/EthTSyn/EthTSyn_layer.png
   :alt: EthTSyn模块层次图(EthTSyn Module Hierarchy Diagram)
   :align: center

如图所示，EthTSyn模块处于AUTOSAR架构中的系统服务层，其依赖Ethif和StbM两个模块。

As shown in the figure, the EthTSyn module is located in the system service layer of the AUTOSAR architecture and depends on two modules, Ethif and StbM.



功能描述 Functional Description
==================================================================
.. 本章节仅描述模块支持的功能大致情况，不宜做细致描述；更加细致的描述在配置章节，结合配置，从集成角度描述

特性 Features
---------------------------------------------------------

.. only:: doc_pbs

  变体 Variant
  ~~~~~~~~~~~~~~~~~~~~~~
  - 支持在同一个时间域下配置不同数量的端口。支持同一个时间域下配置不同端口。
  - Support configuring different numbers of ports under the same time domain. Support configuring different ports under the same time domain.
  - 支持同一个端口配置不同的时间同步角色。
  - Support configuring different time synchronization roles for the same port.
  - 支持同一个端口配置不同的延迟计算参数，支持同一个端口配置或不配置延迟计算。
  - Support configuring different delay calculation parameters for the same port, and support configuring or not configuring delay calculation for the same port.
  - 支持同一个端口配置或不配CRC校验，若配置为支持，则支持同一个端口配置为对不同Sub-Tlv类型的数据进行CRC校验。
  - Support configuring or not configuring CRC check for the same port. If configured to be supported, it supports configuring the same port to perform CRC check on data of different Sub-Tlv types.

周期时间同步 Periodic Time Synchronization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

EthTSyn默认采用的是周期时间同步，作为主时钟（TIME_MASTER）的端口将以可配置的周期循环发送SYNC和FOLLOWUP报文。其中的全局同步时间将在FOLLOWUP报文中携带。从时钟（TIME_SLAVE）收到SYNC报文后，将会记下当前时间。当收到FOLLOWUP报文后，解析出携带的全局同步时间，最后计算出本地需要更新的全局时间进行最终的同步。

EthTSyn adopts periodic time synchronization by default. The port acting as the master clock (TIME_MASTER) will send SYNC and FOLLOWUP messages cyclically at a configurable period. The global synchronization time is carried in the FOLLOWUP message. After receiving the SYNC message, the slave clock (TIME_SLAVE) will record the current time. After receiving the FOLLOWUP message, parse out the carried global synchronization time, and finally calculate the global time that needs to be updated locally for final synchronization.


立即时间同步 Immediate Time Synchronization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

除了周期的时间同步，EthTSyn还支持立即时间同步。通过上层APP调用stbm的立即时间同步接口StbM_TriggerTimeTransmission，EthTSyn模块将立即出发SYNC和Follow-Up报文的发送。

In addition to periodic time synchronization, EthTSyn also supports immediate time synchronization. By calling the immediate time synchronization interface StbM_TriggerTimeTransmission of stbm from the upper-layer APP, the EthTSyn module will immediately trigger the sending of SYNC and Follow-Up messages.



延迟测量 Delay Measurement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

EthTSyn模块支持对网路延迟进行测量，测量发起方将发送Pdelay_Req报文，接收方收到请求报文后，将会恢复Pdelay_Response和Pdelay_Response_Followup报文。请求方通过计算可得到网络延迟。注意：因为AUTOSAR的时间同步符合802.1AS，要求时间同步是p2p的模式，即时间同步和网络延迟是相互独立进行的。

The EthTSyn module supports measuring network delay. The measurement initiator will send a Pdelay_Req message. After receiving the request message, the receiver will restore the Pdelay_Response and Pdelay_Response_Followup messages. The requester can calculate the network delay. Note: Because the time synchronization of AUTOSAR conforms to 802.1AS, the time synchronization is required to be in p2p mode, that is, time synchronization and network delay are performed independently of each other.

偏差 Deviation
---------------------------------------------------------
.. 有序列表示例

1.不支持Time Recording

1.Time Recording is not supported

功能还未开发，将在后续版本中进行开发。

The function has not been developed yet and will be developed in subsequent versions.

2.不支持Security Events 和 Secure Time Synchronization

2.Security Events and Secure Time Synchronization are not supported

功能还未开发，将在后续版本中进行开发。

The function has not been developed yet and will be developed in subsequent versions.

3.不支持Time measurement with Switches

3.Time measurement with Switches is not supported

功能还未开发，将在后续版本中进行开发。

The function has not been developed yet and will be developed in subsequent versions.



扩展 Extension
---------------------------------------------------------
None


集成 Integration
=================================

文件列表 File List
---------------------------------------------------------

静态文件 Static Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - 文件(File)
     - 描述(Description)

   * - EthTSyn.h
     - 实现EthTSyn模块全部外部接口的声明，以及配置文件中全局变量的声明(Implements the declaration of all external interfaces of the EthTSyn module and the declaration of global variables in the configuration file)

   * - EthTSyn_Types.h
     - 实现EthTSyn模块全部数据类型的声明(Implements the declaration of all data types of the EthTSyn module)

   * - EthTSyn.c
     - 作为EthTSyn模块的核心文件，实现EthTSyn模块全部对外接口，以及实现EthTSyn模块功能所必须的local函数，local宏定义，local变量定义(As the core file of the EthTSyn module, it implements all external interfaces of the EthTSyn module, as well as the local functions, local macro definitions, and local variable definitions necessary for implementing the functions of the EthTSyn module)

动态文件 Dynamic Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - 文件(File)
     - 描述(Description)

   * - EthTSyn_Cfg.h
     - 定义Com模块PC配置的宏定义(Defines the macro definitions for PC configuration of the Com module)

   * - EthTSyn_Cfg.c
     - 定义Com模块PC配置的结构体参数(Defines the structure parameters for PC configuration of the Com module)

   * - EthTSyn_PBcfg.c
     - 定义Com模块PB配置的结构体参数(Defines the structure parameters for PB configuration of the Com module)


错误处理 Error Handling
---------------------------------------------------------

开发错误 Development Errors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. list-table::
   :widths: 20 10 30
   :header-rows: 1

   * - Error code
     - Value[hex]
     - Description

   * - ETHTSYN_E_UNINIT
     - 0x20
     - EthTSyn module is not initialized

   * - ETHTSYN_E_INIT_FAILED
     - 0x21
     - EthTSyn module initialization failed

   * - ETHTSYN_E_CTRL_IDX
     - 0x22
     - Invalid controller index

   * - ETHTSYN_E_PARAM_POINTER
     - 0x23
     - Invalid parameter pointer

   * - ETHTSYN_E_PARAM
     - 0x24
     - Invalid parameter

   * - ETHTSYN_E_ALREADY_INITIALIZED
     - 0x25
     - EthTSyn module is already initialized

   * - ETHTSYN_E_INVALID_PARTITION_CONTEXT
     - 0x26
     - Invalid partition context


运行时错误 Runtime Errors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. list-table::
   :widths: 20 10 30
   :header-rows: 1

   * - Error code
     - Value[hex]
     - Description

   * - ETHTSYN_E_TMCONFLICT
     - 0x01
     - Time Master conflict

   * - ETHTSYN_E_TSCONFLICT
     - 0x02
     - Time Slave conflict

接口描述 Interface Description
=================================

.. 目前能够自动生成的有类型定义，普通函数，回调函数。
.. 有些模块的API来自多个头文件，需要自行裁剪合并
.. 引用接口描述。来自于code->doxygen->xml->rst
.. 引用接口描述。 From code->doxygen->xml->rst
.. include:: EthTSyn_Types_h_api.rst
.. include:: EthTSyn_h_api.rst

配置函数 Configuration function
---------------------------------------------------------
EthTSyn_MainFunction_{{EthIfControllor.ShortName}}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

   void Nm_MainFunction_<NmChannel.ShortName>(void)

This function implements the transmission of message,which is running in the EthIfController.

**Sync/Async**
   Synchronous

**Reentrancy**
   Non Reentrant

**Return type**
   void



依赖的服务 Applicable Services
---------------------------------------------------------------------------

强制接口 Compulsory interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. 可选的章节，根据模块实际情况确定

.. list-table::
   :widths: 10 5 30
   :header-rows: 1

   * - API Function
     - Header File
     - Description

   * - Det_ReportRuntimeError
     - Det.h
     - Service to report runtime errors. If a callout has been configured then this callout shall be called.

   * - TcpIp_Bind
     - TcpIp.h
     - By this API service the TCP/IP stack is requested to bind a UDP or TCP socket to a local resource.

可选接口 Optional Interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. list-table::
   :widths: 10 5 30
   :header-rows: 1

   * - API Function
     - Header File
     - Description

   * - Crc_CalculateCRC8H2F
     - Crc.h
     - This service makes a CRC8 calculation with the Polynomial 0x2F on Crc_Length.

   * - Det_ReportError
     - Det.h
     - Service to report development errors.

   * - EthIf_EnableEgressTimeStamp
     - EthIf.h
     - Activates egress time stamping on a dedicated message object. Some HW does store once the egress time stamp marker and some HW needs it
       always before transmission. There will be no "disable" functionality, due to the fact, that the message type is always "time stamped" by
       network design.

   * - EthIf_GetEgressTimeStamp
     - EthIf.h
     - Reads back the egress time stamp on a dedicated message object. It must be called within the TxConfirmation() function.

   * - EthIf_GetIngressTimeStamp
     - EthIf.h
     - Reads back the ingress time stamp on a dedicated message object. It must be called within the RxIndication() function.

   * - EthIf_ProvideTxBuffer
     - EthIf.h
     - Provides access to a transmit buffer of the specified Ethernet controller.

   * - EthIf_Transmit
     - EthIf.h
     - Triggers transmission of a previously filled transmit buffer

   * - StbM_BusSetGlobalTime
     - StbM.h
     - Allows the Time Base Provider Modules to forward the Rx Time Tuple to the StbM.

   * - StbM_GetCurrentTime
     - StbM.h
     - Returns a time tuple (Local time, Global time and Timebase status) and user data details Note: This API shall be called with
       locked interrupts / within an Exclusive Area to prevent interruption (i.e., the risk that the time stamp is outdated on return of the
       function call).

   * - StbM_GetCurrentVirtualLocalTime
     - StbM.h
     - Returns the Virtual Local Time of the referenced Time Base.

   * - StbM_GetTimeBaseStatus
     - StbM.h
     - Returns detailed status information for a Synchronized (or Pure Local) Time Base and, if called for an Offset Time Base, for the Offset Time
       Base and the underlying Synchronized Time Base.

   * - StbM_GetTimeBaseUpdateCounter
     - StbM.h
     - Allows the Timesync Modules to detect, whether a Time Base should be transmitted immediately in the subsequent <Bus>TSyn_MainFunction() cycle.


配置 Configuration
=================================

支持硬件时间戳的时间同步 Time Synchronization Supporting Hardware Timestamp
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

时间同步的实现方式有两种，一种是通过硬件时间戳来实现，另一种是通过软件时间戳来实现。硬件时间戳的实现方式是通过硬件来实现时间戳的采集。

There are two ways to implement time synchronization, one is implemented through hardware timestamp, and the other is implemented through software timestamp. The hardware timestamp implementation method is to collect timestamps through hardware.

硬件时间戳是指获取时间的接口采用以太网硬件的时间戳功能，即通过调用EthIf的接口获取时间戳。对于主时间节点来说，由于时间同步对于精度的要求较高，又因为调用发送接口到报文真正从网口发出去是有时间延迟的，而如果不采用硬件时间戳的方式，是无法拿到较准确的报文出口时间，进而无法计算出准确的preciseOriginalTime，导致slave接收FollowUp报文后同步的精度下降。

Hardware timestamp means that the interface for obtaining time uses the timestamp function of Ethernet hardware, that is, the timestamp is obtained by calling the interface of EthIf. For the master time node, because time synchronization has high requirements for accuracy, and because there is a time delay from calling the sending interface to the message actually being sent from the network port, if the hardware timestamp method is not adopted, it is impossible to obtain a more accurate message exit time, and thus it is impossible to calculate an accurate preciseOriginalTime, resulting in a decrease in the accuracy of synchronization after the slave receives the FollowUp message.

同理，对于slave来说，如果不是用硬件时间戳，无法拿到准确的报文入口时间。

Similarly, for the slave, if hardware timestamp is not used, an accurate message entry time cannot be obtained.

下面是配置支持硬件时间戳的基本步骤：

The following are the basic steps to configure support for hardware timestamp:

.. figure:: ../../../_static/参考手册/EthTSyn/EthTSyn_hardwaretimestamp1.png
   :alt: 通用配置的图片 (Picture of General Configuration)
   :align: center

   通用配置的图片 (Picture of General Configuration)

如上图所示，在EthTSynGeneral中，开启支持硬件时间戳，即勾选EthTSynHardWareTimestampSupport。其他公共配置项，比如周期。

As shown in the figure above, in EthTSynGeneral, enable support for hardware timestamp, that is, check EthTSynHardWareTimestampSupport. Other common configuration items, such as period.

.. figure:: ../../../_static/参考手册/EthTSyn/EthTSyn_hardwaretimestamp2.png
   :alt: domain配置的图片 (Picture of Domain Configuration)
   :align: center

   domain配置的图片 (Picture of Domain Configuration)

.. figure:: ../../../_static/参考手册/EthTSyn/EthTSyn_StbmConfiguration1.png
   :alt: StbM时钟源配置的图片 (Picture of StbM Clock Source Configuration)
   :align: center

   StbM时钟源配置的图片 (Picture of StbM Clock Source Configuration)

在EthTSynGlobalTimeDomain中，配置时间域的相关参数，比如时间域的ID，关联的时间基。

In EthTSynGlobalTimeDomain, configure the relevant parameters of the time domain, such as the ID of the time domain and the associated time base.

.. attention::

  一个时间域可以配置多个Port，EthTSynGlobalTimeHardware是指当前时间域关联的StbM时间基所配的时钟源来自哪个以太网Port。EthTSynGlobalTimeHardware当且仅当该时间域所配的时间基（EthTSynSchronizedTimeBaseRef）下的StbMLocalTimeClock关联的为以太网时钟时，才会生效。

  A time domain can be configured with multiple Ports. EthTSynGlobalTimeHardware refers to which Ethernet Port the clock source configured for the StbM time base associated with the current time domain comes from. EthTSynGlobalTimeHardware takes effect if and only if the time base (EthTSynSchronizedTimeBaseRef) configured in the time domain is associated with the Ethernet clock in StbMLocalTimeClock.

.. figure:: ../../../_static/参考手册/EthTSyn/EthTSyn_hardwaretimestamp3.png
   :alt: port配置的图片 (Picture of Port Configuration)
   :align: center

   port配置的图片 (Picture of Port Configuration)

配置时间域下端口Port，比如时间同步角色EthTSynGlobalTimePortRole，SYNC和Follow-Up报文发送间隔EthTSynGlobalTimeDebounceTime，Port关联的EthIfController。

Configure the Port under the time domain, such as the time synchronization role EthTSynGlobalTimePortRole, the sending interval of SYNC and Follow-Up messages EthTSynGlobalTimeDebounceTime, and the EthIfController associated with the Port.

.. figure:: ../../../_static/参考手册/EthTSyn/EthTSyn_hardwaretimestamp4.png
   :alt: Master的配置的图片 (Picture of Master Configuration)
   :align: center

   Master的配置的图片 (Picture of Master Configuration)

配置时间域下主时间节点的相关参数，比如立即同步恢复到周期同步的恢复时间EthTSynCyclicMsgResumeTime，报文发送周EthTSynGlobalTimeTxPeriod等。

Configure the relevant parameters of the master time node under the time domain, such as the recovery time from immediate synchronization to periodic synchronization EthTSynCyclicMsgResumeTime, the message sending period EthTSynGlobalTimeTxPeriod, etc.

.. figure:: ../../../_static/参考手册/EthTSyn/EthTSyn_EthIf1.png
   :alt: EthIf配置1 (EthIf Configuration 1)
   :align: center

   EthIf配置1 (EthIf Configuration 1)

除了以上配置，为了支持硬件时间戳，还需要将Mcal的硬件时间戳功能打开。同时将硬件时间戳相关的接口注册到EthIf层，如上图所示。并且要将EthTSyn的连接状态回调注册到EthIf层，如下图所示。

In addition to the above configuration, in order to support hardware timestamp, the hardware timestamp function of Mcal also needs to be enabled. At the same time, register the interfaces related to hardware timestamp to the EthIf layer, as shown in the figure above. And register the connection status callback of EthTSyn to the EthIf layer, as shown in the figure below.

.. figure:: ../../../_static/参考手册/EthTSyn/EthTSyn_EthIf2.png
   :alt: EthIf配置2 (EthIf Configuration 2)
   :align: center

   EthIf配置2 (EthIf Configuration 2)


.. attention::


  另外，如果需要激活时间同步Master，需要首先在应用层通过调用StbM设置时间的接口StbM_SetGlobalTime设置本时间域的时间基的全局时间，调用EthTSyn_SetTransmissionMode激活传输状态。

  In addition, if you need to activate the time synchronization Master, you first need to call the interface StbM_SetGlobalTime of StbM in the application layer to set the global time of the time base in this time domain, and call EthTSyn_SetTransmissionMode to activate the transmission state.
