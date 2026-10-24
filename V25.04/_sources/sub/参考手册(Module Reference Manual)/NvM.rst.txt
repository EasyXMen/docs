NvM
#################################

:strong:`缩写词注解 (Abbreviation Notes):`

.. list-table::
   :widths: 34 33 33
   :header-rows: 1

   * - 缩写词 (Abbreviations)
     - 英文全名 (Full English Name)
     - 解释/描述 (Explanation/Description)
   * - DET
     - Development Error Tracer –module to which developmenterrors are reported.
     - 开发错误跟踪器-报告开发错误的模块。 (Develop Error Tracker - Module for Reporting Development Errors.)
   * - DEM
     - Diagnostic Event Manager –module to which productionrelevant errors are reported
     - 诊断事件管理器-报告生产相关错误的模块 (Diagnostic Event Manager - Module for reporting production-related errors)
   * - NV
     - Non volatile
     - 非易失 (Non-volatile)
   * - FEE
     - Flash EEPROM Emulation
     - Flash EEPROM仿真 (Flash EEPROM Simulation)
   * - EA
     - EEPROM Abstraction
     - EEPROM抽象 (EEPROM Abstraction)
   * - FCFS
     - First come first served
     - 先到先得 (First come, first served.)
   * - EEPROM
     - Electrically Erasable andProgrammable ROM (Read OnlyMemory)
     - 电可擦可编程只读存储器(只读型存储器) (Electrically Erasable Programmable Read-Only Memory (ROM))
   * - MemIf
     - Memory Abstraction Interface
     - 内存抽象接口 (Memory abstraction interface)
   * - NvM
     - NVRAM Manager
     - 非易失RAM管理 (Non-Volatile RAM Management)






简介 (Introduction)
=================================

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/NvM/image1.png
   :alt: NvM模块层次图 (NVMe Module Hierarchy Diagram)
   :name: NvM模块层次图 (NVMe Module Hierarchy Diagram)
   :align: center


NvM模块应根据汽车环境中NV(非易失性)数据的不同需求提供服务，以确保数据的存储和维护。NvM模块必须能够管理EEPROM和/或FLASH EEPROM仿真设备的NV数据。NvM模块为NV数据的管理和维护提供所需的同步/异步服务(init/read/write/control)。

The NvM module should provide services to accommodate the varying needs of non-volatile (NV) data in automotive environments, ensuring its storage and maintenance. The NvM module must be capable of managing NV data from EEPROM and/or Flash EEPROM simulation devices. The NvM module offers required synchronous/asynchronous services (init/read/write/control) for the management and maintenance of NV data.

实现对非易失性数据的管理和维护，即NvM模块应该提供服务，以确保在汽车环境中根据非易失性数据的个人需求进行数据存储和维护；以及能够管理EEPROM或FLASH EEPROM仿真设备的非易失数据。

To manage and maintain non-volatile data, the NvM module should provide services to ensure data storage and maintenance according to individual needs for non-volatile data in automotive environments; and it should be capable of managing non-volatile data from EEPROM or Flash EEPROM simulation devices.

NvM模块应该可以根据客户对数据的不同需求，提供对NV（非易失性）数据的管理，包括存储、维护、读取、写入等功能。NvM模块可以管理EEPROM和FLASH EEPROM仿真设备的NV数据。针对NV数据的存储、维护、读取、写入等功能，NvM模块需要提供所需的同步/异步服务。

The NvM module should provide management for NV (non-volatile) data based on the customer's different needs, including storage, maintenance, read, and write functions. The NvM module can manage NV data for EEPROM and FLASH EEPROM simulation devices. For the storage, maintenance, read, and write functions of NV data, the NvM module needs to provide the required synchronous/asynchronous services.

NVM提供的功能包括以下几点：

The features provided by NVM include the following:

- NvM模块应该使用队列机制来缓存外部的请求，并通过异步的形式来完成队列中的请求。NvM模块应该根据请求的优先级顺序来从队列里面获取需要处理的请求，并处理相应的请求。

The NvM module should use a queue mechanism to cache external requests and complete the requests in the queue through an asynchronous form. The NvM module should retrieve requests for processing from the queue based on their priority and handle the corresponding requests.

- NvM模块应该提供隐式技术来检查NVRAM块的数据一致性，NVRAM块的数据一致性检查应通过相应NV块的CRC重新计算来完成。

The NvM module should provide implicit techniques to check the data consistency of NVRAM blocks, with the data consistency checks for NVRAM blocks being performed by recalculating the CRC of the corresponding NV block.

- NvM模块应该提供错误恢复技术。错误恢复取决于NVRAM块管理类型，NvM模块应该通过加载默认值，为每种NVRAM块管理类型提供读时的错误恢复。

The NvM module should provide error recovery techniques. Error recovery depends on the NVRAM block management type; the NvM module should offer run-time error recovery for each NVRAM block management type by loading default values.

- NvM模块应该提供隐式和显式的恢复技术，以便在NV块的不可恢复的数据不一致的情况下，将ROM数据恢复到相应的RAM块中。在隐式恢复期间，相应NV块的数据内容保持不变。

The NvM module should provide both implicit and explicit recovery techniques to recover ROM data into the corresponding RAM blocks when irreversible data inconsistencies occur in NV blocks. During implicit recovery, the data content of the relevant NV block remains unchanged.

- NvM模块应该提供单块/多块请求的中止功能，该功能能通过配置项来决定是否使能，即是否配置相应的cancel函数。

The NvM module should provide the functionality to terminate single/multi-chunk requests, which can be enabled or disabled via configuration options, i.e., by configuring the corresponding cancel functions.

- NvM模块应该提供不同种类的可配置的写保护。每一种写保护都只与NVRAM块的NV部分相关，即RAM块数据可以修改，但不能写入NV内存。

The NVMe module should provide configurable write protection of different types. Each type of write protection is only related to the NV part of the NVRAM block, meaning that data in the RAM block can be modified but not written to NV memory.

参考资料 (Reference materials)
------------------------------------------

[1] AUTOSAR_SWS\_ FlashEEPROMEmulation.PDF，R19-11

[2] AUTOSAR_SWS\_ FlashDriver.PDF，R19-11

[3] AUTOSAR_SWS\_ MemoryAbstractionInterface.PDF，R19-11

[4] AUTOSAR_SWS\_ NVRAMManager.PDF，R19-11

功能描述 (Function Description)
===========================================

写数据功能 (Write data function)
-------------------------------------------

写数据功能介绍 (Data writing functionality)
====================================================

当接收到一个外部写数据调用后，NvM模块会根据请求的对应块的状态信息和当前队列信息进行入队列操作，然后NvM模块会在后台对队列进行进一步的处理，调用相应的下层接口，执行相应的判断等。

Upon receiving an external write data call, the NvM module will enqueue the operation based on the status information of the corresponding block and the current queue information. Then, the NvM module will further process the queue in the background, calling relevant lower-layer interfaces and performing相应的判断等.

写数据功能实现 (Data writing functionality implementation)
===================================================================

当NvM模块的NvM_WriteBlock、NvM_WritePRAMBlock、NvM_WriteAll接口被调用的时候，NvM模块会在调用接口里面进行一些入队列之前的判断，条件符合则将请求放入队列中，然后在NvM_MainFunction函数中进行出队列，并执行相应的请求的操作，符合条件之后会调用MemIf_Write接口进行后续的写操作。如果是轮询模式，则需要调用NvM模块的NvM_GetErrorStatus接口进行任务查询，然后下层执行完成则会返回NVM_REQ_OK，否则会一直返回NVM_REQ_PENDING。如果是回调模式，则NvM模块会在下层执行完成之后，在NvM_MainFunction函数中调用对应块的配置接口NvM_SingleBlockCallbackFunction通知用户执行完成。

When the NvM module's NvM_WriteBlock, NvM_WritePRAMBlock, and NvM_WriteAll interfaces are called, the NvM module performs some checks before queuing the request. If the conditions are met, it will enqueue the request. Then, in the NvM_MainFunction function, it dequeues and executes the corresponding operations. Once the conditions are satisfied, it calls the MemIf_Write interface for subsequent write operations. If in polling mode, the NvM module needs to call the NvM_GetErrorStatus interface to query the task status. Once the lower layer execution is completed, it will return NVM_REQ_OK; otherwise, it will continue to return NVM_REQ_PENDING. In callback mode, after the lower layer execution is complete, the NvM module will call the corresponding block's configuration interface, NvM_SingleBlockCallbackFunction, in the NvM_MainFunction function to notify the user that the operation has been completed.

读取数据功能 (Read data function)
-------------------------------------------

读取数据功能介绍 (Introduction to Data Reading Function)
================================================================

当接收到一个外部读取数据调用后，NvM模块会根据请求的对应块的状态信息和当前队列信息进行入队列操作，然后NvM模块会在后台对队列进行进一步的处理，调用相应的下层接口，执行相应的判断等。

Upon receiving an external read data call, the NvM module performs enqueue operations based on the status information of the corresponding block and the current queue information. Then, the NvM module processes the queue in the background, calling the appropriate lower-level interfaces and performing relevant judgments, etc.

读取数据功能实现 (Implementation of read data functionality)
====================================================================

当NvM模块的NvM_ReadBlock、NvM_ReadPRAMBlock、NvM_ReadAll接口被调用的时候，NvM模块会在调用接口里面进行一些入队列之前的判断，条件符合则将请求放入队列中，然后在NvM_MainFunction函数中进行出队列，并执行相应的请求的操作，符合条件之后会调用MemIf_Read接口进行后续的读操作。如果是轮询模式，则需要调用NvM模块的NvM_GetErrorStatus接口进行任务查询，然后下层执行完成则会返回NVM_REQ_OK，否则会一直返回NVM_REQ_PENDING。如果是回调模式，则NvM模块会在下层执行完成之后，在NvM_MainFunction函数中调用对应块的配置接口NvM_SingleBlockCallbackFunction通知用户执行完成。

When the NvM module's NvM_ReadBlock, NvM_ReadPRAMBlock, and NvM_ReadAll interfaces are called, the NvM module performs some checks before enqueuing the request. If the conditions are met, it places the request in the queue. Then, in the NvM_MainFunction function, it dequeues the requests and executes the corresponding operations. Once the conditions are satisfied, it calls the MemIf_Read interface for subsequent read operations.

In polling mode, the NvM module needs to call the NvM_GetErrorStatus interface of the NvM module to query the task status. If the lower layer execution is completed, it returns NVM_REQ_OK; otherwise, it continuously returns NVM_REQ_PENDING.

In callback mode, after the lower layer execution is completed, the NvM module calls the corresponding block's configuration interface, NvM_SingleBlockCallbackFunction, in the NvM_MainFunction function to notify the user that the task has been completed.

擦除数据功能 (Data erase function)
--------------------------------------------

擦除数据功能介绍 (Data erasure feature introduction)
============================================================

当接收到一个外部擦除数据调用后，NvM模块会根据请求的对应块的状态信息和当前队列信息进行入队列操作，然后NvM模块会在后台对队列进行进一步的处理，调用相应的下层接口，执行相应的判断等。

After receiving an external erase data call, the NvM module queues the operation based on the status information of the corresponding block and current queue information, then the NvM module processes the queue in the background, calling the appropriate lower-level interfaces and performing relevant judgments, etc.

擦除数据功能实现 (The data wiping feature implementation)
=================================================================

当NvM模块的NvM_EraseNvBlock接口被调用的时候，NvM模块会在调用接口里面进行一些入队列之前的判断，条件符合则将请求放入队列中，然后在NvM_MainFunction函数中进行出队列，并执行相应的请求的操作，符合条件之后会调用MemIf_EraseImmediateBlock接口进行后续的擦除操作。如果是轮询模式，则需要调用NvM模块的NvM_GetErrorStatus接口进行任务查询，然后下层执行完成则会返回NVM_REQ_OK，否则会一直返回NVM_REQ_PENDING。如果是回调模式，则NvM模块会在下层执行完成之后，在NvM_MainFunction函数中调用对应块的配置接口NvM_SingleBlockCallbackFunction通知用户执行完成。

When the NvM module's NvM_EraseNvBlock interface is called, the NvM module performs some checks before queuing the request. If the conditions are met, the request is added to the queue. In the NvM_MainFunction function, requests are dequeued and the corresponding operations are executed. Once the conditions are satisfied, the MemIf_EraseImmediateBlock interface is called for subsequent erase operations. If in polling mode, the NvM module needs to call the NvM_GetErrorStatus interface to query the task status. The lower layer will return NVM_REQ_OK upon completion; otherwise, it will continuously return NVM_REQ_PENDING. In callback mode, once the lower layer execution is complete, the NvM_MainFunction function calls the corresponding block's configuration interface NvM_SingleBlockCallbackFunction to notify the user of the task completion.

数据无效/有效功能 (Invalid/Valid Data Function)
-------------------------------------------------------

数据无效/有效功能介绍 (Invalid/Valid Data Function Introduction)
======================================================================

