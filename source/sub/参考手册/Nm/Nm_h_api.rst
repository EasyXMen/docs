
类型定义（Type definition）
-------------------------------------------
.. 如果没有就不存在该章节，或为None

.. list-table:: 
   :widths: 15 5 20
   :header-rows: 1

   * - Type Name
     - Type
     - Description

   * - Nm_ChannelIndexType
     - uint8
     - the type used to indicate the index of channel.

  
   * - Nm_FuncCycTimeType
     - uint16
     - the type used to indicate the period of mainfunction.

   * - Nm_ShutDownTimeType
     - uint16
     - the type used to indicate the time of shutdown timer.

   * - Nm_ConfigType
     - struct
     - post-build configuration parameter type definitions.

   * - Nm_ModeType
     - enum
     - Operational modes of the network management.

   * - Nm_StateType
     - enum
     - States of the network management state machine.

      
提供的服务（ Provided service）
-----------------------------------------------------------
Nm_Init
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Nm_Init(const Nm_ConfigType *configPtr)

This function initializes the NM.

**Sync/Async**
   Asynchronous

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
     - configPtr
     - Identification of the NM-channel

**Return type**
   void

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - No error
   * - E_NOT_OK
     - Passive startup of network management has failed

Nm_PassiveStartUp
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Nm_PassiveStartUp(NetworkHandleType networkHandle)

This function calls the BusNm PassiveStartUp function.

**Sync/Async**
   Asynchronous

**Reentrancy**
   Reentrant (Non-reentrant for the same networkHandle, reentrant otherwise)

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - networkHandle
     - Identification of the NM channel

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - No error
   * - E_NOT_OK
     - Passive startup of network management has failed

Nm_NetworkRequest
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Nm_NetworkRequest(NetworkHandleType networkHandle)

This function calls the <BusNm>_NetworkRequest function.

**Sync/Async**
   Asynchronous

**Reentrancy**
   Reentrant (Non-reentrant for the same NetworkHandle, reentrant otherwise)

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - networkHandle
     - Identification of the NM-channel

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - No error
   * - E_NOT_OK
     - Requesting of bus communication has failed

Nm_NetworkRelease
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Nm_NetworkRelease(NetworkHandleType networkHandle)

This function calls the <BusNm>_NetworkRelease function.

**Sync/Async**
   Asynchronous

**Reentrancy**
   Reentrant (Non-reentrant for the same networkHandle, reentrant otherwise)

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - networkHandle
     - Identification of the NM-channel

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - No error
   * - E_NOT_OK
     - Releasing of bus communication has failed

Nm_DisableCommunication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Nm_DisableCommunication(NetworkHandleType networkHandle)

disables the NM PDU transmission ability.

**Sync/Async**
   Asynchronous

**Reentrancy**
   Reentrant (Non-reentrant for the same NetworkHandle, reentrant otherwise)

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - networkHandle
     - Identification of the NM-channel

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - No error
   * - E_NOT_OK
     - Disabling of NM PDU transmission ability has

Nm_EnableCommunication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Nm_EnableCommunication(NetworkHandleType networkHandle)

Enables the NM PDU transmission ability.

**Sync/Async**
   Asynchronous

**Reentrancy**
   Reentrant (Non-reentrant for the same networkHandle, reentrant otherwise)

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - networkHandle
     - Identification of the NM-channel

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - No error
   * - E_NOT_OK
     - Enabling of NM PDU transmission ability has

Nm_SetUserData
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Nm_SetUserData(NetworkHandleType networkHandle, const uint8 *nmUserDataPtr)

Set user data for NM messages transmitted next on the bus.

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
     - networkHandle
     - Identification of the NM-channel
   * - [in]
     - nmUserDataPtr
     - User data for the next transmitted NM message

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - No error
   * - E_NOT_OK
     - Setting of user data has failed

Nm_GetUserData
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Nm_GetUserData(NetworkHandleType networkHandle, uint8 *nmUserDataPtr)

