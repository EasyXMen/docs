==============
Eth
==============

目标
====

本集成手册用于指导客户进行Eth通信栈集成，文档主要包括的内容为：协议栈集成指导、基于普通应用的集成示例讲解、项目集成特殊说明。

由于各项目的需求不同，集成示例不会针对于特定的商业项目做详细讲解。

缩写词和术语
============

.. table:: 表 缩写词和术语

   +-----------------+------------------------------------------------------+
   | **缩写词/术语** | **描述**                                             |
   +-----------------+------------------------------------------------------+
   | Eth             | Ethernet Driver以太网驱动程序                        |
   +-----------------+------------------------------------------------------+
   | EthIf           | Ethernet Interface以太网接口                         |
   +-----------------+------------------------------------------------------+
   | PduR            | PDU Router为通讯模块提供基于I-PDU的路由服务。        |
   +-----------------+------------------------------------------------------+
   | LdCom           | Large Data Communication 大数据通信模块              |
   +-----------------+------------------------------------------------------+
   | SoAd            | Socket Adapter 套接字适配模块                        |
   +-----------------+------------------------------------------------------+
   | TcpIp           | TCP/IP protocol module TCP/IP协议模块                |
   +-----------------+------------------------------------------------------+
   | MCAL            | Microcontroller Abstraction Layer 微控制器抽象层     |
   +-----------------+------------------------------------------------------+

参考文档
========

[1] 参考手册_EthIf.pdf

[2] 参考手册_EthSM.pdf

[3] 参考手册_TcpIp.pdf

[4] 参考手册_SoAd.pdf

[5] 参考手册_PduR.pdf

[6] 参考手册_LdCom.pdf

协议栈集成
==========

项目交付的内容为：Eth通信栈源码和ORIENTAIS
Studio配置工具。协议栈细分为协议栈的各模块及其对应的配置工具模块。

Eth通信栈各配置模块的功能介绍，参见表 Eth通信栈各配置模块介绍。

使用协议栈源码和配置工具，进行协议栈的集成的步骤，参见表
Eth通信栈集成的步骤。

.. table:: 表 Eth通信栈各配置模块介绍

   +------------+-------------------------------------------------------------------------------------------------------------------------------------------+
   | **模块名** | **功能**                                                                                                                                  |
   +------------+-------------------------------------------------------------------------------------------------------------------------------------------+
   | Eth        | ETH驱动配置。                                                                                                                             |
   +------------+-------------------------------------------------------------------------------------------------------------------------------------------+
   | EthIf      | EthIf模块使用EthIfCtrlIdx来抽象以太网收发器和控制器的底层通信系统对VLAN的访问，以此以太网接口实现从EthCtrlIdx到各自硬件资源控制器的映射。 |
   +------------+-------------------------------------------------------------------------------------------------------------------------------------------+
   | EcuC       | 用于辅助配置工具完成配置的模块。主要提供Pdu的定义，其它模块通过关联EcuC中Pdu，相互关联起来。                                              |
   +------------+-------------------------------------------------------------------------------------------------------------------------------------------+
   | PduR       | PduR模块用于Pdu在TP层和IF层的传输，为COM和DCM的下层                                                                                       |
   +------------+-------------------------------------------------------------------------------------------------------------------------------------------+
   | TcpIp      | TcpIp模块作为以太网基本协议模块，提供了发送和接收互联网协议数据的功能，处于SoAd和EthIf中间。                                              |
   +------------+-------------------------------------------------------------------------------------------------------------------------------------------+
   | SoAd       | SoAd模块使用PDU和socket在TCPIP栈之间创建接口，将Pdu与socket connection 形成映射关系.                                                      |
   +------------+-------------------------------------------------------------------------------------------------------------------------------------------+
   | LdCom      | LdCom模块                                                                                                                                 |
   +------------+-------------------------------------------------------------------------------------------------------------------------------------------+

.. table:: 表 Eth通信栈集成的步骤

   +----------+----------------------------------------+------------------------------------------------------+
   | **步骤** | **操作**                               | **说明**                                             |
   +----------+----------------------------------------+------------------------------------------------------+
   | 1        | ORIENTAIS                              | 若配置工具已经搭建，则仅需进行协议栈模块的加载操作。 |
   |          | Studio配置工具工程搭建和协议栈模块加载 |                                                      |
   +----------+----------------------------------------+------------------------------------------------------+
   | 2        | 模块配置及配置文件生成                 | NA                                                   |
   +----------+----------------------------------------+------------------------------------------------------+
   | 3        | 代码集成                               | 现有工程、协议栈源代码和配置生成文件的集成。         |
   +----------+----------------------------------------+------------------------------------------------------+
   | 4        | 验证测试                               | NA                                                   |
   +----------+----------------------------------------+------------------------------------------------------+

