
外部类型定义 Definition of External Types
------------------------------------------------------------------------------------------------------------------------

.. list-table:: 
   :widths: 15 5 20
   :header-rows: 1

   * - Type Name
     - Type
     - Description

   * - Crypto_62_ConfigType
     - uint8
     - Configuration type.


      
提供外部的服务 External Services Provided
------------------------------------------------------------------------------------------------------------------------
Crypto_62_Init
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Crypto_62_Init(const Crypto_62_ConfigType *configPtr)

Initializes the Crypto_62 module.

**Sync/Async**
   TRUE

**Reentrancy**
   Not reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - configPtr
     - Pointer to the Crypto_62 configuration structure.

**Return type**
   void


Crypto_62_GetVersionInfo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Crypto_62_GetVersionInfo(Std_VersionInfoType *versioninfo)

Retrieves the version information of the Crypto_62 module.

**Sync/Async**
   TRUE

**Reentrancy**
   Not reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [out]
     - versioninfo
     - Pointer to the version information structure.

**Return type**
   void


Crypto_62_ProcessJob
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Crypto_62_ProcessJob(uint32 objectId, Crypto_JobType *job)

Processes a cryptographic job.

**Sync/Async**
   TRUE

**Reentrancy**
   Not reentrant for the same object ID

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - objectId
     - The ID of the cryptographic object.
   * - [in]
     - job
     - Pointer to the cryptographic job structure.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The job was processed successfully.
   * - E_NOT_OK
     - The job could not be processed due to an error.
   * - CRYPTO_E_BUSY
     - The cryptographic object is busy.
   * - CRYPTO_E_PARAM_HANDLE
     - The job's service or key ID is invalid.
   * - CRYPTO_E_PARAM_POINTER
     - The job pointer is NULL.
   * - CRYPTO_E_UNINIT
     - The Crypto_62 module is not initialized.

Crypto_62_CancelJob
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Crypto_62_CancelJob(uint32 objectId, Crypto_JobType *job)

Cancels a cryptographic job.

**Sync/Async**
   TRUE

**Reentrancy**
   Not reentrant for the same object ID

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - objectId
     - The ID of the cryptographic object.
   * - [in]
     - job
     - Pointer to the cryptographic job structure.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The job was canceled successfully.
   * - E_NOT_OK
     - The job could not be canceled due to an error.
   * - CRYPTO_E_JOB_CANCELED
     - The job was canceled and the callback was notified.
   * - CRYPTO_E_PARAM_HANDLE
     - The object ID is invalid.
   * - CRYPTO_E_PARAM_POINTER
     - The job pointer is NULL.
   * - CRYPTO_E_UNINIT
     - The Crypto_62 module is not initialized.

Crypto_62_KeyElementSet
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Crypto_62_KeyElementSet(uint32 cryptokeyId, uint32 keyElementId, const uint8 *keyPtr, uint32 keyLength)

Sets a key element for a cryptographic key.

**Sync/Async**
   TRUE

**Reentrancy**
   Not reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - cryptokeyId
     - The ID of the cryptographic key.
   * - [in]
     - keyElementId
     - The ID of the key element to set.
   * - [in]
     - keyPtr
     - Pointer to the key data.
   * - [in]
     - keyLength
     - The length of the key data.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The key element was set successfully.
   * - E_NOT_OK
     - The key element could not be set due to an error.
   * - CRYPTO_E_PARAM_HANDLE
     - The cryptographic key ID is invalid.
   * - CRYPTO_E_PARAM_POINTER
     - The key pointer is NULL.
   * - CRYPTO_E_PARAM_VALUE
     - The key length is zero.
   * - CRYPTO_E_UNINIT
     - The Crypto_62 module is not initialized.

Crypto_62_KeySetValid
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Crypto_62_KeySetValid(uint32 cryptoKeyId)

Sets a cryptographic key to a valid state.

**Sync/Async**
   TRUE

**Reentrancy**
   Not reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - cryptoKeyId
     - The ID of the cryptographic key.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The key was set to a valid state successfully.
   * - E_NOT_OK
     - The key could not be set to a valid state due to an error.
   * - CRYPTO_E_PARAM_HANDLE
     - The cryptographic key ID is invalid.
   * - CRYPTO_E_UNINIT
     - The Crypto_62 module is not initialized.
   * - CRYPTO_E_RE_NVM_ACCESS_FAILED
     - Access to the NVM block failed.

Crypto_62_KeySetInValid
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Crypto_62_KeySetInValid(uint32 cryptoKeyId)

Sets a cryptographic key to an invalid state.

