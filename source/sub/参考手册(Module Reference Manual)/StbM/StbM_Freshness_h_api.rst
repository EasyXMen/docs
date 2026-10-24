
类型定义
--------
.. 如果没有就不存在该章节，或为None

None

      
提供的服务
-----------
StbM_FreshnessGetConfig
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    const StbM_FreshnessValueType * StbM_FreshnessGetConfig(uint16 freshnessValueId)



**Sync/Async**
   

**Reentrancy**
   

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - 
     - freshnessValueId
     - 

**Return type**
   const StbM_FreshnessValueType *


StbM_FreshnessGetTxData
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType StbM_FreshnessGetTxData(uint16 freshnessValueId, uint8 *freshnessValue, uint32 *freshnessValueLength)



**Sync/Async**
   

**Reentrancy**
   

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - 
     - freshnessValueId
     - 
   * - 
     - freshnessValue
     - 
   * - 
     - freshnessValueLength
     - 

**Return type**
   Std_ReturnType


StbM_FreshnessGetTxTruncData
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType StbM_FreshnessGetTxTruncData(uint16 freshnessValueId, uint8 *freshnessValue, uint32 *freshnessValueLength, uint8 *truncatedFreshnessValue, uint32 *truncatedFreshnessValueLength)



**Sync/Async**
   

**Reentrancy**
   

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - 
     - freshnessValueId
     - 
   * - 
     - freshnessValue
     - 
   * - 
     - freshnessValueLength
     - 
   * - 
     - truncatedFreshnessValue
     - 
   * - 
     - truncatedFreshnessValueLength
     - 

**Return type**
   Std_ReturnType


StbM_FreshnessSPduTxConfirmation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void StbM_FreshnessSPduTxConfirmation(uint16 freshnessValueId)



**Sync/Async**
   

**Reentrancy**
   

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - 
     - freshnessValueId
     - 

**Return type**
   void


StbM_FreshnessGetRxData
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType StbM_FreshnessGetRxData(uint16 freshnessValueId, const uint8 *truncatedFreshnessValue, uint32 truncatedFreshnessValueLength, uint16 authVerifyAttempts, uint8 *freshnessValue, uint32 *freshnessValueLength)



**Sync/Async**
   

**Reentrancy**
   

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - 
     - freshnessValueId
     - 
   * - 
     - truncatedFreshnessValue
     - 
   * - 
     - truncatedFreshnessValueLength
     - 
   * - 
     - authVerifyAttempts
     - 
   * - 
     - freshnessValue
     - 
   * - 
     - freshnessValueLength
     - 

**Return type**
   Std_ReturnType


