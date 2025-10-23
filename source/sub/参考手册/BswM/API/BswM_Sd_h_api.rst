

BswM_Sd_ClientServiceCurrentState
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void BswM_Sd_ClientServiceCurrentState(uint16 SdClientServiceHandleId, Sd_ClientServiceCurrentStateType CurrentClientState)

Function called by Service Discovery to indicate the current state of the Client Service (available/down).

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
     - SdClientServiceHandleId
     - HandleId to identify the ClientService.
   * - [in]
     - CurrentClientState
     - Current state of the ClientService.

**Return type**
   void


BswM_Sd_ConsumedEventGroupCurrentState
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void BswM_Sd_ConsumedEventGroupCurrentState(uint16 SdConsumedEventGroupHandleId, Sd_ConsumedEventGroupCurrentStateType ConsumedEventGroupState)

Function called by Service Discovery to indicate the current status of the Consumed Eventgroup (available/down).

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
     - SdConsumedEventGroupHandleId
     - HandleId to identify the Consumed Eventgroup.
   * - [in]
     - ConsumedEventGroupState
     - Status of the Consumed Eventgroup.

**Return type**
   void


BswM_Sd_EventHandlerCurrentState
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void BswM_Sd_EventHandlerCurrentState(uint16 SdEventHandlerHandleId, Sd_EventHandlerCurrentStateType EventHandlerStatus)

Function called by Service Discovery to indicate the current status of the EventHandler (requested/released).

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
     - SdEventHandlerHandleId
     - HandleId to identify the EventHandler.
   * - [in]
     - EventHandlerStatus
     - Status of the EventHandler.

**Return type**
   void


