====================
CsM
====================

文档信息 Document Information
==============================

版本历史 Version History
----------------------------------------------------

.. list-table::
   :widths: 10 10 10 10 20
   :header-rows: 1

   * - 日期(Date)
     - 作者(Author)
     - 版本(Version)
     - 状态(Status)
     - 说明(Description)

   * - 2025/02/22
     - jie.gu
     - V0.1
     - 发布(Release)
     - 首次发布(First release)

   * - 2025/04/04
     - jie.gu
     - V1.0
     - 发布(Release)
     - 正式发布(Official release)

参考文档 References
----------------------------------------------------

.. list-table::
   :widths: 10 10 30 10
   :header-rows: 1

   * - 编号(Number)
     - 分类(Classification)
     - 标题(Title)
     - 版本(Version)
   * - 1
     - Autosar
     - AUTOSAR_CP_SRS_CryptoStack.pdf
     - R23-11
   * - 2
     - Autosar
     - AUTOSAR_CP_SWS_CryptoServiceManager.pdf
     - R23-11 



术语与简写 Terms and Abbreviations
==================================


术语 Terms
----------------------------------------------------
.. :align: center   表格内容居中(Table contents are centered)


.. list-table::
   :widths: 10 40
   :header-rows: 1

   * - 术语(Terms)
     - 解释(Explanation)

   * - Crypto Driver Object
     - Crypto Driver实现一个或多个Crypto Driver Object。Crypto Driver Object可通过硬件或软件提供不同的crypto primitive。同一Crypto Driver下的各个Crypto Driver Object彼此独立。每个Crypto Driver Object仅拥有一个workspace(即同一时间只能执行一个 crypto primitive)。(Crypto Driver realizes one or more Crypto Driver Objects.) The Crypto Driver Object can provide different crypto primitives via either hardware or software. Each Crypto Driver Object under the same Crypto Driver is independent from each other. Each Crypto Driver Object has one workspace only (i.e. only one crypto primitive can be executed each time).

   * - Key
     - Key可由Csm中的job进行引用。在Crypto Driver中，该Key指向特定的key type。(Key can be referenced by job in Csm.) In Crypto Driver, this key points to the specific key type. 

   * - Key Type 
     - key type由key element构成，且指向这些key element。通常，key type由Crypto Driver的供应商预先配置。(The key type consists of key elements and points to these key elements.) The key type is generally pre-configured by the supplier of the Crypto Driver. 

   * - Key Element 
     - Key element用于存储数据。此类数据例如可以是密钥材料(key material)，或是AES加密所需的初始向量(IV)；Key element还可用于配置密钥管理功能(key management functions)的行为。不同Key对应的Key element拥有不同的存储区域(包括非易失性存储区NV和随机存取存储区RAM)。(The key element is used for storing data.) This type of data can be key material or the initial vector (IV) required for AES encryption; furthermore, the Key elements can also be used for configuring the behavior of key management functions. The Key elements corresponding to different keys have different storage areas (including non-volatile memory NV and random access memory RAM).

   * - Job
     - Job是已完成配置的 “CsmJob”。其中，Job会引用key、cryptographic primitive 以及reference channel等要素。(Job refers to the configured 'CsmJob'.) To be specific, Job will reference elements such as key, cryptographic primitive, and reference channel.

   * - Channel
     - channel是从Crypto Service Manager队列经Crypto Interface到特定Crypto Driver Object的路径。(Channel is the path from the Crypto Service Manager queue to a specific Crypto Driver Object via the Crypto Interface.) 
   
   * - Primitive
     - primitive是在Crypto Driver Object中实现的、已配置的加密算法(cryptographic algorithm)的实例。其中，primitive会引用CSM提供给应用的功能、具体的底层 “algorithmfamily”(如 AES、MD5、RSA等)以及 “algorithmmode”(如 ECB、CBC等)。(primitive is an instance of a configured cryptographic algorithm realized in the Crypto Driver Object.) To be specific, primitive will reference the functions provided by CSM for the application, the specific underlying "algorithm family" (such as AES, MD5, RSA, etc.), and "algorithm mod" (such as ECB, CBC, etc.).

   * - Operation
     - crypto primitive的操作(operation)用于声明应执行该加密原语的哪部分功能。存在三种不同的操作类型：(The operation of crypto primitive is used for declaring the specific part of the function of the encryption primitive that should be executed) There're three different operation types:

   * - START
     - Operation表示一个新的crypto primitive请求，它应取消所有先前的请求，执行必要的初始化，并检查该加密原语是否可被处理。(Operation refers to a new crypto primitive request that should cancel all previous requests, perform necessary initialization, and check if the encryption primitive can be processed.)

   * - UPDATE
     - Operation表示crypto primitive需要输入数据。更新操作(update operation)可提供中间结果。(Operation means that crypto primitive needs data inputting.) The update operation can provide intermediate results.

   * - FINISH
     - Operation表示，至此所有数据已完全输入，crypto primitive可完成最终计算。完成操作(finish operation)可提供最终结果。(Operation means that all data has been fully inputted, and crypto primitive can complete the final calculation.) The finish operation can provide the final results.

   * - Priority
     - job的priority定义了其重要程度。priority数值越高，job的执行就越紧急。cryptographic job的priority是配置的一部分。(The priority of job defines its level of importance.) The higher the priority value, the more urgent the job execution. The priority of cryptographic jobs is part of the configuration.

   * - Processing
     - 指示job处理的类型。(It indicates the type of job processing.) 
 
   * - Service
     - service应按照《TR_Glossary》文档中的定义理解：service是一种operation类型，其接口(interface)和行为(behavior)具有公开的规范(published specification)，涉及能力提供者(provider of the capability)与潜在客户端(potential clients)之间的约定(contract)。(Service should be understood according to the definition in the TR_Glossary file: Service refers to an operation type, the interface and behavior of which have published specifications. It involves the contract between providers of the capability and potential clients.)



