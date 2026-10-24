========================
EthTSyn
========================
.. 标题标识符“===”的长度必须要大于其内容的长度，否则会报错，其他标题亦是如此
.. The length of the title identifier "===" must be greater than the length of its content; otherwise, an error will occur. The same applies to other titles.


文档信息 (Document Information)
==================================================================

版本历史 (Version History)
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

   * - 2026/01/15
     - caihong.liu
     - V1.1
     - 增加
     - 补充3.0版本特性描述


参考文档 (References)
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


术语与简写 (Terms and Abbreviations)
==================================================================


术语 (Terms)
------------------------------------------------------------------------------------------------------------------
.. :align: center   表格内容居中(Table contents are centered)


.. list-table::
   :widths: 10 40
   :header-rows: 1

   * - 术语(Terms)
     - 解释(Explanation)

   * - PTP
     - 一种高精度时间同步协议,可以到达亚微秒级精度(A high-precision time synchronization protocol that can achieve sub-microsecond accuracy)

   * - TLV
     - Type/Tag–Length–Value（TLV） 是一种被多种协议采用（例如 IEEE 802.1AS）用于对数据元素进行编码的方案

   * - ICV
     - 完整性校验值

简写 (Abbreviations)
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

简介 (Introduction)
=================================

  EthTSyn模块负责确保以太网同步时间信息的采集和分发。它与StbM交互,并为StbM提供所有特定于以太网的功能。EthTSyn主要功能包括测量以太网消息之间的延迟和不同时基之前的时间同步。

  The EthTSyn module is responsible for ensuring the collection and distribution of Ethernet synchronized time information. It interacts with StbM and provides all Ethernet-specific functions for StbM. The main functions of EthTSyn include measuring the delay between Ethernet messages and time synchronization before different time bases.

  .. figure:: /_static/参考手册(Module_Reference_Manual)/EthTSyn/EthTSyn_layer.png
    :alt: EthTSyn模块层次图(EthTSyn Module Hierarchy Diagram)
    :align: center

  如图所示，EthTSyn模块处于AUTOSAR架构中的系统服务层，其依赖Ethif和StbM两个模块。

  As shown in the figure, the EthTSyn module is located in the system service layer of the AUTOSAR architecture and depends on two modules, Ethif and StbM.



功能描述 (Functional Description)
==================================================================
.. 本章节仅描述模块支持的功能大致情况，不宜做细致描述；更加细致的描述在配置章节，结合配置，从集成角度描述

公共特性(Public Features)
-----------------------------

多核多分区功能(Multi-core and Multi-partition Features)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  - EthTSyn的工作单位为EthTSynPortConfig，每EthTSynPortConfig从它的上一层容器EthTSynGlobalTimeDomin获取EthIfController引用并决定 EthTSynPortConfig 的分区。

  The working unit of EthTSyn is EthTSynPortConfig. Each EthTSynPortConfig obtains an EthIfController reference from its upper-layer container, EthTSynGlobalTimeDomain, and determines the partition of EthTSynPortConfig.
 
  - EthTSynGlobalTimeDomin 与 EthTSynPortConfig 是一对多的关系，通过创建多个 EthTSynGlobalTimeDomainId 相同的 EthTSynTimeDomin 容器关联不同 EthIfController 和 EthTSynPort

  EthTSynGlobalTimeDomain and EthTSynPortConfig have a one-to-many relationship. Multiple EthTSynTimeDomain containers with the same EthTSynGlobalTimeDomainId are created to associate with different EthIfControllers and EthTSynPorts.







