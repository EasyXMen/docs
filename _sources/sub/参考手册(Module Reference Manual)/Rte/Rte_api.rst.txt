接口描述(Interface Description)
=====================================
     
Rte生命周期(Rte Lifecycle)
-------------------------------------

Rte_Start
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. Return type 和 Return values 是可选板块，视情况而定
.. 小段的代码，用code，大段地用 code-block，此处用 code

.. code:: 

   Std_ReturnType Rte_Start(void)

RTE默认生成API。Rte_Start初始化当前分区使用的系统资源和通信资源。可信分区Rte_Start由BswM进行调度，
不可信分区Rte_Start由初始化Task进行调度，ORIENTAIS会自动为每个不可信分区配置初始化Task，生成的初始化Task代码调用Rte_Start进行初始化操作。

RTE generates APIs by default. Rte_Start initializes system and communication resources for the current partition. Rte_Start is scheduled by BswM in trusted partitions, and by the initialization Task in untrusted partitions. ORIENTAIS automatically configures an initialization Task for each untrusted partition, and the generated initialization Task code calls Rte_Start to perform initialization operations.

**Service ID**
   0x70

**Sync/Async**
   Synchronous

**Reentrancy**
   Non Reentrant

**Parameters**
   None

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description

   * - RTE_E_OK
     - RTE初始化成功(RTE initialization successful)
       


   * - RTE_E_LIMIT
     - RTE初始化时序有问题，初始化不成功(RTE initialization sequence issue, initialization failed)
       


Rte_Stop
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: 

   Std_ReturnType Rte_Stop(void)

RTE默认生成API。Rte_Stop释放当前分区使用的系统资源和通信资源，并关闭 RTE。根据BswM配置情况，在进入睡眠/低功耗等模式时调用

RTE generates APIs by default. Rte_Stop releases system and communication resources used by the current partition and shuts down RTE. It is called when entering sleep/low-power modes based on BswM configuration.

**Service ID**
   0x71

**Sync/Async**
   Synchronous

**Reentrancy**
   Non Reentrant

**Parameters**
   None

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description

   * - RTE_E_OK
     - RTE资源释放成功(RTE resources are released successfully)
              

   * - RTE_E_LIMIT
     - RTE资源释放失败(RTE resource release failed)
              

CallBack回调
-------------------------------------

Rte_COMCbk_<sn>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: 

   void Rte_COMCbk_<sn> (void)

当Com中Signal配置了接收通知时生成。这个回调函数表明Signal已经收到最新值。Com模块中接收到Signal时，通知到RTE。

Generated when reception notification is configured for a Signal in Com. This callback function indicates the Signal has received the latest value. When a Signal is received in the Com module, RTE is notified.

**Service ID**
   0x9f

**Sync/Async**
   Synchronous

**Reentrancy**
   Non Reentrant

**Parameters**
   None

**Return type**
   void

**Return values**
   None

Rte_COMCbkTAck_<sn>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: 

   void Rte_COMCbkTAck_<sn> (void)

当Com中Signal配置了发送确认通知时生成。这个回调函数表明Signal已经由Com打包到Pdu中且发送成功。Com模块中发送Signal成功时，通知到RTE。

Generated when transmission acknowledgment notification is configured for a Signal in Com. This callback function indicates the Signal has been packaged into a PDU by Com and sent successfully. When a Signal is successfully transmitted in the Com module, RTE is notified.

**Service ID**
   0x90

**Sync/Async**
   Synchronous

**Reentrancy**
   Non Reentrant

**Parameters**
   None

**Return type**
   void

**Return values**
   None

Rte_COMCbkTErr_<sn>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: 

   void Rte_COMCbkTErr_<sn> (void)

当Com中Signal配置了发送错误通知时生成。这个回调函数表明Signal发送发生错误。Com模块中发送Signal发生错误时，通知到RTE。

Generated when transmission error notification is configured for a Signal in Com. This callback function indicates an error occurred during Signal transmission. When a Signal transmission error occurs in the Com module, RTE is notified.

**Service ID**
   0x91

**Sync/Async**
   Synchronous

**Reentrancy**
   Non Reentrant

**Parameters**
   None

**Return type**
   void

**Return values**
   None

Rte_COMCbkInv_<sn>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: 

   void Rte_COMCbkInv_<sn> (void)

当Com中Signal配置了接收无效通知时生成。这这个回调函数表明Signal收到的值为无效值。Com模块中接收Signal收到无效值时，通知到RTE。

Generated when reception invalid notification is configured for a Signal in Com. This callback function indicates the Signal received an invalid value. When the Com module receives an invalid Signal value, RTE is notified.

**Service ID**
   0x92

**Sync/Async**
   Synchronous

**Reentrancy**
   Non Reentrant

**Parameters**
   None

**Return type**
   void

**Return values**
   None

Rte_COMCbkRxTOut_<sn>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: 

   void Rte_COMCbkRxTOut_<sn> (void)

当Com中Signal配置了接收超时时生成。这个回调函数表明Signal发生了接收超时。Com模块中接收Signal发生超时时，通知到RTE。

Generated when reception timeout is configured for a Signal in Com. This callback function indicates a reception timeout occurred for the Signal. When a Signal reception timeout occurs in the Com module, RTE is notified.

**Service ID**
   0x93

**Sync/Async**
   Synchronous

**Reentrancy**
   Non Reentrant

**Parameters**
   None

**Return type**
   void

**Return values**
   None

Rte_COMCbkTxTOut_<sn>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: 

   void Rte_COMCbkTxTOut_<sn> (void)

当Com中Signal配置了发送超时时生成。这个回调函数表明Signal发生了发送超时。Com模块中发送Signal发生超时时，通知到RTE。

Generated when transmission timeout is configured for a Signal in Com. This callback function indicates a transmission timeout occurred for the Signal. When a Signal transmission timeout occurs in the Com module, RTE is notified.

**Service ID**
   0x94

**Sync/Async**
   Synchronous

**Reentrancy**
   Non Reentrant

**Parameters**
   None

**Return type**
   void

**Return values**
   None

Rte_COMCbk_<sg>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: 

   void Rte_COMCbk_<sg> (void)

当Com中SignalGroup配置了接收通知时生成。这个回调函数表明SignalGroup已经收到最新值。Com模块中接收到SignalGroup时，通知到RTE。

Generated when reception notification is configured for a SignalGroup in Com. This callback function indicates the SignalGroup has received the latest values. When a SignalGroup is received in the Com module, RTE is notified.

**Service ID**
   0x9f

**Sync/Async**
   Synchronous

**Reentrancy**
   Non Reentrant

**Parameters**
   None

**Return type**
   void

**Return values**
   None

Rte_COMCbkTAck_<sg>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: 

   void Rte_COMCbkTAck_<sg> (void)

当Com中SignalGroup配置了发送确认通知时生成。这个回调函数表明SignalGroup已经由Com打包到Pdu中且发送成功。Com模块中发送SignalGroup成功时，通知到RTE。

Generated when transmission acknowledgment notification is configured for a SignalGroup in Com. This callback function indicates the SignalGroup has been packaged into a PDU by Com and sent successfully. When a SignalGroup is successfully transmitted in the Com module, RTE is notified.

**Service ID**
   0x90

**Sync/Async**
   Synchronous

**Reentrancy**
   Non Reentrant

**Parameters**
   None

**Return type**
   void

**Return values**
   None

Rte_COMCbkTErr_<sg>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: 

   void Rte_COMCbkTErr_<sg> (void)

当Com中SignalGroup配置了发送错误通知时生成。这个回调函数表明SignalGroup发送发生错误。Com模块中发送SignalGroup发生错误时，通知到RTE。

