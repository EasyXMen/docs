===================================================
BndM
===================================================

文档信息
===================================================

版本历史
---------------------------------------------------
.. list-table::
   :header-rows: 1
   :stub-columns: 1

   * - 日期
     - 作者
     - 版本
     - 状态
     - 说明
   
   * - 2025/07/15
     - haibin.shao
     - V0.1
     - 发布
     - 首次发布

   * - 2025/11/28
     - peng.wu
     - V1.1
     - 修正(Modify)
     - 增加多分区功能的描述(Add the description of multi-partition)
   * - 2025/12/17
     - chao.sun
     - V1.2
     - 修正(Modify)
     - 调整文档架构和补充英文说明(Adjust the document structure and add English explanations)

参考文档(Reference Document)
---------------------------------------------------
.. list-table::
   :header-rows: 1
   :stub-columns: 1

   * - 分类(Category)
     - 标题(Title)
     - 版本(Version)
	
   * - SWS
     - AUTOSAR_CP_SWS_BulkNvDataManager.pdf
     - R23-11 2023-11-23
   * - SWS
     - AUTOSAR_CP_SWS_MemoryAccess.pdf
     - R23-11 2023-11-23
   * - RS
     - AUTOSAR_FO_RS_Diagnostics.pdf
     - R23-11 2023-11-23

术语与简写(Terms and Abbreviations)
===================================================

术语(Term)
---------------------------------------------------
.. list-table::
   :header-rows: 1
   :stub-columns: 1

   * - 术语(Term)
     - 解释(Explain)

   * - BlockDescriptor
     - BndM应在直接可访问内存中管理其BndM块。
       The BndM shall manage its BndM blocks in the direct accessible memory.
	 
   * - WriteStartPhase
     - 调用BndM_WriteStart将触发第二个（空闲）分区的准备。
       A call of BndM_WriteStart shall trigger the preparation of the 2nd (free) partition.
	 
   * - WriteBlockPhase
     - 调用BndM_WriteBlock将触发将数据写入第二个（未使用的）分区。不应该修改数据（ImplementationDataType）以允许指针访问。
       A call of BndM_WriteBlock shall trigger the writing of the data to the 2nd (unused) partition. The data (ImplementationDataType) shall be not modified to allow a pointer access.
	 
   * - WriteFinalizePhase
     - 调用BndM_WriteFinalize将触发第二个（未使用的）分区的结束。在后台，BndM通过将所有未更改的BndMBlockDescriptor复制到第二个（未使用的）分区，使第二个（未使用的）分区保持一致。如果最终化成功，BndM将使第二个（未使用的）分区变为活动分区，并触发回调Xxx_BndMWriteFinalizeFinish，结果设置为E_OK。
       A call of BndM_WriteFinalize shall trigger the finalization of the 2nd (unused) partition. In background the BndM shall make the 2nd (unused) partition consistent by coping all unchanged BndMBlockDescriptor to the 2nd (unused) partition.  If the finalization is successful the BndM shall make the 2nd (unused) partition to the active partition and trigger the callback Xxx_BndMWriteFinalizeFinish with the result set to E_OK.

简写(Abbreviation)
---------------------------------------------------
.. list-table::
   :header-rows: 1
   :stub-columns: 1

   * - 简写(Abbreviation)
     - 全称(Full name)
     - 解释(Explain)
	
   * - NvM
     - NVRAM Manager
     - 非易失RAM管理
   * - MemIf
     - Memory Abstraction Interface
     - 内存抽象接口
   * - Fee
     - Flash EEPROM Emulation
     - Flash EEPROM仿真
   * - Ea
     - EEPROM Abstraction
     - EEPROM抽象
   * - BndM
     - Bulk Non Volatile Data Manager
     - 批量非易失性数据管理器
   * - MemAcc
     - Memory Access
     - 统一内存访问
   * - MemDriver
     - Memory Driver
     - 统一内驱动
   * - ROM
     - Read-Only Memory
     - 只读存储器
   * - MROM
     - Mask Read-Only Memory
     - 掩模式只读存储器
   * - PROM
     - Programmable read-only memor
     - 可编程只读存储器
   * - EPROM
     - Erasable Programmable Read-Only Memory
     - 可擦除可编程只读存储器‌
   * - EEPROM
     - Electrically Erasable Programmable Read-Only Memory
     - 电可擦除可编程只读存储器
   * - HBM
     - High Bandwidth Memory
     - 高带宽内存
   * - DDR
     - Double Data Rate Synchronous Dynamic Random Access Memory
     - 双倍速率同步动态随机存储器
   * - FLASH
     - Electrically Erasable and Programmable ROM (Read Only Memory)
     - 电可擦可编程只读存储器(只读型存储器)
   * - NOR-FLASH
     - Not OR Flash Memory
     - N-OR型闪存，采用或非门电路结构，支持随机访问，主要用于代码存储和快速读取场景。
   * - NAND-FLASH
     - Not AND Flash Memory
     - N-AND型闪存，采用非与门电路结构
   * - RAM
     - Random Access Memory
     - 随机存取存储器
   * - SRAM
     - Static Random-Access Memory
     - 静态随机存取存储器
   * - DRAM
     - Dynamic Random Access Memory
     - 动态随机存取存储器
   * - SDRAM
     - Synchronous Dynamic Random Access Memory
     - 同步动态随机存取存储器
   * - API
     - Application Programming Interface
     - 应用编程接口
   * - Det
     - Default Error Tracer
     - 开发/运行时错误报错追踪
   * - Dcm
     - Diagnostic Communication Manager
     - 诊断通信管理
   * - Dem
     - Diagnostic Event Manager
     - 诊断事件管理
   * - EcuM
     - ECU State Manager
     - ECU状态管理器
   * - SchM
     - Basic Software Schedule Manager
     - 基础软件调度管理

简介(Introduction)
===================================================

对于变体编码（variant-coding）等用例场景，对于非易失性大容量数据的需求正在增加。此类数据经常使用，但很少更新。与NvM相比，BndM提供了一个 API来直接从Flash存储单元中读取数据。带来的好处就是避免了RAM镜像，但缺点就是数据的写入会更加复杂。

For use case scenarios such as variable-coding, the demand for non-volatile large-capacity data is increasing. Such data is frequently used but rarely updated. Compared with NvM, BndM provides an API to directly read data from Flash storage units. The advantage it brings is that it avoids RAM mirroring, but the disadvantage is that data writing will be more complicated.

变体编码（Variant coding）是车辆特定的数据集，它在每辆车的生产过程中计算并生成，当然也在生产过程中保存。

Variant coding is a vehicle-specific dataset that is calculated and generated during the production process of each vehicle and, of course, is also saved during the production process.

