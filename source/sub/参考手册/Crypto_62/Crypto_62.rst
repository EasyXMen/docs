====================
Crypto_62
====================

文档信息 Document Information
============================================================

版本历史 Version History
--------------------------------------------------------------------------------------------------------

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
--------------------------------------------------------------------------------------------------------

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
     - AUTOSAR_CP_SWS_CryptoDriver.pdf
     - R23-11 



术语与简写 Terms and Abbreviations
====================================================================


术语 Terms
--------------------------------------------------------------------------------------------------------

.. list-table::
   :widths: 10 40
   :header-rows: 1

   * - 术语(Terms)
     - 解释(Explanation)

   * - Crypto Driver Object
     - Crypto Driver实现一个或多个Crypto Driver Object。Crypto Driver Object可通过硬件或软件提供不同的crypto primitive。同一Crypto Driver下的各个Crypto Driver Object彼此独立。每个Crypto Driver Object仅拥有一个workspace（即同一时间只能执行一个 crypto primitive）。(Crypto Driver realizes one or more Crypto Driver Objects.) The Crypto Driver Object can provide different crypto primitives via either hardware or software. Each Crypto Driver Object under the same Crypto Driver is independent from each other. Each Crypto Driver Object has one workspace only (i.e. only one crypto primitive can be executed each time).

   * - Key
     - Key可由Csm中的job进行引用。在Crypto Driver中，该Key指向特定的key type。(Key can be referenced by job in Csm.) In Crypto Driver, this key points to the specific key type.

   * - Key Type 
     - key type由key element构成，且指向这些key element。通常，key type由Crypto Driver的供应商预先配置。(The key type consists of key elements and points to these key elements.) The key type is generally pre-configured by the supplier of the Crypto Driver.

   * - Key Element 
     - Key element用于存储数据。此类数据例如可以是密钥材料（key material），或是AES加密所需的初始向量（IV）；Key element还可用于配置密钥管理功能（key management functions）的行为。不同Key对应的Key element拥有不同的存储区域（包括非易失性存储区NV和随机存取存储区RAM）。(The key element is used for storing data.) This type of data can be key material or the initial vector (IV) required for AES encryption; furthermore, the Key elements can also be used for configuring the behavior of key management functions. The Key elements corresponding to different keys have different storage areas (including non-volatile memory NV and random access memory RAM).

   * - Job
     - Job是已完成配置的 “CsmJob”。其中，Job会引用key、cryptographic primitive 以及reference channel等要素。(Job refers to the configured 'CsmJob'.) To be specific, Job will reference elements such as key, cryptographic primitive, and reference channel. 

   * - Channel
     - channel是从Crypto Service Manager队列经Crypto Interface到特定Crypto Driver Object的路径。(Channel is the path from the Crypto Service Manager queue to a specific Crypto Driver Object via the Crypto Interface.)  
   
   * - Primitive
     - primitive是在Crypto Driver Object中实现的、已配置的加密算法（cryptographic algorithm）的实例。其中，primitive会引用CSM提供给应用的功能、具体的底层 “algorithmfamily”（如 AES、MD5、RSA等）以及 “algorithmmode”（如 ECB、CBC等）。(primitive is an instance of a configured cryptographic algorithm realized in the Crypto Driver Object.) To be specific, primitive will reference the functions provided by CSM for the application, the specific underlying "algorithm family" (such as AES, MD5, RSA, etc.), and "algorithm mod" (such as ECB, CBC, etc.).

   * - Operation
     - crypto primitive的操作（operation）用于声明应执行该加密原语的哪部分功能。存在三种不同的操作类型：(The operation of crypto primitive is used for declaring the specific part of the function of the encryption primitive that should be executed) There're three different operation types:

   * - START
     - Operation表示一个新的crypto primitive请求，它应取消所有先前的请求，执行必要的初始化，并检查该加密原语是否可被处理。(Operation refers to a new crypto primitive request that should cancel all previous requests, perform necessary initialization, and check if the encryption primitive can be processed.)

   * - UPDATE
     - Operation表示crypto primitive需要输入数据。更新操作（update operation）可提供中间结果。(Operation means that crypto primitive needs data inputting.) The update operation can provide intermediate results.

   * - FINISH
     - Operation表示，至此所有数据已完全输入，crypto primitive可完成最终计算。完成操作（finish operation）可提供最终结果。(Operation means that all data has been fully inputted, and crypto primitive can complete the final calculation.) The finish operation can provide the final results.

   * - Priority
     - job的priority定义了其重要程度。priority数值越高，job的执行就越紧急。cryptographic job的priority是配置的一部分。(The priority of job defines its level of importance.) The higher the priority value, the more urgent the job execution. The priority of cryptographic jobs is part of the configuration.
 
   * - Service
     - service应按照《TR_Glossary》文档中的定义理解：service是一种operation类型，其接口（interface）和行为（behavior）具有公开的规范（published specification），涉及能力提供者（provider of the capability）与潜在客户端（potential clients）之间的约定（contract）。(Service should be understood according to the definition in the TR_Glossary file: Service refers to an operation type, the interface and behavior of which have published specifications. It involves the contract between providers of the capability and potential clients.)



简写 Abbreviations
--------------------------------------------------------------------------------------------------------

.. list-table::
   :widths: 10 20 30
   :header-rows: 1


   * - 简写(Abbreviation)
     - 全称(Full name)
     - 解释(Explanation)
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
==================================

在AUTOSAR加密协议栈中，Crypto Driver处于最底层，为加密功能的最终处理模块。Crypto Driver会执行上层下发的算法任务，计算完成后把结果通过回调函数的方式通知到上层模块。加密算法可通过软件或者硬件HSM模块实现。在本文档中Crypto Driver主要指为软件方式实现的加密算法。

