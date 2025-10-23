类型定义（Type definition）
---------------------------
.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Type Name
     - Type
     - Description
   * - ComM_InitStatusType
     - enum
     - Initialization status of ComM
   * - ComM_StateType
     - enum
     - State and sub-state of ComM state machine
   * - ComM_PncModeType
     - enum
     - Current mode of a PNC
   * - ComM_ConfigType
     - struct
     - This type contains the implementation-specific post build configuration structure
   * - ComM_InhibitionType
     - struct
     - Communication inhibition status and counter


提供的服务（Provided services）
-------------------------------------------
ComM_Init
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void ComM_Init(const ComM_ConfigType *ConfigPtr)

Initializes the AUTOSAR Communication Manager and restarts the internal state machines.

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant (Reentrant for different partitions. Non reentrant for the same partition.)

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - ConfigPtr
     - Pointer to post-build configuration data

**Return type**
   void


ComM_DeInit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void ComM_DeInit(void)

This API de-initializes the AUTOSAR Communication Manager.

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant (Reentrant for different partitions. Non reentrant for the same partition.)


**Return type**
   void


ComM_GetStatus
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType ComM_GetStatus(ComM_InitStatusType *Status)

Returns the initialization status of the AUTOSAR Communication Manager.

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant (Reentrant for different partitions. Non reentrant for the same partition.)

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [out]
     - Status
     - COMM_UNINIT: The ComM is not initialized or not usable. Default value after startup or after

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Successfully return of initialization status
   * - E_NOT_OK
     - Return of initialization status failed

ComM_GetVersionInfo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void ComM_GetVersionInfo(Std_VersionInfoType *Versioninfo)

This function returns the version information of this module.

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
     - Versioninfo
     - See Std_VersionInfoType

**Return type**
   void


ComM_RequestComMode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType ComM_RequestComMode(ComM_UserHandleType User, ComM_ModeType ComMode)

Requesting of a Communication Mode by a user.

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
     - User
     - Handle of the user who requests a mode
   * - [in]
     - ComMode
     - COMM_FULL_COMMUNICATION COMM_NO_COMMUNICATION

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Successfully changed to the new mode
   * - E_NOT_OK
     - Changing to the new mode failed
   * - COMM_E_MODE_LIMITATION
     - Mode can not be granted because of mode inhibition.

ComM_GetMaxComMode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType ComM_GetMaxComMode(ComM_UserHandleType User, ComM_ModeType *ComMode)

Function to query the maximum allowed Communication Mode of the corresponding user.

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
     - User
     - Handle of the user who requests a mode
   * - [out]
     - ComMode
     - See ComM_ModeType

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Successfully returned maximum allowed Communication Mode
   * - E_NOT_OK
     - Return of maximum allowed Communication Mode failed

ComM_GetRequestedComMode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType ComM_GetRequestedComMode(ComM_UserHandleType User, ComM_ModeType *ComMode)

Function to query the currently requested Communication Mode of the corresponding user.

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
     - User
     - Handle of the user who requests a mode
   * - [out]
     - ComMode
     - Name of the requested mode

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Successfully returned requested Communication Mode
   * - E_NOT_OK
     - Return of requested Communication Mode failed

ComM_GetCurrentComMode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType ComM_GetCurrentComMode(ComM_UserHandleType User, ComM_ModeType *ComMode)

Function to query the current Communication Mode. ComM shall use the corresponding interfaces of the Bus State Managers to get the current Communication Mode of the network.

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
     - User
     - Handle of the user who requests a mode
   * - [out]
     - ComMode
     - See ComM_ModeType

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Successfully returned Communication Mode from Bus State Manager
   * - E_NOT_OK
     - Return of Communication Mode from Bus State Manager failed

ComM_GetCurrentPNCComMode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType ComM_GetCurrentPNCComMode(ComM_UserHandleType User, ComM_ModeType *ComMode)

The function returns the current Communication Mode of the corresponding PNC the affected user is assigned to.

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
     - User
     - Handle of the user who requests a mode
   * - [out]
     - ComMode
     - See ComM_ModeType

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Successfully returned the state of the PNC referenced by the given ComMUser
   * - E_NOT_OK
     - Return of the PNC state referenced by the given ComMUser failed
   * - COMM_E_MULTIPLE_PNC_ASSIGNED
     - Function could not provide the current mode of the PNC, since multiple PNCs are assigned to the affected user
   * - COMM_E_NO_PNC_ASSIGNED
     - Function could not provide the current mode of the PNC, since no PNC is assigned to the affected user

