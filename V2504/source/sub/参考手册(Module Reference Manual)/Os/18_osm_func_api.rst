OSM Functions
~~~~~~~~~~~~~~~

OSM模块为用户提供了一些监控系统性能的接口，例如，监控CPU、Task和ISR的负载率，调度次数监控等功能。

The OSM module provides users with several interfaces for monitoring system performance, such as CPU, Task, and ISR load ratios, scheduling count monitoring, and other features.

GetLoadRatioValue
*******************************

.. code::

    uint32 GetLoadRatioValue(ObjectType objectId, LoadRatioCalcType calcType)

GetLoadRatioValue is used to calculate the load ratio of CPU, Task, and ISR.

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - objectId
     - Object ID
   * - [in]
     - calcType
     - Method of calculating load ratio

**Return type**
   uint32

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - loadRatioValue
     - Object's load ratio value


GetTaskScheduleCount
*******************************

.. code::

    void GetTaskScheduleCount(TaskType taskId, uint32* taskCnt)

GetTaskScheduleCount is used to obtain the number of task schedulings.

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant

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
     - taskCnt
     - Pointer for storing the number of task schedulings

**Return type**
   void

**Return values**
   None


GetIsr2ScheduleCount
*******************************

.. code::

    void GetIsr2ScheduleCount(ISRType isrId, uint32* isrCnt)

GetIsr2ScheduleCount is used to obtain the number of ISR2 schedulings.

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - isrId
     - ISR2 reference
   * - [in]
     - isrCnt
     - Pointer for storing the number of ISR2 schedulings

**Return type**
   void

**Return values**
   None


EventResponseTimeHook
*******************************

.. code::

    void EventResponseTimeHook(TaskType taskId, EventMaskType eventMask,  TickType respTime)

EventResponseTimeHook provides a hook function to users for event response time failures.

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - taskId
     - Task reference
   * - [in]
     - eventMask
     - Event mask
   * - [in]
     - respTime
     - Response time

**Return type**
   void

**Return values**
   None


EventResponseRateHook
*******************************

.. code::

    void EventResponseRateHook(Os_TaskType taskId, Os_EventMaskType eventMask, uint16 respNum)

EventResponseRateHook provides a hook function to users for event response rate failures.

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - taskId
     - Task reference
   * - [in]
     - eventMask
     - Event mask
   * - [in]
     - respNum
     - Response number

**Return type**
   void

**Return values**
   None
