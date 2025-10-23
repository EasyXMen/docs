===================
Com
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
   * - 2024/12/02
     - shengnan.sun
     - V0.1
     - 发布（Release）
     - 首次发布（First release）
   * - 2025/04/04
     - shengnan.sun
     - V1.0
     - 发布（Release）
     - 正式发布（Official release）


参考文档（Reference Document）
----------------------------------

.. list-table::
   :widths: 10 15 20 10
   :header-rows: 1

   * - 编号（Number）
     - 分类（Classification）
     - 标题（Title）
     - 版本（Version）
   * - 1
     - Autosar
     - AUTOSAR_CP_SRS_COM.pdf
     - R23-11
   * - 2
     - Autosar
     - AUTOSAR_CP_SRS_Gateway.pdf
     - R23-11
   * - 3
     - Autosar
     - AUTOSAR_CP_SWS_COM.pdf
     - R23-11
   * - 4
     - Autosar
     - AUTOSAR_SWS_PDURouter.pdf
     - R23-11

术语与简写（Terms and Abbreviations）
========================================


术语（Term）
-----------------
   .. :align: center   表格内容居中


.. list-table::
   :widths: 10 40
   :header-rows: 1

   * - 术语（Term）
     - 解释（Explanation）
   * - Confirmation
     - PDU发送成功确认

       Confirmation of successful PDU transmission

   * - Data Invalid Value
     - 用于表示发送方无法再提供有效的数据
       
       Used to indicate that the sender can no longer provide valid data.

   * - Dynamic Length Signal
     - 动态长度信号，其长度在运行时可变
       
       Dynamic length signal, whose length is variable at runtime.

   * - Dynamic Length I-PDU
     - 包含动态长度信号的I-PDU，其长度根据动态长度信号改变
       
       An I-PDU containing dynamic length signals, whose length changes according to the dynamic length signals.

   * - Group signal
     - Group signal是包含在signal group中的信号
       
       A group signal is a signal contained in a signal group.

   * - Indication
     - PDU接收指示，表示接收到数据

       PDU reception indication, indicating that data has been received.
       
   * - Init Value
     - Com模块启动后对IPDU和signal设置的初始值
       
       The initial values set for IPDU and signal after the Com module is started.

   * - I-PDU group
     - I-PDUs的组合，用于I-PDU通信模式的控制
       
       A combination of I-PDUs, used for the control of I-PDU communication modes.

   * - Inter-ECU-communication
     - 多个ECU间通信
       
       Communication between multiple ECUs

   * - Intra-ECU-communication
     - 同一个ECU上多个软件组件通信
       
       Communication between multiple software components on the same ECU

   * - Large Signal
     - 大信号是指不能使用下层传输协议单个LPDU传输的信号
       
       A large signal refers to a signal that cannot be transmitted using a single LPDU of the lower-layer transmission protocol.

   * - Large I-PDU
     - 大IPDU是指不能使用下层传输协议单个LPDU传输的IPDU
       
       A large IPDU refers to an IPDU that cannot be transmitted using a single LPDU of the lower-layer transmission protocol.

   * - Message
     - 消息，等价于信号的意思
       
       Message, which is equivalent to the meaning of signal.

   * - Metadata
     - 在CAN通信中，用户动态改变L-PDU的CanId
       
       In CAN communication, users dynamically change the CanId of L-PDU.

   * - Notification
     - AUTOSAR COM模块的通知功能
       
       Notification function of the AUTOSAR COM module

   * - Signal
     - 信号，与OSEK COM中Message等同
       
       Signal, equivalent to Message in OSEK COM.

   * - Signal Group
     - 信号组，用于复杂数据类型，包含N个Group Signals，其数据一致性需得到保证
       
       Signal group, used for complex data types, contains N Group Signals, and the data consistency of which needs to be guaranteed.

   * - Update-bit
     - 接收端标记发送端的数据是否更新过的机制
       
       A mechanism for the receiver to mark whether the sender's data has been updated.


简写（Abbreviation）
--------------------------

.. list-table::
   :widths: 10 20 30
   :header-rows: 1


   * - 简写（Abbreviation）
     - 全称（Full name）
     - 解释（Explanation）
   * - AUTOSAR COM
     - The AUTOSAR COM module is derived from the OSEK communication protocol.
     - AUTOSAR COM来自OSEK通信协议
   * - DM
     - Deadline Monitoring
     - 超时监控
   * - I-PDU
     - Interaction Layer Protocol Data Unit
     - 交互层协议数据单元
   * - L-PDU
     - Data Link Layer Protocol Data Unit
     - 数据链路层协议数据单元
   * - MDT
     - Minimum Delay Timer
     - 最小延迟时间
   * - PDU Router
     - The PDU Router is a module transferring I-PDUs from one module to another module. The PDU Router can be utilized for gateway operations and for internal routing purposes
     - PDU Router是将PDU从一个模块传递给另一个模块，可用于网关操作和内部路由
   * - SDU
     - Service Data Unit.
     - 协议数据单元
   * - TM
     - Transmission Mode
     - I-PDU传输模式
   * - TMC
     - Transmission Mode Condition
     - （信号）传输模式状况
   * - TMS
     - Transmission Mode Selector
     - (I-PDU)传输模式选择


简介（Introduction）
===============================


Com模块主要实现了Signal在I-PDU中的封装及解析功能，为RTE层提供了基于Signal的发送与接收接口，实现了基于Signal的网关功能，实现了PDU的不同发送模式，以及Signal滤波，Update
bit等功能。

The Com module mainly implements the functions of encapsulating and parsing Signals in I-PDUs, provides Signal-based sending and receiving interfaces for the RTE layer, realizes Signal-based gateway functions, implements different sending modes of PDUs, as well as functions such as Signal filtering and Update bit.

