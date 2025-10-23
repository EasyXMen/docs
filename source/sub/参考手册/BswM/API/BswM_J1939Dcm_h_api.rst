

BswM_J1939DcmBroadcastStatus
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void BswM_J1939DcmBroadcastStatus(uint16 NetworkMask)

This API tells the BswM the desired communication status of the available networks. The status will typically be activated via COM I-PDU group switches.

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
     - NetworkMask
     - Mask containing one bit for each available network.

**Return type**
   void