ComM_PreventWakeUp
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType ComM_PreventWakeUp(NetworkHandleType Channel, boolean Status)

Changes the inhibition status COMM_NO_WAKEUP for the corresponding channel.

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
     - Channel
     - See NetworkHandleType
   * - [in]
     - Status
     - FALSE: Wake up inhibition is switched off TRUE: Wake up inhibition is switched on

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Successfully changed wake up status for the channel
   * - E_NOT_OK
     - Change of wake up status for the channel failed, e.g. ComMEcuGroupClassification disables the functionality (see ECUC_ComM_00563)

ComM_LimitChannelToNoComMode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType ComM_LimitChannelToNoComMode(NetworkHandleType Channel, boolean Status)

Changes the inhibition status for the channel for changing from COMM_NO_COMMUNICATION to a higher Communication Mode. (See also ComM_LimitECUToNoComMode, same functionality but for all channels)

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
     - Channel
     - See NetworkHandleType
   * - [in]
     - Status
     - FALSE: Limit channel to COMM_NO_COMMUNICATION disabled. TRUE: Limit channel to COMM_NO_COMMUNICATION

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Successfully changed inhibition status for the channel
   * - E_NOT_OK
     - Change of inhibition status for the channel failed, e.g. ComMEcuGroupClassification disables the functionality (see ECUC_ComM_00563)

ComM_LimitECUToNoComMode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType ComM_LimitECUToNoComMode(boolean Status)

Changes the inhibition status for the ECU (=all channels) for changing from COMM_NO_COMMUNICATION to a higher Communication Mode. (See also ComM_LimitChannelToNo ComMode, same functionality but for a specific channels)

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
     - Status
     - FALSE: Limit ECU to COMM_NO_COMMUNICATION disabled TRUE: Limit ECU to COMM_NO_COMMUNICATION enabled

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Successfully changed inhibition status for the ECU
   * - E_NOT_OK
     - Change of inhibition status for the ECU failed, e.g. ComMEcuGroupClassification disables the functionality (see ECUC_ComM_00563)

ComM_GetInhibitionStatus
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType ComM_GetInhibitionStatus(NetworkHandleType Channel, ComM_InhibitionStatusType *Status)

Returns the inhibition status of a ComM channel.

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
     - Channel
     - See NetworkHandleType
   * - [out]
     - Status
     - See ComM_InhibitionStatusType

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Successfully returned Inhibition Status
   * - E_NOT_OK
     - Return of Inhibition Status failed

ComM_ReadInhibitCounter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType ComM_ReadInhibitCounter(uint16 *CounterValue)

This function returns the amount of rejected COMM_FULL_COMMUNICATION user requests.

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
     - CounterValue
     - Amount of rejected COMM_FULL_COMMUNICATION user requests

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Successfully returned Inhibition Counter
   * - E_NOT_OK
     - Return of Inhibition Counter failed

ComM_ResetInhibitCounter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType ComM_ResetInhibitCounter(void)

This function resets the Inhibited COMM_FULL_COMMUNICATION request Counter.

**Sync/Async**
   Synchronous

**Reentrancy**
   Non Reentrant


**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Successfully reset of Inhibit COMM_FULL_COMMUNICATION Counter
   * - E_NOT_OK
     - Reset of Inhibit COMM_FULL_COMMUNICATION Counter failed

ComM_SetECUGroupClassification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType ComM_SetECUGroupClassification(ComM_InhibitionStatusType Status)

Changes the ECU Group Classification status.

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
     - Status
     - See ComM_InhibitionStatusType

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Successfully change the ECU Group Classification Status
   * - E_NOT_OK
     - Change of the ECU Group Classification Status failed

ComM_BusSM_ModeIndication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void ComM_BusSM_ModeIndication(NetworkHandleType Channel, ComM_ModeType ComMode)

Indication of the actual bus mode by the corresponding Bus State Manager. ComM shall propagate the indicated state to the users with means of the RTE and BswM.

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
     - Channel
     - See NetworkHandleType
   * - [in]
     - ComMode
     - See ComM_ModeType

**Return type**
   void
