====================
SOMEIP
====================

目的
====

本文档旨在通过一个SOMEIP示例工程的配置，向用户展示SOMEIP的集成过程。

通过阅读本文档，用户可以了解ORIENTAIS配置工具的配置过程，以及如何应用配置工具生成的配置文件。

为了让用户更清晰的了解工具的使用，所用的配置均逐一手动完成。用户在了解了配置的基本过程后，可以快速完成配置。

缩写词和术语
============

.. table:: 表 缩写词和术语

   +-----------------+---------------------------------------------------------+
   | **缩写词/术语** | **描述**                                                |
   +-----------------+---------------------------------------------------------+
   | SoAd            | Socket Adapter 将socket的数据和PDU进行转换              |
   +-----------------+---------------------------------------------------------+
   | Sd              | Service Discovery 服务发现模块                          |
   +-----------------+---------------------------------------------------------+
   | SOMEIP          | Scalable service-Oriented MiddlewarE over IP            |
   |                 | 可扩展的面向服务的IP中间件                              |
   +-----------------+---------------------------------------------------------+
   | RTE             | Runtime Enviroment 虚拟运行唤醒                         |
   +-----------------+---------------------------------------------------------+
   | SWC             | Software Component 软件组件                             |
   +-----------------+---------------------------------------------------------+

参考文档
========

[1] 参考手册_Sd.pdf

[2] 参考手册_SomeIpTp.pdf

[3] 参考手册_SomeIpXf.pdf

协议栈集成
==========

新建ORIENTAIS工程
-----------------

#. 安装ORIENTAIS Manager软件，Install
   SnapShot后双击Controller列名称打开软件。

   |image1|

   图 新建工程-1

#. 菜单栏File🡪New🡪Project，新建工程

   |image2|

   图 新建工程-2

#. 在弹出的新建窗口中选择Autosar下的 [BSW Project]，选择Next

   |image3|

   图 新建工程-3

#. 在弹出的窗口中输入工程名，选择Finish

   |image4|

   图 新建工程-4

#. 在弹出的窗口中选择Yes。

   |image5|

   图 新建工程-5

#. 在工程的[Bsw_Builder]项目上右键，选择New ECU Configuration

   |image6|

   图 新建工程-6

#. 在弹出的窗口中输入一个ECU名，然后选择Next

   |image7|

   图 新建工程-7

#. 在弹出的窗口中勾选需要添加的模块，点击Finish。

   |image8|

   图 新建工程-8

#. 新建完成的工程如下所示，步骤7中添加的模块已经被加入到工程中。

   |image9|

   图 新建工程-9

配置文件生成
------------

模块配置
~~~~~~~~

模块的具体配置，取决于具体的项目需求。SOMEIP各模块配置项的详细介绍，参见《参考手册_Sd.pdf》、《参考手册_SomeIpTp.pdf》、《参考手册_SomeIpXf.pdf》。

配置代码生成
~~~~~~~~~~~~

#. 在工程上右键会弹出校验整个工程和生成整个工程所有模块配置文件的菜单。

#. 首先选择Validate All，没有错误提示信息即校验通过。

   |image10|

   图 配置代码的生成-1

#. 然后选择Generate
   All，生成配置文件。右下角的输出框中会输出生成的配置文件信息。

   |image11|

   图 配置代码的生成-2

#. 在工程Config文件夹下即可查看生成的配置文件。

   |image12|

   图 配置代码的生成-3

功能集成
--------

代码集成
~~~~~~~~

协议栈代码包括两部分：项目提供的协议栈源码和ORIENTAIS
Studio配置生成代码。SOMEIP集成包括SOMEIP源码（SD、SomeipXf）。

用户须将协议栈源码和章节（配置代码生成）生成的配置源代码添加到集成开发工具的对应文件夹。协议栈集成的文件结构，见章节（源代码集成）。

.. note::
   **协议栈集成之前，用户须确保已经有基础工程，以及以太网通信协议栈已集成，且本协议栈相关的其他协议栈能正常工作。**

集成注意事项
~~~~~~~~~~~~

对于集成过程中，协议栈特殊要求和用户经常出现的问题，归类总结形成下表。用户需逐一排查表中的约束项，以避免集成问题出现。