当接收到一个外部数据无效/有效调用后，NvM模块会根据请求的对应块的状态信息和当前队列信息进行入队列操作，然后NvM模块会在后台对队列进行进一步的处理，调用相应的下层接口，执行相应的判断等。

After receiving an invalid/call valid external data invocation, the NvM module performs an enqueue operation based on the state information of the requested block and the current queue information. Then, the NvM module processes the queue in the background by calling the corresponding lower-layer interfaces and executing relevant judgments, etc.

数据无效功能实现 (Invalid data functionality implementation)
====================================================================

当NvM模块的NvM_InvalidateNvBlock/NvM_ValidateAll接口被调用的时候，NvM模块会在调用接口里面进行一些入队列之前的判断，条件符合则将请求放入队列中，然后在NvM_MainFunction函数中进行出队列，并执行相应的请求的操作，符合条件之后会调用MemIf_InvalidateBlock接口进行后续的无效/有效操作。如果是轮询模式，则需要调用NvM模块的NvM_GetErrorStatus接口进行任务查询，然后下层执行完成则会返回NVM_REQ_OK，否则会一直返回NVM_REQ_PENDING。如果是回调模式，则NvM模块会在下层执行完成之后，在NvM_MainFunction函数中调用对应块的配置接口NvM_SingleBlockCallbackFunction通知用户执行完成。

When the NvM module's NvM_InvalidateNvBlock/NvM_ValidateAll interface is called, the NvM module performs some checks before enqueueing the request, and if the conditions are met, it places the request in the queue. Then, in the NvM_MainFunction function, the request is dequeued and the corresponding operations are executed. If the conditions are met after that, it will call the MemIf_InvalidateBlock interface to perform subsequent invalidation/validation operations. If polling mode is used, the NvM_GetErrorStatus interface of the NvM module needs to be called for task queries, and once the lower layer execution is complete, it will return NVM_REQ_OK; otherwise, it will continue to return NVM_REQ_PENDING. If callback mode is used, the NvM module will call the corresponding block's configuration interface NvM_SingleBlockCallbackFunction in the NvM_MainFunction function after the lower layer execution is completed to notify the user that the operation has been completed.

数据恢复功能 (Data recovery feature)
----------------------------------------------

数据恢复功能介绍 (Introduction to Data Recovery Features)
=================================================================

当接收到一个外部数据恢复调用后，NvM模块会根据请求的对应块的状态信息和当前队列信息进行入队列操作，然后NvM模块会在后台对队列进行进一步的处理，调用相应的下层接口，执行相应的判断等。

After receiving an external data recovery call, the NvM module performs enqueue operations based on the state information of the requested block and the current queue information. Then, the NvM module processes the queue in the background, calling corresponding lower-level interfaces and performing relevant judgments, etc.

数据恢复功能实现 (Data recovery functionality implementation)
=====================================================================

当NvM模块的NvM_RestoreBlockDefaults、NvM_RestorePRAMBlockDefaults接口被调用的时候，NvM模块会在调用接口里面进行一些入队列之前的判断，条件符合则将请求放入队列中，然后在NvM_MainFunction函数中进行出队列，并执行相应的请求的操作。如果是轮询模式，则需要调用NvM模块的NvM_GetErrorStatus接口进行任务查询，然后执行完成则会返回NVM_REQ_OK，否则会一直返回NVM_REQ_PENDING。如果是回调模式，则NvM模块会在执行完成之后，在NvM_MainFunction函数中调用对应块的配置接口NvM_SingleBlockCallbackFunction通知用户执行完成。

When the NvM module's NvM_RestoreBlockDefaults and NvM_RestorePRAMBlockDefaults interfaces are called, the NvM module performs some pre-enqueue checks within the interface call. If the conditions are met, it places the request in the queue, then dequeues and executes the corresponding request in the NvM_MainFunction function. If polling mode is used, a task query needs to be performed by calling the NvM_GetErrorStatus interface of the NvM module. The function will return NVM_REQ_OK upon completion; otherwise, it will continue to return NVM_REQ_PENDING. In callback mode, the NvM module invokes the corresponding block's configuration interface NvM_SingleBlockCallbackFunction in the NvM_MainFunction function to notify the user of completion after the execution is finished.

多块写取消功能 (Multi-write cancellation feature)
----------------------------------------------------------

多块写取消功能介绍 (Multi-write cancellation feature introduction)
=========================================================================

当接收到一个外部数据多块写取消调用后，NvM模块会根据请求的对应块的状态信息和当前队列信息进行入队列操作，然后NvM模块会在后台对队列进行进一步的处理，调用相应的下层接口，执行相应的判断等。然后在执行过程中NvM模块接收到NvM_CancelWriteAll接口调用，则会取消正在进行的多块写操作。

Upon receiving a multi-block write cancel call, the NvM module queues the operation based on the status information of the requested blocks and current queue info, then performs further processing on the queue in the background by calling corresponding lower-layer interfaces and executing relevant judgments. If during execution the NvM_CancelWriteAll interface is called, the ongoing multi-block write operation will be canceled.

多块写取消功能实现 (Multi-write abort functionality implementation)
==========================================================================

当NvM模块的NvM_WriteAll接口被调用的时候，NvM模块会在调用接口里面进行一些入队列之前的判断，条件符合则将请求放入队列中，然后在NvM_MainFunction函数中进行出队列，并执行相应的请求的操作。如果在执行过程中NvM模块接收到NvM_CancelWriteAll接口调用，则会取消正在进行的多块写操作。如果是轮询模式，则需要调用NvM模块的NvM_GetErrorStatus接口进行任务查询，会返回NVM_REQ_CANCELED。如果是回调模式，在NvM_MainFunction函数中调用对应块的配置接口NvM_SingleBlockCallbackFunction通知用户NVM_REQ_CANCELED。

When the NvM module's NvM_WriteAll interface is called, the NvM module performs some checks before queuing the request. If the conditions are met, the request is placed in the queue and then dequeued and executed in the NvM_MainFunction function. If the NvM module receives a call to the NvM_CancelWriteAll interface during execution, it will cancel the ongoing multi-block write operation. In polling mode, the NvM_GetErrorStatus interface of the NvM module needs to be called for task queries, which returns NVM_REQ_CANCELED. In callback mode, the corresponding block's configuration interface NvM_SingleBlockCallbackFunction is called in the NvM_MainFunction function to notify the user of NVM_REQ_CANCELED.

支持Dem同步功能 (Support Dem synchronization function)
----------------------------------------------------------------

当Dem有存储需要的时候，Dem模块会执行同步功能，使NvM会自动创建对应长度与个数的NvMBlock，实现快速同步Dem信息的作用。

When Dem has storage requirements, the Dem module performs a synchronization function, causing NvM to automatically create corresponding NvMBlocks in terms of length and quantity, achieving the purpose of rapid synchronization of Dem information.

源文件描述 (Source file description)
===============================================

.. centered:: **表 NvM组件文件描述 (NvM Component File Description)**

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 文件 (Files)
     - 说明 (Description)
   * - NvM_Cfg.h
     - 定义NvM模块预编译时用到的配置参数。 (Define configuration parameters used for pre-compilation of the NvM module.)
   * - NvM_Cfg.c
     - 定义NvM模块配置相关的配置参数。 (Define configuration parameters related to NvM module configuration.)
   * - NvM.h
     - NvM模块头文件，包含了API函数的扩展声明并定义了端口的数据结构。 (NVM module header file, which contains extended declarations of API functions and defines the data structures of ports.)
   * - NvM .c
     - NvM模块源文件，包含了API函数的实现。 (NvM module source files, contain the implementation of API functions.)
   * - NvM_MemMap.h
     - 包含NvM模块的内存抽象。 (Abstraction of memory with NvM module.)
   * - NvM_Types.h
     - 包含NvM模块需要使用的类型定义。 (Contain type definitions needed for the NvM module.)
   * - NvM_Inter.c
     - NvM模块内部处理调用的相关API函数实现。 (The API functions for handling calls within the NvM module are implemented.)
   * - NvM_Inter.h
     - NvM模块内部处理调用的相关API函数声明。 (The API function declarations for handling calls within the NvM module.)
   * - NvM_Cbk.h
     - NvM模块回调接口相关头文件，包含了回调接口相关API函数的扩展声明并定义了端口的数据结构。(在FEE/EA模块中引用) (Header file related to NvM module callback interfaces, which includes extended declarations and definitions of API functions for callback interfaces and port data structures (referenced in the FEE/EA module).)




.. figure:: ../../_static/参考手册(Module_Reference_Manual)/NvM/image2.png
   :alt: NvM组件文件交互关系图 (NVM Component File Interactions Diagram)
   :name: NvM组件文件交互关系图 (NVM Component File Interactions Diagram)
   :align: center


API接口 (API Interface)
=====================================

类型定义 (Type definition)
--------------------------------------

导入类型定义 (Import type definitions)
================================================

NvM_ConfigType类型定义 (NvM_ConfigType Type Definition)
-------------------------------------------------------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 名称 (Name)
     - NvM_ConfigType
   * - 类型 (Type)
     - Structure
   * - 范围 (Range)
     - 无
   * - 描述 (Description)
     - 配置参数结构体类型定义 (Definition of configuration parameter structure type)




NvM_MultiBlockRequestType类型定义 (NvM_MultiBlockRequestType Type Definition)
-----------------------------------------------------------------------------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 名称 (Name)
     - NvM_MultiBlockRequestType
   * - 类型 (Type)
     - Enumeration
   * - 范围 (Range)
     - 执行多块读操作：NVM_READ_ALL = 0 (Execute multiple reads: NVM_READ_ALL = 0)
   * - 
     - 执行多块写操作：NVM_WRITE_ALL = 1 (Perform multiple write operations: NVM_WRITE_ALL = 1)
   * - 
     - 执行多块有效操作：NVM_VALIDATE_ALL = 2 (Execute multiple valid operations: NVM_VALIDATE_ALL = 2)
   * - 
     - 执行多块第一次初始化操作：NVM_FIRST_INIT_ALL = 3 (Perform multiple first-time initialization operations: NVM_FIRST_INIT_ALL = 3)
   * - 
     - 执行多块取消写操作：NVM_CANCEL_WRITE_ALL = 4 (Execute multiple cancel write operations: NVM_CANCEL_WRITE_ALL = 4)
   * - 描述 (Description)
     - 标识通过回调函数发出信号或向BswM报告时在多个块上执行的请求类型 (Identify request types that are executed across multiple blocks when signals are emitted via callback functions or reported to BswM.)




实现数据类型定义 (Define data types)
============================================

NvM_RequestResultType类型定义 (NvM_RequestResultType Type Definition)
---------------------------------------------------------------------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 名称 (Name)
     - NvM_RequestResultType
   * - 类型 (Type)
     - uint8
   * - 范围 (Range)
     - 上一次异步请求已成功完成，NVM_REQ_OK = 0 (The last asynchronous request has successfully completed, NVM_REQ_OK = 0)
   * - 
     - 上一次异步读/写/控制请求未成功完成，NVM_REQ_NOT_OK = 1 (The last asynchronous read/write/control request did not complete successfully, NVM_REQ_NOT_OK = 1)
   * - 
     - 当前正在等待异步读/写/控制挂起，NVM_REQ_PENDING = 2 (Current waiting for asynchronous read/write/control suspension, NVM_REQ_PENDING = 2)
   * - 
     - 上一次异步请求的数据完整性失败，NVM_REQ_INTEGRITY_FAILED=3 (The integrity check failed for the last asynchronous request, NVM_REQ_INTEGRITY_FAILED=3)
   * - 
     - NvM_ReadAll或NvM_WriteAll请求的块被跳过，NVM_REQ_BLOCK_SKIPPED= 4 (NvM_ReadAll or NvM_WriteAll requests have blocks skipped, NVM_REQ_BLOCK_SKIPPED = 4)
   * - 
     - 引用的NV块无效，NVM_REQ_NV_INVALIDATED = 5 (Invalid NV block referenced, NVM_REQ_NV_INVALIDATED = 5)
   * - 
     - NvM_CancelWriteAll取消多块请求，NVM_REQ_CANCELED = 6 (NvM_CancelWriteAll Cancel Multi-Block Requests, NVM_REQ_CANCELED = 6)
   * - 
     - 引用的NV块将默认值复制到RAM映像中，NVM_REQ_RESTORED_FROM_ROM= 8 (The NV block will copy default values into the RAM image, NVM_REQ_RESTORED_FROM_ROM = 8)
   * - 描述 (Description)
     - 调用NvM_GetErrorStatus返回的异步请求结果 (Return result of asynchronous request obtained via NvM_GetErrorStatus)




NvM_BlockIdType类型定义 (NvM_BlockIdType Type Definition)
---------------------------------------------------------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 名称 (Name)
     - NvM_BlockIdType
   * - 类型 (Type)
     - uint16
   * - 范围 (Range)
     - 0..2^(16-NvMDatasetSelectionBits)-1
   * - 描述 (Description)
     - 通过一个唯一的块标识符来标识一个NVRAM块。 (Identify an NVRAM block with a unique block identifier.)
   * - 
     - 保留NVRAM块id： (Preserve NVRAM block id:)
   * - 
     - 0：通过NvM_GetErrorStatus派生多个块请求结果 (Derive multiple block request results through NvM_GetErrorStatus)
   * - 
     - 1：冗余NVRAM块，它保存配置ID (1: Redundant NVRAM block, it saves configuration ID)




