Barrier Functions
~~~~~~~~~~~~~~~~~

Barrier模块为用户提供多核环境下的任务同步，确保多个核心的任务在指定屏障点（Barrier）处等待。

The Barrier module provides users with task synchronization in a multi-core environment, ensuring that tasks across multiple cores wait at specified barrier points.

Os_BarrierSynchronize
*******************************

.. code::

    StatusType Os_BarrierSynchronize(Os_BarrierIdType BarrierID)

Os_BarrierSynchronize is used for task synchronization in a multi-core environment.

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
     - BarrierID
     - Barrier ID

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
     - Invalid BarrierID
   * - E_OS_CALLEVEL
     - Wrong calling environment
   * - E_OS_SYS_NO_BARRIER_PARTICIPANT
     - Task is not configured to participate in barriers
   * - E_OS_DEADLOCK
     - Detected deadlock

