====================
CanTp
====================

文档信息(Document Information)
=======================================

版本历史(Version History)
-----------------------------------

.. list-table::
   :widths: 10 10 10 10 20
   :header-rows: 1

   * - 日期(Date)
     - 作者(Author)
     - 版本(Version)
     - 状态(Status)
     - 说明(Description)
   * - 2025/03/05
     - xue.han
     - V0.1
     - 发布(Release)
     - 首次发布(Initial release)
   * - 2025/04/04
     - xue.han
     - V1.0
     - 发布(Release)
     - 正式发布(Official release)


参考文档(References)
----------------------------------

.. list-table::
   :widths: 10 15 20 10
   :header-rows: 1

   * - 编号(Number)
     - 分类(Classification)
     - 标题(Title)
     - 版本(Version)
   * - 1
     - Autosar
     - AUTOSAR_CP_SRS_CAN.pdf
     - R23-11
   * - 2
     - Autosar
     - AUTOSAR_CP_SWS_BSWGeneral.pdf
     - R23-11
   * - 3
     - Autosar
     - AUTOSAR_CP_SWS_PDURouter.pdf
     - R23-11
   * - 4
     - Autosar
     - AUTOSAR_CP_SWS_CANInterface.pdf
     - R23-11
   * - 5
     - Autosar
     - AUTOSAR_CP_SRS_BSWGeneral.pdf
     - R23-11
   * - 6
     - Autosar
     - ISO15765-2-2016.pdf
     - R23-11


术语与简写(Terms and Abbreviations)
========================================


术语(Terms)
---------------------
   .. :align: center   表格内容居中(Table contents are centered)


.. list-table::
   :widths: 20 30
   :header-rows: 1

   * - 术语(Term)
     - 解释(Explanation)
   * - Extended addressing format
     - 扩展寻址格式(Extended addressing format)
   * - Functional addressing
     - 功能寻址(Functional addressing)
   * - Mixed addressing format
     - 混合寻址格式(Mixed addressing format)
   * - Multiple connection
     - 多个传输协议通信会话(Multiple transport protocol communication sessions)
   * - Normal addressing format
     - 正常寻址格式 (Normal addressing)
   * - Physical addressing
     - 物理寻址(Physical addressing)
   * - Single connection
     - 单个传输协议通信会话(single transport protocol communication session)
   * - Connection channel
     - 传输协议通信会话通道(Transport protocol communication session channel)
   * - Connection
     - 传输协议通信会话(Transport protocol communication session)


简写(Abbreviations)
-----------------------------

.. list-table::
   :widths: 15 20 25
   :header-rows: 1


   * - 简写(Abbreviation)
     - 全称(Full name)
     - 解释(Explanation)
   * - I-
     - AUTOSAR COM Interaction Layer
     - 交互层
   * - L-
     - Relative to the CAN Interface module which is equivalent to the Logical Link Control \
       (the upper part of the Data Link Layer - the lower part is called Media Access Control)
     - 数据链路层
   * - N-
     - Relative to the CAN Transport Layer which is equivalent to the OSI Network Layer.
     - 网络层
   * - CAN L-SDU
     - This is the SDU of the CAN Interface module. It is similar to CAN N-PDU but from the \
       CAN Interface module point of view.
     - CanIf SDU
   * - CAN LSduId
     - This is the unique identifier of a SDU within the CAN Interface. It is used for \
       referencing L-SDU routing properties. Consequently, in order to interact with the \
       CAN Interface through its API, an upper layer uses CAN LSduId to refer to a CAN L-SDU \
       Info Structure.
     - L-SDU唯一标识符
   * - CAN N-PDU
     - This is the PDU of the CAN Transport Layer. It contains a unique identifier, data \
       length and data (protocol control information plus the whole N-SDU or a part of it).
     - CanTp SDU
   * - CAN N-SDU Info Structure
     - This is a CAN Transport Layer internal constant structure that contains specific CAN \
       Transport Layer information to process transmission, reception, segmentation and \
       reassembly of the related CAN N-SDU.
     - N-SDU 数据结构
   * - CAN NSduId
     - Unique SDU identifier within the CAN Transport Layer. It is used to reference N-SDUs \
       routing properties. Consequently, to interact with the CAN Transport Layer via its API, \
       an upper layer uses CAN NSduId to refer to a CAN N-SDU Info Structure.
     - N-SDU唯一标识符
   * - I-PDU
     - This is the PDU of the AUTOSAR COM module.
     - 通信栈 PDU
   * - PDU
     - In layered systems, it refers to a data unit that is specified in the protocol of a \
       given layer. This contains user data of that layer (SDU) plus possible protocol control \
       information. Furthermore, the PDU of layer X is the SDU of its lower layer X-1 \
       (i.e. (X)-PDU = (X-1)-SDU).
     - 协议数据单元
   * - PduInfoType
     - This type refers to a structure used to store basic information to process the \
       transmission\reception of a PDU (or a SDU), namely a pointer to its payload in RAM and \
       the corresponding length (in bytes).
     - PDU/SDU携带的基本信息数据类型
   * - SDU
     - In layered systems, this refers to a set of data that is sent by a user of the services \
       of a given layer, and is transmitted to a peer service user, whilst remaining \
       semantically unchanged.
     - 服务数据单元
   * - BS
     - Block Size
     - 块大小
   * - Can
     - CAN Driver module
     - CAN驱动模块
   * - CAN CF
     - CAN Consecutive Frame N-PDU
     - 连续帧
   * - CAN FC
     - CAN Flow Control N-PDU
     - 流控帧
   * - CAN FF
     - CAN First Frame N-PDU
     - 首帧
   * - CAN SF
     - CAN Single Frame N-PDU
     - 单帧
   * - CF
     - See “CAN CF”
     - 连续帧
   * - DLC
     - Data Length Code (part of CAN PDU that describes the SDU length)
     - SDU长度
   * - FC
     - See “CAN FC”
     - 流控帧
   * - FF
     - See “CAN FF”
     - 首帧
   * - MetaData
     - Meta data transferred alongside a PDU, consisting of a set of meta data items
     - 元数据
   * - MetaDataItem
     - A single item of MetaData of defined type and size
     - 元数据单个条目
   * - Mtype
     - Message Type (possible value: diagnostics, remote diagnostics)
     - 报文类型
   * - N_AI
     - Network Address Information (see ISO 15765-2).
     - 网络地址信息
   * - N_AE
     - Network Address Extension (see ISO 15765-2 [1]).
     - 网络地址信息
   * - N_Ar
     - Time for transmission of the CAN frame (any N-PDU) on the receiver side \
       (see ISO 15765-2 [1]).
     - 接收端CAN帧传输时间
   * - N_As
     - Time for transmission of the CAN frame (any N-PDU) on the sender side \
       (see ISO 15765-2 [1]).
     - 发送端CAN帧传输时间
   * - N_Br
     - Time until transmission of the next flow control N-PDU (see ISO 15765-2 [1]).
     - 接收FF/块最后一个CF时到传输FC的时间
   * - N_Bs
     - Time until reception of the next flow control N-PDU (see ISO 15765-2 [1]).
     - 发送FF/块最后一个CF时到接收FC的时间
   * - N_Cr
     - Time until reception of the next consecutive frame N-PDU (see ISO 15765-2 [1]).
     - 接收下一个CF的时间
   * - N_Cs
     - Time until transmission of the next consecutive frame N-PDU (see ISO 15765-2 [1]).
     - 传输下一个CF的时间
   * - N_Data
     - Data information of the transport layer
     - 传输层数据信息
   * - N_PCI
     - Protocol Control Information of the transport layer
     - 传输层协议控制信息
   * - N_SA
     - Network Source Address (see ISO 15765-2).
     - 网络源地址
   * - N_TA
     - Network Target Address (see ISO 15765-2). It might already contain the N_TAtype \
       (physical/function) in case of ExtendedAddressing.
     - 网络目标地址
   * - N_TAtype
     - Network Target Address type (see ISO 15765-2 [1]).
     - 网络目标地址类型
   * - OBD
     - type (see ISO 15765-2 [1]).OBD
     - 车载诊断，排放相关
   * - SN
     - Sequence Number (see ISO 15765-2 [1]).
     - 序列块
   * - STmin
     - The minimum time the sender is to wait between transmission of two CFs \
       (see ISO 15765-2 [1]).
     - CF发送的最小时间间隔
   * - FS
     - Flow Status
     - Flow Status
   * - CAN FD
     - CAN flexible data rate
     - 可变速率的CAN协议
   * - CAN_DL
     - CAN frame data length
     - CAN帧数据长度
   * - TX_DL
     - Transmit data link layer data length
     - 发送数据链路层的数据长度
   * - RX_DL
     - Received data link layer data length
     - 接收数据链路层的数据长度
   * - SF_DL
     - SingleFrame data length in bytes
     - 单帧数据长度
   * - WFTmax
     - Upper limit to the number of FC.WAIT a receiver is allowed to send in a row \
       (see ISO 15765-2[1]).
     - FC(FS =WAIT)最大数目限制


