Dcm
#################################

:strong:`缩写词注解 (Abbreviation Notes):`

.. list-table::
   :widths: 34 33 33
   :header-rows: 1

   * - 缩写词 (Abbreviation)
     - 解释/描述 (Explanation/Description)
     - 中文解释 (Chinese explanation)
   * - OBD
     - On-Board Diagnostic
     - 车载诊断 (On-board diagnostics)
   * - PDU
     - Protocol Data Unit
     - 协议数据单元 (Protocol Data Unit)
   * - PduR
     - PDU Router
     - PDU路由模块 (PDU Routing Module)
   * - UDS
     - Unified Diagnostic Services
     - 统一诊断服务 (Unified Diagnosis Service)
   * - ECU
     - Electronic Control Unit
     - 电子控制单元 (Electronic Control Unit)
   * - EcuM
     - Electronic Control Unit Manager
     - 电子控制单元管理 (Electronic control unit manages)
   * - Dcm
     - DiagnosticCommunicationManager
     - 诊断通信管理模块 (Diagnostic Communication Management Module)
   * - ComM
     - Communication Manager
     - 通信管理模块 (Communication Management Module)
   * - DSD
     - Diagnostic ServiceDispatcher
     - 诊断服务调度 (Diagnostic Service Scheduling)
   * - DSL
     - Diagnostic Session Layer
     - 诊断会话层 (Diagnose Session Layer)
   * - DSP
     - Diagnostic ServiceProcessing
     - 诊断服务处理 (Diagnostic services handle)
   * - NRC
     - Negative Response Code
     - 负响应码 (Negative response code)
   * - RAM
     - Random Access Memory
     - 随机存取存储器 (Random Access Memory)
   * - Bswmd
     - Basic Software ModuleDescription
     - 基础软件模块描述文件 (Description File for Basic Software Modules)
   * - SW-C
     - Software Component
     - 软件组件 (Software components)
   * - BL
     - BootLoader
     - 引导加载程序 (Boot loader)
   * - 
     - 
     - 


简介 (Introduction)
================================

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/DCM/image1.png
   :alt: Dcm模块层次图 (DCM Module Hierarchy Diagram)
   :name: Dcm模块层次图 (DCM Module Hierarchy Diagram)
   :align: center


Dcm模块实现依据ISO 14229-1和ISO 15031-5等标准规范中定义的UDS诊断和OBD诊断功能。在接收到一个诊断请求后，需要对诊断请求进行分析，包括请求的服务是否支持，寻址方式是否正确，会话级，安全级，长度，子服务等是否正确。一个正确的请求与响应如图 所示。

The Dcm module implements UDS diagnostic and OBD diagnostic functions as defined in standards such as ISO 14229-1 and ISO 15031-5. Upon receiving a diagnostic request, it needs to be analyzed for service support, addressing method, session level, security level, length, sub-service, etc., whether they are correct or not. A correct request and response are shown in the figure.

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/DCM/image2.png
   :alt: 正确请求与响应 (Correct Requests and Responses)
   :name: 正确请求与响应 (Correct Requests and Responses)
   :align: center


在ISO 14229-1协议中，Dcm模块需要实现0x10、0x11、0x14、0x19、0x22、0x23、0x24、0x27、0x28、0x29、0x2A、0x2C、0x2E、0x2F、0x31、0x34、0x35、0x36、0x37、0x38、0x3D、0x3E、0x83、0x84、0x85、0x86、0x87等服务。在ISO 15031-5协议中，Dcm模块需要实现0x01、0x02、0x03、0x04、0x05、0x06、0x07、0x08、0x09、0x0A服务。按照AUTOSAR4.2.2标准规范的定义，Dcm模块还需要对会话级，安全级等进行相应的管理。

In the ISO 14229-1 protocol, the Dcm module needs to implement services 0x10, 0x11, 0x14, 0x19, 0x22, 0x23, 0x24, 0x27, 0x28, 0x29, 0x2A, 0x2C, 0x2E, 0x2F, 0x31, 0x34, 0x35, 0x36, 0x37, 0x38, 0x3D, 0x3E, 0x83, 0x84, 0x85, 0x86, and 0x87. In the ISO 15031-5 protocol, the Dcm module needs to implement services 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, and 0x0A. According to the definition of AUTOSAR 4.2.2 standard specifications, the Dcm module also needs to manage session-level and security-level functionalities accordingly.

按照AUTOSAR4.2.2规范，Dcm模块只能同时处理一个请求，不能进行并行处理，所以推出了协议抢占功能。针对ISO 14229协议中的部分UDS服务按照AUTOSAR4.2.2规范暂不支持，如0x83、0x87、0x84服务暂不实现。在ISO 15031-5协议中，0x05服务不支持，依赖于0x06服务。

According to the AUTOSAR 4.2.2 standard, the Dcm module can only handle one request at a time and cannot process requests in parallel; thus, protocol preemption functionality was introduced. Some UDS services specified in the ISO 14229 protocol are temporarily unsupported according to the AUTOSAR 4.2.2 standard, such as services 0x83, 0x87, and 0x84 which are not currently implemented. In the ISO 15031-5 protocol, service 0x05 is unsupported and relies on service 0x06.

在Dcm模块接收到一个请求后，会根据条件进行处理，给出正响应或者是否定响应；亦或者根据正响应抑制位等处理不给响应。

After receiving a request in the Dcm module, it processes the request based on certain conditions and provides an affirmative or negative response; or it may choose not to respond based on affirmative response suppression bits, etc.

Dcm功能点如下：

Feature points of Dcm include:

1.  Dcm应该按照ISO14229-1中所描述的顺序来进行NRC的发送。UDS服务的标准定义了负响应码(NRC)。Dcm在与其他BSW模块以及SW-C之间的接口中使用这些NRC。

Dcm should send the negative response code (NRC) in the order described in ISO 14229-1 for NRC transmission. UDS services standardly define these NRCs, which Dcm uses in its interfaces with other BSW modules and SW-C.

2.  功能性的“TesterPresent”命令是由测试人员与物理请求/响应并行处理的。这在ISO14229-    1中被称为“保持会话”。这个功能性的“TesterPresent”将在一个单独的DcmRxPduId (UDS func DcmRxPduId)上接收，它与物理请求属于同一个DcmDslConnection。需要使用未显式配置的Dcm内部接收缓冲区，并在DSL层直接进行处理。

The functional "TesterPresent" command is handled concurrently with physical request/response processing by the tester. This is referred to as "keeping the session" in ISO14229-1. This functional "TesterPresent" will be received on a separate DcmRxPduId (UDS func DcmRxPduId), which belongs to the same DcmDslConnection as the physical request. It requires the use of an implicitly configured Dcm internal receive buffer and is processed directly at the DSL layer.

3.  支持周期性发送，UDS服务ReadDataByPeriodicIdentifier     (0x2A)允许测试人员从一个或多个periodicdataidentifier标识的ECU请求定期传输数据记录值。

Supports periodic sending; UDS service ReadDataByPeriodicIdentifier (0x2A) allows testers to request periodic transmission of data record values from one or more ECU using periodic data identifier(s).

4.  事件响应，测试人员使用UDS服务ResponseOnEvent     (0x86)请求ECU启动或停止由指定事件发起的响应的传输。在为传输注册一个事件时，测试人员还指定了相应的服务来响应(e.g：UDS服务ReadDataByIdentifier (0x22))。

Event response, test personnel use the UDS service ResponseOnEvent (0x86) to request the ECU to start or stop transmitting responses initiated by a specified event. When registering an event for transmission, test personnel also specify the corresponding service to respond to (e.g., UDS service ReadDataByIdentifier (0x22)).

5.  分页发送功能，在Dcm的发送缓存空间不够发送一帧很长的数据时，使用分页发送的形式，可以将数据分成很多页来进行一页一页的发送，发送完一页后组装第二页，直到数据发送完。

Pagination sending function, when Dcm's send cache space is not sufficient to send one frame of long data, pagination sending can be used to divide the data into many pages and send them page by page. After sending one page, assemble the second page, until all the data is sent.

6.  管理安全等级，使用0x27服务对安全级进行修改，Dcm模块管理相应的安全级，并判断请求的服务是否在相应的安全级是否可用。

Manage security levels, use the 0x27 service to modify security levels, where the Dcm module manages the corresponding security levels and determines whether the requested service is available at the corresponding security level.

7.  管理会话等级，使用0x10服务对会话级进行修改，Dcm模块管理相应的会话级，并判断请求的服务是否在相应的会话级是否可用。在请求进入到编程会话的时候，Dcm需要配合进行复位跳转到BL。

Manage session levels by using the 0x10 service to modify session-levels. The Dcm module manages the corresponding session levels and determines whether the requested service is available at the corresponding session level. When a request enters the programming session, Dcm needs to cooperate to reset and redirect to BL.

8.  支持不同协议之间的抢占，根据同时请求协议的优先级进行判断，高优先级的抢占低优先级的协议，被抢占的协议停止，开始高优先级协议的处理。

Support preemption between different protocols based on the priority of simultaneously requested protocols, with higher-priority protocols preempting lower-priority ones, stopping the lower-priority protocol and starting the handling of the higher-priority protocol.

9.  通信管理，这个通信管理不是指的0x28服务，是Dcm与ComM模块相互交互的一个管理，包括诊断唤醒之类的，有No_Com,    Silent_Com和Full_Com三种模式。这个会影响Dcm的响应报文是否能够发出。

Communication management, this does not refer to the 0x28 service but rather is the interaction between the Dcm and ComM modules, including diagnostic wake-up functions among others. There are three modes: No_Com, Silent_Com, and Full_Com. This will affect whether Dcm's response messages can be sent out.

10. 支持协议开启临时缓存Queue队列，在一个诊断请求正在处理时，队列缓存最多一个额外请求在Dcm的额外缓存区中，在当前请求结束时接着处理先前缓存的请求。

Support protocols to activate temporary cache queues, where a queue caches at most one additional request in Dcm's extra cache area when a diagnostic request is being processed, and proceeds to handle the previously cached requests upon the current request's completion.

11. 在处理负响应NRC22时，Dcm支持在否定响应报文中额外增加一个字节来存放回复NRC22的具体原因。使用方法：配置工程宏DCM_NRC22_SPECIFIC_CAUSE_CODE为STD_ON，Dcm会在处理NRC0x22时调用Dcm_GetSpecificCauseCode接口获取具体原因字节。若未获取到或为Dcm内部NRC22时，具体原因字节则为默认值0xFF。

When handling negative response NRC22, Dcm supports adding an extra byte to the negative response message to store the specific reason for responding with NRC22. Usage: Configure the engineering macro DCM_NRC22_SPECIFIC_CAUSE_CODE as STD_ON; Dcm will call the Dcm_GetSpecificCauseCode interface to retrieve the specific reason byte when processing NRC0x22. If no byte is retrieved or it is a Dcm internal NRC22, the specific reason byte defaults to 0xFF.

12. 支持提供模块Bswmd文件，右键Dcm选择 update     Bswmd即可生成。若有多分区需求，请在EcuC配置Dcm分区前生成DcmBswmd文件，若EcuC未配置Dcm分区信息，则Dcm在默认分区；若配置，则需要再次生成Dcm Bswmd文件，以更新分区信息。

Support providing module Bswmd files, right-click Dcm and choose update Bswmd to generate it. If multi-partition requirements exist, please generate the DcmBswmd file before configuring Dcm partitions in EcuC; if EcuC has not configured Dcm partition information, Dcm will be in the default partition; if configured, a new generation of Dcm Bswmd file is needed to update partition information.

13. SID识别与正响应抑制处理（带有子服务的服务），格式与子服务检查，服务寻址方式检查等。检查正确后处理相应的服务，检查失败后发送相应的NRC。

SID identification and sub-service negative response suppression processing (with sub-services), format check of sub-services, check of service addressing methods, etc. Process the corresponding service after verification is correct; send the corresponding NRC if the verification fails.

参考资料 (Reference materials)
------------------------------------------

[1] ISO 14229-1 2013

[2] ISO 15031-5 2016

[3] AUTOSAR_SWS_DiagnosticCommunicationManager.PDF，4.2.2

[4] AUTOSAR_SWS_DiagnosticCommunicationManager.PDF，R19-11

[5] AUTOSAR_SWS_DiagnosticEventManager.PDF，4.2.2

[6] AUTOSAR_SWS_DiagnosticEventManager.PDF，4.2.2

功能描述 (Function Description)
===========================================

协议启动功能 (Enable Function According to Agreement)
---------------------------------------------------------------

协议启动功能介绍 (Introduction to Protocol Launch Functionality)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

当Dcm模块接收到一个正确的服务请求之后，需要在处理服务之前将协议启动起来，启动协议需要判断当前是否被运行启动，根据协议启动情况执行后续操作。

When the Dcm module receives a valid service request, it needs to start the protocol before processing the service. Starting the protocol requires determining whether it is already running and executing subsequent operations based on the protocol's startup status.

当Protocol开启Queue队列支持(DcmDslProtocolRequestQueued)时，整体处理流程不变，但如在处理请求过程中收到第二条请求，支持最多一个额外请求的接收，会置入额外缓存区中，待上一条请求完成后会接着处理缓存区中的请求。如缓存区也已满，则返回对应的Buffer状态，无视收到的请求。

When Protocol enables Queue support (DcmDslProtocolRequestQueued), the overall processing flow remains unchanged. However, during request processing, it supports receiving at most one additional request, which is placed in an extra buffer area. Once the previous request is completed, the next request in the buffer area will be processed. If the buffer area is already full, it returns the corresponding Buffer state and ignores any received requests.

协议启动功能实现 (Implementation of Protocol Startup Function)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

当Dcm模块的Dcm_TpRxIndication被调用来接收一个正确的服务请求之后，调用StartProtocol接口来通知用户，让用户判断当前情况下是否允许启动协议，如果允许启动则启动协议并根据配置情况，调用相对应配置的Indication函数通知外部协议启动成功，并执行后续服务；如果协议启动失败则退出处理并发送NRC0x22。

When the Dcm_TpRxIndication of the Dcm module is called to receive a valid service request, call the StartProtocol interface to notify the user to determine whether to start the protocol in the current situation. If allowed, start the protocol and invoke the corresponding configuration Indication function to notify external protocols of successful startup and proceed with subsequent services; if the protocol startup fails, exit processing and send NRC0x22.

服务处理响应功能 (Service Processing Response Function)
---------------------------------------------------------------

服务处理响应功能介绍 (Introduction to Service Processing Response Functionality)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

当Dcm模块接收到一个正确的服务请求之后，在服务正确执行过程中，可能会需要定时发送NRC 0x78来表示服务正在处理过程中，避免请求设备超时，一直到服务处理完成发送出最终响应。

When the Dcm module receives a valid service request and the service is being correctly executed, it may need to periodically send NRC 0x78 to indicate that the service is still processing, in order to avoid timeout on the requesting device, and send the final response only after the service has been processed.

服务处理响应功能实现 (Service processing response functionality implementation)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

当Dcm模块的Dcm_TpRxIndication被调用来接收一个正确的服务请求之后，执行相应的服务，如果在P2ServerMax时间内服务没有处理完成，需要调用PduR_DcmTransmit发送一个NRC 0x78来进行响应，防止请求设备超时。如果在接下来的时间，服务仍未处理完成，则需要在P2*ServerMax到达时调用PduR_DcmTransmit发送一个NRC 0x78来进行响应，如果服务仍未完成则需要在每个P2*ServerMax到达时调用PduR_DcmTransmit发送一个NRC 0x78来进行响应，直到服务处理完成，然后调用PduR_DcmTransmit来发送一个最终响应。

When the Dcm_TpRxIndication of the Dcm module is called to receive a correct service request and the corresponding service is executed, if the service is not processed within P2ServerMax time, PduR_DcmTransmit should be called to send an NRC 0x78 response to prevent the requesting device from timing out. If the service is still not completed in the following period, PduR_DcmTransmit should be called to send an NRC 0x78 at the arrival of P2*ServerMax and then at each subsequent P2*ServerMax until the service is processed, after which PduR_DcmTransmit should be used to send a final response.

更新会话控制时间功能 (Update session control time function)
-----------------------------------------------------------------

更新会话控制时间功能介绍 (Introduction to Update Session Control Timing Function)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

当Dcm模块接收到一个正确的服务请求之后，在服务正确执行完成，响应正确发出之后，对会话时间进行更新。

When the Dcm module receives a correct service request, it updates the session time after the service is correctly executed and the correct response is issued.

更新会话控制时间功能实现 (Implement the updated session control timing feature)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

当Dcm模块的Dcm_TpRxIndication被调用来接收一个正确的服务请求，并在正确处理完服务请求并发出正确响应之后，在调用Dcm_TpTxConfirmation时，对会话时间进行更新，重启会话计时。

When the Dcm_TpRxIndication of the Dcm module is called to receive a valid service request, and after correctly processing the service request and sending a correct response, update the session timer by calling Dcm_TpTxConfirmation and restart the session timer.

通信交互功能 (Communication Interaction Function)
-----------------------------------------------------------

通信交互功能介绍 (Introduction to Communication Interaction Function)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

在默认会话模式下，在收到一个请求时，通知ComM模块启动通信，在请求处理完成，响应发送确认时，通知ComM模块关闭通信。在非默认会话模式下，在收到一个请求时，不会通知ComM模块启动通信，在请求处理完成，响应发送确认时，不会通知ComM模块关闭通信。当默认会话切换到非默认会话的时候，会通知ComM模块启动通信，当非默认会话切换到默认会话的时候，会通知ComM模块关闭通信。ComM模块会在通信状态改变之后，调用Dcm相关接口通知Dcm模块通信状态的改变。

In the default session mode, when a request is received, notify the ComM module to start communication. When the request processing is completed and the response confirmation is sent, notify the ComM module to close communication. In the non-default session mode, when a request is received, do not notify the ComM module to start communication. Upon completion of request processing and sending response confirmation, do not notify the ComM module to close communication. When switching from the default session to the non-default session, notify the ComM module to start communication. When switching from the non-default session to the default session, notify the ComM module to close communication. The ComM module will then call relevant Dcm interfaces to inform the Dcm module of the communication state change after the communication status changes.

通信交互功能实现 (Implementation of Communication Interaction Function)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

当Dcm模块在默认会话模式下被调用Dcm_TpRxIndication，则Dcm模块会先调用ComM_DCM_ActiveDiagnostic通知ComM模块启动通信，然后继续处理服务。当Dcm模块在默认会话模式下被调用Dcm_TpTxConfirmation，则Dcm模块会先调用ComM_DCM_InactiveDiagnostic通知COMM模块关闭通信。

When the Dcm module is called with Dcm_TpRxIndication in the default session mode, the Dcm module first calls ComM_DCM_ActiveDiagnostic to notify the ComM module to start communication, and then continues to process services. When the Dcm module is called with Dcm_TpTxConfirmation in the default session mode, the Dcm module first calls ComM_DCM_InactiveDiagnostic to notify the Comm module to close communication.

当Dcm模块在非默认会话模式下被调用Dcm_TpRxIndication，则Dcm模块不会调用ComM_DCM_ActiveDiagnostic通知ComM模块启动通信，直接继续处理服务。当Dcm模块在非默认会话模式下被调用Dcm_TpTxConfirmation，则Dcm模块不会调用ComM_DCM_InactiveDiagnostic通知ComM模块关闭通信。

When the Dcm module is called with Dcm_TpRxIndication in a non-default session mode, the Dcm module will not call ComM_DCM_ActiveDiagnostic to notify the ComM module to start communication and will continue processing services directly. When the Dcm module is called with Dcm_TpTxConfirmation in a non-default session mode, the Dcm module will not call ComM_DCM_InactiveDiagnostic to notify the ComM module to close communication.

在Dcm模块从默认会话切换到非默认会话的时候，会调用ComM_DCM_ActiveDiagnostic通知ComM模块启动通信。在Dcm模块从非默认会话切换到默认会话的时候，会调用ComM_DCM_InactiveDiagnostic通知ComM模块关闭通信。

When the Dcm module switches from the default session to a non-default session, ComM_DCM_ActiveDiagnostic is called to notify the ComM module to start communication. When the Dcm module switches from a non-default session to the default session, ComM_DCM_InactiveDiagnostic is called to notify the ComM module to stop communication.

当ComM模块状态发送改变之后，会调用Dcm_ComM_NoComModeEntered、Dcm_ComM_SilentComModeEntered和Dcm_ComM_FullComModeEntered接口。在调用Dcm_ComM_NoComModeEntered和Dcm_ComM_SilentComModeEntered接口之后，Dcm模块不能进行报文的发送。在调用Dcm_ComM_FullComModeEntered之后，Dcm模块能对报文进行发送。

After the ComM module state sends a change, the Dcm_ComM_NoComModeEntered, Dcm_ComM_SilentComModeEntered, and Dcm_ComM_FullComModeEntered interfaces are called. After calling the Dcm_ComM_NoComModeEntered and Dcm_ComM_SilentComMode Entered interfaces, the Dcm module cannot send messages. After calling the Dcm_ComM_FullComModeEntered interface, the Dcm module can send messages.

分页发送功能 (Page send functionality)
------------------------------------------------

分页发送功能介绍 (Page Sending Function Introduction)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

在诊断协议中，有些服务允许交换大量数据，如UDS Service 0x19、0x22等。

In diagnostic protocols, some services allow for the exchange of large amounts of data, such as UDS Services 0x19, 0x22, etc.

在传统的方法中，ECU的内部缓冲区必须足够大，以保存将要交换的最长数据消息(最坏情况)，并且在传输开始之前完整的缓冲区被填满。ECU中的RAM内存通常是一种关键资源，特别是在较小的微处理器中。在更节省内存的方法中，缓冲区只被部分填充，部分传输，然后部分填充——以此类推。这种分页机制可以显著减少内存量，但是需要定义良好的反应时间来填充缓冲区。用户可以决定是使用“线性缓冲区”还是分页缓冲区进行诊断。

In traditional methods, the internal buffer of an ECU must be large enough to store the longest data message (worst-case scenario) that is to be exchanged, and the buffer is typically filled completely before transmission begins. RAM memory in ECUs is usually a critical resource, especially in smaller microprocessors. In more memory-saving approaches, the buffer is only partially filled, partially transmitted, then partially refilled – and so on. This paging mechanism can significantly reduce memory usage but requires well-defined response times to refill the buffer. Users can choose between "linear buffers" or paged buffers for diagnostic purposes.

分页发送即是使用有限的发送buffer，将需要发送的超过buffer长度的数据，分页分段进行多次的发送，以达到完整发送的目地。

Pagination sending is using a limited send buffer to segment and send data exceeding the buffer length in multiple iterations, in order to achieve complete transmission.

分页发送功能实现 (Pagination send function implementation)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

在Dcm模块接收到一个服务请求，处理完成之后，发现需要发送的数据长度大于发送缓冲区时且pagedbuffer使能则会按照如下步骤进行处理：

When a service request is received by the Dcm module and processed, if the length of the data to be sent is greater than the send buffer size and pagedbuffer is enabled, the following steps will be taken:

1. 调用DsdInternal_StartPagedProcessing，通过这个API,   DSP子模块将完整的响应长度给Dcm模块，并开始分页缓冲区处理。启动发送，这个API不会实际发送数据。

Call DsdInternal_StartPagedProcessing. Through this API, the DSP sub-module provides the full response length to the Dcm module and starts paged buffer processing. Start sending; this API does not actually send data.

2. 下层调用Dcm_CopyTxData()，然后在接口中调用Dcm_CopyTxData_PagebufferDeal拷贝当前页需要发送数据，当当前页的数据发送完成之后，调用DspInternal_DcmUpdatePage请求更新分页信息和数据。

The lower layer calls Dcm_CopyTxData(), then in the interface, it calls Dcm_CopyTxData_PagebufferDeal to copy the current page's data to be sent. After the data of the current page is sent, it requests an update of the paging information and data by calling DspInternal_DcmUpdatePage.

3. 下层调用Dcm_CopyTxData()，在分页数据没有被更新之前，均返回BUFREQ_E_BUSY。

The lower layer calls Dcm_CopyTxData(), and before the paginated data is updated, it returns BUFREQ_E_BUSY.

4. 下层调用Dcm_CopyTxData()，分页数据被更新之后，调用Dcm_CopyTxData_PagebufferDeal拷贝当前页需要发送数据，并返回BUFREQ_OK。

The lower layer calls Dcm_CopyTxData(), after the paginated data is updated, it calls Dcm_CopyTxData_PagebufferDeal to copy the necessary data for the current page and returns BUFREQ_OK.

5. 如果数据没有被全部发送完，则重复2-4步骤，直到数据全部发送完成并调用Dcm_TpTxConfirmation()。

If the data has not been completely sent, repeat steps 2-4 until all data is sent and Dcm_TpTxConfirmation() is called.

在2-4步骤过程中，分页发送会检测是否当前页发送超时（包括填充和发送整个过程），如果超时则停止发送。

During steps 2-4, pagination sending will detect whether the current page transmission timeout (including padding and the entire sending process) has occurred; if so, it will stop sending.

源文件描述 (Source file description)
===============================================

.. centered:: **表 Dcm组件文件描述 (Table Dcm Component File Description)**

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 文件 (Files)
     - 说明 (Description)
   * - Dcm_Cfg.h
     - 定义Dcm模块预编译时用到的配置参数。 (Define configuration parameters used during pre-compilation of the Dcm module.)
   * - Dcm_Cfg.c
     - 定义Dcm模块配置相关的配置参数。 (Define configuration parameters related to Dcm module configuration.)
   * - Dcm.h
     - Dcm模块头文件，包含了API函数的扩展声明并定义了端口的数据结构。 (Header file for the Dcm module, which includes extended declarations and definitions of API functions and the data structures of ports.)
   * - Dcm.c
     - Dcm模块源文件，包含了API函数的实现。 (Source files for the Dcm module contain the implementation of API functions.)
   * - Dcm_MemMap.h
     - 包含Dcm模块的内存抽象。 (Abstract memory containing the Dcm module.)
   * - Dcm_Types.h
     - 包含Dcm模块需要使用的类型定义。 (Contains type definitions needed for the Dcm module.)
   * - Dcm_Ext.c
     - Dcm模块可供外部使用的函数定义 (Definition of Dcm module functions available for external use)
   * - Dcm_Ext.h
     - Dcm模块可供外部使用的外部变量及函数声明 (External variables and function declarations available for external use in Dcm module)
   * - Dcm_Cbk.h
     - Dcm模块回调接口相关头文件，包含了回调接口相关API函数的扩展声明并定义了端口的数据结构。 (Header file for Dcm module callback interfaces, which includes extended declarations and definitions of API functions related to callback interfaces and port data structures.)
   * - Dcm_Internal.h
     - Dcm模块内部API函数的扩展声明与相关头文件的包含。 (The extension declaration of internal API functions in the Dcm module and the inclusion of related header files.)
   * - DcmDsp.c
     - Dcm模块内部任务处理层的相关API函数实现。 (Implementation of related API functions in the task processing layer of the Dcm module.)
   * - DcmDsd.c
     - Dcm模块内部任务调度层的相关API函数实现。 (Implementation of related API functions for the task scheduling layer within the Dcm module.)
   * - DcmDsl.c
     - Dcm模块内部任务会话层的相关API函数实现。 (The related API functions for the session layer in the Dcm module internal task implementation.)
   * - Dcm_UDS0x10.c
     - Dcm模块UDS服务0x10服务相关函数实现。 (Implementation of functions related to Dcm module UDS service 0x10 service.)
   * - Dcm_UDS0x11.c
     - Dcm模块UDS服务0x11服务相关函数实现。 (Implementation of related functions for Dcm module UDS service 0x11.)
   * - Dcm_UDS0x14.c
     - Dcm模块UDS服务0x14服务相关函数实现。 (Implementation of functions related to Dcm module UDS service 0x14 service.)
   * - Dcm_UDS0x19.c
     - Dcm模块UDS服务0x19服务相关函数实现。 (Implementation of related functions for Dcm module UDS service 0x19.)
   * - Dcm_UDS0x22.c
     - Dcm模块UDS服务0x22服务相关函数实现。 (Implementation of functions related to Dcm module UDS service 0x22.)
   * - Dcm_UDS0x23.c
     - Dcm模块UDS服务0x23服务相关函数实现。 (Implementation of related functions for Dcm module UDS service 0x23.)
   * - Dcm_UDS0x24.c
     - Dcm模块UDS服务0x24服务相关函数实现。 (Implementation of related functions for Dcm module UDS service 0x24.)
   * - Dcm_UDS0x27.c
     - Dcm模块UDS服务0x27服务相关函数实现。 (Implementation of related functions for Dcm module UDS service 0x27.)
   * - Dcm_UDS0x28.c
     - Dcm模块UDS服务0x28服务相关函数实现。 (Implementation of related functions for Dcm module UDS service 0x28.)
   * - Dcm_UDS0x29.c
     - Dcm模块UDS服务0x29服务相关函数实现 (Implementation of Functions Related to Dcm Module UDS Service 0x29)
   * - Dcm_UDS0x2A.c
     - Dcm模块UDS服务0x2A服务相关函数实现。 (Implementation of related functions for Dcm module UDS service 0x2A.)
   * - Dcm_UDS0x2C.c
     - Dcm模块UDS服务0x2C服务相关函数实现。 (Implementation of functions related to Dcm module UDS service 0x2C.)
   * - Dcm_UDS0x2E.c
     - Dcm模块UDS服务0x2E服务相关函数实现。 (Implementation of functions related to Dcm module UDS service 0x2E.)
   * - Dcm_UDS0x2F.c
     - Dcm模块UDS服务0x2F服务相关函数实现。 (Implementation of related functions for Dcm module UDS service 0x2F.)
   * - Dcm_UDS0x31.c
     - Dcm模块UDS服务0x31服务相关函数实现。 (Implementation of related functions for Dcm module UDS service 0x31.)
   * - Dcm_UDS0x34.c
     - Dcm模块UDS服务0x34服务相关函数实现。 (Implementation of related functions for Dcm module UDS service 0x34.)
   * - Dcm_UDS0x35.c
     - Dcm模块UDS服务0x35服务相关函数实现。 (Implementation of related functions for Dcm module UDS service 0x35.)
   * - Dcm_UDS0x36.c
     - Dcm模块UDS服务0x36服务相关函数实现。 (Implementation of related functions for Dcm module UDS service 0x36.)
   * - Dcm_UDS0x37.c
     - Dcm模块UDS服务0x37服务相关函数实现。 (Implementation of functions related to Dcm module UDS service 0x37.)
   * - Dcm_UDS0x38.c
     - Dcm模块UDS服务0x38服务相关函数实现。 (Implementation of related functions for Dcm module UDS service 0x38.)
   * - Dcm_UDS0x3D.c
     - Dcm模块UDS服务0x3D服务相关函数实现。 (Implementation of functions related to DCM module UDS service 0x3D.)
   * - Dcm_UDS0x3E.c
     - Dcm模块UDS服务0x3E服务相关函数实现。 (Implementation of related functions for Dcm module UDS service 0x3E.)
   * - Dcm_UDS0x85.c
     - Dcm模块UDS服务0x85服务相关函数实现。 (Implementation of related functions for Dcm module UDS service 0x85.)
   * - Dcm_UDS0x86.c
     - Dcm模块UDS服务0x86服务相关函数实现。 (Implementation of functions related to Dcm module UDS service 0x86.)
   * - Dcm_OBD0x01.c
     - Dcm模块OBD服务0x01服务相关函数实现。 (Implementation of related functions for Dcm module OBD service 0x01 service.)
   * - Dcm_OBD0x02.c
     - Dcm模块OBD服务0x02服务相关函数实现。 (Implementation of related functions for Dcm module OBD service 0x02.)
   * - Dcm_OBD0x03.c
     - Dcm模块OBD服务0x03服务相关函数实现。 (Implementation of related functions for Dcm module OBD service 0x03.)
   * - Dcm_OBD0x04.c
     - Dcm模块OBD服务0x04服务相关函数实现。 (Implementation of related functions for Dcm module OBD service 0x04.)
   * - Dcm_OBD0x05.c
     - Dcm模块OBD服务0x05服务相关函数实现。 (Implementation of related functions for Dcm module OBD service 0x05.)
   * - Dcm_OBD0x06.c
     - Dcm模块OBD服务0x06服务相关函数实现。 (DCM module OBD service 0x06 related function implementation.)
   * - Dcm_OBD0x07.c
     - Dcm模块OBD服务0x07服务相关函数实现。 (Implementation of related functions for Dcm module OBD service 0x07.)
   * - Dcm_OBD0x08.c
     - Dcm模块OBD服务0x08服务相关函数实现。 (Implementation of related functions for Dcm module OBD service 0x08.)
   * - Dcm_OBD0x09.c
     - Dcm模块OBD服务0x09服务相关函数实现。 (Implementation of related functions for Dcm module OBD service 0x09.)
   * - Dcm_OBD0x0A.c
     - Dcm模块OBD服务0x0A服务相关函数实现。 (Implementation of related functions for Dcm module OBD service 0x0A.)
   * - Rte_Dcm_Type.h
     - 包含Dcm模块与RTE交互需要的配置参数 (Configuration parameters required for interaction between Dcm module and RTE)
   * - Rte_Dcm.h
     - 包含Dcm模块与RTE交互的外部函数声明 (External function declarations for interaction between Dcm module and RTE)
   * - Rte_Dcm.c
     - 定义Dcm模块与RTE交互的函数定义 (Define functions for interaction between Dcm module and RTE)
   * - Dcm_Callout.c
     - Dcm模块Callout接口定义 (DCM module Callout interface definition)
   * - Dcm_Callout.h
     - Dcm模块Callout接口声明 (DCM module Callout interface declaration)
   * - Dcm_CalloutBoot.h
     - Dcm模块与Boot交互相关定义 (Definition related to Dcm module interaction with Boot)
   * - Dcm_MatchFormat.c
     - Dcm模块根据配置（同步异步等）进行接口转换的函数定义 (The function definition for Dcm module to perform interface conversion based on configuration (synchronous, asynchronous, etc.))
   * - Dcm_PBcfg.c
     - Dcm PostBuild配置定义 (Post-build Configuration Definition for Dcm)
   * - Dcm_PBcfg.h
     - Dcm PostBuild配置宏定义 (PostBuild Configuration Macros for Dcm)




