
内部类型定义 Definition of Internal Types
------------------------------------------------------------

.. list-table:: 
   :widths: 15 5 20
   :header-rows: 1

   * - Type Name
     - Type
     - Description

   * - Csm_CallbackFuncType
     - void*
     - Type definition for callback function pointer.

   * - Csm_JobInQueueType
     - struct Csm_JobInQueueType
     - Run-time configuration type definitions.

   * - Csm_JobInQueuePtrType
     - struct Csm_JobInQueueType
     - type definition for the pointer of the job in queue

   * - Csm_QueueChStatusType
     - struct Csm_QueueChStatusType
     - Type definition for the runtime status of a channel.

   * - Csm_JobCbkCfgType
     - struct Csm_JobCbkCfgType
     - Type definition for job notification callback configuration.


      
对内提供的服务 Services Provided Internally
---------------------------------------------------------------
Csm_ReportDetErr
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    static void Csm_ReportDetErr(uint8 serviceId, uint8 error)

Reports a development error to the DET (Development Error Tracer).

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
     - serviceId
     - Identifier of the service that detected the error.
   * - [in]
     - error
     - Error code of the detected error.

**Return type**
   void


Csm_ChkInitParam
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    boolean Csm_ChkInitParam(const Csm_ConfigType *configPtr)

Checks the initialization parameters for the CSM module.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant but not for the same timer instance

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - configPtr
     - Pointer to the configuration structure containing initialization parameters.

**Return type**
   boolean


Csm_ChkGetVersionInfo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Csm_ChkGetVersionInfo(const Std_VersionInfoType *versioninfo, uint8 sid)

Checks the parameters for the Csm_GetVersionInfo function.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant but not for the same timer instance

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - versioninfo
     - Pointer to the version information structure.
   * - [in]
     - sid
     - Service ID for which the version information is requested.

**Return type**
   Std_ReturnType


Csm_ChkServiceParam
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Csm_ChkServiceParam(uint32 jobId, uint8 sid)

Checks the parameters for the Csm_Servicexxx function.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant but not for the same timer instance

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - jobId
     - Job identifier.
   * - [in]
     - sid
     - Service ID.

**Return type**
   Std_ReturnType


Csm_ChkKeyEleSetParam
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Csm_ChkKeyEleSetParam(uint32 keyId, const uint8 *keyPtr, uint32 keyLength, uint8 sid)

Checks the parameters for the CryIf_KeyElementSet function.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant but not for the same timer instance

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - keyId
     - Key identifier.
   * - [in]
     - keyPtr
     - Pointer to the key data.
   * - [in]
     - keyLength
     - Length of the key data.
   * - [in]
     - sid
     - Service ID.

**Return type**
   Std_ReturnType


Csm_ChkKeySetValid
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Csm_ChkKeySetValid(uint32 keyId, uint8 sid)

Checks the parameters for the Csm_KeySetValid function.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant but not for the same timer instance

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - keyId
     - Key identifier.
   * - [in]
     - sid
     - Service ID.

**Return type**
   Std_ReturnType


Csm_ChkKeySetInValid
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Csm_ChkKeySetInValid(uint32 keyId, uint8 sid)

Checks the parameters for the Csm_KeySetInValid function.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant but not for the same timer instance

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - keyId
     - Key identifier.
   * - [in]
     - sid
     - Service ID.

**Return type**
   Std_ReturnType


Csm_ChkKeyEleGet
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Csm_ChkKeyEleGet(uint32 keyId, const uint8 *keyPtr, const uint32 *keyLengthPtr, uint8 sid)

Checks the parameters for the Csm_KeyElementGet function.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant but not for the same timer instance

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - keyId
     - Key identifier.
   * - [out]
     - keyPtr
     - Pointer to the buffer where the key data will be stored.
   * - [out]
     - keyLengthPtr
     - Pointer to the variable where the length of the key data will be stored.
   * - [in]
     - sid
     - Service ID.

**Return type**
   Std_ReturnType


