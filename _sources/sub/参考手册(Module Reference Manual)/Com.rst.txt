Com
#################################

:strong:`缩写词注解 (Abbreviation Notes):`

.. list-table::
   :widths: 34 33 33
   :header-rows: 1

   * - 缩写词 (Abbreviation)
     - 解释/描述 (Explanation/Description)
     - 中文解释 (Chinese explanation)
   * - DM
     - Deadline Monitoring
     - 超时监控 (Timeout Monitoring)
   * - I-PDU
     - Interaction Layer Protocol DataUnit
     - 交互层协议数据单元 (Protocol Data Unit of the Interaction Layer)
   * - L-PDU
     - Data Link Layer Protocol DataUnit
     - 数据链路层协议数据单元 (Data Link Layer Protocol Data Unit)
   * - MDT
     - Minimum Delay Timer
     - 最小延迟时间 (Minimum delay time)
   * - OSEK COM
     - OSEK Communication（opensystems and the correspondinginterfaces for automotiveelectronics）
     - OSEK通信协议 (OSEK Communication Protocol)
   * - TM
     - Transmission Mode
     - I-PDU传输模式 (I-PDU Transmission Mode)
   * - TMC
     - Transmission Mode Condition
     - （信号）传输模式状况 (Transmission mode status)
   * - TMS
     - Transmission Mode Selector
     - (I-PDU)传输模式选择
   * - DET
     - Default Error Tracer
     - 开发错误检测 (Develop error detection)
   * - RTE
     - Runtime environment
     - 运行时环境 (Runtime environment)




简介 (Introduction)
=================================

Com模块主要实现了Signal在I-PDU中的封装及解析功能，为RTE层提供了基于Signal的发送与接收接口，实现了基于Signal的网关功能，实现了PDU的不同发送模式，以及Signal滤波，Update bit，Pdu Counter等功能。

The Com module mainly实现ed the encapsulation and parsing functions of Signal in I-PDU, providing send and receive interfaces based on Signal for the RTE layer. It realized gateway functionality based on Signal, different PDU sending modes, as well as Signal filtering, Update bit, and Pdu Counter functionalities.

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/Com/image1.png
   :alt: Com模块层次图 (Com Module Hierarchy Diagram)
   :name: Com模块层次图 (Com Module Hierarchy Diagram)
   :align: center


Com模块处于AUTOSAR架构中的通信服务层，其下层模块为PduR模块，上层模块为RTE。

The Com module is in the communication service layer of the AUTOSAR architecture, with the PduR module as its lower-layer module and the RTE as its upper-layer module.

参考资料 (Reference materials)
------------------------------------------

[1] AUTOSAR_SRS_COM.pdf，R19-11

[2] AUTOSAR_SWS_COM.pdf，R19-11

[3] AUTOSAR_SWS_PDURouter.pdf，R19-11

功能描述 (Function Description)
===========================================

I-PDU Group功能 (I-PDU Group Function)
----------------------------------------------------

I-PDU Group功能介绍 (Introduction to I-PDU Group Function)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Com模块实现基于I-PDU Group的使能控制，接收超时检测使能控制。根据I-PDU与I-PDU Group的包含关系，间接实现对各个I-PDU的通信使能控制及Rx I-PDU的接收超时检测使能控制。

The Com module implements enable control based on I-PDU Group and receives timeout detection enable control. According to the inclusion relationship between I-PDU and I-PDU Group, it indirectly实现enables communication for each I-PDU and enables reception timeout detection for Rx I-PDU.

I-PDU Group使能控制功能实现 (I-PDU Group Control Function Enabled)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

通过ComIPdu配置参数ComIPduGroupRef，以及ComIPduGroup的配置实现将ComIPdu进行不同的分组。对于不从属于任何ComIPduGroup的ComIPdu其通信使能状态初始化之后一直为Enable且不可动态更改，Rx ComIPdu接收超时使能状态初始化之后一直为Disable且不可动态更改。

By configuring the ComIPdu configuration parameter ComIPduGroupRef and ComIPduGroup, ComIPdus can be grouped in different ways. For ComIPdus that do not belong to any ComIPduGroup, their communication enable state is initialized to Enable and cannot be dynamically changed. The Rx ComIPdu receive timeout enable state is initialized to Disable and cannot be dynamically changed.

IpduGroupVector中的每个bit位代表一个ComIPduGroup，通过调用Com_IpduGroupControl和Com_ReceptionDMControl实现ComIPduGroup通信使能控制和接收超时使能控制，间接实现每个ComIPdu的控制。

Each bit in the IpduGroupVector represents a ComIPduGroup. Communication enable control for ComIPduGroup and reception timeout enable control are achieved through calls to Com_IpduGroupControl and Com_ReceptionDMControl, indirectly controlling each ComIPdu.

Com提供两个接口Com_ClearIpduGroupVector和Com_SetIpduGroup实现对每个ComIPduGroup所在IpduGroupVector中对应bit位置0或置1（0表示Disable，1表示Enable）。

Com provides two interfaces, Com_ClearIpduGroupVector and Com_SetIpduGroup, to set the corresponding bit position in each ComIPduGroup's IpduGroupVector to 0 or 1 (0表示Disable, 1表示Enable).

Signal封装解析功能 (Signal Encapsulation Analysis Function)
---------------------------------------------------------------------

Signal封装解析功能介绍 (Introduction to Signal Packaging and Parsing Function)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

信号的封装和解析是Com模块的核心功能，根据各个信号的配置信息将发送Signal封装到关联的Tx IPdu数据中，从Rx IPdu数据中解析接收Signal。

The encapsulation and parsing of signals are the core functions of the Com module. According to the configuration information of each signal, send signals are encapsulated into associated Tx IPdu data, and received signals are parsed from Rx IPdu data.

Com模块为RTE/应用层提供了完整的基于Signal/SignalGroup的收发接口。

The Com module provides complete send/receive interfaces based on Signal/SignalGroup for the RTE/application layer.

Signal封装解析功能实现 (Signal encapsulation parsing functionality implementation)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

信号的封装和解析涉及的信号配置参数为ComBitPosition，ComBitSize，ComSignalEndianness，ComSignalType，ComSignalLength。Com模块根据这些配置信息，将发送信号值封装到对应IPdu报文数据中，从接收IPdu报文数据中解析出接收信号值。

The encapsulation and parsing of signals involve configuration parameters such as ComBitPosition, ComBitSize, ComSignalEndianness, ComSignalType, and ComSignalLength. The Com module encloses the send signal values in corresponding IPdu message data according to these configuration information and parses the receive signal values from received IPdu message data.

上层通过调用Com_SendSignal来请求非动态长度类型Signal/GroupSignal的发送，调用Com_SendDynSignal来请求动态长度类型（UINT8_DYN）Signal/GroupSignal的发送，调用Com_SendSignalGroup来请求SignalGroup的发送，调用Com_InvalidateSignal来请求Signal发送无效值，调用Com_InvalidateSignalGroup来请求SignalGroup发送无效值，调用Com_SendSignalGroupArray请求上层字节对齐的SignalGroup（已完成各GroupSignal的封装）发送。

The upper layer requests the sending of non-dynamic length types Signal/GroupSignal by calling Com_SendSignal, dynamic length types (UINT8_DYN) Signal/GroupSignal by calling Com_SendDynSignal, SignalGroup by calling Com_SendSignalGroup, invalid value for Signal by calling Com_InvalidateSignal, invalid value for SignalGroup by calling Com_InvalidateSignalGroup, and requests the sending of upper-layer byte-aligned SignalGroup (with each GroupSignal properly encapsulated) by calling Com_SendSignalGroupArray.

上层通过调用Com_ReceiveSignal获取非动态长度类型接收Signal/GroupSignal信号值，调用Com_ReceiveDynSignal获取动态长度类型接收Signal/GroupSignal信号值，调用Com_ReceiveSignalGroup请求SignalGroup的接收，调用Com_ReceiveSignalGroupArray获取字节对齐SignalGroup的数据值。

The upper layer retrieves Signal/GroupSignal signal values for non-dynamic length types by calling Com_ReceiveSignal, retrieves Signal/GroupSignal signal values for dynamic length types by calling Com_ReceiveDynSignal, requests the reception of SignalGroup by calling Com_ReceiveSignalGroup, and obtains byte-aligned SignalGroup data values by calling Com_ReceiveSignalGroupArray.

IPdu收发功能 (IPdu Send and Receive Function)
---------------------------------------------------------

IPdu收发功能介绍 (Introduction to IPdu Reception and Transmission Function)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Com模块实现IPdu的收发方式按数据流分两种类型，即IF方式和TP方式，IF方式通常用于“数据长度较小”的IPdu，而TP方式通常用于“数据长度较大”的IPdu，这里的“数据长度”是相对于传输总线来定义的，如CAN总线为8字节，CANFD为64字节，ETH可以达到1000+字节。其中IF IPdu的发送又分为Direct和TriggerTransmit两种类型，前者发送时机由Com决定，后者发送时机由下层模块决定。

The Com module implements the sending and receiving of IPDUs in two types based on data flow, namely IF mode and TP mode. IF mode is typically used for "shorter data length" IPDUs, while TP mode is usually used for "larger data length" IPDUs. Here, "data length" is defined relative to the communication bus; for example, CAN has 8 bytes, CANFD has 64 bytes, and ETH can reach over 1000 bytes. Among these, the sending of IF IPDUs is divided into Direct and TriggerTransmit types. The former's sending时机is decided by Com, while the latter's sending时机is decided by the lower-level module.

Tx IPdu从发送时机角度又分为四种模式，即PERIODIC，DIRECT，MIXED，NONE。NONE模式通常与TriggerTransmit，或者调用Com_TriggerIPDUSend/Com_TriggerIPDUSendWithMetaData来配置实现IPdu的发送。

Tx IPdu can be divided into four modes from the perspective of transmission时机, namely PERIODIC, DIRECT, MIXED, and NONE. In NONE mode, Tx IPdu is typically configured for sending through TriggerTransmit or by calling Com_TriggerIPDUSend/Com_TriggerIPDUSendWithMetaData.

IPdu收发功能实现 (IPDU Send/Receive Function Implementation)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

通过ComIPdu的配置参数ComIPduType决定该IPdu通过IF/TP方式进行收发：

By configuring the parameter ComIPduType of ComIPdu, it decides whether the IPDU receives and sends data via IF/TP methods:

1.IF发送：PduR_ComTransmit→ Com_TxConfirmation；

IF sends: PduR_ComTransmit → Com_TxConfirmation;

2.IF接收：Com_RxIndication；

IF receive: Com_RxIndication;

3.TP发送：PduR_ComTransmit→N次Com_CopyTxData→ Com_TpTxConfirmation；

TP Send: PduR_ComTransmit→N times Com_CopyTxData→Com_TpTxConfirmation;

4.TP接收：Com_StartOfReception→N次Com_CopyRxData→ Com_TpRxIndication；

TP Reception: Com_StartOfReception → N times Com_CopyRxData → Com_TpRxIndication;

对于Tx IPdu通过配置ComTxModeMode来选择发送模式，对于PERIODIC模式需配置发送偏移ComTxModeTimeOffset和发送周期ComTxModeTimePeriod，对于DIRECT模式需配置发送重复次数ComTxModeNumberOfRepetitions和重复发送报文周期ComTxModeRepetitionPeriod（需重复发送次数＞0），对于MIXED模式需配置以上所有参数，对于NONE模式则不需要配置以上任何参数。

For Tx IPdu to select the sending mode, it is configured through ComTxModeMode. For PERIODIC mode, ComTxModeTimeOffset and ComTxModeTimePeriod need to be configured; for DIRECT mode, ComTxModeNumberOfRepetitions and ComTxModeRepetitionPeriod need to be set (with repeated send count > 0); for MIXED mode, all of the aforementioned parameters should be configured; for NONE mode, no configuration of any of the above parameters is required.

超时监测功能 (Timeout monitoring function)
----------------------------------------------------

超时监测功能介绍 (Timeout Monitoring Feature Introduction)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Com模块实现基于Signal/SignalGroup的超时监测功能。对于发送实现超时通知机制，对于接收实现超时通知和超时替换两种机制。

The Com module implements timeout monitoring functionality based on Signal/SignalGroup. For sending, it realizes a timeout notification mechanism. For receiving, it implements both timeout notification and timeout replacement mechanisms.

超时监测功能实现 (Timeout monitoring function implementation)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

发送超时监测：监测Signal/SignalGroup请求发送到其所在的IPdu发送成功这段时间，IPdu超时时间阈值取请求发送的Signal/SignalGroup配置的超时时间最小值。当发生发送超时，调用各Signal/SignalGroup配置的超时通知函数ComTimeoutNotification通知上层模块。

Timeout Monitoring for Sending: Monitor the period from when Signal/SignalGroup request is sent to its corresponding IPdu sending success, with the IPdu timeout threshold taking the minimum timeout value configured for the Signal/SignalGroup. In case of a send timeout, invoke the timeout notification functions ComTimeoutNotification configured for each Signal/SignalGroup to inform the upper-layer module.

接收超时监测：监测两次正确接收Signal/SignalGroup信号值之间的时间段，Signal/SignalGroup超时时间阈值根据其各自的配置参数决定。当发生超时时，调用其超时通知函数ComTimeoutNotification通知上层模块，也可以将接收信号值替换为初始值（通过配置参数ComRxDataTimeoutAction选择REPLACE实现）或者替换为替代值（通过配置参数ComRxDataTimeoutAction选择SUBSTITUE，且ComSignal配置ComTimeoutSubstitutionValue或者ComGroupSignal配置ComTimeoutSubstitutionValue实现）。

Timeout Monitoring for Reception: Monitor the time interval between two successful receptions of Signal/SignalGroup signal values. The Signal/SignalGroup timeout threshold is decided based on their respective configuration parameters. When a timeout occurs, call its timeout notification function ComTimeoutNotification to inform the upper module. Also, the received signal value can be replaced with an initial value (achieved through configuring ComRxDataTimeoutAction as REPLACE) or with a substitute value (achieved by setting ComRxDataTimeoutAction as SUBSTITUTION and configuring either ComSignal with ComTimeoutSubstitutionValue or ComGroupSignal with ComTimeoutSubstitutionValue).

信号滤波功能 (Signal filtering function)
--------------------------------------------------

信号滤波功能介绍 (Introduction to Signal Filtering Function)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Com模块实现基于信号的信号值进行过滤的机制，虽然对于收发信号的过滤算法一样，但过滤的目的完全不同。

