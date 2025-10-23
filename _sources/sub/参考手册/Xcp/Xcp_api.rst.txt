接口描述 Interface Description
==============================================

类型定义 Type Definitions
--------------------------------------------------------------------------------

.. list-table:: 
   :widths: 15 5 20 20
   :header-rows: 1

   * - Type Name
     - Type
     - Description
     - Range
     
   * - Xcp_ConfigType
     - struct
     - This is the type of the data structure containing the initialization data for XCP
     - None
      
      
提供的服务 Services
---------------------------------------------------------------------------

Xcp_Init
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Xcp_Init(const Xcp_ConfigType *Xcp_ConfigPtr)

Xcp Module Initialization Function.

**Sync/Async**
   TRUE

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
     - Xcp_ConfigPtr
     - Pointer to the Xcp module configuration data.

**Return type**
   void


Xcp_GetVersionInfo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Xcp_GetVersionInfo(Std_VersionInfoType *versioninfo)

The interface provided to the outside for returning version information.

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [out]
     - versioninfo
     - Variable for storing version information.

**Return type**
   void


Xcp_SetTransmissionMode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Xcp_SetTransmissionMode(NetworkHandleType Channel, Xcp_TransmissionModeType Mode)

The interface for enabling or disabling XCP transmission.

**Sync/Async**
   TRUE

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
     - Channel
     - An XCP protocol stack channel.
   * - [in]
     - Mode
     - The mode to be set for enabling or disabling.

**Return type**
   void


Xcp_EventIndication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Xcp_EventIndication(uint16 eventNum)

The event measurement notification interface, which sends the observation data of a DAQ list with each invocation.

**Sync/Async**
   TRUE

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
     - eventNum
     - The event number to start observation.

**Return type**
   void

Xcp_CanIfTxConfirmation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Xcp_CanIfTxConfirmation(PduIdType TxPduId)

The lower layer communication interface module confirms the transmission of a PDU, or the failure to transmit a PDU.

**Sync/Async**
   TRUE

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
     - TxPduId
     - The PDU ID to be notified as having been sent.

**Return type**
   void


Xcp_CanIfRxIndication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Xcp_CanIfRxIndication(PduIdType RxPduId, const PduInfoType *PduInfoPtr)

Indication of a received PDU from a lower layer communication interface module.

**Sync/Async**
   TRUE

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
     - RxPduId
     - Receive the XCP message PDU ID.
   * - [in]
     - PduInfoPtr
     - Pointer to the PDU of the received XCP message.

**Return type**
   void

Xcp_SoAdTxConfirmation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Xcp_SoAdTxConfirmation(PduIdType TxPduId)

The lower layer communication interface module confirms the transmission of a PDU, or the failure to transmit a PDU.

**Sync/Async**
   TRUE

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
     - TxPduId
     - The PDU ID to be notified as having been sent.

**Return type**
   void


Xcp_SoAdRxIndication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Xcp_SoAdRxIndication(PduIdType RxPduId, const PduInfoType *RxPduPtr)

Indication of a received PDU from a lower layer communication interface module.

**Sync/Async**
   TRUE

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
     - RxPduId
     - Receive the XCP message PDU ID.
   * - 
     - RxPduPtr
     - 

**Return type**
   void

void Xcp_MainFunction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Xcp_MainFunction(void)

Handle transmission timeouts, send requests, pending tasks, and deal with session status and interleaved mode according to configuration.

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant

**Parameters**
   None

**Return type**
   void