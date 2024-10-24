===================
UDSonLIN_集成手册
===================



 |
   |             | 应用软件                                               |
   +-------------+--------------------------------------------------------+
   | BSW         | Basic Software 基础软件                                |
   +-------------+--------------------------------------------------------+
   | MCAL        | Micro Controller Abstraction Layer 微控制器抽象层      |
   +-------------+--------------------------------------------------------+
   | LINIF       | LIN Interface Module LIN接口模块                       |
   +-------------+--------------------------------------------------------+
   | LINTP       | LIN Transport Layer Module LIN传输模块                 |
   +-------------+--------------------------------------------------------+
   | ComM        | Communication Manager Module 通信管理模块              |
   +-------------+--------------------------------------------------------+
   | EcuM        | ECU State Manager Module ECU状态管理模块               |
   +-------------+--------------------------------------------------------+
   | PduR        | PDU Router Module PDU路由器模块                        |
   +-------------+--------------------------------------------------------+
   | Dcm         | Diagnostic Communication Manager 诊断通信模块          |
   +-------------+--------------------------------------------------------+
   | Dem         | Diagnostic Event Manager 诊断事件管理模块              |
   +-------------+--------------------------------------------------------+

参考文档
========

[1]LinIf.pdf

[2]PduR.pdf

[3]Dcm.pdf

[4]Dem.pdf

协议栈集成
==========

项目交付的内容为：协议栈源码和ORIENTAIS
Configurator配置工具。协议栈细分为协议栈的各模块及其对应的配置工具模块。

协议栈各配置模块的功能介绍，参见表 4‑1协议栈各配置模块介绍。

使用协议栈源码和配置工具，进行协议栈的集成的步骤，参见表 4‑2
协议栈集成的步骤。

.. table:: 表 4‑1协议栈各配置模块介绍

   +---------+------------------------------------------------------------+
   | **模    | **功能**                                                   |
   | 块名**  |                                                            |
   +---------+------------------------------------------------------------+
   | Lin     | LIN驱动配置。(由EB工具导入，详见章节5.1.1)                 |
   +---------+------------------------------------------------------------+
   | LinIf   | LinIf模块主要处理上层模块与底层驱动的之间PD                |
   |         | U的传递，为上层模块提供统一的接口来管理不同的LIN硬件模块。 |
   +---------+------------------------------------------------------------+
   | EcuC    | 用于辅助配置工具完成配置的模块。主                         |
   |         | 要提供Pdu的定义，其它模块通过关联EcuC中Pdu，相互关联起来。 |
   +---------+------------------------------------------------------------+
   | PduR    | PDU                                                        |
   |         | Router主要为相关模块提供基于I-PDU的路由                    |
   |         | 服务。在UDSonLIN栈中，主要是提供LinTP与DCM之间的路由服务。 |
   +---------+------------------------------------------------------------+
   | Dcm     | 依据ISO15765-3和ISO14229-1标准                             |
   |         | 描述，实现诊断请求报文的解析，响应(正响应和负响应)与执行。 |
   +---------+------------------------------------------------------------+
   | Dem     | 实现诊断故障的存储与管理功能，                             |
   |         | 提供API接口供其他模块读取DTC和对应的冻结帧数据和扩展数据。 |
   +---------+------------------------------------------------------------+

.. table:: 表 4‑2 协议栈集成的步骤

   +-----+--------------------------+------------------------------------+
   | *   | **操作**                 | **说明**                           |
   | *步 |                          |                                    |
   | 骤  |                          |                                    |
   | **  |                          |                                    |
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

#. 安装ORIENTAIS Configurator软件后，双击软件图标打开软件。

.. figure:: ../../_static/集成手册/UDSonLIN/image1.png
   :width: 5.60884in
   :height: 4.10556in

   图 4‑1 主界面

2. 菜单栏File🡪New🡪Project，新建工程。

.. figure:: ../../_static/集成手册/UDSonLIN/image2.png
   :width: 5.76736in
   :height: 4.20417in

   图 4‑2 新建工程

3. 在弹出的新建窗口中选择Autosar下的 [BSW Project]，选择Next。

