

提供的服务 Services
------------------------------------------------------------------
EthIf_Init
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void EthIf_Init(const EthIf_ConfigType *CfgPtr)

Initializes the Ethernet Interface.

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


EthIf_SetControllerMode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthIf_SetControllerMode(uint8 CtrlIdx, Eth_ModeType CtrlMode)

Enables / disables the indexed controller.

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
     - CtrlIdx
     - Index of Ethernet Controller.
   * - [in]
     - CtrlMode
     - Mode for Controller.

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
     - controller mode could not be changed.

EthIf_GetControllerMode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthIf_GetControllerMode(uint8 CtrlIdx, Eth_ModeType *CtrlModePtr)

Enables / disables the indexed controller.

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
     - CtrlIdx
     - Index of Ethernet Controller.
   * - [out]
     - CtrlModePtr
     - Mode of Controller.

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
     - controller could not be initialized.

EthIf_GetTransceiverMode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthIf_GetTransceiverMode(uint8 TrcvIdx, Eth_ModeType *TrcvModePtr)

Obtain state of the indexed transceiver.

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
   * - [out]
     - TrcvModePtr
     - ETH_MODE_DOWN: the transceiver is disabled ETH_MODE_ACTIVE: the transceiver is enable.

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

EthIf_CheckWakeup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthIf_CheckWakeup(EcuM_WakeupSourceType WakeupSource)

This API request the affected Ethernet hardware to check for a signaled wake-up.

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
     - Source device which initiated the wake up event.

**Return type**
   Std_ReturnType


EthIf_GetPhyWakeupReason
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthIf_GetPhyWakeupReason(uint8 TrcvIdx, EthTrcv_WakeupReasonType *WakeupReasonPtr)

obtains the wake up reasons of the indexed Ethernet Transceiver (PHY).

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
     - Index of the transceiver.
   * - [out]
     - WakeupReasonPtr
     - Pointer to structure of least recent wakeup event,which was detected by the Ethernet PHY.

**Return type**
   Std_ReturnType


EthIf_GetSwitchPortWakeupReason
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthIf_GetSwitchPortWakeupReason(uint8 SwitchIdx, uint8 SwitchPortIdx, EthTrcv_WakeupReasonType *WakeupReasonPtr)

This function obtains the wake up reasons of the indexed Ethernet switch port.

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
     - SwitchIdx
     - Index of the Ethernet switch.
   * - [in]
     - SwitchPortIdx
     - Index of the Ethernet switch port.
   * - [out]
     - WakeupReasonPtr
     - Pointer to structure of least recent wakeup event,which was detected by the Ethernet switch port.

**Return type**
   Std_ReturnType


EthIf_GetPhysAddr
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void EthIf_GetPhysAddr(uint8 CtrlIdx, uint8 *PhysAddrPtr)

Obtains the physical source address used by the indexed controller.

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
     - CtrlIdx
     - Index of the Ethernet controller.
   * - [out]
     - PhysAddrPtr
     - Physical source address (MAC address) in network byte order.

**Return type**
   void


EthIf_SetPhysAddr
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void EthIf_SetPhysAddr(uint8 CtrlIdx, const uint8 *PhysAddrPtr)

Sets the physical source address used by the indexed controller.

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant for the same CtrlIdx, reentrant for different

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - CtrlIdx
     - Index of the Ethernet controller.
   * - [out]
     - PhysAddrPtr
     - Pointer to memory containing the physical source address (MAC address) in network byte order.

**Return type**
   void


EthIf_UpdatePhysAddrFilter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthIf_UpdatePhysAddrFilter(uint8 CtrlIdx, const uint8 *PhysAddrPtr, Eth_FilterActionType Action)

Update the physical source address to/from the indexed controller filter.

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
     - CtrlIdx
     - Index of the Ethernet controller.
   * -
     - PhysAddrPtr
     -
   * - [in]
     - Action
     - Add or remove the address from the Ethernet controllers filter.

**Return type**
   Std_ReturnType


EthIf_GetCurrentTime
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthIf_GetCurrentTime(uint8 CtrlIdx, Eth_TimeStampQualType *timeQualPtr, Eth_TimeStampType *timeStampPtr)



**Sync/Async**


**Reentrancy**



**Return type**
   Std_ReturnType


EthIf_GetCurrentTimeTuple
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthIf_GetCurrentTimeTuple(uint8 CtrlIdx, uint8 ClkUnitIdx, TimeTupleType *currentTimeTuplePtr)

Reads the current time of the timestamp clock and the current time of the PHC in an atomic operation.

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
     - CtrlIdx
     - Index of Ethernet Controller.
   * - [in]
     - ClkUnitIdx
     - Index of the Clock Unit.
   * - [out]
     - currentTimeTuplePtr
     - Current time tuple with the: value of the free-running clock used for timestamping and value of the adjustable PHC

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Current time successfully retrieved.
   * - E_NOT_OK
     - Current time could not be retrieved.

EthIf_SetPhcTime
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthIf_SetPhcTime(uint8 CtrlIdx, uint8 ClkUnitIdx, const TimeStampType *timeStampPtr)

Sets the absolute time of the PHC.

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
     - CtrlIdx
     - Index of Ethernet Controller.
   * - [in]
     - ClkUnitIdx
     - Index of the Clock Unit.
   * - [out]
     - timeStampPtr
     - Time value to which the PHC shall be set.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Current time successfully retrieved.
   * - E_NOT_OK
     - Current time could not be retrieved.

EthIf_SetPhcCorrection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthIf_SetPhcCorrection(uint8 CtrlIdx, uint8 ClkUnitIdx, sint32 rateDeviation, sint32 offset)

Sets the absolute time of the PHC.

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
     - CtrlIdx
     - Index of Ethernet Controller.
   * - [in]
     - ClkUnitIdx
     - Index of the Clock Unit.
   * - [in]
     - rateDeviation
     - Rate deviation (resolution: 2-41), by which the PHC is requested to be corrected.
   * - [in]
     - offset
     - Time offset, by which the PHC is requested to be updated.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Current time successfully retrieved.
   * - E_NOT_OK
     - Current time could not be retrieved.

