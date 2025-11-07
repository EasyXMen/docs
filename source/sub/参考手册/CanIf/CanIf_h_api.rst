
类型定义(Type Definition)
-----------------------------------
.. 如果没有就不存在该章节，或为None

None

      
提供的服务(Services)
--------------------------------
CanIf_Init
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void CanIf_Init(const CanIf_ConfigType *ConfigPtr)

This service Initializes internal and external interfaces of the CAN Interface for the further processing.

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
     - Pointer to configuration parameter set, used e.g. for post build parameters.

**Return type**
   void


CanIf_DeInit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void CanIf_DeInit(void)

De-initializes the CanIf module.

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant


**Return type**
   void


CanIf_SetControllerMode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType CanIf_SetControllerMode(uint8 ControllerId, Can_ControllerStateType ControllerMode)

This service calls the corresponding CAN Driver service for changing of the CAN controller mode.

**Sync/Async**
   FALSE

**Reentrancy**
   Reentrant (Not for the same controller)

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - ControllerId
     - Abstracted CanIf ControllerId which is assigned to a CAN controller, which is requested for mode transition.
   * - [in]
     - ControllerMode
     - Requested mode transition.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Controller mode request has been accepted.
   * - E_NOT_OK
     - Controller mode request has not been accepted.

CanIf_GetControllerMode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType CanIf_GetControllerMode(uint8 ControllerId, Can_ControllerStateType *ControllerModePtr)

This service calls the corresponding CAN Driver service for obtaining the current status of the CAN controller.

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
     - ControllerId
     - Abstracted CanIf ControllerId which is assigned to a CAN controller, which is requested for current operation mode.
   * - [out]
     - ControllerModePtr
     - Pointer to a memory location, where the current mode of the CAN controller will be stored.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Controller mode request has been accepted.
   * - E_NOT_OK
     - Controller mode request has not been accepted.

CanIf_Transmit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType CanIf_Transmit(PduIdType TxPduId, const PduInfoType *PduInfoPtr)

Requests transmission of a PDU.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant for different PduIds. Non reentrant for the same PduId.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - TxPduId
     - Identifier of the PDU to be transmitted.
   * - [in]
     - PduInfoPtr
     - Length of and pointer to the PDU data and pointer to MetaData.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Transmit request has been accepted.
   * - E_NOT_OK
     - Transmit request has not been accepted.

CanIf_ReadRxPduData
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType CanIf_ReadRxPduData(PduIdType CanIfRxSduId, PduInfoType *CanIfRxInfoPtr)

This service provides the Data Length and the received data of the requested CanIfRxSduId to the calling upper layer.

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
     - CanIfRxSduId
     - Receive L-SDU handle specifying the corresponding CAN L-SDU ID and implicitly the CAN Driver instance as well as the corresponding CAN controller device.
   * - [out]
     - CanIfRxInfoPtr
     - Contains the length (SduLength) of the received PDU, a pointer to a buffer (SduDataPtr) containing the PDU, and the MetaData related to this PDU.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request for L-SDU data has been accepted.
   * - E_NOT_OK
     - No valid data has been received.

CanIf_ReadTxNotifStatus
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    CanIf_NotifStatusType CanIf_ReadTxNotifStatus(PduIdType CanIfTxSduId)

This service returns the confirmation status (confirmation occurred or not) of a specific static or dynamic CAN Tx L-PDU, requested by the CanIfTxSduId.

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
     - CanIfTxSduId
     - L-SDU handle to be transmitted. This handle specifies the corresponding CAN L-SDU ID and implicitly the CAN Driver instance as well as the corresponding CAN controller device.

**Return type**
    CanIf_NotifStatusType


CanIf_ReadRxNotifStatus
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    CanIf_NotifStatusType CanIf_ReadRxNotifStatus(PduIdType CanIfRxSduId)

This service returns the indication status (indication occurred or not) of a specific CAN Rx L-PDU, requested by the CanIfRxSduId.

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
     - CanIfRxSduId
     - Receive L-SDU handle specifying the corresponding CAN L-SDU ID and implicitly the CAN Driver instance as well as the corresponding CAN controller device.

