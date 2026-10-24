CryIf
#################################

:strong:`缩写词注解 (Abbreviation Notes):`

.. list-table::
   :widths: 34 33 33
   :header-rows: 1

   * - 缩写词 (Abbreviation)
     - 解释/描述 (Explanation/Description)
     - 中文解释 (Chinese explanation)
   * - HSM
     - Hardware SecurityModule
     - 硬件安全模块 (Hardware Security Module)
   * - SHE
     - Security HardwareExtension
     - 安全硬件扩展 (Security Hardware Extension)
   * - SW
     - Software
     - 软件加密算法 (Software encryption algorithms)
   * - HW
     - Hardware
     - 硬件加密算法 (Hardware encryption algorithms)
   * - CDD
     - Complex Device Driver
     - 复杂驱动 (Complex Drive)
   * - CSM
     - Crypto Service Manager
     - AUTOSAR中的加密服务管理 模块 (Encryption Service Management module in AUTOSAR)
   * - CRYIF
     - Crypto Interface
     - AUTOSAR中的加密接口模块 (The cryptographic interface module in AUTOSAR)




简介 (Introduction)
=================================

CryIf 模块位于底层密码解决方案(Crypto Driver 和基于 sw 的 CDD)和上层服务层(CSM)之间。它表示到上层服务层的密码驱动程序服务的接口。CryIf 模块 提供了一个独特的接口来管理不同的密码 HW 和 SW 解决方案，如HSM、SHE 或基于 SW 的 CDD。因此，基于 Crypto 接口维护的映射方案，Crypto 服务管理模块可以利用多种底层的内部和外部加密 HW 以及 SW 解决方案。
The CryIf module resides between the low-level cryptography solutions (Crypto Driver and SW-based CDD) and the upper service layer (CSM). It represents the interface for cryptography driver services toward the upper service layer.The CryIf module provides a unified interface to manage various cryptographic hardware and software solutions such as HSM, SHE, or software-based CDD. Therefore, based on the mapping scheme maintained by the Crypto Interface, the Crypto Service Manager module can utilize multiple underlying internal and external cryptographic hardware as well as software solutions.

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/CryIf/image1.png
   :alt: AUTOSAR 加密栈 (AUTOSAR Encryption Stack)
   :name: AUTOSAR 加密栈 (AUTOSAR Encryption Stack)
   :align: center


CryIf 模块的主要功能为：

The main functions of the CryIf module are:

1、接收 CSM 传输的数据并传输给 Crypto Driver。 2、接收 Crypto Driver返回的信息并返回给 CSM。

Receive data transmitted by CSM and transmit it to the Crypto Driver. 2、Receive information returned by the Crypto Driver and return it to CSM.

参考资料 (References)
---------------------------------

[1] AUTOSAR_SWS_CryptoInterface.pdf，R19-11

功能描述 (Function Description)
===========================================

基本功能 (Basic Functions)
--------------------------------------

CryIf 位于 CSM 和 Crypto Driver 之间，是访问所有上层(BSW)密码操作的唯一接口。密码接口也是密码驱动程序的唯一用户，并提供了一个独特的接口来管理不同的密码硬件和软件解决方案。抽象层封装了不同的硬件和软件访问机制，因此加密接口的实现独立于底层的加密驱动程序，可以在硬件或软件中实现。它还保证了对加密服务的并发访问，使同时处理多个加密任务成为可能。

CryIf is located between CSM and Crypto Driver, serving as the unique interface for all upper-layer (BSW) cryptographic operations and the only user of the crypto drivers, providing a unified interface to manage diverse cryptographic hardware and software solutions; this abstraction layer encapsulates different hardware and software access mechanisms, making the Crypto Interface implementation independent of underlying crypto drivers and realizable in hardware or software, while also guaranteeing concurrent access to cryptographic services to enable simultaneous processing of multiple cryptographic tasks.

除此之外，CryIf 支持多驱动，当需要支持多驱动时，打开CryIfMulDriverSupport 开关，并填写不同驱动接口的前缀，即可根据接口名使 用不同的驱动。

Besides, CryIf supports multiple drivers. When needing to support multiple drivers, turn on the CryIfMulDriverSupport switch and fill in the prefixes of different driver interfaces. This allows for using different drivers based on interface names.

源文件描述 (Source File Description)
===============================================

.. centered:: **表 CryIf 文件描述 (Table CryIf File Description)**

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 文件 (Files)
     - 说明 (Description)
   * - CryIf.c
     - CryIf 模块源文件，包含了 API 函数的实现。 (CryIf module source file, contains the implementation of API functions.)
   * - CryIf.h
     - CryIf 模块头文件，包含了 API函数的扩展声明并定义了配置的 (CryIf module header file, contains extended declarations of API functions and defines the configuration,)
   * - 
     - 数据结构。 (Data structures.)
   * - CryIf_Cfg.h
     - 定义 CryIf 模块预编译时用到的配置参数。 (Define configuration parameters used in pre-compilation of the CryIf module.)
   * - CryIf_cfg.c
     - CryIf 模块配置生成文件。 (Module Configuration Generation File CryIf)


