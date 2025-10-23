
外部类型定义 Definition of External Types
------------------------------------------------------------

.. list-table:: 
   :widths: 15 5 20
   :header-rows: 1

   * - Type Name
     - Type
     - Description

   * - Csm_ConfigType
     - uint8
     - CSM configuration type.


      
对外提供的服务 Services Provided Externally
------------------------------------------------------------
Csm_Init
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Csm_Init(const Csm_ConfigType *configPtr)

Initializes the CSM module.

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
     - configPtr
     - Pointer to a selected configuration structure

**Return type**
   void


Csm_GetVersionInfo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Csm_GetVersionInfo(Std_VersionInfoType *versioninfo)

Returns the version information of this module.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant.

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


Csm_Hash
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Csm_Hash(uint32 jobId, Crypto_OperationModeType mode, const uint8 *dataPtr, uint32 dataLength, uint8 *resultPtr, uint32 *resultLengthPtr)

Uses the given data to perform the hash calculation and stores the hash.

**Sync/Async**
   TRUE or FALSE, depending on the job configuration

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
     - jobId
     - Holds the identifier of the job using the CSM service.
   * - [in]
     - mode
     - Indicates which operation mode(s) to perfom
   * - [in]
     - dataPtr
     - Contains the pointer to the data for which the hash shall be computed.
   * - [in]
     - dataLength
     - Contains the number of bytes to be hashed.
   * - [out]
     - resultPtr
     - Contains the pointer to the data where the hash value shall be stored.
   * - [inout]
     - resultLengthPtr
     - Holds a pointer to the memory location in which the output length in bytes is stored. On calling this function, this parameter shall contain the size of the buffer provided by resultPtr. When the request has finished, the actual length of the returned value shall be stored.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - request successful E_NOT_OK: request failed CRYPTO_E_BUSY: request failed, service is still busy CRYPTO_E_SMALL_BUFFER: the provided buffer is too small to store the result.

Csm_MacGenerate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Csm_MacGenerate(uint32 jobId, Crypto_OperationModeType mode, const uint8 *dataPtr, uint32 dataLength, uint8 *macPtr, uint32 *macLengthPtr)

Uses the given data to perform a MAC generation and stores the MAC in the memory location pointed to by the MAC pointer.

**Sync/Async**
   Sync or Async, dependend on the job configuration

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
     - jobId
     - Holds the identifier of the job using the CSM service.
   * - [in]
     - mode
     - Indicates which operation mode(s) to perfom
   * - [in]
     - dataPtr
     - Contains the pointer to the data for which the MAC shall be computed.
   * - [in]
     - dataLength
     - Contains the number of bytes to be hashed.
   * - [out]
     - macPtr
     - Contains the pointer to the data where the MAC shall be stored.
   * - [inout]
     - macLengthPtr
     - Holds a pointer to the memory location in which the output length in bytes is stored. On calling this function, this parameter shall contain the size of the buffer provided by macPtr. When the request has finished, the actual length of the returned MAC shall be stored.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - request successful E_NOT_OK: request failed CRYPTO_E_BUSY: request failed, service is still busy CRYPTO_E_KEY_NOT_VALID: request failed, the key's state is "invalid" CRYPTO_E_SMALL_BUFFER: the provided buffer is too small to store the result. CRYPTO_E_KEY_SIZE_MISMATCH: Request failed, a key element has the wrong size CRYPTO_E_KEY_EMPTY: Request failed because of uninitialized source key element

Csm_MacVerify
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Csm_MacVerify(uint32 jobId, Crypto_OperationModeType mode, const uint8 *dataPtr, uint32 dataLength, const uint8 *macPtr, uint32 macLength, Crypto_VerifyResultType *verifyPtr)

Verifies the given MAC by comparing if the MAC is generated with the given data.

**Sync/Async**
   Sync or Async, dependend on the job configuration

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
     - jobId
     - Holds the identifier of the job using the CSM service.
   * - [in]
     - mode
     - Indicates which operation mode(s) to perfom
   * - [in]
     - dataPtr
     - Holds a pointer to the data for which the MAC shall be verified
   * - [in]
     - dataLength
     - Contains the number of data bytes for which the MAC shall be verified.
   * - [in]
     - macPtr
     - Holds a pointer to the MAC to be verified.
   * - [in]
     - macLength
     - Contains the MAC length in BITS to be verified
   * - [out]
     - verifyPtr
     - Holds a pointer to the memory location, which will hold the result of the MAC verification.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - request successful E_NOT_OK: request failed CRYPTO_E_BUSY: request failed, service is still busy CRYPTO_E_SMALL_BUFFER:The provided buffer is too small to store the result. CRYPTO_E_KEY_NOT_VALID: request failed, the key's state is "invalid" CRYPTO_E_KEY_SIZE_MISMATCH: Request failed, a key element has the wrong size CRYPTO_E_KEY_EMPTY: Request failed because of uninitialized source key element