.. figure:: ../../../_static/参考手册/Com/image1.png
   :alt: Com模块层次图
   :name: Com_fig_arch
   :align: center

   Figure caption goes here.

   Module hierarchy diagram.


如图 :[Com_fig_arch]所示，Com模块处于AUTOSAR架构中的通信服务层，其下层模块为PduR模块，上层模块为RTE。

As shown in the [Module Hierarchy Diagram], the Com module is located in the Communication Service Layer of the AUTOSAR architecture, with the PduR module as its lower-layer module and the RTE as its upper-layer module.


功能描述（Functional Description）
==========================================
.. 本章节仅描述模块支持的功能大致情况，不宜做细致描述；更加细致的描述在配置章节，结合配置，从集成角度描述

特性（Features）
----------------------

I-PDU Group
~~~~~~~~~~~~~~~~~~~
Com模块实现基于I-PDU Group的使能控制，接收超时检测使能控制。根据I-PDU与I-PDU Group的包含关系，间接实现对各个I-PDU的通信使能控制及Rx I-PDU的接收超时检测使能控制。

The Com module implements enable control based on I-PDU Group and enable control for reception timeout detection. According to the inclusion relationship between I-PDUs and I-PDU Groups, it indirectly realizes the communication enable control for each I-PDU and the enable control for reception timeout detection of Rx I-PDUs.


Signal 封装解析（Signal encapsulation and parsing）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 - 信号的封装和解析是Com模块的核心功能，根据各个信号的配置信息将发送Signal封装到关联的Tx IPdu数据中，从Rx IPdu数据中解析接收Signal。包括对非动态长度类型、动态长度类型的Signal、GroupSignal、字节对齐的SignalGroup的收发。

   The encapsulation and parsing of signals are the core functions of the Com module. It encapsulates the transmitted signals into the associated Tx IPdu data according to the configuration information of each signal, and parses the received signals from the Rx IPdu data. This includes the transmission and reception of non-dynamic length type signals, dynamic length type signals, GroupSignals, and byte-aligned SignalGroups.

 - Com模块为RTE/应用层提供了完整的基于Signal/SignalGroup的收发接口。

   The Com module provides the RTE/application layer with a complete set of sending and receiving interfaces based on Signal/SignalGroup.


IPdu 收发（IPdu transmission and reception）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 - Com模块实现IPdu的收发方式按数据流分两种类型，即IF方式和TP方式，IF方式通常用于“数据长度较小”的IPdu，而TP方式通常用于“数据长度较大”的IPdu，这里的“数据长度”是相对于传输总线来定义的，如CAN总线为8字节，CANFD为64字节，ETH可以达到1000+字节。其中IF IPdu的发送又分为Direct和TriggerTransmit两种类型，前者发送时机由Com决定，后者发送时机由下层模块决定。
 
   The Com module implements two types of IPdu transmission and reception methods based on data flow: the IF mode and the TP mode. The IF mode is usually used for IPdus with "small data length", while the TP mode is generally applied to IPdus with "large data length". Here, the "data length" is defined relative to the transmission bus. For example, the CAN bus is 8 bytes, CANFD is 64 bytes, and ETH can reach more than 1000 bytes. Among them, the transmission of IF IPdu is further divided into two types: Direct and TriggerTransmit. The transmission timing of the former is determined by Com, while that of the latter is decided by the lower-layer module.
 
 - Tx IPdu从发送时机角度又分为四种模式，即PERIODIC，DIRECT，MIXED，NONE。NONE模式通常与TriggerTransmit，或者调用Com_TriggerIPDUSend/ Com_TriggerIPDUSendWithMetaData来配置实现IPdu的发送。

   From the perspective of transmission timing, Tx IPdu is further divided into four modes: PERIODIC, DIRECT, MIXED, and NONE. The NONE mode is usually configured with TriggerTransmit, or by calling Com_TriggerIPDUSend/Com_TriggerIPDUSendWithMetaData to implement the transmission of IPdu.

超时监测功能（Timeout monitoring function）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 - Com模块实现基于Signal/SignalGroup的超时监测功能。对于发送实现超时通知机制，对于接收实现超时通知和超时替换两种机制。

   The Com module implements a timeout monitoring function based on Signal/SignalGroup. For transmission, it implements a timeout notification mechanism; for reception, it implements two mechanisms: timeout notification and timeout replacement.

 - 发送超时监测：监测请求发送到其所在的IPdu发送成功这段时间，IPdu超时时间阈值取请求发送的Signal/SignalGroup配置的超时时间最小值。当发生发送超时，通知上层模块。

   Transmission timeout monitoring: Monitors the period from when a transmission request is made to when the transmission of the IPdu it belongs to is successful. The IPdu timeout threshold is the minimum timeout value configured for the Signal/SignalGroup that requested the transmission. When a transmission timeout occurs, the upper-layer module is notified.

 - 接收超时监测：监测两次正确接收信号值之间的时间段，Signal/SignalGroup超时时间阈值根据其各自的配置参数决定。当发生超时时，进行通知或者将接收信号值替换为初始值、替代值。

   Reception timeout monitoring: Monitors the time period between two successful receptions of signal values. The timeout threshold for a Signal/SignalGroup is determined according to its respective configuration parameters. When a timeout occurs, a notification is sent, or the received signal value is replaced with an initial value or a substitute value.


信号滤波功能（Signal filtering function）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 - Com模块实现基于信号的信号值进行过滤的机制，虽然对于收发信号的过滤算法一样，但过滤的目的完全不同。

   The Com module implements a mechanism for filtering based on the signal values of signals. Although the filtering algorithm for transmitting and receiving signals is the same, the purposes of filtering are completely different.

 - 对于接收Signal/SignalGroup，过滤算法未通过时，将舍弃当前接收到的Signal/SignalGroup。

   For received Signals/SignalGroups, if the filtering algorithm is not passed, the currently received Signal/SignalGroup will be discarded.

 - 对于发送Signal/GroupSignal，过滤算法的结果只决定该发送IPdu选择ComTxModeTrue或者ComTxModeFalse进行报文发送，不会舍弃信号本身。

   For transmitted Signals/GroupSignals, the result of the filtering algorithm only determines whether the transmitting IPdu selects ComTxModeTrue or ComTxModeFalse for message transmission, and the signal itself will not be discarded.


