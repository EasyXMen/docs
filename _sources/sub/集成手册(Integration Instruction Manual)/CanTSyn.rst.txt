================
CanTSyn
================

目标
====

本集成手册用于指导客户进行CanTSyn集成，文档主要包括的内容为：协议栈集成指导、基于普通应用的集成示例讲解。

由于各项目的需求不同，集成示例不会针对于特定的商业项目做详细讲解。

缩写词和术语
============

表  缩写词和术语

+-----------------+------------------------------------------------------+
| **缩写词/术语** | **描述**                                             |
+=================+======================================================+
| CanIf           | Can Interface Can通信的接口模块                      |
+-----------------+------------------------------------------------------+
| CanTSyn         | TimeSyncOverCAN CAN时间同步模块                      |
+-----------------+------------------------------------------------------+
| StbM            | SynchronizedTimeBaseManager 同步时基管理器           |
+-----------------+------------------------------------------------------+

参考文档
========

[1] 参考手册_CanTSyn.pdf

[2] 参考手册_StbM.pdf

协议栈集成
==========

项目交付的内容为：CanTSyn协议栈源码和ORIENTAIS
Studio配置工具。协议栈细分为协议栈的各模块及其对应的配置工具模块。

CanTSyn协议栈各配置模块的功能介绍。

使用协议栈源码和配置工具，进行协议栈的集成的步骤。

表 CanTSyn协议栈各配置模块介绍

+------------+-----------------------------------------------------------------------------------------------------+
| **模块名** | **功能**                                                                                            |
+============+=====================================================================================================+
| Can        | CAN驱动配置。                                                                                       |
+------------+-----------------------------------------------------------------------------------------------------+
| CanIf      | CanIf模块主要处理上层模块与底层驱动的之间PDU的传递，为上层模块提供统一的接口来管理不同的CAN硬件模块 |
+------------+-----------------------------------------------------------------------------------------------------+
| EcuC       | 用于辅助配置工具完成配置的模块。主要提供Pdu的定义，其它模块通过关联EcuC中Pdu，相互关联起来。        |
+------------+-----------------------------------------------------------------------------------------------------+
| CanTSyn    | CAN时间同步模块                                                                                     |
+------------+-----------------------------------------------------------------------------------------------------+
| StbM       | 同步时基管理器                                                                                      |
+------------+-----------------------------------------------------------------------------------------------------+

表 CanTSyn协议栈集成的步骤

+----------+----------------------------------------+------------------------------------------------------+
| **步骤** | **操作**                               | **说明**                                             |
+==========+========================================+======================================================+
| 1        | ORIENTAIS                              | 若配置工具已经搭建，则仅需进行协议栈模块的加载操作。 |
|          | Stuido配置工具工程搭建和协议栈模块加载 |                                                      |
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

#. 新建工程如下所示，上一步添加的模块已经被加入到工程中。

   |image9|

   图 新建工程-9

模块配置及代码生成
------------------

模块配置
~~~~~~~~

模块的具体配置，取决于具体的项目需求。该协议栈各模块配置项的详细介绍。

表 协议栈各模块配置参考文档

+----------+----------------------------------------+-------------------+
| **模块** | **参考文档**                           | **说明**          |
+==========+========================================+===================+
| Can      | MCAL对应的Can配置手册                  |                   |
+----------+----------------------------------------+-------------------+
| Gpt      | MCAL对应的Gpt配置手册                  |                   |
+----------+----------------------------------------+-------------------+
| CanIf    | 集成手册_Can通信.pdf                   |                   |
+----------+----------------------------------------+-------------------+
| EcuC     | 集成手册_Can通信.pdf                   |                   |
+----------+----------------------------------------+-------------------+
| CanTSyn  | 参考手册_CanTSyn.pdf                   |                   |
+----------+----------------------------------------+-------------------+
| StbM     | 参考手册_StbM.pdf                      |                   |
+----------+----------------------------------------+-------------------+

配置代码生成
~~~~~~~~~~~~

#. 在ORIENTAIS Studio主界面左方，选择对应的协议栈，单击右键弹出Validate
   All和GenerateAll菜单。

   |image10|

   图 配置代码的生成-1

