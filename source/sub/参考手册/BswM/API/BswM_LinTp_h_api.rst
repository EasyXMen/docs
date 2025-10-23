

BswM_LinTp_RequestMode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void BswM_LinTp_RequestMode(NetworkHandleType Network, LinTp_Mode LinTpRequestedMode)

Function called by LinTP to request a mode for the corresponding LIN channel. The LinTp_Mode correlates to the LIN schedule table that should be used.

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
     - The LIN channel that the LinTp mode request relates to.
   * - [in]
     - LinTpRequestedMode
     - The requested LIN TP mode.

**Return type**
   void