Generated when transmission error notification is configured for a SignalGroup in Com. This callback function indicates an error occurred during SignalGroup transmission. When a SignalGroup transmission error occurs in the Com module, RTE is notified.

**Service ID**
   0x91

**Sync/Async**
   Synchronous

**Reentrancy**
   Non Reentrant

**Parameters**
   None

**Return type**
   void

**Return values**
   None

Rte_COMCbkInv_<sg>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: 

   void Rte_COMCbkInv_<sg> (void)

当Com中SignalGroup配置了接收无效通知时生成。这个回调函数表明SignalGroup收到的值为无效值。Com模块中接收SignalGroup收到无效值时，通知到RTE。

Generated when reception invalid notification is configured for a SignalGroup in Com. This callback function indicates the SignalGroup received invalid values. When the Com module receives invalid SignalGroup values, RTE is notified.

**Service ID**
   0x92

**Sync/Async**
   Synchronous

**Reentrancy**
   Non Reentrant

**Parameters**
   None

**Return type**
   void

**Return values**
   None

Rte_COMCbkRxTOut_<sg>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: 

   void Rte_COMCbkRxTOut_<sg> (void)

当Com中SignalGroup配置了接收超时时生成。这个回调函数表明SignalGroup发生了接收超时。Com模块中接收SignalGroup发生超时时，通知到RTE。

Generated when reception timeout is configured for a SignalGroup in Com. This callback function indicates a reception timeout occurred for the SignalGroup. When a SignalGroup reception timeout occurs in the Com module, RTE is notified.

**Service ID**
   0x93

**Sync/Async**
   Synchronous

**Reentrancy**
   Non Reentrant

**Parameters**
   None

**Return type**
   void

**Return values**
   None

Rte_COMCbkTxTOut<sg>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: 

   void Rte_COMCbkTxTOut_<sg> (void)

当Com中SignalGroup配置了发送超时时生成。这个回调函数表明SignalGroup发生了发送超时。Com模块中发送SignalGroup发生超时时，通知到RTE。

Generated when transmission timeout is configured for a SignalGroup in Com. This callback function indicates a transmission timeout occurred for the SignalGroup. When a SignalGroup transmission timeout occurs in the Com module, RTE is notified.

**Service ID**
   0x94

**Sync/Async**
   Synchronous

**Reentrancy**
   Non Reentrant

**Parameters**
   None

**Return type**
   void

**Return values**
   None

Rte_LdComCbkRxIndication_<sn>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: 

   void Rte_LdComCbkRxIndication_<sn> (const PduInfoType* PduInfoPtr )

当LdCom中Signal(IF Pdu)配置了接收通知时生成。这个回调函数为Signal接收时通知。LdCom模块中接收Signal(IF Pdu)时，通知到RTE。

Generated when reception notification is configured for a Signal (IF PDU) in LdCom. This callback function notifies upon Signal reception. When the LdCom module receives a Signal (IF PDU), RTE is notified.

**Service ID**
   0x101

**Sync/Async**
   Synchronous

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
     - PduInfoPtr
     - Signal(IF Pdu)的数据指针(Data pointer of Signal (IF Pdu))
       
       

**Return type**
   void

**Return values**
   None

Rte_LdComCbkTxConfirmation_<sn>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: 

   void Rte_LdComCbkTxConfirmation_<sn> (void)

当LdCom中Signal(IF Pdu)配置了发送确认时生成。这个回调函数表明Signal发送确认。LdCom模块中发送Signal发送确认时，通知到RTE。

Generated when transmission acknowledgment is configured for a Signal (IF PDU) in LdCom. This callback function indicates Signal transmission acknowledgment. When LdCom module confirms Signal transmission, RTE is notified.

**Service ID**
   0xA7

**Sync/Async**
   Synchronous

**Reentrancy**
   Non Reentrant

**Parameters**
   None

**Return type**
   void

**Return values**
   None
   
Rte_LdComCbkCopyRxData_<sn>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: 

   BufReq_ReturnType Rte_LdComCbkCopyRxData_<sn> (
    const PduInfoType* info,
    PduLengthType* bufferSizePtr)


当LdCom中Signal(TP Pdu)配置了接收时生成

Generated when reception is configured for a Signal (TP Pdu) in LdCom

**Service ID**
   0xA2

**Sync/Async**
   Synchronous

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
     - info
     - 提供源buffer和待拷贝的字节数(Provide the source buffer and the number of bytes to be copied)
       
       
	 
   * - [out]
     - bufferSizePtr
     - 剩余字节数(Number of remaining bytes)
       
       

**Return type**
   BufReq_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description

   * - BUFREQ_OK
     - 拷贝OK
       
       Copy OK

   * - BUFREQ_E_NOT_OK
     - 拷贝过程有错误产生导致失败，初始化不成功(An error occurred during the copying process, resulting in failure and unsuccessful initialization)
       
      
   
Rte_LdComCbkCopyTxData_<sn>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: 

   BufReq_ReturnType Rte_LdComCbkCopyTxData_<sn> (
    const PduInfoType* info,
    const RetryInfoType* retry,
    PduLengthType* availableDataPtr)

当LdCom中Signal(TP Pdu)配置了发送时生成

Generated when transmission is configured for a Signal (TP Pdu) in LdCom



**Service ID**
   0xA4

**Sync/Async**
   Synchronous

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
     - info
     - 提供目标buffer和待拷贝的字节数(Provides target buffer and bytes to copy)
	 
   * - [in]
     - retry
     - 不会被LdCom模块及其上层模块处理(Not processed by LdCom module or its upper-layer modules)
	 
   * - [out]
     - availableDataPtr
     - 剩余字节数(Number of remaining bytes)

**Return type**
   BufReq_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description

   * - BUFREQ_OK
     - 数据已被传送(Data has been transmitted)
	 
   * - BUFREQ_E_BUSY
     - 没有数据被传送，请求的发送数量data不可用(No data transmitted; requested data quantity unavailable)
	 
   * - BUFREQ_E_NOT_OK
     - 数据未被传送(Data not transmitted)

Rte_LdComCbkStartOfReception_<sn>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: 

   BufReq_ReturnType Rte_LdComCbkStartOfReception_<sn> (
    const PduInfoType* info,
    PduLengthType TpSduLength,
    PduLengthType* bufferSizePtr)

当LdCom中Signal(TP Pdu)配置了接收时生成

Generated when reception is configured for a Signal (TP Pdu) in LdCom

**Service ID**
   0x102

**Sync/Async**
   Synchronous

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
     - info
     - 第一帧或者单一帧的数据和长度(Data and length of first frame or single frame)
	 
   * - [in]
     - TpSduLength
     - 接收总长度(Total reception length)
	 
   * - [out]
     - bufferSizePtr
     - 可用的接收buffer(Available receive buffer)

**Return type**
   BufReq_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description

   * - BUFREQ_OK
     - 连接建立(Connection established)
	 
   * - BUFREQ_E_NOT_OK
     - 连接拒绝(Connection rejected)
	 
   * - BUFREQ_E_OVFL
     - buffer溢出，连接中断(Buffer overflow, connection interrupted)

Rte_LdComCbkTpRxIndication_<sn>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: 

   void Rte_LdComCbkTpRxIndication_<sn> (
    Std_ReturnType result)

当LdCom中Signal(TP Pdu)配置了接收时生成

Generated when reception is configured for a Signal (TP Pdu) in LdCom

**Service ID**
   0x103

**Sync/Async**
   Synchronous

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
     - result
     - 接收结果(Reception result)
       
       

**Return type**
   void

**Return values**
   None

Rte_LdComCbkTpTxConfirmation_<sn>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: 

   void Rte_LdComCbkTpTxConfirmation_<sn> (
    Std_ReturnType result)