Csm_Encrypt
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Csm_Encrypt(uint32 jobId, Crypto_OperationModeType mode, const uint8 *dataPtr, uint32 dataLength, uint8 *resultPtr, uint32 *resultLengthPtr)

Encrypts the given data and store the ciphertext in the memory location pointed by the result pointer.

**Sync/Async**
   Sync or Async, dependend on the job configuration

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
     - jobId
     - Holds the identifier of the job using the CSM service.
   * - [in]
     - mode
     - Indicates which operation mode(s) to perfom
   * - [in]
     - dataPtr
     - Contains the pointer to the data to be encrypted.
   * - [in]
     - dataLength
     - Contains the number of bytes to encrypt.
   * - [out]
     - resultPtr
     - Contains the pointer to the data where the encrypted data shall be stored.
   * - [inout]
     - resultLengthPtr
     - Holds a pointer to the memory location in which the output length information is stored in bytes. On calling this function, this parameter shall contain the size of the buffer provided by resultPtr. When the request has finished, the actual length of the returned value shall be stored.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - request successful E_NOT_OK: request failed CRYPTO_E_BUSY: request failed, service is still busy CRYPTO_E_KEY_NOT_VALID: request failed, the key's state is "invalid" CRYPTO_E_SMALL_BUFFER: the provided buffer is too small to store the result. CRYPTO_E_KEY_SIZE_MISMATCH: Request failed, a key element has the wrong size CRYPTO_E_KEY_EMPTY:Request failed because of uninitialized source key element

Csm_Decrypt
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Csm_Decrypt(uint32 jobId, Crypto_OperationModeType mode, const uint8 *dataPtr, uint32 dataLength, uint8 *resultPtr, uint32 *resultLengthPtr)

Decrypts the given encrypted data and store the decrypted plaintext in the memory location pointed by the result pointer.

**Sync/Async**
   Sync or Async, dependend on the job configuration

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
     - jobId
     - Holds the identifier of the job using the CSM service.
   * - [in]
     - mode
     - Indicates which operation mode(s) to perfom
   * - [in]
     - dataPtr
     - Contains the pointer to the data to be decrypted.
   * - [in]
     - dataLength
     - Contains the number of bytes to decrypt.
   * - [out]
     - resultPtr
     - Contains the pointer to the data where the decrypted data shall be stored.
   * - [inout]
     - resultLengthPtr
     - Holds a pointer to the memory location in which the output length information is stored in bytes. On calling this function, this parameter shall contain the size of the buffer provided by resultPtr. When the request has finished, the actual length of the returned value shall be stored.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - request successful E_NOT_OK: request failed CRYPTO_E_BUSY: request failed, service is still busy CRYPTO_E_KEY_NOT_VALID: request failed, the key's state is "invalid" CRYPTO_E_SMALL_BUFFER: the provided buffer is too small to store the result. CRYPTO_E_KEY_SIZE_MISMATCH: Request failed, a key element has the wrong size CRYPTO_E_KEY_EMPTY:Request failed because of uninitialized source key element

Csm_AEADEncrypt
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Csm_AEADEncrypt(uint32 jobId, Crypto_OperationModeType mode, const uint8 *plaintextPtr, uint32 plaintextLength, const uint8 *associatedDataPtr, uint32 associatedDataLength, uint8 *ciphertextPtr, uint32 *ciphertextLengthPtr, uint8 *tagPtr, uint32 *tagLengthPtr)

Uses the given input data to perform a AEAD encryption and stores the ciphertext and the MAC in the memory locations pointed by the ciphertext.

**Sync/Async**
   Sync or Async, dependend on the job configuration

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
     - jobId
     - Holds the identifier of the job using the CSM service.
   * - [in]
     - mode
     - Indicates which operation mode(s) to perfom
   * - [in]
     - plaintextPtr
     - Contains the pointer to the data to be encrypted.
   * - [in]
     - plaintextLength
     - Contains the number of bytes to encrypt
   * - [in]
     - associatedDataPtr
     - Contains the pointer to the associated data.
   * - [in]
     - associatedDataLength
     - Contains the number of bytes of the associated data
   * - [out]
     - ciphertextPtr
     - Contains the pointer to the data where the encrypted data shall be stored.
   * - [inout]
     - ciphertextLengthPtr
     - Holds a pointer to the memory location in which the output length information is stored in bytes. On calling this function, this parameter shall contain the size of the buffer provided by ciphertextPtr.When the request has finished, the actual length of the returned value shall be stored.
   * - [out]
     - tagPtr
     - Contains the pointer to the data where the Tag shall be stored.
   * - [inout]
     - tagLengthPtr
     - Holds a pointer to the memory location in which the output length information is stored in bytes. On calling this function, this parameter shall contain the size of the buffer provided by tagPtr. When the request has finished, the actual length of the returned value shall be stored.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - request successful E_NOT_OK: request failed CRYPTO_E_BUSY: request failed, service is still busy CRYPTO_E_SMALL_BUFFER: The provided buffer is too small to store the result CRYPTO_E_KEY_NOT_VALID: request failed, the key's state is "invalid" CRYPTO_E_KEY_SIZE_MISMATCH: Request failed, a key element has the wrong size CRYPTO_E_KEY_EMPTY: Request failed because of uninitialized source key element

