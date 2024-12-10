===================
CANNM_集成手册
===================

目标
====

本集成手册用于指导客户进行Can网络管理协议栈集成，文档主要包括的内容为：Can网络管理协议栈集成指导、基于普通应用的集成示例讲解。

由于各项目的需求不同，集成示例不会针对于特定的商业项目做详细讲解。

缩写词和术语
============

.. table:: 表 2‑1 缩写词和术语

   +---------------+------------------------------------------------------+
   | **\           | **描述**                                             |
   | 缩写词/术语** |                                                      |
   +---------------+------------------------------------------------------+
   | BSW           | Basic Software 基础软件层                            |
   +---------------+------------------------------------------------------+
   | BswM          | Basic Software Mode Manager基础软件模式管理器        |
   +---------------+------------------------------------------------------+
   | MCAL          | Microcontroller Abstraction Layer 微控制器抽象层     |
   +---------------+------------------------------------------------------+
   | CANIF         | CAN Interface module CAN接口模块                     |
   +---------------+------------------------------------------------------+
   | CanSm         | CAN State Manager module CAN状态管理器模块           |
   +---------------+------------------------------------------------------+
   | ComM          | Communication Manager module通信管理器模块           |
   +---------------+------------------------------------------------------+
   | EcuM          | ECU State Manager module ECU状态管理器模块           |
   +---------------+------------------------------------------------------+
   | SchM          | Scheduler Module调度程序模块                         |
   +---------------+------------------------------------------------------+

参考文档
========

[1]参考手册_CanIf.pdf

[2]参考手册_Com.pdf

[3]参考手册_EcuC.pdf

[4]参考手册_CanNm.pdf

[5]参考手册_ComM.pdf

[6]参考手册_NmIf.pdf


协议栈通信栈集成
================
项目交付的内容为：协议栈源码和ORIENTAIS Studio配置工具。协议栈细分为协议栈的各模块及其对应的配置工具模块。

网络管理栈各配置模块的功能介绍，参见表 4 1网络管理栈各配置模块介绍。

使用协议栈源码和配置工具，进行协议栈的集成的步骤，参见表 4 2 协议栈集成的步骤。


.. table:: 表 4-1 网络管理栈各配置模块介绍

   +------------+------------------------------------------------------------+
   | **模块名** | **功能**                                                   |
   +------------+------------------------------------------------------------+
   | Can        | CAN驱动配置。(由MCAL工具导入，详见章节5.2.1)               |
   +------------+------------------------------------------------------------+
   | CanIf      | CanIf模块主要处理上层模块与底层驱动之间 Pdu的传递，\       |
   |            | 为上层模块提供统一的接口来管理不同的CAN硬件模块。          |
   +------------+------------------------------------------------------------+
   | EcuC       |用于辅助配置工具完成配置的模块。主要提供 Pdu 的定义，\      |
   |            |其它模块通过关联 EcuC 中 Pdu，相互关联起来。                |
   +------------+------------------------------------------------------------+
   | Nm         |NmIf 模块主要包含两个功能：NmIf 模块是 ComM 与 CanNm 之间的 |
   |            |适配层；网络管理协调功能，协调不同总线 channe \             |
   |            |l的 ECU 节点实现网  络的同步睡眠。                          |
   +------------+------------------------------------------------------------+
   | ComM       |ComM 模块封装了控制底层的通信服务。通信管理模块\            |
   |            |从通信请求者那里收集总线通信访问请求，并协调这些请\         |
   |            |求，主要目的是：为每个 Channel\                             |
   |            |设置一个状态机控制一个 ECU 的多个通信总线通道。             |
   +------------+------------------------------------------------------------+
   | CanSM      |主要功能是与通信硬件抽象层和系统服务层产生交互，            |
   |            |为每一个 CAN 通信总线                                       |
   |            |定义一个总线相关的状态管理，并为相关的总线提供流控制。      |
   +------------+------------------------------------------------------------+
   | CanNm      | 负责实现 ECU 的状态切换。比如合适进入睡眠、是否保持正常的\ |
   |            | 网络状态等。                                               |
   +------------+------------------------------------------------------------+