Csm_ChkKeyEleCopy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Csm_ChkKeyEleCopy(const uint32 keyId, const uint32 targetKeyId, uint8 sid)

Checks the parameters for the Csm_KeyElementCopy function.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant but not for the same timer instance

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - keyId
     - Source key identifier.
   * - [in]
     - targetKeyId
     - tKeyId Target key identifier.
   * - [in]
     - sid
     - Service ID.

**Return type**
   Std_ReturnType


Csm_ChkKeyCopy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Csm_ChkKeyCopy(const uint32 keyId, const uint32 targetKeyId, uint8 sid)

Checks the parameters for the Csm_KeyCopy function.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant but not for the same timer instance

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - keyId
     - Source key identifier.
   * - [in]
     - targetKeyId
     - Target key identifier.
   * - [in]
     - sid
     - Service ID.

**Return type**
   Std_ReturnType


Csm_ChkKeyEleCopyPart
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Csm_ChkKeyEleCopyPart(uint32 keyId, uint32 targetKeyId, uint8 sid)

Checks the parameters for the Csm_KeyElementCopyPartial function.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant but not for the same timer instance

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - keyId
     - Source key identifier.
   * - [in]
     - targetKeyId
     - Target key identifier.
   * - [in]
     - sid
     - Service ID.

**Return type**
   Std_ReturnType


Csm_ChkRandomSeed
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Csm_ChkRandomSeed(uint32 keyId, const uint8 *seedPtr, uint32 seedLength, uint8 sid)

Checks the parameters for the Csm_RandomSeed function.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant but not for the same timer instance

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - keyId
     - Key identifier.
   * - [in]
     - seedPtr
     - Pointer to the random seed data.
   * - [in]
     - seedLength
     - Length of the random seed data.
   * - [in]
     - sid
     - Service ID.

**Return type**
   Std_ReturnType


Csm_ChkKeyGenerate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Csm_ChkKeyGenerate(uint32 keyId, uint8 sid)

Checks the parameters for the Csm_KeyGenerate function.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant but not for the same timer instance

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - keyId
     - Key identifier.
   * - [in]
     - sid
     - Service ID.

**Return type**
   Std_ReturnType


Csm_ChkKeyDerive
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Csm_ChkKeyDerive(uint32 keyId, uint32 targetKeyId, uint8 sid)

Checks the parameters for the Csm_KeyDerive function.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant but not for the same timer instance

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - keyId
     - Source key identifier.
   * - [in]
     - targetKeyId
     - Target key identifier.
   * - [in]
     - sid
     - Service ID.

**Return type**
   Std_ReturnType


Csm_ChkExCalcPubVal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Csm_ChkExCalcPubVal(uint32 keyId, const uint8 *publicValuePtr, const uint32 *publicValueLengthPtr, uint8 sid)

Checks the parameters for the Csm_KeyExchangeCalcPubVal function.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant but not for the same timer instance

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - keyId
     - Key identifier.
   * - [out]
     - publicValuePtr
     - Pointer to the buffer where the public value will be stored.
   * - [out]
     - publicValueLengthPtr
     - Pointer to the variable where the length of the public value will be stored.
   * - [in]
     - sid
     - Service ID.

**Return type**
   Std_ReturnType


Csm_ChkExCalcSecVal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Csm_ChkExCalcSecVal(uint32 keyId, const uint8 *partnerPublicValuePtr, uint32 partnerPublicValueLength, uint8 sid)

Checks the parameters for the Csm_KeyExchangeCalcSecret function.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant but not for the same timer instance

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - keyId
     - Key identifier.
   * - [in]
     - partnerPublicValuePtr
     - Pointer to the partner's public value data.
   * - [in]
     - partnerPublicValueLength
     - Length of the partner's public value data.
   * - [in]
     - sid
     - Service ID.

**Return type**
   Std_ReturnType


Csm_ChkJobKeySetValid
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Csm_ChkJobKeySetValid(uint32 jobId, uint8 sid)

Checks the parameters for the Csm_JobKeySetValid function.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant but not for the same timer instance

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - jobId
     - Job identifier.
   * - [in]
     - sid
     - Service ID.

