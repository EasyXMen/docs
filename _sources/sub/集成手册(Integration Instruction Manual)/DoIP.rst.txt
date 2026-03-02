==============
DoIP
==============

目标
====

本集成手册用于指导客户进行DoIP集成，文档主要包括的内容为：协议栈集成指导、基于普通应用的集成示例讲解、项目集成特殊说明。

由于各项目的需求不同，集成示例不会针对于特定的商业项目做详细讲解。

缩写词和术语
============

.. table:: 表 缩写词和术语

   +-----------------+------------------------------------------------------+
   | **缩写词/术语** | **描述**                                             |
   +=================+======================================================+
   | DoIP            | Diagnostic over IP基于IP的诊断                       |
   +-----------------+------------------------------------------------------+
   | SoAd            | Socket Adapter Socket适配器                          |
   +-----------------+------------------------------------------------------+
   | TcpIp           | Transmission Control Protocol/Internet               |
   |                 | Protocol传输控制协议/网际协议                        |
   +-----------------+------------------------------------------------------+
   | Dcm             | Diagnostic Communication Manager 诊断通信管理        |
   +-----------------+------------------------------------------------------+
   | Dem             | Diagnostic Event Manager诊断时间管理                 |
   +-----------------+------------------------------------------------------+
   | BswM            | Basic Software Mode Manager 基础软件模式管理器       |
   +-----------------+------------------------------------------------------+
   | Rte             | Runtime Environment 运行时环境                       |
   +-----------------+------------------------------------------------------+
   | iRte            | i-Soft Runtime Environment 普华基础模块运行时环境    |
   +-----------------+------------------------------------------------------+

参考文档
========

[1] 参考手册_DoIP.pdf

[2] 参考手册_TCPIP.pdf

[3] 参考手册_DCM.pdf

[4] 参考手册_EthIf.pdf

[5] 参考手册_SoAd.pdf

[7] 集成手册_UDSonCAN.pdf

协议栈集成
==========

项目交付的内容为：DoIP协议栈源码和ORIENTAIS
Studio配置工具。协议栈细分为协议栈的各模块及其对应的配置工具模块。

DoIP协议栈各配置模块的功能介绍，参见表 DoIP协议栈各配置模块介绍。

使用协议栈源码和配置工具，进行协议栈的集成的步骤，参见

表 DoIP协议栈集成的步骤。

.. table:: 表 DoIP协议栈各配置模块介绍

   +------------+-----------------------------------------------------------------------------------------------------------------------------------------+
   | **模块名** |                                                                 **功能**                                                                |
   +------------+-----------------------------------------------------------------------------------------------------------------------------------------+
   | Eth        | ETH驱动配置                                                                                                                             |
   +------------+-----------------------------------------------------------------------------------------------------------------------------------------+
   | EthIf      | EthIf模块使用EthIfCtrlIdx来抽象以太网收发器和控制器的底层通信系统对VLAN的访问，以此以太网接口实现从EthCtrlIdx到各自硬件资源控制器的映射 |
   +------------+-----------------------------------------------------------------------------------------------------------------------------------------+
   | EcuC       | 用于辅助配置工具完成配置的模块。主要提供Pdu的定义，其它模块通过关联EcuC中Pdu，相互关联起来                                              |
   +------------+-----------------------------------------------------------------------------------------------------------------------------------------+
   | PduR       | PduR模块用于Pdu在TP层和IF层的传输，为COM和DCM的下层                                                                                     |
   +------------+-----------------------------------------------------------------------------------------------------------------------------------------+
   | TcpIp      | TcpIp模块作为以太网基本协议模块，提供了发送和接收互联网协议数据的功能，处于SoAd和EthIf中间                                              |
   +------------+-----------------------------------------------------------------------------------------------------------------------------------------+
   | SoAd       | SoAd模块使用PDU和socket在TCPIP栈之间创建接口，将Pdu与socket connection 形成映射关系                                                     |
   +------------+-----------------------------------------------------------------------------------------------------------------------------------------+
   | Dcm        | Dcm模块为DoIP提供诊断通讯管理                                                                                                           |
   +------------+-----------------------------------------------------------------------------------------------------------------------------------------+
   | Dem        | Dem模块为DoIP提供诊断事件管理                                                                                                           |
   +------------+-----------------------------------------------------------------------------------------------------------------------------------------+
   | DoIP       | DoIP即基于以太网的诊断                                                                                                                  |
   +------------+-----------------------------------------------------------------------------------------------------------------------------------------+

