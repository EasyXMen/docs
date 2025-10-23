

BswM_FrSM_CurrentState
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void BswM_FrSM_CurrentState(NetworkHandleType Network, FrSM_BswM_StateType CurrentState)

Function called by FrSM to indicate its current state.

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
     - The FlexRay cluster that the indicated state corresponds to.
   * - [in]
     - CurrentState
     - The current state of the FlexRay cluster.

**Return type**
   void


