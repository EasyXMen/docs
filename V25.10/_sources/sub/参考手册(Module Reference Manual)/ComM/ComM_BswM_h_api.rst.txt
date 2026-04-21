ComM_CommunicationAllowed
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void ComM_CommunicationAllowed(NetworkHandleType Channel, boolean Allowed)

EcuM or BswM shall indicate to ComM when communication is allowed. If EcuM/Flex is used: BswM.

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
   * - [in]
     - Allowed
     - TRUE: Communication is allowed FALSE: Communication is not allowed

**Return type**
   void