BndM模块是AUTOSAR中用于处理大批量非易失性数据（NvData）存储和管理的关键模块；BndM 通过提供批量数据存储和恢复功能，增强了系统的可靠性和数据一致性。

The BndM module is a key module in AUTOSAR for processing the storage and management of large volumes of non-volatile data (NvData). BndM enhances the reliability of the system and data consistency by providing batch data storage and recovery functions.

.. figure:: /_static/参考手册(Module_Reference_Manual)/BndM/BndMInAutosarLayer.png
   :name: BndM模块层次图
   :align: center

   BndM模块层次图

如图 :ref:`BndM模块层次图` 所示，BndM模块处于AUTOSAR软件架构中的通信栈服务层，BndM模块与存储栈抽象层的MemAcc组件进行交互，与诊断栈服务层的Dcm/Det组件进行交互。
As shown in the figure :ref: 'BndM Module Hierarchy Diagram', the BndM module is located in the communication stack service layer of the AUTOSAR software architecture. The BndM module interacts with the MemAcc component in the storage stack abstraction layer and the Dcm/Det component in the diagnostic stack service layer.


BndM对存储栈提供如下功能职责：

BndM provides the following functional responsibilities for the storage stack：

.. list-table::
   :header-rows: 1
   :stub-columns: 1

   * - 功能类型
     - 功能描述
	
   * - 批量数据存储（Bulk Data Storage）
     - 管理批量非易失性数据的存储过程，提高数据写入效率
       Manage the stored procedures of batch non-volatile data to improve the efficiency of data writing
   * - 数据恢复（Data Recovery）
     - 提供从非易失性存储介质中恢复数据的功能，确保系统重启后数据的一致性
       Provide the function of recovering data in non-volatile storage media to ensure the consistency of data after system restart
   * - 错误检测和处理（Error Detection and Handling）
     - 监控数据存储和恢复过程中的各种错误，并采取相应的恢复措施
       Monitor various errors during the data storage and recovery process and take corresponding recovery measures
   * - 数据一致性管理（Data Consistency Management）
     - 保证在多任务并发情况下，数据的一致性和完整性
       Ensure the consistency and integrity of data in the case of concurrent multiple tasks
   * - 优化存储操作（Optimize storage operations）
     - 针对批量数据操作进行优化，减少存储器写入周期，延长存储器寿命
       Optimize for batch data operations to reduce memory write cycles and extend memory lifespan

功能描述(Functional Description)
=====================================


公共特性(Public Features)
----------------------------

多核多分区功能(Multi-core and Multi-partition Features)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
该模块仅支持单分区功能。

This module only supports single-partition functionality.

BndM多分区场景下，必须保持与上层模块在同一分区。

In the BndM multi-partition scenario, it is necessary to remain in the same partition as the upper-level module.

.. only:: doc_pbs

   PBS功能(PBS Features)
   ~~~~~~~~~~~~~~~~~~~~~~~~
   无配置项，不支持。

   No configurations, not supported.

Memmap功能(Memmap Features)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
memmap文件是静态的。存在BNDM_START_SEC_CODE、BNDM_STOP_SEC_CODE、BNDM_START_SEC_VAR_CLEARED_UNSPECIFIED、BNDM_STOP_SEC_VAR_CLEARED_UNSPECIFIED、BNDM_START_SEC_VAR_CLEARED_8、BNDM_STOP_SEC_VAR_CLEARED_8、BNDM_START_SEC_VAR_CLEARED_BOOLEAN、BNDM_STOP_SEC_VAR_CLEARED_BOOLEAN、BNDM_START_SEC_VAR_CLEARED_PTR、BNDM_STOP_SEC_VAR_CLEARED_PTR、BNDM_START_SEC_CONFIG_DATA_UNSPECIFIED、BNDM_STOP_SEC_CONFIG_DATA_UNSPECIFIED、BNDM_START_SEC_CONFIG_DATA_PTR、BNDM_STOP_SEC_CONFIG_DATA_PTR字段。

The memmap file is static.There are BNDM_START_SEC_CODE、BNDM_STOP_SEC_CODE、BNDM_START_SEC_VAR_CLEARED_UNSPECIFIED、BNDM_STOP_SEC_VAR_CLEARED_UNSPECIFIED、BNDM_START_SEC_VAR_CLEARED_8、BNDM_STOP_SEC_VAR_CLEARED_8、BNDM_START_SEC_VAR_CLEARED_BOOLEAN、BNDM_STOP_SEC_VAR_CLEARED_BOOLEAN、BNDM_START_SEC_VAR_CLEARED_PTR、BNDM_STOP_SEC_VAR_CLEARED_PTR、BNDM_START_SEC_CONFIG_DATA_UNSPECIFIED、BNDM_STOP_SEC_CONFIG_DATA_UNSPECIFIED、BNDM_START_SEC_CONFIG_DATA_PTR、BNDM_STOP_SEC_CONFIG_DATA_PTR fields.

独占区功能(Exclusive Area Features)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
None.

模块特性(Module Features)
----------------------------

编程基本原理：Program Basic Principles of BndM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

基本思想是对数据块进行A/B分区切换。意味着完整的非易失性大容量数据（Bulk Nv Data）将存储在分区A中。当写入动作开始时（BndM_WriteStart），B分区需要被擦除。更新的数据块（BndM_WriteBlock）将被写入到分区B。最终确定阶段（BndM_WriteFinalize）将使分区B保持一致（通过将未更新的块复制到分区B）并将激活分区切换到B（进一步调用BndM_GetBlockPtr将指向分区B中的数据）。
The basic idea is to perform A/B partition switching on data blocks. It means that the complete non-volatile Bulk Nv Data will be stored in partition A. When the write operation begins (BndM_WriteStart), partition B needs to be erased. The updated data block (BndM_WriteBlock) will be written to partition B. The final determination phase (BndM_WriteFinalize) will keep partition B consistent (by copying the unupdated block to partition B) and switch the active partition to B (further calls to BndM_GetBlockPtr will point to the data in partition B).

