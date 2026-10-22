===================
IStdLib
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
----------------------------------
None


术语与简写(Terms and Abbreviations)
========================================


术语(Terms)
----------------------

None


简写(Abbreviation)
-----------------------------

.. list-table::
   :widths: 15 20 25
   :header-rows: 1


   * - 简写(Abbreviation)
     - 全称(Full name)
     - 解释(Explanation)

   * - IStdLib
     - ISoft Library
     - 普华自研库(Self-Developed Library)
      


简介(Introduction)
===========================

IStdLib模块由IStdLib_Mem.c和IStdLib_MemHeap.c函数组成，前者包括memcpy，memset和memcmp的自定义实现的内存操作，后者是基于TLSF算法的内存堆分配，将会为用户分配内存到自己的一个内存空间，最低要求是16个字节。

The IStdLib module consists of two functions: IStdLib_Mem.c and IStdLib_MemHeap.c. The former includes custom-implemented memory operations such as memcpy, memset, and memcmp. The latter is a memory heap allocation based on the TLSF algorithm, which will allocate memory for users into their own memory space, with a minimum requirement of 16 bytes.


功能描述(Functional Description)
===================================


特性(Features)
---------------------------

MemHeap简介(Introduction to MemHeap)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
MemHeap模块为其他模块提了供动态内存开辟的手段。

The MemHeap module provides a means for dynamic memory allocation for other modules.

参考TLSF(Two-Level Segregated Fit,内存两级分割策略算法)实现原理，对其代码进行了重构，在满足O(1)的时间复杂度的情况下，进行了以下优化和升级：

Referencing the implementation principle of TLSF (Two-Level Segregated Fit) algorithm, the code has been refactored. While maintaining O(1) time complexity, the following optimizations and enhancements have been made:

#. 缩小了静态管理空间和动态管理块的大小，提高内存管理的空间利用率

   Reduced the size of static management space and dynamic management blocks to improve memory space utilization.

#. 移除了代码中对全局变量的依赖，将其作为库函数，支持各模块的空间隔离

   Removed dependency on global variables in the code, making it a library function that supports spatial isolation across modules.

#. 删除未使用的相关功能

   Removed unused related functions.

#. 增加和完善开发错误检测

   Added and improved development error detection.

MemHeap的使用(Usage of MemHeap)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
一般内存堆的分配，分为内存堆初始化、内存分配、内存释放三个步骤。

Generally, memory heap allocation involves three steps: memory heap initialization, memory allocation, and memory release.

内存堆初始化IStdLib_MemHeapInit，是将某个对齐地址起，分配一定空间给内存堆，将一段内存空间用MemHeap管理，用于分配内存。可根据返回的错误码进行调试修改，包括：

The memory heap initialization function IStdLib_MemHeapInit allocates a block of memory to the heap starting from an aligned address, managing a segment of memory space using MemHeap for memory allocation. Debugging and modifications can be performed based on the returned error codes, including:

#. ISTDLIB_MEMHEAP_INVALID_PTR，表示输入的起始地址无效

   ISTDLIB_MEMHEAP_INVALID_PTR: indicates that the input starting address is invalid.

#. ISTDLIB_MEMHEAP_INVALID_SIZE，表示分配的大小过大(64K)或过小(堆头部大小)

   ISTDLIB_MEMHEAP_INVALID_SIZE: indicates that the allocated size is too large (64K) or too small (smaller than the heap header size).

#. ISTDLIB_MEMHEAP_INVALID_INIT，表示重复初始化

   ISTDLIB_MEMHEAP_INVALID_INIT: indicates repeated initialization.

#. ISTDLIB_MEMHEAP_INVALID_ALIGN，表示堆提供的堆起始地址不满足字节对齐

   ISTDLIB_MEMHEAP_INVALID_ALIGN: indicates that the provided heap starting address does not meet the byte alignment requirement.