The Crypto Driver is at the bottom layer in the AUTOSAR encryption protocol stack, and serves as the final processing module for encryption functions. The Crypto Driver executes the algorithm tasks from the upper layer, and notifies the upper layer module of the results through callback functions after calculation is completed. The encryption algorithm can be implemented through software or hardware HSM modules. In this file, Crypto Driver mainly refers to encryption algorithms realized by software.

Crypto Driver能够向上层提供多种加密算法，如散列算法SHA、对称加密AES、非对称加密RSA以及随机数生成等。

Crypto Driver can provide several encryption algorithms for the upper layer, such as hash algorithm SHA, symmetric encryption AES, asymmetric encryption RSA, and random number generation.

    .. figure:: ../../../_static/参考手册/Crypto_62/Architecture.png
        :alt: Architecture描述(Architecture Description)
        :name: fig_Architecture
        :align: center


功能描述 Functional Description
==========================================================


特性 Features
----------------------------------------------------------------------------------------------------

1.密钥管理

1.Key management

秘钥功能主要就是涉及到秘钥的保存与获取，包括公钥和私钥的生成等。秘钥通过Crypto_KeyElementSet把Key Element设置到内部Ram中，然后通过调用Crypto_KeySetValid把指定的key设置为有效。

The key function mainly includes the storage and retrieval of keys, including the generation of public and private keys. The key sets Key Element inside Ram through Crypto_KeyElementSet, and then sets the specified key valid by calling Crypto_KeySetValid. 

秘钥功能首先需要在Crypto中配置CryptoKeys，然后配置CryptoKeys->CryptoKeyTypes->CryptoKeyElements，不同的算法所需要的的Key Elements是不一样的，可参考[SWS_Csm_01022]规范，如下图：

To realize key function, first, configure CryptoKeys in Crypto, and then configure CryptoKeys->CryptoKeyTypes->CryptoKeyElements. Key Elements required for different algorithms are different (please refer to the [WS_Csm-01022] specification, as shown in the following figure:)
   
.. figure:: ../../../_static/参考手册/Crypto_62/KeyElement.png
    :alt: KeyElement描述(KeyElement Description)
    :name: fig_KeyElement
    :align: center

如MAC所示，使用时就可以配置3个KeyElement，分别为CRYPTO_KE_MAC_KEY（1），CRYPTO_KE_MAC_PROOF（2）以及CRYPTO_KE_KEYGENERATE_SEED（16）。

As shown in MAC, 3 KeyElement can be configured for use, including CRYPTO_KE_MAC_KEY (1), CRYPTO_KE_MAC_PROOF (2) and CRYPTO_KE_KEYGENERATE_SEED (16).


2.加密算法支持

2.Encryption algorithm supported
   

2.1HASH算法

2.1HASH algorithm

HASH（哈希）算法为不需要秘钥的算法，哈希算法又称杂凑算法，能将一定长度的消息计算出固定长度的字符串（又称消息摘要）。SHA包含11个算法，分别是SHA-1、SHA2-224、SHA2-256、SHA2-384,SHA2-512，SHA3-224、SHA3-256、SHA3-384和SHA3-512,SM3,RIPEMD160。SHA-1最大计算明文长度为2^64bit，属于分组算法，分组长度为512bit，产生的信息摘要长度为160bit，也就是20个字节。

The HASH algorithm requires no secret key. It can calculate a fixed length string (also known as message digest) from a certain length of message. SHA includes 11 algorithms, including SHA-1, SHA2-224, SHA2-256, SHA2-384,SHA2-512，SHA3-224, SHA3-256, SHA3-384, SHA3-512,SM3 and RIPEMD160. With a maximum plaintext length of 2^64 bits, SHA-1 belongs to the group algorithm. The group length is 512 bits, and the generated information digest length is 160 bits or 20 bytes.
   
       .. figure:: ../../../_static/参考手册/Crypto_62/Hash.png
        :alt: Hash描述(Hash Description)
        :name: fig_Hash
        :align: center

2.2MAC算法

2.2MAC algorithm
      
MAC算法， SecOc比较常使用的算法，即带秘密密钥的Hash算法。消息的散列值由只有通信双方知道的秘钥K来控制。此时Hash值称作MAC。先对报文第一个64bit加密，得到64bit的加密后数据data1，接着再拿加密后的data1与报文第二个64bit数据进行按位异或，得到同样长64bit的数据data2，再用Key对data2加密，得到加密后的数据data3，再拿data3与报文第三个64bit数据进行按位异或，同样的处理依次类推，直到最后会得到一个64bit的数据，这个算法就叫做MAC算法。

MAC algorithm, a commonly used algorithm in SecOc, refers to the Hash algorithm with a secret key. The hash value of message is controlled by a secret key K known by the parties in communication parties only. In such case, Hash is called MAC. First, encrypt the first 64 bits of the message to obtain the encrypted data 1 of the 64 bits. Then, perform bitwise XOR between the encrypted data 1 and the second 64 bit data of the message to obtain the data 2 of the 64 bits with the same length. Encrypt data 2 with Key to obtain the encrypted data 3. Finally, perform bitwise XOR between data 3 and the third 64 bit data of the message, and do the rest in the same manner until a 64 bit data is obtained. This algorithm is called the MAC algorithm.
   


2.3AES算法

2.3AES algorithm
     
AES的处理单位是字节，128位的输入明文分组P和输入密钥K都被分成16个字节，分别记为P = P0 P1 … P15 和 K = K0 K1 … K15。如，明文分组为P = abcdefghijklmnop，其中的字符a对应P0，p对应P15。一般地，明文分组用字节为单位的正方形矩阵描述，称为状态矩阵。在算法的每一轮中，状态矩阵的内容不断发生变化，最后的结果作为密文输出。

