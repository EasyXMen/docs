===================
UDSOnCan_集成手册
===================





目标
====

本集成手册用于指导客户进行诊断栈集成，文档主要包括的内容为：诊断栈集成指导、基于普通应用的集成示例讲解、项目集成特殊说明。

由于各项目的需求不同，集成示例不会针对于特定的项目做详细讲解。

缩写词和术语
============

.. table:: 表格 2‑1 缩写词和术语

   +---------------+------------------------------------------------------+
   | **\           | **描述**                                             |
   | 缩写词/术语** |                                                      |
   +---------------+------------------------------------------------------+
   | BSW           | Basic Software                                       |
   +---------------+------------------------------------------------------+
   | MCAL          | Microcontroller Abstraction Layer                    |
   +---------------+------------------------------------------------------+
   | CanIf         | CAN Interface module                                 |
   +---------------+------------------------------------------------------+
   | CanSm         | CAN State Manager module                             |
   +---------------+------------------------------------------------------+
   | ComM          | Communication Manager module                         |
   +---------------+------------------------------------------------------+
   | PduR          | PDU Router module                                    |
   +---------------+------------------------------------------------------+
   | Dcm           | Diagnostic Communication Manager                     |
   +---------------+------------------------------------------------------+
   | Dem           | Diagnostic Event Manager                             |
   +---------------+------------------------------------------------------+
   | CanTp         | CAN Transport Layer                                  |
   +---------------+------------------------------------------------------+
   | NvM           | NVRAM Manager                                        |
   +---------------+------------------------------------------------------+

参考文档
========

[1]参考手册_CanIf.pdf

[2]参考手册_PduR.pdf

[3]参考手册_CanSM.pdf

[4]参考手册_DCM.pdf

[5]参考手册_Dem.pdf

[6]参考手册_CanTp.pdf

[7]参考手册_EcuC.pdf

[8]ODX file导入操作说明.docx

诊断栈集成
==========

项目交付的内容为：诊断栈源码和ORIENTAIS
Configurator配置工具。诊断栈细分为诊断栈的各模块及其对应的配置工具模块。

.. table:: 表 4‑1诊断栈各配置模块介绍

   +---------+------------------------------------------------------------+
   | **模\   | **功能**                                                   |
   | 块名**  |                                                            |
   +---------+------------------------------------------------------------+
   | Can     | CAN驱动配置。(由MCAL工具导入)                              |
   +---------+------------------------------------------------------------+
   | CanIf   | CanIf模块主要处理上层模块与底层驱动的之间\                 |
   |         | PDU的传递，为上层模块提供统一的接口来管理不同的CAN硬件模块 |
   +---------+------------------------------------------------------------+
   | EcuC    | 用于辅助配置工具完成配置的模块。主\                        |
   |         | 要提供Pdu的定义，其它模块通过关联EcuC中Pdu，相互关联起来。 |
   +---------+------------------------------------------------------------+
   | PduR    | PDU Router主要为通讯接口模块（CANIF）、传输协议模块（CAN   |
   |         | TP、J1939\                                                 |
   |         | TP）、诊断通讯管理模块（DCM、J1939DCM）以及通讯模块（C     |
   |         | OM、LDCOM）以及IPDUM、SECOC等模块提供基于I-PDU的路由服务。 |
   +---------+------------------------------------------------------------+
   | CanTp   | CANTP模块实现依据ISO15\                                    |
   |         | 765-2标准规范中定义的CAN总线数据在传输层的数据接收发送功能 |
   +---------+------------------------------------------------------------+
   | Dcm     | 依据ISO15765-3和ISO14229-1标\                              |
   |         | 准描述，实现诊断请求报文的解析，响应(正响应和负响应)与执行 |
   +---------+------------------------------------------------------------+
   | Dem     | 实现诊断故障的存储与管理功能\                              |
   |         | ，提供API接口供其他模块读取DTC和对应的冻结帧数据和扩展数据 |
   +---------+------------------------------------------------------------+

