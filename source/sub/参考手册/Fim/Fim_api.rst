接口描述 Interface Description
===================================================================

类型定义 Type Definitions
--------------------------------------------------------------------------------

.. list-table:: 
   :widths: 15 5 20
   :header-rows: 1

   * - Type Name
     - Type
     - Description

   * - FiM_FidStatusChangeType
     - uint8
     - This type is used to distinguish an initial FID state from a FID state change callback call. Range: 0..1.




提供的服务 Services
--------------------------------------------------------------------------------

FiM_Init
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void FiM_Init(const FiM_ConfigType *FiMConfigPtr)

This service initializes the FIM.Initialization needs to be called separately for each partition.

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
     - FiMConfigPtr
     - Pointer to the configuration.

**Return type**
   void


FiM_GetFunctionPermission
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType FiM_GetFunctionPermission(FiM_FunctionIdType FID, boolean *Permission)

This service reports the permission state to the functionality.

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
     - FID
     - Identification of a functionality by assigned FID. The FunctionId is configured in the FIM. Min.: 1 (0: Indication of no functionality) Max.: Result of configuration of FIDs in FIM (Max is either 255 or 65535)
   * - [out]
     - Permission
     - TRUE: FID has permission to run FALSE: FID has no permission to run, i.e. shall not be executed

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The request is accepted
   * - E_NOT_OK
     - The request is not accepted, ie. initialization of FIM not completed

FiM_SetFunctionAvailable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType FiM_SetFunctionAvailable(FiM_FunctionIdType FID, boolean Availability)

This service sets the availability of a function. The function is only available if FiMAvailability Support is configured as True.

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
     - FID
     - Identification of a functionality by assigned FID.
   * - [in]
     - Availability
     - The permission of the requested FID. TRUE: Function is available. FALSE: Function is not available.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The request is accepted
   * - E_NOT_OK
     - Request is not accepted (e.g. invalid FID is given)

FiM_GetVersionInfo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void FiM_GetVersionInfo(Std_VersionInfoType *versioninfo)

This service returns the version information of this module.

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
   * - [out]
     - versioninfo
     - Pointer to where to store the version information of this module.

**Return type**
   void


FiM_MainFunction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void FiM_MainFunction(void)

This function is used to evaluate permission states cyclically.

**Sync/Async**
   Synchronous

**Reentrancy**
   Non Reentrant


**Return type**
   void


FiM_DemTriggerOnMonitorStatus
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void FiM_DemTriggerOnMonitorStatus(Dem_EventIdType EventId)

This service is provided to be called by the Dem in order to inform the Fim about monitor status changes.

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
     - EventId
     - Identification of an Event by assigned event number. The Event Number is configured in the DEM. Min.: 1 (0: Indication of no Event or Failure) Max.: Result of configuration of Event Numbers in DEM (Max is either 255 or 65535)

**Return type**
    void


FiM_DemTriggerOnComponentStatus
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void FiM_DemTriggerOnComponentStatus(Dem_ComponentIdType ComponentId, boolean ComponentFailedStatus)

Triggers on changes of the component failed status.

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
     - ComponentId
     - Identification of a DemComponent.
   * - [in]
     - ComponentFailedStatus
     - New FAILED status of the component.

**Return type**
   void


FiM_DemInit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void FiM_DemInit(void)

This service re-initializes the FIM.

**Sync/Async**
   Synchronous

**Reentrancy**
   Non Reentrant


**Return type**
   void


FiM_DemInitSatellite
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void FiM_DemInitSatellite(ApplicationType ApplicationId)

This service re-initializes the FIM Satellite.

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
     - ApplicationId
     - Partition (OsApplication identifier) of the satellite.

**Return type**
   void