简介(Introduction)
==========================


CanTp模块用于传输诊断(例如OBD和UDS协议)和AUTOSAR COM I-PDU，其主要作用是对CAN I-PDU进行分段和重新组装，并能够同时处理多个连接，即并行进行多个分段会话。

The CanTp module is used to transmit diagnostic data (such as OBD and UDS protocols) and AUTOSAR COM I-PDUs. Its main function is to segment and reassemble CAN I-PDUs, and it can handle multiple connections simultaneously, that is, perform multiple segmentation sessions in parallel.

.. figure:: ../../../_static/参考手册/CanTp/CanTp模块交互图.png
   :alt: CanTp模块交互图 (CanTp Module Interaction Diagram)
   :name: CanTp_interactions_png
   :align: center

   Figure caption goes here.


如图 :ref:`CanTp_interactions_png` 所示，CanTp模块处于AUTOSAR架构中的通信服务层，其下层模块为CanIf模块，上层模块为PduR。

As shown in Figure "CanTp_interactions_png", the CanTp module is located in the Communication Service Layer of the AUTOSAR architecture. Its lower-layer module is the CanIf module, and its upper-layer module is the PduR module.


功能描述(Functional Description)
==========================================
.. 本章节仅描述模块支持的功能大致情况，不宜做细致描述；更加细致的描述在配置章节，结合配置，从集成角度描述

特性(Features)
------------------------

单帧接收功能 Single-frame(Reception Function)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 - 当底层接收到一个SF时，CanIf通过 ``CanTp_RxIndication`` 回调通知CanTp。

   When the underlying layer receives a Single Frame (SF), CanIf notifies CanTp through the ``CanTp_RxIndication`` callback.

 - CanTp执行PDU ID转换，并从N-PDU有效载荷中提取有用的数据长度。

   CanTp performs PDU ID conversion and extracts the useful data length from the N-PDU payload.

 - CanTp使用 ``PduR_<LoTp>StartOfReception`` 回调为这个传入数据请求上层提供一个缓冲区。

   CanTp uses the ``PduR_<LoTp>StartOfReception`` callback to request a buffer from the upper layer for this incoming data.

 - CanTp使用 ``PduR_<LoTp>CopyRxData`` 回调将接收到的有效数据拷贝到上层提供的缓冲区中。

   CanTp uses the ``PduR_<LoTp>CopyRxData`` callback to copy the received valid data into the buffer provided by the upper layer.

 - CanTp使用 ``PduR_<LoTp>RxIndication`` 回调通知上层接收完成。

   CanTp uses the ``PduR_<LoTp>RxIndication`` callback to notify the upper layer that the reception is complete.


单帧发送功能 Single-frame(Transmission Function)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 - 当PDUR需要传输一个SF时，PDUR调用 ``CanTp_Transmit`` 传入相关数据。

   When PDUR needs to transmit a Single Frame (SF), PDUR calls ``CanTp_Transmit`` and passes in the relevant data.

 - CanTp模块检查输入数据，如果检查通过，则返回 ``E_OK``，以指示接受传输请求。

   The CanTp module checks the input data. If the check passes, it returns ``E_OK`` to indicate acceptance of the transmission request.

 - 上层锁定所需的Tx缓冲区，CanTp调用 ``PduR_<LoTp>CopyTxData`` 来复制段数据。

   The upper layer locks the required Tx buffer, and CanTp calls ``PduR_<LoTp>CopyTxData`` to copy the segment data.

 - CanTp在拷贝的数据基础上添加控制信息(PCI,TA,Metadata)，然后调用 ``CanIf_Transmit`` 请求CanIf模块执行发送。

   CanTp adds control information (PCI, TA, Metadata) to the copied data, and then calls ``CanIf_Transmit`` to request the CanIf module to perform the transmission.

 - CanIf模块处理发送请求，成功发送后，CanIf调用 ``CanTp_TxConfirmation`` 通知CanTp发送成功。

   The CanIf module processes the transmission request. After a successful transmission, CanIf notifies CanTp of the successful transmission by calling ``CanTp_TxConfirmation``.

 - CanTp调用 ``PduR_<User：LoTp>TxConfirmation`` 通知PDUR已经成功传输。

   CanTp calls ``PduR_<User: LoTp>TxConfirmation`` to notify PDUR that the transmission has been successfully completed.