.. figure:: ../../_static/集成手册/UDSonLIN/image3.png
   :width: 5.50464in
   :height: 4.02222in

   图 4‑3 新建工程

4. 在弹出的窗口中输入工程名，选择Finish。

图 4‑4 输入工程名

5. 在弹出的窗口中选择Yes。

.. figure:: ../../_static/集成手册/UDSonLIN/image5.png
   :width: 3.90351in
   :height: 1.83118in

   图 4‑5 选择选项

6. 选择[Bsw_Builder]，右键单击，选择New ECU Configuration。

.. figure:: ../../_static/集成手册/UDSonLIN/image6.png
   :width: 5.76736in
   :height: 1.86944in

   图 4‑6 新建ECU

7. 在弹出的窗口中输入ECU名，然后选择Next。

.. figure:: ../../_static/集成手册/UDSonLIN/image7.png
   :width: 4.26287in
   :height: 4.09603in

   图 4‑7 选择MCU

8. 在弹出的窗口中勾选需添加的模块，点击Finish。

.. figure:: ../../_static/集成手册/UDSonLIN/image8.png
   :width: 3.00531in
   :height: 3.76541in

   图 4‑8 选择模块

9. 新建工程如下所示，步骤⑦中添加的模块已经被加入到工程中。

.. figure:: ../../_static/集成手册/UDSonLIN/image9.png
   :width: 5.76736in
   :height: 3.41181in

   图 4‑9 添加模块

模块配置及生产代码
------------------

模块配置
~~~~~~~~

模块的具体配置，取决于具体的项目需求。

.. table:: 表 4‑3协议栈各模块配置参考文档

   +--------+----------------------------------------+-------------------+
   | **     | **参考文档**                           | **说明**          |
   | 模块** |                                        |                   |
   +--------+----------------------------------------+-------------------+
   | Lin    | MCAL对应的Lin配置手册                  |                   |
   +--------+----------------------------------------+-------------------+
   | LinIf  | 参考手册LinIf.pdf                      |                   |
   +--------+----------------------------------------+-------------------+
   | Dcm    | 参考手册Dcm.pdf                        |                   |
   +--------+----------------------------------------+-------------------+
   | PduR   | 参考手册PduR.pdf                       |                   |
   +--------+----------------------------------------+-------------------+
   | Dem    | 参考手册Dem.pdf                        |                   |
   +--------+----------------------------------------+-------------------+

配置代码生成
~~~~~~~~~~~~

#. 在ORIENTAIS
   Configurator主界面左方，选择对应的协议栈，单击右键弹出Validate
   All和Generate All菜单。

.. figure:: ../../_static/集成手册/UDSonLIN/image10.png
   :width: 5.1168in
   :height: 3.07569in

   图 4‑10 检验验证

2. 选择Validate
   All对本协议栈各配置选项进行校验，没有错误提示信息即校验通过。若有错误信息，请按照错误提示修改。

3. 选择Generate
   All，生成配置文件。右下角的Console窗口输出生成的配置文件信息。

.. figure:: ../../_static/集成手册/UDSonLIN/image11.png
   :width: 5.78238in
   :height: 1.84541in

   图 4‑11 生成配置文件

4. 将ORIENTAIS Configurator切换到Resource模式，即可查看生成的配置文件。

.. figure:: ../../_static/集成手册/UDSonLIN/image12.png
   :width: 5.77049in
   :height: 2.45in

   图 4‑12 配置文件

功能集成
--------

代码集成 
~~~~~~~~~

协议栈代码包括两部分：项目提供的协议栈源码和ORIENTAIS
Configurator配置生成代码。

用户须将协议栈源码和章节4.2.2生成的源代码添加到集成开发工具的对应文件夹。协议栈集成的文件结构，见章节5.2。

**注意：协议栈集成之前，用户须确保已经有基础工程，且本协议栈相关的其他协议栈能正常工作。**

集成注意事项
~~~~~~~~~~~~

对于集成过程中，协议栈特殊要求和用户经常出现的问题，归类总结形成 表
4‑3-2-1协议栈集成约束清单。用户需逐一排查表中的约束项，以避免集成问题出现。