EthIf_GetPhcTime
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthIf_GetPhcTime(uint8 CtrlIdx, uint8 ClkUnitIdx, TimeStampQualType *timeQualPtr, TimeStampType *timeStampPtr)

Returns the current time value out of the HW registers of the PHC.

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
     - CtrlIdx
     - Index of Ethernet Controller.
   * - [in]
     - ClkUnitIdx
     - Index of the Clock Unit.
   * - [out]
     - timeQualPtr
     - quality of HW time stamp, e.g. based on current drift.
   * - [out]
     - timeStampPtr
     - current time stamp.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - PHC value successfully retrieved.
   * - E_NOT_OK
     - PHC value could not be retrieved.

EthIf_SetPpsSignalMode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthIf_SetPpsSignalMode(uint8 CtrlIdx, uint8 ClkUnitIdx, boolean signalMode)

Enables/disables the generation of a PPS signal.

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
     - CtrlIdx
     - Index of Ethernet Controller.
   * - [in]
     - ClkUnitIdx
     - Index of the Clock Unit.
   * - [out]
     - signalMode
     - quality of HW time stamp, e.g. based on current drift.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - PPS signal generation successfully enabled/disabled.
   * - E_NOT_OK
     - Failed to enable/disable PPS signal generation.

EthIf_EnableEgressTimeStamp
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void EthIf_EnableEgressTimeStamp(uint8 CtrlIdx, Eth_BufIdxType BufIdx)

Activates egress time stamping on a dedicated message object.

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
     - CtrlIdx
     - Index of Ethernet Controller.
   * - [in]
     - BufIdx
     - Index of the message buffer, where Application expects egress time stamping.

**Return type**
   void


EthIf_GetEgressTimeStamp
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthIf_GetEgressTimeStamp(uint8 CtrlIdx, Eth_BufIdxType BufIdx, Eth_TimeStampQualType *timeQualPtr, Eth_TimeStampType *timeStampPtr)

Reads back the egress time stamp on a dedicated message object.

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
     - CtrlIdx
     - Index of Ethernet Controller.
   * - [in]
     - BufIdx
     - Index of the message buffer, where the Upper Layer expects egress time stamping.
   * - [out]
     - timeQualPtr
     - quality of HW time stamp, e.g. based on current drift.
   * - [out]
     - timeStampPtr
     - current time stamp.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - PPS signal generation successfully enabled/disabled.
   * - E_NOT_OK
     - Failed to enable/disable PPS signal generation.

EthIf_GetIngressTimeStamp
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthIf_GetIngressTimeStamp(uint8 CtrlIdx, const Eth_DataType *DataPtr, Eth_TimeStampQualType *timeQualPtr, Eth_TimeStampType *timeStampPtr)

Reads back the ingress time stamp on a dedicated message object.

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
     - CtrlIdx
     - Index of Ethernet Controller.
   * - [in]
     - DataPtr
     - Pointer to the message buffer, where Application expects ingress time stamping.
   * - [out]
     - timeQualPtr
     - quality of HW time stamp, e.g. based on current drift.
   * - [out]
     - timeStampPtr
     - current time stamp.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - PPS signal generation successfully enabled/disabled.
   * - E_NOT_OK
     - Failed to enable/disable PPS signal generation.

EthIf_ProvideTxBuffer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    BufReq_ReturnType EthIf_ProvideTxBuffer(uint8 CtrlIdx, Eth_FrameType FrameType, uint8 Priority, Eth_BufIdxType *BufIdxPtr, uint8 **BufPtr, uint16 *LenBytePtr)

Provides access to a transmit buffer of the specified Ethernet controller.

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
     - CtrlIdx
     - Index of the transceiver within the context of the Ethernet Interface.
   * - [out]
     - FrameType
     - Ethernet Frame Type (EtherType)
   * - [out]
     - Priority
     - Priority value which shall be used for the 3-bit PCP field of the VLAN tag
   * - [out]
     - BufIdxPtr
     - Index to the granted buffer resource. To be used for subsequent requests.
   * - [out]
     - BufPtr
     - Pointer to the granted buffer
   * - [inout]
     - LenBytePtr
     - in: desired length in bytes, out: granted length in bytes

**Return type**
   BufReq_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - BUFREQ_OK
     - success
   * - BUFREQ_E_NOT_OK
     - development error detected
   * - BUFREQ_E_BUSY
     - all buffers in use
   * - BUFREQ_E_OVFL
     - requested buffer too large

EthIf_Transmit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthIf_Transmit(uint8 CtrlIdx, Eth_BufIdxType BufIdx, Eth_FrameType FrameType, boolean TxConfirmation, uint16 LenByte, const uint8 *PhysAddrPtr)

Triggers transmission of a previously filled transmit buffer.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant for different buffer indexes and Ctrl indexes

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - CtrlIdx
     - Index of the transceiver within the context of the Ethernet Interface.
   * - [in]
     - BufIdx
     - Index of the buffer resource
   * - [in]
     - FrameType
     - Ethernet Frame Type (EtherType)
   * - [in]
     - TxConfirmation
     - Activates transmission confirmation.
   * - [in]
     - LenByte
     - Data length in byte.
   * - [in]
     - PhysAddrPtr
     - Physical target address (MAC address) in network byte order

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - success
   * - E_NOT_OK
     - transmission failed

EthIf_GetVersionInfo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void EthIf_GetVersionInfo(Std_VersionInfoType *VersionInfoPtr)

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
     - VersionInfoPtr
     - Version information of this module.

**Return type**
   void


EthIf_GetCtrlIdxList
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthIf_GetCtrlIdxList(uint8 *NumberOfCtrlIdx, uint8 *CtrlIdxListPtr)

Returns the number and index of all active Ethernet controllers..

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
     - NumberOfCtrlIdx
     -
   * - [out]
     - CtrlIdxListPtr
     - List of active controller indexes.

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
     - failure.

EthIf_MainFunctionRx
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void EthIf_MainFunctionRx(uint8 ethIfPartition)