.. table:: 表 DoIP协议栈集成的步骤

   +----------+----------------------------------------+------------------------------------------------------+
   | **步骤** | **操作**                               | **说明**                                             |
   +==========+========================================+======================================================+
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

新建ORIENTAIS Studio配置工程及模块加载
--------------------------------------

#. 安装ORIENTAIS Studio软件后，双击软件图件并设置workspace。

   |image1|

   图 新建工程-1

#. 菜单栏File🡪New🡪Project，新建工程。

   |image2|

   图 新建工程-2

#. 在弹出的新建窗口中选择Autosar下的 [BSW Project]，选择Next。

   |image3|

   图 新建工程-3

#. 在弹出的窗口中输入工程名，选择Finish

   |image4|

   图 新建工程-4

#. 选择[Bsw_Builder]，右键单击，选择New ECU Configuration。

   |image5|

   图 新建工程-5

#. 在弹出的窗口中输入ECU名，然后选择Next。

   |image6|

   图 新建工程-6

#. 选择[BSW_Builder]->选择目标ECU->右键单机选择[Add Module]。

   |image7|

   图 新建工程-7

#. 在弹出的窗口中勾选需添加的模块，点击Finish。

   |image8|

   图 新建工程-8

#. 新建工程如下所示，上一步添加的模块已经被加入到工程中。

   |image9|

   图 新建工程-9

#. MCAL配置导入，BSW模块需要依赖MCAL生成的Eth模块

   #. 从MCAL配置工具生成arxml
    
      |image10|

      图 新建工程-10

      |image11|

      图 新建工程-11

   #. 导入BSW工具

      |image12|

      图 新建工程-12

      |image13|

      图 新建工程-13

模块配置及生产代码
------------------

模块配置
~~~~~~~~

EcuC配置
~~~~~~~~~~~~~~

|image14|

图 EcuC配置

新建源地址(Source address)和目标地址(Target
address)的数据类型，分别选择SOURCE_ADDRESS_16和TARGET_ADDRESS_16

|image15|

图 Pdu配置

添加DoIP需要的Pdu

EthIf配置
~~~~~~~~~~~~~~

EthIfGeneral
'''''''''''''

|image16|

图 EthIf配置-EthIfGeneral

EthIfConfigSet
'''''''''''''''

|image17|

图 EthIf配置-EthIfConfigSet

|image18|

图 EthIf配置- EthIfConfigSet

添加以太网对应的帧类型，选择对应的EthIfOwner,这里Owner为上层模块编号，此处对应EthRxIndicationConfigs中的以太网报文接收回调函数。

Eth_DriverApiConfigSet
'''''''''''''''''''''''

|image19|

图 EthIf配置-Eth_DriverApiConfigSet

对Eth驱动中的代码原型进行映射，需参考MCAL源码进行修改，一些未使用的Api(如Timestamp功能)需改为NULL_PTR。如存在EthTrcv模块，同理在EthTrcv_DriverApiConfigSet中进行修改。

TcpIp配置
^^^^^^^^^^

TcpIpGeneral
'''''''''''''

使能IPv4(暂时只支持IPv4)

|image20|

图 TcpIp配置-TcpIpGeneral

   使能TCP和UDP，设置对应的最大socket数量。

|image21|

图 TcpIp配置-TcpIpGeneral

TcpIpConfig
''''''''''''

   选择TcpIpIpConfig添加Arp配置

|image22|

图 TcpIp配置-TcpIpConfig

TcpIpLocalAddrs 添加DoIP使用的IP地址

|image23|

图 TcpIp配置-TcpIpConfig