表 SOMEIP集成约束清单

+----------+----------+----------------------------------------------------------------+
| **编号** | **类别** | **约束限制**                                                   |
+----------+----------+----------------------------------------------------------------+
| **1**    | 堆栈     | 用户需确保为任务堆栈和中断堆栈分配足够的堆栈空间。             |
+----------+----------+----------------------------------------------------------------+
| **2**    | 头文件   | - 添加协议栈代码之后，用户需更新集成开发工具中的头文件路径。   |
|          |          |                                                                |
|          |          | - 调用协议栈API的源文件，需要包含协议栈的头文件。              |
+----------+----------+----------------------------------------------------------------+
| **3**    | 初始化   | SOMEIP协议栈的初始化顺序为：EthIf_Init, TcpIp_Init,            |
|          |          | SoAd_Init，SomeIpXf_Init，Sd_Init。                            |
+----------+----------+----------------------------------------------------------------+
| **4**    | 周期函数 | EthSM_MainFunction,EthIf_MainFunctionState,Sd_MainFunction,    |
|          |          | ComM_MainFunction\_<ComMChannel_ETH>需要被周期性任务函数调用。 |
+----------+----------+----------------------------------------------------------------+

配置过程
========

集成目标
--------

本手册会以以下参数作为示例，进行集成演示。

.. table:: 表 配置参数

   +-------------------------+------------------------------------------------------+
   | **参数**                | **值**                                               |
   +-------------------------+------------------------------------------------------+
   | SdServerService实例参数 | SdServerServiceId：0x1                               |
   |                         |                                                      |
   |                         | SdServerServiceInstanceId：0x1                       |
   |                         |                                                      |
   |                         | SdServerServiceMajorVersion：1                       |
   |                         |                                                      |
   |                         | SdServerServiceMinorVersion：1                       |
   +-------------------------+------------------------------------------------------+
   | SdServerTimer时间参数   | SdServerTimerInitialOfferDelayMax：0.1               |
   |                         |                                                      |
   |                         | SdServerTimerInitialOfferDelayMin：0.0               |
   |                         |                                                      |
   |                         | SdServerTimerInitialOfferRepetitionBaseDelay：0.03   |
   |                         |                                                      |
   |                         | SdServerTimerInitialOfferRepetitionsMax：3           |
   |                         |                                                      |
   |                         | SdServerTimerOfferCyclicDelay：1.0                   |
   |                         |                                                      |
   |                         | SdServerTimerRequestResponseMaxDelay：0.5            |
   |                         |                                                      |
   |                         | SdServerTimerRequestResponseMinDelay：0.0            |
   |                         |                                                      |
   |                         | SdServerTimerTTL：300                                |
   +-------------------------+------------------------------------------------------+
   | Socket信息              | Sd单播本地：172.31.30.78/ UDP/30490                  |
   |                         |                                                      |
   |                         | Sd多播本地：239.192.255.250/ UDP/30490               |
   |                         |                                                      |
   |                         | AddMethod本地：172.31.30.78/ TCP/12310               |
   |                         |                                                      |
   |                         | AddMethod远端：172.31.30.80/ TCP/0（端口号为通配符） |
   +-------------------------+------------------------------------------------------+
   | 序列化参数              | 加法运算请求参数：                                   |
   |                         |                                                      |
   |                         | typedef struct                                       |
   |                         |                                                      |
   |                         | {                                                    |
   |                         |                                                      |
   |                         |     uint16 number_a;                                 |
   |                         |                                                      |
   |                         |     uint16 number_b;                                 |
   |                         |                                                      |
   |                         | } AddMethodReq;                                      |
   |                         |                                                      |
   |                         | 加法运算结果参数：                                   |
   |                         |                                                      |
   |                         | typedef uint32 AddMethodResp;                        |
   +-------------------------+------------------------------------------------------+

模块配置
--------

EcuC模块配置
~~~~~~~~~~~~

#. 双击EcuC模块，打开EcuC模块配置界面。

#. 在EcucConfigSets栏目上右键新建 EcucConfigSet。