The function checks for new received frames and issues reception indications in polling mode..

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
     - ethIfPartition
     - Index of the Ethernet partition.

**Return type**
   void


EthIf_MainFunctionTx
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void EthIf_MainFunctionTx(uint8 ethIfPartition)

The function issues transmission confirmations in polling mode.It checks also for transceiver state changes.

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
     - ethIfPartition
     - Index of the Ethernet partition.

**Return type**
   void


EthIf_MainFunctionState
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void EthIf_MainFunctionState(uint8 ethIfPartition)

The function is polling different communication hardware (Ethernet transceiver, Ethernet switch ports) related information, e.g. link state,signal quality.

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
     - ethIfPartition
     - Index of the Ethernet partition.

**Return type**
   void


EthIf_GetVlanId
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthIf_GetVlanId(uint8 CtrlIdx, uint16 *VlanIdPtr)

Returns the VLAN identifier of the requested Ethernet controller..

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
     - CtrlIdx
     - Index of the Ethernet controller.
   * - [out]
     - VlanIdPtr
     - Pointer to store the VLAN identifier (VID) of the Ethernet controller.

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
     - failure.

EthIf_GetAndResetMeasurementData
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthIf_GetAndResetMeasurementData(EthIf_MeasurementIdxType MeasurementIdx, boolean MeasurementResetNeeded, uint32 *MeasurementDataPtr)

Returns the VLAN identifier of the requested Ethernet controller..

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
     - MeasurementIdx
     - Data index of measurement data.
   * - [in]
     - MeasurementResetNeeded
     - Flag to trigger a reset of the measurement data.
   * - [out]
     - MeasurementDataPtr
     - Reference to data buffer, where to copy measurement data.

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
     - failure.

EthIf_GetPortMacAddr
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    BufReq_ReturnType EthIf_GetPortMacAddr(const uint8 *MacAddrPtr, uint8 *SwtichIdxPtr, uint8 *PortIdxPtr)

Obtains the port over which this MAC-address can be reached.

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
     - MacAddrPtr
     - ID of the SDU that is requested to be transmitted.
   * - [out]
     - SwtichIdxPtr
     - Pointer to the switch index.
   * - [out]
     - PortIdxPtr
     - Pointer to the port index.

**Return type**
   BufReq_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - success.
   * - E_NOT_OK
     - an error occurred, e.g. multiple ports were found.

EthIf_GetArlTable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthIf_GetArlTable(uint8 switchIdx, uint16 *numberOfElements, Eth_MacVlanType *arlTableListPointer)

Obtains the address resolution table of a switch and copies the list into a user provided buffer.

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
     - switchIdx
     - Index of the switch.
   * -
     - numberOfElements
     -
   * - [out]
     - arlTableListPointer
     - Returns a pointer to the memory where the ARL table of the switch.

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
     - requested switchIdx is not valid or inactive.

EthIf_StoreConfiguration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthIf_StoreConfiguration(uint8 SwitchIdx)

Trigger the storage/reset of the configuration of the learned MAC/Port tables of a switch in a persistent manner and will be used by e.g. CDD.

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
     - SwitchIdx
     - Index of the switch.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Storage/Reset request accepted.
   * - E_NOT_OK
     - Storage/Reset request not accepted.

EthIf_ResetConfiguration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthIf_ResetConfiguration(uint8 SwitchIdx)

The function shall request to reset the configuration of the learned MAC/Port tables of a Ethernet switch in a persistent manner.

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
     - SwitchIdx
     - Index of the switch.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request to persistently reset the MAC/Port table was accepted.
   * - E_NOT_OK
     - Request to persistently reset the MAC/Port table was not accepted.

EthIf_SwitchPortGroupRequestMode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthIf_SwitchPortGroupRequestMode(EthIf_SwitchPortGroupIdxType PortGroupIdx, Eth_ModeType PortMode)

Request a mode for the EthIfSwtPortGroup.

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
     - PortGroupIdx
     - Index of the switch.
   * - [in]
     - PortMode
     - port group mode for EthIfSwtPortGroup.

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
     - group mode could not be changed.

EthIf_StartAllPorts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthIf_StartAllPorts(void)

Request to set all configured and affected EthSwtPorts to ETH_MODE_ACTIVE.

**Sync/Async**
   FALSE

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
     - Request was accepted.
   * - E_NOT_OK
     - Request was rejected.

EthIf_SetSwitchMgmtInfo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthIf_SetSwitchMgmtInfo(uint8 CtrlIdx, Eth_BufIdxType BufIdx, EthSwt_MgmtInfoType *MgmtInfoPtr)

Provides additional management information along to an Ethernet frame that requires special treatment within the Switch.

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
     - CtrlIdx
     - Index of an Ethernet Interface controller.
   * - [in]
     - BufIdx
     - Ethernet Tx Buffer index.
   * - [in]
     - MgmtInfoPtr
     - Pointer to the management information.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Management infos successfully set
   * - E_NOT_OK
     - Setting of management infos failed.

EthIf_GetRxMgmtObject
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthIf_GetRxMgmtObject(uint8 CtrlIdx, Eth_DataType *DataPtr, EthSwt_MgmtObjectType **MgmtObjectPtr)

Request the MgmtObject of the (in this context) unique DataPtr.

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
     - CtrlIdx
     - Index of an Ethernet Interface controller.
   * - [in]
     - DataPtr
     - Ethernet data pointer.
   * - [out]
     - MgmtObjectPtr
     - Pointer to the management object.

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
     - management object could not be obtained.

EthIf_GetTxMgmtObject
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthIf_GetTxMgmtObject(uint8 CtrlIdx, Eth_BufIdxType BufIdx, EthSwt_MgmtObjectType **MgmtObjectPtr)

Request the MgmtObject of the (in this context) unique BufIdx.

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
     - CtrlIdx
     - Index of an Ethernet Interface controller.
   * - [in]
     - BufIdx
     - Ethernet Rx Buffer index.
   * - [out]
     - MgmtObjectPtr
     - Pointer to the management object.

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
     - management object could not be obtained.

