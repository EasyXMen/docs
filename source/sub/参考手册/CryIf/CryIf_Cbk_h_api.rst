
类型定义 Type Definitions
----------------------------------------

None

      
提供的服务 Services
----------------------------------------
CryIf_CallbackNotification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void CryIf_CallbackNotification(Crypto_JobType *job, Crypto_ResultType result)

Callback function for Crypto Job notification.This function is called by the Crypto driver to notify the application about the completion of a Crypto Job.

**Sync/Async**
   TRUE

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
     - job
     - Pointer to a Crypto Job structure. This parameter is a pointer to a structure that contains information about the Crypto Job, such as the job ID, the input data, and the output data.
   * - [in]
     - result
     - Result of the Crypto Job. This parameter indicates whether the Crypto Job was successful or not. It can be one of the following values

**Return type**
   void