Csm_AEADDecrypt
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Csm_AEADDecrypt(uint32 jobId, Crypto_OperationModeType mode, const uint8 *ciphertextPtr, uint32 ciphertextLength, const uint8 *associatedDataPtr, uint32 associatedDataLength, const uint8 *tagPtr, uint32 tagLength, uint8 *plaintextPtr, uint32 *plaintextLengthPtr, Crypto_VerifyResultType *verifyPtr)

Uses the given data to perform an AEAD Decryption and stores the ciphertext and the MAC in the memory locations pointed by the ciphertext pointer and.

**Sync/Async**
   Sync or Async, dependend on the job configuration

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
     - jobId
     - Holds the identifier of the job using the CSM service.
   * - [in]
     - mode
     - Indicates which operation mode(s) to perfom
   * - [in]
     - ciphertextPtr
     - Contains the pointer to the data to be decrypted..
   * - [in]
     - ciphertextLength
     - Contains the number of bytes to decrypt.
   * - [in]
     - associatedDataPtr
     - Contains the pointer to the associated data.
   * - [in]
     - associatedDataLength
     - Contains the length in bytes of the associated data
   * - [in]
     - tagPtr
     - Contains the pointer to the Tag to be verified.
   * - [in]
     - tagLength
     - Contains the length in bytes of the Tag to be verified.
   * - [out]
     - plaintextPtr
     - Contains the pointer to the data where the decrypted data shall be stored.
   * - [inout]
     - plaintextLengthPtr
     - Holds a pointer to the memory location in which the output length information is stored in bytes. On calling this function, this parameter shall contain the size of the buffer provided by plaintextPtr. When the request has finished, the actual length of the returned value shall be stored.
   * - [out]
     - verifyPtr
     - Contains the pointer to the result of the verification.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - request successful E_NOT_OK: request failed CRYPTO_E_BUSY: request failed, service is still busy CRYPTO_E_SMALL_BUFFER: The provided buffer is too small to store the result CRYPTO_E_KEY_NOT_VALID: request failed, the key's state is "invalid" CRYPTO_E_KEY_SIZE_MISMATCH: Request failed, a key element has the wrong size CRYPTO_E_KEY_EMPTY: Request failed because of uninitialized source key element

Csm_SignatureGenerate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Csm_SignatureGenerate(uint32 jobId, Crypto_OperationModeType mode, const uint8 *dataPtr, uint32 dataLength, uint8 *resultPtr, uint32 *resultLengthPtr)

Uses the given data to perform the signature calculation and stores the signature in the memory location pointed by the result pointer.

**Sync/Async**
   Sync or Async, dependend on the job configuration

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
     - jobId
     - Holds the identifier of the job using the CSM service.
   * - [in]
     - mode
     - Indicates which operation mode(s) to perfom
   * - [in]
     - dataPtr
     - Contains the pointer to the data to be signed...
   * - [in]
     - dataLength
     - Contains the number of bytes to sign.
   * - [out]
     - resultPtr
     - Contains the pointer to the data where the signature shall be stored.
   * - [inout]
     - resultLengthPtr
     - Holds a pointer to the memory location in which the output length information is stored in bytes. On calling this function, this parameter shall contain the size of the buffer provided by resultPtr. When the request has finished, the actual length of the returned value shall be stored.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - request successful E_NOT_OK: request failed CRYPTO_E_BUSY: request failed, service is still busy CRYPTO_E_KEY_NOT_VALID: request failed, the key's state is "invalid" CRYPTO_E_SMALL_BUFFER: the provided buffer is too small to store the result. CRYPTO_E_KEY_SIZE_MISMATCH: Request failed, a key element has the wrong size CRYPTO_E_KEY_EMPTY: Request failed because of uninitialized source key element

Csm_SignatureVerify
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Csm_SignatureVerify(uint32 jobId, Crypto_OperationModeType mode, const uint8 *dataPtr, uint32 dataLength, const uint8 *signaturePtr, uint32 signatureLength, Crypto_VerifyResultType *verifyPtr)

Verifies the given MAC by comparing if the signature is generated with the given data.

