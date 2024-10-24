===================
OBD_集成手册
===================





 目标
=====

本集成手册用于指导客户进行OBD诊断栈集成，文档主要包括的内容为：OBD诊断栈集成指导、基于特定应用的集成示例讲解。

由于各项目的需求不同，集成示例不会针对于特定的项目做详细讲解。

 缩写词和术语
=============

.. table:: 表格 2‑1

   +---------------+------------------------------------------------------+
   | 缩写词/术语   | 描述                                                 |
   +---------------+------------------------------------------------------+
   | MCAL          | Microcontroller Abstraction Layer微控制器抽象层      |
   +---------------+------------------------------------------------------+
   | CanIf         | CAN Interface module CAN接口                         |
   +---------------+------------------------------------------------------+
   | ComM          | Communication Manager module 通信管理                |
   +---------------+------------------------------------------------------+
   | PduR          | PDU Router module PDU路由                            |
   +---------------+------------------------------------------------------+
   | Dcm           | Diagnostic Communication Manager 诊断通信管理        |
   +---------------+------------------------------------------------------+
   | Dem           | Diagnostic Event Manager 诊断事件管理                |
   +---------------+------------------------------------------------------+
   | CanTp         | CAN Transport Layer CAN传输层                        |
   +---------------+------------------------------------------------------+

 参考文档
=========

[1] UDSonCAN

[2] 参考手册 Dem.pdf

[3] 参考手册 DCM.pdf

[4] 参考手册 DCM.pdf

 协议栈集成
===========

项目交付的内容为：协议栈源码和ORIENTAIS
Configurator配置工具。协议栈细分为协议栈的各模块及其对应的配置工具模块。

OBD诊断栈各配置模块的功能介绍，参见表 4‑1诊断栈各配置模块介绍。

使用协议栈源码和配置工具，进行协议栈的集成的步骤，参见表 4‑2
协议栈集成的步骤。

.. table:: 表 4‑1诊断栈各配置模块介绍

   +---------+------------------------------------------------------------+
   | 模块名  | 功能                                                       |
   +---------+------------------------------------------------------------+
   | Can     | CAN驱动配置。(由MCAL具导入)                                |
   +---------+------------------------------------------------------------+
   | CanIf   | CanIf 模块主要处理上层模块与底层驱动的之间PDU 的传递，为上 |
   |         |                                                            |
   |         | 层模块提供统一的接口来管理不同的CAN 硬件模块               |
   +---------+------------------------------------------------------------+
   | EcuC    | 用于辅助配置工具完成配置的模块。主                         |
   |         | 要提供Pdu的定义，其它模块通过关联EcuC中Pdu，相互关联起来。 |
   +---------+------------------------------------------------------------+
   | PduR    | PDU                                                        |
   |         | Router主要为相关模块提供基于I-PDU                          |
   |         | 的路由服务。在诊断栈中，主要是提供CANTP与DCM之间的路由服务 |
   +---------+------------------------------------------------------------+
   | CanTp   | CANTP 模块实现依据ISO15765-2 标准规范中定义的CAN           |
   |         | 总线数据在传输层的数据接收发送功能                         |
   +---------+------------------------------------------------------------+
   | DCM     | 依据IS                                                     |
   |         | O15765-3和ISO15031-5标准描述，实现诊断请求报文的解析，响应 |
   |         | (正响应和负响应)与执行。主要功能有：实现UDS、OBD诊断服务。 |
   +---------+------------------------------------------------------------+
   | DEM     | 实现诊断故障的存储与管理功能，提供API 接口供其他模块读取   |
   |         |                                                            |
   |         | DTC 和对应的冻结帧数据和扩展数据                           |
   +---------+------------------------------------------------------------+

.. table:: 表 4‑2 协议栈集成的步骤

   +-----+--------------------------+------------------------------------+
   | 步  | 操作                     | 说明                               |
   | 骤  |                          |                                    |
   +-----+--------------------------+------------------------------------+
   | 1   | ORIENTAIS                | 若配置工具已经搭建                 |
   |     | Configurator配置工具     | ，则仅需进行协议栈模块的加载操作。 |
   |     | 工程搭建和协议栈模块加载 |                                    |
   +-----+--------------------------+------------------------------------+
   | 2   | 模块配置及配置文件生成   | NA                                 |
   +-----+--------------------------+------------------------------------+
   | 3   | 代码集成                 | 现有工程、                         |
   |     |                          | 协议栈源代码和配置生成文件的集成。 |
   +-----+--------------------------+------------------------------------+
   | 4   | 验证测试                 | NA                                 |
   +-----+--------------------------+------------------------------------+

**注意：协议栈集成之前，用户须确保已经有基础工程，且本协议栈相关的其他协议栈能正常工作。**

新建ORIENTAIS Configurator配置工程及模块加载
--------------------------------------------

安装ORIENTAIS Configurator软件后，双击软件图标打开软件。

.. figure:: ../../_static/集成手册/OBD/image1.png
   :width: 5.76389in
   :height: 3.03542in

   图 4‑1 新建工程

菜单栏File🡪New🡪Project，新建工程。

.. figure:: ../../_static/集成手册/OBD/image2.png
   :width: 5.75625in
   :height: 3.17431in

   图 4‑2新建工程

