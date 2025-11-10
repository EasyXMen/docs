
.. list-table:: 
   :widths: 15 5 20
   :header-rows: 1

   * - Type Name
     - Type
     - Description

   * - EcuM_RunStatusType
     - uint8
     - Result of the Run Request Protocol sent to BswM
   
   * - EcuM_WakeupSourceType
     - uint32
     - The bit field provides one bit for each wake up source.
   
   * - EcuM_WakeupStatusType
     - uint8
     - The type describes the possible states of a wakeup source
   
   * - EcuM_ResetType
     - uint8
     - This type describes the reset mechanisms supported by the ECU State Manager
   
   * - EcuM_StateType
     - uint8
     - 
   
   * - EcuM_TargetType
     - struct
     - Encode states and sub-states of the ECU Manager module.
   
   * - EcuM_ConfigType
     - EcuM_PBConfigType
     - EcuM Configuration Type (PB) 

提供的服务(Services)
---------------------
 

EcuM_GetVersionInfo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void EcuM_GetVersionInfo(Std_VersionInfoType *versioninfo)

Returns the version information of this module.

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
   * - [out]
     - versioninfo
     - Pointer to where to store the version information of this module.

**Return type**
   void


EcuM_GoDownHaltPoll
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EcuM_GoDownHaltPoll(EcuM_UserType UserID)

Instructs the ECU State Manager module to go into a sleep mode, reset, or off depending on the previously selected shutdown target.

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
     - UserID
     - Module ID of the calling module. Only special modules are allowed to call this function and only valid when the shutdown target is RESET or OFF.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request accepted and processed successfully.
   * - E_NOT_OK
     - The request was not accepted.

EcuM_Init
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void EcuM_Init(void)

Initializes the ECU state manager and carries out the startup procedure. The function will never return (it calls StartOS).

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant


**Return type**
   void


EcuM_StartupTwo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void EcuM_StartupTwo(void)

Implements the STARTUP II state.

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant


**Return type**
   void


EcuM_Shutdown
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void EcuM_Shutdown(void)

Typically called from the shutdown hook, this function takes over execution control and carries out GO OFF II activities.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant


**Return type**
   void


EcuM_SetState
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void EcuM_SetState(EcuM_StateType state)

Function called by BswM to notify about a state switch.

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
     - state
     - State indicated by BswM.

**Return type**
   void


EcuM_RequestRUN
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EcuM_RequestRUN(EcuM_UserType user)

Places a request for the RUN state. Requests can be placed by every user made known to the state manager at configuration time.

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
     - user
     - ID of the entity requesting the RUN state.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The request was accepted by EcuM.
   * - E_NOT_OK
     - The request was not accepted by EcuM, a detailed error condition was sent to DET (see Error Codes).

EcuM_ReleaseRUN
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EcuM_ReleaseRUN(EcuM_UserType user)

Releases a RUN request previously done with a call to EcuM_RequestRUN. The service is intended for implementing AUTOSAR ports.

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
     - user
     - ID of the entity releasing the RUN state.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The request was accepted by EcuM.
   * - E_NOT_OK
     - The request was not accepted by EcuM, a detailed error condition was sent to DET (see Error Codes).

EcuM_RequestPOST_RUN
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EcuM_RequestPOST_RUN(EcuM_UserType user)

Places a request for the POST RUN state. Requests can be placed by every user made known to the state manager at configuration time. Requests for RUN and POST RUN must be tracked independently (i.e., using two independent variables). The service is intended for implementing AUTOSAR ports.

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
     - user
     - ID of the entity requesting the POST RUN state.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The request was accepted by EcuM.
   * - E_NOT_OK
     - The request was not accepted by EcuM, a detailed error condition was sent to DET (see Error Codes).

EcuM_ReleasePOST_RUN
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EcuM_ReleasePOST_RUN(EcuM_UserType user)

Releases a POST RUN request previously done with a call to EcuM_RequestPOST_RUN. The service is intended for implementing AUTOSAR ports.

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
     - user
     - ID of the entity releasing the POST RUN state.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The release request was accepted by EcuM.
   * - E_NOT_OK
     - The release request was not accepted by EcuM, a detailed error condition was sent to DET (see Error Codes).

EcuM_SelectShutdownTarget
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EcuM_SelectShutdownTarget(EcuM_ShutdownTargetType shutdownTarget, EcuM_ShutdownModeType shutdownMode)

