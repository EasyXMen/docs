===================
PduR
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
   * - 2024/11/28
     - 赵彤(Zhao Tong)
     - V0.1
     - 发布(Release)
     - 首次发布(First release)
   * - 2025/04/04
     - 赵彤(Zhao Tong)
     - V1.0
     - 发布(Release)
     - 正式发布(Official release)

   * - 2026/3/10
     - 赵彤(Zhao Tong)
     - V1.1
     - 修正(Modify)
     - 调整文档架构(Modify the document structure)

   * - 2026/3/23
     - 赵彤(Zhao Tong)
     - V2.0
     - 添加(Add)
     - 增加Tp多播功能(Add Tp multi-cast operation)

   * - 2026/06/20
     - 赵彤(Zhao Tong)
     - V2.1
     - 修正(Modify)
     - 补充发送链路、接收链路、网关路由和路由控制的功能描述与配置参数表(Supplement functional description and configuration parameter tables for transmit path, receive path, gateway routing, and routing control)

参考文档(References)
----------------------------------

.. list-table::
   :widths: 10 10 30 10
   :header-rows: 1

   * - 编号(Number)
     - 分类(Classification)
     - 标题(Title)
     - 版本(Version)
   * - 1
     - Autosar
     - AUTOSAR_CP_SRS_Gateway
     - R23-11
   * - 2
     - Autosar
     - AUTOSAR_CP_SWS_PDURouter.pdf
     - R23-11


术语与简写(Terms and Abbreviations)
========================================


术语(Term)
----------------------


.. list-table::
   :widths: 10 40
   :header-rows: 1

   * - 术语(Term)
     - 解释(Explanation)

   * - on-the-fly gatewaying
     - 网关能力：在两个TP模块之间进行路由，在接收到所有数据之前(当达到指定阈值时)开始转发数据。(Gateway capability: Routes between two TP modules and starts forwarding data before all data is received (when the specified threshold is reached).)

   * - multicast operation
     - 多播路由，即1：N(Multicast routing, i.e., 1:N)

   * - data provision
     - 数据提供方式：direct data provision 和 trigger transmit data provision(Data provision methods: direct data provision and trigger transmit data provision)

   * - last-is-best buffering
     - Buffer策略：队列深度为1，后接收的数据会覆盖前面存储的数据(Buffer strategy: Queue depth is 1, and subsequently received data overwrites previously stored data)

   * - FIFO buffering
     - Buffer策略：队列深度大于1，采用First in first out(Buffer strategy: Queue depth greater than 1, using First In First Out)

简写(Abbreviations)
------------------------

.. list-table::
   :widths: 10 20 30
   :header-rows: 1


   * - 简写(Abbreviation)
     - 全称(Full name)
     - 解释(Explanation)

   * - <SrcLo>
     - Lower layer communication interface module acting as a source of the I-PDU
     - 下层IF模块关联的PDU作为PduR中的Source I-PDU(Lower layer IF module associated PDU serves as Source I-PDU in PduR)

   * - <DstLo>
     - Lower layer communication interface module acting as a destination of the I-PDU
     - 下层IF模块关联的PDU作为PduR中的Dest I-PDU(Lower layer IF module associated PDU serves as Destination I-PDU in PduR)

   * - <SrcLoTp>
     - Lower layer transport protocol module acting as a source of the I-PDU
     - 下层TP模块关联的PDU作为PduR中的Source I-PDU(Lower layer TP module associated PDU serves as Source I-PDU in PduR)

   * - <DstLoTp>
     - Lower layer transport protocol module acting as a destination of the I-PDU
     - 下层TP模块关联的PDU作为PduR中的Dest I-PDU(Lower layer TP module associated PDU serves as Destination I-PDU in PduR)

   * - I-PDU ID
     - PDU Identifier
     - PDU的ID号(PDU identifier)

   * - I-PDU
     - Interaction Layer PDU
     - 交互层PDU，涉及PDU的ID号，PDU长度，PDU数据(Interaction Layer PDU, involving PDU ID, PDU length, and PDU data)

   * - Upper Layer Modules (Up)
     - Modules above the PDU Router
     - 在AUTOSAR架构下，处于PduR上层的模块(Modules above PduR in AUTOSAR architecture)

   * - Lower Layer Modules (Lo)
     - Modules below the PDU Router
     - 在AUTOSAR架构下，处于PduR下层的模块(Modules below PduR in AUTOSAR architecture)

   * - FIFO
     - First In First Out
     - 先入先出(First In First Out)

   * - DET
     - Default Error Tracer
     - 错误检测模块(Error detection module)

简介(Introduction)
============================


PduR模块主要为通信接口模块(如CanIf)，传输协议模块(如CanTp)，诊断服务模块(如Dcm)，通信服务模块(如Com, LdCom)，以及IpduM，SecOc等模块提供基于PDU的路由服务。PduR模块主要实现基于PDU的接收路由(PDU从CanIf→PduR→Com)，发送路由(Com→PduR→CanIf)，网关路由功能(CanIf→PduR→CanIf)。

The PduR module provides PDU-based routing services for communication interface modules (e.g., CanIf), transport protocol modules (e.g., CanTp), diagnostic service modules (e.g., Dcm), communication service modules (e.g., Com, LdCom), as well as modules such as IpduM and SecOc. The PduR module implements PDU-based reception routing (PDU from CanIf→PduR→Com), transmission routing (Com→PduR→CanIf), and gateway routing (CanIf→PduR→CanIf).

.. figure:: /_static/参考手册(Module_Reference_Manual)/PduR/PduR在Autosar中的位置.png
   :alt: PduR模块层次图
   :name: PduR_module_hierarchy
   :align: center

   PduR模块层次图(PduR Module Hierarchy Diagram)

与PduR模块存在交互的模块可分为三类：1.下层模块(如CanIf, CanTp)；2.上层模块(如Com, Dcm)；3.既是上层又是下层模块(IpduM, SecOC)。
PduR与所有交互模块间实现IF PDU和TP PDU的接收与发送功能。

Modules interacting with the PduR module fall into three categories: 1. Lower-layer modules (e.g., CanIf, CanTp); 2. Upper-layer modules (e.g., Com, Dcm); 3. Modules serving as both upper and lower layers (IpduM, SecOC).
The PduR module handles reception and transmission of IF PDUs and TP PDUs with all interacting modules.


功能描述(Functional Description)
==========================================

公共特性(Public Features)
--------------------------------------------------

多核多分区功能(Multi-core and Multi-partition Features)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- 如果工程中EcucPartition存在大于1个的配置，则认为该工程支持多分区/多核。

  If there is more than one EcucPartition configuration in the project, the project supports multi-partition/multi-core.

- 通过 EcuC / EcucPduDefaultPartitionRef 获取路由默认分区信息。

  The default partition information for routing is obtained via EcuC / EcucPduDefaultPartitionRef.


.. only:: doc_pbs

   PBS功能(PBS Features)
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   PduR 支持在不同变体中：

   - 支持不同的转发路径

     Supports different forwarding paths

   - 支持不同的数据提供方式

     Supports different data provision methods

   - 支持不同的队列深度

     Supports different queue depths

   - 支持不同的私有buffer

     Supports different private buffers

   - 支持不同的路由组

     Supports different routing groups

   - 支持不同的阈值on the fly gatewaying

     Supports different thresholds for on-the-fly gatewaying

