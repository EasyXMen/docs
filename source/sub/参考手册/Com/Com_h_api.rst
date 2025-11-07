
类型定义(Type Definitions)
-------------------------------
.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Type Name
     - Type
     - Description
	 
   * - Com_StatusType
     - enum
     - Com状态类型(Com status type)

   * - Com_SignalIdType
     - uint16
     - 表示信号的Id号(Indicates the ID number of the signal)

   * - Com_SignalGroupIdType
     - uint16
     - 表示信号组的Id号(Indicates the ID number of the signal group)

   * - Com_IpduGroupIdType
     - uint16
     - 表示IpduGroup的Id号(Indicates the ID number of the IpduGroup)

   * - Com_ConfigType
     - struct
     - 表示Com的PB配置结构体(Indicates the PB configuration structure of Com)


提供的服务(Services)
-----------------------------------
Com_Init
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Com_Init(const Com_ConfigType *config)

This service initializes internal and external interfaces and variables of the AUTOSAR COM module layer for the further processing. After calling this function the inter-ECU communication is still disabled.

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
     - config
     - Pointer to the AUTOSAR COM module’s configuration data.

**Return type**
   void


Com_DeInit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Com_DeInit(void)

This service stops the inter-ECU communication. All started I-PDU groups are stopped and have to be started again, if needed, after Com_Init is called. By a call to Com_DeInit the AUTOSAR COM module is put into an not initialized state.

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant


**Return type**
   void


Com_IpduGroupStart
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Com_IpduGroupStart(Com_IpduGroupIdType IpduGroupId, boolean initialize)

Starts a preconfigured I-PDU group.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant for different I-PDU groups. Non reentrant for the same I-PDU group

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - IpduGroupId
     - Id of I-PDU group to be started
   * - [in]
     - initialize
     - flag to request initialization of the data in the I-PDUs of this I-PDU group

**Return type**
   void


Com_IpduGroupStop
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Com_IpduGroupStop(Com_IpduGroupIdType IpduGroupId)

Stops a preconfigured I-PDU group.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant for different I-PDU groups. Non reentrant for the same I-PDU group

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - IpduGroupId
     - Id of I-PDU group to be stopped

**Return type**
   void


Com_EnableReceptionDM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Com_EnableReceptionDM(Com_IpduGroupIdType IpduGroupId)

Enables the reception deadline monitoring for the I-PDUs within the given IPDU group.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant for different I-PDU groups. Non reentrant for the same I-PDU group

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - IpduGroupId
     - Id of I-PDU group where reception DM shall be enabled.

**Return type**
   void


Com_DisableReceptionDM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Com_DisableReceptionDM(Com_IpduGroupIdType IpduGroupId)

Disables the reception deadline monitoring for the I-PDUs within the given IPDU group.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant for different I-PDU groups. Non reentrant for the same I-PDU group

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - IpduGroupId
     - Id of I-PDU group where reception DM shall be disabled.

**Return type**
   void


Com_GetStatus
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Com_StatusType Com_GetStatus(void)

Returns the status of the AUTOSAR COM module.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant


**Return type**
   Com_StatusType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - COM_UNINIT
     - the AUTOSAR COM module is not initialized and not usable
   * - COM_INIT
     - the AUTOSAR COM module is initialized and usable

Com_GetVersionInfo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Com_GetVersionInfo(Std_VersionInfoType *versioninfo)



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
     - versioninfo
     - Pointer to where to store the version information of this module.

**Return type**
   void


Com_SendSignal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    uint8 Com_SendSignal(Com_SignalIdType SignalId, const void *SignalDataPtr)

The service Com_SendSignal updates the signal(include group signal) object identified by SignalId with the signal referenced by the SignalDataPtr parameter.

**Sync/Async**
   FALSE

**Reentrancy**
   Non Reentrant for the same signal. Reentrant for different signals.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - SignalId
     - Id of signal to be sent.
   * - [in]
     - SignalDataPtr
     - Reference to the signal data to be transmitted.

**Return type**
   uint8

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - service has been accepted
   * - COM_SERVICE_NOT_AVAILABLE
     - corresponding I-PDU group was stopped (or service failed due to development error)
   * - COM_BUSY
     - in case the TP-Buffer is locked for large data types handling

Com_SendDynSignal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    uint8 Com_SendDynSignal(Com_SignalIdType SignalId, const void *SignalDataPtr, uint16 Length)

