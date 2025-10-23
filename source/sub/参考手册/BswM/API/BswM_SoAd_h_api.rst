

BswM_SoAd_SoConModeChg
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void BswM_SoAd_SoConModeChg(SoAd_SoConIdType SoConId, SoAd_SoConModeType State)

Function called by SoAd to notify state changes of a socket connection.

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
     - SoConId
     - The socket connection index.
   * - [in]
     - State
     - The state of the SoAd socket connection.

**Return type**
   void


