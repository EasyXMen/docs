接口描述(Interface Description)
===================================

导入类型(Import Types)
-----------------------------------

.. list-table:: 
   :widths: 15 20 20
   :header-rows: 1

   * - module Name
     - Header File
     - Imported Type
     
   * - Std
     - Std_Types.h
     - Std_ReturnType

   * - Std
     - Std_Types.h
     - Std_VersionInfoType

类型定义(Type Definitions)
--------------------------------------

.. list-table:: 
   :widths: 15 10 25 15
   :header-rows: 1

   * - Type Name
     - Type
     - Description
     - Range
     
   * - Det_ConfigType
     - Structure
     - Configuration data structure of the Det module
     - N/A
      
提供的服务(Services)
-----------------------------------------

Det_Init
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. Return type 和 Return values 是可选板块，视情况而定
.. 小段的代码，用code，大段地用 code-block，此处用 code

.. code:: 

   void Det_Init(const Det_ConfigType *ConfigPtr)

Service to initialize the Default Error Tracer.

**Service ID**
   0x00

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
     - Pointer to the selected configuration set.

   * - [out]
     - N/A
     - N/A

   * - [in,out]
     - N/A
     - N/A

**Return type**
   N/A

**Available via**
   Det.h

Det_ReportError
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. Return type 和 Return values 是可选板块，视情况而定
.. 小段的代码，用code，大段地用 code-block，此处用 code

.. code:: 

   Std_ReturnType Det_ReportError(uint16 ModuleId, uint8 InstanceId, uint8 ApiId, uint8 ErrorId)

Service to report development errors.

**Service ID**
   0x01

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
     - ModuleId
     - Module ID of calling module.

   * - [in]
     - InstanceId
     - The identifier of the index based instance of a module, starting from 0, If the module is a single instance module it shall pass 0 as the InstanceId.

   * - [in]
     - ApiId
     - ID of API service in which error is detected (defined in SWS of calling module)

   * - [in]
     - ErrorId
     - ID of detected development error (defined in SWS of calling module).

   * - [out]
     - N/A
     - N/A

   * - [in,out]
     - N/A
     - N/A

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description

   * - E_OK
     - never returns a value, but has a return type for compatibility with services and hooks

   * - E_NOT_OK
     - N/A

**Available via**
   Det.h

Det_Start
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. Return type 和 Return values 是可选板块，视情况而定
.. 小段的代码，用code，大段地用 code-block，此处用 code

.. code:: 

   void Det_Start(void)

Service to start the Default Error Tracer.

**Service ID**
   0x02

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
     - N/A
     - N/A

   * - [out]
     - N/A
     - N/A

   * - [in,out]
     - N/A
     - N/A

**Return type**
   N/A

**Available via**
   Det.h

Det_ReportRuntimeError
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. Return type 和 Return values 是可选板块，视情况而定
.. 小段的代码，用code，大段地用 code-block，此处用 code

.. code:: 

   Std_ReturnType Det_ReportRuntimeError(uint16 ModuleId, uint8 InstanceId, uint8 ApiId, uint8 ErrorId)

Service to report runtime errors. If a callout has been configured then this callout shall be called.

**Service ID**
   0x04

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
     - ModuleId
     - Module ID of calling module.

   * - [in]
     - InstanceId
     - The identifier of the index based instance of a module, starting from 0, If the module is a single instance module it shall pass 0 as the InstanceId.

   * - [in]
     - ApiId
     - ID of API service in which error is detected (defined in SWS of calling module)

   * - [in]
     - ErrorId
     - ID of detected runtime error (defined in SWS of calling module).

   * - [out]
     - N/A
     - N/A

   * - [in,out]
     - N/A
     - N/A

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description

   * - E_OK
     - returns always E_OK (is required for services)

   * - E_NOT_OK
     - N/A

**Available via**
   Det.h

Det_ReportTransientFault
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. Return type 和 Return values 是可选板块，视情况而定
.. 小段的代码，用code，大段地用 code-block，此处用 code

.. code:: 

   Std_ReturnType Det_ReportTransientFault(uint16 ModuleId, uint8 InstanceId, uint8 ApiId, uint8 FaultId)

Service to report transient faults. If a callout has been configured than this callout shall be called and the returned value of the callout shall be returned. Otherwise it returns immediately with E_OK.

**Service ID**
   0x05

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
     - ModuleId
     - Module ID of calling module.

   * - [in]
     - InstanceId
     - The identifier of the index based instance of a module, starting from 0, If the module is a single instance module it shall pass 0 as the InstanceId.

   * - [in]
     - ApiId
     - ID of API service in which transient fault is detected (defined in SWS of calling module)

   * - [in]
     - FaultId
     - ID of detected transient fault (defined in SWS of calling module).

   * - [out]
     - N/A
     - N/A

   * - [in,out]
     - N/A
     - N/A

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description

   * - E_OK
     - If no callout exists it shall return E_OK, otherwise it shall return the value of the configured callout. In case several callouts are configured the logical or (sum) of the callout return values shall be returned. Rationale: since E_OK=0, E_OK will be only returned if all are E_OK, and for multiple error codes there is a good chance to detect several of them.

   * - E_NOT_OK
     - N/A

