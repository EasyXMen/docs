ScheduleTable Functions
--------------------------------------

调度表类似于使用Counter和一系列自动启动的Alarms来实现静态定义的任务激活机制。

A schedule table is similar to a statically defined task activation mechanism implemented using a Counter and a series of automatically started Alarms.

调度表提供了一组静态定义的溢出点封装。每个溢出点定义：

A schedule table provides a set of statically defined overflow point encapsulations. Each overflow point defines:

   - 处理溢出点时，将执行动作（通过ORIENTAIS配置工具OS模块配置）。动作是任务的激活或事件的设置。

     When processing the overflow point, an action (configured via the OS module of the ORIENTAIS configuration tool) will be executed. The action is either the activation of a task or the setting of an event.

   - 从调度表的开始处以“滴答”为单位的偏移量。

     An offset in "tick" units from the start of the schedule table.

在运行时，ORIENTAIS OS将遍历调度表，依次处理每个溢出点。调度表由一个计数器驱动。计数器的属性会影响调度表中允许配置的内容。

During runtime, the ORIENTAIS OS traverses the schedule table and processes each overflow point in sequence. The schedule table is driven by a counter, and the properties of the counter affect the configurable content allowed in the schedule table.

用户可以为调度表设置为同步模式。ORIENTAIS OS通过两种方式提供对同步的支持：

Users can set the schedule table to synchronous mode. The ORIENTAIS OS provides support for synchronization in two ways:

- 隐式同步：驱动调度表的计数器要求是同步计数器。这通常是采用时间触发的网络技术（例如FlexRay，TTP）实现同步的方式-底层硬件管理网络时间同步，并简单地将时间显示为ORIENTAIS OS的输出/比较计时器接口。Figure显示了隐式同步调度表可能出现的状态。

  Implicit Synchronization: The counter driving the schedule table is required to be a synchronous counter. This is typically a synchronization method implemented using time-triggered network technologies (e.g., FlexRay, TTP) — the underlying hardware manages network time synchronization and simply presents the time as an output/compare timer interface for the ORIENTAIS OS. Figure 5-7 shows the possible states of a schedule table with implicit synchronization.

.. figure:: ../../../_static/参考手册/Os/隐式同步调度表的状态图.png
   :alt: 隐式同步调度表的状态图
   :align: center

   隐式同步调度表的状态（States of Schedule Table with Implicit Synchronization）

- 显式同步：调度表由ORIENTAIS OS计数器驱动，而不要求是同步的计数器。ORIENTAIS OS还提供一些其他功能，以使其计数器驱动的调度表与同步计数器同步。通常，这是与定期广播全局时间进行同步的方式。Figure显示了显式同步调度表可能出现的状态。

  Explicit Synchronization: The schedule table is driven by an ORIENTAIS OS counter, which is not required to be a synchronous counter. The ORIENTAIS OS also provides additional functions to synchronize its counter-driven schedule table with a synchronous counter. Typically, this is a method of synchronizing with periodically broadcast global time. Figure 5-8 shows the possible states of a schedule table with explicit synchronization.

.. figure:: ../../../_static/参考手册/Os/显式同步调度表的状态图.png
   :alt: 显式同步调度表的状态图
   :align: center

   显式同步调度表的状态（图中未显示所有的跳转条件）

States of Schedule Table with Explicit Synchronization (not all transition conditions are shown in the diagram)

StartScheduleTableRel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    StatusType StartScheduleTableRel(ScheduleTableType ScheduleTableID, TickType Offset)

This service starts the processing of a schedule table at "Offset" relative to the "Now" value on the underlying counter.

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
     - ScheduleTableID
     - ScheduleTable Identifier
   * - [in]
     - Offset
     - The clock value from the current time to the start of the schedule (the tick value of the counter corresponds to the schedule)

**Return type**
   StatusType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - No errors
   * - E_OS_ID
     - ScheduleTableID is invalid
   * - E_OS_VALUE
     - Offset is greater than (OsCounterMaxAllowedValue-InitialOffset) or equal to 0
   * - E_OS_STATE
     - schedule has started
   * - E_OS_CALLEVEL
     - Wrong calling environment
   * - E_OS_DISABLEDINT
     - Unable to call system services because of interrupt disable/suspend
   * - E_OS_ACCESS
     - Application state error / No access to this object
   * - E_OS_CORE
     - The remote core is not running
   * - E_OS_ILLEGAL_ADDRESS
     - rpcData is NULL_PTR.
   * - E_BUSY
     - The free node can’t be gotten from free queue.
   * - E_OS_TIMEOUT
     - Waiting the execution result timeout.

