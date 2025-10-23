
类型定义 Type Definitions
--------------------------------------------------------------------------------
.. 如果没有就不存在该章节，或为None

.. list-table:: 
   :widths: 15 5 20
   :header-rows: 1

   * - Type Name
     - Type
     - Description
     
   * - DoIP_ConfigType
     - Structure
     - Configuration data structure of the DoIP module

      
提供的服务 Services
--------------------------------------------------------------------------------
DoIP_Init
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void DoIP_Init(const DoIP_ConfigType *doipConfigPtr)

This service initializes all global variables of the DoIP module.After return of this service the DoIP module is operational.

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
     - doipConfigPtr
     - PB configuration.

**Return type**
   void


DoIP_GetVersionInfo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void DoIP_GetVersionInfo(Std_VersionInfoType *versionInfo)

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
     - versionInfo
     - Pointer to where to store the version information of this module.

**Return type**
   void


DoIP_ActivationLineSwitch
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void DoIP_ActivationLineSwitch(boolean *active)

This function is used to notify the DoIP on a switch of the DoIPActivationLine.

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
   * - [inout]
     - active
     - Specifies activate or deactivate，and return status of DoIP.

**Return type**
   void


DoIP_TpTransmit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType DoIP_TpTransmit(PduIdType pdurTxPduId, const PduInfoType *pduInfoPtr)

This service is called to request the transfer data from the PduRouter to the SoAd.It is used to indicate the transmission which will be performed in the DoIP_Mainfunction.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant for different PduIds. Non reentrant for the same PduId.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - pdurTxPduId
     - DoIP unique identifier of the PDU to be transmitted by the PduR
   * - [in]
     - pduInfoPtr
     - Tx Pdu information structure which contains the length of the DoIPTxMessage.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Get The request has been accepted.
   * - E_NOT_OK
     - The request has not been accepted.

DoIP_TpCancelTransmit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType DoIP_TpCancelTransmit(PduIdType pdurTxPduId)

This service primitive is used to cancel the transfer of pending DoIPPduRTxIds. The connection is identified by DoIPPduRTxId. When the function returns, no transmission is in progress anymore with the given DoIPPduRTxId identifier.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant for different PduIds. Non reentrant for the same PduId.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - pdurTxPduId
     - DoIP unique identifier ofthe PDU to be transmitted by the PduR

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Transmit cancellation request of the specified DoIPPduRTxId is accepted.
   * - E_NOT_OK
     - The transmit cancellation request of the DoIPPduRTxId has been rejected.

DoIP_TpCancelReceive
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType DoIP_TpCancelReceive(PduIdType pdurRxPduId)

By calling this API with the corresponding DoIPPduRRxId the currently ongoing data reception is terminated immediately. When the function returns, no reception is in progress anymore with the given DoIPPduRRxId identifier.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant for different PduIds. Non reentrant for the same PduId.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - pdurRxPduId
     - DoIP unique identifier of the PDU for which reception shall be canceled by the PduR

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Reception was canceled successfully.
   * - E_NOT_OK
     - Reception was not canceled.

DoIP_IfTransmit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType DoIP_IfTransmit(PduIdType pdurTxPduId, const PduInfoType *pduInfoPtr)

Requests transmission of an I-PDU.

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
     - pdurTxPduId
     - Identification of the I-PDU.
   * - [in]
     - pduInfoPtr
     - Provides the destination buffer (SduDataPtr) and the number of bytes to be copied (SduLength).

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request is accepted by the destination module.
   * - E_NOT_OK
     - Request is not accepted by the destination module.

DoIP_IfCancelTransmit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType DoIP_IfCancelTransmit(PduIdType pdurTxPduId)

Requests cancellation of an ongoing transmission of an I-PDU in a lower layer communication interface module.

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
     - pdurTxPduId
     - Identification of the I-PDU to be cancelled.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Cancellation was executed successfully by the destination module.
   * - E_NOT_OK
     - Cancellation was rejected by the destination module.

DoIP_MainFunction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void DoIP_MainFunction(void)

Schedules the Diagnostic over IP module. (Entry point for scheduling)

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant


**Return type**
   void


DoIP_MainFunction_HighFrequency
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void DoIP_MainFunction_HighFrequency(void)

Schedules the Diagnostic over IP module. (Entry point for scheduling) for hight frequency tasks.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant


**Return type**
   void


回调函数 Callback Function
------------------------------------------------------------------------------------
.. include:: DoIP_Cbk_h_api.rst