多帧接收功能 Multi-frame(Reception Function)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

当接收到一个多帧报文时，CanTp模块会解析首帧报文的控制信息，并根据相关配置判断是否进行接收，如果通过检查则通知上层，
并根据上层的状态信息将接收的数据传递给上层模块。首帧处理完成之后，发送方会在规定时间内响应一个流控帧，若流控状态为ContinueToSend，
CanTp会继续接收连续帧并向上层传递。当接收完成时通知上层接收完成。

When a multi-frame message is received, the CanTp module parses the control information of the First Frame (FF) and determines whether to receive it based on relevant configurations. If the check is passed, it notifies the upper layer and transmits the received data to the upper layer module according to the status information of the upper layer. After the processing of the First Frame is completed, the sender will respond with a Flow Control Frame (FC) within the specified time. If the flow control status is ContinueToSend, CanTp will continue to receive consecutive frames (CF) and transmit them to the upper layer. When the reception is completed, it notifies the upper layer that the reception is finished.


FF接收流程(FF Reception process)
****************************************************

 - 当接收到一个FF时，CanIf通过 ``CanTp_RxIndication`` 回调通知CanTp。

   When a First Frame (FF) is received, CanIf notifies CanTp through the ``CanTp_RxIndication`` callback.

 - CanTp解析FF的控制信息后，使用 ``PduR_<LoTp>StartOfReception`` 回调请求PDUR为传入的数据提供一个缓冲区。

   After CanTp parses the control information of the First Frame (FF), it uses the ``PduR_<LoTp>StartOfReception`` callback to request PDUR to provide a buffer for the incoming data.


FC发送流程  Flow Control Frame (FC) Transmission Process
*******************************************************************

 - 当需要发送FC时，CanTp会调用 ``CanIf_Transmit`` 接口，并等待确认。

   When a Flow Control Frame (FC) needs to be transmitted, CanTp will call the ``CanIf_Transmit`` function and wait for confirmation.

 - 根据上层的可用缓冲区，流控状态可以是 ``ContinueToSend`` 或 ``Wait``。

   Based on the available buffer of the upper layer, the flow control status can be ``ContinueToSend`` or ``Wait``.


CF接收流程(CF Reception Process)
*******************************************

 - 当接收到一个CF时，CanIf通过 ``CanTp_RxIndication`` 回调通知CanTp。

   When a Consecutive Frame (CF) is received, CanIf notifies CanTp through the ``CanTp_RxIndication`` callback.

 - CanTp验证序列号，若正确，则要求PduR复制数据。

   CanTp verifies the sequence number. If it is correct, it requests PduR to copy the data.


多帧发送功能 Multi-frame(Transmission Function)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

当需要发送一个多帧报文时，CanTp模块会添加首帧报文的控制信息，并在FF发送成功后等待接收一个流控帧(FC)。

hen a multi-frame message needs to be transmitted, the CanTp module adds the control information of the First Frame (FF). After the FF is successfully sent, it waits to receive a Flow Control Frame (FC).

当接收到的FC所带状态信息为 CTS(Continue To Send)时，CanTp将接下来的数据填充成连续帧(CF)并发送。

When the status information carried by the received FC is CTS (Continue To Send), CanTp will fill the subsequent data into Consecutive Frames (CF) and send them.

如果发送的CF个数达到FC所带的BS(Block Size)，则需要等待下一个FC，直到数据发送完成。

If the number of sent CFs reaches the BS (Block Size) carried by the FC, it needs to wait for the next FC until the data transmission is completed.


FF发送流程(FF Transmission Process)
*****************************************************

 - 当PDUR需要传输一个多帧数据时调用CanTp的 ``CanTp_Transmit``。

   When PDUR needs to transmit multi-frame data, it calls CanTp's ``CanTp_Transmit`` function.

 - CanTp会验证输入参数和资源的可用性，并根据发送请求的有用信息(如SF/FF/CF N-PDU标识符、FC N-PDU标识符、N_TA值等)启动带有参数的内部传输任务。

   CanTp verifies the input parameters and resource availability, and initiates an internal transmission task with parameters based on the useful information from the transmission request (such as SF/FF/CF N-PDU identifiers, FC N-PDU identifier, N_TA value, etc.).

 - CanTp在接下来调用 ``PduR_<LoTp>CopyTxData``，上层将数据复制到目标缓冲区。

   CanTp then calls ``PduR_<LoTp>CopyTxData``, and the upper layer copies the data to the target buffer.

 - CanTp通过 ``CanIf_Transmit`` 通知CanIf发送首帧(FF)。

   CanTp notifies CanIf to transmit the First Frame (FF) via ``CanIf_Transmit``.

 - CanTp等待来自CanIf的确认(``CanTp_TxConfirmation``)，确认FF发送成功。

   CanTp waits for confirmation from CanIf (``CanTp_TxConfirmation``) to confirm the successful transmission of the First Frame (FF).

FC接收流程(FC reception process)
*********************************************

 - 在FF发送成功后，CanTp等待接收一个流控帧(FC)。

   After the successful transmission of the First Frame (FF), CanTp waits to receive a Flow Control Frame (FC).

 - 接收到的FC包含以下状态信息：

   The received Flow Control Frame (FC) contains the following status information:

   * ``ContinueToSend`` (Continue To Send): Indicates that data transmission can continue.

     ``ContinueToSend`` (Continue To Send): Indicates that data transmission can continue.

   * ``Wait``：表示需要等待接收方的上层缓冲区可用。
 
     ``Wait``: Indicates that it is necessary to wait for the upper-layer buffer of the receiver to become available.

   * ``Overflow (OVFLW)``：表示接收方buffer溢出，CanTp会终止当前的分段传输。

     ``Overflow (OVFLW)``: Indicates that the receiver's buffer has overflowed, and CanTp will terminate the current segmented transmission.

 - 如果接收到的FC状态为 ``ContinueToSend``，CanTp会根据FC中的BS(Block Size)参数准备发送连续帧(CF)。

   If the status of the received Flow Control Frame (FC) is ``ContinueToSend``, CanTp will prepare to send Consecutive Frames (CF) according to the BS (Block Size) parameter in the FC.

 - 如果接收到的FC状态为 ``Wait``，CanTp会暂停发送，直到接收到新的FC。

   If the status of the received Flow Control Frame (FC) is ``Wait``, CanTp will pause transmission until a new FC is received.


