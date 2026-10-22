SecOC
#################################

:strong:`缩写词注解 (Abbreviation Notes):`

.. list-table::
   :widths: 34 33 33
   :header-rows: 1

   * - 缩写词 (Abbreviation)
     - 解释/描述 (Explanation/Description)
     - 中文解释 (Chinese explanation)
   * - CSM
     - The AUTOSAR CryptoService Manager
     - AUTOSAR加密服务管理 (AUTOSAR Encryption Service Management)
   * - SecOC
     - Secure OnboardCommunication
     - 车载安全通信 (Vehicle Safety Communication)
   * - MAC
     - Message AuthenticationCode
     - 消息认证码 (Message Authentication Code)
   * - FV
     - Freshness Value
     - 新鲜度值 (Freshness Value)
   * - FVM
     - Freshness Value Manager
     - 新鲜度值管理器 (Freshness Value Manager)
   * - AuthenticI-PDU
     - An Authentic I-PDU is anarbitrary AUTOSAR I-PDUthe content of which issecured during networktransmission by means ofthe Secured I-PDU.
     - 用于进行安全认证的原始报文 (Original message used for security authentication)
   * - SecuredI-PDU
     - A Secured I-PDU is anAUTOSAR I-PDU thatcontains Payload of anAuthentic I-PDUsupplemented byadditional AuthenticationInformation.
     - 追加了认证信息的原始报文 (Original message with added authentication information)

简介 (Introduction)
=================================

SecOC模块对车载通信中的敏感数据进行身份验证和完整性保护。确保接收到的数据来自正确的ECU并且数据内容是正确的。

The SecOC module verifies and protects the integrity of sensitive data in vehicle communication. Ensuring that the received data comes from the correct ECU and that the content is accurate.

SecOC模块的目标是在PDU级别上实现资源效率高、可行的敏感数据认证机制。通常SecOC使用基于对称加密算法的MAC，同时SecOC的处理机制也可兼容非对称加密算法的使用。

The goal of the SecOC module is to implement an efficient and feasible mechanism for sensitive data authentication at the PDU level. Typically, SecOC uses MAC based on symmetric encryption algorithms, while the processing mechanism of SecOC can also accommodate the use of asymmetric encryption algorithms.

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/SecOC/image1.png
   :alt: SecOC模块示意图 (Diagram of the SecOC Module)
   :name: SecOC模块示意图 (Diagram of the SecOC Module)
   :align: center


参考资料 (Reference materials)
------------------------------------------

[1] AUTOSAR_SWS_SecureOnboardCommunication.pdf，R19-11

[2] AUTOSAR_SWS_PduRouter.pdf，R19-11

[3] AUTOSAR_SWS_CryptoServiceManager.pdf，R19-11

功能描述 (Function Description)
===========================================

基本概念 (Basic concepts)
-------------------------------------

Authentic I-PDU
===============================

Authentic I-PDU指需要进行保护以应对非法篡改和重放攻击的I-PDU。

Authentic I-PDU refers to I-PDU that needs to be protected against unauthorized tampering and replay attacks.

Secured I-PDU
=============================

Secured I-PDU由Authentic I-PDU和Authenticator (eg: MAC )组成。同时Secured IPDU中可以附加Secured I-PDU Header和FreshnessValue信息。Secured I-PDU Header指示Authentic I-PDU的长度，当没有Secured I-PDU Header时，Authentic I-PDU长度由配置获取。Freshness Value是在生成Authenticator时使用的新鲜度值。Authenticator为生成的认证信息。

Secured I-PDU consists of Authentic I-PDU and Authenticator (e.g., MAC). Additionally, Secured IPDU can include Secured I-PDU Header and FreshnessValue information. The Secured I-PDU Header indicates the length of the Authentic I-PDU; when there is no Secured I-PDU Header, the length of the Authentic I-PDU is obtained through configuration. The Freshness Value is a freshness value used when generating the Authenticator. The Authenticator is the generated authentication information.

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/SecOC/image2.png
   :alt: Secured I-PDU组成部分示意图 (Schematic Diagram of Secured I-PDU Components)
   :name: Secured I-PDU组成部分示意图 (Schematic Diagram of Secured I-PDU Components)
   :align: center


在创建Secured I-PDU时，SecOC支持截取部分FreshnessValue和Authenticator。截取的长度依据配置决定。

When creating a Secured I-PDU, SecOC supports truncating part of the FreshnessValue and Authenticator. The length of the truncation is determined by configuration.

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/SecOC/image3.png
   :alt: 截取FreshnessValue和Authentor组成Secured I-PDU示意图 (Capture FreshnessValue and Authentor to form a Secured I-PDU diagram.)
   :name: 截取FreshnessValue和Authentor组成Secured I-PDU示意图 (Capture FreshnessValue and Authentor to form a Secured I-PDU diagram.)
   :align: center


DataToAuthenticator
===================================

DataToAuthenticator指要传递给CSM模块，按照配置的加密算法进行MAC生成或者校验的数据。按照下列格式生成：

DataToAuthenticator refers to the data that needs to be passed to the CSM module for MAC generation or verification according to the configured encryption algorithm. It is generated in the following format:

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/SecOC/image4.png
   :alt: DataToAuthenticator数据格式 (DataToAuthenticator Data Format)
   :name: DataToAuthenticator数据格式 (DataToAuthenticator Data Format)
   :align: center


Freshness Values
================================

使用Freshness Values能保证生成Secured I-PDU的新鲜度。通常FreshnessValue由新鲜度管理器（FVM）管理，SecOC使用FreshnessValueId从FVM获取相应的新鲜度值。此外，新鲜度值可以从Authentic I-PDU中截取一部分作为新鲜度值，截取开始的位置和长度由配置确定。

Using Freshness Values ensures the freshness of newly generated Secured I-PDU. Typically, FreshnessValue is managed by the Freshness Value Manager (FVM), and SecOC retrieves the corresponding freshness value using FreshnessValueId from FVM. Additionally, freshness values can be extracted partially from Authentic I-PDU, with the starting position and length configured accordingly.

根据配置Secured I-PDU中可以不包含，包含完整或者部分的新鲜度值。

According to configuration, Secured I-PDU may not include, or may include full or partial freshness values.

PduCollection
=============================

PduCollection指Secured I-PDU由Authentic I-PDU和Cryptographic I-PDU两帧独立的报文组成。发送端将Authenticator放在Cryptographic I-PDU发送出去。接收端在接收到Authentic I-PDU和Cryptographic I-PDU后组合成一帧Secured I-PDU。

PduCollection refers to Secured I-PDU composed of two independent messages, Authentic I-PDU and Cryptographic I-PDU. The sender places the Authenticator in the Cryptographic I-PDU for transmission. Upon receiving both Authentic I-PDU and Cryptographic I-PDU, the receiver combines them into one frame of Secured I-PDU.

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/SecOC/image5.png
   :alt: Cryptographic I-PDU组成 (Cryptographic I-PDU Composition)
   :name: Cryptographic I-PDU组成 (Cryptographic I-PDU Composition)
   :align: center


MessageLinker
-----------------------------

在构造Cryptographic I-PDU时，可以将Authentic I-PDU的部分报文截取出来附加在最后，这段信息称为MessageLinker。接收时，SecOC需要首先校验接收到的Authentic I-PDU和Cryptographic I-PDU中的Message Linker是否匹配，校验通过后才进行下一步处理。MessageLinker的起始位置和长度由配置决定。

When constructing the Cryptographic I-PDU, part of the Authentic I-PDU payload can be extracted and appended at the end; this information is referred to as MessageLinker. Upon reception, SecOC needs to first validate whether the Message Linker in the received Authentic I-PDU matches that in the Cryptographic I-PDU; only if the validation passes will further processing proceed. The starting position and length of the MessageLinker are configurable.

MessageLinker是可选的。

MessageLinker is optional.

SecOC和PduR的关系 (The relationship between SecOC and PduR)
-----------------------------------------------------------------------

SecOC需要和PduR进行交互，用于获取和发送数据。

SecOC needs to interact with PduR for obtaining and sending data.

发送数据时，SecOC先作为PduR的下层模块，从PduR获取Authentic I-PDU，将Authentic I-PDU转换为Secured I-PDU之后，SecOC又作为PduR的上层模块，发送数据。

When sending data, SecOC first acts as a lower-layer module of PduR, obtaining Authentic I-PDU from PduR. After converting the Authentic I-PDU into Secured I-PDU, SecOC then acts as an upper-layer module of PduR to send the data.

接收数据时，SecOC先作为PduR的上层模块，从PduR接收Secured I-PDU。SecOC从Secured I-PDU中解析出Authentic I-PDU并通过校验之后，SecOC又作为PduR的下层模块，通过PduR将数据传递给上层。

When receiving data, SecOC first acts as a higher-layer module of PduR, receiving Secured I-PDU from PduR. After parsing out the Authentic I-PDU from the Secured I-PDU and validating it, SecOC then acts as a lower-layer module of PduR, passing the data up through PduR to the upper layer.

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/SecOC/image6.png
   :alt: SecOC和PduR关系示意图 (Diagram showing the relationship between SecOC and PduR)
   :name: SecOC和PduR关系示意图 (Diagram showing the relationship between SecOC and PduR)
   :align: center


认证I-PDU（发送）功能 (Authentication I-PDU (Send) Function)
--------------------------------------------------------------------

认证I-PDU过程即将Authentic I-PDU转化为Secured I-PDU的过程，主要有以下几个个步骤：

The authentication of I-PDU process converts Authenticated I-PDU into Secured I-PDU and mainly includes the following steps:

1.从上层获取Secured I-PDU

Retrieve Secured I-PDU from upper layer

2.创建DataToAuthenticator

CreateDataToAuthenticator

3.生成Authenticator

Generate Authenticator

4.构造Secured I-PDU

Construct Secured I-PDU

5.发送Secured I-PDU

Send Secured I-PDU

认证I-PDU功能实现 (Implementing Authentication I-PDU Function)
========================================================================

上层调用SecOC_IfTransmit()或者SecOC_TpTransmit()发起Secured I-PDU的发送过程。

The upper layer calls SecOC_IfTransmit() or SecOC_TpTransmit() to initiate the sending process of Secured I-PDU.

对于直接发送，SecOC从SecOC_IfTransmit()函数的PduInfo中获取Authentic I-PDU。对于TP发送，SecOC需要分多次调用PduR_SecOCTpCopyTxData()获取Authentic I-PDU。

For direct transmission, SecOC obtains the Authentic I-PDU from the PduInfo of the SecOC_IfTransmit() function. For TP transmission, SecOC needs to call PduR_SecOCTpCopyTxData() multiple times to obtain the Authentic I-PDU.

获取到Authentic I-PDU之后，SecOC根据配置的FreshnessValue相关属性，取得FreshnessValue，再根据DataToAuthenticator的生成规则，构建DataToAuthenticator。

After acquiring the Authentic I-PDU, SecOC obtains the FreshnessValue based on the configured related properties and then constructs DataToAuthenticator according to the generation rules of DataToAuthenticator.

SecOC调用CSM模块的接口，将DataToAuthenticator传递给CSM。CSM模块根据输入的DataToAuthenticator等参数，计算生成Authenticator。

SecOC invokes the interface of CSM module to pass DataToAuthenticator to CSM. The CSM module, based on inputs such as DataToAuthenticator, calculates and generates Authenticator.

生成Authenticator后，SecOC根据配置生成Secured I-PDU。之后SecOC调用PduR的发送接口将Secured I-PDU一次（If）或者多次（TP）发送出去。

After generating the Authenticator, SecOC generates the Secured I-PDU according to the configuration. Then, SecOC calls the sending interface of PduR to send out the Secured I-PDU once (If) or multiple times (TP).

校验I-PDU（接收）功能 (Validate I-PDU (Reception) Function)
-------------------------------------------------------------------

校验Secured I-PDU的过程主要包含以下几个步骤：

The process of validating Secured I-PDU mainly includes the following steps:

1. 从Secured I-PDU中解析出Authentic I-PDU，FreshnessValue以   及Authenticator

Parse out the Authentic I-PDU from Secured I-PDU, FreshnessValue as well as Authenticator

2. 从新鲜度值管理器（FVM）获取FreshnessValue

Get FreshnessValue from the Freshness Value Manager (FVM)

3. 创建DataToAuthenticator

CreateDataToAuthenticator

4. 校验认证信息（Authentication Information）

Validate Authentication Information

5. 向FVM发送确认信息