#. 选择Validate
   All对本协议栈各配置选项进行校验，没有错误提示信息即校验通过。若有错误信息，请按照错误提示修改。

#. 选择Generate
   All，生成配置文件。右下角的Console窗口输出生成的配置文件信息。

   |image11|

   图 配置代码的生成-2

#. 在工程config文件夹，可查看生成的配置文件。

   |image12|

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

对于集成过程中，协议栈特殊要求和用户经常出现的问题，归类总结形成 表
协议栈集成约束清单。用户需逐一排查表中的约束项，以避免集成问题出现。

表 CanTSyn协议栈集成约束清单

+----------+----------+-----------------------------------------------------------------------------------+
| **编号** | **类别** | **约束限制**                                                                      |
+==========+==========+===================================================================================+
| **1**    | 头文件   | - 添加协议栈代码之后，用户需更新集成开发工具中的头文件路径。                      |
|          |          |                                                                                   |
|          |          | - 调用协议栈API的源文件，需要包含协议栈的头文件。                                 |
+----------+----------+-----------------------------------------------------------------------------------+
| **2**    | 初始化   | CanTSyn_Init和StbM_Init初始化前需要确保Can和Gpt已经初始化                         |
+----------+----------+-----------------------------------------------------------------------------------+
| **3**    | 周期函数 | CanTSyn_MainFunction和StbM_MainFunction按照需求放置到相应的周期任务中，一般为10ms |
+----------+----------+-----------------------------------------------------------------------------------+

集成示例
========

本章节通过CanTSyn协议栈为例，向用户展示CanTSyn协议栈的集成过程。用户可以据此熟悉CanTSyn协议栈配置工具的配置过程，以及如何应用配置工具生成的配置文件。

为让用户更清晰的了解工具的使用，所用的配置均逐一手动完成。关于Can驱动的配置，请参考Can配置手册。关于Gpt驱动的配置，请参考Gpt配置手册。CanIf配置的具体操作请参照《集成手册_Can通信.pdf》。

.. note::
   **本示例不代表用户的实际配置情况，用户需要根据自己的实际需求，决定各个参数的配置。**

集成目标
--------

通过Canoe模拟CanTSyn主节点，向本示例的从节点发送时间同步报文，从节点获取主节点同步的时间。由于时间同步的从节点不向外发送时间，故通过一帧CAN
ID为0x666的CAN报文将同步后的时间转发出来。

模块的配置
----------

新建配置工程及模块加载操作，请参考本文档章节（模块配置及代码生成）。此次仅说明如何配置，模块的配置项具体示意参见《集成手册_CanTSyn.pdf》和《集成手册_StbM.pdf》。

CanTSyn模块配置
~~~~~~~~~~~~~~~

#. 双击CanTSyn模块，打开CanTSyn模块的配置界面。

   |image13|

   图 CanTSynGeneral配置界面

#. 在CanTSynGeneral下，有CanTSynDevErrorDetect、CanTSynMainFunctionPeriod和CanTSynVersionInfoApi
   、CanTSynR19CbkVersion、CanTSynMultiplePartitionEnabled五个配置项。

#. 将CanTSynMainFunctionPeriod配置为0.01，其他配置项保持默认。

   |image14|

   图 CanTSynGlobalTimeDomain配置界面

#. CanTSynGlobalTimeDomain配置如下图所示：

   |image15|

   图 CanTSynGlobalTimeDomain配置

#. CanTSynGlobalTimeDomain->CanTSynGlobalTimeFupDataIDList->CanTSynGlobalTimeFupDataIDListElements中的配置(使用CRC时)，根据客户需求去填写CRC值。

   |image16|

   图 SynGlobalTimeFupDataIDListElements的配置

#. CanTSynGlobalTimeSlaves->CanTSynGlobalTimeSlave的配置（做从节 点）：

   |image17|

   图 CanTSynGlobalTimeSlave的配置

#. CanTSynGlobalTimeSlaves->CanTSynGlobalTimeSlavePdus->CanTSynGlobalTimeSlavePdu的配置：

   |image18|

   图 CanTSynGlobalTimeSlavePdu的配置

