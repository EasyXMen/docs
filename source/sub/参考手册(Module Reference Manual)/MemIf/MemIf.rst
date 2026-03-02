===================
MemIf
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
   * - 2025/03/13
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
   :widths: 10 15 25 10
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
     - AUTOSAR_CP_SWS_MemoryAbstractionInterface.pdf
     - R23-11

术语与简写(Terms and Abbreviations)
========================================

术语(Terms)
-------------------------------
   .. :align: center   表格内容居中(Table contents are centered)

.. list-table::
   :widths: 15 40
   :header-rows: 1

   * - 术语(Term)
     - 解释(Explanation)

   * - Address area
     - Contiguous memory area in the logical address space. Typically, multiple physical memory sectors are combined to one logical address area.

   * - Fast Mode
     - During startup / shutdown the underlying driver may be switched into fast mode in order to allow for fast reading / writing in those phases.

   * - Slow Mode
     - During normal operation the underlying driver may be used in slow mode in order to reduce the resource usage in terms of runtime or blocking time of the underlying device /communication media.

   * - Vendor specific library
     - A vendor specific library is an ICC-2 implementation of the FEE/FLS and EA/EEP modules respectively. It provides the same upper layer interface (API) and functionality as the corresponding ICC-3 implementation.

简写(Abbreviations)
-------------------------------

.. list-table::
   :widths: 15 20 25
   :header-rows: 1

   * - 简写(Abbreviation)
     - 全称(Full name)
     - 解释(Explanation)

   * - LSB
     - Least significant bit / byte (depending on context).
     - 最低有效位/字节(取决于上下文)
   * - Mem
     - AUTOSAR Basic Software Module Memory Driver
     - AUTOSAR基本软件模块内存驱动程序.
   * - FEE
     - Flash EEPROM Emulation.
     - Flash EEPROM仿真
   * - EA
     - EEPROM Abstraction
     - EEPROM抽象.
   * - EEPROM
     - Electrically Erasable and Programmable ROM (Read Only Memory)
     - 电可擦可编程只读存储器(只读型存储器).
   * - MemIf
     - Memory Abstraction Interface
     - 内存抽象接口.
   * - NvM
     - NVRAM Manager
     - 非易失RAM管理.
   * - MemAcc
     - Memory Access- AUTOSAR Basic Software module for memory access
     - AUTOSAR基本软件模块存储器访问.
   * - MSB
     - Most significant bit / byte (depending on context)
     - 最高有效位/字节(取决于上下文).
   * - NVRAM
     - Non-volatile RAM (Random Access Memory)
     - 非易失性RAM(随机存取存储器).

简介(Introduction)
===========================
MemIf模块的核心功能是为上层模块(如NvM)提供统一的访问接口，同时将具体的存储操作委托给底层驱动,
由MemIf接口层提供统一FLASH或EEPROM内存写入、读取、擦除、比较等接口给存储栈服务层使用，
存储栈中所有的状态控制类、操作结果等数据类型也是由MemIf接口层来实现。

The core function of the MemIf module is to provide a unified access interface for upper-layer modules (such as NvM), while delegating specific storage operations to the underlying drivers. The MemIf interface layer provides unified interfaces for FLASH or EEPROM memory operations including writing, reading, erasing, and comparing to the storage stack service layer. All state control and operation result data types used within the storage stack are also implemented by the MemIf interface layer.


功能描述(Functional Description)
===================================

特性(Features)
----------------------

抽象接口(Abstract Interface)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
提供统一的读写接口，使得上层模块可以透明地访问不同类型的非易失性存储器。支持同步和异步操作模式。

Provides a unified read/write interface, enabling upper-layer modules to transparently access different types of non-volatile memory. Supports both synchronous and asynchronous operation modes.


多驱动支持 Multi-Driver(Support)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
允许NVM访问多个存储抽象模块，支持多个底层存储驱动(如EEPROM驱动、Flash驱动)。
给Flash或者EEPROM或者同时给两者一个Device Index，根据Device Index将NvM模块的指令转发给对应的Fee模块或者Ea模块。

Allows NVM to access multiple storage abstraction modules and supports multiple underlying storage drivers (such as EEPROM driver, Flash driver). Assigns a Device Index to Flash, EEPROM, or both, and forwards NvM module commands to the corresponding Fee or Ea module based on the Device Index.


错误传递(Error Propagation)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
MemIf模块将底层驱动的错误传递给上层模块(如NvM)，以便进行错误处理。错误类型包括：读取失败、写入失败、擦除失败等。

The MemIf module propagates errors from underlying drivers to upper-layer modules (such as NvM) for error handling. Error types include: read failure, write failure, erase failure, etc.


集成(Integration)
========================

初始化(Initialization)
-----------------------------
MemIf模块没有初始化，没有配置指针，没有状态指针。

The MemIf module has no initialization routine, no configuration pointers, and no status pointers.