.. figure:: ../../_static/参考手册(Module_Reference_Manual)/CryIf/image2.png
   :alt: CryIf 文件交互关系图 (CryIf File Interactions Diagram)
   :name: CryIf 文件交互关系图 (CryIf File Interactions Diagram)
   :align: center


API 接口 (API Interfaces)
=======================================

类型定义 (Type Definitions)
---------------------------------------

CryIf_ConfigType 类型定义 (CryIf_ConfigType Type Definition)
========================================================================

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 名称 (Name)
     - CryIf_ConfigType
   * - 类型 (Type)
     - Structure
   * - 范围 (Range)
     - 无
   * - 描述 (Description)
     - CryIf 模块配置数据结构 (CryIf Module Configuration Data Structure)




输入函数描述 (Input Function Description)
---------------------------------------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 输入模块 (Input Module)
     - API
   * - Det
     - Det_ReportError
   * - CSM
     - Csm_CallbackNotification
   * - Crypto   Driver
     - Crypto\_<vi>_<ai>_ProcessJob()Crypto\_<vi>_<ai>_CancelJob()Crypto\_<vi>_<ai>_KeyElementSet()Crypto\_<vi>_<ai>_KeySetValid()Crypto\_<vi>_<ai>_KeyElementGet()Crypto\_<vi>_<ai>_KeyElementCopy()Crypto\_<vi>_<ai>_KeyElementCopyPartial()Crypto\_<vi>_<ai>_KeyCopy()Crypto\_<vi>_<ai>_RandomSeed()Crypto\_<vi>_<ai>_KeyGenerate()Crypto\_<vi>_<ai>_KeyDerive() Crypto\_<vi>_<ai>_KeyExchangeCalcPubVal()Crypto\_<vi>_<ai>_KeyExchangeCalcSecret()Crypto\_<vi>_<ai>_CertificateParse()Crypto\_<vi>_<ai>_CertificateVerify()多驱动时<vi>_<ai>_与驱动对应，单驱动时无<vi>_<ai> (Crypto\_\<vi\>\_\<ai\>\_ProcessJob()Crypto\_\<vi\>\_\<ai\>\_CancelJob()Crypto\_\<vi\>\_\<ai\>\_KeyElementSet()Crypto\_\<vi\>\_\<ai\>\_KeySetValid()Crypto\_\<vi\>\_\<ai\>\_KeyElementGet()Crypto\_\<vi\>\_\<ai\>\_KeyElementCopy()Crypto\_\<vi\>\_\<ai\>\_KeyElementCopyPartial()Crypto\_\<vi\>\_\<ai\>\_KeyCopy()Crypto\_\<vi\>\_\<ai\>\_RandomSeed()Crypto\_\<vi\>\_\<ai\>\_KeyGenerate()Crypto\_\<vi\>\_\<ai\>\_KeyDerive() Crypto\_\<vi\>\_\<ai\>\_KeyExchangeCalcPubVal()Crypto\_\<vi\>\_\<ai\>\_KeyExchangeCalcSecret()Crypto\_\<vi\>\_\<ai\>\_CertificateParse()Crypto\_\<vi\>\_\<ai\>\_CertificateVerify() Multiple drivers \<vi\>\<ai\> correspond to the drivers, single driver mode has no \<vi\>\<ai\>)


Crypto\_<vi>\_<ai>_CertificateParse()Crypto\_<vi>\_<ai>_CertificateVerify()

多驱动时<vi>\_<ai>_与驱动对应，单驱动时无<vi>\_<ai>\_

Multiple drives:<vi>_<ai> Corresponds to each drive, single drive: no <vi>_<ai>_

静态接口函数定义 (Static Interface Function Definitions)
----------------------------------------------------------------

CryIf_Init
==========================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - CryIf_Init
     - 
     - 
   * - 函数原型： (Function prototype:)
     - FUNC(void,CRYIF_CODE)
     - 
     - 
   * - 
     - CryIf_Init(
     - 
     - 
   * - 
     - P2CONST(CryIf_ConfigType,AUTOMATIC,
     - 
     - 
   * - 
     - CRYIF_APPL_DATA)
     - 
     - 
   * - 
     - configPtr
     - 
     - 
   * - 
     - )
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x00
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
     - configPtr
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
     - 初始化CRYIF模块 (Initialize CRYIF module)
     - 
     - 




CryIf_GetVersionInfo
====================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - CryIf_GetVersionInfo
     - 
     - 
   * - 函数原型： (Function prototype:)
     - FUNC(void, CRYIF_CODE)CryIf_GetVersionInfo(P2VAR(Std\_VersionInfoType,AUTOMATIC,CRYIF\_APPL\_DATA)versioninfo)
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
     - 是 (Is)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - versioninfo
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
     - 获取版本信息 (Get Version Information)
     - 
     - 




