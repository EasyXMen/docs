
类型定义 Type Definitions
----------------------------------------

.. list-table:: 
   :widths: 15 5 20
   :header-rows: 1

   * - Type Name
     - Type
     - Description

   * - CryIf_ConfigType
     - uint8
     - Type definition for CryIf configuration.

   * - CryIf_FuncNameConfigType
     - struct CryIf_FuncNameConfigType
     - Function pointer configuration structure for Crypto operations.

   * - CryIf_KeyCfgType
     - struct CryIf_KeyCfgType
     - Key configuration structure for CryIf.

   * - CryIf_ChannelCfgType
     - struct CryIf_ChannelCfgType
     - Channel configuration structure for CryIf.


      
提供的服务 Services
----------------------------------------
CryIf_Init
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void CryIf_Init(const CryIf_ConfigType *configPtr)

Initializes the Cryptographic Interface (CryIf) module.

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
     - Pointer to the configuration structure for the CryIf module.

**Return type**
   void


CryIf_GetVersionInfo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void CryIf_GetVersionInfo(Std_VersionInfoType *versioninfo)

Retrieves the version information of the Cryptographic Interface (CryIf) module.

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
     - versioninfo
     - Pointer to the version information structure.

**Return type**
   void


CryIf_ProcessJob
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType CryIf_ProcessJob(uint32 channelId, Crypto_JobType *job)

Processes a cryptographic job using the specified channel.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant but not for the same channel ID

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - channelId
     - The ID of the channel to use for processing the job.
   * - [inout]
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
     - The job was successfully processed.
   * - E_NOT_OK
     - The job could not be processed due to an error.

CryIf_CancelJob
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType CryIf_CancelJob(uint32 channelId, Crypto_JobType *job)

Cancels a cryptographic job using the specified channel.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant but not for the same channel ID

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - channelId
     - The ID of the channel to use for canceling the job.
   * - [inout]
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
     - The job was successfully canceled.
   * - E_NOT_OK
     - The job could not be canceled due to an error.

CryIf_KeyElementSet
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType CryIf_KeyElementSet(uint32 cryIfKeyId, uint32 keyElementId, const uint8 *keyPtr, uint32 keyLength)

Sets a key element for a cryptographic key.

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
     - cryIfKeyId
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
     - The key element was successfully set.
   * - E_NOT_OK
     - The key element could not be set due to an error.

CryIf_KeySetValid
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType CryIf_KeySetValid(uint32 cryIfKeyId)

Sets a cryptographic key as valid.

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
     - cryIfKeyId
     - The ID of the cryptographic key to set as valid.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The key was successfully set as valid.
   * - E_NOT_OK
     - The key could not be set as valid due to an error.

CryIf_KeySetInValid
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType CryIf_KeySetInValid(uint32 cryIfKeyId)

Sets a cryptographic key as INvalid.

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
     - cryIfKeyId
     - The ID of the cryptographic key to set as INvalid.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The key was successfully set as INvalid.
   * - E_NOT_OK
     - The key could not be set as valid due to an error.

CryIf_KeyElementGet
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType CryIf_KeyElementGet(uint32 cryIfKeyId, uint32 keyElementId, uint8 *resultPtr, uint32 *resultLengthPtr)

Retrieves a key element from a cryptographic key.

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
     - cryIfKeyId
     - The ID of the cryptographic key.
   * - [in]
     - keyElementId
     - The ID of the key element to retrieve.
   * - [out]
     - resultPtr
     - Pointer to the buffer to store the key element data.
   * - [inout]
     - resultLengthPtr
     - Pointer to the length of the buffer. On return, it contains the actual length of the key element data.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The key element was successfully retrieved.
   * - E_NOT_OK
     - The key element could not be retrieved due to an error.

CryIf_KeyElementCopy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType CryIf_KeyElementCopy(uint32 cryIfKeyId, uint32 keyElementId, uint32 targetCryIfKeyId, uint32 targetKeyElementId)

Copies a key element from one cryptographic key to another.

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
     - cryIfKeyId
     - The ID of the source cryptographic key.
   * - [in]
     - keyElementId
     - The ID of the key element to copy.
   * - [in]
     - targetCryIfKeyId
     - The ID of the target cryptographic key.
   * - [in]
     - targetKeyElementId
     - The ID of the target key element.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The key element was successfully copied.
   * - E_NOT_OK
     - The key element could not be copied due to an error.

CryIf_KeyElementCopyPartial
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType CryIf_KeyElementCopyPartial(uint32 cryIfKeyId, uint32 keyElementId, uint32 keyElementSourceOffset, uint32 keyElementTargetOffset, uint32 keyElementCopyLength, uint32 targetCryIfKeyId, uint32 targetKeyElementId)

Copies a partial key element from one cryptographic key to another.

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
     - cryIfKeyId
     - The ID of the source cryptographic key.
   * - [in]
     - keyElementId
     - The ID of the key element to copy.
   * - [in]
     - keyElementSourceOffset
     - The offset within the source key element to start copying from.
   * - [in]
     - keyElementTargetOffset
     - The offset within the target key element to start copying to.
   * - [in]
     - keyElementCopyLength
     - The length of the data to copy.
   * - [in]
     - targetCryIfKeyId
     - The ID of the target cryptographic key.
   * - [in]
     - targetKeyElementId
     - The ID of the target key element.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The partial key element was successfully copied.
   * - E_NOT_OK
     - The partial key element could not be copied due to an error.