EthIf_SwitchEnableTimeStamping
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthIf_SwitchEnableTimeStamping(uint8 CtrlIdx, Eth_BufIdxType BufIdx, EthSwt_MgmtInfoType *MgmtInfo)

Activates egress time stamping on a dedicated message object, addressed by CtrlIdx and BufIdx.

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
     - CtrlIdx
     - Index of an Ethernet Interface controller.
   * - [in]
     - BufIdx
     - Index of the message buffer, where Application expects egress time stamping.
   * - [out]
     - MgmtInfo
     - Management information.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Time stamping on egress successfully enabled.
   * - E_NOT_OK
     - Enabling of time stamping on egress has been failed.

EthIf_VerifyConfig
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthIf_VerifyConfig(uint8 SwitchIdx, boolean *Result)

Forwarded to EthSwt_VerifyConfig. EthSwt_VerifyConfig verifies the Switch Configuration depending on the HW-Architecture, HW-capability and the intended accuracy of this verification.

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
     - SwitchIdx
     - Index of the switch within the context of the Ethernet Interface.
   * - [out]
     - Result
     - Result of verification, TRUE: configureation verified ok, FALSE:configuraton values found corrupted

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Configuration verificaton succeeded.
   * - E_NOT_OK
     - Configuration verification not succeeded.

EthIf_SetForwardingMode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthIf_SetForwardingMode(uint8 SwitchIdx, boolean mode)

Control of switch frame forwarding.

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
     - SwitchIdx
     - Index of the switch within the context of the Ethernet Interface.
   * - [in]
     - mode
     - True Forwarding enabled, False Forwarding disabled.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - request was accepted.
   * - E_NOT_OK
     - request was rejected.

EthIf_GetTrcvSignalQuality
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthIf_GetTrcvSignalQuality(uint8 TrcvIdx, EthIf_SignalQualityResultType *ResultPtr)

Retrieves the signal quality of the link of the given Ethernet transceiver.

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
     - Index of the transceiver within the context of the Ethernet Interface.
   * - [out]
     - ResultPtr
     - Pointer to the memory where the signal quality in percent shall be stored..

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The signal quality retrieved successfully.
   * - E_NOT_OK
     - The signal quality not retrieved successfully.

EthIf_GetSwitchPortSignalQuality
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthIf_GetSwitchPortSignalQuality(uint8 SwitchIdx, uint8 SwitchPortIdx, EthIf_SignalQualityResultType *ResultPtr)

Retrieves the signal quality of the link of the given Ethernet switch port.

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
     - SwitchIdx
     - Index of the Ethernet switch within the context of the Ethernet Interface.
   * - [in]
     - SwitchPortIdx
     - Index of the Ethernet switch port within the context of the Ethernet Interface.
   * - [out]
     - ResultPtr
     - Pointer to the memory where the signal quality in percent shall be stored..

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The signal quality retrieved successfully.
   * - E_NOT_OK
     - The signal quality not retrieved successfully.

EthIf_ClearTrcvSignalQuality
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthIf_ClearTrcvSignalQuality(uint8 TrcvIdx)

Clear the stored signal quality of the link of the given Ethernet transceiver.

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
     - Index of the transceiver within the context of the Ethernet Interface.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The signal quality cleared successfully.
   * - E_NOT_OK
     - The signal quality cleared not successfully.

EthIf_ClearSwitchPortSignalQuality
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthIf_ClearSwitchPortSignalQuality(uint8 SwitchIdx, uint8 SwitchPortIdx)

Clear the stored signal quality of the link of the given Ethernet switch port.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant for different Ethernet switch indexes and Ethernet Switch port indexes. Non reentrant for the same SwitchPortIdx.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - SwitchIdx
     - Index of the Ethernet switch within the context of the Ethernet Interface.
   * - [in]
     - SwitchPortIdx
     - Index of the Ethernet switch port within the context of the Ethernet Interface.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The signal quality cleared successfully.
   * - E_NOT_OK
     - The signal quality cleared not successfully.

EthIf_SetPhyTestMode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthIf_SetPhyTestMode(uint8 TrcvIdx, EthTrcv_PhyTestModeType Mode)

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
     - Index of the transceiver within the context of the Ethernet Interface.
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

EthIf_SetPhyLoopbackMode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthIf_SetPhyLoopbackMode(uint8 TrcvIdx, EthTrcv_PhyLoopbackModeType Mode)

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
     - Index of the transceiver within the context of the Ethernet Interface.
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

EthIf_SetPhyTxMode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthIf_SetPhyTxMode(uint8 TrcvIdx, EthTrcv_PhyTxModeType Mode)

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
     - Index of the transceiver within the context of the Ethernet Interface.
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

EthIf_GetCableDiagnosticsResult
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthIf_GetCableDiagnosticsResult(uint8 TrcvIdx, EthTrcv_CableDiagResultType *ResultPtr)

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
     - Index of the transceiver within the context of the Ethernet Interface.
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

EthIf_GetPhyIdentifier
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthIf_GetPhyIdentifier(uint8 TrcvIdx, uint32 *OrgUniqueIdPtr, uint8 *ModelNrPtr, uint8 *RevisionNrPtr)

Obtains the PHY identifier of the Ethernet Interface according to IEEE 802.3-2015.

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
     - Index of the transceiver within the context of the Ethernet Interface.
   * - [out]
     - OrgUniqueIdPtr
     - Pointer to the memory where the Organizationally Unique Identifier shall be stored.
   * - [out]
     - ModelNrPtr
     - Pointer to the memory where the Manufacturer’s Model Number shall be stored.
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

EthIf_GetSwitchPortMode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthIf_GetSwitchPortMode(uint8 SwitchIdx, uint8 SwitchPortIdx, Eth_ModeType *PortModePtr)

