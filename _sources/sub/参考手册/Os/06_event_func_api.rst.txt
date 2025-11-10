Event(Functions)
--------------------------------------

事件机制(Event Mechanism)：

 - 是一种同步手段
   
   It is a synchronization mechanism.

 - 仅拓展任务可用

   Only extended tasks can use events.

Figure解释了在完全抢占式调度的情况下通过设置事件使扩展任务的同步，其中扩展任务T1具有更高的优先级。

The figure illustrates the synchronization of extended tasks through event setting under fully preemptive scheduling, where extended task T1 has a higher priority.

.. figure:: ../../../_static/参考手册/Os/event同步任务.png
   :alt: 可抢占扩展任务的同步 (Synchronization of Preemptible Extended Tasks)
   :align: center

   可抢占扩展任务的同步 (Synchronization of Preemptible Extended Tasks)


SetEvent
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    StatusType SetEvent(TaskType TaskID, EventMaskType Mask)

The events of task <TaskID> are set according to the event mask <Mask>. Calling SetEvent causes the task <TaskID> to be transferred to the ready state, if it was waiting for at least one of the events specified in <Mask>.

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
   * - [in]
     - Mask
     - Event mask, the configured event name

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
     - Task is not an extended task / No access to this object
   * - E_OS_STATE
     - event cannot be set when the task is suspended
   * - E_OS_CORE
     - The remote core is not running
   * - E_OS_ILLEGAL_ADDRESS
     - Parameter address access illegal, or rpcData is NULL_PTR.
   * - E_BUSY
     - The free node can’t be gotten from free queue.
   * - E_OS_TIMEOUT
     - waiting the execution result timeout.

.. note::

   - 事件的状态以'位'为单位，事件中未设置的位保持不变。

     The state of an event is measured in bits, and unset bits within the event remain unchanged.

   - 任务可以自行设置事件。

     A task can set events autonomously.

   - 在ECC1，ECC2下有效。

     Valid under ECC1 and ECC2.


ClearEvent
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    StatusType ClearEvent(EventMaskType Mask)

The events of the extended task calling ClearEvent are cleared according to the event mask <Mask>.

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
     - Mask
     - Event mask, the configured event name

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
     - Task is not an extended task

.. note::

   - 仅拓展任务可用。

     Only extended tasks can use this feature.

   - 在ECC1，ECC2下有效。

     This is valid under ECC1 and ECC2.


GetEvent
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    StatusType GetEvent(TaskType TaskID, EventMaskRefType Event)

This service returns the current state of all event bits of the task <TaskID>, not the events that the task is waiting for.

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
   * - 
     - Event
     - 

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
     - Task is not an extended task
   * - E_OS_STATE
     - task is suspended
   * - E_OS_CORE
     - The remote core is not running
   * - E_OS_ILLEGAL_ADDRESS
     - Parameter address access illegal, or rpcData is NULL_PTR.

.. note::

   - 用户可以获取当前正在运行的任务的事件。

     Users can retrieve the events of the currently running task.

   - 在ECC1，ECC2下有效。

     This operation is valid under ECC1 and ECC2.


WaitEvent
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    StatusType WaitEvent(EventMaskType Mask)

The state of the calling task is set to waiting, unless at least one of the events specified in <Mask> has already been set.

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
     - Mask
     - Event mask, the configured event name

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
   * - E_OS_CALLEVEL
     - Wrong calling environment
   * - E_OS_DISABLEDINT
     - Unable to call system services because of interrupt disable/suspend
   * - E_OS_ACCESS
     - Task is not an extended task
   * - E_OS_RESOURCE
     - Resources are still occupied by tasks
   * - E_OS_SPINLOCK
     - Spinlock are still occupied by tasks

**Example**

