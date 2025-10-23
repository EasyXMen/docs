
主要配置类型定义 Main Configuration Type Definitions
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
.. 如果没有就不存在该章节，或为None

.. list-table:: 
   :widths: 15 5 20
   :header-rows: 1

   * - Type Name
     - Type
     - Description

   * - IpduM_TxPartType
     - structIpduM_TxPartTag
     - used to specify the configuration for TxStaticPart and TxDynamicPart.

   * - IpduM_TxRequestCfgType
     - structIpduM_TxRequestTag
     - used to specify the configuration for TxRequest.

   * - IpduM_RxDynamicPartType
     - structIpduM_RxDynamicPartTag
     - This container contains the configuration for the dynamic part of incoming RxIndication calls.

   * - IpduM_RxStaticPartType
     - structIpduM_RxStaticPartTag
     - This container contains the configuration for the static part of incoming RxIndication calls.

   * - IpduM_RxIndicationCfgType
     - structIpduM_RxIndicationTag
     - Contains the configuration for incoming RxIndication calls.

   * - IpduM_ContainedTxPduCfgType
     - structIpduM_ContainedTxPduCfgTag
     - Configuration of a sender ContainedPdu.

   * - IpduM_ContainerTxPduCfgType
     - structIpduM_ContainerTxPduCfgTag
     - Configuration of a transmitted container Pdu.

   * - IpduM_ContainedRxPduCfgType
     - structIpduM_ContainedRxPduCfgTag
     - Configuration of a received contained Pdu.

   * - IpduM_ContainerRxPduCfgType
     - structIpduM_ContainerRxPduTag
     - Configuration of a receiver ContainerPdu which may collect several ContainedPdus.

   * - IpduM_ConfigType
     - structIpduM_ConfigTag
     - configuration type of Ipdum module.


      
对外函数接口 External Function Interfaces
--------------------------------------------------------------------------------------------------------------------------
IpduM_Init
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void IpduM_Init(const IpduM_ConfigType *config)

Initializes the I-PDU Multiplexer.

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
     - config
     - Pointer to the AUTOSAR IpduM module's configuration data.

**Return type**
   voidIpduM_ConfigType


IpduM_GetVersionInfo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void IpduM_GetVersionInfo(Std_VersionInfoType *versioninfo)

Service returns the version information of this module.

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
     - versioninfo
     - Pointer to where to store the version.

**Return type**
   void


IpduM_Transmit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType IpduM_Transmit(PduIdType TxPduId, const PduInfoType *PduInfoPtr)

Service is called by the PDU-Router to request a transmission.

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant for the same PDU-ID. Reentrant for different PDU-ID.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - TxPduId
     - ID of I-PDU to be transmitted.
   * - [in]
     - PduInfoPtr
     - A pointer to a structure with I-PDU related. data that shall be transmitted: data length and pointer to I-SDU buffer.

**Return type**
   Std_ReturnType


IpduM_MainFunctionTx
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void IpduM_MainFunctionTx(IpduM_PartitionIDType ipduMPartitionId)

Performs the rx-processes of the activities that are not directly. initiated by the calls from PDU-R.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant for different partitions. Non reentrant for the same instance.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - ipduMPartitionId
     - ID of partition where this function will running.

**Return type**
   void


IpduM_MainFunctionRx
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void IpduM_MainFunctionRx(IpduM_PartitionIDType ipduMPartitionId)

Performs the tx-processes of the activities that are not directly. initiated by the calls from PDU-R. initiated by the calls from PDU-R.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant for different partitions. Non reentrant for the same instance.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - ipduMPartitionId
     - ID of partition where this function will running.

**Return type**
   void