.. note::
   **协议栈集成之前，用户须确保已经有基础工程，且本协议栈相关的其他协议栈能正常工作。**

新建ORIENTAIS工程
-----------------

#. 安装ORIENTAIS Manager软件，Install
   SnapShot后双击Controller列名称打开软件。

   |image1|

   图 新建工程-1

#. 菜单栏File🡪New🡪Project，新建工程。

   |image2|

   图 新建工程-2

#. 在弹出的新建窗口中选择Autosar下的 [BSW Project]，选择Next。

   |image3|

   图 新建工程-3

#. 在弹出的窗口中输入工程名，选择Finish。

   |image4|

   图 新建工程-4

#. 选择[Bsw_Builder]，右键单击，选择New ECU Configuration。

   |image5|

   图 新建工程-5

#. 在弹出的窗口中输入ECU名，然后选择需要的芯片，点击Next。

   |image6|

   图 新建工程-6

#. 在弹出的窗口中勾选需添加的模块，点击Finish。

   |image7|

   图 新建工程-7

#. 新建工程如下所示，上一步添加的模块已经被加入到工程中。

   |image8|

   图 新建工程-8

#. MCAL配置导入，BSW模块需要依赖MCAL生成的Eth模块

   把MCAL配置工具生成的arxml导入BSW工具

   |image9|

   图 新建工程-9

   |image10|

   图 新建工程-10

   |image11|

   图 新建工程-11

配置文件生成
------------

模块配置
~~~~~~~~

模块的具体配置，取决于具体的项目需求。Eth通信栈各模块配置项的详细介绍，参见文档《参考手册_EthIf.pdf》、《参考手册_EthSM.pdf》、《参考手册_TcpIp.pdf》、《参考手册_SoAd.pdf》、《参考手册_LdCom.pdf》。

配置代码生成
~~~~~~~~~~~~

#. 在ORIENTAIS
   Stuido主界面左方，选择对应的协议栈，或者选择整个ECU，单击右键弹出Validate
   All和Generate All菜单。

   |image12|

   图 配置代码的生成-1

#. 选择Validate
   All对本协议栈各配置选项进行校验，没有错误提示信息即校验通过。若有错误信息，请按照错误提示修改。

#. 选择Generate
   All，生成配置文件。右下角的Console窗口输出生成的配置文件信息。

   |image13|

   图 配置代码的生成-2

#. 将ORIENTAIS Studio切换到Resource模式，即可查看生成的配置文件。

   |image14|

   图 配置代码的生成-3

功能集成
--------

代码集成
~~~~~~~~

协议栈代码包括两部分：项目提供的协议栈源码和ORIENTAIS
Studio配置生成代码。

用户须将协议栈源码和章节（配置代码生成）生成的源代码添加到集成开发工具的对应文件夹。协议栈集成的文件结构，见章节（源码集成）。

.. note::
   **协议栈集成之前，用户须确保已经有基础工程，且本协议栈相关的其他协议栈能正常工作。**

集成注意事项
~~~~~~~~~~~~

用户须提前配置好Eth的MCAL驱动，如果以太网通过中断完成接收发送，需验证发送、接收中断工作正常，如存在OS，则在OS中配置好相关的以太网中断，如无OS，则需手动挂载对应的中断函数并使能中断。

集成示例
========

本章节通过Eth通信栈为例，向用户展示Eth通信栈的集成过程。用户可以据此熟悉Eth通信栈配置工具的配置过程，以及如何应用配置工具生成的配置文件。

为让用户更清晰的了解工具的使用，所用的配置均逐一手动完成。关于Eth驱动的配置，请参考芯片厂商提供的Eth
MCAL配置手册。

.. note::
   **本示例不代表用户的实际配置情况，用户需要根据自己的实际需求，决定各个参数的配置。**

集成目标
--------

通过LdCom_Transmit实现Udp和Tcp(Server及Client)报文的发送。

