===================
Fee
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
   * - 2024/11/12
     - peng.wu
     - V0.1
     - 发布(Release)
     - 首次发布(First release)
   * - 2025/04/04
     - peng.wu
     - V1.0
     - 发布(Release)
     - 正式发布(Official release)

参考文档(References)
----------------------------------

.. list-table::
   :widths: 10 12 25 10
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
     - AUTOSAR_CP_SWS_FlashEEPROMEmulation.pdf
     - R23-11 


术语与简写(Terms and Abbreviations)
========================================


术语(Terms)
------------------
   .. :align: center   表格内容居中(Table contents are centered)


.. list-table::
   :widths: 10 40
   :header-rows: 1

   * - 术语(Term)
     - 解释(Explanation)

   * - (Logical) block
     - 逻辑块，是模块的最小可写/可擦单元，由一个或多个虚拟页组成(A logical block is the smallest writable/erasable unit in the FEE module, consisting of one or more virtual pages)

   * - Virtual page
     - 虚拟页，可能由一个或多个物理页面组成(A virtual page, which may consist of one or more physical pages)

   * - Bank
     - 存储块，可能由一个或几个物理部分组成(A storage block, which may consist of one or several physical parts)

   * - Virtual address
     - 虚拟地址，由逻辑块内的16位块号和16位偏移量组成(A virtual address, composed of a 16-bit block number and a 16-bit offset within a logical block)

   * - Physical address
     - 物理地址，用于访问逻辑块的设备特定格式的地址信息(取决于底层驱动程序和设备)(A physical address, which is device-specific format address information used to access logical blocks (depending on the underlying driver and device))

   * - Internal residue
     - 内部残留，如果配置的块大小不是虚拟页大小的整数倍，则最后一个虚拟页末尾的未使用空间(Internal residue refers to the unused space at the end of the last virtual page if the configured block size is not an integer multiple of the virtual page size)

   * - Address Area
     - 地址区域，逻辑地址空间中的连续内存区，通常将多个物理内存扇区组合到一个逻辑地址区中(An address area is a continuous memory area in the logical address space, usually combining multiple physical memory sectors into one logical address area)

简写(Abbreviations)
----------------------------

.. list-table::
   :widths: 15 25 30
   :header-rows: 1


   * - 简写(Abbreviation)
     - 全称(Full name)
     - 解释(Explanation)

   * - FEE
     - Flash EEPROM Emulation
     - Flash EEPROM仿真

   * - EA
     - EEPROM Abstraction
     - EEPROM抽象

   * - EEPROM
     - Electrically Erasable and Programmable ROM 
     - 电可擦可编程只读存储器

   * - MemIf
     - Memory Abstraction Interface
     - 内存抽象接口

   * - NvM
     - NVRAM Manager
     - 非易失RAM管理

   * - MemAcc
     - Memory Access- AUTOSAR Basic Software module for memory access
     - AUTOSAR基本软件模块存储器访问

   * - LSB
     - Least significant bit / byte 
     - 最低有效位/字节

   * - MSB
     - Most significant bit / byte
     - 最高有效位/字节

简介(Introduction)
=========================


Fee是对Flash块进行逻辑块的划分(逻辑块的大小根据配置可能不同)，以及地址映射，
通过模拟Eeprom(不用先擦除再写入)主要实现基于Block的非易失性数据读、写功能，同时支持
Immediate Block的擦除，Block的使无效操作，任务的取消机制，模块状态及任务结果的获取。

Fee divides Flash blocks into logical blocks (logical block sizes may vary based on configuration) and performs address mapping. By emulating EEPROM (no erase before write), it mainly implements Block-based non-volatile data read/write functions, while supporting Immediate Block erasure, Block invalidation operations, task cancellation mechanisms, and module status and task result acquisition.

Fee模块处于AUTOSAR架构中的存储服务层，其下层模块为Flash模块，上层模块为MemIf模块。
模块架构如图 :ref:`Fee_AUTOSAR_Arch` 所示。

