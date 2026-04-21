

      

Nm_NetworkStartIndication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Nm_NetworkStartIndication(NetworkHandleType nmNetworkHandle)

Notification that a NM-message has been received in the Bus-Sleep Mode, what indicates that some nodes in the network have already entered the Network Mode.

**Sync/Async**
   Synchronous

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
     - nmNetworkHandle
     - Identification of the NM-channel

**Return type**
   void


Nm_NetworkMode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Nm_NetworkMode(NetworkHandleType nmNetworkHandle)

Notification that the network management has entered Network Mode.

**Sync/Async**
   Synchronous

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
     - nmNetworkHandle
     - Identification of the NM-channel

**Return type**
   void


Nm_BusSleepMode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Nm_BusSleepMode(NetworkHandleType nmNetworkHandle)

Notification that the network management has entered Bus-Sleep Mode.

**Sync/Async**
   Synchronous

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
     - nmNetworkHandle
     - Identification of the NM-channel

**Return type**
   void


Nm_PrepareBusSleepMode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Nm_PrepareBusSleepMode(NetworkHandleType nmNetworkHandle)

Notification that the network management has entered Prepare Bus-Sleep Mode.

**Sync/Async**
   Synchronous

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
     - nmNetworkHandle
     - Identification of the NM-channel

**Return type**
   void


Nm_RemoteSleepIndication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Nm_RemoteSleepIndication(NetworkHandleType nmNetworkHandle)

Notification that the network management has detected that all other nodes on the network are ready to enter Bus-Sleep Mode.

**Sync/Async**
   Synchronous

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
     - nmNetworkHandle
     - Identification of the NM-channel

**Return type**
   void


Nm_RemoteSleepCancellation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Nm_RemoteSleepCancellation(NetworkHandleType nmNetworkHandle)

Notification that the network management has detected that not all other nodes on the network are longer ready to enter Bus-Sleep Mode.

**Sync/Async**
   Synchronous

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
     - nmNetworkHandle
     - Identification of the NM-channel

**Return type**
   void


Nm_SynchronizationPoint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Nm_SynchronizationPoint(NetworkHandleType nmNetworkHandle)

Notification to the NM Coordinator functionality that this is a suitable point in time to initiate the coordinated shutdown on.

**Sync/Async**
   Synchronous

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
     - nmNetworkHandle
     - Identification of the NM-channel

**Return type**
   void


Nm_CoordReadyToSleepIndication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Nm_CoordReadyToSleepIndication(NetworkHandleType nmChannelHandle)

Sets an indication, when the NM Coordinator Sleep Ready bit in the Control Bit Vector is set.

**Sync/Async**
   Synchronous

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
     - nmChannelHandle
     - Identification of the NM-channel

**Return type**
   void


Nm_CoordReadyToSleepCancellation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Nm_CoordReadyToSleepCancellation(NetworkHandleType nmChannelHandle)

Cancels an indication, when the NM Coordinator Sleep Ready bit in the Control Bit Vector is set back to 0.

**Sync/Async**
   Synchronous

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
     - nmChannelHandle
     - Identification of the NM-channel

**Return type**
   void


Nm_PduRxIndication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Nm_PduRxIndication(NetworkHandleType nmNetworkHandle)

Notification that a NM message has been received.

**Sync/Async**
   Synchronous

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
     - nmNetworkHandle
     - Identification of the NM-channel

**Return type**
   void


Nm_StateChangeNotification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Nm_StateChangeNotification(NetworkHandleType nmNetworkHandle, Nm_StateType nmPreviousState, Nm_StateType nmCurrentState)

Notification that the state of the lower layer <Bus>Nm has changed.

**Sync/Async**
   Synchronous

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
     - nmNetworkHandle
     - Identification of the NM-channel
   * - [in]
     - nmPreviousState
     - previous state of the NM-channel
   * - [in]
     - nmCurrentState
     - current state of the NM-channel

**Return type**
   void


Nm_RepeatMessageIndication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Nm_RepeatMessageIndication(NetworkHandleType nmNetworkHandle)

Service to indicate that an NM message with set Repeat Message Request Bit has been received.

**Sync/Async**
   Synchronous

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
     - nmNetworkHandle
     - Identification of the NM-channel

**Return type**
   void


Nm_TxTimeoutException
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Nm_TxTimeoutException(NetworkHandleType nmNetworkHandle)

Service to indicate that an attempt to send an NM message failed.

**Sync/Async**
   Synchronous

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
     - nmNetworkHandle
     - Identification of the NM-channel

**Return type**
   void


Nm_CarWakeUpIndication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Nm_CarWakeUpIndication(NetworkHandleType nmChannelHandle)

This function is called by a <Bus>Nm to indicate reception of a CWU request.

**Sync/Async**
   Synchronous

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
     - nmChannelHandle
     - Identification of the NM-channel

**Return type**
   void


Nm_SynchronizeMode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Nm_SynchronizeMode(NetworkHandleType nmNetworkHandle)

Notification that the network management has entered Synchronize Mode.

**Sync/Async**
   Synchronous

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
     - nmNetworkHandle
     - Identification of the NM-channel

**Return type**
   void