Memmap功能(Memmap Features)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  memmap文件是动态的。存在ETHTSYN_START_SEC_CODE、ETHTSYN_START_SEC_CONST_8、ETHTSYN_START_SEC_CONFIG_DATA_32、ETHTSYN_START_SEC_CONFIG_DATA_PTR、ETHTSYN_START_SEC_CONFIG_DATA_UNSPECIFIED、ETHTSYN_START_SEC_VAR_CLEARED_8、ETHTSYN_START_SEC_VAR_CLEARED_16、ETHTSYN_START_SEC_VAR_CLEARED_64、ETHTSYN_START_SEC_VAR_CLEARED_BOOLEAN、ETHTSYN_START_SEC_VAR_CLEARED_PTR、ETHTSYN_START_SEC_VAR_CLEARED_UNSPECIFIED、VAR_CLEARED_GLOBAL_UNSPECIFIED、ETHTSYN_START_SEC_VAR_CLEARED_EcucPartition_C1P0_Trust_UNSPECIFIED。

  The memmap file is dynamic.There are ETHTSYN_START_SEC_CODE、ETHTSYN_START_SEC_CONST_8、ETHTSYN_START_SEC_CONFIG_DATA_32、ETHTSYN_START_SEC_CONFIG_DATA_PTR、ETHTSYN_START_SEC_CONFIG_DATA_UNSPECIFIED、ETHTSYN_START_SEC_VAR_CLEARED_8、ETHTSYN_START_SEC_VAR_CLEARED_16、ETHTSYN_START_SEC_VAR_CLEARED_64、ETHTSYN_START_SEC_VAR_CLEARED_BOOLEAN、ETHTSYN_START_SEC_VAR_CLEARED_PTR、ETHTSYN_START_SEC_VAR_CLEARED_UNSPECIFIED、VAR_CLEARED_GLOBAL_UNSPECIFIED、ETHTSYN_START_SEC_VAR_CLEARED_EcucPartition_C1P0_Trust_UNSPECIFIED.

独占区功能(Exclusive Area Features)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  None.

模块特性(Module Features)
---------------------------------------------------------


周期时间同步 (Periodic Time Synchronization)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  EthTSyn默认采用的是周期时间同步，作为主时钟(TIME_MASTER)的端口将以可配置的周期循环发送SYNC和FOLLOWUP报文。其中的全局同步时间将在FOLLOWUP报文中携带。从时钟(TIME_SLAVE)收到SYNC报文后，将会记下当前时间。当收到FOLLOWUP报文后，解析出携带的全局同步时间，最后计算出本地需要更新的全局时间进行最终的同步。

  EthTSyn adopts periodic time synchronization by default. The port acting as the master clock (TIME_MASTER) will send SYNC and FOLLOWUP messages cyclically at a configurable period. The global synchronization time is carried in the FOLLOWUP message. After receiving the SYNC message, the slave clock (TIME_SLAVE) will record the current time. After receiving the FOLLOWUP message, parse out the carried global synchronization time, and finally calculate the global time that needs to be updated locally for final synchronization.


立即时间同步 (Immediate Time Synchronization)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  除了周期的时间同步，EthTSyn还支持立即时间同步。通过上层APP调用stbm的立即时间同步接口StbM_TriggerTimeTransmission，EthTSyn模块将立即出发SYNC和Follow-Up报文的发送。

  In addition to periodic time synchronization, EthTSyn also supports immediate time synchronization. By calling the immediate time synchronization interface StbM_TriggerTimeTransmission of stbm from the upper-layer APP, the EthTSyn module will immediately trigger the sending of SYNC and Follow-Up messages.



延迟测量 (Delay Measurement)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  EthTSyn模块支持对网路延迟进行测量，测量发起方将发送Pdelay_Req报文，接收方收到请求报文后，将会恢复Pdelay_Response和Pdelay_Response_Followup报文。请求方通过计算可得到网络延迟。注意：因为AUTOSAR的时间同步符合802.1AS，要求时间同步是p2p的模式，即时间同步和网络延迟是相互独立进行的。

  The EthTSyn module supports measuring network delay. The measurement initiator will send a Pdelay_Req message. After receiving the request message, the receiver will restore the Pdelay_Response and Pdelay_Response_Followup messages. The requester can calculate the network delay. Note: Because the time synchronization of AUTOSAR conforms to 802.1AS, the time synchronization is required to be in p2p mode, that is, time synchronization and network delay are performed independently of each other.