#. CanTSynGlobalTimeSyncDataIDLists->CanTSynGlobalTimeSyncDataIDL
   ist->CanTSynGlobalTimeSyncDataIDListElements的配置(使用CRC时)根
   据客户需求去填写CRC值。

   |image19|

   图 CanTSynGlobalTimeSyncDataIDListElements的配置

#. CanTSynGlobalTimeMasters->CanTSynGlobalTimeMaster的配置（做主节
   点）：

   CanTSynCyclicMsgResumeTime：在即时传输之前，第一个常规周期时间的消息传输发生的时间。

   CanTSynGlobalTimeDebounceTime：SYNC报文和FUP报文之间的间隔时间。

   CanTSynGlobalTimeTxCrcSecured：选择是否支持CRC。

   CanTSynGlobalTimeTxPeriod：同步报文周期。

   CanTSynImmediateTimeSync：启用/禁用在CanTSyn_MainFunction()中对StbM_GetTimeBaseUpdateCounter()的周期轮询。

   CanTSynMasterConfirmationTimeout：这表示每次传输Timesync消息后的确认超时时间。

   |image20|

   图 CanTSynGlobalTimeMaster的配置

#. CanTSynGlobalTimeMaster->CanTSynGlobalTimeMasterPdus->CanTSynGloa
   lTimeMasterPdu的配置：

   |image21|

   图 CanTSynGlobalTimeMasterPdu的配置

StbM模块的配置
~~~~~~~~~~~~~~

#. 双击StbM模块，打开StbM模块的配置界面。

   |image22|

   图 StbMGeneral的配置界面

#. 在StbMGeneral的配置。若使用GPT时钟，需打开StbMGptTimerRef，并
   选择mcal配置的Gpt时钟；若用Eth硬件时钟，则不勾选。

   |image23|

   图 StbMGeneral的配置

#. StbMSynchronizedTimeBases->StbMSynchronizedTimeBase的配置。

   |image24|

   图 StbMSynchronizedTimeBase配置界面

#. StbMSynchronizedTimeBases->StbMSynchronizedTimeBase->StbMLocal
   TimeClocks->StbMLocalTimeClock的配置：

#. StbMClockFrequency中填写StbM所引用的Gpt定时器的时钟频率。若是
   Eth时钟则默认1000000000。

#. StbMLocalTimeHardware引用所需要引用的Gpt的定时器通道。若是Eth
   时钟则默认1。

   |image25|

   图 StbMLocalTimeClock配置界面

#. StbMSynchronizedTimeBases->StbMSynchronizedTimeBase->StbMLocal
   TimeClocks->StbMTimeCorrection的配置：

   StbMAllowMasterRateCorrection如果主节点启用correction功能则需要开启。

   StbMMasterRateDeviationMax填写由
   StbM_SetRateCorrection设置的速率偏差值的最大允许绝对值。

   StbMOffsetCorrectionAdaptionInterval填写适应性的速率矫正足以消除速率和时间偏差值的时间区间。

   StbMOffsetCorrectionJumpThreshold用于决定使用什么样的矫正方式。偏差值若小于此值，则在定义的时间周期内使用线性缩减（linear
   reduction）矫正。若大于此值，则以跳跃的方式立即设置正确的时间和速率。

   StbMRateCorrectionMeasurementDuration填写用于计算速率差的时间区间。

#. StbMRateCorrectionsPerMeasurementDuration填写同时进行速率测量的
   次数，以确定当前速率偏差。

   |image26|

   图 StbMLocalTimeCorrection配置界面

源代码集成
----------

项目交付给用户的工程结构如下：

|image27|

图 工程结构目录

- BSW目录，存放模块相关的源代码和配置代码。可以看到Source目录下各个文件夹下是各个模块的源代码。

- BSW下的Config->BSW_Config目录，用于存放配置工具生成的配置文件

CanTSyn协议栈源代码集成步骤如下：

#. 将MCAL生成的CAN、GPT模块配置文件和ORIENTAIS
   Studio生成的配置文件复制到对应的文件夹中；

#. 将MCAL提供的CAN模块源码和普华提供的协议栈源代码文件复制到对应的文件夹中。

#. 添加新增加的模块的代码头文件路径到工程设置中

