
E2E接口描述 E2E(Interface Description)
=========================================

类型定义(Type Definitions)
---------------------------------
.. 如果没有就不存在该章节，或为None

.. list-table:: 
   :widths: 15 5 20
   :header-rows: 1

   * - Type Name
     - Type
     - Description

   * - E2E_PCheckStatusType
     - uint8
     - Profile-independent status of the reception on one single Data in one cycle.

   * - E2E_SMStateType
     - uint8
     - Status of the communication channel exchanging the data. If the status is OK, then the data may be used.

   * - E2E_SMConfigType
     - struct E2E_SMConfigType
     - Configuration of a communication channel for exchanging Data.

   * - E2E_SMCheckStateType
     - struct E2E_SMCheckStateType
     - State of the protection of a communication channel.


      
提供的服务(Services)
----------------------------------------
E2E_GetVersionInfo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void E2E_GetVersionInfo(Std_VersionInfoType *versionInfo)

This service returns the version information of this module.

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [out]
     - versionInfo
     - Pointer to where to store the version

**Return type**
   void


E2E_SMCheck
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType E2E_SMCheck(E2E_PCheckStatusType ProfileStatus, const E2E_SMConfigType *ConfigPtr, E2E_SMCheckStateType *StatePtr)

Checks the communication channel. It determines if the data can be used for safety-related application, based on history of checks performed by a corresponding E2E_P0XCheck() function.

**Sync/Async**
   TRUE

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
     - ProfileStatus
     - Profile-independent status of the reception on one single Data in one cycle.
   * - [in]
     - ConfigPtr
     - Pointer to static configuration.
   * - [inout]
     - StatePtr
     - Pointer to port/data communication state.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E2E_E_INPUTERR_NULL
     - At least one pointer parameter is a NULL pointer
   * - E2E_E_INPUTERR_WRONG
     - At least one input parameter is erroneous, e.g. out of range
   * - E2E_E_INTERR
     - An internal library error has occurred
   * - E2E_E_OK
     - Function completed successfully
   * - E2E_E_WRONGSTATE
     - Function executed in wrong state

E2E_SMCheckInit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType E2E_SMCheckInit(E2E_SMCheckStateType *StatePtr, const E2E_SMConfigType *ConfigPtr)

Initializes the state machine.

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [out]
     - StatePtr
     - Pointer to port/data communication state.
   * - [in]
     - ConfigPtr
     - Pointer to static configuration.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E2E_E_INPUTERR_NULL
     - At least one pointer parameter is a NULL pointer
   * - E2E_E_OK
     - Function completed successfully