The Fee module is located in the storage service layer of the AUTOSAR architecture. Its lower layer module is the Flash module, and its upper layer module is the MemIf module. The module architecture is shown in Figure :ref:`Fee_AUTOSAR_Arch`.

.. figure:: ../../../_static/参考手册/Fee/Fee_AUTOSAR_Architecture.png
   :alt: Fee模块层次图(Fee Module Hierarchy Diagram)
   :name: Fee_AUTOSAR_Arch
   :align: center

   Fee AUTOSAR Architecture

Fee接口调用关系如图 :ref:`Fee_Interface` 所示，接口的详细内容请参考“接口描述”章节。

The Fee interface calling relationship is shown in Figure :ref:`Fee_Interface`. For detailed interface information, please refer to the "Interface Description" chapter.

.. figure:: ../../../_static/参考手册/Fee/Fee_Interface_Relationship.png
   :alt: Fee模块接口关系图(Fee Module Interface Relationship Diagram)
   :name: Fee_Interface
   :align: center

   Fee interface relationship


功能描述(Functional Description)
===================================


特性(Features)
----------------------

模块初始化(Module Initialization)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Fee模块必须在初始化接口调用后才能开始运行。因为Fee初始化可能涉及大量的Flash读操作，
以及可能发生的Flash擦除、写入操作，通常耗时较长。所以Fee的初始化通过异步实现，
Fee_Init加载初始化任务，由Fee_MainFunction来实际执行。

The Fee module can only start operation after the initialization interface is called. Since Fee initialization may involve extensive Flash read operations, and possible Flash erase/write operations, it typically takes a long time. Therefore, Fee initialization is implemented asynchronously. Fee_Init loads the initialization task, which is then executed by Fee_MainFunction.


Block操作功能(Block Operation Functions)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
1. Fee模块对Block的操作是单任务的，同一时间只能处理一个任务，任务处理过程中不能加载新的任务。

   The Fee module processes Block operations as single tasks. Only one task can be processed at a time, and new tasks cannot be loaded during task processing.

2. Fee模块对Block的操作都是通过异步机制实现，通过调用Fee_Read，Fee_Write，Fee_InvalidateBlock，Fee_EraseImmediateBlock加载任务，在Fee_MainFunction中实际执行。

   All Fee module Block operations are implemented through asynchronous mechanisms. Tasks are loaded by calling Fee_Read, Fee_Write, Fee_InvalidateBlock, and Fee_EraseImmediateBlock, and are actually executed in Fee_MainFunction.

3. Block的区分通过参数BlockNumber决定，各个Block的BlockNumber唯一，存储栈集成时BlockNumber的配置需要与NvMDatasetSelectionBits及关联NvM模块中Block的NvMBlockManagementType适配。

   Blocks are distinguished by the BlockNumber parameter. Each Block has a unique BlockNumber. During storage stack integration, BlockNumber configuration must align with NvMDatasetSelectionBits and the NvMBlockManagementType of the associated Block in the NvM module.

4. 任务的结果支持两种机制反馈给上层模块：

   Task results support two feedback mechanisms to upper layer modules:

   a. 在polling模式下实现接口Fee_GetJobResult供上层随时获取Job结果；

      In polling mode, the Fee_GetJobResult interface is implemented for the upper layer to obtain Job results at any time;

   b. 在Notification模式下，任务成功/失败通过调用上层回调函数通知，如NvM_JobEndNotification/NvM_JobErrorNotification。

      In Notification mode, task success/failure is notified by calling upper layer callback functions, such as NvM_JobEndNotification/NvM_JobErrorNotification.

5. 配置为Immediate的Block才支持Fee_EraseImmediateBlock操作，且在调用Fee_Write前需要先执行完Fee_EraseImmediateBlock任务。

   Only Blocks configured as Immediate support the Fee_EraseImmediateBlock operation, and the Fee_EraseImmediateBlock task must be completed before calling Fee_Write.