**Sync/Async**
   Sync or Async, dependend on the job configuration

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
     - jobId
     - Holds the identifier of the job using the CSM service.
   * - [in]
     - mode
     - Indicates which operation mode(s) to perfom
   * - [in]
     - dataPtr
     - Contains the pointer to the data to be verified.
   * - [in]
     - dataLength
     - Contains the number of data bytes.
   * - [in]
     - signaturePtr
     - Holds a pointer to the signature to be verified
   * - [in]
     - signatureLength
     - Contains the signature length in bytes.
   * - [out]
     - verifyPtr
     - Holds a pointer to the memory location, which will hold the result of the signature verification.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - request successful E_NOT_OK: request failed CRYPTO_E_BUSY: request failed, service is still busy CRYPTO_E_SMALL_BUFFER: the provided buffer is too small to store the result. CRYPTO_E_KEY_NOT_VALID: request failed, the key's state is "invalid" CRYPTO_E_KEY_SIZE_MISMATCH: Request failed, a key element has the wrong size CRYPTO_E_KEY_EMPTY: Request failed because of uninitialized source key element

Csm_RandomGenerate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Csm_RandomGenerate(uint32 jobId, Crypto_OperationModeType mode, uint8* resultPtr, uint32* resultLengthPtr)

Generate a random number and stores it in the memory location pointed by the result pointer.

**Sync/Async**
   Sync or Async, dependend on the job configuration

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
     - jobId
     - Holds the identifier of the job using the CSM service.
   * - [out]
     - resultPtr
     - Holds a pointer to the memory location which will hold the result of the random number generation.
   * - [inout]
     - resultLengthPtr
     - Holds a pointer to the memory location in which the result length in bytes is stored. On calling this function, this parameter shall contain the number of random bytes, which shall be stored to the buffer provided by resultPtr. When the request has finished, the actual length of the returned value shall be stored.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - request successful E_NOT_OK: request failed CRYPTO_E_BUSY: request failed, service is still busy CRYPTO_E_ENTROPY_EXHAUSTED: request failed, entropy of random number generator is exhausted.

Csm_KeyElementSet
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Csm_KeyElementSet(uint32 keyId, uint32 keyElementId, const uint8 *keyPtr, uint32 keyLength)

Sets the given key element bytes to the key identified by keyId.

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
     - keyId
     - Holds the identifier of the key for which a new material shall be set.
   * - [in]
     - keyElementId
     - Holds the identifier of the key element to be written.
   * - [in]
     - keyPtr
     - Holds the pointer to the key element bytes to be processed.
   * - [in]
     - keyLength
     - Contains the number of key element bytes.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - request successful E_NOT_OK: request failed CRYPTO_E_BUSY: request failed, service is still busy CRYPTO_E_KEY_WRITE_FAIL:Request failed because write access was denied CRYPTO_E_KEY_NOT_AVAILABLE: Request failed because the key is not available. CRYPTO_E_KEY_SIZE_MISMATCH: Request failed, key element size does not match size of provided data.

Csm_KeySetValid
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Csm_KeySetValid(uint32 keyId)

Sets the key state of the key identified by keyId to valid.

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
     - keyId
     - Holds the identifier of the key for which a new material shall be validated.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - request successful E_NOT_OK: request failed CRYPTO_E_BUSY: request failed, service is still busy

Csm_KeySetInvalid
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Csm_KeySetInvalid(uint32 keyId)

Sets the key state of the key identified by keyId to invalid.

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
     - keyId
     - Holds the identifier of the key for which a new material shall be invalidated.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - request successful E_NOT_OK: request failed CRYPTO_E_BUSY: request failed, service is still busy

Csm_KeyElementGet
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Csm_KeyElementGet(uint32 keyId, uint32 keyElementId, uint8 *keyPtr, uint32 *keyLengthPtr)

Retrieves the key element bytes from a specific key element of the key identified by the keyId and stores the key element in the memory location pointed by the key pointer.

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
     - Holds the identifier of the key from which a key element shall be extracted.
   * - [in]
     - keyElementId
     - Holds the identifier of the key element to be extracted
   * - [out]
     - keyPtr
     - Holds the pointer to the memory location where the key shall be copied to.
   * - [inout]
     - keyLengthPtr
     - Holds a pointer to the memory location in which the output buffer length in bytes is stored. On calling this function, this parameter shall contain the buffer length in bytes of the keyPtr. When the request has finished, the actual size of the written input bytes shall be stored.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - request successful E_NOT_OK: request failed CRYPTO_E_BUSY: request failed, service is still busy CRYPTO_E_KEY_NOT_AVAILABLE: request failed, the requested key element is not available CRYPTO_E_KEY_READ_FAIL: Request failed because read access was denied CRYPTO_E_SMALL_BUFFER: the provided buffer is too small to store the result. CRYPTO_E_KEY_EMPTY:Request failed because of uninitialized source key element

Csm_KeyElementCopy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Csm_KeyElementCopy(const uint32 keyId, const uint32 keyElementId, const uint32 targetKeyId, const uint32 targetKeyElementId)

