==============
UdpNm
==============

目的
====

本集成手册用于指导客户进行UdpNm集成，文档主要包括的内容为：协议栈集成指导、基于普通应用的集成示例讲解、项目集成特殊说明。

由于各项目的需求不同，集成示例不会针对于特定的商业项目做详细讲解。

缩写词和术语
============

.. table:: 表 缩写词和术语

   +-----------------+---------------------------------------------------------+
   | **缩写词/术语** | **描述**                                                |
   +=================+=========================================================+
   | SoAd            | Socket Adapter 套接字适配模块                           |
   +-----------------+---------------------------------------------------------+
   | UdpNm           | UDP Network Management 以太网网络管理模块               |
   +-----------------+---------------------------------------------------------+
   | EthSM           | Ethernet State Manager 以太网状态控制模块               |
   +-----------------+---------------------------------------------------------+
   | Nm              | Generic Network Management Interface                    |
   |                 | 通用网络管理接口模块                                    |
   +-----------------+---------------------------------------------------------+
   | ComM            | Communication Manager 通信管理模块                      |
   +-----------------+---------------------------------------------------------+
   | RTE             | Runtime Enviroment 虚拟运行环境                         |
   +-----------------+---------------------------------------------------------+
   | SWC             | Software Component 软件组件                             |
   +-----------------+---------------------------------------------------------+

参考文档
========

[1] 参考手册_EthIf.pdf

[2] 参考手册_EthSM.pdf

[3] 参考手册_TcpIp.pdf

[4] 参考手册_SoAd.pdf

[5] 参考手册_NmIf.pdf

[6] 参考手册_UdpNm.pdf

[7] 参考手册_ComM.pdf

协议栈集成
==========

新建ORIENTAIS工程
-----------------

#. 安装ORIENTAIS Studio软件后，双击软件图标打开软件。

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

#. 在弹出的窗口中选择Yes。

   |image5|

   图 新建工程-5

#. 选择[Bsw_Builder]，右键单击，选择New ECU Configuration。

   |image6|

   图 新建工程-6

#. 在弹出的窗口中输入ECU名，然后选择Next。

   |image7|

   图 新建工程-7

#. 在弹出的窗口中勾选需添加的模块，点击Finish。

   |image8|

   图 新建工程-8

配置文件生成
------------

模块配置
~~~~~~~~

模块的具体配置，取决于具体的项目需求。UdpNm各模块配置项的详细介绍，参见《参考手册_UdpNm.pdf》。

配置代码生成
~~~~~~~~~~~~

#. 在ORIENTAIS
   Stuido主界面左方，选择对应的协议栈，或者选择整个ECU，单击右键弹出Validate
   All和Generate All菜单。

   |image9|

   图 配置代码的生成-1

#. 选择Validate
   All对本协议栈各配置选项进行校验，没有错误提示信息即校验通过。若有错误信息，请按照错误提示修改。

#. 选择Generate
   All，生成配置文件。右下角的Console窗口输出生成的配置文件信息。

   |image10|

   图 配置代码的生成-2

#. 将ORIENTAIS Studio切换到Resource模式，即可查看生成的配置文件。

   |image11|

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

对于集成过程中，协议栈特殊要求和用户经常出现的问题，归类总结形成下表。用户需逐一排查表中的约束项，以避免集成问题出现。

表 UDPNM集成约束清单

+----------+----------+-------------------------------------------------------------------------------------+
| **编号** | **类别** | **约束限制**                                                                        |
+==========+==========+=====================================================================================+
| **1**    | 堆栈     | 用户需确保为任务堆栈和中断堆栈分配足够的堆栈空间。                                  |
+----------+----------+-------------------------------------------------------------------------------------+
| **2**    | 头文件   | - 添加协议栈代码之后，用户需更新集成开发工具中的头文件路径。                        |
|          |          |                                                                                     |
|          |          | - 调用协议栈API的源文件，需要包含协议栈的头文件。                                   |
+----------+----------+-------------------------------------------------------------------------------------+
| **3**    | 初始化   | UdpNm诊断栈的初始化顺序为：EthIf_Init、TcpIp_Init、SoAd_Init、                      |
|          |          | EthSM_Init、UdpNm_Init、 Nm_Init和ComM_Init。                                       |
+----------+----------+-------------------------------------------------------------------------------------+
| **4**    | 周期函数 | UdpNm_MainFunction，EthSM_MainFunction和ComM_MainFunction需要被周期性任务函数调用。 |
|          |          |                                                                                     |
|          |          | EthSM的调度周期必须大于ComM的调度周期                                               |
+----------+----------+-------------------------------------------------------------------------------------+