访问Flash(Driver Accessing Flash Driver)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Fee功能的实现依赖于通过Flash Driver实现Flash的擦除、读、写功能，以及任务取消，任务结果获取等机制。
Flash Driver中Flash数据的擦除、读、写同样通过异步机制实现，Fee模块与Flash Driver之间任务结果的交互同样分两种机制：

Fee function implementation relies on Flash Driver for Flash erase, read, and write operations, as well as task cancellation and result acquisition mechanisms. Flash data erase, read, and write operations in Flash Driver are also implemented asynchronously. Task result interaction between Fee module and Flash Driver also uses two mechanisms:

1. 在polling模式下，Fee通过调用接口Fls_GetJobResult获取Job结果；

   In polling mode, Fee obtains Job results by calling the Fls_GetJobResult interface;

2. 在Notification模式下，任务成功/失败Flash Driver都通过调用Fee_JobEndNotification回调函数通知Fee模块；

   In Notification mode, Flash Driver notifies the Fee module of task success/failure by calling the Fee_JobEndNotification callback function;


偏差(Deviations)
--------------------------

#. 写访问的扩展(Extension of write access)

   由于写访问的扩展等需求目前受硬件的影响相对较小，暂时忽略。所以写访问的扩展、逻辑块写循环次数的配置暂时未实现。

   Due to relatively minor hardware impact on write access extension requirements, this feature is currently ignored. Therefore, write access extension and logical block write cycle count configuration are not yet implemented.

#. 初始化的同步方式(Synchronous mode of initialization)

   Fee的初始化可以分为异步和同步两种方式，但是由于Fee初始化可能涉及大量的Flash读操作，所以当前实现采用了异步方式，同步方式暂未实现。

   Fee initialization can be implemented in both asynchronous and synchronous modes. However, since Fee initialization may involve extensive Flash read operations, the current implementation uses asynchronous mode, while synchronous mode is not yet implemented.

扩展(Extension)
----------------------
None

集成(Integration)
===========================

文件列表(File List)
----------------------------------

静态文件(Static Files)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - 文件(File)
     - 描述(Description)
   
   * - Fee.c
     - 作为Fee模块的核心文件，实现Fee模块全部对外接口，以及实现Fee模块功能所必须的local函数，local宏定义，local变量定义 (As the core file of the Fee module, implements all external interfaces of the Fee module, as well as local functions, local macro definitions, and local variable definitions necessary for Fee module functionality)
       
   * - Fee.h
     - 实现Fee模块全部外部接口的声明，以及配置文件中全局变量的声明 (Implements declarations of all external interfaces of the Fee module and declarations of global variables in configuration files)
       
   * - Fee_Types.h
     - 实现Fee模块全部外部宏定义，数据类型的定义与声明 (Implements definitions and declarations of all external macro definitions and data types of the Fee module)
       
   * - Fee_InternalTypes.h
     - 实现Fee模块全部内部宏定义，数据类型的定义与声明 (Implements definitions and declarations of all internal macro definitions and data types of the Fee module)
       
   * - Fee_Cbk.h
     - 实现Fee模块全部外部回调接口的声明 (Implements declarations of all external callback interfaces of the Fee module)
       
   * - Fee_MemMap.h
     - 实现Fee模块内存映射抽象的声明 (Implements declaration of memory map abstraction for the Fee module)

