
类型定义 Type Definitions
----------------------------------------

.. list-table:: 
   :widths: 15 5 20
   :header-rows: 1

   * - Type Name
     - Type
     - Description

   * - RamTst_AlgParamsIdType
     - uint8
     - Identification of the algorithm type.

   * - RamTst_NumberOfTestedCellsType
     - uint32
     - Number of the tested cells type.

   * - RamTst_NumberOfBlocksType
     - uint16
     - Number of the test block type.

   * - RamTst_ExecutionStatusType
     - enum
     - Defines status for the execution type.

   * - RamTst_TestResultType
     - enum
     - Type of test result for RamTst.

   * - RamTst_AlgorithmType
     - enum
     - Type of used algorithm for RamTst.


      
提供的服务 Services
----------------------------------------
RamTst_Det_ReportError
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    RAMTST_LOCAL_INLINE void RamTst_Det_ReportError(uint8 ApiId, uint8 ErrorId)

Report Develop Error.

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
     - ApiId
     - Specifies which API reported the error.
   * - [in]
     - ErrorId
     - Specify which error was reported.

**Return type**
   RAMTST_LOCAL_INLINE void


RamTst_GetPartitionId
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    RAMTST_LOCAL_INLINE Std_ReturnType RamTst_GetPartitionId(RamTst_AlgParamsIdType AlgParamsId)

Get partition id of the algorithm parameters set.

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
     - AlgParamsId
     - Identification of the algorithm

**Return type**
   RAMTST_LOCAL_INLINE Std_ReturnType


RamTst_CheckPartition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    RAMTST_LOCAL_INLINE boolean RamTst_CheckPartition(RamTst_AlgParamsIdType AlgParamsId)

Check satellite partition current id.

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
     - AlgParamsId
     - Identification of the algorithm

**Return type**
   RAMTST_LOCAL_INLINE boolean


RamTst_SetOne
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    RAMTST_LOCAL_INLINE uint32 RamTst_SetOne(uint32 Value, uint8 Index)

Set the bit value to '1'.

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
     - Value
     - Set value
   * - [in]
     - Index
     - Index value to be offset

**Return type**
   RAMTST_LOCAL_INLINE uint32


RamTst_SetZero
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    RAMTST_LOCAL_INLINE uint32 RamTst_SetZero(uint32 Value, uint8 Index)

Set the bit value to '0'.

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
     - Value
     - Set value
   * - [in]
     - Index
     - Index value to be offset

**Return type**
   RAMTST_LOCAL_INLINE uint32


RamTst_WalkPathVerify
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    RAMTST_LOCAL_INLINE uint32 RamTst_WalkPathVerify(uint32 Value, uint8 Index)

Verify the bit in WalkPath algorithm.

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
     - Value
     - Verify value
   * - [in]
     - Index
     - Index value to be offset

**Return type**
   RAMTST_LOCAL_INLINE uint32


RamTst_Verify
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    RAMTST_LOCAL_INLINE uint32 RamTst_Verify(uint32 Value, uint8 Index)

Verify the bit value is valid.

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
     - Value
     - Verify value
   * - [in]
     - Index
     - Index value to be offset

**Return type**
   RAMTST_LOCAL_INLINE uint32


RamTst_GalpatSetPatternOne
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    RAMTST_LOCAL_INLINE uint32 RamTst_GalpatSetPatternOne(uint32 Value, uint8 Index)

Set the bit to '1' in Galpat algorithm.

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
     - Value
     - Set value
   * - [in]
     - Index
     - Index value to be offset

**Return type**
   RAMTST_LOCAL_INLINE uint32


RamTst_GalpatSetPatternZero
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    RAMTST_LOCAL_INLINE uint32 RamTst_GalpatSetPatternZero(uint32 Value, uint8 Index)

Set the bit to '0' in Galpat algorithm.

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
     - Value
     - Set value
   * - [in]
     - Index
     - Index value to be offset

**Return type**
   RAMTST_LOCAL_INLINE uint32


RamTst_GalpatCheckOnes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    RAMTST_LOCAL_INLINE uint32 RamTst_GalpatCheckOnes(uint32 Value, uint8 Index)

Check whether the remaining bit are all '1' in ascending order.

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
     - Value
     - Check value
   * - [in]
     - Index
     - Index value to be offset

**Return type**
   RAMTST_LOCAL_INLINE uint32


RamTst_GalpatCheckZero
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    RAMTST_LOCAL_INLINE uint32 RamTst_GalpatCheckZero(uint32 Value, uint8 Index)

Check whether the remaining bit are all '0' in ascending order.

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
     - Value
     - Check value
   * - [in]
     - Index
     - Index value to be offset

**Return type**
   RAMTST_LOCAL_INLINE uint32


RamTst_GalpatCheckAllZero
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    RAMTST_LOCAL_INLINE uint32 RamTst_GalpatCheckAllZero(uint32 Value, uint8 Index)

Check whether the remaining bit are all '0' in descending order.

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
     - Value
     - Check value
   * - [in]
     - Index
     - Index value to be offset

**Return type**
   RAMTST_LOCAL_INLINE uint32


RamTst_GalpatCheckAllOne
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    RAMTST_LOCAL_INLINE uint32 RamTst_GalpatCheckAllOne(uint32 Value, uint8 Index)

Check whether the remaining bit are all '1' in descending order.

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
     - Value
     - Check value
   * - [in]
     - Index
     - Index value to be offset

**Return type**
   RAMTST_LOCAL_INLINE uint32


RamTst_Init
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void RamTst_Init(const RamTst_ConfigType *ConfigPtr)

