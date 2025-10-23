
类型定义 Type Definitions
--------------------------------------------------------------------------------

.. list-table:: 
   :widths: 15 5 20
   :header-rows: 1

   * - Type Name
     - Type
     - Description

   * - KeyM_Asn1DesType
     - struct KeyM_Asn1Type
     - Structure to hold ASN.1 data.

   * - KeyM_CryptoKeyIdType
     - uint16
     - Type definition for a crypto key identifier.

   * - KeyM_CertDataPointerType
     - uint8 *
     - Type definition for a certificate data pointer.

   * - KeyM_KH_UpdateOperationType
     - enum
     - Enumeration of key handler update operations.


      
提供的服务 Services
--------------------------------------------------------------------------------

KeyM_Init
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void KeyM_Init(const KeyM_ConfigType *ConfigPtr)

Initializes the Key Management module.

**Sync/Async**
   TRUE

**Reentrancy**
   Not reentrant.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - ConfigPtr
     - Pointer to the Key Management configuration structure.

**Return type**
   void


KeyM_Deinit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void KeyM_Deinit(void)

Deinitializes the Key Management module.

**Sync/Async**
   TRUE

**Reentrancy**
   Not reentrant.


**Return type**
   void


KeyM_GetVersionInfo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void KeyM_GetVersionInfo(Std_VersionInfoType *VersionInfo)

Retrieves version information for the Key Management module.

**Sync/Async**
   TRUE

**Reentrancy**
   Not reentrant.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [out]
     - VersionInfo
     - Pointer to the structure to store version information.

**Return type**
   void


KeyM_Start
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType KeyM_Start(KeyM_StartType StartType, const uint8 *RequestData, uint16 RequestDataLength, uint8 *ResponseData, uint16 *ResponseDataLength)

Starts the Key Management module.

**Sync/Async**
   TRUE

**Reentrancy**
   Not reentrant.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - StartType
     - Type of start operation.
   * - [in]
     - RequestData
     - Pointer to the request data.
   * - [in]
     - RequestDataLength
     - Length of the request data.
   * - [out]
     - ResponseData
     - Pointer to the response data.
   * - [out]
     - ResponseDataLength
     - Pointer to the length of the response data.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The start operation was successful.
   * - E_NOT_OK
     - The start operation failed.

KeyM_Finalize
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType KeyM_Finalize(const uint8 *RequestDataPtr, uint16 RequestDataLength, uint8 *ResponseDataPtr, uint16 ResponseMaxDataLength)

Finalizes the Key Management module.

**Sync/Async**
   TRUE

**Reentrancy**
   Not reentrant.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - RequestDataPtr
     - Pointer to the request data.
   * - [in]
     - RequestDataLength
     - Length of the request data.
   * - [out]
     - ResponseDataPtr
     - Pointer to the response data.
   * - [in]
     - ResponseMaxDataLength
     - Maximum length of the response data.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The finalize operation was successful.
   * - E_NOT_OK
     - The finalize operation failed.

KeyM_Prepare
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType KeyM_Prepare(const uint8 *RequestData, uint16 RequestDataLength, uint8 *ResponseData, uint16 *ResponseDataLength)

Prepares the Key Management module for a cryptographic operation.

**Sync/Async**
   TRUE

**Reentrancy**
   Not reentrant.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - RequestData
     - Pointer to the request data.
   * - [in]
     - RequestDataLength
     - Length of the request data.
   * - [out]
     - ResponseData
     - Pointer to the response data.
   * - [inout]
     - ResponseDataLength
     - Pointer to the length of the response data.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The preparation was successful.
   * - E_NOT_OK
     - The preparation failed.

KeyM_Update
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType KeyM_Update(const uint8 *KeyNamePtr, uint16 KeyNameLength, const uint8 *RequestDataPtr, uint16 RequestDataLength, uint8 *ResultDataPtr, uint16 ResultDataMaxLength)

Updates a key in the Key Management module.

**Sync/Async**
   TRUE

**Reentrancy**
   Not reentrant.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - KeyNamePtr
     - Pointer to the key name.
   * - [in]
     - KeyNameLength
     - Length of the key name.
   * - [in]
     - RequestDataPtr
     - Pointer to the request data.
   * - [in]
     - RequestDataLength
     - Length of the request data.
   * - [out]
     - ResultDataPtr
     - Pointer to the result data.
   * - [in]
     - ResultDataMaxLength
     - Maximum length of the result data.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The update operation was successful.
   * - E_NOT_OK
     - The update operation failed.

KeyM_Verify
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType KeyM_Verify(const uint8 *KeyNamePtr, uint16 KeyNameLength, const uint8 *RequestData, uint16 RequestDataLength, uint8 *ResponseData, uint16 *ResponseDataLength)

Verifies a key in the Key Management module.

**Sync/Async**
   TRUE