信号Update功能（Signal Update function）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 - Com模块实现基于Signal/SignalGroup的Update Bit机制来识别信号是否更新（信号更新，但信号值不一定变化）。

   The Com module implements an Update Bit mechanism based on Signal/SignalGroup to identify whether a signal has been updated (a signal update does not necessarily mean a change in the signal value).

 - Signal/SignalGroup通过配置参数ComUpdateBitPosition来决定是否支持Update机制，Update Bit本身占用IPdu中一个Bit位，该Bit位为1表示对应Signal/SignalGroup有更新，为0表示对应Signal/SignalGroup没有更新。

   A Signal/SignalGroup determines whether to support the Update mechanism through the configuration parameter ComUpdateBitPosition. The Update Bit itself occupies one bit in the IPdu, where a value of 1 indicates that the corresponding Signal/SignalGroup has been updated, and a value of 0 indicates that the corresponding Signal/SignalGroup has not been updated.

 - 对于发送信号，当请求Signal/SignalGroup发送时，Com模块将其Update位置1，表示该信号有更新，通过ComTxIPdu的配置参数ComTxIPduClearUpdateBit决定什么时候清除（置0）该发送IPdu中所有的Update位。

   For transmitted signals, when a request to send a Signal/SignalGroup is made, the Com module sets its Update Bit to 1, indicating that the signal has been updated. The timing for clearing (setting to 0) all Update Bits in the transmitted IPdu is determined by the configuration parameter ComTxIPduClearUpdateBit of the ComTxIPdu.

 - 对于接收信号，只有当检测到Signal/SignalGroup的Update位为1，才执行进一步的接收操作，否则舍弃该信号。

   For received signals, further reception operations are only performed if the Update Bit of the Signal/SignalGroup is detected as 1; otherwise, the signal is discarded.


信号网关功能（Signal gateway function）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 - Com中信号的网关只针对Signal和GroupSignal，R19_11标准中不再支持基于SignalGroup的网关。信号网关不仅支持1：1，同样支持1：N。

   The signal gateway in Com only targets Signals and GroupSignals. The R19_11 standard no longer supports gateways based on SignalGroups. The signal gateway supports not only 1:1 but also 1:N.

 - 对于GwSource信号与GwDestination信号，其信号类型及信号长度必须一致。GwSource信号关联Rx IPdu，GwDestination信号关联Tx IPdu。

   For GwSource signals and GwDestination signals, their signal types and signal lengths must be consistent. The GwSource signal is associated with the Rx IPdu, and the GwDestination signal is associated with the Tx IPdu.

 - 注：TP Pdu中的Signal/Group Signal不支持信号网关。

   Note: Signals/Group Signals in TP Pdu do not support the signal gateway.

 - 信号网关路由通过配置ComGwMapping实现，GwSource信号可以通过两种方式进行配置，通过配置ComGwSourceDescription方式和通过配置ComGwSignal方式。

   The signal gateway routing is implemented through configuring ComGwMapping. The GwSource signal can be configured in two ways: by configuring ComGwSourceDescription and by configuring ComGwSignal.

 - 同样GwDestination也可以通过两种方式进行配置，通过配置ComGwDestinationDescription方式和通过配置ComGwSignal方式。

   Similarly, the GwDestination can also be configured in two ways: by configuring ComGwDestinationDescription and by configuring ComGwSignal.


