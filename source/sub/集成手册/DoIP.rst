===================
DoIP_集成手册
===================





目标
====

本集成手册用于指导客户进行DoIP集成，文档主要包括的内容为：协议栈集成指导、基于普通应用的集成示例讲解、项目集成特殊说明。

由于各项目的需求不同，集成示例不会针对于特定的商业项目做详细讲解。

缩写词和术语
============

.. table:: 表 2‑1 缩写词和术语

   +---------------+------------------------------------------------------+
   |**缩写词/术语**| **描述**                                             |
   |               |                                                      |
   +---------------+------------------------------------------------------+
   | DoIP          | Diagnostic over IP基于IP的诊断                       |
   +---------------+------------------------------------------------------+
   | SoAd          | Socket Adapter Socket适配器                          |
   +---------------+------------------------------------------------------+
   | TcpIp         | Transmission Control Protocol/Internet               |
   |               | Protocol传输控制协议/网际协议                        |
   +---------------+------------------------------------------------------+
   | Dcm           | Diagnostic Communication Manager 诊断通信管理        |
   +---------------+------------------------------------------------------+
   | Dem           | Diagnostic Event Manager诊断时间管理                 |
   +---------------+------------------------------------------------------+

参考文档
========

[1] 参考手册_DoIP.pdf

[2] 参考手册_TCPIP.pdf

[3] 参考手册_DCM.pdf

[4] 参考手册_EthIf.pdf

[5] 参考手册_SoAd.pdf

[7] UDSonCAN.pdf

协议栈集成
==========

项目交付的内容为：DoIP协议栈源码和ORIENTAIS
Configurator配置工具。协议栈细分为协议栈的各模块及其对应的配置工具模块。

DoIP协议栈各配置模块的功能介绍，参见表 4‑1 DoIP协议栈各配置模块介绍。

使用协议栈源码和配置工具，进行协议栈的集成的步骤，参见
表 4‑2 DoIP协议栈集成的步骤。

.. table:: 表 4‑1 DoIP协议栈各配置模块介绍

   +---------+------------------------------------------------------------+
   | **模\   | **功能**                                                   |
   | 块名**  |                                                            |
   +---------+------------------------------------------------------------+
   | Eth     | ETH驱动配置。                                              |
   +---------+------------------------------------------------------------+
   | EthIf   | EthIf模块使用EthIfCtr                                      |
   |         | lIdx来抽象以太网收发器和控制器的底层通信系统对VLAN的访问， |
   |         | 以此以太网接口实现从EthCtrlIdx到各自硬件资源控制器的映射。 |
   +---------+------------------------------------------------------------+
   | EcuC    | 用于辅助配置工具完成配置的模块。主                         |
   |         | 要提供Pdu的定义，其它模块通过关联EcuC中Pdu，相互关联起来。 |
   +---------+------------------------------------------------------------+
   | PduR    | PduR模块用于Pdu在TP层和IF层的传输，为COM和DCM的下层        |
   +---------+------------------------------------------------------------+
   | TcpIp   | TcpIp模块作为以太网基本协议模块，提                        |
   |         | 供了发送和接收互联网协议数据的功能，处于SoAd和EthIf中间。  |
   +---------+------------------------------------------------------------+
   | SoAd    | S                                                          |
   |         | oAd模块使用PDU和socket在TCPIP栈之间创建接口，将Pdu与socket |
   |         | connection 形成映射关系.                                   |
   +---------+------------------------------------------------------------+
   | Dcm     | Dcm模块为DoIP提供诊断通讯管理                              |
   +---------+------------------------------------------------------------+
   | Dem     | Dem模块为DoIP提供诊断事件管理                              |
   +---------+------------------------------------------------------------+
   | DoIP    | DoIP即基于以太网的诊断，                                   |
   +---------+------------------------------------------------------------+

.. table:: 表 4‑2 DoIP协议栈集成的步骤

   +-----+--------------------------+------------------------------------+
   |**步\| **操作**                 | **说明**                           |
   |骤** |                          |                                    |
   |     |                          |                                    |
   |     |                          |                                    |
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

|image1|

图4-1 新建工程-1

2. 菜单栏File🡪New🡪Project，新建工程。