.. list-table::
   :header-rows: 1
   :stub-columns: 1

   * - 编程序列(Programming Sequence)
     - 功能描述(Function Description)
	
   * - WriteStart
     - 写入准备阶段(Write preparation phase)：
	   (1) BndM模块的上层组件通过调用BndM_WriteStart函数接口，向BndM模块发起一个写入作业的请求任务；
	       The upper-level component of the BndM module initiates a request task for a write job to the BndM module by calling the BndM_WriteStart API.
	   (2) BndM模块获取A-B两个分区的激活状态和版本控制信息；相对而言，当前A分区处于激活状态，B分区处于未激活状态；
	       The BndM module acquires the activation status and version control information of partitions A and B. Relatively speaking, currently partition A is in an active state, while partition B is in an inactive state.
	   (3) BndM模块通过调用MemAcc组件的MemAcc_Erase函数接口，对未激活分区B执行擦除操作；
	       The BndM module performs an erase operation on the inactive partition B by calling the MemAcc_Erase API of the MemAcc component.
	   (4) BndM模块通过调用MemAcc组件的MemAcc_GetJobResult/MemAcc_GetJobStatus函数接口，获取擦除操作的作业结果/状态；
	       The BndM module acquires the job result/status of the erasure operation by calling the MemAcc_GetJobResult /MemAcc_GetJobStatus API of the MemAcc component.
	   (5) 如果检测到擦除作业异常，则通过调用可配置Xxx_BndMWriteStartFinish(result = E_NOT_OK)函数接口，向上层组件通知BndM写入准备错误的反馈状态，并立即释放资源，结束本次写入作业任务；
	       If an anomaly of the erase job is detected, the feedback status of the BndM write preparation error is notified to the upper component by calling the configurable Xxx_BndMWriteStartFinish(result = E_NOT_OK) API, and the resources are immediately released to end this write job task.
	   (6) 如果检测到擦除作业正常，则通过调用可配置Xxx_BndMWriteStartFinish(result = E_OK)函数接口，向上层组件通知BndM写入准备成功的反馈状态，并通知上层允许执行下一个阶段的作业任务。
	       If it is detected that the erasure job is normal, then by calling the configurable Xxx_BndMWriteStartFinish(result = E_OK) API, notify the upper-layer component of the feedback status that the BndM write preparation is successful, and notify the upper-layer to allow the execution of the next stage of the job task.
   * - WriteBlock
     - 写入数据阶段(Data Writing Stage)：
	   (1) BndM模块的上层组件通过调用BndM_WriteBlock函数接口，请求BndM模块开始执行编程任务。
	       The upper-level components of the BndM module request the BndM module to start performing programming tasks by calling the BndM_WriteBlock API.
	   (2) BndM模块通过调用MemAcc组件的MemAcc_Write函数接口，对未激活分区B待更新Block块执行编程操作。
	       The BndM module performs programming operations on the unactivated Block B to be updated by calling the MemAcc_Write API of the MemAcc component.
	   (3) BndM模块通过调用MemAcc组件的MemAcc_GetJobResult/MemAcc_GetJobStatus函数接口，获取编程操作的作业结果/状态；
	       The BndM module acquires the job result/status of the programming operation by calling the MemAcc_GetJobResult/MemAcc_GetJobStatus API of the MemAcc component.
	   (4) 如果检测到编程作业异常，则通过调用可配置Xxx_BndMWriteBlockFinish(result = E_NOT_OK)函数接口，向上层组件通知BndM写入数据错误的反馈状态，并立即释放资源，结束本次写入作业任务；
	       If an abnormal programming job is detected, the feedback status of the BndM writing data error is notified to the upper-layer component by calling the configurable Xxx_BndMWriteBlockFinish(result = E_NOT_OK) API, and resources are immediately released to end this writing job task.
	   (5) 如果检测到编程作业正常，则通过调用可配置Xxx_BndMWriteBlockFinish(result = E_OK)函数接口，向上层组件通知BndM写入数据成功的反馈状态，并通知上层允许执行下一个阶段的作业任务。
	       If it is detected that the programming job is normal, by calling the configurable Xxx_BndMWriteBlockFinish(result = E_OK) API, the feedback status of BndM writing data successfully is notified to the upper component, and the upper component is informed that the job task of the next stage is allowed to be executed.
   * - WriteFinalize
     - 写入收尾阶段(Write to the finishing stage)：
	   (1) BndM模块的上层组件通过调用BndM_WriteFinalize函数接口，请求BndM模块开始执行终结任务。
	       The upper-level components of the BndM module request the BndM module to start the finalization task by calling the BndM_WriteFinalize API.
	   (2) 对未激活分区B未使用的Block块，需要从A激活分区拷贝对应Block块的数据，重复以上编程作业任务，将拷贝的数据写入到未激活分区B对应Block的内存单元中。
	       For the unused blocks in unactivated partition B, it is necessary to copy the data of the corresponding Block from the activated partition A. Repeat the above programming task and write the copied data to the memory unit of the corresponding Block in unactivated partition B.
	   (3) BndM模块通过调用MemAcc组件的MemAcc_Write函数接口，对未激活分区B的“编程标签-版本控制信息”执行更新编程操作。
	       The BndM module performs an update programming operation on the "programming Label - version control information" of the inactive partition B by calling the MemAcc_Write API of the MemAcc component.
	   (4) BndM模块通过调用MemAcc组件的MemAcc_GetJobResult/MemAcc_GetJobStatus函数接口，获取编程操作的作业结果/状态；
	       The BndM module acquires the job result/status of the programming operation by calling the MemAcc_GetJobResult/MemAcc_GetJobStatus API of the MemAcc component.
	   (5) 如果检测到编程作业异常，则通过调用可配置Xxx_BndMWriteFinalizeFinish(result = E_NOT_OK)函数接口，向上层组件通知BndM写入终结错误的反馈状态，并立即释放资源，结束本次写入作业任务；
	       If an abnormal programming job is detected, the feedback status of the BndM write termination error is notified to the upper-layer component by calling the configurable Xxx_BndMWriteFinalizeFinish(result = E_NOT_OK) API, and resources are immediately released to end this write job task.；
	   (6) 如果检测到编程作业正常，则通过调用可配置Xxx_BndMWriteFinalizeFinish(result = E_OK)函数接口，向上层组件通知BndM写入终结成功的反馈状态，并通知上层允许执行下一个阶段的作业任务。
	       If it is detected that the programming job is normal, by calling the configurable Xxx_BndMWriteFinalizeFinish(result = E_OK) API, the feedback status of the successful completion of BndM writing is notified to the upper-level component, and the upper-level component is informed that the job task of the next stage is allowed to be executed.
	   (7) 将A-B分区的激活状态进行切换，并立即释放资源，结束本次写入作业任务。
	       Switch the activation status of partitions A-B and immediately release the resources to end this write job task.
	   (8) BndM模块的上层组件通过调用BndM_GetBlockPtr函数接口，从BndM模块指定地址的内存单元中获取数据，并对数据进行校验，来判决本次写入作业是否更新成功。
	       The upper-layer components of the BndM module get data from the memory unit at the specified address of the BndM module by calling the BndM_GetBlockPtr API and verify the data to determine whether the current write job has been updated successfully.