安全时间同步 (Secure Time Synchronization)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  安全时间同步通过为 Follow_Up 报文添加附加的认证信息来实现。这些认证信息以 TLV 格式附加在 Follow_Up 报文的最尾部，位于所有 Sub-TLV 之后。安全认证信息主要包括两个部分：新鲜度值（Freshness Value，FV）和完整性校验值（Integrity Check Value，ICV）。
  在获取 FV 和生成/验证 ICV 的过程中，若获取失败或者验证失败则会跳过处理并报告相应的安全事件。

  Security Time Synchronization is achieved by appending additional authentication information to Follow_Up messages. This authentication information is attached at the very end of Follow_Up messages in TLV format, following all Sub-TLVs. The security authentication information mainly consists of two parts: the Freshness Value (FV) and the Integrity Check Value (ICV). If the FV acquisition fails or the ICV generation/verification fails during the process of obtaining the FV and generating/verifying the ICV, the processing will be skipped, and corresponding security events will be reported.

新鲜度值(Freshness Value)
******************************
  首先，每个 Timebase 都至少配置一个新鲜度值（Freshness Value，FV）。

  First, each Timebase must be configured with at least one Freshness Value (FV).

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
**************************************************
  ICV 指的是密码学函数的计算结果，用于确保能够检测到对消息的未授权修改。该密码学函数可以采用任意一种密码学原语，并结合相应的密码密钥来实现。

  ICV refers to the calculation result of a cryptographic function, used to ensure that unauthorized modifications to the message can be detected. This cryptographic function can employ any cryptographic primitive and be implemented in combination with a corresponding cryptographic key.

  对应于接收端的 ICV 的使用是可选的。为了在多个时间观测单元之间实现较大的灵活性，相关配置会决定如何处理已认证 Sub-TLV 的 ICV。

  The use of ICV on the receiver side is optional. To achieve greater flexibility across multiple time observation units, relevant configurations determine how messages with ICV are processed.

  如果接收端不启用 ICV 校验，则可能仅使用接收到的数值，而不对 ICV 本身进行验证。

  If the receiver does not enable ICV verification, it may only use the received values without verifying the ICV itself.

  如果接收端启用 ICV 选项，则必须考虑一个副作用：由于 Pdelay 消息不包含任何 TLV，因此无法对相关的时间戳进行 ICV 保护。若应用在 Follow_Up 中使用 ICV，同时又采用非静态的 Pdelay，则在计算相应 Time Base 的值时，不可避免地需要将未受保护的 Pdelay 时间值与受 ICV 保护的 Follow_Up 时间值进行混合使用。

  If the receiving end enables the ICV option, a side effect must be considered: Since Pdelay messages do not contain any TLVs, the associated timestamps cannot be protected by ICV. If the application uses ICV in Follow_Up messages while also employing non-static Pdelay, then when calculating the corresponding Time Base value, it is unavoidable to mix the unprotected Pdelay timestamps with the ICV-protected Follow_Up timestamps.

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

时间主节点和时间从节点的动态端口配置(Dynamic Port Configuration for Time Master and Time Slave Nodes)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  在EthTSyn模块中，考虑到时间同步拓扑中需要引入备份时钟源以确保系统的高可用性，引入动态配置端口角色的功能，即时间主节点和时间从节点的角色可以在运行时动态变化。

  In the EthTSyn module, to ensure high system availability by introducing backup clock sources into the time synchronization topology, a dynamic port role configuration function has been implemented. This allows the roles of time master nodes and time slave nodes to change dynamically during runtime.

  备份时钟源在正常情况下处于非活动状态，当主时钟源发生故障或不可用时，备份时钟源可以被激活以接管时间同步的职责。并且网关节点可以根据网络状况动态切换其时间同步角色，以适应不同的网络拓扑和需求。

  Under normal conditions, the backup clock source remains inactive. When the primary clock source fails or becomes unavailable, the backup clock source can be activated to take over the responsibilities of time synchronization. Additionally, gateway nodes can dynamically switch their time synchronization roles based on network conditions to adapt to different network topologies and requirements.

  如当网关节点的接口被配置成DYNAMIC类型时，当主时钟源向外发送SYNC和Follow_Up报文时，接收到同步报文的DYNAMIC端口将作为SLAVE类型接收时间同步报文，其他所有DYNAMIC端口将作为MASTER类型的端口向外发送SYNC和Follow_Up报文。

  For example, when the interface of a gateway node is configured as the DYNAMIC type, and the primary clock source sends out SYNC and Follow_Up messages, the DYNAMIC port that receives the synchronization messages will operate as a SLAVE type to receive time synchronization messages. All other DYNAMIC ports will function as MASTER type ports to forward SYNC and Follow_Up messages outward.

  当主时钟源不可用时，所有变成了SLAVE或者MASTER的DYNAMIC端口将再次变回DYNAMIC类型，等待备份时钟源重新激活DYNAMIC端口以构造新的时间同步拓扑。

  When the primary clock source becomes unavailable, all DYNAMIC ports that have transitioned to SLAVE or MASTER roles will revert to the DYNAMIC type, awaiting re-activation by the backup clock source to establish a new time synchronization topology.

