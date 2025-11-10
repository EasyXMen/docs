
类型定义(Type Definitions)
-------------------------------------

.. list-table:: 
   :widths: 15 5 20
   :header-rows: 1

   * - Type Name
     - Type
     - Description

   * - Tm_PredefTimer1us16bitType
     - struct Tm_PredefTimer1us16bitTypeTag
     - Data type of Time Service Predef Timer 1us16bit. The structure contains the reference time.

   * - Tm_PredefTimer1us24bitType
     - struct Tm_PredefTimer1us24bitTypeTag
     - Data type of Time Service Predef Timer 1us24bit. The structure contains the reference time.

   * - Tm_PredefTimer1us32bitType
     - struct Tm_PredefTimer1us32bitTypeTag
     - Data type of Time Service Predef Timer 1us32bit. The structure contains the reference time.

   * - Tm_PredefTimer100us32bitType
     - struct Tm_PredefTimer100us32bitTypeTag
     - Data type of Time Service Predef Timer 100µs32bit. The structure contains the reference time.
     
      
提供的服务(Services)
----------------------------------

Tm_GetVersionInfo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Tm_GetVersionInfo(Std_VersionInfoType *versioninfo)

Returns the version information of this module..

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
     - versioninfo
     - to where to store the version information of this module.

**Return type**
    void


Tm_ResetTimer1us16bit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Tm_ResetTimer1us16bit(Tm_PredefTimer1us16bitType *TimerPtr)

Resets a timer instance (user point of view).

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant but not for the same timer instance

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [out]
     - TimerPtr
     - to a timer instance defined by the user.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The underlying GPT driver service has returned E_OK and no development error has been detected
   * - E_NOT_OK
     - The underlying GPT driver service has returned E_NOT_OK, or a development error has been detected

Tm_GetTimeSpan1us16bit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Tm_GetTimeSpan1us16bit(const Tm_PredefTimer1us16bitType *TimerPtr, uint16 *TimeSpanPtr)

Delivers the time difference (current time - reference time).

**Sync/Async**
   TRUE

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
     - TimerPtr
     - to a timer instance defined by the user.
   * - [out]
     - TimeSpanPtr
     - to time span destination data in RAM.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The underlying GPT driver service has returned E_OK and no development error has been detected
   * - E_NOT_OK
     - The underlying GPT driver service has returned E_NOT_OK, or a development error has been detected

Tm_ShiftTimer1us16bit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Tm_ShiftTimer1us16bit(Tm_PredefTimer1us16bitType *TimerPtr, uint16 TimeValue)

Shifts the reference time of the timer instance.

**Sync/Async**
   TRUE

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
     - TimerPtr
     - to a timer instance defined by the user.
   * - [out]
     - TimeValue
     - value in us, the reference time has to be shifted.

**Return type**
   void


Tm_SyncTimer1us16bit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Tm_SyncTimer1us16bit(Tm_PredefTimer1us16bitType *TimerDstPtr, const Tm_PredefTimer1us16bitType *TimerSrcPtr)

Synchronizes two timer instances.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant but not for the same timer instance

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [out]
     - TimerDstPtr
     - to the destination timer instance defined by the user.
   * - [in]
     - TimerSrcPtr
     - to the source timer instance defined by the user.

**Return type**
   void


Tm_BusyWait1us16bit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Tm_BusyWait1us16bit(uint8 WaitingTimeMin)

Performs busy waiting by polling with a guaranteed minimum waiting time.

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
   * - [in]
     - WaitingTimeMin
     - waiting time in microseconds.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The underlying GPT driver service has returned E_OK and no development error has been detected
   * - E_NOT_OK
     - The underlying GPT driver service has returned E_NOT_OK, or a development error has been detected

Tm_ResetTimer1us24bit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Tm_ResetTimer1us24bit(Tm_PredefTimer1us24bitType *TimerPtr)

Resets a timer instance (user point of view).

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant but not for the same timer instance

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [out]
     - TimerPtr
     - to a timer instance defined by the user.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The underlying GPT driver service has returned E_OK and no development error has been detected
   * - E_NOT_OK
     - The underlying GPT driver service has returned E_NOT_OK, or a development error has been detected

Tm_GetTimeSpan1us24bit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Tm_GetTimeSpan1us24bit(const Tm_PredefTimer1us24bitType *TimerPtr, uint32 *TimeSpanPtr)

Delivers the time difference (current time - reference time).

**Sync/Async**
   TRUE

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
     - TimerPtr
     - to a timer instance defined by the user.
   * - [out]
     - TimeSpanPtr
     - to time span destination data in RAM.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The underlying GPT driver service has returned E_OK and no development error has been detected
   * - E_NOT_OK
     - The underlying GPT driver service has returned E_NOT_OK, or a development error has been detected

Tm_ShiftTimer1us24bit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Tm_ShiftTimer1us24bit(Tm_PredefTimer1us24bitType *TimerPtr, uint32 TimeValue)

Shifts the reference time of the timer instance.

**Sync/Async**
   TRUE

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
     - TimerPtr
     - to a timer instance defined by the user.
   * - [out]
     - TimeValue
     - value in us, the reference time has to be shifted.

**Return type**
   void


Tm_SyncTimer1us24bit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Tm_SyncTimer1us24bit(Tm_PredefTimer1us24bitType *TimerDstPtr, const Tm_PredefTimer1us24bitType *TimerSrcPtr)

Synchronizes two timer instances.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant but not for the same timer instance

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [out]
     - TimerDstPtr
     - to the destination timer instance defined by the user.
   * - [in]
     - TimerSrcPtr
     - to the source timer instance defined by the user.