Send confirmation information to FVM

6. 将Authentic I-PDU传递给上层

Pass the Authentic I-PDU to the upper layer

校验I-PDU功能实现 (Implementing I-PDU Function Validation)
====================================================================

PduR收到需要校验的I-PDU时，调用SecOC_RxIndication()或者SecOC_StartOfReception()通知SecOC。SecOC将Secured I-PDU缓存到本地后开始校验I-PDU处理流程。

When PduR receives an I-PDU that needs to be verified, it calls SecOC_RxIndication() or SecOC_StartOfReception() to notify SecOC. After SecOC caches the Secured I-PDU locally, it begins the I-PDU verification process.

在MainFunction中，SecOC从Secured I-PDU中解析出Authentic I-PDU，FreshnessValue以及Authenticator。从新鲜度值管理器（FVM）中获取FreshnessValue，然后和Authentic I-PDU以及DataId组成DataToAuthenticator。

In MainFunction, SecOC extracts the Authentic I-PDU, FreshnessValue, and Authenticator from the Secured I-PDU. It obtains the FreshnessValue from the Freshness Value Manager (FVM), then forms DataToAuthenticator with the Authentic I-PDU and DataId.

SecOC将DataToAuthenticator以及从接收报文中解析出来的Authenticator传递给CSM。CSM校验后将是否从成功的结果反馈给SecOC。

SecOC sends DataToAuthenticator and the Authenticator parsed from received packets to CSM. CSM verifies them and feeds back whether the verification was successful to SecOC.

如果校验成功，SecOC 向FVM发送确认信息，FVM根据该信息维护FV。

If the validation is successful, SecOC sends a confirmation message to FVM, which then maintains the FV based on this information.

SecOC调用PduR接口将Authentic I-PDU分一次（IF）或多次（TP）传递给上层。

SecOC invokes PduR interface to pass Authenticated I-PDU once (IF) or multiple times (TP) to the upper layer.

Override功能 (Override function)
----------------------------------------------

Override功能是一种特殊的可以干扰SecOC正常接收处理流程的机制。根据设置的Override策略，SecOC可能会不执行校验机制，或者在校验失败时也会将Authentic I-PDU传递给上层模块。

Override functionality is a special mechanism that can interfere with the normal reception and processing flow of SecOC. Depending on the set Override strategy, SecOC may not execute validation mechanisms or pass Authentic I-PDU to upper-layer modules even if validation fails.

Override功能实现 (Override Function Implementation)
===============================================================

SecOC会在进行校验前判断Override功能设置的策略，决定是否需要调用CSM的接口进行数据校验。并且在校验结束后，根据Override功能设置的策略决定是否将需要将Authentic I-PDU传递给上层模块。

SecOC will determine whether to call the CSM interface for data validation before performing the check based on the settings of the Override function. After the validation, it will decide whether to pass the Authentic I-PDU to the upper module based on the settings of the Override function.

Override策略见下表：

Override Strategies are as follows:

.. centered:: **表 Override策略一览表 (Table of Override Strategies)**

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 策略 (Strategies)
     - 说明 (Description)
   * - SECOC_OVERRIDE_DROP_UNTIL_NOTICE
     - 在设置新的Override策略之前，SecOC不对接收报文进行校验，并且丢弃接收报文，将校验结果状态设置为SECOC_NO_VERIFICATION (Before setting a new Override policy, SecOC does not validate the received message and discards it, setting the verification result status to SECOC_NO_VERIFICATION)
   * - SECOC_OVERRIDE_DROP_UNTIL_LIMIT
     - 在设置的NumberOfMessagesToOverride个数的报文之内，SecOC不对接收报文进行校验，并且丢弃接收报文，将校验结果状态设置为SECOC_NO_VERIFICATION，之后恢复正常的接收流程 (Within the NumberOfMessagesToOverride number of messages set, SecOC does not verify the received messages and discards them, setting the verification result status to SECOC_NO_VERIFICATION, then resumes normal reception procedures.)
   * - SECOC_OVERRIDE_CANCEL
     - 取消Override (Cancel Override)
   * - SECOC_OVERRIDE_PASS_UNTIL_NOTICE
     - 在设置新的Override策略之前，SecOC要对所有的SecuredI-PDU进行校验，无论校验结果如何都要将AuthenticI-PDU传递给上层模块。当校验结果失败时，将校验结果状态设置为SECOC_VERIFICATIONFAILURE_OVERWRITTEN (Before setting new Override policies, SecOC should validate all SecuredI-PDU. Regardless of the validation result, the AuthenticI-PDU should be passed to the upper layer module. When the validation fails, set the verification result status to SECOC_VERIFICATIONFAILURE_OVERWRITTEN.)
   * - SECOC_OVERRIDE_SKIP_UNTIL_LIMIT
     - 在设置的NumberOfMessagesToOverride个数的报文之内，SecOC不对接收的SecuredI-PDU进行校验，将AuthenticI-PDU直接传递给上层模块。将校验结果状态设置为SECOC_NO_VERIFICATION。如果SecOCRxSecuredPduCollection启用，则直接处理SecOCRxAuthenticPdu，不用等待SecOCRxCryptographicPdu。之后恢复正常的接收流程。 (Within the NumberOfMessagesToOverride messages, SecOC does not validate the received SecuredI-PDU and directly forwards the AuthenticI-PDU to the upper-layer module. The verification result status is set to SECOC_NO_VERIFICATION. If SecOCRxSecuredPduCollection is enabled, process SecOCRxAuthenticPdu directly without waiting for SecOCRxCryptographicPdu. Then, resume normal reception procedures.)
   * - SECOC_OVERRIDE_PASS_UNTIL_LIMIT
     - 在设置的NumberOfMessagesToOverride个数的报文之内，SecOC要对所有的SecuredI-PDU进行校验，无论校验结果如何都要将AuthenticI-PDU传递给上层模块。当校验结果失败时，将校验结果状态设置为SECOC_VERIFICATIONFAILURE_OVERWRITTEN。之后恢复正常的接收流程。 (Within the NumberOfMessagesToOverride messages set, SecOC should verify all SecuredI-PDU, and regardless of the verification result, pass the AuthenticI-PDU to the upper module. When the verification fails, set the verification result status to SECOC_VERIFICATIONFAILURE_OVERWRITTEN. Then resume normal reception procedures.)
   * - SECOC_OVERRIDE_SKIP_UNTIL_NOTICE
     - 在设置新的Override策略之前，SecOC不对接收的SecuredI-PDU进行校验，将AuthenticI-PDU直接传递给上层模块。将校验结果状态设置为SECOC_NO_VERIFICATION。如果SecOCRxSecuredPduCollection启用，则直接处理SecOCRxAuthenticPdu，不用等待SecOCRxCryptographicPdu。 (Before setting the new Override policy, SecOC does not verify the received SecuredI-PDU and directly passes the AuthenticI-PDU to the upper-layer module. The verification result status is set to SECOC_NO_VERIFICATION. If SecOCRxSecuredPduCollection is enabled, then process the SecOCRxAuthenticPdu directly without waiting for SecOCRxCryptographicPdu.)




源文件描述 (Source file description)
===============================================

.. centered:: **表 SecOC组件文件描述 (Table SecOC Component File Description)**

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 文件 (Files)
     - 说明 (Description)
   * - SecOC_Cfg.h
     - 定义SecOC模块预编译时用到的配置参数。 (Define configuration parameters used during pre-compilation of the SecOC module.)
   * - SecOC_cfg.c
     - 定义SecOC模块中连接时用到的配置参数。 (Define configuration parameters used for connection in the SecOC module.)
   * - SecOC.h
     - SecOC模块头文件，包含了API函数的扩展声明并定义了端口的数据结构。 (Header file for the SecOC module, which includes extended declarations of API functions and defines the data structure of ports.)
   * - SecOC .c
     - SecOC模块源文件，包含了API函数的实现。 (SecOC Module source files contain the implementation of API functions.)
   * - SecOC_Callout.h
     - SecOC定义的Callout函数头文件 (Header file for the Callout function defined in SecOC)
   * - SecOC_Callout.c
     - SecOC定义的Callout函数源文件 (Source file for SecOC-defined Callout function)
   * - SecOC_Internal.h
     - SecOC内部需要使用的数据类型，宏定义等 (Data types, macros, and other definitions needed for use within SecOC)
   * - SecOC_MemMap.h
     - SecOC变量和函数存储位置定义文件。 (Definition file for SecOC variable and function storage locations.)
   * - SecOC_Types.h
     - SecOC数据类型定义。 (Definition of SecOC Data Types.)




.. figure:: ../../_static/参考手册(Module_Reference_Manual)/SecOC/image7.png
   :alt: SecOC组件文件交互关系图 (Component Interaction Diagram for SecOC Module)
   :name: SecOC组件文件交互关系图 (Component Interaction Diagram for SecOC Module)
   :align: center


API接口 (API Interface)
=====================================

类型定义 (Type definition)
--------------------------------------

SecOC_ConfigType类型定义 (SecOC_ConfigType Configuration Type Definition)
=====================================================================================

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 名称 (Name)
     - SecOC_ConfigType
   * - 类型 (Type)
     - 结构体 (Structures)
   * - 范围 (Range)
     - 无
   * - 描述 (Description)
     - SecOC模块配置信息 (SecOC Module Configuration Information)




SecOC_StateType类型定义 (SecOC_StateType Type Definition)
=====================================================================

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 名称 (Name)
     - SecOC_StateType
   * - 类型 (Type)
     - 枚举 (Enum)
   * - 范围 (Range)
     - SECOC_UNINIT
   * - 
     - SECOC_INIT
   * - 描述 (Description)
     - SecOC模块初始化状态 (SecOC Module Initialization Status)




SecOC_FreshnessArrayType类型定义 (SecOC_FreshnessArrayType type definition)
=======================================================================================

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 名称 (Name)
     - SecOC_FreshnessArrayType
   * - 类型 (Type)
     - 数组 (Array)
   * - 范围 (Range)
     - 无
   * - 描述 (Description)
     - 用于从FVM获取FreshnessValue (Used for getting FreshnessValue from FVM)




SecOC_VerificationResultType类型定义 (SecOC_VerificationResultType Type Definition)
===============================================================================================

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 名称 (Name)
     - SecOC_VerificationResultType
   * - 类型 (Type)
     - 枚举 (Enum)
   * - 范围 (Range)
     - SECOC_VERIFICATIONSUCCESS
   * - 
     - SECOC_VERIFICATIONFAILURE
   * - 
     - SECOC_FRESHNESSFAILURE
   * - 
     - SECOC_AUTHENTICATIONBUILDFAILURE
   * - 
     - SECOC_NO_VERIFICATION
   * - 
     - SECOC_VERIFICATIONFAILURE_OVERWRITTEN
   * - 描述 (Description)
     - SecOC模块初始化状态 (SecOC Module Initialization Status)




SecOC_VerificationStatusType类型定义 (SecOC_VerificationStatusType Type Definition)
===============================================================================================

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 名称 (Name)
     - SecOC_VerificationStatusType
   * - 类型 (Type)
     - 结构体 (Structures)
   * - 范围 (Range)
     - 无
   * - 描述 (Description)
     - 表示特定FreshnessValueId和DataId的校验尝试结果 (Validation attempt results for specific FreshnessValueId and DataId)




SecOC_OverrideStatusType类型定义 (SecOC_OverrideStatusType Type Definition)
=======================================================================================

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 名称 (Name)
     - SecOC_OverrideStatusType
   * - 类型 (Type)
     - 枚举 (Enum)
   * - 范围 (Range)
     - SECOC_OVERRIDE_DROP_UNTIL_NOTICE
   * - 
     - SECOC_OVERRIDE_DROP_UNTIL_LIMIT
   * - 
     - SECOC_OVERRIDE_CANCEL
   * - 
     - SECOC_OVERRIDE_PASS_UNTIL_NOTICE
   * - 
     - SECOC_OVERRIDE_SKIP_UNTIL_LIMIT
   * - 
     - SECOC_OVERRIDE_PASS_UNTIL_LIMIT
   * - 
     - SECOC_OVERRIDE_SKIP_UNTIL_NOTICE
   * - 描述 (Description)
     - Override策略定义 (Override Strategy Definition)




