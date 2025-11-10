=====================
LdCom
=====================




文档信息 Document Information
================================================

版本历史 Version History
--------------------------------------------------------------------------------

.. list-table::
   :widths: 10 20 20 20 20
   :header-rows: 1

   * - 日期(Date)
     - 作者(Author)
     - 版本(Version)
     - 状态(Status)
     - 说明(Description)

   * - 2024/11/26
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
--------------------------------------------------------------------------------

.. list-table::
   :widths: 10 10 30 10
   :header-rows: 1

   * - 编号(Number)
     - 分类(Classification)
     - 标题(Title)
     - 版本(Version)

   * - 1
     - Autosar
     - AUTOSAR_CP_EXP_LayeredSoftwareArchitecture.pdf
     - R23-11
   * - 2
     - Autosar
     - AUTOSAR_FO_TR_Glossary.pdf
     - R23-11
   * - 3
     - Autosar
     - AUTOSAR_CP_SWS_BSWGeneral.pdf
     - R23-11
   * - 4
     - Autosar
     - AUTOSAR_CP_SWS_RTE.pdf
     - R23-11
   * - 5
     - Autosar
     - AUTOSAR_CP_SWS_SoftwareClusterConnection.pdf
     - R23-11
   * - 6
     - Autosar
     - AUTOSAR_CP_SWS_PDURouter.pdf
     - R23-11
   * - 7
     - Autosar
     - AUTOSAR_CP_SWS_DefaultErrorTracer.pdf
     - R23-11
   * - 8
     - Autosar
     - AUTOSAR_CP_SRS_BSWGeneral.pdf
     - R23-11
   * - 9
     - Autosar
     - AUTOSAR_CP_SRS_COM.pdf
     - R23-11
   * - 10
     - Autosar
     - AUTOSAR_CP_TPS_SystemTemplate.pdf
     - R23-11
   * - 11
     - Autosar
     - AUTOSAR_CP_TPS_ECUConfiguration
     - R23-11

术语与简写 Terms and Abbreviations
============================================================

术语 Terms
----------------------------------------------------------------
None


简写 Abbreviations
----------------------------------------------------------------

.. list-table::
   :widths: 10 40 30
   :header-rows: 1

   * - 简写(Abbreviation)
     - 全称(Full name)
     - 解释(Explanation)

   * - DET
     - Default Error Tracer
     - 开发错误检测
   * - I-PDU
     - Interaction Layer Protocol Data Unit
     - 交互式协议数据单元
   * - LdCom
     - LargeDataCOM
     - "大数据信号"通信模块

简介 Introduction
================================


LdCom 模块主要实现用户(RTE)与 PduR 之间 I-PDU 的传递作用，实现 IF PDU 与 TP PDU 的发送与接收传递。所谓的“Large Data”指的是每个 Pdu即为一个信号，而非大数据的 PDU， LdCom 只执行简单的 Pdu 收发，不涉及信号解析。

The LdCom module is mainly used for transmitting I-PDU between users (RTE) and PduR, to realize transmission and reception of IF PDU and TP PDU. The so-called "Large Data" means each Pdu is a signal, rather than a PDU of big data. LdCom performs simple Pdu transmission and receiving only with no signal parsing.

模块架构 Module architecture

.. figure:: ../../../_static/参考手册/LdCom/LdCom_Autosar_Architecture.png
   :alt: LdCom模块层次图 (LdCom Module Layer Diagram)
   :name: LdCom_AUTOSAR_Arch
   :align: center

   LdComArchitecture in AUTOSAR



如图 :ref:`LdCom_AUTOSAR_Arch` 所示, LdCom 模块处于 AUTOSAR 架构中的通信服务层，其下层模块为 PduR 模块，上层模块为 RTE。

As shown in the figure :ref:`LdCom_AUTOSAR_Arch` , the LdCom module is in the communication service layer of the AUTOSAR architecture. The modules below and above it are PduR module and the RTE respectively.

LdCom 实现了与上下层模块间基于 I-PDU 传输的接口传递，包括 IF Pdu 的发送(Direct 发送/TriggerTransmit 发送)， IF Pdu 的接收， TP Pdu 的发送， TP Pdu的接收，以及 DET 检测报错。

LdCom can realize interface transfer based on I-PDU transmission between the modules of upper and lower layers, including sending IF Pdu (Direct sending/sending via TriggerTransmit), receiving IF Pdu, sending TP Pdu, receiving TP Pdu, and detecting DET errors.


功能描述 Functional Description
======================================================

特性 Features
------------------------------------------------------------

IF IPDU 发送合接收 IF IPDU Sending and Receiving
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

IF IPDU发送 IF IPDU Sending
******************************************************************************************************************************
LdCom 支持 IPdu 以 IF 方式进行发送， IF 方式发送存在两种形式：

