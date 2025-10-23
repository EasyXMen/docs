    
Callback提供的服务 Services Provided by Callback
----------------------------------------------------------------------------
Csm_CallbackNotification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Csm_CallbackNotification(Crypto_JobType *job, Crypto_ResultType result)

the CSM that a job has finished. This function is used by the underlying layer (CRYIF).

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
     - Holds a pointer to the job, which has finished.
   * - [in]
     - result
     - Contains the result of the cryptographic operation

**Return type**
   void