多核分布（Multicore distribution）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 - 为了在多分区（核）之间提供负载分配，通信栈的不同部分可以被分配到不同的分区。不同的网络类型如 FlexRay，CAN 和 Ethernet 的部分可以被分配到不同的分区（核）。

   To provide load distribution among multiple partitions (cores), different parts of the communication stack can be allocated to different partitions. Components of different network types such as FlexRay, CAN, and Ethernet can be assigned to separate partitions (cores).

 - 为了支持上述灵活的分配，减少分区间的通信（从而潜在的减少跨分区同步带来的阻塞），COM 模块可以按照网络类型创建不同的 MainFunction（每个分区至少一个）。在具体的 MainFunction 中仅处理与该网络类型相关的 PDU，接收和发送将保持在单个网络范围内（即在单个分区中），因此不需要考虑跨分区同步的问题。唯一的例外是信号网关，当信号网关的源和目的PDU不在同一个分区时，COM模块提供跨分区的数据一致性保护。每个 MainFunction 都拥有独立的 Time Base。

   To support the above flexible allocation and reduce inter-partition communication (thereby potentially reducing blocking caused by cross-partition synchronization), the COM module can create different MainFunctions according to network types (at least one per partition). Each specific MainFunction only processes PDUs related to that network type, and reception and transmission are kept within a single network scope (i.e., within a single partition), thus eliminating the need to consider cross-partition synchronization. The only exception is the signal gateway: when the source and destination PDUs of the signal gateway are not in the same partition, the COM module provides cross-partition data consistency protection. Each MainFunction has an independent Time Base.

 - ComIPdu 通过 ComIPduMainFunctionRef 与特定的 ComMainFunctionRx/ComMainFunctionTx 关联。ComMainFunctionRouteSignalsRef 仅在信号网关目标信号所在的 ComIPdu 上使用。ComMainRxPartitionRef/ComMainTxPartitionRef/ComMainRouteSignalsPartitionRef 分别表示该 ComMainFunction 实例运行的分区。如果配置了分区信息，则 ComMainFunction 所在的分区必须与 ComIPdu 关联的 Pdu（EcucPduDefaultPartitionRef）的分区一致。此处强调，如果发送IPDU（IPDU或者IPDU包含的信号和组信号）用于信号网关，则其需要同时配置ComIPduMainFunctionRef 关联到ComMainFunctionTx 和配置ComMainFunctionRouteSignalsRef，并且分区一致。

   ComIPdu is associated with specific ComMainFunctionRx/ComMainFunctionTx through ComIPduMainFunctionRef. ComMainFunctionRouteSignalsRef is only used on the ComIPdu where the target signal of the signal gateway is located. ComMainRxPartitionRef/ComMainTxPartitionRef/ComMainRouteSignalsPartitionRef respectively indicate the partition in which the ComMainFunction instance runs. If partition information is configured, the partition where ComMainFunction is located must be consistent with the partition of the Pdu (EcucPduDefaultPartitionRef) associated with ComIPdu. It is emphasized here that if a transmitting IPDU (IPDU or the signals and group signals contained in the IPDU) is used for the signal gateway, it needs to be configured with ComIPduMainFunctionRef associated to ComMainFunctionTx and ComMainFunctionRouteSignalsRef at the same time, and the partitions must be consistent.

 - Com模块如果配置了ComIpduGroup，则其必须被至少一个IPDU关联，且关联在同一个ComIpduGroup的IPDU的分区必须一致。

   If the Com module is configured with ComIpduGroup, it must be associated with at least one IPDU, and the partitions of the IPDUs associated with the same ComIpduGroup must be consistent.

 - IPDU的分区信息是在ECUC模块配置实现的，Com模块配置并校验成功后，在ECUC模块右键Synchronize Module选择Com模块进行同步，可以将Com模块的分区信息同步到ECUC模块的IPDU上。

   The partition information of IPDU is configured and implemented in the ECUC module. After the Com module is configured and verified successfully, right-click "Synchronize Module" in the ECUC module and select the Com module to synchronize, so that the partition information of the Com module can be synchronized to the IPDU of the ECUC module.

 - 代码生成器会为每一个 ComMainFunction 生成一个函数（声明在SchM_Com.h）。每一个 ComMainFunction 的实例和API接口在集成时需要被放在正确的分区中被调用。建议开发阶段打开ComConfigurationUseDet配置，存在不合理的分区调用时，可以报Det错误。

   The code generator will generate a function for each ComMainFunction (declared in SchM_Com.h). Each ComMainFunction instance and API interface needs to be placed in the correct partition to be called during integration. It is recommended to enable the ComConfigurationUseDet configuration during the development phase. If there is an unreasonable partition call, a Det error can be reported.


.. only:: doc_pbs

  支持变体功能（Support variant functionality）
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  - 信号过滤器仅在为ONE_EVERY_N时周期可配置变体
  
    The signal filter is only configurable as a variant when the period is set to ONE_EVERY_N.
  
  - 支持配置IPdu数目、信号数目、信号组、组信号数目、IPduGroup数目变体
    
    Supports configuring variants for the number of IPdus, the number of signals, signal groups, the number of group signals, and the number of IPduGroups.
  
  - 支持IPdu信号处理模式配置变体
  
    Supports configuring variants for the IPdu signal processing mode.
  
  - 支持IPdu关联的信号、信号组、IPduGroup配置变体
  
    Supports configuring variants for signals, signal groups, and IPduGroups associated with IPdus.
  
  - Pdu发送模式支持变体
  
    Supports variants for Pdu transmission modes.
  
  - 信号网关支持变体
  
    Supports variants for signal gateways.


偏差（Deviation）
--------------------------
.. 有序列表示例

#. ComConfig->ComIpduGroup->ComIpduGroupRef

   因为该功能未实现，所以工具不可配置

   Since this function has not been implemented, the tool cannot be configured.

#. ComConfig->ComMainfunctionTx->ComPreparationNotification

   因为该功能未实现，所以工具不可配置

   Since this function has not been implemented, the tool cannot be configured.

#. 暂未实现API

   API not yet implemented

  - Com_ReceiveSignalWithMetaData
  - Com_ReceiveDynSignalWithMetaData
  - Com_ReceiveSignalGroupWithMetaData
  - Com_ReceiveSignalGroupArrayWithMetaData
  - Com_SendSignalWithMetaData
  - Com_SendDynSignalWithMetaData
  - Com_SendSignalGroupArrayWithMetaData

扩展（Extension）
--------------------

None

集成（Integration）
==========================

文件列表（File list）
-------------------------------

静态文件（Static files）
~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - 文件（File）
     - 描述（Description）

   * - Com.h
     - 实现Com模块全部外部接口的声明，以及配置文件中全局变量的声明
       
       Implement the declarations of all external interfaces of the Com module, as well as the declarations of global variables in the configuration file.

   * - Com.c
     - 作为Com模块的核心文件，实现Com模块全部对外接口，以及实现Com模块功能所必须的local函数，local宏定义，local变量定义
       
       As the core file of the Com module, it implements all external interfaces of the Com module, as well as the local functions, local macro definitions, and local variable definitions that are necessary for realizing the functions of the Com module.

   * - Com_Internal.h
     - 实现Com模块内部函数的声明
       
       Implement the declaration of internal functions of the Com module

   * - Com_Internal.c
     - 实现Com模块公共内部函数的定义
       
       Implement the definition of public internal functions of the Com module

   * - Com_GwInternal.c
     - 实现Com模块信号网关功能内部函数的定义
       
       Implement the definition of internal functions for the Com module's signal gateway functionality

   * - Com_RxInternal.c
     - 实现Com模块信号接收内部函数的定义
       
       Implement the definition of internal functions for signal reception in the Com module

   * - Com_TxInternal.c
     - 实现Com模块信号发送内部函数的定义
       
       Implement the definition of internal functions for signal transmission in the Com module

   * - Com_MemMap.h
     - 实现Com模块内存布局
       
       Implement the memory layout of the Com module

   * - Com_Types.h
     - 实现外部/内部类型的定义，包括AUTOSAR标准定义的类型，以及PB/PC配置参数结构体类型，以及内部运行时结构体类型
       
       Implement the definitions of external/internal types, including types defined by the AUTOSAR standard, as well as structure types for PB/PC configuration parameters and internal runtime structure types.

   * - Com_Cbk.h
     - 实现Com模块全部回调函数的声明
       
       Implement the declarations of all callback functions of the Com module


