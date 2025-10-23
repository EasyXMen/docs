

EcuM_ErrorHook
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

     void EcuM_ErrorHook(uint16 reason)

The ECU State Manager will call the error hook if the error codes "ECUM_E_RAM_CHECK_FAILED" or "ECUM_E_CONFIGURATION_DATA_INCONSISTENT" occur. In this situation it is not possible to continue processing and the ECU must be stopped. The integrator may choose the modality how the ECU is stopped, i.e. reset, halt, restart, safe state etc.

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
     - reason
     - Reason for calling the error hook (e.g., "ECUM_E_RAM_CHECK_FAILED" or "ECUM_E_CONFIGURATION_DATA_INCONSISTENT").

**Return type**
    void

EcuM_AL_SetProgrammableInterrupts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void EcuM_AL_SetProgrammableInterrupts(void)

If the configuration parameter EcuMSetProgrammableInterrupts is set to true, this callout EcuM_AL_SetProgrammableInterrupts is executed and shall set the interrupts on ECUs with programmable interrupts.

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant


**Return type**
   void

EcuM_AL_DriverInitZero
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void EcuM_AL_DriverInitZero(void)

This callout shall provide driver initialization and other hardware-related startup activities for loading the post-build configuration data. Beware: Here only pre-compile and link-time configurable modules may be used.

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant


**Return type**
   void



EcuM_DeterminePbConfiguration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    const EcuM_ConfigType * EcuM_DeterminePbConfiguration(void)

This callout should evaluate some condition, like port pin or NVRAM value, to determine which post-build configuration shall be used in the remainder of the startup process. It shall load this configuration data into a piece of memory that is accessible by all BSW modules and shall return a pointer to the EcuM post-build configuration as a base for all BSW module post-build configurations.

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant


**Return type**
   const


EcuM_AL_DriverInitOne
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void EcuM_AL_DriverInitOne(void)

This callout shall provide driver initialization and other hardware-related startup activities in case of a power on reset.

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant

**Return type**
   void



EcuM_LoopDetection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    boolean EcuM_LoopDetection(void)

If the configuration parameter EcuMResetLoopDetection is set to true, this callout EcuM_LoopDetection is called on every startup.

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant


**Return type**
   boolean

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - FALSE
     - No reset loop is detected
   * - TRUE
     - Reset loop is detected

EcuM_OnGoOffOne
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void EcuM_OnGoOffOne(void)

This call allows the system designer to notify that the GO OFF I state is about to be entered.

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant


**Return type**
   void



EcuM_OnGoOffTwo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void EcuM_OnGoOffTwo(void)

This call allows the system designer to notify that the GO OFF II state is about to be entered.

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant


**Return type**
   void



EcuM_AL_SwitchOff
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void EcuM_AL_SwitchOff(void)

This callout shall take the code for shutting off the power supply of the ECU. If the ECU cannot unpower itself, a reset may be an adequate reaction.

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant


**Return type**
   void



EcuM_AL_Reset
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void EcuM_AL_Reset(EcuM_ResetType reset)

This callout shall take the code for resetting the ECU.

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
     - reset
     - Type of reset to be performed.

**Return type**
   void



EcuM_EnableWakeupSources
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void EcuM_EnableWakeupSources(EcuM_WakeupSourceType wakeupSource)

The ECU Manager Module calls EcuM_EnableWakeupSource to allow the system designer to notify wakeup sources defined in the wakeupSource bitfield that SLEEP will be entered and to adjust their source accordingly.

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
     - wakeupSource
     - Bitfield defining the wakeup sources.

**Return type**
   void



EcuM_GenerateRamHash
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void EcuM_GenerateRamHash(void)

Generate code for RAM integrity test.

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant


**Return type**
   void



EcuM_SleepActivity
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void EcuM_SleepActivity(void)

This callout is invoked periodically in all reduced clock sleep modes.

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant


**Return type**
   void



EcuM_StartCheckWakeup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void EcuM_StartCheckWakeup(EcuM_WakeupSourceType WakeupSource)

