
      
提供的服务 Services
---------------------------------


CDD_FVM_Init
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void CDD_FVM_Init(const CDD_FVM_ConfigType *config)

Initializes the the FVM module.

**Sync/Async**
   TRUE

**Reentrancy**
   FALSE

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - config
     - Pointer to a selected configuration structure

**Return type**
   void


CDD_FVM_DeInit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void CDD_FVM_DeInit(void)

This service stops the fvm.

**Sync/Async**
   TRUE

**Reentrancy**
   FALSE


**Return type**
   void


CDD_FVM_GetVersionInfo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void CDD_FVM_GetVersionInfo(Std_VersionInfoType *versioninfo)

Returns the version information of this module.

**Sync/Async**
   TRUE

**Reentrancy**
   TRUE

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [out]
     - versioninfo
     - Pointer to where to store the version information of this module.

**Return type**
   void


CDD_FVM_GetRxFreshness
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType CDD_FVM_GetRxFreshness(uint16 FVMFreshnessValueID, const uint8 *FVMTruncatedFreshnessValue, uint32 FVMTruncatedFreshnessValueLength, uint16 FVMAuthVerifyAttempts, uint8 *FVMFreshnessValue, uint32 *FVMFreshnessValueLength)

This interface is used by the FVM to obtain the current freshness value.

**Sync/Async**
   TRUE

**Reentrancy**
   TRUE

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - FVMFreshnessValueID
     - Holds the identifier of the freshness value.
   * - [in]
     - FVMTruncatedFreshnessValue
     - Holds the truncated freshness value that was contained in the Secured I-PDU.
   * - [in]
     - FVMTruncatedFreshnessValueLength
     - Holds the length in bits of the truncated freshness value.
   * - [in]
     - FVMAuthVerifyAttempts
     - Hold the number of authentication verify attempts of this PDU since the last reception.
   * - [out]
     - FVMFreshnessValue
     - Holds the freshness value to be used for the calculation of the authenticator.
   * - [inout]
     - FVMFreshnessValueLength
     - Holds the length in bits of the freshness value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - request successful.
   * - E_NOT_OK
     - request failed, a freshness value cannot be provided due to general issues for freshness orx this FreshnessValueId.
   * - E_BUSY
     - The freshness information can temporarily not be provided.

CDD_FVM_GetRxFreshnessAuthData
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType CDD_FVM_GetRxFreshnessAuthData(uint16 FVMFreshnessValueID, const uint8 *FVMTruncatedFreshnessValue, uint32 FVMTruncatedFreshnessValueLength, const uint8 *FVMAuthDataFreshnessValue, uint16 FVMAuthDataFreshnessValueLength, uint16 FVMAuthVerifyAttempts, uint8 *FVMFreshnessValue, uint32 *FVMFreshnessValueLength)

This interface is used by the FVM to obtain the current freshness value.

**Sync/Async**
   FALSE

**Reentrancy**
   FALSE

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - FVMFreshnessValueID
     - Holds the identifier of the freshness value.
   * - [in]
     - FVMTruncatedFreshnessValue
     - Holds the truncated freshness value that was contained in the Secured I-PDU.
   * - [in]
     - FVMTruncatedFreshnessValueLength
     - Holds the length in bits of the truncated freshness value.
   * - [in]
     - FVMAuthDataFreshnessValue
     - The parameter holds a part of the received, not yet authenticated PDU.
   * - [in]
     - FVMAuthDataFreshnessValueLength
     - This is the length value in bits that holds the freshness from
   * - [in]
     - FVMAuthVerifyAttempts
     - Holds the number of authentication verify attempts of this PDU since the last reception.
   * - [out]
     - FVMFreshnessValue
     - Holds the freshness value to be used for the calculation of the authenticator.
   * - [inout]
     - FVMFreshnessValueLength
     - Holds the length in bits of the freshness value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - request successful.
   * - E_NOT_OK
     - request failed, a freshness value cannot be provided due to general issues for freshness orx this FreshnessValueId.
   * - E_BUSY
     - The freshness information can temporarily not be provided.

