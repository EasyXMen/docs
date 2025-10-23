
类型定义（Type definition）
------------------------------
.. 如果没有就不存在该章节，或为None


提供的服务（Provided services）
---------------------------------
CanNm_Init
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void CanNm_Init(const CanNm_ConfigType *CanNmConfigPtr)

Initialize the CanNm module.

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
     - CanNmConfigPtr
     - Pointer to a selected configuration structure.

**Return type**
   void


CanNm_DeInit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void CanNm_DeInit(void)

De-initializes the CanNm module.

**Sync/Async**
   Synchronous

**Reentrancy**
   Non Reentrant


**Return type**
   void


CanNm_PassiveStartUp
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType CanNm_PassiveStartUp(NetworkHandleType nmChannelHandle)

Passive startup of the AUTOSAR CAN NM. It triggers the transition from Bus-Sleep Mode or Prepare Bus Sleep Mode to the Network Mode in Repeat Message State.

**Sync/Async**
   Asynchronous

**Reentrancy**
   Reentrant(but not for the same NM-Channel)

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

CanNm_NetworkRequest
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType CanNm_NetworkRequest(NetworkHandleType nmChannelHandle)

Request the network, since ECU needs to communicate on the bus.

**Sync/Async**
   Asynchronous

**Reentrancy**
   Reentrant(but not for the same NM-Channel)

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - nmChannelHandle
     - Identification of the NM-channel.

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
     - Requesting of network has failed

CanNm_NetworkRelease
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType CanNm_NetworkRelease(NetworkHandleType nmChannelHandle)

Release the network, since ECU doesn't have to communicate on the bus.

**Sync/Async**
   Asynchronous

**Reentrancy**
   Reentrant(but not for the same NM-Channel)

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
     - Releasing of network has failed

CanNm_DisableCommunication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType CanNm_DisableCommunication(NetworkHandleType nmChannelHandle)

Disable the NM PDU transmission ability due to a ISO14229 Communication Control (28hex) service.

**Sync/Async**
   Asynchronous

**Reentrancy**
   Reentrant(but not for the same NM-Channel)

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
     - Disabling of NM PDU transmission ability has failed

CanNm_EnableCommunication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType CanNm_EnableCommunication(NetworkHandleType nmChannelHandle)

Enable the NM PDU transmission ability due to a ISO14229 Communication Control (28hex) service.

**Sync/Async**
   Asynchronous

**Reentrancy**
   Reentrant(but not for the same NM-Channel)

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
     - Enabling of NM PDU transmission ability has failed

CanNm_SetUserData
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType CanNm_SetUserData(NetworkHandleType nmChannelHandle, const uint8 *nmUserDataPtr)

Set user data for NM PDUs transmitted next on the bus.

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant(but not for the same NM-Channel)

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
   * - [in]
     - nmUserDataPtr
     - Pointer where the user data for the next transmitted NM PDU shall be copied from

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

CanNm_GetUserData
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType CanNm_GetUserData(NetworkHandleType nmChannelHandle, uint8 *nmUserDataPtr)

Get user data out of the most recently received NM PDU.

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
   * - [in]
     - nmUserDataPtr
     - Pointer where user data out of the most recently received NM PDU shall be copied to

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

CanNm_Transmit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType CanNm_Transmit(PduIdType TxPduId, const PduInfoType *PduInfoPtr)

Requests transmission of a PDU.

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant(but not for the same PduIds)

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - TxPduId
     - Identifier of the PDU to be transmitted
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

CanNm_GetNodeIdentifier
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType CanNm_GetNodeIdentifier(NetworkHandleType nmChannelHandle, uint8 *nmNodeIdPtr)

Get node identifier out of the most recently received NM PDU.

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
   * - [in]
     - nmNodeIdPtr
     - Pointer where node identifier out of the most recently received NM PDU shall be copied to.

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
     - Getting of the node identifier out of the most recently received NM PDU has failed or is not configured for this network handle.

CanNm_GetLocalNodeIdentifier
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType CanNm_GetLocalNodeIdentifier(NetworkHandleType nmChannelHandle, uint8 *nmNodeIdPtr)

Get node identifier configured for the local node.

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
   * - [in]
     - nmNodeIdPtr
     - Pointer where node identifier of the local node shall be copied to.

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
     - Getting of the node identifier of the local node has failed or is not configured for this network handle.