.. table:: 表 4‑2 诊断栈集成的步骤

   +------+--------------------------+------------------------------------+
   |      | **操作**                 | **说明**                           |
   |**步\ |                          |                                    |
   |骤**  |                          |                                    |
   |      |                          |                                    |
   +------+--------------------------+------------------------------------+
   | 1    | ORIENTAIS                | 若配置工程已经搭建\                |
   |      | Configurator配置工具\    | ，则仅需进行诊断栈模块的加载操作。 |
   |      | 工程搭建和诊断栈模块加载 |                                    |
   +------+--------------------------+------------------------------------+
   | 2    | 模块配置及配置文件生成   | 进行基础的诊断栈配置               |
   +------+--------------------------+------------------------------------+
   | 3    | 代码集成                 | 现有工程、\                        |
   |      |                          | 诊断栈源代码和配置生成文件的集成。 |
   +------+--------------------------+------------------------------------+
   | 4    | 验证测试                 | 用CAN报文监测工具收发诊断报文      |
   +------+--------------------------+------------------------------------+

**注意：诊断栈集成之前，用户须确保已经有MCAL层可以跑通的基础工程，且诊断栈相关的其他功能栈如通信栈、网络管理栈、NvM栈能正常工作。**

新建ORIENTAIS Configurator配置工程及模块加载
--------------------------------------------

#. 安装ORIENTAIS Configurator软件后，双击软件图标打开软件。

|image1|

图4.1-1

菜单栏File🡪New🡪Project，新建工程。

|image2|

图4.1-2

2. 在弹出的新建窗口中选择Autosar下的 [BSW Project]，选择Next。

..

|image3|

图4.1-3

3. 在弹出的窗口中输入工程名，选择Finish。

..

|image4|

图4.1-4

4. 选择[Bsw_Builder]，右键单击，选择New ECU
   Configuration，在弹出的窗口中选择并填写对应的Ecu名称。

|image5|

图4.1-5

**注意: 可选择的Ecu可能随项目的不同而不同**

5. 选择新建的Ecu，右键单击，选择“Add Module选项”。

|image6|

图4.1-6

6. 在弹出的选项框中勾选相应模块，点击“Finish”。

|image7|

图4.1-7

7. 新建工程如下所示，上一步中添加的模块已经被加入到工程中。

|image8|

图4.1-8

模块配置及生产代码
------------------

模块配置
~~~~~~~~

.. table:: 表 4‑3诊断栈各模块配置参考文档

   +--------+--------------------------------------------+----------------+
   | **\    | **参考文档及其章节**                       | **说明**       |
   | 模块** |                                            |                |
   +--------+--------------------------------------------+----------------+
   | Can    | MCAL对应的Can配置手册                      |                |
   +--------+--------------------------------------------+----------------+
   | CanIf  | 参考手册_CanTp.pdf                         |                |
   +--------+--------------------------------------------+----------------+
   | PduR   | 参考手册_PduR.pdf                          |                |
   +--------+--------------------------------------------+----------------+
   | NvM    | 参考手册_NvM.pdf                           |                |
   +--------+--------------------------------------------+----------------+
   | CanTp  | 参考手册_CanTp.pdf                         |                |
   +--------+--------------------------------------------+----------------+
   | Dcm    | 参考手册_Dcm.pdf                           |                |
   +--------+--------------------------------------------+----------------+
   | Dem    | 参考手册_Dem.pdf                           |                |
   +--------+--------------------------------------------+----------------+

配置代码生成
~~~~~~~~~~~~

#. 在ORIENTAIS
   Configurator主界面左方，选择对应的诊断栈，单击右键弹出Validate
   All和Generate All菜单。

|image9|

图4.2.2-1

2. 选择Validate All对本诊断栈各配置选项进行校验。

3. 选择Generate
   All，生成配置文件。右下角的Console窗口输出生成的配置文件信息。

|image10|

图4.2.2-2

4. 点击config文件夹，即可查看生成的配置文件。

|image11|

图4.2.2-3

功能集成
--------

代码集成
~~~~~~~~

诊断栈代码包括两部分：项目提供的诊断栈源码和ORIENTAIS
Configurator配置生成代码。诊断栈集成包括诊断栈源码（CANIF，CANSM，PDUR，CANTP，COMM，DCM，DEM等）、定时器源码和部分其他模块源码，具体文件见表4-4。

用户须将诊断栈源码和章节4.2.2生成的源代码添加到集成开发工具的对应文件夹。诊断栈集成的文件结构，见章节5.3。

表4-4诊断栈源码文件