This function shall copy a key elements from one key to a target key.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant, but not for the same keyId

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - keyId
     - Holds the identifier of the key whose key element shall be the source element.
   * - [in]
     - keyElementId
     - Holds the identifier of the key element which shall be the source for the copy operation.
   * - [in]
     - targetKeyId
     - Holds the identifier of the key whose key element shall be the destination element.
   * - [in]
     - targetKeyElementId
     - Holds the identifier of the key element which shall be the destination for the copy operation. Parameters(INOUT): NA Parameters(OUT): NA Return value: E_OK: request successful E_NOT_OK: request failed CRYPTO_E_BUSY: request failed, service is still busy CRYPTO_E_KEY_NOT_AVAILABLE: request failed, the requested key element is not available CRYPTO_E_KEY_READ_FAIL: Request failed because read access was denied CRYPTO_E_KEY_WRITE_FAIL: Request failed, not allowed to write key element. CRYPTO_E_KEY_SIZE_MISMATCH: Request failed, key element sizes are not compatible. CRYPTO_E_KEY_EMPTY:Request failed because of uninitialized source key element.

**Return type**
   Std_ReturnType


Csm_KeyCopy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Csm_KeyCopy(const uint32 keyId, const uint32 targetKeyId)

This function shall copy all key elements from the source key to a target key.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant, but not for the same keyId

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - keyId
     - Holds the identifier of the key whose key element shall be the source element.
   * - [in]
     - targetKeyId
     - Holds the identifier of the key whose key element shall be the destination element.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - request successful E_NOT_OK: request failed CRYPTO_E_BUSY: request failed, service is still busy CRYPTO_E_KEY_NOT_AVAILABLE: request failed, the requested key element is not available CRYPTO_E_KEY_READ_FAIL: Request failed because read access was denied CRYPTO_E_KEY_WRITE_FAIL: Request failed, not allowed to write key element. CRYPTO_E_KEY_SIZE_MISMATCH: Request failed, key element sizes are not compatible. CRYPTO_E_KEY_EMPTY:Request failed because of uninitialized source key element.

Csm_KeyElementCopyPartial
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Csm_KeyElementCopyPartial(uint32 keyId, uint32 keyElementId, uint32 keyElementSourceOffset, uint32 keyElementTargetOffset, uint32 keyElementCopyLength, uint32 targetKeyId, uint32 targetKeyElementId)

Copies a key element to another key element in the same crypto driver. The keyElementSourceOffset and keyElementCopyLength allows to copy just a part of the source key element into the destination. The offset into the target key is also specified with this function.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant, but not for the same keyId

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - keyId
     - Holds the identifier of the key whose key element shall be the source element for copy operation.
   * - [in]
     - keyElementId
     - Holds the identifier of the key element which shall be the source for the copy operation..
   * - [in]
     - keyElementSourceOffset
     - This is the offset of the source key element indicating the start index of the copy operation..
   * - [in]
     - keyElementTargetOffset
     - This is the offset of the destination key element indicating the start index of the copy operation.
   * - [in]
     - keyElementCopyLength
     - Specifies the number of bytes that shall be copied.
   * - [in]
     - targetKeyId
     - target Key Id.
   * - [in]
     - targetKeyElementId
     - Holds the identifier of the key element which shall be the destination for the copy operation.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - request successful E_NOT_OK: request failed CRYPTO_E_BUSY: request failed, service is still busy CRYPTO_E_KEY_NOT_AVAILABLE: request failed, the requested key element is not available CRYPTO_E_KEY_READ_FAIL: Request failed because read access was denied CRYPTO_E_KEY_WRITE_FAIL: Request failed, not allowed to write key element. CRYPTO_E_KEY_SIZE_MISMATCH: Request failed, key element sizes are not compatible. CRYPTO_E_KEY_EMPTY:Request failed because of uninitialized source key element.

Csm_RandomSeed
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Csm_RandomSeed(uint32 keyId, const uint8 *seedPtr, uint32 seedLength)

Feeds the key element CRYPTO_KE_RANDOM_SEED with a random seed.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant, but not for the same keyId

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - keyId
     - Holds the identifier of the key for which a new seed shall be generated.
   * - [in]
     - seedPtr
     - Holds a pointer to the memory location which contains the data to feed the seed.
   * - [in]
     - seedLength
     - Contains the length of the seed in bytes.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - request successful E_NOT_OK: request failed CRYPTO_E_BUSY: Request failed, service is still busy CRYPTO_E_KEY_NOT_VALID: Request failed, the key's state is "invalid".

Csm_KeyGenerate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Csm_KeyGenerate(uint32 keyId)

Generates new key material and store it in the key identified by keyId.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant, but not for the same keyId

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - keyId
     - Holds the identifier of the key for which a new material shall be generated.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - request successful E_NOT_OK: request failed CRYPTO_E_BUSY: Request failed, service is still busy CRYPTO_E_KEY_NOT_VALID: Request failed, the key's state is "invalid". CRYPTO_E_KEY_EMPTY: Request failed because of uninitialized source key element