当LdCom中Signal(TP Pdu)配置了发送时生成

Generated when transmission is configured for a Signal (TP Pdu) in LdCom

**Service ID**
   0xA5

**Sync/Async**
   Synchronous

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
     - result
     - 发送结果(Transmission result)
       
       

**Return type**
   void

**Return values**
   None

Indirect(API)
---------------

Rte_Ports_<i>_<R/P/PR>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: 

   Rte_PortHandle_<i>_<R/P/PR> Rte_Ports_<i>_<R/P/PR>([IN Rte_Instance <instance>])

当Port的配置参数indirectAPI(PortAPIOption)为TRUE时生成。获取基于Ports的首个函数指针，供应用调用。应用Runnable中根据实现逻辑进行调用。

Generated when the Port's indirectAPI configuration parameter (PortAPIOption) is TRUE. Retrieves the first function pointer based on Ports for application calls. Application Runnables call this according to implementation logic.

**Service ID**
   0x10

**Sync/Async**
   Synchronous

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
     - instance
     - 实例参数(多实例时存在，单实例时不存在)(Instance parameter (exists for multiple instances, absent for single instance))
       


**Return type**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description

   * - Rte_PortHandle_<i>_<R/P/PR>
     - PDS数组的首指针(First pointer of PDS array)

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description

   * - <return>
     - 返回对应的PDS数组(Returns the corresponding PDS array)



Rte_NPorts_<i>_<R/P/PR>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: 

   uint8 Rte_NPorts_<i>_<R/P/PR>([IN Rte_Instance <instance>])

当Port的配置参数indirectAPI(PortAPIOption)为TRUE时生成。获取对应PortInterface的Port个数。应用Runnable中根据实现逻辑进行调用。

Generated when the Port's indirectAPI configuration parameter (PortAPIOption) is TRUE. Returns the number of Ports for the corresponding PortInterface. Application Runnables call this according to implementation logic.

**Service ID**
   0x11

**Sync/Async**
   Synchronous

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
     - instance
     - 实例参数(多实例时存在，单实例时不存在)(Instance parameter (exists for multiple instances, absent for single instance))

**Return type**
   uint8

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description

   * - <return>
     - 对应PortInterface的Port个数(Number of Ports for the corresponding PortInterface)



Rte_Port_<p>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: 

   Rte_PortHandle_<i>_<R/P/PR> Rte_Port_<p>([IN Rte_Instance <instance>])

当Port的配置参数indirectAPI(PortAPIOption)为TRUE时生成。获取基于Port的函数指针，供应用调用。应用Runnable中根据实现逻辑进行调用。

Generated when the Port's indirectAPI configuration parameter (PortAPIOption) is TRUE. Retrieves the function pointer based on the Port for application calls. Application Runnables call this according to implementation logic.

**Service ID**
   0x12

**Sync/Async**
   Synchronous

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
     - instance
     - 实例参数(多实例时存在，单实例时不存在)(Instance parameter (exists for multiple instances, absent for single instance))

**Return type**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description

   * - Rte_PortHandle_<i>_<R/P/PR>
     - PDS指针(PDS pointer)

**Return values**
   
.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description

   * - <return>
     - 返回基于Port的RTE访问函数的函数指针(Returns the function pointer for Port-based RTE access functions)

      

SR通信(SR Communication)
--------------------------------------

Rte_Write_<p>_<o>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: 

   Std_ReturnType Rte_Write_<p>_<o>([IN Rte_Instance <instance>],IN <data>,[OUT Std_TransformerError transformerError])

SR显式非队列写通信，或者Nv data写操作时生成。实现SR显式非队列通信写操作，或者Nv Data写操作。应用Runnable中根据实现逻辑进行调用。

Generated for SR explicit non-queued write communication or Nv data write operations. Implements SR explicit non-queued write operations or Nv Data write operations. Application Runnables call this according to implementation logic.

**Service ID**
   0x14

**Sync/Async**
   Synchronous

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
     - instance
     - 实例参数(多实例时存在，单实例时不存在)(Instance parameter (exists for multiple instances, absent for single instance))

   * - [in]
     - data
     - SR/Nv写数据(value/reference)(SR/Nv write data (value/reference))
       
       

   * - [out]
     - transformerError
     - 序列化错误参数(Serialization error parameter)
       
       
        

**Return type**
   Std_ReturnType


**Return values**
   
.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description

   * - RTE_E_OK
     - 数据写入调用成功(Data write call successful)

   * - RTE_E_HARD_TRANSFORMER_ERROR
     - 序列化/反序列化硬错误(Serialization/deserialization hard error)

   * - RTE_E_SOFT_TRANSFORMER_ERROR
     - 序列化/反序列化软错误(Serialization/deserialization soft error)

   * - RTE_E_COM_STOPPED
     - 通信模块不可用(ECU间通信)(Communication module unavailable (inter-ECU communication))

Rte_Send_<p>_<o>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: 

   Std_ReturnType Rte_Send_<p>_<o>([IN Rte_Instance <instance>],IN <data>, [OUT Std_TransformerError transformerError])

SR显式队列发送通信时生成，或者Nv data写操作时生成。实现SR显式队列通信发送操作。应用Runnable中根据实现逻辑进行调用。

Generated for SR explicit queued send communication or Nv data write operations. Implements SR explicit queued send operations. Application Runnables call this according to implementation logic.

**Service ID**
   0x13

**Sync/Async**
   Synchronous

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
     - instance
     - 实例参数(多实例时存在，单实例时不存在)(Instance parameter (exists for multiple instances, absent for single instance))

   * - [in]
     - data
     - SR发送数据(value/reference)(SR sending data (value/reference))
       
       

   * - [out]
     - transformerError
     - 序列化错误参数(Serialization error parameter)
         

**Return type**
   Std_ReturnType


**Return values**
   
.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description

   * - RTE_E_OK
     - data写入成功(Data write successful)

   * - RTE_E_LIMIT
     - 队列已满，事件被忽略(仅限ECU内)(Queue full, event discarded (intra-ECU only))

   * - RTE_E_HARD_TRANSFORMER_ERROR
     - 序列化/反序列化硬错误(Serialization/deserialization hard error)

   * - RTE_E_SOFT_TRANSFORMER_ERROR
     - 序列化/反序列化软错误(Serialization/deserialization soft error)

   * - RTE_E_COM_STOPPED
     - 通信模块不可用(ECU间通信)(Communication module unavailable (inter-ECU communication))

Rte_Invalidate_<p>_<o>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: 

   Std_ReturnType Rte_Invalidate_<p>_<o>([IN Rte_Instance <instance>],[OUT Std_TransformerError transformerError])

SR显式非队列写无效值通信，且配置了无效值及无效策略时生成。实现SR显式非队列写无效值通信操作。应用Runnable中根据实现逻辑进行调用。

Generated for SR explicit non-queued invalid value write communication when invalid values and invalid policies are configured. Implements SR explicit non-queued invalid value write operations. Application Runnables call this according to implementation logic.

**Service ID**
   0x16

**Sync/Async**
   Synchronous

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
     - instance
     - 实例参数(多实例时存在，单实例时不存在)(Instance parameter (exists for multiple instances, absent for single instance))

   * - [out]
     - transformerError
     - 序列化错误参数(Serialization error parameter)

**Return type**
   Std_ReturnType


**Return values**
   
.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description

   * - RTE_E_OK
     - 没有错误产生(No error occurred)

   * - RTE_E_HARD_TRANSFORMER_ERROR
     - 序列化/反序列化硬错误(Serialization/deserialization hard error)

   * - RTE_E_SOFT_TRANSFORMER_ERROR
     - 序列化/反序列化软错误(Serialization/deserialization soft error)

   * - RTE_E_COM_STOPPED
     - 通信模块不可用(ECU间通信)(Communication module unavailable (inter-ECU communication))