LdCom sends IPdu in IF mode, which can be in two different modes:

1.直接调用 LdCom_Transmit 进行发送；

1.Call LdCom_Transmit directly for sending; 

2.下层调用 LdCom_TriggerTransmit 获取发送IPdu 数据进行发送。

2.Call LdCom_TriggerTransmit in lower layer to get sending IPdu data for sending.

若 IPdu 以 IF 方式进行发送，需配置 LdComIPdu 的 LdComApiType 为LDCOM_IF， LdComIPduDirection 为 LDCOM_SEND，若该 Pdu 上层模块支持发送确认需配置 LdComTxConfirmation，若支持 TriggerTransmit 方式发送，还需配置 LdComTxTriggerTransmit。

If IPdu is sent in IF mode, the LdComApiType of LdComIPdu should be configured asLDCOM_IF, and the LdComIPduDirection as LDCOM_SEND. If the upper layer module of the Pdu supports sending confirmation, LdComTxConfirmation should be configured. If sending by TriggerTransmit mode is supported, LdComTxTriggerTransmit is also required.

需要直接发送该 Pdu 时，用户直接调用 LdCom_Transmit 进行发送， LdCom 通过调用下层发送接口进行发送；若下层调用 LdCom_TriggerTransmit 获取发送数据时， LdCom 调用配置的 LdComTxTriggerTransmit 进行接口传递。

If the Pdu is sent directly, the user directly calls LdCom_Transmit to send it while LdCom sends it by calling the sending interface at the lower layer. If the lower layer calls LdCom_TriggerTransmit to get the sent data, LdCom calls the configured LdComTxTriggerTransmit for interface transmission.

发送完成之后，下层调用 LdCom_TxConfirmation， LdCom 调用配置的 LdComTxConfirmation 进行传递。

After the sending is completed, the lower layer calls LdCom_TxCConfirmation while LdCom calls the configured LdComTxConfirmation for transmission.


IF IPDU的接收 IF IPDU Receiving
******************************************************************************************************************************
LdCom 支持 IPdu 以 IF 方式进行接收，下层接收到 IPdu 数据时直接调用LdCom_RxIndication 传递给 LdCom。

LdCom receives IPdu in IF mode. If the lower layer receives IPdu data, it will directly call LdCom_SxCondition and transmit it to LdCom.

若 Pdu 以 IF 方式进行接收，需配置 LdComIPdu 的 LdComApiType 为LDCOM_IF， LdComIPduDirection 为 LDCOM_RECEIVE，配置LdComRxIndication。

If the Pdu is received in IF mode, LdComApiType of LdComIPdu is configured as LDCOM_IF and LdComIPduDirection as LDCOM_RECEIVE. LdComRxIndication is also required.

当下层调用 LdCom_RxIndication 时， LdCom 调用配置的 LdComRxIndication 进行传递。

When the lower layer calls LdCom_RxIndication, LdCom will call the configured LdComRxIndication for transmission.


TP IPDU 发送和接收 TP IPDU Sending and Receiving
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

TP IPDU 发送 TP IPDU Sending
******************************************************************************************************************************
LdCom 支持 IPdu 以 TP 方式进行发送，按 TP 发送流程 Transmit→N 次 CopyTxData→TpTxConfirmation 进行 IPdu 的发送。

LdCom can send IPdu in TP mode based on the TP sending process  Transmit → N times of CopyTxData → TpTxConfirmation.

若 IPdu 以 TP 方式进行发送，需配置 LdComIPdu 的 LdComApiType 为LDCOM_TP， LdComIPduDirection 为 LDCOM_SEND，配置LdComTpTxConfirmation 和 LdComTxCopyTxData。

If IPdu is sent in TP mode, LdComApiType of LdComIPdu should be configured as LDCOM_TP, and LdComIPduDirection as LDCOM_SND. LdComTpTxConfirmation and LdComTxCopyTxData are also required..

用户层调用 LdCom_Transmit 请求 IPdu 的发送，下层模块回调LdCom_CopyTxData 请求 IPdu 数据段的拷贝， LdCom 通过配置的 LdComTxCopyTxData 进行传递，当整个 IPdu 发送结束，下层调用LdCom_TpTxConfirmation， LdCom 通过配置的 LdComTpTxConfirmation 进行传递。

The user layer calls LdCom_Transmit to request the sending of IPdu, and the lower layer module calls LdCom_CopyTxData to request the copying of IPdu data segments. LdCom makes transmission via the configured LdComTxCopyTxData. When the entire IPdu is sent, the lower layer will call LdCom_TpTxConfirmation and LdCom will make transmission via the configured LdComTpTxConfirmation.


TP IPDU 接收 TP IPDU Receiving
******************************************************************************************************************************
LdCom 支持 IPdu 以 TP 方式进行接收，按 TP 接收流程 StartOfReception→N次 CopyRxData→TpRxIndication 进行 IPdu 的接收。