#. 再在EcucPduCollections上右键新建EcucPduCollection。配置PduIdTypeEnum为UINT16，PduLengthTypeEnum为UINT32。

   |image13|

   图 EcuC 模块配置-1

#. 在EcucPduCollection上右键，选择Pdu，生成一个Pdu的配置界面。

   |image14|

   图 EcuC 模块配置-2

#. 配置4个PDU用于加法运算服务的收发，pdu长度为500，
   SoAd_SdInstance0_AddMethodReq、LdCom_SdInstance0_AddMethodReq、SoAd_SdInstance0_AddMethodResp、LdCom_SdInstance0_AddMethodResp；

   配置3个PDU用于用于SD模块的单/多播收发，pdu长度1400，
   SdInstance0_Unicast_Rx、SdInstance0_Multicast_Rx、SdInstance0_Tx。

   |image15|

   图 EcuC 模块配置-3

#. ECUC模块配置完成，在模块上右键，选择校验。

   |image16|

   图 EcuC 模块配置-4

#. 查看校验窗口，校验提示窗口没有错误信息，即校验通过。

   |image17|

   图 EcuC 模块配置-5

Tcpip模块配置
~~~~~~~~~~~~~

#. 在TcpIp模块添加Sd模块使用的多播地址239.192.255.250。

   |image18|

   图 Tcpip模块配置-1

   |image19|

   图 Tcpip模块配置-2

   |image20|

   图Tcpip模块配置-3

#. 按照步骤1配置SD模块单播地址172.31.30.78.

#. 校验后提示窗口没有错误信息，即校验通过。

SoAd模块配置
~~~~~~~~~~~~

#. 配置SoAdGeneral，配置调度周期0.005S，Socket最大个数4和SocketGroup的最大个数10。

   |image21|

   图 SoAd模块配置-1

#. 配置SoAdBswModules，本例中需关联SD和PDUR，所以新建两个模块并配置SoAdBswModuleRef关联对应模块。

   |image22|

   图 SoAd 模块配置-2

#. 配置SoAdSocketGroup，Sd和AddMethod Server各配置一个

   |image23|

   图 SoAd 模块配置-3

   |image24|

   图 SoAd 模块配置-4

#. 配置SoAdSocketConnectionGroup；Sd采用多播/单播收发，需要配置2个Socket，分别用于单播发送/多播发送/单播接收和多播接收；AddMethod
Server是TCP Server，需要配置一个Socket。

   其中单播收发的Socket配置如下：

   |image25|

   图 SoAd 模块配置-5

   |image26|

   图 SoAd 模块配置-6

   |image27|

   图 SoAd 模块配置-7

   多播的Socket配置如下：

   |image28|

   图 SoAd 模块配置-8

   |image29|

   图 SoAd 模块配置-9

   |image30|

   图 SoAd 模块配置-10

   AddMethod Server的配置如下：

   |image31|

   图 SoAd 模块配置-11

   |image32|

   图 SoAd 模块配置-12

   |image33|

   图 SoAd 模块配置-13

#. 配置SoAdPduRoute，即报文发送。

   |image34|

   图 SoAd 模块配置-14

   |image35|

   图 SoAd 模块配置-15

   |image36|

   图 SoAd 模块配置-16

   |image37|

   图 SoAd 模块配置-17

#. 配置SoAdSocketRoute，即报文接收。

   |image38|

   图 SoAd 模块配置-18

   |image39|

   图 SoAd 模块配置-19

   |image40|

   图 SoAd 模块配置-20

   |image41|

   图 SoAd 模块配置-21

   |image42|

   图 SoAd 模块配置-22

   |image43|

   图 SoAd 模块配置-23

#. 校验后提示窗口没有错误信息，即校验通过。

Sd模块配置
~~~~~~~~~~

#. SdGeneral页面配置

   |image44|

   图 Sd模块配置-1

#. 配置SdConfig。

#. 新建一个SdInstance, SdAddrFamily选择TCPIP_AF_INET。

   |image45|

   图 Sd模块配置-2

#. 配置Sd的Pdu，一个多播接收Pdu，一个发送Pdu，一个单播接收Pdu。

   |image46|

   图 Sd模块配置-3

   |image47|

   图 Sd模块配置-4

   |image48|

   图 Sd模块配置-5