.. table:: 表 Eth通信Socket信息

   +----------------+-----------------------------------------------------+
   | **Socket信息** | **值**                                              |
   +----------------+-----------------------------------------------------+
   | Udp            | 本地：192.168.0.200/UDP/65000                       |
   |                |                                                     |
   |                | 远端：192.168.0.123/UDP/10001                       |
   +----------------+-----------------------------------------------------+
   | Tcp Server     | 本地：192.168.0.200/TCP/65000                       |
   |                |                                                     |
   |                | 远端：0.0.0.0/TCP/0                                 |
   +----------------+-----------------------------------------------------+
   | Tcp Client     | 本地：192.168.0.200/TCP/55001                       |
   |                |                                                     |
   |                | 远端：192.168.0.123/TCP/20001                       |
   +----------------+-----------------------------------------------------+

.. _模块配置-1:

模块配置
--------

新建配置工程及模块加载操作，请参考本文档章节(配置文件生成)。

Eth驱动配置
~~~~~~~~~~~

Eth驱动配置为MCAL层配置，可以参考以下S32K148驱动进行配置。

|image15|

图 Eth配置-1

|image16|

图 Eth配置-2

EcuC配置
~~~~~~~~

#. 双击EcuC模块，打开EcuC模块配置界面。

#. 在EcucConfigSets栏目上右键，选择EcucConfigSet。再在EcucConfigSet上右键，选择New🡪
   EcucConfigSet。再在EcucPduCollections上右键，选择New
   EcucPduCollection。

   #. PduIdTypeEnum
      选择UINT16（该参数表示PDU的格式。因为示例只有16个PDU，PDU数不会超过65535，UINT16类型的长度就够存储了）

   #. PduLengthTypeEnum
      选择UINT16（该参数表示数据长度，示例需要配置的报文长度都是在1500以内，所以选择UINT16即可）

   |image17|

   图 配置EcucPduCollection

#. 在EcucPduCollection上右键，选择Pdu，会生成一个Pdu的配置界面。

   #. 建议不要使用默认生成的Pdu名字（如：Pdu_0），将Pdu名字改成有意义的名字对后续的配置过程将会有很大帮助。

   #. 这里按照发送和接收，可以将Pdu名字改为报文的名字。PduLength：Pdu长度，根据实际使用帧的长度设置。

   #. 添加SoAd和LdCom所需的Pdu，并根据客户端和服务端选择不同的Pdu长度。

   |image18|

   图 配置Pdu

#. ECUC模块到此配置结束。可以在模块上右键，然后选择校验，查看是否配置有错误。

#. 校验后提示窗口没有错误信息，即校验通过。

EthIf配置
~~~~~~~~~

#. 配置EthIfGeneral。

   |image19|

   图 配置EthIfGeneral

#. 在EthIfConfigSet中配置EthIfController。

   |image20|

   图 EthIfController配置

#. 添加以太网对应的帧类型，选择对应的EthIfOwner，这里Owner为上层模块编号，此处对应EthRxIndicationConfigs中的以太网报文接收回调函数。

   |image21|

   图 EthIfConfigSet配置

#. 在Eth_DriverApiConfigeSet对Eth驱动中的代码原型进行映射，需参考MCAL源码进行修改，一些未使用的Api(如Timestamp功能)需改为NULL_PTR。如存在EthTrcv模块，同理在EthTrcv_DriverApiConfigSet中进行修改。

   |image22|

   图 Eth_DriverApiConfigSet配置

#. 校验后提示窗口没有错误信息，即校验通过。

TcpIp配置
~~~~~~~~~

#. 配置TcpIpGeneral。

   #. 设置TcpIpMainFunctionPeriod，单位秒，代码中对应10ms执行一次TcpIp_MainFunction()；

   #. 使能TCP和UDP，设置对应的最大socket数量；

   |image23|

   图 TcpIpGeneral配置

#. 配置TcpIpIpV4General，使能IPv4(暂时只支持IPv4)。

   |image24|

   图 TcpIpIpV4General配置

#. 在TcpIpConfig配置页中新建TcpIpIpConfig，并在TcpIpIpConfig中添加Arp配置。

   |image25|

   图 TcpIpArpConfig配置

#. TcpIpCtrl中选择EthIf配置的映射接口。

   |image26|

   图 TcpIpCtrl配置-1

#. 添加TcpIp的IpV4设置，并选择对应的Arp配置。

   |image27|

   图 TcpIpCtrl配置-2