简写 Abbreviations
----------------------------------------------------

.. list-table::
   :widths: 10 20 30
   :header-rows: 1


   * - 简写(Abbreviation)
     - 全称(Full name)
     - 解释(Explanation)
   * - AEAD
     - Authenticated Encryption with Associated Data 
     - 认证加密与关联数据
   * - CDD
     - Complex Device Driver 
     - 复杂设备驱动
   * - CSM
     - Crypto Service Manager
     - 加密服务管理器
   * - CRYIF
     - Crypto Interface 
     - 加密接口层
   * - CRYPTO
     - Crypto Driver 
     - 加密驱动
   * - DET
     - Default Error Tracer 
     - 默认错误追踪器
   * - HSM
     - Hardware Security Module
     - 硬件安全模块
   * - HW
     - Hardware
     - 硬件
   * - SHE
     - Security Hardware Extension 
     - 安全硬件扩展
   * - SW
     - Software
     - 软件

      

简介 Introduction
=================

CSM提供了所有的加密服务，包括对称加密、非对称加密、哈希、签名、密钥管理等，为上层应用提供统一的加密接口。

CSM provides all encryption services, including symmetric encryption, asymmetric encryption, hashing, signature, key management, etc. It also provides unified encryption interface for upper layer applications.


功能描述 Functional Description
==================================


特性 Features
-------------------------------------------------

1.CSM基本功能介绍

1.Introduction to CSM's basic functions

CSM是一种提供加密功能的服务，它基于一个依赖于软件库或硬件模块的加密驱动程序。此外，混合设置与多个密码驱动程序是可能的。CSM通过CRYIF访问不同的加密驱动程序

CSM is a kind of service that provides encryption function and is based on an encryption driver supported by software libraries or hardware modules. It also supports the settings with multiple password drivers. CSM accesses different encryption drivers through CRYIF

2.job状态

2.job status
   
将单一的调用函数与加密Job的流方式相结合，需要模式参数，它决定了加密Job的运行模式。此服务操作是一个标志字段，指示操作模式启动、更新或完成，它显式地声明应该执行什么操作。这些操作模式可以混合使用，并同时执行。状态的实际事务是在与这些状态一起工作的层中进行的，即在加密驱动程序中。

Mode parameter is required for combining a single call function with the flow of encrypted job and it decides the running mode of the encrypted job. This service operation is a mark field, which indicates the start, update or completion of the operation mode. It can also explicitly declare the specific operation required. These operation modes can be mixed and executed simultaneously. The actual transaction of status is carried out in the layer that works with these statuses, i.e., in the encryption driver program.

   .. figure:: ../../../_static/参考手册/CsM/Job状态图.png
      :alt: Job状态图描述 (Description of Job Status Diagram)
      :name: fig_Job状态图(fig_Job status diagram)
      :align: center

单调用方法不需要多次调用显式API，只需要调用一次即可。由于单调用的开销小，可以提高性能，所以多用于需要快速处理的小数据输入过程中。当使用流方法(启动、更新、完成)操作时，专用的加密驱动程序对象正在等待进一步的输入(更新)，直到到达完成状态。同时，不能在此加密驱动程序实例上处理其他Job。

A single call method needs calling explicit API for once instead of several times. In consideration of the low expenses and its effect in performance improvement, single call is mostly used in small data input processes that require a fast processing speed. For operation using the stream method (start, update, complete), the dedicated encryption driver object is waiting for further input (update) until it reaches the complete state. Meanwhile, other Jobs cannot be processed on this encrypted driver instance.

3.同步Job

3.Synchronous Job

如果使用同步接口，则接口函数将必要的信息传递给底层加密堆栈模块并等待返回结果

If any synchronous interface is used, the interface function transmits the necessary information to the underlying encryption stack module and waits for the results

   .. figure:: ../../../_static/参考手册/CsM/同步任务执行流程图.png
      :alt: 同步任务执行流程图描述 (Description of synchronous task execution flow chart)
      :name: fig_同步任务执行流程图(fig_Synchronous task execution flow chart)
      :align: center

4.异步Job

4.Asynchronous Job

如果使用异步接口，则接口函数只能将必要的信息传递给底层加密堆栈模块，然后等待底层处理完成调用回调函数通知CSM。

If any asynchronous interface is used, the interface function can transmit the necessary information to the underlying encryption stack module only, and then call the callback function and notify CSM after the completion of underlying processing.

   .. figure:: ../../../_static/参考手册/CsM/异步任务执行流程图.png
      :alt: 异步任务执行流程图描述 (Description of asynchronous task execution flow chart)
      :name: fig_异步任务执行流程图(fig_Asynchronous task execution flow chart)
      :align: center

5.Queue相关

5.Queue Relation

Quene，即队列，为CSM内部针对Job设置的一个功能，CSM应在内部完成对其的操作。

Quene is a function duly created for Jobs inside CSM, which should complete its operations internally.

CSM可能有多个队列，其中的Job根据其优先级排列，以处理多个加密请求。从CSM队列通过CryIf到加密驱动程序对象的路径称为通道。CSM的每个队列都映射到一个通道，以访问crypto驱动程序对象的crypto原语。队列的大小是可配置的。为了优化加密驱动程序对象的硬件使用，加密驱动程序中还有一个可选的队列。加密驱动程序对象表示独立加密设备(硬件或软件，如AES加速器)的实例。对于具有高优先级的Job，HSM上可以有一个用于快速AES和CMAC计算的通道，该通道在加密驱动程序中的本地AES计算服务上结束。但同时，加密驱动程序对象也可能是软件，例如用于RSA计算，用户能够加密、解密、签名或验证数据。在同步Job处理中，队列将不起作用。因此，如果选择同步Job处理，则队列大小应该为0。但是，也可以将通道(包括队列)与同步和异步Job一起使用。可以在Csm_MainFunction()中将排队的Job传递给CRYIF。如果Job的状态是活动的，则CSM应假定映射的加密驱动程序实例当前正在处理该Job，而调用者希望继续操作(例如，使用update提供更多数据)，必须在加密驱动程序实例中执行可信性检查。

