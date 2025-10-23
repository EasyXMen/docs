===================
Xcp
===================



文档信息 Document Information
==============================================================================

版本历史 Version History
---------------------------------------------------------------------------------------------------------------------------------------

.. list-table::
   :widths: 10 10 10 10 20
   :header-rows: 1

   * - 日期(Date)
     - 作者(Author)
     - 版本(Version)
     - 状态(Status)
     - 说明(Description)

   * - 2024/11/19
     - qinchun.yang
     - V0.1
     - 发布(Release)
     - 首次发布(First release)

   * - 2025/04/04
     - qinchun.yang
     - V1.0
     - 发布(Release)
     - 正式发布(Official release)


参考文档 References
---------------------------------------------------------------------------------

.. list-table::
   :widths: 10 10 30 10
   :header-rows: 1

   * - 编号(Number)
     - 分类(Classification)
     - 标题(Title)
     - 版本(Version)
   * - 1
     - Autosar
     - AUTOSAR_CP_SRS_XCP.pdf
     - R23-11
   * - 2
     - Autosar
     - AUTOSAR_CP_SWS_XCP.pdf
     - R23-11 
   * - 3
     - ASAM
     - ASAM_XCP_Part1-Overview.pdf
     - V1-1-0 
   * - 4
     - ASAM
     - ASAM_XCP_Part2-Protocol-Layer-Specification.pdf
     - V1-1-0           
   * - 5
     - ASAM
     - ASAM_XCP_Part3-Transport-Layer-Specification_XCPonCAN.pdf
     - V1-1-0 
   * - 6
     - ASAM
     - ASAM_XCP_Part3-Transport-Layer-Specification_XCPonEthernet_TCP_IP.pdf
     - V1-1-0 
   * - 7
     - ASAM
     - ASAM_XCP_Part4-Interface-Specification.pdf
     - V1-1-0    
   * - 8
     - ASAM
     - ASAM_XCP_Part5-Example-Communication-Sequences.pdf
     - V1-1-0         

术语与简写 Terms and Abbreviations
==================================================================


术语 Terms
------------------------------------------------------------
None


简写 Abbreviations
------------------------------------------------------------

.. list-table::
   :widths: 10 20 30
   :header-rows: 1


   * - 简写(Abbreviation)
     - 全称(Full name)
     - 解释(Explanation)

   * - A2L
     - File Extension for an ASAM 2MC Language File
     - 上位机和ECU之间的通讯文件

   * - ASAM
     - Association for Standardisation of Automation and Measuring Systems
     - 一个推动汽车开发和测试中工具链的标准化的组织(主要成员是OEM)

   * - MCS
     - measurement and calibration system 
     - 测量&标定系统，如CanApe/INCA等标定上位机     

   * - DAQ
     - Data AcQuisition, Data AcQuisition Packet 
     - 数据采集包（一般指ECU把观测量通过DAQ上传到上位机）       

   * - STIM
     - Data Stimulation 
     - 数据采集包（一般指上位机把观测量通过STIM下发到ECU）  

   * - CTO
     - Packet for transferring generic control commands 
     - XCP通信数据包，用于传输命令以及响应 

   * - DTO
     - Packet for transferring synchronous data 
     - XCP通信数据包，用于传输DAQ以及STIM数据 
     
简介 Introduction
================================================

Xcp全称Universal Measurement and Calibration Protocol（统一测量和标定协议），“X”代表支持多总线传输层。该协议由ASAM组织制定并标准化。Xcp协议继承于Ccp协议，在Ccp协议的基础上扩展了对多总线通信协议（如Ethernet、FlexRay等）的支持。Xcp协议主要功能是为Ecu标定提供一个标准协议，用户以主从的方式去访问Ecu内变量，以实现测量和标定的功能。

Xcp is short for Universal Measurement and Calibration Protocol, "X" means it supports multibus transfer layer. This protocol is formulated and standardized by ASAM. Xcp protocol inherits Ccp protocol. On basis of Ccp protocol, Xcp protocol extends the support of multibus communication protocol (such as Ethernet, FlexRay). Xcp protocol is a standard protocol that is mainly used for Ecu calibration. The user can have access to variable of Ecu by means of master/slave, to realize the measurement and calibration function.

本文档主要介绍了XCP协议层的特性、API、配置。

This document introduces the characteristics, API and configuration of XCP protocol layer.

Xcp协议层是一种独立于硬件的协议，可以移植到几乎任何硬件上。但是由于不同的MCU性能、资源不一样，不能保证Xcp协议栈能在所有的MCU上都能完全正常运行；

Xcp protocol layer is a protocol that is independent of the hardware and can be transplanted to almost all hardware. However, Xcp protocol stack may fail to run normally on all MCU due to different MCU performance and resources;

Xcp在AUTOSAR架构中与其他模块的交互关系如下：

The interactive relationship between Xcp and other modules in AUTOSAR architecture is as follows:

.. figure:: ../../../_static/参考手册/Xcp/Xcp协议栈上下交互图.png
   :alt: Xcp协议栈交互图 (Xcp Protocol Stack Interaction Diagram)
   :name: fig_Xcparch
   :align: center

   Xcp协议栈交互图 (Xcp Protocol Stack Interaction Diagram)

功能描述 Functional Description
========================================================================

本章节分为两部分进行Xcp协议栈描述，首先会从Xcp的基本概念进行介绍，通信模式、数据包格式等；然后另外一部分会着重对Xcp的一些关键特性进行描述，如DAQ、CAL等；

This section describes the Xcp protocol in two parts. Firstly, it will introduce the basic concept, communication mode and data packet format of Xcp; then, it will describe some key characteristics, such as DAQ and CA, of Xcp;

基本概念介绍 Introduction to Basic Concept
----------------------------------------------------------------------------------------------------------------------------------------------------------------

AUTOSAR XCP功能继承于ASAM XCP，核心功能是用于定义MCS（测量和标定系统）和ECU之间通信的协议，从而以实现通过MCS对ECU上数据进行标定调优的功能。

AUTOSAR XCP, which inherits the function of ASAM XCP, has the core function of defining the communication protocol between MCS (measurement and calibration system) and ECU, to realize calibration and optimization of data on ECU through MCS.

XCP采用Master-Slave（主从式）通信方式，一般来讲标定上位机称为“XCP Master-主节点”，被标定的ECU称为“XCP Slave-从节点”。

The Master-Slave communication mode is adopted in XCP. In general, the calibrating upper computer is called “XCP Master-master node”, while the calibrated ECU is called “XCP Slave-slave node”.

主从节点通信过程中，主节点用于发送协议命令，从节点对命令进行解析并返回对应的响应，通信内容称为XCP数据包（XCP PACKET，包含CTO和DTO），通信示意图如下：

During communication of master-slave node, the master node sends the protocol command, and the slave node analyzes the command and returns the corresponding response. The communication content is called XCP data packet (XCP PACKET, containing CTO and DTO). The diagram of communication is as follows:

.. figure:: ../../../_static/参考手册/Xcp/XCP主从通信示意图.png
   :alt: XCP主从通信示意图 (XCP Diagram of Master-Slave Communication)
   :name: fig_XcpMS
   :align: center

   XCP主从通信示意图 (Diagram of XCP Master-Slave Communication)

XCP状态机 XCP state machine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

XCP协议栈从上电开始，包含三种状态：

     - 恢复状态（RESUME）：ECU上电后，会先检查非易失性存储区是否保存了需要恢复的DAQ配置列表，如果存在的话，上电后会立即切换到恢复状态（RESUME），ECU会自动上传被恢复的DAQ列表，在此状态下，ECU会忽略除CONNECT命令之外的其他命令，如果收到CONNECT命令后，将会切换为连接状态；

     - 断开状态（DISCONNECT）：如果不存在需要恢复的DAQ列表，那么XCP会自动切换到断开状态（DISCONNECT），在此状态下，ECU同样会忽略除CONNECT命令之外的其他命令，直到收到CONNECT命令，进入到连接状态（CONNECT）；

     - 连接状态（CONNECT）：在连接状态下，ECU可以处理所有的命令操作，直到收到DISCONNECT命令，进入到断开状态。

