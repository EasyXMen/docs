
类型定义
--------
.. 如果没有就不存在该章节，或为None

.. list-table:: 
   :widths: 15 5 20
   :header-rows: 1

   * - Type Name
     - Type
     - Description

   * - StbM_MeasurementType
     - struct
     - 


      
提供的服务
-----------
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

StbM_GetCurrentSafeTime
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType StbM_GetCurrentSafeTime(StbM_SynchronizedTimeBaseType timeBaseId, StbM_TimeTripleType *timeTriple, StbM_UserDataType *userData)

Returns a time triple (Local Time, Fallback Local Time, Global time and timebase status) and user data details. Note: This API shall be called with locked interrupts / within an Exclusive Area to prevent interruption (i.e., the risk that the time stamp is outdated on return of the function call).

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
     - time base reference
   * - 
     - timeTriple
     - 
   * - 
     - userData
     - 

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - successful
   * - E_NOT_OK
     - failed

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

StbM_GetFallbackVirtualLocalTime
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType StbM_GetFallbackVirtualLocalTime(StbM_SynchronizedTimeBaseType timeBaseId, StbM_VirtualLocalTimeType *localTimePtr)

Returns the fallback Virtual Local Time of the referenced Time Base.

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
     - Time Base reference
   * - [out]
     - localTimePtr
     - Current Fallback Virtual Local Time value

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - successful
   * - E_NOT_OK
     - failed

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

Allows to set the rate of a Synchronized Time Base(being either a Pure Local Time Base or not).

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

StbM_GetBusProtocolParam
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType StbM_GetBusProtocolParam(StbM_SynchronizedTimeBaseType timeBaseId, StbM_ProtocolParamType *protocolParam)

Returns the protocol parameters for the Time Base.

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
     - protocolParam
     - Protocol parameters

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Successfully get protocol parameters
   * - E_NOT_OK
     - Getting protocol parameters failed

StbM_SetBusProtocolParam
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType StbM_SetBusProtocolParam(StbM_SynchronizedTimeBaseType timeBaseId, const StbM_ProtocolParamType *protocolParam)

Sets the protocol parameters for the Time Base.

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
     - protocolParam
     - Protocol parameters

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Successfully set protocol parameters
   * - E_NOT_OK
     - Setting protocol parameters failed

StbM_GetTxFreshness
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType StbM_GetTxFreshness(uint16 StbMFreshnessValueId, uint8 *StbMFreshnessValue, uint32 *StbMFreshnessValueLength)



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
     - StbMFreshnessValueId
     - Holds the identifier of the freshness value
   * - [out]
     - StbMFreshnessValue
     - Holds the current freshness value
   * - [inout]
     - StbMFreshnessValueLength
     - Holds the length of the provided freshness in bits

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - request successful
   * - E_NOT_OK
     - request failed, a Freshness Value cannot be provided due to general issues for Freshness for this FreshnessValueId
   * - STBM_E_BUSY
     - The Freshness information can temporarily not be provided

StbM_GetTxFreshnessTruncData
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType StbM_GetTxFreshnessTruncData(uint16 StbMFreshnessValueId, uint8 *StbMFreshnessValue, uint32 *StbMFreshnessValueLength, uint8 *StbMTruncatedFreshnessValue, uint32 *StbMTruncatedFreshnessValueLength)



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
     - StbMFreshnessValueId
     - Holds the identifier of the freshness value
   * - [out]
     - StbMFreshnessValue
     - Holds the current freshness value
   * - [inout]
     - StbMFreshnessValueLength
     - Holds the length of the provided freshness in bits
   * - [out]
     - StbMTruncatedFreshnessValue
     - Holds the truncated freshness to be included into the Secured time sync message. The parameter is optional.
   * - [inout]
     - StbMTruncatedFreshnessValueLength
     - Provides the truncated freshness length configured for this freshness. The caller may adapt the value if needed or can leave it unchanged if the configured length and provided length is the same.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - request successful
   * - E_NOT_OK
     - request failed, a Freshness Value cannot be provided due to general issues for Freshness for this FreshnessValueId
   * - STBM_E_BUSY
     - The Freshness information can temporarily not be provided.

StbM_SPduTxConfirmation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void StbM_SPduTxConfirmation(uint16 StbMFreshnessValueId)



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
     - StbMFreshnessValueId
     - Holds the identifier of the freshness value

**Return type**
   void


StbM_GetRxFreshness
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType StbM_GetRxFreshness(uint16 StbMFreshnessValueId, const uint8 *StbMTruncatedFreshnessValue, uint32 StbMTruncatedFreshnessValueLength, uint16 StbMAuthVerifyAttempts, uint8 *StbMFreshnessValue, uint32 *StbMFreshnessValueLength)



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
     - StbMFreshnessValueId
     - Holds the identifier of the freshness value.
   * - [in]
     - StbMTruncatedFreshnessValue
     - Holds the truncated freshness value that was contained in the Secured time sync message
   * - [in]
     - StbMTruncatedFreshnessValueLength
     - Holds the length in bits of the truncated freshness value.
   * - [in]
     - StbMAuthVerifyAttempts
     - Holds the number of authentication verify attempts of this time sync message since the last reception. The value is 0 for the first attempt and incremented on every unsuccessful verification attempt.
   * - [out]
     - StbMFreshnessValue
     - Holds the current freshness value
   * - [inout]
     - StbMFreshnessValueLength
     - Holds the length in bits of the freshness value

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - request successful
   * - E_NOT_OK
     - request failed, a Freshness Value cannot be provided due to general issues for Freshness for this FreshnessValueId
   * - STBM_E_BUSY
     - The Freshness information can temporarily not be provided.

StbM_SetCloningOffset
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType StbM_SetCloningOffset(StbM_SynchronizedTimeBaseType timeBaseId, const StbM_TimeStampType *timeOffset)

This interface is used by the StbM to set the time offset for the Time Base.

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
     - timeOffset
     - Time offset

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Successfully set time offset
   * - E_NOT_OK
     - Setting time offset failed

StbM_CloneTimeBase
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType StbM_CloneTimeBase(StbM_SynchronizedTimeBaseType timeBaseId, StbM_CloneConfigType cloneCfg, StbM_TimeBaseStatusType statusMask, StbM_TimeBaseStatusType statusValue)

This interface is used by the StbM to clone the Time Base.

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
     - cloneCfg
     - Clone configuration
   * - [in]
     - statusMask
     - Status mask
   * - [in]
     - statusValue
     - Status value

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Successfully cloned Time Base
   * - E_NOT_OK
     - Cloning Time Base failed