.. table:: 表 4‑4 协议栈集成约束清单

   +-----+---------+-----------------------------------------------------+
   | *   | *       | **约束限制**                                        |
   | *编 | *类别** |                                                     |
   | 号  |         |                                                     |
   | **  |         |                                                     |
   +-----+---------+-----------------------------------------------------+
   | **  | 中断    | 通                                                  |
   | 1** |         | 信栈有中断、轮询或混合三种工作模式。若选取中断或混  |
   |     |         | 合模式，用户需在OS配置对应的中断并填充中断服务API。 |
   +-----+---------+-----------------------------------------------------+
   | **  | 堆栈    | 用户需确保为任务堆栈和中断堆栈分配足够的堆栈空间。  |
   | 2** |         |                                                     |
   +-----+---------+-----------------------------------------------------+
   | **  | 头文件  | -  添加协议                                         |
   | 3** |         | 栈代码之后，用户需更新集成开发工具中的头文件路径。  |
   |     |         |                                                     |
   |     |         | -  调用协议栈API的源文件，需要包含协议栈的头文件。  |
   +-----+---------+-----------------------------------------------------+
   | **  | 初始化  | UDSonLIN的初始化顺序为：Lin_Init， LinIf_Init，     |
   | 4** |         | PduR_Init， LinTp_Init，Dcm \_Init，Dem_PreInit，   |
   |     |         | Dem_Init。                                          |
   +-----+---------+-----------------------------------------------------+
   | **  | 周      | Dcm_MainFunction，Dem_MainFun                       |
   | 5** | 期函数  | ction和LinIf_MainFunction需要被周期性任务函数调用。 |
   +-----+---------+-----------------------------------------------------+

集成示例
========

本章节通过普通的LIN诊断栈为例，向用户展示LIN诊断栈的集成过程。用户可以据此熟悉LIN诊断栈配置工具的配置过程，以及如何应用配置工具生成的配置文件。

为让用户更清晰的了解工具的使用，所用的配置均逐一手动完成。工具有配置文件（arxml文件）生成和导入功能，如果有配置好的arxml文件，用户可以使用工具中的arxml文件导入功能，快速完成配置。

**注意：本示例不代表用户的实际配置情况，用户需要根据自己的实际需求，决定各个参数的配置。**

集成目标

集成后的工程为从节点LIN，集成完成后的工程可以进行诊断服务

信号设置如下表所示：

.. table:: 表5-1

   +-------------------+-------+-----+---+-------------------------------+
   | **帧名称**        | *     | **I | * | **节点地址**                  |
   |                   | *帧类 | D** | * |                               |
   |                   | 型**  |     | T |                               |
   |                   |       |     | x |                               |
   |                   |       |     | \ |                               |
   |                   |       |     | \ |                               |
   |                   |       |     | R |                               |
   |                   |       |     | x |                               |
   |                   |       |     | * |                               |
   |                   |       |     | * |                               |
   +-------------------+-------+-----+---+-------------------------------+
   | **LinIf           | 诊    | 0   | R | **物理地址：0x51              |
   | Frame_MasterReq** | 断帧  | x3C | X | 功能地址：0x7e**              |
   +-------------------+-------+-----+---+-------------------------------+
   | **LinIf           | 诊    | 0   | T | **物理地址：0x51**            |
   | Frame_SlaveResp** | 断帧  | x3D | X |                               |
   +-------------------+-------+-----+---+-------------------------------+

模块的配置
----------

新建配置工程及模块加载操作，请参考本文档\ **4.2**\ 章节。

Lin模块配置
~~~~~~~~~~~

配置诊断协议栈之前需要使用 MCAL 工具配置 Lin
模块，但是只涉及到与诊断栈中报文收发有关系的部分（主要是
HardwareObeject）。该集成示例为从节点LIN，需要将LIN配置为从节点。具体配置选项请参考
MCAL工具的参考手册进行配置。

EcuC模块配置
~~~~~~~~~~~~

#. 双击EcuC模块，打开EcuC模块配置界面。

.. figure:: ../../_static/集成手册/UDSonLIN/image13.png
   :width: 4.94097in
   :height: 3.03889in

   图 5‑1 EcuC配置

