====================
MemAcc
====================

文档信息（Document Information）
========================================================================

版本历史（Version History）
----------------------------------------------------------------------------------------------------------------------------

.. list-table::
   :widths: 10 10 10 10 20
   :header-rows: 1

   * - 日期
     - 作者
     - 版本
     - 状态
     - 说明
   * - 2025/08/13
     - peng.wu
     - V0.1
     - 发布(Release)
     - 正式发布(Official release)

   * - 2025/08/30
     - peng.wu
     - V1.0
     - 发布
     - 正式发布

   * - 2025/11/28
     - peng.wu
     - V1.1
     - 修正(Modify)
     - 增加多分区功能的描述(Add the description of multi-partition)

   * - 2025/12/11
     - peng.wu
     - V1.3
     - 修正(Modify)
     - 调整文档架构(Modify the document structure)


参考文档（References）
----------------------------------------------------------------------------------------------------------------------------

.. list-table::
   :widths: 10 10 30 10
   :header-rows: 1

   * - 编号(Number)
     - 分类(Classification)
     - 标题(Title)
     - 版本(Version)
   * - 1
     - Autosar
     - AUTOSAR_CP_SRS_MemoryHWAbstractionLayer.pdf
     - R23-11
   * - 2
     - Autosar
     - AUTOSAR_CP_SWS_MemoryAccess.pdf
     - R23-11


术语与简写（Terms and Abbreviations）
========================================================================

术语（Terms）
----------------------------------------------------------------------------------------------------------------------------
   .. :align: center   表格内容居中(Table contents are centered)

.. list-table::
   :widths: 15 40
   :header-rows: 1

   * - 术语(Term)
     - 解释(Explanation)

   * - Address Area
     - Contiguous memory area in the logical address space Typically multiple physical memory sectors are combined 
       to one logical address area.

   * - Bank
     - Group of sector batches In case a memory technology is segmented in sectors, a bank is an instance of a sector 
       batch group in which no read-while-write operation is permitted. In case of a flash memory device, this
       typically maps to an individual flash controller.

   * - Job Request
     - Memory access request by an upper layer module for an address area.

   * - Memory Device
     - Group of banks

   * - Page Burst
     - Aggregated access of memory pages for improved performance In case a memory device technology has a physical 
       segmentation, some memory devices provide an optimized access method to read or write multiple pages at a time. 
       Page burst denotes the aggregation of memory pages used for the access optimization.

   * - Sector
     - Smallest erasable memory unit (in bytes) Some memory device technologies require an explicit physical erase
       operation before the memory can be written. A sector defines the minimum size of such an erase unit. Depending 
       on the memory device, sectors can be either uniform- or variable-sized.

   * - Sector Batch
     - Aggregation of sectors with uniform size Logical aggregation of contiguous sectors with the same size.

   * - Sector Burst
     - Aggregation of sectors for improved erase performance In case a memory technology needs a physical erase operation,
       some devices provide an erase performance optimization by erasing an aggregation of sectors in one step.

   * - Sub Address Area
     - Contiguous memory area in the logical address space mapped to a sector batch of one memory device.

   * - Write Page
     - Smallest writeable unit of a memory device (in bytes) Some memory device technologies must be accessed considering
       a physical segmentation. Hence a byte-wise access is not possible for all memory device technologies. This term defines
       the minimum size that needs to be written in one access.


简写（Abbreviations）
--------------------------------------------------------------

.. list-table::
   :widths: 10 20 30
   :header-rows: 1

   * - 简写 (Abbreviation)
     - 全称 (Full name)
     - 解释 (Explanation)

   * - BndM
     - Bulk Non-Volatile Data Manager
     - 大数据非易失性数据管理器
   * - ECC
     - Error Correction Code
     - 错误纠错码
   * - FOTA
     - Firmware Over The Air - remote firmware update using wireless communication
     - 无线通信进行远程固件更新
   * - HSM
     - Hardware Security Module - dedicated security MCU core
     - 硬件安全模块
   * - OTA
     - Over The Air - general term for wireless communication betweenOEM backend and vehicle
     - Over The Air是OEM后端与车辆之间无线通信的总称
   * - RWW
     - Read While Write - capability of a memory device to perform a read operation in one 
       memory bank while at the same time a write/erase operation takes place in another bank
     - 写时读-存储设备在一个存储库中执行读操作而同时在另一个存储库中进行写/擦除操作的能力
   * - EEPROM
     - Electrically Erasable and Programmable ROM (Read Only Memory)
     - 电可擦可编程只读存储器(只读型存储器)
   * - SOTA
     - Software Over The Air - remote software update using wireless communication
     - 无线通信的远程软件更新


