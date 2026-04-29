接口描述(Interface Description)
===================================

类型定义(Type Definitions)
-------------------------------
.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Type Name
     - Type
     - Description

   * - AppModeType
     - Os_AppModeType (uint16)
     - 应用模式类型 (Type definition of the App mode)

   * - ObjectTypeType
     - Os_ObjectTypeType (enum)
     - 对象类型标识 (This data type identifies an object)

   * - CoreIdType
     - Os_CoreIdType (uint16)
     - CoreIdType是一种标量类型，用于唯一标识单个处理器核心。CoreIdType应表示逻辑核心ID (CoreIdType is a scalar that allows identifying a single core. The CoreIdType shall represent the logical CoreID)

   * - ApplicationType
     - Os_ApplicationType (uint16)
     - 操作系统应用标识 (This data type identifies the OS-Application)

   * - ResourceType
     - Os_ResourceType (enum)
     - OS资源类型 (Type definition of OS resources)

   * - TaskStateType
     - Os_TaskStateType (enum)
     - 任务状态类型 (This data type identifies task state)

   * - TaskStateRefType
     - Os_TaskStateType*
     - 任务状态指针类型 (The pointer type definition of the task state)

   * - TaskType
     - Os_TaskType (enum)
     - 任务类型 (Type definition of task)

   * - TaskRefType
     - Os_TaskType*
     - 任务指针类型 (The pointer type definition of the task)

   * - TaskEntry
     - void (*)(void)
     - 任务入口函数指针 (The function pointer definition of the task entry)

   * - TickType
     - Os_TickType (uint32)
     - 时钟节拍类型 (This type of tick)

   * - TickRefType
     - TickType*
     - 时钟节拍指针类型 (The pointer type definition of tick)

   * - CounterType
     - Os_CounterType (enum)
     - 计数器类型 (This data type identifies a counter)

   * - AlarmType
     - Os_AlarmType (enum)
     - 闹钟类型 (This type of alarm)

   * - AlarmBaseType
     - Os_AlarmBaseType (struct)
     - 闹钟基础类型，此类型用于存储计数器特征的结构体 (Alarm base type, this type is used for the structure storing counter characteristics)

   * - AlarmBaseRefType
     - Os_AlarmBaseType*
     - 闹钟基础类型指针 (The pointer type definition of alarm base)

   * - EventMaskType
     - Os_EventMaskType (uint64)
     - 事件掩码类型 (This type of event mask)

   * - EventMaskRefType
     - EventMaskType*
     - 事件掩码指针类型 (The pointer type definition of event mask)

   * - ISRType
     - Os_IsrType (enum)
     - 此数据类型用于标识一个中断服务例程（ISR） (This data type identifies an interrupt service routine (ISR))

   * - ScheduleTableStatusType
     - Os_SchedTblStateType (enum)
     - 此类型描述调度表的状态。 (This type describes the status of a schedule table)

   * - ScheduleTableStatusRefType
     - ScheduleTableStatusType*
     - 调度表状态指针类型 (The pointer type definition of the schedule table)

   * - ScheduleTableType
     - Os_ScheduleTableType (enum)
     - 此数据类型用于标识一个调度表 (This data type identifies a schedule table)

   * - TrustedFunctionIndexType
     - Os_TrustedFunctionIndexType (uint16)
     - 此数据类型用于标识一个可信函数 (This data type identifies a trusted function)

   * - TrustedFunctionParameterRefType
     - void*
     - 此数据类型指向一个结构体，该结构体包含调用可信函数所需的参数 (This data type points to a structure which holds the arguments for a call to a trusted function)

   * - ObjectAccessType
     - enum
     - 此数据类型用于标识一个OS应用对某个对象是否具有访问权限 (This data type identifies if an OS-Application has access to an object)

   * - RestartType
     - Os_RestartType (enum)
     - 此数据类型定义了在终止一个OS应用后使用重启任务的方式 (This data type defines the use of a Restart Task after terminating an OS-Application)

   * - ApplicationStateType
     - Os_ApplicationStateType (enum)
     - 此数据类型用于标识一个OS-Application的状态 (This data type identifies the state of an OS-Application)

   * - ApplicationStateRefType
     - Os_ApplicationStateType*
     - 此数据类型指向可存储ApplicationStateType的位置 (This data type points to location where a ApplicationStateType can be stored)

   * - AppObjectId
     - Os_AppObjectId (uint16)
     - 应用对象ID (The ID of the Application object)

   * - ProtectionReturnType
     - Os_ProtectionReturnType (enum)
     - 此数据类型标识一个值，该值控制在从保护钩子返回后，操作系统进一步要执行的操作 (This data type identifies a value which controls further actions of the OS on return from the protection hook)

   * - AccessType
     - Os_AccessType (uint16)
     - 此类型存储关于特定内存区域访问方式的信息 (This type holds information how a specific memory region can be accessed)

   * - MemoryStartAddressType
     - Os_MemoryStartAddressType (uint32)
     - 此数据类型是一个指针，能够指向微控制器地址空间中的任意位置 (This data type is a pointer which is able to point to any location in the MCU address space)

   * - MemorySizeType
     - Os_MemorySizeType (uint32)
     - 此数据类型存储内存区域的大小（以字节为单位） (This data type holds the size (in bytes) of a memory region)

   * - TryToGetSpinlockType
     - enum
     - TryToGetSpinlockType 用于指示自旋锁是否已被占用 (The TryToGetSpinlockType indicates if the spinlock has been occupied or not)

   * - SpinlockIdType
     - enum
     - SpinlockIdType 用于标识一个自旋锁实例，并由以下API函数使用：GetSpinlock、ReleaseSpinlock 和 TryToGetSpinlock (SpinlockIdType identifies a spinlock instance and is used by the API functions: GetSpinlock, ReleaseSpinlock and TryToGetSpinlock.)

   * - IdleModeType
     - Os_IdleModeType (enum)
     - 此数据类型用于标识空闲模式的行为 (This data type identifies the idle mode behavior)

   * - AreaIdType
     - uint16
     - AreaIdType 用于标识一个外设区域，并由以下API函数使用：ReadPeripheralX、WritePeripheralX 和 ModifyPeripheralX (AreaIdType identifies a peripheral area and is used by the API functions: ReadPeripheralX, Write PeripheralX and ModifyPeripheralX)

   * - Os_BarrierIdType
     - enum
     - 此数据类型用于标识系统中的Barrier对象 (This data type is used to identify a Barrier object within the system)


提供的服务(Services)
-----------------------------------

.. include::  01_task_func_api.rst
.. include::  02_Interrupt_func_api.rst
.. include::  03_counter_func_api.rst
.. include::  04_resource_func_api.rst
.. include::  05_alarm_func_api.rst
.. include::  06_event_func_api.rst
.. include::  07_ScheduleTable_func_api.rst
.. include::  08_hook_func_api.rst
.. include::  09_app_func_api.rst
.. include::  10_Mprot_func_api.rst
.. include::  11_Sprot_func_api.rst
.. include::  12_system_control_func_api.rst
.. include::  13_multi_core_func_api.rst
.. include::  14_spinlock_func_api.rst
.. include::  15_Ioc_func_api.rst
.. include::  16_peripheral_func_api.rst
.. include::  17_extend_func_api.rst
.. include::  18_osm_func_api.rst
.. include::  19_FaultManager_func_api.rst
.. include::  20_barrier_func_api.rst
.. include::  21_adapt_func_api.rst