CF发送流程(CF Transmission Process)
*********************************************

 - 当CanTp接收到状态为 ``CTS`` 的FC后，会调用 ``PduR_<LoTp>CopyTxData``，要求PDUR提供要发送的新数据。

   After CanTp receives an FC with status ``CTS``, it calls ``PduR_<LoTp>CopyTxData`` to request PduR to provide new data for transmission.

 - CanTp将数据填充成连续帧(CF)，并通过 ``CanIf_Transmit`` 通知CanIf发送CF。

   CanTp formats the data into Consecutive Frames (CF) and notifies CanIf to transmit the CF via ``CanIf_Transmit``.

 - CanTp等待来自CanIf的确认(``CanTp_TxConfirmation``)，确认CF发送成功。

   CanTp waits for confirmation from CanIf (``CanTp_TxConfirmation``) to confirm the successful transmission of the CF.

 - 如果发送的CF个数达到FC所带的BS(Block Size)，CanTp会等待接收下一个FC。

   If the number of transmitted CFs reaches the Block Size (BS) specified in the FC, CanTp waits to receive the next FC.

 - 重复上述过程，直到所有数据发送完成,最后调用``PduR_<User:LoTp>TxConfirmation`` 通知PDUR发送结果。

   This process repeats until all data is transmitted, and finally, ``PduR_<User:LoTp>TxConfirmation`` is called to notify PduR of the transmission result.


支持多核分布功能 Support Multi-core(Distribution Function)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 - CanTp模块分布在多分区,具体的分区信息由Pdu配置项EcucPduDefaultPartitionRef决定。

   The CanTp module is distributed across multiple partitions, with specific partition information determined by the Pdu configuration parameter EcucPduDefaultPartitionRef.

 - 支持配置不同的RxNSdu、TxNSdu分布在不同的变体中，但需要统一该NSdu下的分区信息，如NSduRef，NPduRef应该保证分布在统一分区。

   It supports configuring different RxNSdus and TxNSdus to be distributed across different variants, but the partition information under each NSdu must be unified. For example, NSduRef and NPduRef should be guaranteed to be distributed in the same partition.

 - 在多变体情况下，同一RxNSdu、TxNSdu的分区属性不可改变，需保持一致。

   In multi-variant scenarios, the partition attributes of the same RxNSdu and TxNSdu cannot be changed and must remain consistent. 

.. only:: doc_pbs

支持变体功能(Support variant functionality)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 - 支持配置CanTp模块连接通道(CanTpChannel)数目变体。

   Supports configuring variants in the number of CanTp module connection channels (CanTpChannel).

 - 支持配置RxNSdu、TxNSdu数目变体。

   Supports configuring variants in the number of RxNSdus and TxNSdus.

 - 基本支持配置RxNSdu、TxNSdu配置项属性变体，但AddressingFormat、TaType、SA、TA及AE等属性除外。

   Basically supports configuring variants in the attribute configuration items of RxNSdu and TxNSdu, except for attributes such as AddressingFormat, TaType, SA, TA, and AE.

 - 支持配置Pdu引用变体。如CanTpRxNPduRef，CanTpTxNPduRef,CanTpRxFcNPduRef，CanTpTxFcNPduRef，CanTpRxNSduRef，CanTpTxNSduRef。

   Supports configuring Pdu reference variants, such as CanTpRxNPduRef, CanTpTxNPduRef, CanTpRxFcNPduRef, CanTpTxFcNPduRef, CanTpRxNSduRef, and CanTpTxNSduRef.


偏差(Deviation)
--------------------------
.. 有序列表示例

**配置 (Configuration)**

#. Pdu连接
   目前不支持R(T)x N-PDU被重复配置到不同的R(T)x N-SDU,当前N-PDU与N-SDU通过工具校验保持一一对应的关系，暂不支持N-PDU的序列化功能。

   Pdu Connection: Currently, it is not supported to repeatedly configure R(T)x N-PDUs into different R(T)x N-SDUs. At present, N-PDUs and N-SDUs maintain a one-to-one correspondence through tool verification, and the serialization function of N-PDUs is not supported temporarily.


**接口 (Interface)** ： None


扩展(Extension)
-------------------------
当前CanTp模块扩展了一些可用客户自由选择的功能。

The current CanTp module has expanded some optional functions that customers can freely choose.

#. 固定BS(Block Size)配置：

   Fixed BS (Block Size) configuration:

   当启用工程宏CANTP_FIX_BS时，在接收过程中需要发送流控制帧(FC帧)时，BS(块大小)将采用CanTpBs配置的固定值；若未启用该宏，则BS值将由CanTp模块根据上层缓冲区的大小动态计算得出。

   When the engineering macro CANTP_FIX_BS is enabled, the BS (Block Size) will use the fixed value configured by CanTpBs when a Flow Control Frame (FC frame) needs to be sent during the reception process; if the macro is not enabled, the BS value will be dynamically calculated by the CanTp module based on the size of the upper-layer buffer.

#. 接收FIFO(先进先出)机制:

   Receive FIFO (First-In-First-Out) mechanism:

   该功能支持在MainFunction处理接收任务时，使用 FIFO 队列存储接收连接，确保先激活的连接先被处理。如果某个接收连接处理完成，将其从 FIFO 队列中移除，后续连接依次前移。\
   
   该功能可通过配置项CanTpRxQueue来控制该功能的启用状态，默认情况下该功能为关闭状态。

   This function supports using a FIFO queue to store receiving connections when the MainFunction processes receiving tasks, ensuring that the connection activated first is processed first. If a receiving connection is processed, it will be removed from the FIFO queue, and the subsequent connections will move forward in sequence.

   This feature is controlled by the configuration parameter CanTpRxQueue and is disabled by default.

#. 同步接收功能：

   Synchronous reception function:

   同步接收功能是CanTp模块中的一项优化功能，启用该功能后，在接收单帧(SF)或连续帧(CF)的最后一帧时，CanTp模块将直接在CanTp_RxIndication(中断服务程序)中向上层PduR模块发送通知，而无需等待下一个MainFunction周期。
   
   该功能通过配置项CanTpSynchronousRxIndication进行控制，默认情况下该功能为关闭状态。

   The synchronous reception function is an optimized feature in the CanTp module. When this function is enabled, the CanTp module will directly notify the upper-layer PduR module within the CanTp_RxIndication (Interrupt Service Routine) upon receiving a Single Frame (SF) or the last Consecutive Frame (CF), without waiting for the next MainFunction cycle.

   This function is controlled by the configuration item CanTpSynchronousRxIndication and is disabled by default.