#. 设置TcpIp本地地址。

   #. TcpIpAssignmentTrigger选择TCPIP_AUTOMATIC。

      |image28|

      图 TcpIpAddrAssignment配置

   #. 在TcpIpLocalAddrs中添加IP地址设置。

      |image29|

      图 TcpIpStaticIpAddressConfig配置

#. 新建TcpIpSocketOwnerConfig，添加SoAd模块对应的接口Api。

   |image30|

   图 TcpIpSocketOwner配置

#. 在TcpIpTcpConfigs中添加TCP设置。

   |image31|

   图 TcpIpUdpConfig配置

#. 在TcpIpUdpConfig中添加UDP设置。

   |image32|

   图 TcpIpUdpConfig

#. 校验后提示窗口没有错误信息，即校验通过。

SoAd配置
~~~~~~~~

#. SoAdGeneral配置。

   #. 设置SoAdMainFunctionPeriod，单位秒，代码中对应10ms执行一次SoAd_MainFunction()；

   #. 配置SoAdRoutingGroupMax与SoAdSoConMax，设置SoAdRoutingGroup与SoAdSoCon的最大数量；

      |image33|

      图 SoAdGeneral配置

#. 在SoAdBswModules中关联SoAd相关的Bsw模块。

   |image34|

   图 SoAd配置-SoAdBswModules

#. SoAdSocketConnectionGroups中添加Udp Cilent Socket配置。

   #. 此处通过LdCom发送来执行TcpIp报文测试，暂时不使能SoAdPduHeaderEnable，同时也暂不配置对应的HeaderId.

   #. 使能SoAdSocketAutomaticSoConSetup，否则需在代码中手动通过SoAd_OpenSoCon()来使SoAd_SoConMode切换到SOAD_SOCON_ONLINE。

      |image35|

      图 UDP Client配置-SoAdSocketConnectionGroup

   #. 设置Udp发送的远端地址。

      |image36|

      图 UDP Client配置-SoAdSocketRemoteAddress

   #. 创建Udp的SoAdSoket时，SoAdSocketRemoteIpAddress和SoAdSocketRemotePort不可设置为0，SoAdSocketRemoteIpAddress需设置为对应本地以太网的地址。

      |image37|

      图 本地以太网设置IP地址

   #. 在SoAdSocketProtocols中添加对应协议。

      |image38|

      图 UDP Client配置-SoAdSocketProtocol

#. SoAdSocketConnectionGroups中添加Tcp Serve Socket配置。

   #. 此处暂不勾选SoAdSocketAutomaticSoConSetup，同时在代码中添加SoAd_OpenSoCon()，入参时选择对应的SoAdSocketConnectionGroup的SoAdSocketId。

      |image39|

      图 TCP Server配置-SoAdSocketConnectionGroup

   #. 设置TcpServer端的远端地址和Port，对于Tcp而言设置远端地址和Port为0.0.0.0，表示任意远端地址均可进行连接。

      |image40|

      图 TCP Server配置-SoAdSocketRemoteAddress

   #. 在SoAdSocketProtocols中添加对应协议。

      |image41|

      图 TCP Server配置-SoAdSocketTcp

#. SoAdSocketConnectionGroups中添加Tcp Client Socket配置。

   #. 同样此处暂不勾选SoAdSocketAutomaticSoConSetup。

      |image42|

      图 TCP Client配置-SoAdSocketConnectionGroup

   #. 添加对应TCP Client节点对应发送的远端地址与port。

      |image43|

      图 TCP Client配置-SoAdSocketRemoteAddress

   #. 在SoAdSocketProtocols中添加对应协议。

      |image44|

      图 TCP Client配置-SoAdSocketTcp

#. 新建SoAdRoutingGroup，勾选SoAdRoutingGroupIsEnabledAtInit，使能SoAdRoutingGroup。

   |image45|

   图 SoAdRoutingGroup配置

#. 配置SoAdPduRoute。

   #. 添加所需的SoAdPdu路由

      |image46|

      图 SoAdPduRoute配置

   #. 新建SoAdPduRouteDest，选择对应的SoAdTxSocketConnOrSocketConnBundleRef，并在SoAdTxRoutingGroupRef添加SoAdTxRoutingGroupRef。

   |image47|

   图 SoAdPduRouteDest配置