.. figure:: ../../_static/参考手册(Module_Reference_Manual)/DCM/image3.png
   :alt: Dcm组件文件交互关系图 (Component File Interaction Diagram for Dcm)
   :name: Dcm组件文件交互关系图 (Component File Interaction Diagram for Dcm)
   :align: center


API接口 (API Interface)
=====================================

类型定义 (Type definition)
--------------------------------------

Dcm_StatusType类型定义 (Definition of Dcm_StatusType Type)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - 名称 (Name)
     - Dcm_StatusType
   * - 类型 (Type)
     - uint8
   * - 范围 (Range)
     - - DCM_E_OK (0x00): This value represents a successful operation.
       - DCM_E_ROE_NOT_ACCEPTED (0x06): ResponseOnOneEvent request is not accepted by DCM (e.g. old ResponseOnOneEvent is not finished) (used at API: Dcm_ResponseOnOneEvent())
       - DCM_E_PERIODICID_NOT_ACCEPTED (0x07): Periodic transmission request is not accepted by DCM (e.g. Dcm_ResponseOnOneDataByPeriodicId())
   * - 描述 (Description)
     - 用于传输状态信息的基本项类型 (Basic item types for transmitting status information)




Dcm_CommunicationModeType类型定义 (Type definition for Dcm_CommunicationModeType)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - 名称 (Name)
     - Dcm_CommunicationModeType
   * - 类型 (Type)
     - uint8
   * - 范围 (Range)
     - - DCM_ENABLE_RX_TX_NORM (0x00): Enable the Rx and Tx for normal communication.
       - DCM_ENABLE_RX_DISABLE_TX_NORM (0x01): Enable the Rx and disable the Tx for normal communication.
       - DCM_DISABLE_RX_ENABLE_TX_NORM (0x02): Disable the Rx and enable the Tx for normal communication.
       - DCM_DISABLE_RX_TX_NORMAL (0x03): Disable Rx and Tx for normal communication.
       - DCM_ENABLE_RX_TX_NM (0x04): Enable the Rx and Tx for network management communication.
       - DCM_ENABLE_RX_DISABLE_TX_NM (0x05): Enable Rx and disable the Tx for network management communication.
       - DCM_DISABLE_RX_ENABLE_TX_NM (0x06): Disable the Rx and enable the Tx for network management communication.
       - DCM_DISABLE_RX_TX_NM (0x07): Disable Rx and Tx for network management communication.
       - DCM_ENABLE_RX_TX_NORM_NM (0x08): Enable Rx and Tx for normal and network management communication.
       - DCM_ENABLE_RX_DISABLE_TX_NORM_NM (0x09): Enable the Rx and disable the Tx for normal and network management communication.
       - DCM_DISABLE_RX_ENABLE_TX_NORM_NM (0x0A): Disable the Rx and enable the Tx for normal and network management communication.
       - DCM_DISABLE_RX_TX_NORM_NM (0x0B): Disable Rx and Tx for normal and network management communication.
   * - 描述 (Description)
     - 通信控制模式类型定义 (Definition of Communication Control Mode Types)




Dcm_ConfigType类型定义 (Definition of Dcm_ConfigType Type)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - 名称 (Name)
     - Dcm_ConfigType
   * - 类型 (Type)
     - Structure
   * - 范围 (Range)
     - Implementation specific (无)
   * - 描述 (Description)
     - 配置类型定义 (Configuration type definition)




Dcm_ReturnReadMemoryType类型定义 (Dcm_ReturnReadMemoryType type definition)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - 名称 (Name)
     - Dcm_ReturnReadMemoryType
   * - 类型 (Type)
     - uint8
   * - 范围 (Range)
     - - DCM_READ_OK (0x00): Reading has been done.
       - DCM_READ_PENDING (0x01): Reading is pending, another call is requested to finalize the reading.
       - DCM_READ_FAILED (0x02): Reading has failed.
       - DCM_READ_FORCE_RCRRP (0x03): Reading is pending, the response pending transmission starts immediately.
   * - 描述 (Description)
     - 读取内存返回值类型定义 (Define return value type for memory read)




Dcm_ReturnWriteMemoryType类型定义 (Type definition for Dcm_ReturnWriteMemoryType)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - 名称 (Name)
     - Dcm_ReturnWriteMemoryType
   * - 类型 (Type)
     - uint8
   * - 范围 (Range)
     - - DCM_WRITE_OK (0x00): Writing has been done.
       - DCM_WRITE_PENDING (0x01): Writing is pending, another call is requested.
       - DCM_WRITE_FAILED (0x02): The writing has failed.
       - DCM_WRITE_FORCE_RCRRP (0x03): Writing is pending, the response pending transmission starts immediately.
   * - 描述 (Description)
     - 写内存返回值类型定义 (Define return value type for writing)




Dcm_EcuStartModeType类型定义 (Dcm_EcuStartModeType Type Definition)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - 名称 (Name)
     - Dcm_EcuStartModeType
   * - 类型 (Type)
     - uint8
   * - 范围 (Range)
     - - DCM_COLD_START (0x00): The ECU starts normally.
       - DCM_WARM_START (0x01): The ECU starts from a bootloader jump.
   * - 描述 (Description)
     - ECU启动类型定义 (Definition of ECU Boot Type)




Dcm_ProgConditionsType类型定义 (Type definition for Dcm_ProgConditionsType)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - 名称 (Name)
     - Dcm_ProgConditionsType
   * - 类型 (Type)
     - Structure
   * - 范围 (Range)
     - - uint16 TesterSourceAddr: Tester source address configured per protocol.
       - uint8 ProtocolId: Id of the protocol on which the request has been received.
       - uint8 Sid: Service identifier of the received request.
       - uint8 SubFncId: Identifier of the received subfunction.
       - boolean ReprogramingRequest: Set to true in order to request reprogramming of the ECU. HIS representation of FL_ExtProgRequestType.
       - boolean ApplUpdated: Indicate whether the application has been updated or not. HIS representation of FL_ApplicationUpdateType.
       - boolean ResponseRequired: Set to true in case the flashloader or application shall send a response. HIS representation of FL_ResponseRequiredType.
   * - 描述 (Description)
     - 存储和BL相关的信息类型定义 (Definition of information types related to storage and BL.)




Dcm_MsgItemType类型定义 (Type definition for Dcm_MsgItemType)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 名称 (Name)
     - Dcm_MsgItemType
   * - 类型 (Type)
     - uint8
   * - 范围 (Range)
     - 无 (None)
   * - 描述 (Description)
     - 诊断信息类型定义 (Definition of diagnostic information types)




Dcm_MsgType类型定义 (Definition of Dcm_MsgType Type)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 名称 (Name)
     - Dcm_MsgType
   * - 类型 (Type)
     - Dcm_MsgItemType\
   * - 范围 (Range)
     - 无 (None)
   * - 描述 (Description)
     - 诊断数据类型定义 (Diagnostic data type definition)




Dcm_MsgLenType类型定义 (Definition of Dcm_MsgLenType Type)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 名称 (Name)
     - Dcm_MsgLenType
   * - 类型 (Type)
     - uint32
   * - 范围 (Range)
     - 无 (None)
   * - 描述 (Description)
     - 诊断信息长度类型定义 (Diagnostic information length type definition)




Dcm_MsgAddInfoType类型定义 (Dcm_MsgAddInfoType Type Definition)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - 名称 (Name)
     - Dcm_MsgAddInfoType
   * - 类型 (Type)
     - Structure
   * - 范围 (Range)
     - - uint8 ReqType: 0 = physical request, 1 = functional request.
       - boolean SuppressPosResponse: FALSE = Allow positive response, TRUE = Suppress positive response.
       - boolean CancelOperation: FALSE = Not cancel pending, TRUE = Cancel pending.
   * - 描述 (Description)
     - 诊断请求地址信息类型定义 (Definition of Diagnosis Request Address Information Type)



Dcm_IdContextType类型定义 (Dcm_IdContextType Type Definition)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 名称 (Name)
     - Dcm_IdContextType
   * - 类型 (Type)
     - uint8
   * - 范围 (Range)
     - 无
   * - 描述 (Description)
     - 内容ID值类型定义 (Content ID value type definition)




Dcm_MsgContextType类型定义 (Definition of Dcm_MsgContextType Type)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - 名称 (Name)
     - Dcm_MsgContextType
   * - 类型 (Type)
     - uint8
   * - 范围 (Range)
     - - Dcm_MsgType pReqData: Request data, starting directly after service identifier (which is not part of this data).
       - Dcm_MsgLenType ReqDataLen: Request data length (excluding service identifier).
       - Dcm_MsgType pResData: Positive response data, starting directly after service identifier (which is not part of this data).
       - Dcm_MsgLenType ResDataLen: Positive response data length (excluding service identifier).
       - Dcm_MsgAddInfoType MsgAddInfo: Additional information about service request and response (see Dcm_MsgAddInfo).
       - Dcm_MsgLenType resMaxDataLen: The maximal length of a response is restricted by the size of the buffer. The buffer size can depend on the diagnostic protocol identifier which is assigned to this message, e.g., an OBD protocol id can obtain other properties than the enhanced diagnostic protocol id. The resMaxDataLen is a property of the diagnostic protocol assigned by the DSL. The value does not change during communication. It cannot be implemented as a constant, because it can differ between different diagnostic protocols.
       - Dcm_IdContextType IdContext: This message context identifier can be used to determine the relation between request and response confirmation. This identifier can be stored within the application at request time, so that the response can be assigned to the original request. Background: Within the confirmation, the message context is no more valid, all message data is lost. You need an additional information to determine the request to which this confirmation belongs.
       - PduIdType DcmRxPduId: Pdu identifier on which the request was received. The PduId of the request can have consequences for message processing. E.g., an OBD request will be received on the OBD PduId and will be processed slightly different than an enhanced diagnostic request received on the physical PduId.
   * - 描述 (Description)
     - 处理诊断请求的必要信息类型定义 (Types of necessary information defined for processing diagnostic requests.)




Dcm_OpStatusType类型定义 (Definition of Dcm_OpStatusType type)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - 名称 (Name)
     - Dcm_OpStatusType
   * - 类型 (Type)
     - uint8
   * - 范围 (Range)
     - - DCM_INITIAL (0x00): Indicates the initial call to the operation.
       - DCM_PENDING (0x01): Indicates that a pending return has been done on the previous call of the operation.
       - DCM_CANCEL (0x02): Indicates that the Dcm requests to cancel the pending operation.
       - DCM_FORCE_RCRRP_OK (0x03): Confirm a response pending transmission.
   * - 描述 (Description)
     - 操作状态类型定义 (Definition of Operation Status Types)



Dcm_SecLevelType类型定义 (Definition of Dcm_SecLevelType type)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - 名称 (Name)
     - Dcm_SecLevelType
   * - 类型 (Type)
     - uint8
   * - 范围 (Range)
     - - DCM_SEC_LEV_LOCKED (0x00): 无 (None)
       - Configuration dependent (0x01...0x3F): 无 (None)
       - Reserved by Document (0x40...0xFF): 无 (None)
   * - 描述 (Description)
     - 安全级定义 (Security level definition)




Dcm_SesCtrlType类型定义 (Definition of Dcm_SesCtrlType type)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - 名称 (Name)
     - Dcm_SesCtrlType
   * - 类型 (Type)
     - uint8
   * - 范围 (Range)
     - - DCM_DEFAULT_SESSION (0x01): 无 (None)
       - DCM_PROGRAMMING_SESSION (0x02): 无 (None)
       - DCM_EXTENDED_DIAGNOSTIC_SESSION (0x03): 无 (None)
       - DCM_SAFETY_SYSTEM_DIAGNOSTIC_SESSION (0x04): 无 (None)
       - configuration dependent (0x40...0x7E): 根据配置 (According to configuration)
   * - 描述 (Description)
     - 会话级定义 (Session-level definition)




Dcm_ProtocolType类型定义 (Dcm_ProtocolType Type Definition)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - 名称 (Name)
     - Dcm_ProtocolType
   * - 类型 (Type)
     - uint8
   * - 范围 (Range)
     - - DCM_OBD_ON_CAN (0x00): OBD on CAN (ISO15765-4; ISO15031-5).
       - DCM_OBD_ON_FLEXRAY (0x01): OBD on FlexRay (Manufacturer specific; ISO15031-5).
       - DCM_OBD_ON_IP (0x02): OBD on Internet Protocol (Manufacturer specific; ISO15031-5).
       - DCM_UDS_ON_CAN (0x03): UDS on CAN (ISO15765-3; ISO14229-1).
       - DCM_UDS_ON_FLEXRAY (0x04): UDS on FlexRay (Manufacturer specific; ISO14229-1).
       - DCM_UDS_ON_IP (0x05): UDS on Internet Protocol (Manufacturer specific; ISO14229-1).
       - DCM_ROE_ON_CAN (0x06): Response On Event on CAN.
       - DCM_ROE_ON_FLEXRAY (0x07): Response On Event on FlexRay.
       - DCM_ROE_ON_IP (0x08): Response On Event on Internet Protocol.
       - DCM_PERIODICTRANS_ON_CAN (0x09): Periodic Transmission on CAN.
       - DCM_PERIODICTRANS_ON_FLEXRAY (0x0A): Periodic Transmission on FlexRay.
       - DCM_PERIODICTRANS_ON_IP (0x0B): Periodic Transmission on Internet Protocol.
       - DCM_NO_ACTIVE_PROTOCOL (0x0C): No protocol has been started.
       - Reserved for further AUTOSAR implementation (0x0D...0xEF): 无 (None).
       - DCM_SUPPLIER_1 (0xF0): Reserved for SW supplier specific.
       - DCM_SUPPLIER_2 (0xF1): Reserved for SW supplier specific.
       - DCM_SUPPLIER_3 (0xF2): Reserved for SW supplier specific.
       - DCM_SUPPLIER_4 (0xF3): Reserved for SW supplier specific.
       - DCM_SUPPLIER_5 (0xF4): Reserved for SW supplier specific.
       - DCM_SUPPLIER_6 (0xF5): Reserved for SW supplier specific.
       - DCM_SUPPLIER_7 (0xF6): Reserved for SW supplier specific.
       - DCM_SUPPLIER_8 (0xF7): Reserved for SW supplier specific.
       - DCM_SUPPLIER_9 (0xF8): Reserved for SW supplier specific.
       - DCM_SUPPLIER_10 (0xF9): Reserved for SW supplier specific.
       - DCM_SUPPLIER_11 (0xFA): Reserved for SW supplier specific.
       - DCM_SUPPLIER_12 (0xFB): Reserved for SW supplier specific.
       - DCM_SUPPLIER_13 (0xFC): Reserved for SW supplier specific.
       - DCM_SUPPLIER_14 (0xFD): Reserved for SW supplier specific.
       - DCM_SUPPLIER_15 (0xFE): Reserved for SW supplier specific.
   * - 描述 (Description)
     - 协议类型定义 (Type of Agreement Definition)




Dcm_NegativeResponseCodeType类型定义 (Dcm_NegativeResponseCodeType Type Definition)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - 名称 (Name)
     - Dcm_NegativeResponseCodeType
   * - 类型 (Type)
     - uint8
   * - 范围 (Range)
     - - Reserved by ISO 14229 (0x01...0x0F): ISOSAERESRVD
       - DCM_E_GENERALREJECT (0x10): GR
       - DCM_E_SERVICENOTSUPPORTED (0x11): SNS
       - DCM_E_SUBFUNCTIONNOTSUPPORTED (0x12): SFNS
       - DCM_E_INCORRECTMESSAGELENGTHORINVALIDFORMAT (0x13): IMLOIF
       - DCM_E_RESPONSETOOLONG (0x14): RTL
       - Reserved by ISO 14229 (0x15...0x20): ISOSAERESRVD
       - DCM_E_BUSYREPEATREQUEST (0x21): BRR
       - DCM_E_CONDITIONSNOTCORRECT (0x22): CNC
       - Reserved by ISO 14229 (0x23): ISOSAERESRVD
       - DCM_E_REQUESTSEQUENCEERROR (0x24): RSE
       - DCM_E_NORESPONSEFROMSUBNETCOMPONENT (0x25): NRFSC
       - DCM_E_FAILUREPREVENTSEXECUTIONOFREQUESTEDACTIN (0x26): FPEORA
       - Reserved by ISO 14229 (0x27...0x30): ISOSAERESRVD
       - DCM_E_REQUESTOUTOFRANGE (0x31): ROOR
       - Reserved by ISO 14229 (0x32): ISOSAERESRVD
       - DCM_E_SECURITYACCESSDENIED (0x33): SAD
       - Reserved by ISO 14229 (0x34): ISOSAERESRVD
       - DCM_E_INVALIDKEY (0x35): IK
       - DCM_E_EXCEEDNUMBEROFATTEMPTS (0x36): ENOA
       - DCM_E_REQUIREDTIMEDELAYNOTEXPIRED (0x37): RTDNE
       - Reserved by ISO 15764 (0x38...0x4F): RBEDLSD
       - Reserved by ISO 14229 (0x50...0x6F): ISOSAERESRVD
       - DCM_E_UPLOADDOWNLOADNOTACCEPTED (0x70): UDNA
       - DCM_E_TRANSFERDATASUSPENDED (0x71): TDS
       - DCM_E_GENERALPROGRAMMINGFAILURE (0x72): GPF
       - DCM_E_WRONGBLOCKSEQUENCECOUNTER (0x73): WBSC
       - Reserved by ISO 14229 (0x74...0x77): ISOSAERESRVD
       - Reserved by ISO 14229 (0x79...0x7D): ISOSAERESRVD
       - DCM_E_SUBFUNCTIONNOTSUPPORTEDINACTIVESESSION (0x7E): SFNSIAS
       - DCM_E_SERVICENOTSUPPORTEDINACTIVESESSION (0x7F): SNSIAS
       - Reserved by ISO 14229 (0x80): ISOSAERESRVD
       - DCM_E_RPMTOOHIGH (0x81): RPMTH
       - DCM_E_RPMTOOLOW (0x82): RPMTL
       - DCM_E_ENGINEISRUNNING (0x83): EIR
       - DCM_E_ENGINEISNOTRUNNING (0x84): EINR
       - DCM_E_ENGINERUNTIMETOOLOW (0x85): ERTTL
       - DCM_E_TEMPERATURETOOHIGH (0x86): TEMPTH
       - DCM_E_TEMPERATURETOOLOW (0x87): TEMPTL
       - DCM_E_VEHICLESPEEDTOOHIGH (0x88): VSTH
       - DCM_E_VEHICLESPEEDTOOLOW (0x89): VSTL
       - DCM_E_THROTTLE_PEDALTOOHIGH (0x8A): TPTH
       - DCM_E_THROTTLE_PEDALTOOLOW (0x8B): TPTL
       - DCM_E_TRANSMISSIONRANGENOTINNEUTRAL (0x8C): TRNIN
       - DCM_E_TRANSMISSIONRANGENOTINGEAR (0x8D): TRNIG
       - Reserved by ISO 14229 (0x8E): ISOSAERESRVD
       - DCM_E_BRAKESWITCH_NOTCLOSED (0x8F): BSNC
       - DCM_E_SHIFTERLEVERNOTINPARK (0x90): SLNIP
       - DCM_E_TORQUECONVERTERCLUTCHLOCKED (0x91): TCCL
       - DCM_E_VOLTAGETOOHIGH (0x92): VTH
       - DCM_E_VOLTAGETOOLOW (0x93): VTL
       - Reserved by ISO 14229 (0x94...0xEF): RFSCNC
       - DCM_E_VMSCNC_0 (0xF0): VMSCNC
       - DCM_E_VMSCNC_1 (0xF1): VMSCNC1
       - DCM_E_VMSCNC_2 (0xF2): VMSCNC2
       - DCM_E_VMSCNC_3 (0xF3): VMSCNC3
       - DCM_E_VMSCNC_4 (0xF4): VMSCNC4
       - DCM_E_VMSCNC_5 (0xF5): VMSCNC5
       - DCM_E_VMSCNC_6 (0xF6): VMSCNC6
       - DCM_E_VMSCNC_7 (0xF7): VMSCNC7
       - DCM_E_VMSCNC_8 (0xF8): VMSCNC8
       - DCM_E_VMSCNC_9 (0xF9): VMSCNC9
       - DCM_E_VMSCNC_A (0xFA): VMSCNCA
       - DCM_E_VMSCNC_B (0xFB): VMSCNCB
       - DCM_E_VMSCNC_C (0xFC): VMSCNCC
       - DCM_E_VMSCNC_D (0xFD): VMSCNCD
       - DCM_E_VMSCNC_E (0xFE): VMSCNCE
       - Reserved by ISO 14229 (0xFF): ISOSAERESRVD
   * - 描述 (Description)
     - 否定响应类型定义 (Definition of Negative Response Types)




Dcm_ConfirmationStatusType类型定义 (Type definition for Dcm_ConfirmationStatusType)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - 名称 (Name)
     - Dcm_ConfirmationStatusType
   * - 类型 (Type)
     - uint8
   * - 范围 (Range)
     - - DCM_RES_POS_OK (0x00): 无 (None)
       - DCM_RES_POS_NOT_OK (0x01): 无 (None)
       - DCM_RES_NEG_OK (0x02): 无 (None)
       - DCM_RES_NEG_NOT_OK (0x03): 无 (None)
   * - 描述 (Description)
     - 响应类型定义 (Response Type Definition)




Dcm_DidSupportedType类型定义 (Type definition for Dcm_DidSupportedType)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - 名称 (Name)
     - Dcm_DidSupportedType
   * - 类型 (Type)
     - uint8
   * - 范围 (Range)
     - - DCM_DID_SUPPORTED (0x00): 无 (None)
       - DCM_DID_NOT_SUPPORTED (0x01): 无 (None)
   * - 描述 (Description)
     - DID支持类型定义 (Support Types Definition)




输入函数描述 (Describe the input function:)
-----------------------------------------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 输入模块 (Input Module)
     - API
   * - ComM
     - ComM_DCM_ActiveDiagnostic
   * - 
     - ComM_DCM_InactiveDiagnostic
   * - Dem
     - Dem_DcmDisableDTCRecordUpdate
   * - 
     - Dem_DcmDisableDTCSetting
   * - 
     - Dem_DcmEnableDTCRecordUpdate
   * - 
     - Dem_DcmEnableDTCSetting
   * - 
     - Dem_DcmGetDTCByOccurrenceTime
   * - 
     - Dem_DcmGetDTCOfOBDFreezeFrame
   * - 
     - Dem_DcmGetDTCSeverityAvailabilityMask
   * - 
     - Dem_DcmGetDTCStatusAvailabilityMask
   * - 
     - Dem_DcmGetExtendedDataRecordByDTC
   * - 
     - Dem_DcmGetFreezeFrameDataByDTC
   * - 
     - Dem_DcmGetFunctionalUnitOfDTC
   * - 
     - Dem_DcmGetNextFilteredDTC
   * - 
     - Dem_DcmGetNextFilteredDTCAndFDC
   * - 
     - Dem_DcmGetNextFilteredDTCAndSeverity
   * - 
     - Dem_DcmGetNextFilteredRecord
   * - 
     - Dem_DcmGetNumberOfFilteredDTC
   * - 
     - Dem_DcmGetSeverityOfDTC
   * - 
     - Dem_DcmGetSizeOfExtendedDataRecordByDTC
   * - 
     - Dem_DcmGetSizeOfFreezeFrameByDTC
   * - 
     - Dem_DcmGetStatusOfDTC
   * - 
     - Dem_DcmGetTranslationType
   * - 
     - Dem_DcmReadDataOfOBDFreezeFrame
   * - 
     - Dem_DcmSetDTCFilter
   * - 
     - Dem_DcmSetFreezeFrameRecordFilter
   * - Det
     - Det_ReportError
   * - NvM
     - NvM_ReadBlock
   * - 
     - NvM_SetBlockLockStatus
   * - 
     - NvM_SetRamBlockStatus
   * - 
     - NvM_WriteBlock
   * - BswM
     - BswM_Dcm_ApplicationUpdated
   * - 
     - BswM\_Dcm_CommunicationMode_CurrentState
   * - PduR
     - PduR_DcmTransmit
   * - 
     - PduR_DcmCancelReceive
   * - 
     - PduR_DcmCancelTransmit
   * - 
     - PduR_DcmChangeParameter
   * - SchM
     - SchM_Enter_Dcm_ExclusiveArea
   * - 
     - SchM_Exit_Dcm_ExclusiveArea
   * - 
     - SchM_Switch_DcmEcuReset
   * - 
     - SchM\_Switch_DcmDiagnosticSessionControl
   * - 
     - SchM_Switch_DcmControlDTCSetting
   * - Tm
     - Tm_ResetTimer100us32bit
   * - 
     - Tm_GetTimeSpan100us32bit
   * - Os
     - GetElapsedValue




静态接口函数定义 (Static interface function definition)
---------------------------------------------------------------

Dcm_Init函数定义 (The Dcm_Init function definition)
===============================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Dcm_Init
     - 
     - 
   * - 函数原型： (Function prototype:)
     - FUNC(void,DCM_CODE)Dcm_Init(P2CONST(Dcm_CfgType,DCM_CONST,DCM_CONST_PBCFG)ConfigPtr)
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
     - ConfigPtr：配置参数的指针 (ConfigPtr：a pointer to configuration parameters)
     - 值域： (Domain:)
     - 无
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无
     - 
     - 
   * - 返回值： (Return Value:)
     - 无
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 初始化Dcm模块变量 (Initialize Dcm module variables)
     - 
     - 




Dcm_GetVersionInfo函数定义 (The Dcm_GetVersionInfo function definition)
===================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Dcm_GetVersionInfo
     - 
     - 
   * - 函数原型： (Function prototype:)
     - FUNC(void,DCM_CODE)Dcm_GetVersionInfo(P2VAR(Std_VersionInfoType,AUTOMATIC,DCM_VAR)VersionInfo)
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x24
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 是 (Yes)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - 无
     - 值域： (Domain:)
     - 无
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - VersionInfo：版本信息 (VersionInfo：Version Information)
     - 
     - 
   * - 返回值： (Return Value:)
     - 无
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 获取模块版本信息 (Get module version information)
     - 
     - 




Dcm_DemTriggerOnDTCStatus函数定义 (The Dcm_DemTriggerOnDTCStatus function definition)
=================================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Dcm_DemTriggerOnDTCStatus
     - 
     - 
   * - 函数原型： (Function prototype:)
     - FUNC(Std_ReturnType, DCM_CODE) Dcm_DemTriggerOnDTCStatus(uint32 DTC, Dem_UdsStatusByteType DTCStatusOld, Dem_UdsStatusByteType DTCStatusNew)
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x2B
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
     - DTC ：DTC值 (DTC : DTC Value)
     - 值域： (Domain:)
     - 0…0xFFFFFFFF
   * - 
     - DTCStatusOld：DTC老状态 (DTCStatusOld：DTC Old Status)
     - 值域： (Domain:)
     - 0…255
   * - 
     - DTCStatusNew：DTC新状态 (DTCStatusNew：DTC New Status)
     - 值域： (Domain:)
     - 0…255
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无
     - 
     - 
   * - 返回值： (Return Value:)
     - Std_ReturnType：E_OK (成功，只返回这个值) (E_OK: Success, returns only this value)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - ROE的DTC事件触发接口 (The DTC event trigger interface for ROE)
     - 
     - 




Dcm_GetVin函数定义 (The Dcm_GetVin function definition)
===================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Dcm_GetVin
     - 
     - 
   * - 函数原型： (Function prototype:)
     - FUNC(Std_ReturnType,DCM_CODE)Dcm_GetVin(uint8\*Data)
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x07
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 是 (Yes)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - 无
     - 值域： (Domain:)
     - 无
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - Data：TRUE：VIN数据存放指针 (Data：TRUE：Pointer to VIN data storage)
     - 
     - 
   * - 返回值： (Return Value:)
     - Std_ReturnType：
     - 
     - 
   * - 
     - E_OK：VIN被成功填入 (E_OK: VIN successfully entered)
     - 
     - 
   * - 
     - E_NOT_OK：DOIP模块使用默认VIN (E_NOT_OK: DOIP Module Uses Default VIN)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 获取VIN接口 (Get VIN Interface)
     - 
     - 




Dcm_GetSecurityLevel函数定义 (The Dcm_GetSecurityLevel function definition)
=======================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Dcm_GetSecurityLevel
     - 
     - 
   * - 函数原型： (Function prototype:)
     - FUNC(Std_ReturnType, DCM_CODE) Dcm_GetSecurityLevel(P2VAR(Dcm_SecLevelType, AUTOMATIC, DCM_VAR) SecLevel)
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x0d
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 是 (Yes)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - 无
     - 值域： (Domain:)
     - 无
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - SecLevel：当前安全级 (Security Level: Current Security Level)
     - 
     - 
   * - 返回值： (Return Value:)
     - Std_ReturnType：E_OK (请求成功，只返回这个值) (E_OK: Request Success, returns only this value)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 获取当前激活的安全级 (Get the current active security level)
     - 
     - 




Dcm_GetSesCtrlType函数定义 (The Dcm_GetSesCtrlType function definition)
===================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Dcm_GetSesCtrlType
     - 
     - 
   * - 函数原型： (Function prototype:)
     - FUNC(Std_ReturnType, DCM_CODE) Dcm_GetSesCtrlType(P2VAR(Dcm_SesCtrlType, AUTOMATIC, DCM_VAR) SesType)
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
     - 是 (Yes)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - 无
     - 值域： (Domain:)
     - 无
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - SesType：当前会话级 (SesType：Current Session Level)
     - 
     - 
   * - 返回值： (Return Value:)
     - Std_ReturnType：E_OK (请求成功，只返回这个值) (E_OK: Request Success, returns only this value)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 获取当前激活的会话级 (Get the currently active session-level)
     - 
     - 




Dcm_GetActiveProtocol函数定义 (The Dcm_GetActiveProtocol function definition)
=========================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Dcm_GetActiveProtocol
     - 
     - 
   * - 函数原型： (Function prototype:)
     - FUNC(Std_ReturnType, DCM_CODE) Dcm_GetActiveProtocol(P2VAR(Dcm_ProtocolType, AUTOMATIC, DCM_VAR) ActiveProtocol)
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x0f
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 是 (Yes)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - 无
     - 值域： (Domain:)
     - 无
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - ActiveProtocol：当前激活的协议 (ActiveProtocol：Current activated protocol)
     - 
     - 
   * - 返回值： (Return Value:)
     - Std_ReturnType：E_OK (请求成功，只返回这个值) (E_OK: Request Success, returns only this value)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 获取当前激活的协议类型 (Get the currently active protocol type)
     - 
     - 




Dcm_ResetToDefaultSession函数定义 (The Dcm_ResetToDefaultSession function definition)
=================================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Dcm_ResetToDefaultSession
     - 
     - 
   * - 函数原型： (Function prototype:)
     - FUNC(Std_ReturnType,DCM_CODE)Dcm_ResetToDefaultSession(void)
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x2a
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 是 (Yes)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - 无
     - 值域： (Domain:)
     - 无
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无
     - 
     - 
   * - 返回值： (Return Value:)
     - Std_ReturnType：
     - 
     - 
   * - 
     - E_OK：请求成功（只返回这个值） (E_OK: Request Success (only returns this value))
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 重置Dcm模块的会话级为默认会话 (Reset Dcm module session level to default session)
     - 
     - 