在弹出的新建窗口中选择Autosar下的 [BSW Project]，选择Next。

.. figure:: ../../_static/集成手册/OBD/image3.png
   :width: 3.25694in
   :height: 3.10208in

   图 4‑3新建工程

在弹出的窗口中输入工程名，选择Finish。

.. figure:: ../../_static/集成手册/OBD/image4.png
   :width: 3.77011in
   :height: 3.17341in

   图 4‑4新建工程

选择[Bsw_Builder]，右键单击，选择New ECU Configuration。

.. figure:: ../../_static/集成手册/OBD/image5.png
   :width: 3.3153in
   :height: 0.89191in

   图 4‑5新建工程

在弹出的窗口中输入ECU名，然后选择Next。

.. figure:: ../../_static/集成手册/OBD/image6.png
   :width: 2.67153in
   :height: 2.53403in

   图 4‑6选择芯片平台

在弹出的窗口中勾选需添加的模块，点击Finish。

.. figure:: ../../_static/集成手册/OBD/image7.png
   :width: 3.77431in
   :height: 3.57986in

   图 4‑7选择模块

新建工程如下所示，步骤0中添加的模块已经被加入到工程中。

.. figure:: ../../_static/集成手册/OBD/image8.png
   :width: 1.53333in
   :height: 2.18194in

   图 4‑8工程结构示例

模块配置及生产代码
------------------

模块配置
~~~~~~~~

模块的具体配置，取决于具体的项目需求。OBD诊断栈各模块配置项的详细介绍，参见表
4‑3协议栈各模块配置参考文档。

.. table:: 表 4‑3协议栈各模块配置参考文档

   +----------------+-----------------------------------------------------+
   | 模块           | 参考文档及其章节                                    |
   +----------------+-----------------------------------------------------+
   | Can            | MCAL对应的Can配置手册                               |
   +----------------+-----------------------------------------------------+
   | CanIf          | 参考手册_CanTp.pdf                                  |
   +----------------+-----------------------------------------------------+
   | PduR           | 参考手册_PduR.pdf                                   |
   +----------------+-----------------------------------------------------+
   | NvM            | 参考手册_NvM.pdf                                    |
   +----------------+-----------------------------------------------------+
   | CanTp          | 参考手册_CanTp.pdf                                  |
   +----------------+-----------------------------------------------------+
   | Dcm            | 参考手册_Dcm.pdf                                    |
   +----------------+-----------------------------------------------------+
   | Dem            | 参考手册_Dem.pdf                                    |
   +----------------+-----------------------------------------------------+

配置代码生成
~~~~~~~~~~~~

#. 在ORIENTAIS
   Configurator主界面左方，选择对应的协议栈，单击右键弹出Validate
   All和Generate All菜单。

.. figure:: ../../_static/集成手册/OBD/image9.png
   :width: 2.55625in
   :height: 2.24514in

   图 4‑9生成配置

2. 选择Validate
   All对本协议栈各配置选项进行校验，没有错误提示信息即校验通过。若有错误信息，请按照错误提示修改。

3. 选择Generate
   All，生成配置文件。右下角的Console窗口输出生成的配置文件信息。

.. figure:: ../../_static/集成手册/OBD/image10.png
   :width: 2.19375in
   :height: 2.95486in

   图 4‑10生成配置结果

4. 将ORIENTAIS Configurator切换到Resource模式，即可查看生成的配置文件。

.. figure:: ../../_static/集成手册/OBD/image11.png
   :width: 3.61528in
   :height: 2.61944in

   图 4‑11生成配置工程结构

功能集成
--------

代码集成
~~~~~~~~

诊断栈代码包括两部分：项目提供的诊断栈源码和ORIENTAIS
Configurator配置生成代码。诊断栈集成包括诊断栈源码（CANIF，CANSM，PDUR，CANTP，COMM，DCM，DEM等）、定时器源码和部分其他模块源码。

用户须将诊断栈源码和4.2.2章节生成的源代码添加到集成开发工具的对应文件夹。

注意：诊断栈集成之前，用户须确保已经有通信基础工程，且本诊断栈相关的其他功能栈能正常工作。

集成注意事项
~~~~~~~~~~~~

对于集成过程中，协议栈特殊要求和用户经常出现的问题，归类总结形成表
4‑4协议栈协议栈集成约束清单。用户需逐一排查表中的约束项，以避免集成问题出现。

.. table:: 表 4‑4协议栈协议栈集成约束清单

   +-----+---------+-----------------------------------------------------+
   | 编  | 类别    | 约束限制                                            |
   | 号  |         |                                                     |
   +-----+---------+-----------------------------------------------------+
   | 1   | 堆栈    | 用户需确保为任务堆栈和中断堆栈分配足够的堆栈空间。  |
   +-----+---------+-----------------------------------------------------+
   | 2   | 头文件  | 添加协议                                            |
   |     |         | 栈代码之后，用户需更新集成开发工具中的头文件路径。  |
   |     |         |                                                     |
   |     |         | 调用协议栈API的源文件，需要包含协议栈的头文件。     |
   +-----+---------+-----------------------------------------------------+
   | 3   | 初始化  | OBD诊断栈的初始化顺序为：Dem_PreInit，CanTp_Init，  |
   |     |         | Dcm_Init，Dem_Init。                                |
   +-----+---------+-----------------------------------------------------+
   | 4   | 周      | CanTp_MainFunction，Dcm_MainF                       |
   |     | 期函数  | unction和Dem_MainFunction需要被周期性任务函数调用。 |
   +-----+---------+-----------------------------------------------------+

 集成示例