**Return type**
    CanIf_NotifStatusType


CanIf_SetPduMode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType CanIf_SetPduMode(uint8 ControllerId, CanIf_PduModeType PduModeRequest)

This service sets the requested mode at the L-PDUs of a predefined logical PDU channel.

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
     - ControllerId
     - All PDUs of the own ECU connected to the corresponding CanIf ControllerId, which is assigned to a physical CAN controller are addressed.
   * - [in]
     - PduModeRequest
     - Requested PDU mode change.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request for mode transition has been accepted.
   * - E_NOT_OK
     - Request for mode transition has not been accepted.

CanIf_GetPduMode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType CanIf_GetPduMode(uint8 ControllerId, CanIf_PduModeType *PduModePtr)

This service reports the current mode of a requested PDU channel.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant (Not for the same channel)

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - ControllerId
     - All PDUs of the own ECU connected to the corresponding CanIf ControllerId, which is assigned to a physical CAN controller are addressed.
   * - [out]
     - PduModePtr
     - Pointer to a memory location, where the current mode of the logical PDU channel will be stored.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - PDU mode request has been accepted.
   * - E_NOT_OK
     - PDU mode request has not been accepted.

CanIf_GetVersionInfo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void CanIf_GetVersionInfo(Std_VersionInfoType *VersionInfo)

This service returns the version information of the called CAN Interface module.

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
     - VersionInfo
     - Pointer to where to store the version information of this module.

**Return type**
   void


CanIf_SetDynamicTxId
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void CanIf_SetDynamicTxId(PduIdType CanIfTxSduId, Can_IdType CanId)

This service reconfigures the corresponding CAN identifier of the requested CAN L-PDU.

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
     - CanIfTxSduId
     - L-SDU handle to be transmitted. This handle specifies the corresponding CAN L-SDU ID and implicitly the CAN Driver instance as well as the corresponding CAN controller device.
   * - [in]
     - CanId
     - Standard/Extended CAN ID of CAN L-SDU that shall be transmitted as FD or conventional CAN frame.

**Return type**
   void


CanIf_SetTrcvMode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType CanIf_SetTrcvMode(uint8 TransceiverId, CanTrcv_TrcvModeType TransceiverMode)

This service changes the operation mode of the tansceiver TransceiverId, via calling the corresponding CAN Transceiver Driver service.

**Sync/Async**
   FALSE

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
     - TransceiverId
     - Abstracted CanIf TransceiverId, which is assigned to a CAN transceiver, which is requested for mode transition
   * - [in]
     - TransceiverMode
     - Requested mode transition.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Transceiver mode request has been accepted.
   * - E_NOT_OK
     - Transceiver mode request has not been accepted.

CanIf_GetTrcvMode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType CanIf_GetTrcvMode(uint8 TransceiverId, CanTrcv_TrcvModeType *TransceiverModePtr)

This function invokes CanTrcv_GetOpMode and updates the parameter TransceiverModePtr with the value OpMode provided by CanTrcv.

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
     - TransceiverId
     - Abstracted CanIf TransceiverId, which is assigned to a CAN transceiver, which is requested for current operation mode.
   * - [out]
     - TransceiverModePtr
     - Requested mode of requested network the Transceiver is connected to.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Transceiver mode request has been accepted.
   * - E_NOT_OK
     - Transceiver mode request has not been accepted.

CanIf_GetTrcvWakeupReason
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType CanIf_GetTrcvWakeupReason(uint8 TransceiverId, CanTrcv_TrcvWakeupReasonType *TrcvWuReasonPtr)

This service returns the reason for the wake up of the transceiver TransceiverId, via calling the corresponding CAN Transceiver Driver service.

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
     - TransceiverId
     - Abstracted CanIf TransceiverId, which is assigned to a CAN transceiver, which is requested for wake up reason.
   * - [out]
     - TrcvWuReasonPtr
     - Provided pointer to where the requested transceiver wake up reason shall be returned.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Transceiver wake up reason request has been accepted.
   * - E_NOT_OK
     - Transceiver wake up reason request has not been accepted.