.. table:: 表 4-2 协议栈集成的步骤

   +--------+-----------------------------------------------------+-----------------------------------------------------+
   |**步骤**|**操作**                                             |**说明**                                             |
   +--------+-----------------------------------------------------+-----------------------------------------------------+
   | 1      | ORIENTAIS Studio配置工具工程搭建和协议栈模块加载    | 若配置工具已经搭建，则仅需进行协议栈模块的加载操作。|
   +--------+-----------------------------------------------------+-----------------------------------------------------+
   | 2      | 模块配置及配置文件生成                              | NA                                                  |
   +--------+-----------------------------------------------------+-----------------------------------------------------+
   | 3      | 代码集成                                            | 现有工程、协议栈源代码和配置生成文件的集成。        |
   +--------+-----------------------------------------------------+-----------------------------------------------------+
   | 4      | 验证测试                                            | NA                                                  |
   +--------+-----------------------------------------------------+-----------------------------------------------------+

注意：协议栈集成之前，用户须确保已经有基础工程，且本协议栈相关的其他协议栈能正常工作。

新建ORIENTAIS Stuido配置工程及模块加载
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1.安装ORIENTAIS Studio软件后，双击软件图标打开软件。

.. figure:: ../../_static/集成手册/CANNM/image1.png
   :width: 5.76736in
   :height: 3.92239in

图 4-1 配置工程-1

2.菜单栏File->New Project，新建工程。

.. figure:: ../../_static/集成手册/CANNM/image2.png
   :width: 5.76736in
   :height: 3.92239in

图 4-2 配置工程-2

3.在弹出的新建窗口中选择Autosar下的 [BSW Project]，选择Next。

.. figure:: ../../_static/集成手册/CANNM/image3.png
   :width: 5.76736in
   :height: 3.92239in

图 4-3 配置工程-3

4.在弹出的窗口中输入工程名，选择Finish。

.. figure:: ../../_static/集成手册/CANNM/image4.png
   :width: 5.76736in
   :height: 3.92239in

图 4-4 配置工程-4

5.在弹出的窗口中选择Yes。

.. figure:: ../../_static/集成手册/CANNM/image5.png
   :width: 5.76736in
   :height: 2.52239in

图 4-5 配置工程-5

6.选择[Bsw_Builder]，右键单击，选择New ECU Configuration。

.. figure:: ../../_static/集成手册/CANNM/image6.png
   :width: 5.76736in
   :height: 1.92239in

图 4-6 配置工程-6

7.在弹出的窗口中输入ECU名，然后选择Next。

.. figure:: ../../_static/集成手册/CANNM/image7.png
   :width: 5.76736in
   :height: 3.52239in

图 4-7 配置工程-7

8.在弹出的窗口中勾选需添加的模块，点击Finish。

.. figure:: ../../_static/集成手册/CANNM/image8.png
   :width: 5.76736in
   :height: 3.92239in

图 4-8 配置工程-8

.. figure:: ../../_static/集成手册/CANNM/image9.png
   :width: 5.76736in
   :height: 2.92239in

图 4-9 配置工程-9

9.新建工程如下所示，步骤⑦中添加的模块已经被加入到工程中。

.. figure:: ../../_static/集成手册/CANNM/image10.png
   :width: 5.76736in
   :height: 3.52239in

图 4-10 配置工程-10

模块配置及代码生成
~~~~~~~~~~~~~~~~~~~~

模块配置
~~~~~~~~~

模块的具体配置，取决于具体的项目需求。该协议栈各模块配置项的详细介绍，参见表 4 3协议栈各模块配置参考文档。

.. table:: 表 4-3协议栈各模块配置参考文档

   +--------+--------------------------+-------------------+
   |**模块**| **参考文档及其章节**     |**说明**           |
   +--------+--------------------------+-------------------+
   | Can    |MCAL对应的Can配置手册     |                   |
   +--------+--------------------------+-------------------+
   | CanIf  | 参考手册_CanIf.pdf       |                   |
   +--------+--------------------------+-------------------+
   | EcuC   | 参考手册_EcuC.pdf        |                   |
   +--------+--------------------------+-------------------+
   | ComM   | 参考手册_ComM.pdf        |                   |
   +--------+--------------------------+-------------------+
   | NM     | 参考手册_NmIf.pdf        |                   |
   +--------+--------------------------+-------------------+
   | CanNm  | 参考手册_CanNm.pdf       |                   |
   +--------+--------------------------+-------------------+

