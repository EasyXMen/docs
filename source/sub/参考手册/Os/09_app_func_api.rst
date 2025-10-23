OS-APP Functions
--------------------------------------

Os能够支持一系列操作系统对象的集合（任务，中断，Alarm，调度表，计数器）。该对象集合称为OS-Application。

Os can support a collection of a series of operating system objects (tasks, interrupts, Alarms, schedule tables, counters). This collection of objects is called an OS-Application.

存在两类OS-Application：

There are two types of OS-Applications:

   - 可信OS-Application在监视或保护功能关闭的情况下运行。他们能够无限制地访问内存，操作系统模块的API，并且不需要在运行时受到强制时间限制。当处理器支持的情况下，允许它们在特权模式下运行。
   
     Trusted OS-Applications run with monitoring or protection functions turned off. They have unrestricted access to memory, APIs of operating system modules, and do not need to be subject to mandatory time limits during runtime. When supported by the processor, they are allowed to run in privileged mode.
   
   - 不可信任的OS-Application在监视或保护功能开启的情况下运行。它们对内存的访问受到限制，对操作系统模块的API的访问受到限制，并且需要在运行时进行强制时间限制。当处理器支持时，不允许它们在特权模式下运行。

     Untrusted OS-Applications run with monitoring or protection functions turned on. Their access to memory is restricted, access to APIs of operating system modules is restricted, and they are subject to mandatory time limits during runtime. When supported by the processor, they are not allowed to run in privileged mode.

ORIENTAIS OS提供一些服务，这些服务向调用者提供有关访问权限和对象成员身份的信息。这些服务主要在OS-Application之间检查访问权限和参数的情况下使用。

ORIENTAIS OS provides some services that provide callers with information about access rights and object membership. These services are mainly used in situations where access rights and parameters are checked between OS-Applications.

OS-Applications的状态决定其操作系统对象从其他OS-Applications访问的范围。每个OS-Application始终处于以下状态之一：

The state of OS-Applications determines the scope of access to its operating system objects from other OS-Applications. Each OS-Application is always in one of the following states:

   - 激活且可访问的（APPLICATION_ACCESSIBLE）：可以从其他OS-Applications访问操作系统对象。这是启动时的默认状态。

     Active and accessible (APPLICATION_ACCESSIBLE): Operating system objects can be accessed from other OS-Applications. This is the default state at startup.

   - 当前处于重启阶段（APPLICATION_RESTART）。无法从其他OS-Applications访问操作系统对象。状态有效，直到OS-Application调用AllowAccess。

     Currently in the restart phase (APPLICATION_RESTART). Operating system objects cannot be accessed from other OS-Applications. The state remains valid until the OS-Application calls AllowAccess.

   - 已终止且不可访问（APPLICATION_TERMINATED）：不能从其他OS-Applications访问操作系统对象。状态不会改变。

     Terminated and inaccessible (APPLICATION_TERMINATED): Operating system objects cannot be accessed from other OS-Applications. The state does not change.


Figure显示了状态的转换：

Figure shows the state transitions:

.. figure:: ../../../_static/参考手册/Os/OS-Applications状态图.png
   :alt: APP状态图
   :align: center

   OS-Applications状态图（OS-Applications state diagram）



GetApplicationID
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    ApplicationType GetApplicationID(void)

Get the OS-Application ID of the object calling the API.

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant


**Return type**
    ApplicationType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - Application
     - number
   * - INVALID_OSAPPLICATION
     - INVALID OSAPPLICATION Id

.. note::

   - 在SC3、SC4下有效

     Valid under SC3 and SC4.


GetCurrentApplicationID
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    ApplicationType GetCurrentApplicationID(void)

Get the OS-Application ID to which the currently running Task/ISR/Hook belongs.

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant


**Return type**
    ApplicationType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - Application
     - number
   * - INVALID_OSAPPLICATION
     - INVALID OSAPPLICATION Id

**Example**

.. code::

    App0:
    TaskInit: Priority:1, Preemptive Policy:FULL, Autostart:True
    App1: Trusted
    Task0: Priority:2, Preemptive Policy:FULL
    TrustedFunction:
    TRUSTED_OsApplicationTrustedFunction_0

    TASK(TaskInit)
    {
      uint8 para = 0;
      /* step 1*/
      ApplicationType application;
      application = GetApplicationID();
      /* application = App0*/
      application = GetCurrentApplicationID();
      /* application = App0*/

    ret= CallTrustedFunction(CFG_TRUSTED_OsApplicationTrustedFunction_0_IX, &para)
      /* step 3 ret = E_OK*/
    }

    void TRUSTED_OsApplicationTrustedFunction_0(TrustedFunctionIndexType ix,
                      TrustedFunctionParameterRefType ref)
    {
    /* step 2*/
    ApplicationType application;
      application = GetApplicationID();
      /* application = App1*/
      application = GetCurrentApplicationID();
      /* application = App0*/
      ......
    }

