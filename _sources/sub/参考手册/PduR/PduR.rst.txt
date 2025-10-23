===================
PduR
===================
.. 标题标识符“===”的长度必须要大于其内容的长度，否则会报错，其他标题亦是如此


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
   * - 2024/11/28
     - 赵彤（Zhao Tong）
     - V0.1
     - 发布（Release）
     - 首次发布（First release）
   * - 2025/04/04
     - 赵彤（Zhao Tong）
     - V1.0
     - 发布（Release）
     - 正式发布（Official release）

参考文档（Reference Document）
----------------------------------

.. list-table::
   :widths: 10 10 30 10
   :header-rows: 1

   * - 编号（Number）
     - 分类（Classification）
     - 标题（Title）
     - 版本（Version）
   * - 1
     - Autosar
     - AUTOSAR_CP_SRS_Gateway
     - R23-11
   * - 2
     - Autosar
     - AUTOSAR_CP_SWS_PDURouter.pdf
     - R23-11


术语与简写（Terms and Abbreviations）
========================================


术语（Term）
----------------------
   .. :align: center   表格内容居中


.. list-table::
   :widths: 10 40
   :header-rows: 1

   * - 术语（Term）
     - 解释（Explanation）

   * - on-the-fly gatewaying
     - 网关能力：在两个TP模块之间进行路由，在接收到所有数据之前（当达到指定阈值时）开始转发数据。
       
       Gateway capabilities: Route between two TP modules and start forwarding data before all data is received (when the specified threshold is reached).

   * - multicast operation
     - 多播路由，即1：N
       
       Multicast routing, i.e., 1:N

   * - data provision
     - 数据提供方式：direct data provision 和 trigger transmit data provision
       
       Data provision methods: direct data provision and trigger transmit data provision

   * - last-is-best buffering
     - Buffer策略：队列深度为1，后接收的数据回覆盖前面存储的数据
       
       Buffer strategy: The queue depth is 1, and the later received data will overwrite the previously stored data

   * - FIFO buffering
     - Buffer策略：队列深度大于1，采用First in first out
       
       Buffer strategy: The queue depth is greater than 1, using First In First Out

简写（Abbreviation）
------------------------

.. list-table::
   :widths: 10 20 30
   :header-rows: 1


   * - 简写（Abbreviation）
     - 全称（Full name）
     - 解释（Explanation）

   * - <SrcLo>
     - Lower layer communication interface module acting as a source of the I-PDU
     - 下层IF模块关联的PDU作为PduR中的Source I-PDU

   * - <DstLo>
     - Lower layer communication interface module acting as a destination of the I-PDU
     - 下层IF模块关联的PDU作为PduR中的Dest I-PDU

   * - <SrcLoTp>
     - Lower layer transport protocol module acting as a source of the I-PDU
     - 下层TP模块关联的PDU作为PduR中的Source I-PDU

   * - <DstLoTp>
     - Lower layer transport protocol module acting as a destination of the I-PDU
     - 下层TP模块关联的PDU作为PduR中的Dest I-PDU

   * - I-PDU ID
     - PDU Identifier
     - Pdu的Id号

   * - I-PDU
     - Interaction Layer PDU
     - 交互层Pdu，涉及Pdu的Id号，Pdu长度，Pdu数据

   * - Upper Layer Modules (Up)
     - Modules above the PDU Router
     - 在AUTOSAR架构下，处于PduR上层的模块

   * - Lower Layer Modules (Lo)
     - Modules below the PDU Router
     - 在AUTOSAR架构下，处于PduR下层的模块

   * - FIFO
     - first in first out
     - Buffer深度大于1，采用先入先出机制存储

   * - DET
     - Default Error Tracer
     - 错误检测模块

简介（Introduction）
============================


PduR模块主要为通信接口模块（如CanIf），传输协议模块（如CanTp），诊断服务模块（如Dcm），通信服务模块（如Com, LdCom），以及IpduM，SecOc等模块提供基于PDU的路由服务。PduR模块主要实现基于PDU的接收路由（PDU从CanIf→PduR→Com），发送路由(Com→PduR→CanIf)，网关路由功能（CanIf→PduR→CanIf）。

The PduR module mainly provides PDU-based routing services for communication interface modules (such as CanIf), transmission protocol modules (such as CanTp), diagnostic service modules (such as Dcm), communication service modules (such as Com, LdCom), as well as modules like IpduM and SecOc. The PduR module mainly implements PDU-based reception routing (PDU from CanIf→PduR→Com), transmission routing (Com→PduR→CanIf), and gateway routing functions (CanIf→PduR→CanIf).

.. figure:: ../../../_static/参考手册/PduR/简介.png
   :alt: fig_模块层次图
   :name: PduR_fig_arch
   :align: center

   PduR模块层次图

   PduR Module Hierarchy Diagram

与PduR模块存在交互的模块可分为三类：1.下层模块（如CanIf, CanTp）;2.上层模块（如Com, Dcm）;3既是上层又是下层模块（IpduM, SecOC）。
PduR与所有交互模块间实现IF Pdu和TP Pdu的接收与发送功能。

Modules that interact with the PduR module can be divided into three categories: 1. Lower-layer modules (such as CanIf, CanTp); 2. Upper-layer modules (such as Com, Dcm); 3. Modules that are both upper-layer and lower-layer (IpduM, SecOC).
The PduR and all interacting modules implement the receiving and sending functions of IF Pdu and TP Pdu


功能描述（Functional Description）
==========================================


特性（Features ）
--------------------------

发送路由功能（Transmit Routing Function）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TxPdu的发送分为两种方式（IF和TP），在PduR模块实现TP PDU的1：1发送路由，IF PDU的1：N发送路由。通过PduR模块的路由配置可以为上层屏蔽网络细节，上层模块专注于TxPdu报文数据的封装。

The transmission of TxPdu is divided into two modes (IF and TP). The PduR module implements 1:1 transmit routing for TP PDU and 1:N transmit routing for IF PDU. Through the routing configuration of the PduR module, network details can be shielded from the upper layer, allowing upper-layer modules to focus on encapsulating TxPdu message data.


接收路由功能（Receive Routing Function）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
RxPdu的接收分为两种方式（IF和TP），在PduR模块实现TP PDU的1：N发送路由，IF PDU的1：N路由。当PDU从下层模块接收到，根据PduR配置的路由路径传递到上层模块。上层模块不必关注网络细节，专注于接收PDU的解析。

The reception of RxPdu is divided into two modes (IF and TP). The PduR module implements 1:N transmit routing for TP PDU and 1:N routing for IF PDU. When a PDU is received from a lower-layer module, it is delivered to the upper-layer module according to the routing path configured by PduR. Upper-layer modules do not need to pay attention to network details and can focus on parsing the received PDU.