#. 同步发送功能：

   Synchronous transmission function:

   开启该功能后，在CanTp_Transmit被触发时，直接进行SF/FF的发送，不必再等一个MainFunction周期。通过配置项CanTpSynchronousTransmission控制使能，默认情况下该功能为关闭状态。

   When this function is enabled, the transmission of SF/FF will be carried out directly when CanTp_Transmit is triggered, without waiting for another MainFunction cycle. It is controlled by the configuration parameter CanTpSynchronousTransmission and is disabled by default.

#. 报告运行时错误:

   Report runtime errors:

   用户可以通过配置项CanTpRuntimeErrorDetect控制是否向Det报告运行时错误，默认情况下该功能为打开状态。

   Users can control whether to report runtime errors to Det through the configuration item CanTpRuntimeErrorDetect, and this function is enabled by default.

#. Can/CanFD兼容功能:

   CAN/CAN FD compatibility function:

   CAN/CAN FD 兼容功能 是一种支持在 CAN FD 通道下同时处理 CAN 和 CAN FD 帧的机制。开启该功能后，系统能够根据接收到的帧类型(CAN 或 CAN FD)自动切换发送模式，从而实现 CAN 和 CAN FD 的兼容通信。

   该功能通过CanTpSupportCanWithCanFD功能控制，默认情况下该功能为关闭状态。

   The CAN/CAN FD compatibility feature is a mechanism that allows processing of both CAN and CAN FD frames on a CAN FD channel. When this function is enabled, the system can automatically switch the transmission mode according to the type of received frame (CAN or CAN FD), thereby achieving compatible communication between CAN and CAN FD.

   This feature is controlled by the CanTpSupportCanWithCanFD configuration parameter and is disabled by default.


集成(Integration)
===========================

文件列表(File List)
-------------------------------

静态文件(Static Files)
~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - 文件(File)
     - 描述(Description)

   * - CanTp.h
     - CanTp模块头文件，包含外部API函数的扩展声明(CanTp module header file, containing extended declarations of external API functions)

   * - CanTp.c
     - CanTp模块源文件，包含API函数的实现(CanTp module source file, containing the implementation of API functions)

   * - CanTp_Internal.c
     - 定义CanTp模块内部接口(Defines internal interfaces of the CanTp module)

   * - CanTp_Internal.h
     - 包含CanTp模块需要的类型定义、宏定义和内联函数(Contains type definitions, macro definitions, and inline functions required by the CanTp module)

   * - CanTp_MemMap.h
     - 包含CanTp模块的内存抽象，由Memmap模块生成(Contains the memory abstraction of the CanTp module, generated by the Memmap module)

   * - CanTp_Types.h
     - 包含CanTp模块需要的类型定义(Contains type definitions required by the CanTp module)


动态文件(Dynamic file)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - 文件(File)
     - 描述(Description)

   * - CanTp_Lcfg.c
     - 包含运行时变量的定义(Contains definitions of runtime variables)
       
   * - CanTp_Lcfg.h
     - 包含由配置决定的数据类型生成和运行时变量声明(Contains generation of configuration-dependent data types and declarations of runtime variables)

   * - CanTp_PBcfg.c
     - 包含CanTp模块的PB(Post Build)配置信息(Contains PB (Post Build) configuration information for the CanTp module)

   * - CanTp_PBcfg.h
     - 包含CanTp模块内部宏定义和PB配置的数据类型定义(Contains internal macro definitions of the CanTp module and data type definitions for post-build configuration)

   * - CanTp_Cfg.h
     - 包含CanTp模块具体配置功能的使能状态和对外宏定义(Contains enabling status of specific configuration functions and external macro definitions of the CanTp module)


错误处理(Error Handling)
--------------------------------

开发错误(Development Errors)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. list-table::
   :widths: 20 10 30
   :header-rows: 1

   * - Error Code
     - Value[hex]
     - Description

   * - CANTP_E_PARAM_CONFIG
     - 0x01
     - 当调用CanTp_ChangeParameter时，传入的参数值无效(Invalid parameter value passed when calling CanTp_ChangeParameter)

   * - CANTP_E_PARAM_ID
     - 0x02
     - 当调用CanTp_ChangeParameter或CanTp_ReadParameter时，传入的参数ID无效(Invalid parameter ID passed when calling CanTp_ChangeParameter or CanTp_ReadParameter)

   * - CANTP_E_PARAM_POINTER
     - 0x03
     - 调用API服务时传入了一个空指针(NULL pointer passed to the API service)
        
   * - CANTP_E_INIT_FAILED
     - 0x04
     - 模块初始化失败，例如在调用CanTp_Init()时传入了一个无效的PostBuild配置指针(Module initialization failed, for example, an invalid PostBuild configuration pointer passed when calling CanTp_Init())

   * - CANTP_E_UNINIT
     - 0x20
     - 在模块未初始化(状态为CANTP_OFF)时调用了除CanTp_Init()、CanTp_GetVersionInfo()和CanTp_MainFunction()之外的API服务(API service other than CanTp_Init, CanTp_GetVersionInfo, and CanTp_MainFunction called before module initialization while module state is CANTP_OFF)

   * - CANTP_E_INVALID_TX_ID
     - 0x30
     - 无效的发送PDU标识符(例如，调用服务时传入了一个不存在的Tx PDU标识符)(Invalid transmit PDU identifier, for example, a non-existent Tx PDU identifier passed when calling the service)

   * - CANTP_E_INVALID_RX_ID
     - 0x40
     - 无效的接收PDU标识符(例如，调用服务时传入了一个不存在的Rx PDU Id)(Invalid receive PDU identifier, for example, a non-existent Rx PDU Id passed when calling the service)


产品错误(Product Errors)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
None

运行时错误(Runtime Errors)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. list-table::
   :widths: 20 10 30
   :header-rows: 1

   * - Error code
     - Value[hex]
     - Description

   * - CANTP_E_PADDING
     - 0x70
     - 接收到的PDU长度小于8字节(即PduInfoPtr.SduLength < 8)(Received PDU length less than 8 bytes, i.e., PduInfoPtr.SduLength < 8)

   * - CANTP_E_INVALID_TATYPE
     - 0x90
     - 当调用CanTp_Transmit()时，配置的Tx I-PDU使用功能寻址，但长度参数指示消息无法通过单帧(SF)发送(When CanTp_Transmit() is called, the configured Tx I-PDU uses functional addressing, but the length parameter indicates the message cannot be sent via Single Frame (SF))

   * - CANTP_E_OPER_NOT_SUPPORTED
     - 0xA0
     - 请求的操作不支持：取消传输/接收请求时，指定的N-SDU不在传输/接收过程中(Requested operation not supported: specified N-SDU is not in transmission/reception process when canceling transmission/reception request)

   * - CANTP_E_COM
     - 0xB0
     - 在接收或传输过程中发生实现特定的错误(非超时错误)时报告的事件(Event reported when implementation-specific error (non-timeout error) occurs during reception or transmission)

   * - CANTP_E_RX_COM
     - 0xC0
     - 在接收过程中发生超时错误时报告的事件(Event reported when timeout error occurs during reception process)

   * - CANTP_E_TX_COM
     - 0xD0
     - 在传输过程中发生超时错误时报告的事件(Event reported when timeout error occurs during transmission process)