协议栈调度集成
--------------

CanTSyn协议栈调度集成步骤如下：

#. 协议栈调度集成，需要逐一排查并实现表 协议栈集成约束清单
   所罗列的问题，以避免集成出现差错。

#. 编译链接代码，将生成的elf文件烧写进芯片。

CanTSyn协议栈有关的代码，在下方的main.c文件中给出重点标注。

.. note::
   **本示例中，CanTSyn协议栈初始化的代码和启动通信的代码置于main.c文件，并不代表其他项目同样适用于将其置于main.c文件中。**

.. code-block:: c
   :linenos:
   :emphasize-lines: 6-10, 26-29, 32, 38-39, 42-45, 57-58, 61-71

   #include <machine/wdtcon.h>
   #include "Mcu.h"
   #include "Port.h"

   // CanTSyn协议栈相关模块头文件
   #include "Can_17_MCanP.h"
   #include "CanIf.h"
   #include "Gpt.h"
   #include "StbM.h"
   #include "CanTSyn.h"

   StbM_TimeStampType timestamp;
   StbM_UserDataType userData;
   Uint8 Data[8] = {0};
   Can_PduType PduInfo = {0,8,0x666,&Data[0]};

   int main(void)
   {
       /*Initialize ECUM Module*/
       EcuM_Init(&EcuM_ConfigAlternative[0]);

       /*Initialize FlsLoader*/
       FlsLoader_Init(NULL_PTR);

       // 初始化Can、CanIf、CanTSyn、StbM模块
       StbM_Init(&StbM_Config);  
       Can_17_MCanP_Init(&Can_17_MCanP_ConfigRoot[0]);
       CanIf_Init(&CanIf_InitCfgSet);
       CanTSyn_Init(&CanTSyn_config);   

       // 打开通信（主节点使用）
       CanIf_SetControllerMode(0, CANIF_CS_STARTED);

       Gpt_EnableNotification(GptConf_GptChannel_Gpt_1ms);
       Gpt_StartTimer(GptConf_GptChannel_Gpt_1ms, 100000);
       Gpt_StartTimer(GptChannelConfiguration_STBM, 0xFFFFFFu);

       StbM_TimeStampType test1 = {0u};
       StbM_UserDataType  test2 = {0u};

       // 主节点需要添加初始化授时
       test1.secondsHi = 0;
       test1.seconds = 1696903810;  // 初始时间戳（秒）
       test1.nanoseconds = 0;       // 初始时间戳（纳秒）
       StbM_SetGlobalTime(0,&test1,&test2);

       /* infinite loop */
       while (1)
       {
           if(Gpt_1msFlag == TRUE)
           {
               Gpt_1msFlag = FALSE;
           }
           if(Gpt_10msFlag == TRUE)
           {
               // CanTSyn、StbM模块周期处理函数
               CanTSyn_MainFunction();
               StbM_MainFunction();

               // 做从节点时的测试代码：StbM_GetCurrentTime获取时间，将同步到的时间通过0x666报文转发出来
               StbM_GetCurrentTime(0, &timestamp,&userData);
               PduInfo.sdu[0] = (uint8)((StbM_TimeStamp.seconds & 0xff000000) >> 24);
               PduInfo.sdu[1] = (uint8)((StbM_TimeStamp.seconds & 0x00ff0000) >> 16);
               PduInfo.sdu[2] = (uint8)((StbM_TimeStamp.seconds & 0x0000ff00) >> 8);
               PduInfo.sdu[3] = (uint8)((StbM_TimeStamp.seconds & 0x000000ff));
               PduInfo.sdu[4] = (uint8)((StbM_TimeStamp.nanoseconds & 0xff000000) >> 24);
               PduInfo.sdu[5] = (uint8)((StbM_TimeStamp.nanoseconds & 0x00ff0000) >> 16);
               PduInfo.sdu[6] = (uint8)((StbM_TimeStamp.nanoseconds & 0x0000ff00) >> 8);
               PduInfo.sdu[7] = (uint8)((StbM_TimeStamp.nanoseconds & 0x000000ff));

               Can_Write(2, &PduInfo);
           }
       }
       return 1;
   }

