Task(Functions)
---------------------

ORIENTAIS OS提供两种类型的任务:

ORIENTAIS OS provides two types of tasks:

- 基本任务 Basic Task

- 拓展任务 Extended Task

拓展任务与基本任务的区别是，拓展任务允许使用系统服务WaitEvent，这可能会使任务进入Waiting状态。

The difference between an Extended Task and a Basic Task is that the Extended Task is allowed to use the system service WaitEvent, which may cause the task to enter the Waiting state.

.. figure:: ../../../_static/参考手册/Os/Basic_Task_State_Model.png
   :alt: Basic Task State Model
   :align: center

   基本任务状态模型 (Basic Task State Model)


.. list-table::
   :widths: 15 15 15 60
   :header-rows: 1

   * - 过度(Transition)
     - 历史状态(Previous State)
     - 新状态(New State)
     - 描述(Description)
   
   * - **activate**
     - suspended 
     - ready 
     - 系统服务将新任务设置为就绪状态。ORIENTAIS OS确保任务的执行将从第一条指令开始。(The system service sets the new task to the Ready state. ORIENTAIS OS ensures that the task execution starts from the first instruction.)

   * - **start**
     - ready  
     - running  
     - 执行调度器选择的就绪任务。 (Execute the ready task selected by the scheduler.)

   * - **preempt**
     - running 
     - ready 
     - 调度程序尝试启动另一个任务。正在运行的任务变为就绪状态。(通常是在低优先级任务的运行过程中，激活或者释放更高优先级任务) (The scheduler attempts to start another task. The currently running task transitions to the Ready state. (Typically, this occurs when a higher-priority task is activated or released during the execution of a lower-priority task.))

   * - **terminate**
     - running  
     - suspended  
     - 正在运行的任务通过系统服务使其转变为挂起状态。(The running task transitions to the Suspended state via a system service.)

.. figure:: ../../../_static/参考手册/Os/Extend_Task_State_Model.png
   :alt: Extend Task State Model
   :align: center

   拓展任务状态模型(Extended Task State Model)

.. list-table::
   :widths: 15 15 15 60
   :header-rows: 1

   * - 过度(Transition)
     - 历史状态(Previous State)
     - 新状态(New State)
     - 描述(Description)
   
   * - **activate**
     - suspended 
     - ready 
     - 系统服务将新任务设置为就绪状态。ORIENTAIS OS确保任务的执行将从第一条指令开始。 (The system service sets the new task to the Ready state. ORIENTAIS OS ensures that the task execution starts from the first instruction.)

   * - **start**
     - ready  
     - running  
     - 执行调度器选择的就绪任务。 (Execute the ready task selected by the scheduler.)

   * - **wait**
     - running 
     - waiting 
     - 过渡到等待状态是由系统服务引起的(例如：WaitEvent)。为了任务能够继续运行，需要为该任务设置一个它所等待的事件。(The transition to the Waiting state is triggered by a system service (e.g., WaitEvent). For the task to resume running, an event that the task is waiting for must be set for it.)

   * - **release**
     - waiting  
     - ready  
     - 设置至少一个任务等待的事件。(Set at least one event that the task waits for.)

   * - **preempt**
     - running 
     - ready 
     - 调度程序尝试启动另一个任务。正在运行的任务变为就绪状态。(通常是在低优先级任务的运行过程中，激活或者释放更高优先级任务)(The scheduler attempts to start another task. The currently running task transitions to the Ready state. (Typically, this happens when a higher-priority task is activated or released during the execution of a lower-priority task.))

   * - **terminate**
     - running  
     - suspended  
     - 正在运行的任务通过系统服务使其转变为挂起状态。(The running task transitions to the Suspended state through a system service.)


ActivateTask
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    StatusType ActivateTask(TaskType TaskID)

The task<TaskID> is transferred from the suspended state into the ready state.

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
     - Task reference.

**Return type**
   StatusType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - No Error.
   * - E_OS_LIMIT
     - The number of activations has exceeded the limit.
   * - E_OS_ID
     - Invalid TaskID.
   * - E_OS_CALLEVEL
     - Wrong calling environment.
   * - E_OS_DISABLEDINT
     - Unable to call system services because of interrupt disable/suspend.
   * - E_OS_ACCESS
     - Application state error/ No access to this object.
   * - E_OS_CORE
     - The remote core is not running.
   * - E_OS_ILLEGAL_ADDRESS
     - Parameter address access illegal, or rpcData is NULL_PTR.
   * - E_BUSY
     - The free node can’t be gotten from free queue.
   * - E_OS_TIMEOUT
     - waiting the execution result timeout.