=========

本章节通过OBD诊断栈为例，向用户展示OBD诊断栈的集成过程。用户可以据此熟悉OBD诊断栈配置工具的配置过程，以及如何应用配置工具生成的配置文件。示例是基于具有正常工作的CAN通信工程之上。

本章节先完成基本OBD配置，使得工程可以编译通过，并实现基础OBD诊断通讯，然后根据具体需求服务进行添加或修改。

**注意：本示例不代表用户的实际配置情况，用户需要根据自己的实际需求，决定各个参数的配置。**

集成目标
--------

通过搭建基础工程，实现OBD诊断基本请求应答功能。使用标准帧CAN0x7df作为请求，标准帧0x7E8作为响应，同时实现OBD服务01,02,03,07,09的功能。示例网络层时间参数如表
5‑1 网络层定时参数（仅 OBD 排放相关诊断要求）

.. table:: 表 5‑1 网络层定时参数（仅 OBD 排放相关诊断要求）

   +---------+--------------------------+--------------+-----------------+
   | 定      | 描述                     | 超时时间(ms) | 性能            |
   | 时参数  |                          |              | 要求时间（ms）  |
   +---------+--------------------------+--------------+-----------------+
   | N_As    | 发送方 CAN 报文确认超时  | 25           | -               |
   +---------+--------------------------+--------------+-----------------+
   | N_Ar    | 接收方 CAN 报文确认超时  | 25           | -               |
   +---------+--------------------------+--------------+-----------------+
   | N_Bs    | 流控帧传输超时           | 75           | -               |
   +---------+--------------------------+--------------+-----------------+
   | N_Br    | 流控帧接收端发送等待时间 | -            | <10             |
   +---------+--------------------------+--------------+-----------------+
   | N_Cs    | 连续帧发送时间间隔       | -            | ST*min          |
   +---------+--------------------------+--------------+-----------------+
   | N_Cr    | 连续帧传输超时           | 150 ms       | -               |
   +---------+--------------------------+--------------+-----------------+

模块的配置
----------

新建配置工程及模块加载操作，请参考本文档4.1章节。生成代码过程请参考章节4.2。

Can模块与CanIf模块配置
~~~~~~~~~~~~~~~~~~~~~~

在CAN模块与CANIF模块中实现用于OBD通信的CAN报文，具体配置方法请参考文档《CAN通信栈》。

.. table:: 表 5‑2 OBD协议CAN需求

   +--------------+-------------------------+----------------------------+
   | 报文ID       | 发送/接收               | 报文长度                   |
   +--------------+-------------------------+----------------------------+
   | 0x7df        | 接收                    | 8字节                      |
   +--------------+-------------------------+----------------------------+
   | 0x7E0        | 接收                    | 8字节                      |
   +--------------+-------------------------+----------------------------+
   | 0x7E8        | 发送                    | 8字节                      |
   +--------------+-------------------------+----------------------------+

EcuC模块配置
~~~~~~~~~~~~

#. 双击EcuC模块，打开EcuC模块配置界面。

.. figure:: ../../_static/集成手册/OBD/image12.png
   :width: 4.82083in
   :height: 3.65903in

   图 5‑1 ECUC配置界面

在EcucConfigSets栏目上右键，选择EcucConfigSet。再在EcucConfigSet上右键，选择New🡪EcucPduCollection。

.. figure:: ../../_static/集成手册/OBD/image13.png
   :width: 5.75972in
   :height: 1.41528in

   图 5‑2新建EcucPduCollection

·PduIdTypeEnum 选择UINT16（这个参数是定义PDU个数的时用的。）

·PduLengthTypeEnum
选择UINT16（这个参数是定义存储数据长度时使用的变量的长度）

2. 在EcucPduCollection上右键新建Pdu，分别用于CanIf、CanTp、Dcm。

.. figure:: ../../_static/集成手册/OBD/image14.png
   :width: 2.675in
   :height: 1.85833in

   图 5‑3新建PDU

建议不要使用默认生成的Pdu名字（如：Pdu_0），将Pdu名字改成有意义的名字。这里按照发送和接收，可以将Pdu名字改为报文的名字。

.. figure:: ../../_static/集成手册/OBD/image15.png
   :width: 2.32031in
   :height: 2.44713in

   图 5‑4 OBD所需配置的PDU

3. 配置各个PduLength，

.. figure:: ../../_static/集成手册/OBD/image16.png
   :width: 5.31111in
   :height: 1.91111in

   图 5‑5 OBDPDU配置：CANIFRX

CANTP，CANIF PDU的length配置为8；Dcm Pdu
长度必须与/Dcm/DcmConfigSet/DcmDsl/DcmDslBuffer 里面配置的Dcm
Tx、RxBuffer 长度一致。

