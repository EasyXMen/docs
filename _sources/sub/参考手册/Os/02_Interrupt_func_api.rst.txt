Interrupt Functions
--------------------------------------

处理中断的函数（中断服务程序：ISR）分为两类中断：

Functions that handle interrupts (Interrupt Service Routines: ISRs) are divided into two types of interrupts:

 - 1类中断: 此类中断不使用操作系统服务。中断结束后，程序将在发生中断位置继续执行，即中断对任务管理没有影响。此类别的中断具有最小的开销。

   Type 1 Interrupts: This type of interrupt does not use operating system services. After the interrupt ends, the program will continue execution from the location where the interrupt occurred, meaning the interrupt has no impact on task management. Interrupts of this type have minimal overhead.

 - 2类中断: Os提供一个中断框架，为特定的用户程序提供运行环境。这类中断能够使用Os的系统服务。

   Type 2 Interrupts: The Os provides an interrupt framework that offers a runtime environment for specific user programs. This type of interrupt can use the system services of the Os.


.. figure:: ../../../_static/参考手册/Os/ISR类别.png
   :alt: ORIENTAIS OS的ISR类别
   :align: center

   ORIENTAIS OS的ISR类别（ISR Types of ORIENTAIS OS）


EnableAllInterrupts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void EnableAllInterrupts(void)

This service restores the state saved by DisableAllInterrupts.

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant


**Return type**
   void

**Example**

.. code::

    TaskInit: Priority:1, Preemptive Policy:FULL, Autostart:True

    TASK(TaskInit)
    {
      DisableAllInterrupts();
      /*user action except system service*/
      EnableAllInterrupts();
      ......
    }

.. note::

    - 该服务与DisableAllInterrupts服务相对应，后者必须在之前被调用，其目的是保障代码临界区的完整性。

      This service corresponds to the DisableAllInterrupts service, which must have been called beforehand to ensure the integrity of the code critical section.


DisableAllInterrupts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void DisableAllInterrupts(void)

This service disables all interrupts for which the hardware supports disabling. The state before is saved for the EnableAllInterrupts call.

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant


**Return type**
   void

.. note::

    - 主要用于某些不能使用ORIENTAIS OS API的临界段。

      It is mainly used for certain critical sections where the ORIENTAIS OS API cannot be used.


ResumeAllInterrupts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void ResumeAllInterrupts(void)

This service restores t he recognition status of all interrupts saved by the SuspendAllInterrupts service.

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant


**Return type**
   void

**Example**

.. code::

    TaskInit: Priority:1, Preemptive Policy:FULL, Autostart:True

    void function_0()
    {
    SuspendAllInterrupts();
      /*user action except system service*/
      ResumeAllInterrupts();
    }

    TASK(TaskInit)
    {
      SuspendAllInterrupts();
      /*user action except system service*/
      ResumeAllInterrupts();

    SuspendAllInterrupts();
      /*user action except system service*/
      function_0(); /*nested using*/
      ResumeAllInterrupts();
      ......
    }

.. note::

    - SuspendAllInterrupts / ResumeAllInterrupts可以嵌套使用。如果嵌套调用SuspendAllInterrupts和ResumeAllInterrupts，SuspendAllInterrupts第一次调用时保存的中断识别状态将在ResumeAllInterrupts最后一次调用时恢复。

      SuspendAllInterrupts / ResumeAllInterrupts can be used in a nested way. If SuspendAllInterrupts and ResumeAllInterrupts are called nestedly, the interrupt identification state saved during the first call of SuspendAllInterrupts will be restored during the last call of ResumeAllInterrupts.

SuspendAllInterrupts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void SuspendAllInterrupts(void)

This service saves the re cognition status of all interrupts and disables all interrupts for which the hardware supports.

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant


**Return type**
   void

.. note::

    - 主要用于某些不能使用ORIENTAIS OS API的临界段。

      It is mainly used for certain critical sections where the ORIENTAIS OS API cannot be used.


ResumeOSInterrupts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void ResumeOSInterrupts(void)

This service restores the recognition status of interrupts saved by the SuspendOSInterrupts service.

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant


**Return type**
   void

.. note::

    - SuspendOSInterrupts / ResumeOSInterrupts可以嵌套使用。如果嵌套调用SuspendOSInterrupts和ResumeOSInterrupts，SuspendOSInterrupts的第一次调用时保存的中断识别状态将在ResumeAllInterrupts最后一次调用时恢复。
    
      SuspendOSInterrupts / ResumeOSInterrupts can be used in a nested manner. If SuspendOSInterrupts and ResumeOSInterrupts are called nestedly, the interrupt identification state saved when SuspendOSInterrupts is first called will be restored when ResumeAllInterrupts is called for the last time.
    
    - SuspendOSInterrupts / ResumeOSInterrupts仅对2类中断有影响。

      SuspendOSInterrupts / ResumeOSInterrupts only affect Type 2 Interrupts.