**Example**

.. code::

    Example.1
    TaskInit: Priority:1, Preemptive Policy:FULL, Autostart:True

    TASK(TaskInit)
    {
        StatusType ret;
    ret = ActivateTask(Task0);
    /* If the priority of Task0 is greater than TaskInit's, the ActivateTask is don't return directly, and Task0 start to execute. If not, ActivateTask return ‘E_OK’ and program execution continues*/
    ......
    }

    Example.2
    TaskInit: Priority:1, Preemptive Policy:FULL, Autostart:True
    Task0: Priority:1, Preemptive Policy:FULL, Activation Limit:1

    TASK(TaskInit)
    {
        StatusType ret;
    ret = ActivateTask(Task0);
    /* ret = E_OK*/
    ret = ActivateTask(Task0);
    /* ret = E_OS_LIMIT */
    ......
    }

.. note::

   - 如果有多个激活请求，ActivateTask不会立即更改任务状态。如果任务不为挂起状态，任务的激活次数将被记录，并在之后执行激活。

     If there are multiple activation requests, ActivateTask does not change the task state immediately. If the task is not in the Suspended state, the number of activations for the task is recorded and the activation is performed later.

   - ActivateTask激活一个与运行中的任务拥有相同内部资源的任务，该任务不会直接执行。

     ActivateTask activates a task that shares the same internal resources as the currently running task; this task will not be executed directly.

   - 激活任务后，激活计数将增加。如果激活计数超过配置的计数值，那么本次ActivateTask的调用无效。

     After activating a task, the activation count increases. If the activation count exceeds the configured limit, the current call to ActivateTask is invalid.


TerminateTask
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    StatusType TerminateTask(void)

This service causes the termination of the calling task. The calling task is transferred from the running state into the suspended state.

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant


**Return type**
   StatusType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - this
     - function does not return in correct case
   * - E_OS_RESOURCE
     - Resources are still occupied by tasks
   * - E_OS_SPINLOCK
     - Spinlock are still occupied by tasks
   * - E_OS_CALLEVEL
     - Wrong calling environment
   * - E_OS_DISABLEDINT
     - Unable to call system services because of interrupt disable/suspend

**Example**

.. code::

    OsResource: Type:INTERNAL
    TaskInit: Priority:1, Preemptive Policy:FULL, Resource:OsResource, Autostart:True
    Task0: Priority:2, Preemptive Policy:FULL
    Task1: Priority:3, Preemptive Policy:FULL, Resource:OsResource

    TASK(TaskInit)
    {
      /*user code*/
      ActivateTask(Task1); 
    /* TaskInit and Task1 own same internal resource OsResource, therefore Task1 don’t preempt TaskInit. */
      ChainTask(Task0); 
    /*Task0 is activated. ChainTask release TaskInit’s internal resource, therefore Task1 executes firstly due to the highest priority, then Task0 executes. */
      ......
    }

.. note::

   - 严格禁止在未调用TerminateTask或ChainTask的情况下结束任务功能(请勿使用“ return”)，并且可能会使系统处于不确定状态。

     It is strictly prohibited to terminate a task function without calling TerminateTask or ChainTask (do not use "return"), as this may leave the system in an undefined state.

   - 任务必须释放占用的标准资源后才能使用该服务。

     A task must release the standard resources it occupies before using this service.


ChainTask
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    StatusType ChainTask(TaskType TaskID)

This service causes the termination of the calling task. After termination of the calling task a succeeding task <TaskID> is activated.

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
     - Task reference