Csm_KeyDerive
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Csm_KeyDerive(uint32 keyId, uint32 targetKeyId)

Derives a new key by using the key elements in the given key identified by the keyId. The given key contains the key elements for the password and salt. The derived key is stored in the key element with the id 1 of the key identified by targetCryptoKeyId.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant, but not for the same keyId

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - keyId
     - Holds the identifier of the key which is used for key derivation.
   * - [in]
     - targetKeyId
     - Holds the identifier of the key which is used to store the derived key.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - request successful E_NOT_OK: request failed CRYPTO_E_BUSY: request failed, service is still busy CRYPTO_E_KEY_READ_FAIL: Request failed because read access was denied CRYPTO_E_KEY_WRITE_FAIL: Request failed, not allowed to write key element. CRYPTO_E_KEY_NOT_VALID: Request failed, the key's state is "invalid". CRYPTO_E_KEY_SIZE_MISMATCH: Request failed, key element sizes are not compatible. CRYPTO_E_KEY_EMPTY:Request failed because of uninitialized source key element.

Csm_KeyExchangeCalcPubVal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Csm_KeyExchangeCalcPubVal(uint32 keyId, uint8 *publicValuePtr, uint32 *publicValueLengthPtr)

Calculates the public value of the current user for the key exchange and stores the public key in the memory location pointed by the public value pointer.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant, but not for the same keyId

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - keyId
     - Holds the identifier of the key which shall be used for the key exchange protocol.
   * - [out]
     - publicValuePtr
     - Contains the pointer to the data where the public value shall be stored.
   * - [inout]
     - publicValueLengthPtr
     - Holds a pointer to the memory location in which the public value length information is stored. On calling this function, this parameter shall contain the size of the buffer provided by publicValuePtr. When the request has finished, the actual length of the returned value shall be stored.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - request successful E_NOT_OK: request failed CRYPTO_E_BUSY: request failed, service is still busy CRYPTO_E_SMALL_BUFFER: The provided buffer is too small to store the result CRYPTO_E_KEY_NOT_VALID: Request failed, the key's state is "invalid". CRYPTO_E_KEY_EMPTY:Request failed because of uninitialized source key element.

Csm_KeyExchangeCalcSecret
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Csm_KeyExchangeCalcSecret(uint32 keyId, const uint8 *partnerPublicValuePtr, uint32 partnerPublicValueLength)

Calculates the shared secret key for the key exchange with the key material of the key identified by the keyId and the partner public key. The shared secret key is stored as a key element in the same key.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant, but not for the same keyId

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - keyId
     - Holds the identifier of the key which shall be used for the key exchange protocol.
   * - [in]
     - partnerPublicValuePtr
     - Holds the pointer to the memory location which contains the partner's public value.
   * - [in]
     - partnerPublicValueLength
     - Contains the length of the partner's public value in bytes.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - request successful E_NOT_OK: request failed CRYPTO_E_BUSY: request failed, service is still busy CRYPTO_E_SMALL_BUFFER: The provided buffer is too small to store the result CRYPTO_E_KEY_NOT_VALID: Request failed, the key's state is "invalid". CRYPTO_E_KEY_EMPTY:Request failed because of uninitialized source key element.

Csm_JobKeySetValid
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Csm_JobKeySetValid(uint32 jobId)

Stores the key if necessary and sets the key state of the key identified by keyId to valid.

**Sync/Async**
   TRUE or FALSE, depending on the job configuration

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
     - jobId
     - Holds the identifier of the key for which a new material shall be validated.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - request successful E_NOT_OK: request failed CRYPTO_E_BUSY: Request failed, service is still busy

Csm_JobKeySetInValid
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Csm_JobKeySetInValid(uint32 jobId)

Stores the key if necessary and sets the key state of the key identified by keyId to invalid.

**Sync/Async**
   TRUE or FALSE, depending on the job configuration

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
     - jobId
     - Holds the identifier of the key for which a new material shall be invalidated.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - request successful E_NOT_OK: request failed CRYPTO_E_BUSY: Request failed, service is still busy

Csm_JobRandomSeed
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Csm_JobRandomSeed(uint32 jobId, uint32 keyId, const uint8 *seedPtr, uint32 seedLength)

This function shall dispatch the random seed function to the configured crypto driver object.

**Sync/Async**
   TRUE or FALSE, depending on the job configuration

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
     - jobId
     - Holds the identifier of the job using the CSM service.
   * - [in]
     - keyId
     - Holds the identifier of the key for which a new seed shall be generated.
   * - [in]
     - seedPtr
     - Holds a pointer to the memory location which contains the data to feed the seed..
   * - [in]
     - seedLength
     - Contains the length of the seed in bytes.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - request successful E_NOT_OK: request failed CRYPTO_E_BUSY: Request failed, service is still busy CRYPTO_E_KEY_NOT_VALID: Request failed, the key's state is "invalid"