The service Com_SendDynSignal updates the signal object identified by SignalId with the signal referenced by the SignalDataPtr parameter.

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
     - SignalId
     - Id of signal to be sent.
   * - [in]
     - SignalDataPtr
     - Reference to the signal data to be transmitted.
   * - [in]
     - Length
     - Length of the dynamic length signal

**Return type**
   uint8

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - service has been accepted
   * - E_NOT_OK
     - in case the Length is greater than the configured ComSignalLength of this sent signal
   * - COM_SERVICE_NOT_AVAILABLE
     - corresponding I-PDU group was stopped
   * - COM_BUSY
     - in case the TP-Buffer is locked

Com_ReceiveSignal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    uint8 Com_ReceiveSignal(Com_SignalIdType SignalId, void *SignalDataPtr)

Com_ReceiveSignal copies the data of the signal identified by SignalId to the location specified by SignalDataPtr.

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
     - SignalId
     - Id of signal to be received.
   * - [in]
     - SignalDataPtr
     - Reference to the location where the received signal data shall be stored

**Return type**
   uint8

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - service has been accepted
   * - E_NOT_OK
     - in case the Length is greater than the configured ComSignalLength of this sent signal
   * - COM_SERVICE_NOT_AVAILABLE
     - corresponding I-PDU group was stopped
   * - COM_BUSY
     - in case the TP-Buffer is locked for large data types handling

Com_ReceiveDynSignal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    uint8 Com_ReceiveDynSignal(Com_SignalIdType SignalId, void *SignalDataPtr, uint16 *Length)

Com_ReceiveDynSignal copies the data of the signal identified by SignalId to the location specified by SignalDataPtr and stores the length of the dynamical length signal at the position given by the Length parameter.

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
     - SignalId
     - Id of signal to be received.
   * - [in]
     - SignalDataPtr
     - Reference to the location where the received signal data shall be stored
   * - [inout]
     - Length
     - in: maximum length that could be received;out: length of the dynamic length signal

**Return type**
   uint8

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - service has been accepted
   * - E_NOT_OK
     - in case the Length (as in-parameter) is smaller than the received length of the dynamic length signal
   * - COM_SERVICE_NOT_AVAILABLE
     - corresponding I-PDU group was stopped
   * - COM_BUSY
     - in case the TP-Buffer is locked

Com_SendSignalGroup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    uint8 Com_SendSignalGroup(Com_SignalGroupIdType SignalGroupId)

The service Com_SendSignalGroup copies the content of the associated shadow buffer to the associated I-PDU.

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
     - SignalGroupId
     - Id of signal group to be sent.

**Return type**
   uint8

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - service has been accepted
   * - COM_SERVICE_NOT_AVAILABLE
     - corresponding I-PDU group was stopped (or service failed due to development error)
   * - COM_BUSY
     - in case the TP-Buffer is locked for large data types handling

Com_ReceiveSignalGroup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    uint8 Com_ReceiveSignalGroup(Com_SignalGroupIdType SignalGroupId)

The service Com_ReceiveSignalGroup copies the received signal group from the I-PDU to the shadow buffer.

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
     - SignalGroupId
     - Id of signal group to be received.

**Return type**
   uint8

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - service has been accepted
   * - COM_SERVICE_NOT_AVAILABLE
     - corresponding I-PDU group was stoppedailed due to development error)
   * - COM_BUSY
     - in case the TP-Buffer is locked for large data types handling

Com_SendSignalGroupArray
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    uint8 Com_SendSignalGroupArray(Com_SignalGroupIdType SignalGroupId, const uint8 *SignalGroupArrayPtr)

The service Com_SendSignalGroupArray copies the content of the provided SignalGroupArrayPtr to the associated I-PDU. The provided data shall correspond to the array representation of the signal group.

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
     - SignalGroupId
     - Id of signal group to be sent.
   * - [in]
     - SignalGroupArrayPtr
     - Reference to the signal group array.

**Return type**
   uint8

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - service has been accepted
   * - COM_SERVICE_NOT_AVAILABLE
     - corresponding I-PDU group was stopped
   * - COM_BUSY
     - in case the TP-Buffer is locked for large data types handling

Com_ReceiveSignalGroupArray
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    uint8 Com_ReceiveSignalGroupArray(Com_SignalGroupIdType SignalGroupId, uint8 *SignalGroupArrayPtr)

The service Com_ReceiveSignalGroupArray copies the received signal group array representation from the PDU to the location designated by SignalGroupArrayPtr.

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
     - SignalGroupId
     - Id of signal group to be sent.
   * - [in]
     - SignalGroupArrayPtr
     - Reference to the signal group array.