TcpIpSocketOwnerConfigs
'''''''''''''''''''''''

添加SoAd模块对应的接口Api

|image24|

图 TcpIp配置-TcpIpConfig

TcpIpTcpConfig
'''''''''''''''

|image25|

图 TcpIp配置-TcpIpConfig

TcpIpUdpConfig
'''''''''''''''

|image26|

图 TcpIp配置-TcpIpConfig

SoAd配置
^^^^^^^^^

SoAdBswModules
'''''''''''''''

|image27|

图 SoAd配置-SoAdBswModules

关联SoAd相关的Bsw模块

SoAdConfig
'''''''''''

配置DoIP所需的SoAdPdu路由

|image28|

图 SoAd配置-SoAdConfigs

添加SoAdSocketConnectionGroups，设置对应的本地port以及不同连接的远端地址

|image29|

图 SoAd配置-SoAdConfigs

|image30|

图 SoAd配置-SoAdConfigs

在SoAdPduRoutes中关联配置的SoAdSocketConnectionGroups

|image31|

图 SoAd配置-SoAdConfigs

最后设置SoAdSocketRoutes

选择SoAdSocket路由对应的SCGroupConnection

|image32|

图 SoAd配置-SoAdConfigs

配置对应的RouteDest

|image33|

图 SoAd配置-SoAdConfigs

DoIP配置
^^^^^^^^^

DoIPGeneral
''''''''''''

设置DoIP相关的设置

|image34|

|image35|

图 DoIP配置-DoIPGenerals

DoIPConfigSet
''''''''''''''

|image36|

图 DoIP配置-DoIPConfigSets

设置DoIP的事件id，组id和逻辑地址。

|image37|

图 DoIP配置-DoIPConfigSets

设置DoIP功能寻址和物理寻址的通道，选择通道在DoIP中的Role，以及对应的源地址和目标地址的参考点(在DoIPConnections中设置)，以及对应的接收发送Pdu。

|image38|

图 DoIP配置-DoIPConfigSets

添加DoIPConnections中的DoIPTcp&UdpConnections，并分别配置对应的SoAd接收Pdu和发送Pdu，以及Udp连接到SoAd的组播(广播)连接Pdu。

|image39|

图 DoIP配置-DoIPConfigSets

在DoIPConnections中设置DoIP的目标地址。

|image40|

图 DoIP配置-DoIPConfigSets

在DoIPRoutingActivations中添加DoIPConnections中设置的DoIP目标地址参考点

|image41|

图 DoIP配置-DoIPConfigSets

添加DoIP的诊断仪并选择对应的源地址，参考路由激活方式。

PduR配置
^^^^^^^^^

PduRBswModules
'''''''''''''''

|image42|

图 PduR配置-PduRBswModules

添加PduR服务的Bsw模块，选择对应的PduRBswModulesRef后，工具将自动勾选所需Api