|image2|

图4-2 新建工程-2

3. 在弹出的新建窗口中选择Autosar下的 [BSW Project]，选择Next。

..

|image3|

图4-3 新建工程-3

4. 在弹出的窗口中输入工程名，选择Finish

|image4|

图4-4 新建工程-4

5. 选择[Bsw_Builder]，右键单击，选择New ECU Configuration。

|image5|

图4-5 新建工程-5

6. 在弹出的窗口中输入ECU名，然后选择Next。

|image6|

图4-6 新建工程-6

7. 选择[BSW_Builder]->选择目标ECU->右键单机选择[Add Module]。

|image7|

图 4‑7 新建工程-7

8. 在弹出的窗口中勾选需添加的模块，点击Finish。

|image8|

图4-8 新建工程-8

9. 新建工程如下所示，上一步添加的模块已经被加入到工程中。

|image9|

图4-9 新建工程-9

10. MCAL配置导入，BSW模块需要依赖MCAL生成的Eth模块

    a) 从MCAL配置工具生成arxml

..

   |image10|

图4-10 新建工程-10

|image11|

图4-11 新建工程-11

b) 导入BSW工具

..

   |image12|

图4-12 新建工程-12

|image13|

图4-13 新建工程-13

模块配置及生产代码
------------------

模块配置
~~~~~~~~

EcuC配置
~~~~~~~~~~~~~~

|image14|

图4-15 EcuC配置

新建源地址(Source address)和目标地址(Target
address)的数据类型，分别选择SOURCE_ADDRESS_16和TARGET_ADDRESS_16

|image15|

图4-16 Pdu配置

添加DoIP需要的Pdu

EthIf配置
~~~~~~~~~~~~~~

EthIfGeneral


|image16|

图4-17 EthIf配置-EthIfGeneral

EthIfConfigSet


|image17|

图4-18 EthIf配置-EthIfConfigSet

|image18|

图4-19 EthIf配置- EthIfConfigSet

添加以太网对应的帧类型，选择对应的EthIfOwner,这里Owner为上层模块编号，此处对应EthRxIndicationConfigs中的以太网报文接收回调函数。

Eth_DriverApiConfigSet


|image19|

图4-20 EthIf配置-Eth_DriverApiConfigSet

对Eth驱动中的代码原型进行映射，需参考MCAL源码进行修改，一些未使用的Api(如Timestamp功能)需改为NULL_PTR。如存在EthTrcv模块，同理在EthTrcv_DriverApiConfigSet中进行修改。

TcpIp配置
~~~~~~~~~~~~~~

TcpIpGeneral


使能IPv4(暂时只支持IPv4)

|image20|

图4-21 TcpIp配置-TcpIpGeneral

使能TCP和UDP，设置对应的最大socket数量。

|image21|

图4-22 TcpIp配置-TcpIpGeneral

TcpIpConfig


选择TcpIpIpConfig添加Arp配置

|image22|

图4-23 TcpIp配置-TcpIpConfig

TcpIpLocalAddrs 添加DoIP使用的IP地址

|image23|

图4-24 TcpIp配置-TcpIpConfig

TcpIpSocketOwnerConfigs


添加SoAd模块对应的接口Api

|image24|

图4-25 TcpIp配置-TcpIpConfig

TcpIpTcpConfig


|image25|

图4-26 TcpIp配置-TcpIpConfig

TcpIpUdpConfig


|image26|

图4-27 TcpIp配置-TcpIpConfig

SoAd配置
~~~~~~~~~~~~~~

SoAdBswModules


|image27|

图4-28 SoAd配置-SoAdBswModules

关联SoAd相关的Bsw模块

SoAdConfig


配置DoIP所需的SoAdPdu路由

|image28|

图4-29 SoAd配置-SoAdConfigs

添加SoAdSocketConnectionGroups，设置对应的本地port以及不同连接的远端地址

|image29|

图4-30 SoAd配置-SoAdConfigs

|image30|

图4-31 SoAd配置-SoAdConfigs

在SoAdPduRoutes中关联配置的SoAdSocketConnectionGroups

|image31|

图4-32 SoAd配置-SoAdConfigs