This API is called by the ECU Firmware to start the CheckWakeupTimer for the corresponding wakeupSource. If EcuMCheckWakeupTimeout > 0, the CheckWakeupTimer for the wakeupSource is started. If EcuMCheckWakeupTimeout <= 0, the API call is ignored by the EcuM.

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
     - WakeupSource
     - For this wakeup source, the corresponding CheckWakeupTimer shall be started.

**Return type**
   void



EcuM_CheckRamHash
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    uint8 EcuM_CheckRamHash(void)

This callout is intended to provide a RAM integrity test. The goal of this test is to ensure that after a long SLEEP duration, RAM contents are still consistent. The check does not need to be exhaustive since this would consume quite some processing time during wakeups. A well-designed check will execute quickly and detect RAM integrity defects with a sufficient probability. The areas of RAM which will be checked have to be chosen carefully. It depends on the check algorithm itself and the task structure. Stack contents of the task executing the RAM check, for example, very likely cannot be checked. It is good practice to have the hash generation and checking in the same task and that this task is not preemptible and that there is only little activity between hash generation and hash check. The RAM check itself is provided by the system designer. In case of applied multi-core and the existence of Satellite-EcuM(s), this API will be called by the Master-EcuM only.

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant


**Return type**
   uint8

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - 0
     - RAM integrity test failed
   * - non-zero
     - RAM integrity test passed

EcuM_DisableWakeupSources
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void EcuM_DisableWakeupSources(EcuM_WakeupSourceType wakeupSource)

The ECU Manager Module calls EcuM_DisableWakeupSources to set the wakeup source(s) defined in the wakeupSource bitfield so that they are not able to wake the ECU up.

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
     - wakeupSource
     - Bitfield defining the wakeup sources to be disabled.

**Return type**
   void



EcuM_AL_DriverRestart
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void EcuM_AL_DriverRestart(void)

This callout shall provide driver initialization and other hardware-related startup activities in the wakeup case.

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant


**Return type**
   void



EcuM_StartWakeupSources
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void EcuM_StartWakeupSources(EcuM_WakeupSourceType wakeupSource)

The callout shall start the given wakeup source(s) so that they are ready to perform wakeup validation.

**Sync/Async**
   TRUE

**Reentrancy**
   FANon ReentrantLSE

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - wakeupSource
     - Bitfield defining the wakeup sources to be started.

**Return type**
   void



EcuM_CheckValidation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void EcuM_CheckValidation(EcuM_WakeupSourceType wakeupSource)

This callout is called by the EcuM to validate a wakeup source. If a valid wakeup has been detected, it shall be reported to EcuM via

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
     - wakeupSource
     - Bitfield defining the wakeup source to be validated.

**Return type**
   void



EcuM_StopWakeupSources
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void EcuM_StopWakeupSources(EcuM_WakeupSourceType wakeupSource)

The callout shall stop the given wakeup source(s) after unsuccessful wakeup validation.

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
     - wakeupSource
     - Bitfield defining the wakeup sources to be stopped.

**Return type**
   void



EcuM_CheckWakeupHook
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void EcuM_CheckWakeupHook(EcuM_WakeupSourceType wakeupSource)

This callout is called by the EcuM to poll a wakeup source. It shall also be called by the ISR of a wakeup source to set up the PLL and check other wakeup sources that may be connected to the same interrupt.

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
     - wakeupSource
     - Bitfield defining the wakeup source to be polled.

**Return type**
   void



EcuM_McuSetMode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void EcuM_McuSetMode(Mcu_ModeType mode)

This function calls Mcu_SetMode as a callback validation.

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
     - mode
     - Mcu Mode number as configured in the configuration set

**Return type**
   void



EcuM_CurrentTimestampMS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    uint32 EcuM_CurrentTimestampMS(void)

This function retrieves the current timestamp in milliseconds.

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant


**Return type**
   uint32


EcuM_CalculateElapsedMS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    uint32 EcuM_CalculateElapsedMS(uint32 OldCurMs)

This function calculates the elapsed time in milliseconds based on the provided old timestamp.

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
     - OldCurMs
     - Old timestamp value for calculating elapsed time.

**Return type**
   uint32