LdCom can receive IPdu in TP mode based on the TP receiving process   StartOfReception → N times of CopyRxData → TpRxIndication.

若 IPdu 以 TP 方式进行接收，需配置 LdComIPdu 的 LdComApiType 为 LDCOM_TP， LdComIPduDirection 为 LDCOM_RECEIVE，配置LdComRxStartOfReception、 LdComRxCopyRxData 和 LdComTpRxIndication。

If IPdu is received in TP mode, LdComApiType of LdComIPdu should be configured as LDCOM_TP, and LdComIPduDirection as LDCOM_RECEIVE. LdComRxStartOfReception, LdComRxCopyRxData, and LdComTpRxIndication are also required.

下层模块调用 LdCom_StartOfReception， LdCom_CopyRxData，LdCom_TpRxIndication 时， LdCom 依次调用配置的 LdComRxStartOfReception, LdComRxCopyRxData, LdComTpRxIndication 进行传递。

When the lower level module calls LdCom_StartOfReception, LdCom_CpyRxData, and LdCom_TpRXIndication, LdCom will call the configured LdComRxStartOfReception, LdComRxCopyRxData, and LdComTpRxIndication in order for transmission.


偏差 Deviation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
1.调用上层(用户层)的回调接口暂不支持入参 LdComUserCbkHandleId，涉及到的回调接口有LdComUser_LdComCbkCopyTxData,
LdComUser_LdComCbkTpTxConfirmation,LdComUser_LdComCbkStartOfReception,LdComUser_LdComCbkCopyRxData,
LdComUser_LdComCbkTpRxIndication,LdComUser_LdComCbkRxIndication,LdComUser_LdComCbkTriggerTransmit,
LdComUser_LdComCbkTxConfirmation

1.The calling of the callback interface of the upper layer (user layer) does not support the inputting of LdComUserCbkHandleId as a parameter temporarily. 
The callback interfaces include LdComUser_LdComCbkCopyTxData,LdComUser_LdComCbkTpTxConfirmation,LdComUser_LdComCbkStartOfReception,
LdComUser_LdComCbkCopyRxData,LdComUser_LdComCbkTpRxIndication,LdComUser_LdComCbkRxIndication,
LdComUser_LdComCbkTriggerTransmit,LdComUser_LdComCbkTxConfirmation

2.配置工具中LdComIPdu的配置中增加了调用上层(用户层)回调接口配置，具体有LdComRxCopyRxData,LdComRxIndication,LdComRxStartOfReception,LdComTpRxIndication,
LdComTpTxConfirmation,LdComTxCopyTxData,LdComTxTriggerTransmit

