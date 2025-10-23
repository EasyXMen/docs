.. include:: CanTrcv_Types_h.rst

CanTrcv模块接口描述 CanTrcv Module Interface Description
-----------------------------------------------------------------------------------------------------------------------------------------------
CanTrcv_Init
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void CanTrcv_Init(const CanTrcv_ConfigType *ConfigPtr)

This function initializes the CanTrcv module.

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
     - ConfigPtr
     - Pointer to selected configuration structure

**Return type**
   void


CanTrcv_SetOpMode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType CanTrcv_SetOpMode(uint8 Transceiver, CanTrcv_TrcvModeType OpMode)

This function sets the mode of the Transceiver to the value OpMode.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant for different transceivers

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - Transceiver
     - CAN transceiver to which API call has to be applied.
   * - [in]
     - OpMode
     - This parameter contains the desired operating mode.

**Return type**
   Std_ReturnType


CanTrcv_GetOpMode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType CanTrcv_GetOpMode(uint8 Transceiver, CanTrcv_TrcvModeType *OpMode)

This function gets the mode of the Transceiver and returns it in OpMode.

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
     - Transceiver
     - CAN transceiver to which API call has to be applied.
   * - [out]
     - OpMode
     - Pointer to operation mode of the bus the API is applied to.

**Return type**
   Std_ReturnType


CanTrcv_GetBusWuReason
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType CanTrcv_GetBusWuReason(uint8 Transceiver, P2VAR(CanTrcv_TrcvWakeupReasonType, AUTOMATIC, CANTRCV_APPL_DATA) reason)

This function gets the wakeup reason for the Transceiver and returns it in parameter Reason.

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
     - Transceiver
     - CAN transceiver to which API call has to be applied.
   * - [out]
     - reason
     - Pointer to wake up reason of the bus the API is applied to.

**Return type**
   Std_ReturnType


CanTrcv_GetVersionInfo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void CanTrcv_GetVersionInfo(Std_VersionInfoType *versioninfo)

This function gets the version of the module and returns it in VersionInfo.

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
     - Pointer to version information of this module.

**Return type**
   void


CanTrcv_SetWakeupMode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType CanTrcv_SetWakeupMode(uint8 Transceiver, CanTrcv_TrcvWakeupModeType TrcvWakeupMode)

This function enables, disables or clears wake-up events of the Transceiver according to TrcvWakeupMode.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant for different transceivers

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - Transceiver
     - CAN transceiver to which API call has to be applied.
   * - [in]
     - TrcvWakeupMode
     - Requested transceiver wakeup reason.

**Return type**
   Std_ReturnType


CanTrcv_MainFunction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void CanTrcv_MainFunction(void)

This is the main function of CanTrcv, which scans all busses for wake up events and perform these event.

**Sync/Async**
   TRUE

**Reentrancy**
   FALSE


**Return type**
   void


CanTrcv_CheckWakeup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType CanTrcv_CheckWakeup(uint8 Transceiver)

This function is called by underlying CANIF in case a wake up interrupt is detected.

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
     - Transceiver
     - CAN transceiver to which API call has to be applied.

**Return type**
   Std_ReturnType


CanTrcv_MainFunctionDiagnostics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void CanTrcv_MainFunctionDiagnostics(void)

This function reads the transceiver diagnostic status periodically and sets product/development accordingly.

**Sync/Async**
   TRUE

**Reentrancy**
   FALSE


**Return type**
   void


CanTrcv_DeInit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void CanTrcv_DeInit(void)

This function de-initializes the CanTrcv module.

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant


**Return type**
   void


CanTrcv_GetTrcvSystemData
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType CanTrcv_GetTrcvSystemData(uint8 Transceiver, uint32 *TrcvSysData)

This function reads the transceiver configuration/status data and returns it through parameter TrcvSysData.

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
     - Transceiver
     - CAN transceiver to which API call has to be applied.
   * - [out]
     - TrcvSysData
     - Configuration/Status data of the transceiver.

**Return type**
   Std_ReturnType


CanTrcv_ClearTrcvWufFlag
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType CanTrcv_ClearTrcvWufFlag(uint8 Transceiver)

This function clears the WUF flag in the transceiver hardware.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant for different transceivers

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - Transceiver
     - CAN transceiver to which API call has to be applied.

**Return type**
   Std_ReturnType


CanTrcv_ReadTrcvTimeoutFlag
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType CanTrcv_ReadTrcvTimeoutFlag(uint8 Transceiver, CanTrcv_TrcvFlagStateType *FlagState)

This function reads the status of the timeout flag from the transceiver hardware.

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
     - Transceiver
     - CAN transceiver to which API call has to be applied.
   * - [out]
     - FlagState
     - State of the timeout flag.

**Return type**
   Std_ReturnType


CanTrcv_ClearTrcvTimeoutFlag
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType CanTrcv_ClearTrcvTimeoutFlag(uint8 Transceiver)

This function clears the status of the timeout flag in the transceiver hardware.

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
     - Transceiver
     - CAN transceiver to which API call has to be applied.

**Return type**
   Std_ReturnType


CanTrcv_ReadTrcvSilenceFlag
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType CanTrcv_ReadTrcvSilenceFlag(uint8 Transceiver, CanTrcv_TrcvFlagStateType *FlagState)

This function reads the status of the silence flag from the transceiver hardware.

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
     - Transceiver
     - CAN transceiver to which API call has to be applied.
   * - [inout]
     - FlagState
     - State of the silence flag.

**Return type**
   Std_ReturnType


CanTrcv_CheckWakeFlag
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType CanTrcv_CheckWakeFlag(uint8 Transceiver)

This function requests to check the status of the wakeup flag from the transceiver hardware.

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
     - Transceiver
     - CAN transceiver to which API call has to be applied.

**Return type**
   Std_ReturnType


CanTrcv_SetPNActivationState
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType CanTrcv_SetPNActivationState(CanTrcv_PNActivationType ActivationState)

This function configures the wake-up of the transceiver for Standby and Sleep Mode.

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
     - ActivationState
     - PN_ENABLED: PN wakeup functionality in CanTrcv shall be enabled, PN_DISABLED: PN wakeup functionality in CanTrcv shall be disabled.+

**Return type**
   Std_ReturnType