配置代码生成
~~~~~~~~~~~~~~~~~~~~~~~~

1.在ORIENTAIS Stuido主界面左方，选择对应的协议栈，单击右键弹出Validate All和Generate All菜单。

.. figure:: ../../_static/集成手册/CANNM/image11.png
   :width: 5.76736in
   :height: 3.92239in

图 4-11 模块配置-1

2.选择Validate All对本协议栈各配置选项进行校验，没有错误提示信息即校验通过。若有错误信息，请按照错误提示修改。

3.选择Generate All，生成配置文件。右下角的Console窗口输出生成的配置文件信息。

.. figure:: ../../_static/集成手册/CANNM/image12.png
   :width: 5.76736in
   :height: 2.10448in

图 4-12 模块配置-2

4.将ORIENTAIS Studio切换到Resource模式，即可查看生成的配置文件。

.. figure:: ../../_static/集成手册/CANNM/image13.png
   :width: 5.76736in
   :height: 2.92239in

图 4-13 模块配置-3

功能集成
~~~~~~~~~~~~

代码集成
~~~~~~~~~~~~

协议栈代码包括两部分：普华提供的协议栈源码和ORIENTAIS Studio配置生成代码。

用户须将协议栈源码和章节4.2.2生成的源代码添加到集成开发工具的对应文件夹。协议栈集成的文件结构，见章节5.2.7。   

注意：协议栈集成之前，用户须确保已经有基础工程，且本协议栈相关的其他协议栈能正常工作。

集成注意事项

对于集成过程中，协议栈特殊要求和用户经常出现的问题，归类总结形成 表 4 4协议栈集成约束清单。用户需逐一排查表中的约束项，以避免集成问题出现。

.. table:: 表 4-4 协议栈集成约束清单

   +--------+----------+-----------------------------------------------------------------+
   |**编号**| **类别** | **约束限制**                                                    |
   +--------+----------+-----------------------------------------------------------------+
   | 1      | 中断     | 通信栈有中断、轮询或混合三种工作模式。若选取中断或混合模式，    |
   |        |          | 用户需在 OS 配置对应的中断并填充中断服务 API。                  |
   +--------+----------+-----------------------------------------------------------------+
   | 2      | 堆栈     | 用户需确保为任务堆栈和中断堆栈分配足够的堆栈空间。              |
   +--------+----------+-----------------------------------------------------------------+
   | 3      | 头文件   | - 添加协议栈代码之后，用户需更新集成开发工具中的头文件路径。    |
   |        |          | - 调用协议栈 API 的源文件，需要包含协议栈的头文件。             |
   +--------+----------+-----------------------------------------------------------------+
   | 4      | 初始化   | 以 CAN 网络管理为例，网络管理栈的初始化顺序为：                 |
   |        |          | Can_Init，CanIf_Init，Nm_Init，CanSM_Init，ComM_Init，CanNm_Init|
   +--------+----------+-----------------------------------------------------------------+
   | 5      | 周期函数 | CanNm_MainFunction，Com_ComM_MainFunction 和 CanSM_MainFunction |
   |        |          | 需要被周期性任务函数调用。                                      |
   +--------+----------+-----------------------------------------------------------------+

集成示例
~~~~~~~~~~~~

本章节通过普通的CAN网络管理栈为例，向用户展示网络管理栈的集成过程。用户可以据此熟悉网络管理栈配置工具的配置过程，以及如何应用配置工具生成的配置文件。

为让用户更清晰的了解工具的使用，所用的配置均逐一手动完成。用户可以使用工具中的DBC导入功能，快速完成配置。

注意：本示例不代表用户的实际配置情况，用户需要根据自己的实际需求，决定各个参数的配置。

集成目标
~~~~~~~~~~~~

CAN报文需求：

.. table:: 报文相关信息

   +----------+----------------------+--------------+--------------+----------------+--------------+--------------+
   |**报文ID**|**报文名称**          |**发送/接收** |**发送模式**  |**报文周期**    |**报文长度**  |**工作模式**  |
   +----------+----------------------+--------------+--------------+----------------+--------------+--------------+
   | 0x405    | CANNM_Tx_Message1    | 发送         | 周期         | 100ms          | 8字节        | 轮询         |
   +----------+----------------------+--------------+--------------+----------------+--------------+--------------+
   | 0x400    | CANNM_Rx_Message1    | 接收         | NA           | NA             | 8字节        | 轮询         |
   +----------+----------------------+--------------+--------------+----------------+--------------+--------------+

