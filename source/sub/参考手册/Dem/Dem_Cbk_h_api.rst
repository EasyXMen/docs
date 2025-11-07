
提供给NvM的回调函数(Callback functions provided to NvM)
----------------------------------------------------------------
Dem_NvMInitAdminData
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

   Std_ReturnType Dem_NvMInitAdminData(NvM_InitBlockRequestType InitBlockRequest)

Initializes the NvBlock for administrative data supposed to be called by the NvM in order to (re)initialize the data in case the non-volatile memory has never been stored, or was corrupted. (See NvMBlockDescriptor/NvMInitBlockCallback) It can also be used to force a reinitialization of the Dem data triggered by the application (e.g. after a new software version has been flashed to the ECU). In the latter case, make sure the function is not called while the Dem is active.

**Sync/Async**
   Synchronous

**Reentrancy**
   Non reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - InitBlockRequest
     - The request type of the currentlyprocessed block

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Initializes the NvBlock for administrative data successfully
   * - E_NOT_OK
     - Initializes the NvBlock for administrative data failed

Dem_NvMInitStatusData
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_NvMInitStatusData(NvM_InitBlockRequestType InitBlockRequest)

Initializes the NvBlock for event status data supposed to be called by the NvM in order to (re)initialize the data in case the non-volatile memory has never been stored, or was corrupted. (See NvMBlockDescriptor/NvMInitBlockCallback) It can also be used to force a reinitialization of the Dem data triggered by the application (e.g. after a new software version has been flashed to the ECU). In the latter case, make sure the function is not called while the Dem is active.

**Sync/Async**
   Synchronous

**Reentrancy**
   Non reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - InitBlockRequest
     - The request type of the currentlyprocessed block

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Initializes the NvBlock for event status data successfully
   * - E_NOT_OK
     - Initializes the NvBlock for event status data failed

Dem_NvMInitDebounceData
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_NvMInitDebounceData(NvM_InitBlockRequestType InitBlockRequest)

Initializes the NvBlock for persisted debounce values supposed to be called by the NvM in order to (re)initialize the data in case the non-volatile memory has never been stored, or was corrupted. (See NvMBlockDescriptor/NvMInitBlockCallback) It can also be used to force a reinitialization of the Dem data triggered by the application (e.g. after a new software version has been flashed to the ECU). In the latter case, make sure the function is not called while the Dem is active.

**Sync/Async**
   Synchronous

**Reentrancy**
   Non reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - InitBlockRequest
     - The request type of the currentlyprocessed block

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Initializes the NvBlock for persisted debounce values successfully
   * - E_NOT_OK
     - Initializes the NvBlock for persisted debounce values failed

Dem_NvMJobFinished
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Dem_NvMJobFinished(NvM_BlockRequestType ServiceId, NvM_RequestResultType JobResult)

Notifies the Dem module about a completed NV operation This function has to be called by the NvM after a write operation has finished. (See NvMBlockDescriptor/NvMSingleBlockCallback)

**Sync/Async**
   Synchronous

**Reentrancy**
   Non reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - ServiceId
     - Service identifier
   * - [in]
     - JobResult
     - Result of the NV job

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Notification is successful
   * - E_NOT_OK
     - Notification is fail

