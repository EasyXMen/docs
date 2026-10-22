
类型定义
--------
.. 如果没有就不存在该章节，或为None

None

      
提供的服务
-----------
StbM_CanSetSlaveTimingData
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType StbM_CanSetSlaveTimingData(StbM_SynchronizedTimeBaseType timeBaseId, const StbM_CanTimeSlaveMeasurementType *measureDataPtr)

Allows the CanTSyn Module to forward CAN specific details to the StbM.

**Sync/Async**
   Synchronous

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
     - timeBaseId
     - Time Base reference
   * - [in]
     - measureDataPtr
     - New measurement data

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - successful
   * - E_NOT_OK
     - failed

StbM_CanSetMasterTimingData
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType StbM_CanSetMasterTimingData(StbM_SynchronizedTimeBaseType timeBaseId, const StbM_CanTimeMasterMeasurementType *measureDataPtr)

Provides CAN Timesyn module specific data for a Time Master to the StbM.

**Sync/Async**
   Synchronous

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
     - timeBaseId
     - Time Base reference
   * - [out]
     - measureDataPtr
     - New measurement data

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - successful
   * - E_NOT_OK
     - failed