#. 右键新建一个SdServerTimer，并配置。

   |image49|

   图 Sd模块配置-6

#. 右键新建一个SdSeverService，并配置。

   |image50|

   图 Sd模块配置-7

#. 新建一个SdProvidedMethod，并配置。

   |image51|

   图 Sd模块配置-8

#. 校验后提示窗口没有错误信息，即校验通过。

Ldcom模块配置
~~~~~~~~~~~~~

#. 打开LdcomGeneral，配置Ldcom使用的回调函数声明头文件。

   |image52|

   图 Ldcom模块配置-1

#. 打开LdcomConfig，配置AddMethod Server报文的收发。

   |image53|

   图 Ldcom模块配置-2

   |image54|

   图 Ldcom模块配置-3

#. 校验后提示窗口没有错误信息，即校验通过。

PduR模块配置
~~~~~~~~~~~~

#. PduRGemeral页面保持默认配置，不用修改。

#. ②打开PduRBswModeles，新建并配置PduRBswModules_LdCom、PduRBswModules_SoAd。

   |image55|

   图 PduR模块配置-1

   |image56|

   图 PduR模块配置-2

#. 打开PduRRoutingTables，并新建PduRRoutingTable，配置AddrMethod
   Server报文的收发路由。

   |image57|

   图 PduR模块配置-3

   |image58|
   |image59|

   图 PduR模块配置-4

   |image60|

   图 PduR模块配置-5

   |image61|
   |image62|

   图 PduR模块配置-6

#. 校验后提示窗口没有错误信息，即校验通过。

Xfrm模块配置
~~~~~~~~~~~~

#. 新建DataTypeDescription，并配置序列化使用的参数类型和结构体。

   |image63|

   图 Xfrm模块配置-1

   |image64|

   图 Xfrm模块配置-2

   |image65|

   图 Xfrm模块配置-3

   |image66|

   图 Xfrm模块配置-4

   |image67|

   图 Xfrm模块配置-5

#. 打开TransformationSet页面，新建并配置一个SOMEIP序列化使用的TransformationTechnology。

   |image68|

   图 Xfrm模块配置-6

#. 新建一个SOMEIPTransformationDescription，配置序列化的字节对齐方式以及数据大小端类型。

   |image69|

   图 Xfrm模块配置-7

#. 打开BufferProperty，配置序列化报文HeaderLenght长度为16bits。

   |image70|

   图 Xfrm模块配置-8

#. 打开SomeIpXfPublic，新建并配置两个SOMEIPTransformationlSignaProp。

   |image71|

   图 Xfrm模块配置-9

   |image72|

   图 Xfrm模块配置-10

#. 新建并配置两个ClientServerInterface。

   |image73|

   图 Xfrm模块配置-11

   |image74|

   图 Xfrm模块配置-12

#. 新建并配置两个SomeIpXfConfig。

   |image75|

   图 Xfrm模块配置-13

   |image76|

   图 Xfrm模块配置-14

#. 在TransformationSet页面，新建并配置两个Transformations，以生成对应的序列化/反序列化函数。

   |image77|

   图 Xfrm模块配置-15

   |image78|

   图 Xfrm模块配置-16

#. 校验后提示窗口没有错误信息，即校验通过。

源码集成
--------

项目交付给用户的工程结构如下：

   |image79|

   图 源码集成

#. Config目录，这个目录用来存放基础软件配置工具生成的配置文件，SOMEIP有关的配置文件放在该文件夹中。

#. 模块相关的静态源代码，存放在各个模块的文件夹下。

调度集成
--------

#. 将章节（模块配置及代码生成）生成的配置文件复制到Config文件夹中。

#. 添加初始化函数和周期调用函数。

.. note::
   本示例中， SOMEIP初始化的代码和启动通信的代码置于main.c文件，并不代表其他项目同样适用于将其置于main.c文件中。