最后设置SoAdSocketRoutes

选择SoAdSocket路由对应的SCGroupConnection

|image32|

图4-33 SoAd配置-SoAdConfigs

配置对应的RouteDest

|image33|

图4-34 SoAd配置-SoAdConfigs

DoIP配置
~~~~~~~~

DoIPGeneral


设置DoIP相关的设置

|image34|

|image35|

图4-35 DoIP配置-DoIPGenerals

DoIPConfigSet


|image36|

图4-36 DoIP配置-DoIPConfigSets

设置DoIP的事件id，组id和逻辑地址.

|image37|

图4-37 DoIP配置-DoIPConfigSets

设置DoIP功能寻址和物理寻址的通道，选择通道在DoIP中的Role，以及对应的源地址和目标地址的参考点(在DoIPConnections中设置)，以及对应的接收发送Pdu.

|image38|

图4-38 DoIP配置-DoIPConfigSets

添加DoIPConnections中的DoIPTcp&UdpConnections，并分别配置对应的SoAd接收Pdu和发送Pdu，以及Udp连接到SoAd的组播(广播)连接Pdu。

|image39|

图4-39 DoIP配置-DoIPConfigSets

在DoIPConnections中设置DoIP的目标地址。

|image40|

图4-40 DoIP配置-DoIPConfigSets

在DoIPRoutingActivations中添加DoIPConnections中设置的DoIP目标地址参考点

|image41|

图4-41 DoIP配置-DoIPConfigSets

添加DoIP的诊断仪并选择对应的源地址，参考路由激活方式。

PduR配置
~~~~~~~~~~~~~~

PduRBswModules


|image42|

图4-42 PduR配置-PduRBswModules

添加PduR服务的Bsw模块，选择对应的PduRBswModulesRef后，工具将自动勾选所需Api

PduRoutingTables


|image43|

图4-43 PduR配置-PduRRoutingTables

PduR的路由表，在DoIP协议栈，需要配置以上路由，路由类型选择TP，选择路由中的目标Pdu(PduRDestPdus)和源Pdu(PduRSrcPdus)，同理添加功能寻址请求路由和响应路由。

ComM配置
~~~~~~~~

添加一路ComM的通道，后面Dcm模块需要用到这里

|image44|

图4-44 ComM配置-ComMConfigSet

Dcm配置
~~~~~~~

Dcm模块配置可参考《UDSonCAN.pdf》中Dcm的配置，ETH的诊断配置只需修改DcmDsl模块：

添加对应的ETH模块的buffer：

|image45|

图4-45 DCM配置-DCMConfigSets

添加DcmDslProtocol:

|image46|

图4-46 DCM配置-DCMConfigSets

Dem配置
~~~~~~~

请参考《UDSonCAN.pdf》

配置代码生成
~~~~~~~~~~~~

#. 在ORIENTAIS
   Configurator主界面左方，选择对应的协议栈，或者选择整个ECU，单击右键弹出Validate
   All和Generate All菜单。

|image47|

图4-47 配置代码的生成-1

2. 选择Validate
   All对本协议栈各配置选项进行校验，没有错误提示信息即校验通过。若有错误信息，请按照错误提示修改。

3. 选择Generate
   All，生成配置文件。右下角的Console窗口输出生成的配置文件信息。

|image48|

图4-48 配置代码的生成-2

4. 将ORIENTAIS Configurator切换到Resource模式，即可查看生成的配置文件。

|image49|

图4-49 配置代码的生成-3

功能集成
--------

代码集成
~~~~~~~~

协议栈代码包括两部分：项目提供的协议栈源码和ORIENTAIS
Configurator配置生成代码。

用户须将协议栈源码和章节4.2.2生成的源代码添加到集成开发工具的对应文件夹。协议栈集成的文件结构，见章节5.2。

**注意：协议栈集成之前，用户须确保已经有基础工程，且本协议栈相关的其他协议栈能正常工作。**

集成注意事项
~~~~~~~~~~~~

用户须提前配置好Eth的MCAL驱动，如果以太网通过中断完成接收发送，则在集成OS中前在OS中配置好相关的以太网中断。

集成示例
========

