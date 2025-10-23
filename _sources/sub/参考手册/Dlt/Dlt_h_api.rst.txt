
类型定义 Type Definitions
------------------------------------------------------------------------------------------------
.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Type Name
     - Type
     - Description
   * - Dlt_ConfigType
     - Structure
     - The type of the data structure containing the initialization data for DLT (implementation specific)
   * - Dit_MessageType
     - Enumeration
     - Describes the type of the message (LOG=0x00, APP_TRACE=0x01, NW_TRACE=0x02, CONTROL=0x03)
   * - Dlt_MessageIDType
     - Array (uint8[4])
     - Contains the unique MessageID for a message (only relevant in non-verbose mode)
   * - Dit_MessageNetworkTraceInfoType
     - Enumeration
     - Describes transported type of a DLT BUSMESSAGE (IPC=0x01, CAN=0x02, FLEXRAY=0x03, MOST=0x04, ETHERNET=0x05, SOMEIP=0x06)

      
提供的服务 Services
------------------------------------------------------------------------------------------------
Dlt_Init
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    FUNC(void, DLT_APPL_CODE) Dlt_Init(P2CONST(Dlt_ConfigType, AUTOMATIC, DLT_APPL_CONST) config)

Dlt is using the NVRamManager and is to be initialized very late in the ECU startup phase.

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
     -  Pointer to a DLT configuration structure

**Return type**
   void


Dlt_GetVersionInfo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    FUNC(void, DLT_APPL_CODE) Dlt_GetVersionInfo(P2VAR(Std_VersionInfoType, AUTOMATIC, DLT_APPL_DATA) versioninfo)

Returns the version information of this module.

**ServiceId**
   0x02

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
     - Pointer to where to store the version information of this module

**Return type**
   void


Dlt_SendTraceMessage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    FUNC(Std_ReturnType, DLT_APPL_CODE) Dlt_SendTraceMessage(
        Dlt_SessionIDType sessionId,
        P2CONST(Dlt_MessageTraceInfoType, AUTOMATIC, DLT_APPL_CONST) traceInfo,
        P2CONST(uint8, AUTOMATIC, DLT_APPL_CONST) traceData,
        uint16 traceDataLength)

The service represents the interface to be used by basic software modules or by software components to trace parameters.

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
     - sessionId
     - Number of the module (Module ID within BSW, Port defined argument value within SW-C)
   * - [in]
     - traceInfo
     - Structure containing the relevant information for filtering the message
   * - [in]
     - traceData
     - Buffer containing the parameters to be traced (payload of the Trace Message)
   * - [in]
     - traceDataLength
     - Length of the data buffer traceData

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The required operation succeeded
   * - DLT_E_MSG_TOO_LARGE
     - The message is too large for all assigned LogChannels
   * - DLT_E_NO_BUFFER
     - Not enough buffer available
   * - DLT_E_UNKNOWN_SESSION_ID
     - The provided session id is unknown

Dlt_SendLogMessage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    FUNC(Std_ReturnType, DLT_APPL_CODE) Dlt_SendLogMessage(
        Dlt_SessionIDType sessionId,
        P2CONST(Dlt_MessageLogInfoType, AUTOMATIC, DLT_APPL_CONST) logInfo,
        P2CONST(uint8, AUTOMATIC, DLT_APPL_CONST) logData,
        uint16 logDataLength)

The service represents the interface to be used by basic software modules or by software component to send Log Messages.

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
     - sessionId
     - For SW-C this is not visible (Port defined argument value), for BSWmodules it is the module number
   * - [in]
     - logInfo
     - Structure containing the relevant information for filtering the message
   * - [in]
     - logData
     - Buffer containing the parameters to be logged (payload of the Log Message)
   * - [in]
     - logDataLength
     - Length of the data buffer logData

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - DLT_OK
     - The required operation succeeded
   * - DLT_E_MSG_TOO_LARGE
     - The message is too large for all assigned LogChannels
   * - DLT_E_NO_BUFFER
     - The LogMessage could not be buffered at any assigned LogChannel
   * - DLT_E_UNKNOWN_SESSION_ID
     - The provided session id is unknown

Dlt_RegisterContext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    FUNC(Std_ReturnType, DLT_APPL_CODE) Dlt_RegisterContext(
        Dlt_SessionIDType sessionId,
        Dlt_ApplicationIDType appId,
        Dlt_ContextIDType contextId,
        P2CONST(uint8, AUTOMATIC, DLT_APPL_CONST) appDescription,
        uint8 lenAppDescription,
        P2CONST(uint8, AUTOMATIC, DLT_APPL_CONST) contextDescription,
        uint8 lenContextDescription)

The service has to be called when a software module wants to use services offered by DLT software component for a specific context.

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
     - sessionId
     - number of the module (Module ID within BSW, Port defined argument value within SW-C)
   * - [in]
     - appId
     - the ApplicationId
   * - [in]
     - contextId
     - the ContextId
   * - [in]
     - appDescription
     - Points to description string for the provided ApplicationId (max 255 chars)
   * - [in]
     - lenAppDescription
     - The length of the description for the ApplicationId string
   * - [in]
     - contextDescription
     - Points to description string for the provided context (max 255 chars)
   * - [in]
     - lenContextDescription
     - The length of the description string

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The required operation succeeded
   * - DLT_E_CONTEXT_ALREADY_REG
     - The software module context has already registered
   * - DLT_E_UNKNOWN_SESSION_ID
     - The provided session id is unknown