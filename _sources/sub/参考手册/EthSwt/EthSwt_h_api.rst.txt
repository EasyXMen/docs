


提供的服务 Services
------------------------------------------------------------------
EthSwt_Init
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void EthSwt_Init(const EthSwt_ConfigType *CfgPtr)

Initializes the Ethernet Switch Driver.

**Sync/Async**
   TRUE

**Reentrancy**
   FALSE

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - CfgPtr
     - Pointer to the configuration data of the EthSwt module.

**Return type**
   void


EthSwt_GetVersionInfo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void EthSwt_GetVersionInfo(Std_VersionInfoType *versioninfo)

Returns the version information.

**Sync/Async**
   TRUE

**Reentrancy**
   TRUE

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


EthSwt_SetSwitchPortMode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthSwt_SetSwitchPortMode(uint8 SwitchIdx, uint8 SwitchPortIdx, Eth_ModeType PortMode)

Enables/disables the indexed switch port.

**Sync/Async**
   TRUE

**Reentrancy**
   FALSE

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - SwitchIdx
     - Index of the switch within the context of the Ethernet Switch Driver
   * - [in]
     - SwitchPortIdx
     - Index of the port at the addressed switch
   * - [in]
     - PortMode
     - ETH_MODE_DOWN: Disable the addressed Ethernet switch port at the given Ethernet switch ETH_MODE_ACTIVE: Enable the addressed Ethernet switch port at the given Ethernet switch

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
     - The indexed switch port could not be set to Port Mode, or the function is called instate ETHSWT_STATE_UNINIT or ETHSWT_STATE_INIT.

EthSwt_GetSwitchPortMode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthSwt_GetSwitchPortMode(uint8 SwitchIdx, uint8 SwitchPortIdx, Eth_ModeType *SwitchModePtr)

Obtains the mode of the indexed switch port.

**Sync/Async**
   TRUE

**Reentrancy**
   FALSE

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - SwitchIdx
     - Index of the switch within the context of the Ethernet Switch Driver
   * - [in]
     - SwitchPortIdx
     - Index of the port at the addressed switch
   * - [out]
     - SwitchModePtr
     - ETH_MODE_DOWN: The Ethernet switch port of the given Ethernet switch is disabled. ETH_MODE_ACTIVE: The Ethernet switch port of the given Ethernet switch is enabled

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
     - The mode of the indexed switch port could not be obtained, or the function is called in state ETHSWT_STATE_UNINIT or ETHSWT_STATE_INIT.

EthSwt_GetDuplexMode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthSwt_GetDuplexMode(uint8 SwitchIdx, uint8 SwitchPortIdx, EthTrcv_DuplexModeType *DuplexModePtr)

Obtains the duplex mode of the indexed switch port.

**Sync/Async**
   TRUE

**Reentrancy**
   FALSE

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - SwitchIdx
     - Index of the switch within the context of the Ethernet Switch Driver
   * - [in]
     - SwitchPortIdx
     - Index of the port at the addressed switch
   * - [out]
     - DuplexModePtr
     - ETHTRCV_DUPLEX_MODE_HALF: half duplex connections ETHTRCV_DUPLEXMODE_FULL: fullduplex connection switch port of the given Ethernet switch is enabled.

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

EthSwt_GetLinkState
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthSwt_GetLinkState(uint8 SwitchIdx, uint8 SwitchPortIdx, EthTrcv_LinkStateType *LinkStatePtr)

Obtains the link state of the indexed switch port.

**Sync/Async**
   TRUE

**Reentrancy**
   FALSE

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - SwitchIdx
     - Index of the switch within the context of the Ethernet Switch Driver
   * - [in]
     - SwitchPortIdx
     - Index of the port at the addressed switch
   * - [out]
     - LinkStatePtr
     - ETHTRCV_LINK_STATE_DOWN: Switch port is disconnected ETHTRCV_LINK_STATE_ACTIVE: Switch port is connected.

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

EthSwt_GetBaudRate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthSwt_GetBaudRate(uint8 SwitchIdx, uint8 SwitchPortIdx, EthTrcv_BaudRateType *BaudRatePtr)

Obtains the baud rate of the indexed switch port.

**Sync/Async**
   TRUE

**Reentrancy**
   FALSE

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - SwitchIdx
     - Index of the switch within the context of the Ethernet Switch Driver
   * - [in]
     - SwitchPortIdx
     - Index of the port at the addressed switch
   * - [out]
     - BaudRatePtr
     - ETHTRCV_BAUD_RATE_10MBIT: 10MBit connection ETHTRCV_BAUD_RATE_100MBIT: 100MBit connection ETHTRCV_BAUD_RATE_1000MBIT: 1000MBit connection ETHTRCV_BAUD_RATE_2500MBIT: 2500MBit connection.

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
     - Baud rate of the indexed switch port could not be obtained, or the function is called in state ETHSWT_STATE_UNINIT or ETHSWT_STATE_INIT.