本章节通过DoIP协议栈为例，向用户展示DoIP协议栈的集成过程。用户可以据此熟悉DoIP协议栈配置工具的配置过程，以及如何应用配置工具生成的配置文件。

为让用户更清晰的了解工具的使用，所用的配置均逐一手动完成。关于Eth驱动的配置，请参考Eth配置手册。

**注意：本示例不代表用户的实际配置情况，用户需要根据自己的实际需求，决定各个参数的配置。**

集成目标
--------

DoIP集成完成后需根据以下示例测试：

DoIP诊断参数

表5-1 DoIP诊断参数

+----------------------+-----------------------------------------------+
|**参数**              |**值**                                         |
+----------------------+-----------------------------------------------+
| Local IP Address     | 192.168.1.19                                  |
+----------------------+-----------------------------------------------+
| Local Port           | 13400                                         |
+----------------------+-----------------------------------------------+
| Tester SA            | 0x0E88                                        |
+----------------------+-----------------------------------------------+
| 物理寻址TA           | 0x0040                                        |
+----------------------+-----------------------------------------------+
| 功能寻址TA           | 0xE400                                        |
+----------------------+-----------------------------------------------+
| ActiveLine           | 上电开启Active                                |
+----------------------+-----------------------------------------------+
| RoutingActiveNumber  | 0                                             |
+----------------------+-----------------------------------------------+
| DoIP Protocol        | 0x02                                          |
| Version              |                                               |
+----------------------+-----------------------------------------------+
| 诊断示例DID          | 0xF199（R：All                                |
|                      | Session，W：1003Session，Level1Security）     |
+----------------------+-----------------------------------------------+

DoIP报文示例

表5-2 DoIP诊断示例报文

+----------------------+-----------------------------------------------+
|**报文类型**          |**报文格式**                                   |
+----------------------+-----------------------------------------------+
| 路由激活请求         | 02 FD 00 05 00 00 00 07 0E 88 00 00 00 00 00  |
+----------------------+-----------------------------------------------+
| 物理寻址1003诊断请求 | 02 FD 80 01 00 00 00 06 0E 88 00 40 10 03     |
+----------------------+-----------------------------------------------+
| 功能寻址1003诊断请求 | 02 FD 80 01 00 00 00 06 0E 88 BB BB 10 03     |
+----------------------+-----------------------------------------------+
| 请求Level1 Seed      | 02 FD 80 01 00 00 00 06 0E 88 00 40 27 01     |
+----------------------+-----------------------------------------------+
| 发送Level1 Key       | 02 FD 80 01 00 00 00 0A 0E 88 00 40 27 02 11  |
|                      | 22 33 44                                      |
+----------------------+-----------------------------------------------+
| 写DID信息            | 02 FD 80 01 00 00 00 0B 0E 88 00 40 2E F1 99  |
|                      | 01 02 03 04                                   |
+----------------------+-----------------------------------------------+
| 读DID信息            | 02 FD 80 01 00 00 00 07 0E 88 00 40 22 F1 99  |
+----------------------+-----------------------------------------------+

源代码集成
----------

项目交付给用户的工程结构如下：

|image50|

图5-1 工程结构目录

-  ./BSW/Config/BSW_Config目录，这个目录用来存放ORIENTAIS
   Configurator配置工具生成的配置文件

-  ./BSW目录存放模块相关的源代码（除./BSW/Config目录之外）。可以看到Source目录下各个文件夹下是各个模块的源代码。

协议栈调度集成
--------------

DoIP协议栈调度集成步骤如下：

#. 协议栈调度集成。

#. 编译链接代码，将生成的elf文件烧写进芯片。

以下为示例代码：

**#include** "Mcu.h"

**#include** "Gpt.h"

**#include** "Eth_17_GEthMac.h"

**#include** "TcpIp.h"

**#include** "ComM.h"

**#include** "SoAd.h"

**#include** "Dem.h"

**#include** "Dcm.h"

**#include** "DoIP.h"

**void** **main** (**void**)