The processing unit of AES is byte. The 128 bit input plaintext packet P and input key K are divided into 16 bytes, which are recorded as P=P0 P1... P15 and K=K0 K1... K15, respectively. For example, the plaintext is grouped as P = abcdefghijklmnop, where the character a corresponds to P0 and p corresponds to P15. General speaking, the plaintext grouping is described by a square matrix, the unit of which is byte, which is called state matrix. In each round of the algorithm, the content of the state matrix constantly changes, and the final result is output as ciphertext.
   
      .. figure:: ../../../_static/参考手册/Crypto_62/AES.png
        :alt: AES描述(AES Description)
        :name: fig_AES
        :align: center

2.4RSA算法

2.4RSA algorithm
      
非对称加密指双方用不同的KEY加密和解密明文，通信双方都要有自己公共密钥和私有密钥。举个例子比较容易理解，我们们假设通信双方分别是A,B。A拥有KEY_A1（私钥），KEY_A2（公钥）。B拥有KEY_B1（私钥）,KEY_B2（公钥）。公钥和私钥的特点是，经过其中任何一把加密过的明文，只能用另外一把才能够解开。也就是说经过KEY_A1加密过的明文，只有KEY_A2才能够解密，反之亦然。

The asymmetric encryption means encrypting and decrypting plaintext using different KEYS. Both parties in communication have their own public and private keys. It can be understood easier by an example. Suppose the parties in communication are A and B, A has KEY_A1 (private key) and KEY_A2 (public key). B has KEY_B1 (private key) and KEY_B2 (public key). The characteristic of public and private keys is that plaintext encrypted by either one can only be decrypted by the other. In other words, the plaintext encrypted by KEY_A1 can only be decrypted by KEY_A2, and vice versa.



3.队列功能

3.Queue function


由于软件加密算法可能比较耗时，所以个别的算法可以配置为异步模式，即把内容传给下层后，下层不会直接运算，而是会根据下层的功能机制，在后续的mainfunction中对加密任务进行计算，并通过回调函数返回给上层。

As the software encryption algorithm may cost a lot of time, some algorithms can be configured in asynchronous mode, which means transmitting the content to the lower layer. Instead of performing calculation directly, the lower layer will calculate the encryption task in the subsequent mainfunction based on the function mechanism of lower layer and return it to the upper layer through a callback function.

由于异步加密任务可能存在延迟，例如未完成一次计算，又传入了很多其它的加密任务，这时可以启用队列功能。队列功能打开后，便可以同时缓存多个加密任务，每次在Crypto_Mainfunction中去依次执行缓存队列中的加密任务。

As asynchronous encryption task may be delayed, such as the failure in finishing calculation and transmission of many other encryption tasks, the queue function can be enabled. After the queue function is enabled, several encryption tasks can be cached at the same time. During each time, the encryption tasks in the cache queue are executed sequentially in Crypto_Sainfunction.

通过配置项CryptoQueueSize定义队列大小。CSM和Crypto Driver中均可定义队列，两者的功能大体一致，一般情况下是两者选其一即可。

The queue size is defined through the configuration item CryptoQueueSize. Both CSM and Crypto Driver can define queues and basically have the same functions. Either of them is required in general.

偏差 Deviation
--------------------------------------------------------------------
其他SWS支持的算法正在逐步移植开发中.

Other algorithms supported by SWS are under transplantation and development.

扩展 Extension
--------------------------------------------------------------------
None


集成 Integration
========================================

文件列表 File List
--------------------------------------------------------------------

.. figure:: ../../../_static/参考手册/Crypto_62/filelist.png
   :alt: Crypto_62组件文件组织结构描述(Description of Crypto_62 organization file organization structure)
   :name: fig_Crypto_62Filelist
   :align: center

   Crypto_62组件文件组织结构描述. (Description of Crypto_62 organization file organization structure.)

如图  :ref:`fig_Crypto_62Filelist` 所示，Crypto_62模块的文件引用关系如下：

As shown in the figure :ref:`fig_Crypto_62Filelist`, the file reference relationship of the Crypto_62 module is as follows:

静态文件 Static Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

None

动态文件 Dynamic Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. list-table::
      :widths: 10 30
      :header-rows: 1

      * - 文件(File)
        - 描述(Description)
      
      * - Crypto_62_Cfg.h
        - 定义Crypto Driver模块预编译时用到的配置参数。(Defines the configuration parameters used for pre-compiling the Crypto Driver module.)

      * - Crypto_62_Cfg.c
        - 定义Crypto Driver模块中PC配置参数。(Defines the configuration parameters of PC in the Crypto Driver module.)

      * - Crypto_62.h
        - Crypto_62模块头文件，包含了API函数的扩展声明并定义了端口的数据结构。(The Crypto_62 module header file contains extension declarations for API functions and defines the data structure of port.)

      * - Crypto_62.c
        - Crypto_62模块源文件，包含了外部API函数的实现。(The Crypto_62 module source file, which contains the realization of external API functions.)

      * - Crypto_62_internal.c
        - 定义内部函数的实现，如查找配置，缓存拷贝等.(-Define the realization of internal functions, such as searching configurations, caching copies, etc)

      * - Crypto_62_internal.h
        - 定义内部数据结构，内部函数声明等.(Defines internal data structures, internal function declarations, etc.)

      * - Crypto_62_Types.h
        - 定义规范中定义的数据结构等.(Defines the data structure, etc. defined in the specification)

      * - Crypto_MemMap.h
        - 定义数据、代码所用的Memmap段。(Defines the Memmap segment used for data and code.)
      
      * - Crypto_62_KeyManagerment.c
        - 包含了Crypto_62模块中密钥管理部分API函数的实现。(Contains the realization of API functions for key management in the Crypto_62 module.)