动态文件(Dynamic Files)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - 文件(File)
     - 描述(Description)
   
   * - Fee_Cfg.h
     - 定义Fee模块PB配置的宏定义(Defines macro definitions for PB configuration of the Fee module)
       
   * - Fee_Lcfg.h
     - 定义Fee模块PC配置的宏定义以及数据类型(Defines macro definitions and data types for PC configuration of the Fee module)
       
   * - Fee_Lcfg.c
     - 定义Fee模块PC配置的结构体参数(Defines structure parameters for PC configuration of the Fee module)


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

   * - FEE_E_UNINIT
     - 0x01u
     - API service called when module was not initialized

   * - FEE_E_INVALID_BLOCK_NO
     - 0x02u
     - API service called with invalid block number

   * - FEE_E_INVALID_BLOCK_OFS
     - 0x03u
     - API service called with invalid block offset

   * - FEE_E_PARAM_POINTER
     - 0x04u
     - API service called with invalid data pointer

   * - FEE_E_INVALID_BLOCK_LEN
     - 0x05u
     - API service called with invalid length information

运行时错误(Runtime Errors)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: 
   :widths: 20 10 30
   :header-rows: 1

   * - Error code
     - Value[hex]
     - Description

   * - FEE_E_BUSY
     - 0x06u
     - API service called while module is busy processing a user request

   * - FEE_E_INVALID_CANCEL
     - 0x08u
     - Fee_Cancel called while no job was pending

.. 引用接口描述。来自于code->doxygen->latex->rst
.. include:: Fee_api.rst

配置(Configuration)
===============================

FeeBank
----------------------
因为Flash Driver的写操作特性，至少需要配置2个Fee_Bank用于Fee模块页的切换功能。
如图 :ref:`Fee_Bank_Config` 展示了Fee_Bank的配置界面，可配置Bank索引值、Bank起始地址、Bank大小、Flash驱动Sector某一Sector的关联等。

Due to Flash Driver write operation characteristics, at least 2 Fee_Banks need to be configured for Fee module page switching functionality.
As shown in Figure :ref:`Fee_Bank_Config`, it displays the Fee_Bank configuration interface, where Bank index value, Bank start address, Bank size, association with specific Flash driver sector, etc. can be configured.

.. figure:: ../../../_static/参考手册/Fee/Fee_Bank.png
   :alt: Fee模块Bank配置图(Fee Module Bank Configuration Diagram)
   :name: Fee_Bank_Config
   :align: center

   Fee Bank Configuration


头文件包含(Header File Inclusion)
--------------------------------------------
在Fee模块使用过程中，需要使用到下层Flash Driver模块，由于MCAL厂商的文件命名差异，可能会涉及文件名和类型名字不匹配的问题，所以在Fee模块中，需要在配置中包含Flash Driver的头文件#include "xxx.h"。
如图 :ref:`Fee_Header_Including` 所示。

During Fee module usage, the underlying Flash Driver module is required. Due to MCAL vendor file naming differences, file name and type name mismatches may occur. Therefore, in the Fee module, the Flash Driver header file #include "xxx.h" needs to be included in the configuration.
As shown in Figure :ref:`Fee_Header_Including`.

.. figure:: ../../../_static/参考手册/Fee/Fee_Header_Including.png
   :alt: Fee模块配置图 (Fee Module Configuration Diagram)
   :name: Fee_Header_Including
   :align: center

   Fee Header Including


不擦除直接写(Write without Erasing)
-------------------------------------------------
此配置可决定是否使能Flash数据多次写入(未擦除)，以节约Block管理数据占用资源。默认不可配置，只有FeeVirtualPageSize的值 >= 16时该配置项才能配置。

This configuration determines whether to enable multiple Flash data writes (without erasing) to save Block management data resource usage. Not configurable by default, this configuration item can only be configured when FeeVirtualPageSize value >= 16.


Header的大小(Size of Header)
----------------------------------------------
Fee/FeePublishedInformation中的FeeBlockOverhead和FeeBankOverhead配置项，不可手动修改，根据配置的FeeVirtualPageSize，以及是否勾选后了FeePageDirectWriteSupport配置项，最终由工具自动计算得到对应的数值。

FeeBlockOverhead and FeeBankOverhead configuration items in Fee/FeePublishedInformation cannot be manually modified. Based on configured FeeVirtualPageSize and whether FeePageDirectWriteSupport is selected, corresponding values are automatically calculated by the tool.