#. SoAdSocketRoutes配置。

   #. 添加所需的SoAdPdu路由，并在SoAdRxSocketConnOrSocketConnBundleRef选择对应的SCGroupConnection。

      |image48|

      图 SoAdSocketRoute配置

   #. 新建SoAdSocketRouteDest，

      |image49|

      图 SoAdSocketRouteDest配置

#. 校验后提示窗口没有错误信息，即校验通过。

PduR配置
~~~~~~~~

#. PduRBswModules配置，添加PduR服务的Bsw模块，选择对应的PduRBswModulesRef后自动勾选Api。

   |image50|

   图 PduRBswModules

#. PduR的路由表，配置以上路由，路由类型选择IF。

   |image51|

   图 PduRRoutingTables

#. 选择路由中的目标Pdu(PduRDestPdus)和源Pdu(PduRSrcPdus)，同理添加UDP、TCP的客户端和服务端的Pdu路由。

   |image52|

   图 PduRDestPdu配置

   |image53|

   图 PduRSrcPdu配置

#. 校验后提示窗口没有错误信息，即校验通过。

LdCom配置
~~~~~~~~~

#. 配置LdComGeneral，选择Det和版本信息Api和LdCom回调头文件。

   |image54|

   图 LdComGeneral配置

#. 配置LdComConfig，选择LdComApi类型LDCOM_IF，通信路由方向选择发送报文选择LDCOM_SEND、接收报文选择LDCOM_RECEIVE；添加对应发送或接收的TxComfirmation
   / RxIndication；最后选择PduR中配置的Pdu路由。

   |image55|

   图 LdComConfig配置

.. note::
   Ldcom配置的TxComfirmation / RxIndication回调函数需要用户自定义。

源码集成
--------

项目交付给用户的工程结构如下：

|image56|

图 工程结构目录

- Config目录，这个目录用来存放配置工具生成的配置文件

- Source目录，存放模块相关的源代码。可以看到Source目录下各个文件夹下是各个模块的源代码。

调度集成
--------

Eth通信栈调度集成步骤如下：

#. 以太网驱动集成验证工作正常。

#. 若存在外接的以太网Phy，无法建立以太网连接时需考虑添加对应的Phy驱动代码。

#. 按（模块配置）中的内容，配置并集成Eth通信栈代码。

#. 编译链接代码，将生成的elf文件烧写进芯片。

Eth通信有关的代码，在下方的main.c文件中给出重点标注。

.. note::
   本示例中，Eth通信相关代码置于main.c文件，并不代表其他项目同样适用于将其置于main.c文件中。

.. code-block:: c
   :linenos:
   :emphasize-lines: 4-8, 13, 22-30, 37-38, 40-42, 45-47

   #include "UserTimer.h"

   // Eth通信协议相关模块头文件
   #include "EthIf.h"
   #include "TcpIp.h"
   #include "SoAd.h"
   #include "EthSM.h"
   #include "LdCom.h"

   // 定义LdCom发送的Pdu
   int main(void)
   {
       uint8 LdComSrcPduData[10] = {0x0,0x1,0x2,0x3,0x4,0x5,0x6,0x7,0x8,0x9};
       PduInfoType LdComTransmitPdu;
       LdComTransmitPdu.SduDataPtr = LdComSrcPduData;
       LdComTransmitPdu.SduLength = 10;
       LdComTransmitPdu.MetaDataPtr = NULL_PTR;

       UserTimer_Init();

       // Eth通信协议相关模块初始化
       Eth_Init(&Eth_Config);
       Eth_SetControllerMode(EthConf_EthCtrlConfig_EthCtrlConfig_0, ETH_MODE_ACTIVE);
       Eth_T_InitPhys();
       EthIf_Init(&EthIf_ConfigData);
       TcpIp_Init(&TcpIp_Config);
       SoAd_Init(&SoAd_Config);
       SoAd_OpenSoCon(1);
       SoAd_OpenSoCon(2);
       LdCom_Init(&LdCom_InitCfgSet);

       while(1)
       {
           // TcpIp、SoAd模块周期处理函数（10ms周期）
           if(Gpt_10msFlag == TRUE)
           {
               TcpIp_MainFunction();
               SoAd_MainFunction();
               Gpt_10msFlag = FALSE;
           }

           // LdCom模块Pdu发送（50ms周期）
           if(Gpt_50msFlag == TRUE)
           {
               LdCom_Transmit(LdComIPdu_Client_Tcp_Tx,&LdComTransmitPdu);
               LdCom_Transmit(LdComIPdu_Server_Udp_Tx,&LdComTransmitPdu);
               LdCom_Transmit(LdComIPdu_Server_Tcp_Tx,&LdComTransmitPdu);
               Gpt_50msFlag = FALSE;
           }
       }
       return 0;
   }

