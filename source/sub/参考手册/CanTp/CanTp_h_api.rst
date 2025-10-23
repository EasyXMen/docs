
类型定义（Type Definition）
--------------------------------------
.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Type Name
     - Type
     - Description
   * - CanTp_ConfigType
     - Structure
     - 表示CanTp的PB配置结构体
       
       Represents the PB configuration structure of CanTp

      
提供的服务（Provided services）
-----------------------------------------
CanTp_RxIndication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void CanTp_RxIndication(PduIdType RxPduId, const PduInfoType *PduInfoPtr)

Notify CanTp to receive CAN N-PDU frame.

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
     - RxPduId
     - Identification of the received N-PDU.
   * - [in]
     - PduInfoPtr
     - Provides the received PDU length,a pointer to a buffer and the MetaData.

**Return type**
   void


CanTp_TxConfirmation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void CanTp_TxConfirmation(PduIdType TxPduId, Std_ReturnType result)

Notify CanTp to Confirm the transmission of CAN N-PDU frame.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant for different Ids. Non reentrant for the same Id.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - TxPduId
     - Identification of the transmitted N-PDU.
   * - [in]
     - result
     - result : E_OK: The PDU was transmitted. E_NOT_OK: Transmission of the PDU failed.

**Return type**
   void


CanTp_Init
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void CanTp_Init(const CanTp_ConfigType *CfgPtr)

Service for basic initialization of CanTp module.

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - CfgPtr
     - Pointer to configuration set in Variant Post-Build.

**Return type**
   void


CanTp_GetVersionInfo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void CanTp_GetVersionInfo(Std_VersionInfoType *versioninfo)

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
   * - [inout]
     - versioninfo
     - Pointer to where to store the version information of this module.

**Return type**
   void


CanTp_Shutdown
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void CanTp_Shutdown(void)

This function to shutdown the CanTp module.

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant.


**Return type**
   void


CanTp_Transmit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType CanTp_Transmit(PduIdType TxPduId, const PduInfoType *PduInfoPtr)

The transmission of segmented or unsegmented message is requested.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant for different Ids. Non reentrant for the same Id.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - TxPduId
     - Identification of the transmitted N-PDU.
   * - [in]
     - PduInfoPtr
     - Length of and pointer to the PDU data and pointer to MetaData.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Transmit request has been accepted.
   * - E_NOT_OK
     - Transmit request has not been accepted.

CanTp_CancelTransmit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType CanTp_CancelTransmit(PduIdType TxPduId)

Requests cancellation of an ongoing transmission of a PDU in a lower layer communication module.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant for different Ids. Non reentrant for the same Id.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - TxPduId
     - Identification of the PDU to be cancelled.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - CancelTransmit request has been accepted.
   * - E_NOT_OK
     - CancelTransmit request has not been accepted.

CanTp_CancelReceive
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType CanTp_CancelReceive(PduIdType RxPduId)

Requests cancellation of an ongoing reception of a PDU in a lower layer transport protocol module.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant for different Ids. Non reentrant for the same Id.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - RxPduId
     - Identification of the PDU to be cancelled.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - CancelReceive request has been accepted.
   * - E_NOT_OK
     - CancelReceive request has not been accepted.

CanTp_ChangeParameter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType CanTp_ChangeParameter(PduIdType id, TPParameterType parameter, uint16 value)

Request to change a specific transport protocol parameter (e.g. block size).

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - id
     - Identification of the PDU which the parameter change shall affect.
   * - [in]
     - parameter
     - parameter change shall affect.
   * - [in]
     - value
     - The new value of the parameter.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The parameter was changed successfully.
   * - E_NOT_OK
     - The parameter change was rejected.

CanTp_ReadParameter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType CanTp_ReadParameter(PduIdType id, TPParameterType parameter, uint16 *value)

This service is used to read the current value of reception parameters BS and STmin for a specified N-SDU.

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - id
     - Identifier of the received N-SDU on which the reception parameter are read.
   * - [in]
     - parameter
     - Specify the parameter to which the value has to be read (BS or STmin).
   * - [out]
     - value
     - Pointer where the parameter value will be provided.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - request is accepted.
   * - E_NOT_OK
     - request is not accepted.