SuspendOSInterrupts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void SuspendOSInterrupts(void)

This service saves the recognition status of interrupts of category 2 and disables the recognition of these interrupts.

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant


**Return type**
   void

.. note:: 

    - 主要用于某些不能使用ORIENTAIS OS API的临界段。

      It is mainly used for certain critical sections where the ORIENTAIS OS API cannot be used.

GetISRID
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    ISRType GetISRID(void)

This service returns the identifier of the currently executing ISR.

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant


**Return type**
    ISRType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - Returns
     - the ID of CATEGORY_2 interrupt
   * - INVALID_ISR
     - 

**Example**

.. code::

    App0: Trusted
    TaskInit: Priority:1, Preemptive Policy:FULL, Autostart:True
      ERAY_INT0: Priority:101, Category: CATEGORY_2

    TASK(TaskInit)
    {
      ISRType isr;

      /* OS_REG32(OS_SRC_ERAY_INT0_ADDR)) |= 0x04000000*/
      TriggerInterrupt(OS_SRC_ERAY_INT0_ADDR);

    ISRType isr;
      isr = GetISRID();
      /* isr = OS_ISR_INVALID */
    }

    ISR(ERAY_INT0)
    {
      ISRType isr;
      isr = GetISRID();
      /* isr = CFG_ISR_ERAY_INT0_ID */
    }


EnableInterruptSource
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    StatusType EnableInterruptSource(ISRType ISRID, boolean ClearPending)

Enables the interrupt source by modifying the interrupt controller registers. Additionally it may clear the interrupt pending flag.

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
     - ISRID
     - The ID of a category 2 ISR.
   * - [in]
     - ClearPending
     - Whether to clear the interrupt pending flag.

**Return type**
   StatusType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - No error
   * - E_OS_NOFUNC
     - EnableInterruptSource is called for an interrupt source which is already enabled.
   * - E_OS_ID
     - ISRID is not a valid category 2 ISR identifier.
   * - E_OS_CALLEVEL
     - Wrong call context of the API function
   * - E_OS_ACCESS
     - The calling application is not the owner of the ISR passed in ISRID

**Example**

.. code::

    TaskInit: Priority:1, Preemptive Policy:FULL, Autostart:True

    TASK(TaskInit)
    {
      ……
      StatusType ret;
      ret = DisableInterruptSource(CFG_ISR_DMA_SF_DMA0_CH_10_ID);
      ……
      ret = EnableInterruptSource(CFG_ISR_DMA_SF_DMA0_CH_10_ID, TRUE);
      ……
    }

.. note::

    - 该服务为了短时间屏蔽特定的中断或在特定时间内忽略特定源的中断请求。

      This service is used to mask specific interrupts for a short period of time or ignore interrupt requests from specific sources within a specific time frame.


DisableInterruptSource
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    StatusType DisableInterruptSource(ISRType ISRID)

Disables the interrupt source by modifying the interrupt controller registers.

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
     - ISRID
     - The ID of a category 2 ISR.

**Return type**
   StatusType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - No error
   * - E_OS_NOFUNC
     - DisableInterruptSource is called for an interrupt source which is already disabled.
   * - E_OS_ID
     - ISRID is not a valid category 2 ISR identifier.
   * - E_OS_CALLEVEL
     - Wrong call context of the API function
   * - E_OS_ACCESS
     - The calling application is not the owner of the ISR passed in ISRID


ClearPendingInterrupt
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    StatusType ClearPendingInterrupt(ISRType ISRID)

Clears the interrupt pending flag by modifying the interrupt controller registers.

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
     - ISRID
     - The ID of a category 2 ISR.

**Return type**
   StatusType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - No error
   * - E_OS_ID
     - ISRID is not a valid category 2 ISR identifier.
   * - E_OS_CALLEVEL
     - Wrong call context of the API function
   * - E_OS_ACCESS
     - The calling application is not the owner of the ISR passed in ISRID

**Example**

.. code::

    TaskInit: Priority:1, Preemptive Policy:FULL, Autostart:True

        TASK(TaskInit)
        {
          ……
          StatusType ret;
          ret = DisableInterruptSource(CFG_ISR_DMA_SF_DMA0_CH_10_ID);
          ……
          ret = ClearPendingInterrupt(CFG_ISR_DMA_SF_DMA0_CH_10_ID);
          ……
        }

.. note::

    - 该服务为了短时间屏蔽特定的中断或在特定时间内忽略特定源的中断请求。

      This service is used to mask specific interrupts for a short period of time or ignore interrupt requests from specific sources within a given time frame.