ECUC模块到此配置结束。可以在模块上右键，然后选择校验，查看是否配置有错误。校验后提示窗口没有错误信息，即校验通过。

CANTp模块配置
~~~~~~~~~~~~~

CANTp属于通用网络配置，没有针对OBD的特异性配置。

CanTpGeneral配置
^^^^^^^^^^^^^^^^

配置CanTpGeneral

|image1|

图 5‑6 CanTpGeneral

CANTpConfig配置
^^^^^^^^^^^^^^^

#. 配置CanTpChannelMode为全双工(根据实际需要选择)。根据需求的通道配置CanTpMaxChannelCnt，如需要一个通道给UDS，一个通道给OBD，则配置为2。

.. figure:: ../../_static/集成手册/OBD/image18.png
   :width: 5.37569in
   :height: 1.33264in

   图 5-7 CANTpConfig

2. 配置CanTpChannelMode为全双工(根据实际需要选择)。

|image2|

图 5‑8 CanTpChannel

3. 配置一个CanTpRxNSdu。根据需求设定各个网络层参数，关联OBD使用的CANTp的RxPDU。

|image3|

图 5‑9 CanTpRxNSdu配置

4. 配置一个CanTpRxNSdu。根据需求设定各个网络层参数，关联OBD使用的CANTp的RxPDU。

5. 在CanTpRxNSdu下CanTpRxNPdu关联CANIF的PDU。

|image4|

图 5‑10 CanTpRxNSdu配置

6. 配置一个CanTpTxNSdu。根据需求设定各个网络层参数，关联OBD使用的CANTp的TxPDU。

|image5|

图 5‑11 CanTpTxNSdu

7. 在CanTpTxNSdu下CanTpRxFcNPdu关联CANIF的RxPDU。

|image6|

图 5‑12 CanTpTxNSdu

8. 在CanTpTxNSdu下CanTpTxNPdu关联CANIF的TxPDU。

|image7|

图 5‑13 CanTpTxNSdu

PduR模块配置
~~~~~~~~~~~~

#. 双击PduR模块，打开PduR模块配置界面。

|image8|

图 5‑14 PduR

2. PduRGeneral配置。

若不使用PDUR功能，则勾选PduRZeroCostOperation，一般不勾选，使用PDUR实现CANTP与DCM之间的路由。

3. PduRBswModuler配置。

PduR模块的目的是实现上层模块到下层模块的路由。PduRBswModuler对象用来描述上层模块和下层模块属性。本示例中上层模块为DCM，下层模块为CANTp。所以需要新建2个PduRBswModuler对象，分别对应DCM和CANTp。

|image9|

图 5‑15 PduRBswModuler-CanTp

|image10|

图 5‑16 PduRBswModuler-DCM

4. 添加2个PduRRoutingPath，PduRRouteType配置为TP

PDUR_ROUTING_DiagOBDReq_RX：接收OBD请求

PDU配置CANTP_DiagOBDReq->DCM_DiagOBDReq

PDUR_ROUTING_DiagOBDResp_TX：发送OBD响应

PDU配置DCM_DiagOBDResp ->CANTP_DiagOBDResp

.. figure:: ../../_static/集成手册/OBD/image28.png
   :width: 5.75694in
   :height: 1.50764in

   图 5-17 PduRRoutingPath

DCM模块配置
~~~~~~~~~~~

#. 双击DCM模块，打开DCM模块配置界面。

|image11|

图 5‑18 DCMGeneral

2. DCMGeneral标签页中的参数保持默认即可。

DSD配置
^^^^^^^

#. 新建DcmDsdSidTab，配置DcmDsdSidTabId需与其他服务列表（如UDS）不一同的值

|image12|

图 5‑19 DcmDsdSidTab

勾选DcmDsdServiceUsed使能服务；

配置需要的OBD服务DcmDsdSidTabServiceId

|image13|

图 5‑20 DsdService

DSL配置
^^^^^^^

#. DcmDslBuffer中配置两个buffer分别用于发送和接收，配置Dcm
   Tx、RxBuffer及其length，需要与EcuC中Dcm对应的Pdu Length的值保持一致。

|image14|

图 5‑21 DcmDslBuffer

2. 配置OBD的DSLProtocol，实现CANTp与DCM之间的PDU关联。需要修改项如下，若项目无特殊需求，未提到的配置保持默认值即可。

..

   DcmDslProtocolID选择DCM_OBD_ON_CAN；

   DcmDslProtocolSIDTable选择DcmDsdServiceTable中的OBD服务表；

   DcmDslProtocolRxBufferRef和DcmDslProtocolTxBufferRef关联接收和发送的buffer配置。

|image15|

图 5‑22 DSLProtocol

3. 在上步的DcmDslProtocolRow_OBD中新建配置DcmDslMainConnection，选择Dcm通信的ComMChannel，并新建1个DcmDslProtocolRx，1个DcmDslProtocolTx。

|image16|

图 5‑23 DcmDslMainConnection

4. 为每个DcmDslProtocolRx、DcmDslProtocolTx添加Dcm对应的PDU及寻址类型。

|image17|

图 5‑24 DcmDslProtocolRx

|image18|

图 5‑25 DcmDslProtocolTx

5. 右键新建DcmDslCallbackDCMRequestService。

|image19|

