Alarm(Functions)
--------------------------------------

Os提供用于处理重复事件的服务，例如在Alarm到期时激活任务，设置事件或调用AlarmCallBack回调函数。Alarm回调函数是应用程序提供的简短函数。

The OS provides services for handling recurring events, such as activating tasks upon alarm expiration, setting events, or invoking the AlarmCallback function. The alarm callback is a short function supplied by the application.

.. figure:: ../../../_static/参考手册/Os/alarm分层模型.png
   :alt: Alarm的分层模型 Alarm Layered Model
   :align: center

   管理Alarm的分层模型 (Hierarchical Model for Alarm Management)

Counter和Alarm是静态定义的。Counter到Alarm的分配以及Alarm到期时要执行的具体操作也是静态定义的。

Counters and alarms are statically defined. The assignment of counters to alarms and the specific actions to be executed upon alarm expiration are also statically defined.

动态参数是Alarm到期时的计数器值，以及周期性Alarm的周期时间。

Dynamic parameters include the counter value at alarm expiration and the cycle time for periodic alarms.

GetAlarmBase
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    StatusType GetAlarmBase(AlarmType AlarmID, AlarmBaseRefType Info)

The system service GetAlarmBase reads the alarm base characteristics. The return value <Info> is a structure in which the information of data type

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
     - AlarmID
     - Alarm Identifier
   * - [out]
     - Info
     - Information pointing to AlarmID alarms

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
     - Invalid AlarmID
   * - E_OS_CALLEVEL
     - Wrong calling environment
   * - E_OS_DISABLEDINT
     - Unable to call system services because of interrupt disable/suspend
   * - E_OS_ACCESS
     - No access to this object
   * - E_OS_CORE
     - The remote core is not running
   * - E_OS_ILLEGAL_ADDRESS
     - Parameter address access illegal, or rpcData is NULL_PTR.
   * - E_BUSY
     - The free node can’t be gotten from free queue.
   * - E_OS_TIMEOUT
     - Waiting the execution result timeout.

**Example**

.. code::

    TaskInit: Priority:1, Preemptive Policy:FULL, Autostart:True
    Counter_0: MaxTick:1000, MinTick:1, SecondsPerTick:0.001
    Alarm_0: Counter: Counter_0

    typedef struct
    {
        Os_TickType             maxallowedvalue;
        Os_TickType             ticksperbase;
        Os_TickType             mincycle;
    } Os_AlarmBaseType;

    TASK(TaskInit)
    {
      AlarmBaseType alarmbase;
      GetAlarmBase(Alarm_0,&alarmbase); 
      /* alarmbase. maxallowedvalue = MaxTick */
      /* alarmbase. mincycle = MinTick */
      /* alarmbase. ticksperbase = SecondsPerTick */
      ......
    }


GetAlarm
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    StatusType GetAlarm(AlarmType AlarmID, TickRefType Tick)

The system service GetAlarm returns the relative value in ticks before the alarm <AlarmID> expires.

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
     - AlarmID
     - Alarm Identifier
   * - [in]
     - Tick
     - Relative number of ticks before the alarm is triggered

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
   * - E_OS_NOFUNC
     - alarm is not used
   * - E_OS_ID
     - invalid AlarmID
   * - E_OS_CALLEVEL
     - Wrong calling environment
   * - E_OS_DISABLEDINT
     - Unable to call system services because of interrupt disable/suspend
   * - E_OS_ACCESS
     - No access to this object
   * - E_OS_CORE
     - The remote core is not running
   * - E_OS_ILLEGAL_ADDRESS
     - Parameter address access illegal, or rpcData is NULL_PTR.
   * - E_BUSY
     - The free node can’t be gotten from free queue.
   * - E_OS_TIMEOUT
     - Waiting the execution result timeout.

**Example**

.. code::

    TaskInit: Priority:1, Preemptive Policy:FULL, Autostart:True
    Counter_0: CounterType: SOFTWARE, SecondsPerTick:0.001, 
    MaxTick:1000, MinTick:1
    Alarm_0: Counter: Counter_0

    TASK(TaskInit)
    {
      TickType tick;
      /* alarm is not acitve. */
      ret = GetAlarm(Alarm_0,&tick); /*ret = E_OS_NOFUNC */
      SetRelAlarm(Alarm_0,100,0);
    /* alarm is acitve. */
    IncrementCounter(Counter_0); /* Execute [n] times */
    ret = GetAlarm(Alarm_0,&tick); /*ret = E_OK, tick = [n]*/
      ......
    }

.. note::

   - 如果<AlarmID>没有定义，则<Tick>指向的内容不会改变。
    
     If <AlarmID> is not defined, the content pointed to by <Tick> remains unchanged.


SetRelAlarm
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    StatusType SetRelAlarm(AlarmType AlarmID, TickType increment, TickType cycle)