The Com module implements a mechanism for filtering based on signal values, although the filtering algorithms for receiving and sending signals are the same, their purposes are different.

对于接收Signal/SignalGroup，过滤算法未通过时，将舍弃当前接收到的Signal/SignalGroup。

For Signal/SignalGroup reception, if the filtering algorithm fails, the current received Signal/SignalGroup will be discarded.

对于发送Signal/GroupSignal，过滤算法的结果只决定该发送IPdu选择ComTxModeTrue或者ComTxModeFalse进行报文发送，不会舍弃信号本身。

For sending Signal/GroupSignal, the filtering algorithm's result only determines whether to choose ComTxModeTrue or ComTxModeFalse for message transmission, but it does not discard the signal itself.

信号滤波功能实现 (Implementation of Signal Filtering Function)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

通过配置Signal/GroupSignal的ComFilter来选择其过滤算法及算法所需的各种参数，过滤算法的结果分TRUE和FALSE两种。

By configuring the ComFilter of Signal/GroupSignal to select its filtering algorithm and various parameters required by the algorithm, the filtering algorithm results in two types: TRUE and FALSE.

对于接收Signal/SignalGroup只有当通过过滤算法，才将接收信号值更新到接收Buffer中供上层模块获取，未通过过滤算法则舍弃当前接收信号值，不更新接收Buffer中的信号值。对于SignalGroup，只要其包含的任一GroupSignal未通过过滤算法，则整个SignalGroup信号值都将舍弃。

Only when filtered by the filtering algorithm will the received signal value be updated to the receive buffer for the upper module to acquire. If it fails the filter algorithm, the current received signal value will be discarded without updating the signal value in the receive buffer. For a SignalGroup, if any GroupSignal within it fails the filter algorithm, the entire SignalGroup's signal value will be discarded.

对于发送Signal/GroupSignal，若过滤算法通过，其TMC置为TRUE，未通过置为FALSE。只要该IPdu包含的所有Signal/GroupSignal中存在任一TMC为TRUE，则IPdu的TMS为TRUE，否则为FALSE。IPdu根据其TMS选择通过ComTxModeTrue或者ComTxModeFalse进行报文发送，发送Pdu中ComTxIPdu至少需要配置ComTxModeTrue。发送信号的滤波只有在ComTxModeTrue和ComTxModeFalse都配置时才有意义。

For sending Signal/GroupSignal, if the filtering algorithm passes, its TMC is set to TRUE, otherwise FALSE. The IPdu's TMS is TRUE if any of the Signal/GroupSignal within it have a TMC of TRUE; otherwise, it is FALSE. The IPdu sends messages according to its TMS by either ComTxModeTrue or ComTxModeFalse. At least one sending Pdu configured with ComTxModeTrue is required in the sent Pdus. Filtering for sending signals only has meaning when both ComTxModeTrue and ComTxModeFalse are configured.

信号Update功能 (Signal Update Feature)
--------------------------------------------------

信号Update功能介绍 (Signal Update Feature Introduction)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Com模块实现基于Signal/SignalGroup的Update Bit机制来识别信号是否更新（信号更新，但信号值不一定变化）。

The Com module implements an Update Bit mechanism based on Signal/SignalGroup to identify whether a signal has been updated (signal update does not necessarily mean value change).

信号Update功能实现 (Signal update functionality implemented)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Signal/SignalGroup通过配置参数ComUpdateBitPosition来决定是否支持Update机制，Update Bit本身占用IPdu中一个Bit位，该Bit位为1表示对应Signal/SignalGroup有更新，为0表示对应Signal/SignalGroup没有更新。

Signal/SignalGroup uses the configuration parameter ComUpdateBitPosition to decide whether to support the Update mechanism. The Update Bit itself occupies one Bit position in IPdu. This Bit is set to 1 if there is an update for the corresponding Signal/SignalGroup, and it is set to 0 if there is no update.

对于发送信号，当请求Signal/SignalGroup发送时，Com模块将其Update位置1，表示该信号有更新，通过ComTxIPdu的配置参数ComTxIPduClearUpdateBit决定什么时候清除（置0）该发送IPdu中所有的Update位。

For sending signals, when a request to send Signal/SignalGroup is made, the Com module sets its Update position to 1 to indicate that the signal has an update. The ComTxIPduClearUpdateBit configuration parameter determines when to clear (set to 0) all Update bits in the corresponding sent IPdu.

对于接收信号，只有当检测到Signal/SignalGroup的Update位为1，才执行进一步的接收操作，否则舍弃该信号。

For receiving signals, further reception operations are performed only if the Update bit of Signal/SignalGroup is detected as 1; otherwise, the signal is discarded.

IPdu Rolling Counter功能 (IPdu Rolling Counter Function)
----------------------------------------------------------------------

IPdu Rolling Counter功能介绍 (IPdu Rolling Counter Feature Introduction)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Com模块实现基于IPdu的Rolling Counter功能，让IPdu接收端能够识别出IPdu的序列是否正确。

The Com module implements the Rolling Counter function based on IPdu, enabling the IPdu receiver to identify whether the sequence of IPdus is correct.

IPdu Rolling Counter功能实现 (IPdu Rolling Counter Function Implementation)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

对于配置了ComIPduCounter的Tx IPdu，Com每发送一次该IPdu将其Counter值+1，到达Counter最大值之后翻转到0（初始Counter值为0）。Counter值在IPdu中的位置由配置参数ComIPduCounterStartPosition和ComIPduCounterSize决定，需注意的是Counter值所在范围不能跨字节。

For Tx IPdus configured with ComIPduCounter, Com increments the Counter value by 1 each time it sends such an IPdu. The Counter value resets to 0 after reaching its maximum value (initial Counter value is 0). The position of the Counter value within the IPdu is determined by the configuration parameters ComIPduCounterStartPosition and ComIPduCounterSize. Note that the range of the Counter value should not span bytes.

对于配置了ComIPduCounter的Rx IPdu，启动后接收到的第一帧IPdu，其Counter值无论为什么值都匹配成功，之后期望Counter值根据上一次接收IPdu（即使该IPdu的Counter值不匹配）的Counter值+1而定。对于接收Counter是否匹配，需结合当前期望Counter以及ComIPduCounterThreshold来决定。对于Counter不匹配的IPdu，Com将舍弃该IPdu，并可以通过配置ComIPduCounterErrorNotification实现接收Counter错误通知。

For Rx IPdus configured with ComIPduCounter, the first IPdu frame received after startup matches successfully regardless of its Counter value. Thereafter, the expected Counter value is determined by adding 1 to the Counter value of the last received IPdu (even if it did not match). Whether a received Counter matches needs to be decided based on the current expected Counter and ComIPduCounterThreshold. For IPdus with an unmatched Counter, the Com will discard them, and configuration can be made for ComIPduCounterErrorNotification to achieve receipt Counter error notification.

信号网关功能 (Gateway Function for Signaling)
-------------------------------------------------------

信号网关功能介绍 (Function Introduction of Signal Gateway)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Com中信号的网关只针对Signal和GroupSignal，R19_11标准中不再支持基于SignalGroup的网关。信号网关不仅支持1：1，同样支持1：N。

The gateway for signals in Com is only targeting Signal and GroupSignal. The R19_11 standard no longer supports gateways based on SignalGroup. Signal gateways support both 1:1 and 1:N.

对于GwSource信号与GwDestination信号，其信号类型及信号长度必须一致。GwSource信号关联Rx IPdu，GwDestination信号关联Tx IPdu。

For GwSource signals and GwDestination signals, their signal types and lengths must be consistent. GwSource signals are associated with Rx IPdu, while GwDestination signals are associated with Tx IPdu.

注：TP Pdu中的Signal/Group Signal不支持信号网关。

Note: The Signal/Group Signal in TP Pdu does not support signal gateway.

信号网关功能实现 (Function implementation of signal gateway)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

信号网关路由通过配置ComGwMapping实现，信号网关的周期性处理主函数为Com_MainFunctionRouteSignals。

Signal gateway routing is achieved through configuration of ComGwMapping. The periodic processing main function of the signal gateway is Com_MainFunctionRouteSignals.

注：当配置了ComGwMapping时，ComGwSource和ComGwDestination必须要配置具体内容。

Note: When ComGwMapping is configured, both ComGwSource and ComGwDestination must be configured with specific content.

GwSource信号可以通过两种方式进行配置，通过配置ComGwSourceDescription方式和通过配置ComGwSignal方式。前者针对网关Source信号在ComSignal/ComGroupSignal中未配置（上层模块不获取该信号值），后者针对网关Source信号在ComSignal/ComGroupSignal中有配置（不光希望信号被转发，上层模块同样希望获取该信号值），因此前者需要类似配置Signal参数来配置ComGwSourceDescription，而后者只需通过ComGwSignal→ComGwSignalRef关联到ComSignal/ComGroupSignal就行。

The GwSource signal can be configured in two ways: through the configuration of ComGwSourceDescription and through the configuration of ComGwSignal. The former is for when the gateway source signal is not configured in ComSignal/ComGroupSignal (the upper module does not obtain the value of this signal), while the latter is for when it is configured (not only do you want the signal to be forwarded, but the upper module also wants to obtain the value of the signal). Therefore, the former requires configuring similar Signal parameters through ComGwSourceDescription, whereas the latter only needs to associate with ComSignal/ComGroupSignal via ComGwSignal→ComGwSignalRef.

同样GwDestination也可以通过两种方式进行配置，通过配置ComGwDestinationDescription方式和通过配置ComGwSignal方式。前者针对网关Description信号在ComSignal/ComGroupSignal中未配置（上层模块不请求该信号发送），后者针对网关Description信号在ComSignal/ComGroupSignal中有配置（不光希望信号通过网关转发，上层模块同样希望请求该信号发送），因此前者需要类似配置Signal参数来配置ComGwDestinationDescription，而后者只需通过ComGwSignal→ComGwSignalRef关联到ComSignal/ComGroupSignal就行。

Similarly, GwDestination can be configured in two ways: through the configuration of ComGwDestinationDescription and through the configuration of ComGwSignal. The former is for gateway Description signals not being configured in ComSignal/ComGroupSignal (the upper module does not request signal transmission), while the latter is for gateway Description signals being configured in ComSignal/ComGroupSignal (not only do you want the signal to be forwarded through the gateway, but the upper module also requests signal transmission). Therefore, the former requires configuring Signal parameters similar to ComGwDestinationDescription, whereas the latter only needs to associate with ComSignal/ComGroupSignal via ComGwSignal→ComGwSignalRef.

多核分布 (Multi-core Distribution)
----------------------------------------------

多核分布功能介绍 (Introduction to Multi-core Distribution Function)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

为了在多分区（核）之间提供负载分配，通信栈的不同部分可以被分配到不同的分区。不同的网络类型如FlexRay，CAN 和 Ethernet 的部分可以被分配到不同的分区（核）。

To provide load balancing across multiple partitions (cores), different parts of the communication stack can be allocated to separate partitions. Different network types such as FlexRay, CAN, and Ethernet can have their respective parts allocated to different partitions (cores).

为了支持上述灵活的分配，减少分区间的通信（从而潜在的减少跨分区同步带来的阻塞），COM 模块可以按照网络类型创建不同的MainFunction（每个分区至少一个）。在具体的 MainFunction 中仅处理与该网络类型相关的PDU，接收和发送将保持在单个网络范围内（即在单个分区中），因此不需要考虑跨分区同步的问题。唯一的例外是信号网关，当信号网关的源和目的PDU不在同一个分区时，COM模块提供跨分区的数据一致性保护。每个MainFunction 都拥有独立的 Time Base。

To support the above flexible allocation, reduce communication between partitions (thus potentially reducing blocking caused by cross-partition synchronization), the COM module can create different MainFunctions based on network types (with at least one per partition). In specific MainFunctions, only PDU related to that network type is processed; reception and transmission are kept within a single network scope (i.e., within a single partition), so cross-partition synchronization issues do not need to be considered. The only exception is the signal gateway, where the COM module provides data consistency protection across partitions when the source and destination PDU of the signal gateway are in different partitions. Each MainFunction has its own independent Time Base.

多核分布功能实现 (Multi-core distribution functionality implementation)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ComIPdu 通过 ComIPduMainFunctionRef 与特定的 ComMainFunctionRx/ComMainFunctionTx 关联。ComMainFunctionRouteSignalsRef 仅在信号网关目标信号所在的 ComIPdu 上使用。ComMainRxPartitionRef/ComMainTxPartitionRef/ComMainRouteSignalsPartitionRef 分别表示该 ComMainFunction 实例运行的分区。如果配置了分区信息，则ComMainFunction 所在的分区必须与 ComIPdu 关联的Pdu（EcucPduDefaultPartitionRef）的分区一致。此处强调，如果发送IPDU（IPDU或者IPDU包含的信号和组信号）用于信号网关，则其需要同时配置ComIPduMainFunctionRef 关联到ComMainFunctionTx 和配置ComMainFunctionRouteSignalsRef，并且分区一致。

ComIPdu is associated with a specific ComMainFunctionRx / ComMainFunctionTx via ComIPduMainFunctionRef. ComMainFunctionRouteSignalsRef is used only on the ComIPdu where the target signal of the signal gateway is located. ComMainRxPartitionRef/ComMainTxPartitionRef/ComMainRouteSignalsPartitionRef respectively indicate the partition where this ComMainFunction instance runs. If partition information is configured, the partition of the ComMainFunction must be consistent with the PDU (EcucPduDefaultPartitionRef) associated with the ComIPdu. It is emphasized here that if an IPDU for signal gateway usage (IPDU or signals and groups within it) is used, it needs to be configured to have both ComIPduMainFunctionRef associated with ComMainFunctionTx and ComMainFunctionRouteSignalsRef, and the partitions must be consistent.

Com模块如果配置了ComIpduGroup，则其必须被至少一个IPDU关联，且关联在同一个ComIpduGroup的IPDU的分区必须一致。

If the Com module is configured with ComIpduGroup, it must be associated with at least one IPDU, and the partitions of IPDUs associated in the same ComIpduGroup must be consistent.

IPDU的分区信息是在ECUC模块配置实现的，Com模块配置并校验成功后，在ECUC模块右键Synchronize Module选择Com模块进行同步，可以将Com模块的分区信息同步到ECUC模块的IPDU上。

