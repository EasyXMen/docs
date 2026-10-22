====================
EthIf
====================




文档信息 Document Information
==================================================================

版本历史 Version History
------------------------------------------------------------------------------------------------------------------

.. list-table::
   :widths: 10 10 5 5 30
   :header-rows: 1

   * - 日期(Date)
     - 作者(Author)
     - 版本(Version)
     - 状态(Status)
     - 说明(Description)

   * - 2025/04/03
     - jianyu.yang
     - V0.1
     - 发布(Release)
     - 首次发布(First release)

   * - 2025/04/04
     - jianyu.yang
     - V1.0
     - 发布(Release)
     - 正式发布(Official release)

   * - 2026/06/20
     - tong.zhao
     - V1.1
     - 修改(Modify)
     - 补充功能描述章节缺失功能(ETH控制器设定/发送/接收)，配置章节补充各容器必须配置参数列表(Supplement missing features in Functional Description (ETH Controller Setting/Transmission/Reception), and add required parameter list for each container in Configuration)


参考文档 References
------------------------------------------------------------------------------------------------------------------

.. list-table::
   :widths: 5 10 35 10
   :header-rows: 1

   * - 编号(Number)
     - 分类(Classification)
     - 标题(Title)
     - 版本(Version)
   * - 1
     - Autosar
     - AUTOSAR_CP_SWS_EthernetInterface.pdf
     - R23-11
   * - 2
     - Autosar
     - AUTOSAR_CP_SWS_EthernetDriver.pdf
     - R23-11
   * - 3
     - Autosar
     - AUTOSAR_CP_SWS_EthernetTransceiverDriver.pdf
     - R23-11
   * - 4
     - Autosar
     - AUTOSAR_CP_SWS_EthernetSwitchDriver.pdf
     - R23-11


术语与简写 Terms and Abbreviations
==================================================================


术语 Terms
------------------------------------------------------------------------------------------------------------------


.. list-table::
   :widths: 10 40
   :header-rows: 1

   * - 术语(Terms)
     - 解释(Explanation)

   * - Eth
     - 以太网控制器驱动程序(AUTOSAR BSW 模块)(Ethernet Controller Driver (AUTOSAR BSW Module))

   * - EthIf
     - 以太网接口(AUTOSAR BSW 模块)(Ethernet Interface (AUTOSAR BSW Module))

   * - EthSM
     - 以太网状态管理器(AUTOSAR BSW 模块)(Ethernet State Manager (AUTOSAR BSW Module))

   * - EthTrcv
     - 以太网收发器驱动程序(AUTOSAR BSW 模块)(Ethernet Transceiver Driver (AUTOSAR BSW Module))

   * - CBR
     - 信道繁忙率(Channel Busy Ratio)

   * - CIT
     - 信道空闲时间(Channel Idle Time)

   * - CV2x
     - 蜂窝车联网直连通信驱动程序(AUTOSAR BSW 模块)(Cellular Vehicle-to-Everything Driver (AUTOSAR BSW Module))

   * - OA TC10
     - OPEN Alliance TC10 规范(OPEN Alliance TC10 Specification)

简写 Abbreviations
------------------------------------------------------------------------------------------------------------------

.. list-table::
   :widths: 10 20 30
   :header-rows: 1


   * - 简写(Abbreviation)
     - 全称(Full name)
     - 解释(Explanation)

   * - IP
     - Internet Protocol
     - 网际互连协议

   * - MCG
     - Module Configuration Generator
     - 模块配置与生成器

   * - MII
     - Media Independent Interface (standardized Interface provided by Ethernet controllers to access Ethernet transceivers)
     - 媒介独立接口

   * - RSSI
     - Received Signal Strength Indicator
     - 接收信号强度指示

   * - TCP
     - Transmission Control Protocol
     - 传输控制协议

   * - TCP/IP Stack
     - Ethernet communication stack
     - 传输控制与网际互联协议栈

   * - VLAN
     - Virtual Local Area Network
     - 虚拟局域网

   * - WEth
     - Wireless Ethernet Driver
     - 无线以太网驱动

   * - WEthTrcv
     - Wireless Ethernet Transceiver Driver
     - 无线以太网收发器驱动


简介 Introduction
==================================================================

.. figure:: /_static/参考手册(Module_Reference_Manual)/EthIf/EthIf.png
   :alt: EthIf模块层次图 (EthIf Module Layer Diagram)
   :name: EthIf_fig_archLayer
   :align: center

   EthIf模块层次图 (EthIf Module Layer Diagram)


EthIf通过与遵守AUTOSAR规范的以太网Transceiver，以太网Controller以及以太网switch的驱动所提供的接口密切配合，可为EthIf的上层提供独立于这些以太网硬件的独立接口，从而可以支持多种不同以太网控制器和收发器。

