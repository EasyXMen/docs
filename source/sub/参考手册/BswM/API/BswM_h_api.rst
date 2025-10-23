
.. list-table:: 
   :widths: 15 5 20
   :header-rows: 1

   * - Type Name
     - Type
     - Description

   * - BswM_ModeType
     - uint16
     - This type identifies the modes that can be requested by BswM Users.

   * - BswM_UserType
     - uint16
     - This type identifies a BswM User that makes mode requests to the BswM.

   * - BswM_ConfigType
     - BswM_PbConfigType
     - Manager. A pointer to this structure is passed to the BSW Mode Manager initialization function for configuration. This container exists once per partition.

提供的服务(Provided services)
------------------------------------

BswM_Init
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void BswM_Init(const BswM_ConfigType *ConfigPtr)

Initializes the BSW Mode Manager.

**Sync/Async**
   TRUE

**Reentrancy**
   Conditionally Reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - ConfigPtr
     - Pointer to post-build configuration data.

**Return type**
   void


BswM_Deinit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void BswM_Deinit(void)

Deinitializes the BSW Mode Manager. After a call of BswM_Deinit, no mode processing shall be performed by BswM even if any mode requests are made or the BswM main function is called.

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant


**Return type**
   void


BswM_GetVersionInfo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void BswM_GetVersionInfo(Std_VersionInfoType *VersionInfo)

Returns the version information of this module.

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
     - VersionInfo
     - Pointer to where to store the version information of the module.

**Return type**
   void


BswM_BswMPartitionRestarted
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void BswM_BswMPartitionRestarted(void)

Function called by Restart Task if the partition containing the BswM has been restarted.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant


**Return type**
   void


BswM_RequestMode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void BswM_RequestMode(BswM_UserType requesting_user, BswM_ModeType requested_mode)

Generic function call to request modes. This function shall only be used by other BSW modules that do not have a specific mode request interface.

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
     - requesting_user
     - The user that requests the mode.
   * - [in]
     - requested_mode
     - The requested mode.

**Return type**
   void