验证结果
--------

#. 在wireshark中监控到对应50ms周期发送的UDP报文。

   |image57|

   图 UDP报文示例

#. 使用网络调试助手，作为TCP Client创建连接后可以监控到对应的TCP
   Client报文。

   |image58|

   图 TCP Client 报文示例

#. 使用网络调试助手，作为TCP Server创建连接后可以监控到对应的TCP
   Server报文。

   |image59|

   图 TCP Sever 报文示例

.. |image1| image:: /_static/集成手册/集成手册_Eth/image2.png
   :width: 5.76736in
   :height: 2.9125in


.. |image2| image:: /_static/集成手册/集成手册_Eth/image3.png
   :width: 5.76736in
   :height: 2.9125in


.. |image3| image:: /_static/集成手册/集成手册_Eth/image4.png
   :width: 5.76736in
   :height: 2.9125in


.. |image4| image:: /_static/集成手册/集成手册_Eth/image5.png
   :width: 5.76736in
   :height: 2.9125in


.. |image5| image:: /_static/集成手册/集成手册_Eth/image6.png
   :width: 5.76736in
   :height: 2.9125in


.. |image6| image:: /_static/集成手册/集成手册_Eth/image7.png
   :width: 5.76736in
   :height: 3.9125in


.. |image7| image:: /_static/集成手册/集成手册_Eth/image8.png
   :width: 5.76736in
   :height: 6.9125in


.. |image8| image:: /_static/集成手册/集成手册_Eth/image9.png
   :width: 5.76736in
   :height: 3.2125in


.. |image9| image:: /_static/集成手册/集成手册_Eth/image10.png
   :width: 5.76736in
   :height: 2.9125in


.. |image10| image:: /_static/集成手册/集成手册_Eth/image11.png
   :width: 5.76736in
   :height: 2.9125in


.. |image11| image:: /_static/集成手册/集成手册_Eth/image12.png
   :width: 5.76736in
   :height: 4.9125in


.. |image12| image:: /_static/集成手册/集成手册_Eth/image13.png
   :width: 5.76736in
   :height: 4.9125in


.. |image13| image:: /_static/集成手册/集成手册_Eth/image14.png
   :width: 5.76736in
   :height: 2.9125in


.. |image14| image:: /_static/集成手册/集成手册_Eth/image15.png
   :width: 7.76736in
   :height: 4.9125in


.. |image15| image:: /_static/集成手册/集成手册_Eth/image16.png
   :width: 9.76736in
   :height: 3.4825in


.. |image16| image:: /_static/集成手册/集成手册_Eth/image17.png
   :width: 6.96736in
   :height: 2.9125in


.. |image17| image:: /_static/集成手册/集成手册_Eth/image18.png
   :width: 9.76736in
   :height: 1.4825in

.. |image18| image:: /_static/集成手册/集成手册_Eth/image19.png
   :width: 5.76736in
   :height: 2.9125in


.. |image19| image:: /_static/集成手册/集成手册_Eth/image20.png
   :width: 5.76736in
   :height: 2.9125in


.. |image20| image:: /_static/集成手册/集成手册_Eth/image21.png
   :width: 5.76736in
   :height: 2.9125in


.. |image21| image:: /_static/集成手册/集成手册_Eth/image22.png
   :width: 5.76736in
   :height: 2.9125in


.. |image22| image:: /_static/集成手册/集成手册_Eth/image23.png
   :width: 5.76736in
   :height: 2.9125in


.. |image23| image:: /_static/集成手册/集成手册_Eth/image24.png
   :width: 5.76736in
   :height: 2.9125in


.. |image24| image:: /_static/集成手册/集成手册_Eth/image25.png
   :width: 5.76736in
   :height: 2.9125in


.. |image25| image:: /_static/集成手册/集成手册_Eth/image26.png
   :width: 5.76736in
   :height: 2.9125in


.. |image26| image:: /_static/集成手册/集成手册_Eth/image27.png
   :width: 5.76736in
   :height: 2.9125in


.. |image27| image:: /_static/集成手册/集成手册_Eth/image28.png
   :width: 5.76736in
   :height: 2.9125in


