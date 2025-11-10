
类型定义(Type Definitions)
-------------------------------
.. 如果没有就不存在该章节，或为None

.. list-table::
   :widths: 15 5 20
   :header-rows: 1

   * - Type Name
     - Type
     - Description

   * - CanSM_ConfigType
     - struct
     - This type defines a data structure for the post build parameters of the CanSM. At initialization the CanSM gets a pointer to a structure of this type to get access to its configuration data, which is necessary for initialization.

   * - CanSM_BswMCurrentStateType
     - enum
     - Can specific communication modes / states notified to the BswM module.


提供的服务(Services)
-------------------------------------
CanSM_Init
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void CanSM_Init(const CanSM_ConfigType *ConfigPtr)

This service initializes the CanSM module.

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
     - Pointer to init structure for the post build parameters of the CanSM

**Return type**
   void


CanSM_DeInit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void CanSM_DeInit(void)

This service de-initializes the CanSM module.

**Sync/Async**
   Synchronous

**Reentrancy**
   Non Reentrant


**Return type**
   void


CanSM_RequestComMode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType CanSM_RequestComMode(NetworkHandleType network, ComM_ModeType ComM_Mode)

This service shall change the communication mode of a CAN network to the requested one.

**Sync/Async**
   Asynchronous

**Reentrancy**
   Reentrant (only for different network handles)

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - network
     - Handle of destined communication network for request
   * - [in]
     - ComM_Mode
     - Requested communication mode

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Service accepted
   * - E_NOT_OK
     - Service denied

CanSM_GetCurrentComMode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType CanSM_GetCurrentComMode(NetworkHandleType network, ComM_ModeType *ComM_ModePtr)

This service shall put out the current communication mode of a CAN network.

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
     - Network handle, whose current communication mode shall be put out
   * - [out]
     - ComM_ModePtr
     - Pointer, where to put out the current communication mode

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Service accepted
   * - E_NOT_OK
     - Service denied

CanSM_GetVersionInfo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void CanSM_GetVersionInfo(Std_VersionInfoType *VersionInfo)

This service puts out the version information of this module (module ID, vendor ID, vendor specific version numbers related to BSW00407)

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
     - VersionInfo
     - Pointer to where to store the version information of this module.

**Return type**
   void


CanSM_SetBaudrate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType CanSM_SetBaudrate(NetworkHandleType Network, uint16 BaudRateConfigID)

This service shall start an asynchronous process to change the baud rate for the configured CAN controllers of a certain CAN network.

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant for different Networks. Non reentrant for the same Network.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - Network
     - Handle of the addressed CAN network for the baud rate change
   * - [in]
     - BaudRateConfigID
     - references a baud rate configuration by ID (see CanController BaudRateConfigID)

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Controller mode request has been accepted
   * - E_NOT_OK
     - Controller mode request has not been accepted

CanSM_SetEcuPassive
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType CanSM_SetEcuPassive(boolean CanSM_Passive)

This function can be used to set all CanSM channels of the ECU to a receive only mode.

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
     - CanSM_Passive
     - TRUE: set all CanSM channels to passive, i.e. receive only FALSE: set all CanSM channels back to non-passive

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
     - Request denied


CanSM_StartWakeupSource
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType CanSM_StartWakeupSource(NetworkHandleType network)

This function shall be called by EcuM when a wakeup source shall be started.

**Sync/Async**


**Reentrancy**


**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - network
     - Affected CAN network

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
     - Request denied

CanSM_StopWakeupSource
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType CanSM_StopWakeupSource(NetworkHandleType network)

This function shall be called by EcuM when a wakeup source shall be stopped.

**Sync/Async**


**Reentrancy**


**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - network
     - Affected CAN network

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
     - Request denied