+-----------------+---------------------------------+-----------------+
| 移库文件夹      | 移库文件                        | 说明            |
+-----------------+---------------------------------+-----------------+
| ComM            | ComM.c、ComM.h、                | 通信栈源码      |
|                 |                                 |                 |
|                 | ComM_BusSM.h、                  |                 |
|                 |                                 |                 |
|                 | ComM_Com.h、                    |                 |
|                 |                                 |                 |
|                 | ComM_Dcm.h、                    |                 |
|                 |                                 |                 |
|                 | ComM_BswM.h、                   |                 |
|                 |                                 |                 |
|                 | ComM_EcuM.h、ComM_Internal.c、C |                 |
|                 | omM_Internal.h、ComM_MemMap.h、 |                 |
|                 |                                 |                 |
|                 | ComM_Nm.h                       |                 |
+-----------------+---------------------------------+-----------------+
| CanIf           | CanIf.c、CanIf.h、              |                 |
|                 |                                 |                 |
|                 | CanIf_Cbk.h                     |                 |
|                 | 、CanIf_MemMap.h、CanIf_Types.h |                 |
+-----------------+---------------------------------+-----------------+
| CanSM           | CanSM.c、CanSM.h、              |                 |
|                 |                                 |                 |
|                 | CanSM_BswM.h、                  |                 |
|                 |                                 |                 |
|                 | CanSM_Cbk.h、                   |                 |
|                 |                                 |                 |
|                 | CanSM_ComM.h、CanSM_MemMa       |                 |
|                 | p.h、CanSM_TxTimeoutException.h |                 |
+-----------------+---------------------------------+-----------------+
| PDUR            | PduR_CanIf.h、                  |                 |
|                 |                                 |                 |
|                 | PduR_Com.h、PduR_Internal.c     |                 |
|                 | 、PduR_Internal.h、PduR_MemMap. |                 |
|                 | h、PduR_Types.h、PduR.c、PduR.h |                 |
+-----------------+---------------------------------+-----------------+
| CanTp           | CanTp.c、CanTp.h、              |                 |
|                 |                                 |                 |
|                 | CanTp_Cbk.h                     |                 |
|                 | 、CanTp_MemMap.h、CanTp_Types.h |                 |
+-----------------+---------------------------------+-----------------+
| FreeRTimer      | FreeRTimer.c、FreeRTimer.h      | 定时器源码      |
+-----------------+---------------------------------+-----------------+
| Dcm             | Dc                              | Dcm部分源码     |
|                 | m.c、Dcm.h、Dcm_Cbk.h、DcmDsd、 |                 |
|                 |                                 |                 |
|                 | DcmDsl、DcmDsp、Dcm_Include.h、 |                 |
|                 |                                 |                 |
|                 | Dcm_Internal.h、Dcm_MemMap.h、  |                 |
|                 |                                 |                 |
|                 | Dcm_Types.h、                   |                 |
+-----------------+---------------------------------+-----------------+
| Dem             | Dem.c、Dem_CfgEnum              | Dem部分源码     |
|                 | .h、Dem_CfgTypes.h、Dem_Dcm.c、 |                 |
|                 | Dem_Dcm.h、DemEventDebounce.c、 |                 |
|                 | Dem_EventMemory.c、Dem_EventQue |                 |
|                 | ue.c、Dem_ExtendedData.c、Dem_F |                 |
|                 | reezeFrame.c、Dem_Internal.c、D |                 |
|                 | em_MemMap.h、Dem.h、Dem_Types.h |                 |
+-----------------+---------------------------------+-----------------+

**注意：诊断栈集成之前，用户须确保已经有基础工程，且本诊断栈相关的其他功能栈能正常工作。**

集成注意事项
~~~~~~~~~~~~

对于集成过程中，诊断栈特殊要求和用户经常出现的问题，归类总结形成 表
4‑5诊断栈集成约束清单。用户需逐一排查表中的约束项，以避免集成问题出现。

