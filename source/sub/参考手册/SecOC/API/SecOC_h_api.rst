

.. list-table:: 
   :widths: 15 5 20
   :header-rows: 1

   * - Type Name
     - Type
     - Description

   * - SecOC_StateType
     - enum SecOC_StateTag
     - States of the SecOC module.

   * - SecOC_ConfigType
     -  SecOC_PbConfigType
     - Structure for the configuration of the SecOC module.

   * - SecOC_StateTag
     - enum
     - States of the SecOC module.


      
提供的服务 Services
------------------------------------------------------------------------
SecOC_Init
~~~~~~~~~~~~~~~~~~~

.. code::

    void SecOC_Init(const SecOC_ConfigType *config)

Initializes the the SecOC module.

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
     - config
     - Pointer to a selected configuration structure.

**Return type**
   void


SecOC_DeInit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void SecOC_DeInit(void)

This service stops the secure onboard communication. All buffered I-PDU are removed and have to be obtained again, if needed, after SecOC_Init has been called.

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant


**Return type**
   void


SecOC_GetVersionInfo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void SecOC_GetVersionInfo(Std_VersionInfoType *versioninfo)

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


SecOC_IfTransmit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType SecOC_IfTransmit(PduIdType TxPduId, const PduInfoType *PduInfoPtr)

Requests transmission of a PDU.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant for different PduIds.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - TxPduId
     - Identifier of the PDU to be transmitted.
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

SecOC_TpTransmit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType SecOC_TpTransmit(PduIdType TxPduId, const PduInfoType *PduInfoPtr)

Requests transmission of a PDU.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant for different PduIds.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - TxPduId
     - Identifier of the PDU to be transmitted.
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

SecOC_IfCancelTransmit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType SecOC_IfCancelTransmit(PduIdType TxPduId)

Requests cancellation of an ongoing transmission of a PDU in a lower layer communication module.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant for different PduIds.

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
     - Cancellation was executed successfully by the destination module.
   * - E_NOT_OK
     - Cancellation was rejected by the destination module.

SecOC_TpCancelTransmit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType SecOC_TpCancelTransmit(PduIdType TxPduId)

Requests cancellation of an ongoing transmission of a PDU in a lower layer communication module.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant for different PduIds.

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
     - Cancellation was executed successfully by the destination module.
   * - E_NOT_OK
     - Cancellation was rejected by the destination module.

SecOC_TpCancelReceive
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType SecOC_TpCancelReceive(PduIdType RxPduId)

Requests cancellation of an ongoing reception of a PDU in a lower layer transport protocol module.

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
     - Cancellation was executed successfully by the destination module.
   * - E_NOT_OK
     - Cancellation was rejected by the destination module.

SecOC_VerifyStatusOverride
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType SecOC_VerifyStatusOverride(uint16 ValueID, SecOC_OverrideStatusType overrideStatus, uint8 numberOfMessagesToOverride)

This service provides the ability to force specific behaviour of SecOc: accept or drop an I-PDU with or without performing the verification of authenticator or independent of the authenticator verification result, and force a specific result for SecOC_VerificationResultType allowing additional fault handling in the application.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant for different Freshness ValueIDs

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - ValueID
     - ID of the Freshness Value used to control the verification behaviour of all assigned Secured I-PDUs according to the override Status.Or ValueID is the DataID of a Secured I-PDU that shall be controlled by the overrideStatus.
   * - [in]
     - overrideStatus
     - Defines whether verification is executed and whether the I-PDU is passed on, and for how long the override is active.
   * - [in]
     - numberOfMessagesToOverride
     - Number of sequential verification to override when using a specific counter for authentication verification.

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
     - request failed

SecOC_SendDefaultAuthenticationInformation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType SecOC_SendDefaultAuthenticationInformation(uint16 FreshnessValueID, boolean sendDefaultAuthenticationInformation)

The service provides the ability to enable the sending of un-authenticated PDU to lower layer.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant for different FreshnessValueIDs.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - FreshnessValueID
     - ID of the Freshness Value for which sending SecOCDefaultAuthenticationInformationPattern should be enabled.
   * - [in]
     - sendDefaultAuthenticationInformation
     - FALSE - sending SecOCDefaultAuthenticationInformation Pattern shall be disabled for given FreshnessValueID TRUE - sending SecOCDefaultAuthenticationInformationPattern shall be enabled for given FreshnessValueID.

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