基于BndM组件的存储控制机制（Storage control mechanism based on BndM components）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: /_static/参考手册(Module_Reference_Manual)/BndM/StorageControlMechanism.png
   :name: BndM模块的存储控制机制图
   :align: center

   BndM模块的存储控制机制图

如图 :ref:`BndM模块的存储控制机制图` 所示，BndM模块的批量数据写入请求大致分为三个阶段，写入准备阶段，写入数据阶段，写入收尾阶段，并且写入作业的控制完全受制于MemAcc的控制流程。
As shown in the figure :ref: 'Storage Control Mechanism Diagram of BndM Module', the batch data write requests of BndM module are roughly divided into three stages: write preparation stage, write data stage, and write closure stage. Moreover, the control of write jobs is completely subject to the control flow of MemAcc.

基于BndM组件的存储栈交互关联关系（The storage stack interaction association relationship based on BndM components）
基于BndM组件的存储栈交互关联关系（The storage stack interaction association relationship based on BndM components）

.. figure:: /_static/参考手册(Module_Reference_Manual)/BndM/CrossDependency.png
   :name: BndM模块的存储栈交互关联关系图
   :align: center

   BndM模块的存储栈交互关联关系图

如图 :ref:`BndM模块的存储栈交互关联关系图` 所示，BndM模块的上层与Dcm模块进行交互，一般用于UDS-WriteDataByDID，下层直接与MemAcc模块进行交互，间接对底层Flash存储单元执行写入操作。
As shown in the figure :ref: 'The storage Stack Interaction Association Diagram of the BndM module', the upper layer of the BndM module interacts with the Dcm module, which is generally used for UDS-WriteDataByDID, and the lower layer directly interacts with the MemAcc module, indirectly performing write operations on the underlying Flash storage unit.

.. figure:: /_static/参考手册(Module_Reference_Manual)/BndM/InteractiveInterface.png
   :name: BndM模块的存储栈API关联关系图
   :align: center

   BndM模块的存储栈API关联关系图

如图 :ref:`BndM模块的存储栈API关联关系图` 所示，BndM模块的上层Dcm模块调用BndM_WriteStart/BndM_WriteBlock/BndM_WriteFinalize等接口来请求写入作业，并通过Xxx_BndMWriteStartFinish/Xxx_BndMWriteBlockFinish/Xxx_BndMWriteFinalizeFinish回调函数的通知，来获取每一个阶段的作业结果；BndM模块调用下层的MemAcc_Erase/MemAcc_Write/MemAcc_GetJobResult/MemAcc_GetJobStatus来完成内存块的擦除&编程的作业任务。
As shown in the figure :ref: 'The API Association Diagram of the BndM module's storage stack', the upper-layer Dcm module of the BndM module calls interfaces such as BndM_WriteStart/BndM_WriteBlock/BndM_WriteFinalize to request write jobs And obtain the job results of each stage through the notification of the callback functions Xxx_BndMWriteStartFinish/Xxx_BndMWriteBlockFinish/Xxx_BndMWriteFinalizeFinish; The BndM module calls the lower-level MemAcc_Erase/MemAcc_Write/MemAcc_GetJobResult/MemAcc_GetJobStatus to complete the memory block erasure and programming job tasks.

基于BndM组件的数据块写入控制流程（Data block write control flow based on BndM components）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: /_static/参考手册(Module_Reference_Manual)/BndM/WriteOperationControlFlow.png
   :name: BndM模块的数据块写入操作控制流程图
   :align: center

   BndM模块的数据块写入操作控制流程图

如图 :ref:`BndM模块的数据块写入操作控制流程图` 所示
As shown in the figure :ref: 'Control Flowchart for Data Block Write Operations of BndM Module'


基于BndM组件的块描述访问（Block description access based on BndM components）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

(1) BndM模块能够通过指针的方式直接访问内存中管理的BndMBlockDescriptor块。
    The BndM module can directly access the BndMBlockDescriptor block managed in memory through a pointer.
(2) BndM_GetBlockPtr的函数调用能够将基指针传递给当前激活分区中相应的BndMBlockDescriptor块。
    The function call of BndM_GetBlockPtr can pass the base pointer to the corresponding BndMBlockDescriptor block in the currently activated partition.
(3) 函数实现隐藏目的：用于从非易失性存储单元中读取BndM块的数据；读取操作就跟访问RAM的方式一样，可以直接通过指针的方式获取。
    The function implements a hidden purpose: it is used to read the data of BndM blocks from non-volatile storage units. The reading operation is just like accessing RAM and can be directly obtained through a pointer.

基于BndM组件的写入准备描述（Write preparation description based on BndM components）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

(1) BndM_WriteStart的函数调用将触发第二个（空闲）分区的准备；对分区执行擦除操作。
    The function call of BndM_WriteStart will trigger the preparation of the second (idle) partition; Perform an erase operation on the partition.
(2) 在成功完成第二个（空闲）分区的准备后,可以写入第二个分区，并通过异步操作在BndM_MainFunction的上下文中调用回调函数Xxx_BndMWriteStartFinish，并将结果设置为E_OK。
    After successfully completing the preparation of the second (idle) partition, the second partition can be written, and the callback function Xxx_BndMWriteStartFinish can be called in the context of BndM_MainFunction through asynchronous operations, and the result is set to E_OK.
(3) 如果BndM_WriteStart的函数调用处于已激活写入阶段（BndM_WriteStart和BndM_WriteFinalize之间的阶段），则BndM_WriteStart的函数调用将会被拒绝，并且错误代码会被设置为E_NOT_OK。
    If the function call of BndM_WriteStart is in the activated write phase (the phase between BndM_WriteStart and BndM_WriteFinalize), the function call of BndM_WriteStart will be rejected and the error code will be set to E_NOT_OK.

基于BndM组件的写入数据描述（Write data description based on BndM components）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

(1) BndM_WriteBlock的函数调用能够触发将数据写入第二个（未使用的）分区；ImplementationDataType类型的数据不允许通过指针访问并被修改。
    The function call of BndM_WriteBlock can trigger the writing of data to the second (unused) partition. Data of the ImplementationDataType type is not allowed to be accessed and modified through Pointers.
(2) 在第二个（空闲）分区的写入完成后，并通过异步操作在BndM_MainFunction的上下文中调用回调函数Xxx_BndMWriteBlockFinish，并将结果设置为E_OK。
    After the write to the second (idle) partition is completed, call the callback function Xxx_BndMWriteBlockFinish in the context of BndM_MainFunction through an asynchronous operation, and set the result to E_OK.
