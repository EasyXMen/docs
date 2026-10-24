
类型定义
--------
.. 如果没有就不存在该章节，或为None

None

      
提供的服务
-----------
StbM_EthSetSlaveTimingData
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType StbM_EthSetSlaveTimingData(StbM_SynchronizedTimeBaseType timeBaseId, const StbM_EthTimeSlaveMeasurementType *measureDataPtr)

Allows the EthTSyn Module to forward Ethernet specific details to the StbM.

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

StbM_EthSetPdelayInitiatorData
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType StbM_EthSetPdelayInitiatorData(StbM_SynchronizedTimeBaseType timeBaseId, const StbM_PdelayInitiatorMeasurementType *measureDataPtr)

Allows the EthTSyn Module to forward Ethernet specific pdelay initiator data to the StbM.

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

StbM_EthSetMasterTimingData
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType StbM_EthSetMasterTimingData(StbM_SynchronizedTimeBaseType timeBaseId, const StbM_EthTimeMasterMeasurementType *measureDataPtr)

Provides Ethernet Timesyn module specific data for a Time Master to the StbM.

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

StbM_EthSetPdelayResponderData
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType StbM_EthSetPdelayResponderData(StbM_SynchronizedTimeBaseType timeBaseId, const StbM_PdelayResponderMeasurementType *measureDataPtr)

Provides Ethernet Timesyn module specific pdelay responder data for a Time Master to the StbM.

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