XCP protocol stack, which starts from power-on, contains three states:

     - Resume state (RESUME): After power-on, ECU will firstly check whether NV storage area stores the to-be-resumed DAQ configuration list; if yes, it will switch to resume state (RESUME) immediately, and ECU will be automatically uploaded to the resumed DAQ list immediately after power-on; in this state, ECU will ignore other commands other than CONNECT command; it will be switched to connection state upon receiving the CONNECT command;

     - Disconnection state (DISCONNECT): When there’s no to-be-resumed DAQ list, XCP will be switched to disconnection state (DISCONNECT) automatically; in this state, ECU will also ignore other commands other than CONNECT command, until CONNECT command is received and it will enter the connection state (CONNECT);

     - Connection state (CONNECT): In connection state, ECU can handle all commands, until DISCONNECT command is received and it will enter disconnection state.

XCP状态机如下所示：

XCP state machine is as shown below:

.. figure:: ../../../_static/参考手册/Xcp/Xcp状态机.png
   :alt: Xcp状态机 (Xcp state machine)
   :name: fig_XcpState
   :align: center

   Xcp状态机 (Xcp state machine)


XCP通信方式 XCP communication mode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

主从节点通信方式又细分为三种模式，分别是标准模式，块传输和交替模式，其主要特征如下：


     - 标准模式（ Standard Communication Model）：一问一答式交互，主节点发送一条命令，从节点就回复一次；
     - 块传输模式（Master/Slave Block Transfer Model）：块传输又分为Master Block Transfer（主块传输模式：主节点连续发生多次命令，从节点只回复一次）和Slave Block Transfer（从块传输模式：主节点发送一次，从节点回复多次）；
     - 交替模式（Interleaved Communication Model）：主节点在不同时间内联系发送多条不同报文，从节点也在相应的时间分别进行回复.

The master-slave node communication mode is divided into three models: Standard communication model, block transfer and interleaved communication model, of which the main characteristics are as follows:

     - Standard communication model: Question-and-answer interaction, the slave node will have one reply after master node sends one command;
     - Master/slave block transfer model: The block transfer model is divided into Master Block Transfer (master block transfer model: The slave node has one reply after the master node sends multiple commands continuously) and Slave Block Transfer (slave block transfer model: The slave node has repeated replies after the master node sends one command);
     - Interleaved communication model: The master node sends different messages at different time, and the slave nodes will also reply at the corresponding time.

.. figure:: ../../../_static/参考手册/Xcp/Xcp通信模型.png
   :alt: Xcp通信模型 (Xcp communication model)
   :name: fig_XcpComModel
   :align: center

   Xcp通信模型 (Xcp communication model)

XCP数据包 XCP data packet
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Xcp协议适用于多种传输层，因此Xcp数据包格式具有通用性。

Xcp data packet format is universal, for Xcp protocol applies to multiple transfer layers.

Xcp数据包格式包括Xcp头部（XCP Header）、Xcp协议包（XCP Packet）以及Xcp尾部（XCP Tail），不同的传输层的头部和尾部可能不存在差异。如Xcp报文在以太网中进行传输时，需要在Xcp头部（XCP Header）添加消息长度和计数值；

Xcp data packet format includes Xcp header (XCP Header), Xcp protocol packet (XCP Packet) and Xcp tail (XCP Tail). The head and tail at different layers may be different. When Xcp message is transferred in Ethernet, the message length and count value should be added at the Xcp header (XCP Header);

.. figure:: ../../../_static/参考手册/Xcp/XcpFrame.png
   :alt: XcpFrame
   :name: fig_XcpFrame
   :align: center

   Xcp数据包 (Xcp data packet)

其中Xcp协议包（XCP Packet）分为CTO（command transfer object）和DTO（data transfer object）两种。CTO用于主从之间传输控制命令，主要包括发送命令（CMD）/响应应 答（RES）/错误帧应答（RES）/事件（EV）/服务请求处理（SERV），而DTO用来传 输同步数据包，包括数据采集（DAQ）和数据激励（STIM）。

In which, Xcp protocol packet (XCP Packet) is divided into CTO (command transfer object) and DTO (data transfer object). CTO is used for transferring control commands between master and slave, including sending command (CMD)/response (RES)/wrong frame response (RES)/Event (EV)/Service request handling, while DTO is used for transferring synchronous data packet, including data acquisition (DAQ) and data stimulation (STIM).

下表列举了不同传输方向下各个PID所属数据包类型以及对应的功能描述：

The types of PID data packets at different transfer directions and corresponding function descriptions are listed in table below:

.. list-table::
   :widths: 10 10 5 10 
   :header-rows: 1

   * - 数据传输方向(Data transfer direction)
     - PID取值范围(PID value range)
     - 类型(Type)
     - 功能描述(Functional Description)

   * - Master->Slave 
     - 0x00~0xBF
     - DTO
     - STIM激励数据(STIM stimulation data)

   * - Master->Slave 
     - 0xC0~0xFF
     - CTO
     - CMD命令，如0xFF代表CONNECT命令(CMD command, for example, 0xFF represents CONNECT command)   
  
   * - Slave->Master 
     - 0x00~0xFB
     - DTO
     - DAQ数据包，观测数据(DAQ data packet, observation data)     

   * - Slave->Master 
     - 0xFC
     - CTO
     - SERV，下位机请求上位机相应服务(SERV, the lower computer requests for corresponding service of upper computer) 
   
   * - Slave->Master 
     - 0xFD
     - CTO
     - EV，下位机报告异步事件(EV, lower computer reports the asynchronous event)    

   * - Slave->Master 
     - 0xFE
     - CTO
     - ERR，下位机负响应(ERR, lower computer has negative response)    

   * - Slave->Master 
     - 0xFF
     - CTO
     - RES，下位机正响应(RES, lower computer has positive response) 

特性 Features
------------------------------------------------------------------------

数据观测（Measurement） Data observation (Measurement)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Xcp数据测量主要有两种方式：

There are two methods of Xcp data measurement:

1.异步测量（Polling模式）

1.Asynchronous measurement (Polling model)

2.同步测量（DAQ模式）

2.Synchronous measurement (DAQ model)

Polling测量模式  Polling measurement model
*****************************************************************************************************************************************

Polling模式测量是指上位机通过发送指定的地址来从ECU内部获取数据，并通过下位机的响应将数据发送给上位机，如此循环实现数据周期测量。

Polling measurement means the upper computer acquires data from ECU by sending the designated address, and sends data to the upper computer through the response of lower computer, to realize periodic measurement of data through such cycles.

.. figure:: ../../../_static/参考手册/Xcp/Polling测量.png
   :alt: Polling测量 (Polling measurement)
   :name: fig_XcpPolling
   :align: center

   Polling测量 (Polling measurement)

在Polling模式测量过程中，一般使用的命令如下：

During Polling measurement, the general commands used are as follows:

.. list-table::
   :widths: 10 5 15 5 
   :header-rows: 1

   * - 命令（CMD）(Command (CMD))
     - PID
     - 功能描述(Functional Description)
     - 是否支持(Support or not)

   * - UPLOAD  
     - 0xF5
     - 上传SET_MTA地址中的数据(Upload data in SET_MTA address)
     - 是(Yes)

   * - SHORT_UPLOAD  
     - 0xF4
     - 上传命令中指定地址中的数据(Upload data in the designated address of command)
     - 是(Yes)

DAQ测量模式 DAQ measurement model
*****************************************************************************************************************************************

DAQ测量功能主要是为了上传观测量，DAQ由ODT组成，ODT由ODT Entry组成。从通讯角度ODT就是每一帧数据（如一帧CAN报文），而ODT Entry代表一帧数据中（如CAN报文中）的字节内容。在实际应用中，一个周期内一般采集非常多的数据（超过一帧），那么就需要把多个ODT组合起来，这种组合在XCP中称为DAQ List。