简介（Introduction）
====================================

MemAcc模块通过基于地址访问的API提供对不同存储技术设备的访问。
MemAcc模块总是包含一个或多个内存驱动程序。MemAcc模块与存储设备技术无关，可与典型的存储设备（如闪存、EEPROM、RAM或相变存储器）一起使用。
MemAcc模块和内存驱动程序与Fls和Eep驱动程序位于AUTOSAR架构的同一层，但将这些模块分为硬件独立部分（MemAcc）和硬件依赖部分（Mem）。

The MemAcc module provides access to different storage technology devices through an address-based access API.
The MemAcc module always contains one or more memory drivers. The MemAcc module is independent of storage device
technology and can be used in conjunction with typical storage devices such as flash memory, EEPROM, RAM or phase change memory.
The MemAcc module and memory driver are located at the same layer as the Fls and Eep drivers in the AUTOSAR architecture,
but these modules are divided into a hardware-independent part (MemAcc) and a hardware-dependent part (Mem).

在Autosar架构中属于存储硬件抽象层

The MemAcc module belongs to the memory hardware abstraction layer in the Autosar architecture.

模块架构如图 :ref:`MemAcc_AUTOSAR_Arch` 所示。

.. figure:: /_static/参考手册(Module_Reference_Manual)/MemAcc/MemAcc_AUTOSAR_Architecture.png
   :alt: MemAcc模块层次图(MemAcc module hierarchy diagram)
   :name: MemAcc_AUTOSAR_Arch
   :align: center

   MemAcc AUTOSAR Architecture


功能描述(Functional Description)
==========================================

公共特性（Public Features）
--------------------------------------------------------------

多核多分区功能（Multi-core and Multi-partition Features）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
MemAcc多分区场景下，必须保持与上层模块在同一分区。

In the MemAcc multi-partition scenario, it is necessary to remain in the same partition as the upper-level module.


.. only:: doc_pbs

   PBS功能（PBS Features）
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   支持配置不同地址区域的优先级

   Support the configuration of priorities for different address areas

   支持配置不同地址区域的子区域属性（MemAccMemNamePrefix，MemAccMemInvocation除外）

   Support the configuration of sub-region attributes for different address regions (except for MemAccMemNamePrefix and MemAccMemInvocation)


Memmap功能（Memmap Features）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Memmap文件是静态的。存在MEMACC_START_SEC_CODE、MEMACC_STOP_SEC_CODE、MEMACC_START_SEC_VAR_INIT_PTR、MEMACC_STOP_SEC_VAR_INIT_PTR、MEMACC_START_SEC_VAR_CLEARED_8、MEMACC_STOP_SEC_VAR_CLEARED_8、MEMACC_STOP_SEC_VAR_INIT_PTR、MEMACC_START_SEC_VAR_CLEARED_16、MEMACC_STOP_SEC_VAR_CLEARED_16、MEMACC_START_SEC_VAR_CLEARED_UNSPECIFIED、MEMACC_STOP_SEC_VAR_CLEARED_UNSPECIFIED、MEMACC_START_SEC_CONST_UNSPECIFIED、MEMACC_STOP_SEC_CONST_UNSPECIFIED、MEMACC_START_SEC_CONFIG_DATA_UNSPECIFIED、MEMACC_STOP_SEC_CONFIG_DATA_UNSPECIFIED字段。

The memmap file is static.There are MEMACC_START_SEC_CODE、MEMACC_STOP_SEC_CODE、MEMACC_START_SEC_VAR_INIT_PTR、MEMACC_STOP_SEC_VAR_INIT_PTR、MEMACC_START_SEC_VAR_CLEARED_8、MEMACC_STOP_SEC_VAR_CLEARED_8、MEMACC_STOP_SEC_VAR_INIT_PTR、MEMACC_START_SEC_VAR_CLEARED_16、MEMACC_STOP_SEC_VAR_CLEARED_16、MEMACC_START_SEC_VAR_CLEARED_UNSPECIFIED、MEMACC_STOP_SEC_VAR_CLEARED_UNSPECIFIED、MEMACC_START_SEC_CONST_UNSPECIFIED、MEMACC_STOP_SEC_CONST_UNSPECIFIED、MEMACC_START_SEC_CONFIG_DATA_UNSPECIFIED、MEMACC_STOP_SEC_CONFIG_DATA_UNSPECIFIED fields.


