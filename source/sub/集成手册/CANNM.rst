===================
CANNM_集成手册
===================



 |                             |
   +----------------------+-----------------+-----------------------------+

.. _校验-1:

校验
^^^^

CanIf模块到此配置结束。可以在模块上右键，然后选择校验，查看是否配置有错误。校验后提示窗口没有错误信息，即校验通过。

ComM模块配置
~~~~~~~~~~~~

双击ComM模块，打开ComM模块的配置界面。

ComMGeneral配置
^^^^^^^^^^^^^^^

若不使用版本获取API，只需要去掉ComMVersionInfoApi，其他保持默认即可。

|image12|

   图 5‑18配置ComMGeneral

ComMConfigSet配置
^^^^^^^^^^^^^^^^^

#. 配置ComMConfigSet

..

   由于不使用PNC功能，因此不配置。采取默认配置即可。

|image13|

   图 5‑19配置ComMConfigSet

   该容器下，需要配置的容器有ComMChannels和ComMUsers。ComMChannels主要配置的是总线的类型和ComM函数的调用周期。ComMUsers是用户用于请求通信模式。

2. ComMUsers

..

   该容器下，已经默认创建了一个User。若有多个通道，可在ComMConfigSet容器上右键创建。每个通道都需要关联一个User。该容器下，保持默认即可。

|image14|

   图 5‑20配置ComMUsers

3. 配置ComMChannels

..

   该容器下，已经默认创建了一个通道。若有多个通道，可在ComMConfigSet容器上右键创建。此Can网络管理栈DEMO只配置了一个通道。

|image15|

   图 5‑21配置ComMChannels第一步

该容器下，只需要配置ComMBusType和ComM周期调用函数周期，如下所示：

|image16|

   图 5‑22配置ComMChannels第二步

4. 配置ComMNetworkManagements

..

   该容器下，已经默认创建了一个ComMNetworkManagement对象。保持默认即可。

   若该通道不是有网络管理功能，请将ComMNmVariant设置成LIGHT。此Autosar
   NM栈DEMO需要配置成FULL。

|image17|

   图 5‑23配置ComMNetworkManagements

5. 配置ComMUserPerChannels

..

   该容器下，已经默认创建了一个ComMUserPerChannels对象。将对应的User关联到该通道。

.. figure:: ../../_static/集成手册/CANNM/image37.png
   :width: 5.76736in
   :height: 3.23819in

   图 5‑24配置ComMUserPerChannels

.. _校验-2:

校验
^^^^

ComM模块到此配置结束。可以在模块上右键，然后选择校验，查看是否配置有错误。校验后提示窗口没有错误信息，即校验通过。

Nm模块配置
~~~~~~~~~~

双击Nm模块，打开Nm模块的配置界面。

NmGlobalConfig配置
^^^^^^^^^^^^^^^^^^

该页面下有3个容器：NmGlobalConstantss、NmGlobalFeatures和NmGlobalPropertiess。

#. 配置NmGlobalConstants

..

   该示例中只有一个通道，因此配置为1。

.. figure:: ../../_static/集成手册/CANNM/image38.png
   :width: 5.76736in
   :height: 3.08542in

   图 5‑25配置NmGlobalConstants

2. 配置NmGlobalFeatures

..

   该容器主要配置网络管理的功能，若要开通相应的功能，就勾选相应的配置项。这里，Nm的配置如下：

.. figure:: ../../_static/集成手册/CANNM/image39.png
   :width: 5.76736in
   :height: 2.84375in

   图 5‑26配置NmGlobalFeatures

3. 配置NmGlobalPropertiess

..

   保持默认。

NmChannelConfig配置
^^^^^^^^^^^^^^^^^^^

#. 配置NmChannelConfig

..

   该容器主要配置NmComChannelRef，将ComM配置的通道关联到该模块。

.. figure:: ../../_static/集成手册/CANNM/image40.png
   :width: 5.76736in
   :height: 2.90139in

   图 5‑27配置NmChannelConfig

