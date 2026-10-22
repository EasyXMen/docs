FaultManagerHook Functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

FaultManagerHook用于软硬件故障后用户处理（例如，打印故障信息）的钩子函数。

FaultManagerHook is a hook function used for user processing after hardware and software faults (e.g., printing fault information).

FaultManagerHook
*******************************

.. code::

    void FaultManagerHook(const ExceptionMsgType *Error)

FaultManagerHook is a user-defined hook function for handling hardware and software faults (e.g., printing fault information).

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
     - Error
     - Pointer to fault information

**Return type**
   void

**Return values**
   None
