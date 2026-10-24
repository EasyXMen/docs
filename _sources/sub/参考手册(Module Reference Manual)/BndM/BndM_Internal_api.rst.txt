
类型定义
--------
.. 如果没有就不存在该章节，或为None

.. list-table:: 
   :widths: 15 5 20
   :header-rows: 1

   * - Type Name
     - Type
     - Description

   * - BndM_WriteHandleFuncPtr
     - void*
     - This function pointer type is used to describe the link that raise 'WriteHandle' to Upper layer.

   * - BndM_RunTimeDataType
     - struct BndM_RunTimeDataTypeTag
     - Used to describe the type of run time data structure in bulk NV data manager.

   * - BndM_BlockInfoType
     - struct BndM_BlockInfoTypeTag
     - Used to describe the type of block information structure in bulk NV data manager.

   * - BndM_BankParamInfoType
     - struct BndM_BankParamInfoTypeTag
     - Used to describe the type of bank parameter information structure in bulk NV data manager.

   * - BndM_BankDataListType
     - struct BndM_BankDataListTypeTag
     - Used to describe the type of bank data list structure in bulk NV data manager.

   * - BndM_BankDataInfoType
     - union
     - Used to describe the type of bank data information union in bulk NV data manager.

   * - BndM_MemEraseInfoType
     - union
     - Used to describe the type of erase value information union in bulk NV data manager.

   * - BndM_WriteJobSequenceType
     - enum
     - Enumeration type that is used to describe the state of the write job sequence.

   * - BndM_SubJobStatusType
     - enum
     - Enumeration type that is used to describe the status of the write sub job.

   * - BndM_MemAccStateType
     - enum
     - Enumeration type that is used to describe the write state of the MemAcc job.

   * - BndM_CancelStateType
     - enum
     - Enumeration type that is used to describe the state of the write cancel.

   * - BndM_JobResultType
     - enum
     - Enumeration type that is used to describe the result of the write job.


      
提供的服务
-----------
BndM_MemCpy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    BNDM_LOCAL_INLINE void BndM_MemCpy(MemAcc_DataType *dest, const MemAcc_DataType *src, MemAcc_LengthType size)

Service is used to get the pointer of the runtime data.

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant


**Return type**
   BNDM_LOCAL_INLINE void


BndM_MemSet
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    BNDM_LOCAL_INLINE void BndM_MemSet(MemAcc_DataType *dest, const MemAcc_DataType value, MemAcc_LengthType size)

Service is used to get the pointer of the runtime data.

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant


**Return type**
   BNDM_LOCAL_INLINE void


BndM_GetBlockSize
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    BNDM_LOCAL_INLINE MemAcc_LengthType BndM_GetBlockSize(const BndM_BlockIdType BlockId)

Service is used to get the pointer of the runtime data.

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant


**Return type**
   BNDM_LOCAL_INLINE MemAcc_LengthType


BndM_WriteBlockRequest
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType BndM_WriteBlockRequest(const BndM_BlockIdType BlockId, const MemAcc_DataType *WriteBufferPtr)

Service is used to the write request for the given block.

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
     - BlockId
     - The identifier of the given block
   * - [in]
     - WriteBufferPtr
     - The pointer for writing to the data buffer

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The write request is accepted.
   * - E_NOT_OK
     - The write request is rejected.

BndM_GetBankParamInfoPtr
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    BndM_BankParamInfoType * BndM_GetBankParamInfoPtr(void)

Service is used to get the parameter information pointer for the bank.

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant


**Return type**
    BndM_BankParamInfoType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - the
     - parameter information pointer of the bank.

BndM_GetBlockInfoPtr
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    BndM_BlockInfoType * BndM_GetBlockInfoPtr(const BndM_BlockIdType BlockId)

Service is used to get the parameter information pointer for the block.

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
     - BlockId
     - The identifier of the given block

**Return type**
    BndM_BlockInfoType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - the
     - parameter information pointer of the block.

