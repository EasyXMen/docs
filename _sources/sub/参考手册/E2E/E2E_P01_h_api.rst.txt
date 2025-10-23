E2E_P01接口描述（E2E_P01 Interface Description）
=================================================

类型定义（Type Definitions）
--------------------------------
.. 如果没有就不存在该章节，或为None

.. list-table:: 
   :widths: 15 5 20
   :header-rows: 1

   * - Type Name
     - Type
     - Description

   * - E2E_P01ConfigType
     - struct E2E_P01ConfigType
     - Configuration of transmitted Data (Data Element or I-PDU),for E2E Profile 1. For each transmitted Data, there is an instance of this typedef.

   * - E2E_P01ProtectStateType
     - struct E2E_P01ProtectStateType
     - State of the sender for a Data protected with E2E Profile 1.

   * - E2E_P01CheckStateType
     - struct E2E_P01CheckStateType
     - State of the reception on one single Data protected with E2E Profile 1.

   * - E2E_P01DataIDMode
     - enum
     - E2E P01 DataID mode.

   * - E2E_P01CheckStatusType
     - enum
     - Status of the reception on one single Data in one cycle, protected with E2E Profile1.


      
提供的服务（Provided Services）
----------------------------------------
E2E_P01Protect
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType E2E_P01Protect(const E2E_P01ConfigType *ConfigPtr, E2E_P01ProtectStateType *StatePtr, uint8 *DataPtr)

Protects the array/buffer to be transmitted using the E2E profile 1. This includes checksum calculation, handling of counter and Data ID.

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
     - ConfigPtr
     - Pointer to static configuration.
   * - [inout]
     - StatePtr
     - Pointer to port/data communication state.
   * - [inout]
     - DataPtr
     - Pointer to Data to be transmitted.

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

E2E_P01ProtectInit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType E2E_P01ProtectInit(E2E_P01ProtectStateType *StatePtr)

Initializes the protection state.

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

E2E_P01Check
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType E2E_P01Check(const E2E_P01ConfigType *Config, E2E_P01CheckStateType *State, const uint8 *Data)

Checks the Data received using the E2E profile 1. This includes CRC calculation, handling of Counter and Data ID.

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
     - Config
     - Pointer to static configuration.
   * - [inout]
     - State
     - Pointer to port/data communication state.
   * - [in]
     - Data
     - Pointer to received data.

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

E2E_P01CheckInit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType E2E_P01CheckInit(E2E_P01CheckStateType *State)

Initializes the check state.

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
     - State
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
   * - E2E_E_OK
     - Function completed successfully

E2E_P01MapStatusToSM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    E2E_PCheckStatusType E2E_P01MapStatusToSM(Std_ReturnType CheckReturn, E2E_P01CheckStatusType Status, boolean ProfileBehavior)

The function maps the check status of Profile 1 to a generic check status, which can be used by E2E state machine check function. The E2E Profile 1 delivers a more fine-granular status, but this is not relevant for the E2E state machine.

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
     - CheckReturn
     - Return value of the E2E_P01Check function.
   * - [in]
     - Status
     - Status determined by E2E_P01Check function.
   * - [in]
     - ProfileBehavior
     - FALSE : check has the legacy behavior, before R4.2 TRUE : check behaves like new P4/P5/P6 profiles introduced in R4.2

**Return type**
    E2E_PCheckStatusType


