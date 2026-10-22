
类型定义
--------
.. 如果没有就不存在该章节，或为None

.. list-table:: 
   :widths: 15 5 20
   :header-rows: 1

   * - Type Name
     - Type
     - Description

   * - StbMTimeNtfCallbackType
     - void*
     - 

   * - StbM_HwCounterType
     - uint64
     - 

   * - StbM_LocalTimeType
     - uint64
     - 

   * - StbM_Time64TupleType
     - struct
     - 

   * - StbM_RateCorrectionTupleType
     - struct
     - 

   * - StbM_RateCorrectionType
     - struct
     - 

   * - StbM_CurrentRateType
     - struct
     - 

   * - StbM_NotificationType
     - struct
     - 

   * - StbM_RateValidationTimeTripleType
     - struct
     - 

   * - StbM_TimeBaseType
     - struct
     - 


      
提供的服务
-----------
StbM_MainFunction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void StbM_MainFunction(void)

This function needs to be called periodically to perform the AUTOSAR StbM activities.

**Sync/Async**
   Asynchronous

**Reentrancy**
   Reentrant (Reentrant for different partitions. Non reentrant for the same partition.)


**Return type**
   void