集成示例
========

集成目标
--------

本手册会以以下参数作为示例，进行集成演示。

表 UDPNM集成参数表

+-------------------------+--------------------------------------------+
| **参数**                | **值**                                     |
+=========================+============================================+
| 快发周期                | 50ms                                       |
+-------------------------+--------------------------------------------+
| 快发次数                | 10                                         |
+-------------------------+--------------------------------------------+
| 正常发送周期            | 500ms                                      |
+-------------------------+--------------------------------------------+
| 节点Id                  | 50                                         |
+-------------------------+--------------------------------------------+
| RepeatState时间         | 2s                                         |
+-------------------------+--------------------------------------------+
| Nm-Timeout时间          | 5s                                         |
+-------------------------+--------------------------------------------+
| WaitBusSleep时间        | 1.5s                                       |
+-------------------------+--------------------------------------------+
| Socket信息              | 本地：172.31.30.78/ UDP/30500              |
|                         |                                            |
|                         | 远端：239.192.255.250/UDP/30500            |
+-------------------------+--------------------------------------------+


模块配置
--------

EcuC模块配置
~~~~~~~~~~~~

#. 双击EcuC模块，打开EcuC模块配置界面。

#. 在EcucConfigSets栏目上右键，选择EcucConfigSet。再在EcucConfigSet上右键，选择New🡪
   EcucConfigSet。再在EcucPduCollections上右键，选择New
   EcucPduCollection。

   #. PduIdTypeEnum 选择UINT16。

   #. PduLengthTypeEnum 选择UINT16。

   |image12|

   图 配置EcucPduCollection

#. 在EcucPduCollection上右键，选择Pdu，会生成一个Pdu的配置界面。

   #. 建议不要使用默认生成的Pdu名字（如：Pdu_0），将Pdu名字改成有意义的名字对后续的配置过程将会有很大帮助。

   #. 这里按照发送和接收，可以将Pdu名字改为报文的名字。PduLength：Pdu长度，根据实际使用帧的长度设置。

   #. 由于UdpNm的收发报文不需要PduR来路由，因此每个方向（发送/接收）只需要配置一个Pdu。对于需要PduR路由的报文，每个方向需要创建2个Pdu。

   |image13|

   图 配置Pdu-1

   |image14|

   图 配置Pdu-2

#. ECUC模块到此配置结束。可以在模块上右键，然后选择校验，查看是否配置有错误。

#. 校验后提示窗口没有错误信息，即校验通过。

SoAd模块配置
~~~~~~~~~~~~

#. 配置SoAdGeneral，一般配置调度周期，Socket个数和SocketGroup的个数。

   |image15|

   图配置SoAdGeneral

#. 配置SoAdBswModules，若数据流需要通过SoAd模块，则需要配置。本例中只有UdpNm。所以只需要配置UdpNm。

   |image16|

   图 配置SoAdBswModules

#. 配置SoAdConfig。

   #. 配置SoAdSocketGroup。

      |image17|

      图 配置SoAdSocketGroup

   #. 配置SoAdSocketConnectionGroup。UdpNm采用多播收发，需要配置2个Socket。分别用于发送和接收。

      |image18|

      图 配置SoAdSocketConnectionGroup-1

      |image19|

      图 配置SoAdSocketConnectionGroup-2

      |image20|

      图 配置SoAdSocketConnectionGroup-3

      |image21|

      图 配置SoAdSocketConnectionGroup-4

      |image22|

      图 SoAdSocketConnectionGroup-5

      |image23|

      图 配置SoAdSocketConnectionGroup-6

   #. 配置SoAdRoute，即报文发送。

      |image24|

      图 配置SoAdRoute-1

      |image25|

      图 配置SoAdRoute-2

   #. 配置SoAdSocketRoute，即报文接收。

      |image26|

      图 配置SoAdSocketRoute-1

      |image27|

      图 配置SoAdSocketRoute-2

#. 校验后提示窗口没有错误信息，即校验通过。

ComM模块配置
~~~~~~~~~~~~

