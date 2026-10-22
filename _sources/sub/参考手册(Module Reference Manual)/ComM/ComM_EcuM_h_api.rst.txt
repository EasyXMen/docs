ComM_EcuM_WakeUpIndication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void ComM_EcuM_WakeUpIndication(NetworkHandleType Channel)

Notification of a wake up on the corresponding channel.

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


ComM_EcuM_PNCWakeUpIndication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void ComM_EcuM_PNCWakeUpIndication(PNCHandleType Pnc)

Notification of a wake up on the corresponding partial network cluster.

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
     - Pnc
     - Identifier of the partial network cluster

**Return type**
   void