Memmap功能(Memmap Features)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
memmap文件是动态的。存在PDUR_START_SEC_CODE、PDUR_STOP_SEC_CODE、PDUR_START_SEC_VAR_INIT_8、PDUR_STOP_SEC_VAR_INIT_8、PDUR_START_SEC_VAR_INIT_PTR、PDUR_STOP_SEC_VAR_INIT_PTR、PDUR_START_SEC_VAR_INIT_UNSPECIFIED、PDUR_STOP_SEC_VAR_INIT_UNSPECIFIED、PDUR_START_SEC_VAR_CLEARED_BOOLEAN、PDUR_STOP_SEC_VAR_CLEARED_BOOLEAN、PDUR_START_SEC_VAR_CLEARED_8、PDUR_STOP_SEC_VAR_CLEARED_8、PDUR_START_SEC_VAR_CLEARED_16、PDUR_STOP_SEC_VAR_CLEARED_16、PDUR_START_SEC_VAR_CLEARED_32、PDUR_STOP_SEC_VAR_CLEARED_32、PDUR_START_SEC_VAR_CLEARED_PTR、PDUR_STOP_SEC_VAR_CLEARED_PTR、PDUR_START_SEC_VAR_CLEARED_UNSPECIFIED、PDUR_STOP_SEC_VAR_CLEARED_UNSPECIFIED、PDUR_START_SEC_CONFIG_DATA_8、PDUR_STOP_SEC_CONFIG_DATA_8、PDUR_START_SEC_CONFIG_DATA_16、PDUR_STOP_SEC_CONFIG_DATA_16、PDUR_START_SEC_CONFIG_DATA_UNSPECIFIED、PDUR_STOP_SEC_CONFIG_DATA_UNSPECIFIED字段。

The memmap file is dynamic. It contains fields such as PDUR_START_SEC_CODE, PDUR_STOP_SEC_CODE, PDUR_START_SEC_VAR_INIT_8, PDUR_STOP_SEC_VAR_INIT_8, PDUR_START_SEC_VAR_INIT_PTR, PDUR_STOP_SEC_VAR_INIT_PTR, PDUR_START_SEC_VAR_INIT_UNSPECIFIED, PDUR_STOP_SEC_VAR_INIT_UNSPECIFIED, PDUR_START_SEC_VAR_CLEARED_BOOLEAN, PDUR_STOP_SEC_VAR_CLEARED_BOOLEAN, PDUR_START_SEC_VAR_CLEARED_8, PDUR_STOP_SEC_VAR_CLEARED_8, PDUR_START_SEC_VAR_CLEARED_16, PDUR_STOP_SEC_VAR_CLEARED_16, PDUR_START_SEC_VAR_CLEARED_32, PDUR_STOP_SEC_VAR_CLEARED_32, PDUR_START_SEC_VAR_CLEARED_PTR, PDUR_STOP_SEC_VAR_CLEARED_PTR, PDUR_START_SEC_VAR_CLEARED_UNSPECIFIED, PDUR_STOP_SEC_VAR_CLEARED_UNSPECIFIED, PDUR_START_SEC_CONFIG_DATA_8, PDUR_STOP_SEC_CONFIG_DATA_8, PDUR_START_SEC_CONFIG_DATA_16, PDUR_STOP_SEC_CONFIG_DATA_16, PDUR_START_SEC_CONFIG_DATA_UNSPECIFIED, and PDUR_STOP_SEC_CONFIG_DATA_UNSPECIFIED.


独占区功能(Exclusive Area Features)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PduR共有三个独占区保护类型：

PduR provides three exclusive area protection types:

#. SchM_Enter_PduR_ExclusiveArea_Group是对于Group使能或者禁用的保护，因为一个group下的destpdu均属于一个分区，推荐使用禁中断方式ALL_INTERRUPT_BLOCKING

   SchM_Enter_PduR_ExclusiveArea_Group protects group enable/disable operations. Since destpdus within a group belong to one partition, use ALL_INTERRUPT_BLOCKING

#. SchM_Enter_PduR_ExclusiveArea_Route是对于PduRBuffer、路由状态申请的保护，

   SchM_Enter_PduR_ExclusiveArea_Route protects PduRBuffer and routing state application.

   - 如果所有需要配置PduRBuffer的PduRRoutingPath，均配置了私有buffer，且不存在共用私有buffer，不存在一对多多对一，网关等资源竞争时，则推荐使用禁中断方式ALL_INTERRUPT_BLOCKING；

     If all PduRRoutingPaths requiring PduRBuffer configuration have private buffers, with no shared private buffers or resource contention (one-to-many, many-to-one, gateway), use ALL_INTERRUPT_BLOCKING

   - (推荐)如果存在共用buffer且会同时申请buffer，或者一对多多对一，网关等资源竞争时，则需要配置为OS_SPINLOCK；

     (Recommended) If shared buffers are used and multiple buffers will be allocated at the same time or if one-to-many, many-to-one, gateway, etc. resource contention occurs, use OS_SPINLOCK

#. SchM_Enter_PduR_ExclusiveArea_Init是对于初始化时逻辑的保护，推荐使用禁中断方式ALL_INTERRUPT_BLOCKING

   SchM_Enter_PduR_ExclusiveArea_Init protects initialization logic; use ALL_INTERRUPT_BLOCKING


模块特性（Module Features）
------------------------------------------------

发送路由功能(Transmit Routing Function)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PduR发送链路(Transmit Path)负责将上层模块(如Com、Dcm、LdCom等)的Tx PDU路由到下层通信接口模块(如CanIf)或传输协议模块(如CanTp)。

The PduR transmit path routes Tx PDUs from upper-layer modules (e.g., Com, Dcm, LdCom) to lower-layer communication interface modules (e.g., CanIf) or transport protocol modules (e.g., CanTp).

Tx PDU的发送分为两种方式(IF和TP)：

Tx PDU transmission operates in two modes (IF and TP):

IF PDU发送(IF PDU Transmission)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

上层模块通过调用 :code:`PduR_<Up>Transmit` 接口发起IF PDU发送请求。PduR根据配置的PduRRoutingPath（PduRRouteType为IF）查找对应的PduRDestPdu，通过 :code:`PduR_<Lo>TxConfirmation` 通知上层发送结果。

The upper-layer module initiates IF PDU transmission by calling :code:`PduR_<Up>Transmit`. PduR looks up the corresponding PduRDestPdu based on the configured PduRRoutingPath (PduRRouteType = IF), and notifies the upper layer of the transmission result via :code:`PduR_<Lo>TxConfirmation`.

- 支持1:1和1:N路由（一个SrcPdu可路由到多个DestPdu）

  Supports 1:1 and 1:N routing (one SrcPdu can be routed to multiple DestPdus)

- 如果PduRDestPdu关联的Tx PDU发送方式为TriggerTransmit，下层模块通过调用 :code:`PduR_<Lo>TriggerTransmit` 请求上层提供发送数据

  If the Tx PDU transmission mode associated with PduRDestPdu is TriggerTransmit, the lower-layer module requests the upper layer to provide transmission data via :code:`PduR_<Lo>TriggerTransmit`

- 支持发送确认机制，上层通过 :code:`PduR_<Lo>TxConfirmation` 获取发送结果

  Supports transmission confirmation; the upper layer obtains the transmission result via :code:`PduR_<Lo>TxConfirmation`

TP PDU发送(TP PDU Transmission)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

上层模块通过调用 :code:`PduR_<Up>Transmit` 发起TP PDU发送请求。PduR根据配置的PduRRoutingPath（PduRRouteType为TP）查找对应的PduRDestPdu，下层TP模块通过 :code:`PduR_<LoTp>CopyTxData` 分片获取PDU发送数据，通过 :code:`PduR_<LoTp>TxConfirmation` 通知发送结果。

The upper-layer module initiates TP PDU transmission by calling :code:`PduR_<Up>Transmit`. PduR looks up the corresponding PduRDestPdu based on the configured PduRRoutingPath (PduRRouteType = TP). The lower-layer TP module retrieves PDU transmission data segments via :code:`PduR_<LoTp>CopyTxData` and notifies the transmission result via :code:`PduR_<LoTp>TxConfirmation`.

- 支持1:1和1:N路由

  Supports 1:1 and 1:N routing

- 支持发送取消（通过 :code:`PduR_<LoTp>CancelTransmit`）

  Supports transmission cancellation (via :code:`PduR_<LoTp>CancelTransmit`)

- TP PDU的发送过程中，PduR不缓存完整TP报文数据，而是通过CopyTxData机制按需向上层获取数据段

  During TP PDU transmission, PduR does not buffer the complete TP message data but retrieves data segments from the upper layer on demand via the CopyTxData mechanism

