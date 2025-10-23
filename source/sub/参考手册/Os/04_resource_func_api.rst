Resource Functions
--------------------------------------

资源管理用于协调具有不同优先级的多个任务对共享资源的并发访问，例如：管理的实体（调度器），程序，内存或硬件区域。

Resource management is used to coordinate the concurrent access of multiple tasks with different priorities to shared resources, such as managed entities (schedulers), programs, memory, or hardware regions.

在系统生成时，会为每个资源静态分配其自己的最高优先级。用户可以通过在任务/中断中调用GetResource / ReleaseResource来获取/释放标准资源。运行任务/中断的优先级暂时设置为资源的优先级，直到释放资源为止。

During system generation, each resource is statically assigned its own highest priority. Users can acquire/release standard resources by calling GetResource / ReleaseResource in tasks/interrupts. The priority of the running task/interrupt is temporarily set to the priority of the resource until the resource is released.

.. figure:: ../../../_static/参考手册/Os/资源天花板机制.png
   :alt: 可抢占任务间优先级天花板的资源分配
   :align: center

   可抢占任务间优先级天花板的资源分配（Resource Allocation with Priority Ceiling Among Preemptive Tasks）

内部资源是用户不可见的资源，因此系统功能GetResource和ReleaseResource无法操作内部资源。它们在一组明确定义的系统功能内部严格管理。除此之外，内部资源的行为与标准资源完全相同。

Internal resources are invisible to users; therefore, the system functions GetResource and ReleaseResource cannot operate on internal resources. They are strictly managed within a well-defined set of system functions. Beyond this, the behavior of internal resources is identical to that of standard resources.

占用标准资源时，不得调用TerminateTask，ChainTask，Schedule，WaitEvent。中断服务程序不应在占据资源的情况下结束。

When occupying standard resources, TerminateTask, ChainTask, Schedule, and WaitEvent must not be called. Interrupt Service Routines (ISRs) should not terminate while occupying resources.


GetResource
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    StatusType GetResource(ResourceType ResID)

This call serves to enter critical sections in the code that are assigned to the resource referenced by <ResID>. A critical section shall always be left using ReleaseResource.

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
     - ResID
     - Resource Identifier

**Return type**
   StatusType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - No Error
   * - E_OS_ID
     - Invalid ResID
   * - E_OS_CALLEVEL
     - Wrong calling environment
   * - E_OS_DISABLEDINT
     - Unable to call system services because of interrupt disable/suspend
   * - E_OS_ACCESS
     - Attempt to obtain a resource that has been occupied by a task, interrupt, or statically assigned to a ceiling priority task or an interrupt higher than the ceiling priority

**Example**

.. code::

    Example.1
    OsResource: Type:STANDARD

    TaskInit: Priority:1, Preemptive Policy:FULL, Autostart:True, Resource:OsResource
    Task0: Priority:2, Preemptive Policy:FULL, Resource:OsResource

    TASK(TaskInit)
    {
      GetResource(OsResource);
      /* user code*/
      ReleaseResource(OsResource);/*If a task don’t release resource occupied, it cannot activate other tasks configuring the resource and terminate itself.*/
      ActivateTask(Task0);
      ...... 
    }

    Example.2
    OsResource: Type:STANDARD
    TaskInit: Priority:1, Preemptive Policy:FULL, Autostart:True, Resource:OsResource
    Task0: Priority:2, Preemptive Policy:FULL, Resource:OsResource

    TASK(TaskInit)
    {
      GetResource(OsResource);
      ActivateTask(Task0);
      ReleaseResource(OsResource); /* The ReleaseResource can make OS scheduling. Task0 start to execute immediately.*/
      ...... 
    }

.. note::

   - 同一资源不能嵌套获取。用户可以多次获得不同的资源，并且以后进先出（LIFO）的顺序进行操作。

     The same resource cannot be acquired in a nested manner. Users can acquire different resources multiple times and operate on them in Last-In-First-Out (LIFO) order.

   - 建议对GetResource和ReleaseResource的调用尽可能出现在同一函数中。

     It is recommended that calls to GetResource and ReleaseResource appear in the same function whenever possible.

   - 任务获取资源后，系统不允许为不可抢占任务的发起重调度的服务（例如：TerminateTask，ChainTask，Schedule和WaitEvent）。

     After a task acquires a resource, the system does not allow services that initiate rescheduling for non-preemptive tasks (e.g., TerminateTask, ChainTask, Schedule, and WaitEvent).


ReleaseResource
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    StatusType ReleaseResource(ResourceType ResID)

ReleaseResource is the counterpart of GetResource and serves to leave critical sections in the code that are assigned to the resource referenced by <ResID>.

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
     - ResID
     - Resource Identifier

**Return type**
   StatusType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - No Error
   * - E_OS_ID
     - Invalid ResID
   * - E_OS_NOFUNC
     - Attempt to release unused resources / Task/ISR don’t release resource and spinlock in nest order
   * - E_OS_CALLEVEL
     - Wrong calling environment
   * - E_OS_DISABLEDINT
     - Unable to call system services because of interrupt disable/suspend
   * - E_OS_ACCESS
     - An attempt was made to release a resource with a lower ceiling priority than a task that calls a task or interrupts a static configuration.
   * - E_OS_CORE
     - The object is not belong to local core

.. note::

   - 资源释放者可以与资源获取者不同。

     The resource releaser can be different from the resource acquirer.