2.The configuration of calling the callback interface of the upper layer (user layer is added in the configuration tool LdComIPdu, 
including LdComRxCopyRxData,LdComRxIndication,LdComRxStartOfReception,LdComTpRxIndication,
LdComTpTxConfirmation,LdComTxCopyTxData,LdComTxTriggerTransmit
   
3.配置工具暂未实现LdComUserModule,LdComUserUriDefSet,LdComUserModuleCnf,LdComUserCallback,LdComUserIPdu的配置

3.The configuration tool temporarily does not realize the configuration of LdComUserModule,LdComUserUriDefSet,LdComUserModuleCnf,LdComUserCallback,LdComUserIPdu

扩展 Extension
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
None

集成 Integration
==========================================

文件列表 File List
------------------------------------------------------------------

静态文件 Static Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - 文件(File)
     - 描述(Description)

   * - LdCom.c
     - LdCom模块功能实现文件(Function realization file of LdCom module) 

   * - LdCom.h
     - LdCom模块对外接口(除了回调函数)声明头文件(Declaration header file of external interface of LdCom (excluding callback functions))

   * - LdCom_Cbk.h
     - LdCom模块回调函数声明头文件(Declaration header file of callback function of LdCom module)

   * - LdCom_Internal.h
     - LdCom模块内部头文件(Internal header file of LdCom module)

   * - LdCom_Types.h
     - LdCom模块类型定义文件(Type definition file of LdCom module)


动态文件 Dynamic Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - LdCom_Cfg.h
     - LdCom模块PC配置宏定义(Macro definition of PC configuration of LdCom module)

   * - LdCom_Cfg.c
     - LdCom模块非PB配置数据变量定义(Variable definition of non-PB configuration data of LdCom module)

   * - LdCom_PBcfg.h
     - LdCom模块PB配置数据变量声明(Variable declaration of PB configuration data of LdCom module)

   * - LdCom_PBcfg.c
     - LdCom模块PB配置数据变量定义(Variable definition of PB configuration data of LdCom module)

错误处理 Error Handling
------------------------------------------------------------

开发错误 Development Errors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. list-table:: 
   :widths: 20 10 30
   :header-rows: 1

   * - Error code
     - Value[hex]
     - Description

   * - LDCOM_E_UNINIT
     - 0x02u
     - Error code if any other API service,except LdCom_GetVersionInfo is called before the AUTOSAR LdCom module was initialized with LdCom_Init or after a call to LdCom_Deinit

   * - LDCOM_E_PARAM_POINTER
     - 0x03u
     - API service called with a NULL pointer.In case of this error, the API service shall return immediately without any further action, except for reporting this development error.

   * - LDCOM_E_INVALID_PDU_SDU_ID 
     - 0x04u
     - API service called with wrong PDU-ID

   * - LDCOM_E_INVALID_SIGNAL_ID
     - 0x05u
     - API service called with wrong Signal-ID

   * - LDCOM_E_INIT_FAILED
     - 0x06u
     - Invalid configuration set selection 

产品错误 Product Errors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
None

运行时错误 Runtime Errors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
None

.. 引用接口描述。来自于code->doxygen->latex->rst
.. 引用接口描述。 From code->doxygen->latex->rst
.. include:: LdCom_api.rst




配置 Configuration
==========================================

.. figure:: ../../../_static/参考手册/LdCom/LdComIpdu_Cfg.png
   :alt: LdComIpduM配置 (LdComIpduM configuration)
   :name: LdComIpdu
   :align: center

   LdComIpdu Configuration

IF IPDU发送 IF IPDU Sending
------------------------------------------------------------------------------------
用户发送IF IPDU时，需要在LdComIPdu中配置LdComApiType为LDCOM_IF,LdComIPduDirection配置为LDCOM_SEND,LdComPduRef配置为发送Pdu,另外有两个可配置的回调接口LdComTxConfirmation和LdComTxTriggerTransmit，若用户层设计需要，则需要配置，分别用于用于收到来自底层的发送确认和来自底层请求发送的数据。

To send IF IPDU, the user should configure LdComApiType as LDCOM_IF, LdComIPduDirection as LDCOM_SND, and LdComPduRef as sending Pdu in LdCommIPdu. In addition, there are two configurable callback interfaces,LdComTxConfirmation and LdComTxTriggerTransmit. They can be configured, as long as they are required by the user layer design, to receive the sending confirmations from the underlying layer and data requests from the underlying layer respectively.

IF IPDU接收 IF IPDU Receiving
------------------------------------------------------------------------------------
接收IF IPDU时，需要在LdComIPdu中配置LdComApiType为LDCOM_IF,LdComIPduDirection配置为LDCOM_RECEIVE,LdComPduRef配置为接收的Pdu,另外有个可配置的回调接口LdComRxIndication，用于把接收到的数据通知给用户，若用户层设计需要，则需要配置。

To receive IF IPDU, the user should configure LdComApiType as LDCOM_IF, LdComIPduDirection as LDCOM_RECEIVE, LdComPduRef as the received Pdu in LdComIPdu. In addition, callback interface LdComRxIndication is also available, to notify the user of the received data. It needs configuring as long as it is required by the user layer design.

TP IPDU发送 TP IPDU Sending
------------------------------------------------------------------------------------
用户发送TP IPDU时，需要在LdComIPdu中配置LdComApiType为LDCOM_TP,LdComIPduDirection配置为LDCOM_SEND,LdComPduRef配置为发送Pdu,另外有两个可配置的回调接口LdComTpTxConfirmation和LdComTxCopyTxData需要配置，用于把来自底层的发送确认结果通知给用户层和向用户层请求发送数据。

To send TP IPDU, the user should configure LdComApiType as LDCOM_TP, LdComIPduDirection as LDCOM_SEND, and LdComPduRef as sending Pdu in LdCommIPdu. In addition, there are two configurable callback interfaces, LdComTpTxConfirmation and LdComTxCopyTxData, to notify the user layer of the sending confirmation results from the underlying layer and request the user layer to send data.

TP IPDU接收 TP IPDU Receiving
-----------------------------------------------------------------------------------
接收TP IPDU时，需要在LdComIPdu中配置LdComApiType为LDCOM_TP,LdComIPduDirection配置为LDCOM_RECEIVE,LdComPduRef配置为接收的Pdu,另外有三个可配置的回调接口LdComRxStartOfReception,LdComRxCopyRxData和LdComTpRxIndication，分别用于通知用户开始接收数据，把接收到的数据通知给用户和接收数据结果通知给用户。

To receive TP IPDU, the user should configure LdComApiType as LDCOM_TP, LdComIPduDirection as LDCOM_RECEIVE, and LdComPduRef as the received Pdu in LdComIPdu. In addition, there are three configurable callback interfaces, LdComRxStartOfReception, LdComRxCopyRxData and LdComTpRxIndicatio, to notify users to start receiving data, and notify users of the received data, and the received data results.