PduRoutingTables
'''''''''''''''''

|image43|

图 PduR配置-PduRRoutingTables

PduR的路由表，在DoIP协议栈，需要配置以上路由，路由类型选择TP，选择路由中的目标Pdu(PduRDestPdus)和源Pdu(PduRSrcPdus)，同理添加功能寻址请求路由和响应路由。

ComM配置
^^^^^^^^^

添加一路ComM的通道，后面Dcm模块需要用到这里

|image44|

图 ComM配置-ComMConfigSet

Dcm配置
^^^^^^^^

Dcm模块配置可参考《集成手册_UDSonCAN.pdf》中Dcm的配置，基于DoIP的诊断配置只需修改DcmDsl模块：

添加对应的DoIP诊断的buffer：

|image45|

图 DCM配置-DCMConfigSets

添加DcmDslProtocol:

|image46|

图 DCM配置-DCMConfigSets

Dem配置
^^^^^^^^

请参考《集成手册_UDSonCAN.pdf》中的Dem配置。

BswM配置
^^^^^^^^

请参考《集成手册_UDSonCAN.pdf》中的BswM配置。

配置代码生成
~~~~~~~~~~~~

#. 在ORIENTAIS
   Stuido主界面左方，选择对应的协议栈，或者选择整个ECU，单击右键弹出Validate
   All和Generate All菜单。

   |image47|

   图 配置代码的生成-1

#. 选择Validate
   All对本协议栈各配置选项进行校验，没有错误提示信息即校验通过。若有错误信息，请按照错误提示修改。

#. 选择Generate
   All，生成配置文件。右下角的Console窗口输出生成的配置文件信息。

   |image48|

   图 配置代码的生成-2

#. 将ORIENTAIS Studio切换到Resource模式，即可查看生成的配置文件。

   |image49|

   图 配置代码的生成-3

功能集成
--------

代码集成
~~~~~~~~

协议栈代码包括两部分：项目提供的协议栈源码和ORIENTAIS
Studio配置生成代码。

用户须将协议栈源码和章节（配置代码生成）生成的源代码添加到集成开发工具的对应文件夹。协议栈集成的文件结构，见章节（源代码集成）。

.. note::
   **协议栈集成之前，用户须确保已经有基础工程，且本协议栈相关的其他协议栈能正常工作。**

集成注意事项
~~~~~~~~~~~~

用户须提前配置好Eth的MCAL驱动，如果以太网通过中断完成接收发送，则在集成OS中前在OS中配置好相关的以太网中断。

集成示例
========

本章节通过DoIP协议栈为例，向用户展示DoIP协议栈的集成过程。用户可以据此熟悉DoIP协议栈配置工具的配置过程，以及如何应用配置工具生成的配置文件。

为让用户更清晰的了解工具的使用，所用的配置均逐一手动完成。关于Eth驱动的配置，请参考Eth配置手册。

.. note::
   **本示例不代表用户的实际配置情况，用户需要根据自己的实际需求，决定各个参数的配置。**

集成目标
--------

DoIP集成完成后需根据以下示例测试：

DoIP诊断参数

表 DoIP诊断参数

+----------------------+-----------------------------------------------+
| 参数                 | 值                                            |
+======================+===============================================+
| Local IP Address     | 192.168.0.200                                 |
+----------------------+-----------------------------------------------+
| Local Port           | 13400                                         |
+----------------------+-----------------------------------------------+
| Tester SA            | 0x0E80                                        |
+----------------------+-----------------------------------------------+
| 物理寻址TA           | 0x16D7                                        |
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
| 诊断示例DID          | 0xF183（R：All                                |
|                      | Session，W：1003Session，Level3Security）     |
+----------------------+-----------------------------------------------+

DoIP报文示例

表 DoIP诊断示例报文

+----------------------+-----------------------------------------------+
| 报文类型             | 报文格式                                      |
+======================+===============================================+
| 路由激活请求         | 02 FD 00 05 00 00 00 07 0E 80 00 00 00 00 00  |
+----------------------+-----------------------------------------------+
| 物理寻址1003诊断请求 | 02 FD 80 01 00 00 00 06 0E 80 16 D7 10 03     |
+----------------------+-----------------------------------------------+
| 功能寻址1003诊断请求 | 02 FD 80 01 00 00 00 06 0E 80 E4 00 10 03     |
+----------------------+-----------------------------------------------+
| 请求Level3 Seed      | 02 FD 80 01 00 00 00 06 0E 80 16 D7 27 05     |
+----------------------+-----------------------------------------------+
| 发送Level3 Key       | 02 FD 80 01 00 00 00 0A 0E 80 16 D7 27 06 XX  |
|                      | XX XX XX                                      |
+----------------------+-----------------------------------------------+
| 写DID信息            | 02 FD 80 01 00 00 00 0B 0E 80 16 D7 2E F1 83  |
|                      | 00 00 00 00                                   |
+----------------------+-----------------------------------------------+
| 读DID信息            | 02 FD 80 01 00 00 00 07 0E 80 16 D7 22 F1 83  |
+----------------------+-----------------------------------------------+

源代码集成
----------

项目交付给用户的工程结构如下：

|image50|

图工程结构目录

- ./BSW/Config/BSW_Config目录，这个目录用来存放ORIENTAIS
  studio配置工具生成的配置文件

- ./BSW目录存放模块相关的源代码（除./BSW/Config目录之外）。可以看到Source目录下各个文件夹下是各个模块的源代码。

协议栈调度集成
--------------

DoIP协议栈调度集成步骤如下：

#. 协议栈调度集成。

#. 编译链接代码，将生成的elf文件烧写进芯片。

使用iRte集成
~~~~~~~~~~~~

请参考《集成手册_UDSonCAN.pdf》中的使用iRte集成。

使用Rte集成
~~~~~~~~~~~

请参考《集成手册_UDSonCAN.pdf》中的使用Rte集成。

验证结果
--------

程序运行后使用网络调试助手发送以下指令验证DoIP诊断功能：

|image51|

|image52|

|image53|

|image54|

图DoIP报文交互结果示例

.. |image1| image:: /_static/集成手册/集成手册_DoIP/image2.png
   :width: 5.76736in
   :height: 3.10347in
.. |image2| image:: /_static/集成手册/集成手册_DoIP/image3.png
   :width: 5.76736in
   :height: 3.10694in
.. |image3| image:: /_static/集成手册/集成手册_DoIP/image4.png
   :width: 3.79528in
   :height: 3.62205in
.. |image4| image:: /_static/集成手册/集成手册_DoIP/image5.png
   :width: 3.8072in
   :height: 2.92887in
.. |image5| image:: /_static/集成手册/集成手册_DoIP/image6.png
   :width: 5.76736in
   :height: 3.10694in
.. |image6| image:: /_static/集成手册/集成手册_DoIP/image7.png
   :width: 3.82677in
   :height: 3.51969in
.. |image7| image:: /_static/集成手册/集成手册_DoIP/image8.png
   :width: 5.76736in
   :height: 3.10694in
.. |image8| image:: /_static/集成手册/集成手册_DoIP/image9.png
   :width: 4.29138in
   :height: 8.50899in
.. |image9| image:: /_static/集成手册/集成手册_DoIP/image10.png
   :width: 4.37363in
   :height: 5.05676in
.. |image10| image:: /_static/集成手册/集成手册_DoIP/image11.png
   :width: 4.75486in
   :height: 2.975in
.. |image11| image:: /_static/集成手册/集成手册_DoIP/image12.png
   :width: 5.76319in
   :height: 4.34722in
.. |image12| image:: /_static/集成手册/集成手册_DoIP/image13.png
   :width: 3.78745in
   :height: 4.07111in
.. |image13| image:: /_static/集成手册/集成手册_DoIP/image14.png
   :width: 5.00311in
   :height: 4.46673in
.. |image14| image:: /_static/集成手册/集成手册_DoIP/image15.png
   :width: 5.76736in
   :height: 2.62222in
.. |image15| image:: /_static/集成手册/集成手册_DoIP/image16.png
   :width: 5.76736in
   :height: 2.62222in
.. |image16| image:: /_static/集成手册/集成手册_DoIP/image17.png
   :width: 5.76736in
   :height: 2.62569in
.. |image17| image:: /_static/集成手册/集成手册_DoIP/image18.png
   :width: 5.76736in
   :height: 2.62569in
.. |image18| image:: /_static/集成手册/集成手册_DoIP/image19.png
   :width: 5.76736in
   :height: 2.62222in
.. |image19| image:: /_static/集成手册/集成手册_DoIP/image20.png
   :width: 5.76736in
   :height: 2.62222in
.. |image20| image:: /_static/集成手册/集成手册_DoIP/image21.png
   :width: 5.76736in
   :height: 2.62222in
.. |image21| image:: /_static/集成手册/集成手册_DoIP/image22.png
   :width: 5.76736in
   :height: 2.62222in
.. |image22| image:: /_static/集成手册/集成手册_DoIP/image23.png
   :width: 5.76736in
   :height: 2.62222in
.. |image23| image:: /_static/集成手册/集成手册_DoIP/image24.png
   :width: 5.76736in
   :height: 2.62222in
.. |image24| image:: /_static/集成手册/集成手册_DoIP/image25.png
   :width: 5.76736in
   :height: 2.62222in
.. |image25| image:: /_static/集成手册/集成手册_DoIP/image26.png
   :width: 5.76736in
   :height: 2.62222in
.. |image26| image:: /_static/集成手册/集成手册_DoIP/image27.png
   :width: 5.76736in
   :height: 2.62222in
.. |image27| image:: /_static/集成手册/集成手册_DoIP/image28.png
   :width: 5.76736in
   :height: 2.62222in
.. |image28| image:: /_static/集成手册/集成手册_DoIP/image29.png
   :width: 5.76736in
   :height: 2.62222in
.. |image29| image:: /_static/集成手册/集成手册_DoIP/image30.png
   :width: 5.76736in
   :height: 2.62222in
.. |image30| image:: /_static/集成手册/集成手册_DoIP/image31.png
   :width: 5.76736in
   :height: 2.62222in
.. |image31| image:: /_static/集成手册/集成手册_DoIP/image32.png
   :width: 5.76736in
   :height: 2.62222in
.. |image32| image:: /_static/集成手册/集成手册_DoIP/image33.png
   :width: 5.76736in
   :height: 2.62222in
.. |image33| image:: /_static/集成手册/集成手册_DoIP/image34.png
   :width: 5.76736in
   :height: 2.62222in
.. |image34| image:: /_static/集成手册/集成手册_DoIP/image35.png
   :width: 5.76736in
   :height: 2.62222in
.. |image35| image:: /_static/集成手册/集成手册_DoIP/image36.png
   :width: 5.76736in
   :height: 2.62222in
.. |image36| image:: /_static/集成手册/集成手册_DoIP/image37.png
   :width: 5.76736in
   :height: 2.62222in
.. |image37| image:: /_static/集成手册/集成手册_DoIP/image38.png
   :width: 5.76736in
   :height: 2.62222in
.. |image38| image:: /_static/集成手册/集成手册_DoIP/image39.png
   :width: 5.76736in
   :height: 2.62222in
.. |image39| image:: /_static/集成手册/集成手册_DoIP/image40.png
   :width: 5.76736in
   :height: 2.62222in
.. |image40| image:: /_static/集成手册/集成手册_DoIP/image41.png
   :width: 5.76736in
   :height: 2.62222in
.. |image41| image:: /_static/集成手册/集成手册_DoIP/image42.png
   :width: 5.76736in
   :height: 2.62222in
.. |image42| image:: /_static/集成手册/集成手册_DoIP/image43.png
   :width: 5.76736in
   :height: 2.62222in
.. |image43| image:: /_static/集成手册/集成手册_DoIP/image44.png
   :width: 5.76736in
   :height: 2.62222in
.. |image44| image:: /_static/集成手册/集成手册_DoIP/image45.png
   :width: 5.76736in
   :height: 2.62222in
.. |image45| image:: /_static/集成手册/集成手册_DoIP/image46.png
   :width: 5.76736in
   :height: 2.62222in
.. |image46| image:: /_static/集成手册/集成手册_DoIP/image47.png
   :width: 5.76736in
   :height: 2.62222in
.. |image47| image:: /_static/集成手册/集成手册_DoIP/image48.png
   :width: 3.6415in
   :height: 4.21147in
.. |image48| image:: /_static/集成手册/集成手册_DoIP/image49.png
   :width: 5.76736in
   :height: 2.19931in
.. |image49| image:: /_static/集成手册/集成手册_DoIP/image50.png
   :width: 5.76736in
   :height: 3.10347in
.. |image50| image:: /_static/集成手册/集成手册_DoIP/image51.png
   :width: 2.90625in
   :height: 4.44792in
.. |image51| image:: /_static/集成手册/集成手册_DoIP/image52.png
   :width: 5.76736in
   :height: 4.80139in
.. |image52| image:: /_static/集成手册/集成手册_DoIP/image53.png
   :width: 5.76736in
   :height: 2.91458in
.. |image53| image:: /_static/集成手册/集成手册_DoIP/image54.png
   :width: 5.76736in
   :height: 4.67639in
.. |image54| image:: /_static/集成手册/集成手册_DoIP/image55.png
   :width: 5.76736in
   :height: 3.09236in
