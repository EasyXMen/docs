

BswM_J1939Nm_StateChangeNotification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void BswM_J1939Nm_StateChangeNotification(NetworkHandleType Network, uint8 Node, Nm_StateType NmState)

Notification of the current J1939Nm state after state changes.

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
     - Identification of the J1939 channel.
   * - [in]
     - Node
     - Identification of the J1939 node.
   * - [in]
     - NmState
     - Current (new) state of the J1939 node.

**Return type**
   void