Get user data out of the last successfully received NM message.

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant (Non-reentrant for the same networkHandle, reentrant otherwise)

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - networkHandle
     - Identification of the NM-channel
   * - [out]
     - nmUserDataPtr
     - User data for the next transmitted NM message

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - No error
   * - E_NOT_OK
     - Getting of user data has failed

Nm_GetPduData
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Nm_GetPduData(NetworkHandleType networkHandle, uint8 *nmPduData)

Get the whole PDU data out of the most recently received NM message. For that purpose <BusNm>_GetPduData shall be called in case NmBusType is not set to NM_BUSNM_LOCALNM. (e.g. CanNm_GetPduData function is called if channel is configured as CAN).

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant (Non-reentrant for the same NetworkHandle, reentrant otherwise)

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - networkHandle
     - Identification of the NM-channel
   * - [out]
     - nmPduData
     - Pointer where NM PDU shall be copied to.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - No error
   * - E_NOT_OK
     - Getting of NM PDU data has failed NetworkHandle does not exist (development only) Module not yet initialized (development only)

Nm_RepeatMessageRequest
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Nm_RepeatMessageRequest(NetworkHandleType networkHandle)

Set Repeat Message Request Bit for NM messages transmitted next on the bus. For that purpose <Bus>Nm_RepeatMessageRequest shall be called in case NmBusType is not set to NM_BUSNM_LOCALNM. (e.g. CanNm_RepeatMessageRequest function is called if channel is configured as CAN). This will force all nodes on the bus to transmit NM messages so that they can be identified.

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant (Non-reentrant for the same networkHandle, reentrant otherwise)

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - networkHandle
     - Identification of the NM-channel

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - No error
   * - E_NOT_OK
     - Setting of Repeat Message Request Bit has failed networkHandle does not exist (development only) Module not yet initialized (development only)

Nm_GetNodeIdentifier
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Nm_GetNodeIdentifier(NetworkHandleType networkHandle, uint8 *nmNodeIdPtr)

Get node identifier out of the last successfully received NM-message. The function <Bus>Nm_GetNodeIdentifier shall be called in case NmBusType is not set to NM_BUSNM_LOCALNM. (e.g. CanNm_GetNodeIdentifier function is called if channel is configured as CAN).

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant (Non-reentrant for the same NetworkHandle, reentrant otherwise)

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - networkHandle
     - Identification of the NM-channel
   * - [out]
     - nmNodeIdPtr
     - Pointer where node identifier out of the last successfully received NM-message shall be

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - No error
   * - E_NOT_OK
     - Getting of the node identifier out of the last received NM-message has failed NetworkHandle does not exist (development only) Module not yet initialized (development only)

Nm_GetLocalNodeIdentifier
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Nm_GetLocalNodeIdentifier(NetworkHandleType networkHandle, uint8 *nmNodeIdPtr)

Get node identifier configured for the local node. For that purpose <Bus>Nm_GetLocalNodeIdentifier shall be called in case NmBusType is not set to NM_BUSNM_LOCALNM. (e.g. CanNm_GetLocalNodeIdentifier function is called if channel is configured as CAN).

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant (Non-reentrant for the same NetworkHandle, reentrant otherwise)

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - networkHandle
     - Identification of the NM-channel
   * - [out]
     - nmNodeIdPtr
     - Pointer where node identifier out of the last successfully received NM-message shall be copied to

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - No error
   * - E_NOT_OK
     - Getting of the node identifier of the local node has failed NetworkHandle does not exist (development only) Module not yet initialized (development only)

Nm_CheckRemoteSleepIndication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Nm_CheckRemoteSleepIndication(NetworkHandleType networkHandle, boolean *remoteSleepIndPtr)

Check if remote sleep indication takes place or not.

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant (Non-reentrant for the same networkHandle, reentrant otherwise)

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - networkHandle
     - Identification of the NM-channel
   * - [out]
     - remoteSleepIndPtr
     - Pointer where check result of remote

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - No error
   * - E_NOT_OK
     - Checking of remote sleep indication bits has failed

