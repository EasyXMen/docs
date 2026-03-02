类型定义 Type Definitions
------------------------------------------------
.. 如果没有就不存在该章节，或为None

.. list-table:: 
   :widths: 15 5 20
   :header-rows: 1

   * - Type Name
     - Type
     - Description

   * - LinSM_ModeType
     - uint8
     - 

   * - LinSM_ConfigType
     - struct
     - The root struct configuration parameters of LinSM.

.. list-table:: 
   :widths: 15 5 20
   :header-rows: 1

   * - Type Name
     - Type
     - Description

   * - LinSM_RunTimeType
     - struct
     - Runtime variables.

   * - LinSM_ScheduleType
     - struct
     - Record the schedule table configuration of a channel.

   * - LinSM_ScheduleVariant
     - struct
     - Record all schedule table configurations for a variant.

   * - LinSM_ChannelType
     - struct
     - Channel-related configuration parameter structure.
      
提供的服务 Services
------------------------------------------------
LinSM_Init
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void LinSM_Init(const LinSM_ConfigType *ConfigPtr)

This function initializes the LinSM.

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant(Reentrant for different partitions, Non Reentrant for the same partiton.)

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - ConfigPtr
     - Pointer to the LinSM post-build configuration data.

**Return type**
   void


LinSM_ScheduleRequest
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType LinSM_ScheduleRequest(NetworkHandleType network, LinIf_SchHandleType schedule)

The upper layer requests a schedule table to be changed on one LIN network.

**Sync/Async**
   Asynchronous

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
     - network
     - Identification of the LIN channel.
   * - [in]
     - schedule
     - Index of the scheduled table.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Schedule table request has been accepted.
   * - E_NOT_OK
     - Schedule table switch request has not been accepted due to one of the following reasons: 
     
       - LinSM has not been initialized,

       - Referenced channel does not exist (identification is out of range),

       - Referenced schedule table does not exist (identification is out of range),

       - Sub-state is not LINSM_FULL_COM.

LinSM_GetVersionInfo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void LinSM_GetVersionInfo(Std_VersionInfoType *versioninfo)

Function to get the version information of LinSM.

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
     - versioninfo
     - Pointer to where to store the version information of this module.

**Return type**
   void


LinSM_GetCurrentComMode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType LinSM_GetCurrentComMode(NetworkHandleType network, ComM_ModeType *mode)

Function to query the current communication mode.

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
     - network
     - Identification of the LIN channel.
   * - [in]
     - mode
     - Returns the active mode, see ComM_ModeType for descriptions of the modes.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - OK
   * - E_NOT_OK
     - Not possible to perform the request, e.g. not initialized.

LinSM_RequestComMode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType LinSM_RequestComMode(NetworkHandleType network, ComM_ModeType mode)

Requesting of a communication mode. The mode switch will not be made instant. The LinSM will notify the caller when mode transition is made.

**Sync/Async**
   Asynchronous

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
     - network
     - Identification of the LIN channel
   * - [in]
     - mode
     - Request mode

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request accepted
   * - E_NOT_OK
     - Not possible to perform the request, e.g. not initialized.

LinSM_ScheduleRequestConfirmation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void LinSM_ScheduleRequestConfirmation(NetworkHandleType network, LinIf_SchHandleType schedule)

The LinIf module will call this callback when the new requested schedule table is active.

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
     - network
     - Identification of the LIN channel.
   * - [in]
     - schedule
     - Index of the scheduled table.

**Return type**
   void


LinSM_GotoSleepIndication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void LinSM_GotoSleepIndication(NetworkHandleType network)

The LinIf will call this callback when the go to sleep command is received on the network or a bus idle timeout occurs.

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant (Reentrant for different Channels)

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - network
     - Identification of the LIN channel

**Return type**
   void


LinSM_GotoSleepConfirmation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void LinSM_GotoSleepConfirmation(NetworkHandleType network, boolean success)

The LinIf will call this callback when the go to sleep command is sent successfully or not sent successfully on the network.

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
     - network
     - Identification of the LIN channel
   * - [in]
     - success
     - True if goto sleep was successfully sent, false otherwise

**Return type**
   void


LinSM_WakeupConfirmation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void LinSM_WakeupConfirmation(NetworkHandleType network, boolean success)

The LinIf will call this callback when the wake up signal command is sent not successfully/successfully on the network.

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
     - network
     - Identification of the LIN channel
   * - [in]
     - success
     - True if wakeup was successfully sent, false otherwise

**Return type**
   void


LinSM_MainFunction_<LinSMChannel.ShortName>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void LinSM_MainFunction_<LinSMChannel.ShortName>(void)

Periodic function that runs the timers of different request timeouts.

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant (Reentrant for different Channels)

**Return type**
   void