Service for RAM Test initialization.

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
     - Pointer to the selected configuration set

**Return type**
   void


RamTst_DeInit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void RamTst_DeInit(void)

Service for RAM Test deinitialization.

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant


**Return type**
   void


RamTst_Stop
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void RamTst_Stop(void)

Service for stopping the RAM Test.

**Sync/Async**
   FALSE

**Reentrancy**
   Non Reentrant


**Return type**
   void


RamTst_Allow
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void RamTst_Allow(void)

Service for continuing the RAM Test after calling RamTst_Stop.

**Sync/Async**
   FALSE

**Reentrancy**
   Non Reentrant


**Return type**
   void


RamTst_Suspend
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void RamTst_Suspend(void)

Service for suspending current operation of background RAM Test, until RESUME is called.

**Sync/Async**
   FALSE

**Reentrancy**
   Non Reentrant


**Return type**
   void


RamTst_Resume
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void RamTst_Resume(void)

Service for allowing to continue the background RAM Test at the point is was suspended.

**Sync/Async**
   FALSE

**Reentrancy**
   Non Reentrant


**Return type**
   void


RamTst_GetExecutionStatus
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    RamTst_ExecutionStatusType RamTst_GetExecutionStatus(void)

Service returns the current RAM Test execution status.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant


**Return type**
    RamTst_ExecutionStatusType


RamTst_GetTestResult
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    RamTst_TestResultType RamTst_GetTestResult(void)

Service returns the current RAM Test result.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant


**Return type**
    RamTst_TestResultType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - RAMTST_RESULT_NOT_TESTED
     - The RAM Test has been tested with OK result
   * - RAMTST_RESULT_OK
     - request has not been accepted
   * - RAMTST_RESULT_NOT_OK
     - request has not been accepted
   * - RAMTST_RESULT_UNDEFINED
     - request has not been accepted

RamTst_GetTestResultPerBlock
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    RamTst_TestResultType RamTst_GetTestResultPerBlock(RamTst_NumberOfBlocksType BlockID)

Service returns the current RAM Test result for the specified block.

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
     - BlockID
     - Identifies the block

**Return type**
    RamTst_TestResultType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - RAMTST_RESULT_NOT_TESTED
     - The RAM Test has been tested with OK result
   * - RAMTST_RESULT_OK
     - request has not been accepted
   * - RAMTST_RESULT_NOT_OK
     - request has not been accepted
   * - RAMTST_RESULT_UNDEFINED
     - request has not been accepted

RamTst_GetVersionInfo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void RamTst_GetVersionInfo(Std_VersionInfoType *VersionInfo)

Service returns the version information of this module.

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
   * - [out]
     - VersionInfo
     - Pointer to the location / address where to store the version information of this module

**Return type**
   void


RamTst_GetAlgParams
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    RamTst_AlgParamsIdType RamTst_GetAlgParams(void)

Service returns the ID of the current RAM Test algorithm parameter set.

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant


**Return type**
    RamTst_AlgParamsIdType


RamTst_GetTestAlgorithm
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    RamTst_AlgorithmType RamTst_GetTestAlgorithm(void)

Service returns the current RAM Test algorithm.

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant


**Return type**
    RamTst_AlgorithmType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - RAMTST_ALGORITHM_UNDEFINED
     - Undefined algorithm (uninitialized value)
   * - RAMTST_CHECKERBOARD_TEST
     - Checkerboard test algorithm
   * - RAMTST_MARCH_TEST
     - March test algorithm
   * - RAMTST_WALK_PATH_TEST
     - Walk path test algorithm
   * - RAMTST_GALPAT_TEST
     - Galpat test algorithm
   * - RAMTST_TRANSP_GALPAT_TEST
     - Transparent Galpat test algorithm
   * - RAMTST_ABRAHAM_TEST
     - Abraham test algorithm

RamTst_GetNumberOfTestedCells
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    RamTst_NumberOfTestedCellsType RamTst_GetNumberOfTestedCells(void)

Service returns the current number of tested cells per main-function cycle.

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant


**Return type**
    RamTst_NumberOfTestedCellsType


RamTst_SelectAlgParams
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void RamTst_SelectAlgParams(RamTst_AlgParamsIdType NewAlgParamsId)

Service used to set the test algorithm and its parameter set.

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
     - NewAlgParamsId
     - Identifies the parameter set to be used

**Return type**
   void


RamTst_ChangeNumberOfTestedCells
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void RamTst_ChangeNumberOfTestedCells(RamTst_NumberOfTestedCellsType NewNumberOfTestedCells)

Service changes the current number of tested cells.

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
     - NewNumberOfTestedCells
     - Identifies the number of tested cells

**Return type**
   void


RamTst_RunFullTest
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void RamTst_RunFullTest(void)

Service for executing the full RAM Test in the foreground.

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant


**Return type**
   void


RamTst_RunPartialTest
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void RamTst_RunPartialTest(RamTst_NumberOfBlocksType BlockId)

Service for testing one RAM block in the foreground.

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
     - BlockId
     - Identifies the single RAM block to be tested in the selected set of RamTstAlgParams

**Return type**
   void


RamTst_TestCompletedNotification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void RamTst_TestCompletedNotification(void)

The function RamTst_TestCompleted shall be called every time when all RAM blocks of the current test configuration have been tested in the background.

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant


**Return type**
   void


RamTst_ErrorNotification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void RamTst_ErrorNotification(void)

The function RamTst_Error shall be called every time when a RAM failure has been detected by the selected test algorithm in the background.

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant


**Return type**
   void
