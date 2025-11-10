===================
EthSwt
===================
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

   * - 2025/4/1
     - fupeng.yu
     - V0.1
     - 发布(Release)
     - 首次发布(First release)

   * - 2025/04/04
     - fupeng.yu
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
     - AUTOSAR_CP_SRS_Ethernet.pdf
     - R23-11
   * - 2
     - Autosar
     - AUTOSAR_CP_SWS_EthernetSwitchDriver.pdf
     - R23-11


术语与简写 Terms and Abbreviations
==================================================================


术语 Terms
------------------------------------------------------------------------------------------------------------------
.. :align: center   表格内容居中(Table contents are centered)

None



简写 Abbreviations
------------------------------------------------------------------------------------------------------------------

.. list-table::
   :widths: 10 20 30
   :header-rows: 1


   * - 简写(Abbreviation)
     - 全称(Full name)
     - 解释(Explanation)

   * - DEM
     - Diagnostic Event Manager
     - 诊断事件管理器

   * - EcuM
     - ECU State Manager module
     - ECU 状态管理模块

   * - Eth
     - Ethernet Controller Driver (AUTOSAR BSW module)
     - 以太网控制器驱动模块

   * - EthIf
     - Ethernet Interface (AUTOSAR BSW module)
     - 以太网接口模块

   * - EthTrcv
     - Ethernet Transceiver Driver (AUTOSAR BSW module)
     - 以太网收发器驱动模块

   * - MII
     - Media Independent Interface (standardized interface provided by Ethernet controllers to access Ethernet transceivers)
     - 媒体独立接口(以太网控制器提供的标准化接口，用于访问以太网收发器)

   * - MDIO
     - Management Data Input/Output
     - 管理数据输入/输出

   * - OA TC10
     - Open Alliance TC10 specification (see [7])
     - TC10 规范

简介 Introduction
==================================================================

EthSwt 向上层提供与以太网硬件无关的独立接口，该接口可以支持多个不 同的有线或无线以太网控制器和收发器。这些接口按功能可以大体分为模式控制相关的接口、时间同步相关的接口、数据接收发送相关的接口、 EthSwt 本身的初始化或周期任务接口等。

EthSwt provides Ethernet hardware-independent interfaces to the upper layer. These interfaces can support multiple different wired or wireless Ethernet controllers and transceivers. Functionally, these interfaces can be roughly divided into mode control-related interfaces, time synchronization-related interfaces, data transmission and reception-related interfaces, as well as initialization or periodic task interfaces of EthSwt itself.

.. figure:: ../../../_static/参考手册/EthSwt/EthSwt_Autosar_Architecture.png
   :alt: EthSwt模块在AUTOSAR架构中的位置 (Position of EthSwt Module in AUTOSAR Architecture)
   :name: EthSwt_Autosar_Architecture
   :align: center

   EthSwt Architecture in AUTOSAR


如图 :ref:`EthSwt_Autosar_Architecture` 所示，EthSwt模块处于AUTOSAR架构中的EthIf的下层，其位于EthTrcv模块上层

As shown in Figure :ref:`EthSwt_Autosar_Architecture`, the EthSwt module is located in the lower layer of EthIf in the AUTOSAR architecture, and it is positioned in the upper layer of the EthTrcv module.



功能描述 Functional Description
==================================================================


特性 Features
------------------------------------------------------------------------------------------------------------------

MAC 地址学习功能 MAC Address Learning Function
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

以太网交换机能自主学习每一端口相连设备的 MAC 地址，并将地址同相应的端口映射起来存放在交换机缓存中的 MAC 地址表中。

The Ethernet switch can independently learn the MAC address of the device connected to each port, map the address to the corresponding port, and store this mapping in the MAC address table in the switch cache.


VLAN 收发功能 VLAN Transmission and Reception Function
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

EthSwt 负责对 VLAN 报文的解/加 Tag 操作，当接收时，通过 EthSwt 传递给上层的以太网报文将在 EthSwt 中提取出 VLAN 头，并把剩余的数据传递给上层模块。当上层模块需要向下传输报文时，在 EthSwt 中添加 VLAN 头，并通过对应的 Eth 通道发送出去。

