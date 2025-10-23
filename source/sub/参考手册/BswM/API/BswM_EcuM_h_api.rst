

BswM_EcuM_CurrentWakeup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void BswM_EcuM_CurrentWakeup(EcuM_WakeupSourceType source, EcuM_WakeupStatusType state)

Function called by EcuM to indicate the current state of a wakeup source.

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
     - source
     - Wakeup source(s) that changed state.
   * - [in]
     - state
     - The new state of the wakeup source(s).

**Return type**
   void


BswM_EcuM_RequestedState
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void BswM_EcuM_RequestedState(EcuM_StateType State, EcuM_RunStatusType CurrentState)

Function called by EcuM to notify about the current status of the Run Request Protocol.

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
     - State
     - The requested state by EcuMFlex.
   * - 
     - CurrentState
     - 

**Return type**
   void


BswM_EcuM_CurrentState
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void BswM_EcuM_CurrentState(EcuM_StateType CurrentState)

Function called by EcuM to indicate the current ECU Operation Mode.

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
     - CurrentState
     - The requested ECU Operation Mode.

**Return type**
   void