The partition information of IPDU is implemented in the ECUC module configuration. After the Com module configuration and validation are successful, right-clicking Synchronize Module in the ECUC module and selecting the Com module for synchronization can transfer the Com module's partition information to the IPDU on the ECUC module.

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/Com/image2.png
   :alt: EcuC模块同步 (ECuC Module Synchronization)
   :name: EcuC模块同步 (ECuC Module Synchronization)
   :align: center


代码生成器会为每一个 ComMainFunction 生成一个函数（声明在SchM_Com.h）。每一个 ComMainFunction 的实例和API接口在集成时需要被放在正确的分区中被调用。建议开发阶段打开ComConfigurationUseDet配置，存在不合理的分区调用时，可以报Det错误。

The code generator will generate a function for each ComMainFunction (declared in SchM_Com.h). Each instance of ComMainFunction and its API interface need to be called from the correct partition during integration. It is recommended to enable the ComConfigurationUseDet configuration during development; an Det error will be reported if there are unreasonable partition calls.

Com组件文件描述 (Component file description)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 文件 (Files)
     - 说明 (Description)
   * - Com_Cfg.h
     - 定义Com模块PC配置的宏定义。 (Define macros for Com module PC configuration.)
   * - Com_PBcfg.c
     - 定义Com模块PB配置的结构体参数和ComMainFunction的定义。 (Define the structure parameters for Com module PB configuration and the definition of ComMainFunction.)
   * - Com_PBcfg.h
     - 定义Com模块PB配置的宏定义。 (Define macro definitions for Com module PB configuration.)
   * - Com.h
     - 实现Com模块全部外部接口的声明，以及配置文件中全局变量的声明。 (Declare all external interfaces of the Com module and the global variables in the configuration file.)
   * - Com.c
     - 作为Com模块的核心文件，实现Com模块全部对外接口，以及实现Com模块功能所必须的local函数，local宏定义，local变量定义。 (As the core file of the Com module, it implements all external interfaces of the Com module and the local functions, local macro definitions, and local variable definitions necessary for realizing the functionality of the Com module.)
   * - Com_MemMap.h
     - 实现Com模块内存布局。 (Implement Com module memory layout.)
   * - Com_Types.h
     - 实现外部/内部类型的定义，包括AUTOSAR标准定义的类型，以及PB/PC配置参数结构体类型，以及内部运行时结构体类型。 (Define external/internal types, including types defined by the AUTOSAR standard, as well as PB/PC configuration parameter structure types and internal runtime structure types.)
   * - Com_Cbk.h
     - 实现Com模块全部回调函数的声明。 (Implement declarations for all Com module callback functions.)
   * - Com_Callout.c
     - 实现Com模块IPDU配置的Callout回调函数定义。 (Define the Callout callback function for Com module IPDU configuration.)
   * - Com_Callout.h
     - 实现Com模块IPDU配置的Callout回调函数声明。 (Declare the Callout callback function for Com module IPDU configuration.)
   * - Com_Internal.h
     - 实现Com模块内部函数的声明。 (Declare the functions within the Com module.)
   * - Com_Internal.c
     - 实现Com模块公共内部函数的定义。 (Define common internal functions for the Com module.)
   * - Com_GwInternal.c
     - 实现Com模块信号网关功能内部函数的定义。 (Define internal functions for realizing Com module signal gateway functionality.)
   * - Com_RxInternal.c
     - 实现Com模块信号接收内部函数的定义。 (Define the internal function for receiving signals of the Com module.)
   * - Com_TxInternal.c
     - 实现Com模块信号发送内部函数的定义。 (Define the internal function for sending signals in the Com module.)


.. figure:: ../../_static/参考手册(Module_Reference_Manual)/Com/image3.png
   :alt: Com组件文件交互关系图 (Component File Interactions Diagram)
   :name: Com组件文件交互关系图 (Component File Interactions Diagram)
   :align: center


API接口 (API Interface)
=====================================

类型定义 (Type definition)
--------------------------------------

Com_StatusType类型定义 (Definition of Com_StatusType Type)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 名称 (Name)
     - Com_StatusType
   * - 类型 (Type)
     - enum
   * - 范围 (Range)
     - COM_UNINIT = 0x00, COM模块已初始化且可用 (COM_UNINIT = 0x00, The COM module has not been initialized and is unavailable.)
   * - 
     - COM_INIT , COM模块未初始化且不可用 (COM_INIT, COM module is uninitialized and unavailable)
   * - 描述 (Description)
     - Com状态类型 (Com State Type)


Com_SignalIdType类型定义 (Definition of Com_SignalIdType Type)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 名称 (Name)
     - Com_SignalIdType
   * - 类型 (Type)
     - uint16
   * - 范围 (Range)
     - 无 (None)
   * - 描述 (Description)
     - 表示信号的Id号 (ID number for signal representation)


Com_SignalGroupIdType类型定义 (Com_SignalGroupIdType type definition)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 名称 (Name)
     - Com_SignalGroupIdType
   * - 类型 (Type)
     - uint16
   * - 范围 (Range)
     - 无 (None)
   * - 描述 (Description)
     - 表示信号组的Id号 (Indicate the ID number of the signal group)


Com_IpduGroupIdType类型定义 (Type definition for Com_IpduGroupIdType)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 名称 (Name)
     - Com_IpduGroupIdType
   * - 类型 (Type)
     - uint16
   * - 范围 (Range)
     - 无 (None)
   * - 描述 (Description)
     - 表示IpduGroup的Id号 (Indicate the Id number of IpduGroup)


Com_IpduGroupVector类型定义 (Type definition for Com_IpduGroupVector)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 名称 (Name)
     - Com_IpduGroupVector
   * - 类型 (Type)
     - uint8[(ComSupportedIPduGroups-1)/8+1]
   * - 范围 (Range)
     - 无 (None)
   * - 描述 (Description)
     - 表示IpduGroup的使能Flag (Enable Flag for IpduGroup)


