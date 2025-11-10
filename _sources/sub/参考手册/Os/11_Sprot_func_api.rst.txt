Service(Protection Functions)
--------------------------------------

当OS-Application进行API调用，服务保护需要考虑多种情况：

When an OS-Application makes an API call, service protection must consider various scenarios:

   - 句柄无效或超出范围

     The handle is invalid or out of range.

   - 在错误的调用场景中，例如在StartupHook中调用ActivateTask()

     In an incorrect calling context, such as calling ActivateTask() within StartupHook.

   - 或未能进行API调用导致ORIENTAIS OS处于未定义状态，例如：在占用资源期间结束任务

     Or failure to make proper API calls resulting in ORIENTAIS OS entering an undefined state, for example: terminating a task while holding resources.

   - 会影响系统中其他所有OS-Application的行为，例如：ShutdownOS()

     Affecting the behavior of all other OS-Applications in the system, such as: ShutdownOS().

   - 操纵属于另一个OS-Application的操作系统对象(该OS对象没有必需的权限)，例如 OS-Application尝试对其不拥有访问权限的任务执行ActivateTask()

     Manipulating operating system objects belonging to another OS-Application (without the required permissions), for example, an OS-Application attempting to execute ActivateTask() on a task it lacks access permissions for.

关于系统服务在错误的场景中被调用，请参阅**错误!未找到引用源**。

For system services called in incorrect contexts, refer to **Error! Reference source not found**.


CallTrustedFunction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    StatusType CallTrustedFunction(TrustedFunctionIndexType FunctionIndex, TrustedFunctionParameterRefType FunctionParams)

The interface provided by trusted functions to external calls. Untrusted apps can access internal resources of trusted apps.

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
     - FunctionIndex
     - The index number of the trusted function
   * - [in]
     - FunctionParams
     - Pointer to a trusted function parameter

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
   * - E_OS_CALLEVEL
     - Wrong calling environment
   * - E_OS_DISABLEDINT
     - Unable to call system services because of interrupt disable/suspend
   * - E_OS_ILLEGAL_ADDRESS
     - Parameter address access illegal
   * - E_OS_SERVICEID
     - Incoming trusted function index error
   * - E_OS_CORE
     - The object is not belong to local core

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
      /* step 1*/
    ret= CallTrustedFunction(CFG_TRUSTED_OsApplicationTrustedFunction_0_IX);
      /* step 3 ret = E_OK*/
    }

    void TRUSTED_OsApplicationTrustedFunction_0(TrustedFunctionIndexType ix,
                      TrustedFunctionParameterRefType ref)
    {
    /* step 2*/
      ......
    }

.. note::

   - 在SC3，SC4下有效

     Valid under SC3 and SC4