Selects the shutdown target. This function is part of the ECU Manager Module port interface.

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
     - shutdownTarget
     - The selected shutdown target.
   * - [in]
     - shutdownMode
     - The identifier of a sleep mode (if target is ECUM_STATE_SLEEP) or a reset mechanism (if target is ECUM_STATE_RESET) as defined by configuration.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The new shutdown target was set.
   * - E_NOT_OK
     - The new shutdown target was not set.

EcuM_GetShutdownTarget
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EcuM_GetShutdownTarget(EcuM_ShutdownTargetType *shutdownTarget, EcuM_ShutdownModeType *shutdownMode)

Returns the currently selected shutdown target as set by EcuM_SelectShutdownTarget. This function is part of the ECU Manager Module port interface.

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
   * - [out]
     - shutdownTarget
     - One of these values is returned: ECUM_STATE_SLEEP / ECUM_STATE_RESET / ECUM_STATE_OFF.
   * - [out]
     - shutdownMode
     - If the out parameter "shutdownTarget" is ECUM_STATE_SLEEP, shutdownMode indicates which of the configured sleep modes was chosen. If "shutdownTarget" is ECUM_STATE_RESET, shutdownMode indicates which of the configured reset modes was chosen.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The service has succeeded.
   * - E_NOT_OK
     - The service has failed, e.g., due to a NULL pointer being passed.

EcuM_GetLastShutdownTarget
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EcuM_GetLastShutdownTarget(EcuM_ShutdownTargetType *shutdownTarget, EcuM_ShutdownModeType *shutdownMode)

Returns the shutdown target of the previous shutdown process. This function is part of the ECU Manager Module port interface.

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
   * - [out]
     - shutdownTarget
     - One of these values is returned: ECUM_STATE_SLEEP / ECUM_STATE_RESET / ECUM_STATE_OFF.
   * - [out]
     - shutdownMode
     - If the out parameter "shutdownTarget" is ECUM_STATE_SLEEP, shutdownMode indicates which of the configured sleep modes was chosen. If "shutdownTarget" is ECUM_STATE_RESET, shutdownMode indicates which of the configured reset modes was chosen.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The service has succeeded.
   * - E_NOT_OK
     - The service has failed, e.g., due to a NULL pointer being passed.

EcuM_SelectShutdownCause
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EcuM_SelectShutdownCause(EcuM_ShutdownCauseType cause)

Elects the cause for a shutdown. This function is part of the ECU Manager Module port interface.

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
   * - 
     - cause
     - 

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The new shutdown cause was set.
   * - E_NOT_OK
     - The new shutdown cause was not set.

EcuM_GetShutdownCause
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EcuM_GetShutdownCause(EcuM_ShutdownCauseType *shutdownCause)

Returns the selected shutdown cause as set by EcuM_SelectShutdownCause. This function is part of the ECU Manager Module port interface.

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
   * - [out]
     - shutdownCause
     - The selected cause of the next shutdown.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The service has succeeded.
   * - E_NOT_OK
     - The service has failed.

EcuM_GetPendingWakeupEvents
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    EcuM_WakeupSourceType EcuM_GetPendingWakeupEvents(void)

Gets pending wakeup events.

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant


**Return type**
   


EcuM_ClearWakeupEvent
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void EcuM_ClearWakeupEvent(EcuM_WakeupSourceType sources)

Clears wakeup events.

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
     - sources
     - Events to be cleared.

**Return type**
   void


EcuM_GetValidatedWakeupEvents
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    EcuM_WakeupSourceType EcuM_GetValidatedWakeupEvents(void)

Gets validated wakeup events.

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant


**Return type**
   


EcuM_GetExpiredWakeupEvents
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    EcuM_WakeupSourceType EcuM_GetExpiredWakeupEvents(void)

Gets expired wakeup events.

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant


**Return type**
   


EcuM_SetRelWakeupAlarm
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EcuM_SetRelWakeupAlarm(EcuM_UserType user, EcuM_TimeType time)

Sets a user's wakeup alarm relative to the current point in time. This function is part of the ECU Manager Module port interface.

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
     - user
     - The user that wants to set the wakeup alarm.
   * - [in]
     - time
     - Relative time from now in seconds.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The service has succeeded.
   * - E_NOT_OK
     - The service failed.
   * - ECUM_E_EARLIER_ACTIVE
     - An earlier alarm is already set.

