

BswM_Nm_CarWakeUpIndication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void BswM_Nm_CarWakeUpIndication(NetworkHandleType Network)

Function called by NmIf to indicate a CarWakeup.

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
     - Identification of the Nm-Channel.

**Return type**
   void


BswM_Nm_StateChangeNotification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void BswM_Nm_StateChangeNotification(NetworkHandleType Network, Nm_StateType currentState)

Notification of current Nm state after state changes.

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
     - Identification of the Nm-channel
   * - [in]
     - currentState
     - Current (new) state of the Nm-channel

**Return type**
   void


