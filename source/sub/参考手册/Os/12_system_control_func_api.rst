System(Control Functions)
--------------------------------------



StartOS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void StartOS(AppModeType Mode)

The user can call this system service to start the operating system in a specific mode.

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
     - Mode
     - Application mode (launch mode), defined by the user on the tool

**Return type**
   void

.. note::

    - 系统初始化时必须使用此接口。

      This interface must be used during system initialization.

    - 所有核必须以相同模式启动。

      All cores must boot in the same mode.


ShutdownOS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void ShutdownOS(StatusType Error)

The user can call this system service to abort the overall system (e.g. emergency off).

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
     - Error type, see StatusType for detail

**Return type**
   void

.. note::

    - 该服务调用者所属OS-Application必须是可信OS-Application

      The OS-Application to which the service caller belongs must be a trusted OS-Application.


GetActiveApplicationMode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    AppModeType GetActiveApplicationMode(void)

This service returns t he current application mode. It may be used to write mode dependent code.

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant


**Return type**
    AppModeType

**Example**

.. code::

    TaskInit: Priority:1, Preemptive Policy:FULL, Autostart:True

    void mian()
    {
      ......
      StartOS(OSDEFAULTAPPMODE);
      ......
    }

    TASK(TaskInit)
    {
      AppModeType appMode;
      appMode = GetActiveApplicationMode();
      /* appMode = OSDEFAULTAPPMODE */
    }