NvM_InitBlockRequestType类型定义 (Type definition for NvM_InitBlockRequestType)
-------------------------------------------------------------------------------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 名称 (Name)
     - NvM_InitBlockRequestType
   * - 类型 (Type)
     - uint8
   * - 范围 (Range)
     - 请求NvM_ReadBlock/ NvM_ReadPRAMBlock服务， (Request NvM_ReadBlock/NvM_ReadPRAMBlock service,)
   * - 
     - NVM_INIT_READ_BLOCK = 0；
   * - 
     - 请求NvM_RestoreBlockDefaults/NvM_RestorePRAMBlockDefaults服务，NVM_INIT_RESTORE_BLOCK_DEFAULTS= 1； (Request NvM_RestoreBlockDefaults/NvM_RestorePRAMBlockDefaults service, NVM_INIT_RESTORE_BLOCK_DEFAULTS = 1;)
   * - 
     - NvM_ReadAll正在处理这个块，NVM_INIT_READ_ALL_BLOCK = 2； (NVMe_ReadAll is processing this block, NVM_INIT_READ_ALL_BLOCK = 2;)
   * - 
     - NvM_FirstInitAll正在处理这个块NVM_INIT_FIRST_INIT_ALL =3； (NvM_FirstInitAll is processing this block NVM_INIT_FIRST_INIT_ALL = 3;)
   * - 描述 (Description)
     - 标识通过回调函数发出信号时在块上执行的请求类型 (Indicate the request type executed on the block when signaling with a callback function)




NvM_BlockRequestType类型定义 (NvM_BlockRequestType Type Definition)
-------------------------------------------------------------------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 名称 (Name)
     - NvM_BlockRequestType
   * - 类型 (Type)
     - uint8
   * - 范围 (Range)
     - NvM_ReadBlock/ NvM_ReadPRAMBlock服务已执行， (NvM_ReadBlock/ NvM_ReadPRAMBlock service has been executed,)
   * - 
     - NVM_READ_BLOCK = 0；
   * - 
     - NvM_WriteBlock/ NvM_WritePRAMBlock服务已执行， (The NvM_WriteBlock/ NvM_WritePRAMBlock service has been executed,)
   * - 
     - NVM_WRITE_BLOCK = 1；
   * - 
     - NvM_RestoreBlockDefaults/NvM_RestorePRAMBlockDefaults服务已执行，NVM_RESTORE_BLOCK_DEFAULTS= 2； (The NvM_RestoreBlockDefaults/NvM_RestorePRAMBlockDefaults service has been executed, NVM_RESTORE_BLOCK_DEFAULTS = 2;)
   * - 
     - NvM_EraseNvBlock服务已执行，NVM_ERASE_NV_BLOCK = 3； (The NvM_EraseNvBlock service has been executed, NVM_ERASE_NV_BLOCK = 3;)
   * - 
     - NvM_InvalidateNvBlock服务已执行，NVM_INVALIDATE_NV_BLOCK= 4； (NvM_InvalidateNvBlock service has executed, NVM_INVALIDATE_NV_BLOCK = 4;)
   * - 
     - NvM_ReadAll已经完成对这个块的处理，NVM_READ_ALL_BLOCK =5； (NVM_ReadAll has completed processing this block, NVM_READ_ALL_BLOCK = 5;)
   * - 描述 (Description)
     - 标识通过回调函数发出信号时在块上执行的请求类型 (Indicate the request type executed on the block when signaling with a callback function)




输入函数描述 (Describe the input function:)
-----------------------------------------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 输入模块 (Input Module)
     - API
   * - DET
     - Det_ReportError
   * - 
     - Det_ReportRuntimeError
   * - MemIf
     - MemIf_Cancel
   * - 
     - MemIf_EraseImmediateBlock
   * - 
     - MemIf_GetJobResult
   * - 
     - MemIf_GetStatus
   * - 
     - MemIf_InvalidateBlock
   * - 
     - MemIf_Read
   * - 
     - MemIf_Write
   * - 
     - MemIf_SetMode
   * - CRC
     - Crc_CalculateCRC16
   * - 
     - Crc_CalculateCRC32
   * - 
     - Crc_CalculateCRC8
   * - ECUM
     - EcuM_CB_NfyNvMJobEnd
   * - BswM
     - BswM_NvM_CurrentBlockMode
   * - 
     - BswM_NvM_CurrentJobMode




静态接口函数定义 (Static interface function definition)
---------------------------------------------------------------

NvM_Init函数定义 (The NvM_Init function definition)
===============================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - NvM_Init
     - 
     - 
   * - 函数原型： (Function prototype:)
     - FUNC(void, NVM_CODE)NvM_Init(constNvM_ConfigType\*ConfigPtr)
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
     - ConfigPtr：配置数据结构体的指针 (ConfigPtr：Pointer to the configuration data structure)
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
     - 初始化NVM模块变量 (Initialize NVM module variables)
     - 
     - 




NvM_SetDataIndex函数定义 (The NvM_SetDataIndex function defines)
============================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - NvM_SetDataIndex
     - 
     - 
   * - 函数原型： (Function prototype:)
     - FUNC(Std_ReturnType, NVM_CODE)NvM_SetDataIndex(NvM_BlockIdTypeBlockId, uint8 DataIndex)
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
     - BlockId：NVRAM块唯一描述符 (BlockId：Unique Descriptor for NVRAM Block)
     - 值域： (Domain:)
     - 0..65535
   * - 
     - DataIndex：NV/ROM块的索引位置 (DataIndex：Index position of NV/ROM block)
     - 值域： (Domain:)
     - 0..255
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无
     - 
     - 
   * - 返回值： (Return Value:)
     - Std_ReturnType：E_OK: The indexposition was set successfully.
     - 
     - 
   * - 
     - E_NOT_OK: An error occurred.
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 设置指定块的索引值 (Set the index value of the specified block)
     - 
     - 




NvM_GetDataIndex函数定义 (The NvM_GetDataIndex function definition)
===============================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - NvM_GetDataIndex
     - 
     - 
   * - 函数原型： (Function prototype:)
     - FUNC(Std_ReturnType, NVM_CODE)
     - 
     - 
   * - 
     - NvM_GetDataIndex(NvM_BlockIdTypeBlockId, P2VAR(uint8,AUTOMATIC, NVM_APPL_DATA)DataIndexPtr)
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
     - 是 (Is)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - BlockId：NVRAM块唯一描述符 (BlockId：Unique Descriptor for NVRAM Block)
     - 值域： (Domain:)
     - 0.
   * - 
     - 
     - 
     - .65535
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - DataIndexPtr：NV/ROM块的索引位置 (DataIndexPtr: Index position of NV/ROM block)
     - 
     - 
   * - 返回值： (Return Value:)
     - Std_ReturnType：
     - 
     - 
   * - 
     - E_OK：成功 (E_OK: Success)
     - 
     - 
   * - 
     - E_NOT_OK：失败 (E_NOT_OK: Failure)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 获取指定块的索引值 (Get the index value of the specified block)
     - 
     - 




NvM_SetBlockProtection函数定义 (The NvM_SetBlockProtection function definition)
===========================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - NvM_SetBlockProtection
     - 
     - 
   * - 函数原型： (Function prototype:)
     - FUNC(Std_ReturnType,NVM_CODE)NvM_SetBlockProtection(NvM_BlockIdTypeBlockId, booleanProtectionEnabled)
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
     - 是 (Is)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - BlockId：NVRAM块唯一描述符 (BlockId：Unique Descriptor for NVRAM Block)
     - 值域： (Domain:)
     - 0..65535
   * - 
     - ProtectionEnabled：写保护标志 (ProtectionEnabled: Write Protection Flag)
     - 值域： (Domain:)
     - TRUE/FALSE
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无
     - 
     - 
   * - 返回值： (Return Value:)
     - Std_ReturnType：
     - 
     - 
   * - 
     - E_OK：请求成功 (E_OK: Request succeeded)
     - 
     - 
   * - 
     - E_NOT_OK：请求失败 (E_NOT_OK: Request failed)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 设置/重置块保护 (Set/Reset Block Protection)
     - 
     - 




NvM_GetErrorStatus函数定义 (The NvM_GetErrorStatus function definition)
===================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - NvM_GetErrorStatus
     - 
     - 
   * - 函数原型： (Function prototype:)
     - FUNC(Std_ReturnType,NVM_CODE)
     - 
     - 
   * - 
     - NvM_GetErrorStatus(NvM_BlockIdTypeBlockId,NvM_RequestResultType\*RequestResultPtr)
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
     - 是 (Is)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - BlockId：NVRAM块唯一描述符 (BlockId：Unique Descriptor for NVRAM Block)
     - 值域： (Domain:)
     - 0..65535
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - RequestResultPtr：请求结果 (RequestResultPtr: Request Result)
     - 
     - 
   * - 返回值： (Return Value:)
     - Std_ReturnType：
     - 
     - 
   * - 
     - E_OK：请求成功 (E_OK: Request succeeded)
     - 
     - 
   * - 
     - E_NOT_OK：请求失败 (E_NOT_OK: Request failed)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 获取指定块的处理结果 (Get the processing result of the specified block)
     - 
     - 




NvM_GetVersionInfo函数定义 (The NvM_GetVersionInfo function definition)
===================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - NvM_GetVersionInfo
     - 
     - 
   * - 函数原型： (Function prototype:)
     - voidNvM_GetVersionInfo(Std_VersionInfoType\*versioninfo)
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
     - 无
     - 值域： (Domain:)
     - 无
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - versioninfo：版本信息 (versioninfo：Version Information)
     - 
     - 
   * - 返回值： (Return Value:)
     - 无
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 获取NvM模块版本信息 (Get NVMe Module Version Information)
     - 
     - 




NvM_SetRamBlockStatus函数定义 (The NvM_SetRamBlockStatus function definition)
=========================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - NvM_SetRamBlockStatus
     - 
     - 
   * - 函数原型： (Function prototype:)
     - FUNC(Std_ReturnType,NVM_CODE)NvM_SetRamBlockStatus(NvM_BlockIdTypeBlockId, booleanBlockChanged)
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
     - 是 (Is)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - BlockChanged： 有效改变标志 (BlockChanged： Indicator of valid changes)
     - 值域： (Domain:)
     - TRUE/FALSE
   * - 
     - BlockId：NVRAM块唯一描述符 (BlockId：Unique Descriptor for NVRAM Block)
     - 值域： (Domain:)
     - 0..65535
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无
     - 
     - 
   * - 返回值： (Return Value:)
     - Std_ReturnType：
     - 
     - 
   * - 
     - E_OK: The status of thepermanent RAM block or theexplicit synchronization waschanged as requested.
     - 
     - 
   * - 
     - E_NOT_OK: An error occurred.
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 设置永久内存块的状态或NVRAM块显式同步的状态 (Set the state of permanent memory blocks or explicitly synchronize NVRAM blocks.)
     - 
     - 




NvM_SetBlockLockStatus函数定义 (The NvM_SetBlockLockStatus function definition)
===========================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - NvM_SetBlockLockStatus
     - 
     - 
   * - 函数原型： (Function prototype:)
     - FUNC(void, NVM_CODE)NvM_SetBlockLockStatus(NvM_BlockIdTypeBlockId, booleanBlockLocked)
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x13
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
     - BlockLocked：上锁标志 (BlockLocked：Lock Flag)
     - 值域： (Domain:)
     - TRUE/FALSE
   * - 
     - BlockId：NVRAM块唯一描述符 (BlockId：Unique Descriptor for NVRAM Block)
     - 值域： (Domain:)
     - 0..65535
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
     - 设置永久RAM块或NVRAM块显式同步的锁状态 (The lock state for explicitly synchronizing permanent RAM or NVRAM blocks)
     - 
     - 




NvM_CancelJobs函数定义 (The NvM_CancelJobs function definition)
===========================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - NvM_CancelJobs
     - 
     - 
   * - 函数原型： (Function prototype:)
     - FUNC(Std_ReturnType,NVM_CODE)NvM_CancelJobs(NvM_BlockIdTypeBlockId)
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
     - BlockId：NVRAM块唯一描述符 (BlockId：Unique Descriptor for NVRAM Block)
     - 值域： (Domain:)
     - 0..65535
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无
     - 
     - 
   * - 返回值： (Return Value:)
     - Std_ReturnType：
     - 
     - 
   * - 
     - E_OK：取消请求成功 (E_OK: Request cancellation succeeded)
     - 
     - 
   * - 
     - E_NOT_OK：取消请求失败 (E_NOT_OK: Failed to cancel request)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 取消指定块之前的请求 (Cancel request before the specified block)
     - 
     - 