Com_ConfigType类型定义 (ConfigType Configuration Type Definition)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 名称 (Name)
     - Com_ConfigType
   * - 类型 (Type)
     - struct
   * - 范围 (Range)
     - 无 (None)
   * - 描述 (Description)
     - 表示Com的PB配置结构体 (Show Com's PB configuration structure)




输入函数描述 (Describe the input function:)
-----------------------------------------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 输入模块 (Input Module)
     - API
   * - Det
     - Det_ReportError
   * - PduR
     - PduR_ComTransmit
   * - 
     - PduR_ComCancelTransmit
   * - <RTE/Up>
     - Com_CbkTxAck
   * - 
     - Com_CbkTxErr
   * - 
     - Com_CbkTxTOut
   * - 
     - Com_CbkRxAck
   * - 
     - Com_CbkRxTOut
   * - 
     - Com_CbkInv
   * - 
     - Com_CbkCounterErr
   * - 
     - Com_RxIpduCallout
   * - 
     - Com_TxIpduCallout




静态接口函数定义 (Static interface function definition)
---------------------------------------------------------------

Com_Init函数定义 (The Com_Init Function Definition)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Com_Init
     - 
     - 
   * - 函数原型： (Function prototype:)
     - voidCom_Init(constCom_ConfigType\*config)
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x01
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 否 (No)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - config
     - 值域： (Domain:)
     - 无 (None)
   * - 输入输出参数： (Input Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 返回值： (Return Value:)
     - 无 (None)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - Com模块初始化函数 (Com module initialization function)
     - 
     - 




Com_DeInit函数定义 (Definition of Com_DeInit function)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Com_DeInit
   * - 函数原型： (Function prototype:)
     - void Com_DeInit(void)
   * - 服务编号： (Service Number:)
     - 0x02
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
   * - 是否可重入： (Is Reentrant:)
     - 否 (No)
   * - 输入参数： (Input parameters:)
     - 无 (None)
   * - 输入输出参数： (Input Output Parameters:)
     - 无 (None)
   * - 输出参数： (Output Parameters:)
     - 无 (None)
   * - 返回值： (Return Value:)
     - 无 (None)
   * - 功能概述： (Function Overview:)
     - Com模块反初始化 (Com module reverse initialization)




Com_IpduGroupControl函数定义 (The_Com_IpduGroupControl_function_definition)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Com_IpduGroupControl
     - 
     - 
   * - 函数原型： (Function prototype:)
     - voidCom_IpduGroupControl(
     - 
     - 
   * - 
     - Com\_IpduGroupVectoripduGroupVector,
     - 
     - 
   * - 
     - booleaninitialize)
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x03
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 否 (No)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - ipduGroupVector
     - 值域： (Domain:)
     - 无 (None)
   * - 
     - initialize
     - 值域： (Domain:)
     - 无 (None)
   * - 输入输出参数： (Input Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 返回值： (Return Value:)
     - 无 (None)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - IpduGroup使能控制 (IpduGroup Enable Control)
     - 
     - 




Com_ReceptionDMControl函数定义 (Com_ReceptionDMControl function definition)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Com_ReceptionDMControl
     - 
     - 
   * - 函数原型： (Function prototype:)
     - voidCom_ReceptionDMControl(
     - 
     - 
   * - 
     - Com_IpduGroupVectoripduGroupVector)
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x06
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 否 (No)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - ipduGroupVector
     - 值域： (Domain:)
     - 无 (None)
   * - 输入输出参数： (Input Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 返回值： (Return Value:)
     - 无 (None)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - IpduGroup接收超时检测使能控制 (Timeout Detection Enable Control for IpduGroup Reception)
     - 
     - 




Com_GetStatus函数定义 (Definition of Com_GetStatus function)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Com_GetStatus
   * - 函数原型： (Function prototype:)
     - Com_StatusType Com_GetStatus(void)
   * - 服务编号： (Service Number:)
     - 0x07
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
   * - 是否可重入： (Is Reentrant:)
     - 是 (yes)
   * - 输入参数： (Input parameters:)
     - 无 (None)
   * - 输入输出参数： (Input Output Parameters:)
     - 无 (None)
   * - 输出参数： (Output Parameters:)
     - 无 (None)
   * - 返回值： (Return Value:)
     - Com_StatusType
   * - 
     - COM_UNINIT：Com模块未初始化 (COM_UNINIT: COM module uninitialized)
   * - 
     - COM_INIT：Com模块已初始化 (COM_INIT: The Com module has been initialized.)
   * - 功能概述： (Function Overview:)
     - 获取模块初始化状态信息 (Get module initialization status information)




Com_GetVersionInfo函数定义 (The function definition for Com_GetVersionInfo)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Com_GetVersionInfo
     - 
     - 
   * - 函数原型： (Function prototype:)
     - voidCom_GetVersionInfo(
     - 
     - 
   * - 
     - Std\_VersionInfoType\*versioninfo)
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x09
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 是 (yes)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - 无 (None)
     - 
     - 
   * - 输入输出参数： (Input Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - versioninfo
     - 值域： (Domain:)
     - 无 (None)
   * - 返回值： (Return Value:)
     - 无 (None)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 获取模块软件版本 (Get Module Software Version)
     - 
     - 




Com_ClearIpduGroupVector函数定义 (The function definition for Com_ClearIpduGroupVector)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Com_ClearIpduGroupVector
     - 
     - 
   * - 函数原型： (Function prototype:)
     - voidCom_ClearIpduGroupVector(
     - 
     - 
   * - 
     - Com_IpduGroupVectoripduGroupVector)
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x1c
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 否 (No)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - 无 (None)
     - 
     - 
   * - 输入输出参数： (Input Output Parameters:)
     - ipduGroupVector
     - 值域： (Domain:)
     - 无 (None)
   * - 输出参数： (Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 返回值： (Return Value:)
     - 无 (None)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - IpduGroupVector清零 (IpduGroupVector Zero Out)
     - 
     - 




Com_SetIpduGroup函数定义 (The Com_SetIpduGroup function definition)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Com_SetIpduGroup
     - 
     - 
   * - 函数原型： (Function prototype:)
     - voidCom_SetIpduGroup(
     - 
     - 
   * - 
     - Com_IpduGroupVectoripduGroupVector,
     - 
     - 
   * - 
     - Com_IpduGroupIdTypeipduGroupId,
     - 
     - 
   * - 
     - boolean bitval)
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x1d
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 否 (No)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - ipduGroupId
     - 值域： (Domain:)
     - 无 (None)
   * - 
     - bitval
     - 值域： (Domain:)
     - 无 (None)
   * - 输入输出参数： (Input Output Parameters:)
     - ipduGroupVector
     - 值域： (Domain:)
     - 无 (None)
   * - 输出参数： (Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 返回值： (Return Value:)
     - 无 (None)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 设置IpduGroup所在的Vector位 (Set the Vector bit for IpduGroup)
     - 
     - 




Com_SendSignal函数定义 (The Com_SendSignal function definition)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Com_SendSignal
     - 
     - 
   * - 函数原型： (Function prototype:)
     - uint8Com_SendSignal(
     - 
     - 
   * - 
     - Com_SignalIdTypeSignalId,
     - 
     - 
   * - 
     - const void\*SignalDataPtr)
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x0a
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 异步 (Asynchronous)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 不同Signal可重入，相同Signal不可重入 (Different Signals are reentrant, same Signal is not reentrant.)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - SignalId
     - 值域： (Domain:)
     - 无 (None)
   * - 
     - SignalDataPtr
     - 值域： (Domain:)
     - 无 (None)
   * - 输入输出参数： (Input Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 返回值： (Return Value:)
     - uint8
     - 
     - 
   * - 
     - E_OK:发送信号请求被成功接收 (E_OK: The signal request was successfully received.)
     - 
     - 
   * - 
     - COM_SERVICE_NOT_AVAILABLE:对应的IpduGroup停止了 (COM_SERVICE_NOT_AVAILABLE: The corresponding IpduGroup has stopped.)
     - 
     - 
   * - 
     - COM_BUSY:对于大型数据类型处理的情况下TP-Buffer被锁定 (COM_BUSY: When TP-Buffer is locked for handling large data types)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 信号发送请求（非动态长度信号） (Signal Send Request (Non-dynamic Length Signal))
     - 
     - 




Com_SendDynSignal函数定义 (The function definition for Com_SendDynSignal)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Com_SendDynSignal
     - 
     - 
   * - 函数原型： (Function prototype:)
     - uint8Com_SendDynSignal(
     - 
     - 
   * - 
     - Com_SignalIdTypeSignalId,
     - 
     - 
   * - 
     - const void\*SignalDataPtr,
     - 
     - 
   * - 
     - uint16 Length)
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x21
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 异步 (Asynchronous)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 不同Signal可重入，相同Signal不可重入 (Different Signals are reentrant, same Signal is not reentrant.)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - SignalId
     - 值域： (Domain:)
     - 无 (None)
   * - 
     - SignalDataPtr
     - 值域： (Domain:)
     - 无 (None)
   * - 
     - Length
     - 值域： (Domain:)
     - 无 (None)
   * - 输入输出参数： (Input Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 返回值： (Return Value:)
     - uint8
     - 
     - 
   * - 
     - E_OK:发送动态信号请求被成功接收 (E_OK: The dynamic signal request was successfully received)
     - 
     - 
   * - 
     - E_NOT_OK:请求发送的长度大于此信号配置的长度 (E_NOT_OK: The length of the request sent is greater than the length configured for this signal)
     - 
     - 
   * - 
     - COM_SERVICE_NOT_AVAILABLE:对应的IpduGroup停止了 (COM_SERVICE_NOT_AVAILABLE: The corresponding IpduGroup has stopped.)
     - 
     - 
   * - 
     - COM_BUSY:TP-Buffer被锁定，上一次TP还未完成发送 (COM_BUSY: TP-Buffer is locked, the previous TP has not yet completed sending)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 动态长度信号发送请求 (Dynamic Length Signal Send Request)
     - 
     - 




Com_ReceiveSignal函数定义 (The_Com_ReceiveSignal_function_definition)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Com_ReceiveSignal
     - 
     - 
   * - 函数原型： (Function prototype:)
     - uint8Com_ReceiveSignal(
     - 
     - 
   * - 
     - Com_SignalIdTypeSignalId,
     - 
     - 
   * - 
     - void\*SignalDataPtr)
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x0b
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 不同Signal可重入，相同Signal不可重入 (Different Signals are reentrant, same Signal is not reentrant.)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - SignalId
     - 值域： (Domain:)
     - 无 (None)
   * - 输入输出参数： (Input Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - SignalDataPtr
     - 值域： (Domain:)
     - 无 (None)
   * - 返回值： (Return Value:)
     - uint8
     - 
     - 
   * - 
     - E_OK:接收信号请求被成功接收 (E_OK: Signal reception request was successfully received)
     - 
     - 
   * - 
     - COM_SERVICE_NOT_AVAILABLE:对应的IpduGroup停止了 (COM_SERVICE_NOT_AVAILABLE: The corresponding IpduGroup has stopped.)
     - 
     - 
   * - 
     - COM_BUSY:对于大型数据类型处理的情况下TP-Buffer被锁定 (COM_BUSY: When TP-Buffer is locked for handling large data types)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 信号接收（非动态长度信号） (Signal Reception (Non-Dynamic Length Signal))
     - 
     - 




Com_ReceiveDynSignal函数定义 (The_Com_ReceiveDynSignal_function_definition)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Com_ReceiveDynSignal
     - 
     - 
   * - 函数原型： (Function prototype:)
     - uint8Com\_ReceiveDynSignal(
     - 
     - 
   * - 
     - Com_SignalIdTypeSignalId,
     - 
     - 
   * - 
     - void\*SignalDataPtr,
     - 
     - 
   * - 
     - uint16\* Length)
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x22
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 不同Signal可重入，相同Signal不可重入 (Different Signals are reentrant, same Signal is not reentrant.)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - SignalId
     - 值域： (Domain:)
     - 无 (None)
   * - 输入输出参数： (Input Output Parameters:)
     - Length
     - 值域： (Domain:)
     - 无 (None)
   * - 输出参数： (Output Parameters:)
     - SignalDataPtr
     - 值域： (Domain:)
     - 无 (None)
   * - 返回值： (Return Value:)
     - uint8
     - 
     - 
   * - 
     - E_OK:接收动态信号请求被成功接收 (E_OK: The request for dynamic signal reception was successfully received.)
     - 
     - 
   * - 
     - E_NOT_OK:长度(在参数中)小于接收到的动态长度信号的长度 (E_NOT_OK: Length (in parameters) less than the received dynamic length signal length)
     - 
     - 
   * - 
     - COM_SERVICE_NOT_AVAILABLE:对应的IpduGroup停止了 (COM_SERVICE_NOT_AVAILABLE: The corresponding IpduGroup has stopped.)
     - 
     - 
   * - 
     - COM_BUSY:TP-Buffer被锁定 (COM_BUSY: TP-Buffer is locked)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 动态长度信号接收请求 (Dynamic length signal reception request)
     - 
     - 




Com_SendSignalGroup函数定义 (The function definition for Com_SendSignalGroup)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Com_SendSignalGroup
     - 
     - 
   * - 函数原型： (Function prototype:)
     - uint8Com_SendSignalGroup(
     - 
     - 
   * - 
     - Com_SignalGroupIdTypeSignalGroupId)
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x0d
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 异步 (Asynchronous)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 不同SignalGroup可重入，相同SignalGroup不可重入 (Different SignalGroup can re-enter, same SignalGroup cannot re-enter.)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - SignalGroupId
     - 值域： (Domain:)
     - 无 (None)
   * - 输入输出参数： (Input Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 返回值： (Return Value:)
     - uint8
     - 
     - 
   * - 
     - E_OK:发送信号组请求被成功接收 (E_OK: The group signal request was successfully received.)
     - 
     - 
   * - 
     - COM_SERVICE_NOT_AVAILABLE:对应的IpduGroup停止了 (COM_SERVICE_NOT_AVAILABLE: The corresponding IpduGroup has stopped.)
     - 
     - 
   * - 
     - COM_BUSY:对于大型数据类型处理的情况下TP-Buffer被锁定 (COM_BUSY: When TP-Buffer is locked for handling large data types)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - SignalGroup发送请求 (SignalGroup sends a request)
     - 
     - 




Com_ReceiveSignalGroup函数定义 (The Com_ReceiveSignalGroup function definition)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Com_ReceiveSignalGroup
     - 
     - 
   * - 函数原型： (Function prototype:)
     - uint8Com\_ReceiveSignalGroup(
     - 
     - 
   * - 
     - Com_SignalGroupIdTypeSignalGroupId)
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x0e
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 不同SignalGroup可重入，相同SignalGroup不可重入 (Different SignalGroup can re-enter, same SignalGroup cannot re-enter.)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - SignalGroupId
     - 值域： (Domain:)
     - 无 (None)
   * - 输入输出参数： (Input Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 返回值： (Return Value:)
     - uint8
     - 
     - 
   * - 
     - E_OK:接收信号组请求被成功接收 (E_OK: The signal group request was successfully received.)
     - 
     - 
   * - 
     - COM_SERVICE_NOT_AVAILABLE:对应的IpduGroup停止了 (COM_SERVICE_NOT_AVAILABLE: The corresponding IpduGroup has stopped.)
     - 
     - 
   * - 
     - COM_BUSY:对于大型数据类型处理的情况下TP-Buffer被锁定 (COM_BUSY: When TP-Buffer is locked for handling large data types)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - SignalGroup接收请求 (SignalGroup receives the request)
     - 
     - 




Com_SendSignalGroupArray函数定义 (The function definition for Com_SendSignalGroupArray)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Com_SendSignalGroupArray
     - 
     - 
   * - 函数原型： (Function prototype:)
     - uint8Com_SendSignalGroupArray(
     - 
     - 
   * - 
     - Com_SignalGroupIdTypeSignalGroupId,
     - 
     - 
   * - 
     - const uint8\*SignalGroupArrayPtr)
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x23
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 异步 (Asynchronous)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 不同SignalGroup可重入，相同SignalGroup不可重入 (Different SignalGroup can re-enter, same SignalGroup cannot re-enter.)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - SignalGroupId
     - 值域： (Domain:)
     - 无 (None)
   * - 
     - SignalGroupArrayPtr
     - 值域： (Domain:)
     - 无 (None)
   * - 输入输出参数： (Input Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 返回值： (Return Value:)
     - uint8
     - 
     - 
   * - 
     - E_OK:发送请求被成功接收 (E_OK: The request was successfully received.)
     - 
     - 
   * - 
     - COM_SERVICE_NOT_AVAILABLE:对应的IpduGroup停止了 (COM_SERVICE_NOT_AVAILABLE: The corresponding IpduGroup has stopped.)
     - 
     - 
   * - 
     - COM_BUSY:对于大型数据类型处理的情况下TP-Buffer被锁定 (COM_BUSY: When TP-Buffer is locked for handling large data types)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - SignalGroupArray的发送请求 (The send request of SignalGroupArray)
     - 
     - 




Com_ReceiveSignalGroupArray函数定义 (The definition of Com_ReceiveSignalGroupArray function)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Com_ReceiveSignalGroupArray
     - 
     - 
     - 
   * - 函数原型： (Function prototype:)
     - uint8Com_ReceiveSignalGroupArray(
     - 
     - 
     - 
   * - 
     - Com_SignalGroupIdTypeSignalGroupId,
     - 
     - 
     - 
   * - 
     - uint8\*SignalGroupArrayPtr)
     - 
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x24
     - 
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 不同SignalGroup可重入，相同SignalGroup不可重入 (Different SignalGroup can re-enter, same SignalGroup cannot re-enter.)
     - 
     - 
     - 
   * - 输入参数： (Input parameters:)
     - SignalGroupId
     - 值域： (Domain:)
     - 
     - 无 (None)
   * - 输入输出参数： (Input Output Parameters:)
     - 无 (None)
     - 
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - SignalGroupArrayPtr
     - 值域： (Domain:)
     - 无 (None)
     - 
   * - 返回值： (Return Value:)
     - uint8
     - 
     - 
     - 
   * - 
     - E_OK:接收请求被成功接收 (E_OK: The request was successfully received)
     - 
     - 
     - 
   * - 
     - COM_SERVICE_NOT_AVAILABLE:对应的IpduGroup停止了 (COM_SERVICE_NOT_AVAILABLE: The corresponding IpduGroup has stopped.)
     - 
     - 
     - 
   * - 
     - COM_BUSY:对于大型数据类型处理的情况下TP-Buffer被锁定 (COM_BUSY: When TP-Buffer is locked for handling large data types)
     - 
     - 
     - 
   * - 功能概述： (Function Overview:)
     - SignalGroupArray的接收请求 (The reception request of SignalGroupArray)
     - 
     - 
     - 




Com_InvalidateSignal函数定义 (The Com_InvalidateSignal function definition)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Com_InvalidateSignal
     - 
     - 
   * - 函数原型： (Function prototype:)
     - uint8Com_InvalidateSignal(Com_SignalIdTypeSignalId)
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x10
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 异步 (Asynchronous)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 不同Signal可重入，不同Signal不可重入 (Different Signals are reentrant, different Signals are not reentrant.)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - SignalId
     - 值域： (Domain:)
     - 无 (None)
   * - 输入输出参数： (Input Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 返回值： (Return Value:)
     - uint8
     - 
     - 
   * - 
     - E_OK:请求被成功接收 (E_OK: The request was successfully received.)
     - 
     - 
   * - 
     - COM_SERVICE_NOT_AVAILABLE:对应的IpduGroup停止了 (COM_SERVICE_NOT_AVAILABLE: The corresponding IpduGroup has stopped.)
     - 
     - 
   * - 
     - COM_BUSY:对于大型数据类型处理的情况下TP-Buffer被锁定 (COM_BUSY: When TP-Buffer is locked for handling large data types)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 请求发送信号的无效值 (Invalid value for sending signal)
     - 
     - 




Com_InvalidateSignalGroup函数定义 (The function definition for Com_InvalidateSignalGroup)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Com_InvalidateSignalGroup
     - 
     - 
   * - 函数原型： (Function prototype:)
     - uint8Com_InvalidateSignalGroup(
     - 
     - 
   * - 
     - Com_SignalGroupIdTypeSignalGroupId)
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x1b
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 异步 (Asynchronous)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 不同SignalGroup可重入，不同SignalGroup不可重入 (Different SignalGroups can reenter, different SignalGroups cannot reenter.)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - SignalGroupId
     - 值域： (Domain:)
     - 无 (None)
   * - 输入输出参数： (Input Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 返回值： (Return Value:)
     - uint8
     - 
     - 
   * - 
     - E_OK:发送请求被成功接收 (E_OK: The request was successfully received.)
     - 
     - 
   * - 
     - COM_SERVICE_NOT_AVAILABLE:对应的IpduGroup停止了 (COM_SERVICE_NOT_AVAILABLE: The corresponding IpduGroup has stopped.)
     - 
     - 
   * - 
     - COM_BUSY:对于大型数据类型处理的情况下TP-Buffer被锁定 (COM_BUSY: When TP-Buffer is locked for handling large data types)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - SignalGroup无效值发送请求 (Invalid value sent for SignalGroup request)
     - 
     - 




Com_TriggerIPDUSend函数定义 (The Function Define for Com_TriggerIPDUSend)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Com_TriggerIPDUSend
     - 
     - 
   * - 函数原型： (Function prototype:)
     - Std_ReturnTypeCom_TriggerIPDUSend(PduIdTypePduId)
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x17
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 否 (No)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - PduId
     - 值域： (Domain:)
     - 无 (None)
   * - 输入输出参数： (Input Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 返回值： (Return Value:)
     - Std_ReturnType
     - 
     - 
   * - 
     - E\_OK:Ipdu触发发送成功 (E_OK:IPDU trigger send success)
     - 
     - 
   * - 
     - E\_NOT\_OK:Ipdu触发发送失败 (E_NOT_OK: IPDU trigger send failed)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - IPdu触发发送请求 (IPdu Trigger Send Request)
     - 
     - 




Com_TriggerIPDUSendWithMetaData函数定义 (The function definition for Com_TriggerIPDUSendWithMetaData)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Com_TriggerIPDUSendWithMetaData
     - 
     - 
   * - 函数原型： (Function prototype:)
     - Std_ReturnTypeCom_TriggerIPDUSendWithMetaData(
     - 
     - 
   * - 
     - PduIdType PduId,
     - 
     - 
   * - 
     - uint8\* MetaData)
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x28
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 否 (No)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - PduId
     - 值域： (Domain:)
     - 无 (None)
   * - 
     - MetaData
     - 值域： (Domain:)
     - 无 (None)
   * - 输入输出参数： (Input Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 返回值： (Return Value:)
     - Std_ReturnType
     - 
     - 
   * - 
     - E\_OK:Ipdu触发发送成功 (E_OK:IPDU trigger send success)
     - 
     - 
   * - 
     - E\_NOT\_OK:Ipdu触发发送失败 (E_NOT_OK: IPDU trigger send failed)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - IPdu发送请求，并请求MetaData值改变 (IPdu sends a request and requests a change in MetaData value)
     - 
     - 




Com_SwitchIpduTxMode函数定义 (The_Com_SwitchIpduTxMode_function_definition)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Com_SwitchIpduTxMode
     - 
     - 
   * - 函数原型： (Function prototype:)
     - voidCom_SwitchIpduTxMode(
     - 
     - 
   * - 
     - PduIdType PduId,
     - 
     - 
   * - 
     - boolean Mode)
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x27
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 否 (No)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - PduId
     - 值域： (Domain:)
     - 无 (None)
   * - 
     - Mode
     - 值域： (Domain:)
     - 无 (None)
   * - 输入输出参数： (Input Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 返回值： (Return Value:)
     - 无 (None)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - IPdu发送模式切换请求 (IPdu Send Mode Switch Request)
     - 
     - 




Com_TriggerTransmit函数定义 (Com_TriggerTransmit function definition)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Com_TriggerTransmit
     - 
     - 
   * - 函数原型： (Function prototype:)
     - Std_ReturnTypeCom_TriggerTransmit(
     - 
     - 
   * - 
     - PduIdType TxPduId,
     - 
     - 
   * - 
     - PduInfoType\*PduInfoPtr)
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x41
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 不同Pdu可重入，相同Pdu不可重入 (Different PDUs can be reentered, while the same PDU cannot be reentered.)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - TxPduId
     - 值域： (Domain:)
     - 无 (None)
   * - 输入输出参数： (Input Output Parameters:)
     - PduInfoPtr
     - 值域： (Domain:)
     - 无 (None)
   * - 输出参数： (Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 返回值： (Return Value:)
     - Std_ReturnType
     - 
     - 
   * - 
     - E_OK：SDU已经被复制 (E_OK: SDU has been copied)
     - 
     - 
   * - 
     - E_NOT_OK：没有SDU数据被复制 (E_NOT_OK: No SDU data was copied)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - IF TxPdu数据请求 (IF TxPdu Data Request)
     - 
     - 




Com_RxIndication函数定义 (Function definition for Com_RxIndication)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Com_RxIndication
     - 
     - 
   * - 函数原型： (Function prototype:)
     - voidCom_RxIndication(
     - 
     - 
   * - 
     - PduIdType RxPduId,
     - 
     - 
   * - 
     - const PduInfoType\*PduInfoPtr)
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x42
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 不同Pdu可重入，相同Pdu不可重入 (Different PDUs can be reentered, while the same PDU cannot be reentered.)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - RxPduId
     - 值域： (Domain:)
     - 无 (None)
   * - 
     - PduInfoPtr
     - 值域： (Domain:)
     - 无 (None)
   * - 输入输出参数： (Input Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 返回值： (Return Value:)
     - 无 (None)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - IF RxPdu接收指示 (IF RxPdu Reception Indication)
     - 
     - 




Com_TpRxIndication函数定义 (Function definition for Com_TpRxIndication)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Com_TpRxIndication
     - 
     - 
   * - 函数原型： (Function prototype:)
     - voidCom_TpRxIndication(
     - 
     - 
   * - 
     - PduIdType id,
     - 
     - 
   * - 
     - Std_ReturnTyperesult)
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x45
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 是 (yes)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - id
     - 值域： (Domain:)
     - 无 (None)
   * - 
     - result
     - 值域： (Domain:)
     - 无 (None)
   * - 输入输出参数： (Input Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 返回值： (Return Value:)
     - 无 (None)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - TP RxPdu接收结束 (TP RxPdu Reception Completed)
     - 
     - 




Com_TxConfirmation函数定义 (The function definition for Com_TxConfirmation)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Com_TxConfirmation
     - 
     - 
   * - 函数原型： (Function prototype:)
     - voidCom_TxConfirmation(
     - 
     - 
   * - 
     - PduIdType TxPduId)
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x40
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 不同Pdu可重入，相同Pdu不可重入 (Different PDUs can be reentered, while the same PDU cannot be reentered.)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - TxPduId
     - 值域： (Domain:)
     - 无 (None)
   * - 输入输出参数： (Input Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 返回值： (Return Value:)
     - 无 (None)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - IF TxPdu发送确认 (IF TxPdu Send Confirmation)
     - 
     - 




Com_TpTxConfirmation函数定义 (The function definition for Com_TpTxConfirmation)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Com_TpTxConfirmation
     - 
     - 
   * - 函数原型： (Function prototype:)
     - voidCom_TpTxConfirmation(
     - 
     - 
   * - 
     - PduIdType id,
     - 
     - 
   * - 
     - Std_ReturnTyperesult)
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x48
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 是 (yes)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - id
     - 值域： (Domain:)
     - 无 (None)
   * - 
     - result
     - 值域： (Domain:)
     - 无 (None)
   * - 输入输出参数： (Input Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 返回值： (Return Value:)
     - 无 (None)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - TP TxPdu发送结束 (TP TxPdu Send Completed)
     - 
     - 




Com_StartOfReception函数定义 (Function definition for Com_StartOfReception)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Com_StartOfReception
     - 
     - 
   * - 函数原型： (Function prototype:)
     - BufReq_ReturnTypeCom_StartOfReception(
     - 
     - 
   * - 
     - PduIdType id,
     - 
     - 
   * - 
     - const PduInfoType\*info,
     - 
     - 
   * - 
     - PduLengthTypeTpSduLength,
     - 
     - 
   * - 
     - PduLengthType\*bufferSizePtr)
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x46
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 是 (yes)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - id
     - 值域： (Domain:)
     - 无 (None)
   * - 
     - info
     - 值域： (Domain:)
     - 无 (None)
   * - 
     - TpSduLength
     - 值域： (Domain:)
     - 无 (None)
   * - 输入输出参数： (Input Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - bufferSizePtr
     - 值域： (Domain:)
     - 无 (None)
   * - 返回值： (Return Value:)
     - BufReq_ReturnType
     - 
     - 
   * - 
     - BUFREQ_OK：请求成功 (BUFREQ_OK：Request Success)
     - 
     - 
   * - 
     - BUFREQ_E_NOT_OK：请求失败 (BUFREQ_E_NOT_OK: Request Failed)
     - 
     - 
   * - 
     - BUFREQ_E_OVFL：无法提供所需长度的缓冲区 (BUFREQ_E_OVFL: Cannot provide buffer of required length)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - TP开始接收数据请求 (TP begins to receive data requests.)
     - 
     - 




Com_CopyRxData函数定义 (The function definition for Com_CopyRxData)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Com_CopyRxData
     - 
     - 
   * - 函数原型： (Function prototype:)
     - BufReq_ReturnTypeCom_CopyRxData(
     - 
     - 
   * - 
     - PduIdType id,
     - 
     - 
   * - 
     - const PduInfoType\*info,
     - 
     - 
   * - 
     - PduLengthType\*bufferSizePtr)
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x44
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 是 (yes)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - id
     - 值域： (Domain:)
     - 无 (None)
   * - 
     - info
     - 值域： (Domain:)
     - 无 (None)
   * - 输入输出参数： (Input Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - bufferSizePtr
     - 值域： (Domain:)
     - 无 (None)
   * - 返回值： (Return Value:)
     - BufReq_ReturnType
     - 
     - 
   * - 
     - BUFREQ_OK:数据拷贝成功 (BUFREQ_OK: Data copy succeeded)
     - 
     - 
   * - 
     - BUFREQ_E_NOT_OK:数据拷贝失败 (BUFREQ_E_NOT_OK: Data copy failed)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - TP RxPdu数据段接收 (TP RxPdu Data Segment Reception)
     - 
     - 




Com_CopyTxData函数定义 (The function definition for Com_CopyTxData)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Com_CopyTxData
     - 
     - 
   * - 函数原型： (Function prototype:)
     - BufReq_ReturnTypeCom_CopyTxData(
     - 
     - 
   * - 
     - PduIdType id,
     - 
     - 
   * - 
     - const PduInfoType\*info,
     - 
     - 
   * - 
     - RetryInfoType\*retry,
     - 
     - 
   * - 
     - PduLengthType\*availableDataPtr)
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x43
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 否 (No)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - id
     - 值域： (Domain:)
     - 无 (None)
   * - 
     - info
     - 值域： (Domain:)
     - 无 (None)
   * - 
     - retry
     - 值域： (Domain:)
     - 无 (None)
   * - 输入输出参数： (Input Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - availableDataPtr
     - 值域： (Domain:)
     - 
   * - 返回值： (Return Value:)
     - BufReq_ReturnType
     - 
     - 
   * - 
     - BUFREQ_OK：数据已按照请求完全复制到发送缓冲区 (BUFREQ_OK：Data has been fully copied to the send buffer as requested.)
     - 
     - 
   * - 
     - BUFREQ_E_BUSY：请求所需数量的Tx数据不可用 (BUFREQ_E_BUSY: The requested quantity of Tx data is unavailable)
     - 
     - 
   * - 
     - BUFREQ_E_NOT_OK：数据复制请求失败 (BUFREQ_E_NOT_OK: Data replication request failed)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - TP TxPdu数据段请求 (TP TxPdu Data Segment Request)
     - 
     - 




Com_MainFunctionRx函数定义 (The Com_MainFunctionRx function definition)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Com_MainFunctionRx
     - 
     - 
   * - 函数原型： (Function prototype:)
     - voidCom_MainFunctionRx(Com\_MainFunctionTypemainFunctionId)
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x18
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 否 (No)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - mainFunctionId
     - 值域： (Domain:)
     - 无 (None)
   * - 输入输出参数： (Input Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 返回值： (Return Value:)
     - 无 (None)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - RxPdu的周期处理函数 (The periodic processing function of RxPdu)
     - 
     - 




Com_MainFunctionTx函数定义 (Com_MainFunctionTx function definition)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Com_MainFunctionTx
     - 
     - 
   * - 函数原型： (Function prototype:)
     - voidCom_MainFunctionTx(Com\_MainFunctionTypemainFunctionId)
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x19
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 否 (No)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - mainFunctionId
     - 值域： (Domain:)
     - 无 (None)
   * - 输入输出参数： (Input Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 返回值： (Return Value:)
     - 无 (None)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - TxPdu的周期处理函数 (The periodic processing function of TxPdu)
     - 
     - 




Com_MainFunctionRouteSignals函数定义 (The Com_MainFunctionRouteSignals function definition)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Com_MainFunctionRouteSignals
     - 
     - 
   * - 函数原型： (Function prototype:)
     - voidCom_MainFunctionRouteSignals(
     - 
     - 
   * - 
     - Com\_MainFunctionTypemainFunctionId
     - 
     - 
   * - 
     - )
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x1a
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 否 (No)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - mainFunctionId
     - 值域： (Domain:)
     - 无 (None)
   * - 输入输出参数： (Input Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 返回值： (Return Value:)
     - 无 (None)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 信号网关的周期处理函数 (Cycle processing function of the signal gateway)
     - 
     -

Com_EnableReceptionDM函数定义 (Function definition for Com_EnableReceptionDM)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称: (Function Name:)
     - Com_EnableReceptionDM
     - 
     - 
   * - 函数原型: (Function prototype:)
     - voidCom_EnableReceptionDM(Com_IpduGroupIdTypeIpduGroupId)
     - 
     - 
   * - 服务编号: (Service Number:)
     - 0x06
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 不同IpduGroupId可重入，相同的IpduGroupId不可重入 (Different IpduGroupId can re-enter, the same IpduGroupId cannot re-enter.)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - IpduGroupId
     - 值域： (Domain:)
     - 
   * - 输入输出参数: (Input Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 返回值： (Return Value:)
     - 无 (None)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 使能接收监控功能 (Enable receiving monitoring functionality)
     - 
     - 




Com_DisableReceptionDM函数定义 (Function definition for Com_DisableReceptionDM)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称: (Function Name:)
     - Com_DisableReceptionDM
     - 
     - 
   * - 函数原型: (Function prototype:)
     - voidCom_DisableReceptionDM(Com_IpduGroupIdTypeIpduGroupId)
     - 
     - 
   * - 服务编号: (Service Number:)
     - 0x05
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 不同IpduGroupId可重入，相同的IpduGroupId不可重入 (Different IpduGroupId can re-enter, the same IpduGroupId cannot re-enter.)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - IpduGroupId
     - 值域： (Domain:)
     - 
   * - 输入输出参数: (Input Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无 (None)
     - 
     - 
   * - 返回值： (Return Value:)
     - 无 (None)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 禁用接收监控功能 (Disable receiving monitoring functionality)
     - 
     - 




可配置函数定义 (Configurable Function Definition)
----------------------------------------------------------

无。

None.

配置 (Configure)
==============================

ComGeneral
--------------------------

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/Com/image4.png
   :alt: ComGeneral
   :name: ComGeneral
   :align: center


.. centered:: **表  ComGeneral (Table  ComGeneral)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - ComCancellationSupport
     - 取值范围 (Range)
     - true/false
     - 默认取值 (Default value)
     - false
   * - 
     - 参数描述 (Parameter Description)
     - 是否使能取消机制 (Is the cancellation mechanism enabled?)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - ComCancellationSupport的使能需要与PduR中配置的ComModule的配置项PduRCancelTransmit使能保持一致 (The enabling of ComCancellationSupport requires consistency with the configuration item PduRCancelTransmit in the ComModule configured in PduR.)
     - 
     - 
   * - ComConfigurationUseDet
     - 取值范围 (Range)
     - true/false
     - 默认取值 (Default value)
     - false
   * - 
     - 参数描述 (Parameter Description)
     - 是否使能Det检测机制 (Is Det detection mechanism enabled?)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 依赖于Det模块的支持 (Dependent on the support of Det module)
     - 
     - 
   * - ComVersionInfoApi
     - 取值范围 (Range)
     - true/false
     - 默认取值 (Default value)
     - false
   * - 
     - 参数描述 (Parameter Description)
     - 是否使能获取模块软件版本 (Is module software version retrieval enabled?)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无 (None)
     - 
     - 
   * - ComEnableMDTForCyclicTransmission
     - 取值范围 (Range)
     - true/false
     - 默认取值 (Default value)
     - true
   * - 
     - 参数描述 (Parameter Description)
     - 对于周期发送是否使能MDT机制（最小发送间隔） (Enable MDT mechanism (minimum sending interval) for periodic sending?)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无 (None)
     - 
     - 
   * - ComEnableSignalGroupArrayApi
     - 取值范围 (Range)
     - True/false
     - 默认取值 (Default value)
     - false
   * - 
     - 参数描述 (Parameter Description)
     - 是否使能SignalGroupArray的收发接口 (Whether to enable the reception and transmission interfaces of SignalGroupArray)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无 (None)
     - 
     - 
   * - ComMetaDataSupport
     - 取值范围 (Range)
     - true/false
     - 默认取值 (Default value)
     - false
   * - 
     - 参数描述 (Parameter Description)
     - 是否使能MetaData机制 (Is the MetaData mechanism enabled?)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无 (None)
     - 
     - 
   * - ComRetryFailedTransmitRequests
     - 取值范围 (Range)
     - true/false
     - 默认取值 (Default value)
     - false
   * - 
     - 参数描述 (Parameter Description)
     - 是否使能发送失败重发机制 (Is the resend mechanism for failed sends enabled?)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无 (None)
     - 
     - 
   * - ComSupportedIPduGroups
     - 取值范围 (Range)
     - 0..65535
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - Com支持最大IPduGroup数目 (Com supports the maximum number of IPDU groups.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 实际配置ComIPduGroups数目应该要≤ComSupportedIPduGroups (The actual configuration of ComIPduGroups should be ≤ ComSupportedIPduGroups.)
     - 
     - 
   * - ComUserCbkHeaderFile
     - 取值范围 (Range)
     - string
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - Com模块需包含的回调函数头文件 (Header files for callback functions that need to be included in the Com module)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - ComUserCbkHeaderFile中添加的string名格式必须为"xxx.h" (The format of string names added in ComUserCbkHeaderFile must be "xxx.h")
     - 
     - 




ComConfig
-------------------------

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/Com/image5.png
   :alt: ComConfig
   :name: ComConfig
   :align: center


.. centered:: **表 ComConfig (Table ComConfig)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - ComDataMemSize
     - 取值范围 (Range)
     - 0..
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 
     - 18446744073709551615
     - 
     - 
   * - 
     - 参数描述 (Parameter Description)
     - PB配置数据最大值 (Maximum PB Configuration Data)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 用于PB配置内存分配，当前不支持 (For PB configuration memory allocation, current support is not available.)
     - 
     - 
   * - ComMaxIPduCnt
     - 取值范围 (Range)
     - 0..
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 
     - 18446744073709551615
     - 
     - 
   * - 
     - 参数描述 (Parameter Description)
     - IPdus的最大配置数目 (The maximum configuration number of IPdus)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 用于PB配置内存分配，当前不支持 (For PB configuration memory allocation, current support is not available.)
     - 
     - 




ComMainFunctionRx
---------------------------------

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/Com/image6.png
   :alt: ComMainFunctionRx
   :name: ComMainFunctionRx
   :align: center


.. centered:: **表 ComMainFunctionRx (Table ComMainFunctionRx)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - ComMainRxTimeBase
     - 取值范围 (Range)
     - 0..3600
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - Com_MainFunctionRx调用周期 (Call Cycle of Com_MainFunctionRx)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 不能配置为0 (Cannot be configured as 0)
     - 
     - 
   * - ComMainRxPartitionRef
     - 取值范围 (Range)
     - string
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 关联EcucPartition (Associate EcucPartition)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - Com存在多分区的情况时，从EcuC的EcucPartitionCollection下配置的多个EcucPartition中关联一个。Com不存在多分区的情况，ComMainRxPartitionRef不需要配置。 (When Com has multiple partitions, associate one from the multiple EcucPartition configurations under Com's EcucPartitionCollection. When Com does not have multiple partitions, ComMainRxPartitionRef does not need to be configured.)
     - 
     - 




ComMainFunctionTx
---------------------------------

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/Com/image7.png
   :alt: ComMainFunctionTx
   :name: ComMainFunctionTx
   :align: center


.. centered:: **表 ComMainFunctionTx (Table ComMainFunctionTx)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - ComMainTxTimeBase
     - 取值范围 (Range)
     - 0..3600
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - Com_MainFunctionTx调用周期 (Call Cycle of Com_MainFunctionTx)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 不能配置为0 (Cannot be configured as 0)
     - 
     - 
   * - ComPreparationNotification
     - 取值范围 (Range)
     - tring
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 发送的信号/信号组准备好进行发送的通知 (Notifications that the sent signal/signal group is ready for transmission)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 当前不支持 (Current unsupported.)
     - 
     - 
   * - ComMainTxPartitionRef
     - 取值范围 (Range)
     - string
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 关联EcucPartition (Associate EcucPartition)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - Com存在多分区的情况时，从EcuC的EcucPartitionCollection下配置的多个EcucPartition中关联一个。Com不存在多分区的情况，ComMainTxPartitionRef不需要配置。 (When Com has multiple partitions, associate one from the multiple EcucPartition configurations under Com's EcucPartitionCollection. When Com does not have multiple partitions, ComMainTxPartitionRef does not need to be configured.)
     - 
     - 




ComMainFunctionRouteSignals
-------------------------------------------

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/Com/image8.png
   :alt: ComMainFunctionRouteSignals
   :name: ComMainFunctionRouteSignals
   :align: center


.. centered:: **表 ComMainFunctionRouteSignals (Table ComMainFunctionRouteSignals)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - ComMainRouteSignalsTimeBase
     - 取值范围 (Range)
     - 0..3600
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - Com_MainFunctionRouteSignals调用周期 (Call Cycle of Com_MainFunctionRouteSignals)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 不能配置为0 (Cannot be configured as 0)
     - 
     - 
   * - ComMainRouteSignalsPartitionRef
     - 取值范围 (Range)
     - string
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 关联EcucPartition (Associate EcucPartition)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - Com存在多分区的情况时，从EcuC的EcucPartitionCollection下配置的多个EcucPartition中关联一个。Com不存在多分区的情况，ComMainRouteSignalsPartitionRef不需要配置。 (When Com has multiple partitions, associate it from one of the multiple EcucPartitions configured under ComC's EcucPartitionCollection. When Com does not have multiple partitions, ComMainRouteSignalsPartitionRef does not need to be configured.)
     - 
     - 




ComIPduGroup
----------------------------

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/Com/image9.png
   :alt: ComIPduGroup
   :name: ComIPduGroup
   :align: center


.. centered:: **表 ComIPduGroup (Table ComIPduGroup)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - ComIPduGroupHandleId
     - 取值范围 (Range)
     - string
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - IPduGroup的Id号 (The Id number of IPduGroup)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 根据ComIPduGroup名自动生成 (Auto-generate based on ComIPduGroup name)
     - 
     - 
   * - ComIPduGroupGroupRef
     - 取值范围 (Range)
     - 索引[ComIPduGroup] (Index[ComIPduGroup])
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 表示该IPduGroup从属于哪些IPduGroup (Indicates which IPduGroups this IPduGroup belongs to.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 该功能暂不支持 (This feature is暂时 unsupported.)
     - 
     - 




ComIPdu
-----------------------

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/Com/image10.png
   :alt: ComIPdu
   :name: ComIPdu
   :align: center

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/Com/image11.png
   :alt: ComIPdu1
   :name: ComIPdu1
   :align: center


.. centered:: **表 ComIPdu (Table ComIPdu)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - ComIPduCallout
     - 取值范围 (Range)
     - string
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - IPdu的Callout回调函数名 (The callback function name of IPdu's Callout)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无 (None)
     - 
     - 
   * - ComIPduCancellationSupport
     - 取值范围 (Range)
     - true/false
     - 默认取值 (Default value)
     - false
   * - 
     - 参数描述 (Parameter Description)
     - 表示该IPdu是否使能取消发送/接收请求 (Indicate whether this IPDU enables disabling send/receive requests.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 依赖于ComCancellationSupport的使能 (Enabling based on ComCancellationSupport dependency)
     - 
     - 
   * - ComIPduDirection
     - 取值范围 (Range)
     - RECEIVE/SEND
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - IPdu接收/发送属性 (IPdu Reception/Send Properties)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - PDU只有ComIPduDirection配置为SEND时，才能添加ComTxIPdu (PDU can only be added when ComIPduDirection is configured as SEND.)
     - 
     - 
   * - ComIPduHandleId
     - 取值范围 (Range)
     - string
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 表示该IPdu (Indicates this IPDU)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 依赖于ComCancellationSupport的使能 (Enabling based on ComCancellationSupport dependency)
     - 
     - 
   * - ComIPduSignalProcessing
     - 取值范围 (Range)
     - DEFERRED/IMMEDIATE
     - 默认取值 (Default value)
     - DEFERRED
   * - 
     - 参数描述 (Parameter Description)
     - 表示该IPdu中信号的处理时机（延迟处理/立即处理） (Indicate when the signal in this IPDU should be processed (delayed processing/immediate processing))
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无 (None)
     - 
     - 
   * - ComIPduTriggerTransmitCallout
     - 取值范围 (Range)
     - string
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 发送IFIPdu的TriggerTransmit回调函数名 (Callback function name for TriggerTransmit to send IFIPdu)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 依赖于上层模块TriggerTransmit接口名 (Dependent on the TriggerTransmit interface name of the upper-layer module)
     - 
     - 
   * - ComIPduType
     - 取值范围 (Range)
     - NORMAL / TP
     - 默认取值 (Default value)
     - NORMAL
   * - 
     - 参数描述 (Parameter Description)
     - 表示该IPdu为IF/TP收发模式 (Indicates that this IPDU is for IF/TP send/receive mode)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无 (None)
     - 
     - 
   * - ComIPduGroupRef
     - 取值范围 (Range)
     - 索引[ComIPduGroup] (Index[ComIPduGroup])
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 表示该IPdu被哪些ComIPduGroup包含 (Indicate which ComIPduGroup contains this IPdu)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无 (None)
     - 
     - 
   * - ComIPduMainFunctionRef
     - 取值范围 (Range)
     - 索引[ComMainFunctionRx,ComMainFunctionTx] (Index[ComMainFunctionRx,ComMainFunctionTx])
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 表示该IPdu属于哪一个Com_MainFunctionRx/Com_MainFunctionTx (Indicates which Com_MainFunctionRx/Com_MainFunctionTx this IPdu belongs to.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 如果定义了多个ComMainFunctionRx或ComMainFunctionTx，则此项必须配置 (If multiple ComMainFunctionRx or ComMainFunctionTx are defined, this must be configured.)
     - 
     - 
   * - ComMainFunctionRouteSignalsRef
     - 取值范围 (Range)
     - 索引[ComMainFunctionRouteSignals] (Index[ComMainFunctionRouteSignals])
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 表示该IPdu将在哪个ComMainFunctionRouteSignals实例上执行信号网关活动 (Indicate on which ComMainFunctionRouteSignals instance the IPDU will execute the signal gateway activity)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 仅在ComGwDestination所在的 IPdu上可选 (Only selectable on the IPdu where ComGwDestination is located.)
     - 
     - 
   * - ComIPduSignalGroupRef
     - 取值范围 (Range)
     - 索引[ComSignalGroup] (Index[ComSignalGroup])
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 表示该IPdu包含哪些ComSignalGroup (Indicates which ComSignalGroup the IPdu contains)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无 (None)
     - 
     - 
   * - ComIPduSignalRef
     - 取值范围 (Range)
     - 索引[ComSignal] (Index[ComSignal])
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 表示该IPdu包含哪些ComSignal (Indicates which ComSignal(s) are contained in this IPdu.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无 (None)
     - 
     - 
   * - ComPduIdRef
     - 取值范围 (Range)
     - 索引[Pdu] (Index[Pdu])
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 关联EcuC中Pdu (Related EcuC Pdu)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 依赖于EcuC中配置的Pdu，Com模块中不能多个Pdu关联ECUC中同一个Pdu;Com中Pdu实际长度（根据包含的信号计算）不能大于ECUC中配置的Pdu长度；动态信号必要位于Pdu的最后部分 (Dependencies on Pdus configured in EcuC require that no multiple Pdus are associated with the same Pdu in Com; the actual length of a Pdu in Com (calculated based on included signals) cannot exceed the Pdu length configured in EcuC; dynamic signals must be located at the last part of the Pdu.)
     - 
     - 




ComIPduCounter
------------------------------

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/Com/image12.png
   :alt: ComIPduCounter
   :name: ComIPduCounter
   :align: center


.. centered:: **表 ComIPduCounter (Table ComIPduCounter)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - ComIPduCounterErrorNotification
     - 取值范围 (Range)
     - string
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 接收IPdu的Counter值不匹配通知接口名 (Notification Interface Name for Mismatched Counter Value of Received IPdu)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无 (None)
     - 
     - 
   * - ComIPduCounterSize
     - 取值范围 (Range)
     - 1..8
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - IPdu的Counter值所占bit位大小 (The bit size of IPdu's Counter value)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - Counter所在范围不能跨字节 (The range of Counter cannot span bytes.)
     - 
     - 
   * - ComIPduCounterStartPosition
     - 取值范围 (Range)
     - 0..4294967295
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - IPdu的Counter起始bit位 (The starting bit position of IPdu's Counter)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - Counter所在范围不能跨字节 (The range of Counter cannot span bytes.)
     - 
     - 
   * - ComIPduCounterThreshold
     - 取值范围 (Range)
     - 0..255
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 接收IPdu的Counter阈值，用于计算有效Counter的范围 (Threshold for IPdu Counter reception, used to calculate the range of valid Counters)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无 (None)
     - 
     - 




ComIPduReplication
----------------------------------

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/Com/image13.png
   :alt: ComIPduReplication
   :name: ComIPduReplication
   :align: center


.. centered:: **表 ComIPduReplication (Table ComIPduReplication)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - ComIPduReplicationQuorum
     - 取值范围 (Range)
     - 1..3
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 表示该IPdu重复接收阈值，只有当正确接收完全相同的多帧报文，该IPdu才执行接收处理。 (Indicates the IPDU duplicate reception threshold, and this IPDU only performs reception processing when correctly receiving entirely identical multi-frame messages.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无 (None)
     - 
     - 




ComTxIPdu
-------------------------

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/Com/image14.png
   :alt: ComTxIPdu
   :name: ComTxIPdu
   :align: center


.. centered:: **表 ComTxIPdu (Table ComTxIPdu)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - ComMetaDataDefault
     - 取值范围 (Range)
     - string
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - IPdu的默认MetaData值 (The default MetaData value of IPdu)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 依赖于ComMetaDataSupport使能，以及关联的EcuC中Pdu配置了MetaData；配置了MetaData的Pdu不能包含动态信号；当Pdu包含MetaData时，需要配置ComMetaDataDefault；ComMetaDataDefault需要以十六进制进行填写，且数据长度必须与ECUC中MetaData类型的长度匹配 (Enable ComMetaDataSupport and associated EcuC Pdu configured with MetaData; Pdus configured with MetaData cannot contain dynamic signals; when a Pdu contains MetaData, ComMetaDataDefault must be configured; ComMetaDataDefault should be filled in hexadecimal and the data length must match the length of MetaData type in EcuC)
     - 
     - 
   * - ComMinimumDelayTime
     - 取值范围 (Range)
     - 0..3600
     - 默认取值 (Default value)
     - 0.0
   * - 
     - 参数描述 (Parameter Description)
     - IPdu发送的最小时间间隔MDT (Minimum Time Interval (MDT) for IPdu transmission)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无 (None)
     - 
     - 
   * - ComTxIPduClearUpdateBit
     - 取值范围 (Range)
     - Confirmation/Transmit/TriggerTransmit
     - 默认取值 (Default value)
     - Confirmation
   * - 
     - 参数描述 (Parameter Description)
     - IPdu中UpdateBit清除时机 (Timing for Clearing UpdateBit in IPdu)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无 (None)
     - 
     - 
   * - ComTxIPduUnusedAreasDefault
     - 取值范围 (Range)
     - 0..255
     - 默认取值 (Default value)
     - 0x0
   * - 
     - 参数描述 (Parameter Description)
     - IPdu未使用字段的默认值 (Default values for unused fields in IPdu)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无 (None)
     - 
     - 




ComTxMode
-------------------------

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/Com/image15.png
   :alt: ComTxMode
   :name: ComTxMode
   :align: center


.. centered:: **表 ComTxMode (Table ComTxMode)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - ComTxModeMode
     - 取值范围 (Range)
     - DIRECT/MIXED/NONE/PERIODIC
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 表示IPdu的发送模式 (Show IPDU transmission mode)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无 (None)
     - 
     - 
   * - ComTxModeNumberOfRepetitions
     - 取值范围 (Range)
     - 0..255
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - IPdu触发发送重复次数 (IPdu Triggered Resend Count)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 只有当配置为DIRECT/MIXED才可配置，ComTxModeNumberOfRepetitions>0时，其包含的信号不能配置update信息 (Only when Configured as DIRECT/MIXED and ComTxModeNumberOfRepetitions > 0, the signals it contains cannot be configured with update information.)
     - 
     - 
   * - ComTxModeRepetitionPeriod
     - 取值范围 (Range)
     - 0..3600
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - IPdu触发发送重复发送间隔周期 (IPdu Triggered Sending Repeated Send Interval Period)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 只有当配置为DIRECT/MIXED，且ComTxModeNumberOfRepetitions配置大于0时才可配置 (Only configure when set to DIRECT/MIXED and the ComTxModeNumberOfRepetitions configuration is greater than 0.)
     - 
     - 
   * - ComTxModeTimeOffset
     - 取值范围 (Range)
     - 0..3600
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - IPdu起始发送偏移时间 (IPdu Initial Send Offset Time)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 只有当配置为PERIODIC/MIXED才可配置 (Only configure when set to PERIODIC/MIXED.)
     - 
     - 
   * - ComTxModeTimePeriod
     - 取值范围 (Range)
     - 0..3600
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - IPdu发送的周期 (The period of IPdu sending)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 只有当配置为PERIODIC/MIXED才可配置 (Only configure when set to PERIODIC/MIXED.)
     - 
     - 




ComSignal
-------------------------

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/Com/image16.png
   :alt: ComSignal
   :name: ComSignal
   :align: center


.. centered:: **表 ComSignal (Table ComSignal)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - ComBitPosition
     - 取值范围 (Range)
     - 0..4294967295
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - 信号起始位置（bit）
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无 (None)
     - 
     - 
   * - ComBitSize
     - 取值范围 (Range)
     - 0..64
     - 默认取值 (Default value)
     - 8
   * - 
     - 参数描述 (Parameter Description)
     - 信号长度（bit）
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 依赖于ComSignalType的配置;信号类型与信号Size范围要匹配;除了UINT8_N、UINT8_DYN信号外，别的信号的Size不能为0 (Depends on the configuration of ComSignalType; the signal type must match the signal Size range; except for UINT8_N and UINT8_DYN signals, the Size of other signals cannot be 0.)
     - 
     - 
   * - ComDataInvalidAction
     - 取值范围 (Range)
     - NOTIFY/REPLACE
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 接收到信号无效值处理方式 (Handling of invalid signal values)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 依赖于ComSignalDataInvalidValue的配置；当ComDataInvalidAction选择为REPLACE时，ComInvalidNotification必须为NULL_PTR;信号的ComSignalDataInvalidValue需与信号类型匹配（UINT8_N、UINT8_DYN信号还涉及与ComSignalLength匹配）
     - 
     - 
   * - ComErrorNotification
     - 取值范围 (Range)
     - string
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 信号发送错误通知函数名 (Function Name for Sending Signal to Error Notification)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 对于发送信号，该配置项才有意义 (For sending signals, this configuration item makes sense.)
     - 
     - 
   * - ComFirstTimeout
     - 取值范围 (Range)
     - 0..3600
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 信号第一次超时时间（start/restart）
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无 (None)
     - 
     - 
   * - ComHandleId
     - 取值范围 (Range)
     - string
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 信号的Id值 (The ID value of the signal)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 根据ComSignal信号名自动生成 (Auto-generate based on ComSignal signal name)
     - 
     - 
   * - ComInitialValueOnly
     - 取值范围 (Range)
     - true/false
     - 默认取值 (Default value)
     - false
   * - 
     - 参数描述 (Parameter Description)
     - 发送信号的信号值是否只能为初始化 (Is the signal value for sending signals limited to initialization only?)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无 (None)
     - 
     - 
   * - ComInvalidNotification
     - 取值范围 (Range)
     - string
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 信号无效通知 (Signal Invalid Notification)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 依赖于ComSignalDataInvalidValue和ComDataInvalidAction的配置 (Configuration dependent on ComSignalDataInvalidValue and ComDataInvalidAction)
     - 
     - 
   * - ComNotification
     - 取值范围 (Range)
     - string
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 信号接收/发送通知函数名 (Signal Reception/Send Notification Function Name)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 根据Rte回调函数命名规则生成 (According to the Rte callback function naming convention generate)
     - 
     - 
   * - ComRxDataTimeoutAction
     - 取值范围 (Range)
     - NONE/REPLACE/SUBSTITUTE
     - 默认取值 (Default value)
     - NONE
   * - 
     - 参数描述 (Parameter Description)
     - 信号超时处理方式 (Timeout handling for signals)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 依赖于ComTimeout/ComFirstTimeout的配置 (Dependent on the configuration of ComTimeout/ComFirstTimeout)
     - 
     - 
   * - ComSignalDataInvalidValue
     - 取值范围 (Range)
     - string
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 信号的无效信号值 (Invalid signal value)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 按十六进制方式，若为数组类型的信号，字节间通过“，”实现；当接收信号配置了ComSignalDataInvalidValue，必须配置ComDataInvalidAction (Using hexadecimal notation, for array-type signals, bytes are separated by ","; when the receive signal is configured with ComSignalDataInvalidValue, ComDataInvalidAction must be configured.)
     - 
     - 
   * - ComSignalEndianness
     - 取值范围 (Range)
     - BIG_ENDIAN/LITTLE_ENDIAN/OPAQUE
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 信号大小端 (Byte Order)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 依赖于ComSignalType的配置 (Dependent on the configuration of ComSignalType)
     - 
     - 
   * - ComSignalInitValue
     - 取值范围 (Range)
     - string
     - 默认取值 (Default value)
     - 0x00
   * - 
     - 参数描述 (Parameter Description)
     - 信号的初始值 (The initial value of the signal)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 按十六进制方式，若为数组类型的信号，字节间通过“，”实现 (In hexadecimal notation, for array-type signals, bytes are separated by ",".)
     - 
     - 
   * - ComSignalLength
     - 取值范围 (Range)
     - 0..4294967295
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 表示UINT8_N/UINT8_DYN信号的字节长度/最大长度 (Indicate the byte length/max length of UINT8_N/UINT8_DYN signal)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 依赖于ComSignalType的配置;UINT8_N、UINT8_DYN信号，signalLength配置值需＞0 (Dependent on the configuration of ComSignalType; signalLength configuration value for UINT8_N and UINT8_DYN signals needs > 0)
     - 
     - 
   * - ComSignalType
     - 取值范围 (Range)
     - BOOLEAN/FLOAT32/FLOAT64/SINT16/SINT32/SINT64/SINT8/UINT16/UINT32/UINT64/UINT8/UINT8_DYN/UINT8_N
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 信号类型 (Signal Type)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 信号类型ComSignalType配置为UINT8_DYN或者UINT8_N时，ComBitPosition必须为字节的最低位 (When ComSignalType is configured as UINT8_DYN or UINT8_N, ComBitPosition must be the lowest bit of a byte.)
     - 
     - 
   * - ComTimeout
     - 取值范围 (Range)
     - 0..3600
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 信号超时时间 (Timeout duration)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无 (None)
     - 
     - 
   * - ComTimeoutNotification
     - 取值范围 (Range)
     - string
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 信号超时通知函数名 (Timeout Notification Function Name)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 依赖于ComTimeout的配置 (Dependent on ComTimeout Configuration)
     - 
     - 
   * - ComTimeoutSubstitutionValue
     - 取值范围 (Range)
     - string
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 发生超时信号的替换值 (Timeout signal's替代值)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 依赖于ComTimeoutAction配置为SUBSTITUTE (Dependent on ComTimeoutAction configured as SUBSTITUTE)
     - 
     - 
   * - ComTransferProperty
     - 取值范围 (Range)
     - PENDING/TRIGGERED/TRIGGERED_ON_CHANGE/TRIGGERED_ON_CHANGE_WITHOUT_REPETITION/TRIGGERED_WITHOUT_REPETITION
     - 默认取值 (Default value)
     - PENDING
   * - 
     - 参数描述 (Parameter Description)
     - 信号触发方式选择 (Signal trigger mode selection)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 依赖于关联的发送IPdu的ComTxModeMode (Dependent on associated sending IPdu的ComTxModeMode)
     - 
     - 
   * - ComUpdateBitPosition
     - 取值范围 (Range)
     - 0..4294967295
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 信号的UpdateBit位置 (The position of UpdateBit in the signal)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无 (None)
     - 
     - 
   * - ComSystemTemplateSystemSignalRef
     - 取值范围 (Range)
     - 索引[I-SIGNAL-TO-I-PDU-MAPPING] (Index[I-Signal-to-I-PDU-Mapping])
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 信号关联索引 (Signal Association Index)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 用于RTE/应用，与Com模块功能无关 (For RTE/application, unrelated to Com module functionality.)
     - 
     - 




ComFilter
-------------------------

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/Com/image17.png
   :alt: ComFilter
   :name: ComFilter
   :align: center


.. centered:: **表 ComFilter (Table ComFilter)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - ComFilterAlgorithm
     - 取值范围 (Range)
     - ALWAYS/   MASKED_NEW_DIFFERS_MASKED_OLD/ MASKED_NEW_DIFFERS_X/ MASKED_NEW_EQUALS_X/   NEVER/ NEW_IS_OUTSIDE/ NEW_IS_WITHIN/ ONE_EVERY_N
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 信号滤波方式 (Filtering signal method)
     - 
     -
   * - 
     - 依赖关系 (Dependencies)
     - ONE_EVERY_N的过滤方式下，ComFilterOffset配置值应<ComFilterPeriod配置值 (The ComFilterOffset configuration value should be < ComFilterPeriod configuration value under the ONE_EVERY_N filtering method.)
     - 
     - 
   * - ComFilterMask
     - 取值范围 (Range)
     - string（十六进制） (hexadecimal string)
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 信号滤波掩码 (Signal Filter Mask)
     - 
     -
   * - 
     - 依赖关系 (Dependencies)
     - 依赖于ComFilterAlgorithm配置类型 (Dependent on the configuration type ComFilterAlgorithm)
     - 
     - 
   * - ComFilterMax
     - 取值范围 (Range)
     - string（十六进制） (hexadecimal string)
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 信号滤波上限值 (Upper limit value for signal filtering)
     - 
     -
   * - 
     - 依赖关系 (Dependencies)
     - 依赖于ComFilterAlgorithm配置类型；ComFilterMin配置值应≤ComFilterMax配置值 (Dependent on ComFilterAlgorithm configuration type; ComFilterMin configuration value should ≤ ComFilterMax configuration value)
     - 
     - 
   * - ComFilterMin
     - 取值范围 (Range)
     - string（十六进制） (hexadecimal string)
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 信号滤波下限值 (Low limit value for signal filtering)
     - 
     -
   * - 
     - 依赖关系 (Dependencies)
     - 依赖于ComFilterAlgorithm配置类型；ComFilterMin配置值应≤ComFilterMax配置值 (Dependent on ComFilterAlgorithm configuration type; ComFilterMin configuration value should ≤ ComFilterMax configuration value)
     - 
     - 
   * - ComFilterOffset
     - 取值范围 (Range)
     - string（十六进制） (hexadecimal string)
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 信号滤波偏移值 (Offset Value for Signal Filtering)
     - 
     -
   * - 
     - 依赖关系 (Dependencies)
     - 依赖于ComFilterAlgorithm配置类型 (Dependent on the configuration type ComFilterAlgorithm)
     - 
     - 
   * - ComFilterPeriod
     - 取值范围 (Range)
     - string（十六进制） (hexadecimal string)
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 信号滤波周期值 (Signal filter period value)
     - 
     -
   * - 
     - 依赖关系 (Dependencies)
     - 依赖于ComFilterAlgorithm配置类型 (Dependent on the configuration type ComFilterAlgorithm)
     - 
     - 
   * - ComFilterX
     - 取值范围 (Range)
     - string（十六进制） (hexadecimal string)
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 信号滤波X值 (Signal Filter X Value)
     - 
     -
   * - 
     - 依赖关系 (Dependencies)
     - 依赖于ComFilterAlgorithm配置类型 (Dependent on the configuration type ComFilterAlgorithm)
     - 
     - 




ComSignalGroup
------------------------------

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/Com/image18.png
   :alt: ComSignalGroup
   :name: ComSignalGroup
   :align: center


.. centered:: **表 ComSignalGroup (Table ComSignalGroup)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - ComDataInvalidAction
     - 取值范围 (Range)
     - NOTIFY/REPLACE
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 接收到信号组无效值处理方式（至少一个GroupSignal接收值为无效值） (Handling of Invalid Values for Signal Group (at least one GroupSignal received an invalid value))
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 依赖于其包含的GroupSignal配置项ComSignalDataInvalidValue的配置 (Dependent on the configuration of ComSignalDataInvalidValue in GroupSignalConfig.)
     - 
     - 
   * - ComErrorNotification
     - 取值范围 (Range)
     - string
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 信号组发送错误通知函数名 (Signal group send error notification function name)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 对于发送信号组，该配置项才有意义 (This configuration item makes sense for signal groups only.)
     - 
     - 
   * - ComFirstTimeout
     - 取值范围 (Range)
     - 0..3600
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 信号组第一次超时时间（start/restart）
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无 (None)
     - 
     - 
   * - ComHandleId
     - 取值范围 (Range)
     - string
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 信号组的Id值 (The Id value of the Signal Group)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 根据信号组名自动生成 (Auto-generate based on signal group name)
     - 
     - 
   * - ComInitialValueOnly
     - 取值范围 (Range)
     - true/false
     - 默认取值 (Default value)
     - false
   * - 
     - 参数描述 (Parameter Description)
     - 发送信号组的信号值是否只能为初始化 (Are the signal values of the signal group limited to initialization only?)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无 (None)
     - 
     - 
   * - ComInvalidNotification
     - 取值范围 (Range)
     - string
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 信号组无效通知（至少一个GroupSignal接收值为无效值） (Invalid notification for signal group (at least one GroupSignal receives an invalid value))
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 依赖于ComDataInvalidAction的配置 (Dependent on the configuration of ComDataInvalidAction)
     - 
     - 
   * - ComNotification
     - 取值范围 (Range)
     - string
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 信号组接收/发送通知函数名 (Signal Group Receive/Send Notification Function Name)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 根据Rte回调函数命名规则生成 (According to the Rte callback function naming convention generate)
     - 
     - 
   * - ComRxDataTimeoutAction
     - 取值范围 (Range)
     - NONE/REPLACE/SUBSTITUTE
     - 默认取值 (Default value)
     - NONE
   * - 
     - 参数描述 (Parameter Description)
     - 信号组超时处理方式 (Timeout handling for signal group)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 依赖于ComTimeout/ComFirstTimeout的配置 (Dependent on the configuration of ComTimeout/ComFirstTimeout)
     - 
     - 
   * - ComSignalGroupArrayAccess
     - 取值范围 (Range)
     - true/false
     - 默认取值 (Default value)
     - false
   * - 
     - 参数描述 (Parameter Description)
     - 是否支持信号组字节对齐方式收发 (Is support for signal group byte alignment for reception and transmission supported?)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 依赖于ComEnableSignalGroupArrayApi使能 (Depends on ComEnableSignalGroupArrayApi Enable)
     - 
     - 
   * - ComTimeout
     - 取值范围 (Range)
     - 0..3600
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 信号组超时时间 (Timeout for Signal Group)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无 (None)
     - 
     - 
   * - ComTimeoutNotification
     - 取值范围 (Range)
     - string
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 信号组超时通知函数名 (Timeout Notification Function Name for Signal Group)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 依赖于ComTimeout的配置 (Dependent on ComTimeout Configuration)
     - 
     - 
   * - ComTransferProperty
     - 取值范围 (Range)
     - PENDING/TRIGGERED/TRIGGERED_ON_CHANGE/TRIGGERED_ON_CHANGE_WITHOUT_REPETITION/TRIGGERED_WITHOUT_REPETITION
     - 默认取值 (Default value)
     - PENDING
   * - 
     - 参数描述 (Parameter Description)
     - 信号组触发方式选择 (Signal group trigger mode selection)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 依赖于关联的发送IPdu的ComTxModeMode (Dependent on associated sending IPdu的ComTxModeMode)
     - 
     - 
   * - ComUpdateBitPosition
     - 取值范围 (Range)
     - 0..4294967295
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 信号组的UpdateBit位置 (The UpdateBit position in the Signal Group)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无 (None)
     - 
     - 
   * - ComSystemTemplateSignalGroupRef
     - 取值范围 (Range)
     - 索引[I-SIGNAL-TO-I-PDU-MAPPING] (Index[I-Signal-to-I-PDU-Mapping])
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 信号组关联索引 (Signal Group Associated Index)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 用于RTE/应用，与Com模块功能无关 (For RTE/application, unrelated to Com module functionality.)
     - 
     - 




ComGroupSignal
------------------------------

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/Com/image19.png
   :alt: ComGroupSignal
   :name: ComGroupSignal
   :align: center


.. centered:: **表 ComGroupSignal (Table ComGroupSignal)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - ComBitPosition
     - 取值范围 (Range)
     - 0..4294967295
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - 信号起始位置（bit）
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无 (None)
     - 
     - 
   * - ComBitSize
     - 取值范围 (Range)
     - 0..64
     - 默认取值 (Default value)
     - 8
   * - 
     - 参数描述 (Parameter Description)
     - 信号长度（Signal Length）
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 依赖于ComSignalType的配置 (Dependent on the configuration of ComSignalType)
     - 
     - 
   * - ComHandleId
     - 取值范围 (Range)
     - string
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 信号的Id值 (The ID value of the signal)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 根据ComGroupSignal信号名自动生成 (Automatically generate based on ComGroupSignal signal name)
     - 
     - 
   * - ComSignalDataInvalidValue
     - 取值范围 (Range)
     - string
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 信号的无效信号值 (Invalid signal value)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 按十六进制方式，若为数组类型的信号，字节间通过“，”实现 (In hexadecimal notation, for array-type signals, bytes are separated by ",".)
     - 
     - 
   * - ComSignalEndianness
     - 取值范围 (Range)
     - BIG_ENDIAN/LITTLE_ENDIAN/OPAQUE
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 信号大小端 (Byte Order)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 依赖于ComSignalType的配置 (Dependent on the configuration of ComSignalType)
     - 
     - 
   * - ComSignalInitValue
     - 取值范围 (Range)
     - string
     - 默认取值 (Default value)
     - 0x00
   * - 
     - 参数描述 (Parameter Description)
     - 信号的初始值 (The initial value of the signal)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 按十六进制方式，若为数组类型的信号，字节间通过“，”实现;信号的ComSignalInitValue需与信号类型匹配（UINT8_N、UINT8_DYN信号还涉及与ComSignalLength匹配）
     - 
     - 
   * - ComSignalLength
     - 取值范围 (Range)
     - 0..4294967295
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 表示UINT8_N/UINT8_DYN信号的字节长度/最大长度 (Indicate the byte length/max length of UINT8_N/UINT8_DYN signal)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 依赖于ComSignalType的配置 (Dependent on the configuration of ComSignalType)
     - 
     - 
   * - ComSignalType
     - 取值范围 (Range)
     - BOOLEAN/FLOAT32/FLOAT64/SINT16/SINT32/SINT64/SINT8/UINT16/UINT32/UINT64/UINT8/UINT8_DYN/UINT8_N
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 信号类型 (Signal Type)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无 (None)
     - 
     - 
   * - ComTimeoutSubstitutionValue
     - 取值范围 (Range)
     - string
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 组信号发生超时的替换值 (Timeout replacement value for group signal)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 依赖于ComRxDataTimeoutAction配置为SUBSTITUTE (Dependent on ComRxDataTimeoutAction configured as SUBSTITUTE)
     - 
     - 
   * - ComTransferProperty
     - 取值范围 (Range)
     - PENDING/TRIGGERED_ON_CHANGE
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 组信号触发方式选择 (Triggering mode selection for group signals)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 只有其关联的SignalGroup配置项ComTransferProperty为TRIGGERED_ON_CHANGE时，才可配置该项 (Only when the configuration item ComTransferProperty of the associated SignalGroup is set to TRIGGERED_ON_CHANGE can this be configured.)
     - 
     - 
   * - ComSystemTemplateSystemSignalRef
     - 取值范围 (Range)
     - 索引[I-SIGNAL-TO-I-PDU-MAPPING] (Index[I-Signal-to-I-PDU-Mapping])
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 组信号关联索引 (Group Signal Association Index)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 用于RTE/应用，与Com模块功能无关 (For RTE/application, unrelated to Com module functionality.)
     - 
     - 




ComGwSignal
---------------------------

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/Com/image20.png
   :alt: ComGwSignal
   :name: ComGwSignal
   :align: center


.. centered:: **表 ComGwSignal (Table ComGwSignal)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - ComGwSignalRef
     - 取值范围 (Range)
     - 索引[ComSignal/ComGroupSignal] (Index[ComSignal/ComGroupSignal])
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 关联ComSignal/ComGroupSignal (Associate ComSignal/ComGroupSignal)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 当为GwSource时关联接收信号，当为GwDestination时关联发送信号；ComGwSignalRef不能重复关联同一个Signal/GroupSignal (When associated with received signals as GwSource, and with sent signals as GwDestination; ComGwSignalRef cannot be repeatedly associated with the same Signal/GroupSignal.)
     - 
     - 




ComGwSourceDescription
--------------------------------------

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/Com/image21.png
   :alt: ComGwSourceDescription
   :name: ComGwSourceDescription
   :align: center


.. centered:: **表 ComGwSourceDescription (Table ComGwSourceDescription)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - ComBitPosition
     - 取值范围 (Range)
     - 0..4294967295
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - 网关信号起始位置（bit）
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无 (None)
     - 
     - 
   * - ComBitSize
     - 取值范围 (Range)
     - 0..64
     - 默认取值 (Default value)
     - 8
   * - 
     - 参数描述 (Parameter Description)
     - 网关信号长度（Gateway Signal Length）
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 依赖于ComSignalType的配置；网关信号的Srouce和Dest信号，其信号Size和信号类型必须要一样 (Dependent on the configuration of ComSignalType; the source and dest signals of gateway signals require the same signal size and type.)
     - 
     - 
   * - ComSignalEndianness
     - 取值范围 (Range)
     - BIG_ENDIAN/LITTLE_ENDIAN/OPAQUE
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 信号大小端 (Byte Order)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 依赖于ComSignalType的配置 (Dependent on the configuration of ComSignalType)
     - 
     - 
   * - ComSignalLength
     - 取值范围 (Range)
     - 0..4294967295
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 表示UINT8_N/UINT8_DYN信号的字节长度/最大长度 (Indicate the byte length/max length of UINT8_N/UINT8_DYN signal)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 依赖于ComSignalType的配置 (Dependent on the configuration of ComSignalType)
     - 
     - 
   * - ComSignalType
     - 取值范围 (Range)
     - BOOLEAN/FLOAT32/FLOAT64/SINT16/SINT32/SINT64/SINT8/UINT16/UINT32/UINT64/UINT8/UINT8_DYN/UINT8_N
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 信号类型 (Signal Type)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无 (None)
     - 
     - 
   * - ComUpdateBitPosition
     - 取值范围 (Range)
     - 0..4294967295
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 信号的UpdateBit位置 (The position of UpdateBit in the signal)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无 (None)
     - 
     - 
   * - ComGwIPduRef
     - 取值范围 (Range)
     - 索引[ComIPdu] (Index[ComIPdu])
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 表示该网关信号所在的接收ComIPdu (Indicate the received ComIPdu where the gateway signal is located.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 只能关联接收ComIPdu (Can only be associated with receiving ComIPdu)
     - 
     - 




ComGwDestinationDescription
-------------------------------------------

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/Com/image22.png
   :alt: ComGwDestinationDescription
   :name: ComGwDestinationDescription
   :align: center


.. centered:: **表 ComGwDestinationDescription (Table ComGwDestinationDescription)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - ComBitPosition
     - 取值范围 (Range)
     - 0..4294967295
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - 网关信号起始位置（Gateway Signal Start Position）
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无 (None)
     - 
     - 
   * - ComSignalEndianness
     - 取值范围 (Range)
     - BIG_ENDIAN/LITTLE_ENDIAN/OPAQUE
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 信号大小端 (Byte Order)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 依赖于ComSignalType的配置 (Dependent on the configuration of ComSignalType)
     - 
     - 
   * - ComSignalInitValue
     - 取值范围 (Range)
     - string
     - 默认取值 (Default value)
     - 0x00
   * - 
     - 参数描述 (Parameter Description)
     - 信号的初始值 (The initial value of the signal)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 按十六进制方式，若为数组类型的信号，字节间通过“，”实现 (In hexadecimal notation, for array-type signals, bytes are separated by ",".)
     - 
     - 
   * - ComTransferProperty
     - 取值范围 (Range)
     - PENDING/TRIGGERED/TRIGGERED_ON_CHANGE/TRIGGERED_ON_CHANGE_WITHOUT_REPETITION/TRIGGERED_WITHOUT_REPETITION
     - 默认取值 (Default value)
     - PENDING
   * - 
     - 参数描述 (Parameter Description)
     - 网关信号触发方式选择 (Gateway signal trigger mode selection)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 依赖于关联的发送IPdu的ComTxModeMode，TxSignalGroup中有一个GroupSignal配置了ComTransferProperty，该TxSignalGroup中别的GroupSignal也必须配置ComTransferProperty (Dependent on the associated sending IPDU's ComTxModeMode, in the TxSignalGroup where one GroupSignal is configured with ComTransferProperty, all other GroupSignals in that TxSignalGroup must also be configured with ComTransferProperty.)
     - 
     - 
   * - ComUpdateBitPosition
     - 取值范围 (Range)
     - 0..4294967295
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 信号的UpdateBit位置 (The position of UpdateBit in the signal)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无 (None)
     - 
     - 
   * - ComGwIPduRef
     - 取值范围 (Range)
     - 索引[ComIPdu] (Index[ComIPdu])
     - 默认取值 (Default value)
     - 无 (None)
   * - 
     - 参数描述 (Parameter Description)
     - 表示该网关信号所在的发送ComIPdu (Indicates the sending ComIPdu where the gateway signal is located)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 只能关联发送ComIPdu (Can only be associated with sending ComIPdu)
     - 
     - 