验证结果
--------

根据集成目标，能够跟Canoe正常通信，以下是时间同步的同步log.

|image28|

图 验证结果

.. |image1| image:: /_static/集成手册/集成手册_CANTSyn/image2.png
   :width: 5.76736in
   :height: 3.11736in
.. |image2| image:: /_static/集成手册/集成手册_CANTSyn/image3.png
   :width: 5.76736in
   :height: 3.11389in
.. |image3| image:: /_static/集成手册/集成手册_CANTSyn/image4.png
   :width: 4.26818in
   :height: 4.11783in
.. |image4| image:: /_static/集成手册/集成手册_CANTSyn/image5.png
   :width: 4.4128in
   :height: 3.66201in
.. |image5| image:: /_static/集成手册/集成手册_CANTSyn/image6.png
   :width: 5.39516in
   :height: 2.53093in
.. |image6| image:: /_static/集成手册/集成手册_CANTSyn/image7.png
   :width: 4.29931in
   :height: 1.97778in
.. |image7| image:: /_static/集成手册/集成手册_CANTSyn/image8.png
   :width: 3.5041in
   :height: 3.37381in
.. |image8| image:: /_static/集成手册/集成手册_CANTSyn/image9.png
   :width: 3.11763in
   :height: 4.16701in
.. |image9| image:: /_static/集成手册/集成手册_CANTSyn/image10.png
   :width: 2.77741in
   :height: 3.28101in
.. |image10| image:: /_static/集成手册/集成手册_CANTSyn/image11.png
   :width: 3.77191in
   :height: 1.80023in
.. |image11| image:: /_static/集成手册/集成手册_CANTSyn/image12.png
   :width: 3.05251in
   :height: 1.37519in
.. |image12| image:: /_static/集成手册/集成手册_CANTSyn/image13.png
   :width: 3.43559in
   :height: 3.71643in
.. |image13| image:: /_static/集成手册/集成手册_CANTSyn/image14.png
   :width: 5.61077in
   :height: 2.80234in
.. |image14| image:: /_static/集成手册/集成手册_CANTSyn/image15.png
   :width: 5.76736in
   :height: 3.77292in
.. |image15| image:: /_static/集成手册/集成手册_CANTSyn/image16.png
   :width: 5.76736in
   :height: 1.55903in
.. |image16| image:: /_static/集成手册/集成手册_CANTSyn/image17.png
   :width: 5.76736in
   :height: 2.85417in
.. |image17| image:: /_static/集成手册/集成手册_CANTSyn/image18.png
   :width: 5.76736in
   :height: 1.54514in
.. |image18| image:: /_static/集成手册/集成手册_CANTSyn/image19.png
   :width: 5.43502in
   :height: 0.94792in
.. |image19| image:: /_static/集成手册/集成手册_CANTSyn/image20.png
   :width: 5.76736in
   :height: 2.94444in
.. |image20| image:: /_static/集成手册/集成手册_CANTSyn/image21.png
   :width: 5.76736in
   :height: 2.12917in
.. |image21| image:: /_static/集成手册/集成手册_CANTSyn/image22.png
   :width: 4.864in
   :height: 0.84807in
.. |image22| image:: /_static/集成手册/集成手册_CANTSyn/image23.png
   :width: 5.76736in
   :height: 3.31736in
.. |image23| image:: /_static/集成手册/集成手册_CANTSyn/image24.png
   :width: 3.48319in
   :height: 2.13689in
.. |image24| image:: /_static/集成手册/集成手册_CANTSyn/image25.png
   :width: 5.76736in
   :height: 3.03472in
.. |image25| image:: /_static/集成手册/集成手册_CANTSyn/image26.png
   :width: 5.76736in
   :height: 1.33819in
.. |image26| image:: /_static/集成手册/集成手册_CANTSyn/image27.png
   :width: 5.12411in
   :height: 2.40737in
.. |image27| image:: /_static/集成手册/集成手册_CANTSyn/image28.png
   :width: 3.17708in
   :height: 3.13542in
.. |image28| image:: /_static/集成手册/集成手册_CANTSyn/image29.png
   :width: 5.76736in
   :height: 3.94583in
