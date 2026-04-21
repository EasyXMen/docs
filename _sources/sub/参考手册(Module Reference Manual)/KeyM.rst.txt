KeyM
#################################

:strong:`缩写词注解 (Abbreviation Notes):`

.. list-table::
   :widths: 34 33 33
   :header-rows: 1

   * - 缩写词 (Abbreviation)
     - 解释/描述 (Explanation/Description)
     - 中文解释 (Chinese explanation)
   * - CSM
     - Crypto Service Manager
     - 加密服务管理 (Encryption Service Management)
   * - CRYIF
     - Crypto Interface
     - 加密接口层 (Encrypted Interface Layer)
   * - CRYPTO
     - Crypto Driver
     - 加密驱动（硬件驱动或者软件驱动） (Encryption Driver (hardware driver or software driver))
   * - DET
     - Default Error Tracer
     - 开发错误检测模块 (Develop an error detection module)
   * - HSM
     - Hardware Security Module
     - 硬件中用于计算加密算法的模块（相当于另外一块CPU） (A module for computing encryption algorithms in hardware (equivalent to another CPU))
   * - Job
     - CsmJob
     - CSM模块中的一个加密处理任务，一般每个Job会引用到一个cryptographicprimitive (An encryption processing task in the CSM module generally references one cryptographic primitive per Job.)




简介 (Introduction)
=================================

在一个加密功能中，密钥和证书的功能占比重很大。首先，密钥是一种参数，它是在明文转换为密文或将密文转换为明文的算法中输入的参数。许多加密算法需要使用到密钥，因此，就需要keyM模块来管理密钥，而keyM对于密钥的管理主要体现在对密钥的更新和生成密钥方面。

In an encryption function, the proportion of key and certificate functions is significant. First, a key is a parameter that is input into the algorithm for converting plaintext to ciphertext or vice versa. Many encryption algorithms require the use of keys, so the keyM module is needed to manage these keys. The management by keyM mainly involves updating keys and generating new keys.

而证书对网络用户在网络交流中的信息和数据等以加密或解密的形式保证了信息和数据的完整性和安全性。KeyM模块可以实现证书的链的配置保存与验证，这使得网络中的信息和数据的安全性更高。

And certificates ensure the integrity and security of information and data in online communications through encryption or decryption forms. The KeyM module can achieve configuration, storage, and validation of certificate chains, further enhancing the security of information and data in the network.

参考资料 (Reference materials)
------------------------------------------

[1] AUTOSAR_SWS_KeyManager.pdf，R19-11

功能描述 (Function Description)
===========================================

Key Management分为两部分：key子模块和证书子模块。

Key Management is divided into two parts: the key submodule and the certificate submodule.

key子模块通过会话模式更新key及key元素，当会话开启后，可以对key进行更新，结束会话后，更新的key将被置成可用状态。

The key sub-module updates the key and key elements in session mode. Once the session is activated, the key can be updated. Upon ending the session, the updated key will become available.

key子模块可以根据配置的需求，利用HSM的功能派生出新的key。

The key sub-module can derive new keys based on configuration requirements using HSM functionality.

证书子模块允许配置证书链，在配置中将证书的属性和关系设置好，上层应用通过API将证书数据传给keyM后，证书子模块将根据配置内容及HSM按照标准结构解析的证书存储进配置的位置（NVM、CSM或RAM）。

The certificate sub-module allows configuring certificate chains, setting the properties and relationships of certificates in the configuration. After upper-layer applications transmit certificate data to keyM via APIs, the certificate sub-module will store the certificates according to the configuration content and HSM's standard structure into the designated positions (NVM, CSM, or RAM).

在存储之前将对证书进行解析与验证操作，以确定该证书的可靠性。

Before storage, the certificate will be parsed and verified to determine its reliability.

源文件描述 (Source file description)
===============================================