2. 配置NmGenericBusNmConfig

..

   该容器主要配置通道的网络管理的类型。首先创建一个NmGenericBusNmConfig对象。

图 5‑28配置NmGenericBusNmConfig

.. figure:: ../../_static/集成手册/CANNM/image42.png
   :width: 5.76736in
   :height: 3.17986in

   图 5‑29配置NmGenericBusNmConfig

.. _校验-3:

校验
^^^^

Nm模块到此配置结束。可以在模块上右键，然后选择校验，查看是否配置有错误。校验后提示窗口没有错误信息，即校验通过。

CanNM模块配置
~~~~~~~~~~~~~

 CanNmGlobalConfig配置
^^^^^^^^^^^^^^^^^^^^^^

#. 配置CanNmGlobalConfig

..

   该容器保持默认，CanNM主函数周期设置成5ms。

.. figure:: ../../_static/集成手册/CANNM/image43.png
   :width: 5.76736in
   :height: 3.12361in

   图 5‑30配置CanNmGlobalConfig

2. 配置CanNmChannelConfig

..

   该容器的各种配置项，来自于客户需求，例如图例的配置需求为：NM报文快发时间为20ms，快发次数为5次，NM周期报文时间为500ms，NM报文的节点ID是xxD(此处节点ID取决于网络管理的ID号，例如0x405，节点ID为5)，Nm_Repeat模式等待时间为2.1s，Ready
   Sleep状态进入Prepare Bus_Sleep状态时间为2s，Prepare
   Bus_Sleep状态进入Bus_Sleep状态时间为5s。

.. figure:: ../../_static/集成手册/CANNM/image44.png
   :width: 5.76736in
   :height: 2.92917in

   图 5-31配置CanNmGlobalConfig

|image18|

图 5‑32配置CanNmGlobalConfig

3. 配置CanNmRxPdus和CanNmTxPdus

..

   此容器的Pdu参考映射到EcuC中建立的Pdu当中

.. figure:: ../../_static/集成手册/CANNM/image46.png
   :width: 5.76736in
   :height: 2.53194in

   图 5‑33配置CanNmGlobalConfig

.. _校验-4:

校验
^^^^

CanNM模块到此配置结束。可以在模块上右键，然后选择校验，查看是否配置有错误。校验后提示窗口没有错误信息，即校验通过。

源代码集成
---------

项目交付给用户的工程结构如下：

|image19|

-  BSW目录，这个目录放置所有基础软件相关代码，除了MCAL、Config文件夹之外，均按bsw源码路径放置

-  ASW目录，存放应用代码

-  Config目录，存放mcal和bsw生成的动态代码。

-  MCAL目录，存放mcal的动态代码

网络管理栈源代码集成步骤如下：

#. 将5.2章节中EB MCAL生成的CAN模块配置文件和ORIENTAIS
   Configurator，生成的配置文件复制到Config/BSW_Config文件夹中。

#. 将MCAL提供的CAN模块源码和项目提供的协议栈源代码文件复制到BS
   W和MCAL文件夹中。

协议栈调度集成
-------------

通信栈调度集成步骤如下：

#. 协议栈调度集成，需要逐一排查并实现表 5‑1协议栈集成约束清单
   所罗列的问题，以避免集成出现差错。

#. 编译链接代码，将生成的elf文件烧写进芯片。

网络管理栈有关的代码，在下方的main.c文件中给出重点标注。

**注意 :
本示例中，网络管理栈初始化的代码和启动通信的代码置于main.c文件，并不代表其他项目同样适用于将其置于main.c文件中。**

**#include <stdlib.h>**

**#include "Std_Types.h"**

**#include "Mcu.h"**

**#include "Port.h"**

**#include "Dio.h"**

**#include "Irq.h"**

**#include "Gpt.h"**

**#include "Gtm.h"**

**#include "Adc.h"**