额外产品错误(Additional Product Errors)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. list-table::
   :widths: 20 10 30
   :header-rows: 1

   * - Error code
     - Value[hex]
     - Description

   * - CANTP_E_CANTPNAS_TIMEOUT_OCCURRED
     - Value[hex]
     - 检测到N_As超时(N_As timeout detected)

   * - CANTP_E_CANTPNAR_TIMEOUT_OCCURRED
     - Value[hex]
     - 检测到N_Ar超时(N_Ar timeout detected)

   * - CANTP_E_CANTPNBS_TIMEOUT_OCCURRED
     - Value[hex]
     - 检测到N_Bs超时(N_Bs timeout detected)

   * - CANTP_E_CANTPNBR_TIMEOUT_OCCURRED
     - Value[hex]
     - 检测到N_Br超时(N_Br timeout detected)

   * - CANTP_E_CANTPNCS_TIMEOUT_OCCURRED
     - Value[hex]
     - 检测到N_Cs超时(N_Cs timeout detected)

   * - CANTP_E_CANTPNCR_TIMEOUT_OCCURRED
     - Value[hex]
     - 检测到N_Cr超时(N_Cr timeout detected)

   * - CANTP_E_SWAPPED_CONSECUTIVE_FRAMES_RECEIVED
     - Value[hex]
     - 接收到顺序错误的连续帧(CF)(Received consecutive frames (CF) in wrong order)

   * - CANTP_E_DROPPED_CONSECUTIVE_FRAMES_DETECTED
     - Value[hex]
     - 检测到丢失的连续帧(CF)(Missing consecutive frames (CF) detected)

   * - CANTP_E_FC_OVERFLOW_RECEIVED
     - Value[hex]
     - 接收到状态为溢出的流控帧(FC)(Received flow control frame (FC) with overflow status)

   * - CANTP_E_FC_OVERFLOW_TRANSMITTED
     - Value[hex]
     - 发送了状态为溢出的流控帧(FC)(Transmitted flow control frame (FC) with overflow status)


接口描述(Interface Description)
======================================
.. include:: CanTp_h_api.rst

配置函数(Configuration Function)
----------------------------------------
None

依赖的服务(Dependent Services)
-----------------------------------------


强制接口(Mandatory Interfaces)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. 可选的章节，根据模块实际情况确定

.. list-table::
   :widths: 10 5 30
   :header-rows: 1

   * - API Function
     - Header File
     - Description
   * - CanIf_Transmit
     - CanIf.h
     - Requests transmission of a PDU.
   * - Det_ReportRuntimeError
     - Det.h
     - Service to report runtime errors. If a callout has been configured then this callout shall be called.
   * - PduR_CanTpCopyRxData
     - PduR_CanTp.h
     - This function is called to provide the received data of an I-PDU segment (N-PDU) to the upper layer.
   * - PduR_CanTpCopyTxData
     - PduR_CanTp.h
     - This function is called to acquire the transmit data of an I-PDU segment (N-PDU).
   * - PduR_CanTpRxIndication
     - PduR_CanTp.h
     - Called after an I-PDU has been received via the TP API, the result indicates whether the transmission was successful or not.
   * - PduR_CanTpStartOfReception
     - PduR_CanTp.h
     - This function is called at the start of receiving an N-SDU.
   * - PduR_CanTpTxConfirmation
     - PduR_CanTp.h
     - This function is called after the I-PDU has been transmitted on its network, the result indicates whether the transmission was successful or not.


可选接口(Optional Interfaces)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. 可选的章节，根据模块实际情况确定
.. 格式同强制接口

.. list-table::
   :widths: 10 5 30
   :header-rows: 1

   * - API Function
     - Header File
     - Description
   * - Det_ReportError
     - Det.h
     - Service to report development errors.


配置(Configuration)
==========================================
本章节以 **功能** 为导向，从 **集成** 的角度，挑重点，常用，典型配置举例讲解。未涉及的配置项可在工具界面找到详细说明。

This chapter is **functionality**-oriented and, from the perspective of **integration**, focuses on key points, common uses, and typical configuration examples for explanation. The unmentioned configuration items can be found with detailed descriptions in the tool interface.


1.(CanTpGeneral)
----------------------

CanTpGeneral容器包含一些CanTp模块通用的配置参数。

The CanTpGeneral container includes configuration parameters common to the CanTp module.

.. figure:: ../../../_static/参考手册/CanTp/CanTpGeneral.png
   :name: CanTpGeneral
   :align: center
   :width: 500

   CanTpGeneral配置示意图。 (Schematic Diagram of CanTpGeneral Configuration)
  

- CanTpDynIdSupport

  启用或禁用动态 ID 处理支持。Enabled：启用动态ID处理支持，动态ID处理允许CanTp通过N-PDU的MetaData动态调整CAN帧的标识符(ID)。Disabled：禁用动态ID处理支持(默认状态)。

  Enable or disable dynamic ID handling support. Enabled: Enables dynamic ID handling support. This allows CanTp to dynamically determine the CAN identifier (ID) for a frame based on the MetaData associated with an N-PDU.

- CanTpPaddingByte

  CanTpPaddingByte 用于指定填充字节的值，初始化未使用的字节。

  CanTpPaddingByte is used to specify the value of the padding byte and initialize unused bytes.

- CanTpRxQueue

  配置接收 FIFO 机制(功能描述章节-扩展)，Enabled：启用接收 FIFO 机制。Disabled：禁用接收 FIFO 机制(默认状态)。使能之后支持在多个接收连接共存的情况下，启用接收 FIFO 机制可以确保先激活的连接优先处理。

  Configure the receive FIFO mechanism (see the "Functional Description" chapter - Extension). Enabled: Enables the receive FIFO mechanism. Disabled: Disables the receive FIFO mechanism (default state). When enabled, it manages multiple concurrent receive connections by ensuring that the connection activated first is processed first (FIFO order).