Csm_JobKeyGenerate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Csm_JobKeyGenerate(uint32 jobId, uint32 keyId)

Generates new key material and stores it in the key identified by keyId.

**Sync/Async**
   TRUE or FALSE, depending on the job configuration

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
     - jobId
     - Holds the identifier of the job using the CSM service.
   * - [in]
     - keyId
     - Holds the identifier of the key for which a new material shall be generated.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - request successful E_NOT_OK: request failed CRYPTO_E_BUSY: Request failed, service is still busy CRYPTO_E_KEY_NOT_VALID: Request failed, the key's state is "invalid" CRYPTO_E_KEY_EMPTY: Request failed because of uninitialized source key element

Csm_JobKeyDerive
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Csm_JobKeyDerive(uint32 jobId, uint32 keyId, uint32 targetKeyId)

Derives a new key by using the key elements in the given key identified by the keyId. The given key contains the key elements for the password and salt. The derived key is stored in the key element with the id 1 of the key identified by targetCryptoKeyId.

**Sync/Async**
   TRUE or FALSE, depending on the job configuration

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
     - jobId
     - Holds the identifier of the job using the CSM service.
   * - [in]
     - keyId
     - Holds the identifier of the key which is used for key derivation.
   * - [in]
     - targetKeyId
     - Holds the identifier of the key which is used to store the derived key.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - request successful E_NOT_OK: request failed CRYPTO_E_BUSY: Request failed, service is still busy CRYPTO_E_KEY_READ_FAIL: Request failed, not allowed to extract key element CRYPTO_E_KEY_WRITE_FAIL: Request failed, not allowed to write key element CRYPTO_E_KEY_NOT_VALID: Request failed, the key's state is "invalid" CRYPTO_E_KEY_SIZE_MISMATCH: Request failed, key element sizes are not compatible CRYPTO_E_KEY_EMPTY: Request failed because of uninitialized source key element

Csm_JobKeyExchangeCalcPubVal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Csm_JobKeyExchangeCalcPubVal(uint32 jobId, uint32 keyId, uint8 *publicValuePtr, uint32 *publicValueLengthPtr)

Calculates the public value of the current user for the key exchange and stores the public key in the memory location pointed by the public value pointer.

**Sync/Async**
   TRUE or FALSE, depending on the job configuration

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
     - jobId
     - Holds the identifier of the job using the CSM service.
   * - [in]
     - keyId
     - Holds the identifier of the key which shall be used for the key exchange protocol.
   * - [in]
     - publicValuePtr
     - Contains the pointer to the data where the public value shall be stored.
   * - [out]
     - publicValueLengthPtr
     - Holds a pointer to the memory location in which the public value length information is stored.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - request successful E_NOT_OK: request failed CRYPTO_E_BUSY: Request failed, service is still busy CRYPTO_E_SMALL_BUFFER: The provided buffer is too small to store the result CRYPTO_E_KEY_NOT_VALID: Request failed, the key's state is "invalid" CRYPTO_E_KEY_EMPTY: Request failed because of uninitialized source key element

Csm_JobKeyExchangeCalcSecret
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Csm_JobKeyExchangeCalcSecret(uint32 jobId, uint32 keyId, const uint8 *partnerPublicValuePtr, uint32 partnerPublicValueLength)

Calculates the shared secret key for the key exchange with the key material of the key identified by the keyId and the partner public key. The shared secret key is stored as a key element in the same key.

**Sync/Async**
   TRUE or FALSE, depending on the job configuration

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
     - jobId
     - Holds the identifier of the job using the CSM service.
   * - [in]
     - keyId
     - Holds the identifier of the key which shall be used for the key exchange protocol.
   * - [in]
     - partnerPublicValuePtr
     - Holds the pointer to the memory location which contains the partner's public value.
   * - [in]
     - partnerPublicValueLength
     - Contains the length of the partner's public value in bytes.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - request successful E_NOT_OK: request failed E_BUSY:Request failed, Crypto Driver Object is busy CRYPTO_E_SMALL_BUFFER: The provided buffer is too small to store the result CRYPTO_E_BUSY: Request failed, service is still busy CRYPTO_E_KEY_NOT_VALID: Request failed, the key's state is "invalid". CRYPTO_E_KEY_EMPTY:Request failed because of uninitialized source key element.

Csm_CancelJob
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Csm_CancelJob(uint32 job, Crypto_OperationModeType mode)

Cancels the job processing from asynchronous or streaming jobs.

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
     - job
     - Holds the identifier of the job to be canceled
   * - [in]
     - mode
     - Not used, just for interface compatibility provided.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request successful. Job removed from any queue and potentially from crypto driver hardware. E_NOT_OK: Request failed CRYPTO_E_JOB_CANCELED: Immediate cancelation not possible.The cancelation will be done at next suitable processing step and notified via a negative finish callback.

