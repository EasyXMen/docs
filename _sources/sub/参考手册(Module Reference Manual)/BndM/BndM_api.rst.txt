
类型定义
--------
.. 如果没有就不存在该章节，或为None

.. list-table:: 
   :widths: 15 5 20
   :header-rows: 1

   * - Type Name
     - Type
     - Description

   * - BndM_ResultType
     - uint8
     - Used as result of the asynchronous job finish notifications @range 0..255.

   * - BndM_BlockIdType
     - uint16
     - Used as unique identification of an bulk nv block; the BndM_BlockId is assigned by the BndM. @range 0..65535.

   * - BndM_WriteStartFinishFct
     - void*
     - This function pointer type is used to describe the link that raise 'BndM_WriteStart' to Upper layer. @range NA.

   * - BndM_WriteFinalizeFinishFct
     - void*
     - This function pointer type is used to describe the link that raise 'BndM_WriteFinalize' to Upper layer. @range NA.

   * - BndM_WriteBlockFinishFct
     - void*
     - This function pointer type is used to describe the link that raise 'BndM_WriteBlock' to Upper layer. @range NA.

   * - BndM_BankParamListType
     - struct BndM_SwapBlockParamListTypeTag
     - This type is used to describe the parameter list of bank in BndM.

   * - BndM_BlockHeaderInfoType
     - struct BndM_BlockHeaderInfoTypeTag
     - This type is used to describe the header information of block descriptor in BndM.

   * - BndM_BlockDescriptorType
     - struct BndM_BlockDescriptorTypeTag
     - This type is used to describe the parameter list of block descriptor in BndM.

   * - BndM_BlockConfigurationType
     - struct BndM_BlockConfigurationTypeTag
     - This type is used to describe the block configuration information in BndM.

   * - BndM_ConfigType
     - struct BndM_ConfigTypeTag
     - This type is used to describe the configuration information structure of BndM.



提供的服务
-----------
BndM_Init
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void BndM_Init(const BndM_ConfigType *ConfigPtr)

Service is used to initializes the bulk non volatile Data Manager.

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
     - ConfigPtr
     - Pointer to the selected configuration structure.

**Return type**
   void


BndM_GetVersionInfo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void BndM_GetVersionInfo(Std_VersionInfoType *versioninfo)

Service is used to get the version information of BndM module.

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
   * - [out]
     - versioninfo
     - Pointer to where to store the version information of BndM module

**Return type**
   void


BndM_WriteStart
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType BndM_WriteStart(void)

Service is used to will trigger the start of writing phase.

**Sync/Async**
   Asynchronous

**Reentrancy**
   Non Reentrant


**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The preparation request is accepted.
   * - E_NOT_OK
     - The preparation request is rejected.

BndM_WriteFinalize
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType BndM_WriteFinalize(void)

Service is used to will trigger the finalization of writing phase.

**Sync/Async**
   Asynchronous

**Reentrancy**
   Reentrant Finalize the writing.


**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The finalization request is accepted.
   * - E_NOT_OK
     - The finalization request is rejected.

BndM_WriteCancel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void BndM_WriteCancel(void)

Service is used to will trigger the cancel of writing phase.

**Sync/Async**
   Asynchronous

**Reentrancy**
   Reentrant


**Return type**
   void


BndM_JobEndNotification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void BndM_JobEndNotification(MemAcc_AddressAreaIdType addressAreaId, MemAcc_JobResultType jobResult)

This callback function is called when a MemAcc job has been finished with positive result.

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
     - addressAreaId
     - Numeric identifier of address area
   * - [in]
     - jobResult
     - After the end of the job processing, the returned result

**Return type**
   void


BndM_MainFunction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void BndM_MainFunction(void)

Schedule function for the background processing.

**Sync/Async**
   Synchronous

**Reentrancy**
   Non Reentrant


**Return type**
   void