2. 在EcucConfigSets栏目上右键，选择EcucConfigSet。再在EcucConfigSet上右键，选择New🡪EcucPduCollection。

.. figure:: ../../_static/集成手册/UDSonLIN/image14.png
   :width: 4.93194in
   :height: 3.07222in

   图 5‑2 EcucConfigSet

·PduLengthTypeEnum
选择UINT8（这个参数是定义存储数据长度时使用的变量的长度，示例需要配置的报文长度都是8，不会超过255，所以选择UINT8即可）

3. 在EcucPduCollection上右键，选择Pdu，会生成一个Pdu的配置界面。

.. figure:: ../../_static/集成手册/UDSonLIN/image15.png
   :width: 5.76736in
   :height: 3.40833in

   图 5‑3 新建Pdu

这里按照发送和接收，可以将Pdu名字改为报文的名字。LIN诊断需要配置6个Pdu，分别用于LinTp、Dcm。

.. figure:: ../../_static/集成手册/UDSonLIN/image15.png
   :width: 5.76736in
   :height: 3.40833in

   图 5‑4 配置Pdu

4. 为每个 Pdu 配置 Length（根据项目不同配置不同的 Pdu 长度）。

|image1|\ |image2|

图 5‑5 配置Pdu的Length

注意：Dcm Pdu 长度必须与/Dcm/DcmConfigSet/DcmDsl/DcmDslBuffer 里面配置的
Dcm Tx、RxBuffer长度一致。

LinIf模块配置
~~~~~~~~~~~~~

#. 双击LinIf模块，打开LinIf模块的配置界面。

.. figure:: ../../_static/集成手册/UDSonLIN/image18.png
   :width: 5.76736in
   :height: 6.41944in

   图 5‑6 LinIf配置

2. LinIfGeneral标签页打开LinIfTpSupported选项。

3. 在LinIfGlobalConfig标签页下依次打开LinIfGlobalConfigs
   ->LinIfGlobalConfig
   ->LinIfChannel_1->LinIfFrames新建LinFrame用于诊断请求。

.. figure:: ../../_static/集成手册/UDSonLIN/image19.png
   :width: 5.76736in
   :height: 3.41736in

   图 5‑7 新建LinFrame

4. 然后右击LinIfChannel_1新建LinFrame用于诊断响应。

.. figure:: ../../_static/集成手册/UDSonLIN/image20.png
   :width: 5.76736in
   :height: 3.42014in

   图 5‑8 新建响应报文

5. 进入LinTp配置页面，LinTpGeneral配置界面不需要配置

.. figure:: ../../_static/集成手册/UDSonLIN/image21.png
   :width: 5.76736in
   :height: 6.3125in

   图 5‑9 LinTpGeneral配置界面

6. 选择LinTpGlobalConfig标签，LinTpGlobalConfig->LinTpChannelConfigs新建一个LinTpChannelConfig。再关联对应的LinChannel和ComMChannel。

.. figure:: ../../_static/集成手册/UDSonLIN/image22.png
   :width: 5.76736in
   :height: 3.44931in

   图 5‑10 关联Channel

7. 选择LinTpRxNSdus新建物理地址的Sdu，根据需求配置对应的Ncr，NAD关联对应的LinChannel和ComMChannel

.. figure:: ../../_static/集成手册/UDSonLIN/image23.png
   :width: 5.76736in
   :height: 3.42847in

   图 5‑11 新建物理地址Sdu

8. 选择LinTpRxNSdus新建功能地址的Sdu，根据需求配置对应的Ncr，NAD关联对应的LinChannel和ComMChannel。

.. figure:: ../../_static/集成手册/UDSonLIN/image24.png
   :width: 5.76736in
   :height: 3.38819in

   图 5‑12 新建功能地址Sdu

9. 选择LinTpTxNSdus新建响应的Sdu，根据需求配置对应的Nas，Ncs，NAD，关联对应的LinChannel和ComMChannel。

.. figure:: ../../_static/集成手册/UDSonLIN/image25.png
   :width: 5.76736in
   :height: 3.43194in

   图 5‑13 新建响应Sdu

