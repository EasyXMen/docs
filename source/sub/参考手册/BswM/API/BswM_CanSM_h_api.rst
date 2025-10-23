

BswM_CanSM_CurrentState
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void BswM_CanSM_CurrentState(NetworkHandleType Network, CanSM_BswMCurrentStateType CurrentState)

Function called by CanSM to indicate its current state.

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
     - The CAN channel the indicated state corresponds to.
   * - [in]
     - CurrentState
     - The current state of the CAN channel.

**Return type**
   void


