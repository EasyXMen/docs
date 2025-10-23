

BswM_Dcm_ApplicationUpdated
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void BswM_Dcm_ApplicationUpdated(void)

This function is called by the DCM to report an updated application.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant


**Return type**
   void


BswM_Dcm_CommunicationMode_CurrentState
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void BswM_Dcm_CommunicationMode_CurrentState(NetworkHandleType Network, Dcm_CommunicationModeType RequestedMode)

Function called by DCM to inform the BswM about the current state of the communication mode.

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
     - The communication channel that the diagnostic mode corresponds to.
   * - [in]
     - RequestedMode
     - The requested diagnostic communication mode.

**Return type**
   void


