Hook(Functions)
--------------------------------------

ORIENTAIS OS为用户提供了一系列钩子函数功能(Hook)。例如在钩子函数StartupHook中初始化一些硬件，在钩子函数ErrorHook中捕获并处理的一些错误。

ORIENTAIS OS provides users with a series of hook functions. For example, hardware can be initialized in the StartupHook function, and errors can be captured and handled in the ErrorHook function.


ErrorHook
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void ErrorHook(StatusType Error)

The specific error hook is called whenever a Task or ISR calls system service to cause an error.

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
     - Error
     - Error code

**Return type**
   void

**Example**

.. code::

    TASK(TaskInit)
    {
      StatusType ret;
      ret = ActivateTask(OS_TASK_INVALID); /* step 1 */
      /* step 3 : ret = E_OS_ID */
      ......
    }

    void ErrorHook(StatusType Error)
    {
      /* step 2 */
      if (E_OS_ID == Error)
      {
        ......
      }
    }

.. note::

    - 执行错误处理。该接口由用户实现错误处理，并由ORIENTAIS OS调用。

      Performs error handling. This interface is implemented by the user for error handling and is called by ORIENTAIS OS.

    - 用户可以通过输入参数<Error>的值来了解错误类型。

      Users can determine the error type from the value of the input parameter <Error>.



PostTaskHook
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void PostTaskHook(void)

This hook routine is called by ORIENTAIS OS after executing the current task, but before leaving the task's running state (to allow evaluation of the TaskID by GetTaskID).

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant


**Return type**
   void

**Example**

.. code::

    TASK(TaskInit)
    {
      
    TerminateTask(); /* step 1 */
    /* TerminateTask, ChainTask, WaitEvent and Schedule can make OS scheduling.*/
    /* If a task is terminated, the PostTaskHook shall be triggered.*/
      ......
    }

    void PostTaskHook ()
    {
      TaskType taskid;
    /* step 2 */
    GetTaskID(&taskid);
    /* taskid = OS_TASK_INVALID */
      ......
    }

.. note::

    - 该接口由用户实现，并由ORIENTAIS OS调用。

      This interface is implemented by the user and is called by ORIENTAIS OS.


PreTaskHook
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void PreTaskHook(void)