CSM may have several queues, with jobs arranged according to their priority, in order to process many encrypted requests. The path from the CSM queue to the encrypted driver object through CryIf is called channel. CSM's each queue is mapped to a channel to access the crypto primitive of the crypto driver object. The size of queue is settable. An optional queue is available in the encryption driver, in order to optimize the hardware use of encryption driver objects. The encryption driver object indicates an instance of an independent encryption device (hardware or software, such as AES accelerator). For Job with a high priority, a channel for fast AES and CMAC calculation is available on HSM and it ends on the local AES calculation service in the encryption driver. At the same time, the encryption driver object may also be software, such as the RSA calculation software. User can realize encryption, decryption, signature and data verification with it. The queue does not work during synchronous Job processing. Therefore, the size of queue should be 0 for synchronous Job processing. However, channel (including queue) can also be used together with synchronous and asynchronous Jobs. The Job of queue can be transferred to CRYIF in Csm_MainFunction(). If the status of Job is active, CSM should assume that the mapped encrypted driver instance is processing the Job. If the caller hopes to continue with operation (e.g. using update to provide more data), creditability check is required in the encrypted driver instance.

   .. figure:: ../../../_static/参考手册/CsM/Queue.png
      :alt: Queue示意图描述 (Description of Queue diagram)
      :name: fig_Queue示意图(fig_Queue diagram)
      :align: center

6.密钥管理

6.Key management

Key，即对应的keyid具有配置给出的符号名称。Crypto堆栈API使用来自CSM模块的以下关键元素索引定义：

Key is the symbol name give by configuration for the corresponding keyid. The Crypto stack API indexes definition by the following key elements from the CSM module:

   .. figure:: ../../../_static/参考手册/CsM/KeyElement示意图.png
      :alt: KeyElement示意图描述 (Description of KeyElement diagram)
      :name: fig_KeyElement示意图(fig_KeyElement diagram)
      :align: center

对于包含加密密钥材料的每个密钥元素，应在用于数据交换的配置中指定所提供密钥的格式，例如Csm_KeyElementGet()或Csm_KeyElementSet()。特定密码驱动程序支持的密钥格式是随密码驱动程序一起提供的预配置信息的一部分。特定于供应商的keyelementid应该启动1000来避免对未来扩展版本的加密堆栈的干扰。关键元素CRYPTO_KE_[…]_ALGORITHM用于配置密钥管理函数的行为，因为它们独立于Job，因此不能像原语那样进行配置。

For each key element containing encrypted key material, the format of the provided key should be specified in the configuration used for data exchange, such as Csm_KeyElementGet() or Csm_KeyElementSet(). The key format supported by specific password driver is part of the pre-configured information provided together with password driver. For supplier's keyelementid, 1000 should be started to avoid interference with future extended versions of the encryption stack. The key element CRYPTO_KE_[…]_ALGORITHM is used for configuring key management function. It is independent from Job so it cannot be configured like primitives.


偏差 Deviation
----------------------------------
1.Csm模块当前不支持秘钥重定向和秘钥派生。

1.The Csm module does not support key redirection and key derivation temporarily.

扩展 Extension
----------------------------------

None


集成 Integration
====================

文件列表 File List
----------------------------------

.. figure:: ../../../_static/参考手册/CsM/Filelist.png
   :alt: CsM组件文件组织结构描述 (Description of CsM component file organization structure)
   :name: fig_CsmFilelist
   :align: center

   CsM组件文件组织结构描述.
   
   Descriptions of CsM component file organization structure

如图  :ref:`fig_CsmFilelist` 所示，CsM模块的文件引用关系如下：

As shown in the figure :ref:`fig_CsmFilelist`, the file reference relationship of the CsM module is shown as follows:

静态文件 Static Files
~~~~~~~~~~~~~~~~~~~~~~~~~~
None

动态文件 Dynamic Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - 文件(File)
     - 描述(Description)
   
   * - Csm.c 
     - CSM模块源文件，包含了API函数的实现。(The CSM module source file, which contains the realization of API functions.) 

   * - Csm.h 
     - CSM模块头文件，包含了API函数的扩展声明并定义了配置的数据结构体。(The CSM module header file contains extension declarations for API functions and defines the structure of configured data.)

   * - Csm_Cbk.h 
     - 包含CSM供上层调用的API函数的声明。(Declares the API function that includes CSM for upper layer call.)

   * - Csm_Cbk.c 
     - 包含CSM供上层调用的API函数的定义。(Defines the API function that includes CSM for upper layer call.)

   * - Csm_DetCheck.c
     - 定义Csm模块DET检测的API。(Defines the API for DET detection of Csm module .)

   * - Csm_Types.h 
     - 包含Csm模块的数据类型。(Type of data containing Csm module.) 

   * - Crypto_GeneralTypes.h
     - Cryptostack通用的数据类型。(Type of general data for Cryptostack.) 

   * - Csm_MemMap.h 
     - CSM编译抽象文件。(Abstract files compiled by CSM.)

   * - Csm_Internal.h 
     - 包含CSM内部的变量和数据结构体的定义(Definition containing variables and data structures within CSM) 


  

错误处理 Error Handling
----------------------------------