CryIf_ProcessJob
================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - CryIf_ProcessJob
     - 
     - 
   * - 
     - FUNC(Std_ReturnType, CRYIF_CODE) CryIf_ProcessJob(
     - 
     - 
   * - 
     - uint32   channelId,
     - 
     -
   * - 
     - P2VAR(Crypto_JobType,   AUTOMATIC, CRYIF_APPL_DATA)job
     - 
     - 
   * - 函数原型： (Function prototype:)
     - 
     - 
     - 
   * - 
     - )
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x03
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 取决于配置 (Depends on configuration)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 是 (Is)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - channelId
     - 值域： (Domain:)
     - CRYIF_CHANNELS_MAX_CONFIGURED
   * - 输入输出参数： (Input Output Parameters:)
     - job
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无
     - 
     - 
   * - 返回值： (Return Value:)
     - E_OK：请求成功 (E_OK: Request succeeded)
     - 
     -
   * - 
     - E_NOT_OK：请求失败 (E_NOT_OK: Request failed)
     - 
     -
   * - 
     - CRYPTO_E_BUSY：请求失败，Crypro   驱动对象忙 CRYPTO_E_KEY_NOT_VALID：请求失败，密钥无效 CRYPTO_E_KEY_SIZE_MISMATCH：请求失败，一个密钥元素的大 小错误，请求失败，队列已满 CRYPTO_E_KEY_READ_FAIL：服务请求失败，因为不允许提取 key 元素 CRYPTO_E_KEY_WRITE_FAIL：服务请求失败，因为写入访问失败 CRYPTO_E_KEY_NOT_AVAILABLE：服务请求失败，因为密钥不可 用 (CRYPTO_E_BUSY: Request failed, Crypto driver object busy CRYPTO_E_KEY_NOT_VALID: Request failed, Key invalid CRYPTO_E_KEY_SIZE_MISMATCH: Request failed, Size error of a key element Request failed, Queue full CRYPTO_E_KEY_READ_FAIL: Service request failed, due to不允许提取 key 元素 CRYPTO_E_KEY_WRITE_FAIL: Service request failed, due to write access failure CRYPTO_E_KEY_NOT_AVAILABLE: Service request failed, because key not available)
     - 
     -
   * - 
     - CRYPTO_E_SMALL_BUFFER：提供的存储结果缓冲区太小 CRYPTO_E_JOB_CANCELLED：服务请求失败，因为同步作业已被   取消 (CRYPTO_E_SMALL_BUFFER：The storage buffer provided for the result is too small CRYPTO_E_JOB_CANCELLED：Service request failed because the synchronous job was cancelled)
     - 
     -
   * - 
     - CRYPTO_E_KEY_EMPTY：请求失败，因为未初始化的源 key 元素 (CRYPTO_E_KEY_EMPTY：The request failed because an uninitialized source key element was present.)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 将接收到的 Job 分派给配置的加密驱动程序对象 (Dispatch received Job to configured encryption driver object)
     - 
     - 




