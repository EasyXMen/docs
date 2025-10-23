
通用类型定义 Definition of General Types
------------------------------------------------------------------------------------------------------------------------------

.. list-table:: 
   :widths: 15 5 20
   :header-rows: 1

   * - Type Name
     - Type
     - Description

   * - Crypto_JobPrimitiveInputOutputType
     - struct Crypto_JobPrimitiveInputOutputType
     - Structure which contains input and output information depending on the job and the crypto primitive.,ref@01009.

   * - Crypto_AlgorithmInfoType
     - struct Crypto_AlgorithmInfoType
     - Structure which determines the exact algorithm.

   * - Crypto_PrimitiveInfoType
     - struct Crypto_PrimitiveInfoType
     - Structure which contains basic information about the crypto primitive.

   * - Crypto_JobPrimitiveInfoType
     - struct Crypto_JobPrimitiveInfoType
     - Structure which contains further information, which depends on the job and the crypto primitive.

   * - Crypto_JobRedirectionInfoType
     - struct Crypto_JobRedirectionInfoType
     - Structure which holds the identifiers of the keys and key elements which shall be used as input and output for a job and a bit structure which indicates which buffers shall be redirected to those key elements.

   * - Crypto_JobType
     - struct Crypto_JobType
     - Structure which contains further information, which depends on the job and the crypto primitive.

   * - Crypto_AlgorithmFamilyType
     - enum
     - Enumeration of the algorithm family.

   * - Crypto_AlgorithmModeType
     - enum
     - Enumeration of the algorithm mode.

   * - Crypto_InputOutputRedirectionConfigType
     - enum
     - Defines which of the input/output parameters are re-directed to a key element. The values can be combined to define a bit field.

   * - Crypto_JobStateType
     - enum
     - Enumeration of the current job state.

   * - Crypto_ServiceInfoType
     - enum
     - Enumeration of the kind of the service.

   * - Crypto_ProcessingType
     - enum
     - Enumeration of the processing type.


      