开发错误 Development Errors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. list-table:: 
      :widths: 20 10 30
      :header-rows: 1

      * - Error code
        - Value[hex]
        - Description

      * - CSM_E_PARAM_POINTER 
        - 0x01
        - API request called with invalid parameter (Nullpointer) 

      * - CSM_E_PARAM_HANDLE 
        - 0x04
        - Csm Configuration ID out of range 

      * - CSM_E_UNINIT 
        - 0x05
        - API request called before initialization of CSM module

      * - CSM_E_INIT_FAILED
        - 0x07
        - Initialization of CSM module failed 

      * - CSM_E_PROCESSING_MODE 
        - 0x08
        - API request called with invalid processing mode 

      * - CSM_E_SERVICE_TYPE 
        - 0x09
        - Mismatch between the called API request and the service type of the job    


产品错误 Product Errors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
None
   

运行时错误 Runtime Errors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    .. list-table:: 
        :widths: 20 10 30
        :header-rows: 1

        * - Error code
          - Value[hex]
          - Description

        * - CSM_E_QUEUE_FULL 
          - 0x01
          - Queue overrun   


应用程序集成 Application Integration
------------------------------------------------------------------------------------------------------
1.依赖模块

1.Dependency module

配置CsM模块需要保证工程中存在CryptoDriver,CryptoInterface模块，并且配置了CryptoDriver和CryptoInterface模块。

To configure the CsM module, make sure CryptoDriver and CryptoInterface modules are available in the project and have been configured.
   

.. include:: Crypto_GeneralTypes_h_api.rst
.. include:: Csm_Cbk_h_api.rst
.. include:: Csm_h_api.rst
.. include:: Csm_Internal_h_api.rst
.. include:: Csm_Types_h_api.rst


配置 Configuration
===========================


自定义引用头文件配置 Configuration of Self-defined Reference Header File
------------------------------------------------------------------------------------------------------

用于解决编译时需要依赖外部模块所设计的配置项。

Configuration item designed based on external modules for compiling.

.. figure:: ../../../_static/参考手册/CsM/CsmIncludes.png
   :alt:  CsmIncludes配置图 (CsmIncludes Configuration Diagram)
   :name: fig_CsmIncludes
   :align: center

   fig_CsmIncludes

.. table::CsmIncludes通用配置属性(CsmIncludes general configuration attribute)
        :name: Grid_CsmIncludes

+-------------------+-----------------------------------+-------------------------------------------------------+----------------------------------------------------+------------------------------------------------------+
| UI名称（UI name） | 描述（Desription）                |                                                       |                                                    |                                                      |
+-------------------+-----------------------------------+-------------------------------------------------------+----------------------------------------------------+------------------------------------------------------+
| IncludeName       | 取值范围（Value range）           | 无（None）                                            | 默认取值                                           | 无（None）                                           |
|                   +-----------------------------------+-------------------------------------------------------+----------------------------------------------------+------------------------------------------------------+
|                   | 参数描述（Parameter description） | 用户包含外部头文件，主要包含CallCallBack函数的声明文件（The user contains external header files, mainly including the declaration file of CallCallBack function） |
|                   |                                   +-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                   |                                   | 无（None）                                                                                                                                                        |
|                   +-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                   | 依赖关系（Dependence）            | 无（None）                                                                                                                                                        |
+-------------------+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+


异步任务回调函数配置 Configuration of Asynchronous Task Callback Function
----------------------------------------------------------------------------------------------

配置异步任务时需要配置回调函数来返回结果，同步任务不需要配置和关联。

To configure asynchronous tasks, configure callback function to return results; configuration and linking are not required for synchronous task.

.. figure:: ../../../_static/参考手册/CsM/CsmCallbacks.png
   :alt:  CsmCallbacks配置图 (CsmCallbacks Configuration Diagram)
   :name: fig_CsmCallbacks
   :align: center

   fig_CsmCallbacks

.. table::CsmCallbacks通用配置属性(CsmCallbacks general configuration attribute)
        :name: Grid_CsmCallbacks

+-------------------+-----------------------------------+----------------------------+------------------------------+--------------------------------+
| UI名称（UI name） | 描述（Desription）                |                            |                              |                                |
+-------------------+-----------------------------------+----------------------------+------------------------------+--------------------------------+
| CsmCallbackFunc   | 取值范围（Value range）           | string                     | 默认取值                     | 无（None）                     |
|                   +-----------------------------------+----------------------------+------------------------------+--------------------------------+
|                   | 参数描述（Parameter description） | 用户配置于异步任务的回调函数（Callback function configured by user for asynchronous task） |
|                   |                                   +--------------------------------------------------------------------------------------------+
|                   |                                   | 无（None）                                                                                 |
|                   +-----------------------------------+--------------------------------------------------------------------------------------------+
|                   | 依赖关系（Dependence）            | 无（None）                                                                                 |
+-------------------+-----------------------------------+--------------------------------------------------------------------------------------------+


通用配置 General Configurations
------------------------------------------------------------------------------------------------------

按照自己需要是否开启这部分配置，默认不打开。

Decide whether to enable this configuration according to the specific needs; disabled by default.

.. figure:: ../../../_static/参考手册/CsM/CsmGeneral.png
   :alt:  CsmGeneral配置图 (CsmGeneral Configuration Diagram)
   :name: fig_CsmGeneral
   :align: center

   fig_CsmGeneral

.. table::CsmGeneral通用配置属性(CsmGeneral general configuration attribute)
    :name: Grid_CsmGeneral