.. code-block:: c
   :linenos:
   :emphasize-lines: 23, 30-38, 41-42, 50, 56, 63-65, 73-75

   #include "Timer.h"
   #include "Led.h"
   #include "Mcal_User.h"
   #include "UserTimer.h"
   #include "Dio.h"
   #include "ComM.h"
   #include "ComM_Internal.h"
   #include "Can.h"
   #include "E2EXf.h"
   #include "CanNm.h"
   #include "EthIf.h"
   #include "EthSM.h"
   #include "TcpIp.h"
   #include "SoAd.h"
   #include "LdCom.h"
   #include "TestCase.h"
   #include "Wdg.h"
   #include "WdgM.h"
   #include "Mcu.h"
   #include "ringbuf.h"
   #include "Sd.h"
   // SOMEIP协议栈相关头文件
   #include "SomeIpXf.h"

   int main(void)
   {
       eth_ringbuf_init(&g_EthRingBufManager, &g_EthRxPduBuf, ARRAR_SIZE(g_EthRxPduBuf));
       McalUser_Init();

       // 初始化核心通信模块
       PduR_Init(&PduR_PBConfigData);
       ComM_Init(&ComM_Config);
       
       EthIf_Init(&EthIf_ConfigData);
       EthSM_Init();
       TcpIp_Init(&TcpIp_Config);
       SoAd_Init(&SoAd_Config);
       LdCom_Init(&LdCom_InitCfgSet);
       SomeIpXf_Init(&SomeIpXf_Config);  // 初始化SOMEIP适配层
       Sd_Init(&Sd_Config);

       // 使能ETH通信通道并请求全通信模式
       ComM_ChComAllow(ComMUser_ETH, TRUE);
       ComM_RequestComMode(ComMUser_Eth, COMM_FULL_COMMUNICATION);

       while (1)
       {    
           // 1ms周期任务：处理以太网状态机
           if (UserTimer_GetFlag1ms())
           {
               EthSM_MainFunction();
               UserTimer_ClrFlag1ms();
           }

           // 2ms周期任务：处理以太网接口状态
           if (UserTimer_GetFlag2ms())
           {
               EthIf_MainFunctionState();
               UserTimer_ClrFlag2ms();
           }

           // 5ms周期任务：处理TCP/IP和Socket适配
           if (UserTimer_GetFlag5ms())
           {
               ethif_read_buf();
               
               TcpIp_MainFunction();
               SoAd_MainFunction();
               ComM_MainFunction(ComMUser_Eth);

               UserTimer_ClrFlag5ms();
           }

           // 10ms周期任务：发送测试PDU和服务发现
           if (UserTimer_GetFlag10ms())
           {
               TestCase_Send_EthPdu();
               Sd_MainFunction();  // 服务发现模块周期处理

               UserTimer_ClrFlag10ms();
           }
       }
   }

SomeIpXf相关的代码示例需要在LdCom添加函数实现：

.. code-block:: c
   :linenos:
   :emphasize-lines: 6-35

   #include "SomeIpXf.h"

   /* 实现一个加法运算服务 */
   void LdComRxInd_SdInstance0_AddMethodReq(const PduInfoType* PduInfoPtr)
   {
       if ((NULL_PTR != PduInfoPtr) && (NULL_PTR != PduInfoPtr->SduDataPtr))
       {
           AddMethodReq request;  // 定义加法请求结构体
           Rte_Cs_TransactionHandleType TransactionHandle;

           // 解析SOMEIP请求数据
           if (E_OK == SomeIpXf_Inv_AddMethodReq(&TransactionHandle, PduInfoPtr->SduDataPtr, PduInfoPtr->SduLength, &request))
           {
               uint8 data[128];  // 响应数据缓冲区
               uint32 sum = request.number_a + request.number_b;  // 执行加法运算
               uint16 length = 0;

               // 构建SOMEIP响应数据
               if (E_OK == SomeIpXf_AddMethodResp(&TransactionHandle, data, &length, &sum))
               {
                   PduInfoType pdu;  // 定义PDU结构体

                   pdu.SduLength = length;       // 设置响应数据长度
                   pdu.SduDataPtr = data;        // 指向响应数据缓冲区
                   pdu.MetaDataPtr = NULL_PTR;    // 无元数据

                   // 发送SOMEIP响应
                   LdCom_Transmit(SdInstance0_AddMethodResp, &pdu);
               }
           }
       }
   }

   // 响应发送完成回调
   void LdComTxConf_SdInstance0_AddMethodResp(void)
   {
       // 可添加发送完成后的处理逻辑
   }