DAQ measurement function is to upload the observed quantity. DAQ consists of ODT, while ODT consists of ODT Entry. From the perspective of communication, ODT refers to the data per frame (such as CAN message of one frame), while ODT Entry represents the byte content in one frame data (such as CAN message). Multiple ODT needs to be combined in actual application, for many data (over 1 frame) will be collected in one period, and such combination is called DAQ List in XCP.

DAQ模式测量中一般会在ECU内部定义多个周期性事件（XcpEvent），如1ms/2ms/5ms/10ms/100ms等，上位机通过DAQ命令把需要测量的变量配置成DAQ表与对应的事件进行关联，按照命令中的参数配置组包并根据设定的周期进行上传。

In general, multiple periodic events (XcpEvent) will be defined in ECU during DAQ measurement, such as 1ms/2ms/5ms/10ms/100ms. The upper computer configures the to-be-measured variables into DAQ table through DAQ command, to have association with the corresponding events; then forms packet according to parameter configuration in command and uploads them according to the set period.

DAQ又分为静态和动态DAQ模式，静态DAQ下DAQ List、Odt以及Odt Entry的个数都是静态配置的，而动态DAQ模式下，DAQ List个数、每个DAQ包含ODT个数以及每个ODT包含的Entry个数都是在运行时由相关命令配置，都可以不同。使得DAQ功能更具有灵活性和高效性。

DAQ is divided into static and dynamic DAQ model; the count of DAQ List, Odt and Odt Entry has static configuration under static DAQ, while the count of DAQ List, count of ODT contained in each DAQ and count of Entry contained in each ODT, is configured by relevant commands under dynamic DAQ model and they can be different. So, DAQ function enjoys high flexibility and effectiveness.

DAQ相关的命令以及实现情况如下：

The DAQ-related commands and realization are as follows:

静态DAQ命令：

Static DAQ command:

.. list-table::
   :widths: 10 5 15 5 
   :header-rows: 1

   * - 命令（CMD）(Command (CMD))
     - PID
     - 功能描述(Functional Description)
     - 是否支持(Support or not)

   * - CLEAR_DAQ_LIST  
     - 0xE3
     - 清除DAQ配置列表（用于静态DAQ）(Clear DAQ configuration list (for static DAQ))
     - 是(Yes)

   * - GET_DAQ_LIST_INFO  
     - 0xD8
     - 获取DAQ List信息（用于静态DAQ）(Acquire DAQ List information (for static DAQ))
     - 是(Yes)

动态DAQ命令：

Dynamic DAQ command:

.. list-table::
   :widths: 10 5 15 5 
   :header-rows: 1

   * - 命令（CMD）(Command (CMD))
     - PID
     - 功能描述(Functional Description)
     - 是否支持(Support or not)

   * - FREE_DAQ    
     - 0xD6
     - 释放动态DAQ配置列表(Release dynamic DAQ configuration list)  
     - 是(Yes)

   * - ALLOC_DAQ   
     - 0xD5
     - 动态分配DAQ列表(Dynamic distribution of DAQ list)
     - 是(Yes)

   * - ALLOC_ODT    
     - 0xD4
     - 分配Odt到指定的DAQ List中(Distribute Odt to the designated DAQ list)
     - 是(Yes)

   * - ALLOC_ODT_ENTRY    
     - 0xD3
     - 分配Odt Entry到指定的Odt中(Distribute Odt Entry to the designated Odt)
     - 是(Yes)

通用DAQ命令：

Universal DAQ command:

.. list-table::
   :widths: 10 5 15 5 
   :header-rows: 1

   * - 命令（CMD）(Command (CMD))
     - PID
     - 功能描述(Functional Description)
     - 是否支持(Support or not)

   * - SET_DAQ_PTR   
     - 0xE2
     - 初始化DAQ列表指针(Initialize DAQ list pointer)
     - 是(Yes)

   * - WRITE_DAQ    
     - 0xE1
     - 向Odt Entry写入数据(Write data to Odt Entry)
     - 是(Yes)
	 
   * - SET_DAQ_LIST_MODE    
     - 0xE0
     - 设置DAQ列表模式(Set DAQ list mode)
     - 是(Yes)

   * - GET_DAQ_LIST_MODE    
     - 0xDF
     - 获取DAQ列表模式(Get DAQ list mode)
     - 是(Yes)

   * - START_STOP_DAQ_LIST   
     - 0xDE
     - 开始/停止/选中对应的DAQ(Start/stop/select the corresponding DAQ)
     - 是(Yes)

   * - START_STOP_SYNCH    
     - 0xDD
     - 开始或停止已准备DAQ列表，或停止所有DAQ列表(Start or stop the prepared DAQ list, or stop all DAQ lists)
     - 是(Yes)

   * - GET_DAQ_CLOCK    
     - 0xDC
     - 获取DAQ采样时间（基于OS Tick）(Get DAQ sampling time (based on OS Tick))
     - 是(Yes)

   * - READ_DAQ   
     - 0xDB
     - 返回通过SET_DAQ_PTR指定的Odt Entry信息(Return the Odt Entry information that is designated by SET_DAQ_PTR)
     - 是(Yes)
	 	 
   * - GET_DAQ_PROCESSOR_INFO   
     - 0xDA
     - 获取一些DAQ的通用信息（如最大DAQ个数）(Get some universal information of DAQ (such as max. count of DAQ))
     - 是(Yes)
	 	 
   * - GET_DAQ_RESOLUTION_INFO   
     - 0xD9
     - 获取DAQ基本分辨率信息(Get basic resolution information of DAQ) 
     - 是(Yes)
	 	 
   * - GET_DAQ_EVENT_INFO   
     - 0xD7
     - 获取指定的通道事件（XcpEvent）的基本信息(Get the basic information of designated channel event (XcpEvent))
     - 是(Yes)
	 	 
   * - WRITE_DAQ_MULTIPLE   
     - 0xC7
     - 同时写入多个Odt Entry(Write in several Odt Entry simultaneously)
     - 否(No)	 	 	 

Resume功能 Resume function
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

观测量是通过DAQ进行上传，DAQ的交互需要Master和Slave之间进行若干条命令的交互。Resume功能是在上电过程中不需要经过DAQ命令的交互，即可把配置为Resume模式的DAQ自动上传出来。

Observed quantity is uploaded through DAQ. Interaction of several commands between Master and Slave is required to realize the interaction of DAQ. Interaction through DAQ command is not required by Resume function during power-on, which means, DAQ that is configured as Resume mode can be uploaded automatically.

Resume本质上也是上传DAQ，实现方式也是基于DAQ的命令组。唯一的区别在于START_STOP_DAQ_LIST命令发送时Mode需要设置为02（select），且紧接着需要发送SET_REQUEST（STORE_DAQ_REQ_RESUME）。

The essence of Resume is to upload DAQ through the DAQ-based command group. The only difference is, Mode should be set as 02 (select) while sending the START_STOP_DAQ_LIST command, and then it needs to send SET_REQUEST (STORE_DAQ_REQ_RESUME).

Resume功能关联的命令如下：

The Resume function-associated commands are as follows:

.. list-table::
   :widths: 10 5 15 5 
   :header-rows: 1

   * - 命令（CMD）(Command (CMD))
     - PID
     - 功能描述(Functional Description)
     - 是否支持(Support or not)

   * - SET_REQUEST    
     - 0xF9
     - 发起存储请求，当前仅实现把DAQ数据存储到Nvm中(Initiate storage request, only DAQ data can be stored in Nvm at present)
     - 是(Yes)



在线标定（Calibration）Online calibration (Calibration)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

标定数据本质上看是固定的参数（eg：ECU中一些重要的参数），因此他们会实际被配置到FLASH中。而这些数据在开发阶段同时需要被实时标定，那么因此标准数据也需要具备被修改的属性，即RAM属性。在线标定本质上就是修改存放在RAM中的标定数据。