+-------------------+-----------------------------------+----------------------------------+--------------------------------+-----------------------------+
| UI名称（UI name） | 描述（Desription）                |                                  |                                |                             |
+-------------------+-----------------------------------+----------------------------------+--------------------------------+-----------------------------+
| CsmDevErrorDetect | 参数描述（Parameter description） | 打开或关闭开发错误检测和通知（Enable or disable development error detection and notifications） |
|                   |                                   +-------------------------------------------------------------------------------------------------+
|                   |                                   | true：启用检测和通知。（true: Enable detection and notification.）                              |
|                   |                                   +-------------------------------------------------------------------------------------------------+
|                   |                                   | false：禁用检测和通知（false: Disable detection and notification）                              |
|                   +-----------------------------------+----------------------------------+--------------------------------+-----------------------------+
|                   | 依赖关系（Dependence）            | 无（None）                       |                                |                             |
+-------------------+-----------------------------------+----------------------------------+--------------------------------+-----------------------------+
| CsmVersionInfoApi | 取值范围（Value range）           | TRUE/FALSE                       | 默认取值                       | FALSE                       |
|                   +-----------------------------------+----------------------------------+--------------------------------+-----------------------------+
|                   | 参数描述（Parameter description） | 切换以启用和禁用Csm_GetVersionInfo                                                              |
|                   |                                   +-------------------------------------------------------------------------------------------------+
|                   |                                   | True：API Csm_GetVersionInfo()是可用的。（True:API Csm_GetVersionInfo() is available.）         |
|                   |                                   +-------------------------------------------------------------------------------------------------+
|                   |                                   | False：Csm_GetVersionInfo()不可用。（False: Csm_GetVersionInfo() is unavailable.）              |
|                   +-----------------------------------+----------------------------------+--------------------------------+-----------------------------+
|                   | 依赖关系（Dependence）            | 无（None）                       |                                |                             |
+-------------------+-----------------------------------+----------------------------------+--------------------------------+-----------------------------+

重定向配置 Redirect Configuration
------------------------------------------------------------------------------------------------------

此部分配置暂时没有开发对应的源码功能。

The corresponding source code function has not been developed for this part of configuration temporarily.

.. figure:: ../../../_static/参考手册/CsM/CsmInOutRedirection.png
   :alt:  CsmInOutRedirection配置图 (CsmInOutRedirection Configuration Diagram)
   :name: fig_CsmInOutRedirection
   :align: center

   fig_CsmInOutRedirection

.. table::CsmInOutRedirection通用配置属性(CsmInOutRedirection general configuration attribute)
    :name: Grid_CsmInOutRedirection
  
+--------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| UI 名称（UI name）             | 描述（Description）                                                                                                              |
+--------------------------------+-----------------------------------+--------------------------------+--------------------------------------+----------------------+
| CsmInputKeyElementId           | 取值范围（Value range）           | 0 .. 4294967295                | 默认取值（Default value）            | 无（None）           |
|                                +-----------------------------------+--------------------------------+--------------------------------------+----------------------+
|                                | 参数描述（Parameter description） | 用作输入的键元素的标识符(Identifier of the key element used as input)                        |
|                                +-----------------------------------+----------------------------------------------------------------------------------------------+
|                                | 依赖关系（Dependence）            | 无(None)                                                                                     |
+--------------------------------+-----------------------------------+--------------------------------+--------------------------------------+----------------------+
| CsmOutputKeyElementId          | 取值范围（Value range）           | 0 .. 4294967295                | 默认取值（Default value）            | 无（None）           |
|                                +-----------------------------------+--------------------------------+--------------------------------------+----------------------+
|                                | 参数描述（Parameter description） | 用作输出的键元素的标识符(Identifier of the key element used as output)                       |
|                                +-----------------------------------+----------------------------------------------------------------------------------------------+
|                                | 依赖关系（Dependence）            | 无(None)                                                                                     |
+--------------------------------+-----------------------------------+--------------------------------+--------------------------------------+----------------------+
| CsmSecondaryInputKeyElementId  | 取值范围（Value range）           | 0 .. 4294967295                | 默认取值（Default value）            | 无（None）           |
|                                +-----------------------------------+--------------------------------+--------------------------------------+----------------------+
|                                | 参数描述（Parameter description） | 用作辅助输入的键元素的标识符(Identifier of the key element used as auxiliary input)          |
|                                +-----------------------------------+----------------------------------------------------------------------------------------------+
|                                | 依赖关系（Dependence）            | 无(None)                                                                                     |
+--------------------------------+-----------------------------------+--------------------------------+--------------------------------------+----------------------+
| CsmSecondaryOutputKeyElementId | 取值范围（Value range）           | 0 .. 4294967295                | 默认取值（Default value）            | 无（None）           |
|                                +-----------------------------------+--------------------------------+--------------------------------------+----------------------+
|                                | 参数描述（Parameter description） | 用作输出的键元素的标识符(Identifier of the key element used as output)                       |
|                                +-----------------------------------+----------------------------------------------------------------------------------------------+
|                                | 依赖关系（Dependence）            | 无(None)                                                                                     |
+--------------------------------+-----------------------------------+--------------------------------+--------------------------------------+----------------------+
| CsmTertiaryInputKeyElementId   | 取值范围（Value range）           | 0 .. 4294967295                | 默认取值（Default value）            | 无（None）           |
|                                +-----------------------------------+--------------------------------+--------------------------------------+----------------------+
|                                | 参数描述（Parameter description） | 用作第三级输入的关键元素的标识符(Identifier of the key element used as tertiary input)       |
|                                +-----------------------------------+----------------------------------------------------------------------------------------------+
|                                | 依赖关系（Dependence）            | 无(None)                                                                                     |
+--------------------------------+-----------------------------------+--------------------------------+--------------------------------------+----------------------+
| CsmInputKeyRef                 | 取值范围（Value range）           | 无（None）                     | 默认取值（Default value）            | 无（None）           |
|                                +-----------------------------------+--------------------------------+--------------------------------------+----------------------+
|                                | 参数描述（Parameter description） | 这个参数指的是用作输入的key(This parameter refers to the key used as input)                  |
|                                +-----------------------------------+----------------------------------------------------------------------------------------------+
|                                | 依赖关系（Dependence）            | CsmKey                                                                                       |
+--------------------------------+-----------------------------------+--------------------------------+--------------------------------------+----------------------+
| CsmOutputKeyRef                | 取值范围（Value range）           | 无（None）                     | 默认取值（Default value）            | 无（None）           |
|                                +-----------------------------------+--------------------------------+--------------------------------------+----------------------+
|                                | 参数描述（Parameter description） | 此参数引用用作输出的键(This parameter refers to the key referenced as output)                |
|                                +-----------------------------------+----------------------------------------------------------------------------------------------+
|                                | 依赖关系（Dependence）            | CsmKey                                                                                       |
+--------------------------------+-----------------------------------+--------------------------------+--------------------------------------+----------------------+
| CsmSecondaryInputKeyRef        | 取值范围（Value range）           | 无（None）                     | 默认取值（Default value）            | 无（None）           |
|                                +-----------------------------------+--------------------------------+--------------------------------------+----------------------+
|                                | 参数描述（Parameter description） | 这个参数指的是用作辅助输入的键(This parameter refers to the key used as auxiliary input)     |
|                                +-----------------------------------+----------------------------------------------------------------------------------------------+
|                                | 依赖关系（Dependence）            | CsmKey                                                                                       |
+--------------------------------+-----------------------------------+--------------------------------+--------------------------------------+----------------------+
| CsmSecondaryOutputKeyRef       | 取值范围（Value range）           | 无（None）                     | 默认取值（Default value）            | 无（None）           |
|                                +-----------------------------------+--------------------------------+--------------------------------------+----------------------+
|                                | 参数描述（Parameter description） | 这个参数指的是用作辅助输出的键。(This parameter refers to the key used as auxiliary output.) |
|                                +-----------------------------------+----------------------------------------------------------------------------------------------+
|                                | 依赖关系（Dependence）            | CsmKey                                                                                       |
+--------------------------------+-----------------------------------+--------------------------------+--------------------------------------+----------------------+
| CsmTertiaryInputKeyRef         | 取值范围（Value range）           | 无（None）                     | 默认取值（Default value）            | 无（None）           |
|                                +-----------------------------------+--------------------------------+--------------------------------------+----------------------+
|                                | 参数描述（Parameter description） | 这个参数指的是用作第三级输入的键(This parameter refers to the key used as tertiary input)    |
|                                +-----------------------------------+----------------------------------------------------------------------------------------------+
|                                | 依赖关系（Dependence）            | CsmKey                                                                                       |
+--------------------------------+-----------------------------------+--------------------------------+--------------------------------------+----------------------+

