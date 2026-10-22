
类型定义
--------
.. 如果没有就不存在该章节，或为None

.. list-table:: 
   :widths: 15 5 20
   :header-rows: 1

   * - Type Name
     - Type
     - Description

   * - Tm_PreDefTimerType
     - struct Tm_PreDefTimerTypeTag
     - 

   * - Tm_ConfigType
     - struct Tm_ConfigTypeTag
     - 

   * - Tm_PreDefTimerInstanceType
     - enum
     - 


      
提供的服务
-----------
Tm_Init
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Tm_Init(const Tm_ConfigType *config)

This service initializes the Time Service module.

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
     - config
     - Pointer to Tm configuration data.

**Return type**
   void


Tm_GetVersionInfo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Tm_GetVersionInfo(Std_VersionInfoType *versioninfo)

Returns the version information of this module.

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
     - to where to store the version information of this module.

**Return type**
   void


Tm_ResetTimer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Tm_ResetTimer(uint32 timerId)

Resets a timer instance (user point of view).

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant but not for the same timerId.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [out]
     - timerId
     - A timer instance handle.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The underlying GPT driver service has returned E_OK.
   * - E_NOT_OK
     - The underlying GPT driver service has not returned E_NOT_OK.

Tm_GetTimeSpan
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Tm_GetTimeSpan(uint32 timerId, uint32 *timeSpan)

Delivers the time difference (current time - reference time).

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
     - timerId
     - A timer instance handle.
   * - [out]
     - timeSpan
     - Pointer to location where the time will be stored.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The underlying GPT driver service has returned E_OK.
   * - E_NOT_OK
     - The underlying GPT driver service has returned E_NOT_OK.

Tm_ShiftTimer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Tm_ShiftTimer(uint32 timerId, uint32 timeValue)

Shifts the reference time of the timer instance.

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant but not for the same timer instance

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - timerId
     - A timer instance handle.
   * - [out]
     - timeValue
     - Time value in in units (e.g. us), the reference time has to be shifted.

**Return type**
   void


Tm_SyncTimer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Tm_SyncTimer(uint32 timerIdSrc, uint32 timerIdDst)

Synchronizes two timer instances.

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant but not for the same timer instance

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - timerIdSrc
     - Source timer instance defined by the user.
   * - [out]
     - timerIdDst
     - Destination timer instance defined by the user.

**Return type**
   void


Tm_BusyWait1us
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Tm_BusyWait1us(uint8 WaitingTimeMin)

Performs busy waiting by polling with a guaranteed minimum waiting time.

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
     - WaitingTimeMin
     - Minimum waiting time in microseconds.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The underlying GPT driver service has returned E_OK.
   * - E_NOT_OK
     - The underlying GPT driver service has returned E_NOT_OK.