错误处理 Error Handling
------------------------------------------------------------------------

开发错误 Development Errors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. list-table:: 
      :widths: 20 10 30
      :header-rows: 1

      * - Error code
        - Value[hex]
        - Description

      * - CRYPTO_E_UNINIT 
        - 0x00
        - API request called before initialization of CryptoDriver.

      * - CRYPTO_E_INIT_FAILED 
        - 0x01
        - Initialization of Crypto Driver failed 

      * - CRYPTO_E_PARAM_POINTER  
        - 0x02
        - API request called with invalid parameter(Nullpointer without redirection).

      * - CRYPTO_E_PARAM_HANDLE
        - 0x04
        - API request called with invalid parameter (out ofrange).

      * - CRYPTO_E_PARAM_VALUE 
        - 0x05
        - API request called with invalid parameter (invalidvalue).

      * - CRYPTO_E_SMALL_BUFFER 
        - 0x06
        - Buffer is too small for operation 

产品错误 Product Errors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
None


运行时错误 Runtime Errors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    .. list-table:: 
      :widths: 20 10 30
      :header-rows: 1

      * - Error code
        - Value[hex]
        - Description

      * - CRYPTO_E_RE_ENTROPY_EXHAUSTED 
        - 0x03
        - Entropy is too low 

      * - CRYPTO_E_RE_NVM_ACCESS_FAILED 
        - 0x04
        - NVM access has failed 
    


应用程序集成 Application Integration
------------------------------------------------------------------------------------------------------------

1.依赖模块

1.Dependency module

CryptoDriver作为最底层驱动模块，其依赖模块可以为空。当需要存储秘钥等信息时，需要依赖NVM模块。

CryptoDriver is the lowest underlying driver module, whose dependency modules can be empty. Use NVM module when storing keys and other information.

.. include:: Crypto_62_h_api.rst
.. include:: Crypto_62_Internal_h_api.rst
.. include:: Crypto_62_Types_h_api.rst


配置 Configuration
====================================


通用配置 General Configurations
----------------------------------------------------------------------------------------

在CryptoGeneral配置界面中进行一些类似于DET开关的配置，版本号开关，分区信息等，建议优先配置这里。

In the CryptoGeneral configuration interface, perform some configurations similar to DET switches, version number switches, partition information, etc. It is recommended to prioritize the configuration here.

.. figure:: ../../../_static/参考手册/Crypto_62/CryptoGeneral.png
   :alt:  CryptoGeneral配置图 (CryptoGeneral Configuration Diagram)
   :name: fig_CryptoGeneral
   :align: center

   CryptoGeneral配置图 (CryptoGeneral Configuration Diagram)

.. table::CryptoGeneral通用配置属性(CryptoGeneral general configuration attribute)
    :name: Grid_CryptoGeneral

+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| UI 名称（UI name）       | 描述（Description）                                                                                                                                                                                                                                                                      |
+--------------------------+-----------------------------------+-------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+---------------------------------------------------------------+
| CryptoDevErrorDetect     | 取值范围（Value range）           | TRUE/FALSE                                                                                            | 默认取值（Default value）                                                    | FALSE                                                         |
|                          +-----------------------------------+-------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+---------------------------------------------------------------+
|                          | 参数描述（Parameter description） | 是否使能开发错误检查（Enable development error detection or not）                                                                                                                                                                                    |
|                          +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                          | 依赖关系（Dependence）            | 无（None）                                                                                                                                                                                                                                           |
+--------------------------+-----------------------------------+-------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+---------------------------------------------------------------+
| CryptoInstanceId         | 取值范围（Value range）           | 0..255                                                                                                | 默认取值（Default value）                                                    | 无（None）                                                    |
|                          +-----------------------------------+-------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+---------------------------------------------------------------+
|                          | 参数描述（Parameter description） | 加密驱动程序的实例ID，此ID用于识别多个加密驱动程序，以防在同一ECU中使用多个加密驱动（The instance ID of encryption driver; it is used for identifying several encryption drivers to prevent the use of multiple encryption drivers in the same ECU） |
|                          +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                          | 依赖关系（Dependence）            | 无（None）                                                                                                                                                                                                                                           |
+--------------------------+-----------------------------------+-------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+---------------------------------------------------------------+
| CryptoMainFunctionPeriod | 取值范围（Value range）           | 0..INF                                                                                                | 默认取值（Default value）                                                    | 无（None）                                                    |
|                          +-----------------------------------+-------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+---------------------------------------------------------------+
|                          | 参数描述（Parameter description） | 表示调用Crypto_MainFunction的周期（It indicates the cycle of calling Crypto_MainFunction）                                                                                                                                                           |
|                          +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                          | 依赖关系（Dependence）            | 无（None）                                                                                                                                                                                                                                           |
+--------------------------+-----------------------------------+-------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+---------------------------------------------------------------+
| CryptoVersionInfoApi     | 取值范围（Value range）           | TRUE/FALSE                                                                                            | 默认取值（Default value）                                                    | FALSE                                                         |
|                          +-----------------------------------+-------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+---------------------------------------------------------------+
|                          | 参数描述（Parameter description） | 表示是否使能版本获取API（It indicates whether to enable version to get API）                                                                                                                                                                         |
|                          +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                          | 依赖关系（Dependence）            | 无（None）                                                                                                                                                                                                                                           |
+--------------------------+-----------------------------------+-------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+---------------------------------------------------------------+
| CryptoEcucPartitionRef   | 取值范围（Value range）           | 引用到EcucPartition（Reference to EcucPartition）                                                     | 默认取值（Default value）                                                    | 无（None）                                                    |
|                          +-----------------------------------+-------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+---------------------------------------------------------------+
|                          | 参数描述（Parameter description） | 映射Crypto驱动到partition（Map Crypto driver to partition）                                                                                                                                                                                          |
|                          +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                          | 依赖关系（Dependence）            | 仅存在于多核多分区系统中（Existing in multi-core multi-partition system only）                                                                                                                                                                       |
+--------------------------+-----------------------------------+-------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+---------------------------------------------------------------+