Dcm_TriggerOnEvent函数定义 (The Dcm_TriggerOnEvent function definition)
===================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Dcm_TriggerOnEvent
     - 
     - 
   * - 函数原型： (Function prototype:)
     - FUNC(Std_ReturnType,DCM_CODE)Dcm_TriggerOnEvent(uint8 RoeEventId)
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x2D
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 是 (Yes)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - RoeEventId：事件ID (RoeEventId：Event ID)
     - 值域： (Domain:)
     - 0..255
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无
     - 
     - 
   * - 返回值： (Return Value:)
     - Std_ReturnType：
     - 
     - 
   * - 
     - E_OK：取消请求成功 (E_OK: Request cancellation succeeded)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - SWC触发ROE事件接口 (SWC Trigger ROE Event Interface)
     - 
     - 




Dcm\_ SetActiveDiagnostic函数定义 (Define Dcm_SetActiveDiagnostic Function)
=======================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Dcm_SetActiveDiagnostic
     - 
     - 
   * - 函数原型： (Function prototype:)
     - FUNC(Std_ReturnType,DCM_CODE)Dcm_SetActiveDiagnostic(boolean active)
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x56
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 是 (Yes)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - Active：Iffalse Dcm shallnot callComM_DCM_ActiveDiagnostic().
     - 值域： (Domain:)
     - False/True
   * - 
     - If true Dcmwill callComM_DCM_ActiveDiagnostic().
     - 
     - 
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无
     - 
     - 
   * - 返回值： (Return Value:)
     - Std_ReturnType：
     - 
     - 
   * - 
     - E_OK：请求成功（只返回这个值） (E_OK: Request Success (only returns this value))
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 修改Dcm模块调用通信状态修改的状态 (Modify the state called by the Dcm module for communication status update)
     - 
     - 




Dcm_StartOfReception函数定义 (The Dcm_StartOfReception function definition)
=======================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Dcm_StartOfReception
     - 
     - 
   * - 函数原型： (Function prototype:)
     - FUNC(BufReq_ReturnType, DCM_CODE) Dcm_StartOfReception(PduIdType id, P2CONST(PduInfoType, AUTOMATIC, DCM_VAR) info, PduLengthType TpSduLength, P2VAR(PduLengthType, AUTOMATIC, DCM_VAR) bufferSizePtr)
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
     - 是 (Yes)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - id：I-PDU值 (id：PDU Value)
     - 值域： (Domain:)
     - 0…65535
   * - 
     - info：数据信息，数据长度，metadata信息的指针 (info: data information, data length, pointer to metadata information)
     - 值域： (Domain:)
     - 无
   * - 
     - TpSduLength：数据总长度 (TpSduLength：Total data length)
     - 值域： (Domain:)
     - 0…65535
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - bufferSizePtr：上层能用于接收的buffer长度 (bufferSizePtr: The length of the buffer that the upper layer can receive)
     - 
     - 
   * - 返回值： (Return Value:)
     - - BUFREQ_OK：请求成功 (BUFREQ_OK: Request Success)
       - BUFREQ_E_NOT_OK：请求失败 (BUFREQ_E_NOT_OK: Request Failed)
       - BUFREQ_E_OVFL：长度溢出 (BUFREQ_E_OVFL: Length Overflow)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 开始一次接收 (Start receiving.)
     - 
     - 




Dcm_CopyRxData函数定义 (Function definition for Dcm_CopyRxData)
===========================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Dcm_CopyRxData
     - 
     - 
   * - 函数原型： (Function prototype:)
     - FUNC(BufReq_ReturnType, DCM_CODE) Dcm_CopyRxData(PduIdType id, P2CONST(PduInfoType, AUTOMATIC, DCM_VAR) info, P2VAR(PduLengthType, AUTOMATIC, DCM_VAR) bufferSizePtr)
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
     - 是 (Yes)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - id：I-PDU值。 (id：I-PDU Value.)
     - 值域： (Domain:)
     - 0…65535
   * - 
     - info：数据信息，数据长度，metadata信息的指针 (info: data information, data length, pointer to metadata information)
     - 值域： (Domain:)
     - 无
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - bufferSizePtr：上层能用于接收的buffer长度 (bufferSizePtr: The length of the buffer that the upper layer can receive)
     - 
     - 
   * - 返回值： (Return Value:)
     - - BUFREQ_OK：请求成功 (BUFREQ_OK: Request Success)
       - BUFREQ_E_NOT_OK：请求失败 (BUFREQ_E_NOT_OK: Request Failed)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 接收后续数据 (Receive subsequent data)
     - 
     - 




Dcm_TpRxIndication函数定义 (The Dcm_TpRxIndication function definition)
===================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Dcm_TpRxIndication
     - 
     - 
   * - 函数原型： (Function prototype:)
     - FUNC(void,DCM_CODE)Dcm_TpRxIndication(PduIdTypeid,Std_ReturnTyperesult)
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
     - 是 (Yes)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - id：I-PDU值 (id：PDU Value)
     - 值域： (Domain:)
     - 0…65535
   * - 
     - result：接收结果 (result：receive result)
     - 值域： (Domain:)
     - E_OK/E_NOT_OK
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无
     - 
     - 
   * - 返回值： (Return Value:)
     - 无
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 接收完成指引 (Completion Guide Received)
     - 
     - 




Dcm_CopyTxData函数定义 (The Dcm_CopyTxData function definition)
===========================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Dcm_CopyTxData
     - 
     - 
   * - 函数原型： (Function prototype:)
     - FUNC(BufReq_ReturnType, DCM_CODE) Dcm_CopyTxData(PduIdType id, P2CONST(PduInfoType, AUTOMATIC, DCM_VAR) info, P2VAR(RetryInfoType, AUTOMATIC, DCM_VAR) retry, P2VAR(PduLengthType, AUTOMATIC, DCM_VAR) availableDataPtr)
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
     - 是 (Yes)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - id：I-PDU值 (id：PDU Value)
     - 值域： (Domain:)
     - 0…65535
   * - 
     - info：数据信息，数据长度，metadata信息的指针 (info: data information, data length, pointer to metadata information)
     - 值域： (Domain:)
     - 无
   * - 
     - retry：重传信息的指针 (retry: pointer for retried information)
     - 值域： (Domain:)
     - 无
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数
     - availableDataPtr：上层剩余能发送的长度 (availableDataPtr: remaining length that can be sent by the upper layer)
     - 
     - 
   * - 返回值： (Return Value:)
     - - BUFREQ_OK：请求成功 (BUFREQ_OK: Request Success)
       - BUFREQ_E_NOT_OK：请求失败 (BUFREQ_E_NOT_OK: Request Failed)
       - BUFREQ_E_BUSY：发送数据没有准备好 (BUFREQ_E_BUSY: Data for sending is not ready)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 拷贝发送数据 (Copy send data)
     - 
     - 




Dcm_TpTxConfirmation函数定义 (The Dcm_TpTxConfirmation function definition)
=======================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Dcm_TpTxConfirmation
     - 
     - 
   * - 函数原型： (Function prototype:)
     - FUNC(void,DCM_CODE)Dcm_TpTxConfirmation(PduIdType id,Std_ReturnType result)
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
     - 是 (Yes)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - id：I-PDU值 (id：PDU Value)
     - 值域： (Domain:)
     - 0…65535
   * - 
     - result：接收结果 (result：receive result)
     - 值域： (Domain:)
     - E_OK/E_NOT_OK
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无
     - 
     - 
   * - 返回值： (Return Value:)
     - 无
     - 
     - 
   * - 功能概述： (Function Overview:)
     - TP数据发送确认 (TP Data Send Confirmation)
     - 
     - 




Dcm_TxConfirmation函数定义 (The Dcm_TxConfirmation function definition)
===================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Dcm_TxConfirmation
     - 
     - 
   * - 函数原型： (Function prototype:)
     - FUNC(void,DCM_CODE)Dcm_TxConfirmation(PduIdType DcmTxPduId)
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
     - 不同PduId可重入，相同PduId不可重入 (Different PduId can re-enter, same PduId cannot re-enter)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - DcmTxPduId：I-PDU值 (DcmTxPduId：I-PDU Value)
     - 值域： (Domain:)
     - 0…65535
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无
     - 
     - 
   * - 返回值： (Return Value:)
     - 无
     - 
     - 
   * - 功能概述： (Function Overview:)
     - IF数据发送确认 (Confirmation of IF Data Transmission)
     - 
     - 




Dcm_ComM_NoComModeEntered函数定义 (The Dcm_ComM_NoComModeEntered function definition)
=================================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Dcm_ComM_NoComModeEntered
     - 
     - 
   * - 函数原型： (Function prototype:)
     - FUNC(void,DCM_CODE)Dcm_ComM_NoComModeEntered(uint8 NetworkId)
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x21
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 是 (Yes)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - NetworkId：网络ID值 (NetworkId：Network ID value)
     - 值域： (Domain:)
     - 0..255
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无
     - 
     - 
   * - 返回值： (Return Value:)
     - 无
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 通知Dcm进入NOCOM状态 (Notify Dcm to enter NOCOM state)
     - 
     - 




Dcm_ComM_SilentComModeEntered函数定义 (The Dcm_ComM_SilentComModeEntered function definition)
=========================================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Dcm_ComM\_SilentComModeEntered
     - 
     - 
   * - 函数原型： (Function prototype:)
     - FUNC(void,DCM_CODE)Dcm_ComM_SilentComModeEntered(uint8 NetworkId)
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
     - 是 (Yes)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - NetworkId：网络ID值 (NetworkId：Network ID value)
     - 值域： (Domain:)
     - 0..255
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无
     - 
     - 
   * - 返回值： (Return Value:)
     - 无
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 通知Dcm进入到静默模式 (Notify Dcm to enter silent mode)
     - 
     - 




Dcm_ComM_FullComModeEntered函数定义 (Function Dcm_ComM_FullComModeEntered defined)
==============================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Dcm_ComM_FullComModeEntered
     - 
     - 
   * - 函数原型： (Function prototype:)
     - FUNC(void,DCM_CODE)Dcm_ComM_FullComModeEntered(uint8 NetworkId)
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x23
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 是 (Yes)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - NetworkId：网络ID值 (NetworkId：Network ID value)
     - 值域： (Domain:)
     - 0..255
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无
     - 
     - 
   * - 返回值： (Return Value:)
     - 无
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 通知Dcm进入到FULLCOM模式 (Notify Dcm to enter FULLCOM mode)
     - 
     - 




Dcm_ReadMemory函数定义 (The Dcm_ReadMemory function definition)
===========================================================================

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Dcm_ReadMemory
     - 
     - 
     - 
   * - 函数原型： (Function prototype:)
     - Dcm_ReturnReadMemoryType Dcm_ReadMemory(Dcm_OpStatusType OpStatus, uint8 MemoryIdentifier, uint32 MemoryAddress, uint32 MemorySize, uint8* MemoryData, Dcm_NegativeResponseCodeType* ErrorCode)
     - 
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x26
     - 
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 异步 (Asynchronous)
     - 
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 否 (No)
     - 
     - 
     - 
   * - 输入参数： (Input parameters:)
     - OpStatus：操作类型 (OpStatus：Operation Type)
     - 值域： (Domain:)
     - 0…255
     - 
   * - 
     - MemoryIdentifier：内存块ID值 (MemoryIdentifier：Memory Block ID Value)
     - 值域： (Domain:)
     - 0…255
     - 
   * - 
     - MemoryAddress：内存地址 (Memory Address: Memory Address)
     - 值域： (Domain:)
     - 0…0xFFFFFFFF
     - 
   * - 
     - MemorySize：内存长度 (MemorySize：Memory Length)
     - 值域： (Domain:)
     - 0…0xFFFFFFFF
     - 
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - MemoryData（out）：读取的数据存放的地方
     - 
     - 
     - 
   * - 
     - ErrorCode（out）：错误码
     - 
     - 
     - 
   * - 返回值： (Return Value:)
     - - DCM_READ_OK：读取成功 (DCM_READ_OK: Read successfully)
       - DCM_READ_FAILED：读取失败 (DCM_READ_FAILED: Read failure)
       - DCM_READ_PENDING：正在读取 (DCM_READ_PENDING: Reading pending)
       - DCM_READ_FORCE_RCRRP：立即发送NRC78并且正在处理读取 (DCM_READ_FORCE_RCRRP: Immediate sending NRC78 and processing reading)
     - 
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 读取内存callout函数 (Read memory callout function)
     - 
     - 
     - 




Dcm_WriteMemory函数定义 (The Dcm_WriteMemory function definition)
=============================================================================

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Dcm_WriteMemory
     - 
     - 
     - 
   * - 函数原型： (Function prototype:)
     - Dcm_ReturnWriteMemoryType Dcm_WriteMemory(Dcm_OpStatusType OpStatus, uint8 MemoryIdentifier, uint32 MemoryAddress, uint32 MemorySize, uint8* MemoryData, Dcm_NegativeResponseCodeType* ErrorCode)
     - 
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x27
     - 
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 异步 (Asynchronous)
     - 
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 否 (No)
     - 
     - 
     - 
   * - 输入参数： (Input parameters:)
     - OpStatus：操作类型 (OpStatus：Operation Type)，取值范围：DCM_INITIAL, DCM_PENDING, DCM_CANCEL, DCM_FORCE_RCRRP_OK
     - 值域： (Domain:)
     - 0…255
     - 
   * - 
     - MemoryIdentifier：内存块ID值 (MemoryIdentifier：Memory Block ID Value)
     - 值域： (Domain:)
     - 0…255
     - 
   * - 
     - MemoryAddress：内存地址 (Memory Address: Memory Address)
     - 值域： (Domain:)
     - 0…255
     - 
   * - 
     - MemorySize：内存长度 (MemorySize：Memory Length)
     - 值域： (Domain:)
     - 0…0xFFFFFFFF
     - 
   * - 
     - MemoryData（in）：写数据存放地方的指针
     - 值域： (Domain:)
     - 无
     - 
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - ErrorCode（out）：错误码
     - 
     - 
     - 
   * - 返回值： (Return Value:)
     - - DCM_WRITE_OK：写成功 (DCM_WRITE_OK: Write Success)
       - DCM_WRITE_FAILED：写失败 (DCM_WRITE_FAILED: Write Failed)
       - DCM_WRITE_PENDING：正在写 (DCM_WRITE_PENDING: Writing pending)
       - DCM_WRITE_FORCE_RCRRP：立即发送NRC78并且正在处理写 (DCM_WRITE_FORCE_RCRRP: Immediate sending NRC78 and processing write)
     - 
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 写内存callout函数 (Write memory callout function)
     - 
     - 
     - 




Dcm_SetProgConditions函数定义 (The Dcm_SetProgConditions function defines)
======================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Dcm_SetProgConditions
     - 
     - 
   * - 函数原型： (Function prototype:)
     - Std_ReturnType Dcm_SetProgConditions(Dcm_OpStatusType OpStatus, Dcm_ProgConditionsType* ProgConditions)
     - 
     - 
   * - 服务编号： (Service Number:)
     - 无
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 异步 (Asynchronous)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 否 (No)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - OpStatus：操作类型 (OpStatus：Operation Type)，取值范围：DCM_INITIAL, DCM_PENDING, DCM_CANCEL, DCM_FORCE_RCRRP_OK
     - 值域： (Domain:)
     - 0…255
   * - 
     - ProgConditions：编程条件信息的指针 (ProgConditions：Pointer to programming condition information)
     - 值域： (Domain:)
     - 无
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无
     - 
     - 
   * - 返回值： (Return Value:)
     - - E_OK：成功设置 (E_OK: Success Setting)
       - E_NOT_OK：设置失败 (E_NOT_OK: Setting failure)
       - DCM_E_PENDING：正在设置 (DCM_E_PENDING: Pending Setup)
       - DCM_E_FORCE_RCRRP：立即发送NRC 0x78，正在处理 (DCM_E_FORCE_RCRRP: Send NRC 0x78 immediately, processing...)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 设置编程条件 (Set programming conditions)
     - 
     - 




Dcm_GetProgConditions函数定义 (The Dcm_GetProgConditions function definition)
=========================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Dcm_GetProgConditions
     - 
     - 
   * - 函数原型： (Function prototype:)
     - Dcm_EcuStartModeType Dcm_GetProgConditions(Dcm_ProgConditionsType* ProgConditions)
     - 
     - 
   * - 服务编号： (Service Number:)
     - 无
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
     - 无
     - 值域： (Domain:)
     - 无
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - ProgConditions：条件信息 (ProgConditions: Condition Information)
     - 
     - 
   * - 返回值： (Return Value:)
     - Dcm_EcuStartModeType
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 设置编程条件 (Set programming conditions)
     - 
     - 




Dcm_ProcessRequestTransferExit函数定义 (The Dcm_ProcessRequestTransferExit function definition)
===========================================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Dcm_ProcessRequestTransferExit
     - 
     - 
   * - 函数原型： (Function prototype:)
     - Std_ReturnType Dcm_ProcessRequestTransferExit(Dcm_OpStatusType OpStatus, uint8* transferRequestParameterRecord, uint32 transferRequestParameterRecordSize, uint8* transferResponseParameterRecord, uint32* transferResponseParameterRecordSize, Dcm_NegativeResponseCodeType* ErrorCode)
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x32
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 异步 (Asynchronous)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 否 (No)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - OpStatus：操作类型 (OpStatus：Operation Type)，取值范围：DCM_INITIAL, DCM_PENDING, DCM_CANCEL, DCM_FORCE_RCRRP_OK
     - 值域： (Domain:)
     - 0…255
   * - 
     - transferRequestParameterRecord：请求数据的指针 (transferRequestParameterRecord：Pointer to request data)
     - 值域： (Domain:)
     - 无
   * - 
     - transferRequestParameterRecordSize：请求数据长度 (transferRequestParameterRecordSize: Request data length)
     - 值域： (Domain:)
     - 0…0xFFFFFFFF
   * - 输入输出参数： (Input Output Parameters:)
     - transferResponseParameterRecordSize（inout）：数据长度
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - - ErrorCode（out）：错误码
       - transferResponseParameterRecord（out）：响应数据
     - 
     - 
   * - 返回值： (Return Value:)
     - - E_OK：成功 (E_OK: Success)
       - E_NOT_OK：失败 (E_NOT_OK: Failure)
       - DCM_E_PENDING：正在处理 (DCM_E_PENDING: Processing Pending)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 请求退出数据传输的callout函数 (Callout function for requesting exit from data transfer)
     - 
     - 




Dcm_ProcessRequestUpload函数定义 (The Dcm_ProcessRequestUpload function definition)
===============================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Dcm_ProcessRequestUpload
     - 
     - 
   * - 函数原型： (Function prototype:)
     - Std_ReturnType Dcm_ProcessRequestUpload(Dcm_OpStatusType OpStatus, uint8 DataFormatIdentifier, uint32 MemoryAddress, uint32 MemorySize, uint32* BlockLength, Dcm_NegativeResponseCodeType* ErrorCode)
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x31
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 异步 (Asynchronous)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 否 (No)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - OpStatus：操作类型 (OpStatus：Operation Type)，取值范围：DCM_INITIAL, DCM_PENDING, DCM_CANCEL, DCM_FORCE_RCRRP_OK
     - 值域： (Domain:)
     - 0…255
   * - 
     - DataFormatIdentifier：数据格式 (DataFormatIdentifier：Data Format)
     - 值域： (Domain:)
     - 0…255
   * - 
     - MemoryAddress：内存地址 (Memory Address: Memory Address)
     - 值域： (Domain:)
     - 0…0xFFFFFFFF
   * - 
     - MemorySize：内存大小 (MemorySize：Memory Size)
     - 值域： (Domain:)
     - 0…0xFFFFFFFF
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - - ErrorCode（out）：错误码
       - BlockLength（out）：一次传输的块大小
     - 
     - 
   * - 返回值： (Return Value:)
     - - E_OK：成功 (E_OK: Success)
       - E_NOT_OK：失败 (E_NOT_OK: Failure)
       - DCM_E_PENDING：正在处理 (DCM_E_PENDING: Processing Pending)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 请求上传数据 (Request upload data)
     - 
     - 




Dcm_ProcessRequestDownload函数定义 (The Dcm_ProcessRequestDownload function definition)
===================================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Dcm_ProcessRequestDownload
     - 
     - 
   * - 函数原型： (Function prototype:)
     - Std_ReturnType Dcm_ProcessRequestDownload(Dcm_OpStatusType OpStatus, uint8 DataFormatIdentifier, uint32 MemoryAddress, uint32 MemorySize, uint32* BlockLength, Dcm_NegativeResponseCodeType* ErrorCode)
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x30
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 异步 (Asynchronous)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 否 (No)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - OpStatus：操作类型 (OpStatus：Operation Type)，取值范围：DCM_INITIAL, DCM_PENDING, DCM_CANCEL, DCM_FORCE_RCRRP_OK
     - 值域： (Domain:)
     - 0…255
   * - 
     - DataFormatIdentifier：数据格式 (DataFormatIdentifier：Data Format)
     - 值域： (Domain:)
     - 0…255
   * - 
     - MemoryAddress：内存地址 (Memory Address: Memory Address)
     - 值域： (Domain:)
     - 0…0xFFFFFFFF
   * - 
     - MemorySize：内存大小 (MemorySize：Memory Size)
     - 值域： (Domain:)
     - 0…0xFFFFFFFF
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - - ErrorCode（out）：错误码
       - BlockLength（out）：一次传输的块大小
     - 
     - 
   * - 返回值： (Return Value:)
     - - E_OK：成功 (E_OK: Success)
       - E_NOT_OK：失败 (E_NOT_OK: Failure)
       - DCM_E_PENDING：正在处理 (DCM_E_PENDING: Processing Pending)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 请求下载数据 (Request download data)
     - 
     - 



Dcm_ProcessRequestFileTransfer函数定义 (The Dcm_ProcessRequestFileTransfer function definition)
===========================================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Dcm_ProcessRequestFileTransfer
     - 
     - 
   * - 函数原型： (Function prototype:)
     - Std_ReturnType Dcm_ProcessRequestFileTransfer(Dcm_OpStatusType OpStatus, uint8 modeofOperation, uint16 fileSizeParameterLength, uint8* filePathAndName, uint8 dataFormatIdentifier, uint8* fileSizeUncompressedOrDirInfoLength, uint8* fileSizeCompressed, uint32* BlockLength, Dcm_NegativeResponseCodeType* ErrorCode)
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x57
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 异步 (Asynchronous)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 否 (No)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - OpStatus：操作类型 (OpStatus：Operation Type)，取值范围：DCM_INITIAL, DCM_PENDING, DCM_CANCEL, DCM_FORCE_RCRRP_OK
     - 值域： (Domain:)
     - 0…255
   * - 
     - modeofOperation：操作类型 (modeofOperation：Operation Type)
     - 值域： (Domain:)
     - 0…255
   * - 
     - fileSizeParameterLength：文件路径长度 (fileSizeParameterLength：length of file path)
     - 值域： (Domain:)
     - 0…65535
   * - 
     - filePathAndName：文件路径和名字的指针 (filePathAndName: Pointer to file path and name)
     - 值域： (Domain:)
     - 无
   * - 
     - dataFormatIdentifier：数据格式的指针 (dataFormatIdentifier：Pointer to the data format)
     - 值域： (Domain:)
     - 无
   * - 输入输出参数： (Input Output Parameters:)
     - - fileSizeUncompressedOrDirInfoLength：非压缩长度 (fileSizeUncompressedOrDirInfoLength：uncompressed length or directory info length)
       - fileSizeCompressed：压缩长度 (fileSizeCompressed：Compressed Length)
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - - ErrorCode（out）：错误码
       - BlockLength（out）：一次传输的块大小
     - 
     - 
   * - 返回值： (Return Value:)
     - - E_OK：成功 (E_OK: Success)
       - E_NOT_OK：失败 (E_NOT_OK: Failure)
       - DCM_E_PENDING：正在处理 (DCM_E_PENDING: Processing Pending)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 请求文件传输 (Request file transfer)
     - 
     - 




Dcm_MainFunction函数定义 (Definition of Dcm_MainFunction function)
==============================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Dcm_MainFunction
     - 
     - 
   * - 函数原型： (Function prototype:)
     - FUNC(void, DCM_CODE) Dcm_MainFunction(void)
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x25
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
     - 无
     - 值域： (Domain:)
     - 无
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无
     - 
     - 
   * - 返回值： (Return Value:)
     - 无
     - 
     - 
   * - 功能概述： (Function Overview:)
     - Dcm模块主函数处理 (DCM module main function handling)
     - 
     - 




Dcm_KeyMAsyncCertificateVerifyFinished
======================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Dcm_KeyMAsyncCertificateVerifyFinished
     - 
     - 
   * - 函数原型： (Function prototype:)
     - FUNC(Std_ReturnType,DCM_CODE)Dcm_KeyMAsyncCertificateVerifyFinished(KeyM_CertificateIdType CertID,KeyM_CertificateStatusType Result);
     - 
     - 
   * - 服务编号： (Service Number:)
     - 无
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 是 (Yes)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - result：异步处理结果 (Asynchronous processing result)
     - 值域： (Domain:)
     - 无
   * - 
     - certId：证书ID (certId：Certificate ID)
     - 值域： (Domain:)
     - 无
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无
     - 
     - 
   * - 返回值： (Return Value:)
     - Std_ReturnTypeE_OK: thisvalue is alwaysreturned
     - 
     - 
   * - 功能概述： (Function Overview:)
     - KeyM异步任务通知接口 (Asynchronous Task Notification Interface)
     - 
     - 




Dcm_CsmAsyncJobFinished
=======================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Dcm_CsmAsyncJobFinished
     - 
     - 
   * - 函数原型： (Function prototype:)
     - FUNC(Std_ReturnType,DCM_CODE)Dcm_CsmAsyncJobFinished(constCrypto_JobType\*job,Crypto_ResultType result)
     - 
     - 
   * - 服务编号： (Service Number:)
     - 无
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 同步 (Sync)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 是 (Yes)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - Job：异步任务指针 (Asynchronous task pointer)
     - 值域： (Domain:)
     - 无
   * - 
     - result：异步任务结果 (result：Asynchronous task result)
     - 值域： (Domain:)
     - 无
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无
     - 
     - 
   * - 返回值： (Return Value:)
     - Std_ReturnTypeE_OK: thisvalue is alwaysreturned.
     - 
     - 
   * - 功能概述： (Function Overview:)
     - Csm异步任务通知接口 (Asynchronous Task Notification Interface for Csm)
     - 
     - 




可配置函数定义 (Configurable Function Definition)
----------------------------------------------------------

Xxx_GetSeed函数定义 (Xxx_GetSeedFunctionDefinition)
===============================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Xxx_GetSeed
     - 
     - 
   * - 函数原型： (Function prototype:)
     - Std_ReturnType Xxx_GetSeed(const uint8* SecurityAccessDataRecord, Dcm_OpStatusType OpStatus, uint8* Seed, Dcm_NegativeResponseCodeType* ErrorCode)
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x44
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 异步 (Asynchronous)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 否 (No)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - SecurityAccessDataRecord：此数据记录包含用于计算种子值的额外数据的指针 (SecurityAccessDataRecord: This data record contains pointers to additional data used for calculating seed values.)
     - 值域： (Domain:)
     - 无
   * - 
     - OpStatus：操作类型 (OpStatus：Operation Type)，取值范围：DCM_INITIAL, DCM_PENDING, DCM_CANCEL, DCM_FORCE_RCRRP_OK
     - 值域： (Domain:)
     - 0…255
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - - Seed：存放种子的指针 (Pointer to Seed)
       - ErrorCode：负响应码 (Error Code: Negative Response Code)
     - 
     - 
   * - 返回值： (Return Value:)
     - - E_OK：成功 (E_OK: Success)
       - E_NOT_OK：失败 (E_NOT_OK: Failure)
       - DCM_E_PENDING：正在处理 (DCM_E_PENDING: Processing Pending)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 获取种子的配置接口 (Get API for seed configuration)
     - 
     - 




Xxx_CompareKey函数定义 (Xxx_CompareKey Function Definition)
=======================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Xxx_CompareKey
     - 
     - 
   * - 函数原型： (Function prototype:)
     - Std_ReturnType Xxx_CompareKey(const uint8* Key, Dcm_OpStatusType OpStatus, Dcm_NegativeResponseCodeType* ErrorCode)
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x47
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 异步 (Asynchronous)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 否 (No)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - Key：用于比较的key的指针 (Pointer to the key used in comparison)
     - 值域： (Domain:)
     - 无
   * - 
     - OpStatus：操作类型 (OpStatus：Operation Type)，取值范围：DCM_INITIAL, DCM_PENDING, DCM_CANCEL, DCM_FORCE_RCRRP_OK
     - 值域： (Domain:)
     - 0…255
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - ErrorCode：错误码 (ErrorCode: Error Code)
     - 
     - 
   * - 返回值： (Return Value:)
     - - E_OK：成功 (E_OK: Success)
       - E_NOT_OK：失败 (E_NOT_OK: Failure)
       - DCM_E_PENDING：正在处理 (DCM_E_PENDING: Processing Pending)
       - E_COMPARE_KEY_FAILED：Key不匹配 (E_COMPARE_KEY_FAILED: Key Mismatch)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 比较key的配置接口 (Comparison of key configuration interfaces)
     - 
     - 




Xxx_GetSecurityAttemptCounter函数定义 (Xxx_GetSecurityAttemptCounter Function Definition)
=====================================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Xxx_GetSecurityAttemptCounter
     - 
     - 
   * - 函数原型： (Function prototype:)
     - Std_ReturnType Xxx_GetSecurityAttemptCounter(Dcm_OpStatusType OpStatus, uint8* AttemptCounter)
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x59
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 异步 (Asynchronous)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 否 (No)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - OpStatus：操作类型 (OpStatus：Operation Type)，取值范围：DCM_INITIAL, DCM_PENDING, DCM_CANCEL, DCM_FORCE_RCRRP_OK
     - 值域： (Domain:)
     - 0…255
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - AttemptCounter：错误计数指针 (AttemptCounter: Error Count Pointer)
     - 
     - 
   * - 返回值： (Return Value:)
     - - E_OK：成功 (E_OK: Success)
       - E_NOT_OK：失败 (E_NOT_OK: Failure)
       - DCM_E_PENDING：正在处理 (DCM_E_PENDING: Processing Pending)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 获取安全访问错误计数的配置。 (Get the configuration for secure access error counts.)
     - 
     - 




Xxx_ReadData函数定义 (Xxx_ReadData function definition)
===================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Xxx_ReadData
     - 
     - 
   * - 函数原型： (Function prototype:)
     - Std_ReturnType Xxx_ReadData(Dcm_OpStatusType OpStatus, uint8* Data, Dcm_NegativeResponseCodeType* ErrorCode)
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x58
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 异步 (Asynchronous)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 否 (No)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - OpStatus：操作类型 (OpStatus：Operation Type)，取值范围：DCM_INITIAL, DCM_PENDING, DCM_CANCEL, DCM_FORCE_RCRRP_OK
     - 值域： (Domain:)
     - 0…255
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - - Data：读取数据存放的指针 (Data: Pointer to read data storage)
       - ErrorCode：错误码 (ErrorCode: Error Code)
     - 
     - 
   * - 返回值： (Return Value:)
     - - E_OK：成功 (E_OK: Success)
       - E_NOT_OK：失败 (E_NOT_OK: Failure)
       - DCM_E_PENDING：正在处理 (DCM_E_PENDING: Processing Pending)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 获取数据的配置接口 (API for configuring data retrieval)
     - 
     - 




Xxx_WriteData函数定义 (WriteData function definition)
=================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Xxx_WriteData
     - 
     - 
   * - 函数原型： (Function prototype:)
     - Std_ReturnType Xxx_WriteData(uint8* Data, uint16 DataLength, Dcm_OpStatusType OpStatus, Dcm_NegativeResponseCodeType* ErrorCode)
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x3e
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 异步 (Asynchronous)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 否 (No)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - OpStatus：操作类型 (OpStatus：Operation Type)，取值范围：DCM_INITIAL, DCM_PENDING, DCM_CANCEL, DCM_FORCE_RCRRP_OK
     - 值域： (Domain:)
     - 0…255
   * - 
     - Data：写数据存放的指针 (Data：Pointer to store written data)
     - 值域： (Domain:)
     - 无
   * - 
     - DataLength：写入数据的长度 (DataLength：The length of written data)
     - 值域： (Domain:)
     - 0…65535
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - ErrorCode：错误码 (ErrorCode：Error Code)
     - 
     - 
   * - 返回值： (Return Value:)
     - - E_OK：成功 (E_OK: Success)
       - E_NOT_OK：失败 (E_NOT_OK: Failure)
       - DCM_E_PENDING：正在处理 (DCM_E_PENDING: Processing Pending)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 写数据的配置接口 (API for writing data configuration)
     - 
     - 