**Return type**
   void


Tm_BusyWait1us24bit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Tm_BusyWait1us24bit(uint8 WaitingTimeMin)

Performs busy waiting by polling with a guaranteed minimum waiting time.

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
   * - [in]
     - WaitingTimeMin
     - waiting time in microseconds.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The underlying GPT driver service has returned E_OK and no development error has been detected
   * - E_NOT_OK
     - The underlying GPT driver service has returned E_NOT_OK, or a development error has been detected

Tm_ResetTimer1us32bit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Tm_ResetTimer1us32bit(Tm_PredefTimer1us32bitType *TimerPtr)

Resets a timer instance (user point of view).

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant but not for the same timer instance

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [out]
     - TimerPtr
     - to a timer instance defined by the user.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The underlying GPT driver service has returned E_OK and no development error has been detected
   * - E_NOT_OK
     - The underlying GPT driver service has returned E_NOT_OK, or a development error has been detected

Tm_GetTimeSpan1us32bit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Tm_GetTimeSpan1us32bit(const Tm_PredefTimer1us32bitType *TimerPtr, uint32 *TimeSpanPtr)

Delivers the time difference (current time - reference time).

**Sync/Async**
   TRUE

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
     - TimerPtr
     - to a timer instance defined by the user.
   * - [out]
     - TimeSpanPtr
     - to time span destination data in RAM.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The underlying GPT driver service has returned E_OK and no development error has been detected
   * - E_NOT_OK
     - The underlying GPT driver service has returned E_NOT_OK, or a development error has been detected

Tm_ShiftTimer1us32bit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Tm_ShiftTimer1us32bit(Tm_PredefTimer1us32bitType *TimerPtr, uint32 TimeValue)

Shifts the reference time of the timer instance.

**Sync/Async**
   TRUE

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
     - TimerPtr
     - to a timer instance defined by the user.
   * - [out]
     - TimeValue
     - value in us, the reference time has to be shifted.

**Return type**
   void


Tm_SyncTimer1us32bit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Tm_SyncTimer1us32bit(Tm_PredefTimer1us32bitType *TimerDstPtr, const Tm_PredefTimer1us32bitType *TimerSrcPtr)

Synchronizes two timer instances.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant but not for the same timer instance

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [out]
     - TimerDstPtr
     - to the destination timer instance defined by the user.
   * - [in]
     - TimerSrcPtr
     - to the source timer instance defined by the user.

**Return type**
   void


Tm_BusyWait1us32bit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Tm_BusyWait1us32bit(uint8 WaitingTimeMin)

Performs busy waiting by polling with a guaranteed minimum waiting time.

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
   * - [in]
     - WaitingTimeMin
     - waiting time in microseconds.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The underlying GPT driver service has returned E_OK and no development error has been detected
   * - E_NOT_OK
     - The underlying GPT driver service has returned E_NOT_OK, or a development error has been detected

Tm_ResetTimer100us32bit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Tm_ResetTimer100us32bit(Tm_PredefTimer100us32bitType *TimerPtr)

Resets a timer instance (user point of view).

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant but not for the same timer instance

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [out]
     - TimerPtr
     - to a timer instance defined by the user.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The underlying GPT driver service has returned E_OK and no development error has been detected
   * - E_NOT_OK
     - The underlying GPT driver service has returned E_NOT_OK, or a development error has been detected

Tm_GetTimeSpan100us32bit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Tm_GetTimeSpan100us32bit(const Tm_PredefTimer100us32bitType *TimerPtr, uint32 *TimeSpanPtr)

Delivers the time difference (current time - reference time).

**Sync/Async**
   TRUE

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
     - TimerPtr
     - to a timer instance defined by the user.
   * - [out]
     - TimeSpanPtr
     - to time span destination data in RAM.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The underlying GPT driver service has returned E_OK and no development error has been detected
   * - E_NOT_OK
     - The underlying GPT driver service has returned E_NOT_OK, or a development error has been detected

Tm_ShiftTimer100us32bit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Tm_ShiftTimer100us32bit(Tm_PredefTimer100us32bitType *TimerPtr, uint32 TimeValue)

Shifts the reference time of the timer instance.

**Sync/Async**
   TRUE

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
     - TimerPtr
     - to a timer instance defined by the user.
   * - [out]
     - TimeValue
     - value in us, the reference time has to be shifted.

**Return type**
   void


Tm_SyncTimer100us32bit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Tm_SyncTimer100us32bit(Tm_PredefTimer100us32bitType *TimerDstPtr, const Tm_PredefTimer100us32bitType *TimerSrcPtr)

Synchronizes two timer instances.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant but not for the same timer instance

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [out]
     - TimerDstPtr
     - to the destination timer instance defined by the user.
   * - [in]
     - TimerSrcPtr
     - to the source timer instance defined by the user.

**Return type**
   void


Tm_GetTimeSpan1ms32bit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Tm_GetTimeSpan1ms32bit(const Tm_PredefTimer1ms32bitType *TimerPtr, uint32 *TimeSpanPtr)

Delivers the time difference (current time - reference time).

**Sync/Async**
   TRUE

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
     - TimerPtr
     - to a timer instance defined by the user.
   * - [out]
     - TimeSpanPtr
     - to time span destination data in RAM.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The underlying GPT driver service has returned E_OK and no development error has been detected
   * - E_NOT_OK
     - The underlying GPT driver service has returned E_NOT_OK, or a development error has been detected