动态文件（Dynamic file）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - 文件（File）
     - 描述（Description）

   * - Com_Cfg.h
     - 定义Com模块PC配置的宏定义
       
       Define the macro definitions for the Com module's PC configuration

   * - Com_PBcfg.c
     - 定义Com模块PB配置的结构体参数和ComMainFunction的定义。
       
       Define the structure parameters for the Com module's PB configuration and the definition of ComMainFunction.

   * - Com_PBcfg.h
     - 定义Com模块PB配置的宏定义
       
       Define the macro definitions for the PB configuration of the Com module


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

   * - COM_E_PARAM
     - 0x01
     - API 服务调用了错误的参数
       
       The API service was called with incorrect parameters.

   * - COM_E_UNINIT
     - 0x02
     - 未初始化的错误
       
       Uninitialized error

   * - COM_E_PARAM_POINTER
     - 0x03
     - 检测到空指针
       
       Null pointer detected

   * - COM_E_INIT_FAILED
     - 0x04
     - 初始化失败
       
       Initialization failed


产品错误（Product error）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
None

运行时错误（Runtime error）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. list-table::
   :widths: 20 10 30
   :header-rows: 1

   * - Error code
     - Value[hex]
     - Description

   * - COM_E_SKIPPED_TRANSMISSION
     - 0x05
     - 传输请求被跳过
       
       The transmission request was skipped.


接口描述（Interface Description）
======================================
.. include:: Com_Cbk_h_api.rst
.. include:: Com_h_api.rst


配置函数（Configuration function）
----------------------------------------
None

依赖的服务（Dependent services）
-----------------------------------------

强制接口（Mandatory interface）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. 可选的章节，根据模块实际情况确定

.. list-table::
   :widths: 10 5 30
   :header-rows: 1

   * - API Function
     - Header File
     - Description

   * - PduR_ComTransmit
     - PduR_Com.h
     - Requests transmission of a PDU


可选接口（Optional interface）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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

   * - Det_ReportRuntimeError
     - Det.h
     - Service to report runtime errors. If a callout has been configured then this callout shall be called.

   * - PduR_ComCancelTransmit
     - PduR_Com.h
     - Requests cancellation of an ongoing transmission of a PDU in a lower layer communication module.


配置接口（Configuration Interface）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. 可选的章节，根据模块实际情况确定
.. 格式同强制接口

.. list-table::
   :widths: 10 20 10
   :header-rows: 1

   * - API Function
     - Header File
     - Description

   * - Com_CbkTxAck
     - Com_Callout.h(不存在Rte模块情况下)/Rte_Cbk.h(存在Rte模块情况下)
       
       Com_Callout.h (when the Rte module does not exist) / Rte_Cbk.h (when the Rte module exists)

     - 传输成功回调
       
       Transmission success callback

   * - Com_CbkTxErr
     - Com_Callout.h(不存在Rte模块情况下)/Rte_Cbk.h(存在Rte模块情况下)
       
       Com_Callout.h (when the Rte module does not exist) / Rte_Cbk.h (when the Rte module exists)

     - 传输失败回调
       
       Transmission failure callback

   * - Com_CbkTxTOut
     - Com_Callout.h(不存在Rte模块情况下)/Rte_Cbk.h(存在Rte模块情况下)
       
       Com_Callout.h (when the Rte module does not exist) / Rte_Cbk.h (when the Rte module exists)

     - 发送超时回调
       
       Transmission timeout callback

   * - Com_CbkRxAck
     - Com_Callout.h(不存在Rte模块情况下)/Rte_Cbk.h(存在Rte模块情况下)
       
       Com_Callout.h (when the Rte module does not exist) / Rte_Cbk.h (when the Rte module exists)

     - 接收成功回调
       
       Reception success callback

   * - Com_CbkRxTOut
     - Com_Callout.h(不存在Rte模块情况下)/Rte_Cbk.h(存在Rte模块情况下)
       
       Com_Callout.h (when the Rte module does not exist) / Rte_Cbk.h (when the Rte module exists)

     - 接收超时回调
       
       Reception timeout callback

   * - Com_CbkInv
     - Com_Callout.h(不存在Rte模块情况下)/Rte_Cbk.h(存在Rte模块情况下)
       
       Com_Callout.h (when the Rte module does not exist) / Rte_Cbk.h (when the Rte module exists)

     - 接收无效值回调
       
       Reception of invalid value callback

   * - Com_RxIpduCallout
     - Com_Callout.h
     - RxIpdu接收通知
       
       RxIpdu reception notification

   * - Com_TxIpduCallout
     - Com_Callout.h
     - TxIpdu接收通知
       
       TxIpdu reception notification


配置（configuration）
===========================

1. Rx Path
----------------------
1.1 RxIpdu Path
----------------------
.. figure:: ../../../_static/参考手册/Com/RxIpdu1.png
   :alt: RxIpdu1
   :name: RxIpdu1
   :align: center

   RxIpdu1

.. figure:: ../../../_static/参考手册/Com/RxIpdu2.png
   :alt: RxIpdu2
   :name: RxIpdu2
   :align: center

   RxIpdu2