(3) 如果在先前BndM_WriteStart函数未曾调用的情况下，则BndM_WriteBlock函数的调用将被拒绝，并将错误代码设置为E_NOT_OK。
    If the BndM_WriteStart function has not been called before, the call to the BndM_WriteBlock function will be rejected and the error code will be set to E_NOT_OK.
(4) 如果BndM_WriteBlock函数的调用是在另一个相同的或另一个块正在写的时候完成的，则BndM_WriteBlock函数的调用将被拒绝，并将错误码设置为E_NOT_OK。
    If the call to the BndM_WriteBlock function is completed when another identical or another block is being written, the call to the BndM_WriteBlock function will be rejected and the error code will be set to E_NOT_OK.
(5) 如果BndM_WriteBlock函数的调用是在BndM的终结模式内或之后进行的，则BndM_WriteBlock函数的调用将被拒绝，并将错误码设置为E_NOT_OK。
    If the call of the BndM_WriteBlock function is made within or after the terminal mode of BndM, the call of the BndM_WriteBlock function will be rejected and the error code will be set to E_NOT_OK.

基于BndM组件的写入收尾描述（Write closure description based on BndM components）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

(1) BndM_WriteFinalize函数的调用将触发第二个（未使用的）分区的最终化工作（finalization）。在后台通过异步操作方式，BndM能够将所有未更改的BndMBlockDescriptor复制到第二个（未使用的）分区来使第二个（未使用的）分区的数据保持一致。
    The call to the BndM_WriteFinalize function will trigger the finalization of the second (unused) partition. In the background, through asynchronous operation mode, BndM can copy all the unaltered BNDMBlockdescriptors to the second (unused) partition to keep the data in the second (unused) partition consistent.
(2) 如果最终确定成功，BndM能够将第二个（未使用的）分区设为激活分区，并调用回调函数 Xxx_BndMWriteFinalizeFinish，并将结果设置为E_OK。
    If it is finally confirmed to be successful, BndM can set the second (unused) partition as the activation partition and call the callback function Xxx_BndMWriteFinalizeFinish, and set the result to E_OK.
(3) 如果最终确定不成功，则会因为第二个分区数据不一致，导致数据不能使用；BndM应将当前激活分区保持为激活分区，并触发回调Xxx_BndMWriteFinalizeFinish，并将结果设置为E_NOT_OK。
    If it is ultimately determined to be unsuccessful, the second partition data will be inconsistent, resulting in the data being unusable. BndM should keep the current activation partition as the activation partition, trigger the callback Xxx_BndMWriteFinalizeFinish, and set the result to E_NOT_OK.
(4) 在先前BndM_WriteStart函数未被调用的情况下，或者BndM已经在最终化模式（finalization mode）中，当检测到BndM_WriteFinalize函数被调用，则BndM_WriteFinalize函数将抛出一个BNDM_E_WRONG_SEQUENCE的DET错误。
    In the case where the BndM_WriteStart function was not called previously, or BndM was already in the finalization mode, when it was detected that the BndM_WriteFinalize function was called, Then the BndM_WriteFinalize function will throw a DET error of BNDM_E_WRONG_SEQUENCE.

偏差（Deviation）
===================================================

.. list-table::
   :header-rows: 1
   :stub-columns: 1

   * - 需求类型(Type of demand)
     - 详细描述(Detailed description)
     - 需求编号(Requirement Number)
	
   * - API specification
     - 导入数据类型由Fls和MemIf的来源更改成MemAcc
	     Fls_AddressType --> MemAcc_AddressType
	     Fls_LengthType --> MemAcc_LengthType
	     MemIf_JobResultType --> MemAcc_JobResultType
	     MemIf_StatusType --> MemAcc_JobStatusType
       (The data import types have been changed from Fls and MemIf sources to MemAcc
        Fls_AddressType --> MemAcc_AddressType
        Fls_LengthType --> MemAcc_LengthType
        MemIf_JobResultType --> MemAcc_JobResultType
        MemIf_StatusType --> MemAcc_JobStatusType)
     - SWS_BndM_01018
   * - API specification
     - 可选接口由Fls的来源更改成MemAcc
	     Fls_Write --> MemAcc_Write
	     Fls_Erase --> MemAcc_Erase
	     Fls_Cancel --> MemAcc_Cancel
	     Fls_GetJobResult --> MemAcc_GetJobResult
	     Fls_GetStatus --> MemAcc_GetJobStatus
       (Optional interfaces changed from Fls source to MemAcc
        Fls_Write --> MemAcc_Write
        Fls_Erase --> MemAcc_Erase
        Fls_Cancel --> MemAcc_Cancel
        Fls_GetJobResult --> MemAcc_GetJobResult
        Fls_GetStatus --> MemAcc_GetJobStatus)
     - SWS_BndM_01020
   * - Configuration specification
     - BndMEraseValue：新增配置项(Add new configuration item)
     - N/A
   * - Configuration specification
     - BndMHeaderFile：新增配置项(Add new configuration item)
     - N/A
   * - Configuration specification
     - BndMDeviceIndex：删除配置项(Add new configuration item)
     - ECUC_BndM_00008
   * - Configuration specification
     - BndMMemAccAddressArea：新增配置项(Add new configuration item)
     - N/A

集成(Integration)
=====================

文件列表(File List)
---------------------

静态文件(Static Files)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :stub-columns: 1

   * - 文件
     - 描述

   * - BndM.c
     - BndM模块的总体框架实现源文件
       The overall framework implementation source file of the BndM module
   * - BndM.h
     - BndM模块的外部接口声明头文件
       The external interface declaration header file of the BndM module
   * - BndM_Internal.h
     - BndM模块内部公用接口声明，全局变量声明，宏定义和数据类型定义头文件
       The BndM module's internal common interface declaration, global variable declaration, macro definition, and data type definition header files
   * - BndM_OptMacros.h
     - BndM模块内部可选配置宏定义头文件
       The BndM module can optionally configure macro definition header files internally
   * - BndM_Types.h
     - BndM模块的共用宏定义和数据类型定义文件
       The shared macro definition and data type definition file of the BndM module
   * - BndM_MemMap.h
     - BndM模块的内存映射头文件
       The memory-mapped header file of the BndM module

动态文件(Dynamic Files)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :stub-columns: 1

   * - 文件
     - 描述

   * - BndM_Cfg.h
     - BndM模块中常规配置的宏定义文件
       The macro definition file of the regular configuration in the BndM module
   * - BndM_Cfg.c
     - BndM模块中特定配置的数据变量定义文件
       The data variable definition file for specific configurations in the BndM module

错误处理(Error Handling)
---------------------------

