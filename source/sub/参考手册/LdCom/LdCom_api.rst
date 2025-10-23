接口描述 Interface Description
================================================

类型定义 Type Definitions
--------------------------------------------------------------------------------
.. 引用接口描述。来自于code->doxygen->latex->rst
.. 引用接口描述。 From code->doxygen->latex->rst
.. include:: LdCom_Types.rst

      
提供的服务 Services
---------------------------------------------------------------------------------
LdCom_Init
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void LdCom_Init(const LdCom_ConfigType *config)

Initializes internal and external interfaces and variables of the AUTOSAR LdCom module for the further processing.

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
     - Pointer to the AUTOSAR LdCom module's configuration data.

**Return type**
   void


LdCom_DeInit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void LdCom_DeInit(void)

With a call to LdCom_DeInit the AUTOSAR LdCom module is put into an not initialized state.

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant


**Return type**
   void


LdCom_GetVersionInfo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void LdCom_GetVersionInfo(Std_VersionInfoType *versioninfo)

Returns the version information of ldCom module.

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
   * - [out]
     - versioninfo
     - Pointer to where to store the version information of ldCom module.

**Return type**
   void


LdCom_Transmit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType LdCom_Transmit(PduIdType Id, const PduInfoType *PduInfoPtr)

Requests transmission of a signal.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant for different Ids. Non reentrant for the same Id.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - Id
     - Identifier of the signal to be transmitted.
   * - [in]
     - PduInfoPtr
     - Length of and pointer to the signal data and pointer to MetaData.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Transmit request has been accepted.
   * - E_NOT_OK
     - Transmit request has not been accepted.

.. 引用回调接口描述。 来自于code->doxygen->latex->rst
.. 引用回调接口描述。 From code->doxygen->latex->rst
.. include:: LdCom_Cbk_api.rst


依赖的服务 Applicable Services
--------------------------------------------------------------------------------

可选接口 Optional Interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 10 5 30
   :header-rows: 1

   * - API Function
     - Header File
     - Description

   * - Det_ReportError 
     - Det.h
     - Service to report development errors.

   * - PduR_LdComTransmit 
     - PduR_LdCom.h
     - Requests transmission of a PDU.

配置接口 Configuration Interfaces
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 10 5 30
   :header-rows: 1

   * - API Function
     - Header File
     - Description

   * - LdComUser_LdComCbkCopyTxData 
     - LdCom_Callout.h/<user.h>
     - Copy transmission data form user for TP IPdu Send.

   * - LdComUser_LdComCbkTpTxConfirmation 
     - LdCom_Callout.h/<user.h>
     - transition confirmation for TP IPdu Send.

   * - LdComUser_LdComCbkStartOfReception 
     - LdCom_Callout.h/<user.h>
     - start reception for TP IPdu receive.

   * - LdComUser_LdComCbkCopyRxData 
     - LdCom_Callout.h/<user.h>
     - Copy received data to user for TP IPdu receive.

   * - LdComUser_LdComCbkTpRxIndication 
     - LdCom_Callout.h/<user.h>
     - Indication of a received PDU from a lower layer module for TP IPdu receive.

   * - LdComUser_LdComCbkRxIndication 
     - LdCom_Callout.h/<user.h>
     - Indication of a received PDU for IF IPdu receive.

   * - LdComUser_LdComCbkTriggerTransmit 
     - LdCom_Callout.h/<user.h>
     - obtain Transmission data from a lower layer module for IF IPdu Send.

   * - LdComUser_LdComCbkTxConfirmation 
     - LdCom_Callout.h/<user.h>
     - transition confirmation from a lower layer module for TP IPdu Send.