**Sync/Async**
   TRUE

**Reentrancy**
   Not reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - cryptoKeyId
     - The ID of the cryptographic key.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The key was set to an invalid state successfully.
   * - E_NOT_OK
     - The key could not be set to an invalid state due to an error.
   * - CRYPTO_E_PARAM_HANDLE
     - The cryptographic key ID is invalid.
   * - CRYPTO_E_UNINIT
     - The Crypto_62 module is not initialized.

Crypto_62_KeyElementGet
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Crypto_62_KeyElementGet(uint32 cryptoKeyId, uint32 keyElementId, uint8 *resultPtr, uint32 *resultLengthPtr)

Retrieves a key element from a cryptographic key.

**Sync/Async**
   TRUE

**Reentrancy**
   Not reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - cryptoKeyId
     - The ID of the cryptographic key.
   * - [in]
     - keyElementId
     - The ID of the key element to retrieve.
   * - [out]
     - resultPtr
     - Pointer to the buffer where the key element will be stored.
   * - [inout]
     - resultLengthPtr
     - Pointer to the length of the buffer. On return, it contains the actual length of the key element.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The key element was retrieved successfully.
   * - E_NOT_OK
     - The key element could not be retrieved due to an error.
   * - CRYPTO_E_PARAM_HANDLE
     - The cryptographic key ID is invalid or the key is not valid.
   * - CRYPTO_E_PARAM_POINTER
     - The result pointer or result length pointer is NULL.
   * - CRYPTO_E_PARAM_VALUE
     - The result length is zero.
   * - CRYPTO_E_SMALL_BUFFER
     - The result buffer is too small.
   * - CRYPTO_E_KEY_READ_FAIL
     - The key element cannot be read due to access restrictions.
   * - CRYPTO_E_UNINIT
     - The Crypto_62 module is not initialized.

Crypto_62_KeyGetStatus
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Crypto_62_KeyGetStatus(uint32 cryptoKeyId, Crypto_KeyStatusType *keyStatusPtr)

Retrieves the status of a cryptographic key.

**Sync/Async**
   TRUE

**Reentrancy**
   Not reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - cryptoKeyId
     - The ID of the cryptographic key.
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
     - The key status was retrieved successfully.
   * - E_NOT_OK
     - The key status could not be retrieved due to an error.
   * - CRYPTO_E_PARAM_HANDLE
     - The cryptographic key ID is invalid.
   * - CRYPTO_E_PARAM_POINTER
     - The key status pointer is NULL.
   * - CRYPTO_E_UNINIT
     - The Crypto_62 module is not initialized.

Crypto_62_KeyElementCopy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Crypto_62_KeyElementCopy(uint32 cryptoKeyId, uint32 keyElementId, uint32 targetCryptoKeyId, uint32 targetKeyElementId)

Copies a key element from one cryptographic key to another.

**Sync/Async**
   TRUE

**Reentrancy**
   Not reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - cryptoKeyId
     - The ID of the source cryptographic key.
   * - [in]
     - keyElementId
     - The ID of the key element to copy from the source key.
   * - [in]
     - targetCryptoKeyId
     - The ID of the target cryptographic key.
   * - [in]
     - targetKeyElementId
     - The ID of the key element to copy to in the target key.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The key element was copied successfully.
   * - E_NOT_OK
     - The key element could not be copied due to an error.
   * - CRYPTO_E_PARAM_HANDLE
     - The source or target cryptographic key ID is invalid.
   * - CRYPTO_E_KEY_READ_FAIL
     - The source key element cannot be read due to access restrictions.
   * - CRYPTO_E_KEY_WRITE_FAIL
     - The target key element cannot be written due to access restrictions.
   * - CRYPTO_E_KEY_SIZE_MISMATCH
     - The source and target key elements have different sizes.
   * - CRYPTO_E_UNINIT
     - The Crypto_62 module is not initialized.

Crypto_62_KeyElementCopyPartial
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Crypto_62_KeyElementCopyPartial(uint32 cryptoKeyId, uint32 keyElementId, uint32 keyElementSourceOffset, uint32 keyElementTargetOffset, uint32 keyElementCopyLength, uint32 targetCryptoKeyId, uint32 targetKeyElementId)

Copies a partial key element from one cryptographic key to another.

**Sync/Async**
   TRUE

