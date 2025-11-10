E2E_P44接口描述 E2E_P44(Interface Description)
=================================================

类型定义(Type Definitions)
----------------------------------
.. 如果没有就不存在该章节，或为None

.. list-table:: 
   :widths: 15 5 20
   :header-rows: 1

   * - Type Name
     - Type
     - Description

   * - E2E_P44ConfigType
     -  struct E2E_P44ConfigType
     - Configuration of transmitted Data (Data Element or I-PDU), for E2E Profile 44. For each transmitted Data, there is an instance of this typedef.

   * - E2E_P44ProtectStateType
     - struct E2E_P44ProtectStateType
     - State of the sender for a Data protected with E2E Profile 44.

   * - E2E_P44CheckStateType
     - struct E2E_P44CheckStateType
     - State of the reception on one single Data protected with E2E Profile 44.

   * - E2E_P44CheckStatusType
     - enum
     - Status of the reception on one single Data in one cycle, protected with E2E Profile 44.


      
提供的服务(Services)
----------------------------------------
E2E_P44Protect
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType E2E_P44Protect(const E2E_P44ConfigType *ConfigPtr, E2E_P44ProtectStateType *StatePtr, uint8 *DataPtr, uint16 Length)

Protects the array/buffer to be transmitted using the E2E profile 44. This includes checksum calculation, handling of counter and Data ID.

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
   * - [in]
     - Length
     - Length of the data in bytes.

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

E2E_P44ProtectInit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType E2E_P44ProtectInit(E2E_P44ProtectStateType *StatePtr)

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

E2E_P44Check
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType E2E_P44Check(const E2E_P44ConfigType *ConfigPtr, E2E_P44CheckStateType *StatePtr, const uint8 *DataPtr, uint16 Length)

Checks the Data received using the E2E profile 44. This includes CRC calculation, handling of Counter and Data ID.

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
   * - [in]
     - DataPtr
     - Pointer to received data.
   * - [in]
     - Length
     - Length of the data in bytes.

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

E2E_P44CheckInit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType E2E_P44CheckInit(E2E_P44CheckStateType *StatePtr)

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

E2E_P44MapStatusToSM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    E2E_PCheckStatusType E2E_P44MapStatusToSM(Std_ReturnType CheckReturn, E2E_P44CheckStatusType Status)

The function maps the check status of profile 44 to a generic check status, which can be used by E2E state machine check function. The E2E profile 44 delivers a more fine-granular status, but this is not relevant for the E2E state machine.

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

**Return type**
    E2E_PCheckStatusType