This hook routine is called by ORIENTAIS OS before executing a new task, but after the transition of the task to the running state (to allow evaluation of the TaskID by GetTaskID.

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant


**Return type**
   void

**Example**

.. code::

    TASK(TaskInit)
    {
    ActivateTask(Task0); /* step 1 */
    /* Before a task execult, the PreTaskHook shall be triggered.*/
      ......
    }

    TASK(Task0)
    {
      TaskType taskid;
      /* step 3 */
    GetTaskID(&taskid);
    /* taskid = Task0 */
    }

    void PreTaskHook()
    {
    /* step 2 */
      ......
    }

.. note::

    - 该接口由用户实现，并由ORIENTAIS OS调用。

      This interface is implemented by the user and is called by ORIENTAIS OS.


StartupHook
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void StartupHook(void)

This hook routine is called by the operating system at the end of the operating system in itialisation and before the scheduler is running. At this time the applicationcan initialise device drivers etc.

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant


**Return type**
   void

**Example**

.. code::

    void main()
    {
      ......
      StartOS(OSDEFAULTAPPMODE); /*step 1*/
      /*step 3*/
      ......
    }
    void StartupHook()
    {
      /*step 2*/
      ......
    }

.. note::

    - 该接口由用户实现，并由ORIENTAIS OS调用。
       
      This interface is implemented by the user and is called by ORIENTAIS OS.


ShutdownHook
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void ShutdownHook(StatusType Error)

This hook routine is called by the operating system when the OS service ShutdownOS has been called. This routine is called during the operating system shutdown.

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
     - Error
     - Error code

**Return type**
   void

**Example**

.. code::

    TASK(TaskInit)
    {
    ShutdownOS(E_OK); /*step 1*/
    /* Won't execute here.*/
    /* If user calls ShutdownAllCores in mutil-core, a similar situation shall happen in every core. */
      ......
    }

    void ShutdownHook()
    {
      /*step 2*/
      ......
    }

.. note::

    - 该接口由用户实现，并由ORIENTAIS OS调用。

      This interface is implemented by the user and is called by ORIENTAIS OS.


ProtectionHook
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    ProtectionReturnType ProtectionHook(StatusType Fatalerror)

This hook routine is called by the operating system when the OS service protection functions.

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
     - Fatalerror
     - Error code

**Return type**
    ProtectionReturnType

**Example**

.. code::

    App0: Non-Trusted
    TaskInit: Priority:1, Preemptive Policy:FULL, Autostart:True
          TimingProtection: ExecutionBudget:0.005
    uint8 var;

    TASK(TaskInit)
    {
      GetSpinlock(Spinlock_0);
      TerminateTask(); /* step 1 : Invalid Calling, It triggers E_OS_SPINLOCK error.*/
      var = 0; /* Writing global variable to trigger the memory protection*/
      DelayMs(5);  /* Execution time out to trigger the timing protection*/
    }

    ProtectionReturnType ProtectionHook(StatusType Fatalerror) 
    {
      /*step 2*/
      ProtectionReturnType ret = PRO_IGNORE;
      if (E_OS_SPINLOCK == Fatalerror)
      {
    ret = PRO_TERMINATETASKISR;
    /*Return with PRO_TERMINATETASKISR. 
    The fault task/isr shall be terminated.*/
      }
    else if (E_OS_PROTECTION_MEMORY == Fatalerror)
      {
    ret = PRO_SHUTDOWN;
    /*Return with PRO_SHUTDOWN. 
    The OS shall shutdown.*/
      }
    else if (E_OS_PROTECTION_TIME == Fatalerror)
      {
    ret = PRO_TERMINATEAPPL_RESTART;
    /*Return with PRO_TERMINATEAPPL_RESTART. 
    The fault application shall restart.*/
      }
      ......
    }

.. note::

    - 该接口由用户实现错误处理，并由ORIENTAIS OS调用。

      This interface is implemented by the user for error handling and is called by ORIENTAIS OS.

    - 用户可以通过返回值来选择五种处理方式中的一种处理。

      Users can select one of five processing methods through the return value.



IdleHook_Core<n>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void IdleHook_Core<n>(void)

This HOOK is called when ORIENTAIS OS enters an idle task.

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant


**Return type**
   void

.. note::

    - 该接口由用户实现，并由ORIENTAIS OS调用。

      This interface is implemented by the user and is called by ORIENTAIS OS.

    - 如果没有正在运行的任务/中断，则调用此接口。

      This interface is called when no task or interrupt is running.


ErrorHook_<ApplicationName>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void ErrorHook_<ApplicationName> (StatusType Error)

This HOOK is called when ORIENTAIS OS enters an idle task.

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
     - Error
     - Error code

**Return type**
   void

.. note::

    - 该接口由用户实现，并由ORIENTAIS OS调用。

      This interface is implemented by the user and is called by ORIENTAIS OS.


StartupHook_<ApplicationName>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void StartupHook_<ApplicationName> (void)

When a specific application has the startup hook function enabled, ORIENTAIS OS calls this function when that application starts.

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant


**Return type**
   void

.. note::

    - 该接口由用户实现，并由ORIENTAIS OS调用。

      This interface is implemented by the user and is called by ORIENTAIS OS.


ShutdownHook_<ApplicationName>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void ShutdownHook_<ApplicationName> (StatusType Fatalerror) 

When a specific application has the shutdown hook function enabled, ORIENTAIS OS calls this hook function when that application is being shut down.

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
     - Fatalerror
     - Error code

**Return type**
   void

.. note::

    - 该接口由用户实现，并由ORIENTAIS OS调用。

      This interface is implemented by the user and is called by ORIENTAIS OS.