输入函数描述 (Describe the input function:)
-----------------------------------------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 输入模块 (Input Module)
     - API
   * - Det
     - Det_ReportRuntimeError
   * - 
     - Det_ReportError
   * - PduR
     - PduR_SecOCCancelTransmit
   * - 
     - PduR_SecOCIfRxIndication
   * - 
     - PduR_SecOCIfTxConfirmation
   * - 
     - PduR_SecOCTransmit
   * - 
     - PduR_SecOCCancelReceive
   * - 
     - PduR_SecOCTpCopyRxData
   * - 
     - PduR_SecOCTpCopyTxData
   * - 
     - PduR_SecOCTpRxIndication
   * - 
     - PduR_SecOCTpStartOfReception
   * - 
     - PduR_SecOCTpTxConfirmation
   * - Csm
     - Csm_MacGenerate
   * - 
     - Csm_MacVerify
   * - 
     - Csm_SignatureGenerate
   * - 
     - Csm_SignatureVerify




静态接口函数定义 (Static interface function definition)
---------------------------------------------------------------

SecOC_Init函数定义 (The SecOC_Init function definition)
===================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - SecOC_Init
     - 
     - 
   * - 函数原型： (Function prototype:)
     - void SecOC_Init (constSecOC_ConfigType\*config )
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x01
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 不可重入 (Non-reentrant)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - config
     - 值域： (Domain:)
     - 无
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无
     - 
     - 
   * - 返回值： (Return Value:)
     - 无
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 初始化SecOC模块 (Initialize SecOC module)
     - 
     - 




SecOC_DeInit函数定义 (Function definition for SecOC_DeInit)
=======================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - SecOC_DeInit
     - 
     - 
   * - 函数原型： (Function prototype:)
     - void SecOC_DeInit( void )
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x05
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 不可重入 (Non-reentrant)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - 无
     - 值域： (Domain:)
     - 无
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无
     - 
     - 
   * - 返回值： (Return Value:)
     - 无
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 反初始化SecOC模块 (Uninitialize SecOC module)
     - 
     - 




SecOC_GetVersionInfo函数定义 (The SecOC_GetVersionInfo function definition)
=======================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - SecOC_GetVersionInfo
     - 
     - 
   * - 函数原型： (Function prototype:)
     - voidSecOC_GetVersionInfo(Std_VersionInfoType\*versioninfo )
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x02
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 可重入 (Reentrant)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - 无
     - 值域： (Domain:)
     - 无
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - versioninfo
     - 
     - 
   * - 返回值： (Return Value:)
     - 无
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 返回SecOC模块的版本信息 (Return version information of the SecOC module)
     - 
     - 




SecOC_IfTransmit函数定义 (SecOC_IFTransmit_function_definition)
===========================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - SecOC_IfTransmit
     - 
     - 
   * - 函数原型： (Function prototype:)
     - Std_ReturnTypeSecOC_IfTransmit(
     - 
     - 
   * - 
     - PduIdTypeTxPduId,
     - 
     - 
   * - 
     - constPduInfoType\*PduInfoPtr
     - 
     - 
   * - 
     - )
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x49
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 不同TxPduId可重入 (Different TxPduId Reentrant)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - TxPduId
     - 值域： (Domain:)
     - 0 .. 65535
   * - 
     - PduInfoPtr
     - 
     - 无
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无
     - 
     - 
   * - 返回值： (Return Value:)
     - E_OK:发送请求被接受 (E_OK: The request has been accepted.)
     - 
     - 
   * - 
     - E_OK:发送请求被拒绝 (E_OK: Request was denied.)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 请求发送一个IfPDU (Request sending an IfPDU)
     - 
     - 




SecOC_TpTransmit函数定义 (The function definition for SecOC_TpTransmit)
===================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - SecOC_TpTransmit
     - 
     - 
   * - 函数原型： (Function prototype:)
     - Std_ReturnTypeSecOC_TpTransmit(
     - 
     - 
   * - 
     - PduIdTypeTxPduId,
     - 
     - 
   * - 
     - constPduInfoType\*PduInfoPtr
     - 
     - 
   * - 
     - )
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x49
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 不同TxPduId可重入 (Different TxPduId Reentrant)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - TxPduId
     - 值域： (Domain:)
     - 0 .. 65535
   * - 
     - PduInfoPtr
     - 
     - 无
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无
     - 
     - 
   * - 返回值： (Return Value:)
     - E_OK:发送请求被接受 (E_OK: The request has been accepted.)
     - 
     - 
   * - 
     - E_OK:发送请求被拒绝 (E_OK: Request was denied.)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 请求发送一个TPPDU (Request sending a TPPDU)
     - 
     - 




SecOC_IfCancelTransmit函数定义 (SecOC_IFCancelTransmit function definition)
=======================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - SecOC_IfCancelTransmit
     - 
     - 
   * - 函数原型： (Function prototype:)
     - Std_ReturnTypeSecOC_IfCancelTransmit( PduIdTypeTxPduId )
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x4a
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 不同TxPduId可重入 (Different TxPduId Reentrant)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - TxPduId
     - 值域： (Domain:)
     - 0 .. 65535
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无
     - 
     - 
   * - 返回值： (Return Value:)
     - E_OK:取消发送请求被接受 (E_OK: The request to cancel sending has been accepted)
     - 
     - 
   * - 
     - E_OK:取消发送请求被拒绝 (E_OK: The request to cancel sending was rejected)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 请求取消发送一个IfPDU (Request cancel sending an IfPDU)
     - 
     - 




SecOC_TpCancelTransmit函数定义 (The SecOC_TpCancelTransmit function definition)
===========================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - SecOC_TpCancelTransmit
     - 
     - 
   * - 函数原型： (Function prototype:)
     - Std_ReturnTypeSecOC_TpCancelTransmit( PduIdTypeTxPduId )
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x4a
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 不同TxPduId可重入 (Different TxPduId Reentrant)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - TxPduId
     - 值域： (Domain:)
     - 0 .. 65535
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无
     - 
     - 
   * - 返回值： (Return Value:)
     - E_OK:取消发送请求被接受 (E_OK: The request to cancel sending has been accepted)
     - 
     - 
   * - 
     - E_OK:取消发送请求被拒绝 (E_OK: The request to cancel sending was rejected)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 请求取消发送一个TPPDU (Request cancel sending a TP PDU)
     - 
     - 




SecOC_TpCancelReceive函数定义 (The SecOC_TpCancelReceive function definition)
=========================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - SecOC_TpCancelReceive
     - 
     - 
   * - 函数原型： (Function prototype:)
     - Std_ReturnTypeSecOC_TpCancelReceive( PduIdTypeRxPduId )
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x4c
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 不可重入 (Non-reentrant)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - RxPduId
     - 值域： (Domain:)
     - 0 .. 65535
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无
     - 
     - 
   * - 返回值： (Return Value:)
     - E_OK:取消接收请求被接受 (E_OK: Acceptance of cancel receive request)
     - 
     - 
   * - 
     - E_OK:取消接收请求被拒绝 (E_OK: Reject receiving request rejected)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 请求取消接收一个PDU (Request to cancel reception of a PDU)
     - 
     - 




SecOC_VerifyStatusOverride函数定义 (The SecOC_VerifyStatusOverride function definition)
===================================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - SecOC_VerifyStatusOverride
     - 
     - 
   * - 函数原型： (Function prototype:)
     - Std_ReturnTypeSecOC_VerifyStatusOverride(
     - 
     - 
   * - 
     - uint16 ValueID,
     - 
     - 
   * - 
     - SecOC_OverrideStatusTypeoverrideStatus,
     - 
     - 
   * - 
     - uint8numberOfMessagesToOverride
     - 
     - 
   * - 
     - )
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x0b
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 不同FreshnessValueID可重入 (Different FreshnessValueID can re-enter.)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - ValueID
     - 值域： (Domain:)
     - 0 .. 65535
   * - 
     - overrideStatus
     - 值域： (Domain:)
     - 无
   * - 
     - numberOfMessagesToOverride
     - 值域： (Domain:)
     - 0 .. 255
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无
     - 
     - 
   * - 返回值： (Return Value:)
     - E_OK: 请求成功 (E_OK: Request successful)
     - 
     - 
   * - 
     - E_OK: 请求失败 (E_OK: Request failed)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 调用该函数设置Override策略，设置为 (Call this function to set the Override strategy, set it to)
     - 
     - 
   * - 
     - SECOC_OVERRIDE_PASS_UNTIL_NOTICE,SECOC_OVERRIDE_SKIP_UNTIL_LIMIT,SECOC_OVERRIDE_PASS_UNTIL_LIMIT或SECOC_OVERRIDE_SKIP_UNTIL_NOTICE时，SecOCEnableForcedPassOverride参数必须设置为TRUE (When SECOC_OVERRIDE_PASS_UNTIL_NOTICE, SECOC_OVERRIDE_SKIP_UNTIL_LIMIT, SECOC_OVERRIDE_PASS_UNTIL_LIMIT, or SECOC_OVERRIDE_SKIP_UNTILnoticed is enabled, the SecOCEnableForcedPassOverride parameter must be set to TRUE)
     - 
     - 




SecOC_SendDefaultAuthenticationInformation函数定义 (The SecOC_SendDefaultAuthenticationInformation function definition)
===================================================================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - SecOC_SendDefaultAuthenticationInformation
     - 
     - 
   * - 函数原型： (Function prototype:)
     - Std_ReturnTypeSecOC_SendDefaultAuthenticationInformation(
     - 
     - 
   * - 
     - uint16 FreshnessValueID,
     - 
     - 
   * - 
     - booleansendDefaultAuthenticationInformation
     - 
     - 
   * - 
     - )
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x04
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 不可重入 (Non-reentrant)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - FreshnessValueID
     - 值域： (Domain:)
     - 0 .. 65535
   * - 
     - sendDefaultAuthenticationInformation
     - 值域： (Domain:)
     - TRUE / FALSE
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无
     - 
     - 
   * - 返回值： (Return Value:)
     - E_OK: 请求被接受 (E_OK: The request has been accepted.)
     - 
     - 
   * - 
     - E_OK: 请求被拒绝 (E_OK: RequestRejected)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 当FreshnessValueID的sendDefaultAuthenticationInformation参数被设置为TRUE时，当认证AuthenticI-PDU失败时，SecOC可以用DefaultAuthenticationInformation作为Authenticator构建SecuredI-PDU，继续进行发送。 (When the sendDefaultAuthenticationInformation parameter of FreshnessValueID is set to TRUE, SecOC can use DefaultAuthenticationInformation as the Authenticator to construct SecuredI-PDU and continue sending when authentication of AuthenticI-PDU fails.)
     - 
     - 




SecOC_RxIndication函数定义 (The SecOC_RxIndication function definition)
===================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - SecOC_RxIndication
     - 
     - 
   * - 函数原型： (Function prototype:)
     - voidSecOC_RxIndication(
     - 
     - 
   * - 
     - PduIdTypeRxPduId,
     - 
     - 
   * - 
     - constPduInfoType\*PduInfoPtr
     - 
     - 
   * - 
     - )
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x42
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 不同RxPduId可重入 (Different RxPduId Reentrant)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - RxPduId
     - 值域： (Domain:)
     - 0 .. 65535
   * - 
     - PduInfoPtr
     - 值域： (Domain:)
     - 无
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无
     - 
     - 
   * - 返回值： (Return Value:)
     - 无
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 低层模块调用该函数通知SecOC接收到一帧报文 (Lower-level modules call this function to notify SecOC of receiving a frame of message)
     - 
     - 




SecOC_TpRxIndication函数定义 (SecOC_TpRxIndication function definition)
===================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - SecOC_TpRxIndication
     - 
     - 
   * - 函数原型： (Function prototype:)
     - voidSecOC_TpRxIndication( PduIdType id,Std_ReturnTyperesult )
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x45
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 可重入 (Reentrant)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - id
     - 值域： (Domain:)
     - 0 .. 65535
   * - 
     - result
     - 值域： (Domain:)
     - E_OK / E_NOT_OK
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无
     - 
     - 
   * - 返回值： (Return Value:)
     - 无
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 低层模块调用该函数通知SecOC一帧TP报文接收完成。result参数表示接收是否成功。 (Lower-level modules call this function to notify SecOC that a frame TP message reception is completed. The result parameter indicates whether the reception was successful.)
     - 
     - 