Rte_Feedback_<p>_<o>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: 

   Std_ReturnType Rte_Feedback_<p>_<o>([IN Rte_Instance <instance>])

SR显式写通信(队列/非队列)，配置发送确认时生成。SR显式写通信(队列/非队列)，发送确认状态获取。应用Runnable中根据实现逻辑进行调用。

Generated for SR explicit write communication (queued/non-queued) when transmission acknowledgment is configured. Obtains transmission acknowledgment status for SR explicit write communication (queued/non-queued). Application Runnables call this according to implementation logic.

**Service ID**
   0x17

**Sync/Async**
   Synchronous

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
     - instance
     - 实例参数(多实例时存在，单实例时不存在)(Instance parameter (exists for multiple instances, absent for single instance))

**Return type**
   Std_ReturnType

**Return values**
   
.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description

   * - RTE_E_NO_DATA
     - 没有收到发送确认也没有收到错误提示(No transmission acknowledgment or error notification received)

   * - RTE_E_TRANSMIT_ACK
     - 发送完成(Transmission completed)

   * - RTE_E_HARD_TRANSFORMER_ERROR
     - 序列化/反序列化硬错误(Serialization/deserialization hard error)

   * - RTE_E_SOFT_TRANSFORMER_ERROR
     - 序列化/反序列化软错误(Serialization/deserialization soft error)

   * - RTE_E_COM_STOPPED
     - 最后一次发送被拒绝或者在超时前收到COM的错误通知(ECU间通信)(Last transmission rejected or COM error notification received before timeout (inter-ECU communication))

   * - RTE_E_TIMEOUT
     - 在错误通知前，产生了超时(分区间或ECU间通信)(Timeout occurred before error notification (inter-partition or inter-ECU communication))

   * - RTE_E_UNCONNECTED
     - 发送端接口未连接(Sender port not connected)

   * - RTE_E_IN_EXCLUSIVE_AREA
     - 仅使用于阻塞型API，指示函数位于独占区中。(For blocking APIs only; indicates function is within exclusive area)

Rte_Read_<p>_<o>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: 

   Std_ReturnType Rte_Read_<p>_<o>([IN Rte_Instance <instance>],OUT <data>,[OUT Std_TransformerError transformerError])

SR显式非队列读，或者Nv data读操作时生成(dataReceivePointByArgument)。实现SR显式非队列通信读操作，或者Nv Data读操作。应用Runnable中根据实现逻辑进行调用。

Generated for SR explicit non-queued read or Nv data read operations (dataReceivePointByArgument). Implements SR explicit non-queued read operations or Nv Data read operations. Application Runnables call this according to implementation logic.

**Service ID**
   0x19

**Sync/Async**
   Synchronous

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
     - instance
     - 实例参数(多实例时存在，单实例时不存在)(Instance parameter (exists for multiple instances, absent for single instance))

   * - [out]
     - data
     - 读数据指针(Read data pointer)
       
       

   * - [out]
     - transformerError
     - 序列化错误参数(Serialization error parameter)

**Return type**
   Std_ReturnType

**Return values**
   
.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description

   * - RTE_E_OK
     - 数据读取成功(Data read successful)

   * - RTE_E_INVALID
     - 收到无效数据(Invalid data received)

   * - RTE_E_HARD_TRANSFORMER_ERROR
     - 序列化/反序列化硬错误(Serialization/deserialization hard error)

   * - RTE_E_SOFT_TRANSFORMER_ERROR
     - 序列化/反序列化软错误(Serialization/deserialization soft error)

   * - RTE_E_COM_STOPPED
     - 通信模块不可用(ECU间通信)(Communication module unavailable (inter-ECU communication))

   * - RTE_E_MAX_AGE_EXCEEDED
     - 数据过时(Data outdated)

   * - RTE_E_UNCONNECTED
     - 接收端接口未连接(Receiver port not connected)

   * - RTE_E_NEVER_RECEIVED
     - 自从系统启动后，就未接收到数据(No data received since system startup)

Rte_DRead_<p>_<o>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: 

   <return> Rte_DRead_<p>_<o>([IN Rte_Instance <instance>])

SR显式非队列读，或者Nv data读操作时生成(dataReceivePointByValue)。实现SR显式非队列通信读操作，或者Nv Data读操作。应用Runnable中根据实现逻辑进行调用。

Generated for SR explicit non-queued read or Nv data read operations (dataReceivePointByValue). Implements SR explicit non-queued read operations or Nv Data read operations. Application Runnables call this according to implementation logic.

**Service ID**
   0x1A

**Sync/Async**
   Synchronous

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
     - instance
     - 实例参数(多实例时存在，单实例时不存在)(Instance parameter (exists for multiple instances, absent for single instance))

**Return type**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description

   * - <return>
     - SR显式非队列/Nv data的读数据类型(The read data type of SR explicit non-queued/Nv data)
       
  

**Return values**
   
.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description

   * - <return>
     - 返回SR显式非队列/Nv data的读数据值(Return the read data type of SR explicit non-queued/Nv data)



Rte_Receive_<p>_<o>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: 

   Std_ReturnType Rte_Receive_<p>_<o>([IN Rte_Instance <instance>],OUT <data>,[OUT Std_TransformerError transformerError])

SR显式非队列读，或者Nv data读操作时生成(dataReceivePointByValue)。实现SR显式队列通信接收操作。应用Runnable中根据实现逻辑进行调用。

Generated for SR explicit non-queued read or Nv data read operations (dataReceivePointByValue). Implements SR explicit queued communication receive operations. Application Runnables call this according to implementation logic.

**Service ID**
   0x1B

**Sync/Async**
   Synchronous

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
     - instance
     - 实例参数(多实例时存在，单实例时不存在)(Instance parameter (exists for multiple instances, absent for single instance))

   * - [out]
     - data
     - 读数据指针(Read data pointer)
       
       

   * - [out]
     - transformerError
     - 序列化错误参数(Serialization error parameter)

**Return type**
   Std_ReturnType

**Return values**
   
.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description

   * - RTE_E_OK
     - 数据读取成功(Data read successful)

   * - RTE_E_NO_DATA
     - 非阻塞型读取中，读取数据时，没有接收到事件且没有错误产生(No events received and no errors occurred during non-blocking read)

   * - RTE_E_HARD_TRANSFORMER_ERROR
     - 序列化/反序列化硬错误(Serialization/deserialization hard error)

   * - RTE_E_SOFT_TRANSFORMER_ERROR
     - 序列化/反序列化软错误(Serialization/deserialization soft error)

   * - RTE_E_LOST_DATA
     - 队列已满导致的数据丢失(Data lost due to full queue)

   * - RTE_E_TIMEOUT
     - 阻塞型读取中，读取数据时，没有接收到事件且没有错误产生(No events received and no errors occurred during blocking read)

   * - RTE_E_UNCONNECTED
     - 接收端接口未连接(Receiver port not connected)

   * - RTE_E_IN_EXCLUSIVE_AREA
     - 仅使用于阻塞型API，指示函数位于独占区中。(For blocking APIs only; indicates function is within exclusive area)

Rte_IRead_<re>_<p>_<o>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: 

   <return> Rte_IRead_<re>_<p>_<o>([IN Rte_Instance <instance>])

SR隐式读，或者Nv data隐式读时生成。实现SR隐式读，或者Nv data隐式读通信操作。应用Runnable中根据实现逻辑进行调用。

Generated for SR implicit read or Nv data implicit read. Implements SR implicit read or Nv data implicit read communication operations. Application Runnables call this according to implementation logic.