网关路由功能（Gateway Routing Function）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PDU的网关同样分为IF/TP两种方式，IF网关支持1：N，TP网关也支持1：N，不涉及任何报文数据的变化，收发报文速率保持一致（如果Dest端的报文长度小于Src端的报文长度，存在截断以使网关成功）。
需注意PDU的网关不能IF、TP混淆，即接收IF PDU只能通过发送IF PDU进行转发，接收TP PDU只能通过TP PDU进行转发。

The PDU gateway is also divided into IF/TP modes. The IF gateway supports 1:N, and the TP gateway also supports 1:N. It does not involve any changes in message data, and the sending and receiving message rates remain consistent (if the message length of the Dest end is less than that of the Src end, truncation occurs to ensure the gateway functions successfully).
It should be noted that the PDU gateway cannot mix IF and TP, that is, received IF PDUs can only be forwarded through sending IF PDUs, and received TP PDUs can only be forwarded through TP PDUs.


路由控制功能（Routing Control Function）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PduR的路由控制以RoutingPathGroup为单位进行Enable/Disable控制，而PduRRoutingPath通过PduRRoutingPathGroupRef可以关联N个RoutingPathGroup，只要关联的至少一个RoutingPathGroupEnable，则对应的PduRDestPdu使能。

The routing control of PduR performs Enable/Disable control in units of RoutingPathGroup. PduRRoutingPath can be associated with N RoutingPathGroups through PduRRoutingPathGroupRef. As long as at least one associated RoutingPathGroup is enabled, the corresponding PduRDestPdu is enabled.


.. only:: doc_pbs



  支持变体功能（Variant Support Function）
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  - 支持不同的转发路径
 
    Support different forwarding paths
 
  - 支持不同的数据提供方式
 
    Support different data provision methods
 
  - 支持不同的队列深度
 
    Support different queue depths
 
  - 支持不同的私有buffer
 
    Support different private buffers
 
  - 支持不同的路由组
 
    Support different routing groups
 
  - 支持不同的阈值on the fly gatewaying
 
    Support different thresholds for on-the-fly gatewaying

偏差
--------------

None

扩展
-------------

None

集成（Integration）
==========================

文件列表（File List）
----------------------------

静态文件（Static Files）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - 文件（File）
     - 描述（Description）
   
   * - PduR.c
     - 作为PduR模块的核心文件，实现PduR模块全部对外接口，以及实现PduR模块功能所必须的local变量定义、local函数定义和声明。
       
       As the core files of the PduR module, they implement all the external interfaces of the PduR module, as well as the definitions and declarations of local variables and local functions necessary for realizing the functions of the PduR module.

   * - PduR.h
     - 实现PduR模块全部外部接口的声明，以及配置文件中全局变量的声明，必要宏的定义。
       
       Implements the declarations of all external interfaces of the PduR module, as well as the declarations of global variables in the configuration files and the definitions of necessary macros.
        
   * - PduR_Route.c
     - 实现PduR模块Route功能需要使用到的全部内部接口函数定义、local函数声明。
       
       Implements the definitions of all internal interface functions and the declarations of local functions used for realizing the Route function of the PduR module.

   * - PduR_Route.h
     - 实现PduR模块Route功能需要使用到的全部内部接口函数声明。
       
       Implements the declarations of all internal interface functions used for realizing the Route function of the PduR module.

   * - PduR_Buffer.c
     - 实现PduR模块Buffer功能需要使用到的全部内部接口函数定义，以及实现Buffer功能所必须的local变量定义、local函数定义和声明。
       
       Implements the definitions of all internal interface functions used for realizing the Buffer function of the PduR module, as well as the definitions and declarations of local variables and local functions necessary for realizing the Buffer function.

   * - PduR_Buffer.h
     - 实现PduR模块Buffer功能需要使用到的全部内部接口函数声明。
       
       Implements the declarations of all internal interface functions used for realizing the Buffer function of the PduR module.

   * - PduR_Internal.c
     - 实现PduR模块内部全局变量的定义，内部接口的实现。
       
       Implements the definitions of internal global variables and the realization of internal interfaces of the PduR module.

   * - PduR_Internal.h
     - 实现PduR模块内部宏的定义，全局变量的声明，内部inline接口的实现。
       
       Implements the definitions of internal macros, the declarations of global variables, and the realization of internal inline interfaces of the PduR module.

   * - PduR_Types.h
     - 实现外部/内部类型的定义，包括AUTOSAR标准定义的类型，以及PB/PC配置参数结构体类型，以及内部运行时结构体类型。
       
       Implements the definitions of external/internal types, including types defined by the AUTOSAR standard, structure types of PB/PC configuration parameters, and internal runtime structure types.

   * - PduR_MemMap.h
     - 实现PduR模块内存布局。
       
       Implements the memory layout of the PduR module.

动态文件（Dynamic Files）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - 文件（File）
     - 描述（Description）
   
   * - PduR_Cfg.h
     - 定义PduR模块PC配置的宏定义
       
       Defines the macro definitions for the PC configuration of the PduR module

   * - PduR_Cfg.c
     - 定义PduR模块PC配置的结构体参数
       
       Defines the structure parameters for the PC configuration of the PduR module

   * - PduR_PBcfg.h
     - 定义PduR模块PB配置的宏定义
       
       Defines the macro definitions for the PB configuration of the PduR module

   * - PduR_PBcfg.c
     - 定义PduR模块PB配置的结构体参数
       
       Defines the structure parameters for the PB configuration of the PduR module

   * - PduR_<Module>.h
     - 实现Module需要调用的PduR接口宏定义
       
       Implements the macro definitions of PduR interfaces that need to be called by the Module

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

产品错误（Product Error）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
无

运行时错误（Runtime error）
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

.. 引用接口描述。来自于code->doxygen->latex->rst
.. include:: PduR_h_api.rst

配置（configuration）
==========================

发送路由配置（Transmit Routing Configuration）
--------------------------------------------------------------
IF PDU的发送：

