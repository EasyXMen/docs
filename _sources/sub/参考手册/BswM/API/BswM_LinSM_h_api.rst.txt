

BswM_LinSM_CurrentSchedule
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void BswM_LinSM_CurrentSchedule(NetworkHandleType Network, LinIf_SchHandleType CurrentSchedule)

Function called by LinSM to indicate the currently active schedule table for a specific LIN channel.

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
     - The LIN channel that the schedule table switch has occurred on.
   * - [in]
     - CurrentSchedule
     - The currently active schedule table of the LIN channel.

**Return type**
   void


BswM_LinSM_CurrentState
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void BswM_LinSM_CurrentState(NetworkHandleType Network, LinSM_ModeType CurrentState)

Function called by LinSM to indicate its current state.

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
     - The LIN channel that the indicated state corresponds to.
   * - [in]
     - CurrentState
     - The current state of the LIN channel.

**Return type**
   void