模块的配置

新建配置工程及模块加载操作，请参考本文档上述。

Can模块配置
~~~~~~~~~~~~

本章介绍如何使用EB工具配置Can模块，但是只涉及到与通信栈中报文收发有关系的部分（主要是HardwareObeject），其余配置选项请参考EB工具的帮助手册进行配置。

1.打开EB工具，新建CAN模块后，在以下路径配置HardwareObject：

CAN模块CanConfigSetCanHardwareObject。

根据本次配置示例的目标，需要配置2个HardwareObject，如下图所示：

.. figure:: ../../_static/集成手册/CANNM/image14.png
   :width: 5.76736in
   :height: 1.92239in

图5-1 模块配置-1

注意：HardwareObject定义的时候，必须接收报文放在发送报文前面。

2.完成EB配置后，生成Can模块的配置文件，替换工程中原有的Can模块的配置文件。

3.导出EB的配置文件。

4.将3导出的配置文件，导入到ORIENTAIS Studio中。

导入后工程如下图所示：

.. figure:: ../../_static/集成手册/CANNM/image0.png
   :width: 5.76736in
   :height: 2.92239in

图5-2 模块配置-2

EcuC模块配置
~~~~~~~~~~~~

双击EcuC模块，打开EcuC模块配置界面。

EcucConfigSets标签页
~~~~~~~~~~~~~~~~~~~~~~~~

1.在EcucConfigSets栏目上右键，选择EcucConfigSet，再在EcucConfigSet上右键，选择NewEcucPduCollection。

.. figure:: ../../_static/集成手册/CANNM/image15.png
   :width: 5.76736in
   :height: 2.92239in

图5-3 模块配置-3

1)	PduIdTypeEnum这个参数是定义PDU个数的时用的。因为示例只有2个报文，PDU数不会超过255，选择UINT8和UINT16均可，这里直接使用默认值。

2)	PduLengthTypeEnum这个参数是定义存储数据长度时使用的。因为示例需要配置的报文长度都是8，不会超过255，选择UINT8和UINT16均可，这里直接使用默认值。

2.在EcucPduCollection上右键，选择Pdu，会生成一个Pdu的配置界面。

.. figure:: ../../_static/集成手册/CANNM/image16.png
   :width: 5.76736in
   :height: 4.92239in
图5-4 EcucPduCollection标签页设置

可修改PDU命名方便之后配置如：模块名_方向_后缀，CanIf_TxPdu、Com_TxPdu。

3.这里按照“集成目标”中要求的报文，配置Pdu。

.. figure:: ../../_static/集成手册/CANNM/image17.png
   :width: 5.76736in
   :height: 3.92239in

图5-5 配置Pdu

4.在MetaDataTypes上右键，选择New MetaDataType会生成一个MetaDataType

.. figure:: ../../_static/集成手册/CANNM/image18.png
   :width: 5.76736in
   :height: 3.92239in

图5-6 配置MetaDataType

网络管理PDU必要的属性为 PduLength，还需要配置相应的MetaDataType

1）MetaDataItemLength: 定义MetaData长度，由MetaDataItemType决定。

2）MetaDataItemType：定义MetaDataItem类型。

这个属性在配置的报文为网络管理发送报文的时候，可以根据实际的需要去配置。一般配置为CAN_ID_32，用于存放CanNm发送报文的节点地址。CanIf会自动根据MetaData中的内容去修改CanNm发送报文的CanId，这会降低配置的工作量(否则修改节点地址后，都需要修改CanIf层中CanNm发送报文的CanId)。

这个属性在配置的报文为网络管理接收报文的时候，可以根据实际的需要去配置。一般配置为CAN_ID_32，用于存放CanNm接收报文的节点地址。CanNm会将MetaData中的内容识别为节点地址，这会降低配置的工作量(否则接收到不同节点发送的网络管理报文后，都需要增加一个PDU，这也要求CanIf层需要将网络管理报文接收邮箱设置为BasicCan)。