**Example**

.. code::

    Counter_0: MaxTick:1000, MinTick:1, CounterType: SOFTWARE
    TaskInit: Priority:1, Preemptive Policy:FULL, Autostart:True
    OsScheduleTable_0: Counter:Counter_0

    TASK(TaskInit)
    {
      ScheduleTableStatusType ststatus;
    GetScheduleTableStatus(OsScheduleTable_0, &ststatus);
    /* default : ststatus = SCHEDULETABLE_STOPPED */
    StartScheduleTableRel(OsScheduleTable_0, 2);
    /* OsScheduleTable_0 is in queue but not started. */
    /* ststatus = SCHEDULETABLE_STOPPED */
    IncrementCounter(Counter_0);
      GetScheduleTableStatus(OsScheduleTable_0, &ststatus);
    /* ststatus = SCHEDULETABLE_RUNNING */
    ......
    }


StartScheduleTableAbs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    StatusType StartScheduleTableAbs(ScheduleTableType ScheduleTableID, TickType Start)

This service starts the processing of a schedule table at an absolute value "Start" on the underlying counter.

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
     - ScheduleTableID
     - ScheduleTable Identifier
   * - [in]
     - Start
     - The clock value at which the schedule starts processing (the absolute tick value of the counter corresponding to the schedule)

**Return type**
   StatusType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - No errors
   * - E_OS_ID
     - Invalid ScheduleTableID
   * - E_OS_VALUE
     - Start is greater than OsCounterMaxAllowedValue
   * - E_OS_STATE
     - schedule has started
   * - E_OS_CALLEVEL
     - Wrong calling environment
   * - E_OS_DISABLEDINT
     - Unable to call system services because of interrupt disable/suspend
   * - E_OS_ACCESS
     - No access to this object
   * - E_OS_CORE
     - The remote core is not running
   * - E_OS_ILLEGAL_ADDRESS
     - rpcData is NULL_PTR.
   * - E_BUSY
     - The free node can’t be gotten from free queue.
   * - E_OS_TIMEOUT
     - Waiting the execution result timeout.


StopScheduleTable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    StatusType StopScheduleTable(ScheduleTableType ScheduleTableID)

This service cancels the processing of a schedule table immediately at any point while the schedule table is running.

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
     - ScheduleTableID
     - ScheduleTable Identifier

**Return type**
   StatusType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - No errors
   * - E_OS_ID
     - ScheduleTableID is invalid
   * - E_OS_NOFUNC
     - The schedule has stopped
   * - E_OS_CALLEVEL
     - Wrong calling environment
   * - E_OS_DISABLEDINT
     - Unable to call system services because of interrupt disable/suspend
   * - E_OS_ACCESS
     - No access to this object
   * - E_OS_CORE
     - The remote core is not running
   * - E_OS_ILLEGAL_ADDRESS
     - rpcData is NULL_PTR.
   * - E_BUSY
     - The free node can’t be gotten from free queue.
   * - E_OS_TIMEOUT
     - Waiting the execution result timeout.

**Example**

.. code::

    Example.1
    Counter_0: MaxTick:1000, MinTick:1, CounterType: SOFTWARE
    TaskInit: Priority:1, Preemptive Policy:FULL, Autostart:True
    OsScheduleTable_0: Counter:Counter_0

    TASK(TaskInit)
    {
      ScheduleTableStatusType ststatus;
    GetScheduleTableStatus(OsScheduleTable_0, &ststatus);
    /* default : ststatus = SCHEDULETABLE_STOPPED */
    StartScheduleTableRel(OsScheduleTable_0, 1);
    /* OsScheduleTable_0 is in queue but not started. */
    /* ststatus = SCHEDULETABLE_STOPPED */
    IncrementCounter(Counter_0);
      GetScheduleTableStatus(OsScheduleTable_0, &ststatus);
    /* ststatus = SCHEDULETABLE_RUNNING */
    StopScheduleTable(OsScheduleTable_0);
      GetScheduleTableStatus(OsScheduleTable_0, &ststatus);
      /* ststatus = SCHEDULETABLE_STOPPED */
    ......
    }


NextScheduleTable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    StatusType NextScheduleTable(ScheduleTableType ScheduleTableID_From, ScheduleTableType ScheduleTableID_To)