PduR模块配置
~~~~~~~~~~~~

#. 双击PduR模块，打开PduR模块的配置界面。在PduRBswModules中添加Dcm。

.. figure:: ../../_static/集成手册/UDSonLIN/image26.png
   :width: 5.76736in
   :height: 3.46458in

   图 5‑14 PduR模块配置

2. 打开PduRRoutingTables标签页，添加3个PduRRoutingPath。

.. figure:: ../../_static/集成手册/UDSonLIN/image27.png
   :width: 5.76736in
   :height: 6.59306in

   图 5‑15 添加PduRRoutingPath

3. 配置诊断功能寻址请求（FuncReq）、物理寻址请求（PhysReq）、响应（Resp）的路由路径。诊断请求的PduRRoutingPath的PduRSrcPdu选择LinTp对应的PDU，PduRDestPDU选择Dcm对应的PDU。诊断响应的PduRRoutingPath的则相反。

.. figure:: ../../_static/集成手册/UDSonLIN/image28.png
   :width: 5.76736in
   :height: 3.40139in

   图 5‑16 配置物理寻址路由

.. figure:: ../../_static/集成手册/UDSonLIN/image29.png
   :width: 5.76736in
   :height: 3.43194in

   图 5‑17 配置功能寻址路由

.. figure:: ../../_static/集成手册/UDSonLIN/image30.png
   :width: 5.76736in
   :height: 3.43194in

   图 5‑18 配置响应路由

Dcm模块配置
~~~~~~~~~~~

#. 双击Dcm模块，打开Dcm模块配置界面。DcmGeneral配置

.. figure:: ../../_static/集成手册/UDSonLIN/image31.png
   :width: 4.92425in
   :height: 4.07346in

   图 5‑19 DcmGeneral配置

2. 配置DcmDsl，先配置Dcm
   Tx、RxBuffer及其Length，需要与EcuC中Dcm对应的Pdu Length的值保持一致。

.. figure:: ../../_static/集成手册/UDSonLIN/image32.png
   :width: 5.76736in
   :height: 3.47639in

   图 5‑20 配置DcmDsl

3. 配置DcmDslProtocol，选择Protocol,Buffer,ServiceTable。

.. figure:: ../../_static/集成手册/UDSonLIN/image33.png
   :width: 5.76736in
   :height: 3.44028in

   图 5‑21 配置DcmDslProtocol

4. 配置DcmDslMainConnection，选择Dcm通信的ComMChannel，并新建2个DcmDslProtocolRx，1个DcmDslProtocolTx。

.. figure:: ../../_static/集成手册/UDSonLIN/image34.png
   :width: 5.76736in
   :height: 3.42569in

   图 5‑22 配置DcmDslMainConnection

5. 为每个DcmDslProtocolRx,DcmDslProtocolTx添加Dcm对应的PDU及寻址类型。

|image3| |image4| |image5|

图 5‑23 关联Pdu

6. 配置DcmDsdServiceTable，添加所需的服务及子服务，及其寻址方式、会话访问限制、安全级访问限制。

.. figure:: ../../_static/集成手册/UDSonLIN/image38.png
   :width: 5.76736in
   :height: 3.43194in

   图 5‑24 配置服务

7. 配置DcmDspSession，SessionLevel与10服务的子服务对应，P2及P2Star时间参数根据需求进行配置。

|image6|

|image7|

.. figure:: ../../_static/集成手册/UDSonLIN/image41.png
   :width: 5.76736in
   :height: 3.48542in

   图 5‑25 配置会话模式

.. figure:: ../../_static/集成手册/UDSonLIN/image42.png
   :width: 5.76736in
   :height: 3.47917in

   图 5‑26 配置非默认会话

8. 配置DcmDspSerurity，SecurityLevel与27服务的子服务对应，如2705、2706对应level3，2761、2762对应level31。

.. figure:: ../../_static/集成手册/UDSonLIN/image43.png
   :width: 5.76736in
   :height: 3.42569in

   图 5‑27 配置27服务