Transmission of IF PDU:

  在PduR添加配置路由PduRRoutingPath，为每一个PduRDestPdu配置一个PduRRoutingPath（IF PDU 1：N路由场景就存在N个PduRRoutingPath，这N个PduRRoutingPath的PduRSrcPduRRef相同）。
  其中PduRRouteType配置为IF，配置项PduRSrcPduRRef关联一个PduRSrcPdu，该PduRSrcPdu通过PduRSrcPduRef关联的Pdu（EcuC）与上层模块发送TxPdu关联，
  配置项PduRDestPduRRef关联一个PduRDestPdu，该PduRDestPdu通过PduRDestPduRef关联的Pdu与下层IF模块关联。
  上层模块通过调用PduR_<User：Up>Transmit或者下层模块通过调用PduR_<User：Lo>TriggerTransmit（传递到上层）请求PDU的发送，
  发送成功后调用上层PduR_<User：Lo>TxConfirmation进行发送成功确认。

  Add and configure the routing PduRRoutingPath in PduR, and configure a PduRRoutingPath for each PduRDestPdu (in the case of IF PDU 1:N routing, there will be N PduRRoutingPaths, and these N PduRRoutingPaths have the same PduRSrcPduRRef).
  Among them, PduRRouteType is configured as IF, the configuration item PduRSrcPduRRef is associated with a PduRSrcPdu, and this PduRSrcPdu is associated with the TxPdu sent by the upper-layer module through the Pdu (EcuC) associated with PduRSrcPduRef.
  The configuration item PduRDestPduRRef is associated with a PduRDestPdu, and this PduRDestPdu is associated with the lower-layer IF module through the Pdu associated with PduRDestPduRef.
  The upper-layer module requests the transmission of PDU by calling PduR_User:UpTransmit, or the lower-layer module requests the transmission of PDU by calling PduR_User:LoTriggerTransmit (passed to the upper layer).
  After the transmission is successful, call the upper-layer PduR_User:LoTxConfirmation to confirm the successful transmission.

TP PDU的发送：

Transmission of TP PDU:

  在PduR添加配置路由PduRRoutingPath，为每一个PduRDestPdu配置一个PduRRoutingPath。其中PduRRouteType配置为TP，配置项PduRSrcPduRRef关联一个PduRSrcPdu，
  该PduRSrcPdu通过PduRSrcPduRef关联的Pdu（EcuC）与上层模块发送TxPdu关联，配置项PduRDestPduRRef关联一个PduRDestPdu，该PduRDestPdu通过PduRDestPduRef关联的Pdu与下层TP模块关联。
  上层模块通过调用PduR_<User：Up>Transmit请求PDU的发送，下层模块通过调用PduR_<User：LoTp>CopyTxData（传递到上层）来获取PDU发送数据段，
  下层模块通过调用PduR_<User：LoTp>TxConfirmation（传递到上层）通知上层发送结束（成功/失败）。

  Add and configure the routing PduRRoutingPath in PduR, and configure a PduRRoutingPath for each PduRDestPdu. Among them, PduRRouteType is configured as TP, the configuration item PduRSrcPduRRef is associated with a PduRSrcPdu,
  This PduRSrcPdu is associated with the TxPdu sent by the upper-layer module through the Pdu (EcuC) associated with PduRSrcPduRef. The configuration item PduRDestPduRRef is associated with a PduRDestPdu, and this PduRDestPdu is associated with the lower-layer TP module through the Pdu associated with PduRDestPduRef.
  The upper-layer module requests the transmission of PDU by calling PduR_User:UpTransmit, and the lower-layer module obtains the PDU transmission data segment by calling PduR_User:LoTpCopyTxData (passed to the upper layer).
  The lower-layer module notifies the upper layer of the end of transmission (success/failure) by calling PduR_User:LoTpTxConfirmation (passed to the upper layer).

接收路由配置（Receive Routing Configuration）
------------------------------------------------
IF PDU的接收：

Reception of IF PDU:

  在PduR添加配置路由PduRRoutingPath，为每一个PduRDestPdu配置一个PduRRoutingPath（1：N路由场景就存在N个PduRRoutingPath，这N个PduRRoutingPath的PduRSrcPduRRef相同）。
  其中PduRRouteType配置为IF，配置项PduRSrcPduRRef关联一个PduRSrcPdu，该PduRSrcPdu通过PduRSrcPduRef关联的Pdu（EcuC）与下层IF模块接收RxPdu关联，
  配置项PduRDestPduRRef关联一个PduRDestPdu，该PduRDestPdu通过PduRDestPduRef关联的Pdu与上层模块关联。下层模块通过调用PduR_<User：Lo>RxIndication将接收报文传递给上层。

  Add and configure the routing PduRRoutingPath in PduR, and configure a PduRRoutingPath for each PduRDestPdu (in the case of 1:N routing, there will be N PduRRoutingPaths, and these N PduRRoutingPaths have the same PduRSrcPduRRef).
  Among them, PduRRouteType is configured as IF, the configuration item PduRSrcPduRRef is associated with a PduRSrcPdu, and this PduRSrcPdu is associated with the RxPdu received by the lower-layer IF module through the Pdu (EcuC) associated with PduRSrcPduRef.
  The configuration item PduRDestPduRRef is associated with a PduRDestPdu, and this PduRDestPdu is associated with the upper-layer module through the Pdu associated with PduRDestPduRef. The lower-layer module passes the received message to the upper layer by calling PduR_User:LoRxIndication.

TP PDU的接收：

Reception of TP PDU:

  在PduR添加配置路由PduRRoutingPath，为每一个PduRDestPdu配置一个PduRRoutingPath（1：N路由场景就存在N个PduRRoutingPath，这N个PduRRoutingPath的PduRSrcPduRRef相同）。
  其中PduRRouteType配置为TP，配置项PduRSrcPduRRef关联一个PduRSrcPdu，该PduRSrcPdu通过PduRSrcPduRef关联的Pdu（EcuC）与下层TP模块接收RxPdu关联，
  配置项PduRDestPduRRef关联一个PduRDestPdu，该PduRDestPdu通过PduRDestPduRef关联的Pdu与上层模块关联。调用PduR_<User：LoTp>StartOfReception，
  PduR_<User：LoTp>CopyRxData，PduR_<User：LoTp>RxIndication完成TP PDU接收流程。

  Add and configure the routing PduRRoutingPath in PduR, and configure a PduRRoutingPath for each PduRDestPdu (in the case of 1:N routing, there will be N PduRRoutingPaths, and these N PduRRoutingPaths have the same PduRSrcPduRRef).
  Among them, PduRRouteType is configured as TP, the configuration item PduRSrcPduRRef is associated with a PduRSrcPdu, and this PduRSrcPdu is associated with the RxPdu received by the lower-layer TP module through the Pdu (EcuC) associated with PduRSrcPduRef.
  The configuration item PduRDestPduRRef is associated with a PduRDestPdu, and this PduRDestPdu is associated with the upper-layer module through the Pdu associated with PduRDestPduRef. Call PduR_User:LoTpStartOfReception,
  PduR_User:LoTpCopyRxData, PduR_User:LoTpRxIndication to complete the TP PDU reception process.

网关路由配置（Gateway Routing Configuration）
----------------------------------------------
IF PDU的网关：