.. table:: 表 4‑5 诊断栈诊断栈集成约束清单

   +------+---------+-----------------------------------------------------+
   |      |         | **约束限制**                                        |
   |**编\ |**类别** |                                                     |
   |号**  |         |                                                     |
   |      |         |                                                     |
   +------+---------+-----------------------------------------------------+
   | **\  | 中断    | 通信栈\                                             |
   | 1**  |         | 有中断、轮询或混合三种工作模式。若选取中断或混合模\ |
   |      |         | 式，用户需在通信栈配置对应的中断并填充中断服务API。 |
   +------+---------+-----------------------------------------------------+
   | **\  | 堆栈    | 用户需确保为任务堆栈和中断堆栈分配足够的堆栈空间。  |
   | 2**  |         |                                                     |
   +------+---------+-----------------------------------------------------+
   | **\  | 头文件  | 添加\                                               |
   | 3**  |         | 诊断栈代码之后，用户需更新集成开发工具中的头文件路\ |
   |      |         | 径。调用诊断栈API的源文件，需要包含诊断栈的头文件。 |
   +------+---------+-----------------------------------------------------+
   | **\  | 初始化  | 以CAN通信为例，诊断栈的初始化顺序为：Can_Init，\    |
   | 4**  |         | CanI\                                               |
   |      |         | f_Init，PduR_Init，CanSM_Init，CanTp_Init，Dcm_Init |
   +------+---------+-----------------------------------------------------+
   | **\  | 周\     | Dcm_MainFunction，Dem_MainFun\                      |
   | 5**  | 期函数  | ction和CanTp_MainFunction需要被周期性任务函数调用。 |
   +------+---------+-----------------------------------------------------+

集成示例
========

本章节通过普通的CAN诊断栈为例，向用户展示诊断栈的集成过程。用户可以据此熟悉诊断栈配置工具的配置过程，以及如何应用配置工具生成的配置文件。

为让用户更清晰的了解工具的使用，所用的配置均逐一手动完成。

**注意：本示例不代表用户的实际配置情况，用户需要根据自己的实际需求，决定各个参数的配置。**

集成目标
--------

**CAN报文需求：**

.. table:: 表格 5‑1 CAN报文需求

   +--------+------------------+------+------+-------+----------+-------+
   | **报\  | **报文**         |**发\ | **发\| **报\ | **报文** | **工\ |
   | 文ID** |                  |送**  | 送** | 文**  |          | 作**  |
   |        | **名称**         |      |      |       | **长度** |       |
   |        |                  |      | **模\| **周\ |          | **模\ |
   |        |                  |**接\ | 式** | 期**  |          | 式**  |
   |        |                  |收**  |      |       |          |       |
   +--------+------------------+------+------+-------+----------+-------+
   | 0x723  | CAN_DiagReqPhy   | 接收 | 触发 | -     | 8\       | 中断  |
   |        |                  |      |      |       | **字节** |       |
   +--------+------------------+------+------+-------+----------+-------+
   | 0x7ff  | CAN_DiagReqFun   | 接收 | 触发 | -     | 8\       | 中断  |
   |        |                  |      |      |       | **字节** |       |
   +--------+------------------+------+------+-------+----------+-------+
   | 0x623  | CAN_DiagResp     | 发送 | 触发 | -     | 8\       | 中断  |
   |        |                  |      |      |       | **字节** |       |
   +--------+------------------+------+------+-------+----------+-------+

模块的配置
----------

新建配置工程及模块加载操作，请参考本文档4.2章节。

Can模块配置
~~~~~~~~~~~

配置诊断协议栈之前需要使用MCAL工具配置Can模块，但是只涉及到与诊断栈中报文收发有关系的部分（主要是HardwareObeject），具体配置选项请参考MCAL工具的帮助手册进行配置。

EcuC模块配置
~~~~~~~~~~~~

#. 新建9个PDU，分别用于CanIf、CanTp、Dcm。

|image12|

图5.2.2-1

2. 为每个PDU配置length（根据项目不同配置不同的Pdu长度）。

|image13|

图5.2.2-2

|image14|

图5.2.2-3

**注意：Dcm
Pdu长度必须与/Dcm/DcmConfigSet/DcmDsl/DcmDslBuffer里面配置的Dcm
Tx、RxBuffer长度一致**

CanIf模块配置
~~~~~~~~~~~~~

#. 新建Hoh。

|image15|

图5.2.3-1

2. 分别新建至少1个接收诊断报文，1个发送诊断报文。

..

|image16|

图5.2.3-2

3. 分别新建2个接收诊断PDU，1个发送诊断PDU，UL选择CanTp，并选择在EcuC中配置的CanIf对应的PDU。

|image17|

图5.2.3-3

|image18|

图5.2.3-4

|image19|

图5.2.3-5

|image20|

图5.2.3-6

PduR模块配置
~~~~~~~~~~~~

#. 在PduRBswModules中添加CanTp、Dcm。

|image21|

图5.2.4-1

2. 添加3个PduRRoutingPath，PduRRouteType配置为TP。

|image22|

图5.2.4-2