验证结果
--------

#. 使用wireshark监控Offer Service正常多播发送，符合集成目标。

   |image80|

   图 验证结果-1

#. 使用调试助手，发送多播/单播 Find Service报文，都可以接收到单播的Offer
   Service报文，控制器返回正确，符合预期目标。

   |image81|

   图 验证结果-2

#. 使用调试助手，连接AddMthod
TCPserver，发送加法运算请求报文，控制器返回正确运算结果，符合预期目标。

   |image82|

   图 验证结果-3

.. |image1| image:: /_static/集成手册/集成手册_SOMEIP/image2.png
   :width: 5.76736in
   :height: 2.9125in


.. |image2| image:: /_static/集成手册/集成手册_SOMEIP/image3.png
   :width: 5.76736in
   :height: 2.9125in


.. |image3| image:: /_static/集成手册/集成手册_SOMEIP/image4.png
   :width: 5.76736in
   :height: 2.9125in


.. |image4| image:: /_static/集成手册/集成手册_SOMEIP/image5.png
   :width: 5.76736in
   :height: 2.9125in


.. |image5| image:: /_static/集成手册/集成手册_SOMEIP/image6.png
   :width: 5.76736in
   :height: 2.9125in


.. |image6| image:: /_static/集成手册/集成手册_SOMEIP/image7.png
   :width: 5.76736in
   :height: 2.9125in


.. |image7| image:: /_static/集成手册/集成手册_SOMEIP/image8.png
   :width: 5.76736in
   :height: 3.9125in


.. |image8| image:: /_static/集成手册/集成手册_SOMEIP/image9.png
   :width: 5.76736in
   :height: 6.9125in


.. |image9| image:: /_static/集成手册/集成手册_SOMEIP/image10.png
   :width: 5.76736in
   :height: 3.5125in


.. |image10| image:: /_static/集成手册/集成手册_SOMEIP/image11.png
   :width: 5.76736in
   :height: 2.9125in


.. |image11| image:: /_static/集成手册/集成手册_SOMEIP/image12.png
   :width: 5.76736in
   :height: 2.9125in


.. |image12| image:: /_static/集成手册/集成手册_SOMEIP/image13.png
   :width: 5.76736in
   :height: 3.9125in


.. |image13| image:: /_static/集成手册/集成手册_SOMEIP/image14.png
   :width: 5.76736in
   :height: 2.9125in


.. |image14| image:: /_static/集成手册/集成手册_SOMEIP/image15.png
   :width: 5.76736in
   :height: 2.9125in


.. |image15| image:: /_static/集成手册/集成手册_SOMEIP/image16.png
   :width: 5.76736in
   :height: 2.9125in


.. |image16| image:: /_static/集成手册/集成手册_SOMEIP/image17.png
   :width: 5.76736in
   :height: 2.9125in


.. |image17| image:: /_static/集成手册/集成手册_SOMEIP/image18.png
   :width: 4.76736in
   :height: 2.2125in


.. |image18| image:: /_static/集成手册/集成手册_SOMEIP/image19.png
   :width: 5.76736in
   :height: 2.9125in


.. |image19| image:: /_static/集成手册/集成手册_SOMEIP/image20.png
   :width: 5.76736in
   :height: 2.9125in


.. |image20| image:: /_static/集成手册/集成手册_SOMEIP/image21.png
   :width: 5.76736in
   :height: 2.9125in


.. |image21| image:: /_static/集成手册/集成手册_SOMEIP/image22.png
   :width: 5.76736in
   :height: 2.9125in


.. |image22| image:: /_static/集成手册/集成手册_SOMEIP/image23.png
   :width: 5.76736in
   :height: 2.9125in


.. |image23| image:: /_static/集成手册/集成手册_SOMEIP/image24.png
   :width: 5.76736in
   :height: 2.9125in


.. |image24| image:: /_static/集成手册/集成手册_SOMEIP/image25.png
   :width: 5.76736in
   :height: 2.9125in