#. ComMGeneral页面一般不需要配置，保持默认即可。

#. 配置ComMConfigSet页面。

   #. 首先配置一个ComMUser，默认就创建了一个。

      |image28|

      图 配置ComMUser

   #. 配置ComMChannel，默认就创建了一个。

   #. 配置ComMBusType，选择本通道的总线类型。还需要配置ComMMainFunctionPeriod，表示本通道的调度周期。

      |image29|

      图 配置ComMChannels

   #. 配置ComMNmVariant，表示本通道的类型。FULL表示通道由网络管理来管理。LIGHT表示本通道没有网络管理。

      |image30|

      图 配置ComMNmVariant

   #. 每个Channel需要关联一个User，对于大多数常见，一个User就等于一个Channel。

      |image31|

      图 配置ComMUserPerChannel

#. ComM配置完成，校验。

EthSM模块配置
~~~~~~~~~~~~~

#. 配置EthSMGeneral。这里只需要配置一个调度周期，尽可能快。

   |image32|

   图 配置EthSMGeneral

#. 配置EthSMNetwork。

   |image33|

   图 配置EthSMNetwork

#. 校验后提示窗口没有错误信息，即校验通过。

Nm模块配置
~~~~~~~~~~

#. 配置NmChannelConfig，需要配置2个地方。第一个是NmChannelConfig，关联到ComM的channel，第二个需要创建NmStandardBusNmConfig，选择网络管理类型。

   |image34|

   图 配置NmChannelConfig-1

   |image35|

   图 配置NmChannelConfig-2

#. 配置NmGlobalConfig，需要配置NmGlobalConstants和NmGlobalFeatures。配置的重点在NmGlobalFeatures。这里主要是全局选择网络管理的功能。部分功能还需要在OsekNm中配置。

   |image36|

   图 配置NmGlobalConfig-1

   |image37|

   图 配置NmGlobalConfig-2

#. Nm配置完成，校验。

UdpNm模块配置
~~~~~~~~~~~~~

#. 配置UdpNmGlobalConfig。

   |image38|

   图 配置UdpNmGlobalConfig

#. 配置UdpNmChannelConfig，这里主要配置时间参数。

   |image39|
   |image40|

   图 配置UdpNmChannleConfig

#. 配置报文的收发。

   |image41|

   图 配置UdpNmRxPdu

   |image42|

   图 配置UdpNmTxPdu

#. 校验后提示窗口没有错误信息，即校验通过。

源码集成
--------

项目交付给用户的工程结构如下：

   |image43|

   图 工程结构目录

- BSW_Cfg目录，这个目录用来存放配置工具生成的配置文件，网络管理有关的配置文件放在NM和UdpNm文件夹中。

- src目录，存放模块相关的源代码。可以看到Source目录下各个文件夹下是各个模块的源代码。

网络管理源代码集成步骤如下：

#. 将章节（模块的配置）中ORIENTAIS
   Studio生成的配置文件复制到Config文件夹下的各个模块的对应文件夹中【例如：Config\\inc\\NM】。

#. 将项目提供的协议栈源代码文件复制到Source文件夹下的对应模块的文件夹中【例如：SourceS\\NM】。

#. 将所需的头文件包含进工程设置中，如下步骤：

   #. 添加头文件路径。

   #. 添加所需的头文件。

   #. 添加调度文件，点击应用保存。

   #. 编译工程。

调度集成
--------

调度集成步骤如下：

#. 协议栈调度集成。

#. 编译链接代码，将生成的elf文件烧写进芯片。

UdpNm有关的代码，在下方的main.c文件中给出重点标注。

.. note::
   **本示例中，UdpNm网络管理初始化的代码和启动通信的代码置于main.c文件，并不代表其他项目同样适用于将其置于main.c文件中。**