3）duLength：Pdu长度，根据DBC中的定义设置。

配置好的MetaDataType如下：

.. figure:: ../../_static/集成手册/CANNM/image19.png
   :width: 5.76736in
   :height: 3.92239in

图5-7 配置好的MetaDataType示意

配置好的PDU如下：

.. figure:: ../../_static/集成手册/CANNM/image20.png
   :width: 5.76736in
   :height: 3.92239in

图 5-8 配置好的Pdu示意

5.根据步骤3的描述，配置其余报文的Pdu。

.. figure:: ../../_static/集成手册/CANNM/image21.png
   :width: 5.76736in
   :height: 3.92239in

图 5-9 配置NM_RxPdu


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

图 5‑18 配置ComMGeneral

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

图 5‑22 配置ComMChannels第二步

4. 配置ComMNetworkManagements

..

   该容器下，已经默认创建了一个ComMNetworkManagement对象。保持默认即可。

   若该通道不是有网络管理功能，请将ComMNmVariant设置成LIGHT。此Autosar
   NM栈DEMO需要配置成FULL。

|image17|

图 5‑23 配置ComMNetworkManagements

5. 配置ComMUserPerChannels

..

   该容器下，已经默认创建了一个ComMUserPerChannels对象。将对应的User关联到该通道。

.. figure:: ../../_static/集成手册/CANNM/image37.png
   :width: 5.76736in
   :height: 3.23819in

图 5‑24 配置ComMUserPerChannels

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

图 5‑25 配置NmGlobalConstants

2. 配置NmGlobalFeatures

..

   该容器主要配置网络管理的功能，若要开通相应的功能，就勾选相应的配置项。这里，Nm的配置如下：

.. figure:: ../../_static/集成手册/CANNM/image39.png
   :width: 5.76736in
   :height: 2.84375in

图 5‑26 配置NmGlobalFeatures

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

图 5‑27 配置NmChannelConfig

2. 配置NmGenericBusNmConfig

..

   该容器主要配置通道的网络管理的类型。首先创建一个NmGenericBusNmConfig对象。

图 5‑28 配置NmGenericBusNmConfig

.. figure:: ../../_static/集成手册/CANNM/image42.png
   :width: 5.76736in
   :height: 3.17986in

图 5‑29 配置NmGenericBusNmConfig

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

图 5‑30 配置CanNmGlobalConfig

2. 配置CanNmChannelConfig

..

   该容器的各种配置项，来自于客户需求，例如图例的配置需求为：NM报文快发时间为20ms，快发次数为5次，NM周期报文时间为500ms，NM报文的节点ID是xxD(此处节点ID取决于网络管理的ID号，例如0x405，节点ID为5)，Nm_Repeat模式等待时间为2.1s，Ready
   Sleep状态进入Prepare Bus_Sleep状态时间为2s，Prepare
   Bus_Sleep状态进入Bus_Sleep状态时间为5s。

.. figure:: ../../_static/集成手册/CANNM/image44.png
   :width: 5.76736in
   :height: 2.92917in

图 5-31 配置CanNmGlobalConfig

|image18|

图 5‑32 配置CanNmGlobalConfig

3. 配置CanNmRxPdus和CanNmTxPdus

..

   此容器的Pdu参考映射到EcuC中建立的Pdu当中

.. figure:: ../../_static/集成手册/CANNM/image46.png
   :width: 5.76736in
   :height: 2.53194in

图 5‑33 配置CanNmGlobalConfig

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


.. figure:: ../../_static/集成手册/CANNM/code1.png
   :width: 6.6in
   :height: 6.53611in

.. figure:: ../../_static/集成手册/CANNM/code2.png
   :width: 6.6in
   :height: 1.42311in

.. figure:: ../../_static/集成手册/CANNM/code3.png
   :width: 6.6in
   :height: 4.03611in

.. figure:: ../../_static/集成手册/CANNM/code4.png
   :width: 6.6in
   :height: 5.05611in

.. figure:: ../../_static/集成手册/CANNM/code5.png
   :width: 6.6in
   :height: 6.73611in

.. figure:: ../../_static/集成手册/CANNM/code6.png
   :width: 6.6in
   :height: 2.63611in
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