Obtains the mode of the indexed switch port.

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
     - SwitchIdx
     - Index of the switch within the context of the Ethernet Switch Driver.
   * - [in]
     - SwitchPortIdx
     - Index of the port at the addressed switch.
   * - [out]
     - PortModePtr
     - ETH_MODE_DOWN: The Ethernet switch port of the given Ethernet switch is disabled ETH_MODE_ACTIVE: The Ethernet switch port of the given Ethernet switch is enabled

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
     - The mode of the indexed switch port could not be obtained, or the function is called in state ETHSWT_STATE_UNINIT or ETHSWT_STATE_INIT..

EthIf_SwitchPortGetLinkState
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthIf_SwitchPortGetLinkState(uint8 SwitchIdx, uint8 SwitchPortIdx, EthTrcv_LinkStateType *LinkStatePtr)

Obtains the link state of the indexed switch port.

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
     - SwitchIdx
     - Index of the switch within the context of the Ethernet Switch Driver.
   * - [in]
     - SwitchPortIdx
     - Index of the port at the addressed switch.
   * - [in]
     - LinkStatePtr
     - ETHTRCV_LINK_STATE_DOWN: Switch port is disconnected ETHTRCV_LINK_STATE_ACTIVE: Switch port is connected

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
     - Link state of the indexed switch port could not be obtained, or the function is called in state ETHSWT_STATE_UNINIT or ETHSWT_STATE_INIT.

EthIf_TransceiverGetLinkState
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthIf_TransceiverGetLinkState(uint8 TrcvIdx, EthTrcv_LinkStateType *LinkStatePtr)

Obtains the link state of the indexed transceiver.

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
   * - [out]
     - LinkStatePtr
     - ETHTRCV_LINK_STATE_DOWN: transceiver is disconnected ETHTRCV_LINK_STATE_ACTIVE: transceiver is connected

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

EthIf_SwitchPortGetBaudRate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthIf_SwitchPortGetBaudRate(uint8 SwitchIdx, uint8 SwitchPortIdx, EthTrcv_BaudRateType *BaudRatePtr)

Obtains the baud rate of the indexed switch port.

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
     - SwitchIdx
     - Index of the switch within the context of the Ethernet Switch Driver.
   * - [in]
     - SwitchPortIdx
     - Index of the port at the addressed switch.
   * - [out]
     - BaudRatePtr
     - ETHTRCV_BAUD_RATE_10MBIT: 10MBit connection ETHTRCV_BAUD_RATE_100MBIT: 100MBit connection ETHTRCV_BAUD_RATE_1000MBIT: 1000MBit connection ETHTRCV_BAUD_RATE_2500MBIT: 2500MBit connection

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
     - Baud rate of the indexed switch port could not be obtained, or the function is called in state ETHSWT_STATE_UNINIT or ETHSWT_STATE_INIT

EthIf_TransceiverGetBaudRate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthIf_TransceiverGetBaudRate(uint8 TrcvIdx, EthTrcv_BaudRateType *BaudRatePtr)

Obtains the baud rate of the indexed transceiver.

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
   * - [out]
     - BaudRatePtr
     - ETHTRCV_BAUD_RATE_10MBIT: 10MBit connection ETHTRCV_BAUD_RATE_100MBIT: 100MBit connection ETHTRCV_BAUD_RATE_1000MBIT: 1000MBit connection ETHTRCV_BAUD_RATE_2500MBIT: 2500MBit connection

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

EthIf_SwitchPortGetDuplexMode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthIf_SwitchPortGetDuplexMode(uint8 SwitchIdx, uint8 SwitchPortIdx, EthTrcv_DuplexModeType *DuplexModePtr)

Obtains the duplex mode of the indexed switch port.

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
     - SwitchIdx
     - Index of the switch within the context of the Ethernet Switch Driver.
   * - [in]
     - SwitchPortIdx
     - Index of the port at the addressed switch.
   * - [out]
     - DuplexModePtr
     - ETHTRCV_DUPLEX_MODE_HALF: half duplex connections ETHTRCV_DUPLEXMODE_FULL: full duplex connection

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
     - duplex mode of the indexed switch port could not be obtained, or the function is called in state ETHSWT_STATE_UNINIT or ETHSWT_STATE_INIT.

EthIf_TransceiverGetDuplexMode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthIf_TransceiverGetDuplexMode(uint8 TrcvIdx, EthTrcv_DuplexModeType *DuplexModePtr)

Obtains the duplex mode of the indexed transceiver.

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
   * - [out]
     - DuplexModePtr
     - ETHTRCV_DUPLEX_MODE_HALF: half duplex connections ETHTRCV_DUPLEXMODE_FULL: full duplex connection

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
     - transceiver could not be initialized

EthIf_SwitchPortGetCounterValues
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthIf_SwitchPortGetCounterValues(uint8 SwitchIdx, uint8 SwitchPortIdx, Eth_CounterType *CounterPtr)

Reads a list with drop counter values of the corresponding port of the switch.

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
     - SwitchIdx
     - Index of the switch within the context of the Ethernet Switch Driver.
   * - [in]
     - SwitchPortIdx
     - Index of the port at the addressed switch.
   * - [out]
     - CounterPtr
     - counter values according to IETF RFC 1757, RFC 1643 and RFC 2233

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
     - counter values read failure

EthIf_SwitchPortGetCounterValue
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthIf_SwitchPortGetCounterValue(uint8 SwitchIdx, uint8 SwitchPortIdx, Eth_CounterType *CounterPtr)



**Sync/Async**


**Reentrancy**



**Return type**
   Std_ReturnType


EthIf_SwitchPortGetRxStats
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthIf_SwitchPortGetRxStats(uint8 SwitchIdx, uint8 SwitchPortIdx, Eth_RxStatsType *RxStatsPtr)

Returns a list of statistic counters defined with Eth_RxTatsType.The majority of these Counters are derived from the IETF RFC2819.

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
     - SwitchIdx
     - Index of the switch within the context of the Ethernet Switch Driver.
   * - [in]
     - SwitchPortIdx
     - Index of the port at the addressed switch.
   * - [out]
     - RxStatsPtr
     - List of values according to IETF RFC 2819 (Remote Network Monitoring Management Information Base)

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
     - drop counter could not be obtained

