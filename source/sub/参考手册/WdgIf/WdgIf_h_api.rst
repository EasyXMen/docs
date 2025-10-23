提供的服务 Services
------------------------------------------------------------------

WdgIf_SetTriggerCondition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    extern void WdgIf_SetTriggerCondition(uint8 DeviceIndex, uint16 Timeout)

Set the trigger condition value to watchdog driver.

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
     - DeviceIndex
     - uint8

   * - [in]
     - Timeout
     - uint16

**Return type**
   void

WdgIf_SetMode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    extern Std_ReturnType WdgIf_SetMode(uint8 DeviceIndex, WdgIf_ModeType WdgMode)

Set the current mode of watchdog driver.

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
     - DeviceIndex
     - uint8

   * - [in]
     - WdgMode
     - see WdgIf_ModeType, the watchdog driver mode (see Watchdog Driver)

**Return type**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description

   * - E_OK
     - success

   * - E_NOT_OK
     - failure

WdgIf_GetVersionInfo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    extern void WdgIf_GetVersionInfo(Std_VersionInfoType* versionInfoPtr)

Api for getting version info of WdgIf.

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
     - versionInfoPtr
     - Std_VersionInfoType*, Pointer to where to store the version information of this module.

**Return type**
    void