The calibration data are essentially the fixed parameters (eg: Some important parameters in ECU); so, they will be configured in FLASH. These data need to be calibrated in real time during development; so, the standard data should also have modified attribute, i.e. RAM attribute. The essence of online calibration is to modify the calibration data stored in RAM.

.. figure:: ../../../_static/参考手册/Xcp/Xcp在线标定.png
   :alt: Xcp在线标定 (Xcp online calibration)
   :name: fig_XcpOnlineCal
   :align: center

   Xcp在线标定 (Xcp online calibration)

Xcp协议栈中在线标定相关命令如下：

The online calibration commands in Xcp protocol stack are as follows:

.. list-table::
   :widths: 10 5 15 5 
   :header-rows: 1

   * - 命令（CMD）(Command (CMD))
     - PID
     - 功能描述(Functional Description)
     - 是否支持(Support or not)

   * - SET_MTA   
     - 0xF6
     - 初始化标定变量的基地址(Initialize the base address of calibration variable)
     - 是(Yes)

   * - DOWNLOAD   
     - 0xF0
     - 1、在标准通信模式时，作为下载命令2、在块传输模式时，用于首帧数据下载(1. Used as download command under standard communication model; 2. Used for downloading first frame data under block transfer model)
     - 是(Yes)

   * - DOWNLOAD_NEXT    
     - 0xEF
     - 在块传输模式时，搭配DOWNLOAD命令用于后续帧数据下载(DOWNLOAD command is used for downloading the subsequent frame data under block transfer model)
     - 是(Yes)

   * - SHORT_DOWNLOAD   
     - 0xED
     - 功能同DOWNLOAD，但是只能用于标准通信，且命令自带下载地址(The same function as DOWNLOAD, but it applies to standard communication only and the command comes with download address)
     - 是(Yes)
	 
   * - SHORT_UPLOAD  
     - 0xF4
     - 一般用于数据标定后，通过此命令进行标定数据确认(In general, this command is used for confirming the calibrated data)
     - 是(Yes)
	 	 
   * - MODIFY_BITS   
     - 0xEC
     - 修改MTA指定地址(Modify the designated address of MTA)
     - 是(Yes)
	 	
   * - BUILD_CHECKSUM    
     - 0xF3
     - 内存块数据检查(Check memory block data)
     - 是(Yes)
	 	 	 
   * - DOWNLOAD_MAX    
     - 0xEE
     - 功能同DOWNLOAD，但是只能用于标准通信，但每次下载的字节数固定(The same function as DOWNLOAD, but it applies to standard communication only, and the number of bytes downloaded each time is fixed)
     - 是(Yes)	 	 	  	 

Page页切换 Page switching
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

程序运行时将存放在Flash存储器中的标定参数拷贝到RAM存储器中执行。存储器划分为多个扇区（Sector），每个扇区划分为多个段（Segment），每个段又包含多个页（Page）。

While program is running, the calibration data in Flash memory will be copied in RAM memory for execution. The memory is divided into different sectors, each sector is divided into multiple segments, and each segment contains multiple pages.

Flash中的标定数据就称为参考页（Reference Page），RAM中的标定数据就成为工作页（Working Page），一般情况下它们是一一对应的。

The calibration data in Flash are called reference page. The calibration data in RAM are the working page and have one-to-one correspondence in general.

参考页就是可以被ECU/XCP读取但不能写入的数据，工作页就是可以被ECU读取/写入，可以被XCP读取和写入的数据，他们在逻辑上都是对应了相同的FLASH地址而被赋予了不同的读写属性。

The reference page is the data which can be read by ECU/XCP but can’t be written in; working page is the data which can be read/written by ECU and XCP, they correspond to the same FLASH address logically, but they are given different read/write attributes.

页切换一般使用的命令如下：

The general commands of page switching are as follows:

.. list-table::
   :widths: 10 5 15 5 
   :header-rows: 1

   * - 命令（CMD）(Command (CMD))
     - PID
     - 功能描述(Functional Description)
     - 是否支持(Support or not)

   * - SET_CAL_PAGE   
     - 0xEB
     - 设置标定数据页(Set calibration data page)
     - 是(Yes)

   * - GET_CAL_PAGE   
     - 0xEA
     - 获取标定数据段中激活的标定页(Get the calibration page that is activated in calibration data segment)
     - 是(Yes)

   * - GET_PAG_PROCESSOR_INFO   
     - 0xE9
     - 获取页操作配置的通用信息(Get the universal information in page operation configuration)
     - 否(No)

   * - GET_PAG_PROCESSOR_INFO   
     - 0xE8
     - 获取某个段的配置信息(Get the configuration information of certain segment)
     - 否(No)

   * - GET_PAGE_INFO   
     - 0xE7
     - 获取某个页的属性(Get the attribute of certain page)
     - 是(Yes)

   * - SET_SEGMENT_MODE   
     - 0xE6
     - 设置段冻结模式(Set segment freeze mode)
     - 否(No)

   * - GET_SEGMENT_MODE   
     - 0xE5
     - 获取某个段的模式(Get the mode of certain segment)
     - 否(No)

   * - COPY_CAL_PAGE   
     - 0xE4
     - 页之间数据进行拷贝(Copy the data between pages)
     - 是(Yes)

Flash刷写 Flashing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Flash刷写功能主要是用于把标定得到的数据烧写到Flash中，固化标定到内存（也可以刷写可执行代码）。

Flashing function is used for writing the data, which is acquired through calibration, into the Flash and fixing the calibration data in memory (the executable codes can also have flashing).

Flash内存根据物理地址被划分为多个扇区，每个扇区有独立的编号以及地址的起始地址、内存长度；

The Flash memory is divided into multiple sectors by physical address, each sector has independent number, starting address and memory length;

Flash刷写分为两种模式：功能模式和绝对模式。

Flashing is divided into two modes: Function mode and absolute mode.

绝对模式通过SET_MTA指令设置刷写基地址，上位机再发送刷写相关命令。

The base address of flashing is set through SET_MTA command in absolute mode, then the upper computer sends the flashing command.

功能模式中SET_MTA填写的字节不再作为基地址，而是作为模块序列计数值，解决在大量刷写请求时，刷写服务发送序列错误情况。

The byte filled by SET_MTA under function mode is not regarded as base address, but the count value of block sequence, which avoids the errors of flashing sending sequence when there’s large amount of flashing requests.

通过PROGRAM_CLEAR命令获取刷写基地址，然后将数据刷写至Flash内存中（当前Flash刷写只支持绝对模式）。

Get base address of flashing through PROGRAM_CLEAR command, then flash data in Flash memory (current flashing supports absolute mode only).

Flash刷写一般使用的命令如下：

The general commands of flashing are as follows:

.. list-table::
   :widths: 10 5 15 5 
   :header-rows: 1

   * - 命令（CMD）(Command (CMD))
     - PID
     - 功能描述(Functional Description)
     - 是否支持(Support or not)

   * - PROGRAM_START 
     - 0xD2
     - 指示非易失性存储器编程刷写的开始(Start of NVM programming flashing)
     - 是(Yes)

   * - PROGRAM_CLEAR   
     - 0xD1
     - 重新编程之前清除一部分非易失性存储器数据(Clear part of NVM data prior to reprogramming)
     - 是(Yes)

   * - PROGRAM   
     - 0xD0
     - 进行非易失性存储器的刷写(Flashing of NVM)
     - 是(Yes)

   * - PROGRAM_RESET   
     - 0xCF
     - 指示非易失性内存刷写序列的结束(End of flashing sequence of NVM)
     - 是(Yes)

   * - GET_PGM_PROCESSOR_INFO   
     - 0xCE
     - 获取非易失性存储器刷写的信息(Get the information flashed by NVM)
     - 是(Yes)

   * - GET_SECTOR_INFO   
     - 0xCD
     - 获取特定SECTOR的信息(Get information of specific SECTOR)
     - 是(Yes)

   * - PROGRAM_PREPARE   
     - 0xCC
     - 设置非易失性存储器刷写前的前置条件(Set the preset condition before flashing of NVM)
     - 否(No)

   * - PROGRAM_FORMAT   
     - 0xCB
     - 设置非易失性内存刷写的数据格式(Set the data format flashed by NVM)
     - 是(Yes)

   * - PROGRAM_NEXT   
     - 0xCA
     - 进行连续的非易失性存储器数据块刷写(Perform continuous data flashing of NVM)
     - 是(Yes)

   * - PROGRAM_MAX   
     - 0xC9
     - 将固定长度的数据块刷写到非易失性存储器中(Flashing of fixed length data into NVM)
     - 是(Yes)

   * - PROGRAM_VERIFY   
     - 0xC8
     - 验证非易失性内存刷写后的内容(Verify the contents after flashing of NVM)
     - 否(No)