NvM_ReadBlock函数定义 (NvM_ReadBlock Function Definition)
=====================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - NvM_ReadBlock
     - 
     - 
   * - 函数原型： (Function prototype:)
     - FUNC(Std_ReturnType, NVM_CODE)NvM_ReadBlock(NvM_BlockIdTypeBlockId, void\* NvM_DstPtr)
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
     - 是 (Is)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - BlockId：NVRAM块唯一描述符 (BlockId：Unique Descriptor for NVRAM Block)
     - 值域： (Domain:)
     - 0.
   * - 
     - 
     - 
     - .65535
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - NvM_DstPtr：RAM数据块地址 (NvM_DstPtr: RAM data block address)
     - 
     - 
   * - 返回值： (Return Value:)
     - Std_ReturnType：
     - 
     - 
   * - 
     - E_OK：请求成功 (E_OK: Request succeeded)
     - 
     - 
   * - 
     - E_NOT_OK：请求失败 (E_NOT_OK: Request failed)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 将NV块的数据复制到其相应的RAM块 (Copy the data of NV block to its corresponding RAM block)
     - 
     - 




NvM_WriteBlock函数定义 (The NvM_WriteBlock function definition)
===========================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - NvM_WriteBlock
     - 
     - 
   * - 函数原型： (Function prototype:)
     - FUNC(Std_ReturnType,NVM_CODE)NvM_WriteBlock(NvM_BlockIdTypeBlockId, void\*NvM_SrcPtr)
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
     - 是 (Is)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - NvM_SrcPtr：
     - 值域： (Domain:)
     - 无
   * - 
     - 指向RAM数据块的指针 (Pointer to RAM data block)
     - 
     - 
   * - 
     - BlockId：NVRAM块唯一描述符 (BlockId：Unique Descriptor for NVRAM Block)
     - 值域： (Domain:)
     - 0..65535
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无
     - 
     - 
   * - 返回值： (Return Value:)
     - Std_ReturnType：
     - 
     - 
   * - 
     - E_OK：请求成功 (E_OK: Request succeeded)
     - 
     - 
   * - 
     - E_NOT_OK：请求失败 (E_NOT_OK: Request failed)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 将RAM块的数据复制到其相应的NV块。 (Copy the data of the RAM block to its corresponding NV block.)
     - 
     - 




NvM_RestoreBlockDefaults函数定义 (The NvM_RestoreBlockDefaults function definition)
===============================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - NvM_RestoreBlockDefaults
     - 
     - 
   * - 函数原型： (Function prototype:)
     - FUNC(Std_ReturnType, NVM_CODE)NvM_RestoreBlockDefaults(NvM_BlockIdTypeBlockId, void\* NvM_DestPtr)
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x08
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
     - BlockId：NVRAM块唯一描述符 (BlockId：Unique Descriptor for NVRAM Block)
     - 值域： (Domain:)
     - 0..65535
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - NvM_DestPtr：RAM数据块地址 (NvM_DestPtr: RAM data block address)
     - 
     - 
   * - 返回值： (Return Value:)
     - Std_ReturnType：
     - 
     - 
   * - 
     - E_OK：请求成功 (E_OK: Request succeeded)
     - 
     - 
   * - 
     - E_NOT_OK：请求失败 (E_NOT_OK: Request failed)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 请求将指定块恢复为默认数据 (Request to restore the specified block to default data)
     - 
     - 




NvM_EraseNvBlock函数定义 (The definition of NvM_EraseNvBlock function)
==================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - NvM_EraseNvBlock
     - 
     - 
   * - 函数原型： (Function prototype:)
     - FUNC(Std_ReturnType, NVM_CODE)NvM_EraseNvBlock(NvM_BlockIdTypeBlockId)
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
     - 是 (Is)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - BlockId：NVRAM块唯一描述符 (BlockId：Unique Descriptor for NVRAM Block)
     - 值域： (Domain:)
     - 0..65535
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无
     - 
     - 
   * - 返回值： (Return Value:)
     - Std_ReturnType：
     - 
     - 
   * - 
     - E_OK：请求成功 (E_OK: Request succeeded)
     - 
     - 
   * - 
     - E_NOT_OK：请求失败 (E_NOT_OK: Request failed)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 请求擦除指定块 (Request to erase specified block)
     - 
     - 




NvM_CancelWriteAll函数定义 (The definition of NvM_CancelWriteAll function)
======================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - NvM_CancelWriteAll
     - 
     - 
   * - 函数原型： (Function prototype:)
     - FUNC(void,NVM_CODE)NvM_CancelWriteAll(void)
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x0a
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
     - 请求取消全写任务 (Request to cancel full spelling task)
     - 
     - 




NvM_InvalidateNvBlock函数定义 (The function definition for NvM_InvalidateNvBlock)
=============================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - NvM_InvalidateNvBlock
     - 
     - 
   * - 函数原型： (Function prototype:)
     - FUNC(Std_ReturnType, NVM_CODE)NvM_InvalidateNvBlock(NvM_BlockIdTypeBlockId)
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x0b
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 异步 (Asynchronous)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 是 (Is)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - BlockId：NVRAM块唯一描述符 (BlockId：Unique Descriptor for NVRAM Block)
     - 值域： (Domain:)
     - 0.
   * - 
     - 
     - 
     - .65535
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无
     - 
     - 
   * - 返回值： (Return Value:)
     - Std_ReturnType：
     - 
     - 
   * - 
     - E_OK：请求成功 (E_OK: Request succeeded)
     - 
     - 
   * - 
     - E_NOT_OK：请求失败 (E_NOT_OK: Request failed)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 无效化指定块 (Invalidates the specified block)
     - 
     - 




NvM_ReadPRAMBlock函数定义 (The function definition for NvM_ReadPRAMBlock)
=====================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - NvM_ReadPRAMBlock
     - 
     - 
   * - 函数原型： (Function prototype:)
     - FUNC(Std_ReturnType,NVM_CODE)NvM_ReadPRAMBlock(NvM_BlockIdTypeBlockId)
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x16
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 异步 (Asynchronous)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 是 (Is)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - BlockId：NVRAM块唯一描述符 (BlockId：Unique Descriptor for NVRAM Block)
     - 值域： (Domain:)
     - 0..65535
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无
     - 
     - 
   * - 返回值： (Return Value:)
     - Std_ReturnType：
     - 
     - 
   * - 
     - E_OK：请求成功 (E_OK: Request succeeded)
     - 
     - 
   * - 
     - E_NOT_OK：请求失败 (E_NOT_OK: Request failed)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 请求拷贝指定块数据到配置的RAM (Request copy specified block data to configured RAM)
     - 
     - 




NvM_WritePRAMBlock函数定义 (The definition of NvM_WritePRAMBlock function)
======================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - NvM_WritePRAMBlock
     - 
     - 
   * - 函数原型： (Function prototype:)
     - FUNC(Std_ReturnType, NVM_CODE)NvM_WritePRAMBlock(NvM_BlockIdTypeBlockId)
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x17
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 异步 (Asynchronous)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 是 (Is)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - BlockId：NVRAM块唯一描述符 (BlockId：Unique Descriptor for NVRAM Block)
     - 值域： (Domain:)
     - 0..65535
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无
     - 
     - 
   * - 返回值： (Return Value:)
     - Std_ReturnType：
     - 
     - 
   * - 
     - E_OK：请求成功 (E_OK: Request succeeded)
     - 
     - 
   * - 
     - E_NOT_OK：请求失败 (E_NOT_OK: Request failed)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 请求将PRAM数据放入指定的NV块 (Request to place PRAM data into the designated NV block)
     - 
     - 




NvM_RestorePRAMBlockDefaults函数定义 (The function definition for NvM_RestorePRAMBlockDefaults)
===========================================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - NvM_RestorePRAMBlockDefaults
     - 
     - 
   * - 函数原型： (Function prototype:)
     - FUNC(Std_ReturnType,NVM_CODE)NvM_RestorePRAMBlockDefaults(NvM_BlockIdTypeBlockId)
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x18
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
     - BlockId：NVRAM块唯一描述符 (BlockId：Unique Descriptor for NVRAM Block)
     - 值域： (Domain:)
     - 0..65535
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无
     - 
     - 
   * - 返回值： (Return Value:)
     - Std_ReturnType：
     - 
     - 
   * - 
     - E_OK：请求成功 (E_OK: Request succeeded)
     - 
     - 
   * - 
     - E_NOT_OK：请求失败 (E_NOT_OK: Request failed)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 请求将PRAM数据恢复为默认数据 (Request to Restore PRAM Data to Default)
     - 
     - 




NvM_ReadAll函数定义 (The definition of NvM_ReadAll function)
========================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - NvM_ReadAll
     - 
     - 
   * - 函数原型： (Function prototype:)
     - FUNC(void,NVM_CODE)NvM_ReadAll(void)
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x0c
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
     - 请求读取所有块 (Request to read all blocks)
     - 
     - 




NvM_WriteAll函数定义 (NvM_WriteAll function definition)
===================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - NvM_WriteAll
     - 
     - 
   * - 函数原型： (Function prototype:)
     - FUNC(void,NVM_CODE)NvM_WriteAll(void)
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x0d
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
     - 请求对所有块进行写 (Request to write all blocks)
     - 
     - 




NvM_ValidateAll函数定义 (The NvM_ValidateAll function definition)
=============================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - NvM_ValidateAll
     - 
     - 
   * - 函数原型： (Function prototype:)
     - FUNC(void,NVM_CODE)NvM\_ValidateAll(void)
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x19
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
     - 请求将指定块无效化 (Invalidate the specified block)
     - 
     - 




NvM_JobEndNotification函数定义 (The NvM_JobEndNotification function definition)
===========================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - NvM_JobEndNotification
     - 
     - 
   * - 函数原型： (Function prototype:)
     - FUNC(void,NVM_CODE)NvM_JobEndNotification(void)
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
     - 任务完成回调 (Task completion callback)
     - 
     - 




NvM_JobErrorNotification函数定义 (The NvM_JobErrorNotification function definition)
===============================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - NvM_JobErrorNotification
     - 
     - 
   * - 函数原型： (Function prototype:)
     - FUNC(void,NVM_CODE)NvM_JobErrorNotification(void)
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
     - 任务错误回调 (Task error callback)
     - 
     - 




NvM_MainFunction函数定义 (NvM_MainFunction function definition)
===========================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - NvM_MainFunction
     - 
     - 
   * - 函数原型： (Function prototype:)
     - FUNC(void,NVM_CODE)NvM_MainFunction(void)
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
     - 主函数处理任务 (The main function handles tasks.)
     - 
     - 




可配置函数定义 (Configurable Function Definition)
----------------------------------------------------------

NvM_SingleBlockCallbackFunction函数定义 (NvM_SingleBlockCallbackFunction Function Definition)
=========================================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称 (Function Name)
     - NvM_SingleBlockCallbackFunction
     - 
     - 
   * - 函数原型 (Function prototype)
     - Std_ReturnTypeNvM_SingleBlockCallbackFunction(uint8ServiceId,NvM_RequestResultTypeJobResult)
     - 
     - 
   * - 服务编号 (Service Number)
     - 无
     - 
     - 
   * - 同步/异步 (Synchronous/Asynchronous)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入 (Is it reentrant?)
     - 否 (No)
     - 
     - 
   * - 输入参数 (Input parameters)
     - BlockRequest：单个块的请求类型 (BlockRequest: Type of request for a single block)
     - 值域： (Domain:)
     - NVM_INIT_READ_BLOCK,NVM_INIT_RESTORE_BLOCK_DEFAULTS,NVM_INIT_READ_ALL_BLOCK,NVM_INIT_FIRST_INIT_ALL
   * - 
     - JobResult：以前处理的单个块请求的任务结果 (JobResult：The task result of a single block request processed before)
     - 值域： (Domain:)
     - NVM_REQ_OKNVM_REQ_NOT_OK
   * - 
     - 
     - 
     - NVM_REQ_PENDING
   * - 
     - 
     - 
     - NVM_REQ_INTEGRITY_FAILED
   * - 
     - 
     - 
     - NVM_REQ_BLOCK_SKIPPED
   * - 
     - 
     - 
     - NVM_REQ_NV_INVALIDATED
   * - 
     - 
     - 
     - NVM_REQ_CANCELED
   * - 
     - 
     - 
     - NVM_REQ_REDUNDANCY_FAILED
   * - 
     - 
     - 
     - NVM_REQ_RESTORED_FROM_ROM
   * - 输入输出参数 (Input Output Parameters)
     - 无
     - 
     - 
   * - 输出参数
     - 无
     - 
     - 
   * - 返回值 (Return value)
     - Std_ReturnType：E_OK：回调函数已被成功处理 (Std_ReturnType：E_OK：The callback function has been handled successfully)
     - 
     - 
   * - 
     - E_NOT_OK：回调函数没有被成功处理 (E_NOT_OK: The callback function was not processed successfully)
     - 
     - 
   * - 功能概述 (Function Overview)
     - 块回调通知上层一个异步单个块请求已经完成 (Notify the upper layer that an asynchronous single block request has completed)
     - 
     - 