接收路由功能(Receive Routing Function)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PduR接收链路(Receive Path)负责将下层通信接口模块(如CanIf)或传输协议模块(如CanTp)接收到的Rx PDU路由到上层模块(如Com、Dcm、LdCom等)。

The PduR receive path routes Rx PDUs received from lower-layer communication interface modules (e.g., CanIf) or transport protocol modules (e.g., CanTp) to upper-layer modules (e.g., Com, Dcm, LdCom).

Rx PDU的接收分为两种方式(IF和TP)：

Rx PDU reception operates in two modes (IF and TP):

IF PDU接收(IF PDU Reception)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

下层IF模块(如CanIf)通过调用 :code:`PduR_<Lo>RxIndication` 将接收到的IF PDU传递给PduR。PduR根据配置的PduRRoutingPath（PduRRouteType为IF）查找对应的PduRDestPdu，将PDU数据路由到对应的上层模块。

The lower-layer IF module (e.g., CanIf) passes the received IF PDU to PduR via :code:`PduR_<Lo>RxIndication`. PduR looks up the corresponding PduRDestPdu based on the configured PduRRoutingPath (PduRRouteType = IF) and routes the PDU data to the corresponding upper-layer module.

- 支持1:1、1:N和N:1路由（多个SrcPdu可路由到同一个DestPdu）

  Supports 1:1, 1:N, and N:1 routing (multiple SrcPdus can be routed to the same DestPdu)

- 接收链路不缓存IF PDU数据，直接从下层模块传递到上层模块

  The receive path does not buffer IF PDU data; it passes directly from the lower-layer module to the upper-layer module

TP PDU接收(TP PDU Reception)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

下层TP模块(如CanTp)通过 :code:`PduR_<LoTp>StartOfReception` 开始TP PDU接收流程，通过 :code:`PduR_<LoTp>CopyRxData` 分片传递接收数据，最终通过 :code:`PduR_<LoTp>RxIndication` 将完整TP PDU路由到上层模块。

The lower-layer TP module (e.g., CanTp) starts the TP PDU reception process via :code:`PduR_<LoTp>StartOfReception`, passes received data segments via :code:`PduR_<LoTp>CopyRxData`, and finally routes the complete TP PDU to the upper-layer module via :code:`PduR_<LoTp>RxIndication`.

- 支持1:1和1:N路由

  Supports 1:1 and 1:N routing

- 支持接收取消（通过 :code:`PduR_<LoTp>CancelReceive`）

  Supports reception cancellation (via :code:`PduR_<LoTp>CancelReceive`)

- TP PDU接收过程中，PduR不缓存TP报文数据，通过CopyRxData机制由下层模块按需向上层传递数据段

  During TP PDU reception, PduR does not buffer TP message data; data segments are passed from the lower layer to the upper layer on demand via the CopyRxData mechanism

网关路由功能(Gateway Routing Function)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PDU的网关同样分为IF/TP两种方式，IF网关支持1:1、1:N、N:1路由，TP网关也支持1:1、1:N、N:1路由，不涉及任何报文数据的变化，收发报文速率保持一致(如果目的端报文长度小于源端报文长度，会进行截断以确保网关功能正常)。
需注意PDU的网关不能IF、TP混用，即接收的IF PDU只能通过发送IF PDU进行转发，接收的TP PDU只能通过发送TP PDU进行转发。

PDU gateway operation is also divided into IF/TP modes. The IF gateway supports 1:1, 1:N and N:1 routing, and the TP gateway also supports 1:1, 1:N and N:1 routing. This process does not modify message data, and transmission/reception rates remain consistent (if the destination message length is shorter than the source message length, truncation occurs to ensure successful gateway operation).
Note that PDU gateways cannot mix IF and TP modes: received IF PDUs can only be forwarded via transmitted IF PDUs, and received TP PDUs can only be forwarded via transmitted TP PDUs.

路由控制功能(Routing Control Function)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PduR的路由控制以RoutingPathGroup为单位进行启用/禁用控制，而PduRRoutingPath通过PduRRoutingPathGroupRef可以关联N个RoutingPathGroup，只要关联的至少一个RoutingPathGroup启用，则对应的PduRDestPdu使能。

PduR routing control enables/disables RoutingPathGroups as units. PduRRoutingPath can associate with N RoutingPathGroups via PduRRoutingPathGroupRef. The corresponding PduRDestPdu is enabled when at least one associated RoutingPathGroup is enabled.


偏差(Deviation)
-------------------

#. 不支持Tp多播发送（仅支持Tp多播接收）

   PduR does not support Tp multicast transmission (only Tp multicast reception is supported).

#. 不支持PduRDemEventParameterRef

   PduR does not support PduRDemEventParameterRef.
   
#. 自定义配置项PduRRouteType(IF/TP)

   Custom configuration item PduRRouteType (IF/TP)

扩展(Expansion)
----------------

None

集成(Integration)
==========================

文件列表(File List)
----------------------------