Nm_GetState
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Nm_GetState(NetworkHandleType nmNetworkHandle, Nm_StateType *nmStatePtr, Nm_ModeType *nmModePtr)

Returns the state of the network management. The function <Bus>Nm_GetState shall be called in case NmBusType is not set to NM_BUSNM_LOCALNM. (e.g. CanNm_GetState function is called if channel is configured as CAN).

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant (Non-reentrant for the same NetworkHandle, reentrant otherwise)

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - nmNetworkHandle
     - Identification of the NM-channel
   * - [out]
     - nmStatePtr
     - Pointer where state of the network management
   * - [out]
     - nmModePtr
     - Pointer to the location where the mode of the network management shall be copied to

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - No error
   * - E_NOT_OK
     - Getting of NM state has failed NetworkHandle does not exist (development only) Module not yet initialized (development only)

Nm_GetVersionInfo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Nm_GetVersionInfo(Std_VersionInfoType *nmVerInfoPtr)

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
     - nmVerInfoPtr
     - Pointer to where to store the version information

**Return type**
   void


Nm_NetworkStartIndication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Nm_NetworkStartIndication(NetworkHandleType nmNetworkHandle)

Notification that a NM-message has been received in the Bus-Sleep Mode, what indicates that some nodes in the network have already entered the Network Mode.

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
     - nmNetworkHandle
     - Identification of the NM-channel

**Return type**
   void


Nm_NetworkMode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Nm_NetworkMode(NetworkHandleType nmNetworkHandle)

Notification that the network management has entered Network Mode.

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
     - nmNetworkHandle
     - Identification of the NM-channel

**Return type**
   void


Nm_BusSleepMode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Nm_BusSleepMode(NetworkHandleType nmNetworkHandle)

Notification that the network management has entered Bus-Sleep Mode.

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
     - nmNetworkHandle
     - Identification of the NM-channel

**Return type**
   void


Nm_PrepareBusSleepMode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Nm_PrepareBusSleepMode(NetworkHandleType nmNetworkHandle)

Notification that the network management has entered Prepare Bus-Sleep Mode.

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
     - nmNetworkHandle
     - Identification of the NM-channel

**Return type**
   void


Nm_RemoteSleepIndication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Nm_RemoteSleepIndication(NetworkHandleType nmNetworkHandle)

Notification that the network management has detected that all other nodes on the network are ready to enter Bus-Sleep Mode.

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
     - nmNetworkHandle
     - Identification of the NM-channel

**Return type**
   void


Nm_RemoteSleepCancellation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Nm_RemoteSleepCancellation(NetworkHandleType nmNetworkHandle)

Notification that the network management has detected that not all other nodes on the network are longer ready to enter Bus-Sleep Mode.

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
     - nmNetworkHandle
     - Identification of the NM-channel

**Return type**
   void


Nm_SynchronizationPoint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Nm_SynchronizationPoint(NetworkHandleType nmNetworkHandle)

Notification to the NM Coordinator functionality that this is a suitable point in time to initiate the coordinated shutdown on.

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
     - nmNetworkHandle
     - Identification of the NM-channel

**Return type**
   void


Nm_CoordReadyToSleepIndication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Nm_CoordReadyToSleepIndication(NetworkHandleType nmChannelHandle)

Sets an indication, when the NM Coordinator Sleep Ready bit in the Control Bit Vector is set.

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
     - nmChannelHandle
     - Identification of the NM-channel

**Return type**
   void


Nm_CoordReadyToSleepCancellation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Nm_CoordReadyToSleepCancellation(NetworkHandleType nmChannelHandle)

Cancels an indication, when the NM Coordinator Sleep Ready bit in the Control Bit Vector is set back to 0.

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
     - nmChannelHandle
     - Identification of the NM-channel

**Return type**
   void


Nm_PduRxIndication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Nm_PduRxIndication(NetworkHandleType nmNetworkHandle)

Notification that a NM message has been received.

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
     - nmNetworkHandle
     - Identification of the NM-channel

**Return type**
   void