独占区功能（Exclusive Area Features）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
None.


模块特性（Module Features）
------------------------------------------------

内存地址转换(Memory address conversion)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
MemAcc模块通过逻辑地址空间的方式将memm驱动程序的物理内存寻址方案抽象到上层。

The MemAcc module abstracts the physical memory addressing scheme of the memm driver to the upper layer through the logical address space.


内存访问定位(Memory access location)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
MemAcc管理多模块（NvM、OTA、BndM等）对共享存储资源的并发访问请求，确保关键操作的原子性和序列化执行，防止冲突。

MemAcc manages concurrent access requests from multiple modules (such as NvM, OTA, BndM, etc.) to shared storage resources,
ensuring the atomicity and serialization execution of critical operations and preventing conflicts.


任务管理与优先级(Task Management and prioritization)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
通常而言，所有需要较长时间处理操作的MemAcc服务均被定义为异步服务。因此，请求的异步服务仅会将任务请求加入队列，
而队列中作业的实际处理则在MemAcc_MainFunction中完成，请求任务的管理还根据配置的优先级策略，为各客户端分配访问优先级。

Generally speaking, all MemAcc services that require a relatively long time to process operations are
defined as asynchronous services. Therefore, the requested asynchronous service will only add the task request to the queue.
The actual processing of jobs in the queue is completed in the MemAcc_MainFunction, and the managementof request tasks also
assigns access priorities to each client based on the configured priority policy.


任务状态与结果(Task status and results)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
MemAcc模块提供访问接口获取当前任务处理的状态信息，以及获取最后一个MemAcc任务的结果。上层模块可以使用这些接口来检索详细信息。

The MemAcc module provides an access interface to obtain the status information of the current task processing and the result
of the last MemAcc task. The upper-level modules can use these interfaces to retrieve detailed information.


硬件特定服务(Hardware-specific services)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
为了支持特定于内存设备的服务，MemAcc模块提供了一个通用的API来调用特定于硬件的Mem驱动服务。
每个Mem驱动程序可以有多个特定于硬件的服务，调用这些服务时可基于hwServiceId参数选择访问特定的内存设备。

To support services specific to memory devices, the MemAcc module provides a universal API to invoke hardware-specific Mem driver services.
Each Mem driver can have multiple hardware-specific services. When invoking these services, specific memory devices can be accessed based on the hwServiceId parameter.


性能优化(Performance optimization)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
MemAcc模块支持使用一些内存驱动程序提供Burst功能，即不是写/擦除一个尽可能小的单元，而是同时写/擦除几个这样的单元，以增加写/擦除吞吐量。

The MemAcc module supports the use of some memory drivers to provide Burst functionality, that is, instead of writing/erasing a single unit as
small as possible, several such units are written/erased simultaneously to increase the write/erase throughput.


通用锁定机制(General locking mechanism)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
为了支持像OTA/BndM这样的上层，MemAcc模块提供了一个通用的锁API，可以用来限制某个Mem驱动程序对内存的访问。

To support upper layers like OTA/BndM, the MemAcc module provides a universal lock API that can be used to restrict memory access by a certain Mem driver.


内存驱动程序的初始化和调用处理(Initialization and invocation processing of memory drivers)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
支持多种方式调用内存驱动，若配置为MEMACC_DIRECT_STATIC的调用方式，Mem驱动程序与应用程序链接，Mem_Init由EcuM调用，Mem_MainFunction由SchM触发；
若配置为MEMACC_INDIRECT_DYNAMIC的调用方式，Mem驱动程序链接为单独的二进制文件，并动态激活。Mem_Init和Mem_MainFunction的调用由MemAcc处理；
若配置为MEMACC_INDIRECT_STATIC的调用方式，Mem驱动程序与应用程序链接。Mem_Init和Mem_MainFunction的调用由MemAcc处理。

