
类型定义 Type Definitions
--------------------------------------------------------------------------------

.. list-table:: 
   :widths: 15 5 20
   :header-rows: 1

   * - Type Name
     - Type
     - Description

   * - KeyM_CertPCfgType
     - struct KeyM_CertType
     - Structure to hold certificate configuration data.

   * - KeyM_CryptoCsmVerifyJobType
     - enum
     - Enumeration of crypto CSM verify job types.

   * - KeyM_CryptoKeyGenerationType
     - enum
     - Enumeration of crypto key generation types.

   * - KeyM_StorageType
     - enum
     - Enumeration of storage types for keys.

   * - KeyM_CertAlgorithmType
     - enum
     - Enumeration of certificate algorithms.

   * - KeyM_CertFormatType
     - enum
     - Enumeration of certificate formats.

   * - KeyM_CertEleStructType
     - enum
     - Enumeration of certificate element structures.


      
提供的服务 Services
--------------------------------------------------------------------------------
KEYM_DET_REPORT
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    static void KEYM_DET_REPORT(uint8 ApiId, uint8 ErrorId)

Reports an error to the DET (Diagnostic Error Trap) module.

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
     - ApiId
     - API identifier of the function that detected the error.
   * - [in]
     - ErrorId
     - Error identifier specifying the type of error.

**Return type**
   void


CONST
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    CONST(KeyM_NvmBlockPCfgType, KEYM_CONST) KeyM_NvmBlockPCfg[KEYM_NVM_BLOCK_NUM]



**Sync/Async**
   

**Reentrancy**
   


**Return type**
   


CONST
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    CONST(KeyM_CertPCfgType, KEYM_CONST) KeyM_CertPCfg[KEYM_CERT_NUM]



**Sync/Async**
   

**Reentrancy**
   


**Return type**
   


KeyM_CopyData
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void KeyM_CopyData(void *dest, const void *src, uint32 size)

Copies data from the source buffer to the destination buffer.This function performs a byte-wise copy of the specified number of bytes from the source buffer to the destination buffer.

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
     - dest
     - Pointer to the destination buffer.
   * - [in]
     - src
     - Pointer to the source buffer.
   * - [in]
     - size
     - Number of bytes to copy.

**Return type**
   void


KeyM_strcmp
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType KeyM_strcmp(const uint8 *str1, const uint8 *str2, uint16 size)

Compares two strings of a specified length.This function compares the specified number of bytes from two strings.If the strings are identical up to the specified length, it returns E_OK.Otherwise, it returns E_NOT_OK.

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
     - str1
     - Pointer to the first string.
   * - [in]
     - str2
     - Pointer to the second string.
   * - [in]
     - size
     - Number of bytes to compare.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK:The
     - strings are identical up to the specified length.
   * - E_NOT_OK:The
     - strings are not identical up to the specified length.

KeyM_HandleUpdate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType KeyM_HandleUpdate(const uint8 *ResultDataPtr, uint16 ResultDataLength, uint16 KeyIdx, boolean sheKey)

Handles the update of a cryptographic key.This function updates a cryptographic key based on the provided result data.It can store or derive the key according to the configuration.If the key is stored in CSM or RAM, it updates the key directly.If the key is stored in NVM, it writes the key to the specified NVM block.If the key is derived, it performs key derivation using the provided result data and key generation information.

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
     - ResultDataPtr
     - Pointer to the result data used for key update or derivation.
   * - [in]
     - ResultDataLength
     - Length of the result data.
   * - [in]
     - KeyIdx
     - Index of the cryptographic key configuration.
   * - [in]
     - sheKey
     - Flag indicating whether the key is an SHE key.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK:The
     - key update or derivation was successful.
   * - E_NOT_OK:The
     - key update or derivation failed.
   * - KEYM_E_PARAMETER_MISMATCH:Invalid
     - parameters were provided.

KeyM_GetSHEKey_M4M5
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType KeyM_GetSHEKey_M4M5(uint32 keyId, uint8 *ResponseDataPtr, uint16 *ResponseMaxDataLength)

