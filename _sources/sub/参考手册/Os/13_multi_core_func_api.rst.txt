Multi-Core(Functions)
--------------------------------------


GetCoreID
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    CoreIdType GetCoreID(void)

Get the logical ID of the currently executing core.

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant


**Return type**
    CoreIdType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - Logic
     - ID
   * - OS_CORE_INVALID
     - INVALID CORE ID

**Example**

.. code::

    TaskInit: Priority:1, Preemptive Policy:FULL, Autostart:True

    void main(void)
    {
      CoreIdType  coreId;
      coreId = GetCoreID();
      ......
    }

.. note::

   - 用户可以在StratOS之前调用该服务

     Users can call this service before StartOS.


GetNumberOfActivatedCores
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    uint32 GetNumberOfActivatedCores(void)

Get the number of cores currently activated (cores managed by ORIENTAIS OS)

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant


**Return type**
   uint32

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - The
     - number of cores currently activated

**Example**

.. code::

    TaskInit: Priority:1, Preemptive Policy:FULL, Autostart:True

    void main(void)
    {
      uint32  coreNum;
      coreNum = GetNumberOfActivatedCores ();
      ......
    }


StartCore
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void StartCore(CoreIdType CoreID, StatusType *Status)

Start the specified Autosar core.

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
   * - 
     - CoreID
     - 
   * - [out]
     - Status
     - StatusType, The return value of this service

**Return type**
   void

**Example**

.. code::

    void main ()
    {
        StatusType rv;
        switch (GetCoreID())
        {
            case OS_CORE_ID_MASTER:
                /* Check the CPU Information */
                /* Software and hardware initial. */
                /* The master core starts automatically. */
                StartOS(OSDEFAULTAPPMODE);
                /* If other cores exist, they can be started by calling StartCore*/
                #if(TRUE == CFG_CORE1_AUTOSAROS_ENABLE)
                  StartCore(OS_CORE_ID_1, &rv);
    #endif
                ......
                break;
            case OS_CORE_ID_1:
            ......
                /* The slave core is started by master core. */
                StartOS(OSDEFAULTAPPMODE);
            ......
            break;        
            ......
    }
    ......
    }


StartNonAutosarCore
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void StartNonAutosarCore(CoreIdType CoreID, StatusType *Status)

Start the specified non-Autosar core.

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
   * - 
     - CoreID
     - 
   * - [out]
     - Status
     - StatusType, The return value of this service

**Return type**
   void

**Example**

.. code::

    Cores Number:1
    #define		CFG_CORE_MAX							3U
    #define		OS_CORE_ID_MASTER					((Os_CoreIdType)0U)

    #define		OS_CORE_ID_0							((Os_CoreIdType)0U)
    #define		OS_NONAUTOSARCORE_ID_0				((Os_CoreIdType)1U)
    #define		OS_NONAUTOSARCORE_ID_1				((Os_CoreIdType)2U)

    void main()
    {
      ......
    StartNonAutosarCore(OS_NONAUTOSARCORE_ID_0);
    ......
    StartNonAutosarCore(OS_NONAUTOSARCORE_ID_1);
    ......
    }

.. note::

    - 该函数仅允许启动非Autosar内核。

     This function permits starting only non-AUTOSAR kernels.


ShutdownAllCores
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void ShutdownAllCores(StatusType Error)

Get the logical ID of the currently executing core.

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
     - error code, see StatusType

**Return type**
   void

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - Logic
     - ID
   * - OS_CORE_INVALID
     - 

**Example**

.. code::

    App0: Trusted
    TaskInit: Priority:1, Preemptive Policy:FULL, Autostart:True

    TASK(TaskInit)
    {
      ShutdownAllCores(E_OK);
    }

    void ShutdownHook(StatusType Error)
    {
      /* All cores shall enter the hook, and the Error is E_OK */
    }

.. note::

    - 该服务调用者所属OS-Application必须是可信OS-Application。

     The calling OS-Application of this service must be a trusted OS-Application.


ControlIdle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    StatusType ControlIdle(CoreIdType CoreID, IdleModeType IdleMode)

This API allows the caller to select the idle mode action which is performed during idle time of the OS.

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
     - CoreID
     - Core Identifier
   * - [in]
     - IdleMode
     - Selected Idle Mode

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
     - Invalid core and/or invalid idleMode
   * - E_OS_CALLEVEL
     - Call at interrupt level
   * - E_OS_DISABLEDINT
     - Interrupts are disabled/suspended, OS shall ignore the service

**Example**

.. code::

    App0: Trusted
    TaskInit: Priority:1, Preemptive Policy:FULL, Autostart:True

    void main (void)
    {
      StatusType  ret;
      ret = ControlIdle(OS_CORE_ID_0, OS_RUN);
    }