时间记录(Time Recording)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  为时间同步系统能够在运行过程中检测主从节点之间的时间偏差、识别时间同步劣化或异常情况，并从全系统视角判断是否建立了可信的一致时间基准，因此引入Time Validation特性。

  The Time Validation feature is introduced to enable the time synchronization system to detect time deviations between master and slave nodes during operation, identify time synchronization degradation or anomalies, and determine from a system-wide perspective whether a trusted and consistent time base has been established.

  TimeSync 模块需要能够采集时间同步状态信息，并将这些信息提供给应用（即Validator SWC），以支持 Time Validation 功能的实现。Time Slave、Time Master 以及 Time Gateway 会从相应的 TimeSync 模块中收集时间同步过程的相关信息，例如：基于其本地的全局时间实例（通过使用 SyncLocal Time Tuple）、时间同步报文的接收时间戳、时间同步报文中的全局时间信息等，来计算时间偏差和其他相关指标。

  The TimeSync module must be able to collect time synchronization status information and provide this information to the application (i.e., Validator SWC) to support the implementation of the Time Validation function. Time Slave, Time Master, and Time Gateway will collect information related to the time synchronization process from the corresponding TimeSync modules—for example, based on their local global time instances (by using SyncLocal Time Tuple), reception timestamps of time synchronization messages, and global time information within time synchronization messages—to calculate time deviations and other relevant metrics.

  EthTSyn 模块通过 StbM 各个接口将各个阶段的时间同步信息传递到 StbM，涵盖所有报文的收发过程，包括： Master 端向外发送时间同步报文、接收并处理Pdelay报文，Slave 端接收时间同步报文、发送并处理Pdelay报文。

  The CanTSyn module passes time synchronization information from each stage to the StbM through various StbM interfaces.

RateRatio计算(Rate Ratio Calculation)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  时钟速率比（Rate Ratio）是指两个时钟之间的频率关系。通过计算和调整速率比，可以确保从时钟能够以与主时钟相同的速率运行，从而实现更精确的时间同步。

  Clock Rate Ratio refers to the frequency relationship between two clocks. By calculating and adjusting the rate ratio, it ensures that the slave clock can operate at the same rate as the master clock, thereby achieving more precise time synchronization.

  速录比的计算可以根据配置决定是由 StbM 进行计算，还是由 TimeSync 模块进行计算。

  The calculation of the rate ratio can be configured to be performed either by the StbM (Synchronization Time Base Manager) or by the TimeSync module, depending on the system configuration.


偏差 (Deviation)
---------------------------------------------------------
  None
  
.. 有序列表示例

  1.不支持Time measurement with Switches

  Time measurement with Switches is not supported

  功能还未开发，将在后续版本中进行开发。

  The function has not been developed yet and will be developed in subsequent versions.



扩展 (Extension)
---------------------------------------------------------
  None


集成 (Integration)
=================================

文件列表 (File List)
---------------------------------------------------------

静态文件 (Static Files)
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