Retrieves the SHE key for M4 and M5 operations.This function retrieves the key element for the specified key ID, which is used for generating M4 and M5 data in the key update process.M4 is generated by encrypting the CID with K3, and M5 is generated by computing the CMAC of M4 using K4, where K4 is derived from the new key.

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
     - keyId
     - ID of the key to retrieve.
   * - [out]
     - ResponseDataPtr
     - Pointer to the buffer where the key element will be stored.
   * - [inout]
     - ResponseMaxDataLength
     - Pointer to the maximum length of the response data buffer. On return, it contains the actual length of the key element.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK:The
     - key element was successfully retrieved.
   * - E_NOT_OK:The
     - key element retrieval failed.

KeyM_HandleParseCert
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType KeyM_HandleParseCert(KeyM_CertificateIdType CertId, const uint8 *certDataPtr, uint32 certDataLength)

Parses a certificate and extracts relevant information.This function processes a certificate according to the X.509 standard.It extracts the TBS (To Be Signed) certificate, version, serial number, signature algorithm, issuer and subject names, validity period, subject public key info, and extensions (if present).It also validates the structure of the certificate and stores the parsed data.

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
     - CertId
     - ID of the certificate to parse.
   * - [in]
     - certDataPtr
     - Pointer to the certificate data.
   * - [in]
     - certDataLength
     - Length of the certificate data.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK:The
     - certificate was successfully parsed.
   * - E_NOT_OK:The
     - certificate parsing failed.
   * - KEYM_E_KEY_CERT_INVALID:The
     - certificate is invalid.
   * - KEYM_E_CERTIFICATE_INVALID_FORMAT:The
     - certificate has an invalid format.

KeyM_HandleCsmKeyStorage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void KeyM_HandleCsmKeyStorage(uint32 keyId, uint16 certId, boolean keySet)

Handles the storage of certificate elements in the CSM.This function processes each certificate element defined in the certificate configuration and either sets or gets the corresponding key element in the CSM.The operation (set or get) is determined by the

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
     - keyId
     - ID of the key in the CSM where the certificate elements will be stored or retrieved.
   * - [in]
     - certId
     - ID of the certificate configuration.
   * - [in]
     - keySet
     - Flag indicating whether to set (TRUE) or get (FALSE) the key elements.

**Return type**
   void


KeyM_HandleCertcVerify
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType KeyM_HandleCertcVerify(const KeyM_CertPCfgType *certCfgPtr, const KeyM_CertPCfgType *certUpperHierRef)

Verifies a certificate against a higher-level certificate in the chain.This function performs a series of checks to validate a certificate

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
     - certCfgPtr
     - Pointer to the certificate configuration of the certificate to verify.
   * - [in]
     - certUpperHierRef
     - Pointer to the certificate configuration of the higher-level certificate.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK:The
     - certificate is valid.
   * - E_NOT_OK:The
     - certificate verification failed.
   * - KEYM_E_CERT_INVALID_CHAIN_OF_TRUST:The
     - certificate chain of trust is invalid.
   * - KEYM_E_CERTIFICATE_VALIDITY_PERIOD_FAIL:The
     - certificate is outside its validity period.
   * - KEYM_E_CERTIFICATE_INVALID_CONTENT:The
     - certificate content is invalid.
   * - KEYM_E_CERTIFICATE_SIGNATURE_FAIL:The
     - certificate signature is invalid.

KeyM_CertSetStatus
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType KeyM_CertSetStatus(KeyM_CertificateIdType CertId, KeyM_CertificateStatusType Status)

Sets the status of a certificate.This function updates the status of a certificate in the certificate status array.It checks if the provided certificate ID is valid before updating the status.

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
     - CertId
     - ID of the certificate to update the status for.
   * - [in]
     - Status
     - New status of the certificate.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK:The
     - status was successfully updated.
   * - KEYM_E_PARAMETER_MISMATCH:The
     - provided certificate ID is invalid.

KeyM_CertStoreNvmHandle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void KeyM_CertStoreNvmHandle(void)

Handles the storage of certificates in NVM with delayed write.This function iterates through the NVM blocks and checks if any block has a delayed write pending.If a block has a delayed write pending, it decrements the delay counter.When the delay counter reaches zero, it writes the certificate data to the NVM block and resets the delay.This ensures that the certificate data is written to NVM after a specified delay, which can be useful for optimizing write operations and reducing wear on the NVM.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant


**Return type**
   void


