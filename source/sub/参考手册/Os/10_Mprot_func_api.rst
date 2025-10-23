Memory Protection Functions
--------------------------------------

内存保护策略是基于可执行程序的（数据，代码和堆栈）段。

The memory protection strategy is based on the (data, code, and stack) segments of the executable program.

堆栈：OS-Application包含许多任务和中断。根据定义，这些对象的堆栈仅属于所有者，因此即使这些对象属于同一OS-Application，对象之间也不应共享堆栈数据。

Stack: An OS-Application contains many tasks and interrupts. By definition, the stacks of these objects belong only to their owners, so stack data should not be shared between objects even if they belong to the same OS-Application.

任务和中断堆栈的内存保护非常有用，主要有两个原因：

Memory protection for task and interrupt stacks is very useful for two main reasons:

   - 与堆栈监视相比，可以更直接地检测任务或中断的堆栈上溢和下溢

     Compared with stack monitoring, it can more directly detect stack overflows and underflows of tasks or interrupts.

   - 在OS-Application的组成部分之间提供保护，例如满足一些安全约束

     It provides protection between components of an OS-Application, such as meeting some security constraints.

数据：OS-Application具有私有数据段，而任务/中断具有私有数据段。OS-Application的所有任务/中断共享OS-Application的私有数据段。

Data: An OS-Application has a private data segment, and tasks/interrupts have their own private data segments. All tasks/interrupts of an OS-Application share the private data segment of the OS-Application.

代码：代码段是OS-Application专用的，也可以在所有OS-Applications之间共享（以使用共享库）。在不使用代码保护的情况下，执行不正确的代码最终将导致内存，时序或服务冲突。

Code: Code segments are dedicated to an OS-Application, and can also be shared among all OS-Applications (for using shared libraries). Without code protection, executing incorrect code will eventually lead to memory, timing, or service conflicts.


CheckISRMemoryAccess
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    AccessType CheckISRMemoryAccess(ISRType ISRID, MemoryStartAddressType Address, MemorySizeType Size)

This service checks if a memory region is write/read/execute accessible and also returns information if the memory region is part of the stack space.

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - ISRID
     - Interrupt Identifier
   * - [in]
     - Address
     - Memory area start address
   * - [in]
     - Size
     - Memory area size

**Return type**
    AccessType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - NO_PERMISSION
     - Permission denied
   * - OSMEMORY_IS_READABLE(Access)
     - Non-zero means read permission
   * - OSMEMORY_IS_WRITEABLE(Access)
     - Non-zero means write permission
   * - OSMEMORY_IS_EXECUTABLE(Access)
     - Non-zero means execute permission
   * - OSMEMORY_IS_STACKSPACE(Access)
     - Non-zero means stack space

.. note::

   - 在SC3，SC4下有效

     Valid under SC3 and SC4

   - 请在可信OS-Application的任务或中断中调用该服务

     Please call this service in a task or interrupt of a trusted OS-Application


CheckTaskMemoryAccess
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    AccessType CheckTaskMemoryAccess(TaskType TaskID, MemoryStartAddressType Address, MemorySizeType Size)

This service checks if a memory region is write/read/execute accessible and also returns information if the memory region is part of the stack space.

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - TaskID
     - Task Identifier
   * - [in]
     - Address
     - Memory area start address
   * - [in]
     - Size
     - Memory area size

**Return type**
    AccessType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - NO_PERMISSION
     - Permission denied
   * - OSMEMORY_IS_READABLE(Access)
     - Non-zero means read permission
   * - OSMEMORY_IS_WRITEABLE(Access)
     - Non-zero means write permission
   * - OSMEMORY_IS_EXECUTABLE(Access)
     - Non-zero means execute permission
   * - OSMEMORY_IS_STACKSPACE(Access)
     - Non-zero means stack space

**Example**

.. code::

    App0: Trusted
    TaskInit: Priority:1, Preemptive Policy:FULL, Autostart:True
    App1: No Trusted
    Task0: Priority:2, Preemptive Policy:FULL
      ERAY_INT0: Priority:101, Category: CATEGORY_2

    #define OS_START_SEC_CORE0_APP0_PRI_DATA
    #include “Os_Mp_MemMap.h”
    uint8 app0Data;
    #define OS_STOP_SEC_CORE0_APP0_PRI_DATA
    #include “Os_Mp_MemMap.h”

    #define OS_START_SEC_CORE0_APP1_PRI_DATA
    #include “Os_Mp_MemMap.h”
    uint8 app1Data;
    #define OS_STOP_SEC_CORE0_APP1_PRI_DATA
    #include “Os_Mp_MemMap.h”

    TASK(TaskInit)
    {
      AccessType access;

        access = CheckTaskMemoryAccess(Task0, &app1Data, 1);
      /* access = 3 ( 0011 )  4:execult | 2:write | 1:read  */
      access = CheckISRMemoryAccess(CFG_ISR_ERAY_INT0_ID, &app1Data, 1);
      /* access = 3 ( 0011 )*/

      access = CheckTaskMemoryAccess(Task0, &app0Data, 1);
      /* access = 0*/
      access = CheckISRMemoryAccess(CFG_ISR_ERAY_INT0_ID, &app0Data, 1);
      /* access = 0*/
    }

.. note::

   - 在SC3，SC4下有效

     Valid under SC3 and SC4

   - 请在可信OS-Application的任务或中断中调用该服务

     Please call this service in a task or interrupt of a trusted OS-Application