SecOC_TxConfirmation函数定义 (The SecOC_TxConfirmation Function Definition)
=======================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - SecOC_TxConfirmation
     - 
     - 
   * - 函数原型： (Function prototype:)
     - voidSecOC_TxConfirmation(
     - 
     - 
   * - 
     - PduIdTypeTxPduId,
     - 
     - 
   * - 
     - Std_ReturnTyperesult
     - 
     - 
   * - 
     - )
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x40
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 不同TxPduId可重入 (Different TxPduId Reentrant)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - TxPduId
     - 值域： (Domain:)
     - 0 .. 65535
   * - 
     - result
     - 值域： (Domain:)
     - E_OK / E_NOT_OK
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无
     - 
     - 
   * - 返回值： (Return Value:)
     - 无
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 低层模块调用该函数通知SecOC报文发送结果。result参数表示发送是否成功。 (Lower-level modules call this function to notify the SecOC of the message send result. The result parameter indicates whether the sending was successful.)
     - 
     - 




SecOC_TpTxConfirmation函数定义 (SecOC_TpTxConfirmation function definition)
=======================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - SecOC_TpTxConfirmation
     - 
     - 
   * - 函数原型： (Function prototype:)
     - voidSecOC_TpTxConfirmation( PduIdType id,Std_ReturnTyperesult )
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x48
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 可重入 (Reentrant)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - id
     - 值域： (Domain:)
     - 0 .. 65535
   * - 
     - result
     - 值域： (Domain:)
     - E_OK / E_NOT_OK
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无
     - 
     - 
   * - 返回值： (Return Value:)
     - 无
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 低层模块调用该函数通知SecOCTP报文发送结束。result参数表示发送是否成功。 (Lower-level modules call this function to notify that the SecOCTP message sending has ended. The result parameter indicates whether the sending was successful.)
     - 
     - 




SecOC_TriggerTransmit函数定义 (Function definition for SecOC_TriggerTransmit)
=========================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - SecOC_TriggerTransmit
     - 
     - 
   * - 函数原型： (Function prototype:)
     - Std_ReturnTypeSecOC_TriggerTransmit(
     - 
     - 
   * - 
     - PduIdTypeTxPduId,
     - 
     - 
   * - 
     - PduInfoType\*PduInfoPtr
     - 
     - 
   * - 
     - )
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x41
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 不同TxPduId可重入 (Different TxPduId Reentrant)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - TxPduId
     - 值域： (Domain:)
     - 0 .. 65535
   * - 
     - PduInfoPtr
     - 值域： (Domain:)
     - 无
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无
     - 
     - 
   * - 返回值： (Return Value:)
     - E_OK:SDU被复制，SduLength表示复制的字节长度。 (E_OK:SDU was copied, SduLength indicates the byte length copied.)
     - 
     - 
   * - 
     - E_NOT_OK:没有SDU被复制。 (E_NOT_OK: No SDUs were copied.)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 低层模块调用该函数获取要发送的数据。 (Lower-level modules call this function to get the data to be sent.)
     - 
     - 




SecOC_CopyRxData函数定义 (The SecOC_CopyRxData function definition)
===============================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - SecOC_CopyRxData
     - 
     - 
   * - 函数原型： (Function prototype:)
     - BufReq_ReturnTypeSecOC_CopyRxData(
     - 
     - 
   * - 
     - PduIdType id,
     - 
     - 
   * - 
     - constPduInfoType\*info,
     - 
     - 
   * - 
     - PduLengthType\*bufferSizePtr
     - 
     - 
   * - 
     - )
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x44
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 可重入 (Reentrant)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - id
     - 值域： (Domain:)
     - 0 .. 65535
   * - 
     - info
     - 值域： (Domain:)
     - 无
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - bufferSizePtr
     - 
     - 
   * - 返回值： (Return Value:)
     - BUFREQ_OK:数据复制成功 (BUFREQ_OK: Data replication succeeded)
     - 
     - 
   * - 
     - BUFREQ_E_NOT_OK:出现错误，数据未成功复制 (BUFREQ_E_NOT_OK: An error occurred, data replication was unsuccessful.)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 低层模块调用该函数将接收的TP报文分段传输给SecOC。同时SecOC将自己可用的buffer通过bufferSizePtr传递给下层模块。 (Lower-level modules calling this function will segment and forward the received TP packet to SecOC. Meanwhile, SecOC will pass its available buffer to the lower level module through bufferSizePtr.)
     - 
     - 




SecOC_CopyTxData函数定义 (The SecOC_CopyTxData function definition)
===============================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - SecOC_CopyTxData
     - 
     - 
   * - 函数原型： (Function prototype:)
     - BufReq_ReturnTypeSecOC_CopyTxData(
     - 
     - 
   * - 
     - PduIdType id,
     - 
     - 
   * - 
     - constPduInfoType\*info,
     - 
     - 
   * - 
     - constRetryInfoType\*retry,
     - 
     - 
   * - 
     - PduLengthType\*availableDataPtr
     - 
     - 
   * - 
     - )
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x43
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 可重入 (Reentrant)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - id
     - 值域： (Domain:)
     - 0 .. 65535
   * - 
     - info
     - 值域： (Domain:)
     - 无
   * - 
     - retry
     - 值域： (Domain:)
     - 无
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - availableDataPtr
     - 
     - 
   * - 返回值： (Return Value:)
     - BUFREQ_OK:请求的数据成功复制到提供的buffer中 (BUFREQ_OK: The requested data was successfully copied into the provided buffer.)
     - 
     - 
   * - 
     - BUFREQ_E_BUSY:请求的数据不可用，数据未成功复制 (BUFREQ_E_BUSY: The requested data is unavailable, data replication was unsuccessful.)
     - 
     - 
   * - 
     - BUFREQ_E_NOT_OK:出现错误，数据未成功复制 (BUFREQ_E_NOT_OK: An error occurred, data replication was unsuccessful.)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 低层模块调用该函数获取要发送的TP报文分段数据。每次调用SecOC都将下个分段传输给低层模块，除非retry->TpDataState被设置为TP_DATARETRY，此时SecOC从retry->TxTpDataCnt指示的偏移位置开始复制数据。SecOC将当前可用的数据长度通过availableDataPtr传递给低层模块。 (Lower-layer modules call this function to obtain the segmented TP message data to be sent. Each call to SecOC passes the next segment to the lower-layer module, unless retry->TpDataState is set to TP_DATARETRY, in which case SecOC starts copying data from the offset indicated by retry->TxTpDataCnt. SecOC passes the current available data length through availableDataPtr to the lower-layer module.)
     - 
     - 




SecOC_StartOfReception函数定义 (SecOC_StartOfReception function definition)
=======================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - SecOC_StartOfReception
     - 
     - 
   * - 函数原型： (Function prototype:)
     - BufReq_ReturnTypeSecOC_StartOfReception(
     - 
     - 
   * - 
     - PduIdType id,
     - 
     - 
   * - 
     - constPduInfoType\*info,
     - 
     - 
   * - 
     - PduLengthTypeTpSduLength,
     - 
     - 
   * - 
     - PduLengthType\*bufferSizePtr
     - 
     - 
   * - 
     - )
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x46
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 可重入 (Reentrant)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - id
     - 值域： (Domain:)
     - 0 .. 65535
   * - 
     - info
     - 值域： (Domain:)
     - 无
   * - 
     - TpSduLength
     - 值域： (Domain:)
     - 0 .. 65535
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - bufferSizePtr
     - 
     - 
   * - 返回值： (Return Value:)
     - BUFREQ_OK:TP接收被接受，bufferSizePtr表明可用的buffer。bufferSizePtr为0，表示没有可用的buffer。 (BUFREQ_OK: TP reception accepted, bufferSizePtr indicates available buffer. bufferSizePtr is 0, indicating no available buffer.)
     - 
     - 
   * - 
     - BUFREQ_E_NOT_OK:TP接收被拒绝，接收需要被放弃。 (BUFREQ_E_NOT_OK: TP reception was rejected, reception needs to be abandoned.)
     - 
     - 
   * - 
     - BUFREQ_E_OVFL:无法提供要求长度的buffer，接收需要被放弃。 (BUFREQ_E_OVFL: Unable to provide buffer of requested length, reception needs to be abandoned.)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 低层开始接收N-SDU时，调用该函数。该N-SDU可能是FF也可能是SF。当TpSduLength，SecOC提供当前可用的接收buffer的长度。 (This function is called when the lower layer starts receiving an N-SDU. This N-SDU could be either FF or SF. When TpSduLength and SecOC provide the length of the currently available receive buffer.)
     - 
     - 




SecOC_GetRxFreshness函数定义 (The SecOC_GetRxFreshness function definition)
=======================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - SecOC_GetRxFreshness
     - 
     - 
   * - 函数原型： (Function prototype:)
     - Std_ReturnTypeSecOC_GetRxFreshness (
     - 
     - 
   * - 
     - uint16SecOCFreshnessValueID,
     - 
     - 
   * - 
     - const uint8\*SecOCTruncatedFreshnessValue,
     - 
     - 
   * - 
     - uint32SecOCTruncatedFreshnessValueLength,
     - 
     - 
   * - 
     - uint16SecOCAuthVerifyAttempts,
     - 
     - 
   * - 
     - uint8\*SecOCFreshnessValue,
     - 
     - 
   * - 
     - uint32\*SecOCFreshnessValueLength
     - 
     - 
   * - 
     - )
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x4f
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 可重入 (Reentrant)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - SecOCFreshnessValueID
     - 值域： (Domain:)
     - 0 .. 65535
   * - 
     - SecOCTruncatedFreshnessValue
     - 值域： (Domain:)
     - 无
   * - 
     - SecOCTruncatedFreshnessValueLength
     - 值域： (Domain:)
     - 0 .. 4294967295
   * - 
     - SecOCAuthVerifyAttempts
     - 值域： (Domain:)
     - 0 .. 65535
   * - 输入输出参数： (Input Output Parameters:)
     - SecOCFreshnessValueLength
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - SecOCFreshnessValue
     - 
     - 
   * - 返回值： (Return Value:)
     - E_OK: 请求成功 (E_OK: Request successful)
     - 
     - 
   * - 
     - E_NOT_OK:请求失败，无法提供FreshnessValue (E_NOT_OK: Request failed, unable to provide FreshnessValue)
     - 
     - 
   * - 
     - E_BUSY:暂时无法提供FreshnessValue (E_BUSY: Temporarily unable to provide FreshnessValue)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - SecOC调用该函数获取FreshnessValue。 (SecOC calls this function to get FreshnessValue.)
     - 
     - 




SecOC_GetRxFreshnessAuthData函数定义 (The function definition for SecOC_GetRxFreshnessAuthData)
===========================================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - SecOC_GetRxFreshnessAuthData
     - 
     - 
   * - 函数原型： (Function prototype:)
     - Std_ReturnTypeSecOC_GetRxFreshnessAuthData(
     - 
     - 
   * - 
     - uint16SecOCFreshnessValueID,
     - 
     - 
   * - 
     - const uint8\*SecOCTruncatedFreshnessValue,
     - 
     - 
   * - 
     - uint32SecOCTruncatedFreshnessValueLength,
     - 
     - 
   * - 
     - const uint8\*SecOCAuthDataFreshnessValue,
     - 
     - 
   * - 
     - uint16SecOCAuthDataFreshnessValueLength,
     - 
     - 
   * - 
     - uint16SecOCAuthVerifyAttempts,
     - 
     - 
   * - 
     - uint8\*SecOCFreshnessValue,
     - 
     - 
   * - 
     - uint32\*SecOCFreshnessValueLength
     - 
     - 
   * - 
     - )
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x4e
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 可重入 (Reentrant)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - SecOCFreshnessValueID
     - 值域： (Domain:)
     - 0 .. 65535
   * - 
     - SecOCTruncatedFreshnessValue
     - 值域： (Domain:)
     - 无
   * - 
     - SecOCTruncatedFreshnessValueLength
     - 值域： (Domain:)
     - 0 .. 4294967295
   * - 
     - SecOCAuthDataFreshnessValue
     - 值域： (Domain:)
     - 无
   * - 
     - SecOCAuthDataFreshnessValueLength
     - 值域： (Domain:)
     - 0 .. 65535
   * - 
     - SecOCAuthVerifyAttempts
     - 值域： (Domain:)
     - 0 .. 65535
   * - 输入输出参数： (Input Output Parameters:)
     - SecOCFreshnessValueLength
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - SecOCFreshnessValue
     - 
     - 
   * - 返回值： (Return Value:)
     - E_OK: 请求成功 (E_OK: Request successful)
     - 
     - 
   * - 
     - E_NOT_OK:请求失败，无法提供FreshnessValue (E_NOT_OK: Request failed, unable to provide FreshnessValue)
     - 
     - 
   * - 
     - E_BUSY:暂时无法提供FreshnessValue (E_BUSY: Temporarily unable to provide FreshnessValue)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - SecOC调用该函数获取FreshnessValue。 (SecOC calls this function to get FreshnessValue.)
     - 
     - 




