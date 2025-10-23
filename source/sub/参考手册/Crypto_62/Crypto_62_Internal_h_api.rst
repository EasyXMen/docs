提供的服务 Services
---------------------------------------------------------------------------------------------
Crypto_62_Encrypt_Process
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Crypto_62_Encrypt_Process(uint32 objectId, Crypto_AlgorithmFamilyType algorithmfamily, Crypto_AlgorithmModeType mode, Crypto_OperationModeType operateMode)

Processes an encryption operation.

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
     - algorithmfamily
     - The family of the encryption algorithm.
   * - [in]
     - mode
     - The mode of the encryption algorithm.
   * - [in]
     - operateMode
     - The operation mode of the encryption process (e.g., start, update, finish).

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The encryption process was successful.
   * - E_NOT_OK
     - The encryption process failed.
   * - CRYPTO_ERROR_ALGO_NOT_SUPPORTED
     - The specified algorithm family is not supported.

Crypto_62_Decrypt_Process
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Crypto_62_Decrypt_Process(uint32 objectId, Crypto_AlgorithmFamilyType algorithmfamily, Crypto_AlgorithmModeType mode, Crypto_OperationModeType operateMode)

Processes a decryption operation.

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
     - algorithmfamily
     - The family of the decryption algorithm.
   * - [in]
     - mode
     - The mode of the decryption algorithm.
   * - [in]
     - operateMode
     - The operation mode of the decryption process (e.g., start, update, finish).

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The decryption process was successful.
   * - E_NOT_OK
     - The decryption process failed.
   * - CRYPTO_ERROR_ALGO_NOT_SUPPORTED
     - The specified algorithm family is not supported.

Crypto_62_AeadEncrypt_Process
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Crypto_62_AeadEncrypt_Process(uint32 objectId, Crypto_AlgorithmFamilyType algorithmfamily, Crypto_AlgorithmModeType mode, Crypto_OperationModeType operateMode)

Processes an AEAD (Authenticated Encryption with Associated Data) encryption operation.

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
     - algorithmfamily
     - The family of the AEAD encryption algorithm.
   * - [in]
     - mode
     - The mode of the AEAD encryption algorithm.
   * - [in]
     - operateMode
     - The operation mode of the AEAD encryption process (e.g., start, update, finish).

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The AEAD encryption process was successful.
   * - E_NOT_OK
     - The AEAD encryption process failed.
   * - CRYPTO_ERROR_ALGO_NOT_SUPPORTED
     - The specified algorithm family is not supported.

Crypto_62_AeadDecrypt_Process
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Crypto_62_AeadDecrypt_Process(uint32 objectId, Crypto_AlgorithmFamilyType algorithmfamily, Crypto_AlgorithmModeType mode, Crypto_OperationModeType operateMode)

Processes an AEAD (Authenticated Encryption with Associated Data) decryption operation.

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
     - algorithmfamily
     - The family of the AEAD decryption algorithm.
   * - [in]
     - mode
     - The mode of the AEAD decryption algorithm.
   * - [in]
     - operateMode
     - The operation mode of the AEAD decryption process (e.g., start, update, finish).

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The AEAD decryption process was successful.
   * - E_NOT_OK
     - The AEAD decryption process failed.
   * - CRYPTO_ERROR_ALGO_NOT_SUPPORTED
     - The specified algorithm family is not supported.

Crypto_62_SignatureGenerate_Process
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Crypto_62_SignatureGenerate_Process(uint32 objectId, Crypto_AlgorithmFamilyType algorithmfamily, Crypto_AlgorithmModeType mode, Crypto_OperationModeType operateMode)

Processes a signature generation operation.

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
     - algorithmfamily
     - The family of the signature generation algorithm.
   * - [in]
     - mode
     - The mode of the signature generation algorithm.
   * - [in]
     - operateMode
     - The operation mode of the signature generation process (e.g., start, update, finish).

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The signature generation process was successful.
   * - E_NOT_OK
     - The signature generation process failed.

Crypto_62_SignatureVerify_Process
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Crypto_62_SignatureVerify_Process(uint32 objectId, Crypto_AlgorithmFamilyType algorithmfamily, Crypto_AlgorithmModeType mode, Crypto_OperationModeType operateMode)

Processes a signature verification operation.

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
     - algorithmfamily
     - The family of the signature verification algorithm.
   * - [in]
     - mode
     - The mode of the signature verification algorithm.
   * - [in]
     - operateMode
     - The operation mode of the signature verification process (e.g., start, update, finish).

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The signature verification process was successful.
   * - E_NOT_OK
     - The signature verification process failed.

Crypto_62_RandomGenerate_Process
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Crypto_62_RandomGenerate_Process(uint32 objectId, Crypto_AlgorithmFamilyType algorithmfamily, Crypto_AlgorithmModeType mode, Crypto_OperationModeType operateMode)

Processes a random number generation operation.

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
     - algorithmfamily
     - The family of the random number generation algorithm.
   * - [in]
     - mode
     - The mode of the random number generation algorithm.
   * - [in]
     - operateMode
     - The operation mode of the random number generation process (e.g., start, update, finish).

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The random number generation process was successful.
   * - E_NOT_OK
     - The random number generation process failed.
   * - CRYPTO_ERROR_ALGO_NOT_SUPPORTED
     - The specified algorithm mode is not supported.

Crypto_62_RandomSeed_Process
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Crypto_62_RandomSeed_Process(uint32 objectId, Crypto_AlgorithmFamilyType algorithmfamily, Crypto_AlgorithmModeType mode)

Processes a random number generator (RNG) seeding operation.

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
     - algorithmfamily
     - The family of the RNG algorithm.
   * - [in]
     - mode
     - The mode of the RNG algorithm (not used in this function).

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The RNG seeding process was successful.
   * - E_NOT_OK
     - The RNG seeding process failed.