CryIf_KeyCopy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType CryIf_KeyCopy(uint32 cryIfKeyId, uint32 targetCryIfKeyId)

Copies a cryptographic key to another key.

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
     - cryIfKeyId
     - The ID of the source cryptographic key.
   * - [in]
     - targetCryIfKeyId
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
     - The key was successfully copied.
   * - E_NOT_OK
     - The key could not be copied due to an error.

CryIf_RandomSeed
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType CryIf_RandomSeed(uint32 cryIfKeyId, const uint8 *seedPtr, uint32 seedLength)

Seeds the random number generator with a cryptographic key.

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
     - cryIfKeyId
     - The ID of the cryptographic key to use as a seed.
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
     - The random number generator was successfully seeded.
   * - E_NOT_OK
     - The random number generator could not be seeded due to an error.

CryIf_KeyGenerate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType CryIf_KeyGenerate(uint32 cryIfKeyId)

Generates a key using the Crypto driver.This function generates a key based on the provided cryIfKeyId.It first checks if the CryIf module is initialized and if the provided key ID is valid.If the checks pass, it calls the Crypto_KeyGenerate_Name function of the corresponding driver API to generate the key.

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
     - cryIfKeyId
     - Key ID to generate a key for. This parameter is a unique identifier for a key configuration.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The key generation was successful.
   * - E_NOT_OK
     - The key generation failed, or a development error was detected.

CryIf_KeyDerive
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType CryIf_KeyDerive(uint32 cryIfKeyId, uint32 targetCryIfKeyId)

Derives a key from an existing key using the Crypto driver.This function derives a key based on the provided cryIfKeyId and targetCryIfKeyId.It first checks if the CryIf module is initialized and if the provided key IDs are valid.If the checks pass, it calls the Crypto_KeyDerive_Name function of the corresponding driver API to derive the key.

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
     - cryIfKeyId
     - Source key ID to derive a key from. This parameter is a unique identifier for a source key configuration.
   * - [in]
     - targetCryIfKeyId
     - Target key ID to derive a key for. This parameter is a unique identifier for a target key configuration.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The key derivation was successful.
   * - E_NOT_OK
     - The key derivation failed, or a development error was detected.

CryIf_KeyExchangeCalcPubVal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType CryIf_KeyExchangeCalcPubVal(uint32 cryIfKeyId, uint8 *publicValuePtr, uint32 *publicValueLengthPtr)

Calculates the public value for a key exchange using a cryptographic key.

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
     - cryIfKeyId
     - The ID of the cryptographic key to use for the key exchange.
   * - [out]
     - publicValuePtr
     - Pointer to the buffer to store the public value.
   * - [inout]
     - publicValueLengthPtr
     - Pointer to the length of the buffer. On return, it contains the actual length of the public value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The public value was successfully calculated.
   * - E_NOT_OK
     - The public value could not be calculated due to an error.

CryIf_KeyExchangeCalcSecret
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType CryIf_KeyExchangeCalcSecret(uint32 cryIfKeyId, const uint8 *partnerPublicValuePtr, uint32 partnerPublicValueLength)

Calculates the secret value for a key exchange using a cryptographic key and a partner's public value.

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
     - cryIfKeyId
     - The ID of the cryptographic key to use for the key exchange.
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
     - The secret value was successfully calculated.
   * - E_NOT_OK
     - The secret value could not be calculated due to an error.

CryIf_CustomSync
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType CryIf_CustomSync(uint32 dispatchId, uint32 keyId, uint32 keyElementId, uint32 targetKeyId, uint32 targetKeyElementId, const uint8 *inputPtr, uint32 inputLength, uint8 *outputPtr, uint32 *outputLengthPtr, uint8 *secondaryOutputPtr, uint32 *secondaryOutputLengthPtr)

Performs a custom synchronous cryptographic operation.

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
     - dispatchId
     - The dispatch ID for the custom operation.
   * - [in]
     - keyId
     - The ID of the cryptographic key to use.
   * - [in]
     - keyElementId
     - The ID of the key element to use.
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
     - Pointer to the buffer to store the output data.
   * - [inout]
     - outputLengthPtr
     - Pointer to the length of the output buffer. On return, it contains the actual length of the output data.
   * - [out]
     - secondaryOutputPtr
     - Pointer to the buffer to store the secondary output data.
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
     - The custom operation was successfully performed.
   * - E_NOT_OK
     - The custom operation could not be performed due to an error.

CryIf_KeyGetStatus
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType CryIf_KeyGetStatus(uint32 cryIfKeyId, Crypto_KeyStatusType *keyStatusPtr)

Retrieves the status of a key using the Crypto driver.This function retrieves the status of a key based on the provided cryIfKeyId.It calls the Crypto_62_KeyGetStatus function to get the key status.

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
     - cryIfKeyId
     - Key ID to retrieve the status for. This parameter is a unique identifier for a key configuration.
   * - [out]
     - keyStatusPtr
     - Pointer to the key status destination data. This parameter is a pointer to a variable that will store the key status.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The key status retrieval was successful.
   * - E_NOT_OK
     - The key status retrieval failed.