如图 :[RxIpdu1] 和 [RxIpdu2]所示:

 As shown in [RxIpdu1] and [RxIpdu2] in the figure:

 - Ipdu传输方向：ComIPduDirection = RECEIVE

   IPdu transmission direction: ComIPduDirection = RECEIVE

 - 处理时机：ComIPduSignalProcessing = IMMEDIATE立即处理 、DEFERRED异步处理

   Processing timing: ComIPduSignalProcessing = IMMEDIATE (immediate processing), DEFERRED (asynchronous processing) 

 - Ipdu类型：ComIPduType = NORMAL普通类型Ipdu、TP TP类型Ipdu
    
   IPdu type: ComIPduType = NORMAL (normal type IPdu), TP (TP type IPdu)

 .. figure:: ../../../_static/参考手册/Com/RxIpduGroup.png
    :alt: RxIpduGroup
    :name: RxIpduGroup
    :align: center

    RxIpduGroup

 - 关联IpduGroup：ComIPduGroupRef = ComIpduGroup,如图 [RxIpduGroup]所示
   
   Associated IpduGroup: ComIPduGroupRef = ComIpduGroup, as shown in [RxIpduGroup] in the figure

 - MainFunction关联：ComIPduMainFunctionRef = ComMainFunctionRx，存在多个ComMainFunctionRx时，则所有RxIpdu都必须关联ComMainFunctionRx，否则可不关联

   MainFunction association: ComIPduMainFunctionRef = ComMainFunctionRx. When there are multiple ComMainFunctionRx instances, all RxIpdu must be associated with ComMainFunctionRx; otherwise, no association is required.

 - 关联ComIPduSignalGroupRef = ComSignalGroup（如果存在）

   Associated ComIPduSignalGroupRef = ComSignalGroup (if it exists)

 - 关联ComIPduSignalRef = ComIPduSignal（如果存在）

   Associated ComIPduSignalRef = ComIPduSignal (if it exists)

 .. figure:: ../../../_static/参考手册/Com/EcuCRx.png
    :alt: EcuCRx
    :name: EcuCRx
    :align: center

    EcuCRx

 - 关联ComPduIdRef = EcuC模块->EcucConfigSet->EcucPduCollection->Pdu，如图 [EcuCRx]所示:

   Associated ComPduIdRef = EcuC module -> EcucConfigSet -> EcucPduCollection -> Pdu, as shown in [EcuCRx] in the figure:


1.2 RxSignal Path
----------------------
.. figure:: ../../../_static/参考手册/Com/RxSignal.png
   :alt: RxSignal
   :name: RxSignal
   :align: center

   RxSignal

如图 [RxSignal]所示:

As shown in [RxSignal] in the figure:

 - 起始位ComBitPosition

   Start bit: ComBitPosition

 - 信号长度（bit）ComBitSize

   Signal length (bit): ComBitSize

 - 信号端序ComSignalEndianness = LITTLE_ENDIAN小端、BIG_ENDIAN大端

   Signal endianness: ComSignalEndianness = LITTLE_ENDIAN (little-endian), BIG_ENDIAN (big-endian)

 - 初始值ComSignalInitValue

   Initial value: ComSignalInitValue

 - 信号类型ComSignalType如图, [SignalType]所示:

   Signal type: ComSignalType, as shown in [SignalType] in the figure:


 .. figure:: ../../../_static/参考手册/Com/SignalType.png
    :alt: SignalType
    :name: SignalType
    :align: center

    ComSignalType

 - 信号触发方式选择ComTransferProperty如图所示， [TransferProperty]所示:

   The selection of signal triggering mode is ComTransferProperty as shown in [TransferProperty] in the figure:


 .. figure:: ../../../_static/参考手册/Com/TransferProperty.png
    :alt: TransferProperty
    :name: TransferProperty
    :align: center

    TransferProperty

1.3 RxSignalGroup Path
----------------------
.. figure:: ../../../_static/参考手册/Com/RxSignalGroup.png
   :alt: RxSignalGroup
   :name: RxSignalGroup
   :align: center

   RxSignalGroup

如图 [RxSignalGroup]所示:

As shown in [RxSignalGroup]:

 - 信号触发方式选择ComTransferProperty，同 [TransferProperty]所示。

   The selection of signal triggering mode is ComTransferProperty, which is the same as shown in [TransferProperty].