The system service occupies the alarm <AlarmID> element. After <increment> ticks have elapsed, the task assigned to the alarm <AlarmID> is activated or the assigned event (only for extended tasks) is set or the alarm-callback routine is called.

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
     - AlarmID
     - Alarm Identifier
   * - [in]
     - increment
     - the number of clocks triggered for the first time relative to the current number of clocks
   * - [in]
     - cycle
     - The period of the alarm (Tick number), the cycle value of a single alarm is 0

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
   * - E_OS_STATE
     - Alarm corresponding to AlarmID is in use
   * - E_OS_ID
     - Invalid AlarmID
   * - E_OS_CALLEVEL
     - Wrong calling environment
   * - E_OS_DISABLEDINT
     - Unable to call system services because of interrupt disable/suspend
   * - E_OS_ACCESS
     - No access to this object
   * - E_OS_CORE
     - The remote core is not running
   * - E_OS_VALUE
     - Increment value is not within the normal range (less than 0 or greater than maxallowedvalue) or Cycle value is not equal to 0 and is not within the allowed count range (less than mincycle or greater than maxallowedvalue)
   * - E_OS_ILLEGAL_ADDRESS
     - rpcData is NULL_PTR.
   * - E_BUSY
     - The free node can’t be gotten from free queue.
   * - E_OS_TIMEOUT
     - Waiting the execution result timeout.

.. note::

   - 预设时间到期，将根据配置情况触发相关服务，例如：激活任务，设置事件，回调等。

     When the preset time expires, relevant services are triggered based on the configuration, such as task activation, event setting, and callback execution.

   - 如果相对时间为零，将立即触发相关服务。

     If the relative time is zero, the relevant services are triggered immediately.


SetAbsAlarm
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    StatusType SetAbsAlarm(AlarmType AlarmID, TickType start, TickType cycle)

The system service occupies the alarm <AlarmID> element. When <start> ticks are reached, the task assigned to the alarm <AlarmID> is activated or the assigned event (only for extended tasks) is set or the alarm-callback routine is called.

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
     - AlarmID
     - Alarm Identifier
   * - [in]
     - start
     - Number of absolute clocks triggered for the first time
   * - [in]
     - cycle
     - The period of the alarm (Tick number), the cycle value of a single alarm is 0

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
   * - E_OS_STATE
     - Alarm is active
   * - E_OS_ID
     - invalid AlarmID
   * - E_OS_VALUE
     - Increment value is not within the normal range (less than 0 or greater than maxallowedvalue) or Cycle value is not equal to 0 and is not within the allowed count range (less than mincycle or greater than maxallowedvalue)
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

    TaskInit: Priority:1, Preemptive Policy:FULL, Autostart:True
    Task0: Priority:2, Preemptive Policy:FULL
    Counter_0: MaxTick:1000, MinTick:1, CounterType: SOFTWARE
    Alarm_0: Counter: Counter_0 ActivateTask:Task0

    TASK(TaskInit)
    {
      IncrementCounter(Counter_0);/*1*/
      SetAbsAlarm(Alarm_0,2,0);
      IncrementCounter(Counter_0);/*2*/
      ......
    }

    TASK(TaskInit)
    {
      /* step 2*/
    }

.. note::

   - 预设时间到期，将根据配置情况触发相关服务，例如：激活任务，设置事件，回调等。

     When the preset time expires, relevant services are triggered according to the configuration, such as task activation, event setting, and callback execution.

   - 如果绝对时间等于或接近当前时间，将立即触发相关服务。

     If the absolute time equals or is close to the current time, the relevant services are triggered immediately.

   - 如果绝对时间已过，相关服务将在下次到达时触发。

     If the absolute time has passed, the relevant services are triggered upon the next occurrence.


CancelAlarm
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    StatusType CancelAlarm(AlarmType AlarmID)

The system service cancels the alarm <AlarmID>.

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
     - AlarmID
     - Alarm Identifier

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
   * - E_OS_NOFUNC
     - Alarm is not used
   * - E_OS_ID
     - invalid AlarmID
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

    TaskInit: Priority:1, Preemptive Policy:FULL, Autostart:True
    Counter_0: CounterType: SOFTWARE
    Alarm_0: Counter: Counter_0

    TASK(TaskInit)
    {
      StatusType ret;
      TickType tick;
      /* alarm is not acitve. */
      ret = GetAlarm(Alarm_0,&tick); /*ret = E_OS_NOFUNC */
      ret = SetRelAlarm(Alarm_0,100,0); /*ret = E_OK*/
      /* alarm is acitve. */
    ret = GetAlarm(Alarm_0,&tick); /*ret = E_OK*/
      ret = CancelAlarm(Alarm_0); /*ret = E_OK*/
      /* alarm is not acitve. */
      ret = GetAlarm(Alarm_0,&tick); /*ret = E_OS_NOFUNC */
      ......
    }