秘钥配置 Key Configuration
----------------------------------------------------------------------------------------

大部分加密算法是需要使用到秘钥的，所以第一步需要配置秘钥，先创建秘钥元素，然后配置秘钥元素组合成秘钥组即keytype。按照秘钥组的使用方式进行配置秘钥，同一个keytype可以配置多个秘钥元素，如果需要安全存储秘钥到NVM的话需要依赖NVM模块配置block。

Key is required by a majority of encryption algorithms. In the first step, configure the key: Create key elements, and then combine them into a key group, which is keytype. Configure key according to the use method of the key group. Multiple key elements can be configured for one keytype. If the key needs securely storing to NVM, configure block via NVM module.

.. figure:: ../../../_static/参考手册/Crypto_62/CryptoKeyElements.png
   :alt:  CryptoKeyElements配置图 (CryptoKeyElements Configuration Diagram)
   :name: fig_CryptoKeyElements
   :align: center

   CryptoKeyElements配置图 (CryptoKeyElements Configuration Diagram)

.. table::CryptoKeyElements通用配置属性(CryptoKeyElements general configuration attribute)
        :name: Grid_CryptoKeyElements


+------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| UI 名称（UI name）                 | 描述（Description）                                                                                                                                                                                                                                                                    |
+------------------------------------+-----------------------------------+-------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
| CryptoKeyElementAllowPartialAccess | 取值范围（Value range）           | TRUE/FALSE                                                                          | 默认取值（Default value）                                                            | 无（None）                                                            |
|                                    +-----------------------------------+-------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
|                                    | 参数描述（Parameter description） | 表示此KeyElement是否允许被局部访问，访问的长度小于CryptoKeyElementSize配置的长度（It indicates whether this KeyElement is allowed to be accessed locally, and that the length of the access is less than that configured by CryptoKeyElementSize） |
|                                    +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                    | 依赖关系（Dependence）            | 无（None）                                                                                                                                                                                                                                         |
+------------------------------------+-----------------------------------+-------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
| CryptoKeyElementFormat             | 取值范围（Value range）           | 无（None）                                                                          | 默认取值（Default value）                                                            | 无（None）                                                            |
|                                    +-----------------------------------+-------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
|                                    | 参数描述（Parameter description） | 定义KeyElement的格式（Define the format of KeyElement）                                                                                                                                                                                            |
|                                    +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                    | 依赖关系（Dependence）            | 无（None）                                                                                                                                                                                                                                         |
+------------------------------------+-----------------------------------+-------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
| CryptoKeyElementId                 | 取值范围（Value range）           | Uint32                                                                              | 默认取值（Default value）                                                            | 无（None）                                                            |
|                                    +-----------------------------------+-------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
|                                    | 参数描述（Parameter description） | 定义KeyElement的索引（Define the index of KeyElement ）                                                                                                                                                                                            |
|                                    +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                    | 依赖关系（Dependence）            | ID值依赖于算法，如MAC算法可配置ID分别为1,2,16（The ID value depends on the algorithm; for example, the MAC algorithm can configure IDs as 1, 2, and 16 respectively）                                                                              |
+------------------------------------+-----------------------------------+-------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
| CryptoKeyElementInitValue          | 取值范围（Value range）           | 无（None）                                                                          | 默认取值（Default value）                                                            | 无（None）                                                            |
|                                    +-----------------------------------+-------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
|                                    | 参数描述（Parameter description） | 用于startup时填充key element初始值（Used for filling in the initial value of key element during startup）                                                                                                                                          |
|                                    +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                    | 依赖关系（Dependence）            | 仅适用于RAM Key，ROM key存在NVRAM中，无法被修改（CryptoKeyElementPersist = FALSE）（Applicable to RAM Key, ROM key in NVRAM only, cannot be modified (CryptoKeyElementPersist = FALSE)）                                                           |
+------------------------------------+-----------------------------------+-------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
| CryptoKeyElementPersist            | 取值范围（Value range）           | TRUE/FALSE                                                                          | 默认取值（Default value）                                                            | FALSE                                                                 |
|                                    +-----------------------------------+-------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
|                                    | 参数描述（Parameter description） | 表示是否需要将此key element存储到NVRAM（It indicates whether to store this key                                                                                                                                                                     |
|                                    +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                    | 依赖关系（Dependence）            | 无（None）                                                                                                                                                                                                                                         |
+------------------------------------+-----------------------------------+-------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
| CryptoKeyElementReadAccess         | 取值范围（Value range）           | CRYPTO_RA_ALLOWED                                                                   | 默认取值（Default value）                                                            | 无（None）                                                            |
|                                    |                                   +-------------------------------------------------------------------------------------+                                                                                      |                                                                       |
|                                    |                                   | CRYPTO_RA_DENIED                                                                    |                                                                                      |                                                                       |
|                                    |                                   +-------------------------------------------------------------------------------------+                                                                                      |                                                                       |
|                                    |                                   | CRYPTO_RA_ENCRYPTED                                                                 |                                                                                      |                                                                       |
|                                    |                                   +-------------------------------------------------------------------------------------+                                                                                      |                                                                       |
|                                    |                                   | CRYPTO_RA_INTERNAL_COPY                                                             |                                                                                      |                                                                       |
|                                    +-----------------------------------+-------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
|                                    | 参数描述（Parameter description） | 定义此Key element的访问权限（Define the access permission of this Key element）                                                                                                                                                                    |
|                                    +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                    | 依赖关系（Dependence）            | 无（None）                                                                                                                                                                                                                                         |
+------------------------------------+-----------------------------------+-------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
| CryptoKeyElementSize               | 取值范围（Value range）           | Uint32                                                                              | 默认取值（Default value）                                                            | 无（None）                                                            |
|                                    +-----------------------------------+-------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
|                                    | 参数描述（Parameter description） | 定义此key element的长度（Define the length of key element ）                                                                                                                                                                                       |
|                                    +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                    | 依赖关系（Dependence）            | 无（None）                                                                                                                                                                                                                                         |
+------------------------------------+-----------------------------------+-------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
| CryptoKeyElementWriteAccess        | 取值范围（Value range）           | CRYPTO_WA_ALLOWED                                                                   | 默认取值（Default value）                                                            | 无（None）                                                            |
|                                    |                                   +-------------------------------------------------------------------------------------+                                                                                      |                                                                       |
|                                    |                                   | CRYPTO_WA_DENIED                                                                    |                                                                                      |                                                                       |
|                                    |                                   +-------------------------------------------------------------------------------------+                                                                                      |                                                                       |
|                                    |                                   | CRYPTO_WA_ENCRYPTED                                                                 |                                                                                      |                                                                       |
|                                    |                                   +-------------------------------------------------------------------------------------+                                                                                      |                                                                       |
|                                    |                                   | CRYPTO_WA_INTERNAL_COPY                                                             |                                                                                      |                                                                       |
|                                    +-----------------------------------+-------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
|                                    | 参数描述（Parameter description） | 定义此Key element的写权限（Define the writing permission of this Key element）                                                                                                                                                                     |
|                                    +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                    | 依赖关系（Dependence）            | 无（None）                                                                                                                                                                                                                                         |
+------------------------------------+-----------------------------------+-------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------+-----------------------------------------------------------------------+

