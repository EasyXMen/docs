
类型定义
--------
.. 如果没有就不存在该章节，或为None

.. list-table:: 
   :widths: 15 5 20
   :header-rows: 1

   * - Type Name
     - Type
     - Description

   * - CanTSyn_RxIcvVerificationType
     - enum
     - Definition of whether or not ICV verification shall be supported.

   * - CanTSyn_GlobalTimeTxIcvSecuredType
     - enum
     - Definition of whether or not ICV generation shall be supported.

   * - CanTSyn_CriptographySelection
     - enum
     - This type shall define Symmetric or asymmetric cryptography selection for the ICV generation.

   * - CanTSyn_CryptoProcessingType
     - enum
     - Define the encryption and decryption process, synchronous or asynchronous.

   * - CanTSyn_InitStatusType
     - enum
     - define CanTSyn module initiation status

   * - CanTSyn_MasterStatusType
     - enum
     - define CanTSyn master operation status

   * - CanTSyn_TransmissionModeType
     - enum
     - Handles the enabling and disabling of the transmission mode.

   * - CanTSyn_RxCsmJobType
     - struct
     - Define information about the Csm job of verification.

   * - CanTSyn_GlobalTimeRxIcvVerificationType
     - struct
     - This type shall define the configuration of ICV verification.

   * - CanTSyn_TxCsmJobType
     - struct
     - Define information about the Csm job of generation.

   * - CanTSyn_GlobalTimeTxIcvGenerationType
     - struct
     - This type shall define the configuration of ICV generation.

   * - CanTSyn_AuthenticatedFieldInofoType
     - struct
     - This type shall describe the Time Authenticated Field.

   * - CanTSyn_CircularBufferType
     - struct
     - This type shall define the parameters of circular buffer.

   * - CanTSyn_ICVGenarationType
     - struct
     - This type shall define the runtime variables related to ICV generation.

   * - CanTSyn_ICVVerificationType
     - struct
     - This type shall define the runtime variables related to ICV verification.

   * - CanTSyn_MasterTimeInfoType
     - struct
     - store the time information for a time master

   * - CanTSyn_SlaveTimeInfoType
     - struct
     - store the time information for a time slave

   * - CanTSyn_GlobalTimeMasterType
     - struct
     - define configuration of the global time master

   * - CanTSyn_GlobalTimeSlaveType
     - struct
     - define configuration of the global time slave

   * - CanTSyn_DataIDListElementType
     - struct
     - define DataIDList messages

   * - CanTSyn_GlobalTimeDomainType
     - struct
     - define CanTSyn GlobalTimeDomain

   * - CanTSyn_ConfigType
     - struct
     - This is the base type for the configuration of the Time Synchronization over CAN. A pointer to an instance of this structure will be used in the initialization of the Time Synchronization over CAN.


      
提供的服务
-----------
CanTSyn_MainFunction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void CanTSyn_MainFunction(void)

This function needs to be called periodically to perform the AUTOSAR CanTSyn activities.

**Sync/Async**
   Asynchronous

**Reentrancy**
   Reentrant (Reentrant for different partitions. Non reentrant for the same partition.)


**Return type**
   void