EcuM_SetAbsWakeupAlarm
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EcuM_SetAbsWakeupAlarm(EcuM_UserType user, EcuM_TimeType time)

Sets the user's wakeup alarm to an absolute point in time. This function is part of the ECU Manager Module port interface.

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
     - user
     - The user that wants to set the wakeup alarm.
   * - [in]
     - time
     - Absolute time in seconds. Note that absolute alarms use knowledge of the current time.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The service has succeeded.
   * - E_NOT_OK
     - The service failed.
   * - ECUM_E_EARLIER_ACTIVE
     - An earlier alarm is already set.
   * - ECUM_E_PAST
     - The given point in time has already passed.

EcuM_AbortWakeupAlarm
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EcuM_AbortWakeupAlarm(EcuM_UserType user)

Aborts the wakeup alarm previously set by this user. This function is part of the ECU Manager Module port interface.

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
     - user
     - The user that wants to cancel the wakeup alarm.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The service has succeeded.
   * - E_NOT_OK
     - The service failed.
   * - ECUM_E_NOT_ACTIVE
     - No owned alarm found.

EcuM_GetCurrentTime
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EcuM_GetCurrentTime(EcuM_TimeType *time)

Returns the current value of the EcuM clock (i.e., the time since battery connect). This function is part of the ECU Manager Module port interface.

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
   * - [out]
     - time
     - Absolute time in seconds since battery connect.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The service has succeeded.
   * - E_NOT_OK
     - 

EcuM_GetWakeupTime
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EcuM_GetWakeupTime(EcuM_TimeType *time)

Returns the current value of the master alarm clock (the minimum absolute time of all user alarm clocks). This function is part of the ECU Manager Module port interface.

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
   * - [out]
     - time
     - Absolute time in seconds for the next wakeup. 0xFFFFFFFF means no active alarm.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The service has succeeded.
   * - E_NOT_OK
     - 

EcuM_SetClock
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EcuM_SetClock(EcuM_UserType user, EcuM_TimeType time)

Sets the EcuM clock time to the provided value. This API is useful for testing the alarm services; Alarms that take days to expire can be tested. This function is part of the ECU Manager Module port interface.

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
     - user
     - The user that wants to set the clock.
   * - [in]
     - time
     - Absolute time in seconds since battery connect.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The service has succeeded.
   * - E_NOT_OK
     - The service failed.

EcuM_SelectBootTarget
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EcuM_SelectBootTarget(EcuM_BootTargetType target)

Selects a boot target. This function is part of the ECU Manager Module port interface.

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
     - target
     - The selected boot target.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The new boot target was accepted by EcuM.
   * - E_NOT_OK
     - The new boot target was not accepted by EcuM.

EcuM_GetBootTarget
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EcuM_GetBootTarget(EcuM_BootTargetType *target)

Returns the current boot target. This function is part of the ECU Manager Module port interface.

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
   * - [out]
     - target
     - The currently selected boot target.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The service always succeeds.

EcuM_SetWakeupEvent
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void EcuM_SetWakeupEvent(EcuM_WakeupSourceType sources)

Sets the wakeup event. Sets (OR-operation) all events passed as a bit set in the

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
     - sources
     - Value to be set.

**Return type**
   void


EcuM_ValidateWakeupEvent
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void EcuM_ValidateWakeupEvent(EcuM_WakeupSourceType sources)

After wakeup, the ECU State Manager will stop the process during the WAKEUP VALIDATION state/sequence to wait for validation of the wakeup event. This API service is used to indicate to the ECU Manager module that the wakeup events indicated in the

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
     - sources
     - Events that have been validated.

**Return type**
   void


EcuM_CheckWakeup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void EcuM_CheckWakeup(EcuM_WakeupSourceType wakeupSource)

This function can be called to check the given wakeup sources. It will pass the argument to the integrator function EcuM_CheckWakeupHook. It can also be called by the ISR of a wakeup source to set up the PLL and check other wakeup sources that may be connected to the same interrupt.

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
   * - 
     - wakeupSource
     - 

**Return type**
   void


EcuM_AL_DriverInitBswM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void EcuM_AL_DriverInitBswM(uint8 drvInitIdx)

This callback shall provide BSW module initializations to be called by the BSW Mode Manager.

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
     - drvInitIdx
     - Index of the driver to initialize.

**Return type**
   void


