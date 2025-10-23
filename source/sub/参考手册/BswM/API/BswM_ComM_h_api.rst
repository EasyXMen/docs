

BswM_ComM_InitiateReset
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void BswM_ComM_InitiateReset(void)

Function called by ComM to signal a shutdown.

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant


**Return type**
   void


BswM_ComM_CurrentMode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void BswM_ComM_CurrentMode(NetworkHandleType Network, ComM_ModeType RequestedMode)

Function called by ComM to indicate the current communication mode of a ComM channel.

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
     - Network
     - The ComM communication channel that the indicated state corresponds to.
   * - [in]
     - RequestedMode
     - The current state of the ComM communication channel.

**Return type**
   void


BswM_ComM_CurrentPNCMode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void BswM_ComM_CurrentPNCMode(PNCHandleType PNC, ComM_PncModeType CurrentPncMode)

Function called by ComM to indicate the current mode of the PNC.

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
     - PNC
     - The handle of the PNC for which the current state is reported.
   * - [in]
     - CurrentPncMode
     - The current mode of the PNC.

**Return type**
   void