Support multiple ways to call the memory driver. If configured as the MEMACC_DIRECT_STATIC calling method, the Mem driver is
linked to the application,Mem_Init is called by EcuM, and Mem_MainFunction is triggered by SchM.
If configured as the calling method of MEMACC_INDIRECT_DYNAMIC, the Mem driver is linked as a separate binary file and
activated dynamically. The calls to Mem_Init and Mem_MainFunction are handled by MemAcc.
If configured to call MEMACC_INDIRECT_STATIC, the Mem driver is linked to the application.
The calls to Mem_Init and Mem_MainFunction are handled by MemAcc.



地址重试机制(Address retry mechanism)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
如果内存驱动程序的请求或者处理失败时，可通过配置的重试次数进行重新请求尝试，若重试次数超过配置值时，则认定此次请求任务为失败。

If the request or processing of the memory driver fails, a re-request attempt can be made through the configured retry count.
If the retry count exceeds the configured value, the current request task is considered a failure.


对齐机制(Alignment mechanism)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
MemAcc模块不执行任何类型的缓冲区对齐。因此，上层提供的缓冲区需要考虑由MemAccBufferAlignmentValue属性定义的对齐要求。
MemAccBufferAlignmentValue必须配置为底层Mem驱动所需的最小公共倍数值。

The MemAcc module does not perform any type of buffer alignment. Therefore, the upper provide buffer to consider
by MemAccBufferAlignmentValue attribute defines the alignment requirements. MemAccBufferAlignmentValue must be
configured for the underlying Mem drive required minimum public times value.


支持64位地址功能(Supports 64-bit address functionality)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
对于大数据区域，支持配置64位地址功能，MemAcc_AddressType和MemAcc_LengthType都将被定义为64字节。

For the big data area, the 64-bit address configuration function is supported. Both MemAcc_AddressType and MemAcc_LengthType will be defined as 64 bytes.


偏差(Deviations)
--------------------------
.. 有序列表示例

#. MemAccUseReadBurst

   增加了对读操作的Burst功能。(The Burst function for read operations has been added.)

#. MemAccNumberOfReadRetries

   增加了对读操作的重试功能。(The retry function for read operations has been added.)


扩展(Extension)
----------------------
None


集成(Integration)
==================================

文件列表(File List)
----------------------------------

静态文件(Static Files)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - 文件 (File)
     - 描述 (Description)
   
   * - MemAcc.h
     - Implementation header for MemAcc
   * - MemAcc_MemApi.h
     - Mem api definitions of MemAcc
   * - MemAcc_Types.h
     - API declaration and macro definition of MemAcc module; including macro definition, type definition, and configuration structure declaration that need to be used.
   * - MemAcc_MemMap.h
     - Contains the memory abstraction of MemAcc module.
   * - MemAcc.c
     - API implementation of MemAcc module; contains internal functions, and global functions that need to be used.


动态文件(Dynamic Files)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - 文件 (File)
     - 描述 (Description)

   * - MemAcc_Cfg.h
     - Configuration parameter of MemAcc.
   * - MemAcc_Lcfg.c
     - Link time definitions of MemAcc; Contains the Ecc parameters address that need to be used.
   * - MemAcc_Lcfg.h
     - Link time declaration of MemAcc; Contains macro definitions, version information, and API declarations that need to be used.
   * - MemAcc_PBcfg.h
     - Post-build time Configuration declaration of MemAcc; Contains macro definitions, version information, and API declarations that need to be used.
   * - MemAcc_PBcfg.c
     - Post-build time definitions of MemAcc; Contains the block address, size, and algorithm that need to be used.


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

   * - MEMACC_E_NO_ERROR
     - 0x0u
     - API function called with no det error

   * - MEMACC_E_UNINIT
     - 0x01u
     - API service called without module initialization

   * - MEMACC_E_PARAM_POINTER
     - 0x02u
     - API service called with NULL pointer argument

   * - MEMACC_E_PARAM_ADDRESS_AREA_ID
     - 0x03u
     - API service called with wrong address area ID

   * - MEMACC_E_PARAM_ADDRESS_LENGTH
     - 0x04u
     - API service called with address and length not belonging to the passed address area ID

   * - MEMACC_E_PARAM_HW_ID
     - 0x05u
     - API service called with a hardware ID not belonging to the passed address area ID

   * - MEMACC_E_BUSY
     - 0x06u
     - API service called for an address area ID with a pending job request

   * - MEMACC_E_MEM_INIT_FAILED
     - 0x07u
     - Dynamic MEM driver activation failed due to inconsistent MEM driver binary