Nm_StateChangeNotification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Nm_StateChangeNotification(NetworkHandleType nmNetworkHandle, Nm_StateType nmPreviousState, Nm_StateType nmCurrentState)

Notification that the state of the lower layer <Bus>Nm has changed.

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
     - nmNetworkHandle
     - Identification of the NM-channel
   * - [in]
     - nmPreviousState
     - previous state of the NM-channel
   * - [in]
     - nmCurrentState
     - current state of the NM-channel

**Return type**
   void


Nm_RepeatMessageIndication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Nm_RepeatMessageIndication(NetworkHandleType nmNetworkHandle)

Service to indicate that an NM message with set Repeat Message Request Bit has been received.

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
     - nmNetworkHandle
     - Identification of the NM-channel

**Return type**
   void


Nm_TxTimeoutException
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Nm_TxTimeoutException(NetworkHandleType nmNetworkHandle)

Service to indicate that an attempt to send an NM message failed.

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
     - nmNetworkHandle
     - Identification of the NM-channel

**Return type**
   void


Nm_CarWakeUpIndication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Nm_CarWakeUpIndication(NetworkHandleType nmChannelHandle)

This function is called by a <Bus>Nm to indicate reception of a CWU request.

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
     - nmChannelHandle
     - Identification of the NM-channel

**Return type**
   void


Nm_MainFunction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Nm_MainFunction(uint8 chIdx)

implements the processes of the NM Interface which need a fix cyclic scheduling.

**Sync/Async**
   Asynchronous

**Reentrancy**
   Reentrant (Non-reentrant for the same NetworkHandle, reentrant otherwise)

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - chIdx
     - the configured channel index

**Return type**
   void


Nm_SynchronizeMode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Nm_SynchronizeMode(NetworkHandleType nmNetworkHandle)

Notification that the network management has entered Synchronize Mode.

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
     - nmNetworkHandle
     - Identification of the NM-channel

**Return type**
   void


Nm_UpdateIRA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Nm_UpdateIRA(NetworkHandleType networkHandle, const uint8 *pncBitVectorPtr)

Indication by ComM of internal PNC requests. This is used to aggregate the internal PNC requests.

**Sync/Async**
   Synchronous (Non-reentrant for the same NetworkHandle, reentrant otherwise)

**Reentrancy**
   Non Reentrant for the same NetworkHandle, reentrant otherwise

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - networkHandle
     - Identification of the NM-channel
   * - [in]
     - pncBitVectorPtr
     - Pointer to the bit vector with all PNC bits set to "1" of internal requested PNCs (IRA)

**Return type**
   void


Nm_PncBitVectorTxIndication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Nm_PncBitVectorTxIndication(NetworkHandleType networkHandle, uint8 *pncBitVectorPtr)

Function called by <Bus>Nms to request the aggregated internal PNC requests for transmission within the Nm message.

**Sync/Async**
   Synchronous (Non-reentrant for the same NetworkHandle, reentrant otherwise)

**Reentrancy**
   Non Reentrant for the same NetworkHandle, reentrant otherwise

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - networkHandle
     - Identification of the NM-channel
   * - [out]
     - pncBitVectorPtr
     - Pointer to the bit vector with all PNC bits set to 1 of internal requested PNCs

**Return type**
   void


Nm_PncBitVectorRxIndication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Nm_PncBitVectorRxIndication(NetworkHandleType networkHandle, const uint8 *pncBitVectorPtr, boolean *relevantPncRequestDetectedPtr)

The function evaluate if a relevant PNC request (PNC bit set to ’1’) is available in the given PNC bit vector.

**Sync/Async**
   Synchronous (Non-reentrant for the same networkHandle, reentrant otherwise)

**Reentrancy**
   Non Reentrant for the same networkHandle, reentrant otherwise

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - networkHandle
     - Identification of the NM-channel
   * - [in]
     - pncBitVectorPtr
     - Pointer to the bit vector with all PNC bits set to "1" of external requested PNCs
   * - [out]
     - relevantPncRequestDetectedPtr
     - Pointer to a boolean variable which indicates, if a relevant PNC request

**Return type**
   void