图 5‑26 DcmDslCallbackDCMRequestService

DSP配置
^^^^^^^

本小节配置目的是完成基本OBD诊断通讯和编译通过，具体服务的功能请见本章节后续小节具体服务的描述。此小节目的是建立最小系统配置，未提到的配置保持默认即可，服务的配置将在本章节具体服务小节中介绍。

|image20|

图 5‑27 DSP

添加一个DcmDspPid。选择服务后暂不修改其它内容，内容修改将在5.2.7章节进行。

|image21|

图 5‑28 DcmDspPid

|image22|

图 5‑29 DcmDspPidService

DEM模块配置
~~~~~~~~~~~

DEMGeneral配置
^^^^^^^^^^^^^^

#. 如图 5‑30所示添加配置集。添加Dataelement,GeneralOBD,Indicator

..

   |image23|

图 5‑30 DEMGeneral

2. 在DemGeneral->DemOBDSupport配置为DEM_OBD_MASTER。同时关联一个的DemIndicator。

..

   DemGeneral->DemTypeOfDTCSupported选择15031-6

   DemClearDTCLimitation选择DEM_ALL_SUPPORTED_DTCS

   若无明确需求，其它配置可保持默认即可。

|image24|

图 5‑31 DemGeneral

新建CSDataElement在DemGeneralOBD中关联。

|image25|

图 5‑32 DemGeneralOBD

DEMConfig配置
^^^^^^^^^^^^^

配置DemDTCAttributes，关联DemMemoryDestinationRef到DemPrimaryMemory。关联DemFreezeFrameRecNumClassRef。其它配置先保持默认配置。

#. 新建DTCAttribute用于OBD的DTC。

|image26|

图 5-33 DTCAttribute

2. 添加一个DemDTC，设置DemDtcValue，关联DemDTCAttributesRef。

|image27|

图 5-34 DemDTC

3. 配置DemEventParameter：

..

   a)勾选DemEventAvailable；

   b)关联DemOperationCycleRef

   c) DemEventKind选择SWC

   d）DemDTCRef关联步骤②配置的DTC

   e)修改DemEventKind为DEM_EVENT_KIND_SWC

|image28|

图 5‑35 DemEventParameter

Service 0x01 
~~~~~~~~~~~~~

#. 在DcmDsp中添加DcmDspPid，根据需求确定PID。在PidIdentifier填写PID，在DcmDspPidService选择01服务，在DcmDspPidSize中填写其数据长度：

DcmDspPidIdentifier：配置PID

DcmDspPidService：选择使用此PID的服务

DcmDspPidSize：设置数据大小

DcmDspPidUsed：使能此PID

.. figure:: ../../_static/集成手册/OBD/image47.png
   :width: 5.76597in
   :height: 2.22083in

   图 5‑36 DcmDspPid

2. 配置DcmDspPidData建立service1的配置

.. figure:: ../../_static/集成手册/OBD/image48.png
   :width: 4.47917in
   :height: 1.1094in

   图 5-37 DcmDspPidService

3. DcmDspPidDataUsePort一般选择USE_DATA_SYNCH_FNC,协议栈会从DcmDspPidDataReadFnc中获取数据，并设置DcmDspPidDataType。

.. figure:: ../../_static/集成手册/OBD/image49.png
   :width: 4.65347in
   :height: 1.76806in

   图 5‑38 DcmDspPidDataUsePort

4. 根据DcmDspPidDataReadFnc配置构造获取PID数据的函数。示例如下：

Std_ReturnType **Rte_DcmDspPidDataRead_01**\ (

/\* PRQA S 3432++ \*/ /\* MISRA Rule 20.7 \*/

P2VAR(uint8,AUTOMATIC,DCM_VAR)Data

/\* PRQA S 3432-- \*/ /\* MISRA Rule 20.7 \*/)

{

   Data[0] = 1;

   Data[1] = 2;

   Data[2] = 3;

   Data[3] = 4;

   **return** E_OK;

}

Service 0x02 
~~~~~~~~~~~~~

#. 添加DemExternalCSDataElementClass用于获取PID数据

.. figure:: ../../_static/集成手册/OBD/image50.png
   :width: 5.7625in
   :height: 1.66667in

   图 5‑39 DemExternalCSDataElementClass

2. 配置DemPidClass中DemPidIdentifier，并关联步骤1中DemExternalCSDataElementClass

.. figure:: ../../_static/集成手册/OBD/image51.png
   :width: 5.01597in
   :height: 2in

   图 5-40 DemPidClass

.. figure:: ../../_static/集成手册/OBD/image52.png
   :width: 5.76389in
   :height: 2.33056in

   图 5‑41 DemPidClass

3. DCM新建配置一个用于Service02的DcmDspPidData

.. figure:: ../../_static/集成手册/OBD/image53.png
   :width: 4.59931in
   :height: 2.23056in

   图 5‑42 DcmDspPidData

4. DcmDspPidData关联步骤2中DemPidClass。

.. figure:: ../../_static/集成手册/OBD/image54.png
   :width: 4.38264in
   :height: 2.61944in

   图 5‑43 DcmDspPidData

5. DemDTCAttributes_OBD中不能有其它协议的FreezeFrame。