静态文件(Static Files)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - 文件(File)
     - 描述(Description)
   
   * - PduR.c
     - 作为PduR模块的核心文件，实现PduR模块全部对外接口，以及实现PduR模块功能所必须的local变量定义、local函数定义和声明。(Serves as the core file of the PduR module, implementing all external interfaces and necessary local variable definitions, local function definitions, and declarations for PduR module functionality.)

   * - PduR.h
     - 实现PduR模块全部外部接口的声明，以及配置文件中全局变量的声明，必要宏的定义。(Declares all external interfaces of the PduR module, global variables from configuration files, and necessary macro definitions.)

   * - PduR_Route.c
     - 实现PduR模块Route功能需要使用到的全部内部接口函数定义、local函数声明。(Implements all internal interface function definitions and local function declarations required for the PduR module's routing functionality.)

   * - PduR_Route.h
     - 实现PduR模块Route功能需要使用到的全部内部接口函数声明。(Declares all internal interface functions required for the PduR module's routing functionality.)

   * - PduR_Buffer.c
     - 实现PduR模块Buffer功能需要使用到的全部内部接口函数定义，以及实现Buffer功能所必须的local变量定义、local函数定义和声明。(Implements all internal interface function definitions, and necessary local variable definitions, local function definitions, and declarations for the PduR module's buffer functionality.)

   * - PduR_Buffer.h
     - 实现PduR模块Buffer功能需要使用到的全部内部接口函数声明。(Declares all internal interface functions required for the PduR module's buffer functionality.)

   * - PduR_Internal.c
     - 实现PduR模块内部全局变量的定义，内部接口的实现。(Defines internal global variables and implements internal interfaces for the PduR module.)

   * - PduR_Internal.h
     - 实现PduR模块内部宏的定义，全局变量的声明，内部inline接口的实现。(Defines internal macros, declares global variables, and implements internal inline interfaces for the PduR module.)

   * - PduR_Types.h
     - 实现外部/内部类型的定义，包括AUTOSAR标准定义的类型，以及PB/PC配置参数结构体类型，以及内部运行时结构体类型。(Defines external/internal types, including AUTOSAR standard types, PB/PC configuration parameter structure types, and internal runtime structure types.)

   * - PduR_MemMap.h
     - 实现PduR模块内存布局。(Implements the memory layout for the PduR module.)

动态文件(Dynamic Files)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - 文件(File)
     - 描述(Description)
   
   * - PduR_Cfg.h
     - 定义PduR模块PC配置的宏定义(Defines macros for PduR module pre-compile configuration)

   * - PduR_Cfg.c
     - 定义PduR模块PC配置的结构体参数(Defines structure parameters for PduR module pre-compile configuration)

   * - PduR_PBcfg.h
     - 定义PduR模块PB配置的宏定义(Defines macros for PduR module post-build configuration)

   * - PduR_PBcfg.c
     - 定义PduR模块PB配置的结构体参数(Defines structure parameters for PduR module post-build configuration)

   * - PduR_<Module>.h
     - 实现Module需要调用的PduR接口宏定义(Implements PduR interface macro definitions required by specific modules)

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

   * - PDUR_E_INIT_FAILED
     - 0x00
     - Invalid configuration pointer

   * - PDUR_E_UNINIT
     - 0x01
     - API service (except PduR_GetVersionInfo) used without module initialization or PduR_Init called in any state other than PDUR_UNINIT

   * - PDUR_E_PDU_ID_INVALID
     - 0x02
     - Invalid PDU identifier

   * - PDUR_E_ROUTING_PATH_GROUP_ID_INVALID
     - 0x08
     - If the routing table is invalid that is given to the PduR_EnableRouting or PduR_DisableRouting functions

   * - PDUR_E_PARAM_POINTER
     - 0x09
     - If a passed pointer parameter is a NULL pointer

产品错误(Product Errors)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
None

运行时错误(Runtime Errors)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. list-table:: 
   :widths: 20 10 30
   :header-rows: 1

   * - Error code
     - Value[hex]
     - Description

   * - PDUR_E_TP_GW_TX_REQ_REJECTED
     - 0x03
     - TP module rejected a transmit request for a valid PDU identifier in case of gateway operation

   * - PDUR_E_PDU_INSTANCES_LOST
     - 0x0a
     - Loss of a PDU instance (buffer overrun in gateway operation)

   * - PDUR_E_NO_BUFFER
     - 0x0b
     - No buffer available for PDU transmission


接口描述(Interface Description)
=====================================

.. include:: PduR_h_api.rst


配置(Configuration)
==========================

本章包含两部分：(This chapter contains two parts:)

- **场景配置指南(Scenario Configuration Guide)**：按发送/接收/网关/路由控制等使用场景，列出所需容器与关键参数速查表，帮助快速定位配置项。

  **Scenario Configuration Guide**: Lists required containers and key parameter quick-reference tables by usage scenario (transmit/receive/gateway/routing control) for fast configuration lookup.

- **工具参数手册(Tool Parameter Reference)**：按容器列出所有参数的技术细节，包括取值范围、默认值、依赖关系等，配有配置工具截图。

  **Tool Parameter Reference**: Lists technical details of all parameters by container, including ranges, defaults, dependencies, with tool screenshots.

----

场景配置指南(Scenario Configuration Guide)
--------------------------------------------------------------

发送路由配置(Transmit Routing Configuration)


发送路由支持IF和TP两种方式，均支持1:1和1:N路由，为每一个PduRDestPdu配置一个PduRRoutingPath（1:N时N个Path共享同一PduRSrcPduRef）。

Transmit routing supports both IF and TP modes, both supporting 1:1 and 1:N routing. Configure one PduRRoutingPath per PduRDestPdu (in 1:N, N paths share the same PduRSrcPduRef).

- **IF发送**：PduRRouteType = IF。上层调用 :code:`PduR_<Up>Transmit` 或下层通过 :code:`PduR_<Lo>TriggerTransmit` 请求发送。

  **IF Tx**: PduRRouteType = IF. Upper layer calls :code:`PduR_<Up>Transmit` or lower layer triggers via :code:`PduR_<Lo>TriggerTransmit`.

- **TP发送**：PduRRouteType = TP。上层调用 :code:`PduR_<Up>Transmit`，下层分片获取数据。

  **TP Tx**: PduRRouteType = TP. Upper layer calls :code:`PduR_<Up>Transmit`; lower layer retrieves data segments.

涉及容器与关键参数：(Containers and Key Parameters:)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 20 25 30 25
   :header-rows: 1

   * - 容器(Container)
     - 参数(Parameter)
     - 说明(Description)
     - 适用路由/是否必须(Route/Required)

   * - PduRSrcPdu
     - PduRSrcPduRef
     - 关联EcuC中与上层模块Tx PDU对应的PDU(Associates EcuC PDU corresponding to upper-layer module Tx PDU)
     - IF/TP 必须(Required)

   * - PduRSrcPdu
     - PduRSrcPduUpTxConf
     - 是否支持IF发送确认(Whether IF TxConfirmation is supported)
     - 仅IF 可选(IF Only Optional)

   * - PduRDestPdu
     - PduRDestPduRef
     - 关联EcuC中与下层IF/TP模块Tx PDU对应的PDU(Associates EcuC PDU corresponding to lower-layer IF/TP module Tx PDU)
     - IF/TP 必须(Required)

   * - PduRDestPdu
     - PduRTransmissionConfirmation
     - 是否支持TxConfirmation(Whether TxConfirmation is supported)
     - 仅IF 可选(IF Only Optional)

   * - PduRRoutingPath
     - PduRRouteType
     - 路由类型：IF或TP(Route type: IF or TP)
     - IF/TP 必须(Required)

   * - PduRRoutingPath
     - PduRSrcPduRRef
     - 关联PduRSrcPdu(Associates PduRSrcPdu)
     - IF/TP 必须(Required)

   * - PduRRoutingPath
     - PduRDestPduRRef
     - 关联PduRDestPdu(Associates PduRDestPdu)
     - IF/TP 必须(Required)

详细参数说明参见 :ref:`PduRSrcPdu配置`、 :ref:`PduRDestPdu配置`、 :ref:`PduRRoutingPath配置`。

See :ref:`PduRSrcPdu配置`, :ref:`PduRDestPdu配置`, :ref:`PduRRoutingPath配置` for detailed parameter descriptions.

接收路由配置(Receive Routing Configuration)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

接收路由支持IF和TP两种方式，均支持1:1和1:N路由，IF额外支持N:1路由。为每一个PduRDestPdu配置一个PduRRoutingPath（1:N时N个Path共享同一PduRSrcPduRef）。

Receive routing supports both IF and TP modes, both supporting 1:1 and 1:N routing, with IF additionally supporting N:1 routing. Configure one PduRRoutingPath per PduRDestPdu (in 1:N, N paths share the same PduRSrcPduRef).

- **IF接收**：PduRRouteType = IF。下层通过 :code:`PduR_<Lo>RxIndication` 将接收报文传递给上层。

  **IF Rx**: PduRRouteType = IF. Lower layer forwards received messages to upper layer via :code:`PduR_<Lo>RxIndication`.

- **TP接收**：PduRRouteType = TP。下层通过 :code:`PduR_<LoTp>StartOfReception` → :code:`PduR_<LoTp>CopyRxData` → :code:`PduR_<LoTp>RxIndication` 完成TP PDU接收流程。

  **TP Rx**: PduRRouteType = TP. Lower layer completes TP PDU reception via :code:`PduR_<LoTp>StartOfReception` → :code:`PduR_<LoTp>CopyRxData` → :code:`PduR_<LoTp>RxIndication`.

涉及容器与关键参数：(Containers and Key Parameters:)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 20 25 30 25
   :header-rows: 1

   * - 容器(Container)
     - 参数(Parameter)
     - 说明(Description)
     - 适用路由/是否必须(Route/Required)

   * - PduRSrcPdu
     - PduRSrcPduRef
     - 关联EcuC中与下层IF/TP模块Rx PDU对应的PDU(Associates EcuC PDU corresponding to lower-layer IF/TP module Rx PDU)
     - IF/TP 必须(Required)

   * - PduRDestPdu
     - PduRDestPduRef
     - 关联EcuC中与上层模块Rx PDU对应的PDU(Associates EcuC PDU corresponding to upper-layer module Rx PDU)
     - IF/TP 必须(Required)

   * - PduRRoutingPath
     - PduRRouteType
     - 路由类型：IF或TP(Route type: IF or TP)
     - IF/TP 必须(Required)

   * - PduRRoutingPath
     - PduRSrcPduRRef
     - 关联PduRSrcPdu(Associates PduRSrcPdu)
     - IF/TP 必须(Required)

   * - PduRRoutingPath
     - PduRDestPduRRef
     - 关联PduRDestPdu(Associates PduRDestPdu)
     - IF/TP 必须(Required)

详细参数说明参见 :ref:`PduRSrcPdu配置`、 :ref:`PduRDestPdu配置`、 :ref:`PduRRoutingPath配置`。

See :ref:`PduRSrcPdu配置`, :ref:`PduRDestPdu配置`, :ref:`PduRRoutingPath配置` for detailed parameter descriptions.

网关路由配置(Gateway Routing Configuration)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

网关路由支持IF和TP两种方式，均支持1:1、1:N、N:1路由。为每一个PduRDestPdu配置一个PduRRoutingPath（1:N时N个Path共享同一PduRSrcPduRef）。

Gateway routing supports both IF and TP modes, both supporting 1:1, 1:N, and N:1 routing. Configure one PduRRoutingPath per PduRDestPdu (in 1:N, N paths share the same PduRSrcPduRef).

- **IF网关**：PduRRouteType = IF。PduRDestPduDataProvision = PDUR_TRIGGERTRANSMIT 时必须配置queue和PduRDefaultValueElement；PDUR_DIRECT时queue可选。

  **IF Gateway**: PduRRouteType = IF. When PduRDestPduDataProvision = PDUR_TRIGGERTRANSMIT, queue and PduRDefaultValueElement are required; optional for PDUR_DIRECT.

- **TP网关**：PduRRouteType = TP。必须配置queue。可配置PduRTpThreshold实现on-the-fly gatewaying（1:N时同一PduRSrcPduRef最多一个Path配置阈值）。

  **TP Gateway**: PduRRouteType = TP. Queue is required. PduRTpThreshold enables on-the-fly gatewaying (max one path per PduRSrcPduRef in 1:N).

涉及容器与关键参数：(Containers and Key Parameters:)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 20 25 30 25
   :header-rows: 1

   * - 容器(Container)
     - 参数(Parameter)
     - 说明(Description)
     - 适用路由/是否必须(Route/Required)

   * - PduRSrcPdu
     - PduRSrcPduRef
     - 关联EcuC中与下层IF/TP模块Rx PDU对应的PDU(Associates EcuC PDU corresponding to lower-layer IF/TP module Rx PDU)
     - IF/TP 必须(Required)

   * - PduRDestPdu
     - PduRDestPduRef
     - 关联EcuC中与下层IF/TP模块Tx PDU对应的PDU(Associates EcuC PDU corresponding to lower-layer IF/TP module Tx PDU)
     - IF/TP 必须(Required)

   * - PduRDestPdu
     - PduRDestPduDataProvision
     - IF网关数据提供方式：PDUR_DIRECT或PDUR_TRIGGERTRANSMIT(IF gateway data provision: PDUR_DIRECT or PDUR_TRIGGERTRANSMIT)
     - 仅IF 必须(IF Only Required)

   * - PduRDestPdu
     - PduRTransmissionConfirmation
     - 是否支持IF发送确认(Whether IF TxConfirmation is supported)
     - 仅IF 可选(IF Only Optional)

   * - PduRRoutingPath
     - PduRRouteType
     - 路由类型：IF或TP(Route type: IF or TP)
     - IF/TP 必须(Required)

   * - PduRRoutingPath
     - PduRSrcPduRRef
     - 关联PduRSrcPdu(Associates PduRSrcPdu)
     - IF/TP 必须(Required)

   * - PduRRoutingPath
     - PduRDestPduRRef
     - 关联PduRDestPdu(Associates PduRDestPdu)
     - IF/TP 必须(Required)

   * - PduRRoutingPath
     - PduRQueueDepth
     - 队列深度，TP网关和PDUR_TRIGGERTRANSMIT必须配置(Queue depth, required for TP gateway and PDUR_TRIGGERTRANSMIT)
     - TP必须 / IF条件必须(TP Required / IF Conditional Required)

   * - PduRRoutingPath
     - PduRTpThreshold
     - on-the-fly网关阈值，超过该阈值开始转发(On-the-fly gateway threshold; forwarding starts when received data exceeds this value)
     - 仅TP 可选(TP Only Optional)

   * - PduRRoutingPath
     - PduRDestBufferRef
     - 关联PduRBuffer，配置私有Buffer(Associates PduRBuffer for dedicated buffer)
     - 仅TP 可选(TP Only Optional)

   * - PduRDefaultValueElement
     - PduRDefaultValueElement
     - PDU默认值，PDUR_TRIGGERTRANSMIT必须配置(PDU default value, required for PDUR_TRIGGERTRANSMIT)
     - 仅IF 条件必须(IF Only Conditional Required)

详细参数说明参见 :ref:`PduRSrcPdu配置`、 :ref:`PduRDestPdu配置`、 :ref:`PduRRoutingPath配置`、 :ref:`PduRDefaultValueElement配置`、 :ref:`PduRBuffer配置`。

See :ref:`PduRSrcPdu配置`, :ref:`PduRDestPdu配置`, :ref:`PduRRoutingPath配置`, :ref:`PduRDefaultValueElement配置`, :ref:`PduRBuffer配置` for detailed parameter descriptions.

路由控制配置(Routing Control Configuration)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

路由控制通过PduRRoutingPathGroup间接控制PduRDestPdu的使能状态：(Routing control indirectly controls PduRDestPdu enable state via PduRRoutingPathGroup:)

#. RoutingPathGroup通过PduRIsEnabledAtInit决定初始使能状态；运行时通过PduR_EnableRouting/PduR_DisableRouting动态控制

   RoutingPathGroup initial enable state determined by PduRIsEnabledAtInit; runtime control via PduR_EnableRouting/PduR_DisableRouting

#. PduRRoutingPath通过PduRRoutingPathGroupRef关联0..N个RoutingPathGroup

   PduRRoutingPath associates with 0..N RoutingPathGroups via PduRRoutingPathGroupRef

#. PduRDestPdu在未关联任何RoutingPathGroup或关联的至少一个RoutingPathGroup使能时为Enable，否则Disable

   PduRDestPdu enabled when unassociated or associated with ≥1 enabled RoutingPathGroup; otherwise disabled

#. 未关联任何RoutingPathGroup的PduRDestPdu初始化后永久Enable

   PduRDestPdu unassociated with any RoutingPathGroup remains permanently enabled after initialization

涉及容器与关键参数：(Containers and Key Parameters:)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 20 25 30 25
   :header-rows: 1

   * - 容器(Container)
     - 参数(Parameter)
     - 说明(Description)
     - 是否必须(Required)

   * - PduRRoutingPathGroup
     - PduRIsEnabledAtInit
     - 初始化后该RoutingPathGroup是否使能(Whether the RoutingPathGroup is enabled after initialization)
     - 是(Yes)

   * - PduRRoutingPathGroup
     - PduRRoutingPathGroupId
     - RoutingPathGroup的ID，工具自动填充(RoutingPathGroup ID, auto-assigned by tool)
     - 是(Yes)

   * - PduRRoutingPath
     - PduRRoutingPathGroupRef
     - 关联RoutingPathGroup(Associates RoutingPathGroup)
     - 否(No)

   * - PduRRoutingPath
     - PduRDestPduRRef
     - 关联PduRDestPdu(Associates PduRDestPdu)
     - 是(Yes)

   * - PduRRoutingPath
     - PduRRouteType
     - 配置为IF或TP(Set to IF or TP)
     - 是(Yes)

   * - PduRRoutingPath
     - PduRSrcPduRRef
     - 关联PduRSrcPdu(Associates PduRSrcPdu)
     - 是(Yes)

详细参数说明参见 :ref:`PduRRoutingPathGroup配置`、 :ref:`PduRRoutingPath配置`、 :ref:`PduRRoutingPaths配置`。

See :ref:`PduRRoutingPathGroup配置`, :ref:`PduRRoutingPath配置`, :ref:`PduRRoutingPaths配置` for detailed parameter descriptions.

----

工具参数手册(Tool Parameter Reference)
--------------------------------------------------------------


PduRGeneral配置(PduRGeneral Configuration)
----------------------------------------------------

*适用场景：模块级通用参数，所有场景均需配置。*

*Applicable scenarios: Module-level general parameters, required for all scenarios.*

.. figure:: /_static/参考手册(Module_Reference_Manual)/PduR/PduRGeneral.png
   :alt: fig_模块配置图(fig_Module Configuration Diagram)
   :name: PduR_general_configuration
   :align: center

   PduR通用配置(PduR General Configuration)

常规参数配置列表(General Parameter Configuration List)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 10 10 10 30 20
   :header-rows: 1

   * - 参数名称(Parameter Name)
     - 参数范围(Parameter Range)
     - 默认取值(Default Value)
     - 参数描述(Parameter Description)
     - 依赖关系(Dependencies)
	 
   * - PduRDevErrorDetect
     - TRUE/FALSE
     - FALSE
     - 是否使能DET开发错误检测(Enables DET development error detection)
     - 依赖于Det模块的支持(Requires Det module support)
	 
   * - PduRMetaDataSupport
     - TRUE/FALSE
     - FALSE
     - 是否使能MetaData机制(Enables metadata mechanism)
     - 路由表中源PDU和目标PDU的MetaData类型必须一致(Source and destination PDU metadata types must match in routing table)
	 
   * - PduRVersionInfoApi
     - TRUE/FALSE
     - FALSE
     - 是否使能获取模块软件版本(Enables module version information API)
     - 无(None)
	 
   * - PduRZeroCostOperation
     - TRUE/FALSE
     - FALSE
     - 是否使能PduR"透传模式"(Enables PduR transparent pass-through mode)
     - "透传模式"通常用于PduR上下层模块固定且一一对应，不涉及网关(Used when PduR upper/lower modules have fixed one-to-one mapping without gateway functionality)


PduRBswModules配置(PduRBswModules Configuration)
---------------------------------------------------------

*适用场景：定义PduR与上下层模块的交互接口，所有场景均需配置。*

*Applicable scenarios: Defines PduR interaction interfaces with upper/lower modules; required for all scenarios.*

.. figure:: /_static/参考手册(Module_Reference_Manual)/PduR/PduRBswModules.png
   :alt: fig_模块配置图(fig_Module Configuration Diagram)
   :name: PduRBswModules
   :align: center

   PduR Bsw Module Configuration

常规参数配置列表(General Parameter Configuration List)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Autosar架构下，各模块与PduR模块交互的API配置，工具已支持默认勾选(CDD模块除外)

In AUTOSAR architecture, API configurations for module interactions with PduR are pre-selected by default (except CDD modules)

.. list-table::
   :widths: 10 10 10 30 20
   :header-rows: 1

   * - 参数名称(Parameter Name)
     - 参数范围(Parameter Range)
     - 默认取值(Default Value)
     - 参数描述(Parameter Description)
     - 依赖关系(Dependencies)
	 
   * - PduRCancelReceive
     - TRUE/FALSE
     - TRUE
     - 模块是否支持接收取消(Whether the module supports reception cancellation)
     - PduRBswModuleRef关联TP模块时，该项才可配置(Configurable only when PduRBswModuleRef is associated with a TP module)
	 
   * - PduRCancelTransmit
     - TRUE/FALSE
     - TRUE
     - 模块是否支持发送取消(Whether the module supports transmission cancellation)
     - 无(None)
	 
   * - PduRCommunicationInterface
     - TRUE/FALSE
     - FALSE
     - 模块是否支持IF PDU传输(Whether the module supports IF Pdu transmission)
     - 根据PduRBswModuleRef关联的模块自动配置(Auto-configured based on PduRBswModuleRef association)
	 
   * - PduRCopyRxData
     - TRUE/FALSE
     - TRUE
     - 模块是否支持TP I-PDU数据段接收(Whether the module supports TP I-PDU data segment reception)
     - PduRBswModuleRef关联TP模块时，该项才可配置(Configurable only when PduRBswModuleRef is associated with a TP module)
	 
   * - PduRCopyTxData
     - TRUE/FALSE
     - TRUE
     - 模块是否支持TP I-PDU发送数据段拷贝(Whether the module supports TP I-PDU transmission data segment copying)
     - PduRBswModuleRef关联TP模块时，该项才可配置(Configurable only when PduRBswModuleRef is associated with a TP module)
	 
   * - PduRLowerModule
     - TRUE/FALSE
     - FALSE
     - 模块是否处于PduR下层(Whether the module is at the lower layer of PduR)
     - 根据PduRBswModuleRef关联的模块自动配置(Auto-configured based on PduRBswModuleRef association)
	 
   * - PduRRetransmission
     - TRUE/FALSE
     - TRUE
     - 模块是否支持TP PDU重传(Whether the module supports TP Pdu retransmission)
     - PduRBswModuleRef关联TP模块时，该项才可配置(Configurable only when PduRBswModuleRef is associated with a TP module)
	 
   * - PduRRxIndication
     - TRUE/FALSE
     - TRUE
     - 模块是否支持IF PDU接收(Whether the module supports IF Pdu reception)
     - PduRBswModuleRef关联IF模块时，该项才可配置(Configurable only when PduRBswModuleRef is associated with an IF module)
	 
   * - PduRStartOfReception
     - TRUE/FALSE
     - TRUE
     - 模块是否支持TP PDU接收(开始)(Whether the module supports TP Pdu reception (start))
     - PduRBswModuleRef关联TP模块时，该项才可配置(Configurable only when PduRBswModuleRef is associated with a TP module)
	 
   * - PduRTpRxIndication
     - TRUE/FALSE
     - TRUE
     - 模块是否支持TP接收指示(Whether the module supports TP reception indication)
     - PduRBswModuleRef关联TP模块时，该项才可配置(Configurable only when PduRBswModuleRef is associated with a TP module)
	 
   * - PduRTpTransmit
     - TRUE/FALSE
     - TRUE
     - 该模块是否支持TP PDU传输(Whether the module supports TP Pdu transmission)
     - PduRBswModuleRef关联TP模块时，该项才可配置(Configurable only when PduRBswModuleRef is associated with a TP module)

   * - PduRTpTxConfirmation
     - TRUE/FALSE
     - TRUE
     - 模块是否支持TP PDU发送确认(Whether the module supports TP Pdu transmission confirmation)
     - PduRBswModuleRef关联TP模块时，该项才可配置(Configurable only when PduRBswModuleRef is associated with a TP module)
	 
   * - PduRTransmit
     - TRUE/FALSE
     - TRUE
     - 模块是否支持IF PDU发送(Whether the module supports IF Pdu transmission)
     - PduRBswModuleRef关联IF模块时，该项才可配置(Configurable only when PduRBswModuleRef is associated with an IF module)
	 
   * - PduRTransportProtocol
     - TRUE/FALSE
     - FALSE
     - 模块是否支持TP传输(Whether the module supports TP transmission)
     - PduRBswModuleRef关联TP模块时，该项才可配置(Configurable only when PduRBswModuleRef is associated with a TP module)
	 
   * - PduRTriggertransmit
     - TRUE/FALSE
     - TRUE
     - 该模块是否支持IF PDU通过TriggerTransmit机制进行发送(Whether the module supports IF Pdu transmission through the TriggerTransmit mechanism)
     - PduRBswModuleRef关联IF模块时，该项才可配置(Configurable only when PduRBswModuleRef is associated with an IF module)
	 
   * - PduRTxConfirmation
     - TRUE/FALSE
     - TRUE
     - 该模块是否支持IF PDU发送确认(Whether the module supports IF Pdu transmission confirmation)
     - PduRBswModuleRef关联IF模块时，该项才可配置(Configurable only when PduRBswModuleRef is associated with an IF module)
   
   * - PduRUpperModule
     - TRUE/FALSE
     - FALSE
     - 模块是否处于PduR上层(Whether the module is at the upper layer of PduR)
     - 根据PduRBswModuleRef关联的模块自动配置(Auto-configured based on PduRBswModuleRef association)
   
   * - PduRBswModuleRef
     - 索引[Module](Index[Module])
     - 无(None)
     - 关联与PduR模块交互的上下层模块(Associates upper/lower modules interacting with PduR)
     - 根据配置工程中已添加的模块，才能索引(Indexable only based on pre-configured modules in project)

.. _PduRRoutingPaths配置:

PduRRoutingPaths配置(PduRRoutingPaths Configuration)
-----------------------------------------------------------------

*适用场景：路由容量限制参数，所有场景均需配置。*

*Applicable scenarios: Routing capacity limits; required for all scenarios.*

.. figure:: /_static/参考手册(Module_Reference_Manual)/PduR/PduRRoutingPaths.png
   :alt: fig_模块配置图(fig_Module Configuration Diagram)
   :name: PduRRoutingPaths
   :align: center

   PduR RoutingPaths Configuration

常规参数配置列表(List of General Parameter Configurations)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 10 10 10 30 20
   :header-rows: 1

   * - 参数名称(Parameter Name)
     - 参数范围(Parameter Range)
     - 默认取值(Default Value)
     - 参数描述(Parameter Description)
     - 依赖关系(Dependencies)
	 
   * - PduRConfigurationId
     - 0..65535
     - 0
     - 模块PB配置Id号(Module post-build configuration ID)
     - 当前不支持配置(Configuration not currently supported)
	 
   * - PduRMaxRoutingPathCnt
     - 0..65535
     - 20
     - 模块PB配置支持的最大路由路径数(Maximum routing paths supported in post-build configuration)
     - 对配置的路由路径数目进行限制及校验(Limits and validates configured routing path count)
	 
   * - PduRMaxRoutingPathGroupCnt
     - 0..65535
     - 0
     - 模块PB配置支持的最大路由路径组数(Maximum routing path groups supported in post-build configuration)
     - 对配置的路径路径组数目进行限制及校验，该数值决定可以新建几个PduRRoutingPathGroup(Limits and validates routing path group count; determines PduRRoutingPathGroup creation limit)

.. _PduRRoutingPathGroup配置:

PduRRoutingPathGroup配置(Configuration of PduRRoutingPathGroup)
-------------------------------------------------------------------

*适用场景：路由控制(Routing Control)。*

*Applicable scenarios: Routing Control.*

.. figure:: /_static/参考手册(Module_Reference_Manual)/PduR/PduRRoutingPathGroup.png
   :alt: fig_模块配置图(fig_Module Configuration Diagram)
   :name: PduRRoutingPathGroup
   :align: center

   PduR RoutingPath Group Configuration

常规参数配置列表(List of General Parameter Configurations)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 10 10 10 30 20
   :header-rows: 1

   * - 参数名称(Parameter Name)
     - 参数范围(Parameter Range)
     - 默认取值(Default Value)
     - 参数描述(Parameter Description)
     - 依赖关系(Dependencies)
	 
   * - PduRIsEnabledAtInit
     - TRUE/FALSE
     - FALSE
     - 初始化之后该RoutingPathGroup是否使能(Whether the RoutingPathGroup is enabled after initialization)
     - 无(None)

   * - PduRRoutingPathGroupId
     - 0..65535
     - 无(None)
     - 表示RoutingPathGroup的ID(RoutingPathGroup identifier)
     - 工具自动填充(从0开始，逐一递增)(Auto-assigned by tool (starts from 0, increments sequentially))

.. _PduRRoutingPath配置:

PduRRoutingPath配置(Configuration of PduRRoutingPath)
----------------------------------------------------------------

*适用场景：所有场景（发送路由/接收路由/网关路由/路由控制）。*

*Applicable scenarios: All scenarios (Transmit/Receive/Gateway/Routing Control).*

.. figure:: /_static/参考手册(Module_Reference_Manual)/PduR/PduRRoutingPath.png
   :alt: fig_模块配置图(fig_Module Configuration Diagram)
   :name: PduRRoutingPath
   :align: center

   PduR RoutingPath Configuration

常规参数配置列表(List of General Parameter Configurations)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 10 10 10 30 20
   :header-rows: 1

   * - 参数名称(Parameter Name)
     - 参数范围(Parameter Range)
     - 默认取值(Default Value)
     - 参数描述(Parameter Description)
     - 依赖关系(Dependencies)
	 
   * - PduRQueueDepth
     - 1..255
     - 无(None)
     - 定义此路由路径的缓存的深度(Defines buffer depth for this routing path)
     - 取值不能大于定义的所有buffer数目之和；可能需要配置队列的场景：① IF Direct网关可配可不配；② IF TriggerTransmit网关必须配置；③ TP网关必须配置；④ TP PDU网关同时接收到上层，接收也需要配置PduRBuffer(Cannot exceed total defined buffer count; Queue configuration scenarios: ① IF Direct gateway optional; ② IF TriggerTransmit gateway required; ③ TP gateway required; ④ TP PDU gateway receiving from upper layer requires PduRBuffer)
	 
   * - PduRTpThreshold
     - 0..65535
     - 无(None)
     - TP PDU on-the-fly网关时，接收到该配置阈值长度的报文后开始执行转发(For TP PDU on-the-fly gateway, starts forwarding after receiving message length reaches this threshold)
     - 该配置项只针对TP网关(TP gateway only)
	 
   * - PduRRouteType
     - IF/TP
     - IF
     - I-PDU路由类型选择(I-PDU routing type selection)
     - 依赖于I-PDU关联的模块对于该路由类型的支持(Depends on I-PDU associated module's routing type support)
	 
   * - PduRDestBufferRef
     - 索引[PduRBuffer](Index[PduRBuffer])
     - 无(None)
     - 关联PduRBuffer，仅被该PduRRoutingPath关联的PduRBuffer属于该PduRRoutingPath的私有buffer，不会被其它Path申请占用(Associates PduRBuffer; exclusively associated buffers are private to this path)
     - 当前Path的PduRQueueDepth配置且大于0(Requires PduRQueueDepth > 0 for current path)
	 
   * - PduRDestPduRRef
     - 索引[PduRDestPdu](Index[PduRDestPdu])
     - 无(None)
     - 关联PduRDestPdu配置(Associates PduRDestPdu configuration)
     - 无(None)
	 
   * - PduRRoutingPathGroupRef
     - 索引[PduRRoutingPathGroup](Index[PduRRoutingPathGroup])
     - 无(None)
     - 关联PduRRoutingPathGroup(Associates PduRRoutingPathGroup)
     - 无(None)
	 
   * - PduRSrcPduRRef
     - 索引[PduRSrcPdu](Index[PduRSrcPdu])
     - 无(None)
     - 关联PduRSrcPdu配置(Associates PduRSrcPdu configuration)
     - 无(None)

.. _PduRDefaultValueElement配置:

PduRDefaultValueElement配置(Configuration of PduRDefaultValueElement)
------------------------------------------------------------------------------

*适用场景：IF网关(PDUR_TRIGGERTRANSMIT)。*

*Applicable scenarios: IF Gateway (PDUR_TRIGGERTRANSMIT).*

.. figure:: /_static/参考手册(Module_Reference_Manual)/PduR/PduRDefaultValueElement.png
   :alt: fig_模块配置图(fig_Module Configuration Diagram)
   :name: PduRDefaultValueElement
   :align: center

   PduR Default Value Element Configuration

常规参数配置列表(List of General Parameter Configurations)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 10 10 10 30 20
   :header-rows: 1

   * - 参数名称(Parameter Name)
     - 参数范围(Parameter Range)
     - 默认取值(Default Value)
     - 参数描述(Parameter Description)
     - 依赖关系(Dependencies)
	 
   * - PduRDefaultValueElement
     - 0..255
     - 无(None)
     - I-PDU对应字节的默认值(I-PDU byte default value)
     - IF PDU通过TriggerTransmit方式网关时才需要配置；若配置了PduRDefaultValue，其配置的PduRDefaultValueElement字节长度需与ECUC中PDU的PduLength相等(Required for IF PDU TriggerTransmit gatewaying; configured PduRDefaultValueElement byte length must match ECUC PDU PduLength)
	 
   * - PduRDefaultValueElementBytePosition
     - 0..4294967294
     - 无(None)
     - 表示I-PDU字节偏移(I-PDU byte offset)
     - IF PDU通过TriggerTransmit方式网关时才需要配置；根据添加PduRDefaultValueElement依次从0自动递增(Required for IF PDU TriggerTransmit gatewaying; auto-increments from 0 with each added PduRDefaultValueElement)

.. _PduRSrcPdu配置:

PduRSrcPdu配置(Configuration of PduRSrcPdu)
-----------------------------------------------------

*适用场景：所有场景（发送路由/接收路由/网关路由）。*

*Applicable scenarios: All scenarios (Transmit/Receive/Gateway).*

.. figure:: /_static/参考手册(Module_Reference_Manual)/PduR/PduRSrcPdu.png
   :alt: fig_模块配置图(fig_Module Configuration Diagram)
   :name: PduRSrcPdu
   :align: center

   PduR Src Pdu Configuration

常规参数配置列表(List of General Parameter Configurations)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 10 10 10 30 20
   :header-rows: 1

   * - 参数名称(Parameter Name)
     - 参数范围(Parameter Range)
     - 默认取值(Default Value)
     - 参数描述(Parameter Description)
     - 依赖关系(Dependencies)
	 
   * - PduRSourcePduBlockSize
     - 1..4294967295
     - 无(None)
     - 接收TP继续接收所需的最小缓存(Minimum buffer required for TP reception continuation)
     - 依赖于对应PduRRoutingPath中PduRRouteType为TP的传输，当前不支持(Requires TP routing type in corresponding PduRRoutingPath; not currently supported)
	 
   * - PduRSourcePduHandleId
     - 0..PduIdType
     - 无(None)
     - 表示PduR中SrcPdu handle id(SrcPdu handle identifier in PduR)
     - 工具自动填充(从0开始，逐一递增)(Auto-assigned by tool (starts from 0, increments sequentially))
	 
   * - PduRSrcPduUpTxConf
     - TRUE/FALSE
     - TRUE
     - 表示该SrcPdu支持IF发送确认(Enables IF transmission confirmation for this SrcPdu)
     - 依赖于该SrcPdu所关联模块对IF TxConfirmation的支持(Requires IF TxConfirmation support from associated module)
	 
   * - PduRSrcPduRef
     - 索引[Pdu](Index[Pdu])
     - 无(None)
     - 关联EcuC中配置的PDU(Associates PDU configured in EcuC)
     - 依赖于EcuC中PDU的配置；Source PDU关联的ECUC PDU需与PduRBswModules中的某一PDU关联；PDU关联的ECUC中PDU的配置项PduLength必须配置；IF路由PDU不能关联TP PDU，TP路由的PDU不能关联IF PDU(Requires EcuC PDU configuration; ECUC PDU must associate with PduRBswModules PDU; PduLength must be configured; IF routing cannot associate TP PDU, TP routing cannot associate IF PDU)

.. _PduRDestPdu配置:

PduRDestPdu配置(Configuration of PduRDestPdu)
----------------------------------------------------

*适用场景：所有场景（发送路由/接收路由/网关路由）。*

*Applicable scenarios: All scenarios (Transmit/Receive/Gateway).*

.. figure:: /_static/参考手册(Module_Reference_Manual)/PduR/PduRDestPdu.png
   :alt: fig_模块配置图(fig_Module Configuration Diagram)
   :name: PduRDestPdu
   :align: center

   PduR Dest Pdu Configuration

常规参数配置列表(List of General Parameter Configurations)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 10 10 10 30 20
   :header-rows: 1

   * - 参数名称(Parameter Name)
     - 参数范围(Parameter Range)
     - 默认取值(Default Value)
     - 参数描述(Parameter Description)
     - 依赖关系(Dependencies)
	 
   * - PduRDestPduDataProvision
     - PDUR_DIRECT/PDUR_TRIGGERTRANSMIT
     - PDUR_DIRECT
     - IF PDU网关路由的数据传递方式选择(IF PDU gateway routing data provision method)
     - 若选择TriggerTransmit方式，对应的PduRRoutingPath必须配置PduRQueueDepth来对网关I-PDU进行队列缓存；PduRDestPduDataProvision配置为PDUR_DIRECT时，对应的PduRRoutingPath不能配置PduRDefaultValueElement(TriggerTransmit requires PduRQueueDepth for gateway I-PDU buffering; PDUR_DIRECT prohibits PduRDefaultValueElement configuration)
	 
   * - PduRDestPduHandleId
     - 0..PduIdType
     - 无(None)
     - 表示PduR中DestPdu handle id(DestPdu handle identifier in PduR)
     - 工具自动填充(从0开始，逐一递增)(Auto-assigned by tool (starts from 0, increments sequentially))
	 
   * - PduRTransmissionConfirmation
     - TRUE/FALSE
     - TRUE
     - 对于IF PDU发送/网关路由是否支持TxConfirmation(Enables TxConfirmation for IF PDU transmission/gateway routing)
     - 该配置项只针对IF发送/网关(IF transmission/gateway only)
	 
   * - PduRDestPduRef
     - 索引[Pdu](Index[Pdu])
     - 无(None)
     - 关联EcuC中配置的PDU(Associates PDU configured in EcuC)
     - 依赖于EcuC中PDU的配置；Dest PDU关联的ECUC PDU需与PduRBswModules中的某一PDU关联；PDU关联的ECUC中PDU的配置项PduLength必须配置；IF路由PDU不能关联TP PDU，TP路由的PDU不能关联IF PDU；TP路由中仅支持配置1个DestPdu(Requires EcuC PDU configuration; ECUC PDU must associate with PduRBswModules PDU; PduLength must be configured; IF routing cannot associate TP PDU, TP routing cannot associate IF PDU; TP routing supports only one DestPdu)

.. _PduRBuffer配置:

PduRBuffer配置(Configuration of PduRBuffer)
----------------------------------------------------

*适用场景：网关路由(Gateway)及TP接收(TP Receive)。*

*Applicable scenarios: Gateway routing and TP Receive.*

.. figure:: /_static/参考手册(Module_Reference_Manual)/PduR/PduRBuffer.png
   :alt: fig_模块配置图(fig_Module Configuration Diagram)
   :name: PduRBuffer
   :align: center

   PduR Buffer Configuration

常规参数配置列表(List of General Parameter Configurations)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 10 10 10 30 20
   :header-rows: 1

   * - 参数名称(Parameter Name)
     - 参数范围(Parameter Range)
     - 默认取值(Default Value)
     - 参数描述(Parameter Description)
     - 依赖关系(Dependencies)
	 
   * - PduRPduMaxLength
     - 1..4294967295
     - 1
     - Buffer的长度(Buffer length)
     - 如果被Buffer被PduRDestBufferRef关联，则长度应配置为关联的DestPDU的最大长度(IF PDU的最大长度/TP PDU的最大单播长度)；否则根据具体配置中可能使用PduRBuffer的PduRRoutingPath关联的PDU length决定；(If buffer associated with PduRDestBufferRef, length equals associated DestPDU maximum length (IF PDU max length/TP PDU max unicast length); otherwise determined by PDU length of potentially associated PduRRoutingPath)

PduRDemEventParameterRefs配置(Configuration of PduRDemEventParameterRefs)
----------------------------------------------------------------------------------

.. figure:: /_static/参考手册(Module_Reference_Manual)/PduR/PduRDemEventParameterRefs.png
   :alt: fig_模块配置图(fig_Module Configuration Diagram)
   :name: PduRDemEventParameterRefs
   :align: center

   PduR Dem Event Parameter Refs Configuration

常规参数配置列表(List of General Parameter Configurations)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 10 10 10 30 20
   :header-rows: 1

   * - 参数名称(Parameter Name)
     - 参数范围(Parameter Range)
     - 默认取值(Default Value)
     - 参数描述(Parameter Description)
     - 依赖关系(Dependencies)

   * - PDUR_ROUTING_PATH_BUFFER_OVERFLOW
     - references to DemEventParameter
     - 0..1
     - 缓冲区溢出事件参数索引(Buffer overflow event parameter index)
     - 依赖于Dem模块的支持(Requires Dem module support)