SecOC_GetTxFreshness函数定义 (The SecOC_GetTxFreshness function definition)
=======================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - SecOC_GetTxFreshness
     - 
     - 
   * - 函数原型： (Function prototype:)
     - Std_ReturnTypeSecOC_GetTxFreshness(
     - 
     - 
   * - 
     - uint16SecOCFreshnessValueID,
     - 
     - 
   * - 
     - uint8\*SecOCFreshnessValue,
     - 
     - 
   * - 
     - uint32\*SecOCFreshnessValueLength
     - 
     - 
   * - 
     - )
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x52
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 可重入 (Reentrant)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - SecOCFreshnessValueID
     - 值域： (Domain:)
     - 0 .. 65535
   * - 输入输出参数： (Input Output Parameters:)
     - SecOCFreshnessValueLength
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - SecOCFreshnessValue
     - 
     - 
   * - 返回值： (Return Value:)
     - E_OK: 请求成功 (E_OK: Request successful)
     - 
     - 
   * - 
     - E_NOT_OK:请求失败，无法提供FreshnessValue (E_NOT_OK: Request failed, unable to provide FreshnessValue)
     - 
     - 
   * - 
     - E_BUSY:暂时无法提供FreshnessValue (E_BUSY: Temporarily unable to provide FreshnessValue)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 该函数从MSB截取长度为SecOCFreshnessValueLength位的FreshnessValue。大端方式。 (The function extracts a FreshnessValue of length SecOCFreshnessValueLength bits from the MSB in big-endian format.)
     - 
     - 




SecOC_GetTxFreshnessTruncData函数定义 (The SecOC_GetTxFreshnessTruncData function definition)
=========================================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - SecOC_GetTxFreshness
     - 
     - 
   * - 函数原型： (Function prototype:)
     - Std_ReturnTypeSecOC_GetTxFreshnessTruncData(
     - 
     - 
   * - 
     - uint16SecOCFreshnessValueID,
     - 
     - 
   * - 
     - uint8\*SecOCFreshnessValue,
     - 
     - 
   * - 
     - uint32\*SecOCFreshnessValueLength,
     - 
     - 
   * - 
     - uint8\*SecOCTruncatedFreshnessValue,
     - 
     - 
   * - 
     - uint32\*SecOCTruncatedFreshnessValueLength
     - 
     - 
   * - 
     - )
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x51
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 可重入 (Reentrant)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - SecOCFreshnessValueID
     - 值域： (Domain:)
     - 0 .. 65535
   * - 输入输出参数： (Input Output Parameters:)
     - SecOCFreshnessValueLength
     - 
     - 
   * - 
     - SecOCTruncatedFreshnessValueLength
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - SecOCFreshnessValue
     - 
     - 
   * - 
     - SecOCTruncatedFreshnessValue
     - 
     - 
   * - 返回值： (Return Value:)
     - E_OK: 请求成功 (E_OK: Request successful)
     - 
     - 
   * - 
     - E_NOT_OK:请求失败，无法提供FreshnessValue (E_NOT_OK: Request failed, unable to provide FreshnessValue)
     - 
     - 
   * - 
     - E_BUSY:暂时无法提供FreshnessValue (E_BUSY: Temporarily unable to provide FreshnessValue)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 该函数从获取当前的FreshnessValue。同时返回截取后的FreshnessValue。 (The function retrieves the current FreshnessValue and returns the truncated FreshnessValue.)
     - 
     - 




SecOC_SPduTxConfirmation函数定义 (The SecOC_SPduTxConfirmation function definition)
===============================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - SecOC_SPduTxConfirmation
     - 
     - 
   * - 函数原型： (Function prototype:)
     - voidSecOC_SPduTxConfirmation( uint16SecOCFreshnessValueID)
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x4d
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 可重入 (Reentrant)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - SecOCFreshnessValueID
     - 值域： (Domain:)
     - 0 .. 65535
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无
     - 
     - 
   * - 返回值： (Return Value:)
     - 无
     - 
     - 
   * - 功能概述： (Function Overview:)
     - SecOC调用该函数向FVM表明SecuredI-PDU的发送已成功发起。 (SecOC calls this function to indicate to FVM that the sending of SecuredI-PDU has been successfully initiated.)
     - 
     - 




SecOC_MainFunctionRx函数定义 (SecOC_MainFunctionRx function definition)
===================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - SecOC_MainFunctionRx
     - 
     - 
   * - 函数原型： (Function prototype:)
     - voidSecOC_MainFunctionRx( void )
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x06
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 不可重入 (Non-reentrant)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - 无
     - 值域： (Domain:)
     - 无
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无
     - 
     - 
   * - 返回值： (Return Value:)
     - 无
     - 
     - 
   * - 功能概述： (Function Overview:)
     - SecOC模块发送周期处理函数。 (SecOC module send periodic processing function.)
     - 
     - 




SecOC_MainFunctionTx函数定义 (SecOC_MainFunctionTx Function Definition)
===================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - SecOC_MainFunctionTx
     - 
     - 
   * - 函数原型： (Function prototype:)
     - voidSecOC_MainFunctionTx( void )
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x03
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 不可重入 (Non-reentrant)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - 无
     - 值域： (Domain:)
     - 无
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无
     - 
     - 
   * - 返回值： (Return Value:)
     - 无
     - 
     - 
   * - 功能概述： (Function Overview:)
     - SecOC模块接收周期处理函数。 (The SecOC module receives periodic processing functions.)
     - 
     - 




可配置函数定义 (Configurable Function Definition)
----------------------------------------------------------

SecOC_VerificationStatusCallout函数定义 (SecOC_VerificationStatusCallout function definition)
=========================================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - SecOC_VerificationStatusCallout
     - 
     - 
   * - 函数原型： (Function prototype:)
     - voidSecOC_VerificationStatusCallout(
     - 
     - 
   * - 
     - SecOC_VerificationStatusTypeverificationStatus
     - 
     - 
   * - 
     - )
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x50
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 不同FreshnessValueID可重入 (Different FreshnessValueID can re-enter.)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - verificationStatus
     - 值域： (Domain:)
     - 无
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无
     - 
     - 
   * - 返回值： (Return Value:)
     - 无
     - 
     - 
   * - 功能概述： (Function Overview:)
     - SecOC调用该Callout函数通知其他模块校验的结果。 (SecOC calls the Callout function to notify other modules of the validation results.)
     - 
     - 




配置 (Configure)
==============================

SecOCGeneral
----------------------------

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/SecOC/image8.png
   :alt: SecOCGeneral容器配置图 (Container Configuration Diagram for SecOCGeneral)
   :name: SecOCGeneral容器配置图 (Container Configuration Diagram for SecOCGeneral)
   :align: center