动态文件 (Dynamic Files)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - 文件(File)
     - 描述(Description)

   * - EthTSyn_MemMap.h
     - 定义EthTSyn模块的内存映射(Defines the Memory mapping of the EthTSyn module)

   * - EthTSyn_Cfg.h
     - 定义EthTSyn模块PC配置的宏定义(Defines the macro definitions for PC configuration of the EthTSyn module)

   * - EthTSyn_Cfg.c
     - 定义EthTSyn模块PC配置的结构体参数(Defines the structure parameters for PC configuration of the EthTSyn module)

   * - EthTSyn_PBcfg.h
     - 定义EthTSyn模块PB配置的宏定义(Defines the macro definitions for PB configuration of the EthTSyn module)

   * - EthTSyn_PBcfg.c
     - 定义EthTSyn模块PB配置的结构体参数(Defines the structure parameters for PB configuration of the EthTSyn module)


错误处理 (Error Handling)
---------------------------------------------------------

开发错误 (Development Errors)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. list-table::
   :widths: 20 10 30
   :header-rows: 1

   * - Error code
     - Value[hex]
     - Description

   * - ETHTSYN_E_UNINIT
     - 0x20
     - API service called before module initialization

   * - ETHTSYN_E_INIT_FAILED
     - 0x21
     - Module initialization failed

   * - ETHTSYN_E_CTRL_IDX
     - 0x22
     - Invalid controller index parameter provided

   * - ETHTSYN_E_PARAM_POINTER
     - 0x23
     - NULL pointer parameter where valid pointer expected

   * - ETHTSYN_E_PARAM
     - 0x24
     - Invalid parameter value

   * - ETHTSYN_E_ALREADY_INITIALIZED
     - 0x25
     - Module initialization attempted when already initialized

   * - ETHTSYN_E_INVALID_PARTITION_CONTEXT
     - 0x26
     - Service called from wrong partition context

   * - ETHTSYN_E_UNRECOGNIZED_TLV
     - 0x27
     - Received TLV format not recognized

产品错误 (Product Errors)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  None

运行时错误 (Runtime Errors)
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

   * - ETHTSYN_E_FRESHNESSFAILURE
     - 0x03
     - No FV available from the FVM

接口描述 (Interface Description)
=================================

.. 目前能够自动生成的有类型定义，普通函数，回调函数。
.. 有些模块的API来自多个头文件，需要自行裁剪合并
.. 引用接口描述。来自于code->doxygen->xml->rst
.. 引用接口描述。 From code->doxygen->xml->rst
.. include:: EthTSyn_Types_h_api.rst
.. include:: EthTSyn_h_api.rst

配置函数 (Configuration function)
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



依赖的服务 (Applicable Services)
---------------------------------------------------------------------------

强制接口 (Compulsory interface)
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

可选接口 (Optional Interface)
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


配置 (Configuration)
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

  .. figure:: /_static/参考手册(Module_Reference_Manual)/EthTSyn/EthTSyn_hardwaretimestamp1.png
    :alt: 通用配置的图片 (Picture of General Configuration)
    :align: center

  通用配置的图片 (Picture of General Configuration)

  1. 如上图所示，在EthTSynGeneral中，开启支持硬件时间戳，即勾选EthTSynHardWareTimestampSupport。其他公共配置项，比如周期。

  As shown in the figure above, in EthTSynGeneral, enable support for hardware timestamp, that is, check EthTSynHardWareTimestampSupport. Other common configuration items, such as period.

  .. figure:: /_static/参考手册(Module_Reference_Manual)/EthTSyn/EthTSyn_hardwaretimestamp2.png
    :alt: domain配置的图片 (Picture of Domain Configuration)
    :align: center

  domain配置的图片 (Picture of Domain Configuration)

  .. figure:: /_static/参考手册(Module_Reference_Manual)/EthTSyn/EthTSyn_StbmConfiguration1.png
    :alt: StbM时钟源配置的图片 (Picture of StbM Clock Source Configuration)
    :align: center

  StbM时钟源配置的图片 (Picture of StbM Clock Source Configuration)

  2. 在EthTSynGlobalTimeDomain中，配置时间域的相关参数，比如时间域的ID，关联的时间基。

  In EthTSynGlobalTimeDomain, configure the relevant parameters of the time domain, such as the ID of the time domain and the associated time base.