NvM_MultiBlockCallbackFunction函数定义 (The definition of NvM_MultiBlockCallbackFunction)
=====================================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称 (Function Name)
     - NvM_MultiBlockCallbackFunction
     - 
     - 
   * - 函数原型 (Function prototype)
     - voidNvM_MultiBlockCallbackFunction(uint8ServiceId,NvM_RequestResultTypeJobResult)
     - 
     - 
   * - 服务编号 (Service Number)
     - 无
     - 
     - 
   * - 同步/异步 (Synchronous/Asynchronous)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入 (Is it reentrant?)
     - 否 (No)
     - 
     - 
   * - 输入参数 (Input parameters)
     - BlockRequest：多个块的请求类型 (BlockRequest: Type of request for multiple blocks)
     - 值域： (Domain:)
     - NVM_INIT_READ_BLOCK,NVM_INIT_RESTORE_BLOCK_DEFAULTS,NVM_INIT_READ_ALL_BLOCK,NVM_INIT_FIRST_INIT_ALL
   * - 
     - JobResult：以前处理的多个块请求的任务结果 (JobResult：Results of multiple block requests processed before)
     - 值域： (Domain:)
     - NVM_REQ_OKNVM_REQ_NOT_OK
   * - 
     - 
     - 
     - NVM_REQ_PENDING
   * - 
     - 
     - 
     - NVM_REQ_INTEGRITY_FAILED
   * - 
     - 
     - 
     - NVM_REQ_BLOCK_SKIPPED
   * - 
     - 
     - 
     - NVM_REQ_NV_INVALIDATED
   * - 
     - 
     - 
     - NVM_REQ_CANCELED
   * - 
     - 
     - 
     - NVM_REQ_REDUNDANCY_FAILED
   * - 
     - 
     - 
     - NVM_REQ_RESTORED_FROM_ROM
   * - 输入输出参数 (Input Output Parameters)
     - 无
     - 
     - 
   * - 输出参数
     - 无
     - 
     - 
   * - 返回值 (Return value)
     - Std_ReturnType：E_OK：回调函数已被成功处理 (Std_ReturnType：E_OK：The callback function has been handled successfully)
     - 
     - 
   * - 
     - E_NOT_OK：回调函数没有被成功处理 (E_NOT_OK: The callback function was not processed successfully)
     - 
     - 
   * - 功能概述 (Function Overview)
     - 通知上层异步多块请求已经完成的回调 (Callback for completed asynchronous multi-block requests to upper layer)
     - 
     - 




InitBlockCallbackFunction函数定义 (InitBlockCallbackFunction function definition)
=============================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称 (Function Name)
     - InitBlockCallbackFunction
     - 
     - 
   * - 函数原型 (Function prototype)
     - Std_ReturnTypeInitBlockCallbackFunction(NvM_InitBlockRequestTypeInitBlockRequest)
     - 
     - 
   * - 服务编号 (Service Number)
     - 无
     - 
     - 
   * - 同步/异步 (Synchronous/Asynchronous)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入 (Is it reentrant?)
     - 否 (No)
     - 
     - 
   * - 输入参数 (Input parameters)
     - InitBlockRequest：初始块的请求类型 (InitBlockRequest: Request type for initial block)
     - 值域： (Domain:)
     - NVM_INIT_READ_BLOCK,NVM_INIT_RESTORE_BLOCK_DEFAULTS,
   * - 
     - 
     - 
     - NVM_INIT_READ_ALL_BLOCK,NVM_INIT_FIRST_INIT_ALL
   * - 输入输出参数 (Input Output Parameters)
     - 无
     - 
     - 
   * - 输出参数
     - 无
     - 
     - 
   * - 返回值 (Return value)
     - Std_ReturnType：
     - 
     - 
   * - 
     - E_OK：回调函数已被成功处理 (E_OK: The callback function has been successfully processed)
     - 
     - 
   * - 
     - E_NOT_OK：回调函数没有被成功处理 (E_NOT_OK: The callback function was not processed successfully)
     - 
     - 
   * - 功能概述 (Function Overview)
     - 当默认数据需要在RAM中恢复时，由NvM模块调用的回调通知函数，即使配置了一个ROM块 (When default data needs to be restored in RAM, the callback notification function called by the NvM module is invoked even if a ROM block is configured.)
     - 
     - 