Csm_KeyGetStatus
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Csm_KeyGetStatus(uint32 keyId, Crypto_KeyStatusType *keyStatusPtr)

Retrieves the status of a key in the CSM module.

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
     - keyId
     - Identifier of the key.
   * - [out]
     - keyStatusPtr
     - Pointer to the variable where the key status will be stored.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Operation successful.
   * - E_NOT_OK
     - Operation failed.

Csm_CustomService
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Csm_CustomService(uint32 jobId, Crypto_OperationModeType mode, uint32 targetKeyId, const uint8 *inputPtr, uint32 inputLength, const uint8 *secondaryInputPtr, uint32 secondaryInputLength, const uint8 *tertiaryInputPtr, uint32 tertiaryInputLength, uint8 *outputPtr, uint32 *outputLengthPtr, uint8 *secondaryOutputPtr, uint32 *secondaryOutputLengthPtr, Crypto_VerifyResultType *verifyPtr)

Custom service operation for the CSM module.

**Sync/Async**
   Depends on configuration

**Reentrancy**
   Reentrant for different jobId

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - jobId
     - Identifier of the job.
   * - [in]
     - mode
     - Operation mode (e.g., encryption, decryption, signing, verification).
   * - [in]
     - targetKeyId
     - Identifier of the target key.
   * - [in]
     - inputPtr
     - Pointer to the primary input data.
   * - [in]
     - inputLength
     - Length of the primary input data.
   * - [in]
     - secondaryInputPtr
     - Pointer to the secondary input data.
   * - [in]
     - secondaryInputLength
     - Length of the secondary input data.
   * - [in]
     - tertiaryInputPtr
     - Pointer to the tertiary input data.
   * - [in]
     - tertiaryInputLength
     - Length of the tertiary input data.
   * - [out]
     - outputPtr
     - Pointer to the output data.
   * - [out]
     - outputLengthPtr
     - Pointer to the length of the output data.
   * - [out]
     - secondaryOutputPtr
     - Pointer to the secondary output data.
   * - [out]
     - secondaryOutputLengthPtr
     - Pointer to the length of the secondary output data.
   * - [out]
     - verifyPtr
     - Pointer to the verification result.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Operation successful.
   * - E_NOT_OK
     - Operation failed.

Csm_CustomSync
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Csm_CustomSync(uint32 dispatchId, uint32 keyId, uint32 keyElementId, uint32 targetKeyId, uint32 targetKeyElementId, const uint8 *inputPtr, uint32 inputLength, uint8 *outputPtr, uint32 *outputLengthPtr, uint8 *secondaryOutputPtr, uint32 *secondaryOutputLengthPtr)

Custom synchronous operation for the CSM module.

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
     - dispatchId
     - Dispatch ID for the operation.
   * - [in]
     - keyId
     - Identifier of the source key.
   * - [in]
     - keyElementId
     - Identifier of the source key element.
   * - [in]
     - targetKeyId
     - Identifier of the target key.
   * - [in]
     - targetKeyElementId
     - Identifier of the target key element.
   * - [in]
     - inputPtr
     - Pointer to the input data.
   * - [in]
     - inputLength
     - Length of the input data.
   * - [out]
     - outputPtr
     - Pointer to the output data.
   * - [out]
     - outputLengthPtr
     - Pointer to the length of the output data.
   * - [out]
     - secondaryOutputPtr
     - Pointer to the secondary output data.
   * - [out]
     - secondaryOutputLengthPtr
     - Pointer to the length of the secondary output data.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Operation successful.
   * - E_NOT_OK
     - Operation failed.

Csm_SaveContextJob
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Csm_SaveContextJob(uint32 jobId, uint8 *contextBufferPtr, uint32 *contextBufferLengthPtr)

Saves the context of a job in the CSM module.

**Sync/Async**
   Depends on configuration

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
     - jobId
     - Identifier of the job.
   * - [out]
     - contextBufferPtr
     - Pointer to the buffer where the context data will be stored.
   * - [out]
     - contextBufferLengthPtr
     - Pointer to the variable where the length of the context data will be stored.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Operation successful.
   * - E_NOT_OK
     - Operation failed.

Csm_RestoreContextJob
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Csm_RestoreContextJob(uint32 jobId, const uint8 *contextBufferPtr, uint32 contextBufferLength)

Restores the context of a job in the CSM module.

**Sync/Async**
   Depends on configuration

**Reentrancy**
   Reentrant This function restores the context of a specified job in the CSM module. It takes the job ID, a pointer to the context buffer, and the length of the context buffer. The function reads the context data from the provided buffer and restores it for the job.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - jobId
     - Identifier of the job.
   * - [in]
     - contextBufferPtr
     - Pointer to the buffer containing the context data.
   * - [in]
     - contextBufferLength
     - Length of the context data in the buffer.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Operation successful.
   * - E_NOT_OK
     - Operation failed.