.. code::

    TaskInit: Priority:1, Preemptive Policy:FULL, Autostart:True
    Task0: Priority:2, Preemptive Policy:FULL, Event:Event_0

    TASK(TaskInit)
    {
      ActivateTask(Task0); /* step 1*/
      SetEvent(Task0,Event_0);/* step 3: Task state from waiting to running*/
      ......
    }

    TASK(Task0)
    {
      EventMaskType eventmask;
      GetEvent(Task0, &eventmask);/* eventmask & Event_0 = 0 */
      WaitEvent(Event_0); /* step 2: Task state from running to waiting*/

    GetEvent(Task0, &eventmask);/* eventmask & Event_0 = Event_0 */
      WaitEvent(Event_0); /* step 4: Task continues execute because the bit of event don’t be cleared. */

    GetEvent(Task0, &eventmask);/* eventmask & Event_0 = Event_0 */
      ClearEvent(Event_0); /* step 5*/
      GetEvent(Task0, &eventmask);/* eventmask & Event_0 = 0 */
      ......
    }

.. note::

   - 在ECC1，ECC2下有效。

     This service is valid under ECC1 and ECC2.

   - 仅拓展任务可用。

     Only extended tasks can use this service.

   - 如果等待的事件未被设置，则当前任务进入等待状态并进行任务切换。如果等待的事件已被设置，则继续执行当前任务。

     If the waited event is not set, the current task enters the waiting state and a task switch occurs. If the waited event is already set, the current task continues execution.

   - 调用前必须释放占据的资源。

     Occupied resources must be released before invocation.

   - 设置的事件不会被主动清除。用户必须调用ClearEvent来清除事件。

     Set events are not automatically cleared. Users must call ClearEvent to clear events.


WaitAllEvents
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    StatusType WaitAllEvents(EventMaskType Mask)

The state of the calling task is set to waiting, must all the events specified in <Mask> has already been set.

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
     - Mask
     - Event mask, the configured event name

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
   * - E_OS_CALLEVEL
     - Wrong calling environment
   * - E_OS_DISABLEDINT
     - Unable to call system services because of interrupt disable/suspend
   * - E_OS_ACCESS
     - Task is not an extended task
   * - E_OS_RESOURCE
     - Resources are still occupied by tasks
   * - E_OS_SPINLOCK
     - Spinlock are still occupied by tasks

**Example**

.. code::

    TaskInit: Priority:1, Preemptive Policy:FULL, Autostart:True
    Task0: Priority:2, Preemptive Policy:FULL, Event:Event_0

    TASK(TaskInit)
    {
      ActivateTask(Task0); /* step 1*/
      SetEvent(Task0,Event_0 | Event_1);/* step 3: Task state from waiting to running*/
      ......
    }

    TASK(Task0)
    {
      EventMaskType eventmask;
      GetEvent(Task0, &eventmask);/* eventmask & Event_0 = 0 */
      WaitAllEvents(Event_0 | Event_1); /* step 2: Task state from running to waiting*/

    GetEvent(Task0, &eventmask);/* eventmask & Event_0 = Event_0 */
      WaitEvent(Event_0); /* step 4: Task continues execute because the bit of event don’t be cleared. */

    GetEvent(Task0, &eventmask);/* eventmask & Event_0 = Event_0 */
      ClearEvent(Event_0 | Event_1); /* step 5*/
      GetEvent(Task0, &eventmask);/* eventmask & Event_0 = 0 */
      ......
    }


SetEventAsyn
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    StatusType SetEventAsyn(TaskType TaskID, EventMaskType Mask)

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
   * - [in]
     - Mask
     - Event mask, the configured event name

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
     - Task is not an extended task / No access to this object
   * - E_OS_STATE
     - event cannot be set when the task is suspended
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
    Task0: Priority:2, Preemptive Policy:FULL, Event:Event_0

    TASK(TaskInit)
    {
      ActivateTask(Task0); /* step 1*/
      SetEventAsyn(Task0,Event_0 | Event_1);/* step 3: Task state from waiting to running*/
      ......
    }

    TASK(Task0)
    {
      EventMaskType eventmask;
      GetEvent(Task0, &eventmask);/* eventmask & Event_0 = 0 */
      WaitAllEvents(Event_0 | Event_1); /* step 2: Task state from running to waiting*/

    GetEvent(Task0, &eventmask);/* eventmask & Event_0 = Event_0 */
      WaitEvent(Event_0); /* step 4: Task continues execute because the bit of event don’t be cleared. */

    GetEvent(Task0, &eventmask);/* eventmask & Event_0 = Event_0 */
      ClearEvent(Event_0 | Event_1); /* step 5*/
      GetEvent(Task0, &eventmask);/* eventmask & Event_0 = 0 */
      ......
    }