.. |image25| image:: /_static/集成手册/集成手册_SOMEIP/image26.png
   :width: 5.76736in
   :height: 2.9125in


.. |image26| image:: /_static/集成手册/集成手册_SOMEIP/image27.png
   :width: 5.76736in
   :height: 2.9125in


.. |image27| image:: /_static/集成手册/集成手册_SOMEIP/image28.png
   :width: 5.76736in
   :height: 2.9125in


.. |image28| image:: /_static/集成手册/集成手册_SOMEIP/image29.png
   :width: 5.76736in
   :height: 2.9125in


.. |image29| image:: /_static/集成手册/集成手册_SOMEIP/image30.png
   :width: 5.76736in
   :height: 2.9125in


.. |image30| image:: /_static/集成手册/集成手册_SOMEIP/image31.png
   :width: 5.76736in
   :height: 2.9125in


.. |image31| image:: /_static/集成手册/集成手册_SOMEIP/image32.png
   :width: 5.76736in
   :height: 2.9125in


.. |image32| image:: /_static/集成手册/集成手册_SOMEIP/image33.png
   :width: 5.76736in
   :height: 2.9125in


.. |image33| image:: /_static/集成手册/集成手册_SOMEIP/image34.png
   :width: 5.76736in
   :height: 2.9125in


.. |image34| image:: /_static/集成手册/集成手册_SOMEIP/image35.png
   :width: 5.76736in
   :height: 2.9125in


.. |image35| image:: /_static/集成手册/集成手册_SOMEIP/image36.png
   :width: 5.76736in
   :height: 2.9125in


.. |image36| image:: /_static/集成手册/集成手册_SOMEIP/image37.png
   :width: 5.76736in
   :height: 2.9125in


.. |image37| image:: /_static/集成手册/集成手册_SOMEIP/image38.png
   :width: 5.76736in
   :height: 2.9125in


.. |image38| image:: /_static/集成手册/集成手册_SOMEIP/image39.png
   :width: 5.76736in
   :height: 2.9125in


.. |image39| image:: /_static/集成手册/集成手册_SOMEIP/image40.png
   :width: 5.76736in
   :height: 2.9125in


.. |image40| image:: /_static/集成手册/集成手册_SOMEIP/image41.png
   :width: 5.76736in
   :height: 2.9125in


.. |image41| image:: /_static/集成手册/集成手册_SOMEIP/image42.png
   :width: 5.76736in
   :height: 2.9125in


.. |image42| image:: /_static/集成手册/集成手册_SOMEIP/image43.png
   :width: 5.76736in
   :height: 2.9125in


.. |image43| image:: /_static/集成手册/集成手册_SOMEIP/image44.png
   :width: 5.76736in
   :height: 2.9125in


.. |image44| image:: /_static/集成手册/集成手册_SOMEIP/image45.png
   :width: 5.76736in
   :height: 2.9125in


.. |image45| image:: /_static/集成手册/集成手册_SOMEIP/image46.png
   :width: 5.76736in
   :height: 2.9125in


.. |image46| image:: /_static/集成手册/集成手册_SOMEIP/image47.png
   :width: 5.76736in
   :height: 2.9125in


.. |image47| image:: /_static/集成手册/集成手册_SOMEIP/image48.png
   :width: 5.76736in
   :height: 2.9125in


.. |image48| image:: /_static/集成手册/集成手册_SOMEIP/image49.png
   :width: 5.76736in
   :height: 2.9125in


.. |image49| image:: /_static/集成手册/集成手册_SOMEIP/image50.png
   :width: 5.76736in
   :height: 2.9125in


.. |image50| image:: /_static/集成手册/集成手册_SOMEIP/image51.png
   :width: 5.76736in
   :height: 2.9125in


.. |image51| image:: /_static/集成手册/集成手册_SOMEIP/image52.png
   :width: 5.76736in
   :height: 2.9125in


.. |image52| image:: /_static/集成手册/集成手册_SOMEIP/image53.png
   :width: 5.76736in
   :height: 2.9125in


.. |image53| image:: /_static/集成手册/集成手册_SOMEIP/image54.png
   :width: 5.76736in
   :height: 2.9125in