EthSwt is responsible for the VLAN tag removal/insertion operations for VLAN frames. When receiving a frame, the Ethernet frame passed by EthSwt to the upper layer will have its VLAN header extracted in EthSwt, and the remaining data will be transmitted to the upper-layer module. When the upper-layer module needs to transmit a frame downward, a VLAN header will be added to the frame in EthSwt, and the frame will be sent out through the corresponding Eth channel.

VLAN 隔离功能介绍 Introduction to VLAN Isolation Function
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

通过配置，属于同一 VLAN 的 port 间可以相互通信，不属于同一 VLAN 的port 间不能相互通信。

Through configuration, ports belonging to the same VLAN can communicate with each other, while ports not belonging to the same VLAN cannot communicate with each other.

接口传递功能介绍 Introduction to Interface Transmission Function
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

EthSwt 负责对底层 switch 驱动进行设置和封装，并提供相应接口传递给EthSwt。

EthSwt is responsible for configuring and encapsulating the underlying switch driver, and providing corresponding interfaces for transmission to EthSwt.


偏差 Deviation
---------------------------------------------------------

None



扩展 Extension
---------------------------------------------------------

None

集成 Integration
=================================

文件列表 File List
---------------------------------------------------------

静态文件 Static Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - 文件(File)
     - 描述(Description)

   * - EthSwt.h
     - EthSwt 模块头文件，包含了 API 函数的扩展声明并定义了端口的数据结构(Header file of the EthSwt module, which contains extended declarations of API functions and defines the data structure of ports)

   * - EthSwt_Internal.h
     - 定义EthSwt 模块中不依赖于芯片的内部函数(Defines internal functions of the EthSwt module that are not dependent on the chip)

   * - EthSwt_Types.h
     - 实现外部/内部类型的定义，包括 AUTOSAR 标准定义的类型，以及 PB/PC 配置参数结构体类型，以及内部运行时结构体类型(Implements definitions of external/internal types, including types defined by AUTOSAR standards, PB/PC configuration parameter structure types, and internal runtime structure types)

   * - EthSwt.c
     - EthSwt 模块源文件，包含了 API 函数的实现(Source file of the EthSwt module, which contains the implementation of API functions)

   * - EthSwt_88Q5050.c
     -  EthSwt 模块中依赖 88Q5050 的函数实现(Implementation of functions in the EthSwt module that are dependent on 88Q5050)

   * - EthSwt_88Q5050.h
     - 定义 EthSwt 模块中依赖 88Q5050 宏定义和结构体(Defines macros and structures in the EthSwt module that are dependent on 88Q5050)

动态文件 Dynamic Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - 文件(File)
     - 描述(Description)

   * - EthSwt_Cfg.h
     - 定义 EthSwt 模块预编译时用到的配置参数(Defines configuration parameters used in the pre-compilation of the EthSwt module)

   * - EthSwt_PBCfg.c
     - 定义 EthSwt 模块中链接时用到的配置变量(Defines configuration variables used in the linking of the EthSwt module)

   * - EthSwt_PBCfg.h
     - 定义 EthSwt 模块中配置变量结构体(Defines the configuration variable structure in the EthSwt module)

错误处理 Error Handling
---------------------------------------------------------



开发错误 Development Errors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. list-table::
   :widths: 20 10 30
   :header-rows: 1

   * - Error code
     - Value[hex]
     - Description

   * - ETHSWT_E_INV_SWITCH_IDX
     - 0x01
     - Invalid switch index

   * - ETHSWT_E_UNINIT
     - 0x02
     - EthSwt module was not initialized

   * - ETHSWT_E_PARAM_POINTER
     - 0x03
     - Invalid pointer in parameter list

   * - ETHSWT_E_INV_API
     - 0x05
     - Invalid API which is not available by another module

   * - ETHSWT_E_INV_SWITCHPORT_IDX
     - 0x06
     - Invalid switch port index

   * - ETHSWT_E_INV_CTRL_IDX
     - 0x07
     - Invalid Controller Index

   * - ETHSWT_E_INV_PARAM
     - 0x08
     - Invalid input parameter

   * - ETHSWT_E_INIT_FAILED
     - 0x09
     - Invalid configuration