By closely cooperating with the interfaces provided by the Ethernet Transceiver, Ethernet Controller, and Ethernet Switch drivers that comply with the AUTOSAR specification, EthIf can provide interfaces independent of these Ethernet hardware for the upper layer of EthIf, thus supporting a variety of different Ethernet controllers and transceivers.

EthIf提供的这些接口，按功能可以大体分为模式控制相关的接口、时间同步相关的接口、数据接收发送相关的接口。另外，EthIf还存在的初始化或周期任务接口。

These interfaces provided by EthIf can be roughly divided into mode control-related interfaces, time synchronization-related interfaces, and data transmission/reception-related interfaces by function. In addition, EthIf also has initialization or periodic task interfaces.

.. figure:: /_static/参考手册(Module_Reference_Manual)/EthIf/EthIf_layer.png
   :alt: EthIf模块交互图 (EthIf Module Interaction Diagram)
   :name: EthIf_fig_arch
   :align: center

   EthIf模块交互图 (EthIf Module Interaction Diagram)


如图 :ref:`EthIf_fig_arch`  所示，EthIf向下通过统一的交互接口与以太网控制器，以太网收发器以及以太网交互机等这些以太网硬件间进行交互，向上它将这些交互得到的信息再传递以太网通讯栈或者其他相关模块，以及将这些上层模块的请求传递到对应的以太网硬件上，使得这些上层模块可以独立于以太网硬件而访问以太网通讯资源。

As shown in Figure :ref:`EthIf_fig_arch`, EthIf interacts downward with Ethernet hardware such as Ethernet Controllers, Ethernet Transceivers, and Ethernet Switches through a unified interaction interface. Upward, it transmits the information obtained from these interactions to the Ethernet communication stack or other related modules, and also transmits the requests from these upper-layer modules to the corresponding Ethernet hardware, enabling these upper-layer modules to access Ethernet communication resources independently of the Ethernet hardware.



功能描述 Functional Description
==================================================================


公共特性(Public Features)
------------------------------------------------------

多核多分区功能(Multi-core and Multi-partition Features)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- EthIf模块支持多核与多分区部署,具体的分区信息由EthIfPhysController配置项EthIfCtrlPartitionRef决定。

  The EthIf supports multi-core and multi-partition deployment, with specific partition information determined by the configuration parameter EthIfCtrlPartitionRef of EthIfPhysController.


.. only:: doc_pbs

   PBS功能(PBS Features)
   ~~~~~~~~~~~~~~~~~~~~~~~~
   - 模块支持PBS
          
     The module supports PBS.

   - EthIfConfig中的子容器支持属性变体
        
   - The sub-containers in EthIfConfig support attribute variants

   - EthIf模块不支持数量变体

   - The EthIf module does not support quantity variants

   - 不同变体EthIf使用的EcuC的Partitions需要一致

   - The EcuC Partitions used by EthIf in different variants must be consistent


Memmap功能(Memmap Features)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
memmap文件是动态的。包含这些名称的标签段 ETHIF_CODE、ETHIF_CODE_FAST、ETHIF_VAR_INIT_PTR、ETHIF_CONST_PTR、ETHIF_CONFIG_DATA_8、ETHIF_CONFIG_DATA_PTR、ETHIF_CONFIG_DATA_UNSPECIFIED、ETHIF_VAR_INIT_GLOBAL_8、ETHIF_VAR_CLEARED_GLOBAL_UNSPECIFIED、ETHIF_VAR_CLEARED_GLOBAL_BOOLEAN、ETHIF_VAR_CLEARED_PTR。

The memmap file is dynamic. There are ETHIF_CODE、ETHIF_CODE_FAST、ETHIF_VAR_INIT_PTR、ETHIF_CONST_PTR、ETHIF_CONFIG_DATA_8、ETHIF_CONFIG_DATA_PTR、ETHIF_CONFIG_DATA_UNSPECIFIED、ETHIF_VAR_INIT_GLOBAL_8、ETHIF_VAR_CLEARED_GLOBAL_UNSPECIFIED、ETHIF_VAR_CLEARED_GLOBAL_BOOLEAN、ETHIF_VAR_CLEARED_PTR. 


独占区功能(Exclusive Area Features)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
None.


模块特性(Module Features)
----------------------------


Vlan的支持 VLAN Support
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

EthIf负责对VLAN报文的解/加Tag操作，当接收时，通过EthIf传递给上层的以太网报文将在EthIf中提取出VLAN头，并把剩余的数据传递给上层模块。当上层模块需要向下传输报文时，在EthIf中添加VLAN头，并通过合适的Eth通道发送出去。

