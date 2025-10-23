Counter Functions
--------------------------------------

一个计数器由一个以“滴答”为单位表示的计数器值和一些计数器特定的常数。 Os提供标准化的API，以直接操作计数器。
Os提供了两种不同的计数器：

A counter consists of a counter value represented in "tick" units and some counter-specific constants. The Os provides standardized APIs to directly manipulate counters.
The Os offers two distinct types of counters:

 - 硬件Counter（Hardware Counter）
 - 软件Counter（Software Counter）

**硬件Counter:** 由硬件（例如定时器）增加计数器的计数值。计数值由外围设备“在硬件中”维护。

**Hardware Counter**: The counter value is incremented by hardware (e.g., a timer). The counter value is maintained "in hardware" by peripheral devices.

**软件Counter:** 通过调用IncrementCounter增加计数器的计数值。计数值由ORIENTAIS OS “在软件中”维护。

**Software Counter**: The counter value is incremented by calling IncrementCounter. The counter value is maintained "in software" by ORIENTAIS OS.

IncrementCounter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    StatusType IncrementCounter(CounterType CounterID)

This service increments a software counter.

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
     - CounterID
     - Counter Identifier

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
     - CounterID is invalid or the counter implemented by hardware cannot be incremented by software
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

    Alarm_10ms: ActivateTask: Task_10ms, CycleTime:10ms, Autostart:True
    Task_10ms: Priority:1, Preemptive Policy:FULL
    Counter_0: CounterType:SOFTWARE
    TASK(Task_10ms)
    {
      IncrementCounter(Counter_0); /*The current tick value of Counter_0 increases 1*/
    }

.. note::

   - 该函数不能增加硬件计数器的计数值。

     This function cannot increment the count value of a hardware counter.


GetCounterValue
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    StatusType GetCounterValue(CounterType CounterID, TickRefType Value)

This service reads the current count value of a counter .

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
     - CounterID
     - Counter Identifier
   * - [out]
     - Value
     - Counter's current clock value

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
     - CounterID is invalid
   * - E_OS_ILLEGAL_ADDRESS
     - Parameter address access illegal, or rpcData is NULL_PTR.
   * - E_OS_CALLEVEL
     - Wrong calling environment
   * - E_OS_DISABLEDINT
     - Unable to call system services because of interrupt disable/suspend
   * - E_OS_ACCESS
     - No access to this object
   * - E_OS_CORE
     - The remote core is not running
   * - E_OS_VALUE
     - Parameter address is invalid
   * - E_BUSY
     - The free node can’t be gotten from free queue.
   * - E_OS_TIMEOUT
     - waiting the execution result timeout.

**Example**

.. code::

    Alarm_10ms: ActivateTask: Task_10ms, CycleTime:10ms, Autostart:True
    Task_10ms: Priority:1, Preemptive Policy:FULL
    Counter_0: CounterType:SOFTWARE
    Counter_1: CounterType:HARDWARE

    TASK(Task_10ms)
    {
      TickType tick;
      IncrementCounter(Counter_0);
    /*The software counter need to increse by calling IncrementCounter.*/
      GetCounterValue(Counter_0,&tick); /*The current tick value of Counter_0*/
      GetCounterValue(Counter_1,&tick); /*The current tick value of Counter_1*/
    }

.. note::

   - 如果计数器是由硬件驱动的，则返回硬件计数器的计数值；如果计数器是由软件驱动的，则返回软件计数器的计数值。

     If the counter is driven by hardware, it returns the count value of the hardware counter; if the counter is driven by software, it returns the count value of the software counter.


GetElapsedValue
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    StatusType GetElapsedValue(CounterType CounterID, TickRefType Value, TickRefType ElapsedValue)

This service gets the number of ticks between the current tick value and a previously read tick value.

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
     - CounterID
     - Counter Identifier
   * - [out]
     - Value
     - The current value of the counter (used as the next starting value)
   * - [out]
     - ElapsedValue
     - Interval between current clock value and start value

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
     - CounterID is invalid
   * - E_OS_CALLEVEL
     - Wrong calling environment
   * - E_OS_ILLEGAL_ADDRESS
     - Parameter address access illegal, or rpcData is NULL_PTR.
   * - E_OS_DISABLEDINT
     - Unable to call system services because of interrupt disable/suspend
   * - E_OS_ACCESS
     - No access to this object
   * - E_OS_CORE
     - The remote core is not running
   * - E_OS_VALUE
     - Parameter address is invalid
   * - E_BUSY
     - The free node can’t be gotten from free queue.
   * - E_OS_TIMEOUT
     - waiting the execution result timeout.

**Example**

.. code::

    TaskInit: Priority:1, Preemptive Policy:FULL, Autostart:True
    Counter_0: CounterType:SOFTWARE, MaxTick:1000,MinTick:1

    TASK(TaskInit)
    {
      TickType tick0,tick1,tick2;
      IncrementCounter(Counter_0);  /* the count of calling IncrementCounter is n.*/
      tick0 = 5;
    GetElapsedValue(Counter_0,&tick0,&tick1);
    GetCounterValue(Counter_0,&tick2);
    /* tick1 = ((n + 1000) – tick0(5)) % 1000 = n - 5, tick0 = tick2 = 10*/
      ...... 
    }