CsmJob配置 CsmJob Configuration
--------------------------------------------

必配项，需要先配置primitives里面的模式和长度，然后关联到job中，从而实现此任务执行对应的加密算法。

Required item; first, configure the mode and length in primitive, and then link them with the job to realize the corresponding encryption algorithm for executing this task.

.. figure:: ../../../_static/参考手册/CsM/CsmJob.png
   :alt:  CsmJob配置图 (CsmJob Configuration Diagram)
   :name: fig_CsmJob
   :align: center

   fig_CsmJob

.. table::CsmJob通用配置属性(CsmJob general configuration attribute)
    :name: Grid_CsmJob

+-------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| UI 名称（UI name）                        | 描述（Description）                                                                                                                                                                                                                                                                                                                                       |
+-------------------------------------------+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+
| CsmJobId                                  | 取值范围（Value range）           | 0 .. 4294967295                                                                                                            | 默认取值（Default value）                                                                           | 无（None）                                                                         |
|                                           +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+
|                                           | 参数描述（Parameter description） | CSMjob的标识符。实际配置的标识符集应该是连续的、无间隙的。（Identifier of CSMjob. The actual identifier set configured is continuous and free of any gap.）                                                                                                                                                           |
|                                           +-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                           | 依赖关系（Dependence）            | 无(None)                                                                                                                                                                                                                                                                                                              |
+-------------------------------------------+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+
| CsmJobInterfaceUsePort                    | 取值范围（Value range）           | CRYPTO_USE_FNC、CRYPTO_USE_PORT、CRYPTO_USE_PORT                                                                           | 默认取值（Default value）                                                                           | 无（None）                                                                         |
|                                           +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+
|                                           | 参数描述（Parameter description） | job是否需要RTE接口（Whether job requires RTE interface）                                                                                                                                                                                                                                                              |
|                                           +-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                           | 依赖关系（Dependence）            | 无(None)                                                                                                                                                                                                                                                                                                              |
+-------------------------------------------+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+
| CsmJobPrimitiveCallbackUpdateNotification | 取值范围（Value range）           | TRUE/FALSE                                                                                                                 | 默认取值（Default value）                                                                           | FALSE                                                                              |
|                                           +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+
|                                           | 参数描述（Parameter description） | 此参数指示，如果更新操作已完成，是否应调用回调函数。（This parameter indicates whether to call a callback function after update is complete.）                                                                                                                                                                        |
|                                           +-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                           | 依赖关系（Dependence）            | 无(None)                                                                                                                                                                                                                                                                                                              |
+-------------------------------------------+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+
| CsmJobPriority                            | 取值范围（Value range）           | 0 .. 4294967295                                                                                                            | 默认取值（Default value）                                                                           | 无（None）                                                                         |
|                                           +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+
|                                           | 参数描述（Parameter description） | job的优先级。值越高，job的优先级越高。（Priority of job.The higher the value, the higher the job priority.）                                                                                                                                                                                                          |
|                                           +-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                           | 依赖关系（Dependence）            | 无(None)                                                                                                                                                                                                                                                                                                              |
+-------------------------------------------+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+
| CsmProcessingMode                         | 取值范围（Value range）           | CRYPTO_PROCESSING_ASYNC、CRYPTO_PROCESSING_SYNC                                                                            | 默认取值（Default value）                                                                           | 无（None）                                                                         |
|                                           +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+
|                                           | 参数描述（Parameter description） | 确定该job的接口应使用的方式。同步处理返回结果，而异步处理返回而不处理job。相应的回调将通知调用者。（Determine the specific use method of job interface. Synchronous processing returns results while asynchronous processing returns without processing jobs. Notify the caller of the corresponding callback.）      |
|                                           +-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                           | 依赖关系（Dependence）            | 无(None)                                                                                                                                                                                                                                                                                                              |
+-------------------------------------------+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+
| CsmInOutRedirectionRef                    | 取值范围（Value range）           | 无（None）                                                                                                                 | 默认取值（Default value）                                                                           | 无（None）                                                                         |
|                                           +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+
|                                           | 参数描述（Parameter description） | 此参数引用使用的重定向（This parameter references the used redirection ）                                                                                                                                                                                                                                             |
|                                           +-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                           | 依赖关系（Dependence）            | CsmInOutRedirections                                                                                                                                                                                                                                                                                                  |
+-------------------------------------------+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+
| CsmJobKeyRef                              | 取值范围（Value range）           | 无（None）                                                                                                                 | 默认取值（Default value）                                                                           | 无（None）                                                                         |
|                                           +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+
|                                           | 参数描述（Parameter description） | 这个参数指的是CsmPrimitive的应使用键。可以为不同的job使用CsmKey。（This parameter refers to the key that CsmPrimitive should use.CsmKey can be used for different jobs.）                                                                                                                                             |
|                                           +-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                           | 依赖关系（Dependence）            | CsmKey                                                                                                                                                                                                                                                                                                                |
+-------------------------------------------+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+
| CsmJobPrimitiveCallbackRef                | 取值范围（Value range）           | 无（None）                                                                                                                 | 默认取值（Default value）                                                                           | 无（None）                                                                         |
|                                           +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+
|                                           | 参数描述（Parameter description） | 此参数引用使用的CsmCallback。当加密job完成时，将调用所引用的CsmCallback。(This parameter references CsmCallback used.When the encryption job is completed, the referenced CsmCallback will be called.)|                                                                                                               |
|                                           +-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                           | 依赖关系（Dependence）            | 当CsmProcessingMode配置为ASYN异步模式(When CsmProcessingMode is configured as ASYN asynchronous mode)                                                                                                                                                                                                                 |
+-------------------------------------------+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+
| CsmJobPrimitiveRef                        | 取值范围（Value range）           | 无（None）                                                                                                                 | 默认取值（Default value）                                                                           | 无（None）                                                                         |
|                                           +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+
|                                           | 参数描述（Parameter description） | 此参数引用所使用的CsmPrimitive。不同的job可以引用一个CsmPrimitive。所引用的CsmPrimitive提供了关于实际密码例程的详细信息。(The CsmPrimitive used for referencing this parameter.One CsmPrimitive can be referenced for different jobs. The referenced CsmPrimitive provides details on the actual password routines.)| |
|                                           +-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                           | 依赖关系（Dependence）            | CsmPrimitives                                                                                                                                                                                                                                                                                                         |
+-------------------------------------------+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+
| CsmJobQueueRef                            | 取值范围（Value range）           | 无（None）                                                                                                                 | 默认取值（Default value）                                                                           | 无（None）                                                                         |
|                                           +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+
|                                           | 参数描述（Parameter description） | 如果底层加密驱动程序对象忙，则使用该队列。队列也引用所使用的通道。(Use this queue, if the underlying encryption driver object is busy. The used channel can also be referenced by queue.)                                                                                                                             |
|                                           +-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                           | 依赖关系（Dependence）            | CsmQueue                                                                                                                                                                                                                                                                                                              |
+-------------------------------------------+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+