.. code-block:: c
   :linenos:
   :emphasize-lines: 6-14, 23-29, 32-33, 45, 61-63, 79-80

   #include "Timer.h"
   #include "Led.h"
   #include "Mcal.h"
   #include "UserTimer.h"
   // UdpNm协议栈相关模块头文件
   #include "EthIf.h"
   #include "TcpIp.h"
   #include "SoAd.h"
   #include "EthSM.h"
   #include "Nm.h"
   #include "UdpNm.h"
   #include "ComM.h"
   #include "ComM_Internal.h"

   Com_IpduGroupVector g_ComIpduGroupVector;

   int main(void) 
   {
       McalUser_Init();
       Led_Init();

       // 初始化EthIf、EthSM、TcpIp、SoAd、Nm、UdpNm、ComM模块
       EthIf_Init(&EthIf_ConfigData);
       EthSM_Init();
       TcpIp_Init(&TcpIp_Config);
       SoAd_Init(&SoAd_Config);
       Nm_Init(&Nm_Config);
       UdpNm_Init(&UdpNm_Config);
       ComM_Init(&ComM_Config);
       
       // 打开通信：初始化网络管理及UdpNm模块
       ComM_Channel[ComMChannel_Eth].CommunicationAllowed = TRUE;
       ComM_RequestComMode(ComMUser_Eth, COMM_FULL_COMMUNICATION);

       StartOS(OSDEFAULTAPPMODE);

       while (1);
   }

   /* OsTask_c0_1ms: Core0(CPU0), Type = BASIC, Priority = 8*/        
   TASK(OsTask_c0_1ms)
   {
       /* please insert your code here ... */
       // EthSM模块周期处理函数
       EthSM_MainFunction();

       if (E_OK != TerminateTask())
       {
           while (1)
           {
               /* dead loop */
           }
       }
   }                             

   /* OsTask_c0_5ms: Core0(CPU0), Type = BASIC, Priority = 6*/        
   TASK(OsTask_c0_5ms)
   {
       /* please insert your code here ... */
       // ComM、EthIf、UdpNm模块周期处理函数
       ComM_MainFunction(ComMUser_Eth);
       EthIf_MainFunctionState();
       UdpNm_MainFunction(0);

       if (E_OK != TerminateTask())
       {
           while (1)
           {
               /* dead loop */
           }
       }
   }      

   /* OsTask_c0_20ms: Core0(CPU0), Type = BASIC, Priority = 6*/ 
   TASK(OsTask_c0_20ms)
   {
       /* please insert your code here ... */
       // SoAd、TcpIp模块周期处理函数
       SoAd_MainFunction();
       TcpIp_MainFunction();
       
       if (E_OK != TerminateTask())
       {
           while (1)
           {
               /* dead loop */
           }
       }
   }

验证结果
--------

根据集成目标，使用Wireshark工具查看报文发送方式是否正确。前10个报文发送间隔50ms，后面报文的间隔是500ms，符合集成目标。

   |image44|

   图 UdpNm报文发送示例

.. |image1| image:: /_static/集成手册/集成手册_UdpNm/image2.png
   :width: 5.76736in
   :height: 2.9125in


.. |image2| image:: /_static/集成手册/集成手册_UdpNm/image3.png
   :width: 5.76736in
   :height: 2.9125in


.. |image3| image:: /_static/集成手册/集成手册_UdpNm/image4.png
   :width: 5.76736in
   :height: 2.9125in


.. |image4| image:: /_static/集成手册/集成手册_UdpNm/image5.png
   :width: 5.76736in
   :height: 2.9125in


.. |image5| image:: /_static/集成手册/集成手册_UdpNm/image6.png
   :width: 5.76736in
   :height: 2.9125in


.. |image6| image:: /_static/集成手册/集成手册_UdpNm/image7.png
   :width: 5.76736in
   :height: 2.9125in


.. |image7| image:: /_static/集成手册/集成手册_UdpNm/image8.png
   :width: 5.76736in
   :height: 2.9125in


.. |image8| image:: /_static/集成手册/集成手册_UdpNm/image9.png
   :width: 5.76736in
   :height: 6.9125in


.. |image9| image:: /_static/集成手册/集成手册_UdpNm/image10.png
   :width: 5.76736in
   :height: 2.9125in


.. |image10| image:: /_static/集成手册/集成手册_UdpNm/image11.png
   :width: 5.76736in
   :height: 2.9125in


.. |image11| image:: /_static/集成手册/集成手册_UdpNm/image12.png
   :width: 5.76736in
   :height: 2.9125in


.. |image12| image:: /_static/集成手册/集成手册_UdpNm/image13.png
   :width: 5.76736in
   :height: 2.9125in


.. |image13| image:: /_static/集成手册/集成手册_UdpNm/image14.png
   :width: 5.76736in
   :height: 2.9125in


