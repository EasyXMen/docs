===================
Bfx
===================


文档信息(Document Information)
====================================

版本历史(Version History)
-------------------------------

.. list-table::
   :widths: 10 10 10 10 20
   :header-rows: 1

   * - 日期(Date)
     - 作者(Author)
     - 版本(Version)
     - 状态(Status)
     - 说明(Description)
   * - 2025/03/13
     - qinmei.chen
     - V0.1
     - 发布(Release)
     - 首次发布(First release)
   * - 2025/04/04
     - qinmei.chen
     - V1.0
     - 发布(Release)
     - 正式发布(Official release)

参考文档(References)
-------------------------------

.. list-table::
   :widths: 10 15 25 10
   :header-rows: 1

   * - 编号(Number)
     - 分类(Classification)
     - 标题(Title)
     - 版本(Version)
   * - 1
     - Autosar
     - AUTOSAR_CP_SWS_BFXLibrary.pdf
     - R23-11


术语与简写(Terms and Abbreviations)
========================================


术语(Terms)
-----------------

None


简写(Abbreviations)
---------------------

.. list-table::
   :widths: 15 20 25
   :header-rows: 1


   * - 简写(Abbreviation)
     - 英文全称(Full English name)
     - 中文解释(Chinese explanation)

   * - Bfx
     - Bitfield functions for fixed point
     - 定点数bit操作

   * - DET
     - Default Error Tracer
     - 默认错误追踪

简介(Introduction)
=======================

Bfx模块实现了AUTOSAR中需要的位操作，包括特定位的置位、清零、取状态值、左右移、按位取反等。

The Bfx module implements the bit operations required in AUTOSAR, including setting, clearing, getting the status value of specific bits, left and right shifting, and bitwise negation, etc.

Bfx在架构上属于AUTOSAR静态库代码。

Architecturally, Bfx belongs to AUTOSAR static library code.

.. figure:: /_static/参考手册(Module_Reference_Manual)/Bfx/CP产品架构图-R23V3.0版本_Bfx.png
   :alt: Bfx架构图(Bfx Architecture Diagram)
   :name: fig_Bfx_architecture
   :align: center

   Bfx架构图 (Bfx Architecture Diagram)

功能描述(Functional Description)
=====================================


公共特性(Public Features)
----------------------------

多核多分区功能(Multi-core and Multi-partition Features)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Bfx支持多分区调用，所有接口都是可重入的，可以同时由多个应用程序使用。无模块描述文件。

Bfx supports multi-partition calls. All interfaces are reentrant and can be used simultaneously by multiple applications. No module description file.

.. only:: doc_pbs

   PBS功能(PBS Features)
   ~~~~~~~~~~~~~~~~~~~~~~~~
   无配置项，不支持。

   No configurations, not supported.

Memmap功能(Memmap Features)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
memmap文件是静态的。存在BFX_START_SEC_CODE、BFX_STOP_SEC_CODE字段。

The memmap file is static.There are BFX_START_SEC_CODE and BFX_STOP_SEC_CODE fields.

独占区功能(Exclusive Area Features)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
None.

模块特性(Module Features)
----------------------------

初始化和shutdown(Initialization and shutdown)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Bfx库不需要初始化阶段。库函数可以在ECU初始化的第一步调用。

The Bfx library does not require an initialization stage. Library functions can be called in the first step of ECU initialization. 

Bfx库不需要shutdown操作阶段。

The Bfx library does not need a shutdown operation stage.

分区与共享(Partitioning and Sharing)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Bfx库应该以一种代码可以在不同内存分区中的调用者之间共享的方式实现。

The Bfx library should be implemented in such a way that its code can be shared among callers residing in different memory partitions.

偏差 (Deviation)
-----------------
None

扩展 (Extension)
------------------
None


集成(Integration)
=====================

文件列表(File List)
---------------------

静态文件(Static Files)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - 文件(File)
     - 描述(Description)

   * - Bfx.h
     - Bfx模块头文件。(Bfx module header file.)

   * - Bfx_Static.h
     - Bfx模块宏实现头文件。(Header file for Bfx module macro implementations.)

   * - Bfx.c
     - Bfx源码。(Bfx source code.)

动态文件(Dynamic Files)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
None


错误处理(Error Handling)
---------------------------
None

.. 引用接口描述。来自于code->doxygen->latex->rst
.. include:: Bfx_h_api.rst

配置 (Configuration)
=======================
None