.. figure:: ../../../_static/参考手册/Crypto_62/CryptoKeyTypes.png
   :alt:  CryptoKeyTypes配置图 (CryptoKeyTypes Configuration Diagram)
   :name: fig_CryptoKeyTypes
   :align: center

   CryptoKeyTypes配置图 (CryptoKeyTypes Configuration Diagram)

.. table::CryptoKeyTypes通用配置属性(CryptoKeyTypes general configuration attribute)
        :name: Grid_CryptoKeyTypes

+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| UI 名称（UI name）  | 描述（Description）                                                                                                                                  |
+---------------------+-----------------------------------+--------------------------------------------------------------+---------------------------------+-----------------+
| CryptoKeyElementRef | 取值范围（Value range）           | 引用[CryptoKeyElement]（Reference [CryptoKeyElement]）       | 默认取值（Default value）       | 无（None）      |
|                     +-----------------------------------+--------------------------------------------------------------+---------------------------------+-----------------+
|                     | 参数描述（Parameter description） | 表示此CryptoKeyType包含哪些Key element（It indicates the specific Key elements contained by this CryptoKeyType） |
|                     +-----------------------------------+------------------------------------------------------------------------------------------------------------------+
|                     | 依赖关系（Dependence）            | 无（None）                                                                                                       |
+---------------------+-----------------------------------+--------------------------------------------------------------+---------------------------------+-----------------+


.. figure:: ../../../_static/参考手册/Crypto_62/CryptoKey.png
   :alt:  CryptoKey配置图 (CryptoKey Configuration Diagram)
   :name: fig_CryptoKey
   :align: center

   CryptoKey配置图 (CryptoKey Configuration Diagram)

.. table::CryptoKey通用配置属性(CryptoKey general configuration attribute)
        :name: Grid_CryptoKey

+---------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| UI 名称（UI name）  | 描述（Description）                                                                                                                   |
+---------------------+-----------------------------------+------------------------------------------------------+-----------------------------+--------------+
| CryptoKeyId         | 取值范围（Value range）           | Uint32                                               | 默认取值（Default value）   | 无（None）   |
|                     +-----------------------------------+------------------------------------------------------+-----------------------------+--------------+
|                     | 参数描述（Parameter description） | Crypto 秘钥索引（Crypto Key index）                                                               |
|                     +-----------------------------------+---------------------------------------------------------------------------------------------------+
|                     | 依赖关系（Dependence）            | 无（None）                                                                                        |
+---------------------+-----------------------------------+------------------------------------------------------+-----------------------------+--------------+
| CryptoKeyTypeRef    | 取值范围（Value range）           | 引用[CryptoKeyType]（Reference [CryptoKeyType]）     | 默认取值（Default value）   | 无（None）   |
|                     +-----------------------------------+------------------------------------------------------+-----------------------------+--------------+
|                     | 参数描述（Parameter description） | 表示此Crypto Key包含哪些CryptoKeyType（It indicates the CryptoKeyTypes contained in Crypto Key ） |
|                     +-----------------------------------+---------------------------------------------------------------------------------------------------+
|                     | 依赖关系（Dependence）            | 无（None）                                                                                        |
+---------------------+-----------------------------------+------------------------------------------------------+-----------------------------+--------------+
| CryptoKeyNvBlockRef | 取值范围（Value range）           | 引用CryptoKeyNvBlock（Reference CryptoKeyNvBlock）   | 默认取值（Default value）   | 无（None）   |
|                     +-----------------------------------+------------------------------------------------------+-----------------------------+--------------+
|                     | 参数描述（Parameter description） | 表示此Crypto Key关联的Nvblock（It indicates Nvblock linked with this Crypto Key ）                |
|                     +-----------------------------------+---------------------------------------------------------------------------------------------------+
|                     | 依赖关系（Dependence）            | 无（None）                                                                                        |
+---------------------+-----------------------------------+------------------------------------------------------+-----------------------------+--------------+