.. |image14| image:: /_static/集成手册/集成手册_UdpNm/image15.png
   :width: 5.76736in
   :height: 2.9125in


.. |image15| image:: /_static/集成手册/集成手册_UdpNm/image16.png
   :width: 5.76736in
   :height: 2.9825in


.. |image16| image:: /_static/集成手册/集成手册_UdpNm/image17.png
   :width: 5.96736in
   :height: 2.9125in


.. |image17| image:: /_static/集成手册/集成手册_UdpNm/image18.png
   :width: 5.76736in
   :height: 2.9825in

.. |image18| image:: /_static/集成手册/集成手册_UdpNm/image19.png
   :width: 5.76736in
   :height: 2.9125in


.. |image19| image:: /_static/集成手册/集成手册_UdpNm/image20.png
   :width: 5.76736in
   :height: 2.9125in


.. |image20| image:: /_static/集成手册/集成手册_UdpNm/image21.png
   :width: 5.76736in
   :height: 2.9125in


.. |image21| image:: /_static/集成手册/集成手册_UdpNm/image22.png
   :width: 5.76736in
   :height: 2.9125in


.. |image22| image:: /_static/集成手册/集成手册_UdpNm/image23.png
   :width: 5.76736in
   :height: 2.9125in


.. |image23| image:: /_static/集成手册/集成手册_UdpNm/image24.png
   :width: 5.76736in
   :height: 2.9125in


.. |image24| image:: /_static/集成手册/集成手册_UdpNm/image25.png
   :width: 5.76736in
   :height: 2.9125in


.. |image25| image:: /_static/集成手册/集成手册_UdpNm/image26.png
   :width: 5.76736in
   :height: 2.9125in


.. |image26| image:: /_static/集成手册/集成手册_UdpNm/image27.png
   :width: 5.76736in
   :height: 2.9125in


.. |image27| image:: /_static/集成手册/集成手册_UdpNm/image28.png
   :width: 5.76736in
   :height: 2.9125in


.. |image28| image:: /_static/集成手册/集成手册_UdpNm/image29.png
   :width: 5.76736in
   :height: 2.9125in


.. |image29| image:: /_static/集成手册/集成手册_UdpNm/image30.png
   :width: 5.76736in
   :height: 2.9125in


.. |image30| image:: /_static/集成手册/集成手册_UdpNm/image31.png
   :width: 5.76736in
   :height: 2.9125in


.. |image31| image:: /_static/集成手册/集成手册_UdpNm/image32.png
   :width: 5.76736in
   :height: 2.9125in


.. |image32| image:: /_static/集成手册/集成手册_UdpNm/image33.png
   :width: 5.76736in
   :height: 2.9125in


.. |image33| image:: /_static/集成手册/集成手册_UdpNm/image34.png
   :width: 5.76736in
   :height: 2.9125in


.. |image34| image:: /_static/集成手册/集成手册_UdpNm/image35.png
   :width: 5.76736in
   :height: 2.9125in


.. |image35| image:: /_static/集成手册/集成手册_UdpNm/image36.png
   :width: 5.76736in
   :height: 2.9125in


.. |image36| image:: /_static/集成手册/集成手册_UdpNm/image37.png
   :width: 5.76736in
   :height: 2.9125in


.. |image37| image:: /_static/集成手册/集成手册_UdpNm/image38.png
   :width: 5.76736in
   :height: 2.9125in


.. |image38| image:: /_static/集成手册/集成手册_UdpNm/image39.png
   :width: 5.76736in
   :height: 2.9125in


.. |image39| image:: /_static/集成手册/集成手册_UdpNm/image40.png
   :width: 5.76736in
   :height: 2.9125in


.. |image40| image:: /_static/集成手册/集成手册_UdpNm/image41.png
   :width: 5.76736in
   :height: 2.9125in


.. |image41| image:: /_static/集成手册/集成手册_UdpNm/image42.png
   :width: 5.76736in
   :height: 2.9125in


.. |image42| image:: /_static/集成手册/集成手册_UdpNm/image43.png
   :width: 5.76736in
   :height: 2.9125in


.. |image43| image:: /_static/集成手册/集成手册_UdpNm/image44.png
   :width: 5.76736in
   :height: 3.9125in


.. |image44| image:: /_static/集成手册/集成手册_UdpNm/image45.png
   :width: 5.76736in
   :height: 4.9125in