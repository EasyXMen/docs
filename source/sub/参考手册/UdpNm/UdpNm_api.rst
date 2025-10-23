
类型定义 Type Definitions
--------------------------------------------------------------------------------
.. 如果没有就不存在该章节，或为None

None

      
提供的服务 Services
--------------------------------------------------------------------------------
UdpNm_Init
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void UdpNm_Init(const UdpNm_ConfigType *UdpNmConfigPtr)

Initialize the complete UdpNm module.

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
     - UdpNmConfigPtr
     - Pointer to a selected configuration

**Return type**
   void


UdpNm_PassiveStartUp
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType UdpNm_PassiveStartUp(NetworkHandleType nmChannelHandle)

Passive startup of the AUTOSAR UdpNm.

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

UdpNm_NetworkRequest
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType UdpNm_NetworkRequest(NetworkHandleType nmChannelHandle)

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
     - Requesting of network has failed

UdpNm_NetworkRelease
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType UdpNm_NetworkRelease(NetworkHandleType nmChannelHandle)

Release the network,since ECU doesn't have to communicate on the bus.

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

UdpNm_DisableCommunication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType UdpNm_DisableCommunication(NetworkHandleType nmChannelHandle)

Disable the NM PDU transmission ability due to a ISO14229 Communication Control (0x28) service.

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

UdpNm_EnableCommunication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType UdpNm_EnableCommunication(NetworkHandleType nmChannelHandle)

Enable the NM PDU transmission ability due to a ISO14229 Communication Control (0x28) service.

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

UdpNm_SetUserData
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType UdpNm_SetUserData(NetworkHandleType nmChannelHandle, const uint8 *nmUserDataPtr)

Set user data for all NM messages transmitted on the bus after this function has returned without error.

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
   * - [in]
     - nmUserDataPtr
     - Pointer where the user data for the next transmitted NM message shall be copied from.

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
     - Setting of user data has failed.

UdpNm_GetUserData
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType UdpNm_GetUserData(NetworkHandleType nmChannelHandle, uint8 *nmUserDataPtr)

Get user data from the most recently received NM message.

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
   * - [in]
     - nmUserDataPtr
     - Pointer where user data out of the most recently received NM PDU shall be copied to.

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

UdpNm_GetNodeIdentifier
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType UdpNm_GetNodeIdentifier(NetworkHandleType nmChannelHandle, uint8 *nmNodeIdPtr)

Get node identifier from the most recently received NM PDU.

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

UdpNm_GetLocalNodeIdentifier
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType UdpNm_GetLocalNodeIdentifier(NetworkHandleType nmChannelHandle, uint8 *nmNodeIdPtr)

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
   * - [out]
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

UdpNm_RepeatMessageRequest
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType UdpNm_RepeatMessageRequest(NetworkHandleType nmChannelHandle)

Set Repeat Message Request Bit for all NM messages transmitted on the bus after this function has returned without error.

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
     - Setting of Repeat Message Request Bit has failed or is not configured for this network handle.

UdpNm_GetPduData
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType UdpNm_GetPduData(NetworkHandleType nmChannelHandle, uint8 *nmPduDataPtr)

Get the whole PDU data out of the most recently received NM message. @id 0x0a.

**Sync/Async**
   Synchronous @reentrancy Reentrant

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

UdpNm_GetState
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType UdpNm_GetState(NetworkHandleType nmChannelHandle, Nm_StateType *nmStatePtr, Nm_ModeType *nmModePtr)

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
     - Pointer where state of the network management shall be copied to.
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

UdpNm_GetVersionInfo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void UdpNm_GetVersionInfo(Std_VersionInfoType *versioninfo)

Returns the version information of this module.

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
     - versioninfo
     - Pointer to where to store the version information of this module

**Return type**
   void


UdpNm_RequestBusSynchronization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType UdpNm_RequestBusSynchronization(NetworkHandleType nmChannelHandle)

Request bus synchronization.

**Sync/Async**
   Asynchronous

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

UdpNm_CheckRemoteSleepIndication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType UdpNm_CheckRemoteSleepIndication(NetworkHandleType nmChannelHandle, boolean *nmRemoteSleepIndPtr)

Check if remote sleep indication takes place or not.

**Sync/Async**
   Synchronous(but not for the same NM-Channel)

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
     - Pointer where check result of remote sleep indication shall be copied to.

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
     - Checking of remote sleep indication bits failed

UdpNm_SetSleepReadyBit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType UdpNm_SetSleepReadyBit(NetworkHandleType nmChannelHandle, boolean nmSleepReadyBit)

Set the NM Coordinator Sleep Ready bit in the Control Bit Vector.

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
   * - [in]
     - nmSleepReadyBit
     - Value written to ReadySleep Bit in CBV

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

UdpNm_Transmit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType UdpNm_Transmit(PduIdType TxPduId, const PduInfoType *PduInfoPtr)

Requests transmission of a PDU.

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant(for different PduIds. Non reentrant for the same PduId)

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

UdpNm_SoAdIfTxConfirmation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void UdpNm_SoAdIfTxConfirmation(PduIdType TxPduId, Std_ReturnType result)

The lower layer communication interface module confirms the transmission of an IPDU, or the failure to transmit a PDU.

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant(for different PduIds. Non reentrant for the same PduId)

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
     - result
     - E_OK: The PDU was transmitted. E_NOT_OK: Transmission of the PDU failed.

**Return type**
   void


UdpNm_SoAdIfRxIndication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void UdpNm_SoAdIfRxIndication(PduIdType RxPduId, const PduInfoType *PduInfoPtr)

Indication of a received PDU from a lower layer communication interface module.

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant(for different PduIds. Non reentrant for the same PduId.)

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
     - Contains the length (SduLength) of the received I-PDU and a pointer to a buffer (SduDataPtr) containing the I-PDU.

**Return type**
   void


UdpNm_SoAdIfTriggerTransmit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType UdpNm_SoAdIfTriggerTransmit(PduIdType TxPduId, PduInfoType *PduInfoPtr)

Within this API, the upper layer module (called module) shall check whether the available data fits into the buffer size reported by PduInfoPtr->SduLength. If it fits, it shall copy its data into the buffer provided by PduInfoPtr->SduDataPtr and update the length of the actual copied data in PduInfoPtr->SduLength. If not, it returns E_NOT_OK without changing PduInfoPtr.

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant(for different PduIds. Non reentrant for the same PduId.)

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
   * - [in]
     - PduInfoPtr
     - Contains a pointer to a buffer (SduDataPtr) to where the SDU data shall be copied, and the available buffer size in SduLengh. On return, the service will indicate the length of the copied SDU data in SduLength.

**Return type**
   Std_ReturnType


UdpNm_MainFunction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void UdpNm_MainFunction(UdpNm_ChannelIndexType chIndex)

Main function of the UdpNm which processes the algorithm describes in that document.

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant(for different NM-channel)

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - chIndex
     - Index value of the NM-channel.

**Return type**
   void