产品错误 Product Errors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
None

运行时错误 Runtime Errors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. list-table::
   :widths: 20 10 30
   :header-rows: 1

   * - Error code
     - Value[hex]
     - Description

   * - ETHSWT_INIT_NOT_COMPLETED
     - 0x01
     - Initialization of ports is not finished


接口描述 Interface Description
=====================================================

.. include:: EthSwt_h_api.rst
.. include:: EthSwt_Internal_h_api.rst


依赖的服务 Applicable Services
-------------------------------------------------------------------------------------------

强制接口 Compulsory interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

None


可选接口 Optional Interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 10 5 30
   :header-rows: 1

   * - API Function
     - Header File
     - Description

   * - Det_ReportError
     - Det.h
     - Service to report development errors.

   * - Dem_SetEventStatus
     - Dem.h
     - Called by SW-Cs or BSW modules to report monitor status information to the Dem.

   * - Eth_ReadMii
     - Eth.h
     - Reads a transceiver register.

   * - Eth_WriteMii
     - Eth.h
     - Configures a transceiver register or triggers a function offered by the receiver.

   * - EthTrcv_GetBaudRate
     - EthTrcv.h
     - Obtains the baud rate of the indexed transceiver.

   * - EthTrcv_GetDuplexMode
     - EthTrcv.h
     - Obtains the duplex mode of the indexed transceiver.

   * - EthTrcv_GetLinkState
     - EthTrcv.h
     - Obtains the link state of the indexed transceiver.

   * - EthTrcv_GetTransceiverMode
     - EthTrcv.h
     - Obtains the state of the indexed transceiver.

   * - EthTrcv_SetTransceiverMode
     - EthTrcv.h
     - Enables / disables the indexed transceiver.

   * - EthTrcv_StartAutoNegotiation
     - EthTrcv.h
     - Restarts the negotiation of the transmission parameters used by the indexed transceiver.

   * - NvM_GetErrorStatus
     - NvM.h
     - Service to read the block dependent error/status information.

   * - NvM_ReadBlock
     - NvM.h
     - Service to copy the data of the NV block to its corresponding RAM block.

   * - NvM_WriteBlock
     - NvM.h
     - Service to copy the data of the RAM block to its corresponding NV block.

   * - Spi_AsyncTransmit
     - Spi.h
     - Service to transmit data on the SPI bus.

   * - Spi_Cancel
     - Spi.h
     - Service cancels the specified on-going sequence transmission.

   * - Spi_ReadIB
     - Spi.h
     - Service for reading synchronously one or more data from an IB SPI Handler/Driver Channel specified by parameter.

   * - Spi_SetAsyncMode
     - Spi.h
     - Service to set the asynchronous mechanism mode for SPI busses handled asynchronously.

   * - Spi_SetupEB
     - Spi.h
     - Service to setup the buffers and the length of data for the EB SPI Handler/Driver Channel specified.

   * - Spi_SyncTransmit
     - Spi.h
     - Service to transmit data on the SPI bus.

   * - Spi_WriteIB
     - Spi.h
     - Service for writing one or more data to an IB SPI Handler/Driver Channel specified by parameter.

配置接口 Configuration Interfaces
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. list-table::
   :widths: 10 5 30
   :header-rows: 1

   * - API Function
     - Header File
     - Description

   * - <EthSwtLinkDownCallout>
     - EthSwt_Externals.h
     - Is called, if a link which is configured goes down.

   * - <EthSwtLinkUpCallout>
     - EthSwt_Externals.h
     - Is called, if a link which is configured goes up.

   * - <GetCfgDataRawDone>
     - EthSwt_Externals.h
     - The call of the function EthSwt_GetCfgDataRaw() triggers a asynchrony read of a certain memory section of the Ethernet switch driver.

配置 Configuration
=================================

EthSwtGeneral
---------------------------------------------------------

配置是否使能相关特性的API

Configure whether to enable APIs for relevant features.

Switch 配置 Switch Configuration
------------------------------------------------------------------------------------------------------------------

Switch Port出口和入口的配置, VLAN需求的配置等

Configuration of Switch Port egress and ingress, configuration of VLAN requirements, etc.