CDD_FVM_GetTxFreshness
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType CDD_FVM_GetTxFreshness(uint16 FVMFreshnessValueID, uint8 *FVMFreshnessValue, uint32 *FVMFreshnessValueLength)

This API returns the freshness value from the Most Significant Bits in the first byte in the array (FVMFreshnessValue), in big endian format.

**Sync/Async**
   TRUE

**Reentrancy**
   TRUE

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - FVMFreshnessValueID
     - Holds the identifier of the freshness value.
   * - [out]
     - FVMFreshnessValue
     - Holds the freshness value to be used for the calculation of the authenticator.
   * - [inout]
     - FVMFreshnessValueLength
     - Holds the length in bits of the freshness value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - request successful.
   * - E_NOT_OK
     - request failed, a freshness value cannot be provided due to general issues for freshness orx this FreshnessValueId.
   * - E_BUSY
     - The freshness information can temporarily not be provided.

CDD_FVM_GetTxFreshnessTruncData
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType CDD_FVM_GetTxFreshnessTruncData(uint16 FVMFreshnessValueID, uint8 *FVMFreshnessValue, uint32 *FVMFreshnessValueLength, uint8 *FVMTruncatedFreshnessValue, uint32 *FVMTruncatedFreshnessValueLength)

This interface is used by the FVM to obtain the current freshness value.The interface function provides also the truncated freshness transmitted in the secured I-PDU.

**Sync/Async**
   TRUE

**Reentrancy**
   TRUE

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - FVMFreshnessValueID
     - Holds the identifier of the freshness value.
   * - [out]
     - FVMFreshnessValue
     - Holds the current freshness value.
   * - [inout]
     - FVMFreshnessValueLength
     - Holds the length in bits of the freshness value.
   * - [out]
     - FVMTruncatedFreshnessValue
     - Holds the truncated freshness to be included into the Secured I-PDU.
   * - [inout]
     - FVMTruncatedFreshnessValueLength
     - Provides the truncated freshness length configured for this freshness.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - request successful.
   * - E_NOT_OK
     - request failed, a freshness value cannot be provided due to general issues for freshness orx
   * - E_BUSY
     - The freshness information can temporarily not be provided.

CDD_FVM_SPduTxConfirmation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType CDD_FVM_SPduTxConfirmation(uint16 FVMFreshnessValueID)

This interface is used by the FVM to indicate that the Secured I-PDU has been initiated for transmission.

**Sync/Async**
   TRUE

**Reentrancy**
   TRUE

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - FVMFreshnessValueID
     - Holds the identifier of the freshness value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Notification successful.
   * - E_NOT_OK
     - Notification failed.

CDD_FVM_RxSecOCVerificationNotify
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void CDD_FVM_RxSecOCVerificationNotify(SecOC_VerificationStatusType verificationStatus)

This function is used to notify the reception of SecOC verification status.

**Sync/Async**
   TRUE

**Reentrancy**
   FALSE

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - verificationStatus
     - SecOC verification status to notify.

**Return type**
   void


CDD_FVM_RxIndication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void CDD_FVM_RxIndication(PduIdType RxPduId, const PduInfoType *PduInfoPtr)

This function is the Rx indication callback function for the CDD FVM module.

**Sync/Async**
   TRUE

**Reentrancy**
   FALSE

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - RxPduId
     - ID of the received PDU.
   * - [in]
     - PduInfoPtr
     - Pointer to the received PDU data.

**Return type**
   void


CDD_FVM_MainFunctionMaster
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void CDD_FVM_MainFunctionMaster(void)

This function is the main function for the master ECU of the CDD FVM module.

**Sync/Async**
   TRUE

**Reentrancy**
   FALSE


**Return type**
   void


CDD_FVM_SlaveRequestSyncMsg
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType CDD_FVM_SlaveRequestSyncMsg(uint16 syncMsgId)

This function is used to request a synchronization message by the slave.

**Sync/Async**
   TRUE

**Reentrancy**
   FALSE

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - syncMsgId
     - ID of the synchronization message.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - Standard
     - return type indicating the success or failure of the function.