运行时错误(Runtime Errors)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
None


产品错误(Product Errors)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
None


扩展产品错误(Extended Product Errors)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
None


接口描述(Interface Description)
=====================================

.. include:: MemAcc_api.rst


依赖的服务(Dependent Services)
----------------------------------------

可选接口(Optional Interfaces)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 10 5 30
   :header-rows: 1

   * - API Function
     - Header File
     - Description

   * - Det_ReportError
     - Det.h
     - Service to report development errors


强制接口(Mandatory Interfaces)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. 可选的章节，根据模块实际情况确定

.. list-table::
   :widths: 10 5 30
   :header-rows: 1

   * - API Function
     - Header File
     - Description
   * - Mem_BlankCheck
     - Mem.h
     - Triggers a job to check the erased state of the page which is referenced by targetAddress. The result of this service can be 
       retrieved using the Mem_GetJob Result API. If the checked page is blank, the result of the job is MEM_JOB_OK. Otherwise, if
       the page is not blank, the result is MEM_INCONSISTENT.
   * - Mem_Erase
     - Mem.h
     - Triggers an erase job of the given sector/sector batch defined by targetAddress and length. The result of this service can
       be retrieved using the Mem_GetJobResult API. If the erase operation was successful, the result of the job is MEM_JOB_OK. If
       the erase operation failed, e.g. due to a hardware issue, the result of the job is MEM_JOB_FAILED.
   * - Mem_GetJobResult
     - Mem.h
     - Service to return results of the most recent job.
   * - Mem_HwSpecificService
     - Mem.h
     - Triggers a hardware specific memory driver job. dataPtr can be used to pass and return data to/from this service. This service
       is just a dispatcher to the hardware specific service implementation referenced by hwServiceId. The result of this service can
       be retrieved using the Mem_GetJob Result API. If the hardware specific operation was successful, the result of the job is
       MEM_JOB_OK. If the hardware specific operation failed,the result of the job is MEM_JOB_FAILED.
   * - Mem_Init
     - Mem.h
     - Initialization function - initializes all variables and sets the module state to initialized.
   * - Mem_MainFunction
     - Mem.h
     - Service to handle the requested jobs and the internal management operations.
   * - Mem_PropagateError
     - Mem.h
     - This service can be used to report an access error in case the Mem driver cannot provide the access error information - typically
       for ECC faults. It is called by the system ECC handler to propagate an ECC error to the memory upper layers.
   * - Mem_Read
     - Mem.h
     - Triggers a read job to copy the from the source address into the referenced destination data buffer. The result of this service
       can be retrieved using the Mem_GetJobResult API. If the read operation was successful, the result of the job is MEM_JOB_OK. If
       the read operation failed, the result of the job is either MEM_JOB_FAILED in case of a general error or 
       MEM_ECC_CORRECTED/MEM_ECC_UNCORRECTED in case of a correctable/uncorrectable ECC error.
   * - Mem_Write
     - Mem.h
     - Triggers a write job to store the passed data to the provided address area with given address and length. The result of this service
       can be retrieved using the Mem_GetJobResult API. If the write operation was successful, the job result is MEM_JOB_OK. If there was
       an issue writing the data, the result is MEM_FAILED.


配置接口(Configuration Interfaces)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. 可选的章节，根据模块实际情况确定
.. 格式同强制接口

.. list-table::
   :widths: 10 5 30
   :header-rows: 1

   * - API Function
     - Header File
     - Description
   * - AddressAreaJobEndNotification
     - None
     - MemAcc application job end notification callback. The function name is configurable.
   * - ApplicationLockNotification
     - None
     - Address area lock application callback. The function name is configurable.


配置(Configuration)
============================

头文件包含(The header file contains)
--------------------------------------------
在MemAcc模块使用过程中，需要使用到下层Mem Driver模块，或者用户自定义的一些callout接口，所以在MemAcc模块中，若需要使用自定义的一些文件，可在配置中包含对应的头文件。
如图 :ref:`MemAccPublicCddHeaderFile` 所示。

During the use of the MemAcc module, the lower-level Mem Driver module or some user-defined callout interfaces need to be used. Therefore, in
the MemAcc module, if some custom files need to be used, the corresponding header files can be included in the configuration.
As shown in figure: ref: ` MemAccPublicCddHeaderFile ` shown below.