**Service ID**
   0x21

**Sync/Async**
   Synchronous

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
     - instance
     - 实例参数(多实例时存在，单实例时不存在)(Instance parameter (exists for multiple instances, absent for single instance))

**Return type**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description

   * - <return>
     - SR隐式读数据类型(SR implicit read data type)
       


**Return values**
   
.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description

   * - <return>
     - 返回SR隐式读数据值(Returns SR implicit read data value)

       

Rte_IWrite_<re>_<p>_<o>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: 

   void Rte_IWrite_<re>_<p>_<o>([IN Rte_Instance <instance>],IN <data>)

SR隐式写，或者Nv data隐式写时生成。实现SR隐式写，或者Nv data隐式写数据操作。应用Runnable中根据实现逻辑进行调用。

Generated for SR implicit write or Nv data implicit write. Implements SR implicit write or Nv data implicit write operations. Application Runnables call this according to implementation logic.

**Service ID**
   0x22

**Sync/Async**
   Synchronous

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
     - instance
     - 实例参数(多实例时存在，单实例时不存在)(Instance parameter (exists for multiple instances, absent for single instance))

   * - [in]
     - data
     - SR写数据(value/reference)(SR write data (value/reference))
       
       

**Return type**
   void

**Return values**
   None

Rte_IWriteRef_<re>_<p>_<o>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: 

   <return reference> Rte_IWriteRef_<re>_<p>_<o>([IN Rte_Instance <instance>])

SR隐式写，或者Nv data隐式写时生成。实现SR隐式写，或者Nv data隐式写数据操作(返回写数据指针，应用对其进行赋值)。应用Runnable中根据实现逻辑进行调用。

Generated for SR implicit write or Nv data implicit write. Implements SR implicit write or Nv data implicit write operations (returns write data pointer for application assignment). Application Runnables call this according to implementation logic.

**Service ID**
   0x23

**Sync/Async**
   Synchronous

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
     - instance
     - 实例参数(多实例时存在，单实例时不存在)(Instance parameter (exists for multiple instances, absent for single instance))

**Return type**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description

   * - <return reference>
     - 写数据类型指针(write data pointer)
       
       

**Return values**
   
.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description

   * - <return reference>
     - 返回写数据类型指针(Returns write data pointer.)

       

Rte_IInvalidate_<re>_<p>_<o>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: 

   void Rte_IInvalidate_<re>_<p>_<o>([IN Rte_Instance <instance>])

SR显式写通信，且配置了无效值及无效策略时生成。实现SR隐式写无效值通信。应用Runnable中根据实现逻辑进行调用。

Generated for SR explicit write communication with invalid values and invalid policies configured. Implements SR implicit write invalid value communication. Application Runnables call this according to implementation logic.

**Service ID**
   0x24

**Sync/Async**
   Synchronous

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
     - instance
     - 实例参数(多实例时存在，单实例时不存在)(Instance parameter (exists for multiple instances, absent for single instance))

**Return type**
   void

**Return values**
   None

Rte_IStatus_<re>_<p>_<o>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: 

   Std_ReturnType Rte_IStatus_<re>_<p>_<o>([IN Rte_Instance <instance>],[OUT Std_TransformerError transformerError])

SR隐式读通信，且满足接收状态条件时生成。实现SR隐式读状态获取操作。应用Runnable中根据实现逻辑进行调用。
  
Generated for SR implicit read communication when reception status conditions are met. Implements SR implicit read status acquisition operations. Application Runnables call this according to implementation logic.

**Service ID**
   0x25

**Sync/Async**
   Synchronous

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
     - instance
     - 实例参数(多实例时存在，单实例时不存在)(Instance parameter (exists for multiple instances, absent for single instance))

   * - [out]
     - transformerError
     - 序列化错误参数(Serialization error parameter)

**Return type**
   Std_ReturnType


**Return values**
   
.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description

   * - RTE_E_OK
     - 无错误产生(No errors occurred)

   * - RTE_E_INVALID
     - 数据无效(Data invalid)

   * - RTE_E_HARD_TRANSFORMER_ERROR
     - 序列化/反序列化硬错误(Serialization/deserialization hard error)

   * - RTE_E_SOFT_TRANSFORMER_ERROR
     - 序列化/反序列化软错误(Serialization/deserialization soft error)

   * - RTE_E_COM_STOPPED
     - 通信模块不可用(ECU间通信)(Communication module unavailable (inter-ECU communication))

   * - RTE_E_NEVER_RECEIVED
     - 自系统启动就未收到数据(No data received since system startup)

   * - RTE_E_UNCONNECTED
     - 接收端接口未连接(Receiver port not connected)

   * - RTE_E_MAX_AGE_EXCEEDED
     - 数据过时(Data outdated)

Rte_IFeedback_<re>_<p>_<o>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: 

   Std_ReturnType Rte_IFeedback_<re>_<p>_<o>([IN RTE_Instance <instance>])

SR隐式写通信且配置了发送确认时生成。实现SR隐式写通信发送确认状态获取。应用Runnable中根据实现逻辑进行调用。

Generated for SR implicit write communication with transmission acknowledgment configured. Implements SR implicit write communication transmission acknowledgment status acquisition. Application Runnables call this according to implementation logic.

**Service ID**
   0x2F

**Sync/Async**
   Synchronous

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
     - instance
     - 实例参数(多实例时存在，单实例时不存在)(Instance parameter (exists for multiple instances, absent for single instance))

   * - [out]
     - transformerError
     - 序列化错误参数(Serialization error parameter)

**Return type**
   Std_ReturnType


**Return values**
   
.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description

   * - RTE_E_NO_DATA
     - 函数启动后，没有收到发送确认或者错误通知。(No transmission acknowledgment or error notification received after function start)

   * - RTE_E_HARD_TRANSFORMER_ERROR
     - 序列化/反序列化硬错误(Serialization/deserialization hard error)

   * - RTE_E_SOFT_TRANSFORMER_ERROR
     - 序列化/反序列化软错误(Serialization/deserialization soft error)

   * - RTE_E_COM_STOPPED
     - 最后一个发送被拒绝(ECU间通信)(Last transmission rejected (inter-ECU communication))

   * - RTE_E_TIMEOUT
     - 发送超时(ECU间通信)(Transmission timeout (inter-ECU communication))

   * - RTE_E_UNCONNECTED
     - 客户端接口未连接(Client port not connected)

   * - RTE_E_TRANSMIT_ACK
     - 收到发送确认(Transmission acknowledgment received)

Rte_IsUpdated_<p>_<o>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: 

   boolean Rte_IsUpdated_<p>_<o>([IN RTE_Instance <instance>])

SR显式非队列读通信且使能了更新机制时生成。实现SR显式非队列读通信更新状态获取。应用Runnable中根据实现逻辑进行调用。

Generated for SR explicit non-queued read communication with update mechanism enabled. Implements SR explicit non-queued read communication update status acquisition. Application Runnables call this according to implementation logic.

**Service ID**
   0x30

**Sync/Async**
   Synchronous

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
     - instance
     - 实例参数(多实例时存在，单实例时不存在)(Instance parameter (exists for multiple instances, absent for single instance))

   * - [out]
     - transformerError
     - 序列化错误参数(Serialization error parameter)

**Return type**
   boolean


**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description

   * - TRUE
     - 自上次读完后，数据已被更新(Data updated since last read)

       

   * - FALSE
     - 自上次读完后，数据还未被更新(Data not updated since last read)

       

CS通信(CS Communication)
------------------------------------

Rte_Call_<p>_<o>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: 

   Std_ReturnType Rte_Call_<p>_<o>([IN Rte_Instance <instance>],[IN|IN/OUT|OUT] <data_1>,...[IN|IN/OUT|OUT] <data_n>,[OUT Std_TransformerError transformerError])