.. centered:: **表 KeyM组件文件描述 (Table Description of KeyM Component File)**

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 文件 (Files)
     - 说明 (Description)
   * - KeyM.c
     - KeyM模块源文件，包含了API函数的实现。 (Source files for the KeyM module, which include the implementation of API functions.)
   * - KeyM.h
     - KeyM模块头文件，包含了API函数的扩展声明并定义了配置的数据结构。 (KeyM module header file contains extended declarations of API functions and defines the configuration data structures.)
   * - KeyM \_Cfg.h
     - 定义KeyM模块预编译时用到的配置参数。 (Define configuration parameters for the KeyM module during pre-compilation.)
   * - KeyM \_Cfg.c
     - KeyM模块配置生成文件。 (KeyM module configuration generation file.)
   * - SchM_KeyM.h
     - 声明KeyM模块需要循环调用的API。 (Declare the APIs that need to be cyclically called for the KeyM module.)
   * - Rte_KeyM_Type.h
     - 定义其它模块可能使用的KeyM模块的数据结构。 (Define the data structure of the KeyM module, which other modules may use.)
   * - KeyM_Externals.c
     - KeyM模块源文件，包含KeyM模块外部实现的接口。 (Source files for the KeyM module, containing the external interfaces of the KeyM module's implementation.)
   * - KeyM_Externals.h
     - KeyM模块头文件，定义KeyM模块外部实现的接口。 (KeyM module header file, defines the interfaces of KeyM module external implementations.)
   * - KeyM_Internal.h
     - KeyM内部变量 (Internal Variables of KeyM)
   * - KeyM_MemMap.h
     - KeyM模块的内存映射 (Memory mapping of the KeyM module)
   * - KeyM_Type.h
     - KeyM的配置类型结构 (The configuration type structure of KeyM)




.. figure:: ../../_static/参考手册(Module_Reference_Manual)/KeyM/image1.png
   :alt: KeyM组件文件交互图 (Component File Interaction Diagram for KeyM)
   :name: KeyM组件文件交互图 (Component File Interaction Diagram for KeyM)
   :align: center


API接口 (API Interface)
=====================================

类型定义 (Type definition)
--------------------------------------

KeyM_Certificate类型定义 (KeyM_Certificate Type Definition)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 名称 (Name)
     - KeyM_Certificate
   * - 类型 (Type)
     - structure
   * - 范围 (Range)
     - 无
   * - 描述 (Description)
     - 证书基本配置结构 (Certificate basic configuration structure)




KeyM_CertificateElement类型定义 (KeyM_CertificateElement Type Definition)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 名称 (Name)
     - KeyM_CertificateElement
   * - 类型 (Type)
     - structure
   * - 范围 (Range)
     - 无
   * - 描述 (Description)
     - 证书元素基本配置结构 (Basic configuration structure of certificate elements)




KeyM_CertificateElementVerification类型定义 (Type Definition for KeyM_CertificateElementVerification)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 名称 (Name)
     - KeyM_CertificateElementVerification
   * - 类型 (Type)
     - structure
   * - 范围 (Range)
     - 无
   * - 描述 (Description)
     - 证书元素验证基本配置结构 (Certificate element validation basic configuration structure)




KeyM_CertificateElementRule类型定义 (KeyM_CertificateElementRule Type Definition)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 名称 (Name)
     - KeyM_CertificateElementRule
   * - 类型 (Type)
     - structure
   * - 范围 (Range)
     - 无
   * - 描述 (Description)
     - 证书元素验证规则 (Certificate element validation rules)




KeyM_CertificateElementCondition类型定义 (TypeDefinitionForKeyM_CertificateElementCondition)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 名称 (Name)
     - KeyM_CertificateElementCondition
   * - 类型 (Type)
     - structure
   * - 范围 (Range)
     - 无
   * - 描述 (Description)
     - 证书元素验证条件 (Certificate element validation conditions)




KeyM_CertificateElementConditionValue类型定义 (TypeDefinitionForKeyM_CertificateElementConditionValue)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 名称 (Name)
     - KeyM_CertificateElementConditionValue
   * - 类型 (Type)
     - structure
   * - 范围 (Range)
     - 无
   * - 描述 (Description)
     - 证书元素验证条件值 (Certificate element validation condition value)




KeyM_CertificateElementConditionArrayElement类型定义 (Type definition for KeyM_CertificateElementConditionArrayElement)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 名称 (Name)
     - KeyM_CertificateElementConditionArrayElement
   * - 类型 (Type)
     - structure
   * - 范围 (Range)
     - 无
   * - 描述 (Description)
     - 证书元素验证数组比较值 (Certificate element validation array compare value)




KeyM_CryptoKey类型定义 (KeyM_CryptoKey Type Definition)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 名称 (Name)
     - KeyM_CryptoKey
   * - 类型 (Type)
     - structure
   * - 范围 (Range)
     - 无
   * - 描述 (Description)
     - 密钥基本配置结构 (Key basic configuration structure)




输入函数描述 (Describe the input function:)
-----------------------------------------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 输入模块 (Input Module)
     - API
   * - Det
     - Det_ReportError
   * - CSM
     - Csm_KeyElementGet
   * - 
     - Csm_KeyElementSet
   * - 
     - Csm_KeySetValid
   * - 
     - Csm_KeyDerive
   * - 
     - Csm_SignatureVerify
   * - NVM
     - NvM_ReadBlock
   * - 
     - NvM_WriteBlock
   * - StbM
     - StbM_GetCurrentTime




静态接口函数定义 (Static interface function definition)
---------------------------------------------------------------

KeyM_Init函数定义 (The KeyM_Init function definition)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - KeyM_Init
     - 
     - 
   * - 函数原型： (Function prototype:)
     - void KeyM_Init (constKeyM_ConfigType\*ConfigPtr)
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
     - 否 (No)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - ConfigPtr
     - 值域： (Domain:)
     - NULL_PTR
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
     - 初始化KeyM模块 (Initialize KeyM module)
     - 
     - 




KeyM_Deinit函数定义 (The KeyM_Deinit function definition)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - KeyM_Deinit
     - 
     - 
   * - 函数原型： (Function prototype:)
     - static FUNC(void,KEYM_CODE)KeyM_Deinit(void)
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
     - 否 (No)
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
     - 将密钥管理模块重置为未初始化状态 (Reset the key management module to an uninitialized state)
     - 
     - 




KeyM_GetVersionInfo函数定义 (The KeyM_GetVersionInfo function definition)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - KeyM_GetVersionInfo
     - 
     - 
   * - 函数原型： (Function prototype:)
     - voidKeyM_GetVersionInfo(Std_VersionInfoType\*VersionInfo)
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
     - 否 (No)
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
     - VersionInfo
     - 
     - 
   * - 返回值： (Return Value:)
     - 无
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 提供版本信息 (Provide version information)
     - 
     - 




KeyM_Start函数定义 (The KeyM_Start function definition)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - KeyM_Start
     - 
     - 
   * - 函数原型： (Function prototype:)
     - staticFUNC(Std_ReturnType,KEYM_CODE)
     - 
     - 
   * - 
     - KeyM_Start
     - 
     - 
   * - 
     - (
     - 
     - 
   * - 
     - VAR(KeyM_StartType,KEYM_VAR)StartType,
     - 
     - 
   * - 
     - P2CONST(uint8,AUTOMATIC,KEYM_APPL_CONST)RequestData,
     - 
     - 
   * - 
     - VAR(uint16,KEYM_VAR)RequestDataLength,
     - 
     - 
   * - 
     - P2VAR(uint8,AUTOMATIC,KEYM_APPL_DATA)ResponseData,
     - 
     - 
   * - 
     - P2VAR(uint16,AUTOMATIC,KEYM_APPL_DATA)ResponseDataLength
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
     - 否 (No)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - StartType
     - 值域： (Domain:)
     - 无
   * - 
     - RequestData
     - 
     - 无
   * - 
     - RequestDataLength
     - 
     - 无
   * - 输入输出参数： (Input Output Parameters:)
     - ResponseDataLength
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - ResponseData
     - 
     - 
   * - 返回值： (Return Value:)
     - Std_ReturnType
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 允许秘钥更新 (Allow key updates)
     - 
     - 




KeyM_Prepare函数定义 (The KeyM_Prepare function definition)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - KeyM_Prepare
     - 
     - 
   * - 函数原型： (Function prototype:)
     - staticFUNC(Std_ReturnType,KEYM_CODE)
     - 
     - 
   * - 
     - KeyM_Prepare(
     - 
     - 
   * - 
     - P2CONST(uint8,AUTOMATIC,KEYM_APPL_CONST)RequestData,
     - 
     - 
   * - 
     - VAR(uint16,KEYM_VAR)RequestDataLength,
     - 
     - 
   * - 
     - P2VAR(uint8,AUTOMATIC,KEYM_APPL_DATA)ResponseData,
     - 
     - 
   * - 
     - P2VAR(uint16,AUTOMATIC,KEYM_APPL_DATA)ResponseDataLength
     - 
     - 
   * - 
     - )
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
     - 否 (No)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - RequestData
     - 值域： (Domain:)
     - 无
   * - 
     - RequestDataLength
     - 
     - 无
   * - 输入输出参数： (Input Output Parameters:)
     - ResponseDataLength
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - ResponseData
     - 
     - 
   * - 返回值： (Return Value:)
     - Std_ReturnType
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 准备密钥更新，主要目的是为密钥服务器的密钥操作提供信息 (Prepare for key updates, primarily aimed at providing information for key operations on the key server.)
     - 
     - 




KeyM_Update函数定义 (The KeyM_Update function definition)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - KeyM_Update
     - 
     - 
   * - 函数原型： (Function prototype:)
     - staticFUNC(Std_ReturnType,KEYM_CODE)
     - 
     - 
   * - 
     - KeyM_Update(
     - 
     - 
   * - 
     - P2CONST(uint8,AUTOMATIC,KEYM_APPL_CONST)KeyNamePtr,
     - 
     - 
   * - 
     - VAR(uint16,KEYM_VAR)KeyNameLength,
     - 
     - 
   * - 
     - P2CONST(uint8,AUTOMATIC,KEYM_APPL_CONST)RequestDataPtr,
     - 
     - 
   * - 
     - VAR(uint16,KEYM_VAR)RequestDataLength,
     - 
     - 
   * - 
     - P2VAR(uint8,AUTOMATIC,KEYM_APPL_DATA)ResultDataPtr,
     - 
     - 
   * - 
     - VAR(uint16,KEYM_VAR)ResultDataMaxLength
     - 
     - 
   * - 
     - )
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x06
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 异步 (Asynchronous)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 否 (No)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - KeyNamePtr
     - 值域： (Domain:)
     - 无
   * - 
     - KeyNameLength
     - 
     - 无
   * - 
     - RequestDataPtr
     - 
     - 无
   * - 
     - RequestDataLength
     - 
     - 无
   * - 
     - ResultDataMaxLength
     - 
     - 无
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - ResultDataPtr
     - 
     - 
   * - 返回值： (Return Value:)
     - Std_ReturnType
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 启动生成或更新密钥 (Generate or update key)
     - 
     - 




KeyM_Finalize函数定义 (The KeyM_Finalize function definition)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - KeyM_Finalize
     - 
     - 
   * - 函数原型： (Function prototype:)
     - Std_ReturnTypeKeyM_Finalize (const uint8\*RequestDataPtr,uint16RequestDataLength,uint8\*ResponseDataPtr,uint16ResponseMaxDataLength)
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x07
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 异步 (Asynchronous)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 否 (No)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - RequestDataPtr
     - 值域： (Domain:)
     - 无
   * - 
     - RequestDataLength
     - 
     - 无
   * - 输入输出参数： (Input Output Parameters:)
     - ResponseMaxDataLength
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - ResponseDataPtr
     - 
     - 
   * - 返回值： (Return Value:)
     - Std_ReturnType
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 完成密钥更新，并将密钥操作返回到空闲模式 (Complete key update and return key operation to idle mode)
     - 
     - 




KeyM_Verify函数定义 (Definition of KeyM_Verify function)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - KeyM_Verify
     - 
     - 
   * - 函数原型： (Function prototype:)
     - staticFUNC(Std_ReturnType,KEYM_CODE)
     - 
     - 
   * - 
     - KeyM_Verify
     - 
     - 
   * - 
     - (
     - 
     - 
   * - 
     - P2CONST(uint8,AUTOMATIC,KEYM_APPL_DATA)KeyNamePtr,
     - 
     - 
   * - 
     - uint16KeyNameLength,
     - 
     - 
   * - 
     - P2CONST(uint8,AUTOMATIC,KEYM_APPL_DATA)RequestData,
     - 
     - 
   * - 
     - uint16RequestDataLength,
     - 
     - 
   * - 
     - P2VAR(uint8,AUTOMATIC,KEYM_APPL_DATA)ResponseData,
     - 
     - 
   * - 
     - P2VAR(uint16,AUTOMATIC,KEYM_APPL_DATA)ResponseDataLength
     - 
     - 
   * - 
     - )
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x08
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 取决于配置 (Depends on configuration)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 否 (No)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - KeyNamePtr
     - 值域： (Domain:)
     - 无
   * - 
     - KeyNameLength
     - 
     - 无
   * - 
     - RequestData
     - 
     - 无
   * - 
     - RequestDataLength
     - 
     - 无
   * - 输入输出参数： (Input Output Parameters:)
     - ResponseDataLength
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - ResponseData
     - 
     - 
   * - 返回值： (Return Value:)
     - Std_ReturnType
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 验证密钥 (Verify Key)
     - 
     - 




KeyM_ServiceCertificate函数定义 (The KeyM_ServiceCertificate function definition)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - KeyM_ServiceCertificate
     - 
     - 
   * - 函数原型： (Function prototype:)
     - staticFUNC(Std_ReturnType,KEYM_CODE)
     - 
     - 
   * - 
     - KeyM_ServiceCertificate(
     - 
     - 
   * - 
     - KeyM_ServiceCertificateTypeService,
     - 
     - 
   * - 
     - P2CONST(uint8,AUTOMATIC,KEYM_APPL_DATA)CertNamePtr,
     - 
     - 
   * - 
     - uint16CertNameLength,
     - 
     - 
   * - 
     - P2CONST(uint8,AUTOMATIC,KEYM_APPL_DATA)RequestData,
     - 
     - 
   * - 
     - uint16RequestDataLength,
     - 
     - 
   * - 
     - P2VAR(uint8,AUTOMATIC,KEYM_APPL_DATA)ResponseData,
     - 
     - 
   * - 
     - uint16ResponseDataLength
     - 
     - 
   * - 
     - )
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x09
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 异步 (Asynchronous)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 否 (No)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - Service
     - 值域： (Domain:)
     - 无
   * - 
     - CertNamePtr
     - 
     - 无
   * - 
     - CertNameLength
     - 
     - 无
   * - 
     - RequestData
     - 
     - 无
   * - 
     - RequestDataLength
     - 
     - 无
   * - 
     - ResponseDataLength
     - 
     - 无
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - ResponseData
     - 
     - 
   * - 返回值： (Return Value:)
     - Std_ReturnType
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 根据参数对秘钥进行操作 (Operate on the key based on parameters)
     - 
     - 




KeyM_SetCertificate函数定义 (The KeyM_SetCertificate function defines)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - KeyM_SetCertificate
     - 
     - 
   * - 函数原型： (Function prototype:)
     - staticFUNC(Std_ReturnType,KEYM_CODE)
     - 
     - 
   * - 
     - KeyM_SetCertificate
     - 
     - 
   * - 
     - (
     - 
     - 
   * - 
     - KeyM_CertificateIdTypeCertId,
     - 
     - 
   * - 
     - P2CONST(KeyM_CertDataType,AUTOMATIC,KEYM_APPL_DATA)CertificateDataPtr
     - 
     - 
   * - 
     - )
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x0a
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 否 (No)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - CertId
     - 值域： (Domain:)
     - 无
   * - 
     - CertificateDataPtr
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
     - Std_ReturnType
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 将证书数据提供给KeyM以临时存储证书 (Provide the certificate data to KeyM for temporary storage of the certificate.)
     - 
     - 




KeyM_GetCertificate函数定义 (The KeyM_GetCertificate function definition)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - KeyM_GetCertificate
     - 
     - 
   * - 函数原型： (Function prototype:)
     - staticFUNC(Std_ReturnType,KEYM_CODE)
     - 
     - 
   * - 
     - KeyM_GetCertificate
     - 
     - 
   * - 
     - (
     - 
     - 
   * - 
     - KeyM_CertificateIdTypeCertId,
     - 
     - 
   * - 
     - P2VAR(KeyM_CertDataType,AUTOMATIC,KEYM_APPL_DATA)CertificateDataPtr
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
     - 否 (No)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - CertId
     - 值域： (Domain:)
     - 无
   * - 输入输出参数： (Input Output Parameters:)
     - CertificateDataPtr
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无
     - 
     - 
   * - 返回值： (Return Value:)
     - Std_ReturnType
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 提供证书内容 (Provide certificate content)
     - 
     - 




KeyM_VerifyCertificates函数定义 (KeyM_VerifyCertificates function definition)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - KeyM_VerifyCertificates
     - 
     - 
   * - 函数原型： (Function prototype:)
     - staticFUNC(Std_ReturnType,KEYM_CODE)
     - 
     - 
   * - 
     - KeyM_VerifyCertificates
     - 
     - 
   * - 
     - (
     - 
     - 
   * - 
     - KeyM_CertificateIdTypeCertId,
     - 
     - 
   * - 
     - KeyM_CertificateIdTypeCertUpperId
     - 
     - 
   * - 
     - )
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x0c
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 否 (No)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - CertId
     - 值域： (Domain:)
     - 无
   * - 
     - CertUpperId
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
     - Std_ReturnType
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 相互验证两个证书 (Verify two certificates mutually)
     - 
     - 




KeyM_VerifyCertificate函数定义 (The KeyM_VerifyCertificate function definition)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - KeyM_VerifyCertificate
     - 
     - 
   * - 函数原型： (Function prototype:)
     - staticFUNC(Std_ReturnType,KEYM_CODE)
     - 
     - 
   * - 
     - KeyM_VerifyCertificate
     - 
     - 
   * - 
     - (
     - 
     - 
   * - 
     - KeyM_CertificateIdTypeCertId
     - 
     - 
   * - 
     - )
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x0d
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 否 (No)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - CertId
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
     - Std_ReturnType
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 验证KeyM_Setcertificate()存储的证书 (Validate the certificate stored in KeyM_Setcertificate())
     - 
     - 




KeyM_VerifyCertificateChain函数定义 (The KeyM_VerifyCertificateChain function definition)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - KeyM_VerifyCertificateChain
     - 
     - 
   * - 函数原型： (Function prototype:)
     - staticFUNC(Std_ReturnType,KEYM_CODE)
     - 
     - 
   * - 
     - KeyM_VerifyCertificateChain
     - 
     - 
   * - 
     - (
     - 
     - 
   * - 
     - KeyM_CertificateIdTypeCertId,
     - 
     - 
   * - 
     - P2CONST(KeyM_CertDataType,AUTOMATIC,KEYM_APPL_DATA)certChainData,
     - 
     - 
   * - 
     - uint8NumberOfCertificates
     - 
     - 
   * - 
     - )
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x0e
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 否 (No)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - CertId
     - 值域： (Domain:)
     - 无
   * - 
     - certChainData
     - 
     - 无
   * - 
     - NumberOfCertificates
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
     - Std_ReturnType
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 根据证书列表执行证书验证。并且根证书要么在列表中，要么已经分配给其他证书之一，这是一个先决条件 (Execute certificate validation according to the certificate list. And the root certificate must either be in the list or allocated to one of the other certificates, which is a prerequisite.)
     - 
     - 




KeyM_CertElementGet函数定义 (The KeyM_CertElementGet function definition)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - KeyM_CertElementGet
     - 
     - 
   * - 函数原型： (Function prototype:)
     - staticFUNC(Std_ReturnType,KEYM_CODE)
     - 
     - 
   * - 
     - KeyM_CertElementGet
     - 
     - 
   * - 
     - (
     - 
     - 
   * - 
     - KeyM_CertificateIdTypeCertId,
     - 
     - 
   * - 
     - KeyM_CertElementIdTypeCertElementId,
     - 
     - 
   * - 
     - P2VAR(uint8,AUTOMATIC,KEYM_APPL_DATA)CertElementData,
     - 
     - 
   * - 
     - P2VAR(uint32,AUTOMATIC,KEYM_APPL_DATA)CertElementDataLength
     - 
     - 
   * - 
     - )
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x0f
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 否 (No)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - CertId
     - 值域： (Domain:)
     - 无
   * - 
     - CertElementId
     - 
     - 无
   * - 输入输出参数： (Input Output Parameters:)
     - CertElementDataLength
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - CertElementData
     - 
     - 
   * - 返回值： (Return Value:)
     - Std_ReturnType
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 提供特定证书元素的内容 (Provide content for specific certificate elements.)
     - 
     - 




KeyM_CertElementGetFirst函数定义 (The KeyM_CertElementGetFirst function definition)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - KeyM_CertElementGetFirst
     - 
     - 
   * - 函数原型： (Function prototype:)
     - staticFUNC(Std_ReturnType,KEYM_CODE)
     - 
     - 
   * - 
     - KeyM_CertElementGetFirst
     - 
     - 
   * - 
     - (
     - 
     - 
   * - 
     - KeyM_CertificateIdTypeCertId,
     - 
     - 
   * - 
     - KeyM_CertElementIdTypeCertElementId,
     - 
     - 
   * - 
     - P2VAR(KeyM_CertElementIteratorType,AUTOMATIC,KEYM_APPL_DATA)CertElementIterator,
     - 
     - 
   * - 
     - P2VAR(uint8,AUTOMATIC,KEYM_APPL_DATA)CertElementData,
     - 
     - 
   * - 
     - P2VAR(uint32,AUTOMATIC,KEYM_APPL_DATA)CertElementDataLength
     - 
     - 
   * - 
     - )
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x10
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 否 (No)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - CertId
     - 值域： (Domain:)
     - 无
   * - 
     - CertElementId
     - 
     - 无
   * - 输入输出参数： (Input Output Parameters:)
     - CertElementIterator
     - 
     - 
   * - 
     - CertElementDataLength
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - CertElementData
     - 
     - 
   * - 返回值： (Return Value:)
     - Std_ReturnType
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 用于初始化证书数据元素的交互提取。它总是从配置的证书元素中检索顶部元素，并初始化结构KeyM_CertElementIterator，以便可以使用KeyM_CertElementGetNext()读取来自该元素的连续数据 (For initializing certificate data elements through interactive extraction. It always retrieves the top element from the configured certificate elements and initializes the structure KeyM_CertElementIterator so that consecutive data can be read using KeyM_CertElementGetNext().)
     - 
     - 




KeyM_CertElementGetNext函数定义 (The KeyM_CertElementGetNext function definition)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - KeyM_CertElementGetNext
     - 
     - 
   * - 函数原型： (Function prototype:)
     - staticFUNC(Std_ReturnType,KEYM_CODE)
     - 
     - 
   * - 
     - KeyM_CertElementGetNext
     - 
     - 
   * - 
     - (
     - 
     - 
   * - 
     - P2VAR(KeyM_CertElementIteratorType,AUTOMATIC,KEYM_APPL_DATA)CertElementIterator,
     - 
     - 
   * - 
     - P2VAR(uint8,AUTOMATIC,KEYM_APPL_DATA)CertElementData,
     - 
     - 
   * - 
     - P2VAR(uint32,AUTOMATIC,KEYM_APPL_DATA)CertElementDataLength
     - 
     - 
   * - 
     - )
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x11
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 否 (No)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - 无
     - 值域： (Domain:)
     - 无
   * - 输入输出参数： (Input Output Parameters:)
     - CertElementIterator
     - 
     - 
   * - 
     - CertElementDataLength
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - CertElementData
     - 
     - 
   * - 返回值： (Return Value:)
     - Std_ReturnType
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 在KeyM_CertElementGetFirst被调用后进一步提供来自证书元素的数据 (After KeyM_CertElementGetFirst is called, further data from the certificate element is provided.)
     - 
     - 




KeyM_CertGetStatus函数定义 (The KeyM_CertGetStatus function definition)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - KeyM_CertGetStatus
     - 
     - 
   * - 函数原型： (Function prototype:)
     - staticFUNC(Std_ReturnType,KEYM_CODE)
     - 
     - 
   * - 
     - KeyM_CertGetStatus
     - 
     - 
   * - 
     - (
     - 
     - 
   * - 
     - KeyM_CertificateIdTypeCertId,
     - 
     - 
   * - 
     - P2VAR(KeyM_CertificateStatusType,AUTOMATIC,KEYM_APPL_DATA)Status
     - 
     - 
   * - 
     - )
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x12
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 否 (No)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - CertId
     - 值域： (Domain:)
     - 无
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - Status
     - 
     - 
   * - 返回值： (Return Value:)
     - Std_ReturnType
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 提供证书的状态 (Status of certificate provided)
     - 
     - 




KeyM_MainFunction函数定义 (KeyM_MainFunction function definition)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - KeyM_MainFunction
     - 
     - 
   * - 函数原型： (Function prototype:)
     - voidKeyM_MainFunction(void)
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x19
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 否 (No)
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
     - 根据指定的时间间隔定期调用 (Call at regular intervals as specified.)
     - 
     - 




KeyM_MainBackgroudFunction函数定义 (KeyM_MainBackgroudFunction function definition)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - KeyM_MainBackgroudFunction
     - 
     - 
   * - 函数原型： (Function prototype:)
     - voidKeyM_MainBackgroundFunction(void)
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x1a
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 否 (No)
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
     - 在不需要其他任务操作时，从抢占式操作系统调用函数 (When there are no other task operations required, call functions from a preemptive operating system.)
     - 
     - 




配置 (Configure)
==============================

KeyMGeneral
---------------------------

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/KeyM/image2.png
   :alt: KeyMGeneral容器配置图 (KeyMGeneral Container Configuration Diagram)
   :name: KeyMGeneral容器配置图 (KeyMGeneral Container Configuration Diagram)
   :align: center


.. centered:: **表 KeyMGeneral属性描述 (Table KeyMGeneral Property Description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - KeyMCertificateChainMaxDepth
     - 取值范围 (Range)
     - 1 .. 255
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 证书链中定义的最大证书数 (The maximum number of certificates defined in the certificate chain)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - KeyMCertificateManagerEnabled为TRUE (KeyMCertificateManagerEnabled is TRUE)
     - 
     - 
   * - KeyMCertificateManagerEnabled
     - 取值范围 (Range)
     - True、False
     - 默认取值 (Default value)
     - False
   * - 
     - 参数描述 (Parameter Description)
     - 启用 (TRUE)或禁用 (FALSE)管理证书的部分
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - KeyMCryptoKeyManagerEnabled为TRUE (KeyMCryptoKeyManagerEnabled is TRUE)
     - 
     - 
   * - KeyMCryptoKeyHandlerPrepareEnabled
     - 取值范围 (Range)
     - True、False
     - 默认取值 (Default value)
     - False
   * - 
     - 参数描述 (Parameter Description)
     - 启用 (TRUE)或禁用 (FALSE)键处理程序准备函数调用。如果设置为TRUE，则应提供相应的处理程序函数
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - KeyMCryptoKeyHandlerServiceCertificateEnabled
     - 取值范围 (Range)
     - True、False
     - 默认取值 (Default value)
     - False
   * - 
     - 参数描述 (Parameter Description)
     - 启用 (TRUE)或禁用 (FALSE)密钥处理程序服务函数调用。如果设置为TRUE，则应提供证书子模块函数KeyM_KH_ServiceCertificate
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - KeyMCryptoKeyHandlerStartFinalizeEnabled
     - 取值范围 (Range)
     - True、False
     - 默认取值 (Default value)
     - False
   * - 
     - 参数描述 (Parameter Description)
     - 启用 (TRUE)或禁用 (FALSE)键处理程序启动和完成函数调用。如果设置为TRUR，则应提供密钥处理函数KeyM_KH_Start()和KeyM_KH_Finalize()
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - KeyMCryptoKeyHandlerUpdateEnabled
     - 取值范围 (Range)
     - True、False
     - 默认取值 (Default value)
     - False
   * - 
     - 参数描述 (Parameter Description)
     - 启用 (TRUE)或禁用 (FALSE)对密钥处理程序更新函数KeyM_KH_Update()的调用。如果设置为TRUE，则应提供相应的处理函数
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - KeyMCryptoKeyHandlerVerifyEnabled
     - 取值范围 (Range)
     - True、False
     - 默认取值 (Default value)
     - False
   * - 
     - 参数描述 (Parameter Description)
     - 启用 (TRUE)或禁用 (FALSE)对密钥处理程序验证函数KeyM_KH_Verify()的调用。如果设置为TRUE，则应提供相应的处理函数
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - KeyMCryptoKeyManagerEnabled
     - 取值范围 (Range)
     - True、False
     - 默认取值 (Default value)
     - False
   * - 
     - 参数描述 (Parameter Description)
     - 启用 (TRUE)或禁用 (FALSE)管理加密密钥操作的部分
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - KeyMCryptoKeyManagerEnabled为TRUE (KeyMCryptoKeyManagerEnabled is TRUE)
     - 
     - 
   * - KeyMCryptoKeyPrepareFunctionEnabled
     - 取值范围 (Range)
     - True、False
     - 默认取值 (Default value)
     - False
   * - 
     - 参数描述 (Parameter Description)
     - 启用 (TRUE)或禁用 (FALSE)密钥管理器的准备功能。如果设置为TRUE，则必须相应地调用KeyM_Prepare()函数
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - KeyMCryptoKeyManagerEnabled为TRUE (KeyMCryptoKeyManagerEnabled is TRUE)
     - 
     - 
   * - KeyMCryptoKeyStartFinalizeFunctionEnabled
     - 取值范围 (Range)
     - True、False
     - 默认取值 (Default value)
     - False
   * - 
     - 参数描述 (Parameter Description)
     - 启用 (TRUE)或禁用 (FALSE)密钥管理器的启动和完成功能。如果设置为TRUE，则必须调用KeyM_Start()和KeyM_Finalize()函数
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - KeyMCryptoKeyManagerEnabled为TRUE (KeyMCryptoKeyManagerEnabled is TRUE)
     - 
     - 
   * - KeyMCryptoKeyVerifyAsyncMode
     - 取值范围 (Range)
     - True、False
     - 默认取值 (Default value)
     - False
   * - 
     - 参数描述 (Parameter Description)
     - 此参数定义函数KeyM_Verify()是在同步模式还是异步模式下运行 (This parameter defines whether the function KeyM_Verify() runs in synchronous mode or asynchronous mode.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - KeyMCryptoKeyManagerEnabled为TRUE (KeyMCryptoKeyManagerEnabled is TRUE)
     - 
     - 
   * - KeyMCryptoKeyVerifyFunctionEnabled
     - 取值范围 (Range)
     - True、False
     - 默认取值 (Default value)
     - False
   * - 
     - 参数描述 (Parameter Description)
     - 启用 (TRUE)或禁用 (FALSE)密钥管理器的验证功能。如果设置为TRUE，则可以调用KeyM_Verify()函数
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - KeyMCryptoKeyManagerEnabled为TRUE (KeyMCryptoKeyManagerEnabled is TRUE)
     - 
     - 
   * - KeyMDevErrorDetect
     - 取值范围 (Range)
     - True、False
     - 默认取值 (Default value)
     - False
   * - 
     - 参数描述 (Parameter Description)
     - 开发错误检测使能 (Enable Error Detection in Development)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - KeyMKeyCertNameMaxLength
     - 取值范围 (Range)
     - 1 .. 255
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 用于服务接口的证书或密钥名称的最大长度（以字节为单位） (Maximum length of certificate or key name for service interfaces (in bytes))
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - KeyMCertificateManagerEnabled为TRUE (KeyMCertificateManagerEnabled is TRUE)
     - 
     - 
   * - KeyMMainFunctionPeriod
     - 取值范围 (Range)
     - 0 .. INF
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 调度函数的周期 (The cycle of scheduling functions)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - KeyMServiceCertificateFunctionEnabled
     - 取值范围 (Range)
     - True、False
     - 默认取值 (Default value)
     - False
   * - 
     - 参数描述 (Parameter Description)
     - 启用 (TRUE)或禁用 (FALSE)密钥管理器的证书服务功能。如果设置为TRUE，则必须相应地调用KeyM_ServiceCertificate()函数
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - KeyMCertificateManagerEnabled为TRUE (KeyMCertificateManagerEnabled is TRUE)
     - 
     - 
   * - KeyMEnableSecurityEventReporting
     - 取值范围 (Range)
     - True、False
     - 默认取值 (Default value)
     - False
   * - 
     - 参数描述 (Parameter Description)
     - 启用或禁用安全事件报告到IdsM (Enable or Disable Security Event Reporting to IdsM)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 




KeyMCertificate
-------------------------------

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/KeyM/image3.png
   :alt: KeyMCertificate容器配置图 (KeyMCertificate Container Configuration Diagram)
   :name: KeyMCertificate容器配置图 (KeyMCertificate Container Configuration Diagram)
   :align: center


.. centered:: **表 KeyMCertificate属性描述 (Table KeyMCertificate Property Description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - KeyMCertAlgorithmType
     - 取值范围 (Range)
     - Enumeration
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 指定提供证书的格式 (Specify the format of the certificate provided.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - KeyMCertFormatType
     - 取值范围 (Range)
     - Enumeration
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 指定提供证书的格式 (Specify the format of the certificate provided.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - KeyMCertificateId
     - 取值范围 (Range)
     - 0 .. 65535
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 证书的标识符。配置的标识符集应该是连续的和无间隙的 (Identifier of the certificate. The set of identifiers configured should be continuous and gapless.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - KeyMCertificateMaxLength
     - 取值范围 (Range)
     - 1 .. 65535
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 指定证书的最大长度（以字节为单位） (Specify the maximum length of the certificate (in bytes))
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - KeyMCertificateName
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 提供证书的唯一名称以供识别。临时证书将以此唯一名称引用证书 (Provide the unique name for identification of the certificate. The temporary certificate will reference the certificate by this unique name.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - KeyMCertificateStorage
     - 取值范围 (Range)
     - Enumeration
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 指定证书的存储位置 (The storage location of the specified certificate)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - KeyMCertificateVerifyCallbackNotificationFunc
     - 取值范围 (Range)
     - Function
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 此参数提供回调<KeyM_CertificateVerifyCallbackNotification>的函数名称。它指示证书验证操作是否已完成并提供其状态 (This parameter provides the function name for the callback <KeyM_CertificateVerifyCallbackNotification>. It indicates whether the certificate verification operation has been completed and provides its status.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - KeyMServiceCertificateCallbackNotificationFunc
     - 取值范围 (Range)
     - Function
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 此参数为服务证书回调<KeyM_ServiceCertificateCallbackNotification>提供函数名称。它指示证书服务操作是否已完成并提供其状态 (This parameter provides the function name for service certificate callback <KeyM_ServiceCertificateCallbackNotification>. It indicates whether the certificate service operation has been completed and provides its status.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - KeyMCertCertificateElementRuleRef
     - 取值范围 (Range)
     - Reference
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 参考应在认证验证步骤中验证的证书元素规则 (Rules for certificate elements to be verified in the authentication validation steps)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - KeyMCertificateElementRule
     - 
     - 
   * - KeyMCertCsmSignatureGenerateJobRef
     - 取值范围 (Range)
     - Reference
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 引用用于生成签名的CSM Job (Quote the CSM Job used for generating the signature)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - CsmJob
     - 
     - 
   * - KeyMCertCsmSignatureVerifyJobRef
     - 取值范围 (Range)
     - reference
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 引用用于验证签名的CSM Job (Reference CSM Job used for signature verification)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - CsmJob
     - 
     - 
   * - KeyMCertCsmSignatureVerifyKeyRef
     - 取值范围 (Range)
     - reference
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 对与 CSM签名验证Job关联的CSM密钥的引用。如果证书存储在CSM中并且公钥自动引用签名验证Job，则可以省略此参数，例如带虚拟钥匙。如果存在此配置选项，则证书的公钥将被放入此密钥及其元素（编号#1）中以存储密钥。 (Reference to the CSM key associated with the CSM signature verification Job. This parameter can be omitted if the certificate is stored in CSM and the public key is automatically referenced by the signature verification Job, for example, with virtual keys. If this configuration option exists, the certificate's public key will be placed into this key and its elements (numbered #1) to store the key.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - KeyMCertificateCsmKeyTargetRef
     - 取值范围 (Range)
     - reference
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 定义对应生成的关联CSM 密钥的引用 (Reference for the CSM key corresponding to the generated association)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - CsmKey
     - 
     - 
   * - KeyMCertificateNvmBlockRef
     - 取值范围 (Range)
     - Reference
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 定义对将存储证书的NvMblock的引用。 (Define a reference to the NvMblock that will store the certificate.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - KeyMCertPrivateKeyStorageCryptoKeyRef
     - 取值范围 (Range)
     - Reference
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 定义证书私钥的存储位置 (Define the storage location for certificate private keys)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - KeyMCryptoKey
     - 
     - 
   * - KeyMCertTimebaseRef
     - 取值范围 (Range)
     - Reference
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 用于验证有效期的StbM 时基的引用 (Reference for StbM timing base used for validity verification)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - StbMSynchronizedTimeBase
     - 
     - 
   * - KeyMCertUpperHierarchicalCertRef
     - 取值范围 (Range)
     - Reference
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - PKI层次结构中下一个更高的证书的标识符。根证书的引用指向自身 (Identifier for the next higher certificate in the PKI hierarchy. The reference to the root certificate points to itself.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - KeyMCertificate
     - 
     - 




KeyMCertificateElement 
---------------------------------------

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/KeyM/image4.png
   :alt: KeyMCertificateElement容器配置图 (KeyMCertificateElement Container Configuration Diagram)
   :name: KeyMCertificateElement容器配置图 (KeyMCertificateElement Container Configuration Diagram)
   :align: center


.. centered:: **表 KeyMCertificateElement属性描述 (Table KeyMCertificateElement Property Description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - KeyMCertificateElementHasIteration
     - 取值范围 (Range)
     - True、False
     - 默认取值 (Default value)
     - False
   * - 
     - 参数描述 (Parameter Description)
     - 定义证书元素是否可以出现多次。如果是这样，迭代器可用于检索此证书元素的各个数据值。 (Define whether a certificate element can appear multiple times. If so, an iterator can be used to retrieve each data value of this certificate element.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - KeyMCertificateElementId
     - 取值范围 (Range)
     - 0 .. 65535
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 证书元素的标识符 (Identifier of certificate elements)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - KeyMCertificateElementMaxLength
     - 取值范围 (Range)
     - 1 .. 65535
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 证书的标识符。配置的标识符集应该是连续的和无间隙的 (Identifier of the certificate. The set of identifiers configured should be continuous and gapless.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - KeyMCertificateElementIterationDepth
     - 取值范围 (Range)
     - 1 .. 65535
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 证书元素迭代的个数 (Number of iterations for certificate element iteration)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - KeyMCertificateElementHasIteration被勾选后可用 (KeyMCertificateElementHasIteration is enabled after being checked)
     - 
     - 
   * - KeyMCertificateElementObjectId
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 这是用于标识其元素结构中的证书元素的对象标识符(OID)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - KeyMCertificateElementObjectType
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 证书元素以ASN.1格式存储。在此项中，可以指定ASN.1 TLV的类型。这可用于仅标识此类证书元素。如果类型不同，则搜索中不包括该元素。如果未指定KeyMCertificateElementObjectType，则使用任何ASN.1编码数据类型来读取值。 (Certificate elements are stored in ASN.1 format. In this item, the type of ASN.1 TLV can be specified. This is used to仅标识此类证书元素 identify such certificate elements solely. If the type is different, the element will not be included in the search. If KeyMCertificateElementObjectType is not specified, any ASN.1 encoded data type will be used to read the value.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - KeyMCertificateElementOfStructure
     - 取值范围 (Range)
     - Enumeration
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 这定义了证书元素位于哪个结构中 (This defines which structure the certificate element resides in.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 




KeyMCertificateElementRule
------------------------------------------

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/KeyM/image5.png
   :alt: KeyMCertificateElementRule容器配置图 (KeyMCertificateElementRule Container Configuration Diagram)
   :name: KeyMCertificateElementRule容器配置图 (KeyMCertificateElementRule Container Configuration Diagram)
   :align: center


.. centered:: **表 KeyMCertificateElementRule属性描述 (Table KeyMCertificateElementRule Property Description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - KeyMLogicalOperator
     - 取值范围 (Range)
     - Enumeration
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 此参数指定要在逻辑表达式中使用的逻辑运算符。如果表达式仅由单个条件组成，则不应使用此参数 (This parameter specifies the logical operator to be used in the logical expression. If the expression consists of only a single condition, this parameter should not be used.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - KeyMArgumentRef
     - 取值范围 (Range)
     - reference
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 这是对条件或另一个用作子表达式的规则的选择引用 (This is a reference to either a condition or another rule used as a sub-expression.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - KeyMCertificateElementCondition,
     - 
     - 
   * - 
     - 
     - KeyMCertificateElementRule
     - 
     - 




KeyMCertificateElementCondition
-----------------------------------------------

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/KeyM/image6.png
   :alt: KeyMCertificateElementCondition容器配置图 (KeyMCertificateElementCondition Container Configuration Diagram)
   :name: KeyMCertificateElementCondition容器配置图 (KeyMCertificateElementCondition Container Configuration Diagram)
   :align: center


.. centered:: **表 KeyMCertificateElementCondition属性描述 (KeyMCertificateElementCondition property description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - KeyMCertElementConditionType
     - 取值范围 (Range)
     - Enumeration
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 此参数指定为评估模式条件而进行的比较类型 (This parameter specifies the comparison type for evaluation mode conditions.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - KeyMCertificateElementRef
     - 取值范围 (Range)
     - reference
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 对用于条件的证书元素的引用 (References to certificate elements used for conditions.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - KeyMCertificateElement
     - 
     - 




KeyMCertificateElementConditionArrayElement
-----------------------------------------------------------

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/KeyM/image7.png
   :alt: KeyMCertificateElementConditionArrayElement容器配置图 (KeyMCertificateElementConditionArrayElement Container Configuration Diagram)
   :name: KeyMCertificateElementConditionArrayElement容器配置图 (KeyMCertificateElementConditionArrayElement Container Configuration Diagram)
   :align: center

.. centered:: **表 KeyMCertificateElementConditionArrayElement属性描述 (Properties Description of KeyMCertificateElementConditionArrayElement)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - KeyMCertificateElementConditionArrayElementIndex
     - 取值范围 (Range)
     - 0 .. 65535
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 比较值数组元素的索引 (Compare the indices of array elements)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - KeyMCertificateElementConditionArrayElementValue
     - 取值范围 (Range)
     - 0 ..
     - 默认取值 (Default value)
     - 无
   * - 
     - 
     - 744073709551615
     - 
     - 
   * - 
     - 参数描述 (Parameter Description)
     - 数组元素比较值的值 (Compare values of array elements)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 




KeyMCertificateElementConditionArray
----------------------------------------------------

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/KeyM/image8.png
   :alt: KeyMCertificateElementConditionArray容器配置图 (KeyMCertificateElementConditionArray Container Configuration Diagram)
   :name: KeyMCertificateElementConditionArray容器配置图 (KeyMCertificateElementConditionArray Container Configuration Diagram)
   :align: center


.. centered:: **表 KeyMCertificateElementConditionArray属性描述 (KeyMCertificateElementConditionArray property description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - KeyMCertificateElementRef
     - 取值范围 (Range)
     - Reference
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 对另一个证书元素的引用 (Reference to another certificate element)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - KeyMCertificateElement
     - 
     - 




KeyMCertificateElementConditionPrimitive
--------------------------------------------------------

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/KeyM/image9.png
   :alt: KeyMCertificateElementConditionPrimitive容器配置图 (KeyMCertificateElementConditionPrimitive Container Configuration Diagram)
   :name: KeyMCertificateElementConditionPrimitive容器配置图 (KeyMCertificateElementConditionPrimitive Container Configuration Diagram)
   :align: center


.. centered:: **表 KeyMCertificateElementConditionPrimitive属性描述 (KeyMCertificateElementConditionPrimitive property description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - KeyMCertificateElementConditionPrimitiveValue
     - 取值范围 (Range)
     - 0 ..
     - 默认取值 (Default value)
     - 无
   * - 
     - 
     - 744073709551615
     - 
     - 
   * - 
     - 参数描述 (Parameter Description)
     - 原始比较值 (Original comparative value)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 




KeyMCertificateElementConditionSenderReceiver
-------------------------------------------------------------

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/KeyM/image10.png
   :alt: KeyMCertificateElementConditionSenderReceiver容器配置图 (KeyMCertificateElementConditionSenderReceiver Container Configuration Diagram)
   :name: KeyMCertificateElementConditionSenderReceiver容器配置图 (KeyMCertificateElementConditionSenderReceiver Container Configuration Diagram)
   :align: center

.. centered:: **表 KeyMCertificateElementConditionSenderReceiver属性描述 (KeyMCertificateElementConditionSenderReceiver Attribute Description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - KeyMCertificateElementConditionSenderReceiver
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 该参数用于S/R端口的动态比较 (This parameter is used for dynamic comparison of S/R ports.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 




KeyMCryptoKey
-----------------------------

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/KeyM/image11.png
   :alt: KeyMCryptoKey容器配置图 (KeyMCryptoKey Container Configuration Diagram)
   :name: KeyMCryptoKey容器配置图 (KeyMCryptoKey Container Configuration Diagram)
   :align: center


.. centered:: **表 KeyMCryptoKey属性描述 (Table KeyMCryptoKey Property Description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - KeyMCryptoCsmVerifyJobType
     - 取值范围 (Range)
     - Enumeration
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 指定使用哪种类型的密钥验证操作函数 (Specify which type of key verification function to use.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - KeyMCryptoKeyCryptoProps
     - 取值范围 (Range)
     - String
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 如果设置，它将为KeyM用来识别密钥的加密密钥提供额外的提示。典型的方法是将值设置为放置密钥的SHE-Slot ID。如果存在，KeyM将获取信息并通过其插槽ID 识别密钥。时隙信息将从M1M2M3数据的相应字段中提取 (If configured, it will provide additional hints for KeyM to identify the encryption key used for keys. A typical approach is to set the value to the SHE-Slot ID where the key is placed. If available, KeyM will retrieve the information and identify the key through its slot ID. Slot information will be extracted from the corresponding fields of M1M2M3 data.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - KeyMCryptoKeyGenerationInfo
     - 取值范围 (Range)
     - String
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 该数据可能包含用于密钥派生的静态数据。如果一个key被配置为从另一个key派生，并且设置了这个配置项，那么数据将被添加为salt。 (This data may contain static information used for key derivation. If a key is configured to derive from another key and this configuration item is set, the data will be added as salt.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - KeyMCryptoKeyGenerationType
     - 取值范围 (Range)
     - Enumeration
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 指定如何生成CryptoKey。如果它是从另一个密钥派生的，或者只是与KeyElementSet一起存储。 (Specify how the CryptoKey is generated. If it is derived from another key, or stored together with KeyElementSet.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - KeyMCryptoKeyId
     - 取值范围 (Range)
     - 0 .. 65535
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 加密密钥的标识符。配置的标识符集应连续且无间隙 (Identifier for encryption key. The set of configured identifiers should be continuous and gapless.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - KeyMCryptoKeyMaxLength
     - 取值范围 (Range)
     - 1 .. 4294967295
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - CryptoKey的最大字节数 (The maximum number of bytes for CryptoKey)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - KeyMCryptoKeyName
     - 取值范围 (Range)
     - String
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 提供密钥的唯一名称以供识别。密钥主将通过这个唯一的密钥名称来引用密钥 (Provide a unique name for the key for identification. The key master will reference the key using this unique key name.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - KeyMCryptoKeyStorage
     - 取值范围 (Range)
     - Enumeration
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 指定证书的存储位置 (The storage location of the specified certificate)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - KeyMCryptoKeyCsmKeySourceDeriveRef
     - 取值范围 (Range)
     - reference
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 定义对用作此密钥的密钥派生源的关联CSM 密钥的引用 (Define a reference to the associated CSM key used as the key derivation source.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - CsmKey
     - 
     - 
   * - KeyMCryptoKeyCsmKeyTargetRef
     - 取值范围 (Range)
     - reference
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 定义对应生成的关联CSM 密钥的引用 (Reference for the CSM key corresponding to the generated association)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - CsmKey
     - 
     - 
   * - KeyMCryptoKeyCsmVerifyJobRef
     - 取值范围 (Range)
     - reference
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 定义密钥验证功能可用于验证某个密钥的加密作业 (Define key validation functionality can be used to verify an encrypted job's key.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - CsmJob
     - 
     - 
   * - KeyMCryptoKeyNvmBlockRef
     - 取值范围 (Range)
     - Reference
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 定义对将存储密钥的NvM 块的引用 (Define a reference to the NvM block that will store the keys)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - KeyMNvmBlock
     - 
     - 




KeyMNvmBlock
----------------------------

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/KeyM/image12.png
   :alt: KeyMNvmBlock容器配置图 (KeyMNvmBlock Container Configuration Diagram)
   :name: KeyMNvmBlock容器配置图 (KeyMNvmBlock Container Configuration Diagram)
   :align: center


.. centered:: **表 KeyMNvmBlock属性描述 (KeyMNvmBlock Property Description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - KeyMNvmBlockWriteDelayed
     - 取值范围 (Range)
     - 0 .. 65535
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 这是更新后将密钥写入NVM的延迟时间（以毫秒为单位）。值 0表示密钥在更新后立即写入。如果多个密钥被更新分配给同一个容器，则应使用第一个延迟时间到期。在此期间已更新的所有密钥都应更新并停止其延迟计时器 (This is the delay time (in milliseconds) for writing the key to NVM after an update. A value of 0 indicates that the key is written immediately upon updating. If multiple keys are updated and assigned to the same container, the first delayed time expiration should be used. During this period, all updated keys should be updated and their delay timers stopped.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - KeyMNvmBlockDescriptorRef
     - 取值范围 (Range)
     - reference
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 引用到Nvm的Block (Reference to Nvm's Block)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - NvMBlockDescriptor
     - 
     - 