9. 配置DcmDspRoutines，其中DcmDspCommonAuthorizationRef配置为每个Routine的会话访问限制与安全级访问限制。

.. figure:: ../../_static/集成手册/UDSonLIN/image44.png
   :width: 5.76736in
   :height: 3.50347in

   图 5‑28 配置属性

10. Routine下的3个容器分别对应3101、3102、3103的子服务功能，可按需求选择配置，并且可在容器中配置子服务的IN/OUT参数类型及长度。

.. figure:: ../../_static/集成手册/UDSonLIN/image45.png
   :width: 5.76736in
   :height: 3.42569in

   图 5‑29 配置子服务

11. 配置DcmDspComControl，此项用于配置28服务控制通信的ComM channel。

.. figure:: ../../_static/集成手册/UDSonLIN/image46.png
   :width: 5.76736in
   :height: 2.98403in

   图 5‑30 配置ComM channel

12. 配置DcmDspDidInfos，此项为每个Did配置22服务可读或2E服务可写，以及相关的会话访问限制、安全级访问限制。

|image8|\ |image9|

图 5‑31 配置DcmDspDidInfos

13. 配置DcmDspDatas，为每个Did配置DcmDspDataUsePort、类型、长度（bit为单位），并按需求选择上一步配置的DcmDspDidInfos。

.. figure:: ../../_static/集成手册/UDSonLIN/image49.png
   :width: 5.76736in
   :height: 3.33958in

   图 5‑32 配置DidData

14. 配置DcmDspDid，配置Did的DcmDspDidIdentifier及DcmDspDidInfos。

.. figure:: ../../_static/集成手册/UDSonLIN/image50.png
   :width: 5.76736in
   :height: 3.37083in

   图 5‑33 配置DID

15. 配置DcmDspSignal，选择上一步DcmDspDatas中添加的配置。

.. figure:: ../../_static/集成手册/UDSonLIN/image51.png
   :width: 5.76736in
   :height: 3.45833in

   图 5‑34 配置DcmDspSignal

Dem模块配置
~~~~~~~~~~~

#. 根据需求配置DemGeneral，相关配置项的意义可参考Dem参考手册.pdf。

|image10| |image11|

图 5‑35 Dem配置

2. 配置DemDataElementClass，其中可配置DemInternalDataElement（Dem内部数据）及DemExternalCSDataElement。

|image12|

|image13|

.. figure:: ../../_static/集成手册/UDSonLIN/image56.png
   :width: 5.76736in
   :height: 2.625in

   图 5‑36 配置DemDataElementClass

3. 配置扩展数据Extended
   Data，需要配置DemExtendedDataRecordClass以及DemExtendedDataClass。

|image14|

.. figure:: ../../_static/集成手册/UDSonLIN/image58.png
   :width: 5.76736in
   :height: 2.63681in

   图 5‑37 配置扩展数据Extended Data

4. 配置冻结帧Freeze
   Frame，需要配置DemDidClass、DemFreezeFrameClass、DemFreezeFrameRecNumClass以及DemFreezeFrameRecordClass。

|image15|

|image16|

.. figure:: ../../_static/集成手册/UDSonLIN/image61.png
   :width: 5.76736in
   :height: 2.61458in

   图 5‑38 配置冻结帧Freeze Frame

5. 配置DemPrimaryMemory，配置Event存储的最大数量，一般与DTC数量保持一致，若DTC数量太大，可考虑采用Displacement策略，减少此存储数量。

.. figure:: ../../_static/集成手册/UDSonLIN/image62.png
   :width: 5.76736in
   :height: 2.61458in

   图 5‑39 配置DemPrimaryMemory

6. 配置DemDTCAttribute，选择上面几步配置中添加的配置项。

|image17|

.. figure:: ../../_static/集成手册/UDSonLIN/image64.png
   :width: 5.76736in
   :height: 2.61458in

   图 5‑40 配置DemDTCAttribute

7. 配置DemDebounceCounterBasedClass。

.. figure:: ../../_static/集成手册/UDSonLIN/image65.png
   :width: 5.76736in
   :height: 2.61458in

   图 5‑41 配置DemDebounceCounterBasedClass