Seed&Key功能 Seed&Key function
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Seed&Key是Xcp协议栈中一种安全机制，用于对上位机访问权限进行限制；

As a safety mechanism in Xcp protocol stack, Seed&Key is used for limiting the access authority of upper computer;

上位机在使用如测量、标定、Flash刷写等功能时，首先需要进行权限解锁，只有成功解锁后，才能使用此资源；

The authority needs to be unlocked before using the functions of upper computer, such as measurement, calibration and Flash;

.. caution:: 注意 (Caution)

   Seed&Key秘钥算法可根据项目需求进行定制。

   Seed&Key secret key algorithm can be customized based on project demands.

Seed&Key关联命令如下：

Seed&Key commands are as follows:

.. list-table::
   :widths: 10 5 15 5 
   :header-rows: 1

   * - 命令（CMD）(Command (CMD))
     - PID
     - 功能描述(Functional Description)
     - 是否支持(Support or not)

   * - GET_SEED    
     - 0xF8
     - 获取对应资源的种子(Get the seeds of corresponding resources)
     - 是(Yes)

   * - UNLOCK    
     - 0xF7
     - 解锁对应资源(Unlock the corresponding resources)
     - 是(Yes)	  	 

偏差 Deviation
--------------------------------------------------------

不支持的AUTOSAR-XCP功能 Unsupported AUTOSAR-XCP functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 10 20
   :header-rows: 1


   * - SRS
     - SRS概述(SRS overview)

   * - SRS_Xcp_29006
     - AUTOSAR Xcp协议栈需要支持FlexRay总线(AUTOSAR Xcp protocol stack needs to support FlexRay bus)

   * - SRS_Xcp_29021
     - AUTOSAR Xcp协议栈需要能够控制总线通信，对应Xcp_SetTransmissionMode函数的实现(AUTOSAR Xcp protocol stack should control the bus communication and realize the corresponding Xcp_SetTransmissionMode functions)

不支持的ASAM-XCP功能 Unsupported ASAM-XCP functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 10 20
   :header-rows: 1


   * - ASAM Xcp特性(ASAM Xcp characteristics)
     - 描述(Description)

   * - 预定义DAQ功能(Predefine DAQ function)
     - 支持静态&动态DAQ，暂不支持预定义配置DAQ(Support static & dynamic DAQ, predefined DAQ is not supported temporarily) 

   * - Bypassing功能(Bypassing function) 
     - Bypassing功能需借助上位机配套使用，目前暂未实现(Bypassing function needs to be used along with upper computer and it is not realized temporarily)

   * - DAQ优先级(DAQ priority) 
     - 暂不支持ALTERNATING(ALTERNATING not supported temporarily)

   * - DAQ ALTERNATING模式上传(DAQ ALTERNATING mode upload)
     - 暂不支持(Not supported temporarily)     

   * - Page Freezing功能(Page Freezing function) 
     - 暂不支持(Not supported temporarily) 

   * - 多总线标定共存(Coexistence of multibus calibration) 
     - 暂不支持，目前工程仅支持同时存在一种总线（CAN或者ETH）(Not supported temporarily, only one bus (CAN or ETH) is supported simultaneously by the project at present) 



扩展 Extension
----------------------------------------------------

None

集成 Integration
==============================

文件列表 File List
----------------------------------------------------

静态文件 Static Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - 文件(File)
     - 描述(Description)
   
   * - Xcp_GenericType.h
     - Xcp的通用类型的类型定义(Definition of universal type of Xcp)

   * - Xcp_Internal.h
     - Xcp local数据类型定义、local宏定义、local函数声明、local变量声明(Xcp local data type definition, local macro definition, local function declaration, local variable declaration)
	 
   * - Xcp.h
     - 实现Xcp模块全部外部接口的声明，以及配置文件中全局变量的声明(Realize the declaration of all external interfaces of Xcp module, and declaration of global variable in configuration file)

   * - XcpOnCan_Cbk.h
     - Xcp On Can的函数声明(Function declaration of Xcp On Can)

   * - XcpOnEth_Cbk.h
     - Xcp On Eth的函数声明(Function declaration of Xcp On Eth)

   * - Xcp_Cal.c
     - 实现Xcp标定和页切换功能的函数定义(Realize the function definition of Xcp calibration and page switch function)

   * - Xcp_Daq.c
     - 实现Xcp DAQ测量及STIM功能的函数定义(Realize the function definition of Xcp DAQ measurement and STIM function)

   * - Xcp_Pgm.c
     - 实现Xcp Flash刷写功能的函数定义(Realize the function definition of Xcp Flash function)

   * - Xcp_Std.c
     - 实现Xcp std命令的函数定义(Realize the function definition of Xcp std command)

   * - Xcp.c
     - 作为Xcp模块的核心文件，实现Com模块全部对外接口，以及实现Xcp模块功能所必须的local函数，local宏定义，local变量定义(As the core file of Xcp module, it can realize all external interfaces of Com module, as well as all local functions, local macro definitions and local variable definitions which are required for realizing Xcp module function)

   * - XcpOnCan.c
     - Xcp On Can的函数定义(Function definition of Xcp On Can)

   * - XcpOnEth.c
     - Xcp On Eth的函数定义(Function definition of Xcp On Eth)

动态文件 Dynamic Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - 文件(File)
     - 描述(Description)
   
   * - Xcp_Callout.c
     - 定义Xcp模块Seed&Unlock功能自定义算法函数(Defines the customized algorithm function of Seed&Unlock function of Xcp module)

   * - Xcp_Callout.h
     - Xcp模块Seed&Unlock功能自定义算法函数的声明(Declares the customized algorithm function of Seed&Unlock function of Xcp module)

   * - Xcp_Cfg.c
     - 定义Xcp模块PC配置的结构体参数(Defines the structure parameters for the PC configuration of the Xcp module)
	 
   * - Xcp_Cfg.h
     - 声明Xcp模块PC配置的结构体参数(Defines the structure parameters for the PC configuration of the Xcp module)
	 
   * - Xcp_PBcfg.c
     - 定义Xcp模块PB配置的结构体参数(Defines the structure parameters for the PB configuration of the Xcp module)


错误处理 Error Handling
----------------------------------------------------------------------------------

开发错误 Development Errors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: 
   :widths: 20 10 30
   :header-rows: 1

   * - Error code
     - Value[hex]
     - Description

   * - XCP_E_UNINIT
     - 0x02
     - Module not initialized.

   * - XCP_E_INVALID_PDUID
     - 0x03
     - API call with wrong PDU ID.

   * - XCP_E_INIT_FAILED
     - 0x04
     - Initialization of XCP failed.

   * - XCP_E_PARAM_POINTER
     - 0x12
     - Null pointer has been passed as an argument.


产品错误 Product Errors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

None

运行时错误 Runtime Errors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

None


.. include:: Xcp_api.rst


配置 Configuration
================================================

传输层配置 Transfer layer configuration
----------------------------------------------------------------------------------------------------

Xcp协议栈目前支持基于CAN（支持CAN和CANFD）和ETH总线的总线标定协议。不同的传输层，Xcp数据包长度（CTO和DTO）均可配置。并且Xcp数据帧的传输速率也根据传输层不一样而会有不同。