.. figure:: ../../_static/集成手册/OBD/image55.png
   :width: 5.76181in
   :height: 3.21458in

   图 5‑44 DemDTCAttributes

Service 0x03 / 07 
~~~~~~~~~~~~~~~~~~

#. 在DcmDsdServiceTable中添加03和07服务；

#. （0x0A服务选用）在DemGeneral中添加DemPermanentMemory用于0x0A服务。根据需求将DemGeneral中DemMaxNumberEventEntryPermanent配置为非0值。

.. figure:: ../../_static/集成手册/OBD/image56.png
   :width: 1.91181in
   :height: 3.05139in

   图 5‑45 DcmDsdServiceTable

.. figure:: ../../_static/集成手册/OBD/image57.png
   :width: 5.76458in
   :height: 1.59167in

   图 5‑46 DemGeneral

3. 添加DemObdDTC并配置DemDtcValue

.. figure:: ../../_static/集成手册/OBD/image58.png
   :width: 5.75764in
   :height: 1.95in

   图 5‑47 DemObdDTC

4. （0x0A服务选用）DemMemoryDestinationRef选择DemPermanentMemory

.. figure:: ../../_static/集成手册/OBD/image59.png
   :width: 5.75764in
   :height: 2.84444in

   图 5‑48 DemDTCAttributes

5. 添加DemDTC_P014300并配置，根据需求选择DemDTCAttributes。

.. figure:: ../../_static/集成手册/OBD/image60.png
   :width: 5.46173in
   :height: 1.99266in

   图 5‑49 DemDTC_P014300

6. 添加DemEventParameter，勾选DemEventAvailable；关联DemDTCRef；选择DemOperationCycleRef。

.. figure:: ../../_static/集成手册/OBD/image61.png
   :width: 5.76458in
   :height: 2.6625in

   图 5‑50 DemEventParameter

5. 在初始化和开启操作循环后通过DEM函数Dem_SetEventStatus报告故障发生。如下：

..

   **void** **Task_Init**\ (**void**)

   {

   EcuM_StartupTwo();

   Dem_Init(&DemPbCfg);

   Dem_SetOperationCycleState(DemOperationCycle_ID,DEM_CYCLE_STATE_START);

   Dem_SetEventStatus(DemEventParameter_P0143, DEM_EVENT_STATUS_FAILED);

   }

Service 0x09
~~~~~~~~~~~~

#. 在DcmDsdServiceTable中添加0x09的OBD服务列表。

.. figure:: ../../_static/集成手册/OBD/image62.png
   :width: 6.0599in
   :height: 2.80637in

   图 5‑51 DcmDsdServiceTable

2. 在DSP中添加DcmDspVehInfo，配置DcmDspVehInfoInfoType，此处以INFOTYPE
   0x02 (VIN)为例，填写为0x02。

.. figure:: ../../_static/集成手册/OBD/image63.png
   :width: 5.75764in
   :height: 3.34861in

   图 5‑52 DcmDspVehInfo

3. 在DcmDspVehInfo中添加DcmDspVehInfoData，配置获取Vehicle
   information的函数名称
   DcmDspVehInfoDataReadFnc，并根据需求配置数据的大小DcmDspVehInfoDataSize为17字节。

.. figure:: ../../_static/集成手册/OBD/image64.png
   :width: 5.75903in
   :height: 3.43333in

   图 5‑53 DcmDspVehInfoData

4. 在Rte_Dcm.c中将数据传入 DcmDspVehInfoDataReadFnc配置的函数.

.. figure:: ../../_static/集成手册/OBD/image65.png
   :width: 5.76111in
   :height: 1.29861in

   图 5‑54 测试示例程序

源代码集成
----------

诊断栈源代码集成步骤如下：

#. 在MCAL工程的基础上，同步5.2.1章添加的Can模块配置文件。

#. 从基线中取出4.3.1章中相关的源代码添加到工程中。

#. 将在4.2.2章中ORIENTAS配置生成的诊断相关配置文件添加到工程中。

#. 添加相关头文件目录。

协议栈调度集成
--------------

OBD诊断栈调度集成步骤如下：

#. 协议栈调度集成，需要逐一排查并实现表
   4‑4协议栈协议栈集成约束清单所罗列的问题，以避免集成出现差错。

#. 集成CanTp_Callout.c 中CanTp_ResetTime、CanTp_GetTimeSpan 函数。

..

   FUNC(**void**, CANTP_CODE)\ **CanTp_ResetTime**\ (

   P2VAR(uint32, AUTOMATIC, CANTP_APPL_DATA) TimerPtr)

   {

   \*TimerPtr = Frt_ReadOutMS();

   }

   FUNC(**void**, CANTP_CODE)\ **CanTp_GetTimeSpan**\ (

   uint32 TimerPtr,

   P2VAR(uint32, AUTOMATIC, CANTP_APPL_DATA) TimeSpanPtr)

   {

   \*TimeSpanPtr = Frt_CalculateElapsedMS(TimerPtr);

}

3. 集成Dcm_Callout.c 中Dcm_ResetTime、Dcm_GetTimeSpan 函数。