内存分配IStdLib_MemHeapMalloc或IStdLib_MemHeapCalloc，从内存堆中分配所需大小的空间出来，IStdLib_MemHeapCalloc还会将该分配空间填充0。当返回非空指针时表示分配成功。

The memory allocation functions IStdLib_MemHeapMalloc or IStdLib_MemHeapCalloc allocate space of the required size from the memory heap. IStdLib_MemHeapCalloc also fills the allocated space with zeros. A non-null pointer return indicates successful allocation.

内存释放IStdLib_MemHeapFree，将分配出来的某段内存返还给内存堆。可根据返回的错误码进行调试修改，包括：

The memory release function IStdLib_MemHeapFree returns an allocated segment of memory to the memory heap. Debugging and modifications can be performed based on the returned error codes, including:

#. ISTDLIB_MEMHEAP_INVALID_PTR，表示输入参数的两个地址存在无效指针的情况，或待释放的指针为无效指针。

   ISTDLIB_MEMHEAP_INVALID_PTR: indicates that one of the two input addresses is an invalid pointer, or the pointer to be freed is invalid.

#. ISTDLIB_MEMHEAP_INVALID_INIT，表示提供的堆地址未初始化

   ISTDLIB_MEMHEAP_INVALID_INIT: indicates that the provided heap address is not initialized.

#. ISTDLIB_MEMHEAP_INVALID_ALIGN，表示堆提供的堆起始地址不满足字节对齐

   ISTDLIB_MEMHEAP_INVALID_ALIGN: indicates that the provided heap starting address does not meet the byte alignment requirement.

常出现的问题有内存未正确释放引入的内存泄漏，内存堆过于碎片化等。碎片化可能导致分配失败，可使用IStdLib_MemHeapGetRealMaxSize获取当前实际可用的最大空间，以及IStdLib_MemHeapGetCurFreeMaxBlockSize获取当前可申请的最大连续空间。

Common issues include memory leaks due to incorrect memory release and excessive fragmentation of the memory heap. Fragmentation may lead to allocation failures. You can use IStdLib_MemHeapGetRealMaxSize to obtain the current maximum actually available space, and IStdLib_MemHeapGetCurFreeMaxBlockSize to obtain the current maximum contiguous space that can be allocated.

内存操作函数简介(Introduction to Memory Operation Functions)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
为了在嵌入式开发等受限环境下优化性能和内存占用，我们自主实现了 memcpy、memset 和 memcmp 等基础内存操作函数。

To optimize performance and memory usage in constrained environments such as embedded development, we have independently implemented basic memory operation functions like memcpy, memset, and memcmp.

这些函数在功能上覆盖了标准库的基本操作，并针对对齐性和大小端处理进行了特别优化。尽管当前实现在性能上可能稍逊于标准库，

These functions cover the basic operations of the standard library and are specifically optimized for alignment and endianness handling. Although the current implementation may slightly underperform compared to the standard library,

但它提供了更灵活、更轻量的解决方案，为后续优化和特定场景的性能调优提供了空间。使用方法和标准库一致。

It offers a more flexible and lightweight solution, providing room for subsequent optimizations and performance tuning in specific scenarios. The usage method is consistent with the standard library.

偏差(Deviation)
------------------
None

扩展(Extension)
------------------
None

集成(Integration)
=====================

文件列表(File List)
----------------------------------

静态文件(Static Files)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - 文件(File)
     - 描述(Description)

   * - IStdLib.h
     - IStdLib模块头文件(Header file of the IStdLib module)
	 
   * - IStdLib_MemMap.h
     - 内存分配头文件(Memory allocation header file)
	 
   * - IStdLib_MemHeap.c
     - 内存分配源代码(Source code for memory allocation)
	 
   * - IStdLib_Mem.c
     - 内存管理源代码(Source code for memory management)

动态文件(Dynamic Files)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
None


错误处理(Error Handling)
--------------------------------
None

.. 引用接口描述。来自于code->doxygen->latex->rst
.. include:: IStdLib_h_api.rst

配置(Configuration)
======================
None
