Spinlock(Functions)
--------------------------------------

在多核中，需要一种新的机制来支持不同核上任务的互斥。这种新机制不适用于同核上的任务，且将返回错误。

In multi-core systems, a new mechanism is required to support mutual exclusion among tasks on different cores. This new mechanism is not applicable to tasks on the same core and returns an error.

"SpinlockType"是类似于"ResourceType"，且离线配置的自旋锁。

"SpinlockType" is a spinlock similar to "ResourceType" and is configured offline.

自旋锁是一种繁忙的等待机制，它轮询某个自旋锁变量(Spinlock Variable)直到可用。

A spinlock is a busy-waiting mechanism that polls a spinlock variable until it becomes available.

一旦自旋锁被任务或2类中断占用，其他内核上的任务或2类中断将无法占用这个自旋锁。自旋锁机制不会在轮询锁定变量时对其他任务进行调度。

Once a spinlock is acquired by a task or a Category 2 interrupt, tasks or Category 2 interrupts on other cores cannot acquire this spinlock. The spinlock mechanism does not schedule other tasks while polling the lock variable.


GetSpinlock
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    StatusType GetSpinlock(SpinlockIdType SpinlockId)

GetSpinlock tries to occupy a spin-lock variable. If the function returns, either the lock is successfully taken or an error has occurred.

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
     - SpinlockId
     - The spin lock number user want to get

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
   * - E_OS_ID: 
     - Invalid ID
   * - E_OS_CALLEVEL
     - Wrong calling environment
   * - E_OS_DISABLEDINT
     - Unable to call system services because of interrupt disable/suspend
   * - E_OS_ACCESS
     - No access to this object
   * - E_OS_INTERFERENCE_DEADLOCK
     - Conflict deadlock, lock is already occupied by task
   * - E_OS_NESTING_DEADLOCK
     - Nested deadlock, another task on the same core is occupying another spinlock

**Example**

.. code::

    Spinlock_0:LockMethod:LOCK_NOTHING
    AccessingApplication: App0,App1
    App0:  Core: 0
    TaskInit: Priority:1, Preemptive Policy:FULL, Autostart:True
    App1:  Core:1
    Task0: Priority:2, Preemptive Policy:FULL
        AccessingApplication:App0

    TASK(TaskInit)  /* core 0*/
    {
      GetSpinlock(Spinlock_0);
      ActivateTask(Task0);
      /*user code*/
      ReleaseSpinlock(Spinlock_0);
      ......
    } 

    TASK(Task0)  /* core 1*/
    {
      GetSpinlock(Spinlock_0);
      /*Waiting releasing spinlock on core0*/
      /*user code*/
    ReleaseSpinlock(Spinlock_0);
      ......
    }

.. note::

   - 自旋锁机制是一种主动轮询机制。该功能不会引起调度问题。

     The spinlock mechanism is an active polling mechanism. This functionality does not cause scheduling issues.


ReleaseSpinlock
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    StatusType ReleaseSpinlock(SpinlockIdType SpinlockId)

ReleaseSpinlock is the counterpart of GetSpinlock. ReleaseSpinlock releases a spinlock variable that was occupied before.

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
     - SpinlockId
     - The spin lock number user want to release

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
     - Invalid ID
   * - E_OS_CALLEVEL
     - Wrong calling environment
   * - E_OS_DISABLEDINT
     - Unable to call system services because of interrupt disable/suspend
   * - E_OS_ACCESS
     - No access to this object
   * - E_OS_STATE
     - Spinlock is not occupied by a task
   * - E_OS_NOFUNC
     - The spin locks are released in the wrong order

.. note::

   - 在终止任务之前，必须释放通过GetSpinlock占用的所有自旋锁变量。在调用WaitEvent之前，应释放所有自旋锁。

     All spinlock variables acquired via GetSpinlock must be released before terminating a task. All spinlocks should be released before calling WaitEvent.

   - 如果ReleaseSpinlock尝试释放未获得的自旋锁，则会发生错误。

     An error occurs if ReleaseSpinlock attempts to release a spinlock that has not been acquired.


TryToGetSpinlock
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    StatusType TryToGetSpinlock(SpinlockIdType SpinlockId, TryToGetSpinlockType *Success)

Try to acquire a spinlock.

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
     - SpinlockId
     - The spin lock number user want to get
   * - [out]
     - Success
     - Returns whether the specified spin lock is occupied

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
     - Invalid ID
   * - E_OS_CALLEVEL
     - Wrong calling environment
   * - E_OS_DISABLEDINT
     - Unable to call system services because of interrupt disable/suspend
   * - E_OS_ILLEGAL_ADDRESS
     - Parameter address access illegal
   * - E_OS_ACCESS
     - No access to this object
   * - E_OS_INTERFERENCE_DEADLOCK
     - Conflict deadlock, lock is already occupied by task
   * - E_OS_NESTING_DEADLOCK
     - Nested deadlock, another task on the same core is occupying another spinlock
   * - E_OS_ACCESS
     - No access to this spin lock

**Example**

.. code::

    Spinlock_0:LockMethod:LOCK_NOTHING
    AccessingApplication: App0,App1
    App0:  Core: 0
    TaskInit: Priority:1, Preemptive Policy:FULL, Autostart:True
    App1:  Core: 1
    Task0: Priority:2, Preemptive Policy:FULL
        AccessingApplication:App0

    TASK(TaskInit)  /* core 0*/
    {
      GetSpinlock(Spinlock_0);
      ActivateTask(Task0);
      /*user code*/
      ReleaseSpinlock(Spinlock_0);
      ......
    } 
    TASK(Task0)  /* core 1*/
    {
      TryToGetSpinlock (Spinlock_0);
      /* TryToGetSpinlock return error directly, if the Spinlock_0 is not released on core0*/
      ......
    }

.. note::

   - TryToGetSpinlock具有与GetSpinlock相同的功能，不同之处在于，如果自旋锁已被另一个内核上的任务占用，则该函数将设置输出参数"Success"并返回E_OK。

     TryToGetSpinlock provides the same functionality as GetSpinlock, except that if the spinlock is already held by a task on another core, this function sets the output parameter "Success" and returns E_OK.