.. |image28| image:: /_static/集成手册/集成手册_Eth/image29.png
   :width: 5.76736in
   :height: 2.9125in


.. |image29| image:: /_static/集成手册/集成手册_Eth/image30.png
   :width: 5.76736in
   :height: 2.9125in


.. |image30| image:: /_static/集成手册/集成手册_Eth/image31.png
   :width: 5.76736in
   :height: 2.9125in


.. |image31| image:: /_static/集成手册/集成手册_Eth/image32.png
   :width: 5.76736in
   :height: 2.9125in


.. |image32| image:: /_static/集成手册/集成手册_Eth/image33.png
   :width: 5.76736in
   :height: 2.9125in


.. |image33| image:: /_static/集成手册/集成手册_Eth/image34.png
   :width: 5.76736in
   :height: 2.9125in


.. |image34| image:: /_static/集成手册/集成手册_Eth/image35.png
   :width: 5.76736in
   :height: 2.9125in


.. |image35| image:: /_static/集成手册/集成手册_Eth/image36.png
   :width: 5.76736in
   :height: 2.9125in


.. |image36| image:: /_static/集成手册/集成手册_Eth/image37.png
   :width: 5.76736in
   :height: 2.9125in


.. |image37| image:: /_static/集成手册/集成手册_Eth/image38.png
   :width: 5.76736in
   :height: 2.9125in


.. |image38| image:: /_static/集成手册/集成手册_Eth/image39.png
   :width: 5.76736in
   :height: 2.9125in


.. |image39| image:: /_static/集成手册/集成手册_Eth/image40.png
   :width: 5.76736in
   :height: 2.9125in


.. |image40| image:: /_static/集成手册/集成手册_Eth/image41.png
   :width: 5.76736in
   :height: 2.9125in


.. |image41| image:: /_static/集成手册/集成手册_Eth/image42.png
   :width: 5.76736in
   :height: 2.9125in


.. |image42| image:: /_static/集成手册/集成手册_Eth/image43.png
   :width: 5.76736in
   :height: 2.9125in


.. |image43| image:: /_static/集成手册/集成手册_Eth/image44.png
   :width: 5.76736in
   :height: 2.9125in


.. |image44| image:: /_static/集成手册/集成手册_Eth/image45.png
   :width: 5.76736in
   :height: 2.9125in


.. |image45| image:: /_static/集成手册/集成手册_Eth/image46.png
   :width: 5.76736in
   :height: 2.9125in


.. |image46| image:: /_static/集成手册/集成手册_Eth/image47.png
   :width: 5.76736in
   :height: 2.9125in


.. |image47| image:: /_static/集成手册/集成手册_Eth/image48.png
   :width: 5.76736in
   :height: 2.9125in


.. |image48| image:: /_static/集成手册/集成手册_Eth/image49.png
   :width: 5.76736in
   :height: 2.9125in


.. |image49| image:: /_static/集成手册/集成手册_Eth/image50.png
   :width: 5.76736in
   :height: 2.9125in


.. |image50| image:: /_static/集成手册/集成手册_Eth/image51.png
   :width: 5.76736in
   :height: 2.9125in


.. |image51| image:: /_static/集成手册/集成手册_Eth/image52.png
   :width: 5.76736in
   :height: 2.9125in


.. |image52| image:: /_static/集成手册/集成手册_Eth/image53.png
   :width: 5.76736in
   :height: 2.9125in


.. |image53| image:: /_static/集成手册/集成手册_Eth/image54.png
   :width: 5.76736in
   :height: 2.9125in


.. |image54| image:: /_static/集成手册/集成手册_Eth/image55.png
   :width: 5.76736in
   :height: 2.9125in


.. |image55| image:: /_static/集成手册/集成手册_Eth/image56.png
   :width: 5.76736in
   :height: 2.9125in


.. |image56| image:: /_static/集成手册/集成手册_Eth/image57.png
   :width: 4.76736in
   :height: 5.9125in


.. |image57| image:: /_static/集成手册/集成手册_Eth/image58.png
   :width: 5.76736in
   :height: 2.9125in


.. |image58| image:: /_static/集成手册/集成手册_Eth/image59.png
   :width: 5.76736in
   :height: 2.9125in


.. |image59| image:: /_static/集成手册/集成手册_Eth/image60.png
   :width: 5.76736in
   :height: 2.9125in
