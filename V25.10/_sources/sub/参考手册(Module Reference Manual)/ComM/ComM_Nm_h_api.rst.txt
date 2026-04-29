ComM_Nm_NetworkStartIndication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void ComM_Nm_NetworkStartIndication(NetworkHandleType Channel)



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
     - Channel
     - See NetworkHandleType

**Return type**
   void


ComM_Nm_NetworkMode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void ComM_Nm_NetworkMode(NetworkHandleType Channel)



**Sync/Async**
   Asynchronous

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
     - Channel
     - Channel

**Return type**
   void


ComM_Nm_PrepareBusSleepMode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void ComM_Nm_PrepareBusSleepMode(NetworkHandleType Channel)



**Sync/Async**
   Asynchronous

**Reentrancy**
   Reentrant (but not for the same NM-Channel)

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - Channel
     - Channel

**Return type**
   void


ComM_Nm_BusSleepMode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void ComM_Nm_BusSleepMode(NetworkHandleType Channel)



**Sync/Async**
   Asynchronous

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
     - Channel
     - Channel

**Return type**
   void


ComM_Nm_RestartIndication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void ComM_Nm_RestartIndication(NetworkHandleType Channel)



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
     - Channel
     - Channel

**Return type**
   void


ComM_Nm_UpdateEIRA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void ComM_Nm_UpdateEIRA(const uint8 *PncBitVectorPtr)



**Sync/Async**
   Synchronous

**Reentrancy**
   Non Reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - PncBitVectorPtr
     - Pointer to the PNC bit vector which contain the current aggregated internal and external PNC requests (EIRA)

**Return type**
   void


ComM_Nm_UpdateERA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void ComM_Nm_UpdateERA(NetworkHandleType Channel, const uint8 *PncBitVectorPtr)



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
     - Channel
     - Channel
   * - [in]
     - PncBitVectorPtr
     - PNC bit vector which contain the current external PNC requests (ERA) received on the given channel

**Return type**
   void