CsmKeys配置 CsmKeys Configuration
------------------------------------------------------------------------------------------------------

必配项，大部分算法需要秘钥进行加密。直接从下层的CryIf模块中获取引用，然后被job关联，在对应的算法中使用该秘钥。

Required, for key is required in most algorithms key for encryption. Get a reference directly from the CryIf module at the lower level, then link it with Job and use the key in the corresponding algorithm.

.. figure:: ../../../_static/参考手册/CsM/CsmKeys.png
   :alt:  CsmKeys配置图 (CsmKeys Configuration Diagram)
   :name: fig_CsmKeys
   :align: center

   fig_CsmKeys

.. table::CsmKeys通用配置属性(CsmKeys general configuration attribute)
    :name: Grid_CsmKeys

+--------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| UI 名称（UI name） | 描述（Description）                                                                                                                                                                                                                                               |
+--------------------+-----------------------------------+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------+---------------------------------------------------------+
| CsmKeyId           | 取值范围（Value range）           | 0 .. 4294967295                                                                            | 默认取值（Default value）                                              | 无（None）                                              |
|                    +-----------------------------------+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------+---------------------------------------------------------+
|                    | 参数描述（Parameter description） | CsmKey的标识符。实际配置的标识符集应该是连续的、无间隙的。（Identifier of CsmKey. The actual identifier set configured is continuous and free of any gap.）                                                                   |
|                    +-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                    | 依赖关系（Dependence）            | 无(None)                                                                                                                                                                                                                      |
+--------------------+-----------------------------------+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------+---------------------------------------------------------+
| CsmKeyUsePort      | 取值范围（Value range）           | TRUE/FALSE                                                                                 | 默认取值（Default value）                                              | FALSE                                                   |
|                    +-----------------------------------+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------+---------------------------------------------------------+
|                    | 参数描述（Parameter description） | Key需要RTE接口吗? True：此键使用的RTE接口；False：此键没有使用RTE接口（Does Key require RTE interface?True: RTE interface is used for this key；False: RTE interface is not used for this key）                               |
|                    +-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                    | 依赖关系（Dependence）            | 无(None)                                                                                                                                                                                                                      |
+--------------------+-----------------------------------+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------+---------------------------------------------------------+
| CsmKeyRef          | 取值范围（Value range）           | 无（None）                                                                                 | 默认取值（Default value）                                              | 无（None）                                              |
|                    +-----------------------------------+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------+---------------------------------------------------------+
|                    | 参数描述（Parameter description） | 此参数引用所使用的CryIfKey。底层的CryIfKey指的是加密驱动程序中的一个特定的加密密钥。（CryIfKey used is referenced for this parameter. The underlying CryIfKey refers to a specific encryption key in the encryption driver.） |
|                    +-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                    | 依赖关系（Dependence）            | CryIfKey                                                                                                                                                                                                                      |
+--------------------+-----------------------------------+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------+---------------------------------------------------------+