.. note::

   - GetApplicationID和GetCurrentApplicationID区别在于GetApplicationID可以获取可信函数的应用程序ID。

     The difference between GetApplicationID and GetCurrentApplicationID is that GetApplicationID can obtain the application ID of a trusted function.

   - 在SC3、SC4下有效

     Valid under SC3 and SC4



CheckObjectAccess
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    ObjectAccessType CheckObjectAccess(ApplicationType ApplID, ObjectTypeType ObjectType, AppObjectId ObjectID)

This service determines if the OS-Applications, given by ApplID, is allowed to use the IDs of a Task, ISR, Resource,Counter, Alarm or Schedule Table in API calls.

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
     - ApplID
     - OsApplication number
   * - [in]
     - ObjectType
     - Entity type, see
   * - [in]
     - ObjectID
     - Entity number

**Return type**
    ObjectAccessType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - ACCESS
     - the ApplID has access to the object.
   * - NO_ACCESS
     - the ApplID is invalid; ObjectType is invalid;the ApplID does not have access to the object.

**Example**

.. code::

    App0:
    TaskInit: Priority:1, Preemptive Policy:FULL, Autostart:True
    App1:
    Task0: Priority:2, Preemptive Policy:FULL

    TASK(TaskInit)
    {
      ObjectAccessType objectaccess;
      objectaccess = CheckObjectAccess(App0, OBJECT_TASK, TaskInit);
      /* objectaccess = ACCESS */
      objectaccess = CheckObjectAccess(App0, OBJECT_TASK, Task0);
      /* objectaccess = NO_ACCESS*/
    }

.. note::

   - 请确保对象类型和对象ID是匹配的。

     Please ensure that the object type and object ID match.

   - 在SC3，SC4下有效

     Valid under SC3 and SC4



CheckObjectOwnership
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    ApplicationType CheckObjectOwnership(ObjectTypeType ObjectType, AppObjectId ObjectID)

This service determines to which OS-Application a given Task, ISR, Resource, Counter, Alarm or Schedule Table belongs.

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
     - ObjectType
     - Entity type, see
   * - [in]
     - ObjectID
     - Entity number

**Return type**
    ApplicationType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - 
     - the OS-Application to which the object ObjectType belongs.
   * - INVALID_OSAPPLICATION
     - the ObjectID does not exist; ObjectType is invalid; the object type is BJECT_RESOURCE and the object is RES_SCHEDULER.

**Example**

.. code::

    App0:
    TaskInit: Priority:1, Preemptive Policy:FULL, Autostart:True
    App1:
    Task0: Priority:2, Preemptive Policy:FULL

    TASK(TaskInit)
    {
      ApplicationType application;
      application = CheckObjectOwnership(OBJECT_TASK, TaskInit);
      /* objectaccess = App0,*/
      application = CheckObjectOwnership(OBJECT_TASK, Task0);
      /* objectaccess = App1*/
    }

.. note::

   - 请确保对象类型和对象ID是匹配的。

     Please ensure that the object type and object ID match.

   - 在SC3，SC4下有效

     Valid under SC3 and SC4



TerminateApplication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    StatusType TerminateApplication(ApplicationType Application, RestartType RestartOption)

This service returns the current state of an OS-Application.

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
     - Application
     - Application user want to end
   * - [in]
     - RestartOption
     - RESTART: Perform a restart NO_RESTART: Do not restart the app

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
     - <Application> was not valid (only in EXTENDED status)
   * - E_OS_VALUE
     - <RestartOption> was neither RESTART nor NO_RESTART (only in EXTENDED status)
   * - E_OS_ACCESS
     - The caller does not have the right to terminate<Application> (only in EXTENDED status)
   * - E_OS_STATE
     - The state of <Application> does not allow terminating <Application>
   * - E_OS_CALLEVEL
     - Call level at wrong context.
   * - E_OS_DISABLEDINT
     - Interrupts are disabled/suspended, OS shall ignore the service.

**Example**

