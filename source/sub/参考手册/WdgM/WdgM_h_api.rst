提供的服务 Services
------------------------------------------------------------------
WdgM_Init
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void WdgM_Init(const WdgM_ConfigType *WdgMConfigPtr)

Initializes the Watchdog Manager.

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
     - WdgMConfigPtr
     - Pointer to post-build configuration data.

**Return type**
   void


WdgM_GetMode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType WdgM_GetMode(WdgM_ModeType *Mode)

Returns the current mode of the Watchdog Manager.

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
     - Mode
     - Current mode of the Watchdog Manager.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - success
   * - E_NOT_OK
     - failure

WdgM_SetMode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType WdgM_SetMode(WdgM_ModeType Mode)

Sets the current mode of Watchdog Manager.

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
     - Mode
     - One of the configured Watchdog Manager modes.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Successfully changed to the new mode
   * - E_NOT_OK
     - Changing to the new mode failed

WdgM_CheckpointReached
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType WdgM_CheckpointReached(WdgM_SupervisedEntityIdType SEID, WdgM_CheckpointIdType CheckpointID)

Indicates to the Watchdog Manager that a Checkpoint within a Supervised Entity has been reached.

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
     - SEID
     - Identifier of the Supervised Entity that reports a Checkpoint.
   * - [in]
     - CheckpointID
     - Identifier of the Checkpoint within a Supervised Entity that has been reached.


**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Successfully updated alive counter
   * - E_NOT_OK
     - updated failed

WdgM_GetGlobalStatus
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType WdgM_GetGlobalStatus(WdgM_GlobalStatusType *Status)

Returns the global supervision status of the Watchdog Manager.

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
     - Status
     - Global supervision status of the Watchdog Manager.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Current supervision status successfully returned
   * - E_NOT_OK
     - Returning current supervision status failed

WdgM_PerformReset
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void WdgM_PerformReset(void)

Instructs the Watchdog Manager to cause a watchdog reset.

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant


**Return type**
   void

WdgM_GetFirstExpiredSEID
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType WdgM_GetFirstExpiredSEID(WdgM_SupervisedEntityIdType *SEID)

Returns SEID that first reached the state WDGM_LOCAL_STATUS_EXPIRED.

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
     - SEID
     - Identifier of the supervised entity that first reached the state WDGM_LOCAL_STATUS_EXPIRED.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Success
   * - E_NOT_OK
     - failure

WdgM_GetLocalStatus
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType WdgM_GetLocalStatus(WdgM_SupervisedEntityIdType SEID, WdgM_LocalStatusType *Status)

Returns the supervision status of an individual Supervised Entity.

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
     - SEID
     - Identifier of the supervised entity whose supervision status shall be returned.
   * - [out]
     - Status
     - Supervision status of the given supervised entity.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Current supervision status successfully returned
   * - E_NOT_OK
     - Returning current supervision status failed

WdgM_DeInit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void WdgM_DeInit(void)

Deinit the local status of all SE in the Mode.

**Sync/Async**
   Synchronous

**Reentrancy**
   Reentrant

**Parameters**
   None

**Return type**
   void


WdgM_GetVersionInfo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void WdgM_GetVersionInfo(Std_VersionInfoType *VersionInfo)

Gets the version of Watchdog Manager.

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
     - Pointer to where to store the version information of the module WdgM.

**Return type**
   void