EthSwt_StartSwitchPortAutoNegotiation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthSwt_StartSwitchPortAutoNegotiation(uint8 SwitchIdx, uint8 SwitchPortIdx)

Starts the auto-negotiation of the indexed switch port.

**Sync/Async**
   TRUE

**Reentrancy**
   FALSE

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - SwitchIdx
     - Index of the switch within the context of the Ethernet Switch Driver
   * - [in]
     - SwitchPortIdx
     - Index of the port at the addressed switch

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
     - Automatic negotiation could not be started for the indexed switch port, or the function is called in state ETHSWT_STATE_UNINIT or ETHSWT_STATE_INIT.

EthSwt_CheckWakeup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthSwt_CheckWakeup(uint8 SwitchIdx)

API is called by EthIf.The Ethernet switch driver request to check for a wake-up at all Ethernet switch ports which reference an EthTrcv.For those Ethernet switch ports the call is forwarded to the referenced EthTrcv.The function could be called in context of an interrupt service routine or on task leve.

**Sync/Async**
   TRUE

**Reentrancy**
   FALSE

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - SwitchIdx
     - Index of the switch within the context of the Ethernet Switch Driver

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - request to check for a wake-up is accepted.
   * - E_NOT_OK
     - request to check for a wake-up is not accepted.

EthSwt_GetSwitchPortWakeupReason
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthSwt_GetSwitchPortWakeupReason(uint8 SwitchIdx, uint8 SwitchPortIdx, EthTrcv_WakeupReasonType *Reason)

This function obtains the wake up reasons of the the indexed Ethernet switch port by calling Eth Trcv_GetBusWuReason(...) of the referenced EthTrcv.

**Sync/Async**
   TRUE

**Reentrancy**
   FALSE

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
     - Index of the Ethernet switch port index in the context of the Ethernet switch driver.
   * - [out]
     - Reason
     - Pointer to structure of least recent wakeup event, which was detected by the Ethernet switch port.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Ethernet switch port wake up reason request has been accepted.
   * - E_NOT_OK
     - Ethernet switch port wake up reason request has not been accepted.

EthSwt_GetPortMacAddr
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthSwt_GetPortMacAddr(uint8 SwitchIdx, const uint8 *MacAddrPtr, uint8 *PortIdxPtr)

Obtains the port over which this MAC-address at the indexed switch can be reached The result might be used for a DHCP-server which will need the port/MAC-resolution.If for the PortIdxPtr the maximal possible value (255) is returned the given MAC address cannot be reached via a port of this switch.If multiple ports were found the API returns E_NOT_OK.

**Sync/Async**
   TRUE

**Reentrancy**
   FALSE

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - SwitchIdx
     - Index of the switch within the context of the Ethernet Switch Driver
   * - [in]
     - MacAddrPtr
     - MAC-address for which a switch port is searched over which the node with this MAC-address can be reached
   * - [out]
     - PortIdxPtr
     - Pointer to the port index.

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
     - multiple ports were found.

EthSwt_EnableVlan
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthSwt_EnableVlan(uint8 SwitchIdx, uint8 SwitchPortIdx, uint16 VlanId, boolean Enable)

Enables or disables a pre-configured VLAN at a certain port of a switch.

**Sync/Async**
   TRUE

**Reentrancy**
   FALSE

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - SwitchIdx
     - Index of the switch within the context of the Ethernet Switch Driver
   * - [in]
     - SwitchPortIdx
     - Index of the port at the addressed switch
   * - [in]
     - VlanId
     - VLAN-ID to a preconfigured configuration on the given ingress port
   * - [in]
     - Enable
     - 1 = VLAN-configuration enabled 0 = VLAN-configuration disabled(frames with given VLAN-ID will be dropped)

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
     - buffer level could not be obtained.

EthSwt_SetMacLearningMode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthSwt_SetMacLearningMode(uint8 SwitchIdx, uint8 SwitchPortIdx, EthSwt_MacLearningType MacLearningMode)

Sets the MAC learning mode in one of the tree modes.

**Sync/Async**
   TRUE

**Reentrancy**
   FALSE

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - SwitchIdx
     - Index of the switch within the context of the Ethernet Switch Driver
   * - [in]
     - SwitchPortIdx
     - Index of the port at the addressed switch
   * - [in]
     - MacLearningMode
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

EthSwt_GetMacLearningMode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthSwt_GetMacLearningMode(uint8 SwitchIdx, uint8 SwitchPortIdx, EthSwt_MacLearningType *MacLearningMode)

Returns the MAC learning mode.

**Sync/Async**
   TRUE

**Reentrancy**
   FALSE

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - SwitchIdx
     - Index of the switch within the context of the Ethernet Switch Driver
   * - [in]
     - SwitchPortIdx
     - Index of the port at the addressed switch
   * - [out]
     - MacLearningMode
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
     - configuration could be persistently reset.