Gateway of IF PDU:

  在PduR添加配置路由PduRRoutingPath，为每一个PduRDestPdu配置一个PduRRoutingPath（1：N路由场景就存在N个PduRRoutingPath，这N个PduRRoutingPath的PduRSrcPduRRef相同）。其中PduRRouteType配置为IF，配置项PduRSrcPduRRef关联一个PduRSrcPdu，该PduRSrcPdu通过PduRSrcPduRef关联的Pdu（EcuC）与下层IF模块接收RxPdu关联，配置项PduRDestPduRRef关联一个PduRDestPdu，该PduRDestPdu通过PduRDestPduRef关联的Pdu与下层IF模块发送TxPdu关联，若PduRDestPduRRef通过PduRDestPduRef关联的TxPdu发送方式为TriggerTransmit, 则相应PduRDestPdu的PduRDestPduDataProvision需配置为PDUR_TRIGGERTRANSMIT，反之配置为PDUR_DIRECT。若配置为PDUR_TRIGGERTRANSMIT则必须为该PduRRoutingPath配置queue，以及配置PduRDefaultValueElement来设置Pdu初始默认值。配置为PDUR_DIRECT时也可以选择配置queue，以降低丢帧概率。
  
  Add and configure the routing PduRRoutingPath in PduR, and configure a PduRRoutingPath for each PduRDestPdu (in the case of 1:N routing, there will be N PduRRoutingPaths, and these N PduRRoutingPaths have the same PduRSrcPduRRef). Among them, PduRRouteType is configured as IF, the configuration item PduRSrcPduRRef is associated with a PduRSrcPdu, and this PduRSrcPdu is associated with the RxPdu received by the lower-layer IF module through the Pdu (EcuC) associated with PduRSrcPduRef. The configuration item PduRDestPduRRef is associated with a PduRDestPdu, and this PduRDestPdu is associated with the TxPdu sent by the lower-layer IF module through the Pdu associated with PduRDestPduRef. If the transmission mode of the TxPdu associated with PduRDestPduRRef through PduRDestPduRef is TriggerTransmit, then PduRDestPduDataProvision of the corresponding PduRDestPdu must be configured as PDUR_TRIGGERTRANSMIT; otherwise, it is configured as PDUR_DIRECT. If configured as PDUR_TRIGGERTRANSMIT, a queue must be configured for this PduRRoutingPath, and PduRDefaultValueElement must be configured to set the initial default value of Pdu. When configured as PDUR_DIRECT, a queue can also be optionally configured to reduce the probability of frame loss.

  注意：queue的配置，①需要在相应的PduRRoutingPath中配置非0的PduRQueueDepth值；②添加PduRTxBuffer配置，没有被任何PduRRoutingPath关联的PduRTxBuffer属于Global buffer，存在资源抢占。仅被某一个PduRRoutingPath关联的PduRTxBuffer属于该PduRRoutingPath的Dedicated buffer，该PduRTxBuffer仅可以被该PduRRoutingPath申请；③PduRDestTxBufferRef可以关联最多PduRQueueDepth个PduRTxBuffer，也可以不关联任何PduRTxBuffer。

  Note: For queue configuration, ① a non-zero PduRQueueDepth value needs to be configured in the corresponding PduRRoutingPath; ② add PduRTxBuffer configuration. PduRTxBuffer not associated with any PduRRoutingPath belongs to the Global buffer, and there is resource preemption. PduRTxBuffer associated with only one PduRRoutingPath belongs to the Dedicated buffer of that PduRRoutingPath, and this PduRTxBuffer can only be applied for by that PduRRoutingPath; ③ PduRDestTxBufferRef can be associated with up to PduRQueueDepth PduRTxBuffers, or it can not be associated with any PduRTxBuffer.

TP PDU的网关：

Gateway of TP PDU:

  在PduR添加配置路由PduRRoutingPath，为每一个PduRDestPdu配置一个PduRRoutingPath（1：N路由场景就存在N个PduRRoutingPath，这N个PduRRoutingPath的PduRSrcPduRRef相同）。其中PduRRouteType配置为TP，配置项PduRSrcPduRRef关联一个PduRSrcPdu，该PduRSrcPdu通过PduRSrcPduRef关联的Pdu（EcuC）与下层TP模块接收RxPdu关联，配置项PduRDestPduRRef关联一个PduRDestPdu，该PduRDestPdu通过PduRDestPduRef关联的Pdu与下层TP模块发送TxPdu关联。若不希望等到全部RxPdu数据接收完成才开始执行转发，即希望通过“gatewaying-on-the-fly”方式进行转发，可通过配置PduRTpThreshold（1：N时只允许最多一个相同PduRSrcPduRRef的PduRRoutingPath配置阈值）来实现，当接收数据长度超过该阈值或者接收完成，则触发TxPdu进行转发。
  
  Add and configure the routing PduRRoutingPath in PduR, and configure a PduRRoutingPath for each PduRDestPdu (in the case of 1:N routing, there will be N PduRRoutingPaths, and these N PduRRoutingPaths have the same PduRSrcPduRRef). Among them, PduRRouteType is configured as TP, the configuration item PduRSrcPduRRef is associated with a PduRSrcPdu, and this PduRSrcPdu is associated with the RxPdu received by the lower-layer TP module through the Pdu (EcuC) associated with PduRSrcPduRef. The configuration item PduRDestPduRRef is associated with a PduRDestPdu, and this PduRDestPdu is associated with the TxPdu sent by the lower-layer TP module through the Pdu associated with PduRDestPduRef. If you do not want to wait for all RxPdu data to be received before starting forwarding, that is, you want to forward in the "gatewaying-on-the-fly" mode, you can configure PduRTpThreshold (in the case of 1:N, only one PduRRoutingPath with the same PduRSrcPduRRef is allowed to configure the threshold). When the received data length exceeds this threshold or the reception is completed, the TxPdu is triggered for forwarding.

  注意：TP PDU的网关必须配置queue；IF PDU的网关（PduRDestPduDataProvision为PDUR_TRIGGERTRANSMIT的路由必须配置queue；PDUR_DIRECT的路由不需要配queue，如果配置的话可以在一定程度上减少丢帧）

  Note: The gateway of TP PDU must be configured with a queue; for the gateway of IF PDU (the route with PduRDestPduDataProvision as PDUR_TRIGGERTRANSMIT must be configured with a queue; the route with PDUR_DIRECT does not need to be configured with a queue, but if configured, it can reduce frame loss to a certain extent)

路由控制配置（Routing Control Configuration）
-------------------------------------------------
基于下面原则：（Based on the following principles:）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#. RoutingPathGroup通过配置项PduRIsEnabledAtInit决定初始化之后，该RoutingPathGroup的使能状态

   RoutingPathGroup determines the enable state of the RoutingPathGroup after initialization through the configuration item PduRIsEnabledAtInit