**Return type**
   StatusType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - this
     - function does not return in correct case
   * - E_OS_LIMIT
     - The number of activations has exceeded the limit
   * - E_OS_ID
     - Invalid TaskID
   * - E_OS_RESOURCE
     - Resources are still occupied by tasks
   * - E_OS_SPINLOCK
     - Spinlock are still occupied by tasks
   * - E_OS_CALLEVEL
     - Wrong calling environment
   * - E_OS_DISABLEDINT
     - Unable to call system services because of interrupt disable/suspend
   * - E_OS_ACCESS
     - Application state error/ No access to this object
   * - E_OS_CORE
     - The remote core is not running
   * - E_OS_ILLEGAL_ADDRESS
     - Parameter address access illegal, or rpcData is NULL_PTR.
   * - E_BUSY
     - The free node can’t be gotten from free queue.
   * - E_OS_TIMEOUT
     - waiting the execution result timeout.

**Example**

.. code::

    OsResource: Type:INTERNAL
    TaskInit: Priority:1, Preemptive Policy:FULL, Resource:OsResource, Autostart:True
    Task0: Priority:2, Preemptive Policy:FULL
    Task1: Priority:3, Preemptive Policy:FULL, Resource:OsResource

    TASK(TaskInit)
    {
      /*user code*/
      ActivateTask(Task1); 
    /* TaskInit and Task1 own same internal resource OsResource, therefore Task1 don’t preempt TaskInit. */
      ChainTask(Task0); 
    /*Task0 is activated. ChainTask release TaskInit’s internal resource, therefore Task1 executes firstly due to the highest priority, then Task0 executes. */
      ......
    }

.. note::

   - 如果后续任务与当前任务相同，则不会导致多个请求。任务不会转移到挂起状态，但是会立即再次准备就绪。

     If the subsequent task is the same as the current task, it will not result in multiple requests. The task will not transition to the Suspended state but will immediately become ready again.

   - 即使后续任务与当前任务相同，分配给调用任务的内部资源也会自动释放。 

     Even if the subsequent task is the same as the current task, the internal resources allocated to the calling task are automatically released.

   - 调用任务所占用的非内部资源应在调用ChainTask之前释放。

     Non-internal resources occupied by the calling task should be released before calling ChainTask.

   - 激活任务后，计数将增加。如果激活计数超过配置的计数，本次ChainTask调用无效。

     After the task is activated, the count increases. If the activation count exceeds the configured limit, the current call to ChainTask is invalid.


Schedule
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    StatusType Schedule(void)

If a higher-priority task is ready , the internal resource of the task is released, the current task is put into the ready state, its context is saved and the highe r-priority task is executed. Otherwise the calling task is continued.

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant


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
   * - E_OS_RESOURCE
     - Resources are still occupied by tasks
   * - E_OS_SPINLOCK
     - Spinlock are still occupied by tasks
   * - E_OS_CALLEVEL
     - Wrong calling environment
   * - E_OS_DISABLEDINT
     - Unable to call system services because of interrupt disable/suspend

**Example**

.. code::

    OsResource: Type:INTERNAL
    TaskInit: Priority:1, Preemptive Policy:FULL, Resource:OsResource, Autostart:True
    Task1: Priority:3, Preemptive Policy:FULL, Resource:OsResource

    TASK(TaskInit)
    {
      /*user code*/
      ActivateTask(Task1); 
    /* TaskInit and Task1 own same internal resource OsResource, therefore Task1 don’t preempt TaskInit. */
      Schedule(); 
    /* Schedule release TaskInit’s internal resource, therefore Task1 executes. */
      ......
    }

.. note::

   - 该服务对分配了内部资源的任务有影响。

     This service has an impact on tasks allocated with internal resources.

   - 任务必须释放占用的非内部资源后才能调用。

     The task must release any occupied non-internal resources before calling this service.


GetTaskID
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    StatusType GetTaskID(TaskRefType TaskID)

GetTaskID returns the information about the TaskID of the task which is currently running.

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
     - Task reference

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
   * - E_OS_CALLEVEL
     - Wrong calling environment
   * - E_OS_DISABLEDINT
     - Unable to call system services because of interrupt disable/suspend
   * - E_OS_ILLEGAL_ADDRESS
     - Parameter address access illegal, or rpcData is NULL_PTR.

**Example**

.. code::

    TaskInit: Priority:1, Preemptive Policy:FULL, Autostart:True
    ISR_0: Priority:101, Category:CATEGORY_2

    TASK(TaskInit)
    {
    TaskType taskid;
      StatusType ret;
      ret = GetTaskID(&taskid);
      /* ret = E_OK , taskid = TaskInit */
      /* trigger interrupt ISR_0*/
      ......
    }

    ISR(ISR_0)
    {
      TaskType taskid;
      StatusType ret;
      ret = GetTaskID(&taskid);
      /* ret = E_OK , taskid = TaskInit */
    }