3. 配置诊断功能寻址请求（FuncReq）、物理寻址请求（PhysReq）、响应（Resp）的路由路径。诊断请求的PduRRoutingPath的PduRSrcPdu选择CanTp对应的PDU，PduRDestPDU选择Dcm对应的PDU。诊断响应的PduRRoutingPath的则相反。

|image23|

图5.2.4-3

|image24|

图5.2.4-4

CanTp模块配置
~~~~~~~~~~~~~

#. CanTpGeneral的配置如下。

|image25|

图5.2.5-1

2. 添加1个CanTpChannel，CanTpChannelMode配置为FULL_DUPLEX全双工，并添加2个CanTpRxNSdu，1个CanTpTxNSdu，分别对应功能、物理寻址请求及响应。

|image26|

图5.2.5-2

3. 为每个NSdu配置相关参数，并且选择EcuC中对应的CanTp的PDU。

|image27|

图5.2.5-3

|image28|

图5.2.5-4

|image29|

图5.2.5-5

4. 为每个NSdu配置关联的CanIf对应的PDU，注意功能寻址请求NSdu不需要配置发送流控帧的CanTpTxFcNPdu，物理寻址请求需要配置发送流控帧的CanTpTxFcNPdu，响应的NSdu需要配置接收流控帧的CanTpRxFcNPdu，如下图所示。

|image30|

图5.2.5-6

|image31|

图5.2.5-7

|image32|

图5.2.5-8

Dcm模块配置
~~~~~~~~~~~

#. DcmGeneral配置

|image33|

图5.2.6-1

2. 配置DcmDsl，先配置Dcm
   Tx、RxBuffer及其length，需要与EcuC中Dcm对应的Pdu Length的值保持一致。

|image34|

图5.2.6-2

3. 配置DcmDslProtocol，选择Protocol、Buffer、ServiceTable。

|image35|

图5.2.6-3

4. 配置DcmDslMainConnection，选择Dcm通信的ComMChannel，并新建2个DcmDslProtocolRx，1个DcmDslProtocolTx。

|image36|

图5.2.6-4

5. 为每个DcmDslProtocolRx、DcmDslProtocolTx添加Dcm对应的PDU及寻址类型。

|image37|

图5.2.6-5\ 

|image38|

图5.2.6-6

6. 配置DcmDsdServiceTable，添加所需的服务及子服务，及其寻址方式、会话访问限制、安全级访问限制。

|image39|

图5.2.6-7

7. 配置DcmDspSession，SessionLevel与10服务的子服务对应，P2及P2Star时间参数根据需求进行配置。

|image40|

图5.2.6-8

|image41|

图5.2.6-9

8. 配置DcmDspSerurity，SecurityLevel与27服务的子服务对应，如2701、2702对应level1，2705、2706对应level3。

|image42|

图5.2.6-10

9. 配置DcmDspRoutines，其中DcmDspCommonAuthorizationRef配置为每个Routine的会话访问限制与安全级访问限制。

|image43|

图5.2.6-11

10. Routine下的3个容器分别对应3101、3102、3103的子服务功能，可按需求选择配置，并且可在容器中配置子服务的IN/OUT参数类型及长度。

|image44|

图5.2.6-12

11. 配置DcmDspComControl，此项用于配置28服务控制通信的ComM channel。

|image45|

图5.2.6-13

12. 配置DcmDspDidInfos，此项为每个Did配置22服务可读或2E服务可写，以及相关的会话访问限制、安全级访问限制。

|image46|

图5.2.6-14

|image47|

图5.2.6-15

13. 配置DcmDspDatas，为每个Did配置DcmDspDataUsePort、类型、长度（bit为单位），并按需求选择上一步配置的DcmDspDidInfos。

|image48|

图5.2.6-16

14. 配置DcmDspDid，配置Did的DcmDspDidIdentifier及DcmDspDidInfos。

|image49|

图5.2.6-17

15. 配置DcmDspSignal，选择上一步DcmDspDatas中添加的配置。

|image50|

图5.2.6-18

Dem模块配置
~~~~~~~~~~~

#. 根据需求配置DemGeneral，相关配置项的意义可参考AutoSAR标准或Dem参考手册。

|image51|

图5.2.7-1

|image52|

图5.2.7-2

|image53|

图5.2.7-3

2. 配置DemDataElementClass，其中可配置DemInternalDataElement（Dem内部数据）及DemExternalCSDataElement（外部CS接口获取数据）。