Xxx_ReadDataLength函数定义 (Xxx_ReadDataLength Function Definition)
===============================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Xxx_ReadDataLength
     - 
     - 
   * - 函数原型： (Function prototype:)
     - Std_ReturnType Xxx_ReadDataLength(Dcm_OpStatusType OpStatus, uint16* DataLength)
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x4c
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 异步 (Asynchronous)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 否 (No)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - OpStatus：操作类型 (OpStatus：Operation Type)，取值范围：DCM_INITIAL, DCM_PENDING, DCM_CANCEL, DCM_FORCE_RCRRP_OK
     - 值域： (Domain:)
     - 0…255
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - DataLength：写入数据的长度 (DataLength: The length of written data)
     - 
     - 
   * - 返回值： (Return Value:)
     - - E_OK：成功 (E_OK: Success)
       - E_NOT_OK：失败 (E_NOT_OK: Failure)
       - DCM_E_PENDING：正在处理 (DCM_E_PENDING: Processing Pending)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 获取读取数据长度的配置接口 (Get configuration interface for reading data length)
     - 
     - 



Xxx_ConditionCheckRead函数定义 (Xxx_ConditionCheckRead function definition)
=======================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Xxx_ConditionCheckRead
     - 
     - 
   * - 函数原型： (Function prototype:)
     - Std_ReturnType Xxx_ConditionCheckRead(Dcm_OpStatusType OpStatus, Dcm_NegativeResponseCodeType* ErrorCode)
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x37
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 异步 (Asynchronous)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 否 (No)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - OpStatus：操作类型 (OpStatus：Operation Type)，取值范围：DCM_INITIAL, DCM_PENDING, DCM_CANCEL, DCM_FORCE_RCRRP_OK
     - 值域： (Domain:)
     - 0…255
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - ErrorCode：错误码 (ErrorCode: Error Code)
     - 
     - 
   * - 返回值： (Return Value:)
     - - E_OK：成功 (E_OK: Success)
       - E_NOT_OK：失败 (E_NOT_OK: Failure)
       - DCM_E_PENDING：正在处理 (DCM_E_PENDING: Processing Pending)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 读取条件检查的配置接口 (Read conditions check configuration interface)
     - 
     - 




Xxx_GetScalingInformation函数定义 (Xxx_GetScalingInformation function definition)
=============================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Xxx_GetScalingInformation
     - 
     - 
   * - 函数原型： (Function prototype:)
     - Std_ReturnType Xxx_GetScalingInformation(uint8* ScalingInfo, Dcm_NegativeResponseCodeType* ErrorCode)
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x4b
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
     - 无
     - 值域： (Domain:)
     - 无
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - - ScalingInfo（out）：数据信息的指针 (Pointer to data information)
       - ErrorCode（out）：错误码 (Error Code)
     - 
     - 
   * - 返回值： (Return Value:)
     - - E_OK：成功 (E_OK: Success)
       - E_NOT_OK：失败 (E_NOT_OK: Failure)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 获取数据信息的配置接口 (API for configuring data information retrieval)
     - 
     - 




Xxx_SetSecurityAttemptCounter函数定义 (Xxx_SetSecurityAttemptCounter function definition)
=====================================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Xxx_SetSecurityAttemptCounter
     - 
     - 
   * - 函数原型： (Function prototype:)
     - Std_ReturnType Xxx_SetSecurityAttemptCounter(Dcm_OpStatusType OpStatus, uint8 AttemptCounter)
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x5a
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 异步 (Asynchronous)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 否 (No)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - OpStatus：操作类型 (OpStatus：Operation Type)，取值范围：DCM_INITIAL, DCM_PENDING, DCM_CANCEL, DCM_FORCE_RCRRP_OK
     - 值域： (Domain:)
     - 0…255
   * - 
     - AttemptCounter：错误计数指针的指针 (AttemptCounter: Pointer to error count pointer)
     - 值域： (Domain:)
     - 无
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无
     - 
     - 
   * - 返回值： (Return Value:)
     - - E_OK：成功 (E_OK: Success)
       - E_NOT_OK：失败 (E_NOT_OK: Failure)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 存储安全访问错误计数的接口 (Interface for storing error counts of secure access attempts)
     - 
     - 



Xxx_ReturnControlToECU函数定义 (Xxx_ReturnControlToECU function definition)
=======================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Xxx_ReturnControlToECU
     - 
     - 
   * - 函数原型： (Function prototype:)
     - Std_ReturnType Xxx_ReturnControlToECU([Dcm_ControlMask_{Data} controlMask,] Dcm_NegativeResponseCodeType* ErrorCode)
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x4f
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
     - controlMask：控制掩码 (controlMask: Control Mask)
     - 值域： (Domain:)
     - 0…255
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - ErrorCode：错误码 (ErrorCode: Error Code)
     - 
     - 
   * - 返回值： (Return Value:)
     - - E_OK：成功 (E_OK: Success)
       - E_NOT_OK：失败 (E_NOT_OK: Failure)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 重置为ECU默认数据的配置接口 (The configuration interface for resetting to ECU default data)
     - 
     - 




Xxx_ResetToDefault函数定义 (Xxx_ResetToDefault function definition)
===============================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Xxx_ResetToDefault
     - 
     - 
   * - 函数原型： (Function prototype:)
     - Std_ReturnType Xxx_ResetToDefault([Dcm_ControlMask_{Data} controlMask,] Dcm_NegativeResponseCodeType* ErrorCode)
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x4d
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
     - controlMask：控制掩码 (controlMask: Control Mask)
     - 值域： (Domain:)
     - 0…255
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - ErrorCode：错误码 (ErrorCode: Error Code)
     - 
     - 
   * - 返回值： (Return Value:)
     - - E_OK：成功 (E_OK: Success)
       - E_NOT_OK：失败 (E_NOT_OK: Failure)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 重置为默认数据的配置接口 (API for resetting configuration to default data)
     - 
     - 




Xxx_FreezeCurrentState函数定义 (Xxx_FreezeCurrentState function definition)
=======================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Xxx_FreezeCurrentState
     - 
     - 
   * - 函数原型： (Function prototype:)
     - Std_ReturnType Xxx_FreezeCurrentState(Dcm_OpStatusType OpStatus, [Dcm_ControlMask_{Data} controlMask,] Dcm_NegativeResponseCodeType* ErrorCode)
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x4a
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
     - controlMask：控制掩码 (controlMask: Control Mask)
     - 值域： (Domain:)
     - 0…255
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - ErrorCode：错误码 (ErrorCode: Error Code)
     - 
     - 
   * - 返回值： (Return Value:)
     - - E_OK：成功 (E_OK: Success)
       - E_NOT_OK：失败 (E_NOT_OK: Failure)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 用于冻结当前数据状态的配置接口 (API for configuring the freezing of current data status)
     - 
     - 




Xxx_ShortTermAdjustment函数定义 (Xxx_ShortTermAdjustment Function Definition)
=========================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Xxx_ShortTermAdjustment
     - 
     - 
   * - 函数原型： (Function prototype:)
     - Std_ReturnType Xxx_ShortTermAdjustment(uint8* ControlStateInfo, uint16 DataLength, [Dcm_ControlMask_{Data} controlMask,] Dcm_NegativeResponseCodeType* ErrorCode)
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x54
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
     - ControlStateInfo：ControlState信息的指针 (ControlStateInfo: Pointer to ControlState information)
     - 值域： (Domain:)
     - 无
   * - 
     - DataLength：控制数据 (DataLength: Control Data)
     - 值域： (Domain:)
     - 0…65535
   * - 
     - controlMask：控制掩码 (controlMask: Control Mask)
     - 值域： (Domain:)
     - 0…255
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - ErrorCode：错误码 (ErrorCode: Error Code)
     - 
     - 
   * - 返回值： (Return Value:)
     - - E_OK：成功 (E_OK: Success)
       - E_NOT_OK：失败 (E_NOT_OK: Failure)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 调整数据控制的配置接口 (Adjust the configuration interface for data control)
     - 
     - 




Xxx_IsDidAvailable函数定义 (Xxx_IsDidAvailable function definition)
===============================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Xxx_IsDidAvailable
     - 
     - 
   * - 函数原型： (Function prototype:)
     - Std_ReturnType Xxx_IsDidAvailable(uint16 DID, Dcm_OpStatusType OpStatus, Dcm_DidSupportedType* supported)
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x53
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 异步 (Asynchronous)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 否 (No)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - OpStatus：操作类型 (OpStatus：Operation Type)，取值范围：DCM_INITIAL, DCM_PENDING, DCM_CANCEL, DCM_FORCE_RCRRP_OK
     - 值域： (Domain:)
     - 0…255
   * - 
     - DID：DID值 (DID: DID value)
     - 值域： (Domain:)
     - 0…65535
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - supported：支持结果 (supported: Support Result)
     - 
     - 
   * - 返回值： (Return Value:)
     - - E_OK：成功 (E_OK: Success)
       - E_NOT_OK：失败 (E_NOT_OK: Failure)
       - DCM_E_PENDING：正在处理 (DCM_E_PENDING: Processing Pending)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 范围DID检查支持的配置接口 (Range DID Check Support Configuration Interface)
     - 
     - 




Xxx_ReadDidData函数定义 (Xxx_ReadDidData function definition)
=========================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Xxx_ReadDidData
     - 
     - 
   * - 函数原型： (Function prototype:)
     - Std_ReturnType Xxx_ReadDidData(uint16 DID, uint8* Data, Dcm_OpStatusType OpStatus, uint16 DataLength, Dcm_NegativeResponseCodeType* ErrorCode)
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x40
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 异步 (Asynchronous)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 否 (No)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - OpStatus：操作类型 (OpStatus：Operation Type)，取值范围：DCM_INITIAL, DCM_PENDING, DCM_CANCEL, DCM_FORCE_RCRRP_OK
     - 值域： (Domain:)
     - 0…255
   * - 
     - DID：DID值 (DID: DID value)
     - 值域： (Domain:)
     - 0…255
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - - Data：数据输出指针 (Data: Output pointer for data)
       - DataLength：数据输出长度 (DataLength: Output length)
       - ErrorCode：错误码 (ErrorCode: Error Code)
     - 
     - 
   * - 返回值： (Return Value:)
     - - E_OK：成功 (E_OK: Success)
       - E_NOT_OK：失败 (E_NOT_OK: Failure)
       - DCM_E_PENDING：正在处理 (DCM_E_PENDING: Processing Pending)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 范围DID读取数据接口 (DID Read Data Interface for Range)
     - 
     - 




Xxx_WriteDidData函数定义 (Xxx_WriteDidData function definition)
===========================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Xxx_WriteDidData
     - 
     - 
   * - 函数原型： (Function prototype:)
     - Std_ReturnType Xxx_WriteDidData(uint16 DID, uint8* Data, Dcm_OpStatusType OpStatus, uint16 DataLength, Dcm_NegativeResponseCodeType* ErrorCode)
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x41
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 异步 (Asynchronous)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 否 (No)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - OpStatus：操作类型 (OpStatus：Operation Type)，取值范围：DCM_INITIAL, DCM_PENDING, DCM_CANCEL, DCM_FORCE_RCRRP_OK
     - 值域： (Domain:)
     - 0…255
   * - 
     - DID：DID值 (DID: DID value)
     - 值域： (Domain:)
     - 0…255
   * - 
     - Data：数据输出指针的指针 (Data: Pointer to pointer of data output)
     - 值域： (Domain:)
     - 无
   * - 
     - DataLength：数据输出长度 (DataLength: Output length)
     - 值域： (Domain:)
     - 0…65535
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - ErrorCode：错误码 (ErrorCode: Error Code)
     - 
     - 
   * - 返回值： (Return Value:)
     - - E_OK：成功 (E_OK: Success)
       - E_NOT_OK：失败 (E_NOT_OK: Failure)
       - DCM_E_PENDING：正在处理 (DCM_E_PENDING: Processing Pending)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 范围DID数据写配置接口 (Interface for DID Data Write Configuration in Range)
     - 
     - 




Xxx_ReadDidRangeDataLength函数定义 (Xxx_ReadDidRangeDataLength function definition)
===============================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Xxx_ReadDidRangeDataLength
     - 
     - 
   * - 函数原型： (Function prototype:)
     - Std_ReturnType Xxx_ReadDidRangeDataLength(uint16 DID, Dcm_OpStatusType OpStatus, uint16* DataLength)
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x5e
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 异步 (Asynchronous)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 否 (No)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - OpStatus：操作类型 (OpStatus：Operation Type)，取值范围：DCM_INITIAL, DCM_PENDING, DCM_CANCEL, DCM_FORCE_RCRRP_OK
     - 值域： (Domain:)
     - 0…255
   * - 
     - DID：DID值 (DID: DID value)
     - 值域： (Domain:)
     - 0…255
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - DataLength：数据输出长度 (DataLength: Output Length)
     - 
     - 
   * - 返回值： (Return Value:)
     - - E_OK：成功 (E_OK: Success)
       - E_NOT_OK：失败 (E_NOT_OK: Failure)
       - DCM_E_PENDING：正在处理 (DCM_E_PENDING: Processing Pending)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 范围DID读取数据长度配置接口 (Range DID Read Data Length Configuration Interface)
     - 
     - 




Xxx_Start函数定义 (Xxx_Start function definition)
=============================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Xxx_Start
     - 
     - 
   * - 函数原型： (Function prototype:)
     - Std_ReturnType Xxx_Start(
         [DcmDspRoutineSignalType dataIn_1, ... DcmDspRoutineSignalType dataIn_n],
         [const uint8* dataInVar],
         Dcm_OpStatusType OpStatus,
         [DcmDspRoutineSignalType dataOut_1, ... DcmDspRoutineSignalType dataOut_n],
         [uint8* dataOutVar],
         [uint16* currentDataLength],
         Dcm_NegativeResponseCodeType* ErrorCode)
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x5b
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 异步 (Asynchronous)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 否 (No)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - dataIn_1 ... dataIn_n：固定输入数据 (Fixed input data 1...n)，取值范围：0…14
     - 值域： (Domain:)
     - 无
   * - 
     - dataInVar：可变长度输入数据的指针 (Pointer to variable-length input data)
     - 值域： (Domain:)
     - 无
   * - 
     - OpStatus：操作类型 (Operation Type)，取值范围：DCM_INITIAL, DCM_PENDING, DCM_CANCEL, DCM_FORCE_RCRRP_OK
     - 值域： (Domain:)
     - 0…255
   * - 
     - currentLengthDataInVar：dataInVar参数的字节长度的指针 (Pointer to the byte length of dataInVar)
     - 值域： (Domain:)
     - 无
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - - dataOut_1 ... dataOut_n：固定输出数据 (Fixed output data 1...n)
       - dataOutVar：可变长度输出数据 (Variable-length output data)
       - currentLengthDataInVar：dataInVar参数的字节长度 (Byte length of dataInVar parameter)
       - ErrorCode：错误码 (Error Code)
     - 
     - 
   * - 返回值： (Return Value:)
     - - E_OK：成功 (E_OK: Success)
       - E_NOT_OK：失败 (E_NOT_OK: Failure)
       - DCM_E_PENDING：正在处理 (DCM_E_PENDING: Processing Pending)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 启动例程的配置接口 (Interface for configuring the launch routine)
     - 
     - 




Xxx_Stop函数定义 (Xxx_Stop function definition)
===========================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Xxx_Stop
     - 
     - 
   * - 函数原型： (Function prototype:)
     - Std_ReturnType Xxx_Stop(
         [DcmDspRoutineSignalType dataIn_1, ... DcmDspRoutineSignalType dataIn_n],
         [const uint8* dataInVar],
         [DcmDspRoutineSignalType dataOut_1, ... DcmDspRoutineSignalType dataOut_n],
         [uint8* dataOutVar],
         uint16 currentLengthDataInVar,
         [uint16* currentLengthDataOutVar],
         Dcm_NegativeResponseCodeType* ErrorCode)
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x5c
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 异步 (Asynchronous)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 否 (No)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - dataIn_1 ... dataIn_n：固定输入数据 (Fixed input data 1...n)，取值范围：0…14
     - 值域： (Domain:)
     - 无
   * - 
     - dataInVar：可变长度输入数据 (Variable-length input data)
     - 值域： (Domain:)
     - 无
   * - 
     - currentLengthDataInVar：dataInVar参数的字节长度 (Byte length of dataInVar parameter)
     - 值域： (Domain:)
     - 无
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - - dataOut_1 ... dataOut_n：固定输出数据 (Fixed output data 1...n)
       - dataOutVar：可变长度输出数据 (Variable-length output data)
       - currentLengthDataOutVar：输出数据长度指针 (Pointer to output data length)
       - ErrorCode：错误码 (Error Code)
     - 
     - 
   * - 返回值： (Return Value:)
     - - E_OK：成功 (E_OK: Success)
       - E_NOT_OK：失败 (E_NOT_OK: Failure)
       - DCM_E_PENDING：正在处理 (DCM_E_PENDING: Processing Pending)
       - DCM_E_FORCE_RCRRP：立即发送0x78，并且正在处理 (DCM_E_FORCE_RCRRP: Send 0x78 immediately, and processing...)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 停止例程的配置接口 (The API for configuring the stop procedure)
     - 
     - 




Xxx_RequestResults函数定义 (The Xxx_RequestResults function definition)
===================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Xxx_RequestResults
     - 
     - 
   * - 函数原型： (Function prototype:)
     - Std_ReturnType Xxx_RequestResults(Dcm_OpStatusType OpStatus, [DcmDspRoutineSignalType* dataOut_1, ... DcmDspRoutineSignalType* dataOut_n], [uint8* dataOutVar], [uint16* currentLengthDataOutVar], Dcm_NegativeResponseCodeType* ErrorCode)
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x5d
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - 异步 (Asynchronous)
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - 否 (No)
     - 
     - 
   * - 输入参数： (Input parameters:)
     - OpStatus：操作类型 (Operation Type)，取值范围：DCM_INITIAL, DCM_PENDING, DCM_CANCEL, DCM_FORCE_RCRRP_OK
     - 值域： (Domain:)
     - 0…255
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - - dataOut_1 ... dataOut_n：固定输出数据 (Fixed output data 1...n)
       - dataOutVar：可变长度输出数据 (Variable-length output data)
       - currentLengthDataOutVar：输出数据长度指针 (Pointer to output data length)
       - ErrorCode：错误码 (Error Code)
     - 
     - 
   * - 返回值： (Return Value:)
     - - E_OK：成功 (E_OK: Success)
       - E_NOT_OK：失败 (E_NOT_OK: Failure)
       - DCM_E_PENDING：正在处理 (DCM_E_PENDING: Processing Pending)
       - DCM_E_FORCE_RCRRP：立即发送0x78，并且正在处理 (DCM_E_FORCE_RCRRP: Send 0x78 immediately, and processing...)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 获取例程结果的配置接口 (Interface for configuring access to routine results)
     - 
     - 




Xxx_ClearDTCCheckFnc函数定义 (Xxx_ClearDTCCheckFnc function definition)
===================================================================================

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Xxx_ClearDTCCheckFnc
     - 
     - 
   * - 函数原型： (Function prototype:)
     - Std_ReturnType Xxx_ClearDTCCheckFnc(uint32 GoDTC, Dcm_NegativeResponseCodeType* ErrorCode)
     - 
     - 
   * - 服务编号： (Service Number:)
     - 0x5f
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
     - GoDTC：DTC组 (DTC group)
     - 值域： (Domain:)
     - 0…0xFFFFFFFF
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - ErrorCode：错误码 (Error Code)
     - 
     - 
   * - 返回值： (Return Value:)
     - - E_OK：成功 (E_OK: Success)
       - E_NOT_OK：失败 (E_NOT_OK: Failure)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 清除DTC组的检查配置接口 (Clear DTC Group Check Configuration Interface)
     - 
     - 




SWC服务组件封装 (SWC Service Component Packaging)
-----------------------------------------------------------

以下类型和接口可以封装至SWC生成完整的服务组件，可以与应用通过端口连接，没有列出的部分dcm底层暂时不支持。

The following types and interfaces can be encapsulated to generate complete service components via SWC, which can be connected to the application through ports. The underlying dcm temporarily does not support the unlisted parts.

实现数据类型封装 (Implement data type encapsulation)
============================================================

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 类型名及定义引用 (Type Name and Definition Reference)
     - 生成条件 (Generate Conditions)
   * - 4.1.2 Dcm_SecLevelType
     - 无
   * - 4.1.3 Dcm_SesCtrlType
     - 无
   * - 4.1.4 Dcm_ProtocolType
     - 无
   * - 4.1.5 Dcm_NegativeResponseCodeType
     - 无
   * - 4.1.8 Dcm_ConfirmationStatusType
     - 无
   * - 4.1.9 Dcm_OpStatusType
     - 无




CS接口封装 (CS Interface Packaging)
===============================================

注：下面提到的<UserModule>和<UserPortName>分别为用户SWC的名字和对应端口名，在与Dcm服务组件端口连接后适用。

Note: The <UserModule> and <UserPortName> mentioned below are respectively the name of the user SWC and the corresponding port name, applicable after connecting to the Dcm service component port.

Rte_Call_Dcm_CallbackDCMRequestServices\_{Name}_StartProtocol
-----------------------------------------------------------------------------

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Rte_Call_Dcm_CallbackDCMRequestServices\_{Name}_StartProtocol
     - 
     - 
   * - 函数定义： (Function definition:)
     - Std_ReturnTypeRte_Call_Dcm_CallbackDCMRequestServices\_{Name}_StartProtocol
     - 
     - 
   * - 
     - (const Dcm_ProtocolType ProtocolId)
     - 
     - 
   * - 服务编号： (Service Number:)
     - N/A
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - N/A
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - N/A
     - 
     - 
   * - 输入参数： (Input parameters:)
     - ProtocolId：协议ID (ProtocolId：Protocol ID)
     - 值域： (Domain:)
     - 0…255
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无
     - 
     - 
   * - 返回值： (Return Value:)
     - Std_ReturnType：
     - 
     - 
   * - 
     - E_OK： 成功 (E_OK: Success)
     - 
     - 
   * - 
     - E_NOT_OK： 失败 (E_NOT_OK: Failure)
     - 
     - 
   * - 
     - E_PROTOCOL_NOT_ALLOWED： 协议不允许 (E_PROTOCOL_NOT_ALLOWED: Protocol Not Allowed)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 请求开始协议 (Request Start Protocol)
     - 
     - 
   * - 变体： (Variants:)
     - Name=DcmConfigSet/DcmDsl/DcmDslCallbackDCMRequestService.
     - 
     - 
   * - 
     - SHORT-NAME
     - 
     - 
   * - 生成条件： (Generate conditions:)
     - DcmConfigSet/DcmDsl/DcmDslCallbackDCMRequestService
     - 
     - 
   * - 端口类型： (Port Type:)
     - Require Port
     - 
     - 
   * - 从属端口： (Subordinate Port:)
     - CallbackDCMRequestServices\_{Name}
     - 
     - 




Rte_Call_Dcm_CallbackDCMRequestServices\_{Name}_StopProtocol
----------------------------------------------------------------------------

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Rte_Call_Dcm_CallbackDCMRequestServices\_{Name}_StopProtocol
     - 
     - 
   * - 函数定义： (Function definition:)
     - Std_ReturnTypeRte_Call_Dcm_CallbackDCMRequestServices\_{Name}_StopProtocol
     - 
     - 
   * - 
     - (const Dcm_ProtocolType ProtocolId)
     - 
     - 
   * - 服务编号： (Service Number:)
     - N/A
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - N/A
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - N/A
     - 
     - 
   * - 输入参数： (Input parameters:)
     - ProtocolId：协议ID (ProtocolId：Protocol ID)
     - 值域： (Domain:)
     - 0…255
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无
     - 
     - 
   * - 返回值： (Return Value:)
     - Std_ReturnType：
     - 
     - 
   * - 
     - E_OK： 成功 (E_OK: Success)
     - 
     - 
   * - 
     - E_NOT_OK： 失败 (E_NOT_OK: Failure)
     - 
     - 
   * - 
     - E_PROTOCOL_NOT_ALLOWED： 协议不允许 (E_PROTOCOL_NOT_ALLOWED: Protocol Not Allowed)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 请求结束协议 (Request to Terminate Agreement)
     - 
     - 
   * - 变体： (Variants:)
     - Name=DcmConfigSet/DcmDsl/DcmDslCallbackDCMRequestService.
     - 
     - 
   * - 
     - SHORT-NAME
     - 
     - 
   * - 生成条件： (Generate conditions:)
     - DcmConfigSet/DcmDsl/DcmDslCallbackDCMRequestService
     - 
     - 
   * - 端口类型： (Port Type:)
     - Require Port
     - 
     - 
   * - 从属端口： (Subordinate Port:)
     - CallbackDCMRequestServices\_{Name}
     - 
     - 




Rte_Call_Dcm_DataServices_DIDRange\_{Range}_IsDidAvailable
--------------------------------------------------------------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Rte_Call_Dcm_DataServices_DIDRange\_{Range}_IsDidAvailable
   * - 引用函数定义： (Quote function definition:)
     - 详见4.4.14 (See 4.4.14)
   * - 变体： (Variants:)
     - Range=DcmConfigSet/DcmDsp/DcmDsp/DcmDspDidRange.SHORT_NAME
   * - 生成条件： (Generate conditions:)
     - 1. DcmConfigSet/DcmDsp/DcmDsp/DcmDspDidRange.
   * - 
     - DcmDspDidRangeUsePort == TRUE
   * - 
     - And
   * - 
     - 2. DcmConfigSet/DcmDsp/DcmDsp/DcmDspDidRange.DcmDspDidRangeHasGaps== TRUE
   * - 端口类型： (Port Type:)
     - Require Port
   * - 从属端口： (Subordinate Port:)
     - DataServices_DIDRange\_{Range}




Rte_Call_Dcm_DataServices_DIDRange\_{Range}_ReadDidData
-----------------------------------------------------------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Rte_Call_Dcm_DataServices_DIDRange\_{Range}_ReadDidData
   * - 引用函数定义： (Quote function definition:)
     - 详见4.4.15 (See 4.4.15)
   * - 变体： (Variants:)
     - Range=DcmConfigSet/DcmDsp/DcmDsp/DcmDspDidRange.SHORT_NAME
   * - 生成条件： (Generate conditions:)
     - 1. DcmConfigSet/DcmDsp/DcmDsp/DcmDspDidRange.
   * - 
     - DcmDspDidRangeUsePort == TRUE
   * - 
     - And
   * - 
     - 2. Dcm/DcmConfigSet/DcmDsp/DcmDspDidRange/DcmDspDidRangeInfoRef->DcmDspDidRead!= NULL
   * - 端口类型： (Port Type:)
     - Require Port
   * - 从属端口： (Subordinate Port:)
     - DataServices_DIDRange\_{Range}




Rte_Call_Dcm_DataServices_DIDRange\_{Range}_ReadDidRangeDataLength
----------------------------------------------------------------------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Rte\_Call\_Dcm\_DataServices_DIDRange\_{Range}_ReadDidRangeDataLength
   * - 引用函数定义： (Quote function definition:)
     - 详见4.4.17 (See 4.4.17)
   * - 变体： (Variants:)
     - Range=DcmConfigSet/DcmDsp/DcmDsp/DcmDspDidRange.SHORT_NAME
   * - 生成条件： (Generate conditions:)
     - 1. DcmConfigSet/DcmDsp/DcmDsp/DcmDspDidRange.
   * - 
     - DcmDspDidRangeUsePort == TRUE
   * - 
     - And
   * - 
     - 2. Dcm/DcmConfigSet/DcmDsp/DcmDspDidRange/DcmDspDidRangeInfoRef->DcmDspDidRead!= NULL
   * - 端口类型： (Port Type:)
     - Require Port
   * - 从属端口： (Subordinate Port:)
     - DataServices_DIDRange\_{Range}




Rte_Call_Dcm_DataServices_DIDRange\_{Range}_WriteDidData
------------------------------------------------------------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Rte_Call_Dcm_DataServices_DIDRange\_{Range}_WriteDidData
   * - 引用函数定义： (Quote function definition:)
     - 详见4.4.16 (See 4.4.16)
   * - 变体： (Variants:)
     - Range=DcmConfigSet/DcmDsp/DcmDsp/DcmDspDidRange.SHORT_NAME
   * - 生成条件： (Generate conditions:)
     - 1. DcmConfigSet/DcmDsp/DcmDsp/DcmDspDidRange.
   * - 
     - DcmDspDidRangeUsePort == TRUE
   * - 
     - And
   * - 
     - 2. Dcm/DcmConfigSet/DcmDsp/DcmDspDidRange/DcmDspDidRangeInfoRef->DcmDspDidWrite!= NULL
   * - 端口类型： (Port Type:)
     - Require Port
   * - 从属端口： (Subordinate Port:)
     - DataServices_DIDRange\_{Range}




