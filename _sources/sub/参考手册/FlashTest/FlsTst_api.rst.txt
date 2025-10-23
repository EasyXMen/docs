

类型定义 Type Definitions
--------------------------------------------------------------------------------

.. list-table:: 
   :widths: 15 5 20
   :header-rows: 1

   * - Type Name
     - Type
     - Description

   * - FlsTst_BlockIdFgndType
     - uint32
     - Identification of the Foreground test block @range 0..0xFFFFFFFF.

   * - FlsTst_TestResultBgndType
     - struct FlsTst_TestResultBgndTypeTag
     - Definition of Background test result datatype.

   * - FlsTst_ErrorDetailsType
     - struct FlsTst_ErrorDetailsTypeTag
     - Definition of detail error information datatype.

   * - FlsTst_TestSignatureFgndType
     - struct FlsTst_TestSignatureFgndTypeTag
     - Definition of Foreground test signature datatype.

   * - FlsTst_TestSignatureBgndType
     - struct FlsTst_TestSignatureBgndTypeTag
     - Definition of Background test signature information datatype.

   * - FlsTst_StateType
     - enum
     - Definition of status datatype.

   * - FlsTst_TestResultType
     - enum
     - Definition of test result datatype.

   * - FlsTst_TestResultFgndType
     - enum
     - Definition of Foreground test result datatype.

   * - FlsTst_AlgorithmType
     - enum
     - Definition of test algorithm datatype.


提供的服务 Services
--------------------------------------------------------------------------------
FlsTst_Det_ReportError
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    FLSTST_LOCAL_INLINE void FlsTst_Det_ReportError(uint8 ApiId, uint8 ErrorId)

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
   FLSTST_LOCAL_INLINE void


FlsTst_CheckPartition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    FLSTST_LOCAL_INLINE boolean FlsTst_CheckPartition(void)

Check satellite partition current id.

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant


**Return type**
   FLSTST_LOCAL_INLINE boolean


FlsTst_Init
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void FlsTst_Init(const FlsTst_ConfigType *ConfigPtr)

Service for Flash Test initialization.

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
     - Pointer to configuration set

**Return type**
   void


FlsTst_DeInit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void FlsTst_DeInit(void)

Service for Flash Test De-Initialization.

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant


**Return type**
   void


FlsTst_StartFgnd
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType FlsTst_StartFgnd(FlsTst_BlockIdFgndType FgndBlockId)

Service for executing foreground Flash Test.

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
     - FgndBlockId
     - Number of the foreground test to be executed

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Foreground test processed
   * - E_NOT_OK
     - Foreground test not accepte

FlsTst_Abort
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void FlsTst_Abort(void)

Service for aborting the Flash Test.

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant


**Return type**
   void


FlsTst_Suspend
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void FlsTst_Suspend(void)

Service for suspending current operation of the Flash Test, until FlsTst_Resume is called.

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant


**Return type**
   void


FlsTst_Resume
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void FlsTst_Resume(void)

Service for continuing the Flash Test at the point it was suspended.

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant


**Return type**
   void


FlsTst_GetCurrentState
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    FlsTst_StateType FlsTst_GetCurrentState(void)

Service returns the current Flash Test exection state.

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant


**Return type**
    FlsTst_StateType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - FLSTST_UNINIT
     - The Flash Test is not initialized or not usable
   * - FLSTST_INIT
     - The Flash Test is initialized and ready to be started
   * - FLSTST_RUNNING
     - The Flash Test is currently running
   * - FLSTST_ABORTED
     - The Flash Test is aborted
   * - FLSTST_SUSPENDED
     - The Flash Test is waiting to be resumed or is waiting to start forground mode test

FlsTst_GetTestResultBgnd
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    FlsTst_TestResultBgndType FlsTst_GetTestResultBgnd(void)

Service returns the Background Flash Test result.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant


**Return type**
    FlsTst_TestResultBgndType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - FlsTstIntervalID
     - current value of FlsTstTestIntervalId, which is incremented by each new start of an test interval
   * - result
     - Test Result in background flash test

FlsTst_GetTestResultFgnd
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    FlsTst_TestResultFgndType FlsTst_GetTestResultFgnd(void)

Service returns the Foreground Flash Test result.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant


**Return type**
    FlsTst_TestResultFgndType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - FLSTST_NOT_TESTED
     - There is no result availabl
   * - FLSTST_OK
     - The last Flash Test has been tested with OK result
   * - FLSTST_NOT_OK
     - The last Flash Test has been tested with NOT_OK result

FlsTst_GetVersionInfo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void FlsTst_GetVersionInfo(Std_VersionInfoType *versionInfo)

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
     - versionInfo
     - Pointer to where to store the version information of this module

**Return type**
   void


FlsTst_GetTestSignatureBgnd
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    FlsTst_TestSignatureBgndType FlsTst_GetTestSignatureBgnd(void)

Service returns the Foreground Flash Test result.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant


**Return type**
    FlsTst_TestSignatureBgndType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - FlsTstIntervalID
     - current value of FlsTstTestIntervalId, which is incremented by each new start of an test interval
   * - BgndSignature
     - It represents the signature value of the last completed test interval

FlsTst_GetTestSignatureFgnd
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    FlsTst_TestSignatureFgndType FlsTst_GetTestSignatureFgnd(void)

Service returns the Flash Test result in background.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant


**Return type**
    FlsTst_TestSignatureFgndType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - FlsTstIntervalID
     - current value of FlsTstTestIntervalId, which is incremented by each new start of an test interval
   * - BgndSignature
     - It represents the signature value of the last completed test interval

FlsTst_GetErrorDetails
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    FlsTst_ErrorDetailsType FlsTst_GetErrorDetails(void)

Service returns error detais monitored from the Flash module.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant


**Return type**
    FlsTst_ErrorDetailsType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - ErrorBlockID
     - Record the block ID value when the error occurred
   * - Algorithm
     - The test algorithm used by the current block
   * - SignatureResult
     - The signature result of the current block

FlsTst_TestEcc
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType FlsTst_TestEcc(void)

Service executes a test of ECC hardware. This is only applicable in case the hardware provices such functionality.

**Sync/Async**
   TRUE

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
     - ECC test processed
   * - E_NOT_OK
     - ECC test not accepte