#. 所有PduRRoutingPath通过PduRRoutingPathGroupRef会关联0..N个RoutingPathGroup

   All PduRRoutingPaths will be associated with 0..N RoutingPathGroups through PduRRoutingPathGroupRef

#. 如果该PduRRoutingPath未关联任何RoutingPathGroup 或者 关联的至少一个RoutingPathGroup处于使能状态，则该PduRRoutingPath对应的PduRDestPdu（唯一）为Enable，否则为Disable状态

   If the PduRRoutingPath is not associated with any RoutingPathGroup or is associated with at least one enabled RoutingPathGroup, then the PduRDestPdu (unique) corresponding to the PduRRoutingPath is in the Enable state; otherwise, it is in the Disable state

#. 运行时，通过调用PduR_EnableRouting/ PduR_DisableRouting来控制RoutingPathGroup的使能状态，从而间接控制PduRDestPdu使能状态

   During runtime, call PduR_EnableRouting/ PduR_DisableRouting to control the enable state of RoutingPathGroup, thereby indirectly controlling the enable state of PduRDestPdu

#. 未通过PduRRoutingPathGroupRef关联任何RoutingPathGroup的PduRDestPdu初始化之后其状态一直为Enable，不可改变

   The PduRDestPdu not associated with any RoutingPathGroup through PduRRoutingPathGroupRef will remain in the Enable state after initialization and cannot be changed

多分区控制配置（Multi-Partition Control Configuration）
----------------------------------------------------------
如果在工程中EcucPartition存在大于1个的配置，则认为该工程支持多分区 / 多核。
PduR共有三个独占区保护类型：

If there are more than one configurations for EcucPartition in the project, the project is considered to support multi-partition/multi-core.
PduR has three exclusive area protection types:

#. SchM_Enter_PduR_ExclusiveArea_Group是对于Group使能或者禁用的保护，因为一个group下的destpdu均属于一个分区，推荐使用禁中断方式ALL_INTERRUPT_BLOCKING

   SchM_Enter_PduR_ExclusiveArea_Group is for protecting the enabling or disabling of Group. Since the destpdus under a group belong to one partition, it is recommended to use the interrupt disabling method ALL_INTERRUPT_BLOCKING

#. SchM_Enter_PduR_ExclusiveArea_Route是对于PduRBuffer申请的保护，

   SchM_Enter_PduR_ExclusiveArea_Route is for protecting the application for PduRBuffer,

   - (推荐)如果所有需要配置PduRBuffer的PduRRoutingPath，均配置了私有buffer，且不存在共用私有buffer，则推荐使用禁中断方式ALL_INTERRUPT_BLOCKING；

     (Recommended) If all PduRRoutingPaths that need to configure PduRBuffer are configured with private buffers and there is no shared private buffer, it is recommended to use the interrupt disabling method ALL_INTERRUPT_BLOCKING;

   - 如果存在共用buffer且会同时申请buffer，则需要配置为OS_SPINLOCK;

     If there are shared buffers and they may apply for buffers at the same time, it needs to be configured as OS_SPINLOCK;

#. SchM_Enter_PduR_ExclusiveArea_Init是对于初始化时逻辑的保护，推荐使用禁中断方式ALL_INTERRUPT_BLOCKING

   SchM_Enter_PduR_ExclusiveArea_Init is for protecting the logic during initialization, and it is recommended to use the interrupt disabling method ALL_INTERRUPT_BLOCKING

配置（configuration）
==================================

PduRGeneral配置（PduRGeneral Configuration）
----------------------------------------------------

.. figure:: ../../../_static/参考手册/PduR/PduRGeneral.png
   :alt: fig_模块配置图
   :name: PduRGeneral
   :align: center

   PduR General Configuration

常规参数配置列表（List of General Parameter Configurations）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 10 10 10 30 20
   :header-rows: 1

   * - 参数名称（Parameter Name）
     - 参数范围（Parameter Range）
     - 默认取值（Default Value）
     - 参数描述（Parameter Description）
     - 依赖关系（Dependencies）
   * - PduRDevErrorDetect
     - TRUE/FALSE
     - FALSE
     - 是否使能DET开发错误检测
       
       Whether to enable DET development error detection
     - 依赖于Det模块的支持
       
       Depends on the support of the Det module
   * - PduRMetaDataSupport
     - TRUE/FALSE
     - FALSE
     - 是否使能MetaData机制
      
       Whether to enable the MetaData mechanism
     - 路由表中Soure Pdu和Dest Pdu的MetaData类型必须一致
      
       The MetaData types of Source Pdu and Dest Pdu in the routing table must be consistent
   * - PduRVersionInfoApi
     - TRUE/FALSE
     - FALSE
     - 是否使能获取模块软件版本
       
       Whether to enable obtaining the module software version
     - 无

       None
   * - PduRZeroCostOperation
     - TRUE/FALSE
     - FALSE
     - 是否使能PduR“透传模式”
       
       Whether to enable PduR "transparent transmission mode"
     - “透传模式”通常用于PduR上下层模块固定且一一对应，不涉及网关。
      
       The "transparent transmission mode" is usually used when the upper and lower modules of PduR are fixed and in one-to-one correspondence, and no gateway is involved.


PduRBswModules配置（PduRBswModules Configuration）
---------------------------------------------------------

.. figure:: ../../../_static/参考手册/PduR/PduRBswModules.png
   :alt: fig_模块配置图
   :name: PduRBswModules
   :align: center

   PduR Bsw Moduele Configuration

常规参数配置列表（List of General Parameter Configurations）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Autosar架构下，各模块与PduR模块交互的Api配置，工具已支持默认勾选（CDD模块除外）

In the Autosar architecture, the Api configuration for interaction between each module and the PduR module is supported by the tool with default checkmarks (except for the CDD module)