This service switches the processing from one schedule table to another schedule table.

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
     - ScheduleTableID_From
     - Schedules currently being processed
   * - [in]
     - ScheduleTableID_To
     - Next processing schedule with a series of trigger points

**Return type**
   StatusType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - No errors
   * - E_OS_ID
     - ScheduleTableID_From or ScheduleTableID_To is invalid
   * - E_OS_NOFUNC
     - ScheduleTableID_From did not start
   * - E_OS_STATE
     - ScheduleTableID_To has started or is in Next
   * - E_OS_CALLEVEL
     - Wrong calling environment
   * - E_OS_DISABLEDINT
     - Unable to call system services because of interrupt disable/suspend
   * - E_OS_ACCESS
     - No access to this object
   * - E_OS_CORE
     - These two schedule tables do not belong to the same core

**Example**

.. code::

    Counter_0: MaxTick:1000, MinTick:1, CounterType: SOFTWARE
    TaskInit: Priority:1, Preemptive Policy:FULL, Autostart:True
    OsScheduleTable_0: Counter:Counter_0,
    The Final ExpiryPoint: ExpPoint Offset: [n]
    OsScheduleTable_1: Counter:Counter_0

    TASK(TaskInit)
    {
      ScheduleTableStatusType ststatus;
    StartScheduleTableRel(OsScheduleTable_0, 1);
    IncrementCounter(Counter_0);
      GetScheduleTableStatus(OsScheduleTable_0, &ststatus);
    /* ststatus = SCHEDULETABLE_RUNNING */
    NextScheduleTable(OsScheduleTable_0, OsScheduleTable_1);
    GetScheduleTableStatus(OsScheduleTable_1, &ststatus);
    /* ststatus = SCHEDULETABLE_NEXT */
    IncrementCounter(Counter_0); /* Execult [n] times.*/
    GetScheduleTableStatus(OsScheduleTable_0, &ststatus);
    /* ststatus = SCHEDULETABLE_STOPPED */
    GetScheduleTableStatus(OsScheduleTable_1, &ststatus);
    /* ststatus = SCHEDULETABLE_RUNNING */
    ......
    }


StartScheduleTableSynchron
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    StatusType StartScheduleTableSynchron(ScheduleTableType ScheduleTableID)

This service starts an explicitly synchronized schedule table synchronously.

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
     - ScheduleTableID
     - ScheduleTable Identifier

**Return type**
   StatusType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - No errors
   * - E_OS_ID
     - ScheduleTableID is invalid
   * - E_OS_STATE
     - ScheduleTableID has been started
   * - E_OS_CALLEVEL
     - Wrong calling environment
   * - E_OS_DISABLEDINT
     - Unable to call system services because of interrupt disable/suspend
   * - E_OS_ACCESS
     - No access to this object
   * - E_OS_CORE
     - The object is not belong to local core

**Example**

.. code::

    Example.1
    Counter_0: MaxTick:1000, MinTick:1, CounterType: SOFTWARE
    TaskInit: Priority:1, Preemptive Policy:FULL, Autostart:True
    OsScheduleTable_0: Counter:Counter_0, Sync Strategy:EXPLICIT

    TASK(TaskInit)
    {
      ScheduleTableStatusType ststatus;
    GetScheduleTableStatus(OsScheduleTable_0, &ststatus);
    /* default : ststatus = SCHEDULETABLE_STOPPED */
      StartScheduleTableSynchron(OsScheduleTable_0);
    GetScheduleTableStatus(OsScheduleTable_0, &ststatus);
    /* default : ststatus = SCHEDULETABLE_WAITING */
    ......
    }

.. note::

   - 仅在SC3、SC4下有效

     It is only valid under SC3 and SC4.

   - 调度表同步策略必须是显性。

     The schedule table synchronization strategy must be explicit.


SyncScheduleTable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    StatusType SyncScheduleTable(ScheduleTableType ScheduleTableID, TickType value)

This service provides the schedule table with a synchronization count and start synchronization.

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
     - ScheduleTableID
     - ScheduleTable Identifier
   * - 
     - value
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
     - No errors
   * - E_OS_ID
     - ScheduleTableID is invalid or the schedule cannot be synchronized (OsScheduleTblSyncStrategy is not set or OsScheduleTblSynStrategy = IMPLICIT)
   * - E_OS_VALUE
     - Value is out of range
   * - E_OS_STATE
     - The status of ScheduleTableID is SCHEDULETABLE_STOPPED
   * - E_OS_CALLEVEL
     - Wrong calling environment
   * - E_OS_DISABLEDINT
     - Unable to call system services because of interrupt disable/suspend
   * - E_OS_ACCESS
     - No access to this object
   * - E_OS_CORE
     - The object is not belong to local core