.. figure:: /_static/参考手册(Module_Reference_Manual)/MemAcc/MemAccPublicCddHeaderFile.png
   :alt: MemAcc模块配置图 (MemAcc module configuration diagram)
   :name: MemAccPublicCddHeaderFile
   :align: center

   MemAccPublicCddHeaderFile Config


地址区域ID(Address area ID)
--------------------------------------------
如图 :ref:`MemAccAddressAreaId` 所示，MemAcc的地址区域ID为默认不可配置，由工具自动计算，并递增的。

As shown in the figure :ref: 'MemAccAddressAreaId', the address area ID of MemAcc is unconfigurable by default, automatically calculated by the tool and incremented.

.. figure:: /_static/参考手册(Module_Reference_Manual)/MemAcc/MemAccAddressAreaId.png
   :alt: MemAccAddressAreaId配置图 (MemAcc Address Area Id configuration diagram)
   :name: MemAccAddressAreaId
   :align: center

   MemAccAddressAreaId Config


Mem驱动设置以及调用方式(Mem driver Settings and invocation methods)
-------------------------------------------------------------------------
如图 :ref:`MemAccMem` 所示，Mem驱动的名称可在MemAccMemNamePrefix中进行配置。（注意：一个驱动只能使用一种调用方式）
Mem驱动的调用方式可以根据实际使用情况在MemAccMemInvocation中进行配置，分为三种情况：
(1)MEMACC_DIRECT_STATIC;(2)MEMACC_INDIRECT_DYNAMIC;(3)MEMACC_INDIRECT_STATIC;
详细可参考“功能描述”章节中的“内存驱动程序的初始化和调用处理”。

As shown in the figure :ref: 'MemAccMem', the name of the Mem driver can be configured in MemAccMemNamePrefix. (Note: A driver can only be invoked in one way.)
The calling method of the Mem driver can be configured in MemAccMemInvocation according to the actual usage situation, and it is divided into three cases:
(1)MEMACC_DIRECT_STATIC; (2)MEMACC_INDIRECT_DYNAMIC; (3)MEMACC_INDIRECT_STATIC;
For detailed information, please refer to the "Initialization and Invocation Processing of Memory Drivers" in the "Function Description" section.

.. figure:: /_static/参考手册(Module_Reference_Manual)/MemAcc/MemAccMem.png
   :alt: MemAccMem配置图 (MemAcc Mem configuration diagram)
   :name: MemAccMem
   :align: center

   MemAccMem Config


重试功能(Retry function)
-------------------------------------
如图 :ref:`MemAccRetries` 所示，可在每一个子区域中设置读写擦除的失败重试次数。

As shown in the figure :ref: 'MemAccRetries', the number of failed retries for read-write erasure can be set in each sub-area.

.. figure:: /_static/参考手册(Module_Reference_Manual)/MemAcc/MemAccRetries.png
   :alt: MemAccRetries配置图 (MemAcc Retries configuration diagram)
   :name: MemAccRetries
   :align: center

   MemAccRetries Config


使用大数据功能(Use the burst data function)
--------------------------------------------
如图 :ref:`MemAccUseBurst` 所示，可以配置读写擦除的Burst功能，但前提是底层的Mem驱动支持此功能，并且已打开Burst功能的配置。

As shown in the figure :ref: 'MemAccUseBurst', the Burst function for read-write erasing can be configured, but only if the underlying
Mem driver supports this function and the Burst function configuration is enabled.

.. figure:: /_static/参考手册(Module_Reference_Manual)/MemAcc/MemAccUseBurst.png
   :alt: MemAccUseBurst配置图 (MemAcc UseBurst configuration diagram)
   :name: MemAccUseBurst
   :align: center

   MemAccUseBurst Config


Sector的使用(The use of Sector)
--------------------------------------------
如图 :ref:`MemAccSector` 所示，MemAccSectorOffset表示当前子区域从哪一个Sector开始，MemAccNumberOfSectors表示当前子区域使用了几个Sector。

As shown in the figure :ref: 'MemAccSector', MemAccSectorOffset indicates from which Sector the current subregion starts,
and MemAccNumberOfSectors indicates how many sectors are used in the current subregion.

.. figure:: /_static/参考手册(Module_Reference_Manual)/MemAcc/MemAccSector.png
   :alt: MemAccSector配置图 (MemAcc Sector configuration diagram)
   :name: MemAccSector
   :align: center

   MemAccSector Config