.. list-table::
   :widths: 10 10 10 30 20
   :header-rows: 1

   * - 参数名称（Parameter Name）
     - 参数范围（Parameter Range）
     - 默认取值（Default Value）
     - 参数描述（Parameter Description）
     - 依赖关系（Dependencies）
   * - PduRCancelReceive
     - TRUE/FALSE
     - TRUE
     - 模块是否支持接收取消
        
       Whether the module supports reception cancellation
     - PduRBswModuleRef关联TP模块时，该项才可配置
      
       Configurable only when PduRBswModuleRef is associated with a TP module
   * - PduRCancelTransmit
     - TRUE/FALSE
     - TRUE
     - 模块是否支持发送取消
      
       Whether the module supports transmission cancellation
     - 无

       None
   * - PduRCommunicationInterface
     - TRUE/FALSE
     - FALSE
     - 模块是否支持IF Pdu传输
      
       Whether the module supports IF Pdu transmission
     - 根据PduRBswModuleRef关联的模块自动配置
      
       Automatically configured according to the module associated with PduRBswModuleRef
   * - PduRCopyRxData
     - TRUE/FALSE
     - TRUE
     - 模块是否支持TP I-PDU数据段接收
      
       Whether the module supports TP I-PDU data segment reception
     - PduRBswModuleRef关联TP模块时，该项才可配置
      
       Configurable only when PduRBswModuleRef is associated with a TP module
   * - PduRCopyTxData
     - TRUE/FALSE
     - TRUE
     - 模块是否支持TP I-PDU发送数据段拷贝
      
       Whether the module supports TP I-PDU transmission data segment copying
     - PduRBswModuleRef关联TP模块时，该项才可配置
      
       Configurable only when PduRBswModuleRef is associated with a TP module
   * - PduRLowerModule
     - TRUE/FALSE
     - FALSE
     - 模块是否处于PduR下层
      
       Whether the module is at the lower layer of PduR
     - 根据PduRBswModuleRef关联的模块自动配置
      
       Automatically configured according to the module associated with PduRBswModuleRef
   * - PduRRetransmission
     - TRUE/FALSE
     - TRUE
     - 模块是否支持TP Pdu重传
      
       Whether the module supports TP Pdu retransmission
     - PduRBswModuleRef关联TP模块时，该项才可配置
      
       Configurable only when PduRBswModuleRef is associated with a TP module
   * - PduRRxIndication
     - TRUE/FALSE
     - TRUE
     - 模块是否支持IF Pdu接收
      
       Whether the module supports IF Pdu reception
     - PduRBswModuleRef关联IF模块时，该项才可配置
      
       Configurable only when PduRBswModuleRef is associated with an IF module
   * - PduRStartOfReception
     - TRUE/FALSE
     - TRUE
     - 模块是否支持TP Pdu接收（开始）
      
       Whether the module supports TP Pdu reception (start)
     - PduRBswModuleRef关联TP模块时，该项才可配置
      
       Configurable only when PduRBswModuleRef is associated with a TP module
   * - PduRTpRxIndication
     - TRUE/FALSE
     - TRUE
     - 模块是否支持TP接收指示
      
       Whether the module supports TP reception indication
     - PduRBswModuleRef关联TP模块时，该项才可配置
      
       Configurable only when PduRBswModuleRef is associated with a TP module
   * - PduRTpTransmit
     - TRUE/FALSE
     - TRUE
     - 该模块是否支持TP Pdu传输
       
       Whether the module supports TP Pdu transmission
     - PduRBswModuleRef关联TP模块时，该项才可配置
      
       Configurable only when PduRBswModuleRef is associated with a TP module
   * - PduRTpTxConfirmation
     - TRUE/FALSE
     - TRUE
     - 模块是否支持TP Pdu发送确认
      
       Whether the module supports TP Pdu transmission confirmation
     - PduRBswModuleRef关联TP模块时，该项才可配置
      
       Configurable only when PduRBswModuleRef is associated with a TP module
   * - PduRTransmit
     - TRUE/FALSE
     - TRUE
     - 模块是否支持IF Pdu发送
      
       Whether the module supports IF Pdu transmission
     - PduRBswModuleRef关联IF模块时，该项才可配置
      
       Configurable only when PduRBswModuleRef is associated with an IF module
   * - PduRTransportProtocol
     - TRUE/FALSE
     - FALSE
     - 模块是否支持TP传输
      
       Whether the module supports TP transmission
     - PduRBswModuleRef关联TP模块时，该项才可配置
      
       Configurable only when PduRBswModuleRef is associated with a TP module
   * - PduRTriggertransmit
     - TRUE/FALSE
     - TRUE
     - 该模块是否支持IF Pdu通过TriggerTransmit机制进行发送
      
       Whether the module supports IF Pdu transmission through the TriggerTransmit mechanism
     - PduRBswModuleRef关联IF模块时，该项才可配置
      
       Configurable only when PduRBswModuleRef is associated with an IF module
   * - PduRTxConfirmation
     - TRUE/FALSE
     - TRUE
     - 该模块是否支持IF Pdu发送确认
      
       Whether the module supports IF Pdu transmission confirmation
     - PduRBswModuleRef关联IF模块时，该项才可配置
      
       Configurable only when PduRBswModuleRef is associated with an IF module
   * - PduRUpperModule
     - TRUE/FALSE
     - FALSE
     - 模块是否处于PduR上层
       
       Whether the module is at the upper layer of PduR
     - 根据PduRBswModuleRef关联的模块自动配置
      
       Automatically configured according to the module associated with PduRBswModuleRef
   * - PduRBswModuleRef
     - 索引[Module]
    
       Index [Module]
     - 无

       None
     - 关联与PduR模块交互的上下层模块
      
       Associates the upper and lower modules that interact with the PduR module
     - 根据配置工程中已添加的模块，才能索引
      
       Can only be indexed based on the modules already added in the configuration project

PduRRoutingPaths配置（Configuration of PduRRoutingPaths）
-----------------------------------------------------------------

.. figure:: ../../../_static/参考手册/PduR/PduRRoutingPaths.png
   :alt: fig_模块配置图
   :name: PduRRoutingPaths
   :align: center

   PduR RoutingPaths Configuration

常规参数配置列表（List of General Parameter Configurations）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 10 10 10 30 20
   :header-rows: 1

   * - 参数名称（Parameter Name）
     - 参数范围（Parameter Range）
     - 默认取值（Default Value）
     - 参数描述（Parameter Description）
     - 依赖关系（Dependencies）
   * - PduRConfigurationId
     - 0 .. 65535
     - 0
     - 模块PB配置Id号
      
       Module PB Configuration ID Number
     - 当前不支持配置
      
       Configuration is not currently supported
   * - PduRMaxRoutingPathCnt
     - 0 .. 65535
     - 20
     - 模块PB配置支持的最大路由路径数
      
       The maximum number of routing paths supported by the module PB configuration
     - 对配置的路由路径数目进行限制及校验
      
       Restrict and verify the number of configured routing paths
   * - PduRMaxRoutingPathGroupCnt
     - 0 .. 65535
     - 0
     - 模块PB配置支持的最大路由路径组数
      
       The maximum number of routing path groups supported by the module PB configuration
     - 对配置的路径路径组数目进行限制及校验，该数值决定可以新建几个PduRRoutingPathGroup
      
       Restrict and verify the number of configured path groups, and this value determines how many PduRRoutingPathGroups can be created