CryIf_CancelJob
===============================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - CryIf_CancelJob
     - 
     - 
   * - 函数原型： (Function prototype:)
     - FUNC(Std_ReturnType,CRYIF\_CODE)
     - 
     - 
   * - 
     - CryIf\_CancelJob(
     - 
     - 
   * - 
     - uint32channelId,
     - 
     - 
   * - 
     - P2VAR(Crypto_JobType,AUTOMATIC,CRYIF_APPL_DATA)job
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
     - 是 (Is)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - channelId
     - 值域： (Domain:)
     - CRYIF_CHANNELS_MAX\_CONFIGURED
   * - 输入输出参数： (Input Output Parameters:)
     - job
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无
     - 
     - 
   * - 返回值： (Return Value:)
     - E_OK：请求成功，作业已被删除 (E_OK: Request succeeded, job has been deleted)
     - 
     - 
   * - 
     - E_NOT_OK：请求失败，无法删除作业 (E_NOT_OK: Request failed, unable to delete job)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 将Job取消函数分派给配置的加密驱动程序对象 (Assign the job cancellation function to the configured encryption driver object)
     - 
     - 




CryIf_KeyElementSet
===================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - CryIf_KeyElementSet
     - 
     - 
   * - 函数原型： (Function prototype:)
     - FUNC(Std_ReturnType,CRYIF\_CODE)CryIf\_KeyElementSet(
     - 
     - 
   * - 
     - uint32cryIfKeyId,uint32
     - 
     - 
   * - 
     - keyElementId,
     - 
     -
   * - 
     - P2CONST(uint8,AUTOMATIC,CRYIF_APPL_DATA)keyPtr,
     - 
     - 
   * - 
     - uint32keyLength
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
     - cryIfKeyId
     - 值域： (Domain:)
     - CRYIF_KEY_MAX\_CONFIGURED
   * - 
     - keyElementId
     - 
     - CRYIF_KEYELEMENT_MAX\_CONFIGURED
   * - 
     - keyPtr
     - 
     - 无
   * - 
     - keyLength
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
     - E_OK：请求成功 (E_OK: Request succeeded)
     - 
     - 
   * - 
     - E_NOT_OK：请求失败 (E_NOT_OK: Request failed)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 将把 set keyelement 函数分配给配置好的cryptodriver 对象 (Set the keyelement function to the configured cryptodriver object)
     - 
     - 




CryIf_KeySetValid
=================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - CryIf_KeySetValid
     - 
     - 
   * - 函数原型： (Function prototype:)
     - FUNC(Std_ReturnType,CRYIF_CODE)CryIf_KeySetValid(
     - 
     - 
   * - 
     - uint32cryIfKeyId
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
     - cryIfKeyId
     - 值域： (Domain:)
     - CRYIF_KEY_MAX\_CONFIGURED
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无
     - 
     - 
   * - 返回值： (Return Value:)
     - E_OK：请求成功E_NOT_OK：请求失败 (E_OK: Request succeeded E_NOT_OK: Request failed)
     - 
     - 
   * - 
     - CRYPTO_E_BUSY：请求失败，Crypro驱动对象忙 (CRYPTO_E_BUSY: Request failed, Crypto driver object busy)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 把设置的密钥有效函数分派给配置的密码驱动程序对象。 (Assign the configured password driver object with the effective key setting function.)
     - 
     - 




CryIf_KeyElementGet
===================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - CryIf_KeyElementGet
     - 
     - 
   * - 函数原型： (Function prototype:)
     - FUNC(Std_ReturnType, CRYIF_CODE)CryIf_KeyElementGet(uint32cryIfKeyId,uint32keyElementId,P2VAR(uint8,AUTOMATIC,
     - 
     - 
   * - 
     - CRYIF_APPL_DATA)resultPtr,P2VAR(uint32,AUTOMATIC,
     - 
     - 
   * - 
     - CRYIF_APPL_DATA)
     - 
     - 
   * - 
     - resultLengthPtr
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
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 是 (Is)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - cryIfKeyId
     - 值域： (Domain:)
     - CRYIF_KEY_MAX\_CONFIGURED
   * - 
     - keyElementId
     - 
     - CRYIF_KEYELEMENT_MAX\_CONFIGURED
   * - 输入输出参数： (Input Output Parameters:)
     - resultPtr
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - resultLengthPtr
     - 
     - 
   * - 返回值： (Return Value:)
     - E_OK：请求成功E\_NOT\_OK：请求加密失败 (E_OK: Request succeededE_NOT_OK: Request encryption failed)
     - 
     - 
   * - 
     - CRYPTO\_E_BUSY：请求失败，密码驱动对象忙CRYPTO_E_KEY_NOT_AVAILABLE：请求失败，被请求的密钥元素不可用 (CRYPTO_E BUSY: Request failed, cryptographic object busy CRYPTO_E_KEY_NOTAVAILABLE: Request failed, requested key element unavailable)
     - 
     - 
   * - 
     - CRYPTO_E_KEY_READ_FAIL：请求失败，因为readaccess被拒绝CRYPTO_E_SMALL_BUFFER：提供的缓冲区太小，无法存储结果CRYPTO_E_KEY_EMPTY：由于未初始化源密钥元素而导致请求失败 (CRYPTO_E_KEY_READ_FAIL：Request failed because read access was denied CRYPTO_E_SMALL_BUFFER：The provided buffer is too small to store the result CRYPTO_E_KEY_EMPTY：Request failed due to uninitialized source key elements)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 把 get密钥元素函数分派给已配置的密码驱动程序对象 (Delegate the get密钥元素函数 to the configured password driver object)
     - 
     - 




CryIf_KeyElementCopy
====================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - CryIf_KeyElementCopy
     - 
     - 
   * - 函数原型： (Function prototype:)
     - FUNC(Std_ReturnType,CRYIF_CODE)CryIf_KeyElementCopy(uint32
     - 
     - 
   * - 
     - cryIfKeyId,uint32
     - 
     - 
   * - 
     - keyElementId,uint32targetCryIfKeyId,
     - 
     - 
   * - 
     - uint32targetKeyElementId
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
     - 是 (Is)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - cryIfKeyId
     - 值域： (Domain:)
     - CRYIF_KEY_MAX_CONFIGURED
   * - 
     - keyElementId
     - 
     - CRYIF_KEYELEMENT_MAX\_CONFIGURED
   * - 
     - targetCryIfKeyId
     - 
     - CRYIF_KEY_MAX_CONFIGURED
   * - 
     - targetKeyElementId
     - 
     - CRYIF_KEYELEMENT_MAX\_CONFIGURED
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无
     - 
     - 
   * - 返回值： (Return Value:)
     - E_OK：请求成功E_NOT_OK：请求失败 (E_OK: Request succeeded E_NOT_OK: Request failed)
     - 
     - 
   * - 
     - CRYPTO_E_BUSY：请求失败，密码驱动对象忙CRYPTO_E\_KEY_NOT\_AVAILABLE：请求失败，请求的密钥元素不可用 (CRYPTO_E_BUSY: Request failed, cryptographic object busy CRYPTO_E_KEY_NOT_AVAILABLE: Request failed, requested key element unavailable)
     - 
     - 
   * - 
     - CRYPTO_E_KEY_READ_FAIL：请求失败，不允许提取key 元素CRYPTO_E_KEY_WRITE_FAIL：请求失败，不允许写入密钥元素CRYPTO_E_KEY_SIZE_MISMATCH：请求失败，key元素大小不兼容 (CRYPTO_E_KEY_READ_FAIL：Request failed, key element extraction not allowedCRYPTO_E_KEY_WRITE_FAIL：Request failed, key writing not allowedCRYPTO_E_KEY_SIZE_MISMATCH：Request failed, key element size mismatch)
     - 
     - 
   * - 
     - CRYPTO\_E_KEY_EMPTY：由于未初始化源密钥元素而导致请求失败 (CRYPTO_E_KEY_EMPTY：Failed due to uninitialized source key element)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 将一个key元素从一个key复制到一个目标key (Copy a key element from one key to a target key)
     - 
     - 




CryIf_KeyElementCopyPartial
===========================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - CryIf_KeyElementCopyPartial
     - 
     - 
   * - 函数原型： (Function prototype:)
     - FUNC(Std_ReturnType,CRYIF_CODE)CryIf_KeyElementCopyPartial(
     - 
     - 
   * - 
     - uint32cryIfKeyId,uint32keyElementId,
     - 
     - 
   * - 
     - uint32keyElementSourceOffset,uint32keyElementTargetOffset,uint32keyElementCopyLength,uint32
     - 
     - 
   * - 
     - targetCryIfKeyId,
     - 
     - 
   * - 
     - uint32targetKeyElementId
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
     - 是 (Is)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - cryIfKeyId
     - 值域： (Domain:)
     - CRYIF_KEY_MAX\_CONFIGURED
   * - 
     - keyElementId
     - 
     - CRYIF_KEYELEMENT_MAX\_CONFIGURED
   * - 
     - keyElementSourceOffset
     - 
     - 无
   * - 
     - keyElementTargetOffset
     - 
     - 无
   * - 
     - keyElementCopyLength
     - 
     - 无
   * - 
     - targetCryIfKeyId
     - 
     - CRYIF_KEY_MAX\_CONFIGURED
   * - 
     - targetKeyElementId
     - 
     - CRYIF_KEYELEMENT_MAX\_CONFIGURED
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无
     - 
     - 
   * - 返回值： (Return Value:)
     - E_OK：请求成功E_NOT_OK：请求失败 (E_OK: Request succeeded E_NOT_OK: Request failed)
     - 
     - 
   * - 
     - CRYPTO_E_BUSY：请求失败，密码驱动对象忙CRYPTO_E_KEY_NOT_AVAILABLE：请求失败，请求的密钥元素不可用 (CRYPTO_E_BUSY：Request failed, cryptographic object busy CRYPTO_E_KEY_NOT_AVAILABLE：Request failed, requested key element unavailable)
     - 
     - 
   * - 
     - CRYPTO_E_KEY_READ_FAIL：请求失败，不允许提取key 元素CRYPTO_E_KEY_WRITE_FAIL：请求失败，不允许写入密钥元素CRYPTO\_E_KEY_SIZE_MISMATCH：请求失败，key元素大小不兼容 (CRYPTO_E_KEY_READ_FAIL：Request failed, key element extraction not allowed CRYPTO_E_KEY_WRITE_FAIL：Request failed, key element writing not allowed CRYPTO_E_KEY_SIZE_MISMATCH：Request failed, key element size mismatch)
     - 
     - 
   * - 
     - CRYPTO\_E_KEY_EMPTY：由于未初始化源密钥元素而导致请求失败 (CRYPTO_E_KEY_EMPTY：Failed due to uninitialized source key element)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 将一个键元素复制到另一个键元素。 (Copy a key element to another key element.)
     - 
     - 
   * - 
     - keyElementOffsets和keyElementCopyLength只允许将源键元素的一部分复制到目标键元素中。 (keyElementOffsets and keyElementCopyLength only allow copying a part of source key elements to target key elements.)
     - 
     - 




CryIf_KeyCopy
=============================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - CryIf_KeyCopy
     - 
     - 
   * - 函数原型： (Function prototype:)
     - FUNC(Std_ReturnType,CRYIF_CODE)CryIf_KeyCopy(
     - 
     - 
   * - 
     - uint32cryIfKeyId,uint32
     - 
     - 
   * - 
     - targetCryIfKeyId
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
     - 是 (Is)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - cryIfKeyId
     - 值域： (Domain:)
     - CRYIF_KEY_MAX\_CONFIGURED
   * - 
     - targetCryIfKeyId
     - 
     - CRYIF_KEY_MAX\_CONFIGURED
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无
     - 
     - 
   * - 返回值： (Return Value:)
     - E_OK：请求成功E\_NOT_OK：请求失败 (E_OK：Request succeeded E_NOT_OK：Request failed)
     - 
     - 
   * - 
     - CRYPTO\_E_BUSY：请求失败，密码驱动对象忙CRYPTO_E_KEY_NOT_AVAILABLE：请求失败，请求的密钥元素不可用 (CRYPTO_E_BUSY: Request failed, cryptographic object is busy CRYPTO_E_KEY_NOTAVAILABLE: Request failed, requested key element unavailable)
     - 
     - 
   * - 
     - CRYPTO_E_KEY_READ_FAIL：请求失败，不允许提取key 元素CRYPTO_E_KEY_WRITE_FAIL：请求失败，不允许写入密钥元素CRYPTO\_E\_KEY_SIZE_MISMATCH：请求失败，key元素大小不兼容CRYPTO_E_KEY_EMPTY：由于未初始化源密钥元素而导致请求失败 (CRYPTO_E_KEY_READ_FAIL：Request failed, key element extraction not allowed CRYPTO_E_KEY_WRITE_FAIL：Request failed, key writing not allowed CRYPTO_E_KEY_SIZE_MISMATCH：Request failed, key element size mismatch CRYPTO_E_KEY_EMPTY：Request failed due to uninitialized source key element)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 将源密钥中的所有key元素复制到目标密钥中 (Copy all key elements from the source key to the target key)
     - 
     - 




CryIf_RandomSeed
================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - CryIf_RandomSeed
     - 
     - 
   * - 函数原型： (Function prototype:)
     - Std_ReturnTypeCryIf_RandomSeed( uint32cryIfKeyId，const uint8\*seedPtr，uint32seedLength)
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x07
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步或异步，取决于配置 (Synchronized or asynchronous, depends on the configuration.)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 是 (Is)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - cryIfKeyId
     - 值域： (Domain:)
     - CRYIF_KEY_MAX\_CONFIGURED
   * - 
     - seedPtr：保存一个指向内存位置的指针，该内存位置包含为种子提供数据的指针。 (seedPtr: A pointer that saves a memory location which contains the pointer providing data for the seed.)
     - 
     - 无
   * - 
     - seedLength：包含种子的长度，以字节为单位 (seedLength：The length of the seed, in bytes)
     - 
     - uint32
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无
     - 
     - 
   * - 返回值： (Return Value:)
     - E_OK：请求成功 (E_OK: Request succeeded)
     - 
     - 
   * - 
     - E_NOT_OK：请求失败 (E_NOT_OK: Request failed)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 该函数将随机种子函数分配给配置好的密码驱动对象 (The function assigns a random seed function to the configured password driver object.)
     - 
     - 




CryIf_KeyGenerate
=================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - CryIf_KeyGenerate
     - 
     - 
   * - 函数原型： (Function prototype:)
     - FUNC(Std_ReturnType,CRYIF_CODE)CryIf_KeyGenerate(
     - 
     - 
   * - 
     - uint32cryIfKeyId
     - 
     - 
   * - 
     - )
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x07
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 取决于配置 (Depends on configuration)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 是 (Is)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - cryIfKeyId
     - 值域： (Domain:)
     - CRYIF_KEY_MAX\_CONFIGURED
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无
     - 
     - 
   * - 返回值： (Return Value:)
     - E_OK：请求成功 (E_OK: Request succeeded)
     - 
     - 
   * - 
     - E\_NOT_OK：请求失败 (E_NOT_OK: Request failed)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 将随机种子函数分配给配置好的密码驱动对象 (Assign the random seed function to the configured password driver object)
     - 
     - 




CryIf_KeyDerive
===============================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - CryIf_KeyDerive
     - 
     - 
   * - 函数原型： (Function prototype:)
     - FUNC(Std_ReturnType,CRYIF_CODE)
     - 
     - 
   * - 
     - CryIf_KeyDerive(
     - 
     - 
   * - 
     - uint32cryIfKeyId,uint32
     - 
     - 
   * - 
     - targetCryIfKeyId
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
     - 是 (Is)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - cryIfKeyId
     - 值域： (Domain:)
     - CRYIF_KEY_MAX\_CONFIGURED
   * - 
     - targetCryIfKeyId
     - 
     - CRYIF_KEY_MAX\_CONFIGURED
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无
     - 
     - 
   * - 返回值： (Return Value:)
     - E_OK：请求成功E_NOT_OK：请求失败 (E_OK: Request succeeded E_NOT_OK: Request failed)
     - 
     - 
   * - 
     - CRYPTO_E_KEY_EMPTY：由于未初始化源密钥元素而导致请求失败 (CRYPTO_E_KEY_EMPTY：Due to failure in request due to uninitialized source key element)
     - 
     - 


CryIf_KeyExchangeCalcPubVal
===========================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - CryIf_KeyExchangeCalcPubVal
     - 
     - 
   * - 函数原型： (Function prototype:)
     - FUNC(Std_ReturnType,CRYIF_CODE)CryIf_KeyExchangeCalcPubVal(
     - 
     - 
   * - 
     - uint32cryIfKeyId,
     - 
     - 
   * - 
     - P2VAR(uint8,AUTOMATIC,
     - 
     - 
   * - 
     - CRYIF_APPL_DATA)publicValuePtr,
     - 
     - 
   * - 
     - P2VAR(uint32,AUTOMATIC,
     - 
     - 
   * - 
     - CRYIF_APPL_DATA)publicValueLengthPtr
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
     - 是 (Is)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - cryIfKeyId
     - 值域： (Domain:)
     - CRYIF_KEY_MAX\_CONFIGURED
   * - 输入输出参数： (Input Output Parameters:)
     - publicValueLengthPtr
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - publicValuePtr
     - 
     -
   * - 返回值： (Return Value:)
     - E_OK：请求成功E_NOT_OK：请求失败 (E_OK: Request succeeded E_NOT_OK: Request failed)
     - 
     - 
   * - 
     - CRYPTO_E_BUSY：请求失败，密码驱动对象忙CRYPTO_E_SMALL_BUFFER：提供的缓冲区太小，无法存储结果 (CRYPTO_E BUSY: Request failed, cryptographic driver object is busy CRYPTO_E SMALL BUFFER: The provided buffer is too small to store the result)
     - 
     - 
   * - 
     - CRYPTO\_E\_KEY\_EMPTY：请求失败，因为没有初始化源key 元素 (CRYPTO_E_KEY_EMPTY：The request failed because the source key element has not been initialized.)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 将密钥交换公共值计算函数分配给配置好的密码驱动对象 (Assign the key exchange public value calculation function to the configured cryptographic driver object)
     - 
     - 




CryIf_KeyExchangeCalcSecret
===========================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - CryIf_KeyExchangeCalcSecret
     - 
     - 
   * - 函数原型： (Function prototype:)
     - FUNC(Std_ReturnType,CRYIF_CODE)CryIf_KeyExchangeCalcSecret(
     - 
     - 
   * - 
     - uint32cryIfKeyId,
     - 
     - 
   * - 
     - P2CONST(uint8,AUTOMATIC,
     - 
     -
   * - 
     - CRYIF_APPL_DATA)partnerPublicValuePtr,uint32partnerPublicValueLength
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
     - 是 (Is)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - cryIfKeyId
     - 值域： (Domain:)
     - CRYIF_KEY_MAX\_CONFIGURED
   * - 
     - partnerPublicValuePtr
     - 
     - 无
   * - 
     - partnerPublicValueLength
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
     - E_OK：请求成功 (E_OK: Request succeeded)
     - 
     - 
   * - 
     - E_NOT_OK：请求失败 (E_NOT_OK: Request failed)
     - 
     -
   * - 
     - CRYPTO_E_BUSY：请求失败，密码驱动对象忙CRYPTO_E_SMALL_BUFFER：提供的缓冲区太小，无法存储结果 (CRYPTO_E BUSY: Request failed, cryptographic driver object is busy CRYPTO_E SMALL BUFFER: The provided buffer is too small to store the result)
     - 
     - 
   * - 
     - CRYPTO_E_KEY_EMPTY：请求失败，因为没有初始化源key 元素 (CRYPTO_E_KEY_EMPTY：Failed due to uninitialized source key element)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 将密钥交换公共共享秘密计算函数分配给配置好的密码驱动对象 (Assign the key exchange public shared secret computation function to the configured cryptographic driver object)
     - 
     - 


CryIf_CallbackNotification
==========================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - CryIf_CallbackNotification
     - 
     - 
   * - 函数原型： (Function prototype:)
     - FUNC(void,CRYIF_CODE)
     - 
     - 
   * - 
     - CryIf_CallbackNotification(
     - 
     - 
   * - 
     - P2VAR(Crypto_JobType,AUTOMATIC,CRYIF_APPL_DATA)job,Std_ReturnTyperesult
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
     - job
     - 值域： (Domain:)
     - 无
   * - 
     - result
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
     - 无
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 通知 CRYIF关于密码操作结果的请求的完成 (Notification of Completion for Password Operation Result Request by CRYIF)
     - 
     - 


可配置函数定义 (Configurable Function Definitions)
-----------------------------------------------------------

无。

None.

配置 (Configuration)
==================================

CryIfGeneralConfig
----------------------------------

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/CryIf/image3.png
   :alt: CryIfGeneralConfig 容器配置图 (CryIfGeneralConfig Container Configuration Diagram)
   :name: CryIfGeneralConfig 容器配置图 (CryIfGeneralConfig Container Configuration Diagram)
   :align: center


.. centered:: **表 ryIfGeneralConfig 属性描述 (Table ryIfGeneralConfig Property Description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - CryIfDevErrorDetect
     - 取值范围 (Range)
     - TRUE/FALSE
     - 默认取值 (Default value)
     - FALSE
   * - 
     - 参数描述 (Parameter Description)
     - 打开或关闭开发错误检测和通知。 (Enable or disable development error detection and notifications.)
     - 
     - 
   * - 
     - 
     - true：启用检测和通知。false：检测和通知被禁用。 (true: Enable detection and notification. false: Detection and notification are disabled.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - CryIfVersionInfoApi
     - 取值范围 (Range)
     - TRUE/FALSE
     - 默认取值 (Default value)
     - FALSE
   * - 
     - 参数描述 (Parameter Description)
     - 如预处理程序切换以启用和禁用API 的可用性 (Switch the preprocessor to enable and disable API availability)
     - 
     - 
   * - 
     - 
     - CryIf_GetVersionInfo()。
     - 
     - 
   * - 
     - 
     - True： APICryIf_GetVersionInfo()是可用的错误：APICryIf_GetVersionInfo()不可用。 (True: APICryIf_GetVersionInfo() is available Error: APICryIf_GetVersionInfo() is not available.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 




CryIfChannelConfig
----------------------------------

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/CryIf/image4.png
   :alt: CryIfChannelConfig 容器配置图 (CryIfChannelConfig Container Configuration Diagram)
   :name: CryIfChannelConfig 容器配置图 (CryIfChannelConfig Container Configuration Diagram)
   :align: center


.. centered:: **表 CryIfChannelConfig 属性描述 (Table CryIfChannelConfig Property Description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - CryIfChannelId
     - 取值范围 (Range)
     - 0..4294967295
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 密码通道的标识符。 (Identifier for the password channel.)
     - 
     - 
   * - 
     - 
     - 指定 CSM队列连接到哪个加密通道。 (Specify which encryption channel the CSM queue connects to.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 创建后自动生成ID (Automatically generate ID after creation)
     - 
     - 
   * - CryIfDriverObjectRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 此参数引用加密驱动程序对象。指定密码通道连接到哪个密码驱动程序对象 (This parameter references an encryption driver object. Specify the password channel to connect to which encryption driver object.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 依赖于 CryptoDriver 中配置的Channel (Dependent on the Channel configured in CryptoDriver)
     - 
     - 




CryIfKeyConfig
------------------------------

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/CryIf/image5.png
   :alt: CryIfKeyConfig 容器配置图 (CryIfKeyConfig Container Configuration Diagram)
   :name: CryIfKeyConfig 容器配置图 (CryIfKeyConfig Container Configuration Diagram)
   :align: center


.. centered:: **表 CryIfKeyConfig 属性描述 (Table CryIfKeyConfig Property Description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - CryIfKeyId
     - 取值范围 (Range)
     - 0..4294967295
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - CryIfkey的标识符。 (Identifier.of.CryIfkey.)
     - 
     - 
   * - 
     - 
     - 指定 CSM密钥映射到哪个CryIf 密钥。 (Map the specified CSM key to which CryIf key.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 创建后自动生成ID (Automatically generate ID after creation)
     - 
     - 
   * - CryIfKeyRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 此参数引用密码驱动程序密钥。 (This parameter references the password driver key.)
     - 
     - 
   * - 
     - 
     - 指定 CryIf密钥映射到哪个加密驱动程序密钥。 (Map the CryIf key to which encryption driver key.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 依赖于 CryptoDriver 中配置的Key (Dependent on the Key configured in CryptoDriver)
     - 
     - 




CryifIncludesConfig
-----------------------------------

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/CryIf/image6.png
   :alt: CryifIncludeConfig配置图 (CryifIncludeConfig Configuration Diagram)
   :name: CryifIncludeConfig配置图 (CryifIncludeConfig Configuration Diagram)
   :align: center


.. centered:: **表 CryifIncludeConfig属性描述 (Table CryifIncludeConfig Property Description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - IncludeName
     - 取值范围 (Range)
     - String
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 此参数用于cryif的配置文件引用头文件 (This parameter is used for referencing header files in the cryif configuration file.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
