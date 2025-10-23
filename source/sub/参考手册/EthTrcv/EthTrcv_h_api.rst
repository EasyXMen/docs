
类型定义 Type Definitions
--------------------------------------------------------------------------------
.. 如果没有就不存在该章节，或为None

None

      
提供的服务 Services
--------------------------------------------------------------------------------
EthTrcv_Init
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void EthTrcv_Init(const EthTrcv_ConfigType *CfgPtr)

Initializes the Ethernet Transceiver Driver.

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
     - CfgPtr
     - Points to the implementation specific structure.

**Return type**
   void


EthTrcv_SetTransceiverMode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthTrcv_SetTransceiverMode(uint8 TrcvIdx, Eth_ModeType TrcvMode)

Enables / disables the indexed transceiver.

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
     - TrcvIdx
     - Index of the transceiver within the context of the Transceiver Driver.
   * - [in]
     - TrcvMode
     - ETH_MODE_DOWN: disable the transceiver. ETH_MODE_ACTIVE: enable the transceiver. ETH_MODE_ACTIVE_WITH_WAKEUP_REQUEST: enable the transceiver and request to trigger a wake-up on the network, if the used PHY support such a feature. E.g. used for PHYs compliant to OA TC10.

**Return type**
   Std_ReturnType


EthTrcv_GetTransceiverMode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthTrcv_GetTransceiverMode(uint8 TrcvIdx, Eth_ModeType *TrcvModePtr)

Obtains the state of the indexed transceiver.

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
     - TrcvIdx
     - Index of the transceiver within the context of the Transceiver Driver.
   * - [out]
     - TrcvModePtr
     - ETH_MODE_DOWN: the transceiver is disabled. ETH_MODE_ACTIVE: the transceiver is enable.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - success.
   * - E_NOT_OK
     - transceiver could not be initialized.

EthTrcv_GetBusWuReason
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthTrcv_GetBusWuReason(uint8 TrcvIdx, EthTrcv_WakeupReasonType *WakeupReasonPtr)

This function returns the least recent wakeup reasons.

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
     - TrcvIdx
     - Index of the transceiver within the context of the Ethernet Transceiver Driver.
   * - [out]
     - WakeupReasonPtr
     - Pointer to structure of least recent wakeup event, which was detected by the Ethernet PHY.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - PHY wake up reason request has been accepted.
   * - E_NOT_OK
     - PHY wake up reason request has not been accepted.

EthTrcv_CheckWakeup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthTrcv_CheckWakeup(uint8 TrcvIdx)

Service is called by EthIf in case a wake-up interrupt is detected.

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
     - TrcvIdx
     - Index of the transceiver within the context of the Transceiver Driver.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The function has been successfully executed.
   * - E_NOT_OK
     - The function could not be successfully executed.

EthTrcv_StartAutoNegotiation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthTrcv_StartAutoNegotiation(uint8 TrcvIdx)

Restarts the negotiation of the transmission parameters used by the indexed transceiver.

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
     - TrcvIdx
     - Index of the transceiver within the context of the Ethernet Transceiver Driver.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - success.
   * - E_NOT_OK
     - transceiver could not be initialized.

EthTrcv_TransceiverLinkStateRequest
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthTrcv_TransceiverLinkStateRequest(uint8 TrcvIdx, EthTrcv_LinkStateType LinkState)

Request the given link state for the given transceiver.

**Sync/Async**
   FALSE

**Reentrancy**
   Reentrant for different TrcvIdx. Non reentrant for the same TrcvIdx.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - TrcvIdx
     - Index of the transceiver within the context of the Transceiver Driver.
   * - [in]
     - LinkState
     - The link state of a physical connection.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The request has been accepted.
   * - E_NOT_OK
     - The request has not been accepted.

EthTrcv_GetLinkState
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthTrcv_GetLinkState(uint8 TrcvIdx, EthTrcv_LinkStateType *LinkStatePtr)

Obtains the link state of the indexed transceiver.

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - TrcvIdx
     - Index of the transceiver within the context of the Transceiver Driver.
   * - [out]
     - LinkStatePtr
     - ETHTRCV_LINK_STATE_DOWN: transceiver is disconnected. ETHTRCV_LINK_STATE_ACTIVE: transceiver is connected.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - success.
   * - E_NOT_OK
     - transceiver could not be initialized.

EthTrcv_GetBaudRate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthTrcv_GetBaudRate(uint8 TrcvIdx, EthTrcv_BaudRateType *BaudRatePtr)

Obtains the baud rate of the indexed transceiver.

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - TrcvIdx
     - Index of the transceiver within the context of the Ethernet Transceiver Driver.
   * - [out]
     - BaudRatePtr
     - ETHTRCV_BAUD_RATE_10MBIT: 10MBit connection. ETHTRCV_BAUD_RATE_100MBIT: 100MBit connection. ETHTRCV_BAUD_RATE_1000MBIT: 1000MBit connection. ETHTRCV_BAUD_RATE_2500MBIT: 2500MBit connection.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - success.
   * - E_NOT_OK
     - transceiver could not be initialized.

EthTrcv_GetDuplexMode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthTrcv_GetDuplexMode(uint8 TrcvIdx, EthTrcv_DuplexModeType *DuplexModePtr)

Obtains the duplex mode of the indexed transceiver.

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - TrcvIdx
     - Index of the transceiver within the context of the Ethernet Transceiver Driver.
   * - [out]
     - DuplexModePtr
     - ETHTRCV_DUPLEX_MODE_HALF: half duplex connections. ETHTRCV_DUPLEX_MODE_FULL: full duplex connection.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - success.
   * - E_NOT_OK
     - transceiver could not be initialized.

