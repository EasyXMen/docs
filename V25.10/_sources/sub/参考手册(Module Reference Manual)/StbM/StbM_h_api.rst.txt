
StbM对外类型定义 StbM External Type Definitions
----------------------------------------------------------------------------------------------------------------------------------------

.. 如果没有就不存在该章节，或为None

.. list-table::
   :widths: 15 5 20
   :header-rows: 1

   * - Type Name
     - Type
     - Description

   * - StbM_ConfigType
     - struct
     - Configuration data structure of the StbM module

   * - StbM_SynchronizedTimeBaseType
     - uint16
     - Variables of this type are used to represent the kind of synchronized time-base

   * - StbM_TimeTupleType
     - struct
     - Variables of this type are used for expressing time tuples

   * - StbM_UserDataType
     - struct
     - Current user data of the Time Base

   * - StbM_TimeStampType
     - struct
     - Variables of this type are used for expressing time stamps including relative time and absolute calendar time.

   * - StbM_MeasurementType
     - struct
     - structure which contains additional measurement data

   * - StbM_RateDeviationType
     - sint16
     - Variables of this type are used to express a rate deviation in ppm

   * - StbM_TimeDiffType
     - sint32
     - Variables of this type are used to express time differences / offsets as signed values in in nanoseconds

   * - StbM_TimeBaseStatusType
     - uint16
     - Variables of this type are used to express if and how a Local Time Base is synchronized to the Global Time Master

   * - StbM_CustomerIdType
     - uint16
     - unique identifier of a notification customer

   * - StbM_SyncRecordTableHeadType
     - struct
     - Synchronized Time Base Record Table Header

   * - StbM_MasterConfigType
     - uint8
     - This type indicates if an ECU is configured for a system wide master for a given Time Base is available or not


StbM对外提供的服务 Services Provided Externally by StbM
----------------------------------------------------------------------------------------------------------------------------------------

StbM_Init
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void StbM_Init(const StbM_ConfigType *configPtr)

Initializes the Synchronized Timebase Manager.

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant (Reentrant for different partitions. Non reentrant for the same partition.)

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - configPtr
     - Pointer to post-build configuration data

**Return type**
   void


StbM_GetVersionInfo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void StbM_GetVersionInfo(Std_VersionInfoType *versioninfo)

This function returns the version information of this module.

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
     - Pointer to the memory location holding the version information.

**Return type**
   void

StbM_GetCurrentTime
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType StbM_GetCurrentTime(StbM_SynchronizedTimeBaseType timeBaseId, StbM_TimeTupleType *timeTuple, StbM_UserDataType *userData)

Returns a time value(Local Time Base derived from Global Time Base) in standard format.

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
     - timeBaseId
     - Identification of a Time Base
   * - [out]
     - timeTuple
     - Current time stamp that is valid at this time
   * - [out]
     - userData
     - User data of the Time Base

**Return type**
   Std_ReturnType


**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Successfully get the Current time
   * - E_NOT_OK
     - Getting the Current time failed

StbM_GetCurrentVirtualLocalTime
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType StbM_GetCurrentVirtualLocalTime(StbM_SynchronizedTimeBaseType timeBaseId, StbM_VirtualLocalTimeType *localTimePtr)

Returns the Virtual Local Time of the referenced Time Base.

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
     - timeBaseId
     - Identification of a Time Base
   * - [out]
     - localTimePtr
     - Current Virtual Local Time value

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Successfully get the Virtual Local Time
   * - E_NOT_OK
     - Getting the Virtual Local Time failed


StbM_SetGlobalTime
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType StbM_SetGlobalTime(StbM_SynchronizedTimeBaseType timeBaseId, const StbM_TimeStampType *timeStamp, const StbM_UserDataType *userData)

Allows the Customers to set the new global time that has to be valid for the system, which will be sent to the busses. This function will be used if a Time Master is present in this ECU.

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
     - timeBaseId
     - Identification of a Time Base
   * - [in]
     - timeStamp
     - New time stamp
   * - [in]
     - userData
     - New user data(if not NULL)

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Successfully set the global time
   * - E_NOT_OK
     - Setting the global Time failed


StbM_UpdateGlobalTime
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType StbM_UpdateGlobalTime(StbM_SynchronizedTimeBaseType timeBaseId, const StbM_TimeStampType *timeStamp, const StbM_UserDataType *userData)

Allows the Customers to set the Global Time that will be sent to the buses. This function will be used if a Time Master is present in this ECU. Using UpdateGlobal Time will not lead to an immediate transmission of the Global Time.

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
     - timeBaseId
     - Identification of a Time Base
   * - [in]
     - timeStamp
     - New time stamp
   * - [in]
     - userData
     - New user data(if not NULL)

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Successfully update the global time
   * - E_NOT_OK
     - updating the global Time failed


StbM_SetUserData
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType StbM_SetUserData(StbM_SynchronizedTimeBaseType timeBaseId, const StbM_UserDataType *userData)

Allows the customers to set the new user data that has to be valid for the system, which will be sent to the busses.

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
     - timeBaseId
     - Identification of a Time Base
   * - [in]
     - userData
     - New user data

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Successfully set the user data
   * - E_NOT_OK
     - setting the user data failed