EthSwt_SetForwardingMode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthSwt_SetForwardingMode(uint8 SwitchIdx, boolean mode)

Configures switch to start or stop forwarding for all ports.This API call may be used during switch configuration verification.

**Sync/Async**
   TRUE

**Reentrancy**
   FALSE

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - SwitchIdx
     - Index of the switch within the context of the Ethernet Switch Driver
   * - [in]
     - mode
     - True Forewarding enabled, False Forwarding disabled

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - stopping of frame forwarding succeeded,
   * - E_NOT_OK
     - stopping of frame forwarding not succeeded.

EthSwt_SetPortTxMode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthSwt_SetPortTxMode(uint8 SwitchIdx, uint8 PortIdx, EthTrcv_PhyTxModeType Mode)

Activates a given transmission mode of the indexed Ethernet switch port.

**Sync/Async**
   TRUE

**Reentrancy**
   FALSE

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - SwitchIdx
     - Index of the switch within the context of the Ethernet Switch Driver
   * - [in]
     - PortIdx
     - Index of the port at the addressed switch
   * - [in]
     - Mode
     - Transmission mode to be activated

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

EthSwt_WritePortMirrorConfiguration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthSwt_WritePortMirrorConfiguration(uint8 MirroredSwitchIdx, const EthSwt_PortMirrorCfgType *PortMirrorConfigurationPtr)

Store the given port mirror configuration in a shadow buffer in the Ethernet switch driver for the given MirroredSwitchIdx.

**Sync/Async**
   TRUE

**Reentrancy**
   FALSE

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
   * - [in]
     - PortMirrorConfigurationPtr
     - Pointer of the port configuration, which shall be stored in a shadow buffer in the Ethernet switch driver.

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
     - the port mirror configuration for the indexed Ethernet switch port was not written.

EthSwt_ReadPortMirrorConfiguration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthSwt_ReadPortMirrorConfiguration(uint8 MirroredSwitchIdx, EthSwt_PortMirrorCfgType *PortMirrorConfigurationPtr)

Obtain the port mirror configuration of the given Ethernet switch.

**Sync/Async**
   TRUE

**Reentrancy**
   FALSE

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
   * - [in]
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
     - the port mirror configuration for the indexed Ethernet switch was not red successfully.

EthSwt_DeletePortMirrorConfiguration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthSwt_DeletePortMirrorConfiguration(uint8 MirroredSwitchIdx)

Delete the stored port mirror configuration of the given MirroredSwitchIdx.If no port mirror configuration was found for the given MirroredSwitchIdx, the return value shall be E_OK.

**Sync/Async**
   TRUE

**Reentrancy**
   FALSE

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
     - Port mirror configuration was not deleted successfully. (e.g. the port mirroring is enabled).

EthSwt_GetPortMirrorState
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthSwt_GetPortMirrorState(uint8 SwitchIdx, uint8 PortIdx, EthSwt_PortMirrorStateType *PortMirrorStatePtr)

Obtain the current status of the port mirroring for the indexed Ethernet switch port.

**Sync/Async**
   TRUE

**Reentrancy**
   FALSE

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - SwitchIdx
     - Index of the switch within the context of the Ethernet Switch Driver
   * - [in]
     - PortIdx
     - Index of the port at the addressed switch
   * - [out]
     - PortMirrorStatePtr
     - Pointer to the memory where the port mirroring state (either PORT_MIRRORING_ENABLED or PORT_MIRRORING_DISABLED)of the given Ethernet switch port shall be stored.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - the port mirroring state for the indexed Ethernet switch port returned successfully.
   * - E_NOT_OK
     - the port mirror configuration for the indexed Ethernet switch returned not successfully.

EthSwt_SetPortMirrorState
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType EthSwt_SetPortMirrorState(uint8 MirroredSwitchIdx, EthSwt_PortMirrorStateType PortMirrorState)

Request to set the given port mirroring state of the port mirror configuration for the given Ethernet switch.

**Sync/Async**
   TRUE

**Reentrancy**
   FALSE

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - MirroredSwitchIdx
     - Index of the Ethernet switch within the context of the Ethernet Switch Driver, where the port mirroring configuration is located that has to be enabled anddisabled, repectively.
   * - [in]
     - PortMirrorState
     - Contain the requested port mirroring state either PORT_MIRRORING_ENABLED or PORT_MIRRORING_DISABLED

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - the requested port mirroring state for the indexed Ethernet switch port was set successfully
   * - E_NOT_OK
     - the requested port mirroring state for the indexed Ethernet switch was not set successfully.

EthSwt_MainFunction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void EthSwt_MainFunction(void)

Service to support asynchronous behavior of API calls.

**Sync/Async**
   TRUE

**Reentrancy**
   FALSE


**Return type**
   void


EthSwt_BackgroundTask
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void EthSwt_BackgroundTask(void)

Returns the version information.

**Sync/Async**
   TRUE

**Reentrancy**
   FALSE


**Return type**
   void

