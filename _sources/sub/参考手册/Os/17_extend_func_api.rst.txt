Extend Functions
--------------------------------------

Extend模块为用户提供了一些扩展功能：获取系统堆栈、任务堆栈、ISR堆栈使用情况的接口，检查版本信息的接口，获取检查ISR中断源的接口，检查CPU信息的接口。

The Extend module provides users with several extended functions: interfaces for obtaining the usage of system stacks, task stacks, and ISR stacks; interfaces for checking version information; interfaces for obtaining and checking ISR interrupt sources; and interfaces for checking CPU information.


OSGetVersionInfo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void OSGetVersionInfo(Std_VersionInfoType *osVerInfoPtr)

Provide Version information to user.

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
   * - [out]
     - osVerInfoPtr
     - pointer for getting OS version

**Return type**
   void

**Example**

.. code::

    TaskInit: Priority:1, Preemptive Policy:FULL, Autostart:True

    TASK(TaskInit)
    {
    ……
    Std_VersionInfoType * osVerInfoPtr；
    OSGetVersionInfo(osVerInfoPtr);
        ……
    }


OSGetStackUsage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    osStackUsageType OSGetStackUsage(osStackObject stack, uint16 id)

Get max usage of system,task,ISR2 stack.

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
     - stack
     - Stack type
   * - [in]
     - id
     - Object ID

**Return type**
    osStackUsageType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - uint32
     - Max usage of stack

**Example**

.. code::

    TaskInit: Priority:1, Preemptive Policy:FULL, Autostart:True

    TASK(TaskInit)
    {
        ……
    osStackUsageType MaxUsage;
    MaxUsage = OSGetStackUsage(OS_STACK_TASK, TaskInit);
        ……
    }


OSCheckISRSource
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    StatusType OSCheckISRSource(uint32 Source)

OSCheckISRSource is used to check the interrupt source.

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
     - Source
     - Isr source

**Return type**
   StatusType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - TRUE
     - current triggered interrupt.
   * - FALSE
     - not current triggered interrupt.

**Example**

.. code::

    /*
    *ISR(ISR_DMA_SF_DMA0_CH_0: Core0(CPU0))
    */
    ISR(ISR_DMA_SF_DMA0_CH_0)
    {
        ……
        StatusType ret;
        ret = OSCheckISRSource(DMA_SF_DMA0_CH_0)
        ……
    }


OSCheckCPUInformation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void OSCheckCPUInformation(void)

OSCheckCPUInformation is used to check if the CPU information is correct.

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant


**Return type**
   void

**Example**

.. code::

    TaskInit: Priority:1, Preemptive Policy:FULL, Autostart:True

    void main()
    {
      ......
      OSCheckCPUInformation();
      StartOS(OSDEFAULTAPPMODE);
      ......
    }