PduRRoutingPathGroup配置（Configuration of PduRRoutingPathGroup）
-------------------------------------------------------------------

.. figure:: ../../../_static/参考手册/PduR/PduRRoutingPathGroup.png
   :alt: fig_模块配置图
   :name: PduRRoutingPathGroup
   :align: center

   PduR RoutingPaths Group Configuration

常规参数配置列表（List of General Parameter Configurations）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 10 10 10 30 20
   :header-rows: 1

   * - 参数名称（Parameter Name）
     - 参数范围（Parameter Range）
     - 默认取值（Default Value）
     - 参数描述（Parameter Description）
     - 依赖关系（Dependencies）
   * - PduRIsEnabledAtInit
     - TRUE/FALSE
     - FALSE
     - 初始化之后该RoutingPathGroup是否使能
      
       Whether the RoutingPathGroup is enabled after initialization
     - 无
      
       None
   * - PduRRoutingPathGroupId
     - 0..65535
     - 无

       None
     - 表示RoutingPathGroup的Id
      
       Represents the ID of the RoutingPathGroup
     - 工具自动填充（从0开始，逐一递增）
      
       Automatically populated by the tool (starting from 0 and incrementing one by one)

PduRRoutingPath配置（Configuration of PduRRoutingPath）
----------------------------------------------------------------

.. figure:: ../../../_static/参考手册/PduR/PduRRoutingPath.png
   :alt: fig_模块配置图
   :name: PduRRoutingPath
   :align: center

   PduR RoutingPath Configuration

常规参数配置列表（List of General Parameter Configurations）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 10 10 10 30 20
   :header-rows: 1

   * - 参数名称（Parameter Name）
     - 参数范围（Parameter Range）
     - 默认取值（Default Value）
     - 参数描述（Parameter Description）
     - 依赖关系（Dependencies）
   * - PduRQueueDepth
     - 1 .. 255
     - 无

       None
     - 定义此路由路径的缓存的深度
      
       Define the buffer depth of this routing path
     - 取值不能大于定义的所有buffer数目之和；可能需要配置队列的场景：① IF Direct网关可配可不配；② IF TriggerTransmit网关必须配置；③ Tp 网关必须配置；④ Tp Pdu网关同时接收到上层，接收也需要配置PduRBuffer
        
       The value cannot be greater than the sum of all defined buffer numbers; Scenarios where a queue may need to be configured: ① IF Direct gateway can be configured or not; ② IF TriggerTransmit gateway must be configured; ③ Tp gateway must be configured; ④ When the Tp Pdu gateway receives data from the upper layer at the same time, PduRBuffer also needs to be configured for reception
   * - PduRTpThreshold
     - 0 .. 65535
     - 无

       None
     - TP Pdu on-the-fly网关时，接收到该配置阈值长度的报文后开始执行转发
      
       For TP Pdu on-the-fly gateway, start forwarding after receiving a message with the length specified by this configured threshold
     - 该配置项只针对TP网关
      
       This configuration item is only for TP gateway
   * - PduRRouteType
     - IF/TP
     - IF
     - I-PDU路由类型选择
      
       Selection of I-PDU routing type
     - 依赖于I-PDU关联的模块对于该路由类型的支持
      
       Depends on the support of the module associated with the I-PDU for this routing type
   * - PduRDestBufferRef
     - 索引[PduRBuffer]
      
       Index [PduRBuffer]
     - 无

       None
     - 关联PduRBuffer，仅被该PduRRoutingPath关联的PduRBuffer属于该PduRRoutingPath的私有buffer，不会被其它Path申请占用
      
       Associated with PduRBuffer, the PduRBuffer associated only with this PduRRoutingPath belongs to the private buffer of this PduRRoutingPath and will not be applied for and occupied by other Paths
     - 当前Path的PduRQueueDepth 配置且大于 0
      
       The PduRQueueDepth of the current Path is configured and greater than 0
   * - PduRDestPduRRef
     - 索引[PduRDestPdu]
     - 无

       None
     - 关联PduRDestPdu配置
      
       Index [PduRDestPdu]
     - 无

       None
   * - PduRRoutingPathGroupRef
     - 索引[PduRRoutingPathGroup]
      
       Index [PduRRoutingPathGroup]
     - 无

       None
     - 关联PduRRoutingPathGroup
      
       Associated with PduRRoutingPathGroup
     - 无

       None
   * - PduRSrcPduRRef
     - 索引[PduRSrcPdu]
      
       Index [PduRSrcPdu]
     - 无

       None
     - 关联PduRSrcPdu配置
      
       Associated with PduRSrcPdu configuration
     - 无

       None

PduRDefaultValueElement配置（Configuration of PduRDefaultValueElement）
------------------------------------------------------------------------------

.. figure:: ../../../_static/参考手册/PduR/PduRDefaultValueElement.png
   :alt: fig_模块配置图
   :name: PduRDefaultValueElement
   :align: center

   PduR Default Value Element Configuration

常规参数配置列表（List of General Parameter Configurations）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 10 10 10 30 20
   :header-rows: 1

   * - 参数名称（Parameter Name）
     - 参数范围（Parameter Range）
     - 默认取值（Default Value）
     - 参数描述（Parameter Description）
     - 依赖关系（Dependencies）
   * - PduRDefaultValueElement
     - 0 .. 255
     - 无

       None
     - I-PDU对应字节的默认值
      
       Default value of the corresponding byte of I-PDU
     - IF Pdu通过TriggerTransmit方式网关时才需要配置; 若配置了PduRDefaultValue，其配置的PduRDefaultValueElement字节长度需与ECUC中Pdu的PduLength相等
      
       It only needs to be configured when the IF Pdu is gatewayed through the TriggerTransmit method; if PduRDefaultValue is configured, the byte length of the configured PduRDefaultValueElement must be equal to the PduLength of the Pdu in ECUC
   * - PduRDefaultValueElementBytePosition
     - 0 .. 4294967294(工具自动填充)

       0 .. 4294967294 (automatically populated by the tool)
     - 无

       None
     - 表示I-PDU字节偏移
      
       Represents the I-PDU byte offset
     - IF Pdu通过TriggerTransmit方式网关时才需要配置；根据添加PduRDefaultValueElement依次从0自动递增；
      
       It only needs to be configured when the IF Pdu is gatewayed through the TriggerTransmit method; it automatically increments from 0 in sequence according to the added PduRDefaultValueElement;

PduRSrcPdu配置（Configuration of PduRSrcPdu）
-----------------------------------------------------

.. figure:: ../../../_static/参考手册/PduR/PduRSrcPdu.png
   :alt: fig_模块配置图
   :name: PduRSrcPdu
   :align: center

   PduR Src Pdu Configuration

