LinIf_Init
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void LinIf_Init(const LinIf_ConfigType *ConfigPtr)

Initializes the LIN Interface.

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
     - Pointer to the LIN Interface configuration

**Return type**
   void


LinIf_GetVersionInfo
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void LinIf_GetVersionInfo(Std_VersionInfoType *versionInfo)

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
     - versionInfo
     - Pointer to where to store the version information of this module.

**Return type**
   LINIF_LOCAL_INLINE void


LinIf_Transmit
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType LinIf_Transmit(PduIdType LinTxPduId, const PduInfoType *PduInfoPtr)

Indicates a request.

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
     - LinTxPduId
     - Upper layer identification of the LIN frame to be transmitted (not the LIN protected ID).
   * - [in]
     - PduInfoPtr
     - This parameter is not used by this call.

**Return type**
   Std_ReturnType


LinIf_ScheduleRequest
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType LinIf_ScheduleRequest(NetworkHandleType Channel, LinIf_SchHandleType Schedule)

Requests a schedule table to be executed.

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
     - Channel
     - Channel index.
   * - [in]
     - Schedule
     - Identification of the new schedule to be set.

**Return type**
   Std_ReturnType


LinIf_GotoSleep
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType LinIf_GotoSleep(NetworkHandleType Channel)

Initiates a transition into the Sleep Mode on the selected channel.

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
     - Channel
     - Identification of the LIN channel.

**Return type**
   Std_ReturnType


LinIf_Wakeup
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType LinIf_Wakeup(NetworkHandleType Channel)

Initiates the wake up process.

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
     - Channel
     - Identification of the LIN channel.

**Return type**
   Std_ReturnType


LinIf_SetTrcvMode
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType LinIf_SetTrcvMode(NetworkHandleType Channel, LinTrcv_TrcvModeType TransceiverMode)

Set the given LIN transceiver to the given mode.

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
     - Channel
     - Identification of the LIN channel.
   * - [in]
     - TransceiverMode
     - Requested mode transition.

**Return type**
   Std_ReturnType


LinIf_GetTrcvMode
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType LinIf_GetTrcvMode(NetworkHandleType Channel, LinTrcv_TrcvModeType *TransceiverModePtr)

Returns the actual state of a LIN Transceiver Driver.

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
     - Channel
     - Identification of the LIN channel.
   * - [out]
     - TransceiverModePtr
     - Pointer to a memory location where output value will be stored.

**Return type**
   Std_ReturnType


LinIf_GetTrcvWakeupReason
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType LinIf_GetTrcvWakeupReason(NetworkHandleType Channel, LinTrcv_TrcvWakeupReasonType *TrcvWuReasonPtr)

Returns the reason for the wake up that has been detected by the LIN Transceiver Driver.

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
     - Channel
     - Identification of the LIN channel.
   * - [out]
     - TrcvWuReasonPtr
     - Pointer to a memory location where output value will be stored.

**Return type**
   Std_ReturnType


LinIf_SetTrcvWakeupMode
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType LinIf_SetTrcvWakeupMode(NetworkHandleType Channel, LinTrcv_TrcvWakeupModeType LinTrcvWakeupMode)

This API enables, disables and clears the notification for wakeup events on the addressed network.

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
     - Channel
     - Identification of the LIN channel.
   * - [in]
     - LinTrcvWakeupMode
     - Requested transceiver wake up reason.

**Return type**
   Std_ReturnType


LinIf_ChannelMainFunction
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void LinIf_ChannelMainFunction(NetworkHandleType ch)

LinIf main function.

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
     - ch
     - Identification of the LIN channel.

**Return type**
   void


LinIf_CheckWakeup
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType LinIf_CheckWakeup(EcuM_WakeupSourceType WakeupSource)

Will be called when the EcuM has been notified about a wakeup on a specific LIN channel.

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
     - WakeupSource
     - Source device, which initiated the wakeup event: LIN controller or LIN transceiver.

**Return type**
   Std_ReturnType


LinIf_GetPIDTable
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType LinIf_GetPIDTable(NetworkHandleType Channel, Lin_FramePidType *PidBuffer, uint8 *PidBufferLength)

Retrieves all assigned PID values.The order is congruent to the LIN frame index.Only applicable for LIN slave nodes.

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
     - Channel
     - Identification of the LIN channel.
   * - [inout]
     - PidBuffer
     - Pointer to existing buffer to which the current assigned PID values are copied to.
   * - [inout]
     - PidBufferLength
     - Pointer to actual length of provided buffer. After successful return,it contains the number of copied PID values

**Return type**
   Std_ReturnType


LinIf_SetPIDTable
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType LinIf_SetPIDTable(NetworkHandleType Channel, Lin_FramePidType *PidBuffer, uint8 PidBufferLength)

Sets all assigned PID values.The order is congruent to the LIN frame index.Only applicable for LIN slave nodes.

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
     - Channel
     - Identification of the LIN channel.
   * - [in]
     - PidBuffer
     - Pointer to buffer which contains the PID values to configure.
   * - [in]
     - PidBufferLength
     - Number of PID values in the provided buffer.

**Return type**
   Std_ReturnType


LinIf_GetConfiguredNAD
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType LinIf_GetConfiguredNAD(NetworkHandleType Channel, uint8 *Nad)

Reports the current configured NAD.Only applicable for LIN slave nodes.

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
     - Channel
     - Identification of the LIN channel.
   * - [out]
     - Nad
     - Configured NAD of slave.

**Return type**
   Std_ReturnType


LinIf_SetConfiguredNAD
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType LinIf_SetConfiguredNAD(NetworkHandleType Channel, uint8 Nad)



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
     - Channel
     - Identification of the LIN channel.
   * - [in]
     - Nad
     - Configured NAD to set as new slave NAD.

**Return type**
   Std_ReturnType