{

Eth_Init(&Eth_Config);

Eth_SetControllerMode(EthConf_EthCtrlConfig_EthCtrlConfig_0,
ETH_MODE_ACTIVE);

/\*\ *Eth*\ 外接\ *phy*\ 初始化*/

Eth_T_InitPhys();

EthIf_Init(&EthIf_ConfigData);

TcpIp_Init(&TcpIp_Config);

SoAd_Init(&SoAd_Config);

DoIP_Init(&DoIP_PBConfigPtr);

Dem_PreInit();

Dem_Init(&DemPbCfg);

Dcm_Init(&Dcm_Cfg);

**while**\ (1)

{

**if**\ (Gpt_1msFlag == TRUE)

{

/\*DoIPGeneral中选择DoIPHighFrequencyTaskSupport*/

DoIP_MainFunction_HighFrequency();

Gpt_1msFlag = FALSE;

}

**if**\ (Gpt_5msFlag == TRUE)

{

Gpt_5msFlag = FALSE;

}

**if**\ (Gpt_10msFlag == TRUE)

{

**if**\ ( TCPIP_STATE_ONLINE ==

   TcpIp_GetControlState(TcpIp_Config.CtrlPtr->EthIfCtrlRef ))

{

DoIP_ActivationLineSwitch();

}

Dcm_MainFunction();

Dem_MainFunction();

EcuM_MainFunction();

BswM_MainFunction();

TcpIp_MainFunction();

SoAd_MainFunction();

DoIP_MainFunction();

}

}

}

验证结果
--------

程序运行后使用网络调试助手发送以下指令验证DoIP诊断功能：

|图形用户界面, 文本, 应用程序 描述已自动生成|

图5-2 DoIP报文交互结果示例

22读 DID

2E 写DID

发送seed 27 01

发送key 27 02

物理寻址10 03

路由请求激活



.. |image1| image:: ../../_static/集成手册/DoIP/image1.png
   :width: 5.60345in
   :height: 3.71875in
.. |image2| image:: ../../_static/集成手册/DoIP/image2.png
   :width: 5.76667in
   :height: 3.82847in
.. |image3| image:: ../../_static/集成手册/DoIP/image3.png
   :width: 5.32292in
   :height: 5.13542in
.. |image4| image:: ../../_static/集成手册/DoIP/image4.png
   :width: 5.35694in
   :height: 4.55208in
.. |image5| image:: ../../_static/集成手册/DoIP/image5.png
   :width: 5.76458in
   :height: 3.82708in
.. |image6| image:: ../../_static/集成手册/DoIP/image6.png
   :width: 5.3125in
   :height: 5.125in
.. |image7| image:: ../../_static/集成手册/DoIP/image7.png
   :width: 5.76042in
   :height: 3.83125in
.. |image8| image:: ../../_static/集成手册/DoIP/image8.png
   :width: 3.55486in
   :height: 6.16597in
.. |image9| image:: ../../_static/集成手册/DoIP/image9.png
   :width: 3.84375in
   :height: 4.62292in
.. |image10| image:: ../../_static/集成手册/DoIP/image10.png
   :width: 4.75486in
   :height: 2.975in
.. |image11| image:: ../../_static/集成手册/DoIP/image11.png
   :width: 5.76319in
   :height: 4.34722in
.. |image12| image:: ../../_static/集成手册/DoIP/image12.png
   :width: 4.13056in
   :height: 3.27222in
.. |image13| image:: ../../_static/集成手册/DoIP/image13.png
   :width: 5.66667in
   :height: 5.11458in
.. |image14| image:: ../../_static/集成手册/DoIP/image14.png
   :width: 5.76042in
   :height: 1.98889in
.. |image15| image:: ../../_static/集成手册/DoIP/image15.png
   :width: 5.76458in
   :height: 3.03819in
.. |image16| image:: ../../_static/集成手册/DoIP/image16.png
   :width: 3.71574in
   :height: 4.74458in
.. |image17| image:: ../../_static/集成手册/DoIP/image17.png
   :width: 5.75694in
   :height: 2.56319in
.. |image18| image:: ../../_static/集成手册/DoIP/image18.png
   :width: 5.75903in
   :height: 2.49444in
.. |image19| image:: ../../_static/集成手册/DoIP/image19.png
   :width: 5.76111in
   :height: 2.925in
.. |image20| image:: ../../_static/集成手册/DoIP/image20.png
   :width: 5.75556in
   :height: 2.52292in