.. attention::

  一个时间域可以配置多个Port，EthTSynGlobalTimeHardware是指当前时间域关联的StbM时间基所配的时钟源来自哪个以太网Port。EthTSynGlobalTimeHardware当且仅当该时间域所配的时间基(EthTSynSchronizedTimeBaseRef)下的StbMLocalTimeClock关联的为以太网时钟时，才会生效。

  A time domain can be configured with multiple Ports. EthTSynGlobalTimeHardware refers to which Ethernet Port the clock source configured for the StbM time base associated with the current time domain comes from. EthTSynGlobalTimeHardware takes effect if and only if the time base (EthTSynSchronizedTimeBaseRef) configured in the time domain is associated with the Ethernet clock in StbMLocalTimeClock.

  .. figure:: /_static/参考手册(Module_Reference_Manual)/EthTSyn/EthTSyn_hardwaretimestamp3.png
    :alt: port配置的图片 (Picture of Port Configuration)
    :align: center

  port配置的图片 (Picture of Port Configuration)

  3. 配置时间域下端口Port，比如时间同步角色EthTSynGlobalTimePortRole，SYNC和Follow-Up报文发送间隔EthTSynGlobalTimeDebounceTime。

  Configure the Port under the time domain, such as the time synchronization role EthTSynGlobalTimePortRole, the sending interval of SYNC and Follow-Up messages EthTSynGlobalTimeDebounceTime, and the EthIfController associated with the Port.

  .. figure:: /_static/参考手册(Module_Reference_Manual)/EthTSyn/EthTSyn_hardwaretimestamp4.png
    :alt: Master的配置的图片 (Picture of Master Configuration)
    :align: center

  Master的配置的图片 (Picture of Master Configuration)

  4. 配置时间域下主时间节点的相关参数，比如立即同步恢复到周期同步的恢复时间EthTSynCyclicMsgResumeTime，报文发送周EthTSynGlobalTimeTxPeriod等。

  Configure the relevant parameters of the master time node under the time domain, such as the recovery time from immediate synchronization to periodic synchronization EthTSynCyclicMsgResumeTime, the message sending period EthTSynGlobalTimeTxPeriod, etc.

  .. figure:: /_static/参考手册(Module_Reference_Manual)/EthTSyn/EthTSyn_EthIf1.png
    :alt: EthIf配置1 (EthIf Configuration 1)
    :align: center

  EthIf配置1 (EthIf Configuration 1)

  除了以上配置，为了支持硬件时间戳，还需要将Mcal的硬件时间戳功能打开。同时将硬件时间戳相关的接口注册到EthIf层，如上图所示。并且要将EthTSyn的连接状态回调注册到EthIf层，如下图所示。

  In addition to the above configuration, in order to support hardware timestamp, the hardware timestamp function of Mcal also needs to be enabled. At the same time, register the interfaces related to hardware timestamp to the EthIf layer, as shown in the figure above. And register the connection status callback of EthTSyn to the EthIf layer, as shown in the figure below.

  .. figure:: /_static/参考手册(Module_Reference_Manual)/EthTSyn/EthTSyn_EthIf2.png
    :alt: EthIf配置2 (EthIf Configuration 2)
    :align: center

  EthIf配置2 (EthIf Configuration 2)


.. attention::


  另外，如果需要激活时间同步Master，需要首先在应用层通过调用StbM设置时间的接口StbM_SetGlobalTime设置本时间域的时间基的全局时间，调用EthTSyn_SetTransmissionMode激活传输状态。

  In addition, if you need to activate the time synchronization Master, you first need to call the interface StbM_SetGlobalTime of StbM in the application layer to set the global time of the time base in this time domain, and call EthTSyn_SetTransmissionMode to activate the transmission state.