CanIf_SetTrcvWakeupMode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType CanIf_SetTrcvWakeupMode(uint8 TransceiverId, CanTrcv_TrcvWakeupModeType TrcvWakeupMode)

This function shall call CanTrcv_SetTrcvWakeupMode.

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
     - TransceiverId
     - Abstracted CanIf TransceiverId, which is assigned to a CAN transceiver, which is requested for wake up notification mode transition.
   * - [in]
     - TrcvWakeupMode
     - Requested transceiver wake up notification mode.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Will be returned, if the wake up notifications state has been changed to the requested mode.
   * - E_NOT_OK
     - Will be returned, if the wake up notifications state change has failed or the parameter is out of the allowed range. The previous state has not been changed.

CanIf_CheckWakeup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType CanIf_CheckWakeup(EcuM_WakeupSourceType WakeupSource)

This service checks, whether an underlying CAN driver or a CAN transceiver driver already signals a wakeup event.

**Sync/Async**
   FALSE

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
     - Source device, which initiated the wake up event: CAN controller or CAN transceiver.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Will be returned, if the check wake up request has been accepted.
   * - E_NOT_OK
     - Will be returned, if the check wake up request has not been accepted.

CanIf_CheckValidation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType CanIf_CheckValidation(EcuM_WakeupSourceType WakeupSource)

This service is performed to validate a previous wakeup event.

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
     - Source device which initiated the wake-up event and which has to be validated: CAN controller or CAN transceiver

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Will be returned, if the check validation request has been accepted.
   * - E_NOT_OK
     - Will be returned, if the check validation request has not been accepted.

CanIf_GetTxConfirmationState
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    CanIf_NotifStatusType CanIf_GetTxConfirmationState(uint8 ControllerId)

This service reports, if any TX confirmation has been done for the whole CAN controller since the last CAN controller start.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant (Not for the same controller)

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - ControllerId
     - Abstracted CanIf ControllerId which is assigned to a CAN controller.

**Return type**
    CanIf_NotifStatusType


CanIf_ClearTrcvWufFlag
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType CanIf_ClearTrcvWufFlag(uint8 TransceiverId)

Requests the CanIf module to clear the WUF flag of the designated CAN transceiver.

**Sync/Async**
   FALSE

**Reentrancy**
   Reentrant for different CAN transceivers

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - TransceiverId
     - Abstract CanIf TransceiverId, which is assigned to the designated CAN transceiver.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request has been accepted.
   * - E_NOT_OK
     - Request has not been accepted.

CanIf_CheckTrcvWakeFlag
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType CanIf_CheckTrcvWakeFlag(uint8 TransceiverId)

Requests the CanIf module to check the Wake flag of the designated CAN transceiver.

**Sync/Async**
   FALSE

**Reentrancy**
   Reentrant for different CAN transceivers

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - TransceiverId
     - Abstract CanIf TransceiverId, which is assigned to the designated CAN transceiver.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request has been acceptedl
   * - E_NOT_OK
     - Request has not been accepted.

CanIf_SetBaudrate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType CanIf_SetBaudrate(uint8 ControllerId, uint16 BaudRateConfigID)

This service shall set the baud rate configuration of the CAN controller. Depending on necessary baud rate modifications the controller might have to reset.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant for different ControllerIds. Non reentrant for the same ControllerId.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - ControllerId
     - Abstract CanIf ControllerId which is assigned to a CAN controller, whose baud rate shall be set.
   * - [in]
     - BaudRateConfigID
     - References a baud rate configuration by ID.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Service request accepted, setting of (new) baud rate started.
   * - E_NOT_OK
     - Service request not accepted.

CanIf_ConfirmPnAvailability
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void CanIf_ConfirmPnAvailability(uint8 TransceiverId)

This service indicates that the transceiver is running in PN communication mode referring to the corresponding CAN transceiver with the abstract CanIf TransceiverId.

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
     - TransceiverId
     - Abstract CanIf TransceiverId, which is assigned to a CAN transceiver, which was checked for PN availability.

**Return type**
    void