EthIf is responsible for the VLAN tag removal/insertion operations for VLAN frames. When receiving a frame, the Ethernet frame passed by EthIf to the upper layer will have its VLAN header extracted in EthIf, and the remaining data will be transmitted to the upper-layer module. When the upper-layer module needs to transmit a frame downward, a VLAN header will be added to the frame in EthIf, and the frame will be sent out through the appropriate Eth channel.


ETH控制器设定 ETH Controller Setting
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

EthIf通过EthIf_SetControllerMode接口对Ethernet Controller的工作模式进行设定，支持的模式包括ETH_MODE_DOWN(下电模式)与ETH_MODE_ACTIVE(活动模式)。当上层模块(例如EthSM)请求将以太网控制器上线或下线时，通过该接口将模式切换请求传递给底层Eth驱动。EthIf同时提供EthIf_GetControllerMode接口用于查询控制器当前的工作模式。

EthIf sets the operating mode of the Ethernet Controller through the EthIf_SetControllerMode interface. The supported modes include ETH_MODE_DOWN (power-down mode) and ETH_MODE_ACTIVE (active mode). When an upper-layer module (e.g., EthSM) requests the Ethernet controller to go online or offline, the mode switch request is passed to the underlying Eth driver through this interface. EthIf also provides the EthIf_GetControllerMode interface to query the current operating mode of the controller.

控制器模式的设定与EthIfPhysController配置容器相关联，EthIf依据配置的CtrlIdx将模式请求路由到对应的物理以太网控制器。在多控制器场景下，每个EthIfController通过EthIfPhysControllerRef关联到一个EthIfPhysController，从而实现对不同物理控制器的独立模式控制。

The controller mode setting is associated with the EthIfPhysController configuration container. EthIf routes the mode request to the corresponding physical Ethernet controller based on the configured CtrlIdx. In multi-controller scenarios, each EthIfController is associated with an EthIfPhysController through EthIfPhysControllerRef, thereby enabling independent mode control of different physical controllers.


ETH控制器发送 ETH Controller Transmission
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

EthIf提供以太网报文的发送功能。发送流程为：上层模块先通过EthIf_ProvideTxBuffer获取发送缓冲区，填充报文数据后再通过EthIf_Transmit触发发送。EthIf在发送过程中负责VLAN Tag的添加(当EthIfController配置了EthIfVlanId时)，并依据EthIfPhysController配置将报文路由到对应的物理以太网控制器与发送通道。

EthIf provides the Ethernet frame transmission function. The transmission flow is as follows: the upper-layer module first obtains a transmit buffer through EthIf_ProvideTxBuffer, fills in the frame data, and then triggers the transmission through EthIf_Transmit. During transmission, EthIf is responsible for adding the VLAN Tag (when EthIfVlanId is configured for the EthIfController), and routes the frame to the corresponding physical Ethernet controller and transmit channel based on the EthIfPhysController configuration.

当底层Eth驱动完成报文发送后，会调用EthIf_TxConfirmation通知EthIf。EthIf通过EthIfFrameOwnerConfig匹配确定报文归属的上层模块(EthIfOwner)，再调用EthIfTxConfirmationConfig中对应的回调函数，将发送完成确认报告给上层模块。具体的匹配机制与配置要求详见 :ref:`EthIfFrameOwnerConfig匹配机制 <EthIfFrameOwnerConfig_matching>`。

When the underlying Eth driver completes the frame transmission, it calls EthIf_TxConfirmation to notify EthIf. EthIf determines the owning upper-layer module (EthIfOwner) through EthIfFrameOwnerConfig matching, and then calls the corresponding callback function in EthIfTxConfirmationConfig to report the transmission confirmation to the upper-layer module. For details on the matching mechanism and configuration requirements, see :ref:`EthIfFrameOwnerConfig Matching Mechanism <EthIfFrameOwnerConfig_matching>`.


ETH控制器接收 ETH Controller Reception
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

EthIf提供以太网报文的接收功能。当底层Eth驱动接收到以太网报文时，通过EthIf_RxIndication回调通知EthIf。EthIf在接收路径上负责VLAN Tag的提取(去除VLAN头)，并将剩余数据向上传递。

EthIf provides the Ethernet frame reception function. When the underlying Eth driver receives an Ethernet frame, it notifies EthIf through the EthIf_RxIndication callback. EthIf is responsible for extracting the VLAN Tag (removing the VLAN header) on the reception path, and passes the remaining data upward.

EthIf依据EthIfFrameOwnerConfig中的EthIfFrameType对收到的报文进行匹配，将不同类型的以太网报文分发到对应的上层模块进行处理。具体的匹配机制与配置要求详见 :ref:`EthIfFrameOwnerConfig匹配机制 <EthIfFrameOwnerConfig_matching>`。