CS同步/异步访问时生成。实现CS同步/异步服务请求通信(异步无OUT参数)。应用Runnable中根据实现逻辑进行调用。

Generated for CS synchronous/asynchronous access. Implements CS synchronous/asynchronous service request communication (asynchronous without OUT parameters). Application Runnables call this according to implementation logic.

**Service ID**
   0x1C

**Sync/Async**
   Synchronous/Asynchronous

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
     - instance
     - 实例参数(多实例时存在，单实例时不存在)(Instance parameter (exists for multiple instances, absent for single instance))

   * - [in|in/out|out]
     - data_1
     - CS函数参数(CS function parameters)
       
       

   * - [in|in/out|out]
     - data_n
     - CS函数参数(CS function parameters)

   * - [out]
     - transformerError
     - 序列化错误参数(Serialization error parameter)

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description

   * - RTE_E_OK
     - API调用成功(API call successful)

   * - RTE_E_LIMIT
     - 达到最大并发数，无法处理新的请求，该次请求被拒绝，返回参数的缓冲区未被修改(Maximum concurrency reached; request rejected; return parameter buffers unmodified)

   * - RTE_E_HARD_TRANSFORMER_ERROR
     - 序列化/反序列化硬错误(Serialization/deserialization hard error)

   * - RTE_E_SOFT_TRANSFORMER_ERROR
     - 序列化/反序列化软错误(Serialization/deserialization soft error)

   * - RTE_E_COM_STOPPED
     - 通信模块不可用(ECU间通信)(Communication module unavailable (inter-ECU communication))

   * - RTE_E_TIMEOUT
     - 服务请求超时(任务间或ECU间通信)(Service request timeout (inter-task or inter-ECU communication))

   * - RTE_E_UNCONNECTED
     - 客户端接口未连接(Client port not connected)

   * - RTE_E_IN_EXCLUSIVE_AREA
     - 阻塞API调用时，调用方处于独占区内(Caller in exclusive area during blocking API call)

   * - RTE_E_TIMEOUT
     - RTE未初始化完成(RTE not fully initialized)

Rte_Result_<p>_<o>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: 

   Std_ReturnType Rte_Result_<p>_<o>([IN Rte_Instance <instance>],[IN/OUT|OUT <param 1>],...,[IN/OUT|OUT <param n>],[OUT Std_TransformerError transformerError])

CS异步通信获取结果时生成。实现CS异步通信获取服务结果。应用Runnable中根据实现逻辑进行调用。
 
Generated for obtaining results from CS asynchronous communication. Implements CS asynchronous communication result retrieval. Application Runnables call this according to implementation logic.

**Service ID**
   0x1D

**Sync/Async**
   Synchronous

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
     - instance
     - 实例参数(多实例时存在，单实例时不存在)(Instance parameter (exists for multiple instances, absent for single instance))

   * - [in|in/out|out]
     - param 1
     - CS函数参数(CS function parameters)

   * - [in|in/out|out]
     - param n
     - CS函数参数(CS function parameters)

   * - [out]
     - transformerError
     - 序列化错误参数(Serialization error parameter)

**Return type**
   Std_ReturnType


**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description

   * - RTE_E_OK
     - API调用成功(API call successful)

   * - RTE_E_LIMIT
     - 达到最大并发数，无法处理新的请求，该次请求被拒绝，返回参数的缓冲区未被修改(Maximum concurrency reached; request rejected; return parameter buffers unmodified)

   * - RTE_E_HARD_TRANSFORMER_ERROR
     - 序列化/反序列化硬错误(Serialization/deserialization hard error)

   * - RTE_E_SOFT_TRANSFORMER_ERROR
     - 序列化/反序列化软错误(Serialization/deserialization soft error)

   * - RTE_E_COM_STOPPED
     - 通信模块不可用(ECU间通信)(Communication module unavailable (inter-ECU communication))

   * - RTE_E_TIMEOUT
     - 服务请求超时(任务间或ECU间通信)(Service request timeout (inter-task or inter-ECU communication))

   * - RTE_E_UNCONNECTED
     - 客户端接口未连接(Client port not connected)

   * - RTE_E_IN_EXCLUSIVE_AREA
     - 阻塞API调用时，调用方处于独占区内(Caller in exclusive area during blocking API call)

   * - RTE_E_TIMEOUT
     - RTE未初始化完成(RTE not fully initialized)

   * - RTE_E_NO_DATA
     - Server端结果不可用(Server result unavailable)

模式管理(Mode Management)
---------------------------

Rte_Switch_<p>_<o>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: 

   Std_ReturnType Rte_Switch_<p>_<o>([IN Rte_Instance <instance>],IN <mode>)

配置模式切换请求(ModeSwitchPoint)时生成。实现模式切换请求。应用Runnable中根据实现逻辑进行调用。

Generated when mode switch request (ModeSwitchPoint) is configured. Implements mode switch request operations. Application Runnables call this according to implementation logic.

**Service ID**
   0x15

**Sync/Async**
   Asynchronous

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
     - instance
     - 实例参数(多实例时存在，单实例时不存在)(Instance parameter (exists for multiple instances, absent for single instance))

   * - [in]
     - mode
     - 切换的目标模式(Target mode for switching)
       
       

**Return type**
   Std_ReturnType


**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - RTE_E_OK
     - 模式切换发送成功(Mode switch sent successfully)
	 
   * - RTE_E_LIMIT 
     - 模式切换队列满，或RTE未启动(Mode switch queue full, or RTE not started)
	 
 
Rte_SwitchAck_<p>_<o>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: 

   Std_ReturnType Rte_SwitchAck_<p>_<o>([IN Rte_Instance <instance>])

配置模式切换确认请求(ModeSwitchedAckRequest)时生成。获取当前模式请求的执行状态。应用Runnable中根据实现逻辑进行调用。

Generated when mode switch acknowledgment request (ModeSwitchedAckRequest) is configured. Retrieves execution status of current mode request. Application Runnables call this according to implementation logic.

**Service ID**
   0x18

**Sync/Async**
   Synchronous

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
     - instance
     - 实例参数(多实例时存在，单实例时不存在)(Instance parameter (exists for multiple instances, absent for single instance))

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
	 
   * - RTE_E_NO_DATA (non-blocking read)
     - 模式切换正在切换中(非阻塞Rte_SwitchAck)(Mode switch in progress (non-blocking Rte_SwitchAck))
	 
   * - RTE_E_TIMEOUT
     - 模式切换超时(Mode switch timeout)
	 
   * - RTE_E_TRANSMIT_ACK
     - 模式切换完成(Mode switch completed)
	 
   * - RTE_E_UNCONNECTED
     - 模式切换端口未连接(Mode switch port not connected)
	 
   * - RTE_E_IN_EXCLUSIVE_AREA
     - Runnable正在独占区中，拒绝阻塞式Rte_SwitchAck执行(Runnable in exclusive area; blocking Rte_SwitchAck rejected)
 
Rte_Mode_<p>_<o>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: 

   标准模式：(Standard mode)
   <return> Rte_Mode_<p>_<o>([IN Rte_Instance <instance>])
   增强模式：(Enhanced mode)
   <return> Rte_Mode_<p>_<o>([IN Rte_Instance <instance>],OUT <previousmode>,OUT <nextmode>)

当配置模式访问(ModeAccessPoint)，增强模式(enhancedModeApi)配置为false生成标准接口，增加模式(enhancedModeApi)配置为true生成增强接口。
实现当前模式的获取(增强模式下，还要获取前模式和后模式)。应用Runnable中根据实现逻辑进行调用。