..

   FUNC(**void**, *DCM_CODE*) **Dcm_ResetTime**\ (P2VAR(uint32,
   AUTOMATIC, DCM_VAR) TimerPtr)

   {

   \*TimerPtr = Frt_ReadOutMS();

}

   FUNC(**void**, DCM_CODE) **Dcm_GetTimeSpan**\ (uint32
   TimerPtr,P2VAR(uint32, AUTOMATIC, DCM_VAR) TimeSpanPtr)

   {

   \*TimeSpanPtr = Frt_CalculateElapsedMS(TimerPtr);

}

4. 编译链接代码，将软件烧写进芯片。

OBD诊断栈有关的代码，在下方的main.c文件中给出重点标注。

**注意 :
本示例中，OBD诊断栈初始化的代码置于main.c文件，并不代表其他项目同样适用于将其置于main.c文件中。**

#include "CanTp.h"

#include "Dcm.h"

#include "Dem.h"

初始化、mainfunction及应用接口集成如下：

int main\ **(**\ void\ **)**

**{**

Mcu_Init\ **(**\ Mcu_ConfigRoot\ **);**

Mcu_InitClock\ **(**\ 0\ **);**

**while** **(**\ MCU_PLL_UNLOCKED **==** Mcu_GetPllStatus\ **())**

**{**

/\* wait for PLL locked \*/

**}**

Mcu_DistributePllClock\ **();**

/\* IrqGtm_Init \*/

IrqGtm_Init\ **();**

/\* Port Initialize \*/

Port_Init\ **(&**\ Port_ConfigRoot\ **[**\ 0\ **]);**

/\* GPT Initialize \*/

Gpt_Init\ **(&**\ Gpt_ConfigRoot\ **[**\ 0\ **]);**

/\* Gpt enable 1ms notification,and start \*/

Gpt_EnableNotification\ **(**\ GptConf_GptChannel_GptChannelConfiguration_0\ **);**

Gpt_StartTimer\ **(**\ GptConf_GptChannel_GptChannelConfiguration_0\ **,**
6250\ **);**

/\* CAN Initialize \*/

Can_17_MCanP_Init\ **(&**\ Can_17_MCanP_ConfigRoot\ **[**\ 0\ **]);**

/\*Enable CAN*/

Can_17_MCanP_SetControllerMode\ **(**\ Can_17_MCanPConf_CanController_CanController_0\ **,**
CAN_T_START\ **);**

/\*Dem module Pre_Init*/

Dem_PreInit\ **();**

CanIf_Init\ **(&**\ CanIf_InitCfgSet\ **);**

/\* end Add Code \*/

/\* Initialize the CanSM module \*/

CanSM_Init\ **(&**\ CanSM_Config\ **);**

/\* Initialize the ComM module \*/

ComM_Init\ **(&**\ ComM_Config\ **);**

/\* end Add Code \*/

/\*Initialize the CanTp module*/

CanTp_Init(&CanTp_Config);

Dcm_Init(&Dcm_Cfg);

Dem_Init(&DemPbCfg);

Dem_SetOperationCycleState\ **((**\ uint8\ **)**\ DemOperationCycle_ID\ **,**
DEM_CYCLE_STATE_START\ **);**

ComM_CommunicationAllowed\ **(**\ 0\ **,** TRUE\ **);**

Mcal_EnableAllInterrupts\ **();**

ComM_RequestComMode\ **(**\ ComMUser_0\ **,**
COMM_FULL_COMMUNICATION\ **);**

**while(**\ 1\ **)**

**{**

**if** **(**\ TRUE **==** Gpt_1msFlag\ **)**

**{**

Gpt_1msFlag **=** FALSE\ **;**

Run_msCounter\ **();**

**}**

**if** **(**\ TRUE **==** Gpt_5msFlag\ **)**

**{**

Gpt_5msFlag **=** FALSE\ **;**

CanSM_MainFunction\ **();**

ComM_MainFunction\ **(**\ 0\ **);**

CanTp_MainFunction\ **();**

Dcm_MainFunction\ **();**

Dem_MainFunction\ **();**

**}**

**}**

**return** 1\ **;**

**}**

验证结果
--------

验证Service 0x01
~~~~~~~~~~~~~~~~

#. 通过CAN工具向ECU发送01服务请求报文：

CANID：0x7df

请求内容：02 01 00 00 00 00 00 00

期望结果：收到CANID0x7E8报文06 41 00 80 00 00 00 00

2. 通过CAN工具向ECU发送01服务请求报文：

CANID：0x7df

请求内容：02 01 01 00 00 00 00 00

期望结果：收到CANID0x7E8响应，内容与章节5.2.7接口填写的数据内容一致，报文为06
41 01 01 02 03 04 00

.. figure:: ../../_static/集成手册/OBD/image66.png
   :width: 5.76111in
   :height: 1.47083in

   图 5‑55 验证结果01

验证Service 0x02
~~~~~~~~~~~~~~~~

#. 通过CAN工具向ECU发送02服务请求报文：

CANID：0x7df

请求内容：03 02 00 00 00 00 00 00

期望结果：收到CANID0x7E8返回报文内容07 42 00 00 00 10 00 00

2. 通过CAN工具向ECU发送02服务请求报文：

CANID：0x7df

请求内容：03 02 0C 00 00 00 00 00