.. figure:: ../../../_static/参考手册/Crypto_62/CryptoNvStorage.png
   :alt:  CryptoNvStorage配置图 (CryptoNvStorage Configuration Diagram)
   :name: fig_CryptoNvStorage
   :align: center

   CryptoNvStorage配置图 (CryptoNvStorage Configuration Diagram)

.. table::CryptoNvStorage通用配置属性(CryptoNvStorage general configuration attribute)
    :name: Grid_CryptoNvStorage

+----------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| UI 名称（UI name）         | 描述（Description）                                                                                                                 |
+----------------------------+-----------------------------------+--------------------------------------------------------+---------------------------+------------+
| CryptoNvBlockFailedRetries | 取值范围（Value range）           | Uint16                                                 | 默认取值（Default value） | 无（None） |
|                            +-----------------------------------+--------------------------------------------------------+---------------------------+------------+
|                            | 参数描述（Parameter description） | 尝试请求NVM服务的次数（Times of trying to request NVM services）                                |
|                            +-----------------------------------+-------------------------------------------------------------------------------------------------+
|                            | 依赖关系（Dependence）            | 无（None）                                                                                      |
+----------------------------+-----------------------------------+--------------------------------------------------------+---------------------------+------------+
| CryptoNvBlockProcessing    | 取值范围（Value range）           | Enumeration                                            | 默认取值（Default value） | 无（None） |
|                            +-----------------------------------+--------------------------------------------------------+---------------------------+------------+
|                            | 参数描述（Parameter description） | 更新NVM块的时候采取的模式（Mode used for updating NVM block ）                                  |
|                            +-----------------------------------+-------------------------------------------------------------------------------------------------+
|                            | 依赖关系（Dependence）            | 无（None）                                                                                      |
+----------------------------+-----------------------------------+--------------------------------------------------------+---------------------------+------------+
| CryptoNvBlockDescriptorRef | 取值范围（Value range）           | 引用NvMBlockDescriptor（Reference NvMBlockDescriptor） | 默认取值（Default value） | 无（None） |
|                            +-----------------------------------+--------------------------------------------------------+---------------------------+------------+
|                            | 参数描述（Parameter description） | 表示此Crypto Key关联的Nvblock（It indicates Nvblock linked with this Crypto Key ）              |
|                            +-----------------------------------+-------------------------------------------------------------------------------------------------+
|                            | 依赖关系（Dependence）            | 需要NVM配置NvMBlockDescriptor（NVM needs to be configured with NvMBlockDescriptor）             |
+----------------------------+-----------------------------------+--------------------------------------------------------+---------------------------+------------+

加密算法配置 Configuration of Encryption Algorithm
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

这里需要配置加密算法的种类和模式，如加密服务的AES种类下面的ECB模式，用于生成宏定义开关。

The type and mode of encryption algorithm need configuring here, such as the ECB mode under the AES type of encryption service, in order to generate the macro defined switches.

.. figure:: ../../../_static/参考手册/Crypto_62/CryptoPrimitives.png
   :alt:  CryptoPrimitives配置图 (CryptoPrimitives Configuration Diagram)
   :name: fig_CryptoPrimitives
   :align: center

   CryptoPrimitives配置图 (CryptoPrimitives Configuration Diagram)

.. table::CryptoPrimitives通用配置属性(CryptoPrimitives general configuration attribute)
        :name: Grid_CryptoPrimitives

+-----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| UI 名称（UI name）                      | 描述（Description）                                                                                                                             |
+-----------------------------------------+-----------------------------------+--------------------------------+---------------------------------------------+------------------------------+
| CryptoPrimitiveAlgorithmFamily          | 取值范围（Value range）           | Enumeration                    | 默认取值（Default value）                   | 无（None）                   |
|                                         +-----------------------------------+--------------------------------+---------------------------------------------+------------------------------+
|                                         | 参数描述（Parameter description） | 确定用于加密服务的算法系列（Determine the algorithm series used for encryption services）                   |
|                                         +-----------------------------------+-------------------------------------------------------------------------------------------------------------+
|                                         | 依赖关系（Dependence）            | 无（None）                                                                                                  |
+-----------------------------------------+-----------------------------------+--------------------------------+---------------------------------------------+------------------------------+
| CryptoPrimitiveAlgorithmMode            | 取值范围（Value range）           | Enumeration                    | 默认取值（Default value）                   | 无（None）                   |
|                                         +-----------------------------------+--------------------------------+---------------------------------------------+------------------------------+
|                                         | 参数描述（Parameter description） | 确定用于加密服务的算法模式（Determine the algorithm mode used for encryption services）                     |
|                                         +-----------------------------------+-------------------------------------------------------------------------------------------------------------+
|                                         | 依赖关系（Dependence）            | 无（None）                                                                                                  |
+-----------------------------------------+-----------------------------------+--------------------------------+---------------------------------------------+------------------------------+
| CryptoPrimitiveAlgorithmSecondaryFamily | 取值范围（Value range）           | Enumeration                    | 默认取值（Default value）                   | 无（None）                   |
|                                         +-----------------------------------+--------------------------------+---------------------------------------------+------------------------------+
|                                         | 参数描述（Parameter description） | 确定用于加密服务的算法二级系列（Determine the secondary series of algorithms used for encryption services） |
|                                         +-----------------------------------+-------------------------------------------------------------------------------------------------------------+
|                                         | 依赖关系（Dependence）            | 无（None）                                                                                                  |
+-----------------------------------------+-----------------------------------+--------------------------------+---------------------------------------------+------------------------------+
| CryptoPrimitiveService                  | 取值范围（Value range）           | Enumeration                    | 默认取值（Default value）                   | 无（None）                   |
|                                         +-----------------------------------+--------------------------------+---------------------------------------------+------------------------------+
|                                         | 参数描述（Parameter description） | 确定用于定义功能的加密服务（Determine the encryption services used for defining functions）                 |
|                                         +-----------------------------------+-------------------------------------------------------------------------------------------------------------+
|                                         | 依赖关系（Dependence）            | 无（None）                                                                                                  |
+-----------------------------------------+-----------------------------------+--------------------------------+---------------------------------------------+------------------------------+