.. note::

   - 当没有任务在运行时，“ TaskID”的值为INVALID_TASK。

     When no task is running, the value of "TaskID" is INVALID_TASK.


GetTaskState
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    StatusType GetTaskState(TaskType TaskID, TaskStateRefType State)

Returns the state of a task (running, ready, waiting, suspended)at the time of calling GetTaskState.

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
     - Task reference
   * - [out]
     - State
     - Status of the task

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
     - Invalid TaskID
   * - E_OS_CALLEVEL
     - Wrong calling environment
   * - E_OS_DISABLEDINT
     - Unable to call system services because of interrupt disable/suspend
   * - E_OS_ACCESS
     - Application state error/ No access to this object
   * - E_OS_CORE
     - The remote core is not running
   * - E_OS_ILLEGAL_ADDRESS
     - Parameter address access illegal, or rpcData is NULL_PTR.
   * - E_BUSY
     - The free node can’t be gotten from free queue.
   * - E_OS_TIMEOUT
     - waiting the execution result timeout.

**Example**

.. code::

    TaskInit: Priority:1, Preemptive Policy:FULL, Autostart:True
    Task0: Priority:2, Preemptive Policy:FULL,
    Task1: Priority:3, Preemptive Policy:FULL, 
    Task2: Priority:4, Preemptive Policy:FULL, Event: Event_0
    TASK(TaskInit)
    {
      ActivateTask(Task0); /* step 1*/
      ......
    }
    TASK(Task0)
    {
      TaskStateType taskstate;
      ActivateTask(Task2); /* step 2*/
      /* step4*/
      ret = GetTaskState(TaskInit,&taskstate);/*taskstate = TASK_STATE_READY*/
    ret = GetTaskState(Task0,&taskstate); /*taskstate = TASK_STATE_RUNNING*/
    ret = GetTaskState(Task1,&taskstate);/*taskstate = TASK_STATE_SUSPENDED*/
    ret = GetTaskState(Task2,&taskstate); /*taskstate = TASK_STATE_WAITING*/
      ......
    }
    TASK(Task2)
    {
      WaitEvent(Event_0); /* step 3*/
      ......
    }

.. note::

   - 在完全抢占式系统中从任务进行调用时，返回时结果可能已经不正确。 

     When called from a task in a fully preemptive system, the result might already be incorrect by the time of return.

   - 如果为某个任务(多次激活)调用服务，则如果该任务的任何实例正在运行，则状态将设置为“正在运行”。

     If the service is called for a task (with multiple activations), and if any instance of that task is currently running, the state will be set to "running".


ActivateTaskAsyn
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    StatusType ActivateTaskAsyn(TaskType TaskID)

Asynchronous version of the

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
     - Task reference

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
   * - E_OS_LIMIT
     - The number of activations has exceeded the limit
   * - E_OS_ID
     - Invalid TaskID
   * - E_OS_CALLEVEL
     - Wrong calling environment
   * - E_OS_DISABLEDINT
     - Unable to call system services because of interrupt disable/suspend
   * - E_OS_ACCESS
     - Application state error/ No access to this object
   * - E_OS_CORE
     - The remote core is not running
   * - E_OS_ILLEGAL_ADDRESS
     - Parameter address access illegal, or rpcData is NULL_PTR.
   * - E_BUSY
     - The free node can’t be gotten from free queue.
   * - E_OS_TIMEOUT
     - waiting the execution result timeout.

**Example**

.. code::

    C0_TaskInit(Core0): Priority:1, Preemptive Policy:FULL, Autostart:True
    C1_Task0(Core0): Priority:1, Preemptive Policy:FULL

    TASK(C0_TaskInit)
    {
        StatusType ret;
    ret = ActivateTaskAsyn (C1_Task0);
    ......
    }

.. note::

   - 如果待激活的任务与当前任务不在同一个核，ActivateTaskAsyn()采用异步的方式激活该任务。

     If the task to be activated is not on the same core as the current task, ActivateTaskAsyn() activates the task asynchronously.