CanIf_ClearTrcvWufFlagIndication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void CanIf_ClearTrcvWufFlagIndication(uint8 TransceiverId)

This service indicates that the transceiver has cleared the WufFlag referring to the corresponding CAN transceiver with the abstract CanIf TransceiverId.

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
     - TransceiverId
     - Abstract CanIf TransceiverId, which is assigned to a CAN transceiver, for which this function was called.

**Return type**
   void


CanIf_CheckTrcvWakeFlagIndication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void CanIf_CheckTrcvWakeFlagIndication(uint8 TransceiverId)

This service indicates that the check of the transceiver’s wake-up flag has been finished by the corresponding CAN transceiver with the abstract CanIf TransceiverId. This indication is used to cope with the asynchronous transceiver communication.

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
     - TransceiverId
     - Abstract CanIf TransceiverId, which is assigned to a CAN transceiver, for which this function was called.

**Return type**
   void


CanIf_TrcvModeIndication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void CanIf_TrcvModeIndication(uint8 TransceiverId, CanTrcv_TrcvModeType TransceiverMode)

This service indicates a transceiver state transition referring to the corresponding CAN transceiver with the abstract CanIf TransceiverId.

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
     - TransceiverId
     - Abstract CanIf TransceiverId, which is assigned to a CAN transceiver, which state has been transitioned.
   * - [in]
     - TransceiverMode
     - Mode to which the CAN transceiver transitioned.

**Return type**
   void

CanIf_TriggerTransmit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType CanIf_TriggerTransmit(PduIdType TxPduId, PduInfoType *PduInfoPtr)

Within this API, the upper layer module (called module) shall check whether the available data fits into the buffer size reported by PduInfoPtr->SduLength. If it fits, it shall copy its data into the buffer provided by PduInfoPtr->SduDataPtr and update the length of the actual copied data in PduInfoPtr->SduLength. If not, it returns E_NOT_OK without changing PduInfoPtr.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant for different PduIds. Non reentrant for the same PduId.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - TxPduId
     - ID of the SDU that is requested to be transmitted.
   * - [inout]
     - PduInfoPtr
     - Contains a pointer to a buffer (SduDataPtr) to where the SDU data shall be copied, and the available buffer size in SduLength. On return, the service will indicate the length of the copied SDU data in SduLength.

**Return type**
    Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - SDU has been copied and SduLength indicates the number of copied bytes.
   * - E_NOT_OK
     - No SDU data has been copied. PduInfoPtr must not be used since it may contain a NULL pointer or point to invalid data.

CanIf_TxConfirmation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void CanIf_TxConfirmation(PduIdType CanTxPduId)

This service confirms a previously successfully processed transmission of a CAN TxPDU.

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
     - CanTxPduId
     - L-PDU handle of CAN L-PDU successfully transmitted.

**Return type**
   void


CanIf_RxIndication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void CanIf_RxIndication(const Can_HwType *Mailbox, const PduInfoType *PduInfoPtr)

This service indicates a successful reception of a received CAN Rx L-PDU to the CanIf after passing all filters and validation checks.

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
     - Mailbox
     - Identifies the HRH and its corresponding CAN Controller.
   * - [in]
     - PduInfoPtr
     - Pointer to the received L-PDU.

**Return type**
   void


CanIf_ControllerBusOff
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void CanIf_ControllerBusOff(uint8 ControllerId)

This service indicates a Controller BusOff event referring to the corresponding CAN Controller with the abstract CanIf ControllerId.

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
     - ControllerId
     - Abstract CanIf ControllerId which is assigned to a CAN controller, where a BusOff occured.

**Return type**
   void


CanIf_ControllerModeIndication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void CanIf_ControllerModeIndication(uint8 ControllerId, Can_ControllerStateType ControllerMode)

This service indicates a controller state transition referring to the corresponding CAN controller with the abstract CanIf ControllerId.

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
     - ControllerId
     - Abstract CanIf ControllerId which is assigned to a CAN controller, which state has been transitioned.
   * - [in]
     - ControllerMode
     - Mode to which the CAN controller transitioned.

**Return type**
   void