**Return type**
   Std_ReturnType


Csm_ChkJobKeySetInValid
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Csm_ChkJobKeySetInValid(uint32 jobId, uint8 sid)

Checks the parameters for the Csm_JobKeySetInValid function.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant but not for the same timer instance

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - jobId
     - Job identifier.
   * - [in]
     - sid
     - Service ID.

**Return type**
   Std_ReturnType


Csm_ChkJobRandomSeed
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Csm_ChkJobRandomSeed(uint32 jobId, uint32 keyId, const uint8 *seedPtr, uint32 seedLength, uint8 sid)

Checks the parameters for the Csm_JobRandomSeed function.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant but not for the same timer instance

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - jobId
     - Job identifier.
   * - [in]
     - keyId
     - Key identifier.
   * - [in]
     - seedPtr
     - Pointer to the random seed data.
   * - [in]
     - seedLength
     - Length of the random seed data.
   * - [in]
     - sid
     - Service ID.

**Return type**
   Std_ReturnType


Csm_ChkJobKeyGenerate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Csm_ChkJobKeyGenerate(uint32 jobId, uint32 keyId, uint8 sid)

Checks the parameters for the Csm_JobKeyGenerate function.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant but not for the same timer instance

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - jobId
     - Job identifier.
   * - [in]
     - keyId
     - Key identifier.
   * - [in]
     - sid
     - Service ID.

**Return type**
   Std_ReturnType


Csm_ChkJobKeyDerive
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Csm_ChkJobKeyDerive(uint32 jobId, uint32 keyId, uint32 targetKeyId, uint8 sid)

Checks the parameters for the Csm_JobKeyDerive function.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant but not for the same timer instance

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - jobId
     - Job identifier.
   * - [in]
     - keyId
     - Source key identifier.
   * - [in]
     - targetKeyId
     - Target key identifier.
   * - [in]
     - sid
     - Service ID.

**Return type**
   Std_ReturnType


Csm_ChkJobExCalcPubVal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Csm_ChkJobExCalcPubVal(uint32 jobId, uint32 keyId, const uint8 *publicValuePtr, const uint32 *publicValueLengthPtr, uint8 sid)

Checks the parameters for the Csm_JobKeyExchangeCalcPubVal function.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant but not for the same timer instance

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - jobId
     - Job identifier.
   * - [in]
     - keyId
     - Key identifier.
   * - [out]
     - publicValuePtr
     - Pointer to the buffer where the public value will be stored.
   * - [out]
     - publicValueLengthPtr
     - Pointer to the variable where the length of the public value will be stored.
   * - [in]
     - sid
     - Service ID.

**Return type**
   Std_ReturnType


Csm_ChkJobExCalcSec
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Csm_ChkJobExCalcSec(uint32 jobId, uint32 keyId, const uint8 *partnerPublicValuePtr, uint32 partnerPublicValueLength, uint8 sid)

Checks the parameters for the Csm_JobKeyExchangeCalcSecret function.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant but not for the same timer instance

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - jobId
     - Job identifier.
   * - [in]
     - keyId
     - Key identifier.
   * - [in]
     - partnerPublicValuePtr
     - Pointer to the partner's public value data.
   * - [in]
     - partnerPublicValueLength
     - Length of the partner's public value data.
   * - [in]
     - sid
     - Service ID.

**Return type**
   Std_ReturnType


Csm_ChkCancelJob
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Csm_ChkCancelJob(uint32 jobId, uint8 sid)

Checks the parameters for the Csm_CancelJob function.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant but not for the same timer instance

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - jobId
     - Job identifier.
   * - [in]
     - sid
     - Service ID.

**Return type**
   Std_ReturnType


Csm_ChkCbkNotify
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Csm_ChkCbkNotify(const Crypto_JobType *job, uint8 sid)

Checks the parameters for the Csm_CbkNotify function.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant but not for the same timer instance

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - job
     - Pointer to the job structure.
   * - [in]
     - sid
     - Service ID.

**Return type**
   Std_ReturnType