|image54|

图5.2.7-4

|image55|

图5.2.7-5

|image56|

图5.2.7-6

3. 配置扩展数据Extended
   Data，需要配置DemExtendedDataRecordClass以及DemExtendedDataClass，如下图所示添加相应的配置。

|image57|

图5.2.7-6

4. 配置冻结帧Freeze
   Frame，需要配置DemDidClass、DemFreezeFrameClass、DemFreezeFrameRecNumClass以及DemFreezeFrameRecordClass，如下图所示添加相应的配置。

|image58|

图5.2.7-7

|image59|

图5.2.7-8

|image60|

图5.2.7-9

|image61|

图5.2.7-10

5. 配置DemPrimaryMemory，配置Event存储的最大数量，一般与DTC数量保持一致，若DTC数量太大，可考虑采用Displacement策略，减少此存储数量。

|image62|

图5.2.7-11

6. 配置DemDTCAttribute，选择上面几步配置中添加的配置项。

|image63|

图5.2.7-12

7. 配置DemDebounceCounterBasedClass

|image64|

图5.2.7-13

8. 配置DemDebounceTimeBasedClass

|image65|

图5.2.7-14

9. 配置DemDTC，添加DTC Value，并选择DemDTCAttribute。

|image66|

图5.2.7-15

10. 配置DemEventParameter，选择Event类型、关联的DTC及操作循环等，并可根据需求配置是否添加Debounce以及Debounce
    Base。

|image67|

图5.2.7-16

|image68|

图5.2.7-17

源代码集成
----------

诊断栈源代码集成步骤如下：

#. 在MCAL工程的基础上，同步5.2.1章添加的Can模块配置文件。

#. 从基线中取出4.3.1章中相关的源代码添加到工程中。

#. 将在4.2.2章中ORIENTAS配置生成的诊断相关配置文件添加到工程中。

#. 添加相关头文件目录。

诊断栈调度集成
--------------

诊断栈调度集成步骤如下：

#. 集成CanTp_Callout.c中CanTp_ResetTime、CanTp_GetTimeSpan函数。

#. 集成Dcm_Callout.c中Dcm_ResetTime、Dcm_GetTimeSpan函数。CanTp_Callout.c集成源码如下（若无TM模块，使用FreeRTimer中的接口）：

|image69|

图5.4-1

Dcm_Callout.c集成源码如下（本工程集成OS相关接口，如果项目中无OS，可使用FreeRTimer中的接口）：

|image70|

图5.4-2

|image71|

图5.4-3

3. 诊断栈调度集成，需要逐一排查并实现表 4‑5诊断栈集成约束清单
   所罗列的问题，以避免集成出现差错。

|image_code_1|
|image_code_2|

4. 编译链接代码，将生成的elf文件烧写进芯片。

验证结果
--------

根据集成目标，共配置了3个报文，其中2个接收报文分别为诊断物理寻址及诊断功能寻址，1个发送报文为诊断响应。

|image72|

图5.5-1

.. |image1| image:: ../../_static/集成手册/UDSonCAN/image1.png
   :width: 5.74792in
   :height: 3.01389in
.. |image2| image:: ../../_static/集成手册/UDSonCAN/image2.png
   :width: 5.75069in
   :height: 3.00347in
.. |image3| image:: ../../_static/集成手册/UDSonCAN/image3.png
   :width: 3.63611in
   :height: 3.50903in
.. |image4| image:: ../../_static/集成手册/UDSonCAN/image4.png
   :width: 4.01528in
   :height: 3.40764in
.. |image5| image:: ../../_static/集成手册/UDSonCAN/image5.png
   :width: 3.29514in
   :height: 3.16667in
.. |image6| image:: ../../_static/集成手册/UDSonCAN/image6.png
   :width: 5.19167in
   :height: 3.13333in
.. |image7| image:: ../../_static/集成手册/UDSonCAN/image7.png
   :width: 4.6875in
   :height: 4.21181in
.. |image8| image:: ../../_static/集成手册/UDSonCAN/image8.png
   :width: 4.86797in
   :height: 3.58681in
.. |image9| image:: ../../_static/集成手册/UDSonCAN/image9.png
   :width: 5.75833in
   :height: 3.47569in
.. |image10| image:: ../../_static/集成手册/UDSonCAN/image10.png
   :width: 5.75833in
   :height: 3.47222in