.. |image54| image:: /_static/集成手册/集成手册_SOMEIP/image55.png
   :width: 5.76736in
   :height: 2.9125in


.. |image55| image:: /_static/集成手册/集成手册_SOMEIP/image56.png
   :width: 5.76736in
   :height: 2.9125in


.. |image56| image:: /_static/集成手册/集成手册_SOMEIP/image57.png
   :width: 5.76736in
   :height: 2.9125in


.. |image57| image:: /_static/集成手册/集成手册_SOMEIP/image58.png
   :width: 5.76736in
   :height: 2.9125in


.. |image58| image:: /_static/集成手册/集成手册_SOMEIP/image59.png
   :width: 5.76736in
   :height: 2.9125in


.. |image59| image:: /_static/集成手册/集成手册_SOMEIP/image60.png
   :width: 5.76736in
   :height: 2.9125in


.. |image60| image:: /_static/集成手册/集成手册_SOMEIP/image61.png
   :width: 5.76736in
   :height: 2.9125in


.. |image61| image:: /_static/集成手册/集成手册_SOMEIP/image62.png
   :width: 5.76736in
   :height: 2.9125in


.. |image62| image:: /_static/集成手册/集成手册_SOMEIP/image63.png
   :width: 5.76736in
   :height: 2.9125in


.. |image63| image:: /_static/集成手册/集成手册_SOMEIP/image64.png
   :width: 5.76736in
   :height: 2.9125in


.. |image64| image:: /_static/集成手册/集成手册_SOMEIP/image65.png
   :width: 5.76736in
   :height: 2.9125in


.. |image65| image:: /_static/集成手册/集成手册_SOMEIP/image66.png
   :width: 5.76736in
   :height: 2.9125in


.. |image66| image:: /_static/集成手册/集成手册_SOMEIP/image67.png
   :width: 5.76736in
   :height: 2.9125in


.. |image67| image:: /_static/集成手册/集成手册_SOMEIP/image68.png
   :width: 5.76736in
   :height: 2.9125in


.. |image68| image:: /_static/集成手册/集成手册_SOMEIP/image69.png
   :width: 5.76736in
   :height: 2.9125in


.. |image69| image:: /_static/集成手册/集成手册_SOMEIP/image70.png
   :width: 5.76736in
   :height: 2.9125in


.. |image70| image:: /_static/集成手册/集成手册_SOMEIP/image71.png
   :width: 5.76736in
   :height: 2.9125in


.. |image71| image:: /_static/集成手册/集成手册_SOMEIP/image72.png
   :width: 5.76736in
   :height: 2.9125in


.. |image72| image:: /_static/集成手册/集成手册_SOMEIP/image73.png
   :width: 5.76736in
   :height: 2.9125in


.. |image73| image:: /_static/集成手册/集成手册_SOMEIP/image74.png
   :width: 5.76736in
   :height: 2.9125in


.. |image74| image:: /_static/集成手册/集成手册_SOMEIP/image75.png
   :width: 5.76736in
   :height: 2.9125in


.. |image75| image:: /_static/集成手册/集成手册_SOMEIP/image76.png
   :width: 5.76736in
   :height: 2.9125in


.. |image76| image:: /_static/集成手册/集成手册_SOMEIP/image77.png
   :width: 5.76736in
   :height: 2.9125in


.. |image77| image:: /_static/集成手册/集成手册_SOMEIP/image78.png
   :width: 5.76736in
   :height: 2.9125in


.. |image78| image:: /_static/集成手册/集成手册_SOMEIP/image79.png
   :width: 5.76736in
   :height: 2.9125in


.. |image79| image:: /_static/集成手册/集成手册_SOMEIP/image80.png
   :width: 3.76736in
   :height: 2.9125in


.. |image80| image:: /_static/集成手册/集成手册_SOMEIP/image81.png
   :width: 5.76736in
   :height: 2.9125in


.. |image81| image:: /_static/集成手册/集成手册_SOMEIP/image82.png
   :width: 5.76736in
   :height: 2.9125in


.. |image82| image:: /_static/集成手册/集成手册_SOMEIP/image83.png
   :width: 5.76736in
   :height: 5.9125in