CsmMainFunction配置 Configuration of CsmMainFunction
------------------------------------------------------------------------------------------------------

配置周期性函数的周期，支持多分区配置，目前源码尚未进行多核验证。

Configure the periodicity of periodic functions and support multi-partition configuration. The source code has not undergone multi-core validation yet.


.. figure:: ../../../_static/参考手册/CsM/CsmMainFunction.png
   :alt:  CsmMainFunction配置图 (CsmMainFunction Configuration Diagram)
   :name: fig_CsmMainFunction
   :align: center

   fig_CsmMainFunction

.. table::CsmMainFunction通用配置属性(CsmMainFunction general configuration attribute)
    :name: Grid_CsmMainFunction

+-----------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| UI 名称（UI name）          | 描述（Description）                                                                                                                                                                                                               |
+-----------------------------+-----------------------------------+----------------------------------------------------------------------------------+-------------------------------------------------------------+----------------------------------------------+
| CsmMainFunctionPeriod       | 取值范围（Value range）           | 0 .. INF                                                                         | 默认取值（Default value）                                   | 0.01                                         |
|                             +-----------------------------------+----------------------------------------------------------------------------------+-------------------------------------------------------------+----------------------------------------------+
|                             | 参数描述（Parameter description） | 配置CSM模块周期性函数的周期。（Configure the periodicity of periodic function of CSM module. ）                                                                                               |
|                             +-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                             | 依赖关系（Dependence）            | 无(None)                                                                                                                                                                                      |
+-----------------------------+-----------------------------------+----------------------------------------------------------------------------------+-------------------------------------------------------------+----------------------------------------------+
| CsmMainFunctionPartitionRef | 取值范围（Value range）           | 无（None）                                                                       | 默认取值（Default value）                                   | 无（None）                                   |
|                             +-----------------------------------+----------------------------------------------------------------------------------+-------------------------------------------------------------+----------------------------------------------+
|                             | 参数描述（Parameter description） | CSM模块周期性函数所在的分区信息。（The partition information where the periodic function of CSM module is located.）                                                                          |
|                             +-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                             | 依赖关系（Dependence）            | 需要存在分区信息（Partition information is required）                                                                                                                                         |
+-----------------------------+-----------------------------------+----------------------------------------------------------------------------------+-------------------------------------------------------------+----------------------------------------------+

CsmPrimitives配置 Configuration of CsmPrimitives
------------------------------------------------------------------------------------------------------

.. figure:: ../../../_static/参考手册/CsM/CsmPrimitives.png
   :alt:  CsmPrimitives配置图 (CsmPrimitives Configuration Diagram)
   :name: fig_CsmPrimitives
   :align: center

   fig_CsmPrimitives

.. table::CsmPrimitives通用配置属性(CsmPrimitives general configuration attribute)
    :name: Grid_CsmPrimitives

CsmQueues配置 Configuration of CsmQueues
------------------------------------------------------------------

.. figure:: ../../../_static/参考手册/CsM/CsmQueues.png
   :alt:  CsmQueues配置图 (CsmQueues Configuration Diagram)
   :name: fig_CsmQueues
   :align: center

   fig_CsmQueues

.. table::CsmQueues通用配置属性(CsmQueues general configuration attribute)
    :name: Grid_CsmQueues

+--------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| UI 名称（UI name） | 描述（Description）                                                                                                                                                                                                                                                                                                                                           |
+--------------------+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------+
| CsmQueueSize       | 取值范围（Value range）           | 1..4294967295                                                                                                            | 默认取值（Default value）                                                                             | 无（None）                                                                             |
|                    +-----------------------------------+--------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------+
|                    | 参数描述（Parameter description） | CsmQueue的大小。如果由于硬件繁忙而无法由底层硬件处理job，则job将保留在优先队列中。如果队列已满，则将拒绝下一个job。（Size of CsmQueue. If job cannot be processed by the underlying hardware due to hardware's busy schedule, the job will remain in the priority queue.Next job will be refused if the queue is full. ） |
|                    +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                    | 依赖关系（Dependence）            | 无(None)                                                                                                                                                                                                                                                                                                                  |
+--------------------+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------+
| CsmChannelRef      | 取值范围（Value range）           | 无（None）                                                                                                               | 默认取值（Default value）                                                                             | 无（None）                                                                             |
|                    +-----------------------------------+--------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------+
|                    | 参数描述（Parameter description） | 指底层的密码接口通道（efers to the underlying password interface channel）                                                                                                                                                                                                                                                |
|                    +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                    | 依赖关系（Dependence）            | CryIfChannel                                                                                                                                                                                                                                                                                                              |
+--------------------+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------+