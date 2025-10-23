

BswM_EthIf_PortGroupLinkStateChg
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void BswM_EthIf_PortGroupLinkStateChg(EthIf_SwitchPortGroupIdxType PortGroupIdx, EthTrcv_LinkStateType PortGroupState)

Function called by EthIf to indicate the link state change of a certain Ethernet switch port group.

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
     - PortGroupIdx
     - The port group index in the context of the Ethernet Interface.
   * - [in]
     - PortGroupState
     - The state of the port group. State is derived from the physical link of the Ethernet Transceiver

**Return type**
   void