.. |image11| image:: ../../_static/集成手册/UDSonCAN/image11.png
   :width: 5.75833in
   :height: 3.45833in
.. |image12| image:: ../../_static/集成手册/UDSonCAN/image12.png
   :width: 5.76528in
   :height: 3.51458in
.. |image13| image:: ../../_static/集成手册/UDSonCAN/image13.png
   :width: 5.76667in
   :height: 2.44653in
.. |image14| image:: ../../_static/集成手册/UDSonCAN/image14.png
   :width: 5.76458in
   :height: 2.43681in
.. |image15| image:: ../../_static/集成手册/UDSonCAN/image15.png
   :width: 5.75833in
   :height: 3.77083in
.. |image16| image:: ../../_static/集成手册/UDSonCAN/image16.png
   :width: 4.95278in
   :height: 3.24236in
.. |image17| image:: ../../_static/集成手册/UDSonCAN/image17.png
   :width: 5.75833in
   :height: 3.73819in
.. |image18| image:: ../../_static/集成手册/UDSonCAN/image18.png
   :width: 5.75833in
   :height: 3.76111in
.. |image19| image:: ../../_static/集成手册/UDSonCAN/image19.png
   :width: 5.75833in
   :height: 3.75069in
.. |image20| image:: ../../_static/集成手册/UDSonCAN/image20.png
   :width: 5.75833in
   :height: 3.74653in
.. |image21| image:: ../../_static/集成手册/UDSonCAN/image21.png
   :width: 5.76736in
   :height: 2.62361in
.. |image22| image:: ../../_static/集成手册/UDSonCAN/image22.png
   :width: 5.76458in
   :height: 2.43681in
.. |image23| image:: ../../_static/集成手册/UDSonCAN/image23.png
   :width: 5.02917in
   :height: 2.12569in
.. |image24| image:: ../../_static/集成手册/UDSonCAN/image24.png
   :width: 5.05486in
   :height: 2.13681in
.. |image25| image:: ../../_static/集成手册/UDSonCAN/image25.png
   :width: 5.76458in
   :height: 2.43681in
.. |image26| image:: ../../_static/集成手册/UDSonCAN/image26.png
   :width: 5.76458in
   :height: 2.43681in
.. |image27| image:: ../../_static/集成手册/UDSonCAN/image27.png
   :width: 5.76458in
   :height: 2.43681in
.. |image28| image:: ../../_static/集成手册/UDSonCAN/image28.png
   :width: 5.76458in
   :height: 2.43681in
.. |image29| image:: ../../_static/集成手册/UDSonCAN/image29.png
   :width: 5.76458in
   :height: 2.43681in
.. |image30| image:: ../../_static/集成手册/UDSonCAN/image30.png
   :width: 5.76458in
   :height: 2.43681in
.. |image31| image:: ../../_static/集成手册/UDSonCAN/image31.png
   :width: 5.76458in
   :height: 2.43681in
.. |image32| image:: ../../_static/集成手册/UDSonCAN/image32.png
   :width: 5.76458in
   :height: 2.43681in
.. |image33| image:: ../../_static/集成手册/UDSonCAN/image33.png
   :width: 5.76458in
   :height: 2.43681in
.. |image34| image:: ../../_static/集成手册/UDSonCAN/image34.png
   :width: 5.76458in
   :height: 2.43681in
.. |image35| image:: ../../_static/集成手册/UDSonCAN/image35.png
   :width: 5.76458in
   :height: 2.43681in
.. |image36| image:: ../../_static/集成手册/UDSonCAN/image36.png
   :width: 5.75833in
   :height: 2.43194in
.. |image37| image:: ../../_static/集成手册/UDSonCAN/image37.png
   :width: 5.76458in
   :height: 2.43681in
.. |image38| image:: ../../_static/集成手册/UDSonCAN/image38.png
   :width: 5.76458in
   :height: 2.43681in
.. |image39| image:: ../../_static/集成手册/UDSonCAN/image39.png
   :width: 5.76458in
   :height: 2.43681in
.. |image40| image:: ../../_static/集成手册/UDSonCAN/image40.png
   :width: 5.76458in
   :height: 2.43681in
.. |image41| image:: ../../_static/集成手册/UDSonCAN/image41.png
   :width: 5.76458in
   :height: 2.43681in
.. |image42| image:: ../../_static/集成手册/UDSonCAN/image42.png
   :width: 5.76458in
   :height: 2.43681in