- CanTpRuntimeErrorDetect

  启用或禁用运行时错误报告功能(功能描述章节-扩展)。Enabled：启用运行时错误报告，报告给 Det(默认状态)。Disabled：禁用运行时错误报告，CANTP 模块不会将错误报告给 Det。

  Enable or disable the runtime error reporting function (see the "Functional Description" chapter - Extension).Enabled: Enables runtime error reporting, which is reported to Det (default state).Disabled: Disables runtime error reporting, and the CANTP module will not report errors to Det.

- CanTpSynchronousRxIndication

  控制同步接收功能的启用状态(详见 功能描述章节-扩展)。Enabled：启用同步接收功能。Disabled：禁用同步接收功能(默认状态)。

  Control the activation status of the synchronous reception function (see details in the "Functional Description" chapter - Extension).Enabled: Enables the synchronous reception function.Disabled: Disables the synchronous reception function (default state).

- CanTpSynchronousTransmission

  控制同步发送功能的启用状态(详见 功能描述章节-扩展)。Enabled：启用同步发送功能。Disabled：禁用同步发送功能(默认状态)。

  Control the activation status of the synchronous transmission function (see details in the "Functional Description" chapter - Extension).Enabled: Enables the synchronous transmission function.Disabled: Disables the synchronous transmission function (default state).

2.(CanTpDemEventParameterRefs)
--------------------------------------

.. figure:: ../../../_static/参考手册/CanTp/CanTpDemEventParameterRefs.png
   :alt: CanTpDemEventParameterRefs
   :name: CanTpDemEventParameterRefs
   :align: center

   CanTpDemEventParameterRefs配置示意图。 (Schematic Diagram of CanTpDemEventParameterRefs Configuration)


如图 :ref:`CanTpDemEventParameterRefs` 所示:

As shown in the Schematic Diagram of CanTpDemEventParameterRefs Configuration: 

当CanTp运行过程中发生额外的产品错误(详见错误处理章节-额外产品错误)时，可以在CanTpDemEventParameterRefs配置需要向Dem报告的产品错误并关联对应
的DemEventParameter，当错误被触发时CanTp会使用API Dem_SetEventStatus通知Dem。

When an additional product error occurs during CanTp operation (see details in the "Error Handling" chapter - Additional Product Errors), you can configure the product errors that need to be reported to Dem in CanTpDemEventParameterRefs and associate the corresponding DemEventParameter. When an error is triggered, CanTp will use the API Dem_SetEventStatus to notify Dem.


3.(Channel property)
----------------------

.. figure:: ../../../_static/参考手册/CanTp/CanTpSupportCanWithCanFD.png
   :alt: CanTpSupportCanWithCanFD
   :name: CanTpSupportCanWithCanFD
   :align: center

   CanTpSupportCanWithCanFD配置示意图。 (Schematic Diagram of CanTpSupportCanWithCanFD Configuration)
  

如图 :ref:`CanTpSupportCanWithCanFD` 所示:

As shown in the Schematic Diagram of CanTpSupportCanWithCanFD Configuration:

CanTpSupportCanWithCanFD：控制CAN/CAN FD 兼容功能的启用状态(详见 功能描述章节-扩展),Enabled：打开CAN/CAN FD兼容功能。Disabled：保持该channel下原有的传输格式。

CanTpSupportCanWithCanFD: Controls the activation status of the CAN/CAN FD compatibility function (see details in the "Functional Description" chapter - Extension). Enabled: Enables the CAN/CAN FD compatibility function. Disabled: Maintains the original transmission format for this channel.


4.(Reception)
----------------------
4.1(CanTpRxNSdu)
----------------------
RxNSdu 负责接收 CAN 总线上的分段数据并将其重组为完整的数据包以及未分段数据。CanTp会使用该RxNSdu将接收到的数据传递给上层模块PduR。

An RxNSdu is responsible for receiving data (both segmented and unsegmented) from the CAN bus and reassembling segmented data into complete packets. CanTp uses this RxNSdu to transfer the received data to the upper-layer module PduR.

.. figure:: ../../../_static/参考手册/CanTp/CanTpRxNSdu.png
   :alt: CanTpRxNSdu
   :name: CanTpRxNSdu
   :align: center

   CanTpRxNSdu 的配置示意图。 (Schematic Diagram of CanTpRxNSdu Configuration)


如图 :ref:`CanTpRxNSdu` 所示，RxNSdu 负责接收和重组数据。

As shown in the Schematic Diagram of CanTpRxNSdu Configuration, RxNSdu is responsible for receiving and reassembling data.

 - CanTpRxAddressingFormat：寻址格式，需保持与发送端一致。
   
   CanTpRxAddressingFormat: Addressing format, which must be consistent with that of the sender.

 - CanTpRxTaType：代表了此条接收通路选择哪种通信类型，包括物理寻址或者功能寻址。

   CanTpRxTaType: Represents the communication type selected for this receiving channel, including physical addressing or functional addressing.

 - CanTpRxPaddingActivation：定义接收帧是否使用填充。

   CanTpRxPaddingActivation: Defines whether padding is used for received frames.

 - CanTpRxNSduRef：用于唯一标识一个 RxNSdu 实例，确保接收到的数据能够正确路由到对应的 RxNSdu。

   CanTpRxNSduRef: Used to uniquely identify an RxNSdu instance, ensuring that received data can be correctly routed to the corresponding RxNSdu.

如果需要接收分段数据，还需打开以下配置项：

The following parameters are also relevant for the reception of segmented data:

 - CanTpBs：设置接收端期望的数据块大小，注意搭配工程宏CANTP_FIX_BS使用。

   CanTpBs: Sets the data block size expected by the receiver. Note that it should be used together with the engineering macro CANTP_FIX_BS.

 - CanTpSTmin：设置接收端期望的FC帧最小时间间隔。

   CanTpSTmin: Sets the minimum time interval for FC frames expected by the receiver.

 - CanTpNa(b,c)r：设置超时时间，防止因网络问题导致的长时间等待。

   CanTpNa(b,c)r: Sets the timeout period to prevent long waits caused by network issues.


4.1.1(CanTpRxNPdu)
----------------------
CanTpRxNPdu 是 CanTp模块中用于接收协议数据单元(Protocol Data Unit, PDU)的关键组件。
下层模块CanIf会使用该CanTpRxNPdu将来自 CAN 总线的数据帧传递给 CanTp 模块，从而使CanTp进行进一步处理(如解析、重组等)。

CanTpRxNPdu is a key component in the CanTp module for receiving Protocol Data Units (PDUs).
The lower-layer module CanIf uses this CanTpRxNPdu to transfer data frames from the CAN bus to the CanTp module, enabling the CanTp module to perform further processing (such as parsing, reassembly, etc.).

