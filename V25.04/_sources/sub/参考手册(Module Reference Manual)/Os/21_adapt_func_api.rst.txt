Adapt Functions
~~~~~~~~~~~~~~~

Adapt模块为用户提供了一些兼容接口，例如：中断使能/禁用、错误信息获取、任务当前堆栈使用量查询、未处理中断或异常请求获取等功能接口。

The Adapt module provides users with a set of compatible interfaces, such as: interrupt enabling/disabling, error information retrieval, querying the current task stack usage, obtaining pending interrupt or exception requests, and other functional interfaces.

Os_GetDetailedError
*******************************

.. code::

    StatusType Os_GetDetailedError(Os_ErrorInformationRefType ErrorRef)

Os_GetDetailedError is used to return the last error information that occurred on the local core.

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
   * - [out]
     - ErrorRef
     - A reference to an Os_ErrorInformationType object

**Return type**
   StatusType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Successfully obtained detailed error information
   * - E_OS_SERVICEID
     - Service protection is not enabled
   * - E_OS_ILLEGAL_ADDRESS
     - Parameter pointer is NULL
   * - E_OS_CALLEVEL
     - Wrong calling environment


Os_GetTaskStackUsage
*******************************

.. code::

    uint32 Os_GetTaskStackUsage(TaskType TaskID)

Os_GetTaskStackUsage is used to obtain the current stack usage of a given task.

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

**Return type**
   uint32

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - MaxUsage
     - Current stack usage for a given task


Os_DisableGlobalKM
*******************************

.. code::

    void Os_DisableGlobalKM(void)

Os_DisableGlobalKM is used to disable the recognition of all interrupts. This service performs no nesting checks or service protection checks.

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant

**Parameters**
   None

**Return type**
   void

**Return values**
   None


Os_EnableGlobalKM
*******************************

.. code::

    void Os_EnableGlobalKM(void)

Os_EnableGlobalKM is used to enable the recognition of all interrupts. This service performs no nesting checks or service protection checks.

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant

**Parameters**
   None

**Return type**
   void

**Return values**
   None


Os_DisableLevelKM
*******************************

.. code::

    void Os_DisableLevelKM(void)

Os_DisableLevelKM is used to disable the recognition of ISR2. This service performs no nesting checks or service protection checks.

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant

**Parameters**
   None

**Return type**
   void

**Return values**
   None


Os_EnableLevelKM
*******************************

.. code::

    void Os_EnableLevelKM(void)

Os_EnableLevelKM is used to enable the recognition of ISR2. This service performs no nesting checks or service protection checks.

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant

**Parameters**
   None

**Return type**
   void

**Return values**
   None

Os_IsInterruptSourceEnabled
*******************************

.. code::

    StatusType Os_IsInterruptSourceEnabled(ISRType ISRID, boolean* IsEnabled)

Os_IsInterruptSourceEnabled is used to check whether a given interrupt source is enabled.

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
     - ISRID
     - ISR2 ID
   * - [out]
     - IsEnabled
     - Pointer to whether the interrupt source is enabled

**Return type**
   StatusType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Successfully obtained the interrupt source status
   * - E_OS_ID
     - Invalid ISR2 ID
   * - E_OS_ILLEGAL_ADDRESS
     - Parameter pointer is NULL
   * - E_OS_CALLEVEL
     - Wrong calling environment
   * - E_OS_ACCESS
     - ISRID's OS-Application is not accessible


Os_InitialEnableInterruptSources
***********************************

.. code::

    StatusType Os_InitialEnableInterruptSources(boolean ClearPending)

Os_InitialEnableInterruptSources is used to enable category 2 ISR interrupt sources on the current core.

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
     - ClearPending
     - Define whether to clear the pending flag

**Return type**
   StatusType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Successfully enable the interrupt source
   * - E_OS_VALUE
     - Invalid ISR2 ID
   * - E_OS_NOFUNC
     - ClearPending is neither TRUE nor FALSE
   * - E_OS_CALLEVEL
     - Wrong calling environment
   * - E_OS_ACCESS
     - ISRID's OS-Application is not accessible


Os_GetUnhandledIrq
*******************************

.. code::

    StatusType Os_GetUnhandledIrq (Os_InterruptSourceIdRefType InterruptSource)

Os_GetUnhandledIrq is used to distinguish the source of interrupts when there are pending interrupt requests that have not been handled.

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
   * - [out]
     - InterruptSource
     - Reference to interrupt source ID

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
   * - E_OS_ILLEGAL_ADDRESS
     - Parameter pointer is NULL
   * - E_OS_CALLEVEL
     - Wrong calling environment
   * - E_OS_STATE
     - Unreported unhandled interrupts since autostart


Os_GetUnhandledExc
*******************************

.. code::

    StatusType Os_GetUnhandledExc(Os_ExceptionSourceIdRefType ExceptionSource)

Os_GetUnhandledExc is used to distinguish the source of exceptions when there are pending exception requests that have not been handled.

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
   * - [out]
     - ExceptionSource
     - Reference to exception source ID

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
   * - E_OS_ILLEGAL_ADDRESS
     - Parameter pointer is NULL
   * - E_OS_CALLEVEL
     - Wrong calling environment
   * - E_OS_STATE
     - Unreported unhandled exception since autostart