**Example**

.. code::

    Counter_0: MaxTick:1000, MinTick:1, CounterType: SOFTWARE
    TaskInit: Priority:1, Preemptive Policy:FULL, Autostart:True
    OsScheduleTable_0: Counter:Counter_0, Sync Strategy:EXPLICIT

    TASK(TaskInit)
    {
      ScheduleTableStatusType ststatus;
    GetScheduleTableStatus(OsScheduleTable_0, &ststatus);
    /* default : ststatus = SCHEDULETABLE_STOPPED */
      StartScheduleTableSynchron(OsScheduleTable_0);
    GetScheduleTableStatus(OsScheduleTable_0, &ststatus);
    /* default : ststatus = SCHEDULETABLE_WAITING */
    SyncScheduleTable(OsScheduleTable_0, 1);
      GetScheduleTableStatus(OsScheduleTable_0, &ststatus);
    /*default : ststatus = SCHEDULETABLE_RUNNING_AND_SYNCHRONOUS*/
    ......
    }

.. note::

   - 仅在SC3、SC4下有效

     It is only valid under SC3 and SC4.

   - 调度表同步策略必须是显性

     The schedule table synchronization strategy must be explicit.


SetScheduleTableAsync
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    StatusType SetScheduleTableAsync(ScheduleTableType ScheduleTableID)

Stop schedule table explicit sync and set state to running.

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
     - ScheduleTableID
     - ScheduleTable Identifier

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
     - Invalid ScheduleTableID
   * - E_OS_STATE
     - The schedule table is not running
   * - E_OS_CORE
     - The object is not belong to local core
   * - E_OS_CALLEVEL
     - Wrong calling environment
   * - E_OS_DISABLEDINT
     - Unable to call system services because of interrupt disable/suspend
   * - E_OS_ACCESS
     - No access to this object

**Example**

.. code::

    Counter_0: MaxTick:1000, MinTick:1, CounterType: SOFTWARE
    TaskInit: Priority:1, Preemptive Policy:FULL, Autostart:True
    OsScheduleTable_0: Counter:Counter_0, Sync Strategy:EXPLICIT

    TASK(TaskInit)
    {
      ScheduleTableStatusType ststatus;
    GetScheduleTableStatus(OsScheduleTable_0, &ststatus);
    /* default : ststatus = SCHEDULETABLE_STOPPED */

      StartScheduleTableSynchron(OsScheduleTable_0);
    GetScheduleTableStatus(OsScheduleTable_0, &ststatus);
    /* default : ststatus = SCHEDULETABLE_WAITING */

    SyncScheduleTable(OsScheduleTable_0, 1);
      GetScheduleTableStatus(OsScheduleTable_0, &ststatus);
    /*default : ststatus = SCHEDULETABLE_RUNNING_AND_SYNCHRONOUS*/

    SetScheduleTableAsync(OsScheduleTable_0);
    GetScheduleTableStatus(OsScheduleTable_0, &ststatus);
    /*default : ststatus = SCHEDULETABLE_RUNNING */
    ......
    }

.. note::

   - 仅在SC3、SC4下有效

     It is only valid under SC3 and SC4.

   - 调度表同步策略必须是显性

     The schedule table synchronization strategy must be explicit.


GetScheduleTableStatus
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    StatusType GetScheduleTableStatus(ScheduleTableType ScheduleTableID, ScheduleTableStatusRefType ScheduleStatus)

Get the status of the specified schedule.

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
     - ScheduleTableID
     - ScheduleTable Identifier
   * - [out]
     - ScheduleStatus
     - Pointer to the status value of the obtained schedule

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
     - Invalid ScheduleTableID
   * - E_OS_CALLEVEL
     - Wrong calling environment
   * - E_OS_DISABLEDINT
     - Unable to call system services because of interrupt disable/suspend
   * - E_OS_ACCESS
     - No access to this object
   * - E_OS_ILLEGAL_ADDRESS
     - Parameter address access illegal, or rpcData is NULL_PTR.
   * - E_OS_CORE
     - The remote core is not running
   * - E_OS_VALUE
     - Parameter address is invalid
   * - E_BUSY
     - The free node can’t be gotten from free queue.
   * - E_OS_TIMEOUT
     - Waiting the execution result timeout.