.. figure:: ../../../_static/参考手册/CanTp/CanTpRxNPdu.png
   :name: CanTpRxNPdu
   :align: center
   :width: 500

   CanTpRxNPdu 的配置示意图。 (Schematic Diagram of CanTpRxNPdu Configuration)



- CanTpRxNPduRef：用于唯一标识一个 RxNPdu 实例，确保接收到的数据能够正确路由到对应的 RxNPdu。

  CanTpRxNPduRef: Used to uniquely identify an RxNPdu instance, ensuring that the received data can be correctly routed to the corresponding RxNPdu.


4.1.2(CanTpTxFcNPdu)
----------------------
当接收端接收到数据帧后，根据上层缓冲区状态和数据处理能力，通过 TxFcNPdu 发送流控帧(如 CTS、Wait 或 Overflow)来控制发送端的行为。

After the receiver receives the data frame, it sends flow control frames (such as CTS, Wait, or Overflow) through TxFcNPdu to control the behavior of the sender, based on the status of the upper-layer buffer and data processing capability.

.. figure:: ../../../_static/参考手册/CanTp/CanTpTxFcNPdu.png
   :alt: CanTpTxFcNPdu
   :name: CanTpTxFcNPdu
   :align: center

   CanTpTxFcNPdu 的配置示意图。 (Schematic Diagram of CanTpTxFcNPdu Configuration)



如图 :ref:`CanTpTxFcNPdu` 所示:

As shown in the Schematic Diagram of CanTpTxFcNPdu Configuration:

 - CanTpTxFcNPduRef：用于唯一标识一个 TxFcNPdu 实例，确保在ECU需要发送流控帧时，能够正确使用对应的 TxFcNPdu。

   CanTpTxFcNPduRef: Used to uniquely identify a TxFcNPdu instance, ensuring that when the ECU needs to send a flow control frame, the corresponding TxFcNPdu can be used correctly.


5.(Transmission)
----------------------
5.1(CanTpTxNSdu)
----------------------
CanTpTxNSdu的主要作用是将上层应用的数据打包成适合 CAN 总线传输的格式，传递给下层模块。

The main function of CanTpTxNSdu is to package data from upper-layer applications into a format suitable for transmission over the CAN bus and pass it to lower-layer modules.

.. figure:: ../../../_static/参考手册/CanTp/CanTpTxNSdu.png
   :alt: CanTpTxNSdu
   :name: CanTpTxNSdu
   :align: center

   CanTpTxNSdu 的配置示意图。 (Schematic Diagram of CanTpTxNSdu Configuration)



如图 :[CanTpTxNSdu] 所示:

As shown in: [CanTpTxNSdu]:

 - CanTpTxAddressingFormat：寻址格式，需保持与接收端一致。

   CanTpTxAddressingFormat: Addressing format, which must be consistent with that of the receiver.

 - CanTpTxTaType：代表了此条发送通路选择哪种通信类型，包括物理寻址或者功能寻址。

   CanTpTxTaType: Represents the type of communication selected for this transmission path, including physical addressing or functional addressing.

 - CanTpTxPaddingActivation：定义发送帧是否使用填充。

   CanTpTxPaddingActivation: Defines whether padding is used for the transmitted frame.

 - CanTpTxNSduRef：用于唯一标识一个 TxNSdu 实例，将上层应用的数据与具体的 TxNSdu 实例关联起来。

   CanTpTxNSduRef: Used to uniquely identify a TxNSdu instance, associating data from upper-layer applications with a specific TxNSdu instance.

 - CanTpNas：设置帧发送超时时间，防止因网络问题导致的长时间等待。

   CanTpNas: Sets the frame transmission timeout period to prevent long waits caused by network issues.

如果需要发送分段数据，还需打开以下配置项：

The following parameters are also relevant for the transmission of segmented data:

 - CanTpNbs：发送方发完当前块的数据时，等待接收下一个流控帧的最大时间。

   CanTpNbs: The maximum time the sender waits to receive the next flow control frame after finishing sending the data of the current block.

 - CanTpNcs：发送方发送连续帧时，允许从 PduR层获取数据的最大时间。

   CanTpNcs: The maximum time allowed for the sender to obtain data from the PduR layer when sending consecutive frames.

5.1.1(CanTpTxNPdu)
----------------------
CanTpTxNPdu 负责将 CanTp 模块处理后的数据帧发送给CanIf模块，从而发送到CAN总线。

CanTpTxNPdu is responsible for sending the data frames processed by the CanTp module to the CanIf module, which are then transmitted to the CAN bus.

.. figure:: ../../../_static/参考手册/CanTp/CanTpTxNPdu.png
   :alt: CanTpTxNPdu
   :name: CanTpTxNPdu
   :align: center

   CanTpTxNPdu 的配置示意图。 (Schematic Diagram of CanTpTxNPdu Configuration)


如图 :ref:`CanTpTxNPdu` 所示:

As shown in the Schematic Diagram of CanTpTxNPdu Configuration:

 - CanTpTxNPduRef：用于唯一标识一个 TxNPdu 实例，确保处理后的数据能够正确路由到对应的 TxNPdu，从而发送给下层 CanIf 模块。

   CanTpTxNPduRef: Used to uniquely identify a TxNPdu instance, ensuring that the processed data can be correctly routed to the corresponding TxNPdu for transmission to the lower-layer CanIf module.


5.1.2(CanTpRxFcNPdu)
----------------------
CanTpRxFcNPdu 负责从 CAN 总线接收流控帧， CanTp会进行解析Fc，提取其中的关键信息(如 BS 和 STmin)。

An RxFcNPdu is used to receive Flow Control Frames (FC) from the CAN bus. CanTp parses the received FC to extract key information (such as BS and STmin).

.. figure:: ../../../_static/参考手册/CanTp/CanTpRxFcNPdu.png
   :alt: CanTpRxFcNPdu
   :name: CanTpRxFcNPdu
   :align: center

   CanTpRxFcNPdu 的配置示意图。 (Schematic Diagram of CanTpRxFcNPdu Configuration)


如图 :ref:`CanTpRxFcNPdu` 所示:

As shown in the Schematic Diagram of CanTpRxFcNPdu Configuration:

 - CanTpRxFcNPduRef：用于唯一标识一个 RxFcNPdu 实例，确保接收到的流控帧能够正确路由到对应的 RxFcNPdu。

   CanTpRxFcNPduRef: Used to uniquely identify an RxFcNPdu instance, ensuring that the received flow control frame can be correctly routed to the corresponding RxFcNPdu.