

BswM_NvM_CurrentJobMode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void BswM_NvM_CurrentJobMode(NvM_MultiBlockRequestType MultiBlockRequest, NvM_RequestResultType CurrentJobMode)

Function called by NvM to inform the BswM about the current state of a multi block job.

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
     - MultiBlockRequest
     - Indicates which multi block service this callback refers to.
   * - [in]
     - CurrentJobMode
     - Current state of the multi block job indicated by parameter ServiceId.

**Return type**
   void


BswM_NvM_CurrentBlockMode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void BswM_NvM_CurrentBlockMode(NvM_BlockIdType Block, NvM_RequestResultType CurrentBlockMode)

Function called by NvM to indicate the current block mode of an NvM block. To use this function, integration code will be needed.

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
     - Block
     - The block that the new NvM mode corresponds to.
   * - [in]
     - CurrentBlockMode
     - The current block mode of the NvM block.

**Return type**
   void