EthIf_SwitchPortGetTxStats
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthIf_SwitchPortGetTxStats(uint8 SwitchIdx, uint8 SwitchPortIdx, Eth_TxStatsType *TxStatsPtr)

List of values to read statistic values for transmission.

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
     - SwitchIdx
     - Index of the switch within the context of the Ethernet Switch Driver.
   * - [in]
     - SwitchPortIdx
     - Index of the port at the addressed switch.
   * - [out]
     - TxStatsPtr
     - List of values to read statistic values for transmission.

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
     - Tx-statistics could not be obtained

EthIf_SwitchPortGetTxErrorCounterValues
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthIf_SwitchPortGetTxErrorCounterValues(uint8 SwitchIdx, uint8 SwitchPortIdx, Eth_TxErrorCounterValuesType *TxStatsPtr)

List of values to read statistic error counter values for transmission from.

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
     - SwitchIdx
     - Index of the switch within the context of the Ethernet Switch Driver.
   * - [in]
     - SwitchPortIdx
     - Index of the port at the addressed switch.
   * - [out]
     - TxStatsPtr
     - List of values to read statistic error counter values for transmission.

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
     - Tx-statistics could not be obtained

EthIf_SwitchPortGetMacLearningMode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthIf_SwitchPortGetMacLearningMode(uint8 SwitchIdx, uint8 SwitchPortIdx, EthSwt_MacLearningType *MacLearningModePtr)

Returns the MAC learning mode.

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
     - SwitchIdx
     - Index of the switch within the context of the Ethernet Switch Driver.
   * - [in]
     - SwitchPortIdx
     - Index of the port at the addressed switch.
   * - [out]
     - MacLearningModePtr
     - Defines whether MAC addresses shall be learned and if they shall be learned in software or hardware.

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
     - configuration could be persistently reset

EthIf_GetSwitchPortIdentifier
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthIf_GetSwitchPortIdentifier(uint8 SwitchIdx, uint8 SwitchPortIdx, uint32 *OrgUniqueIdPtr, uint8 *ModelNrPtr, uint8 *RevisionNrPtr)

Returns the MAC learning mode.

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
     - SwitchIdx
     - Index of the switch within the context of the Ethernet Switch Driver.
   * - [in]
     - SwitchPortIdx
     - Index of the port at the addressed switch.
   * - [out]
     - OrgUniqueIdPtr
     - Pointer to the memory where the Organizationally Unique Identifier (OUI) shall be stored.
   * - [out]
     - ModelNrPtr
     - Pointer to the memory where the Manufacturer’s Model Number shall be stored.
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
     - organizationally unique identifier of the Ethernet transceiver could be read.
   * - E_NOT_OK
     - organizationally unique identifier of the Ethernet transceiver could not be obtained (i.e. OUI is not available).

EthIf_GetSwitchIdentifier
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthIf_GetSwitchIdentifier(uint8 SwitchIdx, uint32 *OrgUniqueIdPtr)

Obtain the Organizationally Unique Identifier that is given by the IEEE of the indexed Ethernet switch.

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
     - SwitchIdx
     - Index of the switch within the context of the Ethernet Switch Driver.
   * - [out]
     - OrgUniqueIdPtr
     - Pointer to the memory where the Organizationally Unique Identifier (OUI) shall be stored.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - organizationally unique identifier of the Ethernet switch could be read..
   * - E_NOT_OK
     - organizationally unique identifier of the Ethernet switch could not be read (i.e. no OUI is available for this Ethernet switch).

EthIf_WritePortMirrorConfiguration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthIf_WritePortMirrorConfiguration(uint8 MirroredSwitchIdx, const EthSwt_PortMirrorCfgType *PortMirrorConfigurationPtr)

Store the given port mirror configuration in a shadow buffer in the Ethernet switch driver for the given MirroredSwitchIdx.

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
     - MirroredSwitchIdx
     - Index of the switch within the context of the Ethernet Switch Driver, where the Ethernet switch port is located, that has to be mirrored.
   * - [out]
     - PortMirrorConfigurationPtr
     - Pointer to the memory where the port configuration shall be used.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - the port mirror configuration for the indexed Ethernet switch port was written.
   * - E_NOT_OK
     - the port mirror configuration for the indexed Ethernet switch port was not written. (i.e. indexed ethernet switch is not available).

EthIf_ReadPortMirrorConfiguration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthIf_ReadPortMirrorConfiguration(uint8 MirroredSwitchIdx, EthSwt_PortMirrorCfgType *PortMirrorConfigurationPtr)