EthIf matches received frames based on EthIfFrameType in EthIfFrameOwnerConfig, distributing different types of Ethernet frames to the corresponding upper-layer modules for processing. For details on the matching mechanism and configuration requirements, see :ref:`EthIfFrameOwnerConfig Matching Mechanism <EthIfFrameOwnerConfig_matching>`.


偏差 Deviation
------------------------------------------------------------------------------------------------------------------

**配置**

**Configuration**

1.EthIfClkUnit: 位于EthIfPhysController下的EthIfClkUnit配置项因为没有相应版本的Eth驱动进行验证，所以本配置项目前不支持。

1.EthIfClkUnit: The EthIfClkUnit configuration item under EthIfPhysController is not currently supported because there is no corresponding version of the Eth driver for verification.

2.EthIfPhysCtrlRxMainFunctionIngressQueueProcessing: 位于EthIfPhysController下的EthIfPhysCtrlRxMainFunctionIngressQueueProcessing配置项因为没有相应版本的Eth驱动进行验证，所以本配置项目前不支持。

2.EthIfPhysCtrlRxMainFunctionIngressQueueProcessing: The EthIfPhysCtrlRxMainFunctionIngressQueueProcessing configuration item under EthIfPhysController is not currently supported because there is no corresponding version of the Eth driver for verification.

3.EthIfFrameOwnerPdu: 位于EthIfFrameOwnerConfig下的EthIfFrameOwnerPdu配置项因为它相关功能的实现需要依赖L-SDU(该模块本阶段未实现)，所以该配置及其子配置项目前不支持。

3.EthIfFrameOwnerPdu: The EthIfFrameOwnerPdu configuration item under EthIfFrameOwnerConfig is not currently supported, along with its sub-configuration items, because the implementation of its related functions depends on L-SDU (this module is not implemented in this phase).

**接口**

**Interfaces**

1.EthIf_MainFunctionRx_<IngressQueueProcessing ShortName>：本接口不支持因为需求为Draft状态，且未有对应版本的Eth驱动进行验证。

1.EthIf_MainFunctionRx_<IngressQueueProcessing ShortName>: This interface is not supported because the requirement is in Draft status and there is no corresponding version of the Eth driver for verification.

2.EthIf_ReleaseRxBuffer：本接口不支持因为配置中不支持EthIfFrameOwnerPdu，即以PDU形式的通讯方式不支持。

2.EthIf_ReleaseRxBuffer: This interface is not supported because EthIfFrameOwnerPdu is not supported in the configuration, i.e., the communication mode in the form of PDU is not supported.

3.无线以太网相关的接口现阶段尚未开发。

3.Interfaces related to Wireless Ethernet have not been developed at this stage.

4.蜂窝网络的V2X相关接口现阶段尚未开发，且需求为Draft状态。

4.Interfaces related to Cellular V2X have not been developed at this stage, and the requirement is in Draft status.

5.MACsec相关的接口现阶段尚未开发，且需求为Draft状态。

5.Interfaces related to MACsec have not been developed at this stage, and the requirement is in Draft status.

6.Firewall相关的接口现阶段尚未开发，且需求为Draft状态。

6.Interfaces related to Firewall have not been developed at this stage, and the requirement is in Draft status.

扩展 Extension
------------------------------------------------------------------------------------------------------------------
None


集成 Integration
==================================================================

文件列表 File List
------------------------------------------------------------------------------------------------------------------