.. code::

    Example.1
    Counter_0: MaxTick:1000, MinTick:1, CounterType:SOFTWARE
    App0:
    TaskInit: Priority:1, Preemptive Policy:FULL, Autostart:True
    App1:
    Task0:Priority:2,PreemptivePolicy:FULL,Resource:Resource_0, AccessingApplication: App0
      Alarm:Alarm_0, Couner:Counter_0, 
    AccessingApplication: App0
      ScheduleTable:OsScheduleTable_0, Couner:Counter_0, 
    AccessingApplication: App0

    TASK(TaskInit)
    {	
      StatusType ret;
      TickType tick;
      TaskStateRefType taskState;
      ScheduleTableStatusType scheduletableStatus;
      ApplicationStateType applicationState;

    GetApplicationState(App1, &applicationState);
    /* applicationState = APPLICATION_ACCESSIBLE */

      SetRelAlarm(Alarm_0,1,0);
      StartScheduleTableRel(OsScheduleTable_0, 1);
      IncrementCounter(Counter_0);

      ret = GetAlarm(Alarm_0, &tick);
      /* ret = E_OK*/
      ret = GetTaskState(Task0, &taskState);
      /* taskState = TASK_STATE_WAITING */
      GetScheduleTableStatus(OsScheduleTable_0, &scheduletableStatus);
      /* scheduletableStatus = SCHEDULETABLE_RUNNING */

      ActivateTask(Task0);/* Activating Task0 to terminate App1*/

    applicationState = APPLICATION_ACCESSIBLE;
    while(applicationState == APPLICATION_ACCESSIBLE)
    {
      GetApplicationState(App1, &applicationState);
    }

      ret = GetAlarm(Alarm, &tick);
    /* ret = E_OS_ACCESS*/
    ret = GetTaskState(OsTask_0, &taskState);
    /* ret = E_OS_ACCESS*/
    ret = GetScheduleTableStatus(OsScheduleTable_0, &scheduletableStatus);
    /* ret = E_OS_ACCESS*/
    GetApplicationState(App1, &applicationState);
    /* applicationState = APPLICATION_TERMINATED */
    }

    TASK(Task0)
    {
      TerminateApplication(App1, NO_RESTART);
    }

    Example.2
    App0:
    TaskInit: Priority:1, Preemptive Policy:FULL, Autostart:True
    App1:  
    RestartTask: Task_Restart
    Task0:Priority:2,PreemptivePolicy:FULL, 
    AccessingApplication: App0
    Task_Restart: Priority:3,PreemptivePolicy:FULL

    TASK(TaskInit)
    {	
      ApplicationStateType applicationState;

      /* step 1*/
      GetApplicationState(App1, &applicationState);
      /* applicationState = APPLICATION_ACCESSIBLE */

      ActivateTask(Task0);
      
    while(applicationState == APPLICATION_ACCESSIBLE)
    {
      GetApplicationState(App1, &applicationState);
    }

    /* step 4*/
    GetApplicationState(App1, &applicationState);
      /* applicationState = APPLICATION_RESTARTING */
    }

    TASK(Task0)
    {
    /* step 2*/
      TerminateApplication(App1, RESTART);
    }

    TASK(Task_Restart)
    {
    /* step 3*/
    }


.. note::

   - 如果重新启动的OS-Application配置了重启任务，则该任务将在重新启动时被激活。

     If the OS-Application to be restarted is configured with a restart task, this task will be activated during the restart.

   - 在SC3，SC4下有效

     Valid under SC3 and SC4



AllowAccess
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    StatusType AllowAccess(void)

This service sets the own state of an OS-Application from APPLICATION_RESTARTING to APPLICATION_ACCESSIBLE.

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant


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
   * - E_OS_STATE
     - The OS-Application of the caller is in the wrong state
   * - E_OS_CALLEVEL
     - Call level at wrong context.
   * - E_OS_DISABLEDINT
     - Interrupts are disabled/suspended, OS shall ignore the service.

**Example**

.. code::

    Example.1
    App0:
    TaskInit: Priority:1, Preemptive Policy:FULL, Autostart:True
    App1:  
    RestartTask: Task_Restart
    Task0:Priority:2,PreemptivePolicy:FULL, 
    AccessingApplication: App0
    Task_Restart: Priority:3,PreemptivePolicy:FULL

    TASK(TaskInit)
    {	
      ApplicationStateType applicationState;

      /* step 1*/
      GetApplicationState(App1, &applicationState);
      /* applicationState = APPLICATION_ACCESSIBLE */

      ActivateTask(Task0);

    while(applicationState == APPLICATION_ACCESSIBLE)
    {
      GetApplicationState(App1, &applicationState);
    }

    while(applicationState != APPLICATION_ACCESSIBLE)
    {
      GetApplicationState(App1, &applicationState);
    }

    /* step 4*/
    GetApplicationState(App1, &applicationState);
      /* applicationState = APPLICATION_ACCESSIBLE */
    }

    TASK(Task0)
    {
    /* step 2*/
      TerminateApplication(App1, RESTART);
    }

    TASK(Task_Restart)
    {
    /* step 3*/
    AllowAccess();
    }

.. note::

   - 在SC3，SC4下有效

     Valid under SC3 and SC4


GetApplicationState
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    StatusType GetApplicationState(ApplicationType Application, ApplicationStateRefType Value)

This service returns the current state of an OS-Application.

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
     - Application
     - Application number user want to get
   * - [out]
     - Value
     - ACCESSIBLE:accessible RESTARTING:Restarting TERMINATED:ended

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
     - <Application> is not valid.
   * - E_OS_CALLEVEL
     - Call level at wrong context.
   * - E_OS_DISABLEDINT
     - Interrupts are disabled/suspended, OS shall ignore the service.
   * - E_OS_ILLEGAL_ADDRESS
     - The address of Value is invalid.

.. note::

   - 在SC3，SC4下有效

     Valid under SC3 and SC4