EthTrcv_SetPhyTestMode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthTrcv_SetPhyTestMode(uint8 TrcvIdx, EthTrcv_PhyTestModeType Mode)

Activates a given test mode.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant for different TrcvIdx. Non reentrant for the same TrcvIdx.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - TrcvIdx
     - Index of the transceiver within the context of the Ethernet Transceiver Driver.
   * - [in]
     - Mode
     - Test mode to be activated.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The request has been accepted.
   * - E_NOT_OK
     - The request has not been accepted.

EthTrcv_SetPhyLoopbackMode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthTrcv_SetPhyLoopbackMode(uint8 TrcvIdx, EthTrcv_PhyLoopbackModeType Mode)

Activates a given loopback mode.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant for different TrcvIdx. Non reentrant for the same TrcvIdx.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - TrcvIdx
     - Index of the transceiver within the context of the Ethernet Transceiver Driver.
   * - [in]
     - Mode
     - Loopback mode to be activated.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The request has been accepted.
   * - E_NOT_OK
     - The request has not been accepted.

EthTrcv_GetPhySignalQuality
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthTrcv_GetPhySignalQuality(uint8 TrcvIdx, uint32 *SignalQualityPtr)

Obtains the current signal quality of the link of the indexed transceiver.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant for different TrcvIdx. Non reentrant for the same TrcvIdx.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - TrcvIdx
     - Index of the transceiver within the context of the Ethernet Transceiver Driver.
   * - [out]
     - SignalQualityPtr
     - Pointer to the memory where the signal quality shall be stored.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The request has been accepted.
   * - E_NOT_OK
     - The request has not been accepted.

EthTrcv_SetPhyTxMode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthTrcv_SetPhyTxMode(uint8 TrcvIdx, EthTrcv_PhyTxModeType Mode)

Activates a given transmission mode.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant for different TrcvIdx. Non reentrant for the same TrcvIdx.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - TrcvIdx
     - Index of the transceiver within the context of the Ethernet Transceiver Driver.
   * - [in]
     - Mode
     - Transmission mode to be activated.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The request has been accepted.
   * - E_NOT_OK
     - The request has not been accepted.

EthTrcv_RunCableDiagnostic
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthTrcv_RunCableDiagnostic(uint8 TrcvIdx)

Trigger the cable diagnostics for the given Ethernet transceiver.

**Sync/Async**
   FALSE

**Reentrancy**
   Reentrant for different TrcvIdx. Non reentrant for the same TrcvIdx.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - TrcvIdx
     - Index of the Ethernet transceiver within the context of the Ethernet Transceiver Driver.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The trigger has been accepted.
   * - E_NOT_OK
     - The trigger has not been accepted.

EthTrcv_GetCableDiagnosticsResult
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthTrcv_GetCableDiagnosticsResult(uint8 TrcvIdx, EthTrcv_CableDiagResultType *ResultPtr)

Retrieves the cable diagnostics result of a given transceiver.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant for different TrcvIdx. Non reentrant for the same TrcvIdx.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - TrcvIdx
     - Index of the transceiver within the context of the Ethernet Transceiver Driver.
   * - [out]
     - ResultPtr
     - Pointer to the location where the cable diagnostics result shall be stored.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The request has been accepted.
   * - E_NOT_OK
     - The request has not been accepted.

EthTrcv_GetPhyIdentifier
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthTrcv_GetPhyIdentifier(uint8 TrcvIdx, uint32 *OrgUniqueIdPtr, uint8 *ModelNrPtr, uint8 *RevisionNrPtr)

Obtains the PHY identifier of the Ethernet Transceiver according to IEEE 802.3-2015 chapter 22.2.4.3.1 PHY Identifer.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant for different TrcvIdx. Non reentrant for the same TrcvIdx.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - TrcvIdx
     - Index of the transceiver within the context of the Ethernet Transceiver Driver.
   * - [out]
     - OrgUniqueIdPtr
     - Pointer to the memory where the Organizationally Unique Identifier shall be stored.
   * - [out]
     - ModelNrPtr
     - Pointer to the memory where the Manufacturer's Model Number shall be stored.
   * - [out]
     - RevisionNrPtr
     - Pointer to the memory where the Revision Number shall be stored.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The request has been accepted.
   * - E_NOT_OK
     - The request has not been accepted.

EthTrcv_GetMacMethod
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthTrcv_GetMacMethod(uint8 *TrcvIdx, EthTrcv_MacMethodType *MacModePtr)

Obtains the media access mode of the transceiver when EthTrcvDuplexMode is configured as ETHTRCV_DUPLEX_MODE_HALF.

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - TrcvIdx
     - Index of the transceiver within the context of the Ethernet Transceiver Driver.
   * - [out]
     - MacModePtr
     - ETHTRCV_MAC_TYPE_CSMA_CD: Carrier-sense multiple access with collicion detection. ETHTRCV_MAC_TYPE_PLCA: Physical layer collision avoidance.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - success.
   * - E_NOT_OK
     - MacType could not be returned.

EthTrcv_GetVersionInfo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void EthTrcv_GetVersionInfo(Std_VersionInfoType *VersionInfoPtr)

Returns the version information of this module.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [out]
     - VersionInfoPtr
     - Version information of this module.

**Return type**
   void


EthTrcv_MainFunction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void EthTrcv_MainFunction(void)

Used for polling state changes and wakeup reasons. Calls EthIf_TrcvModeIndication when the transceiver mode changed. Stores wakeup events if EthTrcvWakeUpSupport is set to ETHTRCV_WAKEUP_BY_POLLING.

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant.


**Return type**
   void