开发错误(Development Error)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :stub-columns: 1

   * - Error code
     - Value[hex]
     - Description

   * - BNDM_E_PARAM
     - 0x01
     - API service called with wrong parameter
       使用错误的参数调用API服务
   * - BNDM_E_WRONG_SEQUENCE
     - 0x02
     - API called in wrong sequence
       API调用序列错误

运行时错误(Runtime error)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
无。

None.

产品错误(Product error)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
无。

None.

接口描述(Interface Description)
=================================================

.. 目前能够自动生成的有类型定义，普通函数，回调函数。
.. 有些模块的API来自多个头文件，需要自行裁剪合并
.. 引用接口描述。来自于code->doxygen->xml->rst
.. include:: BndM_api.rst
.. include:: BndM_Internal_api.rst

可配置回调函数(Configurable callback function)
------------------------------------------------
.. 可选的章节，根据模块实际情况确定
.. 格式同提供的服务

BndM_MainFunction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

   void BndM_MainFunction_<ComMChannel.ShortName>(void)

This function shall perform the processing of the AUTOSAR BndM activities that are not directly initiated by the calls from the RTE.
该函数将执行非由RTE调用直接发起的AUTOSAR BndM活动的处理。

**Sync/Async**
   Synchronous

**Reentrancy**
   Non Reentrant

**Return type**
   void

依赖的服务(Dependent services)
--------------------------------------------------

导入类型：Imported Types
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :stub-columns: 1

   * - Module
     - Header File
     - Imported Type

   * - MemAcc
     - MemAcc.h
     - MemAcc_AddressType
   * - MemAcc
     - MemAcc.h
     - MemAcc_LengthType
   * - MemAcc
     - MemAcc.h
     - MemAcc_DataType
   * - MemAcc
     - MemAcc.h
     - MemAcc_JobResultType
   * - MemAcc
     - MemAcc.h
     - MemAcc_JobStatusType
   * - MemAcc
     - MemAcc.h
     - MemAcc_JobType
   * - MemAcc
     - MemAcc.h
     - MemAcc_MemAddressType
   * - MemAcc
     - MemAcc.h
     - MemAcc_MemDataType
   * - MemAcc
     - MemAcc.h
     - MemAcc_MemJobResultType
   * - MemAcc
     - MemAcc.h
     - MemAcc_MemLengthType
   * - MemAcc
     - MemAcc.h
     - MemAcc_MemEraseFuncType
   * - MemAcc
     - MemAcc.h
     - MemAcc_MemWriteFuncType
   * - MemAcc
     - MemAcc.h
     - MemAcc_MemGetJobResultFuncType
   * - MemAcc
     - MemAcc.h
     - MemAcc_MemGetStatusFuncType
   * - Std
     - Std_Types.h
     - Std_ReturnType
   * - Std
     - Std_Types.h
     - Std_VersionInfoType

强制接口(Mandatory interface)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. 可选的章节，根据模块实际情况确定

无。

None.

可选接口(Optional interface)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. 可选的章节，根据模块实际情况确定
.. 格式同强制接口

.. list-table::
   :header-rows: 1
   :stub-columns: 1

   * - API Function
     - Header File
     - Description

   * - Det_ReportError
     - Det.h
     - Service to report development errors.
       用于报告开发错误的服务。
   * - Det_ReportRuntimeError
     - Det.h
     - Service to report runtime errors.
       服务报告运行时错误。
   * - MemAcc_Write
     - MemAcc.h
     - Service to Writes one or more complete Memory Area.
       写入一个或多个完整内存区域的服务。
   * - MemAcc_Erase
     - MemAcc.h
     - Service to Erases Memory Area sector.
       Service to Erases Memory Area sector.
   * - MemAcc_Cancel
     - MemAcc.h
     - Service to Cancels an ongoing job.
       用于取消正在进行的作业的服务。
   * - MemAcc_GetJobResult
     - MemAcc.h
     - Service to returns the result of the last job.
       返回最后一个作业的结果的服务。
   * - MemAcc_GetJobStatus
     - MemAcc.h
     - Service to Returns the Memory Area state.
       返回内存区域状态的服务。
   * - MemAcc_GetMemoryInfo
     - MemAcc.h
     - Service to returns the memory information of given area.
       返回给定区域的内存信息的服务。

配置接口(Configuration Interface)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :stub-columns: 1

   * - API Function
     - Header File
     - Description

   * - SchM_Enter_BndM_BNDM_EXCLUSIVE_AREA_0
     - SchM_BndM.h
     - Enter exclusive area ExclusiveArea0.
   * - SchM_Exit_BndM_BNDM_EXCLUSIVE_AREA_0
     - SchM_BndM.h
     - Enter exclusive area ExclusiveArea0.
   * - Xxx_BndMWriteStartFinish
     - BndM_Externals.h
     - This callback function is called when BndM_WriteStart is finished.
   * - Xxx_BndMWriteBlockFinish
     - BndM_Externals.h
     - This callback function is called when BndM_WriteBlock is finished.
   * - Xxx_BndMWriteFinalizeFinish
     - BndM_Externals.h
     - This callback function is called when BndM_WriteFinalize is finished.

配置描述(Configuration Description)
=================================================
.. 1. 配置建议以 **功能** 为导向，从 **集成** 的角度，挑重点，常用，典型配置举例讲解。示例中若需要依赖其他模块的配置，也可以截图描述，配置截图不局限于本模块。重点是功能导向，把一件事讲清楚
.. 2. 不必呈现所有容器，配置细节的属性，可能用户不太关心
.. 3. 配置项描述等信息，在工具界面上都能看到

BndM模块的常规配置(General Configuration of the BndM Module)
--------------------------------------------------------------

.. figure:: /_static/参考手册(Module_Reference_Manual)/BndM/BndMGeneral.PNG
   :name: BndM模块中的常规配置项参数描述
   :align: center

   BndM模块中的常规配置项参数描述

BndM模块的常规配置的参数列表(Parameter list for the standard configuration of the BndM module)：