.. |image43| image:: ../../_static/集成手册/UDSonCAN/image43.png
   :width: 5.76458in
   :height: 2.43681in
.. |image44| image:: ../../_static/集成手册/UDSonCAN/image44.png
   :width: 5.76458in
   :height: 2.43681in
.. |image45| image:: ../../_static/集成手册/UDSonCAN/image45.png
   :width: 5.76458in
   :height: 2.43681in
.. |image46| image:: ../../_static/集成手册/UDSonCAN/image46.png
   :width: 5.76458in
   :height: 2.43681in
.. |image47| image:: ../../_static/集成手册/UDSonCAN/image47.png
   :width: 5.76458in
   :height: 2.43681in
.. |image48| image:: ../../_static/集成手册/UDSonCAN/image48.png
   :width: 5.76458in
   :height: 2.43681in
.. |image49| image:: ../../_static/集成手册/UDSonCAN/image49.png
   :width: 5.76458in
   :height: 2.43681in
.. |image50| image:: ../../_static/集成手册/UDSonCAN/image50.png
   :width: 5.76458in
   :height: 2.43681in
.. |image51| image:: ../../_static/集成手册/UDSonCAN/image51.png
   :width: 5.76458in
   :height: 2.43681in
.. |image52| image:: ../../_static/集成手册/UDSonCAN/image52.png
   :width: 5.76458in
   :height: 2.43681in
.. |image53| image:: ../../_static/集成手册/UDSonCAN/image53.png
   :width: 5.76458in
   :height: 2.43681in
.. |image54| image:: ../../_static/集成手册/UDSonCAN/image54.png
   :width: 5.76458in
   :height: 2.43681in
.. |image55| image:: ../../_static/集成手册/UDSonCAN/image55.png
   :width: 5.76458in
   :height: 2.43681in
.. |image56| image:: ../../_static/集成手册/UDSonCAN/image56.png
   :width: 5.76458in
   :height: 2.43681in
.. |image57| image:: ../../_static/集成手册/UDSonCAN/image57.png
   :width: 5.76458in
   :height: 2.43681in
.. |image58| image:: ../../_static/集成手册/UDSonCAN/image58.png
   :width: 5.76458in
   :height: 2.43681in
.. |image59| image:: ../../_static/集成手册/UDSonCAN/image59.png
   :width: 5.76458in
   :height: 2.43681in
.. |image60| image:: ../../_static/集成手册/UDSonCAN/image60.png
   :width: 5.76458in
   :height: 2.43681in
.. |image61| image:: ../../_static/集成手册/UDSonCAN/image61.png
   :width: 5.76458in
   :height: 2.43681in
.. |image62| image:: ../../_static/集成手册/UDSonCAN/image62.png
   :width: 5.76458in
   :height: 2.43681in
.. |image63| image:: ../../_static/集成手册/UDSonCAN/image63.png
   :width: 5.76736in
   :height: 3.0625in
.. |image64| image:: ../../_static/集成手册/UDSonCAN/image64.png
   :width: 5.76458in
   :height: 2.43681in
.. |image65| image:: ../../_static/集成手册/UDSonCAN/image65.png
   :width: 5.76458in
   :height: 2.43681in
.. |image66| image:: ../../_static/集成手册/UDSonCAN/image66.png
   :width: 5.76458in
   :height: 2.43681in
.. |image67| image:: ../../_static/集成手册/UDSonCAN/image67.png
   :width: 5.76458in
   :height: 2.43681in
.. |image68| image:: ../../_static/集成手册/UDSonCAN/image68.png
   :width: 5.76458in
   :height: 2.43681in
.. |image69| image:: ../../_static/集成手册/UDSonCAN/image69.png
   :width: 5.76111in
   :height: 7.29514in
.. |image70| image:: ../../_static/集成手册/UDSonCAN/image70.png
   :width: 5.76667in
   :height: 3.02292in
.. |image71| image:: ../../_static/集成手册/UDSonCAN/image71.png
   :width: 5.7625in
   :height: 5.74167in
.. |image72| image:: ../../_static/集成手册/UDSonCAN/image72.png
   :width: 5.75764in
   :height: 3.72639in
.. |image_code_1| image:: ../../_static/集成手册/UDSonCAN/image_code_1.png
   :width: 5.75764in
.. |image_code_2| image:: ../../_static/集成手册/UDSonCAN/image_code_2.png
   :width: 5.75764in