底层模块映射(Underlying Module Mapping)
----------------------------------------------
MemIf模块配置了MemIfDevErrorDetect功能后，将使用源码对底层模块进行。可以使用MemIf_Read、MemIf_Write、MemIf_InvalidateBlock、
MemIf_EraseImmediateBlock、MemIf_Cancel、MemIf_GetJobResult等接口。若打开了MemIfDevErrorDetect功能，且MemIfNumberOfDevices为2，则可使用MemIf_GetStatus接口。
若打开了MemIfVersionInfoApi功能，则可使用MemIf_GetVersionInfo接口。
若没有打开MemIfDevErrorDetect功能。则将使用宏定义映射底层模块的MemIf_Read、MemIf_Write、MemIf_InvalidateBlock、MemIf_EraseImmediateBlock、MemIf_Cancel、
MemIf_GetJobResult、MemIf_GetStatus等接口。

When the MemIfDevErrorDetect feature is configured in the MemIf module, it uses source code to interface with underlying modules. Interfaces such as MemIf_Read, MemIf_Write, MemIf_InvalidateBlock, MemIf_EraseImmediateBlock, MemIf_Cancel, and MemIf_GetJobResult can be used. If MemIfDevErrorDetect is enabled and MemIfNumberOfDevices is set to 2, the MemIf_GetStatus interface becomes available.
If the MemIfVersionInfoApi feature is enabled, the MemIf_GetVersionInfo interface can be used.
If MemIfDevErrorDetect is not enabled, macro definitions are used to map the underlying module's interfaces including MemIf_Read, MemIf_Write, MemIf_InvalidateBlock, MemIf_EraseImmediateBlock, MemIf_Cancel, MemIf_GetJobResult, and MemIf_GetStatus.


文件列表(File List)
----------------------------------

静态文件(Static Files)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - 文件(File)
     - 描述(Description)
   
   * - MemIf_Types.h
     - Type definition of MemIf module; including type definition, and configuration structure declaration that need to be used.
   * - MemIf.h
     - API declarations and macro definitions of MemIf module; including macro definitions, and external function declarations that need to be used.
   * - MemIf.c
     - API implementation of MemIf module; contains macro definitions, internal functions, and global functions that need to be used.
   * - MemIf_MemMap.h
     - Memory abstraction including MemIf module.


动态文件(Dynamic Files)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - 文件(File)
     - 描述(Description)

   * - MemIf_Cfg.h
     - Configuration parameters required for the implementation of MemIf; Contains macro definitions, version information.
   * - MemIf_Cfg.c
     - Configuration parameters required for the implementation of MemIf; Contains the API information that need to be used.

错误处理(Error Handling)
--------------------------------

开发错误(Development Error)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. list-table:: 
   :widths: 20 10 30
   :header-rows: 1

   * - Error code
     - Value[hex]
     - Description

   * - MEMIF_E_NO_ERROR
     - 0x0u
     - API function called with no det error

   * - MEMIF_E_PARAM_DEVICE
     - 0x01u
     - API service called with wrong device index parameter

   * - MEMIF_E_PARAM_POINTER
     - 0x02u
     - API service called with NULL pointer argument


产品错误(Product Errors)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
None


接口描述(Interface Description)
========================================

.. include:: MemIf_api.rst



依赖的服务(Dependent Services)
---------------------------------------------

可选接口(Optional Interfaces)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. 可选的章节，根据模块实际情况确定

.. list-table::
   :widths: 10 5 30
   :header-rows: 1

   * - API Function
     - Header File
     - Description
   * - Ea_EraseImmediateBlock
     - Ea.h
     - Erases the block BlockNumber
   * - Ea_GetStatus
     - Ea.h
     - Service to return the Status
   * - Ea_InvalidateBlock
     - Ea.h
     - Invalidates the block BlockNumber
   * - Fee_EraseImmediateBlock
     - Fee.h
     - Service to erase a logical block
   * - Fee_GetStatus
     - Fee.h
     - Service to return the status.
   * - Fee_InvalidateBlock
     - Fee.h
     - Service to invalidate a logical block


配置(Configuration)
=============================

MemIfGeneral
---------------------------
在General中，MemIfVersionInfoApi配置项用于打开获取版本的功能。MemIfDevErrorDetect配置项用于配置MemIf模块是使用函数指针还是宏定义的方式进行映射，
MemIfDevErrorDetect没有勾选，则使用宏定义的方式。若勾选了，则使用函数指针的方式，且当MemIfDevErrorDetect勾选后，MemIfNumberOfDevices配置为2，
则可使用MemIf_GetStatus接口。
如图 :ref:`General` 展示了MemIfGeneral的配置界面。

In the General section, the MemIfVersionInfoApi configuration item is used to enable the version information retrieval function. The MemIfDevErrorDetect configuration item determines whether the MemIf module uses function pointers or macro definitions for mapping. If MemIfDevErrorDetect is not selected, macro definitions are used. If selected, function pointers are used, and when MemIfDevErrorDetect is selected with MemIfNumberOfDevices configured as 2, the MemIf_GetStatus interface becomes available.
Figure :ref:`General` shows the configuration interface of MemIfGeneral.

.. figure:: ../../../_static/参考手册/MemIf/MemIfGeneral.png
   :alt: MemIf模块TestEccApi配置图 (TestEccApi Configuration Diagram of MemIf Module)
   :name: General
   :align: center

   MemIf General Configuration