.. table:: BndMGeneral
   :name: BndMGeneral
   :align: left

   +--------------------------+------------------------------------------------------------------------------------------------------------------+
   | BndMGeneral              | Configuration of the BulkNvDataManager module.                                                                   |
   +==========================+================+=================================================================================================+
   | BndMVersionInfoApi       | Description    | Pre-processor switch to enable / disable the API to read out the modules version information.   |
   |                          +----------------+-------------------------------------------------------------------------------------------------+
   |                          | PB Supported   | false                                                                                           |
   |                          +----------------+-------------------------------------------------------------------------------------------------+
   |                          | Multiplicity   | 1                                                                                               |
   |                          +----------------+-------------------------------------------------------------------------------------------------+
   |                          | Type           | boolean                                                                                         |
   |                          +----------------+-------------+-----------------------------------------------------------------------------------+
   |                          | Value Range    | true        | Version info API enabled                                                          |
   |                          |                +-------------+-----------------------------------------------------------------------------------+
   |                          |                | false       | Version info API disabled                                                         |
   |                          +----------------+-------------+-----------------------------------------------------------------------------------+
   |                          | Default Value  | false                                                                                           |
   |                          +----------------+-------------------------------------------------------------------------------------------------+
   |                          | Dependency     | Depends on the configuration of Det                                                             |
   +--------------------------+----------------+-------------------------------------------------------------------------------------------------+
   | BndMDevErrorDetect       | Description    | Switches the development error detection and notification on or off.                            |
   |                          +----------------+-------------------------------------------------------------------------------------------------+
   |                          | PB Supported   | false                                                                                           |
   |                          +----------------+-------------------------------------------------------------------------------------------------+
   |                          | Multiplicity   | 1                                                                                               |
   |                          +----------------+-------------------------------------------------------------------------------------------------+
   |                          | Type           | boolean                                                                                         |
   |                          +----------------+-------------+-----------------------------------------------------------------------------------+
   |                          | Value Range    | true        | detection and notification is enabled.                                            |
   |                          |                +-------------+-----------------------------------------------------------------------------------+
   |                          |                | false       | detection and notification is disabled.                                           |
   |                          +----------------+-------------+-----------------------------------------------------------------------------------+
   |                          | Default Value  | false                                                                                           |
   |                          +----------------+-------------------------------------------------------------------------------------------------+
   |                          | Dependency     | Depends on the configuration of Det                                                             |
   +--------------------------+----------------+-------------------------------------------------------------------------------------------------+
   | BndMMainFunctionPeriod   | Description    | The period between successive calls to the main function in seconds.                            |
   |                          +----------------+-------------------------------------------------------------------------------------------------+
   |                          | PB Supported   | false                                                                                           |
   |                          +----------------+-------------------------------------------------------------------------------------------------+
   |                          | Multiplicity   | 1                                                                                               |
   |                          +----------------+-------------------------------------------------------------------------------------------------+
   |                          | Type           | Float                                                                                           |
   |                          +----------------+-------------------------------------------------------------------------------------------------+
   |                          | Value Range    | 0..INF                                                                                          |
   |                          +----------------+-------------------------------------------------------------------------------------------------+
   |                          | Default Value  | N/A                                                                                             |
   |                          +----------------+-------------------------------------------------------------------------------------------------+
   |                          | Dependency     | N/A                                                                                             |
   +--------------------------+----------------+-------------------------------------------------------------------------------------------------+
   | BndMEraseValue           | Description    | Value of an erased BndM cell.                                                                   |
   |                          +----------------+-------------------------------------------------------------------------------------------------+
   |                          | PB Supported   | false                                                                                           |
   |                          +----------------+-------------------------------------------------------------------------------------------------+
   |                          | Multiplicity   | 1                                                                                               |
   |                          +----------------+-------------------------------------------------------------------------------------------------+
   |                          | Type           | Integer                                                                                         |
   |                          +----------------+-------------------------------------------------------------------------------------------------+
   |                          | Value Range    | 0..255                                                                                          |
   |                          +----------------+-------------------------------------------------------------------------------------------------+
   |                          | Default Value  | N/A                                                                                             |
   |                          +----------------+-------------------------------------------------------------------------------------------------+
   |                          | Dependency     | N/A                                                                                             |
   +--------------------------+----------------+-------------------------------------------------------------------------------------------------+
   | BndMBufferAlignmentValue | Description    | Parameter determines the alignment of the start address that Fee buffers need to have.          |
   |                          |                | Value shall be inherited from MemAccBufferAlignmentValue.                                       |
   |                          +----------------+-------------------------------------------------------------------------------------------------+
   |                          | PB Supported   | false                                                                                           |
   |                          +----------------+-------------------------------------------------------------------------------------------------+
   |                          | Multiplicity   | 0..1                                                                                            |
   |                          +----------------+-------------------------------------------------------------------------------------------------+
   |                          | Type           | Symbolic name reference to MemAccAddressAreaConfiguration                                       |
   |                          +----------------+-------------------------------------------------------------------------------------------------+
   |                          | Value Range    | N/A                                                                                             |
   |                          +----------------+-------------------------------------------------------------------------------------------------+
   |                          | Default Value  | N/A                                                                                             |
   |                          +----------------+-------------------------------------------------------------------------------------------------+
   |                          | Dependency     | N/A                                                                                             |
   +--------------------------+----------------+-------------------------------------------------------------------------------------------------+
   | BndMHeaderFile           | Description    | Users can choose the dynamic loading configuration of header files                              |
   |                          +----------------+-------------------------------------------------------------------------------------------------+
   |                          | PB Supported   | false                                                                                           |
   |                          +----------------+-------------------------------------------------------------------------------------------------+
   |                          | Multiplicity   | 1                                                                                               |
   |                          +----------------+-------------------------------------------------------------------------------------------------+
   |                          | Type           | String                                                                                          |
   |                          +----------------+-------------------------------------------------------------------------------------------------+
   |                          | Value Range    | N/A                                                                                             |
   |                          +----------------+-------------------------------------------------------------------------------------------------+
   |                          | Default Value  | N/A                                                                                             |
   |                          +----------------+-------------------------------------------------------------------------------------------------+
   |                          | Dependency     | N/A                                                                                             |
   +--------------------------+----------------+-------------------------------------------------------------------------------------------------+

BndM模块的常规回调配置(Regular callback configuration for the BndM module)
---------------------------------------------------------------------------

.. figure:: /_static/参考手册(Module_Reference_Manual)/BndM/BndMCallbackGeneral.PNG
   :name: BndM模块中的常规回调配置项参数描述
   :align: center

   BndM模块中的常规回调配置项参数描述

BndM模块的常规回调配置的参数列表(Parameter list for the regular callback configuration of the BndM module)：