**Return type**
   uint8

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - service has been accepted
   * - COM_SERVICE_NOT_AVAILABLE
     - corresponding I-PDU group was stopped
   * - COM_BUSY
     - in case the TP-Buffer is locked for large data types handling

Com_InvalidateSignal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    uint8 Com_InvalidateSignal(Com_SignalIdType SignalId)

The service Com_InvalidateSignal invalidates the signal with the given SignalId by setting its value to its configured ComSignalDataInvalidValue.

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
     - SignalId
     - Id of signal to be invalidated.

**Return type**
   uint8

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - service has been accepted
   * - COM_SERVICE_NOT_AVAILABLE
     - corresponding I-PDU group is stopped, no ComSignalDataInvalidValue is configured for the given signalId
   * - COM_BUSY
     - in case the TP-Buffer is locked

Com_InvalidateSignalGroup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    uint8 Com_InvalidateSignalGroup(Com_SignalGroupIdType SignalGroupId)

The service Com_InvalidateSignalGroup invalidates all group signals of the signal group with the given SignalGroupId by setting their values to their configured ComSignalDataInvalidValues.

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
     - SignalGroupId
     - Id of signal group to be invalidated.

**Return type**
   uint8

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - service has been accepted
   * - COM_SERVICE_NOT_AVAILABLE
     - corresponding I-PDU group is stopped, no ComSignalDataInvalidValue is configured for any of the group signals
   * - COM_BUSY
     - in case the TP-Buffer is locked

Com_TriggerIPDUSend
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Com_TriggerIPDUSend(PduIdType PduId)

By a call to Com_TriggerIPDUSend the I-PDU with the given ID is triggered for transmission.

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
     - PduId
     - The I-PDU-ID of the I-PDU that shall be triggered for sending

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - I-PDU was triggered for transmission
   * - E_NOT_OK
     - I-PDU is stopped, the transmission could not be triggered

Com_TriggerIPDUSendWithMetaData
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Com_TriggerIPDUSendWithMetaData(PduIdType PduId, uint8 *MetaData)

By a call to Com_TriggerIPDUSendWithMetaData the AUTOSAR COM module updates its internal metadata for the I-PDU with the given ID by copying the metadata from the given position and with respect to the globally configured metadata length of the I-PDU. Then the I-PDU is triggered for transmission.

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
     - PduId
     - The I-PDU-ID of the I-PDU that shall be triggered for sending
   * - [in]
     - MetaData
     - A pointer to the metadata for the triggered send-request

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - I-PDU was triggered for transmission
   * - E_NOT_OK
     - I-PDU is stopped, the transmission could not be triggered

Com_SwitchIpduTxMode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Com_SwitchIpduTxMode(PduIdType PduId, boolean Mode)

The service Com_SwitchIpduTxMode sets the transmission mode of the I-PDU referenced by PduId to Mode. In case the transmission mode changes, the new mode shall immediately be effective. In case the requested transmission mode was already active for this I-PDU, the call will have no effect.

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
     - PduId
     - Id of the I-PDU of which the transmission mode shall be changed.
   * - [in]
     - Mode
     - the transmission mode that shall be set.

**Return type**
   void


Com_MainFunctionRx
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Com_MainFunctionRx(Com_MainFunctionIdType RxMainFunctionId)

This function performs the processing of the AUTOSAR COM module's receive processing that are not directly handled within the COM's functions invoked by the PDU-R, for example Com_RxIndication.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant for different instances. Non reentrant for the same instance.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - RxMainFunctionId
     - MainfunctionId for Rx.

**Return type**
   void


Com_MainFunctionTx
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Com_MainFunctionTx(Com_MainFunctionIdType TxMainFunctionId)

This function performs the processing of the AUTOSAR COM module's transmission activities that are not directly handled within the COM's function invoked by the RTE, for example Com_SendSignal.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant for different instances. Non reentrant for the same instance.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - TxMainFunctionId
     - MainfunctionId for Tx.

**Return type**
   void


Com_MainFunctionRouteSignals
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Com_MainFunctionRouteSignals(Com_MainFunctionIdType RouteSignalsMainFunctionId)

Calls the signal gateway part of the AUTOSAR COM module to forward received signals to be routed.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant for different instances. Non reentrant for the same instance.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - RouteSignalsMainFunctionId
     - MainfunctionId for RouteSignals.

**Return type**
   void