2. Tx Path
----------------------
2.1 TxIpdu Path
----------------------
 .. figure:: ../../../_static/参考手册/Com/TxIpdu1.png
    :alt: TxIpdu1
    :name: TxIpdu1
    :align: center

    TxIpdu1

 .. figure:: ../../../_static/参考手册/Com/TxIpdu2.png
    :alt: TxIpdu2
    :name: TxIpdu2
    :align: center

    TxIpdu2

 - Ipdu传输方向：ComIPduDirection = SEND

   IPdu transmission direction: ComIPduDirection = SEND

 - 处理时机：ComIPduSignalProcessing = IMMEDIATE立即处理 、DEFERRED异步处理

   Processing timing: ComIPduSignalProcessing = IMMEDIATE (immediate processing), DEFERRED (asynchronous processing)

 - Ipdu类型：ComIPduType = NORMAL普通类型Ipdu、TP TP类型Ipdu

   IPdu type: ComIPduType = NORMAL (normal type IPdu), TP (TP type IPdu)

 - 关联IpduGroup：ComIPduGroupRef = ComIpduGroup,如图 [TxIpduGroup]所示
      
   Associated IpduGroup: ComIPduGroupRef = ComIpduGroup, as shown in [TxIpduGroup] in the figure
 

 .. figure:: ../../../_static/参考手册/Com/TxIpduGroup.png
    :alt: TxIpduGroup
    :name: TxIpduGroup
    :align: center

    TxIpduGroup

 - MainFunction关联：ComIPduMainFunctionRef = ComMainFunctionTx，存在多个ComMainFunctionTx时，则所有TxIpdu都必须关联ComMainFunctionTx，否则可不关联

   MainFunction association: ComIPduMainFunctionRef = ComMainFunctionTx. When there are multiple ComMainFunctionTx instances, all TxIpdu must be associated with ComMainFunctionTx; otherwise, no association is required.

 - MainFunction关联：ComMainFunctionRouteSignalsRef = ComMainFunctionRouteSignals，如果该Ipdu或者包含的Signal/GroupSignal用于信号网关，且ComMainFunctionRouteSignals存在多个，则该TxIpdu都必须关联，否则可不关联

   MainFunction association: ComMainFunctionRouteSignalsRef = ComMainFunctionRouteSignals. If this IPdu or the contained Signal/GroupSignal is used for the signal gateway, and there are multiple ComMainFunctionRouteSignals instances, this TxIpdu must be associated; otherwise, no association is required.

 - 关联ComIPduSignalGroupRef = ComSignalGroup（如果存在）
 
   Associated ComIPduSignalGroupRef = ComSignalGroup (if it exists)

 - 关联ComIPduSignalRef = ComIPduSignal（如果存在）

   Associated ComIPduSignalRef = ComIPduSignal (if it exists)

 - 关联ComPduIdRef = EcuC模块->EcucConfigSet->EcucPduCollection->Pdu，如图 [EcuCTx]所示:

   Associated ComPduIdRef = EcuC module -> EcucConfigSet -> EcucPduCollection -> Pdu, as shown in [EcuCTx] in the figure:

  .. figure:: ../../../_static/参考手册/Com/EcuCTx.png
    :alt: EcuCTx
    :name: EcuCTx
    :align: center

    EcuCTx

2.2 TxSignal Path
----------------------
.. figure:: ../../../_static/参考手册/Com/TxSignal.png
   :alt: TxSignal
   :name: TxSignal
   :align: center

   TxSignal

如图 [TxSignal]所示:

As shown in [TxSignal]:

 - 起始位ComBitPosition

   Start bit: ComBitPosition

 - 信号长度（bit）ComBitSize
   Signal length (bit): ComBitSize
 - 信号端序ComSignalEndianness = LITTLE_ENDIAN小端、BIG_ENDIAN大端

   Signal endianness: ComSignalEndianness = LITTLE_ENDIAN (little-endian), BIG_ENDIAN (big-endian)

 - 初始值ComSignalInitValue

   Initial value: ComSignalInitValue

 - 信号类型ComSignalType如图, [SignalType]所示

   Signal type: ComSignalType, as shown in [SignalType]

 - 信号触发方式选择ComTransferProperty如图所示， [TransferProperty]所示

   The selection of signal triggering mode: ComTransferProperty, as shown in [TransferProperty]

2.3 TxSignalGroup Path
----------------------
.. figure:: ../../../_static/参考手册/Com/TxSignalGroup.png
   :alt: TxSignalGroup
   :name: TxSignalGroup
   :align: center

   TxSignalGroup

如图 [TxSignalGroup]所示:

As shown in [TxSignalGroup]:

 - 信号触发方式选择ComTransferProperty，同 [TransferProperty]所示。

   The selection of signal triggering mode is ComTransferProperty, which is the same as shown in [TransferProperty].

2.4 TxFilter Path
----------------------
发送滤波可配置在TxSignal、TxGroupSignal、ComGwDestinationDescription，配置滤波的前提条件是必须同时配置了，如图 [TxModeTrueFalse]所示:

Transmission filtering can be configured in TxSignal, TxGroupSignal, and ComGwDestinationDescription. The prerequisite for configuring filtering is that it must be configured simultaneously, as shown in [TxModeTrueFalse] in the figure:

.. figure:: ../../../_static/参考手册/Com/TxModeTrueFalse.png
   :alt: TxModeTrueFalse
   :name: TxModeTrueFalse
   :align: center

   TxModeTrueFalse

滤波配置，如图 [Filter]所示:

Filter configuration, as shown in [Filter] in the figure:

.. figure:: ../../../_static/参考手册/Com/Filter.png
   :alt: Filter
   :name: Filter
   :align: center

   Filter

2.5 RxFilter Path
----------------------
接收滤波可配置在RxSignal、RxGroupSignal，滤波配置，如图 [Filter]所示:

Reception filtering can be configured in RxSignal and RxGroupSignal. The filter configuration is as shown in [Filter] in the figure:

3. Gateway Path
----------------------
3.1 Src:Signal
----------------------
.. figure:: ../../../_static/参考手册/Com/SrcSignal.png
   :alt: SrcSignal
   :name: SrcSignal
   :align: center

   Source:ComGwSignal

信号网关Source配置，ComGwSignal关联Signal或者GroupSignal如图 [SrcSignal]所示:

Signal gateway Source configuration: ComGwSignal is associated with Signal or GroupSignal as shown in [SrcSignal].

3.2 Src:Description
----------------------
.. figure:: ../../../_static/参考手册/Com/SrcDesp.png
   :alt: SrcDesp
   :name: SrcDesp
   :align: center

   Source:ComGwSourceDescription

信号网关Source配置，ComGwSourceDescription关联Ipdu如图 [SrcDesp]所示:

Signal gateway Source configuration: ComGwSourceDescription is associated with Ipdu as shown in [SrcDesp]:

 - 起始位ComBitPosition

   Start bit: ComBitPosition

 - 信号长度（bit）ComBitSize

   Signal length (bit): ComBitSize

 - 信号端序ComSignalEndianness = LITTLE_ENDIAN小端、BIG_ENDIAN大端

   Signal endianness: ComSignalEndianness = LITTLE_ENDIAN (little-endian), BIG_ENDIAN (big-endian)

 - 初始值ComSignalInitValue

   Initial value: ComSignalInitValue

 - 信号类型ComSignalType如图, [SignalType]所示

   Signal type: ComSignalType, as shown in [SignalType]

 - 关联ComGwIPduRef = RxIpdu

   Associated ComGwIPduRef = RxIpdu