静态文件 Static Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - 文件(File)
     - 描述(Description)

   * - EthIf.h
     - 实现EthIf模块对外的函数接口的声明，以及配置文件中全局变量类型的声明(Implements the declaration of the EthIf module's external function interfaces and the declaration of global variable types in the configuration file)

   * - EthIf_Cbk.h
     - 实现EthIf模块回调函数接口的声明(Implements the declaration of the EthIf module's callback function interfaces)

   * - EthIf_Type.h
     - EthIf模块宏定义及数据类型定义(Defines macros and data types for the EthIf module)

   * - EthIf.c
     - EthIf模块源文件，包含了API函数的实现(Source file of the EthIf module, containing the implementation of API functions)

动态文件 Dynamic Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - 文件(File)
     - 描述(Description)

   * - EthIf_Cfg.h
     - 定义EthIf模块内部结构体以及相应宏常量(Defines the internal structures and corresponding macro constants of the EthIf module)

   * - EthIf_Cfg.c
     - 定义EthIf模块内部描述各个以太网硬件资源(例如controller,transceiver以及switch与相关的switch port等)状态的变量(Defines variables in the EthIf module that describe the status of various Ethernet hardware resources (such as controllers, transceivers, switches, and related switch ports))

   * - EthIf_PBcfg.c
     - 定义EthIf模块PB配置的结构体参数(Defines the structure parameters for the PB configuration of the EthIf module)

   * - EthIf_MemMap.h
     - 实现EthIf模块内存布局(Implements the memory mapping of the EthIf module)


错误处理 Error Handling
------------------------------------------------------------------------------------------------------------------

开发错误 Development Errors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. list-table::
   :widths: 20 10 30
   :header-rows: 1

   * - Error code
     - Value[hex]
     - Description

   * - ETHIF_E_INV_CTRL_IDX
     - 0x01
     - API service called with invalid controller index

   * - ETHIF_E_INV_TRCV_IDX
     - 0x02
     - API service called with invalid transceiver index

   * - ETHIF_E_INV_SWT_IDX
     - 0x03
     - API service called with invalid switch index

   * - ETHIF_E_INV_PORT_GROUP_IDX
     - 0x04
     - API service called with invalid port group index

   * - ETHIF_E_UNINIT
     - 0x05
     - API service called when EthIf module was not initialized

   * - ETHIF_E_PARAM_POINTER
     - 0x06
     - API service called with invalid pointer in parameter list

   * - ETHIF_E_INV_PARAM
     - 0x07
     - API service called with invalid parameter

   * - ETHIF_E_INIT_FAILED
     - 0x08
     - EthIf_Init called with an invalid configuration pointer

   * - ETHIF_E_INV_PORT_IDX
     - 0x09
     - Invalid port index

产品错误 Product Errors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
None

运行时错误 Runtime Errors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. list-table::
   :widths: 20 10 30
   :header-rows: 1

   * - Error code
     - Value[hex]
     - Description

   * - ETHIF_E_PDU_STATE_TRANSITION_FAILED
     - 0x01
     - A PDU is requested to be used while it is already in use or requested to be available while it is already available

接口描述 Interface Description
==================================================================

.. include:: EthIf_h_api.rst
.. include:: EthIf_Cbk_h_api.rst
.. include:: EthIf_Types_h_api.rst

配置 Configuration
==================================================================


OverView
--------------------------------------------
如下图所示EthIfConfigSet与EthIfGeneral页面上的内容是按照AUTOSAR的规范进行开发设置的，另外的EthTrcv_DriverApiConfigSet，Eth_DriverApiConfigSet与EthSwt_DriverApiConfigSet分别用于配置Ethernet Transceiver，Ethernet Driver与Ethnernet Switch相关的驱动的API(后续称这三个页面为驱动具体名称配置页面)。

As shown in the figure below, the contents on the EthIfConfigSet and EthIfGeneral pages are developed and set in accordance with AUTOSAR specifications. In addition, EthTrcv_DriverApiConfigSet, Eth_DriverApiConfigSet, and EthSwt_DriverApiConfigSet are used to configure the APIs of drivers related to Ethernet Transceiver, Ethernet Driver, and Ethernet Switch respectively (these three pages are referred to as "Driver-Specific Name Configuration Pages" hereinafter).

.. figure:: /_static/参考手册(Module_Reference_Manual)/EthIf/EthIf_ConfigOverview.png
   :alt: EthIf模块配置界面概览 (EthIf Module Configuration Interface Overview)
   :name: EthIf_overview_arch
   :align: center

   EthIf模块配置界面概览 (EthIf Module Configuration Interface Overview)

驱动具体名称的配置页面与EthIfGeneral页面的内容基本可以按照字面意思进行配置，下面将着重说一下EthIfConfigSet中的容器的配置。

The contents of the Driver-Specific Name Configuration Pages and the EthIfGeneral page can basically be configured according to their literal meanings. The following will focus on the configuration of the containers in EthIfConfigSet.

EthIfGeneral容器中必须配置的关键参数如下：

The key parameters that must be configured in the EthIfGeneral container are as follows:

.. list-table::
   :widths: 25 10 65
   :header-rows: 1

   * - 参数(Parameter)
     - 是否必须(Required)
     - 说明(Description)

   * - EthIfMainFunctionPeriod
     - 是(Yes)
     - EthIf主函数周期，单位秒(EthIf MainFunction period in seconds)

   * - EthIfMaxTrcvsTotal
     - 是(Yes)
     - 收发器总数上限(1~255)(Maximum total number of transceivers, 1~255)

   * - EthIfDevErrorDetect
     - 是(Yes)
     - 开发错误检测开关(Development error detection switch)

   * - EthIfEnableRxInterrupt
     - 是(Yes)
     - 接收中断使能(Enable Rx interrupt)

   * - EthIfEnableTxInterrupt
     - 是(Yes)
     - 发送中断使能(Enable Tx interrupt)

   * - EthIfTrcvLinkStateChgMainReload
     - 是(Yes)
     - 收发器链路状态变化检查频率(1~255)(Transceiver link state change check frequency, 1~255)

   * - EthDriverAutosarVersion
     - 是(Yes)
     - Eth驱动AUTOSAR版本(Eth driver AUTOSAR version)


EthIfConfigSet中的容器 Containers in EthIfConfigSet
--------------------------------------------------------------------------------------------------------------------------------------------------------------------


容器EthIfPhysController Container EthIfPhysController
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

这个容器主要是用于EthIf层抽象的EthIfPhysController关联Ethernet Driver(后续也可以是WEthernet与CanXL)的物理以太网控制器。在多分区的工程中这里还需要配置EthIfCtrlPartitionRef。

This container is mainly used for the EthIfPhysController abstracted by the EthIf layer to associate the physical Ethernet Controller of the Ethernet Driver (which can also be WEthernet and CanXL hereinafter). In a multi-partition project, EthIfCtrlPartitionRef also needs to be configured here.

.. figure:: /_static/参考手册(Module_Reference_Manual)/EthIf/EthIf_PhyController.png
   :alt: EthIfPhysController配置界面 (EthIfPhysController Configuration Interface)
   :name: EthIfPhysController_config
   :align: center

   EthIfPhysController配置界面 (EthIfPhysController Configuration Interface)

此外，EthIfPhysController几乎只被EthIf模块内部使用，而EthIf外的模块访问以太网硬件通过关联EthIfController来实现。

In addition, EthIfPhysController is almost only used internally by the EthIf module, while modules outside EthIf access Ethernet hardware through associating EthIfController.

EthIfPhysController容器中必须配置的参数如下：

The parameters that must be configured in the EthIfPhysController container are as follows:

.. list-table::
   :widths: 25 10 65
   :header-rows: 1

   * - 参数(Parameter)
     - 是否必须(Required)
     - 说明(Description)

   * - EthIfEthCtrlRef
     - 是(Yes)
     - 引用下层Eth驱动中的以太网控制器配置(References the Ethernet controller configuration in the lower-layer Eth driver)

   * - EthIfPhysControllerIdx
     - 是(Yes)
     - 物理控制器索引，用于EthIf内部索引管理(Physical controller index for internal index management of EthIf)

   * - EthIfCtrlPartitionRef
     - 否(多分区时必须)(No, required for multi-partition)
     - 引用EcuC分区，多分区部署时必须配置(References the EcuC partition, must be configured for multi-partition deployment)


容器EthIfController Container EthIfController
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
这里主要用于配置EthIf模块向上层抽象出的EthIfController，配置界面上提供了不少的属性，其中EthIfVlanId比较重要。

This is mainly used to configure the EthIfController abstracted by the EthIf module for the upper layer. The configuration interface provides many attributes, among which EthIfVlanId is relatively important.

.. figure:: /_static/参考手册(Module_Reference_Manual)/EthIf/EthIf_Controller.png
   :alt: EthIfController配置界面 (EthIfController Configuration Interface)
   :name: EthIfController_config
   :align: center

   EthIfController配置界面 (EthIfController Configuration Interface)

EthIfController容器中必须配置的参数如下：

The parameters that must be configured in the EthIfController container are as follows:

.. list-table::
   :widths: 25 10 65
   :header-rows: 1

   * - 参数(Parameter)
     - 是否必须(Required)
     - 说明(Description)

   * - EthIfCtrlIdx
     - 是(Yes)
     - 控制器索引，上层模块通过该索引访问以太网硬件(Controller index, upper-layer modules access Ethernet hardware through this index)

   * - EthIfPhysControllerRef
     - 是(Yes)
     - 引用EthIfPhysController，关联到底层物理以太网控制器(References EthIfPhysController, associating with the underlying physical Ethernet controller)

   * - EthIfEthTrcvRef
     - 否(No)
     - 引用EthIfTransceiver，关联到以太网收发器(References EthIfTransceiver, associating with the Ethernet transceiver)

   * - EthIfVlanId
     - 否(No)
     - VLAN ID，配置后EthIf将在发送时添加VLAN Tag，接收时去除VLAN Tag(VLAN ID, when configured, EthIf will add VLAN Tag on transmission and remove VLAN Tag on reception)

   * - EthIfCtrlMtu
     - 否(No)
     - 最大传输单元(Maximum Transfer Unit)

   * - EthIfMaxTxBufsTotal
     - 否(No)
     - 该控制器支持的最大发送缓冲区总数(Maximum total number of transmit buffers supported by this controller)


容器EthIfTransceiver，EthIfSwitch与EthIfSwitchPortGroup Containers EthIfTransceiver, EthIfSwitch, and EthIfSwitchPortGroup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
这三类容器主要都是引用外部模块的配置，可依据需要与配置属性的介绍进行配置。

These three types of containers are mainly used to reference the configurations of external modules, and can be configured according to needs and the description of configuration attributes.

EthIfTransceiver容器中必须配置的参数如下：

The parameters that must be configured in the EthIfTransceiver container are as follows:

.. list-table::
   :widths: 25 10 65
   :header-rows: 1

   * - 参数(Parameter)
     - 是否必须(Required)
     - 说明(Description)

   * - EthIfTransceiverIdx
     - 是(Yes)
     - 收发器索引(Transceiver index)

   * - EthIfEthTrcvRef
     - 是(Yes)
     - 引用下层EthTrcv驱动中的收发器配置(References the transceiver configuration in the lower-layer EthTrcv driver)

EthIfSwitch容器中必须配置的参数如下：

The parameters that must be configured in the EthIfSwitch container are as follows:

.. list-table::
   :widths: 25 10 65
   :header-rows: 1

   * - 参数(Parameter)
     - 是否必须(Required)
     - 说明(Description)

   * - EthIfSwitchIdx
     - 是(Yes)
     - 交换机索引(Switch index)

   * - EthIfSwitchRef
     - 是(Yes)
     - 引用下层EthSwt驱动中的交换机配置(References the switch configuration in the lower-layer EthSwt driver)

EthIfSwitchPortGroup容器中必须配置的参数如下：

The parameters that must be configured in the EthIfSwitchPortGroup container are as follows:

.. list-table::
   :widths: 25 10 65
   :header-rows: 1

   * - 参数(Parameter)
     - 是否必须(Required)
     - 说明(Description)

   * - EthIfSwitchPortGroupIdx
     - 是(Yes)
     - 端口组索引(Port group index)

   * - EthIfPortRef
     - 是(Yes)
     - 引用下层EthSwt驱动中的交换机端口(References the switch port in the lower-layer EthSwt driver)


容器EthIfTrcvLinkStateChgConfig Container EthIfTrcvLinkStateChgConfig
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
这个容器用于配置EthIf模块检测到Transceiver的link状态发生变化时将新的link状态报告给对应的模块，EthIf模块会调用容器配置的目标模块的回调函数。

This container is used to configure that when the EthIf module detects a change in the link state of the Transceiver, it will report the new link state to the corresponding module, and the EthIf module will call the callback function of the target module configured in the container.

具体实现时EthIf会根据发送link状态变化的Transceiver所关联的EthIfController作为参数，遍历所有的EthIfTrcvLinkStateChgConfig配置并调用其配置的目标模块的回调函数。

In specific implementation, EthIf will use the EthIfController associated with the Transceiver that sends the link state change as a parameter, traverse all EthIfTrcvLinkStateChgConfig configurations, and call the callback function of the target module configured therein.

EthIfTrcvLinkStateChgConfig容器中必须配置的参数如下：

The parameters that must be configured in the EthIfTrcvLinkStateChgConfig container are as follows:

.. list-table::
   :widths: 25 10 65
   :header-rows: 1

   * - 参数(Parameter)
     - 是否必须(Required)
     - 说明(Description)

   * - EthIfTrcvLinkStateChgFunction
     - 是(Yes)
     - 配置目标模块的Link状态变化回调函数(Configures the link state change callback function of the target module)

.. figure:: /_static/参考手册(Module_Reference_Manual)/EthIf/EthIf_TransceiverLinkChg.png
   :alt: EthIfTrcvLinkStateChgConfig配置界面 (EthIfTrcvLinkStateChgConfig Configuration Interface)
   :name: EthIfTrcvLinkStateChgConfig
   :align: center

EthIfTrcvLinkStateChgConfig配置界面 (EthIfTrcvLinkStateChgConfig Configuration Interface)


容器EthIfRxIndicationConfig,EthIfTxConfirmationConfig与EthIfFrameOwnerConfig Containers EthIfRxIndicationConfig, EthIfTxConfirmationConfig, and EthIfFrameOwnerConfig
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
容器EthIfRxIndicationConfig用于配置EthIf接收到以太网报文时将会调用的目标模块用于接收EthIf传递的以太网数据的回调函数，这个容器中可以配置多个EthIfRxIndicationConfig，但是EthIf会依据EthIfFrameOwnerConfig的配置选择调用哪一个配置的回调函数。

The container EthIfRxIndicationConfig is used to configure the callback function of the target module that the EthIf module will call to receive the Ethernet data transmitted by EthIf when it receives an Ethernet frame. Multiple EthIfRxIndicationConfig configurations can be set in this container, but EthIf will select which configured callback function to call based on the configuration of EthIfFrameOwnerConfig.

容器EthIfTxConfirmationConfig用于配置EthIf接收到以太网报文发送完成确认时向上层模块报告以太网报文的发送完成确认，即调用配置在这个容器中的上层模块的发送完成确认的回调函数，EthIf会依据EthIfFrameOwnerConfig的配置选择调用哪一个配置的回调函数。

The container EthIfTxConfirmationConfig is used to configure that when the EthIf module receives the confirmation of the completion of Ethernet frame transmission, it will report the transmission completion confirmation of the Ethernet frame to the upper-layer module, i.e., call the transmission completion confirmation callback function of the upper-layer module configured in this container. EthIf will select which configured callback function to call based on the configuration of EthIfFrameOwnerConfig.

.. figure:: /_static/参考手册(Module_Reference_Manual)/EthIf/EthIf_TxConfirmation.png
   :alt: EthIf_TxConfirmation回调函数可以配置成NULL_PTR (The EthIf_TxConfirmation callback function can be configured as NULL_PTR)
   :name: EthIf_TxConfirmation_config
   :align: center

   EthIf_TxConfirmation回调函数可以配置成NULL_PTR (The EthIf_TxConfirmation callback function can be configured as NULL_PTR)

.. _EthIfFrameOwnerConfig_matching:

.. important::
   EthIf依据EthIfFrameOwnerConfig中的EthIfFrameType对报文进行匹配。接收时，当EthIfFrameType与收到的报文匹配时，根据EthIfOwner(从0开始计数)调用EthIfRxIndicationConfig中对应序号的回调函数。发送时，EthIf在EthIfFrameOwnerConfig对应条目中记录EthIfPhyController与BufIndex；当EthIf_TxConfirmation被调用时，通过该匹配确定EthIfOwner，再调用EthIfTxConfirmationConfig对应的回调函数。

   EthIf matches frames based on EthIfFrameType in EthIfFrameOwnerConfig. On reception, when EthIfFrameType matches the received frame, the callback function at the corresponding index in EthIfRxIndicationConfig is called according to EthIfOwner (counted from 0). On transmission, EthIf records EthIfPhyController and BufIndex in the corresponding EthIfFrameOwnerConfig entry; when EthIf_TxConfirmation is called, the EthIfOwner is determined through this matching, and the corresponding callback function in EthIfTxConfirmationConfig is called.

   因此配置时需要确保同一个上层模块的TxConfirmation与RxIndication函数在EthIfTxConfirmationConfig与EthIfRxIndicationConfig中处于相同的序号位置，若没有对应的回调函数可配置"NULL_PTR"以保持顺序一致。

   Therefore, during configuration, ensure that the TxConfirmation and RxIndication functions of the same upper-layer module are at the same index position in EthIfTxConfirmationConfig and EthIfRxIndicationConfig. If there is no corresponding callback function, configure "NULL_PTR" to maintain sequence consistency.

EthIfRxIndicationConfig容器中必须配置的参数如下：

The parameters that must be configured in the EthIfRxIndicationConfig container are as follows:

.. list-table::
   :widths: 25 10 65
   :header-rows: 1

   * - 参数(Parameter)
     - 是否必须(Required)
     - 说明(Description)

   * - EthIfRxIndicationFunction
     - 是(Yes)
     - 配置接收指示回调函数，可配置为NULL_PTR(Configures the Rx indication callback function, can be configured as NULL_PTR)

EthIfTxConfirmationConfig容器中必须配置的参数如下：

The parameters that must be configured in the EthIfTxConfirmationConfig container are as follows:

.. list-table::
   :widths: 25 10 65
   :header-rows: 1

   * - 参数(Parameter)
     - 是否必须(Required)
     - 说明(Description)

   * - EthIfTxConfirmationFunction
     - 是(Yes)
     - 配置发送确认回调函数，可配置为NULL_PTR(Configures the Tx confirmation callback function, can be configured as NULL_PTR)

EthIfFrameOwnerConfig容器中必须配置的参数如下：

The parameters that must be configured in the EthIfFrameOwnerConfig container are as follows:

.. list-table::
   :widths: 25 10 65
   :header-rows: 1

   * - 参数(Parameter)
     - 是否必须(Required)
     - 说明(Description)

   * - EthIfFrameType
     - 是(Yes)
     - 以太网报文类型(EtherType)，用于匹配收到的报文(Ethernet frame type, used to match received frames)

   * - EthIfOwner
     - 是(Yes)
     - 报文归属Owner索引(从0开始)，用于关联EthIfRxIndicationConfig与EthIfTxConfirmationConfig中对应序号的回调函数(Frame owner index counted from 0, used to associate with the callback function at the corresponding index in EthIfRxIndicationConfig and EthIfTxConfirmationConfig)