Crypto_62_KeyGenerate_Process
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Crypto_62_KeyGenerate_Process(uint32 objectId, Crypto_AlgorithmFamilyType algorithmfamily, Crypto_AlgorithmModeType mode)

Processes a key generation operation.

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
     - algorithmfamily
     - The family of the key generation algorithm.
   * - [in]
     - mode
     - The mode of the key generation algorithm (not used in this function).

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The key generation process was successful.
   * - E_NOT_OK
     - The key generation process failed.

Crypto_62_KeyDerive_Process
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Crypto_62_KeyDerive_Process(uint32 objectId, Crypto_AlgorithmFamilyType algorithmfamily, Crypto_AlgorithmModeType mode)

Processes a key derivation operation.

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
     - algorithmfamily
     - The family of the key derivation algorithm.
   * - [in]
     - mode
     - The mode of the key derivation algorithm (not used in this function).

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The key derivation process was successful.
   * - E_NOT_OK
     - The key derivation process failed.

Crypto_62_KeyExchangeCalcPubval_Process
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Crypto_62_KeyExchangeCalcPubval_Process(uint32 objectId, Crypto_AlgorithmFamilyType algorithmfamily, Crypto_AlgorithmModeType mode)

Processes a key exchange operation to calculate the public value.

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
     - algorithmfamily
     - The family of the key exchange algorithm.
   * - [in]
     - mode
     - The mode of the key exchange algorithm (not used in this function).

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The public value calculation was successful.
   * - E_NOT_OK
     - The public value calculation failed.

Crypto_62_KeyExchangeCalcSecret_Process
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Crypto_62_KeyExchangeCalcSecret_Process(uint32 objectId, Crypto_AlgorithmFamilyType algorithmfamily, Crypto_AlgorithmModeType mode)

Processes a key exchange operation to calculate the shared secret.

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
     - algorithmfamily
     - The family of the key exchange algorithm.
   * - [in]
     - mode
     - The mode of the key exchange algorithm (not used in this function).

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The shared secret calculation was successful.
   * - E_NOT_OK
     - The shared secret calculation failed.

Custom_Service_Process
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Custom_Service_Process(uint32 objectId, Crypto_AlgorithmFamilyType algorithmfamily, Crypto_AlgorithmModeType mode)

Processes a custom cryptographic service.

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
     - algorithmfamily
     - The family of the custom cryptographic algorithm.
   * - [in]
     - mode
     - The mode of the custom cryptographic algorithm (not used in this function).

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The custom service process was successful.
   * - E_NOT_OK
     - The custom service process failed.

Crypto_AesDecryptProcess
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Crypto_AesDecryptProcess(uint32 objectId, Crypto_AlgorithmModeType mode)

Processes an AES decryption operation.

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
     - mode
     - The mode of the AES decryption algorithm.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The AES decryption process was successful.
   * - E_NOT_OK
     - The AES decryption process failed.
   * - CRYPTO_ERROR_ALGO_NOT_SUPPORTED
     - The specified algorithm mode is not supported.

Crypto_AesEncryptProcess
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Crypto_AesEncryptProcess(uint32 objectId, Crypto_AlgorithmModeType mode)

Processes an AES encryption operation.

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
     - mode
     - The mode of the AES encryption algorithm.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The AES encryption process was successful.
   * - E_NOT_OK
     - The AES encryption process failed.
   * - CRYPTO_ERROR_ALGO_NOT_SUPPORTED
     - The specified algorithm mode is not supported.

Crypto_62_ProcessAsyncJob_NonQueue
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Crypto_62_ProcessAsyncJob_NonQueue(uint32 objectId, Crypto_JobType *job)

Processes an asynchronous cryptographic job without queuing.

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

Crypto_ProcessAlgorithm
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Crypto_ProcessAlgorithm(uint32 objectId, Crypto_OperationModeType operateMode)

Processes the specified cryptographic algorithm based on the given object ID and operation mode.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant but not for the same object ID

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - objectId
     - Unique identifier of the cryptographic job.
   * - [in]
     - operateMode
     - Mode of operation for the cryptographic process (e.g., initialization, processing, finalization).

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The cryptographic operation was successfully processed.
   * - E_NOT_OK
     - The cryptographic operation failed due to an underlying error or unsupported algorithm/service.

Crypto_62_ProcessJob_Internal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Crypto_62_ProcessJob_Internal(uint32 objectId, Crypto_JobType *job, Crypto_OperationModeType operationMode)

Processes a cryptographic job internally based on the specified operation mode.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant but not for the same object ID and job

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - objectId
     - Unique identifier of the cryptographic job.
   * - [inout]
     - job
     - Pointer to the cryptographic job structure containing input and output data.
   * - [in]
     - operationMode
     - Mode of operation for the cryptographic job (e.g., start, update, finish).

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The cryptographic job was successfully processed according to the specified operation mode.
   * - E_NOT_OK
     - The cryptographic job failed due to an underlying error, invalid operation mode, or job state mismatch.

Crypto_62_QueueInJob
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Crypto_62_QueueInJob(uint32 objectid, Crypto_JobType *job)

Enqueues a cryptographic job into the job queue based on its priority.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant but not for the same object ID and job

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - objectid
     - Unique identifier of the cryptographic job
   * - [in]
     - job
     - Pointer to the cryptographic job structure to be enqueued.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The cryptographic job was successfully enqueued.
   * - E_NOT_OK
     - The cryptographic job failed to be enqueued due to an underlying error.
   * - CRYPTO_E_BUSY
     - The job queue is full and the job cannot be enqueued at this time.