Rte_Call_Dcm_DataServices\_{Data}_ConditionCheckRead
--------------------------------------------------------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Rte_Call_Dcm_DataServices\_{Data}_ConditionCheckRead
   * - 引用函数定义： (Quote function definition:)
     - 详见4.4.7 (See 4.4.7)
   * - 变体： (Variants:)
     - Data=DcmConfigSet/DcmDsp/DcmDspData.SHORT-NAME
   * - 生成条件： (Generate conditions:)
     - 1. DcmConfigSet/DcmDsp/DcmDspData.DcmDspDataUsePort==USE_DATA_SYNCH_CLIENT_SERVER/USE_DATA_ASYNCH_CLIENT_SERVER/USE_DATA_ASYNCH_CLIENT_SERVER_ERROR
   * - 
     - And
   * - 
     - 2. DcmConfigSet/DcmDsp/DcmDspDidInfo/DcmDspDidRead !=NULL
   * - 
     - And
   * - 
     - 3. (Dcm/DcmConfigSet/DcmDsp/DcmDspData.DcmDspDataConditionCheckReadFncUsed== TRUE
   * - 端口类型： (Port Type:)
     - Require Port
   * - 从属端口： (Subordinate Port:)
     - DataServices\_{Data}




Rte_Call_Dcm_DataServices\_{Data}_FreezeCurrentState
--------------------------------------------------------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Rte_Call_Dcm_DataServices\_{Data}_FreezeCurrentState
   * - 引用函数定义： (Quote function definition:)
     - 详见4.4.12 (See 4.4.12)
   * - 变体： (Variants:)
     - Data=DcmConfigSet/DcmDsp/DcmDspData.SHORT-NAME
   * - 生成条件： (Generate conditions:)
     - 1. DcmConfigSet/DcmDsp/DcmDspData.DcmDspDataUsePort==USE_DATA_SYNCH_CLIENT_SERVER/USE_DATA_ASYNCH_CLIENT_SERVER/USE_DATA_ASYNCH_CLIENT_SERVER_ERROR
   * - 
     - And
   * - 
     - 2. DcmConfigSet/DcmDsp/DcmDspDidInfo/DcmDspDidControl/DcmDspDidFreezeCurrentState==TRUE
   * - 端口类型： (Port Type:)
     - Require Port
   * - 从属端口： (Subordinate Port:)
     - DataServices\_{Data}




Rte_Call_Dcm_DataServices\_{Data}_GetScalingInformation
-----------------------------------------------------------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Rte_Call_Dcm_DataServices\_{Data}_GetScalingInformation
   * - 引用函数定义： (Quote function definition:)
     - 详见4.4.8 (See 4.4.8)
   * - 变体： (Variants:)
     - Data=DcmConfigSet/DcmDsp/DcmDspData.SHORT-NAME
   * - 生成条件： (Generate conditions:)
     - 1. DcmConfigSet/DcmDsp/DcmDspData.DcmDspDataUsePort==USE_DATA_SYNCH_CLIENT_SERVER/USE_DATA_ASYNCH_CLIENT_SERVER/USE_DATA_ASYNCH_CLIENT_SERVER_ERROR
   * - 
     - And
   * - 
     - 2. DcmConfigSet/DcmDsp/DcmDspData/DcmDspDataInfoRef->DcmDspDataScalingInfoSize!= NULL
   * - 端口类型： (Port Type:)
     - Require Port
   * - 从属端口： (Subordinate Port:)
     - DataServices\_{Data}




Rte_Call_Dcm_DataServices\_{Data}_ReadData
----------------------------------------------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Rte_Call_Dcm_DataServices\_{Data}_ReadData
   * - 引用函数定义： (Quote function definition:)
     - 详见4.4.4 (See 4.4.4)
   * - 变体： (Variants:)
     - Data=
   * - 
     - 1. DcmConfigSet/DcmDsp/DcmDspData.SHORT-NAME
   * - 
     - Or
   * - 
     - 2. DcmConfigSet/DcmDsp/DcmDspPid/DcmDspPidData.SHORT-NAME
   * - 生成条件： (Generate conditions:)
     - {
   * - 
     - 1. DcmConfigSet/DcmDsp/DcmDspData.DcmDspDataUsePort==USE_DATA_SYNCH_CLIENT_SERVER/USE_DATA_ASYNCH_CLIENT_SERVER/USE_DATA_ASYNCH_CLIENT_SERVER_ERROR
   * - 
     - And
   * - 
     - 2. DcmConfigSet/DcmDsp/DcmDspDidInfo/DcmDspDidRead !=NULL
   * - 
     - }
   * - 
     - Or
   * - 
     - {
   * - 
     - DcmConfigSet/DcmDsp/DcmDspPid/DcmDspPidData/DcmDspPidService01.DcmDspPidDataUsePort== USE_DATA_SYNCH_CLIENT_SERVER
   * - 
     - }
   * - 端口类型： (Port Type:)
     - Require Port
   * - 从属端口： (Subordinate Port:)
     - DataServices\_{Data}




Rte_Call_Dcm_DataServices\_{Data}_ReadDataLength
----------------------------------------------------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Rte_Call_Dcm_DataServices\_{Data}_ReadDataLength
   * - 引用函数定义： (Quote function definition:)
     - 详见4.4.6 (See 4.4.6)
   * - 变体： (Variants:)
     - Data=DcmConfigSet/DcmDsp/DcmDspData.SHORT-NAME
   * - 生成条件： (Generate conditions:)
     - 1. DcmConfigSet/DcmDsp/DcmDspData.DcmDspDataUsePort==USE_DATA_SYNCH_CLIENT_SERVER/USE_DATA_ASYNCH_CLIENT_SERVER/USE_DATA_ASYNCH_CLIENT_SERVER_ERROR
   * - 
     - And
   * - 
     - 2. DcmConfigSet/DcmDsp/DcmDspDidInfo/DcmDspDidRead !=NULL
   * - 
     - And
   * - 
     - 3. Dcm/DcmConfigSet/DcmDsp/DcmDspData.DcmDspDataType== UINT8_DYN
   * - 端口类型： (Port Type:)
     - Require Port
   * - 从属端口： (Subordinate Port:)
     - DataServices\_{Data}




Rte_Call_Dcm_DataServices\_{Data}_ResetToDefault
----------------------------------------------------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Rte_Call_Dcm_DataServices\_{Data}_ResetToDefault
   * - 引用函数定义： (Quote function definition:)
     - 详见4.4.11 (See 4.4.11)
   * - 变体： (Variants:)
     - Data=DcmConfigSet/DcmDsp/DcmDspData.SHORT-NAME
   * - 生成条件： (Generate conditions:)
     - 1. DcmConfigSet/DcmDsp/DcmDspData.DcmDspDataUsePort==USE_DATA_SYNCH_CLIENT_SERVER/USE_DATA_ASYNCH_CLIENT_SERVER/USE_DATA_ASYNCH_CLIENT_SERVER_ERROR
   * - 
     - And
   * - 
     - 2. DcmConfigSet/DcmDsp/DcmDspDidInfo/DcmDspDidControl/DcmDspDidResetToDefault== TRUE
   * - 端口类型： (Port Type:)
     - Require Port
   * - 从属端口： (Subordinate Port:)
     - DataServices\_{Data}




Rte_Call_Dcm_DataServices\_{Data}_ReturnControlToECU
--------------------------------------------------------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Rte_Call_Dcm_DataServices\_{Data}_ReturnControlToECU
   * - 引用函数定义： (Quote function definition:)
     - 详见4.4.10 (See 4.4.10)
   * - 变体： (Variants:)
     - Data=DcmConfigSet/DcmDsp/DcmDspData.SHORT-NAME
   * - 生成条件： (Generate conditions:)
     - 1. DcmConfigSet/DcmDsp/DcmDspData.DcmDspDataUsePort==USE_DATA_SYNCH_CLIENT_SERVER/USE_DATA_ASYNCH_CLIENT_SERVER/USE_DATA_ASYNCH_CLIENT_SERVER_ERROR
   * - 
     - And
   * - 
     - {
   * - 
     - 1. DcmConfigSet/DcmDsp/DcmDspDidInfo/DcmDspDidControl/DcmDspDidFreezeCurrentState== TRUE
   * - 
     - Or
   * - 
     - 2. DcmConfigSet/DcmDsp/DcmDspDidInfo/DcmDspDidControl/
   * - 
     - DcmDspDidResetToDefault == TRUE
   * - 
     - Or
   * - 
     - 3. DcmConfigSet/DcmDsp/DcmDspDidInfo/DcmDspDidControl/
   * - 
     - DcmDspDidShortTermAdjustment == TRUE
   * - 
     - }
   * - 端口类型： (Port Type:)
     - Require Port
   * - 从属端口： (Subordinate Port:)
     - DataServices\_{Data}




Rte_Call_Dcm_DataServices\_{Data}_ShortTermAdjustment
---------------------------------------------------------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Rte_Call_Dcm_DataServices\_{Data}_ShortTermAdjustment
   * - 引用函数定义： (Quote function definition:)
     - 详见4.4.13 (See 4.4.13)
   * - 变体： (Variants:)
     - Data=DcmConfigSet/DcmDsp/DcmDspData.SHORT-NAME
   * - 生成条件： (Generate conditions:)
     - 1. DcmConfigSet/DcmDsp/DcmDspData.DcmDspDataUsePort==USE_DATA_SYNCH_CLIENT_SERVER/USE_DATA_ASYNCH_CLIENT_SERVER/USE_DATA_ASYNCH_CLIENT_SERVER_ERROR
   * - 
     - And
   * - 
     - 2. DcmConfigSet/DcmDsp/DcmDspDidInfo/DcmDspDidControl/
   * - 
     - DcmDspDidShortTermAdjustment == TRUE
   * - 端口类型： (Port Type:)
     - Require Port
   * - 从属端口： (Subordinate Port:)
     - DataServices\_{Data}




Rte_Call_Dcm_InfotypeServices\_{VehInfoData}_GetInfotypeValueData
---------------------------------------------------------------------------------

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Rte_Call_Dcm_InfotypeServices\_{VehInfoData}_GetInfotypeValueData
     - 
     - 
   * - 函数定义： (Function definition:)
     - Std_ReturnTypeRte_Call_Dcm_InfotypeServices\_{VehInfoData}_GetInfotypeValueData(const Dcm_OpStatusType OpStatus,
     - 
     - 
   * - 
     - InfoTypeServicesArrayType\_{VehInfoData}
     - 
     - 
   * - 
     - DataValueBuffer,
     - 
     - 
   * - 
     - uint8\* DataValueBufferSize)
     - 
     - 
   * - 服务编号： (Service Number:)
     - N/A
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - N/A
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - N/A
     - 
     - 
   * - 输入参数： (Input parameters:)
     - OpStatus：操作类型 (OpStatus：Operation Type)
     - 值域： (Domain:)
     - DCM_INITIALDCM_PENDINGDCM_CANCEL
   * - 
     - 
     - 
     - DCM_FORCE_RCRRP_OK
   * - 输入输出参数： (Input Output Parameters:)
     - DataValueBufferSize：数据长度 (DataValueBufferSize: Data Length)
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - DataValueBuffer：数据内容注：InfoTypeServicesArrayType\_{VehInfoData}类型实际为uint8\* (DataValueBuffer: Data content note: InfoTypeServicesArrayType_VehInfoData type actually is uint8*)
     - 
     - 
   * - 返回值： (Return Value:)
     - Std_ReturnType：E_OK： 成功E_NOT_OK： 失败 (Std_ReturnType：E_OK： Success E_NOT_OK： Failure)
     - 
     - 
   * - 
     - DCM_E_PENDING： 暂未完成 (DCM_E_PENDING: Not Completed Yet)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 获取车辆信息数据 (Get vehicle information data)
     - 
     - 
   * - 变体： (Variants:)
     - VehInfoData=DcmConfigSet/DcmDsp/DcmDspVehInfo/DcmDspVehInfoData.SHORT-NAME
     - 
     - 
   * - 生成条件： (Generate conditions:)
     - DcmConfigSet/DcmDsp/DcmDspVehInfo/DcmDspVehInfoData/DcmDspVehInfoDataUsePort == TRUE
     - 
     - 
   * - 端口类型： (Port Type:)
     - Require Port
     - 
     - 
   * - 从属端口： (Subordinate Port:)
     - InfotypeServices\_{VehInfoData}
     - 
     - 




Rte_Call_Dcm_RoutineServices\_{RoutineName}_RequestResults
--------------------------------------------------------------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Rte_Call_Dcm_RoutineServices\_{RoutineName}_RequestResults
   * - 引用函数定义： (Quote function definition:)
     - 详见4.4.20 (See 4.4.20)
   * - 变体： (Variants:)
     - RoutineName=DcmConfigSet/DcmDsp/DcmDspRRoutine.SHORT_NAME
   * - 生成条件： (Generate conditions:)
     - 1. DcmConfigSet/DcmDsp/DcmDspRRoutine.DcmDspRoutineUsePort== TRUE
   * - 
     - And
   * - 
     - 2. DcmConfigSet/DcmDsp/DcmDspRoutine/DcmDspRequestRoutineResults!= NULL
   * - 端口类型： (Port Type:)
     - Require Port
   * - 从属端口： (Subordinate Port:)
     - RoutineServices\_{RoutineName}




Rte_Call_Dcm_RoutineServices\_{RoutineName}_Start
-----------------------------------------------------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Rte_Call_Dcm_RoutineServices\_{RoutineName}_Start
   * - 引用函数定义： (Quote function definition:)
     - 详见4.4.18 (See 4.4.18)
   * - 变体： (Variants:)
     - RoutineName=DcmConfigSet/DcmDsp/DcmDspRRoutine.SHORT_NAME
   * - 生成条件： (Generate conditions:)
     - 1. DcmConfigSet/DcmDsp/DcmDspRRoutine.DcmDspRoutineUsePort== TRUE
   * - 
     - And
   * - 
     - 2.
   * - 
     - DcmConfigSet/DcmDsp/DcmDspRoutine/DcmDspStartRoutine!= NULL
   * - 端口类型： (Port Type:)
     - Require Port
   * - 从属端口： (Subordinate Port:)
     - RoutineServices\_{RoutineName}




Rte_Call_Dcm_RoutineServices\_{RoutineName}_Stop
----------------------------------------------------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Rte_Call_Dcm_RoutineServices\_{RoutineName}_Stop
   * - 引用函数定义： (Quote function definition:)
     - 详见4.4.19 (See 4.4.19)
   * - 变体： (Variants:)
     - RoutineName=DcmConfigSet/DcmDsp/DcmDspRRoutine.SHORT_NAME
   * - 生成条件： (Generate conditions:)
     - 1. DcmConfigSet/DcmDsp/DcmDspRRoutine.DcmDspRoutineUsePort== TRUE
   * - 
     - And
   * - 
     - 2. DcmConfigSet/DcmDsp/DcmDspRoutine/DcmDspStopRoutine!= NULL
   * - 端口类型： (Port Type:)
     - Require Port
   * - 从属端口： (Subordinate Port:)
     - RoutineServices\_{RoutineName}




Rte_Call_Dcm_RequestControlServices\_{Tid}_RequestControl
-------------------------------------------------------------------------

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Rte_Call_Dcm_RequestControlServices\_{Tid}_RequestControl
     - 
     - 
   * - 函数定义： (Function definition:)
     - Std_ReturnTypeRte_Call_Dcm_RequestControlServices\_{Tid}_RequestControl
     - 
     - 
   * - 
     - (RequestControlServicesOutArrayType\_{Tid}
     - 
     - 
   * - 
     - OutBuffer,
     - 
     - 
   * - 
     - constRequestControlServicesInArrayType\_{Tid}
     - 
     - 
   * - 
     - InBuffer
     - 
     - 
   * - 
     - )
     - 
     - 
   * - 服务编号： (Service Number:)
     - N/A
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - N/A
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - N/A
     - 
     - 
   * - 输入参数： (Input parameters:)
     - InBuffer：输入数据的指针注：实际数据类型为uint8\* (InBuffer：Pointer to input data Note: Actual data type is uint8*)
     - 值域： (Domain:)
     - 无
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - OutBuffer：输出数据 (OutBuffer：output data)
     - 
     - 
   * - 
     - 注：实际数据类型为uint8\* (Note: The actual data type is uint8*.)
     - 
     - 
   * - 返回值： (Return Value:)
     - Std_ReturnType：
     - 
     - 
   * - 
     - E_OK： 成功 (E_OK: Success)
     - 
     - 
   * - 
     - E_NOT_OK： 失败 (E_NOT_OK: Failure)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 请求控制 (Request Control)
     - 
     - 
   * - 变体： (Variants:)
     - Tid=DcmConfigSet/DcmDsp/DcmDspRequestControl.SHORT-NAME
     - 
     - 
   * - 生成条件： (Generate conditions:)
     - DcmConfigSet/DcmDsp/DcmDspRequestControl!= NULL
     - 
     - 
   * - 端口类型： (Port Type:)
     - Require Port
     - 
     - 
   * - 从属端口： (Subordinate Port:)
     - RequestControlServices\_{Tid}
     - 
     - 




Rte_Call_Dcm_SecurityAccess\_{SecurityLevel}_CompareKey
-----------------------------------------------------------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Rte_Call_Dcm_SecurityAccess\_{SecurityLevel}_CompareKey
   * - 引用函数定义： (Quote function definition:)
     - 详见4.4.2 (See 4.4.2)
   * - 变体： (Variants:)
     - SecurityLevel=DcmConfigSet/DcmDsp/DcmDspSecurity/DcmDspSecurityRow.SHORT-NAME
   * - 生成条件： (Generate conditions:)
     - DcmConfigSet/DcmDsp/DcmDspSecurity/DcmDspSecurityRow.
   * - 
     - DcmDspSecurityUsePort == USE_ASYNCH_CLIENT_SERVER
   * - 端口类型： (Port Type:)
     - Require Port
   * - 从属端口： (Subordinate Port:)
     - SecurityAccess\_{SecurityLevel}




Rte_Call_Dcm_SecurityAccess\_{SecurityLevel}_GetSecurityAttemptCounter
--------------------------------------------------------------------------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Rte_Call_Dcm_SecurityAccess\_{SecurityLevel}_GetSecurityAttemptCounter
   * - 引用函数定义： (Quote function definition:)
     - 详见4.4.3 (See 4.4.3)
   * - 变体： (Variants:)
     - SecurityLevel=DcmConfigSet/DcmDsp/DcmDspSecurity/DcmDspSecurityRow.SHORT-NAME
   * - 生成条件： (Generate conditions:)
     - 1.
   * - 
     - DcmConfigSet/DcmDsp/DcmDspSecurity/DcmDspSecurityRow.
   * - 
     - DcmDspSecurityAttemptCounterEnabled == TRUE
   * - 
     - And
   * - 
     - 2. DcmConfigSet/DcmDsp/DcmDspSecurity/DcmDspSecurityRow.DcmDspSecurityUsePort== USE_ASYNCH_CLIENT_SERVER
   * - 端口类型： (Port Type:)
     - Require Port
   * - 从属端口： (Subordinate Port:)
     - SecurityAccess\_{SecurityLevel}




Rte_Call_Dcm_SecurityAccess\_{SecurityLevel}_GetSeed
--------------------------------------------------------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Rte_Call_Dcm_SecurityAccess\_{SecurityLevel}_GetSeed
   * - 引用函数定义： (Quote function definition:)
     - 详见4.4.1 (See 4.4.1)
   * - 变体： (Variants:)
     - SecurityLevel=DcmConfigSet/DcmDsp/DcmDspSecurity/DcmDspSecurityRow.SHORT-NAME
   * - 生成条件： (Generate conditions:)
     - DcmConfigSet/DcmDsp/DcmDspSecurity/DcmDspSecurityRow.DcmDspSecurityUsePort== USE_ASYNCH_CLIENT_SERVER
   * - 端口类型： (Port Type:)
     - Require Port
   * - 从属端口： (Subordinate Port:)
     - SecurityAccess\_{SecurityLevel}




Rte_Call_Dcm_SecurityAccess\_{SecurityLevel}_SetSecurityAttemptCounter
--------------------------------------------------------------------------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Rte_Call_Dcm_SecurityAccess\_{SecurityLevel}_SetSecurityAttemptCounter
   * - 引用函数定义： (Quote function definition:)
     - 详见4.4.9 (See 4.4.9)
   * - 变体： (Variants:)
     - SecurityLevel=DcmConfigSet/DcmDsp/DcmDspSecurity/DcmDspSecurityRow.SHORT-NAME
   * - 生成条件： (Generate conditions:)
     - 1. DcmConfigSet/DcmDsp/DcmDspSecurity/DcmDspSecurityRow.DcmDspSecurityUsePort== USE_ASYNCH_CLIENT_SERVER
   * - 
     - And
   * - 
     - 2. DcmConfigSet/DcmDsp/DcmDspSecurity/DcmDspSecurityRow.DcmDspSecurityAttemptCounterEnabled== TRUE
   * - 端口类型： (Port Type:)
     - Require Port
   * - 从属端口： (Subordinate Port:)
     - SecurityAccess\_{SecurityLevel}




Rte_Call_Dcm_ServiceRequestNotification_Confirmation 
---------------------------------------------------------------------

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Std_ReturnTypeRte\_Call\_Dcm_ServiceRequestNotification_Confirmation
     - 
     - 
   * - 
     - (const uint8 SID,
     - 
     - 
   * - 
     - const uint8 ReqType,
     - 
     - 
   * - 
     - const uint16 SourceAddress,
     - 
     - 
   * - 
     - const Dcm_ConfirmationStatusTypeconfirmationStatus)
     - 
     - 
   * - 函数定义： (Function definition:)
     - 
     - 
     - 
   * - 服务编号： (Service Number:)
     - N/A
     - 
     - 
   * - 同步/异步： (Synchronous/asynchronous:)
     - N/A
     - 
     - 
   * - 是否可重入： (Is Reentrant:)
     - N/A
     - 
     - 
   * - 输入参数： (Input parameters:)
     - SID：服务ID (Service ID)
     - 值域： (Domain:)
     - 0…255
   * - 
     - ReqType：请求类型 (ReqType：Request Type)
     - 值域： (Domain:)
     - 0…255
   * - 
     - SourceAddress：源地址 (Source Address：Source address)
     - 值域： (Domain:)
     - 0…65535
   * - 
     - confirmationStatus：确认状态 (confirmationStatus：Confirmation Status)
     - 值域： (Domain:)
     - 0…255
   * - 输入输出参数： (Input Output Parameters:)
     - 无
     - 
     - 
   * - 输出参数： (Output Parameters:)
     - 无
     - 
     - 
   * - 返回值： (Return Value:)
     - Std_ReturnType：E_OK： 成功 (Std_ReturnType: E_OK: Success)
     - 
     - 
   * - 
     - E_NOT_OK： 失败 (E_NOT_OK: Failure)
     - 
     - 
   * - 功能概述： (Function Overview:)
     - 服务请求通知确认 (Service Request Notification Confirmation)
     - 
     - 
   * - 变体： (Variants:)
     - 无
     - 
     - 
   * - 生成条件： (Generate conditions:)
     - 1. DcmConfigSet/DcmDsd/DcmDsdRequestManufacturerNotificationEnabled== TRUE
     - 
     - 
   * - 
     - Or
     - 
     - 
   * - 
     - 2. DcmConfigSet/DcmDsd/DcmDsdRequestSupplierNotificationEnabled== TRUE
     - 
     - 
   * - 端口类型： (Port Type:)
     - Require Port
     - 
     - 
   * - 从属端口： (Subordinate Port:)
     - ServiceRequestManufacturerNotification\_{Name}
     - 
     - 
   * - 
     - And
     - 
     - 
   * - 
     - ServiceRequestSupplierNotification\_{Name}
     - 
     - 




Rte_Call\_<UserModule>\_<UserPortName>_TriggerOnEvent
---------------------------------------------------------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Rte_Call\_<UserModule>\_<UserPortName>_TriggerOnEvent
   * - 运行实体函数定义： (Definition of running entity function:)
     - 详见4.3.9 (See 4.3.9)
   * - 变体： (Variants:)
     - RoeName=Dcm/DcmConfigSet/DcmDsp/DcmDspRoe/DcmDspRoeEvent.
   * - 
     - SHORT-NAME
   * - 生成条件： (Generate conditions:)
     - ConfigSet/DcmDsp/DcmDspRoe/DcmDspRoeEvent != NULL
   * - 端口类型： (Port Type:)
     - Provided Port
   * - 从属端口： (Subordinate Port:)
     - DCM_Roe\_{RoeName}




Rte_Call\_<UserModule>\_<UserPortName>_GetActiveProtocol
------------------------------------------------------------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Rte_Call\_<UserModule>\_<UserPortName>_GetActiveProtocol
   * - 运行实体函数定义： (Definition of running entity function:)
     - 详见4.3.7 (See 4.3.7)
   * - 变体： (Variants:)
     - 无
   * - 生成条件： (Generate conditions:)
     - 无
   * - 端口类型： (Port Type:)
     - Provided Port
   * - 从属端口： (Subordinate Port:)
     - DCMServices




Rte_Call\_<UserModule>\_<UserPortName>_GetSecurityLevel
-----------------------------------------------------------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Rte_Call\_<UserModule>\_<UserPortName>_GetSecurityLevel
   * - 运行实体函数定义： (Definition of running entity function:)
     - 详见4.3.5 (See 4.3.5)
   * - 变体： (Variants:)
     - 无
   * - 生成条件： (Generate conditions:)
     - 无
   * - 端口类型： (Port Type:)
     - Provided Port
   * - 从属端口： (Subordinate Port:)
     - DCMServices




Rte_Call\_<UserModule>\_<UserPortName>_GetSesCtrlType
---------------------------------------------------------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Rte_Call\_<UserModule>\_<UserPortName>_GetSesCtrlType
   * - 运行实体函数定义： (Definition of running entity function:)
     - 详见4.3.6 (See 4.3.6)
   * - 变体： (Variants:)
     - 无
   * - 生成条件： (Generate conditions:)
     - 无
   * - 端口类型： (Port Type:)
     - Provided Port
   * - 从属端口： (Subordinate Port:)
     - DCMServices




Rte_Call\_<UserModule>\_<UserPortName>_ResetToDefaultSession
----------------------------------------------------------------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Rte_Call\_<UserModule>\_<UserPortName>_ResetToDefaultSession
   * - 运行实体函数定义： (Definition of running entity function:)
     - 详见4.3.8 (See 4.3.8)
   * - 变体： (Variants:)
     - 无
   * - 生成条件： (Generate conditions:)
     - 无
   * - 端口类型： (Port Type:)
     - Provided Port
   * - 从属端口： (Subordinate Port:)
     - DCMServices




Rte_Call\_<UserModule>\_<UserPortName>_SetActiveDiagnostic
--------------------------------------------------------------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 函数名称： (Function Name:)
     - Rte_Call\_<UserModule>\_<UserPortName>_SetActiveDiagnostic
   * - 运行实体函数定义： (Definition of running entity function:)
     - 详见4.3.10 (See 4.3.10)
   * - 变体： (Variants:)
     - 无
   * - 生成条件： (Generate conditions:)
     - 无
   * - 端口类型： (Port Type:)
     - Provided Port
   * - 从属端口： (Subordinate Port:)
     - DCMServices




模式转换接口封装 (Interface Encapsulation for Mode Conversion)
======================================================================

DcmDiagnosticSessionControl
-------------------------------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 接口名称： (Interface Name:)
     - DcmDiagnosticSessionControl
   * - 变体： (Variants:)
     - 无
   * - 生成条件： (Generate conditions:)
     - DcmConfigSet/DcmDsp/DcmDspSession/DcmDspSessionRow!= NULL
   * - 模式组： (Pattern Group:)
     - diagnosticSession
   * - 端口类型： (Port Type:)
     - Provided Port
   * - 从属端口： (Subordinate Port:)
     - modeSwitchPort_DcmDiagnosticSessionControl




DcmEcuReset
---------------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 接口名称： (Interface Name:)
     - DcmEcuReset
   * - 变体： (Variants:)
     - 无
   * - 生成条件： (Generate conditions:)
     - 无
   * - 模式组： (Pattern Group:)
     - ecuReset
   * - 端口类型： (Port Type:)
     - Provided Port
   * - 从属端口： (Subordinate Port:)
     - modeSwitchPort_DcmEcuReset




配置 (Configure)
==============================

DcmGeneral
--------------------------

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/DCM/image4.png
   :alt: DcmGeneral容器配置图 (DcmGeneral Container Configuration Diagram)
   :name: DcmGeneral容器配置图 (DcmGeneral Container Configuration Diagram)
   :align: center


.. centered:: **表 DcmGeneral容器配置 (Table DcmGeneral Container Configuration)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - DcmConfigType
     - 取值范围 (Range)
     - PB_CONFIG/PC_CONFIG
     - 默认取值 (Default value)
     - PC_CONFIG
   * - 
     - 
     - 控制Dcm模块配置权限 (Control Dcm module configuration permissions)
     - 
     -
   * - 
     - 
     - 无
     - 
     - 
   * - DcmDDDIDStorage
     - 取值范围 (Range)
     - true/false
     - 默认取值 (Default value)
     - FALSE
   * - 
     - 参数描述 (Parameter Description)
     - 定义的DDDID存储使能开关 (Defined DDDID Storage Enable Switch)
     - 
     -
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDevErrorDetect
     - 取值范围 (Range)
     - true/false
     - 默认取值 (Default value)
     - TRUE
   * - 
     - 
     - DET检查使能开关 (DET Check Enable Switch)
     - 
     -
   * - 
     - 
     - 无
     - 
     - 
   * - PreemptionProtocolCancelSupport
     - 
     - true/false
     - 
     -
   * - 
     - 取值范围 (Range)
     - 抢占协议取消支持使能开关 (Disable switch for protocol preempt support)
     - 
     -
   * - 
     - 
     - 无
     - 
     - 
   * - DcmHeaderFileInclusion
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 
     - 头文件包含 (Header file inclusion)
     - 
     -
   * - 
     - 
     - 无
     - 
     - 
   * - DcmRespondAllRequest
     - 
     - true/false
     - 
     -
   * - 
     - 取值范围 (Range)
     - 如果设置为FALSE, Dcm将不会响应包含服务ID的诊断请求，服务ID的范围是0x40到0x7F或0xC0到0xFF(响应ID)。 (If set to FALSE, Dcm will not respond to diagnostic requests that include a service ID, where the service ID ranges from 0x40 to 0x7F or 0xC0 to 0xFF (response ID).)
     - 
     -
   * - 
     - 
     - 无
     - 
     - 
   * - DcmTaskTime
     - 取值范围 (Range)
     - 1E-4 ... 0.1
     - 默认取值 (Default value)
     - 0.001
   * - 
     - 
     - 主函数调用周期 (Main function call period)
     - 
     -
   * - 
     - 
     - 依赖于底层硬件要求 (Dependent on underlying hardware requirements)
     - 
     - 
   * - DcmVersionInfoApi
     - 
     - true/false
     - 
     -
   * - 
     - 
     - 获取版本信息接口使能开关 (Enable Switch for Getting Version Information Interface)
     - 
     -
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - 
     - 取值范围 (Range)
     - Os/Callout/Tm/MainFunction
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 选择计时类型[1] (Select Timer Type [1])
     - 
     -
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmNvRamBlockIdRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 动态DID存储的NVM的块关联 (Dynamic DID storage block association in NVM)
     - 
     -
   * - 
     - 依赖关系 (Dependencies)
     - DcmDDDIDStorage配置打开 (DCMDDDIIDStorage Configuration Enabled)
     - 
     - 
   * - DcmVinRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - VIN码信息关联DID (VIN Code information associates with DID)
     - 
     -
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 




DcmConfigSet
----------------------------

DcmDsd
~~~~~~~~~~~~

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/DCM/image5.png
   :alt: DcmDsd容器配置图 (Container Configuration Diagram for DcmDsd)
   :name: DcmDsd容器配置图 (Container Configuration Diagram for DcmDsd)
   :align: center


.. centered:: **表 DcmDsd属性描述 (Table DcmDsd Property Description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - DcmDsdRequestManufacturerNotificationEnabled
     - 取值范围 (Range)
     - true/false
     - 默认取值 (Default value)
     - False
   * - 
     - 参数描述 (Parameter Description)
     - 请求通知主机厂通知函数使能开关 (Request notify host factory enable switch function notify)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDsdRequestSupplierNotificationEnabled
     - 取值范围 (Range)
     - true/false
     - 默认取值 (Default value)
     - False
   * - 
     - 参数描述 (Parameter Description)
     - 请求通知供应商通知函数使能开关 (Request notify supplier notification function enable switch)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 




DcmDsdServiceRequestManufacturerNotification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/DCM/image6.png
   :alt: DcmDsdServiceRequestManufacturerNotification容器配置图 (DcmDsdServiceRequestManufacturerNotification Container Configuration Diagram)
   :name: DcmDsdServiceRequestManufacturerNotification容器配置图 (DcmDsdServiceRequestManufacturerNotification Container Configuration Diagram)
   :align: center


.. centered:: **表 DcmDsdServiceRequestManufacturerNotification属性描述 (Table DcmDsdServiceRequestManufacturerNotification Property Description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - DcmDsdServiceRequestManufacturerNotification
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 主机厂通知接口 (Automaker notification interface)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - DcmDsdRequestManufacturerNotificationEnabled打开 (DcmDsdRequestManufacturerNotificationEnabled Enabled)
     - 
     - 




DcmDsdServiceRequestSupplierNotification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/DCM/image7.png
   :alt: DcmDsdServiceRequestSupplierNotification容器配置图 (DcmDsdServiceRequestSupplierNotification Container Configuration Diagram)
   :name: DcmDsdServiceRequestSupplierNotification容器配置图 (DcmDsdServiceRequestSupplierNotification Container Configuration Diagram)
   :align: center


.. centered:: **表 DcmDsdServiceRequestSupplierNotification属性描述 (Table DcmDsdServiceRequestSupplierNotification Property Description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - DcmDsdServiceRequestSupplierNotification
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 供应商通知接口 (Supplier Notification Interface)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - DcmDsdRequestSupplierNotificationEnabled打开 (DcmDsdRequestSupplierNotificationEnabled Enabled)
     - 
     - 




DcmDsdServiceTable
~~~~~~~~~~~~~~~~~~~~~

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/DCM/image8.png
   :alt: DcmDsdServiceTable容器配置图 (DcmDsdServiceTable Container Configuration Diagram)
   :name: DcmDsdServiceTable容器配置图 (DcmDsdServiceTable Container Configuration Diagram)
   :align: center


.. centered:: **表 DcmDsdServiceTable属性描述 (Table DcmDsdServiceTable Properties Description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - DcmDsdSidTabId
     - 取值范围 (Range)
     - 0 … 255
     - 默认取值 (Default value)
     - 当前index (Current index)
   * - 
     - 参数描述 (Parameter Description)
     - 唯一的服务表号 (Unique service number)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 




DcmDsdService
~~~~~~~~~~~~~~~~~~~~~

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/DCM/image9.png
   :alt: DcmDsdService容器配置图(Diagram of DcmDsdService Container Configuration)
   :name: DcmDsdService容器配置图(Diagram of DcmDsdService Container Configuration)
   :align: center

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/DCM/image10.png
   :alt: DcmDsdService容器配置图1(Diagram of DcmDsdService Container Configuration)
   :name: DcmDsdService容器配置图1(Diagram of DcmDsdService Container Configuration)
   :align: center

.. centered:: **表 DcmDsdService属性描述 (Table DcmDsdService Property Description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - DcmDsdServiceUsed
     - 取值范围 (Range)
     - true/false
     - 默认取值 (Default value)
     - True
   * - 
     - 参数描述 (Parameter Description)
     - 服务使能开关 (Service Enable Switch)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDsdSidTabFnc
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - NULL_PTR
   * - 
     - 参数描述 (Parameter Description)
     - 服务的回调接口 (The callback interface of the service)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 根据DcmDsdSidTabServiceId的配置自动获取对应接口名字，如配置值的服务不支持，则报错。 (Automatically obtain the corresponding interface name based on the configuration of DcmDsdSidTabServiceId. If the configured service is not supported, an error will be reported.)
     - 
     - 
   * - DcmDsdSidTabServiceId
     - 取值范围 (Range)
     - 0 ... 255
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - 服务ID值 (Service ID value)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDsdSidTabSubfuncAvail
     - 取值范围 (Range)
     - true/false
     - 默认取值 (Default value)
     - False
   * - 
     - 参数描述 (Parameter Description)
     - 服务的子服务使能开关 (Enable switch for sub-services of the service)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 默认生成，不可修改，根据ISO规范决定 (Default generated, non-modifiable, decided according to ISO norms)
     - 
     - 
   * - DcmDsdSuppressPosRsp
     - 取值范围 (Range)
     - true/false
     - 默认取值 (Default value)
     - False
   * - 
     - 参数描述 (Parameter Description)
     - 服务正响应抑制使能开关 (Service response inhibition enable switch)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - DcmDsdSidTabSubfuncAvail使能时可配置 (Enable when configurable)
     - 
     - 
   * - DcmDsdSidTabAddressingFormat
     - 取值范围 (Range)
     - PHYANDFUNC/PHYSICAL/FUNCTIONAL
     - 默认取值 (Default value)
     - PHYANDFUNC
   * - 
     - 参数描述 (Parameter Description)
     - 服务支持的寻址模式 (Addressing modes supported by service support)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDsdSidTabModeRuleRef
     - 取值范围 (Range)
     - Ref
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 对控制服务执行的DcmDspModeRule的引用 (The reference to DcmDspModeRule for controlling service execution)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - DcmModeRule
     - 
     - 
   * - DcmDsdSidTabSecurityLevelRef
     - 取值范围 (Range)
     - Ref
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 支持服务的安全级关联 (Association of Security Level for Support Service)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDsdSidTabSessionLevelRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 支持服务的会话级关联 (Session-level association for support services)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDsdServiceRoleRef
     - 取值范围 (Range)
     - Ref
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 对DcmDspAuthenticationRow的引用 (Reference to DcmDspAuthenticationRow)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 


DcmDsdSubService
~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/DCM/image11.png
   :alt: DcmDsdSubService容器配置图 (Container Configuration Diagram for DcmDsdSubService)
   :name: DcmDsdSubService容器配置图 (Container Configuration Diagram for DcmDsdSubService)
   :align: center

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/DCM/image12.png
   :alt: DcmDsdSubService容器配置图1 (Container Configuration Diagram for DcmDsdSubService)
   :name: DcmDsdSubService容器配置图1 (Container Configuration Diagram for DcmDsdSubService)
   :align: center


.. centered:: **表 DcmDsdSubService属性描述 (Table DcmDsdSubService Property Description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - DcmDsdSubServiceFnc
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 子服务的回调接口 (Callback interface of sub-services)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDsdSubServiceId
     - 取值范围 (Range)
     - 0 ... 255
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - 子服务ID值 (Service ID value)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 此处如果作为10/27服务的子服务，则需配置对应的DcmDspSessionRow/DcmDspSecurityRow来匹配会话级/安全级，如没有一一对应，则报错。 (If this is a sub-service of the 10/27 service, corresponding DcmDspSessionRow/DcmDspSecurityRow configurations are needed to match session-level/security-level. If there is no one-to-one correspondence, an error will be reported.)
     - 
     - 
   * - DcmDsdSubServiceRole
     - 取值范围 (Range)
     - 0 ... 4294967295
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 每个位代表一个专用的角色。如果位值为1，则授予诊断服务的子功能访问权限。如果位值为0，则不允许为该角色执行服务 (Each bit represents a dedicated role. If the bit value is 1, it grants access to sub-functions of diagnostic services for that role. If the bit value is 0, it does not allow service execution for that role.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDsdSubServiceUsed
     - 取值范围 (Range)
     - true/false
     - 默认取值 (Default value)
     - True
   * - 
     - 参数描述 (Parameter Description)
     - 子服务使能开关 (Service Enable Switch)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDsdSidTabModeRuleRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 对控制服务执行的DcmDspModeRule的引用。如果没有配置引用，则不进行模式规则检查 (Reference to DcmDspModeRule for controlling service execution. Mode rule checks are not performed if no reference is configured.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDsdSubServiceSecurityLevelRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 支持子服务的安全级关联 (Support sub-service security level association)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDsdSubServiceSessionLevelRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 支持子服务的会话级关联 (Session-level association for services with sub-services)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDsdSubServiceRoleRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 对DcmDspAuthenticationRow的引用 (Reference to DcmDspAuthenticationRow)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 




DcmDsl
~~~~~~~~~~~~~~~

DcmDslBuffer 
~~~~~~~~~~~~~~~~~

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/DCM/image13.png
   :alt: DcmDslBuffer容器配置图 (DcmDslBuffer Container Configuration Diagram)
   :name: DcmDslBuffer容器配置图 (DcmDslBuffer Container Configuration Diagram)
   :align: center


.. centered:: **表 DcmDslBuffer属性描述 (Table DcmDslBuffer Property Description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - DcmDslBufferSize
     - 取值范围 (Range)
     - 8 … 4294967294
     - 默认取值 (Default value)
     - 8
   * - 
     - 参数描述 (Parameter Description)
     - 缓冲区大小 (Buffer size)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 




DcmDslCallbackDCMRequestService 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/DCM/image14.png
   :alt: DcmDslCallbackDCMRequestService容器配置图 (Container Configuration Diagram for DcmDslCallbackDCMRequestService)
   :name: DcmDslCallbackDCMRequestService容器配置图 (Container Configuration Diagram for DcmDslCallbackDCMRequestService)
   :align: center


.. centered:: **表 DcmDslCallbackDCMRequestService属性描述 (Table DcmDslCallbackDCMRequestService Property Description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - DcmDslCallbackDCMRequestService
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 启动协议和停止协议的通知接口配置 (Notification interface configuration for start protocol and stop protocol notifications)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 多协议时需要配置此项，默认生成相关接口 (When configuring for multi-protocols, related interfaces are default generated.)
     - 
     - 




DcmDslDiagResp 
~~~~~~~~~~~~~~~~~~~~

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/DCM/image15.png
   :alt: DcmDslDiagResp容器配置图 (DcmDslDiagResp Container Configuration Diagram)
   :name: DcmDslDiagResp容器配置图 (DcmDslDiagResp Container Configuration Diagram)
   :align: center


.. centered:: **表 DcmDslDiagResp属性描述 (Table DcmDslDiagResp Property Description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - DcmDslDiagRespMaxNumRespPend
     - 取值范围 (Range)
     - 0 ...255
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - 一次服务请求0x78响应的最大次数 (The maximum number of responses for a service request 0x78)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDslDiagRespOnSecondDeclinedRequest
     - 取值范围 (Range)
     - true/false
     - 默认取值 (Default value)
     - False
   * - 
     - 参数描述 (Parameter Description)
     - 多设备请求时响应NRC0x21的使能开关 (Enable switch for responding NRC 0x21 when multiple device requests)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 




DcmDslProtocol
~~~~~~~~~~~~~~~~~

DcmDslProtocolRow
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/DCM/image16.png
   :alt: DcmDslProtocolRow容器配置图 (DcmDslProtocolRow Container Configuration Diagram)
   :name: DcmDslProtocolRow容器配置图 (DcmDslProtocolRow Container Configuration Diagram)
   :align: center


.. centered:: **表 DcmDslProtocolRow属性描述 (Table DcmDslProtocolRow Property Description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - DcmDslProtocolMaximumResponseSize
     - 取值范围 (Range)
     - 1 ... 65535
     - 默认取值 (Default value)
     - 0xfff
   * - 
     - 参数描述 (Parameter Description)
     - 分页发送能发送的最大长度 (Pagination sending can send the maximum length)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - DcmPagedBufferEnabled== TRUE
     - 
     - 
   * - DcmDslProtocolPriority
     - 取值范围 (Range)
     - 0 ... 255
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - 协议优先级 (Protocol Priority)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDslProtocolRowUsed
     - 取值范围 (Range)
     - true/false
     - 默认取值 (Default value)
     - True
   * - 
     - 参数描述 (Parameter Description)
     - 协议使能开关 (Enable Switch)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDslProtocolTransType
     - 取值范围 (Range)
     - TYPE1/TYPE2
     - 默认取值 (Default value)
     - TYPE1
   * - 
     - 参数描述 (Parameter Description)
     - 协议传输类型 (Protocol transmission type)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 未使用，可以不用关心 (Not used, can be ignored.)
     - 
     - 
   * - DcmDslProtocolType
     - 取值范围 (Range)
     - DCM_OBD_ON_CAN/DCM_OBD_ON_FLEXRAY/DCM_OBD_ON_IP/DCM\_PERIODICTRANS_ON_CAN/DCM_PERIODICTRANS_ON_FLEXRAY/DCM_PERIODICTRANS_ON_IP/DCM_ROE_ON_CAN/DCM_ROE_ON_FLEXRAY/DCM\_ROE_ON_IP/DCM_SUPPLIER_1/DCM_SUPPLIER_10/DCM_SUPPLIER_11/DCM_SUPPLIER_12/DCM_SUPPLIER_13/DCM_SUPPLIER_14/DCM_SUPPLIER_15/DCM_SUPPLIER_2/DCM_SUPPLIER_3/DCM_SUPPLIER_4/DCM_SUPPLIER_5/DCM_SUPPLIER_6/DCM_SUPPLIER_7/DCM_SUPPLIER\_8/DCM_SUPPLIER_9/DCM_UDS_ON_CAN/DCM_UDS_ON_FLEXRAY/DCM_UDS_ON_IP
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 协议类型 (Type of Agreement)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspProtocolEcuAddr
     - 取值范围 (Range)
     - 0 ... 65535
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 用于诊断通信的Ecu源地址 (Source address of ECU for diagnostic communication)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmSendRespPendOnRestart
     - 取值范围 (Range)
     - true/false
     - 默认取值 (Default value)
     - True
   * - 
     - 参数描述 (Parameter Description)
     - 如果设置为TRUE,Dcm将在过渡到引导加载程序或执行ECU复位之前发送NRC 0x78。如果设置为False，在这种情况下不发送0x78 (If set to TRUE, Dcm will send NRC 0x78 before transitioning to the bootloader or performing ECU reset. If set to False, 0x78 will not be sent in this case.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmTimStrP2ServerAdjust
     - 取值范围 (Range)
     - 0 .. 1
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - P2协议调整时间 (P2 Protocol Adjustment Time)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmTimStrP2StarServerAdjust
     - 取值范围 (Range)
     - 0 .. 5
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - P2*协议调整时间 (P2* Protocol Adjustment Time)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDslProtocolRequestQueued
     - 取值范围 (Range)
     - true/false
     - 默认取值 (Default value)
     - False
   * - 
     - 参数描述 (Parameter Description)
     - 允许提供一个额外的缓冲区，以便在此协议下处理另一个请求时最多排队一个请求 (Allow an additional buffer to be provided so that when handling another request under this protocol, at most one request is queued.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDemClientRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 关联DemClient (Associate DemClient)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDslProtocolRxBufferRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 接收buffer关联 (Associate with receive buffer)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDslProtocolSIDTable
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 服务表关联 (Service Table Association)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDslProtocolTxBufferRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 发送buffer关联 (Associate with send buffer)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 




DcmDslConnection
~~~~~~~~~~~~~~~~~~~~~~~

DcmDslMainConnection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/DCM/image17.png
   :alt: DcmDslMainConnection容器配置图 (DcmDslMainConnection Container Configuration Diagram)
   :name: DcmDslMainConnection容器配置图 (DcmDslMainConnection Container Configuration Diagram)
   :align: center


.. centered:: **表 DcmDslMainConnection属性描述 (Table DcmDslMainConnection Property Description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - DcmDslProtocolRxConnectionId
     - 取值范围 (Range)
     - 0 ... 65535
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 使用此连接进行诊断通信的测试器的唯一标识符 (Unique identifier of the tester using this connection for diagnostic communication)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDslProtocolRxTesterSourceAddr
     - 取值范围 (Range)
     - 0 ... 65535
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - TA值 (TAValue)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDslPeriodicTransmissionConRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 周期发送关联 (Periodic Associated Sending)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDslROEConnectionRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - ROE发送关联 (ROE Sending Associated)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDslProtocolComMChannelRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 通信通道关联 (Communication channel association)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 




DcmDslProtocolRx
********************************

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/DCM/image18.png
   :alt: DcmDslProtocolRx容器配置图 (DcmDslProtocolRx Container Configuration Diagram)
   :name: DcmDslProtocolRx容器配置图 (DcmDslProtocolRx Container Configuration Diagram)
   :align: center


.. centered:: **表 DcmDslProtocolRx属性描述 (Table DcmDslProtocolRx Properties Description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - DcmDslProtocolRxAddrType
     - 取值范围 (Range)
     - DCM_FUNCTIONAL_TYPE/DCM_PHYSICAL_TYPE
     - 默认取值 (Default value)
     - DCM_FUNCTIONAL_TYPE
   * - 
     - 参数描述 (Parameter Description)
     - 接收寻址类型 (Addressing Type Reception)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDslProtocolRxPduId
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 接收PDU值 (Receive PDU value)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 不可配置，根据DcmDslProtocolRxPduRef自动生成 (Not configurable, generated automatically based on DcmDslProtocolRxPduRef)
     - 
     - 
   * - DcmDslProtocolRxPduRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 接收PDU关联 (Establish PDU Association)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 




DcmDslProtocolTx
********************************

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/DCM/image19.png
   :alt: DcmDslProtocolTx容器配置图 (DcmDslProtocolTx Container Configuration Diagram)
   :name: DcmDslProtocolTx容器配置图 (DcmDslProtocolTx Container Configuration Diagram)
   :align: center


.. centered:: **表 DcmDslProtocolTx属性描述 (Table DcmDslProtocolTx Property Description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - DcmDslProtocolTxPduId
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 发送PDU值 (Send PDU value)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 不可配置，根据DcmDslProtocolTxPduRef自动生成 (Not configurable, generated automatically based on DcmDslProtocolTxPduRef)
     - 
     - 
   * - DcmDslProtocolTxPduRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 发送PDU关联 (Send PDU Association)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 




DcmDslPeriodicTransmission
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

DcmDslPeriodicConnection
****************************************

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/DCM/image20.png
   :alt: DcmDslPeriodicConnection容器配置图 (Diagram for DcmDslPeriodicConnection Container Configuration)
   :name: DcmDslPeriodicConnection容器配置图 (Diagram for DcmDslPeriodicConnection Container Configuration)
   :align: center


.. centered:: **表 DcmDslPeriodicConnection属性描述 (Table DcmDslPeriodicConnection Property Description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - DcmDslPeriodicTxConfirmationPduId
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 周期发送PDU值 (Periodic PDU value)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 不可配置，根据DcmDslPeriodicTxPduRef自动生成 (Not configurable, generated automatically based on DcmDslPeriodicTxPduRef)
     - 
     - 
   * - DcmDslPeriodicTxPduRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 周期发送PDU关联 (Periodic PDU Association Sending)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 




DcmDslResponseOnEvent
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/DCM/image21.png
   :alt: DcmDslResponseOnEvent容器配置图 (Container Configuration Diagram for DcmDslResponseOnEvent)
   :name: DcmDslResponseOnEvent容器配置图 (Container Configuration Diagram for DcmDslResponseOnEvent)
   :align: center


.. centered:: **表 DcmDslResponseOnEvent属性描述 (Table DcmDslResponseOnEvent attribute description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - DcmDslRoeTxConfirmationPduId
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - ROE发送PDU值 (ROE sends PDU value)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 不可配置，根据DcmDslRoeTxPduRef自动生成 (Not configurable, generated automatically based on DcmDslRoeTxPduRef)
     - 
     - 
   * - DcmDslRoeTxPduRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - ROE发送PDU关联 (ROE sends PDU association)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 




DcmDsp
~~~~~~~~~

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/DCM/image22.png
   :alt: DcmDsp容器配置图 (DcmDsp Container Configuration Diagram)
   :name: DcmDsp容器配置图 (DcmDsp Container Configuration Diagram)
   :align: center


.. centered:: **表 DcmDsp属性描述 (Table DcmDsp Property Description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - DcmDspDDDIDcheckPerSourceDID
     - 取值范围 (Range)
     - True/false
     - 默认取值 (Default value)
     - False
   * - 
     - 参数描述 (Parameter Description)
     - DDDID检查每个源DID使能开关 (DDDI checks each source DID enable switch)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspDataDefaultEndianness
     - 取值范围 (Range)
     - BIG_ENDIAN/LITTLE_ENDIAN/OPAQUE
     - 默认取值 (Default value)
     - BIG_ENDIAN
   * - 
     - 参数描述 (Parameter Description)
     - 大小端 (Little-Endian)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 未使用 (Not used)
     - 
     - 
   * - DcmDspEnableObdMirror
     - 取值范围 (Range)
     - True/false
     - 默认取值 (Default value)
     - False
   * - 
     - 参数描述 (Parameter Description)
     - OBD镜像应答使能开关 (OBDR mirror response enable switch)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspMaxDidToRead
     - 取值范围 (Range)
     - 1 ... 65535
     - 默认取值 (Default value)
     - 1
   * - 
     - 参数描述 (Parameter Description)
     - 一个读取DID请求最大携带的DID个数 (Read DID request maximum number of DIDs carried)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspMaxPeriodicDidToRead
     - 取值范围 (Range)
     - 1 ... 65535
     - 默认取值 (Default value)
     - 1
   * - 
     - 参数描述 (Parameter Description)
     - 最大能读取的周期DID个数 (Maximum number of周期 DID that can be read)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspPowerDownTime
     - 取值范围 (Range)
     - 0 … 255
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - 下电延迟时间 (Power-off delay time)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 未使用 (Not used)
     - 
     - 
   * - DcmResponseToEcuReset
     - 取值范围 (Range)
     - AFTER_RESET/BEFORE_RESET
     - 默认取值 (Default value)
     - AFTER_RESET
   * - DcmDspRoutineCheckRestart
     - 取值范围 (Range)
     - True/false
     - 默认取值 (Default value)
     - False
   * - 
     - 参数描述 (Parameter Description)
     - 是否检查例程重启并报告NRC24 (Is there a check for the routine restart and report NRC24?)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 




DcmDspAuthentication
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/DCM/image23.png
   :alt: DcmDspAuthentication属性描述 (Property Description for DcmDspAuthentication Attribute)
   :name: DcmDspAuthentication属性描述 (Property Description for DcmDspAuthentication Attribute)
   :align: center

.. centered:: **表 DcmDspAuthentication容器配置图 (Table DcmDspAuthentication Container Configuration Diagram)**

.. list-table::
   :widths: 15 15 14 14 14 14 14
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
     - 
     - 
   * - DcmDspAuthenticationDefaultSessionTimeOut
     - 取值范围 (Range)
     - 0 ... INF
     - 
     - 默认取值 (Default value)
     - 
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 定义在没有活动通信的情况下，Dcm转换到未认证状态所需的秒数 (The number of seconds required for Dcm to transition to an unauthenticated state in the absence of active communication)
     - 
     - 
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
     - 
     - 
   * - DcmDspAuthenticationGeneralNRC
     - 取值范围 (Range)
     - 0 ... 255
     - 
     - 默认取值 (Default value)
     - 
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 定义了在证书或内容无效的情况下，应发送替代所有ISO14229-1定义的NRC的NRC (Define an NRC to be sent as a substitute for all ISO14229-1 defined NRCs in case of certificate or content invalidity)
     - 
     - 
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
     - 
     - 
   * - DcmDspAuthenticationRoleSize
     - 取值范围 (Range)
     - 1 … 4
     - 
     - 默认取值 (Default value)
     - 
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 以字节为单位定义证书中角色元素的大小 (Define the size of role elements in the certificate in bytes)
     - 
     - 
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
     - 
     - 
   * - DcmDspAuthenticationWhiteListDIDMaxSize
     - 取值范围 (Range)
     - 1 ... 255
     - 
     - 默认取值 (Default value)
     - 
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 定义证书中白名单元素的最大字节大小 (Define the maximum byte size of whitelist elements in the certificate)
     - 
     - 
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
     - 
     - 
   * - DcmDspAuthenticationWhiteListMemorySelectionMaxSize
     - 取值范围 (Range)
     - 1 ... 255
     - 
     - 默认取值 (Default value)
     - 
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 定义证书中白名单元素的最大字节大小 (Define the maximum byte size of whitelist elements in the certificate)
     - 
     - 
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
     - 
     - 
   * - DcmDspAuthenticationWhiteListRIDMaxSize
     - 取值范围 (Range)
     - 1 ... 255
     - 
     - 默认取值 (Default value)
     - 
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 定义证书中白名单元素的最大字节大小 (Define the maximum byte size of whitelist elements in the certificate)
     - 
     - 
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
     - 
     - 
   * - DcmDspAuthenticationWhiteListServicesMaxSize
     - 取值范围 (Range)
     - 1 ... 255
     - 
     - 默认取值 (Default value)
     - 
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 定义证书中白名单元素的最大字节大小 (Define the maximum byte size of whitelist elements in the certificate)
     - 
     - 
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
     - 
     - 
   * - DcmDspAuthenticationGeneralNRCModeRuleRef
     - 取值范围 (Range)
     - 无
     - 
     - 默认取值 (Default value)
     - 
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 模式规则，定义由于证书或内容无效导致的所有故障是否应发送一般NRC (Pattern rules, define whether all failures due to invalid certificates or content should be sent as general NRCs.)
     - 
     - 
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
     - 
     - 
   * - DcmDspAuthenticationDeauthenticatedRoleRef
     - 取值范围 (Range)
     - 无
     - 
     - 默认取值 (Default value)
     - 
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 对DcmDspAuthenticationRow的引用，该引用定义了其中的角色，该角色被用作去身份验证的角色 (Reference to DcmDspAuthenticationRow, which defines the role used as an unauthentication role.)
     - 
     - 
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
     - 
     - 
   * - DcmDspAuthenticationPersistStateModeRuleRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 
     - 无
     - 
   * - 
     - 参数描述 (Parameter Description)
     - 存储当前状态的模式规则 (Rules for storing the current state)
     - 
     - 
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
     - 
     - 




DcmDspAuthenticationConnection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/DCM/image24.png
   :alt: DcmDspAuthenticationConnection容器配置图 (Container Configuration Diagram for DcmDspAuthenticationConnection)
   :name: DcmDspAuthenticationConnection容器配置图 (Container Configuration Diagram for DcmDspAuthenticationConnection)
   :align: center


.. centered:: **表 DcmDspAuthenticationConnection属性描述 (Table DcmDspAuthenticationConnection Property Description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - DcmDspAuthenticationEcuChallengeLength
     - 取值范围 (Range)
     - 1..65535
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - ECUChallenge的字节长度 (The byte length of ECUChallenge)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspAuthenticationCertificatePublicKeyStoreJobRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 对用于在Csm中存储公钥的CsmJob的引用 (Reference for CsmJob used to store public keys in Csm)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspAuthenticationClientChallengeSignJobRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 引用用于签署客户端挑战的作业 (Reference used for signing client challenge)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspAuthenticationConnectionCertificateRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 对用于在KeyM中存储证书的KeyM证书的引用 (Reference to the KeyM certificate used for storing certificates in KeyM)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspAuthenticationConnectionMainConnectionRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 对使用此身份验证配置的dsl诊断连接的引用 (References for diagnosing connections using this authentication configuration)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspAuthenticationECUCertificateKeyElementRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 对双向身份验证期间用作服务器证书的CryptoKeyElement的引用 (Reference to CryptoKeyElement used as a server certificate during two-factor authentication)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspAuthenticationECUCertificateRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 使用服务器证书引用KeyMCertificate进行双向认证 (Reference KeyMCertificate for mutual authentication using server certificate.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspAuthenticationPublicKeyElementRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 使用证书中的公钥引用证书数据元素 (Reference certificate data elements using the public key in the certificate.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspAuthenticationRandomJobRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 使用服务器证书引用KeyMCertificate进行双向认证 (Reference KeyMCertificate for mutual authentication using server certificate.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspAuthenticationRoleElementRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 使用服务器证书引用KeyMCertificate进行双向认证 (Reference KeyMCertificate for mutual authentication using server certificate.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspAuthenticationTargetIdentificationModeRuleRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 对用于评估目标标识的模式规则的引用 (Reference for pattern rules used to assess target identifiers.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspAuthenticationVerifyProofOfOwnerShipClientJobRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 对CsmJob的引用，用于在Csm中验证所有权证明客户端 (Reference to CsmJob for validation of ownership proof client in Csm.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspAuthenticationWhiteListDIDElementRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 使用证书中数据标识符的白名单引用证书数据元素 (Whitelist references certificate data elements using identifiers from the certificate.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspAuthenticationWhiteListMemorySelectionElementRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 对证书数据元素的引用，其中包含证书中用户定义内存选择的白名单 (Reference to certificate data elements, containing a whitelist of user-defined memory selections in the certificate)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspAuthenticationWhiteListRIDElementRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 使用证书中例程标识符的白名单引用证书数据元素 (White-list reference certificate data elements using identifiers from the certificate routines.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspAuthenticationWhiteListServicesElementRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 使用证书中的白名单引用证书数据元素 (Use whitelist references from certificate data elements in the certificate.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 




DcmDspAuthenticationRow
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/DCM/image25.png
   :alt: DcmDspAuthenticationRow容器配置图 (Container Configuration Diagram for DcmDspAuthenticationRow)
   :name: DcmDspAuthenticationRow容器配置图 (Container Configuration Diagram for DcmDspAuthenticationRow)
   :align: center


.. centered:: **表 DcmDspAuthenticationRow属性描述 (Table DcmDspAuthenticationRow Property Description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - DcmDspAuthenticationRoleBitPosition
     - 取值范围 (Range)
     - 1 ... 65535
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 在身份验证位域中定义代表角色的位 (Define bits in the authentication field that represent roles)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 




DcmDspClearDTC
~~~~~~~~~~~~~~~~~

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/DCM/image26.png
   :alt: DcmDspClearDTC容器配置图 (DcmDspClearDTC Container Configuration Diagram)
   :name: DcmDspClearDTC容器配置图 (DcmDspClearDTC Container Configuration Diagram)
   :align: center


.. centered:: **表 DcmDspClearDTC属性描述 (Table DcmDspClearDTC Property Description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - DcmDspClearDTCCheckFnc
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 打开后默认函数名为 (Default function name after opening is)
   * - 
     - 
     - 
     - 
     - Rte_ClearDTCCheck
   * - 
     - 参数描述 (Parameter Description)
     - 清除DTC检查条件回调接口 (Clear DTC Inspection Condition Callback Interface)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspClearDTCModeRuleRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 关联DcmModeRule (Associate DcmModeRule)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 




DcmDspComControl
~~~~~~~~~~~~~~~~~~~~~

DcmDspComControlAllChannel
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/DCM/image27.png
   :alt: DcmDspComControlAllChannel容器配置图 (Container Configuration Diagram for DcmDspComControlAllChannel)
   :name: DcmDspComControlAllChannel容器配置图 (Container Configuration Diagram for DcmDspComControlAllChannel)
   :align: center


.. centered:: **表 DcmDspComControlAllChannel属性描述 (Table DcmDspComControlAllChannel Property Description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - DcmDspComControlAllChannelUsed
     - 取值范围 (Range)
     - True/false
     - 默认取值 (Default value)
     - True
   * - 
     - 参数描述 (Parameter Description)
     - 所有通信控制使能开关 (All communication control enable switches)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspAllComMChannelRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 关联的通信通道 (Associated communication channel)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 




DcmDspComControlSpecificChannel
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/DCM/image28.png
   :alt: DcmDspComControlSpecificChannel容器配置图 (Container Configuration Diagram for DcmDspComControlSpecificChannel)
   :name: DcmDspComControlSpecificChannel容器配置图 (Container Configuration Diagram for DcmDspComControlSpecificChannel)
   :align: center


.. centered:: **表 DcmDspComControlSpecificChannel属性描述 (Table DcmDspComControlSpecificChannel property description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - DcmDspComControlSpecificChannelUsed
     - 取值范围 (Range)
     - True/false
     - 默认取值 (Default value)
     - True
   * - 
     - 参数描述 (Parameter Description)
     - 特殊通信控制使能开关 (Special Communication Control Enable Switch)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspSpecificComMChannelRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 关联的通信通道 (Associated communication channel)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspSubnetNumber
     - 取值范围 (Range)
     - 1..14
     - 默认取值 (Default value)
     - 1
   * - 
     - 参数描述 (Parameter Description)
     - 子网号 (Subnet ID)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 




DcmDspComControlSubNode
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/DCM/image29.png
   :alt: DcmDspComControlSubNode容器配置图 (DcmDspComControlSubNode Container Configuration Diagram)
   :name: DcmDspComControlSubNode容器配置图 (DcmDspComControlSubNode Container Configuration Diagram)
   :align: center


.. centered:: **表 DcmDspComControlSubNode属性描述 (Table DcmDspComControlSubNode Property Description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - DcmDspComControlSubNodeUsed
     - 取值范围 (Range)
     - True/false
     - 默认取值 (Default value)
     - True
   * - 
     - 参数描述 (Parameter Description)
     - 子节点控制使能开关 (Child node control enable switch)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspComControlSubNodeComMChannelRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 关联的通信通道 (Associated communication channel)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspComControlSubNodeId
     - 取值范围 (Range)
     - 1..65535
     - 默认取值 (Default value)
     - 1
   * - 
     - 参数描述 (Parameter Description)
     - 子节点号 (Node Number)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 




DcmDspCommonAuthorization 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/DCM/image30.png
   :alt: DcmDspCommonAuthorization 容器配置图 (DcmDspCommonAuthorization Container Configuration Diagram)
   :name: DcmDspCommonAuthorization 容器配置图 (DcmDspCommonAuthorization Container Configuration Diagram)
   :align: center


.. centered:: **表 DcmDspCommonAuthorization 属性描述 (Table DcmDspCommonAuthorization Property Description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - DcmDspCommonAuthorizationModeRuleRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 关联DcmModeRule (Associate DcmModeRule)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspCommonAuthorizationSecurityLevelRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 安全级关联 (Security Level Association)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspCommonAuthorizationSessionRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 会话级关联 (Session-level association)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 




DcmDspControlDTCSetting
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/DCM/image31.png
   :alt: DcmDspControlDTCSetting容器配置图 (Container Configuration Diagram for DcmDspControlDTCSetting)
   :name: DcmDspControlDTCSetting容器配置图 (Container Configuration Diagram for DcmDspControlDTCSetting)
   :align: center


.. centered:: **表 DcmDspControlDTCSetting属性描述 (Property Description of DcmDspControlDTCSetting)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - DcmSupportDTCSettingControlOptionRecord
     - 取值范围 (Range)
     - True/false
     - 默认取值 (Default value)
     - False
   * - 
     - 参数描述 (Parameter Description)
     - DTC控制可选码使能开关 (DTC Control Optional Code Enable Switch)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspControlDTCSettingReEnableModeRuleRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 关联DcmModeRule (Associate DcmModeRule)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 




DcmDspData
~~~~~~~~~~~~~~~~

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/DCM/image32.png
   :alt: DcmDspData容器配置图 (Container Configuration Diagram for DcmDspData)
   :name: DcmDspData容器配置图 (Container Configuration Diagram for DcmDspData)
   :align: center


.. centered:: **表 DcmDspData属性描述 (Table DcmDspData Property Description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - DcmDspDataUsePort
     - 取值范围 (Range)
     - USE_BLOCK_ID/USE_DATA\_ASYNCH_CLIENT_SERVER/USE_DATA_ASYNCH_CLIENT_SERVER_ERROR/USE_DATA_ASYNCH_FNC/USE_DATA_ASYNCH_FNC_ERROR/USE_DATA\_SENDER_RECEIVER/USE_DATA_SENDER\_RECEIVER_AS_SERVICE/USE_DATA_SYNCH_CLIENT_SERVER/USE_DATA_SYNCH_FNC/USE_ECU_SIGNAL
     - 默认取值 (Default value)
     - USE_BLOCK_ID
   * - 
     - 参数描述 (Parameter Description)
     - DTC控制可选码使能开关 (DTC Control Optional Code Enable Switch)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspDataType
     - 取值范围 (Range)
     - BOOLEAN/SINT16/SINT16_N/SINT32/SINT32_N/SINT8/SINT8_N/UINT16/UINT16_N/UINT32/UINT32_N/UINT8/UINT8_DYN/UINT8_N
     - 默认取值 (Default value)
     - BOOLEAN
   * - 
     - 参数描述 (Parameter Description)
     - 数据的类型 (The type of data)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspDataConditionCheckReadFncUsed
     - 取值范围 (Range)
     - True/false
     - 默认取值 (Default value)
     - False
   * - 
     - 参数描述 (Parameter Description)
     - 条件检查接口使能开关 (Condition check interface enable switch)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspDataConditionCheckReadFnc
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - False
   * - 
     - 参数描述 (Parameter Description)
     - 条件检查配置接口 (Condition Check Configuration Interface)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - DcmDspDataConditionCheckReadFncUsed为true且DcmDspDataUsePort不为使用RTE接口的类型 (DcmDspDataConditionCheckReadFncUsed is true and DcmDspDataUsePort is not of the type using RTE interface)
     - 
     - 
   * - DcmDspDataEcuSignal
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - ECU数据获取配置接口 (ECU Data Acquisition Configuration Interface)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - DcmDspDataUsePort为USE_ECU_SIGNAL (DcmDspDataUsePort为USE_ECU_SIGNAL)
     - 
     - 
   * - DcmDspDataEndianness
     - 取值范围 (Range)
     - BIG_ENDIAN/LITTLE_ENDIAN/OPAQUE
     - 默认取值 (Default value)
     - BIG_ENDIAN
   * - 
     - 参数描述 (Parameter Description)
     - 大小端 (Little-Endian)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 未使用 (Not used)
     - 
     - 
   * - DcmDspDataFreezeCurrentStateFnc
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 冻结当前控制的配置接口 (Freeze the current control configuration interface)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - DcmDspDidFreezeCurrentState为true且DcmDspDataUsePort不为使用RTE接口的类型 (DcmDspDidFreezeCurrentState is true and DcmDspDataUsePort is not of the RTE interface type)
     - 
     - 
   * - DcmDspDataGetScalingInfoFnc
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 获取输入数据的配置接口 (Get configuration interface for input data)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - DcmDspDataScalingInfoSize配置且DcmDspDataUsePort不为使用RTE接口的类型 (DcmDspDataScalingInfoSize configured and DcmDspDataUsePort is not of the RTE interface type)
     - 
     - 
   * - DcmDspDataReadDataLengthFnc
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 获取读取数据长度的配置接口 (Get configuration interface for reading data length)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - DcmDspDataType为UINT8_DYN/UINT8_N且DcmDspDataUsePort不为使用RTE接口的类型 (DcmDspDataType is UINT8_DYN/UINT8_N and DcmDspDataUsePort is not a type that uses the RTE interface.)
     - 
     - 
   * - DcmDspDataReadEcuSignal
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 读取ECU数据的配置接口 (Interface for reading ECU data)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - DcmDspDataUsePort为USE_ECU_SIGNAL (DcmDspDataUsePort为USE_ECU_SIGNAL)
     - 
     - 
   * - DcmDspDataReadFnc
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 读取数据的配置接口 (Configuration interface for reading data)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - DcmDspDataUsePort不为使用RTE接口的类型 (DcmDspDataUsePort is not for types using the RTE interface)
     - 
     - 
   * - DcmDspDataResetToDefaultFnc
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 重置为默认控制的配置接口 (Reset configuration interface to default control)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - DcmDspDidResetToDefault为true且DcmDspDataUsePort不为使用RTE接口的类型 (DcmDspDidResetToDefault is true and DcmDspDataUsePort is not of the type using RTE interface)
     - 
     - 
   * - DcmDspDataReturnControlToEcuFnc
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 重置为ECU控制的配置接口 (Reset to ECU-Controlled Configuration Interface)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - DcmDspDataUsePort不为使用RTE接口的类型 (DcmDspDataUsePort is not for types using the RTE interface)
     - 
     - 
   * - DcmDspDataShortTermAdjustmentFnc
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 短暂控制的配置接口 (Temporary control configuration interface)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - DcmDspDidShortTermAdjustment为true且DcmDspDataUsePort不为使用RTE接口的类型 (DcmDspDidShortTermAdjustment为true且DcmDspDataUsePort不为使用RTE接口的类型)
     - 
     - 
   * - DcmDspDataByteSize
     - 取值范围 (Range)
     - 0..65535
     - 默认取值 (Default value)
     - 1
   * - 
     - 参数描述 (Parameter Description)
     - 数据长度，byte为单位 (Length of data, in bytes)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspDataWriteFnc
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 写数据的配置接口 (API for writing data configuration)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - DcmDspDataUsePort不为使用RTE接口的类型 (DcmDspDataUsePort is not for types using the RTE interface)
     - 
     - 
   * - DcmDspDidInfoRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - DID信息关联 (DID Information Association)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspDataBlockIdRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - NV存储块关联 (NV Storage Block Association)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - DcmDspDataUsePort为USE_BLOCK_ID (DcmDspDataUsePort为USE_BLOCK_ID)
     - 
     - 
   * - DcmDspDataInfoRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - data信息关联 (Data Information Association)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 




DcmDspDataInfo
~~~~~~~~~~~~~~~~~~~~~

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/DCM/image33.png
   :alt: DcmDspDataInfo容器配置图 (Container Configuration Diagram for DcmDspDataInfo)
   :name: DcmDspDataInfo容器配置图 (Container Configuration Diagram for DcmDspDataInfo)
   :align: center


.. centered:: **表 DcmDspDataInfo属性描述 (Table DcmDspDataInfo property description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - DcmDspDataScalingInfoSize
     - 取值范围 (Range)
     - 0..4294967295
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - scalinginformation的数据长度 (The length of scalinginformation data)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 




DcmDspDid
~~~~~~~~~~~~~~~~~~

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/DCM/image34.png
   :alt: DcmDspDid容器配置图 (Container Configuration Diagram for DcmDspDid)
   :name: DcmDspDid容器配置图 (Container Configuration Diagram for DcmDspDid)
   :align: center


.. centered:: **表 DcmDspDid属性描述 (Table DcmDspDid Property Description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - DcmDspDidIdentifier
     - 取值范围 (Range)
     - 0..65535
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - DID值 (DID Value)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspDidSize
     - 取值范围 (Range)
     - 0..65535
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - DID的长度 (The length)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspDidUsed
     - 参数描述 (Parameter Description)
     - DID值 (DID Value)
     - 默认取值 (Default value)
     - False
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspDidUsePort
     - 参数描述 (Parameter Description)
     - USE_ATOMIC_BNDM;USE_ATOMIC_NV_DATA\_INTERFACE;
     - 默认取值 (Default value)
     - USE_DATA_ELEMENT_SPECIFIC\_INTERFACES
   * - 
     - 
     - USE_ATOMIC_SENDER\_
     - 
     - 
   * - 
     - 
     - RECEIVER_INTERFACE;
     - 
     - 
   * - 
     - 
     - USE_ATOMIC_SENDER\_
     - 
     - 
   * - 
     - 
     - RECEIVER_INTERFACE\_
     - 
     - 
   * - 
     - 
     - AS_SERVICE;
     - 
     - 
   * - 
     - 
     - USE_DATA_ELEMENT_S
     - 
     - 
   * - 
     - 
     - PECIFIC_INTERFACES
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 为所有数据元素的单个操作或特定于数据元素的操作之间的DID数据元素选择应用程序接口类型 (Select an API type for DID data elements for operations on all data elements or data element-specific operations.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspDidBndMBlockIdRef
     - 参数描述 (Parameter Description)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 依赖关系 (Dependencies)
     - 将此DID与一个BndM块关联 (Associate this DID with a BndM block.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspDidInfoRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - DID信息关联 (DID Information Association)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspDidRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - DID与DID关联 (DID with DID association)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 未使用 (Not used)
     - 
     - 




DcmDspDidSignal
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/DCM/image35.png
   :alt: DcmDspDidSignal容器配置图 (Container Configuration Diagram for DcmDspDidSignal)
   :name: DcmDspDidSignal容器配置图 (Container Configuration Diagram for DcmDspDidSignal)
   :align: center


.. centered:: **表 DcmDspDidSignal属性描述 (Table DcmDspDidSignal attribute description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - DcmDspDidDataPos
     - 取值范围 (Range)
     - 0..65535
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - DID数据偏移位置 (DID Data Offset Position)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspDidDataRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 回调接口等的data配置项关联 (The data configuration item associates with the callback interface etc.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 




DcmDspDidInfo
~~~~~~~~~~~~~~~

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/DCM/image36.png
   :alt: DcmDspDidInfo容器配置图 (Container Configuration Diagram for DcmDspDidInfo)
   :name: DcmDspDidInfo容器配置图 (Container Configuration Diagram for DcmDspDidInfo)
   :align: center


.. centered:: **表 DcmDspDidInfo属性描述 (Table DcmDspDidInfo Property Description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - DcmDspDDDIDMaxElements
     - 取值范围 (Range)
     - 1..255
     - 默认取值 (Default value)
     - 1
   * - 
     - 参数描述 (Parameter Description)
     - 动态DID情况能有个最大源元素 (Dynamic DID status can have a maximum source element.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspDidDynamicallyDefined
     - 取值范围 (Range)
     - True/false
     - 默认取值 (Default value)
     - False
   * - 
     - 参数描述 (Parameter Description)
     - 动态DID使能开关 (Dynamic DID Enable Switch)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 




DcmDspDidControl
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/DCM/image37.png
   :alt: DcmDspDidControl容器配置图 (Container Configuration Diagram for DcmDspDidControl)
   :name: DcmDspDidControl容器配置图 (Container Configuration Diagram for DcmDspDidControl)
   :align: center


.. centered:: **表 DcmDspDidControl属性描述 (Table DcmDspDidControl Property Description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - DcmDspDidControlMask
     - 取值范围 (Range)
     - DCM_CONTROLMASK_EXTERNAL/DCM_CONTROLMASK_INTERNAL/DCM_CONTROLMASK_NO
     - 默认取值 (Default value)
     - DCM_CONTROLMASK_EXTERNAL
   * - 
     - 参数描述 (Parameter Description)
     - 控制掩码的类型 (Types of control mask)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspDidControlMaskSize
     - 取值范围 (Range)
     - 1..4294967294
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 该值以字节为单位定义controlEnableMaskRecord的大小 (This value defines the size of controlEnableMaskRecord in bytes.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspDidControlRole
     - 取值范围 (Range)
     - 0..4294967295
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 每个位代表一个专用的角色。如果位值为1，则授予DIDIOcontrol访问权限。如果位值为0，则不允许对该角色控制DID (Each bit represents a dedicated role. If the bit value is 1, DIDIOcontrol access is granted for that role. If the bit value is 0, control for that role on DID is not allowed.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspDidFreezeCurrentState
     - 取值范围 (Range)
     - True/false
     - 默认取值 (Default value)
     - False
   * - 
     - 参数描述 (Parameter Description)
     - 冻结当前状态使能开关 (Freeze current state enable switch)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspDidResetToDefault
     - 取值范围 (Range)
     - True/false
     - 默认取值 (Default value)
     - False
   * - 
     - 参数描述 (Parameter Description)
     - 重置为默认控制使能开关 (Reset default control enable switch)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspDidShortTermAdjustment
     - 取值范围 (Range)
     - True/false
     - 默认取值 (Default value)
     - False
   * - 
     - 参数描述 (Parameter Description)
     - 短暂调整控制使能开关 (Briefly adjust the control enable switch)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspDidControlModeRuleRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 关联DcmModeRule (Associate DcmModeRule)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspDidControlSecurityLevelRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 控制信息的安全级关联 (Security level association for control information)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspDidControlSessionRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 控制信息的会话级关联 (Session-level association of control information)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspDidControlRoleRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 对DcmDspAuthenticationRow的引用，该引用定义了可以控制该IO的角色 (Reference to DcmDspAuthenticationRow, which defines the roles that can control this IO.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 




DcmDspDidControlEnableMask
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/DCM/image38.png
   :alt: DcmDspDidControlEnableMask容器配置图 (Container Configuration Diagram for DcmDspDidControlEnableMask)
   :name: DcmDspDidControlEnableMask容器配置图 (Container Configuration Diagram for DcmDspDidControlEnableMask)
   :align: center


.. centered:: **表 DcmDspDidControlEnableMask属性描述 (Table DcmDspDidControlEnableMask property description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - DcmDspDidControlMaskBitPosition
     - 取值范围 (Range)
     - 0..31
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - 控制掩码位偏移 (Control mask bit offset)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - value <(DcmDspDidControlMaskSize\* 8)
     - 
     - 




DcmDspDidRead
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/DCM/image39.png
   :alt: DcmDspDidRead容器配置图 (Container Configuration Diagram for DcmDspDidRead)
   :name: DcmDspDidRead容器配置图 (Container Configuration Diagram for DcmDspDidRead)
   :align: center


.. centered:: **表 DcmDspDidRead属性描述 (Table DcmDspDidRead attribute description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - DcmDspDidReadRole
     - 取值范围 (Range)
     - 0..4294967295
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 每个位代表一个专用的角色。如果位值为1，则授予DID读访问权限。如果位值为0，则不允许读取该角色的DID (Each bit represents a dedicated role. If the bit value is 1, it grants read access to the DID. If the bit value is 0, it denies read access to that role's DID.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspDidReadModeRuleRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 关联DcmModeRule (Associate DcmModeRule)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspDidReadSecurityLevelRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 读取数据的DID的安全级关联 (Security level association of DID for reading data)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspDidReadSessionRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 读取数据的DID的会话级关联 (Session-level association of DID for reading data)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspDidReadRoleRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 对DcmDspAuthenticationRow的引用，该引用定义了可以读取此DID的角色 (Reference to DcmDspAuthenticationRow, which defines the roles that can read this DID.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 




DcmDspDidWrite
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/DCM/image40.png
   :alt: DcmDspDidWrite容器配置图 (Container Configuration Diagram for DcmDspDidWrite)
   :name: DcmDspDidWrite容器配置图 (Container Configuration Diagram for DcmDspDidWrite)
   :align: center


.. centered:: **表 DcmDspDidWrite属性描述 (Attribute DcmDspDidWrite describes)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - DcmDspDidWriteRole
     - 取值范围 (Range)
     - 0..4294967295
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 每个位代表一个专用的角色。如果位值为1，则授予DID写访问权限。如果位值为0，则不允许写该角色的DID (Each bit represents a dedicated role. If the bit value is 1, it grants write access to the DID. If the bit value is 0, it denies write access to that role's DID.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspDidWriteModeRuleRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 关联DcmModeRule (Associate DcmModeRule)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspDidWriteSecurityLevelRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 写数据的DID的安全级关联 (The security level associated with DID for writing data)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspDidWriteSessionRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 写数据的DID的会话级关联 (Session-level association of DID for writing data)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspDidWriteRoleRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 对DcmDspAuthenticationRow的引用，该引用定义了可以写此DID的角色 (Reference to DcmDspAuthenticationRow, which defines the roles that can write this DID.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 




DcmDspDidRange
~~~~~~~~~~~~~~~~

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/DCM/image41.png
   :alt: DcmDspDidRange容器配置图 (Container Configuration for DcmDspDidRange)
   :name: DcmDspDidRange容器配置图 (Container Configuration for DcmDspDidRange)
   :align: center


.. centered:: **表 DcmDspDidRange属性描述 (Table DcmDspDidRange Property Description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - DcmDspDidRangeHasGaps
     - 取值范围 (Range)
     - True/false
     - 默认取值 (Default value)
     - False
   * - 
     - 参数描述 (Parameter Description)
     - 范围DID是否存在间隔 (Is there an interval for DID in range?)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspDidRangeIdentifierLowerLimit
     - 取值范围 (Range)
     - 0..65535
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - 范围DID的下限值 (Lower limit value of DID range)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspDidRangeIdentifierUpperLimit
     - 取值范围 (Range)
     - 0..65535
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - 范围DID的上限值 (The upper limit value of DID range)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspDidRangeIsDidAvailableFnc
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - DID在范围内是否支持的配置接口 (Is the configuration interface supported within the range of DID?)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - DcmDspDidRangeUsePort为false才可配，否则默认生成rte标准接口 (DcmDspDidRangeUsePort can only be configured when it is false; otherwise, the rte standard interface will be default generated.)
     - 
     - 
   * - DcmDspDidRangeMaxDataLength
     - 取值范围 (Range)
     - 0..65535
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - 范围DID的最大数据长度 (Maximum data length for range DID)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspDidRangeReadDataLengthFnc
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 范围DID的读取数据长度获取配置接口 (Read Data Length Acquisition Interface for DID in Range)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - DcmDspDidRangeUsePort为false才可配，否则默认生成rte标准接口 (DcmDspDidRangeUsePort can only be configured when it is false; otherwise, the rte standard interface will be default generated.)
     - 
     - 
   * - DcmDspDidRangeReadDidFnc
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 范围DID数据读取配置接口 (DID Data Reading Configuration Interface for Range)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - DcmDspDidRangeUsePort为false才可配，否则默认生成rte标准接口 (DcmDspDidRangeUsePort can only be configured when it is false; otherwise, the rte standard interface will be default generated.)
     - 
     - 
   * - DcmDspDidRangeUsePort
     - 取值范围 (Range)
     - True/false
     - 默认取值 (Default value)
     - False
   * - 
     - 参数描述 (Parameter Description)
     - 范围DID是否使用RTE接口 (Does range DID use RTE interface?)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspDidRangeWriteDidFnc
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 范围DID写数据的配置接口 (Configuration interface for writing data to DID in range D)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - DcmDspDidRangeUsePort为false才可配，否则默认生成rte标准接口 (DcmDspDidRangeUsePort can only be configured when it is false; otherwise, the rte standard interface will be default generated.)
     - 
     - 
   * - DcmDspDidRangeInfoRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 范围DID安全级会话级信息关联 (Range DID Security Level Session-Level Information Association)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 




DcmDspMemory
~~~~~~~~~~~~~~~

DcmDspAddressAndLengthFormatIdentifier
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/DCM/image42.png
   :alt: DcmDspAddressAndLengthFormatIdentifier容器配置图 (Container Configuration for DcmDspAddressAndLengthFormatIdentifier Format Identifier Container Configuration Diagram)
   :name: DcmDspAddressAndLengthFormatIdentifier容器配置图 (Container Configuration for DcmDspAddressAndLengthFormatIdentifier Format Identifier Container Configuration Diagram)
   :align: center


.. centered:: **表 DcmDspAddressAndLengthFormatIdentifier属性描述 (Property Description for DcmDspAddressAndLengthFormatIdentifier)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - DcmDspSupportedAddressAndLengthFormatIdentifier
     - 取值范围 (Range)
     - 0..65535
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - 支持的请求地址格式 (Supported request address formats)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 




DcmDspMemoryIdInfo
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/DCM/image43.png
   :alt: DcmDspMemoryIdInfo容器配置图 (Container Configuration Diagram for DcmDspMemoryIdInfo)
   :name: DcmDspMemoryIdInfo容器配置图 (Container Configuration Diagram for DcmDspMemoryIdInfo)
   :align: center


.. centered:: **表 DcmDspMemoryIdInfo属性描述 (Table DcmDspMemoryIdInfo property description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - DcmDspMemoryIdValue
     - 取值范围 (Range)
     - 0..65535
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - 内存地址ID (Memory Address ID)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 




DcmDspReadMemoryRangeInfo
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/DCM/image44.png
   :alt: DcmDspReadMemoryRangeInfo容器配置图 (Container Configuration Diagram for DcmDspReadMemoryRangeInfo)
   :name: DcmDspReadMemoryRangeInfo容器配置图 (Container Configuration Diagram for DcmDspReadMemoryRangeInfo)
   :align: center


.. centered:: **表 DcmDspReadMemoryRangeInfo属性描述 (Table DcmDspReadMemoryRangeInfo property description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - DcmDspReadMemoryRangeHigh
     - 取值范围 (Range)
     - 0..4294967294
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - 读取内存的最高地址 (Read the highest memory address)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspReadMemoryRangeLow
     - 取值范围 (Range)
     - 0..4294967294
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - 读取内存的最低地址 (Read memory from the lowest address)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspReadMemoryRangeModeRuleRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 关联DcmModeRule (Associate DcmModeRule)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspReadMemoryRangeSecurityLevelRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 内存地址读取的安全级关联 (Security Level Association for Memory Address Read)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspReadMemoryRangeSessionLevelRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 内存地址读取的会话级关联 (Session-level association for memory address reading)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 




DcmDspWriteMemoryRangeInfo
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/DCM/image45.png
   :alt: DcmDspWriteMemoryRangeInfo容器配置图 (Container Configuration Diagram for DcmDspWriteMemoryRangeInfo)
   :name: DcmDspWriteMemoryRangeInfo容器配置图 (Container Configuration Diagram for DcmDspWriteMemoryRangeInfo)
   :align: center


.. centered:: **表 DcmDspWriteMemoryRangeInfo属性描述 (Property Describes DcmDspWriteMemoryRangeInfo)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - DcmDspWriteMemoryRangeHigh
     - 取值范围 (Range)
     - 0..4294967294
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - 写内存的最高地址 (The highest address of memory写作内存的最高地址)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspWriteMemoryRangeLow
     - 取值范围 (Range)
     - 0..4294967294
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - 写内存的最低地址 (Write memory lowest address)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspReadMemoryRangeModeRuleRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 关联DcmModeRule (Associate DcmModeRule)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspWriteMemoryRangeSecurityLevelRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 内存地址写的安全级关联 (Memory address write security level association)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspWriteMemoryRangeSessionLevelRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 内存地址写的会话级关联 (Session-level association written in memory address)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 




DcmDspPeriodicTransmission
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/DCM/image46.png
   :alt: DcmDspPeriodicTransmission容器配置图 (DcmDspPeriodicTransmission Container Configuration Diagram)
   :name: DcmDspPeriodicTransmission容器配置图 (DcmDspPeriodicTransmission Container Configuration Diagram)
   :align: center


.. centered:: **表 DcmDspPeriodicTransmission属性描述 (Table DcmDspPeriodicTransmission Property Description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - DcmDspMaxPeriodicDidScheduler
     - 取值范围 (Range)
     - 1..255
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 定义可并发调度的periodicdataidentifier的最大数量 (Define the maximum number of concurrent schedulable periodicdataidentifier.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspPeriodicTransmissionFastRate
     - 取值范围 (Range)
     - 1E-4..0.255
     - 默认取值 (Default value)
     - 0.001
   * - 
     - 参数描述 (Parameter Description)
     - 周期DID快速发送周期 (Period DID Quick Period Send)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspPeriodicTransmissionMaxPeriodicFastTransmissions
     - 取值范围 (Range)
     - 1..65535
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 定义用于快速传输的周期性连接的最大数目。 (Define the maximum number of periodic connections for fast transfer.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspPeriodicTransmissionMaxPeriodicMediumTransmissions
     - 取值范围 (Range)
     - 1E-4..0.255
     - 默认取值 (Default value)
     - 0.001
   * - 
     - 参数描述 (Parameter Description)
     - 周期DID中速发送周期 (Period DID Medium Speed Send Period)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspPeriodicTransmissionSlowRate
     - 取值范围 (Range)
     - 1E-4..0.255
     - 默认取值 (Default value)
     - 0.001
   * - 
     - 参数描述 (Parameter Description)
     - 周期DID慢速发送周期 (Period DID slow speed period)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspPeriodicTransmissionMediumRate
     - 取值范围 (Range)
     - 1E-4..1
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 传输速率 (Transmission rate)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspPeriodicTransmissionSchedulerType
     - 取值范围 (Range)
     - SCHEDULER_TYPE1;SCHEDULER_TYPE2
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 根据ISO14229-1:2018按周期标识符定义所使用的调度器类型 (According to ISO14229-1:2018, the scheduler type defined by periodic identifier)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspPeriodicTransmissionSlowRate
     - 取值范围 (Range)
     - 1E-4..1
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 传输速率 (Transmission rate)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 




DcmDspPid
~~~~~~~~~~~

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/DCM/image47.png
   :alt: DcmDspPid容器配置图 (Container Configuration Diagram for DcmDspPid)
   :name: DcmDspPid容器配置图 (Container Configuration Diagram for DcmDspPid)
   :align: center


.. centered:: **表 DcmDspPid属性描述 (Table DcmDspPid Property Description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - DcmDspPidIdentifier
     - 取值范围 (Range)
     - 0..255
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - PID值 (PID value)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspPidService
     - 取值范围 (Range)
     - DCM_SERVICE_01/DCM_SERVICE_01_02/DCM_SERVICE_02
     - 默认取值 (Default value)
     - DCM_SERVICE_01
   * - 
     - 参数描述 (Parameter Description)
     - 能使用PID的服务 (Services that can use PID:)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 根据此选项决定子容器中Service01和Service02是否可配。 (Decide whether Service01 and Service02 in the sub-container are configurable based on this option.)
     - 
     - 
   * - DcmDspPidSize
     - 取值范围 (Range)
     - 0..255
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - PID数据长度 (PID Data Length)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspPidUsed
     - 取值范围 (Range)
     - True/false
     - 默认取值 (Default value)
     - False
   * - 
     - 参数描述 (Parameter Description)
     - PID使能开关 (PID Enable Switch)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 




DcmDspPidData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/DCM/image48.png
   :alt: DcmDspPidData容器配置图 (Container Configuration Diagram for DcmDspPidData)
   :name: DcmDspPidData容器配置图 (Container Configuration Diagram for DcmDspPidData)
   :align: center


.. centered:: **表 DcmDspPidData属性描述 (Table DcmDspPidData Property Description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - DcmDspPidDataPos
     - 取值范围 (Range)
     - 0..2040
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - PID数据偏移值 (PID Data Offset Value)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspPidDataSize
     - 取值范围 (Range)
     - 0..2040
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - PID数据长度 (PID Data Length)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 




DcmDspPidDataSupportInfo
~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/DCM/image49.png
   :alt: DcmDspPidDataSupportInfo容器配置图 (Container Configuration Diagram for DcmDspPidDataSupportInfo)
   :name: DcmDspPidDataSupportInfo容器配置图 (Container Configuration Diagram for DcmDspPidDataSupportInfo)
   :align: center


.. centered:: **表 DcmDspPidDataSupportInfo属性描述 (Table DcmDspPidDataSupportInfo Property Description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - DcmDspPidDataSupportInfoBit
     - 取值范围 (Range)
     - 0..255
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - 支持信息位 (Support information bits)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspPidDataSupportInfoRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 支持信息关联 (Support information association)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 




DcmDspPidService01
~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/DCM/image50.png
   :alt: DcmDspPidService01容器配置图 (Container Configuration Diagram for DcmDspPidService01)
   :name: DcmDspPidService01容器配置图 (Container Configuration Diagram for DcmDspPidService01)
   :align: center


.. centered:: **表 DcmDspPidService01属性描述 (Table DcmDspPidService01 Property Description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - DcmDspPidDataUsePort
     - 取值范围 (Range)
     - USE_DATA_SENDER_RECEIVER/USE_DATA_SYNCH\_CLIENT_SERVER/USE_DATA_SYNCH_FNC
     - 默认取值 (Default value)
     - USE\_DATA_SENDER_RECEIVER
   * - 
     - 参数描述 (Parameter Description)
     - 接口类型 (Interface Type)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspPidDataEndianness
     - 取值范围 (Range)
     - BIG_ENDIAN/LITTLE_ENDIAN/OPAQUE
     - 默认取值 (Default value)
     - BIG_ENDIAN
   * - 
     - 参数描述 (Parameter Description)
     - 大小端 (Little-Endian)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 未使用 (Not used)
     - 
     - 
   * - DcmDspPidDataReadFnc
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 获取数据的配置接口 (API for configuring data retrieval)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - DcmDspPidDataUsePort为USE_DATA_SYNCH_FNC (DcmDspPidDataUsePort for USE_DATA_SYNCH_FNC)
     - 
     - 
   * - DcmDspPidDataType
     - 取值范围 (Range)
     - BOOLEAN/SINT16/SINT16_N/SINT32/SINT32_N/SINT8/SINT8_N/UINT16/UINT16_N/UINT32/UINT32_N/UINT8/UINT8_N
     - 默认取值 (Default value)
     - BOOLEAN
   * - 
     - 参数描述 (Parameter Description)
     - 数据类型 (Data types)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 未使用 (Not used)
     - 
     - 




DcmDspPidService02
~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/DCM/image51.png
   :alt: DcmDspPidService02容器配置图 (DcmDspPidService02 Container Configuration Diagram)
   :name: DcmDspPidService02容器配置图 (DcmDspPidService02 Container Configuration Diagram)
   :align: center


.. centered:: **表 DcmDspPidService02属性描述 (Table DcmDspPidService02 Attribute Description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - DcmDspPidDataDemRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - PID数据获取与DEM的接口进行关联 (PID data acquisition interface associated with DEM)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 




DcmDspPidSupportInfo
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/DCM/image52.png
   :alt: DcmDspPidSupportInfo容器配置图 (Container Configuration Diagram for DcmDspPidSupportInfo)
   :name: DcmDspPidSupportInfo容器配置图 (Container Configuration Diagram for DcmDspPidSupportInfo)
   :align: center


.. centered:: **表 DcmDspPidSupportInfo属性描述 (Table DcmDspPidSupportInfo Property Description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - DcmDspPidSupportInfoLen
     - 取值范围 (Range)
     - 0..255
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - 支持信息的长度 (The length of support information)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspPidSupportInfoPos
     - 取值范围 (Range)
     - 0..255
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - 支持信息的偏移量 (Support for offset of information)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 




DcmDspRequestControl
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/DCM/image53.png
   :alt: DcmDspRequestControl容器配置图 (Container Configuration Diagram for DcmDspRequestControl)
   :name: DcmDspRequestControl容器配置图 (Container Configuration Diagram for DcmDspRequestControl)
   :align: center


.. centered:: **表 DcmDspRequestControl属性描述 (Table DcmDspRequestControl Property Description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - DcmDspRequestControlInBufferSize
     - 取值范围 (Range)
     - 0..255
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - 输入数据长度 (Input data length)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspRequestControlInfoByte
     - 取值范围 (Range)
     - 0..255
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - 制造商特定的值报告给测试人员，用于记录标识符0xE000到OxE1FF (Manufacturer-specific values are reported to testers for recording identifiers 0xE000 to OxE1FF)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspRequestControlOutBufferSize
     - 取值范围 (Range)
     - 0..255
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - 输出数据长度 (Length of Output Data)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspRequestControlTestId
     - 取值范围 (Range)
     - 0..255
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - TID值 (TID Value)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 




DcmDspRequestFileTransfer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/DCM/image54.png
   :alt: DcmDspRequestFileTransfer容器配置图 (Container Configuration Diagram for DcmDspRequestFileTransfer)
   :name: DcmDspRequestFileTransfer容器配置图 (Container Configuration Diagram for DcmDspRequestFileTransfer)
   :align: center


.. centered:: **表 DcmDspRequestFileTransfer属性描述 (Table DcmDspRequestFileTransfer property description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - DcmRequestFileTransferFileSizeParameterLength
     - 取值范围 (Range)
     - 0..255
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - 文件传输文件大小参数的长度 (The length of the parameter for file size in file transfer)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmRequestFileTransferLengthFormatIdentifier
     - 取值范围 (Range)
     - 0..255
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - 文件传输长度格式定义 (File transfer length format definition)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmRequestFileTransferMaxFileAndDirName
     - 取值范围 (Range)
     - 1..65535
     - 默认取值 (Default value)
     - 1
   * - 
     - 参数描述 (Parameter Description)
     - 定义用于RequestFileTransfer的RTE接口允许的FileAndDirName参数的最大大小 (Define the maximum size allowed for the FileAndDirName parameter in the RTE interface used for RequestFileTransfer.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmRequestFileTransferUsePort
     - 取值范围 (Range)
     - True/false
     - 默认取值 (Default value)
     - False
   * - 
     - 参数描述 (Parameter Description)
     - 定义C/S或C函数调用是否用于RequestFileTransfer处理 (Determine whether C/S or C functions are used for RequestFileTransfer processing)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 




DcmDspRoe
~~~~~~~~~~~~~~~~

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/DCM/image55.png
   :alt: DcmDspRoe容器配置图 (DcmDspRoe Container Configuration Diagram)
   :name: DcmDspRoe容器配置图 (DcmDspRoe Container Configuration Diagram)
   :align: center


特别说明：ROE为86服务，在设置服务后，响应为触发模式，第一次触发时是立即发出响应，之后的响应受DcmDspRoeInterMessageTime控制。在触发ROE响应后，ROE请求会被不同协议的诊断请求抢占掉，当新的诊断请求和ROE响应相同协议时，新的诊断请求会被忽略进而处理ROE响应。建议将ROE服务与普通的诊断进行区分，配置在不同的协议表中。

Special Note: The ROE service (ID 86) operates in trigger mode once the service is set up, issuing an immediate response upon the first trigger. Subsequent responses are controlled by DcmDspRoeInterMessageTime. After triggering the ROE response, requests under different protocols will preempt the ROE request. When a new diagnostic request under the same protocol as the ROE response arrives, it will be ignored in favor of processing the ROE response. It is recommended to differentiate the ROE service from regular diagnostics and configure them in separate protocol tables.

.. centered:: **表 DcmDspRoe属性描述 (Table DcmDspRoe Property Description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - DcmDspRoeInterMessageTime
     - 取值范围 (Range)
     - 0..5
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - 消息间隔时间 (Message interval time)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspRoeStorageBlockIdRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - ROE信息存储NV块的关联 (Information on ROE storage associated with NV block)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 




DcmDspRoeEvent
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/DCM/image56.png
   :alt: DcmDspRoeEvent容器配置图 (Container Configuration Diagram for DcmDspRoeEvent)
   :name: DcmDspRoeEvent容器配置图 (Container Configuration Diagram for DcmDspRoeEvent)
   :align: center


.. centered:: **表 DcmDspRoeEvent属性描述 (Table DcmDspRoeEvent Property Description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - DcmDspRoeEventId
     - 取值范围 (Range)
     - 0..254
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - ROE事件ID值 (ROE Event ID Value)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspRoeInitialEventStatus
     - 取值范围 (Range)
     - DCM_ROE_CLEARED/DCM_ROE_STOPPED
     - 默认取值 (Default value)
     - DCM_ROE_CLEARED
   * - 
     - 参数描述 (Parameter Description)
     - ROE事件初始化状态 (ROE Event Initialization Status)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 




DcmDspRoeEventProperties
~~~~~~~~~~~~~~~~~~~~~~~~~

DcmDspRoeOnChangeOfDataIdentifier
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/DCM/image57.png
   :alt: DcmDspRoeOnChangeOfDataIdentifier容器配置图 (DcmDspRoeOnChangeOfDataIdentifier Container Configuration Diagram)
   :name: DcmDspRoeOnChangeOfDataIdentifier容器配置图 (DcmDspRoeOnChangeOfDataIdentifier Container Configuration Diagram)
   :align: center


.. centered:: **表 DcmDspRoeOnChangeOfDataIdentifier属性描述 (Property Description for DcmDspRoeOnChangeOfDataIdentifier)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - DcmDspRoeDidRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - ROE事件DID关联 (ROE Event DID Associated)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 




DcmDspRoeOnDTCStatusChange
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/DCM/image58.png
   :alt: DcmDspRoeOnDTCStatusChange容器配置图 (Container Configuration for DcmDspRoeOnDtcStatusChange)
   :name: DcmDspRoeOnDTCStatusChange容器配置图 (Container Configuration for DcmDspRoeOnDtcStatusChange)
   :align: center


.. centered:: **表 DcmDspRoeOnDTCStatusChange属性描述 (Property Description for DcmDspRoeOnDTCStatusChange)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - DcmDspRoeDTCStatusMask
     - 取值范围 (Range)
     - 0..255
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - ROE事件DTC状态掩码 (ROE Event DTC Status Mask)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 




DcmDspRoeEventWindowTime
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/DCM/image59.png
   :alt: DcmDspRoeEventWindowTime容器配置图 (Container Configuration Diagram for DcmDspRoeEventWindowTime)
   :name: DcmDspRoeEventWindowTime容器配置图 (Container Configuration Diagram for DcmDspRoeEventWindowTime)
   :align: center


.. centered:: **表 DcmDspRoeEventWindowTime属性描述 (Table DcmDspRoeEventWindowTime Property Description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     -
     - 
     - 
   * - DcmDspRoeEventWindowTime
     - 取值范围 (Range)
     - DCM_ROE_EVENT_WINDOW_CURRENT_AND\_FOLLOWING_CYCLE/DCM_ROE_EVENT_WINDOW_CURRENT_CYCLE/DCM_ROE_EVENT_WINDOW_INFINITE
     - 默认取值 (Default value)
     - DCM_ROE_EVENT_WINDOW_INFINITE
   * - 
     - 参数描述 (Parameter Description)
     - ROE事件窗口时间 (ROE Event Window Time)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 




DcmDspRoutine
~~~~~~~~~~~~~~~~~~

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/DCM/image60.png
   :alt: DcmDspRoutine容器配置图 (DcmDspRoutine Container Configuration Diagram)
   :name: DcmDspRoutine容器配置图 (DcmDspRoutine Container Configuration Diagram)
   :align: center


.. centered:: **表 DcmDspRoutine属性描述 (Table DcmDspRoutine Property Description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - DcmDspRoutineIdentifier
     - 取值范围 (Range)
     - 0..65535
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - RID值 (RID Value)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspRoutineInfoByte
     - 取值范围 (Range)
     - 0..255
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - 特殊值报告给测试设备的 (Special values reported to the test equipment)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 未使用 (Not used)
     - 
     - 
   * - DcmDspRoutineUsePort
     - 取值范围 (Range)
     - True/false
     - 默认取值 (Default value)
     - False
   * - 
     - 参数描述 (Parameter Description)
     - 使用RTE接口的使能开关 (Enable switch for using RTE interface)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspRoutineUsed
     - 取值范围 (Range)
     - True/false
     - 默认取值 (Default value)
     - False
   * - 
     - 参数描述 (Parameter Description)
     - RID使能开关 (RID Enable Switch)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspCommonAuthorizationRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - RID的安全级会话级关联 (The security level session-level association of RID.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 




DcmDspRequestRoutineResults
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/DCM/image61.png
   :alt: DcmDspRequestRoutineResults容器配置图 (Container Configuration Diagram for DcmDspRequestRoutineResults)
   :name: DcmDspRequestRoutineResults容器配置图 (Container Configuration Diagram for DcmDspRequestRoutineResults)
   :align: center


.. centered:: **表 DcmDspRequestRoutineResults属性描述 (Table DcmDspRequestRoutineResults attribute description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - DcmDspRequestRoutineResultsConfirmationEnabled
     - 取值范围 (Range)
     - True/false
     - 默认取值 (Default value)
     - false
   * - 
     - 参数描述 (Parameter Description)
     - 允许启用/禁用确认功能，以指示传输对RequestRoutineResults请求的响应 (Allow enabling/disabling the confirmation feature to indicate transmission of the response for the RequestRoutineResults request.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspRequestRoutineResultsConfirmationFnc
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 发送者需要传输确认时调用的c函数(BSW模块)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspRequestRoutineResultsFnc
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - RID请求结果的配置接口 (API for configuring RID request results)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - DcmDspRoutineUsePort为false才可配置，否则自动生成rte标准接口 (DcmDspRoutineUsePort is configurable only when false; otherwise, the rte standard interface is automatically generated.)
     - 
     - 
   * - DcmDspRequestRoutineResultsRole
     - 取值范围 (Range)
     - 0..4294967295
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 每个位代表一个专用的角色。如果位值为1，则授予带有子函数requestResults的RoutineControl访问权限。如果位值为0，则不允许该例程用于该角色 (Each bit represents a dedicated role. If the bit value is 1, it grants access to RoutineControl with the sub-function requestResults for that role. If the bit value is 0, the routine is not allowed for that role.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspRoutineInterfaceArgumentIntegrity
     - 取值范围 (Range)
     - True/false
     - 默认取值 (Default value)
     - false
   * - 
     - 参数描述 (Parameter Description)
     - 定义ClientServerOperation的值。diagArgIntegrity用于创建这个例程的C/S接口 (Define the value of ClientServerOperation. diagArgIntegrity is used to create the C/S interface for this subroutine.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspRequestRoutineResultsCommonAuthorizationRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - RID请求结果的安全级会话级关联 (The security level of RID request results is session-level association.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspRequestRoutineResultsRoleRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 引用DcmDspAuthenticationRow，它定义了一个角色，在这个角色中可以读取这个例程的结果 (引用DcmDspAuthenticationRow, it defines a role in which the result of this procedure can be read.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 




DcmDspRequestRoutineResultsIn
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

DcmDspRequestRoutineResultsInSignal
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/DCM/image62.png
   :alt: DcmDspRequestRoutineResultsInSignal容器配置图 (Container Configuration Diagram for DcmDspRequestRoutineResultsInSignal)
   :name: DcmDspRequestRoutineResultsInSignal容器配置图 (Container Configuration Diagram for DcmDspRequestRoutineResultsInSignal)
   :align: center


.. centered:: **表 DcmDspRequestRoutineResultsInSignal属性描述 (Property Describes the table DcmDspRequestRoutineResultsInSignal)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - DcmDspRoutineSignalLength
     - 取值范围 (Range)
     - 0..65535
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - 输入的信号长度 (Length of the input signal)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspRoutineSignalEndianness
     - 取值范围 (Range)
     - BIG_ENDIAN/LITTLE_ENDIAN/OPAQUE
     - 默认取值 (Default value)
     - BIG_ENDIAN
   * - 
     - 参数描述 (Parameter Description)
     - 大小端 (Little-Endian)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 未使用 (Not used)
     - 
     - 
   * - DcmDspRoutineSignalType
     - 取值范围 (Range)
     - BOOLEAN/SINT16/SINT16_N/SINT32/SINT32_N/SINT8/SINT8_N/UINT16/UINT16_N/UINT32/UINT32_N/UINT8/VARIABLE_LENGTH/UINT8_N
     - 默认取值 (Default value)
     - BOOLEAN
   * - 
     - 参数描述 (Parameter Description)
     - 数据类型 (Data types)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 未使用 (Not used)
     - 
     - 
   * - DcmDspRoutineSignalPos
     - 取值范围 (Range)
     - 0..65535
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - 信号偏移量 (Signal offset)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 未使用 (Not used)
     - 
     - 




DcmDspRequestRoutineResultsOuts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

DcmDspRequestRoutineResultsOutSignal
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/DCM/image63.png
   :alt: DcmDspRequestRoutineResultsOutSignal容器配置图 (Container Configuration Diagram for DcmDspRequestRoutineResultsOutSignal)
   :name: DcmDspRequestRoutineResultsOutSignal容器配置图 (Container Configuration Diagram for DcmDspRequestRoutineResultsOutSignal)
   :align: center


.. centered:: **表 DcmDspRequestRoutineResultsOutSignal属性描述 (Property Description for DcmDspRequestRoutineResultsOutSignal)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - DcmDspRoutineSignalLength
     - 取值范围 (Range)
     - 0..65535
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - 输出的信号长度 (The length of the output signal)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspRoutineSignalEndianness
     - 取值范围 (Range)
     - BIG_ENDIAN/LITTLE_ENDIAN/OPAQUE
     - 默认取值 (Default value)
     - BIG_ENDIAN
   * - 
     - 参数描述 (Parameter Description)
     - 大小端 (Little-Endian)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 未使用 (Not used)
     - 
     - 
   * - DcmDspRoutineSignalType
     - 取值范围 (Range)
     - BOOLEAN/SINT16/SINT16_N/SINT32/SINT32_N/SINT8/SINT8_N/UINT16/UINT16_N/UINT32/UINT32_N/UINT8/VARIABLE_LENGTH/UINT8_N
     - 默认取值 (Default value)
     - BOOLEAN
   * - 
     - 参数描述 (Parameter Description)
     - 数据类型 (Data types)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 未使用 (Not used)
     - 
     - 
   * - DcmDspRoutineSignalPos
     - 取值范围 (Range)
     - 0..65535
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - 信号偏移量 (Signal offset)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 未使用 (Not used)
     - 
     - 




DcmDspStartRoutine
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/DCM/image64.png
   :alt: DcmDspStartRoutine容器配置图 (DcmDspStartRoutine Container Configuration Diagram)
   :name: DcmDspStartRoutine容器配置图 (DcmDspStartRoutine Container Configuration Diagram)
   :align: center


.. centered:: **表 DcmDspStartRoutine属性描述 (Table DcmDspStartRoutine Property Description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - DcmDspRoutineInterfaceArgumentIntegrity
     - 取值范围 (Range)
     - True/false
     - 默认取值 (Default value)
     - false
   * - 
     - 参数描述 (Parameter Description)
     - 定义ClientServerOperation的值，diagArgIntegrity用于创建这个例程的C/S接口 (Define the value of ClientServerOperation as diagArgIntegrity for creating the C/S interface of this routine.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspStartRoutineConfirmationEnabled
     - 取值范围 (Range)
     - True/false
     - 默认取值 (Default value)
     - false
   * - 
     - 参数描述 (Parameter Description)
     - 允许启用/禁用确认功能，以指示对StartRoutine请求的响应的传输 (Allow enabling/disabling the confirmation feature to indicate the transmission of responses to StartRoutine requests.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspStartRoutineConfirmationFnc
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 发送者需要传输确认时调用的c函数(BSW模块)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspStartRoutineFnc
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - RID启动例程的配置接口 (The configuration interface for the RID Boot Routine)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - DcmDspRoutineUsePort为false才可配置，否则自动生成rte标准接口 (DcmDspRoutineUsePort is configurable only when false; otherwise, the rte standard interface is automatically generated.)
     - 
     - 
   * - DcmDspStartRoutineRole
     - 取值范围 (Range)
     - 0..4294967295
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 每个位代表一个专用的角色。如果位值为1，则授予带有子函数startRoutine的RoutineControl访问权限。如果位值为0，则不允许该例程用于该角色 (Each bit represents a dedicated role. If the bit value is 1, it grants access to the RoutineControl with the sub-function startRoutine for that role. If the bit value is 0, the routine is not allowed for that role.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspStartRoutineCommonAuthorizationRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - RID启动例程的安全级会话级关联 (The security level session-level association of the RID Startup Routine)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - DcmDspRoutineUsePort为false才可配置，否则自动生成rte标准接口 (DcmDspRoutineUsePort is configurable only when false; otherwise, the rte standard interface is automatically generated.)
     - 
     - 
   * - DcmDspStartRoutineRoleRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 关联DcmDspAuthenticationRow (Associate DcmDspAuthenticationRow)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 




DcmDspStartRoutineIn
~~~~~~~~~~~~~~~~~~~~~~~

DcmDspStartRoutineInSignal
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/DCM/image65.png
   :alt: DcmDspStartRoutineInSignal容器配置图 (Container Configuration Diagram for DcmDspStartRoutineInSignal)
   :name: DcmDspStartRoutineInSignal容器配置图 (Container Configuration Diagram for DcmDspStartRoutineInSignal)
   :align: center


.. centered:: **表 DcmDspStartRoutineInSignal属性描述 (Attribute describes the DcmDspStartRoutineInSignal table.)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - DcmDspRoutineParameterSize
     - 取值范围 (Range)
     - 0..65535
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - 输入的信号长度 (Length of the input signal)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspRoutineSignalEndianness
     - 取值范围 (Range)
     - BIG_ENDIAN/LITTLE_ENDIAN/OPAQUE
     - 默认取值 (Default value)
     - BIG_ENDIAN
   * - 
     - 参数描述 (Parameter Description)
     - 大小端 (Little-Endian)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 未使用 (Not used)
     - 
     - 
   * - DcmDspRoutineSignalType
     - 取值范围 (Range)
     - BOOLEAN/SINT16/SINT16_N/SINT32/SINT32_N/SINT8/SINT8_N/UINT16/UINT16_N/UINT32/UINT32_N/UINT8/VARIABLE_LENGTH/UINT8_N
     - 默认取值 (Default value)
     - BOOLEAN
   * - 
     - 参数描述 (Parameter Description)
     - 数据类型 (Data types)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 未使用 (Not used)
     - 
     - 
   * - DcmDspRoutineSignalPos
     - 取值范围 (Range)
     - 0..65535
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - 信号偏移量 (Signal offset)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 未使用 (Not used)
     - 
     - 




DcmDspStartRoutineOut
~~~~~~~~~~~~~~~~~~~~~~~~~

DcmDspStartRoutineOutSignal
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/DCM/image66.png
   :alt: DcmDspStartRoutineOutSignal容器配置图 (Container Configuration Diagram for DcmDspStartRoutineOutSignal)
   :name: DcmDspStartRoutineOutSignal容器配置图 (Container Configuration Diagram for DcmDspStartRoutineOutSignal)
   :align: center


.. centered:: **表 DcmDspStartRoutineOutSignal属性描述 (Property Description for DcmDspStartRoutineOutSignal)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - DcmDspRoutineParameterSize
     - 取值范围 (Range)
     - 0..65535
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - 输出的信号长度 (The length of the output signal)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspRoutineSignalEndianness
     - 取值范围 (Range)
     - BIG_ENDIAN/LITTLE_ENDIAN/OPAQUE
     - 默认取值 (Default value)
     - BIG_ENDIAN
   * - 
     - 参数描述 (Parameter Description)
     - 大小端 (Little-Endian)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 未使用 (Not used)
     - 
     - 
   * - DcmDspRoutineSignalType
     - 取值范围 (Range)
     - BOOLEAN/SINT16/SINT16_N/SINT32/SINT32_N/SINT8/SINT8_N/UINT16/UINT16_N/UINT32/UINT32_N/UINT8/VARIABLE_LENGTH/UINT8_N
     - 默认取值 (Default value)
     - BOOLEAN
   * - 
     - 参数描述 (Parameter Description)
     - 数据类型 (Data types)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 未使用 (Not used)
     - 
     - 
   * - DcmDspRoutineSignalPos
     - 取值范围 (Range)
     - 0..65535
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - 信号偏移量 (Signal offset)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 未使用 (Not used)
     - 
     - 




DcmDspStopRoutine
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/DCM/image67.png
   :alt: DcmDspStopRoutine容器配置图 (Container Configuration Diagram for DcmDspStopRoutine)
   :name: DcmDspStopRoutine容器配置图 (Container Configuration Diagram for DcmDspStopRoutine)
   :align: center


.. centered:: **表 DcmDspStopRoutine属性描述 (Property Description for DcmDspStopRoutine)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - DcmDspRoutineInterfaceArgumentIntegrity
     - 取值范围 (Range)
     - True/false
     - 默认取值 (Default value)
     - false
   * - 
     - 参数描述 (Parameter Description)
     - 定义ClientServerOperation的值，diagArgIntegrity用于创建这个例程的C/S接口 (Define the value of ClientServerOperation as diagArgIntegrity for creating the C/S interface of this routine.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspStopRoutineConfirmationEnabled
     - 取值范围 (Range)
     - True/false
     - 默认取值 (Default value)
     - false
   * - 
     - 参数描述 (Parameter Description)
     - 允许启用/禁用确认功能，以指示对StopRoutine请求的响应的传输 (Enable/disable the confirmation feature to indicate the transmission of a response to the StopRoutine request.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspStopRoutineConfirmationFnc
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 发送者需要传输确认时调用的c函数(BSW模块)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspStopRoutineFnc
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - RID停止例程的配置接口 (Interface to configure the stop routine of RID)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - DcmDspRoutineUsePort为false才可配置，否则自动生成rte标准接口 (DcmDspRoutineUsePort is configurable only when false; otherwise, the rte standard interface is automatically generated.)
     - 
     - 
   * - DcmDspStopRoutineRole
     - 取值范围 (Range)
     - 0..4294967295
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 每个位代表一个专用的角色。如果位值为1，则授予带有子函数stopRoutine的RoutineControl访问权限。如果位值为0，则不允许该例程用于该角色 (Each bit represents a dedicated role. If the bit value is 1, it grants access to the RoutineControl with the sub-function stopRoutine for that role. If the bit value is 0, the routine is not allowed for that role.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspStopRoutineCommonAuthorizationRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 关联DcmDspCommonAuthorization (RelateDcmDspCommonAuthorization)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - DcmDspRoutineUsePort为false才可配置，否则自动生成rte标准接口 (DcmDspRoutineUsePort is configurable only when false; otherwise, the rte standard interface is automatically generated.)
     - 
     - 
   * - DcmDspStopRoutineRoleRef
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - RID停止例程的安全级会话级关联 (The safety-level session-level association of the RID Stop Routine.)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 




DcmDspStopRoutineIn
~~~~~~~~~~~~~~~~~~~~~~~~~~~

DcmDspStopRoutineInSignal
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/DCM/image68.png
   :alt: DcmDspStopRoutineInSignal容器配置图 (Container Configuration Diagram for DcmDspStopRoutineInSignal)
   :name: DcmDspStopRoutineInSignal容器配置图 (Container Configuration Diagram for DcmDspStopRoutineInSignal)
   :align: center


.. centered:: **表 DcmDspStopRoutineInSignal属性描述 (Property Description for DcmDspStopRoutineInSignal)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - DcmDspRoutineParameterSize
     - 取值范围 (Range)
     - 0..65535
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - 输入的信号长度 (Length of the input signal)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspRoutineSignalEndianness
     - 取值范围 (Range)
     - BIG_ENDIAN/LITTLE_ENDIAN/OPAQUE
     - 默认取值 (Default value)
     - BIG_ENDIAN
   * - 
     - 参数描述 (Parameter Description)
     - 大小端 (Little-Endian)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 未使用 (Not used)
     - 
     - 
   * - DcmDspRoutineSignalType
     - 取值范围 (Range)
     - BOOLEAN/SINT16/SINT16_N/SINT32/SINT32_N/SINT8/SINT8_N/UINT16/UINT16_N/UINT32/UINT32_N/UINT8/VARIABLE_LENGTH/UINT8_N
     - 默认取值 (Default value)
     - BOOLEAN
   * - 
     - 参数描述 (Parameter Description)
     - 数据类型 (Data types)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 未使用 (Not used)
     - 
     - 
   * - DcmDspRoutineSignalPos
     - 取值范围 (Range)
     - 0..65535
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - 信号偏移量 (Signal offset)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 未使用 (Not used)
     - 
     - 




DcmDspStopRoutineOut
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

DcmDspStopRoutineOutSignal
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/DCM/image69.png
   :alt: DcmDspStopRoutineOutSignal容器配置图 (DcmDspStopRoutineOutSignal Container Configuration Diagram)
   :name: DcmDspStopRoutineOutSignal容器配置图 (DcmDspStopRoutineOutSignal Container Configuration Diagram)
   :align: center


.. centered:: **表 DcmDspStopRoutineOutSignal属性描述 (Attribute description for DcmDspStopRoutineOutSignal)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - DcmDspRoutineParameterSize
     - 取值范围 (Range)
     - 0..65535
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - 输出的信号长度 (The length of the output signal)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspRoutineSignalEndianness
     - 取值范围 (Range)
     - BIG_ENDIAN/LITTLE_ENDIAN/OPAQUE
     - 默认取值 (Default value)
     - BIG_ENDIAN
   * - 
     - 参数描述 (Parameter Description)
     - 大小端 (Little-Endian)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 未使用 (Not used)
     - 
     - 
   * - DcmDspRoutineSignalType
     - 取值范围 (Range)
     - BOOLEAN/SINT16/SINT16_N/SINT32/SINT32_N/SINT8/SINT8_N/UINT16/UINT16_N/UINT32/UINT32_N/UINT8/VARIABLE_LENGTH/UINT8_N
     - 默认取值 (Default value)
     - BOOLEAN
   * - 
     - 参数描述 (Parameter Description)
     - 数据类型 (Data types)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 未使用 (Not used)
     - 
     - 
   * - DcmDspRoutineSignalPos
     - 取值范围 (Range)
     - 0..65535
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - 信号偏移量 (Signal offset)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 未使用 (Not used)
     - 
     - 




DcmDspSecurity
~~~~~~~~~~~~~~~~~~~~~

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/DCM/image70.png
   :alt: DcmDspSecurity容器配置图 (DcmDspSecurity Container Configuration Diagram)
   :name: DcmDspSecurity容器配置图 (DcmDspSecurity Container Configuration Diagram)
   :align: center


.. centered:: **表 DcmDspSecurity属性描述 (Table DcmDspSecurity Property Description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - DcmDspSecurityMaxAttemptCounterReadoutTime
     - 取值范围 (Range)
     - 0..65535
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - 读取安全级错误计数的最大尝试周期 (Maximum attempt period for reading security level error count)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - DcmTaskTime的倍数，填写的是执行的最多周期 (Multiple of DcmTaskTime, fill in the maximum number of cycles executed.)
     - 
     - 




DcmDspSecurityRow
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/DCM/image71.png
   :alt: DcmDspSecurityRow容器配置图 (Container Configuration Diagram for DcmDspSecurityRow)
   :name: DcmDspSecurityRow容器配置图 (Container Configuration Diagram for DcmDspSecurityRow)
   :align: center


.. centered:: **表 DcmDspSecurityRow属性描述 (Table DcmDspSecurityRow Property Description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - DcmDspSecurityADRSize
     - 取值范围 (Range)
     - 1..4294967295
     - 默认取值 (Default value)
     - 1
   * - 
     - 参数描述 (Parameter Description)
     - 用于获取种子的输入参数长度 (Length of input parameters for getting seeds)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspSecurityAttemptCounterEnabled
     - 取值范围 (Range)
     - True/false
     - 默认取值 (Default value)
     - False
   * - 
     - 参数描述 (Parameter Description)
     - 使能启用安全尝试计数器的外部处理 (Enable External Handling with Security Attempt Counter Enabled)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspSecurityCompareKeyFnc
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 用于比较key的配置接口 (Interface for configuring comparison keys)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - DcmDspSecurityUsePort为USE_ASYNCH_FNC (DcmDspSecurityUsePort为USE_ASYNCH_FNC)
     - 
     - 
   * - DcmDspSecurityDelayTime
     - 取值范围 (Range)
     - 0..65535
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - 比较密钥失败延时时间 (Failed key comparison delay time)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspSecurityDelayTimeOnBoot
     - 取值范围 (Range)
     - 0..65535
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - 从boot跳转后的延时时间 (Delay time after jumping from boot)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 未使用 (Not used)
     - 
     - 
   * - DcmDspSecurityGetAttemptCounterFnc
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 用于获取失败计数的配置接口 (API for retrieving failure count configuration)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - DcmDspSecurityUsePort为USE_ASYNCH_FNC且DcmDspSecurityAttemptCounterEnabled为true (DcmDspSecurityUsePort is USE_ASYNCH_FNC and DcmDspSecurityAttemptCounterEnabled is true)
     - 
     - 
   * - DcmDspSecurityGetSeedFnc
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 用于获取种子的配置接口 (API for obtaining seed configuration)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - DcmDspSecurityUsePort为USE_ASYNCH_FNC (DcmDspSecurityUsePort为USE_ASYNCH_FNC)
     - 
     - 
   * - DcmDspSecurityKeySize
     - 取值范围 (Range)
     - 1..4294967295
     - 默认取值 (Default value)
     - 1
   * - 
     - 参数描述 (Parameter Description)
     - 密钥长度 (Key length)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspSecurityLevel
     - 取值范围 (Range)
     - 1..63
     - 默认取值 (Default value)
     - 1
   * - 
     - 参数描述 (Parameter Description)
     - 安全级的级别 (The level of security level)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - SecurityLevel=(SecurityAccessType(requestSeed)+ 1) / 2
     - 
     - 
   * - DcmDspSecurityNumAttDelay
     - 取值范围 (Range)
     - 1..255
     - 默认取值 (Default value)
     - 1
   * - 
     - 参数描述 (Parameter Description)
     - 用于延时的错误计数门限值 (Threshold value for error counting for delay compensation)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspSecuritySeedSize
     - 取值范围 (Range)
     - 1..4294967295
     - 默认取值 (Default value)
     - 1
   * - 
     - 参数描述 (Parameter Description)
     - 种子长度 (Seed length)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspSecuritySetAttemptCounterFnc
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 用于存储错误计数的配置接口 (Configuration interface for storing error counts)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - DcmDspSecurityUsePort为USE_ASYNCH_FNC且DcmDspSecurityAttemptCounterEnabled为true (DcmDspSecurityUsePort is USE_ASYNCH_FNC and DcmDspSecurityAttemptCounterEnabled is true)
     - 
     - 
   * - DcmDspSecurityUsePort
     - 取值范围 (Range)
     - USE_ASYNCH_CLIENT_SERVER;
     - 默认取值 (Default value)
     - 无
   * - 
     - 
     - USE_ASYNCH_FNC
     - 
     - 
   * - 
     - 参数描述 (Parameter Description)
     - 定义用于安全访问的接口类型 (Define interface types for secure access)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 




DcmDspSession
~~~~~~~~~~~~~~~~~~

DcmDspSessionRow
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/DCM/image72.png
   :alt: DcmDspSessionRow容器配置图 (Container Configuration Diagram for DcmDspSessionRow)
   :name: DcmDspSessionRow容器配置图 (Container Configuration Diagram for DcmDspSessionRow)
   :align: center


.. centered:: **表 DcmDspSessionRow属性描述 (Table DcmDspSessionRow Property Description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - DcmDspSessionForBoot
     - 取值范围 (Range)
     - DCM_NO_BOOT/DCM_OEM_BOOT/DCM_OEM_BOOT_RESPAPP/DCM_SYS_BOOT/DCM_SYS_BOOT_RESPAPP
     - 默认取值 (Default value)
     - DCM_NO_BOOT
   * - 
     - 参数描述 (Parameter Description)
     - 会话级是否进行复位的类型 (Whether the type of reset is performed at the session level)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspSessionLevel
     - 取值范围 (Range)
     - 1..126
     - 默认取值 (Default value)
     - 1
   * - 
     - 参数描述 (Parameter Description)
     - 会话级的级别 (Session-level)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspSessionP2ServerMax
     - 取值范围 (Range)
     - 0..1
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - P2时间 (P2 Time)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspSessionP2StarServerMax
     - 取值范围 (Range)
     - 0..1
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - P2*时间 (P2*Time)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 




DcmDspVehInfo
~~~~~~~~~~~~~~~~

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/DCM/image73.png
   :alt: DcmDspVehInfo容器配置图 (Container Configuration Diagram for DcmDspVehInfo)
   :name: DcmDspVehInfo容器配置图 (Container Configuration Diagram for DcmDspVehInfo)
   :align: center


.. centered:: **表 DcmDspVehInfo属性描述 (Table DcmDspVehInfo property description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - DcmDspVehInfoInfoType
     - 取值范围 (Range)
     - 0..255
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - InfoType值 (InfoType Value)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspVehInfoNODIProvResp
     - 取值范围 (Range)
     - TRUE/FALSE
     - 默认取值 (Default value)
     - False
   * - 
     - 参数描述 (Parameter Description)
     - true：只允许有一个子容器 (true: Only one sub-container is allowed.)
     - 
     - 
   * - 
     - 
     - false或不存在：不受影响 (false or non-existent: unaffected)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 




DcmDspVehInfoData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/DCM/image74.png
   :alt: DcmDspVehInfoData容器配置图 (Container Configuration Diagram for DcmDspVehInfoData)
   :name: DcmDspVehInfoData容器配置图 (Container Configuration Diagram for DcmDspVehInfoData)
   :align: center


.. centered:: **表 DcmDspVehInfoData属性描述 (Table DcmDspVehInfoData Property Description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - DcmDspVehInfoDataOrder
     - 取值范围 (Range)
     - 0..255
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - 顺序值 (Sequence Value)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 未使用 (Not used)
     - 
     - 
   * - DcmDspVehInfoDataReadFnc
     - 取值范围 (Range)
     - 无
     - 默认取值 (Default value)
     - 无
   * - 
     - 参数描述 (Parameter Description)
     - 数据获取的配置接口 (Data acquisition configuration interface)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspVehInfoDataSize
     - 取值范围 (Range)
     - 0..255
     - 默认取值 (Default value)
     - 1
   * - 
     - 参数描述 (Parameter Description)
     - 数据长度 (Data length)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmDspVehInfoDataUsePort
     - 取值范围 (Range)
     - True/false
     - 默认取值 (Default value)
     - False
   * - 
     - 参数描述 (Parameter Description)
     - 是否使用port接口 (Is port interface used?)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 未使用 (Not used)
     - 
     - 




DcmPageBufferCfg
================================

.. figure:: ../../_static/参考手册(Module_Reference_Manual)/DCM/image75.png
   :alt: DcmPageBufferCfg容器配置图 (DcmPageBufferCfg Container Configuration Diagram)
   :name: DcmPageBufferCfg容器配置图 (DcmPageBufferCfg Container Configuration Diagram)
   :align: center


.. centered:: **表 DcmPageBufferCfg属性描述 (Table DcmPageBufferCfg Property Description)**

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - UI名称 (UI Name)
     - 描述 (Description)
     - 
     - 
     - 
   * - DcmPagedBufferEnabled
     - 取值范围 (Range)
     - True/false
     - 默认取值 (Default value)
     - False
   * - 
     - 参数描述 (Parameter Description)
     - 分页发送功能使能开关 (Page Send Function Enable Switch)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - 无
     - 
     - 
   * - DcmPagedBufferTimeout
     - 取值范围 (Range)
     - 0..1
     - 默认取值 (Default value)
     - 0
   * - 
     - 参数描述 (Parameter Description)
     - 分页发送的超时时间 (Timeout for paginated sending)
     - 
     - 
   * - 
     - 依赖关系 (Dependencies)
     - DcmPagedBufferEnabled为true (DcmPagedBufferEnabled is true)
     - 
     - 




附录1 (Appendix 1)
================================

[1]通过DcmTimerType配置项可以选择四种计时方法。分别为TM、OS、Mainfunction、Callout。TM:使用 TM模块内部标准接口。OS：使用Os system counter。Mainfunction：依赖周期调度，由Dcm内部计时。不同计时方法的对应接口由配置工具生成在Dcm_Callout.c 中，其中Callout是由客户自定义的计时类型，可以参照生成示例中TM/OS/Mainfunction的实现，结合项目工程情况修改接口自行实现计时功能。

Four timing methods, namely TM, OS, Mainfunction, and Callout, can be selected via the DcmTimerType configuration item: TM uses the standard internal interface of the TM module, OS uses the OS system counter, Mainfunction relies on periodic scheduling with timing handled internally by DCM, the corresponding interfaces for different timing methods are generated by the configuration tool in Dcm_Callout.c, and Callout is a customer-defined timing type for which you can refer to the implementation of TM/OS/Mainfunction in the generated example, modify the interfaces according to project engineering conditions, and implement the timing function independently.

附录2 (Appendix 2)
================================

.. centered:: **表 工程预编译宏定义表(Table 1 Engineering Precompiled Macro Definition Table)**

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - 宏定义名称 (Macro definition name)
     - 功能 (Functions)
     - 范围（使用方法） (Scope (Usage))
     - 默认值 (Default value)
   * - DCM_DELAY_COMM_INACTIVE=1
     - 任意的诊断请求结束后Dcm会维diagnosticstate 为active5秒钟，计时达到之后才会调用ComM_DCM_InactiveDiagnostic接口去通知ComM模块diagnosticstate 为inactive。 (After any diagnostic request, Dcm will maintain the diagnosticstate as active for 5 seconds. The ComM_DCM_InactiveDiagnostic interface will be called to notify the ComM module of diagnosticstate being inactive only after the timer reaches the count.)
     - 定义：使能未定义：不使能 (Definition: Enable Undefined: Disable)
     - 未定义 (Undefined)