StbM_BusSetGlobalTime
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType StbM_BusSetGlobalTime(StbM_SynchronizedTimeBaseType timeBaseId, const StbM_TimeTupleType *timeTuplePtr, const StbM_UserDataType *userDataPtr, const StbM_MeasurementType *measureDataPtr)

Allows the Time Base Provider Modules to forward a new Global Time tuple(i.e., the Received Time Tuple) to the StbM.

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
     - timeBaseId
     - Identification of a Time Base
   * - [in]
     - timeTuplePtr
     - New Global Time Tuple value
   * - [in]
     - userDataPtr
     - New User Data(if not NULL)
   * - [in]
     - measureDataPtr
     - New measurement data

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Successfully set Global Time tuple
   * - E_NOT_OK
     - Setting the Global Time tuple failed


StbM_GetRateDeviation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType StbM_GetRateDeviation(StbM_SynchronizedTimeBaseType timeBaseId, StbM_RateDeviationType *rateDeviation)

Returns value of the current rate deviation of a Time Base.

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
     - timeBaseId
     - Identification of a Time Base
   * - [out]
     - rateDeviation
     - Value of the current rate deviation of a Time Base

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Successfully get rate deviation of a Time Base
   * - E_NOT_OK
     - Getting the rate deviation failed


StbM_SetRateCorrection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType StbM_SetRateCorrection(StbM_SynchronizedTimeBaseType timeBaseId, StbM_RateDeviationType rateDeviation)

Allows to set the rate of a Synchronized Time Base(being either a Pure Local Time Base or not)

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
     - timeBaseId
     - Identification of a Time Base
   * - [in]
     - rateDeviation
     - value of the applied rate deviation

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Successfully set rate deviation of a Time Base
   * - E_NOT_OK
     - Setting the rate deviation failed


StbM_GetTimeLeap
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType StbM_GetTimeLeap(StbM_SynchronizedTimeBaseType timeBaseId, StbM_TimeDiffType *timeJump)

Returns value of Time Leap.

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
     - timeBaseId
     - Identification of a Time Base
   * - [out]
     - timeJump
     - Time leap value

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Successfully get Time leap value
   * - E_NOT_OK
     - Getting Time leap value failed


StbM_GetTimeBaseStatus
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType StbM_GetTimeBaseStatus(StbM_SynchronizedTimeBaseType timeBaseId, StbM_TimeBaseStatusType *timeBaseStatus)

Returns detailed status information for a Synchronized(or Pure Local) Time Base.

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
     - timeBaseId
     - Identification of a Time Base
   * - [out]
     - timeBaseStatus
     - Status of the Synchronized(or Pure Local) Time Base

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Successfully get status of the Time Base
   * - E_NOT_OK
     - Getting status of the Time Base failed


StbM_StartTimer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType StbM_StartTimer(StbM_SynchronizedTimeBaseType timeBaseId, StbM_CustomerIdType customerId, const StbM_TimeStampType *expireTime)

Sets a time value, which the Time Base value is compared against.

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
     - timeBaseId
     - Identification of a Time Base
   * - [in]
     - customerId
     - The ID of the customer that is being used
   * - [in]
     - expireTime
     - Time value relative to current Time Base value of the Notification

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Successfully start the timer
   * - E_NOT_OK
     - Starting the timer failed


StbM_GetSyncTimeRecordHead
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType StbM_GetSyncTimeRecordHead(StbM_SynchronizedTimeBaseType timeBaseId, StbM_SyncRecordTableHeadType *syncRecordTableHead)

Accesses to the recorded snapshot data Header of the table belonging to the Synchronized Time Base.

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
     - timeBaseId
     - Identification of a Time Base
   * - [out]
     - syncRecordTableHead
     - Header of the table

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Successful
   * - E_NOT_OK
     - Failed


StbM_TriggerTimeTransmission
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType StbM_TriggerTimeTransmission(StbM_SynchronizedTimeBaseType timeBaseId)

Called by the <Upper Layer> to force the Timesync Modules to transmit the current Time Base again due to an incremented timeBaseUpdateCounter[timeBaseId].

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
     - timeBaseId
     - Identification of a Time Base

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Successful
   * - E_NOT_OK
     - Failed

StbM_GetTimeBaseUpdateCounter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    uint8 StbM_GetTimeBaseUpdateCounter(StbM_SynchronizedTimeBaseType timeBaseId)

Allows the Timesync Modules to detect, whether a Time Base should be transmitted immediately in the subsequent <Bus>TSyn_MainFunction() cycle.

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
     - timeBaseId
     - Identification of a Time Base

**Return type**
   uint8

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - Counter
     - value belonging to the Time Base, that indicates a Time Base update to the Timesync Modules


StbM_GetMasterConfig
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType StbM_GetMasterConfig(StbM_SynchronizedTimeBaseType timeBaseId, StbM_MasterConfigType *masterConfig)

Indicates if the functionality for a system wide master(e.g. StbM_SetGlobalTime) for a given Time Base is available or not.

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
     - timeBaseId
     - Identification of a Time Base
   * - [out]
     - masterConfig
     - Indicates, if system wide master functionality is supported

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Successful
   * - E_NOT_OK
     - Failed