Generated when mode access (ModeAccessPoint) is configured. Standard interface generated when enhancedModeApi is false; enhanced interface generated when enhancedModeApi is true.
Implements current mode acquisition (in enhanced mode, also acquires previous and next modes). Application Runnables call this according to implementation logic.

**Service ID**
   0x2C

**Sync/Async**
   Synchronous

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
     - instance
     - 实例参数(多实例时存在，单实例时不存在)(Instance parameter (exists for multiple instances, absent for single instance))

   * - [out]
     - previousmode
     - 前一个模式(增强模式下才存在)( Previous mode (exists only in enhanced mode))
       
      

   * - [out]
     - nextmode
     - 下一个模式(增强模式下才存在)(Next mode (exists only in enhanced mode))
       
       

**Return type**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description

   * - <return> 
     - 返回当前模式(Returns the current mode)
       
       

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - RTE_TRANSITION_<ModeDeclarationGroup> 
     - 模式切换正在切换中(Mode switch in progress)
	 
   * - RTE_MODE_<ModeDeclarationGroup>_<ModeDeclaration> 
     - 当前模式(Current mode)

PIM实例内存访问(PIM Instance Memory Access)
-------------------------------------------------

Rte_Pim_<name>
~~~~~~~~~~~~~~~~~~~~

.. code:: 

   <type>/<return reference> Rte_Pim_<name>([IN Rte_Instance <instance>])

配置实例内存(PerInstanceMemory或者arTypedPerInstanceMemory)时生成。实现PIM内存地址获取。应用Runnable中根据实现逻辑进行调用。

Generated when instance memory (PerInstanceMemory or arTypedPerInstanceMemory) is configured. Implements PIM memory address acquisition. Application Runnables call this according to implementation logic.

**Service ID**
   0x1E

**Sync/Async**
   Synchronous

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
     - instance
     - 实例参数(多实例时存在，单实例时不存在)(Instance parameter (exists for multiple instances, absent for single instance))

**Return type**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description

   * - <type>/<return reference>
     - PerInstanceMemory时为type，arTypedPerInstanceMemory时为return   reference(type for PerInstanceMemory, return reference for arTypedPerInstanceMemory)


**Return values**
   
.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description

   * - <type>/<return reference>
     - 返回PIM内存地址(Returns PIM memory address)

       

标定数据访问(Calibration Data Access)
---------------------------------------------

Rte_CData_<name>
~~~~~~~~~~~~~~~~~~~~

.. code:: 

   <return> Rte_CData_<name>([IN Rte_Instance <instance>])

当配置访问内部标定参数(perInstanceParameter or sharedParameter)时生成。实现组件内部标定参数获取。应用Runnable中根据实现逻辑进行调用。

Generated when accessing internal calibration parameters (perInstanceParameter or sharedParameter) is configured. Implements component internal calibration parameter acquisition. Application Runnables call this according to implementation logic.

**Service ID**
   0x1F

**Sync/Async**
   Synchronous

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
     - instance
     - 实例参数(多实例时存在，单实例时不存在)(Instance parameter (exists for multiple instances, absent for single instance))

**Return type**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description

   * - <return>
     - 标定参数值类型(Calibration parameter value type)
       

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description

   * - <return>
     - 返回标定参数值(Returns the value of calibration parameter )

       

Rte_Prm_<p>_<o>
~~~~~~~~~~~~~~~~~~~~

.. code:: 

   <return> Rte_Prm_<p>_<o>([IN Rte_Instance <instance>])

配置访问RPort获取标定参数时生成。实现基于Port的标定参数获取。应用Runnable中根据实现逻辑进行调用。

Generated when accessing calibration parameters via RPort is configured. Implements port-based calibration parameter acquisition. Application Runnables call this according to implementation logic.

**Service ID**
   0x20

**Sync/Async**
   Synchronous

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
     - instance
     - 实例参数(多实例时存在，单实例时不存在)(Instance parameter (exists for multiple instances, absent for single instance))

**Return type**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description

   * - <return>
     - 返回标定参数值类型，复合数据类型则返回其指针(Returns parameter value type; returns pointer for composite data types)

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description

   * - <return>
     - 返回标定参数值(Returns the value of calibration parameter )


IRV通信(IRV Communication)
---------------------------------

Rte_IrvIRead_<re>_<o>
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: 

   <return> Rte_IrvIRead_<re>_<o>([IN RTE_Instance <instance>])

当配置组件内部读取隐式IRV(implicitInterRunnableVariable)数据时生成。实现组件内部隐式IRV数据的读取。应用Runnable中根据实现逻辑进行调用。

Generated when reading implicit IRV (implicitInterRunnableVariable) data within the component is configured. Implements reading of component internal implicit IRV data. Application Runnables call this according to implementation logic.

**Service ID**
   0x26

**Sync/Async**
   Synchronous

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
     - instance
     - 实例参数(多实例时存在，单实例时不存在)(Instance parameter (exists for multiple instances, absent for single instance))

**Return type**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description

   * - <return>
     - 对应的IRV的实现数据类型(Corresponding IRV implementation data type)




**Return values**
   
.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description

   * - <return>
     - 返回组件内IRV变量值或地址(Returns IRV variable value or address within component)

Rte_IrvIWrite_<re>_<o>
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: 

   void Rte_IrvIWrite_<re>_<o>([IN RTE_Instance <instance>],IN <data>)

当配置组件内部写隐式IRV(implicitInterRunnableVariable)数据时生成。实现组件内部隐式IRV数据的写操作。应用Runnable中根据实现逻辑进行调用。

Generated when writing implicit IRV (implicitInterRunnableVariable) data within the component is configured. Implements writing of component internal implicit IRV data. Application Runnables call this according to implementation logic.

**Service ID**
   0x27

**Sync/Async**
   Synchronous

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
     - instance
     - 实例参数(多实例时存在，单实例时不存在)(Instance parameter (exists for multiple instances, absent for single instance))

   * - [in]
     - data
     - 希望写入的IRV数据(IRV data to be written)

**Return type**
   void

**Return values**
   None

Rte_IrvIWriteRef_<re>_<o>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: 

   <return reference> Rte_IrvIWriteRef_<re>_<o>([IN RTE_Instance <instance>])

当配置组件内部写隐式IRV(implicitInterRunnableVariable)数据时生成。实现隐式IRV变量地址的获取，供应用对地址进行写值操作。应用Runnable中根据实现逻辑进行调用。

Generated when writing implicit IRV (implicitInterRunnableVariable) data within the component is configured. Implements implicit IRV variable address acquisition for application write operations. Application Runnables call this according to implementation logic.

**Service ID**
   0x31

**Sync/Async**
   Synchronous

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
     - instance
     - 实例参数(多实例时存在，单实例时不存在)(Instance parameter (exists for multiple instances, absent for single instance))

**Return type**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description

   * - return reference
     - 对应的IRV的实现数据类型(Corresponding IRV implementation data type)

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description

   * - return reference
     - 返回IRV变量地址(Returns the address of the IRV variable)
   
       

Rte_IrvRead_<re>_<o>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: 
   
   primitive(VALUE)数据类型：(For primitive (VALUE) data types)
   <return> Rte_IrvRead_<re>_<o>([IN RTE_Instance <instance>])
   complex数据类型：(For complex data types)
   void Rte_[<Byps>_]IrvRead_<re>_<o>([IN RTE_Instance <instance>],OUT <data>)

配置组件内部显式读IRV(explicitInterRunnableVariable)数据时生成。实现组件内部显式IRV数据的读取。应用Runnable中根据实现逻辑进行调用。

Generated when reading explicit IRV (explicitInterRunnableVariable) data within the component is configured. Implements reading of component internal explicit IRV data. Application Runnables call this according to implementation logic.