期望结果：收到CANID0x7E8返回报文内容05 42 0C 00 11 22 00 00

.. figure:: ../../_static/集成手册/OBD/image67.png
   :width: 5.76181in
   :height: 1.47778in

   图 5‑56 验证02服务功能

验证0x03 / 07
~~~~~~~~~~~~~

#. 通过CAN工具向ECU发送03服务请求报文：

CANID：0x7df

请求内容：01 03 00 00 00 00 00 00

期望结果：收到CANID0x7E8返回DTC，报文内容04 43 01 01 43 00 00 00

2. 通过CAN工具向ECU发送07服务请求报文：

CANID：0x7df

请求内容：01 07 00 00 00 00 00 00

期望结果：收到CANID0x7E8响应返回DTC，报文为04 47 01 43 00 00 00 00

.. figure:: ../../_static/集成手册/OBD/image68.png
   :width: 5.76042in
   :height: 1.64583in

   图 5‑57 03&07验证结果

验证Service 0x09
~~~~~~~~~~~~~~~~

#. 通过CAN工具向ECU发送09服务请求报文：

CANID：0x7df

请求内容：02 09 00 00 00 00 00 00

期望结果：收到CANID0x7E8返回报文内容06 49 00 40 00 00 00 00

2. 通过CAN工具向ECU发送09服务请求报文：

CANID：0x7df

请求内容：02 09 02 00 00 00 00 00

期望结果：收到CANID0x7E8响应，内容与5.2.10章节填写的数据内容一致。

.. figure:: ../../_static/集成手册/OBD/image69.png
   :width: 5.76736in
   :height: 2.35417in

   图 5‑58 验证结果09

.. |image1| image:: ../../_static/集成手册/OBD/image17.png
   :width: 3.07014in
   :height: 2.50486in
.. |image2| image:: ../../_static/集成手册/OBD/image19.png
   :width: 5.0125in
   :height: 2.01181in
.. |image3| image:: ../../_static/集成手册/OBD/image20.png
   :width: 5.16458in
   :height: 2.46597in
.. |image4| image:: ../../_static/集成手册/OBD/image21.png
   :width: 5.75972in
   :height: 2.27639in
.. |image5| image:: ../../_static/集成手册/OBD/image22.png
   :width: 5.76111in
   :height: 2.28611in
.. |image6| image:: ../../_static/集成手册/OBD/image23.png
   :width: 5.76111in
   :height: 2.33542in
.. |image7| image:: ../../_static/集成手册/OBD/image24.png
   :width: 5.75694in
   :height: 2.32083in
.. |image8| image:: ../../_static/集成手册/OBD/image25.png
   :width: 2.40347in
   :height: 2.29028in
.. |image9| image:: ../../_static/集成手册/OBD/image26.png
   :width: 4.83542in
   :height: 3.22083in
.. |image10| image:: ../../_static/集成手册/OBD/image27.png
   :width: 4.25625in
   :height: 2.88403in
.. |image11| image:: ../../_static/集成手册/OBD/image29.png
   :width: 3.16042in
   :height: 3.58194in
.. |image12| image:: ../../_static/集成手册/OBD/image30.png
   :width: 5.75903in
   :height: 2.825in
.. |image13| image:: ../../_static/集成手册/OBD/image31.png
   :width: 4.89653in
   :height: 2.96319in
.. |image14| image:: ../../_static/集成手册/OBD/image32.png
   :width: 4.47778in
   :height: 3.00208in
.. |image15| image:: ../../_static/集成手册/OBD/image33.png
   :width: 5.24792in
   :height: 3.10625in
.. |image16| image:: ../../_static/集成手册/OBD/image34.png
   :width: 6.06736in
   :height: 3.05069in
.. |image17| image:: ../../_static/集成手册/OBD/image35.png
   :width: 5.75556in
   :height: 2.87292in
.. |image18| image:: ../../_static/集成手册/OBD/image36.png
   :width: 5.75556in
   :height: 2.80556in
.. |image19| image:: ../../_static/集成手册/OBD/image37.png
   :width: 3.88134in
   :height: 3.61962in
.. |image20| image:: ../../_static/集成手册/OBD/image38.png
   :width: 4.08472in
   :height: 2.43958in
.. |image21| image:: ../../_static/集成手册/OBD/image39.png
   :width: 4.37569in
   :height: 2.69792in
.. |image22| image:: ../../_static/集成手册/OBD/image40.png
   :width: 5.29816in
   :height: 3.21084in
.. |image23| image:: ../../_static/集成手册/OBD/image41.png
   :width: 2.79028in
   :height: 3.19444in
.. |image24| image:: ../../_static/集成手册/OBD/image42.png
   :width: 5.35903in
   :height: 3.60208in
.. |image25| image:: ../../_static/集成手册/OBD/image43.png
   :width: 5.17222in
   :height: 3.13056in
.. |image26| image:: ../../_static/集成手册/OBD/image44.png
   :width: 5.44722in
   :height: 3.4625in
.. |image27| image:: ../../_static/集成手册/OBD/image45.png
   :width: 5.8232in
   :height: 2.05949in
.. |image28| image:: ../../_static/集成手册/OBD/image46.png
   :width: 5.99514in
   :height: 3.28611in