.. centered:: **表 SecOCGeneral属性描述 (Table SecOCGeneral Property Description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - SecOCDefaultAuthenticationInformationPattern
     - 取值范围 (Range)
     - 0 .. 255
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 当SecOC创建Authenticator失败时，如果该参数配置，则不放弃发送，SecOC使用该参数作为默认值构造Authenticator。如果该值未配置，则放弃发送。 (When SecOC fails to create an Authenticator, if this parameter is configured, sending will not be abandoned, and SecOC uses this parameter as the default value to construct the Authenticator. If this value is not configured, sending will be abandoned.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - SecOCDevErrorDetect
     - 取值范围 (Range)
     - STD_ON / STD_OFF
     - 默认取值 (Default value)
     - STD_OFF
   * - 
     - 参数描述 (Parameter Description)
     - DET检测功能的开关 (The switch for DET detection function)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - SecOCEnableForcedPassOverride
     - 取值范围 (Range)
     - STD_ON / STD_OFF
     - 默认取值 (Default value)
     - STD_OFF
   * - 
     - 参数描述 (Parameter Description)
     - 当该参数设置为TRUE时，可通过SecOC_VerifyStatusOverride接口设置Override策略，在校验失败时，可将AuthenticI-PDU传到上层模块 (When this parameter is set to TRUE, the SecOC_VerifyStatusOverride interface can be used to set the Override policy, and upon validation failure, the AuthenticI-PDU can be passed to the upper module.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - SecOCIgnoreVerificationResult
     - 取值范围 (Range)
     - STD_ON / STD_OFF
     - 默认取值 (Default value)
     - STD_OFF
   * - 
     - 参数描述 (Parameter Description)
     - 如果该参数设置为TRUE，当校验失败时，SecOC仍然将AuthenticI-PDU传递给上层模块 (If this parameter is set to TRUE, when validation fails, SecOC still passes the AuthenticI-PDU to the upper module.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - SecOCMainFunctionPeriodRx
     - 取值范围 (Range)
     - 0 .. INF
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - SecOC接收处理周期 (SecOC Receives and Processes Cycles)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - SecOCMainFunctionPeriodTx
     - 取值范围 (Range)
     - 0 .. INF
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - SecOC发送处理周期 (SecOC Processing Cycle Time)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - SecOCOverrideStatusWithDataId
     - 取值范围 (Range)
     - STD_ON / STD_OFF
     - 默认取值 (Default value)
     - STD_OFF
   * - 
     - 参数描述 (Parameter Description)
     - TRUE：SecOC_VerifyStatusOverride()函数接受SecOCDataId作为参数 (TRUE: The SecOC_VerifyStatusOverride() function accepts SecOCDataId as a parameter.)
     - 
     - 
   * - 
     - 
     - FALSE：SecOC_VerifyStatusOverride()函数接受SecOCFreshnessValueId作为参数 (FALSE: The SecOC_VerifyStatusOverride() function accepts SecOCFreshnessValueId as a parameter.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - SecOCQueryFreshnessValue
     - 取值范围 (Range)
     - CFUNC / RTE
     - 默认取值 (Default value)
     - CFUNC
   * - 
     - 参数描述 (Parameter Description)
     - 设置获取FreshnessValue时通过C函数还是RTE的接口 (Set whether to use C function or RTE interface when obtaining FreshnessValue)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - SecOCVerificationStatusCallout
     - 取值范围 (Range)
     - 函数 (Function)
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 设置SecOCVerificationStatusCallout类型的函数 (Set the function of SecOCVerificationStatusCallout type)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - SecOCVersionInfoApi
     - 取值范围 (Range)
     - STD_ON / STD_OFF
     - 默认取值 (Default value)
     - STD_OFF
   * - 
     - 参数描述 (Parameter Description)
     - 获取版本信息的API是否可用的开关 (Switch for checking if the API for getting version information is available)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - SecOCEcucPartitionRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 引用到EcucPartition，指示SecOC属于哪个EcucPartition (Indicate which EcucPartition SecOC belongs to.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 




SecOCRxPduProcessing
------------------------------------

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/SecOC/image9.png
   :alt: SecOCRxPduProcessing容器配置图 (Container Configuration Diagram for SecOCRxPduProcessing)
   :name: SecOCRxPduProcessing容器配置图 (Container Configuration Diagram for SecOCRxPduProcessing)
   :align: center


.. centered:: **表 SecOCRxPduProcessing属性描述 (Table SecOCRxPduProcessing Property Description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - SecOCAuthDataFreshnessLen
     - 取值范围 (Range)
     - 0 .. 65535
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 从AuthenticI-PDU中截取作为FreshnessValue的数据的长度，单位为bit (Extract the length of the data as FreshnessValue from AuthenticI-PDU in bits)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - SecOCAuthDataFreshnessLen参数被配置时，SecOCAuthDataFreshnessStartPosition参数必须被配置，SecOCUseAuthDataFreshness参数必须设置为TRUE (When the SecOCAuthDataFreshnessLen parameter is configured, the SecOCAuthDataFreshnessStartPosition parameter must be configured, and the SecOCUseAuthDataFreshness parameter must be set to TRUE.)
     - 
     - 
   * - SecOCAuthDataFreshnessStartPosition
     - 取值范围 (Range)
     - 0 .. 65535
     - 默认取值 (Default value)
     - STD_OFF
   * - 
     - 参数描述 (Parameter Description)
     - 从AuthenticI-PDU中截取作为FreshnessValue的数据的起始位置，单位为bit。计算位置从PDU的第一个字节的MSB开始。 (Extract the starting position of FreshnessValue from AuthenticI-PDU in bits. The calculation starts from the MSB of the first byte of PDU.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - SecOCAuthDataFreshnessStartPosition参数被配置时，SecOCAuthDataFreshnessLen参数必须被配置，SecOCUseAuthDataFreshness参数必须设置为TRUE (The SecOCAuthDataFreshnessStartPosition parameter must be configured when the SecOCAuthDataFreshnessLen parameter is configured, and the SecOCUseAuthDataFreshness parameter must be set to TRUE.)
     - 
     - 
   * - SecOCAuthenticationBuildAttempts
     - 取值范围 (Range)
     - 0 .. 65535
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 该参数表示authentication创建失败时可以重试的次数。 (This parameter indicates the number of times authentication can be retried when creation fails.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - SecOCAuthenticationVerifyAttempts
     - 取值范围 (Range)
     - 0 .. 65535
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 该参数表示校验SecuredI-PDU中的Authenticator失败时，可以再次尝试的次数。设置为0，则校验只进行一次。 (This parameter indicates the number of times an additional attempt can be made to validate the Authenticator in SecuredI-PDU when validation fails. Setting it to 0 means validation will only occur once.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - SecOCAuthInfoTruncLength
     - 取值范围 (Range)
     - 0 .. 65535
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 表示需要追加到SecuredI-PDU中的Authenticator截取长度，单位为bit (Length of the Authenticator to be appended to SecuredI-PDU, in bits)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - SecOCDataId
     - 取值范围 (Range)
     - 0 .. 65535
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - DataId，用于唯一的表示SecuredI-PDU (DataId，used for uniquely representing SecuredI-PDU)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - SecOCFreshnessValueId
     - 取值范围 (Range)
     - 0 .. 65535
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - SecOCFreshnessValueId。
     - 
     - 
   * - 
     - 
     - 可能是个计数器，也可能是时间值等。 (It might be a counter, or it could be a time value, etc.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - SecOCFreshnessValueLength
     - 取值范围 (Range)
     - 0 .. 64
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 表示完整的FreshnessValue的长度 (Length of the complete FreshnessValue representation)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - SecOCFreshnessValueTruncLength
     - 取值范围 (Range)
     - 0 .. 64
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 表示需要追加到SecuredI-PDU中的FreshnessValue截取长度。从LSB开始截取，设置为0表示不需要把FreshnessValue追加到SecuredI-PDU中。 (The length of the FreshnessValue to be appended to SecuredI-PDU. Starting from the LSB, set to 0 if FreshnessValue should not be appended to SecuredI-PDU.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - SecOCFreshnessCounterTxLength小于等于SecOCFreshnessCounterLength (SecOCFreshnessCounterTxLength <= SecOCFreshnessCounterLength)
     - 
     - 
   * - SecOCReceptionOverflowStrategy
     - 取值范围 (Range)
     - QUEUEREJECTREPLACE
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 该参数表示接收报文溢出时的策略 (This parameter indicates the strategy for handling received packet overflow.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - SecOCReceptionQueueSize
     - 取值范围 (Range)
     - 1 .. 65535
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 当接收溢出策略设置为QUEUE时，接收队列的长度 (When the receive overflow strategy is set to QUEUE, the length of the receive queue)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - SecOCReceptionOverflowStrategy= QUEUE
     - 
     - 
   * - SecOCUseAuthDataFreshness
     - 取值范围 (Range)
     - STD_ON / STD_OFF
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 表示是否使用AuthenticI-PDU中的一部分作为FreshnessValue (Indicate whether part of the AuthenticI-PDU is used as FreshnessValue)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - SecOCUseAuthDataFreshness参数设置为TRUE时，SecOCAuthDataFreshnessLen和SecOCAuthDataFreshnessStartPosition参数必须被配置 (When SecOCUseAuthDataFreshness is set to TRUE, the SecOCAuthDataFreshnessLen and SecOCAuthDataFreshnessStartPosition parameters must be configured.)
     - 
     - 
   * - SecOCVerificationStatusPropagationMode
     - 取值范围 (Range)
     - BOTHFAILURE_ONLYNONE
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - SecOC将校验的结果传递给SWC时需要采用的策略 (When transmitting the validation results to SWC, SecOC needs to adopt a strategy)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - SecOCAuthenticPduBuffLength
     - 取值范围 (Range)
     - 0 .. 65535
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 存储AuthenticI-PDU的buffer长度 (Buffer length for storing AuthenticI-PDU)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 该参数值不可配置，根据SecOCRxPduProcessing->SecOCRxAuthenticPduLayer.SecOCRxAuthenticLayerPduRef关联的PDU，从EcuC中获取该PDU的PduLength参数进行填充 (This parameter value is not configurable and is obtained from the PduLength parameter of the related PDU in EcuC based on the association with SecOCRxPduProcessing->SecOCRxAuthenticPduLayer.SecOCRxAuthenticLayerPduRef.)
     - 
     - 
   * - SecOCRxAuthServiceConfigRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 引用到一个CsmJob对象，表示进行校验时使用的加密算法 (Refer to a CsmJob object, indicating the encryption algorithm used during validation.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - SecOCSameBufferPduRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 引用到一个SecOCSameBufferPduCollection对象，指接收处理使用相同的buffer (Reference to a SecOCSameBufferPduCollection object, indicating reception processing using the same buffer.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 




SecOCRxAuthenticPduLayer
========================================

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/SecOC/image10.png
   :alt: SecOCRxAuthenticPduLayer容器配置图 (Container Configuration Diagram for SecOCRxAuthenticPduLayer)
   :name: SecOCRxAuthenticPduLayer容器配置图 (Container Configuration Diagram for SecOCRxAuthenticPduLayer)
   :align: center


.. centered:: **表 SecOCRxAuthenticPduLayer属性描述 (Table SecOCRxAuthenticPduLayer Properties Description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - SecOCPduType
     - 取值范围 (Range)
     - SECOC_IFPDUSECOC_TPPDU
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 表示AuthenticI-PDU的类型 (Indicates the type of AuthenticI-PDU)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - SecOCRxAuthenticLayerPduId
     - 取值范围 (Range)
     - 0 .. 65535
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 表示SecOCRxAuthenticLayerPduRef引用的PDU在SecOC中分配的序号 (Indicates the PDU sequence number allocated in SecOC for the PDU referenced by SecOCRxAuthenticLayerPduRef.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - SecOCRxAuthenticLayerPduRef
     - 取值范围 (Range)
     - EcuC中定义的PDU (PDU defined in EcuC)
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 指向一个PDU，该PDU表示从接收报文中解析出的AuthenticI-PDU (Point to a PDU, which represents the AuthenticI-PDU extracted from the received message.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 




SecOCRxPduSecuredArea
=====================================

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/SecOC/image11.png
   :alt: SecOCRxPduSecuredArea容器配置图 (SecOCRxPduSecuredArea Container Configuration Diagram)
   :name: SecOCRxPduSecuredArea容器配置图 (SecOCRxPduSecuredArea Container Configuration Diagram)
   :align: center


.. centered:: **表 SecOCRxPduSecuredArea属性描述 (Property Description of Table SecOCRxPduSecuredArea)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - SecOCSecuredRxPduLength
     - 取值范围 (Range)
     - 0 .. 4294967295
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 表示要传入Authenticator验证算法的AuthenticI-PDU的长度，单位为Byte (Indicates the length of the AuthenticI-PDU that will be passed to the Authenticator validation algorithm, in bytes)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - SecOCSecuredRxPduLength参数<=通过SecOCRxPduProcessing->SecOCRxAuthenticPduLayer.SecOCRxAuthenticLayerPduRef关联的PDU，从EcuC中获取该PDU的PduLength参数的值-SecOCSecuredRxPduOffset (Parameter SecOCSecuredRxPduLength <= PduLength value of the PDU retrieved from EcuC through SecOCRxPduProcessing->SecOCRxAuthenticPduLayer.SecOCRxAuthenticLayerPduRef - SecOCSecuredRxPduOffset)
     - 
     - 
   * - SecOCSecuredRxPduOffset
     - 取值范围 (Range)
     - 0 .. 4294967295
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 该参数表示要传入验证算法的AuthenticI-PDU的开始位置，单位为Byte (This parameter indicates the starting position in bytes of the AuthenticI-PDU to be passed into the validation algorithm.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - SecOCSecuredRxPduOffset参数必须小于通过SecOCRxPduProcessing->SecOCRxAuthenticPduLayer.SecOCRxAuthenticLayerPduRef关联的PDU，从EcuC中获取该PDU的PduLength参数的值 (The SecOCSecuredRxPduOffset parameter must be less than the PduLength value of the PDU obtained from EcuC through the association with SecOCRxAuthenticPduLayer.SecOCRxAuthenticLayerPduRef in SecOCRxPduProcessing.)
     - 
     - 




SecOCRxSecuredPduLayer
======================================

SecOCRxSecuredPdu
---------------------------------

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/SecOC/image12.png
   :alt: SecOCRxSecuredPdu容器配置图 (Container Configuration Diagram for SecOCRxSecuredPdu)
   :name: SecOCRxSecuredPdu容器配置图 (Container Configuration Diagram for SecOCRxSecuredPdu)
   :align: center


.. centered:: **表 SecOCRxSecuredPdu属性描述 (Table SecOCRxSecuredPdu Property Description)**

.. list-table::
   :widths: 17 17 17 17 16 16
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
     - 
   * - SecOCAuthPduHeaderLength
     - 取值范围 (Range)
     - 0 .. 4
     - 默认取值 (Default value)
     - 0
     - 
   * - 
     - 参数描述 (Parameter Description)
     - 表示SecuredI-PDU中的Header的长度，单位为Byte (Indicates the length of the Header in SecuredI-PDU, in Bytes)
     - 
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
     - 
   * - SecOCRxSecuredLayerPduId
     - 取值范围 (Range)
     - 0 .. 65535
     - 默认取值 (Default value)
     - 无
     - 
   * - 
     - 参数描述 (Parameter Description)
     - SecOC分配的PduId。PduR调用 (SecOC allocation of PduId. PduR call.)
     - 
     - 
     - 
   * - 
     - 
     - SecOC\_[If
     - Tp]RxIndic
     - 
     - 
   * - 
     - 
     - ation函数时使用该Id。 (Use this Id when calling the ation function.)
     - 
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
     - 
   * - SecOCSecuredRxPduVerification
     - 取值范围 (Range)
     - TRUE / FALSE
     - 默认取值 (Default value)
     - TRUE
     - 
   * - 
     - 参数描述 (Parameter Description)
     - 该参数表示是否要对接收到的SecuredI-PDU进行校验。如果设置为FALSE，则从SecuredI-PDU中解析出AuthenticI-PDU直接传递给上层，而不进行校验。 (This parameter indicates whether to verify the received SecuredI-PDU. If set to FALSE, AuthenticatedI-PDU is directly passed to the upper layer by parsing from the SecuredI-PDU without verification.)
     - 
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
     - 
   * - SecOCRxSecuredPduBuffLength
     - 取值范围 (Range)
     - 0 .. 65535
     - 默认取值 (Default value)
     - 无
     - 
   * - 
     - 参数描述 (Parameter Description)
     - 用于存放SecuredI-PDU的buffer的长度。 (The length of the buffer used for storing SecuredI-PDU.)
     - 
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 该参数值不可配置，根据SecOCRxSecuredPdu.SecOCRxSecuredLayerPduRef关联的PDU，从EcuC中获取该PDU的PduLength参数进行填充 (This parameter value is not configurable and is obtained by filling in the PduLength parameter of the PDU associated with SecOCRxSecuredPdu.SecOCRxSecuredLayerPduRef from EcuC.)
     - 
     - 
     - 
   * - SecOCRxSecuredLayerPduRef
     - 取值范围 (Range)
     - EcuC中定义的PDU (PDU defined in EcuC)
     - 默认取值 (Default value)
     - 无
     - 
   * - 
     - 参数描述 (Parameter Description)
     - 引用到一个EcuC中定义的PDU，该PDU表示接收到的SecuredI-PDU。 (Reference a PDU defined in an EcuC, which represents received SecuredI-PDU.)
     - 
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
     - 




SecOCRxSecuredPduCollection
-------------------------------------------

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/SecOC/image13.png
   :alt: SecOCRxSecuredPduCollection容器配置图 (SecOCRxSecuredPduCollection Container Configuration Diagram)
   :name: SecOCRxSecuredPduCollection容器配置图 (SecOCRxSecuredPduCollection Container Configuration Diagram)
   :align: center


.. centered:: **表 SecOCRxSecuredPduCollection属性描述 (Table SecOCRxSecuredPduCollection Property Description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - SecOCSecuredRxPduVerification
     - 取值范围 (Range)
     - TRUE / FALSE
     - 默认取值 (Default value)
     - TRUE
   * - 
     - 参数描述 (Parameter Description)
     - 该参数表示是否要对接收到的SecuredI-PDU进行校验。如果设置为FALSE，则从SecuredI-PDU中解析出AuthenticI-PDU直接传递给上层，而不进行校验。 (This parameter indicates whether to verify the received SecuredI-PDU. If set to FALSE, AuthenticatedI-PDU is directly passed to the upper layer by parsing from the SecuredI-PDU without verification.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 


SecOCRxAuthenticPdu
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/SecOC/image14.png
   :alt: SecOCRxAuthenticPdu容器配置图 (Container Configuration Diagram for SecOCRxAuthenticPdu)
   :name: SecOCRxAuthenticPdu容器配置图 (Container Configuration Diagram for SecOCRxAuthenticPdu)
   :align: center


.. centered:: **表 SecOCRxAuthenticPdu属性描述 (Table SecOCRxAuthenticPdu Properties Description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - SecOCAuthPduHeaderLength
     - 取值范围 (Range)
     - 0 .. 4
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - 表示使用PDUCollection功能的AuthenticI-PDU中的Header的长度，单位为Byte (Indicate the length of the Header in AuthenticI-PDU using PDUCollection functionality, in units of Byte)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - SecOCRxAuthenticPduId
     - 取值范围 (Range)
     - 0 .. 65535
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - SecOC分配的PduId。PduR调用SecOC_IfRxIndication函数时使用该Id。 (PDuId assigned by SecOC. This Id is used when PduR calls the SecOC_IfRxIndication function.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - SecOCRxColAuthenticPduBuffLength
     - 取值范围 (Range)
     - 0 .. 65535
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 用于存放AuthenticI-PDU的buffer的长度。 (The length of the buffer used for storing AuthenticI-PDU.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 该参数不可配置，值根据SecOCRxAuthenticPdu.SecOCRxAuthenticPduRef关联的PDU，从EcuC中获取该PDU的PduLength参数进行填充 (This parameter is not configurable and its value is obtained by filling with the PduLength parameter of the PDU associated with SecOCRxAuthenticPdu.SecOCRxAuthenticPduRef from EcuC.)
     - 
     - 
   * - SecOCRxAuthenticPduRef
     - 取值范围 (Range)
     - EcuC中定义的PDU (PDU defined in EcuC)
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 引用到一个EcuC中定义的PDU，该PDU表示接收到的AuthenticI-PDU。 (Reference a PDU defined in an EcuC, which represents received AuthenticI-PDU.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 




SecOCRxCryptographicPdu
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/SecOC/image15.png
   :alt: SecOCRxCryptographicPdu容器配置图 (SecOCRxCryptographicPdu Container Configuration Diagram)
   :name: SecOCRxCryptographicPdu容器配置图 (SecOCRxCryptographicPdu Container Configuration Diagram)
   :align: center


.. centered:: **表 SecOCRxCryptographicPdu属性描述 (Table SecOCRxCryptographicPdu Property Description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - SecOCRxCryptographicPduId
     - 取值范围 (Range)
     - 0 .. 65535
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - SecOC为 CryptographicI-PDU分配的Id，PduR调用SecOC_IfRxIndication函数时使用该Id。 (SecOC assigns an Id to the CryptographicI-PDU, which is used by PduR when calling the SecOC_IfRxIndication function.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - SecOCRxCryptographicPduBuffLength
     - 取值范围 (Range)
     - 0 .. 65535
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 存放CryptographicI-PDU的buffer的长度。 (The length of the buffer for storing CryptographicI-PDU.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 该参数不可配置，值根据SecOCRxCryptographicPdu.SecOCRxCryptographicPduRef关联的PDU，从EcuC中获取该PDU的PduLength参数进行填充 (This parameter is not configurable and its value is obtained by filling with the PduLength parameter of the PDU associated with SecOCRxCryptographicPdu.SecOCRxCryptographicPduRef from EcuC.)
     - 
     - 
   * - SecOCRxCryptographicPduRef
     - 取值范围 (Range)
     - EcuC中定义的PDU (PDU defined in EcuC)
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 指向一个PDU，该PDU表示CryptographicI-PDU。 (Point to a PDU, which represents CryptographicI-PDU.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 




SecOCUseMessageLink
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/SecOC/image16.png
   :alt: SecOCUseMessageLink容器配置图 (Container Configuration Diagram for SecOCUseMessageLink)
   :name: SecOCUseMessageLink容器配置图 (Container Configuration Diagram for SecOCUseMessageLink)
   :align: center

.. centered:: **表 SecOCUseMessageLink属性描述 (Table SecOCUseMessageLink Property Description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - SecOCMessageLinkLen
     - 取值范围 (Range)
     - 0 .. 65535
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - MessageLinker的长度，单位为bit (The length of MessageLinker, in bits)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - SecOCMessageLinkLen参数<=通过SecOCRxPduProcessing->SecOCRxAuthenticPduLayer.SecOCRxAuthenticLayerPduRef关联的PDU，从EcuC中获取该PDU的PduLength参数的值*8-SecOCUseMessageLink.SecOCMessageLinkPos (SecOCMessageLinkLen parameter <= through SecOCRxPduProcessing->SecOCRxAuthenticPduLayer.SecOCRxAuthenticLayerPduRef associated PDU, get the value of PduLength parameter from EcuC * 8 - SecOCUseMessageLink.SecOCMessageLinkPos)
     - 
     - 
   * - SecOCMessageLinkPos
     - 取值范围 (Range)
     - 0 .. 65535
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - MessageLinker的开始位置，单位为bit (The starting position of MessageLinker, in bits)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - SecOCMessageLinkPos参数必须小于通过SecOCRxPduProcessing->SecOCRxAuthenticPduLayer.SecOCRxAuthenticLayerPduRef关联的PDU，从EcuC中获取该PDU的PduLength参数的值\*8 (The SecOCMessageLinkPos parameter must be less than the PDU length value obtained by multiplying \*8 the PduLength parameter of the PDU retrieved from EcuC through the association with SecOCRxAuthenticPduLayer.SecOCRxAuthenticLayerPduRef in SecOCRxPduProcessing.)
     - 
     - 




SecOCSameBufferPduCollection
--------------------------------------------

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/SecOC/image17.png
   :alt: SecOCSameBufferPduCollection容器配置图 (Container Configuration Diagram for SecOCSameBufferPduCollection)
   :name: SecOCSameBufferPduCollection容器配置图 (Container Configuration Diagram for SecOCSameBufferPduCollection)
   :align: center


.. centered:: **表 SecOCSameBufferPduCollection属性描述 (Table SecOCSameBufferPduCollection Property Description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - SecOCBufferLength
     - 取值范围 (Range)
     - 0 .. 4294967295
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - 该SameBuffer对象的总长度 (The total length of the SameBuffer object)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 该参数值不可配置，其值为SecOCAuthenticPduBuffLength+SecOCSecuredPduBuffLength+SecOCColAuthenticPduBuffLength+SecOCCryptographicPduBuffLength (This parameter value is not configurable, its value is SecOCAuthenticPduBuffLength+SecOCSecuredPduBuffLength+SecOCColAuthenticPduBuffLength+SecOCCryptographicPduBuffLength)
     - 
     - 
   * - SecOCAuthenticPduBuffLength
     - 取值范围 (Range)
     - 0 .. 4294967295
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - 存放AuthenticI-PDU的buffer的长度。 (The length of the buffer for storing AuthenticI-PDU.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - SecOCSecuredPduBuffLength
     - 取值范围 (Range)
     - 0 .. 4294967295
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - 存放SecuredI-PDU的buffer的长度。 (The length of the buffer for storing SecuredI-PDU.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - SecOCColAuthenticPduBuffLength
     - 取值范围 (Range)
     - 0 .. 4294967295
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - 存放PduCollection中的AuthenticI-PDU的buffer的长度。 (The length of the buffer storing AuthenticI-PDU in PduCollection.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - SecOCCryptographicPduBuffLength
     - 取值范围 (Range)
     - 0 .. 4294967295
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - 存放PduCollection中的CryptographicI-PDU的buffer的长度。 (The length of the buffer storing Cryptographic I-PDU in PduCollection.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 




SecOCTxPduProcessing
------------------------------------

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/SecOC/image18.png
   :alt: SecOCTxPduProcessing容器配置图 (Container Configuration Diagram for SecOCTxPduProcessing)
   :name: SecOCTxPduProcessing容器配置图 (Container Configuration Diagram for SecOCTxPduProcessing)
   :align: center


.. centered:: **表 SecOCTxPduProcessing属性描述 (Table SecOCTxPduProcessing Property Description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - SecOCAuthDataFreshnessLen
     - 取值范围 (Range)
     - 0 .. 65535
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - authentication创建时可以尝试的次数 (trials for authentication to attempt when created)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - SecOCAuthInfoTruncLength
     - 取值范围 (Range)
     - 0 .. 65535
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 表示需要追加到SecuredI-PDU中的Authenticator截取长度，单位为bit (Length of the Authenticator to be appended to SecuredI-PDU, in bits)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - SecOCDataId
     - 取值范围 (Range)
     - 0 .. 65535
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - DataId，用于唯一的表示SecuredI-PDU (DataId，used for uniquely representing SecuredI-PDU)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - SecOCFreshnessValueId
     - 取值范围 (Range)
     - 0 .. 65535
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - SecOCFreshnessValueId。
     - 
     - 
   * - 
     - 
     - 可能是个计数器，也可能是时间值等。 (It might be a counter, or it could be a time value, etc.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - SecOCFreshnessValueLength
     - 取值范围 (Range)
     - 0 .. 64
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 表示完整的FreshnessValue的长度 (Length of the complete FreshnessValue representation)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - SecOCFreshnessValueTruncLength
     - 取值范围 (Range)
     - 0 .. 64
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 表示需要追加到SecuredI-PDU中的FreshnessValue截取长度。从LSB开始截取，设置为0表示不需要把FreshnessValue追加到SecuredI-PDU中。 (The length of the FreshnessValue to be appended to SecuredI-PDU. Starting from the LSB, set to 0 if FreshnessValue should not be appended to SecuredI-PDU.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - SecOCFreshnessValueTruncLength参数的值必须小于等于SecOCFreshnessValueLength参数的值 (The value of SecOCFreshnessValueTruncLength must be less than or equal to the value of SecOCFreshnessValueLength parameter.)
     - 
     - 
   * - SecOCProvideTxTruncatedFreshnessValue
     - 取值范围 (Range)
     - STD_ON / STD_OFF
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 表示是否可以从FVM的接口获取到截取后的FreshnessValue，如果设置为TRUE，则不需要自己截取，SecOC直接将该信息追加到AuthenticI-PDU后。 (Indicate whether the FreshnessValue after truncation can be obtained from the FVM interface. If set to TRUE, there is no need for manual truncation; SecOC will append this information directly to the AuthenticI-PDU.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - SecOCUseTxConfirmation
     - 取值范围 (Range)
     - STD_ON / STD_OFF
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 表示SecOC_SpduTxConfirmation函数是否会被调用。 (Indicates whether the SecOC_SpduTxConfirmation function will be called.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - SecOCAuthenticPduBuffLength
     - 取值范围 (Range)
     - 0 .. 65535
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 存储AuthenticI-PDU的buffer长度 (Buffer length for storing AuthenticI-PDU)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 该参数不可配置，值根据SecOCTxPduProcessing->SecOCTxAuthenticPduLayer.SecOCTxAuthenticLayerPduRef关联的PDU，从EcuC中获取该PDU的PduLength参数进行填充 (This parameter is not configurable, and its value is obtained from the PduLength parameter of the PDU associated with SecOCTxPduProcessing->SecOCTxAuthenticPduLayer.SecOCTxAuthenticLayerPduRef for filling.)
     - 
     - 
   * - SecOCSameBufferPduRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 引用到一个SecOCSameBufferPduCollection对象，几个发送PDU使用相同的buffer (Referencing a SecOCSameBufferPduCollection object, several send PDU use the same buffer.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - SecOCTxAuthServiceConfigRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 引用到CsmJob对象，表示认证过程使用的加密算法。 (Indicates the encryption algorithm used in the authentication process for the CsmJob object.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 




SecOCTxAuthenticPduLayer
========================================

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/SecOC/image19.png
   :alt: SecOCTxAuthenticPduLayer容器配置图 (Container Configuration Diagram for SecOCTxAuthenticPduLayer)
   :name: SecOCTxAuthenticPduLayer容器配置图 (Container Configuration Diagram for SecOCTxAuthenticPduLayer)
   :align: center


.. centered:: **表 SecOCTxAuthenticPduLayer属性描述 (Property Description of Table SecOCTxAuthenticPduLayer)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - SecOCPduType
     - 取值范围 (Range)
     - SECOC_IFPDUSECOC_TPPDU
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 表示AuthenticI-PDU的类型 (Indicates the type of AuthenticI-PDU)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - SecOCTxAuthenticLayerPduId
     - 取值范围 (Range)
     - 0 .. 65535
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 表示SecOCTxAuthenticLayerPduRef引用的PDU在SecOC中分配的序号 (Indicates the sequence number allocated in SecOC for the PDU referenced by SecOCTxAuthenticLayerPduRef.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - SecOCTxAuthenticLayerPduRef
     - 取值范围 (Range)
     - EcuC中定义的PDU (PDU defined in EcuC)
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 指向一个PDU，该PDU表示要发送的AuthenticI-PDU (Point to a PDU, which represents the AuthenticI-PDU to be sent.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 




SecOCTxPduSecuredArea
=====================================

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/SecOC/image20.png
   :alt: SecOCTxPduSecuredArea容器配置图 (Container Configuration Diagram for SecOCTxPduSecuredArea)
   :name: SecOCTxPduSecuredArea容器配置图 (Container Configuration Diagram for SecOCTxPduSecuredArea)
   :align: center


.. centered:: **表 SecOCTxPduSecuredArea属性描述 (Property Description of Table SecOCTxPduSecuredArea)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - SecOCSecuredTxPduLength
     - 取值范围 (Range)
     - 0 .. 4294967295
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 表示要传入Authenticator验证算法的AuthenticI-PDU的长度，单位为Byte (Indicates the length of the AuthenticI-PDU that will be passed to the Authenticator validation algorithm, in bytes)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - SecOCSecuredTxPduLength参数<=通过SecOCTxPduProcessing->SecOCTxAuthenticPduLayer.SecOCTxAuthenticLayerPduRef关联的PDU，从EcuC中获取该PDU的PduLength参数的值-SecOCTxPduSecuredArea.SecOCSecuredTxPduOffset (SecOCSecuredTxPduLength parameter <= Through SecOCTxPduProcessing->SecOCTxAuthenticPduLayer.SecOCTxAuthenticLayerPduRef associated PDU, get the value of the PduLength parameter from EcuC - SecOCTxPduSecuredArea.SecOCSecuredTxPduOffset)
     - 
     - 
   * - SecOCSecuredTxPduOffset
     - 取值范围 (Range)
     - 0 .. 4294967295
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 该参数表示要传入验证算法的AuthenticI-PDU的开始位置，单位为Byte (This parameter indicates the starting position in bytes of the AuthenticI-PDU to be passed into the validation algorithm.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - SecOCSecuredTxPduOffset参数必须小于通过SecOCTxPduProcessing->SecOCTxAuthenticPduLayer.SecOCTxAuthenticLayerPduRef关联的PDU，从EcuC中获取该PDU的PduLength参数的值 (The SecOCSecuredTxPduOffset parameter must be less than the PDU length value retrieved from EcuC for the PDU associated through SecOCTxPduProcessing->SecOCTxAuthenticPduLayer.SecOCTxAuthenticLayerPduRef.)
     - 
     - 




SecOCTxSecuredPduLayer
======================================

SecOCTxSecuredPdu
---------------------------------

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/SecOC/image21.png
   :alt: SecOCTxSecuredPdu容器配置图 (Container Configuration Diagram for SecOCTxSecuredPdu)
   :name: SecOCTxSecuredPdu容器配置图 (Container Configuration Diagram for SecOCTxSecuredPdu)
   :align: center


.. centered:: **表 SecOCTxSecuredPdu属性描述 (Property Description of表 SecOCTxSecuredPdu)**

.. list-table::
   :widths: 17 17 17 17 16 16
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
     - 
   * - SecOCAuthPduHeaderLength
     - 取值范围 (Range)
     - 0 .. 4
     - 默认取值 (Default value)
     - 0
     - 
   * - 
     - 参数描述 (Parameter Description)
     - 表示SecuredI-PDU中的Header的长度，单位为Byte (Indicates the length of the Header in SecuredI-PDU, in Bytes)
     - 
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
     - 
   * - SecOCTxSecuredLayerPduId
     - 取值范围 (Range)
     - 0 .. 65535
     - 默认取值 (Default value)
     - 无
     - 
   * - 
     - 参数描述 (Parameter Description)
     - SecOC分配的PduId。PduR调用Se (SecOC Assigned PduId. PduR calls Se)
     - 
     - 
     - 
   * - 
     - 
     - cOC\_[If
     - Tp]TxConfirm
     - 
     - 
   * - 
     - 
     - ation函数和TriggerTransmit函数时使用该Id。 (When using the Id with the ation function and TriggerTransmit function.)
     - 
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
     - 
   * - SecOCTxSecuredPduBuffLength
     - 取值范围 (Range)
     - 0 .. 65535
     - 默认取值 (Default value)
     - 无
     - 
   * - 
     - 参数描述 (Parameter Description)
     - 用于存放SecuredI-PDU的buffer的长度。 (The length of the buffer used for storing SecuredI-PDU.)
     - 
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - SecOCTxSecuredPduBuffLength参数设置为不可配置，值根据SecOCTxSecuredPdu.SecOCTxSecuredLayerPduRef关联的PDU，从EcuC中获取该PDU的PduLength参数进行填充 (The SecOCTxSecuredPduBuffLength parameter is set to non-configurable, with its value obtained by filling in the PduLength parameter of the PDU associated with SecOCTxSecuredPdu.SecOCTxSecuredLayerPduRef from EcuC.)
     - 
     - 
     - 
   * - SecOCTxSecuredLayerPduRef
     - 取值范围 (Range)
     - EcuC中定义的PDU (PDU defined in EcuC)
     - 默认取值 (Default value)
     - 无
     - 
   * - 
     - 参数描述 (Parameter Description)
     - 引用到一个EcuC中定义的PDU，该PDU表示要发送的SecuredI-PDU。 (Reference a PDU defined in an EcuC, which represents the SecuredI-PDU to be sent.)
     - 
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
     - 




SecOCTxSecuredPduCollection
-------------------------------------------

SecOCTxAuthenticPdu
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/SecOC/image22.png
   :alt: SecOCTxAuthenticPdu容器配置图 (Container Configuration Diagram for SecOCTxAuthenticPdu)
   :name: SecOCTxAuthenticPdu容器配置图 (Container Configuration Diagram for SecOCTxAuthenticPdu)
   :align: center


.. centered:: **表 SecOCTxAuthenticPdu属性描述 (Property Description of SecOCTxAuthenticPdu Table)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - SecOCAuthPduHeaderLength
     - 取值范围 (Range)
     - 0 .. 4
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - 表示使用PDUCollection功能的AuthenticI-PDU中的Header的长度，单位为Byte (Indicate the length of the Header in AuthenticI-PDU using PDUCollection functionality, in units of Byte)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - SecOCTxAuthenticPduId
     - 取值范围 (Range)
     - 0 .. 65535
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - SecOC分配的PduId。PduR调用SecOC_IfTxConfirmation函数和TriggerTransmit函数时使用该Id。 (PduId allocated by SecOC. This Id is used when PduR calls the SecOC_IfTxConfirmation function and the TriggerTransmit function.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - SecOCTxColAuthenticPduBuffLength
     - 取值范围 (Range)
     - 0 .. 65535
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 用于存放AuthenticI-PDU的buffer的长度。 (The length of the buffer used for storing AuthenticI-PDU.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - SecOCTxColAuthenticPduBuffLength参数不可配置，值根据SecOCTxAuthenticPdu.SecOCTxAuthenticPduRef关联的PDU，从EcuC中获取该PDU的PduLength参数进行填充 (The SecOCTxColAuthentiPduBuffLength parameter is not configurable; its value is obtained by filling in with the PduLength parameter of the PDU associated with SecOCTxAuthenticPdu.SecOCTxAuthenticPduRef from EcuC.)
     - 
     - 
   * - SecOCTxAuthenticPduRef
     - 取值范围 (Range)
     - EcuC中定义的PDU (PDU defined in EcuC)
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 引用到一个EcuC中定义的PDU，该PDU表示要发送的AuthenticI-PDU。 (Reference a PDU defined in an EcuC, which represents the Authentici-PDU to be sent.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 




SecOCTxCryptographicPdu
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/SecOC/image23.png
   :alt: SecOCTxCryptographicPdu容器配置图 (SecOCTxCryptographicPdu Container Configuration Diagram)
   :name: SecOCTxCryptographicPdu容器配置图 (SecOCTxCryptographicPdu Container Configuration Diagram)
   :align: center


.. centered:: **表 SecOCTxCryptographicPdu属性描述 (Table SecOCTxCryptographicPdu Properties Description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - SecOCTxCryptographicPduId
     - 取值范围 (Range)
     - 0 .. 65535
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - SecOC为 CryptographicI-PDU分配的Id，PduR调用SecOC_IfTxConfirmation函数和TriggerTransmit函数时使用该Id。 (SecOC assigns an Id to the CryptographicI-PDU, which is used by PduR when calling the SecOC_IfTxConfirmation function and the TriggerTransmit function.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - SecOCTxCryptographicPduBuffLength
     - 取值范围 (Range)
     - 0 .. 65535
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 存放CryptographicI-PDU的buffer的长度。 (The length of the buffer for storing CryptographicI-PDU.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - SecOCTxCryptographicPduBuffLength参数不可配置，值根据SecOCTxCryptographicPdu.SecOCTxCryptographicPduRef关联的PDU，从EcuC中获取该PDU的PduLength参数进行填充 (The SecOCTxCryptographicPduBuffLength parameter is not configurable; its value is obtained based on the PDU referenced by SecOCTxCryptographicPdu.SecOCTxCryptographicPduRef, and it is filled with the PduLength parameter of that PDU from EcuC.)
     - 
     - 
   * - SecOCTxCryptographicPduRef
     - 取值范围 (Range)
     - EcuC中定义的PDU (PDU defined in EcuC)
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 指向一个PDU，该PDU表示要发送的CryptographicI-PDU。 (Point to a PDU, which represents the CryptographicI-PDU to be sent.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 




.. _secocusemessagelink-1:

SecOCUseMessageLink
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/SecOC/image24.png
   :alt: SecOCUseMessageLink容器配置图11 (Container Configuration Diagram for SecOCUseMessageLink)
   :name: SecOCUseMessageLink容器配置图11 (Container Configuration Diagram for SecOCUseMessageLink)
   :align: center


.. centered:: **表 SecOCUseMessageLink属性描述 (Table SecOCUseMessageLink Property Description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - SecOCMessageLinkLen
     - 取值范围 (Range)
     - 0 .. 65535
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - MessageLinker的长度，单位为bit (The length of MessageLinker, in bits)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - SecOCMessageLinkLen参数<=通过SecOCTxPduProcessing->SecOCTxAuthenticPduLayer.SecOCTxAuthenticLayerPduRef关联的PDU，从EcuC中获取该PDU的PduLength参数的值*8-SecOCUseMessageLink.SecOCMessageLinkPos (SecOCMessageLinkLen parameter <= through SecOCTxPduProcessing->SecOCTxAuthenticPduLayer.SecOCTxAuthenticLayerPduRef associated PDU, get the value of PduLength parameter from EcuC * 8 - SecOCUseMessageLink.SecOCMessageLinkPos)
     - 
     - 
   * - SecOCMessageLinkPos
     - 取值范围 (Range)
     - 0 .. 65535
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - MessageLinker的开始位置，单位为bit (The starting position of MessageLinker, in bits)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - SecOCMessageLinkPos参数必须小于通过SecOCTxPduProcessing->SecOCTxAuthenticPduLayer.SecOCTxAuthenticLayerPduRef关联的PDU，从EcuC中获取该PDU的PduLength参数的值*8 (The SecOCMessageLinkPos parameter must be less than the PduLength value of the PDU retrieved from EcuC via the association through SecOCTxPduProcessing->SecOCTxAuthenticPduLayer.SecOCTxAuthenticLayerPduRef * 8)
     - 
     - 