**Reentrancy**
   Not reentrant.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - KeyNamePtr
     - Pointer to the key name.
   * - [in]
     - KeyNameLength
     - Length of the key name.
   * - [in]
     - RequestData
     - Pointer to the request data.
   * - [in]
     - RequestDataLength
     - Length of the request data.
   * - [out]
     - ResponseData
     - Pointer to the response data.
   * - [inout]
     - ResponseDataLength
     - Pointer to the length of the response data.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The verify operation was successful.
   * - E_NOT_OK
     - The verify operation failed.
   * - KEYM_E_PENDING
     - The verify operation is pending.

KeyM_ServiceCertificate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType KeyM_ServiceCertificate(KeyM_ServiceCertificateType Service, const uint8 *CertNamePtr, uint32 CertNameLength, const uint8 *RequestData, uint32 RequestDataLength, uint8 *ResponseData, uint32 *ResponseDataLength)

Performs a certificate service operation in the Key Management module.

**Sync/Async**
   TRUE

**Reentrancy**
   Not reentrant.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - Service
     - Type of certificate service operation.
   * - [in]
     - CertNamePtr
     - Pointer to the certificate name.
   * - [in]
     - CertNameLength
     - Length of the certificate name.
   * - [in]
     - RequestData
     - Pointer to the request data.
   * - [in]
     - RequestDataLength
     - Length of the request data.
   * - [out]
     - ResponseData
     - Pointer to the response data.
   * - [in]
     - ResponseDataLength
     - Length of the response data.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The certificate service operation was successful.
   * - E_NOT_OK
     - The certificate service operation failed.

KeyM_ServiceCertificateByCertId
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType KeyM_ServiceCertificateByCertId(KeyM_CertificateIdType CertId, KeyM_ServiceCertificateType Service, const uint8 *RequestData, uint32 RequestDataLength, uint8 *ResponseData, uint32 *ResponseDataLength)

Performs a certificate service operation in the Key Management module.

**Sync/Async**
   TRUE

**Reentrancy**
   Not reentrant.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - CertId
     - the certificate ID.
   * - [in]
     - Service
     - Type of certificate service operation.
   * - [in]
     - RequestData
     - Pointer to the request data.
   * - [in]
     - RequestDataLength
     - Length of the request data.
   * - [out]
     - ResponseData
     - Pointer to the response data.
   * - [in]
     - ResponseDataLength
     - Length of the response data.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The certificate service operation was successful.
   * - E_NOT_OK
     - The certificate service operation failed.

KeyM_SetCertificate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType KeyM_SetCertificate(KeyM_CertificateIdType CertId, const KeyM_CertDataType *CertificateDataPtr)

Sets a certificate in the Key Management module.

**Sync/Async**
   TRUE

**Reentrancy**
   Not reentrant.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - CertId
     - ID of the certificate to set.
   * - [in]
     - CertificateDataPtr
     - Pointer to the certificate data.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The certificate was set successfully.
   * - E_NOT_OK
     - The certificate could not be set.

KeyM_GetCertificate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType KeyM_GetCertificate(KeyM_CertificateIdType CertId, KeyM_CertDataType *CertificateDataPtr)

Retrieves a certificate from the Key Management module.

**Sync/Async**
   TRUE

**Reentrancy**
   Not reentrant.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - CertId
     - ID of the certificate to retrieve.
   * - [out]
     - CertificateDataPtr
     - Pointer to the buffer to store the certificate data.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The certificate was retrieved successfully.
   * - E_NOT_OK
     - The certificate could not be retrieved.
   * - KEYM_E_KEY_CERT_SIZE_MISMATCH
     - The provided buffer is too small to hold the certificate.
   * - KEYM_E_KEY_CERT_EMPTY
     - The certificate is empty.

KeyM_VerifyCertificates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType KeyM_VerifyCertificates(KeyM_CertificateIdType CertId, KeyM_CertificateIdType CertUpperId)

Verifies a certificate chain in the Key Management module.

**Sync/Async**
   TRUE

**Reentrancy**
   Not reentrant.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - CertId
     - ID of the certificate to verify.
   * - [in]
     - CertUpperId
     - ID of the upper-level certificate in the chain.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The certificate chain was verified successfully.
   * - E_NOT_OK
     - The certificate chain could not be verified.
   * - KEYM_E_PARAMETER_MISMATCH
     - The certificate IDs are invalid.
   * - KEYM_E_CERT_INVALID_CHAIN_OF_TRUST
     - The certificate chain is invalid.

KeyM_VerifyCertificate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType KeyM_VerifyCertificate(KeyM_CertificateIdType CertId)

Verifies a certificate in the Key Management module.

**Sync/Async**
   TRUE

**Reentrancy**
   Not reentrant.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - CertId
     - ID of the certificate to verify.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The certificate was verified successfully.
   * - E_NOT_OK
     - The certificate could not be verified.
   * - KEYM_E_PARAMETER_MISMATCH
     - The certificate ID is invalid.
   * - KEYM_E_CERT_INVALID_CHAIN_OF_TRUST
     - The certificate chain is invalid.

KeyM_VerifyCertificateChain
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType KeyM_VerifyCertificateChain(KeyM_CertificateIdType CertId, const KeyM_CertDataType certChainData[], uint8 NumberOfCertificates)