NvM_WriteRamBlockToNvm函数定义 (The definition of NvM_WriteRamBlockToNvm function)
==============================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称 (Function Name)
     - NvM_WriteRamBlockToNvm
     - 
     - 
   * - 函数原型 (Function prototype)
     - Std_ReturnTypeNvM_WriteRamBlockToNvm(void\*NvMBuffer)
     - 
     - 
   * - 服务编号 (Service Number)
     - 无
     - 
     - 
   * - 同步/异步 (Synchronous/Asynchronous)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入 (Is it reentrant?)
     - 否 (No)
     - 
     - 
   * - 输入参数 (Input parameters)
     - 无
     - 值域： (Domain:)
     - 无
   * - 输入输出参数 (Input Output Parameters)
     - 无
     - 
     - 
   * - 输出参数
     - NvMBuffer：数据要写入的缓冲区的地址 (NVMBUFFER: The address of the buffer where data is to be written)
     - 
     - 
   * - 返回值 (Return value)
     - Std_ReturnType：
     - 
     - 
   * - 
     - E_OK：回调函数已被成功处理 (E_OK: The callback function has been successfully processed)
     - 
     - 
   * - 
     - E_NOT_OK：回调函数没有被成功处理 (E_NOT_OK: The callback function was not processed successfully)
     - 
     - 
   * - 功能概述 (Function Overview)
     - 为了将数据从RAM块复制到NvM模块的镜像，需要调用特定块的回调例程 (To copy data from the RAM block to the mirror of the NvM module, a specific block's callback routine needs to be called.)
     - 
     - 




NvM_ReadRamBlockFromNvm函数定义 (The definition of NvM_ReadRamBlockFromNvm function)
================================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称 (Function Name)
     - NvM_ReadRamBlockFromNvm
     - 
     - 
   * - 函数原型 (Function prototype)
     - Std_ReturnTypeNvM_ReadRamBlockFromNvm(const void\*NvMBuffer)
     - 
     - 
   * - 服务编号 (Service Number)
     - 无
     - 
     - 
   * - 同步/异步 (Synchronous/Asynchronous)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入 (Is it reentrant?)
     - 否 (No)
     - 
     - 
   * - 输入参数 (Input parameters)
     - NvMBuffer：可以从中读取数据的缓冲区的地址 (NVMBuffer: The address of a buffer from which data can be read)
     - 值域： (Domain:)
     - 无
   * - 输入输出参数 (Input Output Parameters)
     - 无
     - 
     - 
   * - 输出参数
     - 无
     - 
     - 
   * - 返回值 (Return value)
     - Std_ReturnType：
     - 
     - 
   * - 
     - E_OK：回调函数已被成功处理 (E_OK: The callback function has been successfully processed)
     - 
     - 
   * - 
     - E_NOT_OK：回调函数没有被成功处理 (E_NOT_OK: The callback function was not processed successfully)
     - 
     - 
   * - 功能概述 (Function Overview)
     - 为了让将数据从NvM模块的镜像复制到RAM块，需要调用特定块的回调例程。 (To copy data from the NvM module's image to the RAM block, a specific block's callback routine needs to be called.)
     - 
     - 





SWC服务组件封装 (SWC Service Component Packaging)
-----------------------------------------------------------

以下类型和接口可以封装至SWC生成完整的服务组件，可以与应用通过端口连接，没有列出的部分NvM底层暂时不支持。

The following types and interfaces can be encapsulated to generate complete service components with SWC, which can be connected to the application via ports. The NvM lower layer temporarily does not support the unlisted parts.

实现数据类型封装 (Implement data type encapsulation)
============================================================

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 类型名及定义引用 (Type Name and Definition Reference)
     - 生成条件 (Generate Conditions)
   * - NvM_RequestResultType
     - 无
   * - NvM_BlockIdType
     - 无
   * - NvM_InitBlockRequestType
     - 无
   * - NvM_BlockRequestType
     - 无




CS接口封装 (CS Interface Packaging)
===============================================

Rte_Call_NvM_PAdmin\_{Block}_SetBlockProtection
---------------------------------------------------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Rte_Call_NvM_PAdmin\_{Block}_SetBlockProtection
   * - 引用函数定义： (Quote function definition:)
     - 详见4.3.4 (See 4.3.4)
   * - 变体： (Variants:)
     - Block = nvBlockDescriptor.shortname();
   * - 生成条件： (Generate conditions:)
     - UsePort =nvBlockDescriptor.subElt("NvMBlockUsePort").value() ==true;
   * - 端口类型： (Port Type:)
     - Provided Port
   * - 从属端口： (Subordinate Port:)
     - PAdmin\_{Block}




Rte_Call_NvM_PM\_{Block}_ReadRamBlockFromNvM
------------------------------------------------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Rte_Call_NvM_PM\_{Block}_ReadRamBlockFromNvM
   * - 引用函数定义： (Quote function definition:)
     - 详见4.4.5 (See 4.4.5)
   * - 变体： (Variants:)
     - Block = nvBlockDescriptor.shortname();
   * - 生成条件： (Generate conditions:)
     - 1. UsePort =nvBlockDescriptor.subElt("NvMBlockUsePort").value()== true;
   * - 
     - 2. UsePortSyncMech =nvBlockDescriptor.subElt("NvMBlockUseSyncMechanism").value()== true;
   * - 端口类型： (Port Type:)
     - Required Port
   * - 从属端口： (Subordinate Port:)
     - PM\_{Block}




Rte_Call_NvM_PM\_{Block}_WriteRamBlockToNvM
-----------------------------------------------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Rte_Call_NvM_PM\_{Block}_WriteRamBlockToNvM
   * - 引用函数定义： (Quote function definition:)
     - 详见4.4.4 (See 4.4.4)
   * - 变体： (Variants:)
     - Block = nvBlockDescriptor.shortname();
   * - 生成条件： (Generate conditions:)
     - 1. UsePort =nvBlockDescriptor.subElt("NvMBlockUsePort").value()== true;
   * - 
     - 2. UsePortSyncMech =nvBlockDescriptor.subElt("NvMBlockUseSyncMechanism").value()== true;
   * - 端口类型： (Port Type:)
     - Required Port
   * - 从属端口： (Subordinate Port:)
     - PM\_{Block}




Rte_Call_NvM_PNIB\_{Block}_InitBlock
----------------------------------------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Rte_Call_NvM_PNIB\_{Block}_InitBlock
   * - 引用函数定义： (Quote function definition:)
     - 详见4.4.3 (See 4.4.3)
   * - 变体： (Variants:)
     - Block = nvBlockDescriptor.shortname();
   * - 生成条件： (Generate conditions:)
     - 1. UsePort =nvBlockDescriptor.subElt("NvMBlockUsePort").value()== true;
   * - 
     - 2. InitBlockCallbackDef =nvBlockDescriptor.subElt("NvMInitBlockCallback").isDefined();
   * - 
     - 3. InitBlockCallbackFncDef =nvBlockDescriptor.subElt("NvMInitBlockCallback/NvMInitBlockCallbackFnc").isDefined();
   * - 端口类型： (Port Type:)
     - Required Port
   * - 从属端口： (Subordinate Port:)
     - PNIB\_{Block}




Rte_Call_NvM_PNJF\_{Block}_JobFinished
------------------------------------------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Rte_Call_NvM_PNJF\_{Block}_JobFinished
   * - 引用函数定义： (Quote function definition:)
     - 详见4.4.1 (See 4.4.1)
   * - 变体： (Variants:)
     - Block = nvBlockDescriptor.shortname();
   * - 生成条件： (Generate conditions:)
     - 1. UsePort =nvBlockDescriptor.subElt("NvMBlockUsePort").value()== true;
   * - 
     - 2. SingleBlockCallbackDef =nvBlockDescriptor.subElt("NvMSingleBlockCallback").isDefined();
   * - 
     - 3. SingleBlockCallbackFncDef =nvBlockDescriptor.subElt("NvMSingleBlockCallback/NvMSingleBlockCallbackFnc").isDefined();
   * - 端口类型： (Port Type:)
     - Required Port
   * - 从属端口： (Subordinate Port:)
     - PNJF\_{Block}




Rte_Call_NvM_PS\_{Block}_EraseBlock
---------------------------------------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Rte_Call_NvM_PS\_{Block}_EraseBlock
   * - 引用函数定义： (Quote function definition:)
     - 详见4.3.13 (See 4.3.13)
   * - 变体： (Variants:)
     - Block = nvBlockDescriptor.shortname();
   * - 生成条件： (Generate conditions:)
     - UsePort =nvBlockDescriptor.subElt("NvMBlockUsePort").value() ==true;
   * - 端口类型： (Port Type:)
     - Provided Port
   * - 从属端口： (Subordinate Port:)
     - PS\_{Block}




Rte_Call_NvM_PS\_{Block}_GetDataIndex
-----------------------------------------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Rte_Call_NvM_PS\_{Block}_GetDataIndex
   * - 引用函数定义： (Quote function definition:)
     - 详见4.3.3 (See 4.3.3)
   * - 变体： (Variants:)
     - Block = nvBlockDescriptor.shortname();
   * - 生成条件： (Generate conditions:)
     - UsePort =nvBlockDescriptor.subElt("NvMBlockUsePort").value() ==true;
   * - 端口类型： (Port Type:)
     - Provided Port
   * - 从属端口： (Subordinate Port:)
     - PS\_{Block}




Rte_Call_NvM_PS\_{Block}_GetErrorStatus
-------------------------------------------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Rte_Call_NvM_PS\_{Block}_GetErrorStatus
   * - 引用函数定义： (Quote function definition:)
     - 详见4.3.5 (See 4.3.5)
   * - 变体： (Variants:)
     - Block = nvBlockDescriptor.shortname();
   * - 生成条件： (Generate conditions:)
     - UsePort =nvBlockDescriptor.subElt("NvMBlockUsePort").value() ==true;
   * - 端口类型： (Port Type:)
     - Provided Port
   * - 从属端口： (Subordinate Port:)
     - PS\_{Block}




Rte_Call_NvM_PS\_{Block}_InvalidateNvBlock
----------------------------------------------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Rte_Call_NvM_PS\_{Block}_InvalidateNvBlock
   * - 引用函数定义： (Quote function definition:)
     - 详见4.3.15 (See 4.3.15)
   * - 变体： (Variants:)
     - Block = nvBlockDescriptor.shortname();
   * - 生成条件： (Generate conditions:)
     - UsePort =nvBlockDescriptor.subElt("NvMBlockUsePort").value() ==true;
   * - 端口类型： (Port Type:)
     - Provided Port
   * - 从属端口： (Subordinate Port:)
     - PS\_{Block}




Rte_Call_NvM_PS\_{Block}_ReadBlock
--------------------------------------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Rte_Call_NvM_PS\_{Block}_ReadBlock
   * - 引用函数定义： (Quote function definition:)
     - 详见4.3.10 (See 4.3.10)
   * - 变体： (Variants:)
     - Block = nvBlockDescriptor.shortname();
   * - 生成条件： (Generate conditions:)
     - UsePort =nvBlockDescriptor.subElt("NvMBlockUsePort").value() ==true;
   * - 端口类型： (Port Type:)
     - Provided Port
   * - 从属端口： (Subordinate Port:)
     - PS\_{Block}




Rte_Call_NvM_PS\_{Block}_ReadPRAMBlock
------------------------------------------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Rte_Call_NvM_PS\_{Block}_ReadPRAMBlock
   * - 引用函数定义： (Quote function definition:)
     - 详见4.3.16 (See 4.3.16)
   * - 变体： (Variants:)
     - Block = nvBlockDescriptor.shortname();
   * - 生成条件： (Generate conditions:)
     - UsePort =nvBlockDescriptor.subElt("NvMBlockUsePort").value() ==true;
   * - 端口类型： (Port Type:)
     - Provided Port
   * - 从属端口： (Subordinate Port:)
     - PS\_{Block}




Rte_Call_NvM_PS\_{Block}_RestoreBlockDefaults
-------------------------------------------------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Rte_Call_NvM_PS\_{Block}_RestoreBlockDefaults
   * - 引用函数定义： (Quote function definition:)
     - 详见4.3.12 (See 4.3.12)
   * - 变体： (Variants:)
     - Block = nvBlockDescriptor.shortname();
   * - 生成条件： (Generate conditions:)
     - UsePort =nvBlockDescriptor.subElt("NvMBlockUsePort").value() ==true;
   * - 端口类型： (Port Type:)
     - Provided Port
   * - 从属端口： (Subordinate Port:)
     - PS\_{Block}




Rte_Call_NvM_PS\_{Block}_RestorePRAMBlockDefaults
-----------------------------------------------------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Rte_Call_NvM_PS\_{Block}_RestorePRAMBlockDefaults
   * - 引用函数定义： (Quote function definition:)
     - 详见4.3.18 (See 4.3.18)
   * - 变体： (Variants:)
     - Block = nvBlockDescriptor.shortname();
   * - 生成条件： (Generate conditions:)
     - UsePort =nvBlockDescriptor.subElt("NvMBlockUsePort").value() ==true;
   * - 端口类型： (Port Type:)
     - Provided Port
   * - 从属端口： (Subordinate Port:)
     - PS\_{Block}




Rte_Call_NvM_PS\_{Block}_SetDataIndex
-----------------------------------------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Rte_Call_NvM_PS\_{Block}_SetDataIndex
   * - 引用函数定义： (Quote function definition:)
     - 详见4.3.2 (See 4.3.2)
   * - 变体： (Variants:)
     - Block = nvBlockDescriptor.shortname();
   * - 生成条件： (Generate conditions:)
     - UsePort =nvBlockDescriptor.subElt("NvMBlockUsePort").value() ==true;
   * - 端口类型： (Port Type:)
     - Provided Port
   * - 从属端口： (Subordinate Port:)
     - PS\_{Block}




Rte_Call_NvM_PS\_{Block}_SetRamBlockStatus
----------------------------------------------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Rte_Call_NvM_PS\_{Block}_SetRamBlockStatus
   * - 引用函数定义： (Quote function definition:)
     - 详见4.3.7 (See 4.3.7)
   * - 变体： (Variants:)
     - Block = nvBlockDescriptor.shortname();
   * - 生成条件： (Generate conditions:)
     - UsePort =nvBlockDescriptor.subElt("NvMBlockUsePort").value() ==true;
   * - 端口类型： (Port Type:)
     - Provided Port
   * - 从属端口： (Subordinate Port:)
     - PS\_{Block}




Rte_Call_NvM_PS\_{Block}_WriteBlock
---------------------------------------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Rte_Call_NvM_PS\_{Block}_WriteBlock
   * - 引用函数定义： (Quote function definition:)
     - 详见4.3.11 (See 4.3.11)
   * - 变体： (Variants:)
     - Block = nvBlockDescriptor.shortname();
   * - 生成条件： (Generate conditions:)
     - UsePort =nvBlockDescriptor.subElt("NvMBlockUsePort").value() ==true;
   * - 端口类型： (Port Type:)
     - Provided Port
   * - 从属端口： (Subordinate Port:)
     - PS\_{Block}




Rte_Call_NvM_PS\_{Block}_WritePRAMBlock
-------------------------------------------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Rte_Call_NvM_PS\_{Block}_WritePRAMBlock
   * - 引用函数定义： (Quote function definition:)
     - 详见4.3.17 (See 4.3.17)
   * - 变体： (Variants:)
     - Block = nvBlockDescriptor.shortname();
   * - 生成条件： (Generate conditions:)
     - UsePort =nvBlockDescriptor.subElt("NvMBlockUsePort").value() ==true;
   * - 端口类型： (Port Type:)
     - Provided Port
   * - 从属端口： (Subordinate Port:)
     - PS\_{Block}




配置 (Configure)
==============================

NvMCommon
-------------------------

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/NvM/image3.png
   :alt: NvMCommon容器配置图 (NVMeCommon Container Configuration Diagram)
   :name: NvMCommon容器配置图 (NVMeCommon Container Configuration Diagram)
   :align: center


.. centered:: **表 NvMCommon属性描述 (Table NvMCommon Property Description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - NvMApiConfigClass
     - 取值范围 (Range)
     - NVM_API_CONFIG_CLASS_1/NVM_API_CONFIG_CLASS_2/NVM_API_CONFIG_CLASS_3
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 预处理器开关，使能一些API的调用 (Preprocessor switch, enables calls to some APIs)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - NvMBswMMultiBlockJobStatusInformation
     - 取值范围 (Range)
     - True/False
     - 默认取值 (Default value)
     - True
   * - 
     - 参数描述 (Parameter Description)
     - 是否通知BswM多块作业的当前状态 (Does BswM need to be notified of the current status of multiple jobs?)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - NvMCompiledConfigId
     - 取值范围 (Range)
     - 0 … 65535
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - 关于NV内存布局的配置ID。 (Configuration ID for NV memory layout.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - NvMCrcNumOfBytes
     - 取值范围 (Range)
     - 1 ... 65535
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 如果为至少一个NVRAM块配置CRC，则此参数定义在请求处理的一个周期内应处理的最大字节数，CRC计算的长度。 (If CRC is configured for at least one NVRAM block, this parameter defines the maximum number of bytes to be processed in a single period request, including the length of the CRC calculation.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - NvMDatasetSelectionBits
     - 取值范围 (Range)
     - 0 … 8
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 在内存硬件抽象接口中定义最低有效位的数目，用于寻址dataset类型的NVRAM块。 (Define the number of least significant bits for addressing NVRAM blocks of dataset type in the memory hardware abstraction interface.)
     - 
     - 
   * - 
     - 
     - 0...8：用于数据集或冗余块寻址的bit位。 (0...8：Bit positions used for addressing datasets or redundant blocks.)
     - 
     - 
   * - 
     - 
     - 0：根本没有dataset或冗余NVRAM块，不需要选择位。 (There is no dataset or redundant NVRAM block, no bits to select.)
     - 
     - 
   * - 
     - 
     - 1：配置了冗余NVRAM块，但没有dataset的NVRAM块。 (1: Redundant NVRAM blocks are configured, but there is no NVRAM block for a dataset.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 依赖于底层硬件要求 (Dependent on underlying hardware requirements)
     - 
     - 
   * - NvMDevErrorDetect
     - 取值范围 (Range)
     - true/false
     - 默认取值 (Default value)
     - False
   * - 
     - 参数描述 (Parameter Description)
     - DET检查使能开关 (DET Check Enable Switch)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - NvMDrvModeSwitch
     - 取值范围 (Range)
     - true/false
     - 默认取值 (Default value)
     - False
   * - 
     - 参数描述 (Parameter Description)
     - 预处理器开关，使驱动在执行NvM_ReadAll和NvM_WriteAll时切换到快速模式 (Preprocessor switch to enable fast mode when executing NvM_ReadAll and NvM_WriteAll.)
     - 
     - 
   * - 
     - 
     - true：启用快速模式。 (true: Enable fast mode.)
     - 
     - 
   * - 
     - 
     - false：禁用快速模式。 (False: Disable Fast Mode.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - NvMDynamicConfiguration
     - 取值范围 (Range)
     - true/false
     - 默认取值 (Default value)
     - False
   * - 
     - 参数描述 (Parameter Description)
     - 动态配置管理处理NvM_ReadAll请求。 (Dynamic configuration management handles the NvM_ReadAll request.)
     - 
     - 
   * - 
     - 
     - true：启用动态配置管理处理。 (Enable dynamic configuration management processing.)
     - 
     - 
   * - 
     - 
     - false：禁用动态配置管理处理。 (false: Disable dynamic configuration management processing.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - NvMJobPrioritization
     - 取值范围 (Range)
     - true/false
     - 默认取值 (Default value)
     - False
   * - 
     - 参数描述 (Parameter Description)
     - 优先级处理开关 (Priority processing switch)
     - 
     - 
   * - 
     - 
     - true：启用优先级处理。 (true: Enable priority processing.)
     - 
     - 
   * - 
     - 
     - false：禁用优先级处理。 (false: Disable priority processing.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - NvMMainFunctionPeriod
     - 取值范围 (Range)
     - 0 … INF
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - 主函数周期 (Main function cycle)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 未使用，可以不用关心 (Not used, can be ignored.)
     - 
     - 
   * - NvMMultiBlockCallback
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 每个异步多块请求终止时调用的公共回调函数 (A common callback function called when each asynchronous multiple block request terminates.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - NvMBswMMultiBlockJobStatusInformation
     - 
     - 
   * - NvMPollingMode
     - 取值范围 (Range)
     - true/false
     - 默认取值 (Default value)
     - False
   * - 
     - 参数描述 (Parameter Description)
     - 启用/禁用轮询模式，同时禁用/启用底层可用的回调函数 (Enable/Disable Polling Mode, Additionally Enable/Disable Underlying Available Callback Functions)
     - 
     - 
   * - 
     - 
     - true：开启轮询模式，关闭回调功能。 (true: Enable polling mode and disable callback function.)
     - 
     - 
   * - 
     - 
     - false：关闭轮询模式，启用回调功能。 (false: Disable polling mode and enable callback functionality.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - NvMRepeatMirrorOperations
     - 取值范围 (Range)
     - 0-7
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - 在推迟当前作业之前，让应用程序将数据复制到NvM模块的镜像或从NvM模块复制数据的重试次数。 (Before delaying the current job, allow the application to retry copying data to the NvM module's mirror or from the NvM module.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - NvMSetRamBlockStatusApi
     - 取值范围 (Range)
     - true/false
     - 默认取值 (Default value)
     - False
   * - 
     - 参数描述 (Parameter Description)
     - Nvm_setramblockstatus函数使能开关。 (The Nvm_setramblockstatus function enables the switch.)
     - 
     - 
   * - 
     - 
     - true：NvM_SetRamBlockStatus使能。 (true: NvM_SetRamBlockStatus enabled.)
     - 
     - 
   * - 
     - 
     - false：NvM_SetRamBlockStatus不使能。 (false: NvM_SetRamBlockStatus is not enabled.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - NvMSizeImmediateJobQueue
     - 取值范围 (Range)
     - 1-255
     - 默认取值 (Default value)
     - 1
   * - 
     - 参数描述 (Parameter Description)
     - 定义立即优先级作业队列的队列条目数。如果NVM_JOB_PRIORITIZATION被关闭，则该参数将超出范围。 (Define the number of queue entries for the immediate priority job queue. If NVM_JOB_PRIORITIZATION is disabled, this parameter will be out of range.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - NVM_JOB_PRIORITIZATION需要使能 (NVM_JOB_PRIORITIZATION needs to be enabled)
     - 
     - 
   * - NvMSizeStandardJobQueue
     - 取值范围 (Range)
     - 1-255
     - 默认取值 (Default value)
     - 1
   * - 
     - 参数描述 (Parameter Description)
     - 标准作业队列的队列条目数 (Number of items in the queue of standard work procedure queues)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - NvMVersionInfoApi
     - 取值范围 (Range)
     - true/false
     - 默认取值 (Default value)
     - False
   * - 
     - 参数描述 (Parameter Description)
     - 版本获取函数开关 (Version Retrieval Function Switch)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 




NvMBlockDescriptor
----------------------------------

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/NvM/image4.png
   :alt: NvMBlockDescriptor容器配置图 (NvM Block Descriptor container configuration diagram)
   :name: NvMBlockDescriptor容器配置图 (NvM Block Descriptor container configuration diagram)
   :align: center

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/NvM/image5.png
   :alt: NvMBlockDescriptor容器配置图1 (NvM Block Descriptor container configuration diagram)
   :name: NvMBlockDescriptor容器配置图1 (NvM Block Descriptor container configuration diagram)
   :align: center


.. centered:: **表 NvMBlockDescriptor属性描述 (Table NvMBlockDescriptor Properties Described)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - NvMBlockCrcType
     - 取值范围 (Range)
     - NVM_CRC16/NVM_CRC32/NVM_CRC8
     - 默认取值 (Default value)
     - NVM_CRC16
   * - 
     - 参数描述 (Parameter Description)
     - 定义NVRAM块的CRC数据宽度。 (Define the CRC data width for NVRAM blocks.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - NVM_BLOCK_USE_CRC使能后可配置 (NVM_BLOCK_USE_CRC enabled can be configured)
     - 
     - 
   * - NvMBlockHeaderInclude
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 定义头文件，其中NVRAM块的所有者有永久RAM数据块的声明，ROM数据块(如果配置)和每个配置回调的回调函数原型。如果没有永久的RAM块，ROM块或回调函数被配置，那么这个配置参数将被忽略。 (Define a header file where the owners of NVRAM blocks declare permanent RAM data blocks, ROM data blocks (if configured), and prototype callback functions for each configuration. If no permanent RAM block, ROM block, or callback function is configured, this configuration parameter will be ignored.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - NvMBlockJobPriority
     - 取值范围 (Range)
     - 0 … 255
     - 默认取值 (Default value)
     - 1
   * -
     - 参数描述 (Parameter Description)
     - NV块的优先级 (Priority of NV blocks)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 只有在配置页面NvMApiConfigClass不选择Class1并且NvMJobPrioritization打勾的情况下才可配 (Only configure when Class1 is not selected in the NvMApiConfigClass on the configuration page and NvMJobPrioritization is checked.)
     - 
     - 
   * - NvMBlockManagementType
     - 取值范围 (Range)
     - NVM_BLOCK_DATASET/NVM_BLOCK_NATIVE/NVM_BLOCK_REDUNDANT
     - 默认取值 (Default value)
     - NVM_BLOCK_REDUNDANT
   * - 
     - 参数描述 (Parameter Description)
     - 块类型 (Block Type)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - NvMBlockUseAutoValidation
     - 取值范围 (Range)
     - true/false
     - 默认取值 (Default value)
     - False
   * -
     - 参数描述 (Parameter Description)
     - 定义RAM块在关闭阶段是否应自动验证。 (Define whether RAM blocks should be automatically validated during the shutdown phase.)
     - 
     - 
   * - 
     - 
     - True：使用自动验证机制， (True: Using automatic validation mechanisms,)
     - 
     - 
   * - 
     - 
     - false：其他情况 (false: Other circumstances)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - NvMBlockUseCompression
     - 取值范围 (Range)
     - true/false
     - 默认取值 (Default value)
     - False
   * - 
     - 参数描述 (Parameter Description)
     - 定义数据在写入前是否压缩。 (Define whether data should be compressed before writing.)
     - 
     - 
   * - 
     - 
     - True：需要压缩， (True: Need compression,)
     - 
     - 
   * - 
     - 
     - false：不需要压缩 (False: No compression needed)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - NvMBlockUseCrc
     - 取值范围 (Range)
     - true/false
     - 默认取值 (Default value)
     - False
   * - 
     - 参数描述 (Parameter Description)
     - NVRAM块的CRC使能开关，即在RAM和NV内存中保留用于CRC的内存空间。 (The CRC enable switch for NVRAM blocks, which reserves memory space in RAM and NV memory for CRC.)
     - 
     - 
   * - 
     - 
     - true：此NVRAM块将使用CRC。 (True: This NVRAM block will use CRC.)
     - 
     - 
   * - 
     - 
     - false：此NVRAM块不使用CRC。 (False: This NVRAM block does not use CRC.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - NvMWriteBlockOnce使能是此项不可配置并且使能 (NvMWriteBlockOnce enable is non-configurable and enabled)
     - 
     - 
   * - NvMBlockUseCRCCompMechanism
     - 取值范围 (Range)
     - true/false
     - 默认取值 (Default value)
     - False
   * -
     - 参数描述 (Parameter Description)
     - 是否在写期间将RAM块的CRC与上次成功读写作业期间计算的CRC进行比较。 (Is RAM block CRC compared with the CRC calculated during the last successful read/write operation?)
     - 
     - 
   * - 
     - 
     - True：使用比较机制， (True: Use comparative mechanisms,)
     - 
     - 
   * - 
     - 
     - false：其他情况 (false: Other circumstances)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - NvMBlockUsePort
     - 取值范围 (Range)
     - true/false
     - 默认取值 (Default value)
     - False
   * - 
     - 参数描述 (Parameter Description)
     - 是否使用RTE中PORT接口。 (Is the PORT interface used in the RTE?)
     - 
     - 
   * - 
     - 
     - True：使用， (True: Use,)
     - 
     - 
   * - 
     - 
     - false：不使用 (false: Not using)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - NvMBlockUseSetRamBlockStatus
     - 取值范围 (Range)
     - true/false
     - 默认取值 (Default value)
     - False
   * -
     - 参数描述 (Parameter Description)
     - 这个块是否使能NvMSetRamBlockStatus。 (Does this block enable NvMSetRamBlockStatus.)
     - 
     - 
   * - 
     - 
     - true：这个RAM块的NvMSetRamBlockStatus使能。 (true: This RAM block's NvMSetRamBlockStatus is enabled.)
     - 
     - 
   * - 
     - 
     - false：这个RAM块的NvMSetRamBlockStatus将被忽略。 (false: This NvMSetRamBlockStatus for this RAM block will be ignored.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 如果禁用NvMCommon中的NvMSetRamBlockStatus，此配置参数将被忽略 (If NvMSetRamBlockStatus in NvMCommon is disabled, this configuration parameter will be ignored.)
     - 
     - 
   * - NvMBlockUseSyncMechanism
     - 取值范围 (Range)
     - true/false
     - 默认取值 (Default value)
     - False
   * -
     - 参数描述 (Parameter Description)
     - NV块是否使用带有RAM镜像和回调例程的显式同步机制来传输NvM模块的RAM镜像的数据。 (Does the NV block use an explicit synchronization mechanism with RAM mirror and callback routines to transfer data of the NvM module's RAM mirror?)
     - 
     - 
   * - 
     - 
     - true：使用同步机制 (true: Use synchronization mechanisms)
     - 
     - 
   * - 
     - 
     - false：不使用 (false: Not using)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - NvMBlockUseCrc
     - 
     - 
   * - NvMBlockWriteProt
     - 取值范围 (Range)
     - true/false
     - 默认取值 (Default value)
     - False
   * -
     - 参数描述 (Parameter Description)
     - 定义NV块的初始写保护 (Define initial write protection for NV blocks)
     - 
     - 
   * - 
     - 
     - true：启用初始块写保护。 (true: Enable initial block write protection.)
     - 
     - 
   * - 
     - 
     - false：关闭初始块写保护。 (false: Disable initial block write protection.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - NvMWriteBlockOnce和NvMBlockWriteProt只能配置两者之一 (NvMWriteBlockOnce and NvMBlockWriteProt can only be configured with one of them.)
     - 
     - 
   * - NvMBswMBlockStatusInformation
     - 取值范围 (Range)
     - true/false
     - 默认取值 (Default value)
     - False
   * -
     - 参数描述 (Parameter Description)
     - 是否告知BswM指定块的当前状态。 (Does BswM need to be informed about the current status of the designated block.)
     - 
     - 
   * - 
     - 
     - True：在变更时调用BswM_NvM_CurrentBlockMode (True: Call BswM_NvM_CurrentBlockMode when changing.)
     - 
     - 
   * - 
     - 
     - False：根本不通知BswM (False: Does not notify BswM at all)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - NvMCalcRamBlockCrc
     - 取值范围 (Range)
     - true/false
     - 默认取值 (Default value)
     - False
   * -
     - 参数描述 (Parameter Description)
     - 是否为配置为使用显式同步机制的永久RAM块或NVRAM块定义CRC(重新)计算。 (Is CRC(re-)calculation defined for a permanent RAM block or NVRAM block configured to use an explicit synchronization mechanism?)
     - 
     - 
   * - 
     - 
     - true：这个永久RAM块的CRC将被(重新)计算。 (True: The CRC of this permanent RAM block will be (re-)calculated.)
     - 
     - 
   * - 
     - 
     - false：这个永久RAM块不会(重新)计算CRC。 (false: This permanent RAM block will not (re-)calculate CRC.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - NVM_BLOCK_USE_CRC使能情况下可配置 (NVM_BLOCK_USE_CRC Enabled Configuration)
     - 
     - 
   * - NvMMaxNumOfReadRetries
     - 取值范围 (Range)
     - 0 .. 7
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - 最大读取重试次数 (Maximum read retry times)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - NvMMaxNumOfWriteRetries
     - 取值范围 (Range)
     - 0 .. 7
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - 最大写重试次数 (Maximum write retry attempts)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - NvMNvBlockBaseNumber
     - 取值范围 (Range)
     - 1 .. 65534
     - 默认取值 (Default value)
     - 1
   * -
     - 参数描述 (Parameter Description)
     - 连接到下层的基础块号 (Block number connected to lower layer)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 下层块号右移配置项NvMDatasetSelectionBits的位数 (Configuration item NvMDatasetSelectionBits bit count for right shift of lower block number)
     - 
     - 
   * - NvMNvBlockLength
     - 取值范围 (Range)
     - 1 .. 65535
     - 默认取值 (Default value)
     - 2
   * -
     - 参数描述 (Parameter Description)
     - NV块长度 (NV Block Length)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 检查下层FEE和EA关联的块长度，如果比NVM配置的块长度加上CRC长度小则报错 (Check the block length of the lower layer FEE and EA associated blocks, if it is smaller than the NVM configured block length plus CRC length, report an error.)
     - 
     - 
   * - NvMNvBlockNum
     - 取值范围 (Range)
     - 1 … 255
     - 默认取值 (Default value)
     - 1
   * -
     - 参数描述 (Parameter Description)
     - 根据给定的块管理类型，定义一个相邻区域内的多个NV块的数量。 (Define the number of multiple NV blocks within an adjacent area based on the given block management type.)
     - 
     - 
   * - 
     - 
     - 1-255用于配置块管理类型为NVM_BLOCK_DATASET的块。 (1-255 are used to configure blocks with a block management type of NVM_BLOCK_DATASET.)
     - 
     - 
   * - 
     - 
     - 1用于需要配置块管理类型为NVM_BLOCK_NATIVE的NVRAM块 (1 For NVRAM blocks that require configuring the block management type as NVM_BLOCK_NATIVE)
     - 
     - 
   * - 
     - 
     - 2用于配置块管理类型为NVM_BLOCK_REDUNDANT的NVRAM块 (2 Used for configuring block management type as NVM_BLOCK_REDUNDANT for NVRAM blocks)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 取决于NVM_BLOCK_MANAGEMENT_TYPE (Depends on NVM_BLOCK_MANAGEMENT_TYPE)
     - 
     - 
   * - NvMNvramBlockIdentifier
     - 取值范围 (Range)
     - 1…65535
     - 默认取值 (Default value)
     - 无
   * -
     - 参数描述 (Parameter Description)
     - NV块号，自动生成，不可配置 (NV Block Number, auto-generated, not configurable)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - NvMNvramDeviceId
     - 取值范围 (Range)
     - 0…1
     - 默认取值 (Default value)
     - 无
   * -
     - 参数描述 (Parameter Description)
     - 设备号，自动生成，不可配置 (Device ID, auto-generated, not configurable)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - NvMRamBlockDataBufferAutoFill
     - 取值范围 (Range)
     - true/false
     - 默认取值 (Default value)
     - True
   * - 
     - 参数描述 (Parameter Description)
     - 自动计算ram地址 (Automatically calculate RAM address)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - NvMRamBlockDataAddress
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * -
     - 参数描述 (Parameter Description)
     - Ram地址，可以通过配置项进行选择为自动计算 (RAM address can be selected for automatic calculation through configuration items.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - NvMRamBlockDataBufferAutoFill使能时，会根据NvMRamBlockStartAddress、NvMNvBlockLength以及前一个块的ram地址进行自动计算 (When NvMRamBlockDataBufferAutoFill is enabled, it automatically calculates based on NvMRamBlockStartAddress, NvMNvBlockLength, and the RAM address of the previous block.)
     - 
     - 
   * - NvMReadRamBlockFromNvCallback
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * -
     - 参数描述 (Parameter Description)
     - 块特定回调接口的入口地址，为了让应用程序从NvM模块的镜像复制数据到RAM块，应该调用这个回调接口。 (The entry point for a specific callback interface to allow applications to copy data from the NvM module's image to an RAM block should be called.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - NvMBlockUseSyncMechanism
     - 
     - 
   * - NvMResistantToChangedSw
     - 取值范围 (Range)
     - true/false
     - 默认取值 (Default value)
     - True
   * - 
     - 参数描述 (Parameter Description)
     - NVRAM块对更改是否具有抵抗力。如果在配置时没有可用的默认数据，则应用程序应负责提供默认初始化数据。在这种情况下，应用程序必须使用NvM_GetErrorStatus()来区分第一次初始化和数据损坏。 (Does the NVRAM block resist changes? If there is no available default data when configured, the application should be responsible for providing default initialization data. In this case, the application must use NvM_GetErrorStatus() to distinguish between the first initialization and data corruption.)
     - 
     - 
   * - 
     - 
     - true：NVRAM块是抵抗更改。 (true: NVRAM blocks are resistant to changes.)
     - 
     - 
   * - 
     - 
     - false：NVRAM块不抵抗更改。 (False: NVRAM blocks do not resist changes.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - NvMDynamicConfiguration
     - 
     - 
   * - NvMRomBlockDataAddress
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * -
     - 参数描述 (Parameter Description)
     - ROM块数据的起始地址。如果不配置，则所选的块管理类型没有ROM块可用。 (Starting address of ROM block data. No ROM blocks are available if not configured.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - NvMRomBlockNum
     - 取值范围 (Range)
     - 0...254
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - 根据块管理类型，定义一个连续区域中的多个ROM块的数量。 (Define the number of multiple ROM blocks in a continuous area according to the block management type.)
     - 
     - 
   * - 
     - 
     - 0-254用于配置块管理类型为NVM_BLOCK_DATASET的块。 (0-254 are used for configuring blocks with a block management type of NVM_BLOCK_DATASET.)
     - 
     - 
   * - 
     - 
     - 0-1配置块管理类型为NVM_BLOCK_NATIVE的块 (Configure the block management type as NVM_BLOCK_NATIVE for 0-1 configuration block.)
     - 
     - 
   * - 
     - 
     - 0-1用于配置块管理类型为NVM_BLOCK_REDUNDANT的块 (0-1 used for configuring block management type as NVM_BLOCK_REDUNDANT for the block.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 取决于NVM_BLOCK_MANAGEMENT_TYPE (Depends on NVM_BLOCK_MANAGEMENT_TYPE)
     - 
     - 
   * - NvMSelectBlockForFirstInitAll
     - 取值范围 (Range)
     - true/false
     - 默认取值 (Default value)
     - False
   * - 
     - 参数描述 (Parameter Description)
     - NVRAM块是否会被NvM_FirstInitAll处理。此配置参数只影响那些配置为具有永久RAM块或配置为使用显式同步机制的NVRAM块。 (Will the NVRAM block be processed by NvM_FirstInitAll. This configuration parameter only affects NVRAM blocks configured with persistent RAM blocks or those using explicit synchronization mechanisms.)
     - 
     - 
   * - 
     - 
     - true：NVRAM块由NvM_FirstInitAll处理 (true: The NVRAM block is processed by NvM_FirstInitAll.)
     - 
     - 
   * - 
     - 
     - false：NVRAM块不被NvM_FirstInitAll处理 (False: NVRAM blocks are not handled by NvM_FirstInitAll.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - NvMSelectBlockForReadAll
     - 取值范围 (Range)
     - true/false
     - 默认取值 (Default value)
     - False
   * - 
     - 参数描述 (Parameter Description)
     - NVRAM块是否应在NvM_ReadAll期间处理。此配置参数只影响那些配置为具有永久RAM块或配置为使用显式同步机制的NVRAM块。 (Should NVRAM blocks be processed during NvM_ReadAll. This configuration parameter only affects NVRAM blocks configured with permanent RAM blocks or those using explicit synchronization mechanisms.)
     - 
     - 
   * - 
     - 
     - true：NVRAM块由NvM_ReadAll处理 (true: The NVRAM block is processed by NvM_ReadAll.)
     - 
     - 
   * - 
     - 
     - false：NVRAM块不被NvM_ReadAll处理 (false: The NVRAM block is not processed by NvM_ReadAll.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - NVM_RAM_BLOCK_DATA_ADDRESS是否配置 (Is NVM_RAM_BLOCK_DATA_ADDRESS Configured?)
     - 
     - 
   * - 
     - 
     - NvMBlockManagementType
     - 
     - 
   * - NvMSelectBlockForWriteAll
     - 取值范围 (Range)
     - true/false
     - 默认取值 (Default value)
     - False
   * - 
     - 参数描述 (Parameter Description)
     - NVRAM块是否应该在NvM_WriteAll期间处理。此配置参数只影响那些配置为具有永久RAM块或配置为使用显式同步机制的NVRAM块。 (Should NVRAM blocks be handled during NvM_WriteAll. This configuration parameter affects only those configured with persistent RAM blocks or NVRAM blocks using explicit synchronization mechanisms.)
     - 
     - 
   * - 
     - 
     - true：NVRAM块由NvM_WriteAll处理 (true: The NVRAM block is handled by NvM_WriteAll.)
     - 
     - 
   * - 
     - 
     - false：NVRAM块不被NvM_WriteAll处理 (false: NVRAM block is not handled by NvM_WriteAll)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - NVM_RAM_BLOCK_DATA_ADDRESS是否配置 (Is NVM_RAM_BLOCK_DATA_ADDRESS Configured?)
     - 
     - 
   * - NvMStaticBlockIDCheck
     - 取值范围 (Range)
     - true/false
     - 默认取值 (Default value)
     - False
   * - 
     - 参数描述 (Parameter Description)
     - 是否启用了静态块ID检查。 (Is static block ID checking enabled.)
     - 
     - 
   * - 
     - 
     - false：禁用静态块ID检查。 (false: Disable static block ID check.)
     - 
     - 
   * - 
     - 
     - true：启用静态块ID检查。 (true: Enable static block ID checking.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - NvMWriteBlockOnce
     - 取值范围 (Range)
     - true/false
     - 默认取值 (Default value)
     - False
   * - 
     - 参数描述 (Parameter Description)
     - 首次写入后的写保护。NVRAM管理器在第一次写入NV块后设置写保护位。这意味着NVRAM中的一些NV块永远不应该被擦除，也不应该在第一次初始化后被默认ROM数据替换。 (Write protection after the first write. The NVRAM manager sets the write-protect bit after the first write to NV blocks. This means that some NV blocks in NVRAM should never be erased, and should not be replaced with default ROM data after the first initialization.)
     - 
     - 
   * - 
     - 
     - true：首次写入后写保护。 (true: Write protection after first write.)
     - 
     - 
   * - 
     - 
     - false：禁用第一次写后写保护。 (Disable first write then write protection.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - NvMWriteBlockOnce和NvMBlockWriteProt只能配置两者之一 (NvMWriteBlockOnce and NvMBlockWriteProt can only be configured with one of them.)
     - 
     - 
   * - NvMWriteRamBlockToNvCallback
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 让应用程序将数据从RAM块复制到NvM模块的镜像，需要调用块的回调接口。 (To enable an application to copy data from a RAM block to the mirror of an NvM module, a block's callback interface needs to be invoked.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - NvMWriteVerification
     - 取值范围 (Range)
     - true/false
     - 默认取值 (Default value)
     - False
   * - 
     - 参数描述 (Parameter Description)
     - 是否启用写入验证。 (Is write verification enabled.)
     - 
     - 
   * - 
     - 
     - false：关闭写验证。 (False: Disable write verification.)
     - 
     - 
   * - 
     - 
     - true：开启写验证。 (True: Enable write verification.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - NvMWriteVerificationDataSize
     - 取值范围 (Range)
     - 1 .. 65535
     - 默认取值 (Default value)
     - 1
   * - 
     - 参数描述 (Parameter Description)
     - 在比较RAM块和回读块的内容时，每一步中要比较的字节数。 (The number of bytes to be compared at each step when comparing the contents of RAM blocks and read-back blocks.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - NvMNvBlockLength
     - 
     - 




NvMInitBlockCallback
====================================

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/NvM/image6.png
   :alt: NvMInitBlockCallback容器配置图 (NvMInitBlockCallback Container Configuration Diagram)
   :name: NvMInitBlockCallback容器配置图 (NvMInitBlockCallback Container Configuration Diagram)
   :align: center


.. centered:: **表 NvMInitBlockCallback属性描述 (Property Description of NvMInitBlockCallback Table)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - NvMInitBlockCallback
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 块特定回调程序的入口地址，如果没有ROM数据可用来初始化NVRAM块，该回调程序将被调用。如果没有配置，则不需要调用特定的回调例程来初始化带有默认数据的NVRAM块。 (The entry address for a specific callback, which will be called if there is no ROM data available to initialize the NVRAM block. No specific callback routine needs to be called to initialize the NVRAM block with default data if it is not configured.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 




NvMSingleBlockCallback
======================================

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/NvM/image7.png
   :alt: NvMSingleBlockCallback容器配置图 (NvMSingleBlockCallback Container Configuration Diagram)
   :name: NvMSingleBlockCallback容器配置图 (NvMSingleBlockCallback Container Configuration Diagram)
   :align: center


.. centered:: **表 NvMSingleBlockCallback属性描述 (Property Description for NvMSingleBlockCallback)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - NvMSingleBlockCallback
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 块特定回调函数，该回调函数将在每个异步单个块请求终止时被调用。 (A specific callback function that will be called upon the termination of each individual asynchronous block request.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 




NvMTargetBlockReference
=======================================

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/NvM/image8.png
   :alt: NvMTargetBlockReference容器配置图 (Diagram for NvM Target Block Reference Container Configuration)
   :name: NvMTargetBlockReference容器配置图 (Diagram for NvM Target Block Reference Container Configuration)
   :align: center

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/NvM/image9.png
   :alt: NvMTargetBlockReference容器配置图1 (Diagram for NvM Target Block Reference Container Configuration)
   :name: NvMTargetBlockReference容器配置图1 (Diagram for NvM Target Block Reference Container Configuration)
   :align: center

.. centered:: **表 NvMTargetBlockReference属性描述 (Property Description of NvMTargetBlockReference)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - NvMNameOfEaBlock
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - EA块关联 (EA Block Associated)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - NvMNameOfFeeBlock
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - FEE块关联 (Fee Block Association)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 




NvmDemEventParameterRefs
----------------------------------------

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/NvM/image10.png
   :alt: NvmDemEventParameterRefs容器配置图 (NvmDemEventParameterRefs Container Configuration Diagram)
   :name: NvmDemEventParameterRefs容器配置图 (NvmDemEventParameterRefs Container Configuration Diagram)
   :align: center


.. centered:: **表 NvmDemEventParameterRefs属性描述 (Table NvmDemEventParameterRefs Property Description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - NVM_E_HARDWARE
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 硬件故障发生的事件DEM关联 (Events associated with hardware failure incidents DEM)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - NVM_E_INTEGRITY_FAILED
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - API请求完整性失败发生的事件DEM关联 (Failed event for API request integrity check associated with DEM)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - NVM_E_LOSS_OF_REDUNDANCY
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 冗余丢失发生的事件DEM关联 (Redundant loss occurring events DEM association)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - NVM_E_REQ_FAILED
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 请求失败发生的事件DEM关联 (Events associated with failure occurrences of request DEM)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - NVM_E_VERIFY_FAILED
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 校验失败发生的事件DEM关联 (Failure events for DEM association validation)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - NVM_E_WRITE_PROTECTED
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 请求写已经写保护的块发生的事件DEM关联 (Events associated with writing to blocks that are write-protected DEM)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - NVM_E_WRONG_BLOCK_ID
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 静态块ID检查失败发生的事件DEM关联 (Failed static block ID check associated with event DEM)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