8. 配置DemDebounceTimeBasedClass。

.. figure:: ../../_static/集成手册/UDSonLIN/image66.png
   :width: 5.76736in
   :height: 2.61458in

   图 5‑42 配置DemDebounceTimerBasedClass

9. 配置DemDTC，添加DTC Value，并选择DemDTCAttribute。

.. figure:: ../../_static/集成手册/UDSonLIN/image67.png
   :width: 5.76736in
   :height: 2.61458in

   图 5‑43 配置DemDTC

10. 配置DemEventParameter，选择Event类型、关联的DTC及操作循环等，并可根据需求配置是否添加Debounce以及Debounce
    Base。

|image18|

.. figure:: ../../_static/集成手册/UDSonLIN/image69.png
   :width: 5.76736in
   :height: 2.61458in

   图 5‑44 配置DemEventParameter

源代码集成
----------

诊断栈源代码集成步骤如下：

#. 在 MCAL 工程的基础上，同步 5.2.1 章添加的 Lin 模块配置文件。

#. 从基线中取出 4.3.1 章中相关的源代码添加到工程中。

#. 将在 4.2.2 章中 ORIENTAS 配置生成的诊断相关配置文件添加到工程中。

#. 添加相关头文件目录。

协议栈调度集成
--------------

诊断栈调度集成步骤如下：

#. 集成Dcm_Callout.c中Dcm_ResetTime、Dcm_GetTimeSpan函数。

..

   Dcm_Callout.c集成源码如下（本工程集成OS相关接口，如果项目中无OS，可使用FreeRTimer中的接口）：

#include "Dcm_Internal.h"

#include "UDS.h"

#include "DcmDsl_MsgManage.h"

#include "Dcm_CalloutBoot.h"

#include "FreeRTimer.h"

#define DCM_START_SEC_CODE

#include "Dcm_MemMap.h"

/\* Showing TM solution as an example \*/

/\* if not having TM, need to implement other methods for timing
functionality \*/

/\* PRQA S 3432++ \*/ /\* MISRA Rule 20.7 \*/

FUNC(void, DCM_CODE) Dcm_ResetTime(P2VAR(uint32, AUTOMATIC, DCM_VAR)
TimerPtr)

/\* PRQA S 3432-- \*/ /\* MISRA Rule 20.7 \*/

{

#if (DCM_TM == STD_ON)

Tm_PredefTimer100us32bitType Timer;

Timer.ui32RefTime = 0;

(void)Tm_ResetTimer100us32bit(&Timer);

\*TimerPtr = Timer.ui32RefTime / (uint32)10;

#else /\* DCM_TM == STD_ON \*/

DCM_UNUSED(TimerPtr);

\*TimerPtr = Frt_ReadOutMS();

#endif /\* DCM_TM == STD_ON \*/

}

#define DCM_STOP_SEC_CODE

#include "Dcm_MemMap.h"

#define DCM_START_SEC_CODE

#include "Dcm_MemMap.h"

/\* Showing TM solution as an example \*/

/\* if not having TM, need to implement other methods for timing
functionality \*/

/\* PRQA S 3432++ \*/ /\* MISRA Rule 20.7 \*/

FUNC(void, DCM_CODE) Dcm_GetTimeSpan(uint32 TimerPtr,P2VAR(uint32,
AUTOMATIC, DCM_VAR) TimeSpanPtr)

/\* PRQA S 3432-- \*/ /\* MISRA Rule 20.7 \*/

{

#if (DCM_TM == STD_ON)

Tm_PredefTimer100us32bitType Timer;

\*TimeSpanPtr = 0u;

Timer.ui32RefTime = TimerPtr \* (uint32)10;

(void)Tm_GetTimeSpan100us32bit(&Timer,TimeSpanPtr);

\*TimeSpanPtr = \*TimeSpanPtr / (uint32)10;

#else /\* DCM_TM == STD_ON \*/

DCM_UNUSED(TimerPtr);

DCM_UNUSED(TimeSpanPtr);

\*TimeSpanPtr = Frt_CalculateElapsedMS(TimerPtr);

#endif /\* DCM_TM == STD_ON \*/

}