**Reentrancy**
   Not reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - cryptoKeyId
     - The ID of the source cryptographic key.
   * - [in]
     - keyElementId
     - The ID of the key element to copy from the source key.
   * - [in]
     - keyElementSourceOffset
     - The offset in the source key element where the copy starts.
   * - [in]
     - keyElementTargetOffset
     - The offset in the target key element where the copy starts.
   * - [in]
     - keyElementCopyLength
     - The length of the data to be copied.
   * - [in]
     - targetCryptoKeyId
     - The ID of the target cryptographic key.
   * - [in]
     - targetKeyElementId
     - The ID of the key element to copy to in the target key.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The partial key element was copied successfully.
   * - E_NOT_OK
     - The partial key element could not be copied due to an error.
   * - CRYPTO_E_PARAM_HANDLE
     - The source or target cryptographic key ID is invalid.
   * - CRYPTO_E_KEY_READ_FAIL
     - The source key element cannot be read due to access restrictions.
   * - CRYPTO_E_KEY_WRITE_FAIL
     - The target key element cannot be written due to access restrictions.
   * - CRYPTO_E_KEY_SIZE_MISMATCH
     - The source and target key elements have different sizes or the copy length exceeds the element size.
   * - CRYPTO_E_UNINIT
     - The Crypto_62 module is not initialized.

Crypto_62_KeyCopy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Crypto_62_KeyCopy(uint32 cryptoKeyId, uint32 targetCryptoKeyId)

Copies all key elements from one cryptographic key to another.

**Sync/Async**
   TRUE

**Reentrancy**
   Not reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - cryptoKeyId
     - The ID of the source cryptographic key.
   * - [in]
     - targetCryptoKeyId
     - The ID of the target cryptographic key.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - All key elements were copied successfully.
   * - E_NOT_OK
     - The key elements could not be copied due to an error.
   * - CRYPTO_E_PARAM_HANDLE
     - The source or target cryptographic key ID is invalid.
   * - CRYPTO_E_UNINIT
     - The Crypto_62 module is not initialized.

Crypto_62_KeyElementIdsGet
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Crypto_62_KeyElementIdsGet(uint32 cryptoKeyId, uint32 *keyElementIdsPtr, uint32 *keyElementIdsLengthPtr)

Retrieves the IDs and lengths of all key elements for a cryptographic key.

**Sync/Async**
   TRUE

**Reentrancy**
   Not reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - cryptoKeyId
     - The ID of the cryptographic key.
   * - [out]
     - keyElementIdsPtr
     - Pointer to the array where the key element IDs will be stored.
   * - [out]
     - keyElementIdsLengthPtr
     - Pointer to the array where the key element lengths will be stored.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The key element IDs and lengths were retrieved successfully.
   * - E_NOT_OK
     - The key element IDs and lengths could not be retrieved due to an error.
   * - CRYPTO_E_PARAM_HANDLE
     - The cryptographic key ID is invalid.
   * - CRYPTO_E_UNINIT
     - The Crypto_62 module is not initialized.

Crypto_62_RandomSeed
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Crypto_62_RandomSeed(uint32 cryptoKeyId, const uint8 *seedPtr, uint32 seedLength)

Seeds the random number generator with a given seed.

**Sync/Async**
   TRUE

**Reentrancy**
   Not reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - cryptoKeyId
     - The ID of the cryptographic key associated with the random number generator.
   * - [in]
     - seedPtr
     - Pointer to the seed data.
   * - [in]
     - seedLength
     - The length of the seed data.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The random number generator was seeded successfully.
   * - E_NOT_OK
     - The random number generator could not be seeded due to an error.
   * - CRYPTO_E_PARAM_HANDLE
     - The cryptographic key ID is invalid.
   * - CRYPTO_E_PARAM_POINTER
     - The seed pointer is NULL.
   * - CRYPTO_E_PARAM_VALUE
     - The seed length is zero.
   * - CRYPTO_E_KEY_NOT_VALID
     - The cryptographic key is not valid.
   * - CRYPTO_E_UNINIT
     - The Crypto_62 module is not initialized.

Crypto_62_KeyGenerate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Crypto_62_KeyGenerate(uint32 cryptoKeyId)

Generates a cryptographic key.

**Sync/Async**
   TRUE

**Reentrancy**
   Not reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - cryptoKeyId
     - The ID of the cryptographic key to generate.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The key was generated successfully.
   * - E_NOT_OK
     - The key could not be generated due to an error.
   * - CRYPTO_E_PARAM_HANDLE
     - The cryptographic key ID is invalid.
   * - CRYPTO_E_UNINIT
     - The Crypto_62 module is not initialized.

Crypto_62_KeyDerive
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Crypto_62_KeyDerive(uint32 cryptoKeyId, uint32 targetCryptoKeyId)