队列配置Queue Configuration
----------------------------------------------------------------------------------------

加密驱动以Object为单位，可以配置多个Object，每个Object可以配置多个服务，按照队列的形式处理任务。

The encryption driver takes Object as the unit and can configure several objects, each of which can be configured with several services to process tasks in a queue format.


  .. figure:: ../../../_static/参考手册/Crypto_62/CryptoDriverObject.png
    :alt:  CryptoDriverObject配置图 (CryptoDriverObject Configuration Diagram)
    :name: fig_CryptoDriverObject
    :align: center

    CryptoDriverObject配置图 (CryptoDriverObject Configuration Diagram)

.. table::CryptoDriverObject通用配置属性(CryptoDriverObject general configuration attribute)
          :name: Grid_CryptoDriverObject

+------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| UI 名称（UI name）                 | 描述（Description）                                                                                                                                                                  |
+------------------------------------+-----------------------------------+------------------------------------------------------------------------+--------------------------------------------+----------------------------+
| CryptoDriverObjectId               | 取值范围（Value range）           | Uint32                                                                 | 默认取值（Default value）                  | 无（None）                 |
|                                    +-----------------------------------+------------------------------------------------------------------------+--------------------------------------------+----------------------------+
|                                    | 参数描述（Parameter description） | 加密驱动对象ID（Encryption driver object ID）                                                                                                    |
|                                    +-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
|                                    | 依赖关系（Dependence）            | 无（None）                                                                                                                                       |
+------------------------------------+-----------------------------------+------------------------------------------------------------------------+--------------------------------------------+----------------------------+
| CryptoQueueSize                    | 取值范围（Value range）           | Uint32                                                                 | 默认取值（Default value）                  | 无（None）                 |
|                                    +-----------------------------------+------------------------------------------------------------------------+--------------------------------------------+----------------------------+
|                                    | 参数描述（Parameter description） | 定义队列的长度（Define queue length）                                                                                                            |
|                                    +-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
|                                    | 依赖关系（Dependence）            | 无（None）                                                                                                                                       |
+------------------------------------+-----------------------------------+------------------------------------------------------------------------+--------------------------------------------+----------------------------+
| CryptoDefaultRandomKeyRef          | 取值范围（Value range）           | 引用[CryptoKey]（Reference [CryptoKey]）                               | 默认取值（Default value）                  | 无（None）                 |
|                                    +-----------------------------------+------------------------------------------------------------------------+--------------------------------------------+----------------------------+
|                                    | 参数描述（Parameter description） | 密钥包含为随机数生成器提供种子所必需的关键元素（The key contains the key elements required for providing seeds for the random number generator） |
|                                    +-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
|                                    | 依赖关系（Dependence）            | 无（None）                                                                                                                                       |
+------------------------------------+-----------------------------------+------------------------------------------------------------------------+--------------------------------------------+----------------------------+
| CryptoDefaultRandomPrimitiveRef    | 取值范围（Value range）           | 引用[CryptoPrimitive]（Reference [CryptoPrimitive]）                   | 默认取值（Default value）                  | 无（None）                 |
|                                    +-----------------------------------+------------------------------------------------------------------------+--------------------------------------------+----------------------------+
|                                    | 参数描述（Parameter description） | 对配置默认随机数生成器的原语的引用（Reference the primitive for configuring the default random number generator）                                |
|                                    +-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
|                                    | 依赖关系（Dependence）            | 无（None）                                                                                                                                       |
+------------------------------------+-----------------------------------+------------------------------------------------------------------------+--------------------------------------------+----------------------------+
| CryptoDriverObjectEcucPartitionRef | 取值范围（Value range）           | 引用[EcucPartition]（Reference[EcucPartition]）                        | 默认取值（Default value）                  | 无（None）                 |
|                                    +-----------------------------------+------------------------------------------------------------------------+--------------------------------------------+----------------------------+
|                                    | 参数描述（Parameter description） | 表示此CryptoDriverObject处于哪一个分区中（It indicates the specific partition where this CryptoDriver Object is located）                        |
|                                    +-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
|                                    | 依赖关系（Dependence）            | 仅在多核系统中配置（Configured in multi-core system only）                                                                                       |
+------------------------------------+-----------------------------------+------------------------------------------------------------------------+--------------------------------------------+----------------------------+
| CryptoPrimitiveRef                 | 取值范围（Value range）           | 引用[CryptoPrimitive]（Reference [CryptoPrimitive] ）                  | 默认取值（Default value）                  | 无（None）                 |
|                                    +-----------------------------------+------------------------------------------------------------------------+--------------------------------------------+----------------------------+
|                                    | 参数描述（Parameter description） | 加密服务的预配置（pre-configuration of encryption services）                                                                                     |
|                                    +-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
|                                    | 依赖关系（Dependence）            | 无（None）                                                                                                                                       |
+------------------------------------+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+