**Service ID**
   0x28

**Sync/Async**
   Synchronous

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
     - instance
     - 实例参数(多实例时存在，单实例时不存在)(Instance parameter (exists for multiple instances, absent for single instance))

   * - [out]
     - data
     - 读取IRV数据的指针(complex数据类型时才存在)(Pointer to read IRV data (exists only for complex data types))

**Return type**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description

   * - return
     - 对应的IRV的实现数据类型(primitive数据类型时才存在)(Corresponding IRV implementation data type (exists only for primitive data types))

**Return values**
   
.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description

   * - return
     - 返回IRV数据(primitive数据类型时才存在)(Returns IRV data (exists only for primitive data types))

Rte_IrvWrite_<re>_<o>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: 
   
   void Rte_IrvWrite_<re>_<o>([IN RTE_Instance <instance>],IN <data>)

配置组件内部显式写IRV(explicitInterRunnableVariable)数据时生成。实现组件内部显式IRV数据的写操作。应用Runnable中根据实现逻辑进行调用。

Generated when writing explicit IRV (explicitInterRunnableVariable) data within the component is configured. Implements writing of component internal explicit IRV data. Application Runnables call this according to implementation logic.

**Service ID**
   0x29

**Sync/Async**
   Synchronous

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
     - instance
     - 实例参数(多实例时存在，单实例时不存在)(Instance parameter (exists for multiple instances, absent for single instance))

   * - [in]
     - data
     - 写入的IRV数据(IRV data to be written)
       
       

**Return type**
   void

**Return values**
   None

独占区保护(Exclusive Area Protection)
---------------------------------------------

Rte_Enter_[<re>_]<name>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: 
   
   void Rte_Enter_[<re>_]<name>([IN Rte_Instance <instance>])

当配置使用独占区canEnterExclusiveArea时生成。实现进入独占区的接口，供应用Runnable使用。应用Runnable中根据实现逻辑进行调用。

Generated when exclusive area canEnterExclusiveArea is configured. Implements exclusive area entry interface for application Runnables. Application Runnables call this according to implementation logic.

**Service ID**
   0x2A

**Sync/Async**
   Synchronous

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
     - instance
     - 实例参数(多实例时存在，单实例时不存在)(Instance parameter (exists for multiple instances, absent for single instance))

**Return type**
   void

**Return values**
   None

Rte_Exit_[<re>_]<name>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: 
   
   void Rte_Exit_[<re>_]<name>([IN Rte_Instance <instance>])

当配置使用独占区canEnterExclusiveArea时生成。实现退出独占区的接口，供应用Runnable使用。应用Runnable中根据实现逻辑进行调用。

Generated when exclusive area canEnterExclusiveArea is configured. Implements exclusive area exit interface for application Runnables. Application Runnables call this according to implementation logic.

**Service ID**
   0x2B

**Sync/Async**
   Synchronous

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
     - instance
     - 实例参数(多实例时存在，单实例时不存在)(Instance parameter (exists for multiple instances, absent for single instance))

**Return type**
   void

**Return values**
   None

内外部触发(Internal and External Triggering)
-----------------------------------------------------

Rte_Trigger_<p>_<o>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: 

   非队列：(Non-queued)
   void Rte_Trigger_<p>_<o>([IN Rte_Instance <instance>])
   队列： (Queued)
   Std_ReturnType Rte_Trigger_<p>_<o>([IN Rte_Instance <instance>])

当配置了外部触发(ExternalTriggeringPoint)时生成。实现外部触发Runnable，供应用使用。应用Runnable中根据实现逻辑进行调用。

Generated when external trigger (ExternalTriggeringPoint) is configured. Implements external Runnable triggering for application use. Application Runnables call this according to implementation logic.

**Service ID**
   0x2D

**Sync/Async**
   Synchronous

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
     - instance
     - 实例参数(多实例时存在，单实例时不存在)(Instance parameter (exists for multiple instances, absent for single instance))

**Return type**
   void/Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - RTE_E_OK
     - The trigger was successfully queued
   * - RTE_E_LIMIT
     -  The trigger was not queued because the maximum queue size is already reached.

Rte_IrTrigger_<re>_<o>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: 

   非队列：(Queue)
   void Rte_IrTrigger_<re>_<o>([IN Rte_Instance <instance>])
   队列： (Non-queue)
   Std_ReturnType Rte_IrTrigger_<re>_<o>([IN Rte_Instance <instance>])

当Port的配置参数indirectAPI(PortAPIOption)为TRUE时生成。实现内部触发Runnable，供应用使用。应用Runnable中根据实现逻辑进行调用。

Generated when the Port's indirectAPI configuration parameter (PortAPIOption) is TRUE. Implements internal Runnable triggering for application use. Application Runnables call this according to implementation logic.

**Service ID**
   0x2E

**Sync/Async**
   Synchronous

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
     - instance
     - 实例参数(多实例时存在，单实例时不存在)(Instance parameter (exists for multiple instances, absent for single instance))

**Return type**
   void/Std_ReturnType


**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - RTE_E_OK
     - The trigger was successfully queued
   * - RTE_E_LIMIT
     -  The trigger was not queued because the maximum queue size is already reached.

SchM
-----------

SchM实现AUTOSAR BSW模块MainFunction主函数的调度，为BSW模块提供独占区接口服务，为BSW模块间实现跨分区函数调用提供CS接口。
所有SchM接口均与应用无关，只适配BSW的实现逻辑。故只列出实现的接口清单，不对其进行详细描述。

SchM schedules AUTOSAR BSW module MainFunction execution, provides exclusive area interfaces for BSW modules, and implements CS interfaces for cross-partition function calls between BSW modules.
All SchM interfaces are application-independent and adapt solely to BSW implementation logic. Therefore, only the interface list is provided without detailed descriptions.

.. table::

   +-----------------+---------------------+
   |                 |                     |
   | 功能分类        | 接口名              |
   +-----------------+---------------------+
   |                 |                     |
   |                 | SchM_Init           |
   |                 +---------------------+
   |                 |                     |
   |                 | SchM_Start          |
   | 生成周期函数    +---------------------+
   |                 |                     |
   |                 | SchM_StartTiming    |
   |                 +---------------------+
   |                 |                     |
   |                 | SchM_Deinit         |
   +-----------------+---------------------+
   |                 |                     |
   |                 | SchM_Enter          |
   | 独占区          +---------------------+
   |                 |                     |
   |                 | SchM_Exit           |
   +-----------------+---------------------+
   |                 |                     |
   | CS同步通信      | SchM_Call           |
   +-----------------+---------------------+
   |                 |                     |
   |                 | SchM_Switch         |
   |                 +---------------------+
   |  模式管理       |                     |
   |                 | SchM_SwitchAck      |
   |                 +---------------------+
   |                 |                     |
   |                 | SchM_Mode           |
   +-----------------+---------------------+

+-----------------+---------------------+
| Function        | Interface Name      |
| Category        |                     |
+=================+=====================+
|                 | SchM_Init           |
|                 +---------------------+
|                 | SchM_Start          |
| Periodic        +---------------------+
| Function        | SchM_StartTiming    |
| Generation      +---------------------+
|                 | SchM_Deinit         |
+-----------------+---------------------+
| Exclusive       | SchM_Enter          |
| Area            +---------------------+
|                 | SchM_Exit           |
+-----------------+---------------------+
| CS Synchronous  | SchM_Call           |
| Communication   |                     |
+-----------------+---------------------+
|                 | SchM_Switch         |
|                 +---------------------+
| Mode            | SchM_SwitchAck      |
| Management      +---------------------+
|                 | SchM_Mode           |
+-----------------+---------------------+   