Derives a cryptographic key from another key.

**Sync/Async**
   TRUE

**Reentrancy**
   Not reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - cryptoKeyId
     - The ID of the source cryptographic key.
   * - [in]
     - targetCryptoKeyId
     - The ID of the target cryptographic key to derive.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The key was derived successfully.
   * - E_NOT_OK
     - The key could not be derived due to an error.
   * - CRYPTO_E_PARAM_HANDLE
     - The source or target cryptographic key ID is invalid.
   * - CRYPTO_E_UNINIT
     - The Crypto_62 module is not initialized.

Crypto_62_KeyExchangeCalcPubVal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Crypto_62_KeyExchangeCalcPubVal(uint32 cryptoKeyId, uint8 *publicValuePtr, uint32 *publicValueLengthPtr)

Calculates the public value for a key exchange operation.

**Sync/Async**
   TRUE

**Reentrancy**
   Not reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - cryptoKeyId
     - The ID of the cryptographic key used for the key exchange.
   * - [out]
     - publicValuePtr
     - Pointer to the buffer where the public value will be stored.
   * - [inout]
     - publicValueLengthPtr
     - Pointer to the length of the public value buffer. On return, it contains the actual length of the public value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The public value was calculated successfully.
   * - E_NOT_OK
     - The public value could not be calculated due to an error.
   * - CRYPTO_E_PARAM_HANDLE
     - The cryptographic key ID is invalid.
   * - CRYPTO_E_PARAM_POINTER
     - The public value pointer or public value length pointer is NULL.
   * - CRYPTO_E_PARAM_VALUE
     - The public value length is zero.
   * - CRYPTO_E_UNINIT
     - The Crypto_62 module is not initialized.

Crypto_62_KeyExchangeCalcSecret
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Crypto_62_KeyExchangeCalcSecret(uint32 cryptoKeyId, const uint8 *partnerPublicValuePtr, uint32 partnerPublicValueLength)

Calculates the shared secret for a key exchange operation.

**Sync/Async**
   TRUE

**Reentrancy**
   Not reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - cryptoKeyId
     - The ID of the cryptographic key used for the key exchange.
   * - [in]
     - partnerPublicValuePtr
     - Pointer to the partner's public value.
   * - [in]
     - partnerPublicValueLength
     - The length of the partner's public value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The shared secret was calculated successfully.
   * - E_NOT_OK
     - The shared secret could not be calculated due to an error.
   * - CRYPTO_E_PARAM_HANDLE
     - The cryptographic key ID is invalid.
   * - CRYPTO_E_PARAM_POINTER
     - The partner's public value pointer is NULL.
   * - CRYPTO_E_PARAM_VALUE
     - The partner's public value length is zero.
   * - CRYPTO_E_UNINIT
     - The Crypto_62 module is not initialized.

Crypto_62_CustomSync
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Crypto_62_CustomSync(uint32 dispatchId, uint32 keyId, uint32 keyElementId, uint32 targetKeyId, uint32 targetKeyElementId, const uint8 *inputPtr, uint32 inputLength, uint8 *outputPtr, uint32 *outputLengthPtr, uint8 *secondaryOutputPtr, uint32 *secondaryOutputLengthPtr)

Performs a custom synchronous cryptographic operation.

**Sync/Async**
   TRUE

**Reentrancy**
   Not reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - dispatchId
     - The ID of the dispatch table entry.
   * - [in]
     - keyId
     - The ID of the source cryptographic key.
   * - [in]
     - keyElementId
     - The ID of the source key element.
   * - [in]
     - targetKeyId
     - The ID of the target cryptographic key.
   * - [in]
     - targetKeyElementId
     - The ID of the target key element.
   * - [in]
     - inputPtr
     - Pointer to the input data.
   * - [in]
     - inputLength
     - The length of the input data.
   * - [out]
     - outputPtr
     - Pointer to the buffer where the output data will be stored.
   * - [inout]
     - outputLengthPtr
     - Pointer to the length of the output buffer. On return, it contains the actual length of the output data.
   * - [out]
     - secondaryOutputPtr
     - Pointer to the buffer where the secondary output data will be stored.
   * - [inout]
     - secondaryOutputLengthPtr
     - Pointer to the length of the secondary output buffer. On return, it contains the actual length of the secondary output data.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The operation was performed successfully.
   * - E_NOT_OK
     - The operation could not be performed due to an error.
   * - CRYPTO_E_PARAM_HANDLE
     - The target cryptographic key ID is invalid.
   * - CRYPTO_E_UNINIT
     - The Crypto_62 module is not initialized.