#define DCM_STOP_SEC_CODE

#include "Dcm_MemMap.h"

2. 诊断栈调度集成，需要逐一排查并实现表 4- 5
   诊断栈集成约束清单所罗列的问题，以避免集成出现差错。

void Os1MSTask(void \*arg)

{

const TickType_t xDelay = BSW_SERVICE_TASK_FAST_PERIOD_MS;

for(;;)

{

n1MsCounter ++;

systick_Count ++;

n5MsCount ++;

Reset_MainFunction();

LinSM_MainFunction();

LinIf_MainFunction();

if(5 == n5MsCount)

{

n5MsCount = 0;

n5MsCounter ++;

ComM_MainFunction_ComMChannel_HUD();

Com_MainFunctionTx();

Com_MainFunctionRx();

}

vTaskDelay(xDelay);

}

}

void Os10MSTask(void \*arg)

{

const TickType_t xDelay = 2 \* BSW_SERVICE_TASK_PERIOD_MS;

for(;;)

{

n10MsCounter ++;

Dcm_MainFunction();

Dem_MainFunction();

NvM_MainFunction();

Fee_MainFunction();

Fls_MainFunction();

vTaskDelay(xDelay);

}

}

验证结果
--------

根据集成目标，共配置了3个报文，其中2个接收报文分别为诊断物理寻址及诊断功能寻址，1个发送报文为诊断响应。(验证设备为ZLGCANFD-400U，上位机为ZXDOC)

.. figure:: ../../_static/集成手册/UDSonLIN/image70.png
   :width: 5.76736in
   :height: 3.06181in

   图 5‑45 验证结果

图5-5-1

.. |image1| image:: ../../_static/集成手册/UDSonLIN/image16.png
   :width: 5.76736in
   :height: 3.39653in
.. |image2| image:: ../../_static/集成手册/UDSonLIN/image17.png
   :width: 5.76736in
   :height: 3.40556in
.. |image3| image:: ../../_static/集成手册/UDSonLIN/image35.png
   :width: 5.76736in
   :height: 3.46458in
.. |image4| image:: ../../_static/集成手册/UDSonLIN/image36.png
   :width: 5.76736in
   :height: 3.47014in
.. |image5| image:: ../../_static/集成手册/UDSonLIN/image37.png
   :width: 5.76736in
   :height: 3.47361in
.. |image6| image:: ../../_static/集成手册/UDSonLIN/image39.png
   :width: 5.76736in
   :height: 3.47361in
.. |image7| image:: ../../_static/集成手册/UDSonLIN/image40.png
   :width: 5.76736in
   :height: 3.45556in
.. |image8| image:: ../../_static/集成手册/UDSonLIN/image47.png
   :width: 5.77105in
   :height: 2.47561in
.. |image9| image:: ../../_static/集成手册/UDSonLIN/image48.png
   :width: 5.46513in
   :height: 2.61573in
.. |image10| image:: ../../_static/集成手册/UDSonLIN/image52.png
   :width: 5.76736in
   :height: 2.62292in
.. |image11| image:: ../../_static/集成手册/UDSonLIN/image53.png
   :width: 5.76736in
   :height: 2.62292in
.. |image12| image:: ../../_static/集成手册/UDSonLIN/image54.png
   :width: 5.76736in
   :height: 2.64722in
.. |image13| image:: ../../_static/集成手册/UDSonLIN/image55.png
   :width: 5.76736in
   :height: 2.81389in
.. |image14| image:: ../../_static/集成手册/UDSonLIN/image57.png
   :width: 5.76736in
   :height: 2.62847in
.. |image15| image:: ../../_static/集成手册/UDSonLIN/image59.png
   :width: 5.76736in
   :height: 2.62986in
.. |image16| image:: ../../_static/集成手册/UDSonLIN/image60.png
   :width: 5.76736in
   :height: 2.63194in
.. |image17| image:: ../../_static/集成手册/UDSonLIN/image63.png
   :width: 5.76736in
   :height: 2.61458in
.. |image18| image:: ../../_static/集成手册/UDSonLIN/image68.png
   :width: 5.76736in
   :height: 2.61458in