At presence, the Xcp protocol stack supports the bus calibration protocol that is based on CAN (support CAN and CANFD) and ETH bus. The Xcp data packet length (CTO and DTO) can be configured for different transfer layers. The transfer rate of Xcp data frame varies along with transfer layer.

其关联配置项如下：

The associated configuration items are as follows:

.. list-table:: 
   :widths: 10 10 20
   :header-rows: 1

   * - 父容器(Parent container)
     - 配置项(Configuration item)
     - 描述(Description)

   * - XcpGeneral->General Settings
     - XcpSupportType
     - 选择传输层，目前仅支持CAN和ETH单选(Select transfer layer, only single selection of CAN and ETH is supported at presence)

   * - XcpGeneral->General Settings
     - XcpMaxCto
     - 上位机和ECU通讯传输的CTO最大长度(Max. length of CTO transferred by upper computer and ECU)

   * - XcpGeneral->General Settings
     - XcpMaxDto
     - 上位机和ECU通讯传输的DTO最大长度(Max. length of DTO transferred by upper computer and ECU)	 
	 

其CTO和DTO取值范围如下：

The value range of CTO and DTO is as follows: 


.. list-table:: 
   :widths: 20 20 20
   :header-rows: 1

   * - 总线(Bus)
     - Xcp数据包(Xcp data packet)
     - 取值范围(Value range)

   * - XcpOnCan
     - CTO
     - 8

   * - XcpOnCan
     - DTO
     - 8

   * - XcpOnCanFD
     - CTO
     - 8~64

   * - XcpOnCanFD
     - DTO
     - 8~64

   * - XcpOnEth
     - CTO
     - 8~255

   * - XcpOnEth
     - DTO
     - 8~1500


.. figure:: ../../../_static/参考手册/Xcp/XcpBusSlect.png
   :alt: XcpBusSlect
   :name: fig_XcpBusSelct
   :align: center

   Xcp传输层配置 (Xcp transfer layer configuration)

PDU关联 PDU association
~~~~~~~~~~~~~~~~~~~~~~~~

Xcp在AUTOSAR中，其下层模块分别为CanIf（XcpOnCan）、Soad(XcpOnEth)，其模块之间是通过PDU进行交互。

The lower module of Xcp in AUTOSAR is CanIf (XcpOnCan) and Soad(XcpOnEth) respectively, and the interaction between modules is realized through PDU.

其关联配置项如下：

The associated configuration items are as follows:

.. list-table:: 
   :widths: 10 10 20
   :header-rows: 1

   * - 父容器(Parent container)
     - 配置项(Configuration item)
     - 描述(Description)

   * - XcpConfig->XcpPdu
     - XcpRxPdu
     - 选择传输层交互的接收PDU（从CanIf或者Soad收上来）(Select receiving PDU (from CanIf or Soad) that has interaction in transfer layer)

   * - XcpConfig->XcpPdu
     - XcpTxPdu
     - 选择传输层交互的发送PDU（从Xcp下发到CanIf或者Soad）(Select sending PDU (distributed to CanIf or Soad from Xcp) that has interaction in transfer layer)

.. figure:: ../../../_static/参考手册/Xcp/XcpPdu.png
   :alt: XcpPdu
   :name: fig_XcpPdu
   :align: center

   Xcp PDU关联 (Xcp PDU association)

且XcpRxPdu和XcpTxPdu通过XcpRxPduRef引用的PDU必须在传输层（CanIf或者Soad）被引用。下图以XcpOnCan进行举例说明：

PDU that is quoted by XcpRxPdu and XcpTxPdu through XcpRxPduRef must be quoted in transfer layer (CanIf or Soad). Taking XcpOnCan as example in picture below:
   
.. figure:: ../../../_static/参考手册/Xcp/Xcp_CanIF_PDURef.png
   :alt: Xcp_CanIF_PDURef
   :name: fig_Xcp_CanIF_PDURef
   :align: center

   Xcp & CanIF PDU关联 (Xcp & CanIF PDU association)

XcpOnCanFD配置 XcpOnCanFD configuration
*****************************************************************************************************************************************

XcpOnCan和XcpOnCanFD区别为：

Difference between XcpOnCan and XcpOnCanFD:

1.在CanIF关联的Xcp PDU的CanIfRxPduCanIdType属性配置为XXX_FD_CAN；

1.The CanIfRxPduCanIdType attribute of Xcp PDU, which is associated in CanIF, is configured as XXX_FD_CAN;

2.在Xcp模块中XcpGeneral->XcpMaxCto和XcpGeneral->XcpMaxDto配置值范围会不一样；详情参见CTO和DTO取值范围。

2.The configuration value range of XcpGeneral->XcpMaxCto and XcpGeneral->XcpMaxDto in Xcp module may be different; for details, see The value range of CTO and DTO.
	 
Xcp多核分区配置 Configuration of Xcp multi-core partitioning
********************************************************************************************************************************************************************************************************

Xcp协议栈目前仅支持同一时间内在一种总线上进行标定，因此Xcp的分区归属依赖于传输层。

At presence, Xcp protocol stack supports calibration of one bus simultaneously; therefore, the partitioning of Xcp depends on the transfer layer.

多分区系统下，Xcp需要强制要求XcpRxPdu和XcpTxPdu所在分区需一致（通过ECUC进行分区匹配），Xcp协议栈的分区即为收发PDU所在分区。

For multi-partition system, the partition for XcpRxPdu and XcpTxPdu must be consistent (partition is matched through ECUC) compulsorily; the partition of Xcp is the partition of receiving/distribution PDU.

且相应的调度接口，如Xcp_MainFunction以及Xcp_EventIndication则只能在对应分区内进行调用执行。

The corresponding dispatch interfaces, such as Xcp_MainFunction and Xcp_EventIndication, can be called and executed in the corresponding partitions only.

.. figure:: ../../../_static/参考手册/Xcp/XcpPartition.png
   :alt: XcpPartition
   :name: fig_XcpPartition
   :align: center

   Xcp分区映射 (Xcp partition mapping)

XcpEvent配置 XcpEvent configuration
----------------------------------------------------------------------------------------------------------------

XcpEventchannel作为DAQ周期上传的载体，其配置不仅用于Xcp协议栈还需要生成部分A2L文件相关信息，关联静态配置参数如下：

As the carrier that is periodically uploaded by DAQ, XcpEventchannel configuration is not only used for Xcp protocol stack, but also generates the relevant information of some A2L files. The associated static configuration parameters are as follows:

.. list-table:: 
   :widths: 10 10 20
   :header-rows: 1

   * - 父容器(Parent container)
     - 配置项(Configuration item)
     - 描述(Description)

   * - XcpGeneral->General Settings
     - XcpMaxEventChannel
     - 定义ECU中最多能创建的通道的个数(Define the max. number of channels which can be created in ECU)

   * - XcpEventChannel
     - XcpEventChannelNumber
     - 定义此通道的索引（默认生成）(Define the index of this channel (generated by default))

   * - XcpEventChannel
     - XcpEventChannelConsistency
     - 定义此通道上DAQ的采样一致性(Define the sampling consistency of DAQ in this channel)

   * - XcpEventChannel
     - XcpEventChannelMaxDaqList
     - 定义此通道上最多能发送多少个DAQ(Define the max. number of DAQ that can be sent in this channel)

   * - XcpEventChannel
     - XcpEventChannelPriority
     - 定义此通道的发送优先级（暂不支持）(Define the sending priority of this channel (not supported temporarily))	 

   * - XcpEventChannel
     - XcpEventChannelTimeCycle
     - 与XcpEventChannelTimeUnit配置一起确认此通道的周期信息（用于A2L文件）(Confirm the period information of this channel along with XcpEventChannelTimeUnit (used for A2L file))	
 	 
   * - XcpEventChannel
     - XcpEventChannelTimeUnit
     - 与XcpEventChannelTimeCycle配置一起确认此通道的周期信息（用于A2L文件）(Confirm the period information of this channel along with XcpEventChannelTimeCycle (used for A2L file))

   * - XcpEventChannel
     - XcpEventChannelType
     - 定义此通道上能够承载的DAQ类型（DAQ或者STIM）(Define the type of DAQ (DAQ or STIM) that can be carried by this channel)
	 
   * - XcpEventChannel
     - XcpEventChannelTriggeredDaqListRef
     - 定义此通道上能够承载的DAQ索引（仅适用于静态DAQ）(Define the DAQ index (applies to static DAQ only) that can be carried by this channel)
	 