Verifies a certificate chain in the Key Management module.

**Sync/Async**
   TRUE

**Reentrancy**
   Not reentrant.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - CertId
     - ID of the starting certificate in the chain.
   * - [in]
     - certChainData
     - Array of certificate data for the chain.
   * - [in]
     - NumberOfCertificates
     - Number of certificates in the chain.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The certificate chain was verified successfully.
   * - E_NOT_OK
     - The certificate chain could not be verified.

KeyM_CertElementGet
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType KeyM_CertElementGet(KeyM_CertificateIdType CertId, KeyM_CertElementIdType CertElementId, uint8 *CertElementData, uint32 *CertElementDataLength)

Retrieves a certificate element from the Key Management module.

**Sync/Async**
   TRUE

**Reentrancy**
   Not reentrant.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - CertId
     - ID of the certificate.
   * - [in]
     - CertElementId
     - ID of the certificate element to retrieve.
   * - [out]
     - CertElementData
     - Pointer to the buffer to store the certificate element data.
   * - [inout]
     - CertElementDataLength
     - Pointer to the length of the certificate element data.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The certificate element was retrieved successfully.
   * - E_NOT_OK
     - The certificate element could not be retrieved.

KeyM_CertificateElementGetByIndex
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType KeyM_CertificateElementGetByIndex(KeyM_CertificateIdType CertId, KeyM_CertElementIdType CertElementId, uint32 Index, uint8 *CertElementDataPtr, uint32 *CertElementDataLengthPtr)

Retrieves a certificate element by index from the Key Management module.

**Sync/Async**
   TRUE

**Reentrancy**
   Not reentrant.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - CertId
     - ID of the certificate.
   * - [in]
     - CertElementId
     - ID of the certificate element to retrieve.
   * - [in]
     - Index
     - Index of the certificate element to retrieve.
   * - [out]
     - CertElementDataPtr
     - Pointer to the buffer to store the certificate element data.
   * - [inout]
     - CertElementDataLengthPtr
     - Pointer to the length of the certificate element data.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The certificate element was retrieved successfully.
   * - E_NOT_OK
     - The certificate element could not be retrieved.

KeyM_CertificateElementGetCount
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType KeyM_CertificateElementGetCount(KeyM_CertificateIdType CertId, KeyM_CertElementIdType CertElementId, uint16 *CountPtr)

Retrieves the count of a specific certificate element in the Key Management module.

**Sync/Async**
   TRUE

**Reentrancy**
   Not reentrant.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - CertId
     - ID of the certificate.
   * - [in]
     - CertElementId
     - ID of the certificate element.
   * - [out]
     - CountPtr
     - Pointer to store the count of the certificate element.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The count was retrieved successfully.
   * - E_NOT_OK
     - The count could not be retrieved.

KeyM_CertElementGetFirst
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType KeyM_CertElementGetFirst(KeyM_CertificateIdType CertId, KeyM_CertElementIdType CertElementId, KeyM_CertElementIteratorType *CertElementIterator, uint8 *CertElementData, uint32 *CertElementDataLength)

Retrieves the first occurrence of a certificate element and initializes an iterator.

**Sync/Async**
   TRUE

**Reentrancy**
   Not reentrant.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - CertId
     - ID of the certificate.
   * - [in]
     - CertElementId
     - ID of the certificate element to retrieve.
   * - [out]
     - CertElementIterator
     - Pointer to the iterator to be initialized.
   * - [out]
     - CertElementData
     - Pointer to the buffer to store the certificate element data.
   * - [inout]
     - CertElementDataLength
     - Pointer to the length of the certificate element data.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The first certificate element was retrieved successfully and the iterator was initialized.
   * - E_NOT_OK
     - The first certificate element could not be retrieved or the iterator could not be initialized.

KeyM_CertElementGetNext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType KeyM_CertElementGetNext(KeyM_CertElementIteratorType *CertElementIterator, uint8 *CertElementData, uint32 *CertElementDataLength)

Retrieves the next occurrence of a certificate element using an iterator.

**Sync/Async**
   TRUE

**Reentrancy**
   Not reentrant.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [inout]
     - CertElementIterator
     - Pointer to the iterator initialized by KeyM_CertElementGetFirst.
   * - [out]
     - CertElementData
     - Pointer to the buffer to store the certificate element data.
   * - [inout]
     - CertElementDataLength
     - Pointer to the length of the certificate element data.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The next certificate element was retrieved successfully.
   * - E_NOT_OK
     - The next certificate element could not be retrieved.

KeyM_CertGetStatus
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType KeyM_CertGetStatus(KeyM_CertificateIdType CertId, KeyM_CertificateStatusType *Status)

Retrieves the status of a certificate in the Key Management module.

**Sync/Async**
   TRUE

**Reentrancy**
   Not reentrant.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - CertId
     - ID of the certificate.
   * - [out]
     - Status
     - Pointer to store the status of the certificate.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The status was retrieved successfully.
   * - E_NOT_OK
     - The status could not be retrieved.