完整性校验值发送端配置描述
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  1. 为 EthTSynPortConfig 添加子容器 EthTSynGlobalTimeTxIcvGeneration 用于配置完整性校验值发送端的相关参数：

  .. figure:: /_static/参考手册(Module_Reference_Manual)/EthTSyn/EthTSynGlobalTimeTxIcvGeneration.png
    :alt: EthTSyn发送端ICV配置
    :align: center

  EthTSyn发送端ICV配置

  2. 其中 EthTSynIcvGenerationFvIdRef 需要引用 StbMFreshnessValue 的配置：

  .. figure:: /_static/参考手册(Module_Reference_Manual)/EthTSyn/StbMFreshnessValue.png
    :alt: EthTSyn引用 FV 配置
    :align: center

  EthTSyn引用 FV 配置

  3. 其中 EthTSynIcvGenerationJobRef 需要引用 CsmJob 的配置：

  .. figure:: /_static/参考手册(Module_Reference_Manual)/EthTSyn/CsmJobs.png
    :alt: EthTSyn引用 CsmJob 配置
    :align: center

  EthTSyn引用 CsmJob 配置

完整性校验值接收端配置描述
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  1. 为 EthTSynPortConfig 添加子容器 EthTSynGlobalTimeRxIcvVerification 用于配置完整性校验值接收端的相关参数：EthTSynRxAuthenticationBuildAttempts当解析失败时仍可重新尝试构建认证TLV的次数，而EthTSynIcvVerificationAttempts仅在每次 Csm 获取返回 BUSSY 等非失败性错误时支持重新校验 ICV。

  .. figure:: /_static/参考手册(Module_Reference_Manual)/EthTSyn/EthTSynGlobalTimeRxIcvVerification.png
    :alt: EthTSyn接收端ICV配置
    :align: center

  EthTSyn接收端ICV配置

  2. 其中 EthTSynIcvGenerationFvIdRef 需要引用 StbMFreshnessValue 的配置同于发送端
  3. 其中 EthTSynIcvGenerationJobRef 需要引用 CsmJob 的配置同于发送端


DYNAMIC端口配置描述
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  1. EthTSynGlobalTimePortRole 配置为 DYNAMIC 类型：

  .. figure:: /_static/参考手册(Module_Reference_Manual)/EthTSyn/EthTSynGlobalTimePortRole_DYNAMIC.png
    :alt: EthTSyn DYNAMIC端口配置
    :align: center

  EthTSyn DYNAMIC端口配置1

  2. EthTSynPortRole 需要同时配置 EthTSynGlobalTimeMaster 和 EthTSynGlobalTimeSlave 两种角色需要的参数：

  .. figure:: /_static/参考手册(Module_Reference_Manual)/EthTSyn/EthTSynPortRole_DYNAMIC.png
    :alt: EthTSyn DYNAMIC端口配置
    :align: center

  EthTSyn DYNAMIC端口配置2

时间记录配置描述
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  1. EthTSyn 需要使能 EthTSynTimeValidationSupport 和 EthTSynEnableTimeValidation 两个配置选项：

  .. figure:: /_static/参考手册(Module_Reference_Manual)/EthTSyn/EthTSynEnableTimeValidation.png
    :alt: EthTSynEnableTimeValidation配置
    :align: center

  EthTSynEnableTimeValidation配置

  2. StbM 需要为 Timebase 配置 StbMTimeValidation:

  .. figure:: /_static/参考手册(Module_Reference_Manual)/EthTSyn/StbMTimeRecording.png
    :alt: StbMTimeRecording配置
    :align: center

  StbMTimeRecording配置

RateRatio计算配置描述
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  1. EthTSyn 需要使能 EthTSynRateRatioEnable 配置选项：

  .. figure:: /_static/参考手册(Module_Reference_Manual)/EthTSyn/EthTSynRateRatioEnable.png
    :alt: EthTSynRateRatioEnable配置
    :align: center

  RateRatio配置1

  2. StbM 需要为 Timebase 配置 StbMRateRatioSource 选择 RateRatio 的计算来源：

  .. figure:: /_static/参考手册(Module_Reference_Manual)/EthTSyn/StbMRateSource.png
    :alt: StbMRateSource配置
    :align: center

  RateRatio配置2