**#include "Can_17_MCanP.h"**

**#include "CanIf.h"**

**#include "ComM_EcuMBswM.h"**

**#include "ComM.h"**

**#include "CanSM.h"**

**#include "CanNm.h"**

**#include "Nm.h"**

**#include "CanNm_Internal.h"**

**#include "Bsw_Test.h"**

**#include "Icu_17_GtmCcu6.h"**

**#include "Pwm_17_Gtm.h"**

**#include "Spi.h"**

**int** **main**\ (**void**)

{

Mcu_Init(Mcu_ConfigRoot);

Mcu_InitClock(0);

while (MCU_PLL_UNLOCKED == Mcu_GetPllStatus())

{

/\* wait for PLL locked \*/

}

Mcu_DistributePllClock();

/\* IrqGtm_Init \*/

IrqGtm_Init();

/\* Port Initialize \*/

Port_Init(&Port_ConfigRoot[0]);

Gpt_Init(&Gpt_ConfigRoot[0]);

Gpt_EnableNotification(GptConf_GptChannel_GptChannelConfiguration_0);

Gpt_StartTimer(GptConf_GptChannel_GptChannelConfiguration_0, 6250);

Can_17_MCanP_Init(&Can_17_MCanP_ConfigRoot[0]);

Icu_17_GtmCcu6_Init(&Icu_ConfigRoot[0]);

Icu_17_GtmCcu6_StartSignalMeasurement(ICU_17_GTMCCU6_INSTANCE_ID);

Pwm_17_Gtm_Init(&Pwm_ConfigRoot[0]);

Spi_Init(&Spi_ConfigRoot[0]);

Mcal_EnableAllInterrupts();

CanIf_Init(&CanIf_InitCfgSet);

memset(buff, 0, 8*sizeof(uint8));

Nm_Init(&Nm_Config);

CanSM_Init(&CanSM_Config);

ComM_Init(&ComM_Config);

CanNm_Init(&CanNm_PBConfig);

ComM_RequestComMode(ComMChannel_0, COMM_FULL_COMMUNICATION);

ComM_CommunicationAllowed(ComMUser_0, TRUE);

/\* infinite loop \*/

**while** (1)

{

if (TRUE == Gpt_1msFlag)

{

Gpt_1msFlag = FALSE;

CanSM_MainFunction();

Can_17_MCanP_MainFunction_Read();

Can_17_MCanP_MainFunction_Write();

Can_17_MCanP_MainFunction_BusOff();

Can_17_MCanP_MainFunction_Wakeup();

if(wakeuplag==TRUE)

{

wakeuplag=0;

ComM_RequestComMode(0, COMM_FULL_COMMUNICATION);

}

}

if (TRUE == Gpt_5msFlag)

{

Gpt_5msFlag = FALSE;

CanNm_MainFunction();

ComM_MainFunction(0);

Nm_GetPduData(0,buff);

if(buff[2]==0x01)

{

for(loop = 0x0u; loop < CANNM_DEFAULT_NMPDU_LEN; loop++)

{

CanNm_ChRunTime[0].rxPduData[loop]=0;

}

ComM_RequestComMode(0, COMM_NO_COMMUNICATION);

}

if(buff[2]==0x02)

{

for(loop = 0x0u; loop < CANNM_DEFAULT_NMPDU_LEN; loop++)

{

CanNm_ChRunTime[0].rxPduData[loop]=0;

}

ComM_RequestComMode(0, COMM_SILENT_COMMUNICATION);

}

if(buff[2]==0x03)

{

for(loop = 0x0u; loop < CANNM_DEFAULT_NMPDU_LEN; loop++)

{

CanNm_ChRunTime[0].rxPduData[loop]=0;

}

ComM_RequestComMode(0, COMM_FULL_COMMUNICATION);

}

}

if (TRUE == Gpt_10msFlag)

{

Gpt_10msFlag = FALSE;

}

if (TRUE == Gpt_200msFlag)

{

Gpt_200msFlag = FALSE;

}

if (TRUE == Gpt_1000msFlag)

{

Gpt_1000msFlag = FALSE;

}

验证结果
-------

根据集成目标，共配置了2个报文，其中1个网络管理发送报文，1个网络管理接收报文。

#. 系统启动后有一个报文发送（CANNM_Tx_Message1），ID
   0x400，周期100ms，初始化值和设置一致

.. figure:: ../../_static/集成手册/CANNM/image48.png
   :width: 5.76736in
   :height: 3.96333in

   图 5-34 验证结果-1

2. 发送睡眠指令后，过一段时间后，节点会停止发送网络管理报文。如下图：

.. figure:: ../../_static/集成手册/CANNM/image49.png
   :width: 5.40297in
   :height: 3.71942in

   图 5-35 验证结果-2

3. 发送唤醒指令后，过一段时间后，节点会继续发送网络管理报文。

.. figure:: ../../_static/集成手册/CANNM/image50.png
   :width: 5.30244in
   :height: 3.63873in

   图 5-35 验证结果-3

4. 发送Silent指令后，过一段时间后，节点停止发送网络管理报文。再继续调用唤醒或者通信指令后，节点继续发送网络管理报文。

.. figure:: ../../_static/集成手册/CANNM/image51.png
   :width: 5.76736in
   :height: 3.92239in

   图 5-35 验证结果-4

.. |image1| image:: ../../_static/集成手册/CANNM/image20.png
   :width: 5.76736in
   :height: 2.91319in
.. |image2| image:: ../../_static/集成手册/CANNM/image21.png
   :width: 5.76736in
   :height: 3.0375in
.. |image3| image:: ../../_static/集成手册/CANNM/image22.png
   :width: 5.76736in
   :height: 3.06597in
.. |image4| image:: ../../_static/集成手册/CANNM/image23.png
   :width: 5.76736in
   :height: 2.94306in
.. |image5| image:: ../../_static/集成手册/CANNM/image24.png
   :width: 5.77153in
   :height: 3.75417in
.. |image6| image:: ../../_static/集成手册/CANNM/image25.png
   :width: 5.76806in
   :height: 3.44236in
.. |image7| image:: ../../_static/集成手册/CANNM/image26.png
   :width: 4.53539in
   :height: 2.10448in
.. |image8| image:: ../../_static/集成手册/CANNM/image27.png
   :width: 4.74658in
   :height: 2.38925in
.. |image9| image:: ../../_static/集成手册/CANNM/image28.png
   :width: 4.94968in
   :height: 2.37045in
.. |image10| image:: ../../_static/集成手册/CANNM/image29.png
   :width: 5.77308in
   :height: 2.96212in
.. |image11| image:: ../../_static/集成手册/CANNM/image30.png
   :width: 5.76736in
   :height: 3.11736in
.. |image12| image:: ../../_static/集成手册/CANNM/image31.png
   :width: 5.76736in
   :height: 5.17153in
.. |image13| image:: ../../_static/集成手册/CANNM/image32.png
   :width: 5.76736in
   :height: 3.15347in
.. |image14| image:: ../../_static/集成手册/CANNM/image33.png
   :width: 5.76736in
   :height: 3.09653in
.. |image15| image:: ../../_static/集成手册/CANNM/image34.png
   :width: 5.76736in
   :height: 2.53958in
.. |image16| image:: ../../_static/集成手册/CANNM/image35.png
   :width: 5.76736in
   :height: 2.92778in
.. |image17| image:: ../../_static/集成手册/CANNM/image36.png
   :width: 5.76736in
   :height: 3.02083in
.. |image18| image:: ../../_static/集成手册/CANNM/image45.png
   :width: 5.33377in
   :height: 2.95878in
.. |image19| image:: ../../_static/集成手册/CANNM/image47.png
   :width: 5.45833in
   :height: 5.30208in