.. table:: BndMCallbackGeneral
   :name: BndMCallbackGeneral
   :align: left

   +-----------------------------+-------------------------------------------------------------------------------+
   | BndMCallbackGeneral         | This container contains the general callbacks.                                |
   +=============================+================+==============================================================+
   | BndMWriteFinalizeFinishFnc  | Description    | Callback function for the WriteFinalizeFinish callback.      |
   |                             +----------------+--------------------------------------------------------------+
   |                             | PB Supported   | false                                                        |
   |                             +----------------+--------------------------------------------------------------+
   |                             | Multiplicity   | 1                                                            |
   |                             +----------------+--------------------------------------------------------------+
   |                             | Type           | Function                                                     |
   |                             +----------------+--------------------------------------------------------------+
   |                             | Value Range    | N/A                                                          |
   |                             +----------------+--------------------------------------------------------------+
   |                             | Default Value  | N/A                                                          |
   |                             +----------------+--------------------------------------------------------------+
   |                             | Dependency     | N/A                                                          |
   +-----------------------------+----------------+--------------------------------------------------------------+
   | BndMWriteStartFinishFnc     | Description    | Callback function for the WriteStartFinish callback..        |
   |                             +----------------+--------------------------------------------------------------+
   |                             | PB Supported   | false                                                        |
   |                             +----------------+--------------------------------------------------------------+
   |                             | Multiplicity   | 1                                                            |
   |                             +----------------+--------------------------------------------------------------+
   |                             | Type           | Function                                                     |
   |                             +----------------+--------------------------------------------------------------+
   |                             | Value Range    | N/A                                                          |
   |                             +----------------+--------------------------------------------------------------+
   |                             | Default Value  | N/A                                                          |
   |                             +----------------+--------------------------------------------------------------+
   |                             | Dependency     | N/A                                                          |
   +-----------------------------+----------------+--------------------------------------------------------------+

BndM模块的特定块回调配置
--------------------------------------------------

.. figure:: /_static/参考手册(Module_Reference_Manual)/BndM/BndMCallbackBlock.PNG
   :name: BndM模块中的特定块回调配置项参数描述
   :align: center

   BndM模块中的特定块回调配置项参数描述

BndM模块的特定块回调配置的参数列表(Parameter list for specific block callback configuration of the BndM module)：

.. table:: BndMCallbackBlock
   :name: BndMCallbackBlock
   :align: left

   +-------------------------+-------------------------------------------------------------------------------+
   | BndMCallbackBlock       | This container contains the block-specific callbacks.                         |
   +=========================+================+==============================================================+
   | BndMWriteBlockFinishFnc | Description    | Callback function for the WriteBlockFinish callback.         |
   |                         +----------------+--------------------------------------------------------------+
   |                         | PB Supported   | false                                                        |
   |                         +----------------+--------------------------------------------------------------+
   |                         | Multiplicity   | 1                                                            |
   |                         +----------------+--------------------------------------------------------------+
   |                         | Type           | Function                                                     |
   |                         +----------------+--------------------------------------------------------------+
   |                         | Value Range    | N/A                                                          |
   |                         +----------------+--------------------------------------------------------------+
   |                         | Default Value  | N/A                                                          |
   |                         +----------------+--------------------------------------------------------------+
   |                         | Dependency     | N/A                                                          |
   +-------------------------+----------------+--------------------------------------------------------------+

BndM模块的特定块参数列表描述配置(Description and configuration of specific block parameters for the BndM module)
------------------------------------------------------------------------------------------------------------------

.. figure:: /_static/参考手册(Module_Reference_Manual)/BndM/BndMBlockDescriptor.PNG
   :name: BndM模块中的特定块参数列表描述配置项参数描述
   :align: center

   BndM模块中的特定块参数列表描述配置项参数描述

BndM模块的特定块参数列表描述配置的参数列表(The list of specific block parameters of the BndM module describes the configured parameters)：

.. table:: BndMBlockDescriptor
   :name: BndMBlockDescriptor
   :align: left

   +-----------------------+-------------------------------------------------------------------------------+
   | BndMBlockDescriptor   | Each container defines a Bulk NV Block which can be individually accessed.    |
   +=======================+================+==============================================================+
   | BndMBlockIdentifier   | Description    | Unique identification of the block.                          |
   |                       +----------------+--------------------------------------------------------------+
   |                       | PB Supported   | false                                                        |
   |                       +----------------+--------------------------------------------------------------+
   |                       | Multiplicity   | 1                                                            |
   |                       +----------------+--------------------------------------------------------------+
   |                       | Type           | Integer                                                      |
   |                       +----------------+--------------------------------------------------------------+
   |                       | Value Range    | 0..65535                                                     |
   |                       +----------------+--------------------------------------------------------------+
   |                       | Default Value  | N/A                                                          |
   |                       +----------------+--------------------------------------------------------------+
   |                       | Dependency     | N/A                                                          |
   +-----------------------+----------------+--------------------------------------------------------------+
   | BndMBlockDescriptor   | Description    | This parameter defines the data structure of the block.      |
   |                       +----------------+--------------------------------------------------------------+
   |                       | PB Supported   | false                                                        |
   |                       +----------------+--------------------------------------------------------------+
   |                       | Multiplicity   | 1                                                            |
   |                       +----------------+--------------------------------------------------------------+
   |                       | Type           | Foreign reference to IMPLEMENTATION-DATA-TYPE                |
   |                       +----------------+--------------------------------------------------------------+
   |                       | Value Range    | N/A                                                          |
   |                       +----------------+--------------------------------------------------------------+
   |                       | Default Value  | N/A                                                          |
   |                       +----------------+--------------------------------------------------------------+
   |                       | Dependency     | N/A                                                          |
   +-----------------------+----------------+--------------------------------------------------------------+
   | BndMCallbackRef       | Description    | Reference to the block-specific callback function.           |
   |                       +----------------+--------------------------------------------------------------+
   |                       | PB Supported   | false                                                        |
   |                       +----------------+--------------------------------------------------------------+
   |                       | Multiplicity   | 1                                                            |
   |                       +----------------+--------------------------------------------------------------+
   |                       | Type           | Reference to BndMCallbackBlock                               |
   |                       +----------------+--------------------------------------------------------------+
   |                       | Value Range    | N/A                                                          |
   |                       +----------------+--------------------------------------------------------------+
   |                       | Default Value  | N/A                                                          |
   |                       +----------------+--------------------------------------------------------------+
   |                       | Dependency     | N/A                                                          |
   +-----------------------+----------------+--------------------------------------------------------------+
   | BndMMemAccAddressArea | Description    | Reference to the MemAccAddressAreaConfiguration.             |
   |                       +----------------+--------------------------------------------------------------+
   |                       | PB Supported   | false                                                        |
   |                       +----------------+--------------------------------------------------------------+
   |                       | Multiplicity   | 1                                                            |
   |                       +----------------+--------------------------------------------------------------+
   |                       | Type           | Reference                                                    |
   |                       +----------------+--------------------------------------------------------------+
   |                       | Value Range    | N/A                                                          |
   |                       +----------------+--------------------------------------------------------------+
   |                       | Default Value  | N/A                                                          |
   |                       +----------------+--------------------------------------------------------------+
   |                       | Dependency     | N/A                                                          |
   +-----------------------+----------------+--------------------------------------------------------------+