Obtain the port mirror configuration of the given Ethernet switch.

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
     - MirroredSwitchIdx
     - Index of the switch within the context of the Ethernet Switch Driver, where the Ethernet switch port is located, that has to be mirrored.
   * - [out]
     - PortMirrorConfigurationPtr
     - Pointer to the memory where the port configuration shall be stored.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - the port mirror configuration for the indexed Ethernet switch port was red successfully.
   * - E_NOT_OK
     - the port mirror configuration for the indexed Ethernet switch was not red successfully. (i.e. indexed Ethernet switch is not available.

EthIf_DeletePortMirrorConfiguration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthIf_DeletePortMirrorConfiguration(uint8 MirroredSwitchIdx)

Delete the stored port mirror configuration of the given MirroredSwitchIdx.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant Reentrant for different MirroredSwitchIdx. Non reentrant for the same SwitchIdx.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - MirroredSwitchIdx
     - Index of the switch within the context of the Ethernet Switch Driver.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Port mirror configuration was deleted successfully.
   * - E_NOT_OK
     - Port mirror configuration was not deleted successfully. (e.g. the port mirroring is enabled)

EthIf_GetPortMirrorState
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthIf_GetPortMirrorState(uint8 SwitchIdx, uint8 PortIdx, EthSwt_PortMirrorStateType *PortMirrorStatePtr)

Obtain the current status of the port mirroring for the indexed Ethernet switch port.

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
     - SwitchIdx
     - Index of the switch within the context of the Ethernet Switch Driver.
   * - [in]
     - PortIdx
     - Index of the port at the addressed switch.
   * - [out]
     - PortMirrorStatePtr
     - Pointer to the memory where the port mirroring state of the given Ethernet switch port shall be stored.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - the port mirroring state for the indexed Ethernet switch port returned successfully..
   * - E_NOT_OK
     - the port mirror configuration for the indexed Ethernet switch returned not successfully. (i.e. indexed ethernet switch port is not available)

EthIf_SetPortMirrorState
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthIf_SetPortMirrorState(uint8 MirroredSwitchIdx, uint8 PortIdx, EthSwt_PortMirrorStateType PortMirrorState)

Request to set the given port mirroring state of the port mirror configuration for the given Ethernet switch.

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
     - MirroredSwitchIdx
     -
   * - [in]
     - PortIdx
     - Index of the port at the addressed switch.
   * - [out]
     - PortMirrorState
     - Contain the requested port mirroring state either PORT_MIRRORING_ENABLED or PORT_MIRRORING_DISABLED.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - the requested port mirroring state for the indexed Ethernet switch port was set successfully.
   * - E_NOT_OK
     - the requested port mirroring state for the indexed Ethernet switch was not set successfully.

EthIf_SetPortTestMode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthIf_SetPortTestMode(uint8 SwitchIdx, uint8 PortIdx, EthTrcv_PhyTestModeType Mode)

Activates a given test mode of the indexed Ethernet switch port.

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
     - SwitchIdx
     - Index of the switch within the context of the Ethernet Switch Driver.
   * - [in]
     - PortIdx
     - Index of the port at the addressed switch.
   * - [out]
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
     - the port test mode for the indexed Ethernet switch port was set successfully.
   * - E_NOT_OK
     - the port test mode for the indexed Ethernet switch was not set successfully.

EthIf_SetPortLoopbackMode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthIf_SetPortLoopbackMode(uint8 SwitchIdx, uint8 PortIdx, EthTrcv_PhyLoopbackModeType Mode)

Activates a given test loop-back mode of the indexed Ethernet switch port..

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
     - SwitchIdx
     - Index of the switch within the context of the Ethernet Switch Driver.
   * - [in]
     - PortIdx
     - Index of the port at the addressed switch.
   * - [out]
     - Mode
     - Loop-back mode to be activated.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - the port mirroring loop-back back mode for the indexed Ethernet switch port was activated successfully.
   * - E_NOT_OK
     - the port mirroring loop-back back mode for the indexed Ethernet switch port was not activated successfully.

EthIf_SetPortTxMode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthIf_SetPortTxMode(uint8 SwitchIdx, uint8 PortIdx, EthTrcv_PhyTxModeType Mode)

Activates a given transmission mode of the indexed Ethernet switch port.

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
     - SwitchIdx
     - Index of the switch within the context of the Ethernet Switch Driver.
   * - [in]
     - PortIdx
     - Index of the port at the addressed switch.
   * - [out]
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
     - the port Tx mode for the indexed Ethernet switch port was activated successfully.
   * - E_NOT_OK
     - the port Tx mode for the indexed Ethernet switch port was not activated successfully.

EthIf_GetPortCableDiagnosticsResult
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthIf_GetPortCableDiagnosticsResult(uint8 SwitchIdx, uint8 PortIdx, EthTrcv_CableDiagResultType *ResultPtr)

Retrieves the cable diagnostics result of the indexed Ethernet switch port respectively the referenced Ethernet Transceiver Driver.

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
     - SwitchIdx
     - Index of the switch within the context of the Ethernet Switch Driver.
   * - [in]
     - PortIdx
     - Index of the port at the addressed switch.
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
     - the port cable diagnostic result for the indexed Ethernet switch port was obtained successfully.
   * - E_NOT_OK
     - the port cable diagnostic result for the indexed Ethernet switch port was not obtained successfully.

EthIf_RunPortCableDiagnostic
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthIf_RunPortCableDiagnostic(uint8 SwitchIdx, uint8 PortIdx)

Trigger the cable diagnostics of the given Ethernet Switch port (PortIdx) by calling EthTrcv_Run CableDiagnostic of the referenced Ethernet transceiver.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant Reentrant for different SwitchIdx and PortIdx. Non reentrant for the same SwitchIdx and PortIdx.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - SwitchIdx
     - Index of the switch within the context of the Ethernet Switch Driver.
   * - [in]
     - PortIdx
     - Index of the port at the addressed switch.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The trigger to run the cable diagnostic has been accepted.
   * - E_NOT_OK
     - The trigger to run the cable diagnostic has not been accepted.

EthIf_RunCableDiagnostic
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthIf_RunCableDiagnostic(uint8 TrcvIdx)

Trigger the cable diagnostics for the given Ethernet transceiver..

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant Reentrant for different TrcvIdx. Non reentrant for the same TrcvIdx..

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - TrcvIdx
     - Index of the switch within the context of the Ethernet Switch Driver.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The trigger has been accepted..
   * - E_NOT_OK
     - The trigger has not been accepted.

EthIf_SwitchGetCfgDataRaw
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthIf_SwitchGetCfgDataRaw(uint8 SwitchIdx, uint32 Offset, uint16 Length, uint8 *BufferPtr)

Retrieves the data in memory of the indexed Ethernet switch in variable length.

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
     - SwitchIdx
     - Index of the Ethernet switch within the context of the Ethernet Switch Driver.
   * - [in]
     - Offset
     - Offset of the Ethernet switch memory from where the reading starts.
   * - [in]
     - Length
     - Length of data in bytes that shall be copied.
   * - [out]
     - BufferPtr
     - Pointer to the location where the data shall be copied.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The trigger has been accepted..
   * - E_NOT_OK
     - The trigger has not been accepted.

EthIf_SwitchGetCfgDataInfo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthIf_SwitchGetCfgDataInfo(uint8 SwitchIdx, uint32 *DataSizePtr, uint32 *DataAdressPtr)

Retrieves the data in memory of the indexed Ethernet switch in variable length.

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
     - SwitchIdx
     - Index of the Ethernet switch within the context of the Ethernet Switch Driver.
   * - [out]
     - DataSizePtr
     - Pointer to the location where the total size of the configuration data shall be copied.
   * - [out]
     - DataAdressPtr
     - Pointer to the location where the start address of the configuration registers shall be copied.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - the data was obtained successfully.
   * - E_NOT_OK
     - the data was not obtained successfully. (i.e. indexedEthernet switch is not available).

EthIf_SwitchPortGetMaxFIFOBufferFillLevel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthIf_SwitchPortGetMaxFIFOBufferFillLevel(uint8 SwitchPortIdx, uint8 PortIdx, uint8 SwitchPortEgressFifoIdx, uint32 *SwitchPortEgressFifoBufferLevelPtr)

The function retrieves the maximum amount of allocated FIFO buffer of the indexed Ethernet switch egress port.If the Ethernet switch hardware does not support Ethernet switch port based maximal FIFO buffer level, the content of SwitchPortEgressFifoBufferLevelPtr shall be set to 0xFFFFFFFF.This API may be called by e.g. a CDD.

**Sync/Async**
   FALSE

**Reentrancy**
   Reentrant Reentrant for different SwitchIdx and PortIdx. Non reentrant for the same SwitchIdx and PortIdx.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * -
     - SwitchPortIdx
     -
   * - [in]
     - PortIdx
     - Index of the port at the addressed switch.
   * - [out]
     - SwitchPortEgressFifoIdx
     - Index of the egress FIFO of the addressed Ethernet switch port.
   * - [out]
     - SwitchPortEgressFifoBufferLevelPtr
     - Pointer to a memory location, where the maximum amount of allocated FIFO buffer (in bytes) since the last read out shall be stored.

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
     - The maximal FIFO buffer level could not be obtained.

EthIf_TransceiverGetMacMethod
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthIf_TransceiverGetMacMethod(uint8 TrcvIdx, EthTrcv_MacMethodType *MacModePtr)

Obtains the media access mode of the transceiver..

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
     - success..
   * - E_NOT_OK
     - transceiver request has not been accepted.

EthIf_EthGetSpiStatus
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthIf_EthGetSpiStatus(uint8 CtrlIdx, Eth_SpiStatusType *SpiStatusPtr)

When MACPHY controller are used, obtains the SPI interface status..

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
     - CtrlIdx
     - Index of the controller within the context of the Ethernet controller Driver.
   * - [out]
     - SpiStatusPtr
     - Status of the SPI interface.

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
     - Controller request has not been accepted..

EthIf_RxIndication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void EthIf_RxIndication(uint8 CtrlIdx, Eth_FrameType FrameType, boolean IsBroadcast, const uint8 *PhysAddrPtr, const Eth_DataType *DataPtr, uint16 DataLen, TimeTupleType *IngressTimeTuplePtr, Eth_BufIdxType RxHandleId)

Receive indication of an Ethernet frame which was received by the indexed controller.

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
     - CtrlIdx
     - Index of the physical Ethernet controller within the context of the Ethernet Interface.
   * - [in]
     - FrameType
     - Frame type of received Ethernet frame.
   * - [in]
     - IsBroadcast
     - parameter to indicate a broadcast frame.
   * - [in]
     - PhysAddrPtr
     - Pointer to Physical source address (MAC address in network byte order) of received Ethernet frame.
   * - [in]
     - DataPtr
     - Pointer to payload of received Ethernet frame.
   * - [in]
     - DataLen
     - Length (bytes) of the payload in received frame.
   * - [in]
     - IngressTimeTuplePtr
     - Pointer to ingress timestamp provided as time tuple.
   * - [in]
     - RxHandleId
     - Unique receive handle id provided by the Ethernet Driver, to identify the ingress queue element per hysical Ethernet controller.

**Return type**
   void


EthIf_TxConfirmation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void EthIf_TxConfirmation(uint8 CtrlIdx, Eth_BufIdxType BufIdx, Std_ReturnType Result)

Confirms frame transmission by the indexed controller.

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
     - CtrlIdx
     - Index of the physical Ethernet controller within the context of the Ethernet Interface.
   * - [in]
     - BufIdx
     - Index of the transmitted buffer.
   * - [in]
     - Result
     - E_OK: The transmission was successful, E_NOT_OK: The transmission failed.

**Return type**
   void


EthIf_CtrlModeIndication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void EthIf_CtrlModeIndication(uint8 CtrlIdx, Eth_ModeType CtrlMode)

Called asynchronously when mode has been read out.

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant for the same CtrlIdx, reentrant for different

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - CtrlIdx
     - Index of the physical Ethernet controller within the context of the Ethernet Interface.
   * - [in]
     - CtrlMode
     - Notified Ethernet controller mode.

**Return type**
   void


EthIf_TrcvModeIndication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void EthIf_TrcvModeIndication(uint8 TrcvIdx, Eth_ModeType TrcvMode)

Called asynchronously when a mode change has been read out.

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant for the same CtrlIdx, reentrant for different

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - TrcvIdx
     - Index of the Ethernet transceiver within the context of the Ethernet Interface.
   * - [in]
     - TrcvMode
     - Notified Ethernet transceiver mode.

**Return type**
   void


EthIf_SwitchPortModeIndication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void EthIf_SwitchPortModeIndication(uint8 SwitchIdx, uint8 SwitchPortIdx, Eth_ModeType PortMode)

The EthIf shall determine the expected notifications based on the EthSwtPort configuration.In case the EthSwtPort references an EthTrcv the EthIf expects a notification from the EthTrcv via API

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
     - SwitchIdx
     - Index of the switch.
   * - [in]
     - SwitchPortIdx
     - Index of the port at the addressed switch.
   * - [in]
     - PortMode
     - Notified Ethernet Switch port mode.

**Return type**
   void


EthIf_SleepIndication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void EthIf_SleepIndication(uint8 TrcvIdx)

This API is called by the corresponding EthTrcv, if a sleep indication was detected on the network.

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
     - Index of the Ethernet transceiver within the context of the Ethernet Interface.

**Return type**
   void