常规参数配置列表（List of General Parameter Configurations）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 10 10 10 30 20
   :header-rows: 1

   * - 参数名称（Parameter Name）
     - 参数范围（Parameter Range）
     - 默认取值（Default Value）
     - 参数描述（Parameter Description）
     - 依赖关系（Dependencies）
   * - PduRSourcePduBlockSize
     - 1 .. 4294967295
     - 无

       None
     - 接收TP继续接收所需的最小缓存
      
       Minimum buffer required for receiving TP to continue receiving
     - 依赖于对应PduRRoutingPath 中PduRRouteType为TP的传输，当前不支持
      
       Depends on the transmission where PduRRouteType in the corresponding PduRRoutingPath is TP, not currently supported
   * - PduRSourcePduHandleId
     - 0..PduIdType
     - 无

       None
     - 表示PduR中SrcPdu handle id
      
       Represents the SrcPdu handle id in PduR
     - 工具自动填充（从0开始，逐一递增）
      
       Automatically populated by the tool (starting from 0 and incrementing one by one)
   * - PduRSrcPduUpTxConf
     - TRUE/FALSE
     - TRUE
     - 表示该SrcPdu支持IF发送确认
      
       Indicates that the SrcPdu supports IF transmission confirmation
     - 依赖于该SrcPdu所关联模块对IF TxConfirmation的支持
      
       Depends on the support of IF TxConfirmation by the module associated with the SrcPdu
   * - PduRSrcPduRef
     - 索引[Pdu]
      
       Index [Pdu]
     - 无

       None
     - 关联EcuC中配置的Pdu
      
       Associates the Pdu configured in EcuC
     - 依赖于EcuC中Pdu的配置; Soure Pdu关联的ECUC Pdu需与PduRBswModules中的某一Pdu关联; Pdu关联的ECUC中Pdu的配置项PduLength必须配置；IF路由Pdu不能关联TP Pdu，TP路由的Pdu不能关联IF Pdu
      
       Depends on the configuration of Pdu in EcuC; The ECUC Pdu associated with the Source Pdu must be associated with a Pdu in PduRBswModules; The configuration item PduLength of the Pdu in ECUC associated with the Pdu must be configured; IF routing Pdu cannot be associated with TP Pdu, and TP routing Pdu cannot be associated with IF Pdu

PduRDestPdu配置（Configuration of PduRDestPdu）
----------------------------------------------------

.. figure:: ../../../_static/参考手册/PduR/PduRDestPdu.png
   :alt: fig_模块配置图
   :name: PduRDestPdu
   :align: center

   PduR Dest Pdu Configuration

常规参数配置列表（List of General Parameter Configurations）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 10 10 10 30 20
   :header-rows: 1

   * - 参数名称（Parameter Name）
     - 参数范围（Parameter Range）
     - 默认取值（Default Value）
     - 参数描述（Parameter Description）
     - 依赖关系（Dependencies）
   * - PduRDestPduDataProvision
     - PDUR_DIRECT/ PDUR_TRIGGERTRANSMIT
     - PDUR_DIRECT
     - IF Pdu网关路由的数据传递方式选择
      
       Selection of data transmission mode for IF Pdu gateway routing
     - 若选择TriggerTransmit方式，对应的PduRRoutingPath必须配置PduRQueueDepth来对网关I-PDU进行队列缓存; PduRDestPduDataProvision配置为PDUR_DIRECT时，对应的PduRRoutingPath不能配置PduRDefaultValueElement
      
       If the TriggerTransmit mode is selected, the corresponding PduRRoutingPath must configure PduRQueueDepth to queue and cache the gateway I-PDU; When PduRDestPduDataProvision is configured as PDUR_DIRECT, the corresponding PduRRoutingPath cannot configure PduRDefaultValueElement
   * - PduRDestPduHandleId
     - 0..PduIdType
     - 无

       None
     - 表示PduR中DestPdu handle id
      
       Represents the DestPdu handle id in PduR
     - 工具自动填充（从0开始，逐一递增）
      
       Automatically populated by the tool (starting from 0 and incrementing one by one)
   * - PduRTransmissionConfirmation
     - TRUE/FALSE
     - TRUE
     - 对于IF Pdu发送/网关路由是否支持TxConfirmation
      
       Whether TxConfirmation is supported for IF Pdu transmission/gateway routing
     - 该配置项只针对IF发送/网关
      
       This configuration item is only for IF transmission/gateway
   * - PduRDestPduRef
     - 索引[Pdu]

       Index [Pdu]
     - 无

       None
     - 关联EcuC中配置的Pdu
      
       Associates the Pdu configured in EcuC
     - 依赖于EcuC中Pdu的配置; Dest Pdu关联的ECUC Pdu需与PduRBswModules中的某一Pdu关联; Pdu关联的ECUC中Pdu的配置项PduLength必须配置；IF路由Pdu不能关联TP Pdu，TP路由的Pdu不能关联IF Pdu；TP路由中仅支持配置1个DestPdu
      
       Depends on the configuration of Pdu in EcuC; The ECUC Pdu associated with the Dest Pdu must be associated with a Pdu in PduRBswModules; The configuration item PduLength of the Pdu in ECUC associated with the Pdu must be configured; IF routing Pdu cannot be associated with TP Pdu, and TP routing Pdu cannot be associated with IF Pdu; Only one DestPdu can be configured in TP routing

PduRBuffer配置（Configuration of PduRBuffer）
----------------------------------------------------

.. figure:: ../../../_static/参考手册/PduR/PduRBuffer.png
   :alt: fig_模块配置图
   :name: PduRBuffer
   :align: center

   PduR Buffer Configuration

常规参数配置列表（List of General Parameter Configurations）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 10 10 10 30 20
   :header-rows: 1

   * - 参数名称（Parameter Name）
     - 参数范围（Parameter Range）
     - 默认取值（Default Value）
     - 参数描述（Parameter Description）
     - 依赖关系（Dependencies）
   * - PduRPduMaxLength
     - 1 .. 4294967295
     - 1
     - Buffer的长度
      
       Length of the Buffer
     - 如果被Buffer被PduRDestBufferRef关联，则长度应配置为关联的DestPdu的最大长度（IF Pdu的最大长度/TP Pdu的最大单播长度）；否则根据具体配置中可能使用PduRBuffer的PduRRoutingPath关联的PduR length决定；
      
       If the Buffer is associated with PduRDestBufferRef, its length should be configured as the maximum length of the associated DestPdu (maximum length of IF Pdu / maximum unicast length of TP Pdu); otherwise, it is determined by the PduR length associated with the PduRRoutingPath that may use the PduRBuffer in the specific configuration;