.. figure:: ../../../_static/参考手册/Xcp/XcpEvent.png
   :alt: XcpEvent
   :name: fig_XcpEvent
   :align: center

   Xcp Eventchannel配置 (Xcp Eventchannel configuration)
   
	 
DAQ配置 DAQ configuration
--------------------------------------------------------------------------------------------------------------------------------------------

动态DAQ（推荐） Dynamic DAQ (recommended)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

DAQ作为Xcp协议栈中非常重要的一个功能，简化了工程的集成难度，相对于静态DAQ，不用配置XcpDaqList，仅需配置如下动态参数即可：

As an important function of Xcp protocol stack, DAQ simplifies the integration of engineering, and avoids configuration of XcpDaqList when compared with static DAQ. Only the following dynamic parameters need to be configured:

.. list-table:: 
   :widths: 10 10 20
   :header-rows: 1

   * - 父容器(Parent container)
     - 配置项(Configuration item)
     - 描述(Description)

   * - XcpGeneral->DAQFormat
     - XcpDaqConfigType
     - 配置为DAQ_DYNAMIC，表示动态DAQ(Configured as DAQ_DYNAMIC, which means dynamic DAQ)

   * - XcpGeneral->DAQFormat
     - XcpDynDaqBufSize
     - 动态DAQ所用的动态内存空间，动态分配的DAQ/ODT/Entry等均从此空间进行分配(Dynamic memory space used by dynamic DAQ, the dynamically distributed DAQ/ODT/Entry is distributed from this space)

   * - XcpGeneral->DAQFormat
     - XcpDaqCount
     - 动态分配的DAQ最大数量（ALLOC_DAQ）(The max. number of dynamically distributed DAQ (ALLOC_DAQ))
	 
   * - XcpGeneral->DAQFormat
     - XcpOdtCount
     - 动态分配的ODT最大数量（ALLOC_ODT）(The max. number of dynamically distributed ODT (ALLOC_ODT))
	
   * - XcpGeneral->DAQFormat
     - XcpOdtEntriesCount
     - 动态分配的ODT Entry最大数量（ALLOC_ODT_ENTRY）(The max. Number of dynamically distributed ODT Entry (ALLOC_ODT_ENTRY))	
	 
.. figure:: ../../../_static/参考手册/Xcp/XcpDynDaq.png
   :alt: XcpDynDaq
   :name: fig_XcpDynDaq
   :align: center

   动态DAQ关联配置 (Associated configuration of dynamic DAQ)
   
静态DAQ Static DAQ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

静态DAQ的特点就是DAQ、ODT、ODT Entry的个数均需要预先配置，静态DAQ关联配置项如下：

As the feature of static DAQ, the number of DAQ, ODT and ODT Entry needs to be configured in advance. The associated configuration of static DAQ is as follows:

.. list-table:: 
   :widths: 10 10 20
   :header-rows: 1

   * - 父容器(Parent container)
     - 配置项(Configuration item)
     - 描述(Description)

   * - XcpGeneral->DAQFormat
     - XcpDaqConfigType
     - 配置为DAQ_STATIC，表示静态DAQ(Configured as DAQ_STATIC, which means static DAQ)

   * - XcpDaqList
     - XcpDaqListNumber
     - DAQ List的索引编号，从0开始默认排序(Index number of DAQ List, sorting from 0 by default)	 

   * - XcpDaqList
     - XcpDaqListType
     - 表示此DAQ List的方向（DAQ或者STIM）(The direction of this DAQ List (DAQ or STIM))

   * - XcpDaqList
     - XcpMaxOdt
     - 表示此DAQ List最多能创建多少个ODT（根据创建的ODT个数默认生成）(The max. number of ODT (which is generated according to number of created ODT by default) that can be created by DAQ List)

   * - XcpDaqList
     - XcpMaxOdtEntries
     - 表示此DAQ List中任一一个ODT最大能创建的ODT Entry数量（默认生成）(The max. Number of ODT Entry (created by default) that can be created by any ODT in this DAQ list)

   * - XcpDaqList
     - XcpDto
     - DAQ List可通过此配置选择接收的PDU（暂不支持）(DAQ List can configure the received PDU (not supported temporarily) through this configuration)
	 
   * - XcpDaqList
     - XcpOdt
     - DAQ List下静态分配的ODT(Statically distributed ODT under DAQ List)

   * - XcpOdt
     - XcpOdtEntryMaxSize
     - 表示此ODT下创建的ODT Entry长度的上限值(Upper limit of ODT Entry length created under this ODT)

   * - XcpOdt
     - XcpOdtEntry
     - ODT下静态分配的ODT Entry(Statically distributed ODT Entry under ODT)

   * - XcpOdtEntry
     - XcpOdtEntryAddress
     - ODT Entry地址（暂不可配，通过WRITE_DAQ写入）(ODT Entry address (not configurable at presence, written in through WRITE_DAQ))
	
   * - XcpOdtEntry
     - XcpOdtEntryBitOffset
     - ODT Entry位偏移（暂不可配，通过WRITE_DAQ写入）(ODT Entry bit offset (not configurable at presence, written in through WRITE_DAQ))

   * - XcpOdtEntry
     - XcpOdtEntryLength
     - ODT Entry长度（暂不可配，通过WRITE_DAQ写入）(ODT Entry length (not configurable at presence, written in through WRITE_DAQ))

   * - XcpOdtEntry
     - XcpOdtEntryNumber
     - ODT Entry索引（暂不可配，通过WRITE_DAQ写入）(ODT Entry index (not configurable at presence, written in through WRITE_DAQ))	 

   * - XcpEventChannel
     - XcpEventChannelTriggeredDaqListRef
     - 静态DAQ List需要挂载到XcpEventChannel上才有权限在此通道上周期发送(Static DAQ List needs to be mounted on XcpEventChannel before it can have period sending in this channel)
	 
.. figure:: ../../../_static/参考手册/Xcp/XcpStaticDaq.png
   :alt: XcpStaticDaq
   :name: fig_XcpStaticDaq
   :align: center

   静态DAQ关联配置 (Associated configuration of static DAQ)
   
DAQ Resume
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

DAQ Resume功能主要是通过SET_REQUEST命令把DAQ List储存到Nvm中，此功能关联的配置项如下：

DAQ Resume function is to store DAQ List in Nvm through SET_REQUEST command. The associated configuration items of this function are as follows:

.. list-table:: 
   :widths: 10 10 20
   :header-rows: 1

   * - 父容器(Parent container)
     - 配置项(Configuration item)
     - 描述(Description)

   * - XcpCommand->XcpStandard->XcpStdCmd
     - SET_REQUEST
     - SET_REQUEST命令使能开关(Enable switch of SET_REQUEST command)

   * - XcpCommand->XcpDaqStim
     - XcpDaqEnable
     - DAQ功能使能开关(Enable switch of DAQ function)

   * - XcpCommand->XcpDaqStim
     - XcpDaqResumeModeEnable
     - DAQ Resume功能使能开关（仅在XcpDaqEnable使能时可配）(Enable switch of DAQ Resume function (configurable only when XcpDaqEnable is enabled))

   * - XcpCommand->XcpDaqStim
     - XcpNvRamBlockIdRef
     - DAQ List需要存储到的目标Nvm块（仅在XcpDaqResumeModeEnable使能时可配）(DAQ List needs to be stored in the target Nvm block (configurable only when XcpDaqResumeModeEnable is enabled))

DAQ观测地址检测 DAQ observation address detection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Xcp协议栈支持限制DAQ观测地址的功能。当观测量不在此空间范围内时，会通过负响应码回复上位机。此功能关联的配置项如下：