CanNm_RepeatMessageRequest
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType CanNm_RepeatMessageRequest(NetworkHandleType nmChannelHandle)

Set Repeat Message Request Bit for NM PDUs transmitted next on the bus.

**Sync/Async**
   Synchronous (but not for the same NM-channel)

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
     - Setting of Repeat Message Request Bit has failed or is not configured for this network handle.

CanNm_GetPduData
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType CanNm_GetPduData(NetworkHandleType nmChannelHandle, uint8 *nmPduDataPtr)

Get the whole PDU data out of the most recently received NM PDU.

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
   * - [in]
     - nmPduDataPtr
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
     - Getting of NM PDU Data has failed or is not configured for this network handle.

CanNm_GetState
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType CanNm_GetState(NetworkHandleType nmChannelHandle, Nm_StateType *nmStatePtr, Nm_ModeType *nmModePtr)

Returns the state and the mode of the network management.

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
   * - [out]
     - nmStatePtr
     - Pointer where state of the network management shall be copied to
   * - [out]
     - nmModePtr
     - Pointer where the mode of the network management shall be copied to

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
     - Getting of NM state has failed

CanNm_GetVersionInfo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void CanNm_GetVersionInfo(Std_VersionInfoType *versioninfo)

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


CanNm_RequestBusSynchronization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType CanNm_RequestBusSynchronization(NetworkHandleType nmChannelHandle)

Request bus synchronization.

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
     - Requesting of bus synchronization has failed

CanNm_CheckRemoteSleepIndication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType CanNm_CheckRemoteSleepIndication(NetworkHandleType nmChannelHandle, boolean *nmRemoteSleepIndPtr)

Check if remote sleep indication takes place or not.

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
   * - [out]
     - nmRemoteSleepIndPtr
     - Pointer where check result of remote sleep indication shall be copied to

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

CanNm_SetSleepReadyBit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType CanNm_SetSleepReadyBit(NetworkHandleType nmChannelHandle, boolean nmSleepReadyBit)

Set the NM Coordinator Sleep Ready bit in the Control Bit Vector.

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant (but not for the same NM-channel)

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
   * - [in]
     - nmSleepReadyBit
     - Pointer where check result of remote sleep indication shall be copied to

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
     - Writing of remote sleep indication bit has failed

CanNm_RxIndication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void CanNm_RxIndication(PduIdType RxPduId, const PduInfoType *PduInfoPtr)

Indication of a received PDU from a lower layer communication interface module.

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant (but not for the same PduId)

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - RxPduId
     - ID of the received PDU.
   * - [in]
     - PduInfoPtr
     - Contains the length (SduLength) of the received PDU, a pointer to a buffer (SduDataPtr) containing the PDU, and the MetaData related to this PDU.

**Return type**
   void


CanNm_TxConfirmation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void CanNm_TxConfirmation(PduIdType TxPduId, Std_ReturnType result)

The lower layer communication interface module confirms the transmission of a PDU, or the failure to transmit a PDU.

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant (but not for the same PduId)

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - 
     - TxPduId
     - 
   * - [in]
     - result
     - E_OK: The PDU was transmitted E_NOT_OK: Transmission of the PDU failed.

**Return type**
   void


CanNm_ConfirmPnAvailability
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void CanNm_ConfirmPnAvailability(NetworkHandleType nmChannelHandle)

Enables the PN filter functionality on the indicated NM channel.

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant (but not for the same NM-channel)

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - nmChannelHandle
     - Identification of the NM-channel.

**Return type**
   void


CanNm_TriggerTransmit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType CanNm_TriggerTransmit(PduIdType TxPduId, PduInfoType *PduInfoPtr)

Within this API, the upper layer module (called module) shall check whether the available data fits into the buffer size reported by PduInfoPtr->SduLength.

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant (but not for the same PduId)

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
     - Contains a pointer to a buffer (SduDataPtr) to where the SDU data shall be copied, and the available buffer size in SduLengh. On return, the service will indicate the length of the copied SDU data in SduLength.

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

CanNm_MainFunction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void CanNm_MainFunction(CanNm_ChannelIndexType chIndex)

Main function of the CanNm which processes the algorithm describes in that document.

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant (but not for the same Identification of the NM-channel)

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - chIndex
     - Identification of the NM-channel

**Return type**
   void