3.3 Dest:Signal
----------------------
信号网关Destination配置，ComGwSignal关联Signal或者GroupSignal如图 [DestSignal]所示:

Signal gateway Destination configuration: ComGwSignal is associated with Signal or GroupSignal as shown in [DestSignal].

.. figure:: ../../../_static/参考手册/Com/DestSignal.png
   :alt: DestSignal
   :name: DestSignal
   :align: center

   Source:ComGwSignal

3.4 Dest:Description
----------------------
信号网关Destination配置，ComGwDestinationDescription关联Ipdu如图 [DestDesp]所示:

Signal gateway Destination configuration: ComGwDestinationDescription is associated with Ipdu as shown in [DestDesp]:

 .. figure:: ../../../_static/参考手册/Com/DestDesp.png
    :alt: DestDesp
    :name: DestDesp
    :align: center

    Source:ComGwDestinationDescription

 - 起始位ComBitPosition

   Start bit: ComBitPosition

 - 信号端序ComSignalEndianness = LITTLE_ENDIAN小端、BIG_ENDIAN大端

   Signal endianness: ComSignalEndianness = LITTLE_ENDIAN (little-endian), BIG_ENDIAN (big-endian)

 - 初始值ComSignalInitValue

   Initial value: ComSignalInitValue

 - 信号触发方式选择ComTransferProperty如图所示， [TransferProperty]所示

   Selection of signal triggering mode: ComTransferProperty as shown in [TransferProperty]

 - 关联ComGwIPduRef = TxIpdu

   Associated ComGwIPduRef = TxIpdu

4. Notification/Callback and Callout
--------------------------------------------
4.1 Notification
----------------------
 - 接收回调,如图 [RxCbk]所示

   Receive callback, as shown in [RxCbk] in the figure

 .. figure:: ../../../_static/参考手册/Com/RxCbk.png
    :alt: RxCbk
    :name: RxCbk
    :align: center

    ComNotification:Rte_COMCbk

 - 发送回调,如图 [TxCbk]所示

   Transmission callback, as shown in [TxCbk] in the figure

 .. figure:: ../../../_static/参考手册/Com/TxCbk.png
    :alt: TxCbk
    :name: TxCbk
    :align: center

    ComNotification:Rte_COMCbkTAck

 - 无效值接收通知,先配置无效值ComSignalDataInvalidValue，才可以配置ComDataInvalidAction，如果ComDataInvalidAction = NOTIFY，则可配置ComInvalidNotification无效值通知， 如果ComDataInvalidAction = REPLACE,则实现的是接收无效值后，接收值被替换为初始值。
     
   Invalid value reception notification: The invalid value ComSignalDataInvalidValue must be configured first before ComDataInvalidAction can be configured. If ComDataInvalidAction = NOTIFY, then the ComInvalidNotification (invalid value notification) can be configured. If ComDataInvalidAction = REPLACE, it means that after receiving an invalid value, the received value will be replaced with the initial value.

 - 无效值发送通知,通无效值接收通知，但是区别在于发送不会进行无效值替换，只有通知功能。发送无效值可以使用API函数实现。如图 :[RxInvalid]所示
     
   Invalid value transmission notification: Similar to the invalid value reception notification, but the difference is that transmission will not perform invalid value replacement and only has a notification function. Sending invalid values can be implemented using API functions.As shown in: [RxInvalid]

 .. figure:: ../../../_static/参考手册/Com/RxInvalid.png
    :alt: RxInvalid
    :name: RxInvalid
    :align: center

    ComInvalidNotification

 - 接收超时监测通知，必须配置非零ComTimeout，可根据需求配置ComFirstTimeout，接收超时通知ComTimeoutNotification与接收通知相互独立，接收超时动作ComRxDataTimeoutAction = NONE不处理、REPLACE替换初始值、SUBSTITUTE替换ComTimeoutSubstitutionValue值。如图 :[RxTimeout]所示
     
   Reception timeout monitoring notification: A non-zero ComTimeout must be configured. ComFirstTimeout can be configured as required. The reception timeout notification (ComTimeoutNotification) is independent of the reception notification. The reception timeout action (ComRxDataTimeoutAction) includes: NONE (no processing), REPLACE (replace with initial value), and SUBSTITUTE (replace with ComTimeoutSubstitutionValue).As shown in: [RxTimeout]

 .. figure:: ../../../_static/参考手册/Com/RxTimeout.png
    :alt: RxTimeout
    :name: RxTimeout
    :align: center

    ComTimeoutNotification

 - 发送超时监测通知，必须配置非零ComTimeout，可根据需求配置发送超时通知ComTimeoutNotification与发送通知相互独立，超时动作ComRxDataTimeoutAction = NONE不处理。如图 :[TxTimeout]所示
     
   Transmission timeout monitoring notification: A non-zero ComTimeout must be configured. The transmission timeout notification (ComTimeoutNotification) can be configured as required and is independent of the transmission notification. The timeout action (ComRxDataTimeoutAction) is set to NONE (no processing).As shown in: [TxTimeout]

 .. figure:: ../../../_static/参考手册/Com/TxTimeout.png
    :alt: TxTimeout
    :name: TxTimeout
    :align: center

    ComTimeoutNotification

 - 接收发送IPDU callout,用户填写callout使用的函数名字，如图 :[RxCallout]所示
     
   Receive and send IPDU callout: Users fill in the function name used for the callout, as shown in: [RxCallout]

 .. figure:: ../../../_static/参考手册/Com/RxCallout.png
    :alt: RxCallout
    :name: RxCallout
    :align: center

    ComIPduCallout