Xcp protocol stack supports limiting of DAQ observation address. When the observed quantity is not within this spacial range, the upper computer will be responded by the negative response code. The associated configuration items of this function are as follows:

.. list-table:: 
   :widths: 5 5 20
   :header-rows: 1

   * - 父容器(Parent container)
     - 配置项(Configuration item)
     - 描述(Description)

   * - XcpCommand->XcpDaqStim
     - XcpDaqEnable
     - DAQ功能使能开关(Enable switch of DAQ function)

   * - XcpCommand->XcpDaqStim
     - XcpMeaAddrCfgs
     - DAQ观测地址集（可配置多个），不配置代表不对观测地址做限制，配置则代表通过WRITE_DAQ命令写入的DAQ地址必须在XcpMeaAddrCfgs配置集中（仅在XcpDaqEnable使能时可配）(DAQ observation address set (multiple sets can be configured); the observation address is not limited when it is not configured; when it is configured, the DAQ address that is written through WRITE_DAQ command must be within the XcpMeaAddrCfgs configuration set (configurable only when XcpDaqEnable is enabled))

   * - XcpMeaAddrCfgs
     - XcpMeasuremenAddr
     - DAQ观测起始地址(Starting address of DAQ observation)

   * - XcpMeaAddrCfgs
     - XcpMeasuremenLen
     - DAQ观测地址长度(Length of DAQ observation address)

.. figure:: ../../../_static/参考手册/Xcp/XcpCheckMeaAddr.png
   :alt: XcpCheckMeaAddr
   :name: fig_XcpCheckMeaAddr
   :align: center

   Xcp观测地址检测 (Detection of Xcp observation address)
   
Xcp在线标定 Xcp online calibration
----------------------------------------------------------------------------------------

页切换 Page switching
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Xcp协议栈中页切换功能主要是RP和WP之间做切换，通过软件方式额外创建一块缓存区，用于RP和WP之间中间数据的拷贝。

The page switching function of Xcp protocol stack is mainly used for switching between RP and WP, and creating a cache region through software, to copy the intermediate data between RP and WP.

但目前MCU中大部分都自带硬件单元模块（如英飞凌Overlay）用于页切换，因此配置数据中可由用户自定义去配置页切换使能与实现方式，相关配置如下：

Most of MCU is fitted with hardware unit module (such as Infineon Overlay) for page switching; so, the configuration data can be customized by user to configure the enabling and realization method of page switching. The relevant configurations are as follows:

.. list-table:: 
   :widths: 5 5 20
   :header-rows: 1

   * - 父容器(Parent container)
     - 配置项(Configuration item)
     - 描述(Description)

   * - XcpCommand->XcpCal
     - XcpCalEnable
     - CAL功能使能开关(Enable switch of CAL function)

   * - XcpCommand->XcpCal
     - XcpPageSwitch
     - 页切换的使能以及实现方式配置。配置为DISABLE时，不使能页切换功能；当选择为BY_HW时，那么相关的页切换操作由应用实现；(Configure enabling and realization method of page switching.) When configured as DISABLE, page switching function is not enabled; when configured as BY_HW, the relevant pages are switched by APP;
	 
.. figure:: ../../../_static/参考手册/Xcp/XcpPageSwitch.png
   :alt: XcpPageSwitch
   :name: fig_XcpPageSwitch
   :align: center

   Xcp页切换配置 (Configuration of Xcp page switching)	 

通信模式配置 Configuration of communication model
------------------------------------------------------------------------------------------------

Xcp通信支持三种通信模型，分别是标准通信、块传输以及交替通信模式。当块传输和交替通信功能均为使能时，默认就为标准通信模式。

Xcp communication supports three communication models, i.e. standard communication, block transfer and interleaved communication model. Standard communication model is entered by default when both block transfer and interleaved communication functions are enabled.

相关配置项如下：

The relevant configuration items are as follows:

.. list-table:: 
   :widths: 5 5 20
   :header-rows: 1

   * - 父容器(Parent container)
     - 配置项(Configuration item)
     - 描述(Description)

   * - XcpCommand->XcpStandard
     - XcpSlaveBlockMode
     - Slave块传输模式（主要指UPLOAD块传输）(Slave block transfer model (mainly refers to UPLOAD block transfer))	 

   * - XcpCommand->XcpStandard
     - XcpMasterBlockMode
     - Master块传输模式（主要指DOWNLOAD和PROGRAM块传输，使用相同的Minst和MaxBs），其功能与交替模式为互斥配置(Master block transfer model (mainly refers to DOWNLOAD and PROGRAM block transfer, using the same Minst and MaxBs); its function and interleaved mode are mutual exclusion configurations)

   * - XcpCommand->XcpStandard
     - XcpMinSt
     - Master块传输模式下两帧报文之间的最小时间间隔(The min. time interval between two frame messages under Master block transfer model)

   * - XcpCommand->XcpStandard
     - XcpMaxBs
     - Master块传输模式下最多能连续发送多少帧报文(The max. number of frame messages which can be sent continuously under Master block transfer model)

   * - XcpCommand->XcpStandard
     - XcpInterLeavedMode
     - 交替通信使能开关(Enable switch of interleaved communication)
	
   * - XcpCommand->XcpStandard
     - XcpnterLeavedQueueSize
     - 交替通信模式下ECU最多能缓存多少帧命令(The min. number of frame commands which can be cached by ECU under interleaved communication model)		 
	 
.. figure:: ../../../_static/参考手册/Xcp/XcpComModel.png
   :alt: XcpComModel
   :name: fig_XcpComModelCfg
   :align: center

   Xcp通信模式配置 (Configuration of Xcp communication model)


其他特性 Other characteristics
----------------------------------------------------------------------------------------

内存操作 Memory operation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Xcp协议栈支持加速拷贝和内存对齐，当使能加速拷贝配置项时，会加快Xcp协议栈中数据拷贝的速度，会避免复杂场景下(比如多核工程，一个核在测量时另一个核在快速的写入数据)测量数据的一致性出现问题；

Xcp protocol stack supports accelerated copy and memory alignment. When accelerated copy is enabled, it will increase the speed of data copying in Xcp protocol stack, to avoid the consistency error of measurement data under complex scenarios (for example, one kernel is measuring while the other one is writing data quickly in the multi-kernel engineering);

当使能内存对齐配置项时，会在Xcp协议栈内部将传输的地址进行内存对齐后再进行操作，避免在一些芯片平台上因为地址没对齐而进而使得对地址的操作报错。此功能关联的配置项如下：

When memory alignment is enabled, the transfer address will be subject to memory alignment in the Xcp protocol stack prior to operation, to avoid address error when the address is not aligned in some chip platforms. The associated configuration items of this function are as follows:

.. figure:: ../../../_static/参考手册/Xcp/Xcp拷贝加速和内存对齐配置项.png
   :alt: XcpFastCopy&AddressAlign
   :name: fig_XcpFastCopy&AddressAlign
   :align: center

   Xcp拷贝加速和内存对齐配置 (Configuration of Xcp copy acceleration and memory alignment)
   
大小端自检 Big/small end self-check
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Xcp内部涉及到内存组装时会受到大小端的影响，当配置的大小端和实际硬件大小端不一致时，会导致一些意想不到的错误，大小端自检配置项使能后会在初始化时对芯片的大小端和配置的大小端进行校验，不匹配将初始化失败；此功能关联的配置项如下：

The memory assembly of Xcp may be affected by the big/small end. When the configured big/small end is inconsistent with that of actual hardware, some unexpected errors may occur. When big/small end self-check is enabled, the big/small end of chip and configuration will pass self-check during initialization, and initialization will fail if they do not match; the associated configuration items of this function are as follows:

.. figure:: ../../../_static/参考手册/Xcp/Xcp大小端自检.png
   :alt: XcpEndiannessself-check
   :name: fig_XcpEndiannessself-check
   :align: center

   Xcp大小端自检配置 (Configuration of Xcp Big/small-end Self-check)