**Available via**
   Det.h

Det_GetVersionInfo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. Return type 和 Return values 是可选板块，视情况而定
.. 小段的代码，用code，大段地用 code-block，此处用 code

.. code:: 

   void Det_GetVersionInfo(Std_VersionInfoType *  versioninfo)

Returns the version information of this module.

**Service ID**
   0x023

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
     - N/A
     - N/A

   * - [out]
     - versioninfo
     - Pointer to where to store the version information of this module.

   * - [in,out]
     - N/A
     - N/A

**Return type**
   N/A

**Available via**
   Det.h


回调函数
-----------
格式同提供的服务

<User_Error_Hooks>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. Return type 和 Return values 是可选板块，视情况而定
.. 小段的代码，用code，大段地用 code-block，此处用 code

.. code:: 

   Std_ReturnType <User_Error_Hooks>(uint16 ModuleId, uint8 InstanceId, uint8 ApiId, uint8 ErrorId)

If Det_ReportError function is called, all configured callout functions shall be called. User_ErrorHooks functions should have the Service ID 0x10.

**Service ID**
   0x10

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
     - ModuleId
     - Module ID of calling module.

   * - [in]
     - InstanceId
     - The identifier of the index based instance of a module, starting from 0, If the module is a single instance module it shall pass 0 as the InstanceId.

   * - [in]
     - ApiId
     - ID of API service in which error is detected (defined in SWS of calling module)

   * - [in]
     - ErrorId
     - ID of detected runtime error (defined in SWS of calling module).

   * - [out]
     - N/A
     - N/A

   * - [in,out]
     - N/A
     - N/A

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description

   * - E_OK
     - returns always E_OK (is required for services)

   * - E_NOT_OK
     - N/A

**Available via**
   Det_Externals.h

<DetReportRuntimeErrorCallout>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. Return type 和 Return values 是可选板块，视情况而定
.. 小段的代码，用code，大段地用 code-block，此处用 code

.. code:: 

   Std_ReturnType <DetReportRuntimeErrorCallout>(uint16 ModuleId, uint8 InstanceId, uint8 ApiId, uint8 ErrorId)

If Det_ReportRuntimeError function is called, all configured callout functions shall be called.  DetReportRuntimeErrorCallout functions should have the Service ID 0x11.

**Service ID**
   0x11

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
     - ModuleId
     - Module ID of calling module.

   * - [in]
     - InstanceId
     - The identifier of the index based instance of a module, starting from 0, If the module is a single instance module it shall pass 0 as the InstanceId.

   * - [in]
     - ApiId
     - ID of API service in which error is detected (defined in SWS of calling module)

   * - [in]
     - ErrorId
     - ID of detected runtime error (defined in SWS of calling module).

   * - [out]
     - N/A
     - N/A

   * - [in,out]
     - N/A
     - N/A

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description

   * - E_OK
     - returns always E_OK (is required for services)

   * - E_NOT_OK
     - N/A

**Available via**
   Det_Externals.h

<DetReportTransientFaultCallout>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. Return type 和 Return values 是可选板块，视情况而定
.. 小段的代码，用code，大段地用 code-block，此处用 code

.. code:: 

   Std_ReturnType <DetReportTransientFaultCallout>(uint16 ModuleId, uint8 InstanceId, uint8 ApiId, uint8 FaultId)

If Det_ReportTransientFault function is called, all configured callout functions are called.  DetReportTransientFaultCallout functions should have the Service ID 0x12.

**Service ID**
   0x12

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
     - ModuleId
     - Module ID of calling module.

   * - [in]
     - InstanceId
     - The identifier of the index based instance of a module, starting from 0, If the module is a single instance module it shall pass 0 as the InstanceId.

   * - [in]
     - ApiId
     - ID of API service in which transient fault is detected (defined in SWS of calling module)

   * - [in]
     - ErrorId
     - ID of detected transient fault (defined in SWS of calling module).

   * - [out]
     - N/A
     - N/A

   * - [in,out]
     - N/A
     - N/A

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description

   * - E_OK
     - Value is propagated to caller of Det_ReportTransientFault.

   * - E_NOT_OK
     - N/A

**Available via**
   Det_Externals.h

配置函数(Configuration Functions)
----------------------------------------
格式同提供的服务

The format is the same as the provided services

依赖的服务(Dependent Services)
-------------------------------------
格式同提供的服务

The format is the same as the provided services

.. list-table:: 
   :widths: 15 20 20
   :header-rows: 1

   * - API Function
     - Header File
     - Description
     
   * - Dlt_DetForwardErrorTrace
     - Dlt_Det.h
     - Service to forward error reports from Det to Dlt.