.. |image21| image:: ../../_static/集成手册/DoIP/image21.png
   :width: 5.7625in
   :height: 2.26181in
.. |image22| image:: ../../_static/集成手册/DoIP/image22.png
   :width: 5.75556in
   :height: 3.75486in
.. |image23| image:: ../../_static/集成手册/DoIP/image23.png
   :width: 5.75903in
   :height: 2.83403in
.. |image24| image:: ../../_static/集成手册/DoIP/image24.png
   :width: 5.76111in
   :height: 3.20417in
.. |image25| image:: ../../_static/集成手册/DoIP/image25.png
   :width: 5.76736in
   :height: 3.50556in
.. |image26| image:: ../../_static/集成手册/DoIP/image26.png
   :width: 5.76667in
   :height: 3.55in
.. |image27| image:: ../../_static/集成手册/DoIP/image27.png
   :width: 5.75556in
   :height: 2.34375in
.. |image28| image:: ../../_static/集成手册/DoIP/image28.png
   :width: 5.76597in
   :height: 2.75208in
.. |image29| image:: ../../_static/集成手册/DoIP/image29.png
   :width: 5.76111in
   :height: 2.99653in
.. |image30| image:: ../../_static/集成手册/DoIP/image30.png
   :width: 5.76667in
   :height: 2.57917in
.. |image31| image:: ../../_static/集成手册/DoIP/image31.png
   :width: 5.76528in
   :height: 2.68056in
.. |image32| image:: ../../_static/集成手册/DoIP/image32.png
   :width: 5.76597in
   :height: 2.40486in
.. |image33| image:: ../../_static/集成手册/DoIP/image33.png
   :width: 5.76458in
   :height: 2.41736in
.. |image34| image:: ../../_static/集成手册/DoIP/image34.png
   :width: 5.76389in
   :height: 2.99306in
.. |image35| image:: ../../_static/集成手册/DoIP/image35.png
   :width: 5.75417in
   :height: 3.22986in
.. |image36| image:: ../../_static/集成手册/DoIP/image36.png
   :width: 5.76181in
   :height: 2.07153in
.. |image37| image:: ../../_static/集成手册/DoIP/image37.png
   :width: 5.76528in
   :height: 2.14653in
.. |image38| image:: ../../_static/集成手册/DoIP/image38.png
   :width: 5.62205in
   :height: 2.6853in
.. |image39| image:: ../../_static/集成手册/DoIP/image39.png
   :width: 5.50041in
   :height: 2.64898in
.. |image40| image:: ../../_static/集成手册/DoIP/image40.png
   :width: 5.4958in
   :height: 2.41481in
.. |image41| image:: ../../_static/集成手册/DoIP/image41.png
   :width: 5.45976in
   :height: 1.99768in
.. |image42| image:: ../../_static/集成手册/DoIP/image42.png
   :width: 5.75972in
   :height: 3.46667in
.. |image43| image:: ../../_static/集成手册/DoIP/image43.png
   :width: 5.75694in
   :height: 2.32708in
.. |image44| image:: ../../_static/集成手册/DoIP/image44.png
   :width: 5.76458in
   :height: 2.77778in
.. |image45| image:: ../../_static/集成手册/DoIP/image45.png
   :width: 5.76667in
   :height: 2.38611in
.. |image46| image:: ../../_static/集成手册/DoIP/image46.png
   :width: 5.75625in
   :height: 2.87361in
.. |image47| image:: ../../_static/集成手册/DoIP/image47.png
   :width: 3.68657in
   :height: 3.76841in
.. |image48| image:: ../../_static/集成手册/DoIP/image48.png
   :width: 5.76319in
   :height: 1.75139in
.. |image49| image:: ../../_static/集成手册/DoIP/image49.png
   :width: 5.75972in
   :height: 2.22917in
.. |image50| image:: ../../_static/集成手册/DoIP/image50.png
   :width: 1.98472in
   :height: 3.65625in
.. |图形用户界面, 文本, 应用程序 描述已自动生成| image:: ../../_static/集成手册/DoIP/image51.png
   :width: 5.76736in
   :height: 5.17361in
