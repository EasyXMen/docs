==============
CANNM
==============

目标
====

本集成手册用于指导客户进行Can网络管理协议栈集成，文档主要包括的内容为：Can网络管理协议栈集成指导、基于普通应用的集成示例讲解。

由于各项目的需求不同，集成示例不会针对于特定的商业项目做详细讲解。

缩写词和术语
============

+-----------------+------------------------------------------------------+
| **缩写词/术语** | **描述**                                             |
+=================+======================================================+
| BSW             | 基础软件                                             |
+-----------------+------------------------------------------------------+
| BswM            | 基础软件模式管理                                     |
+-----------------+------------------------------------------------------+
| MCAL            | 微控制器抽象层                                       |
+-----------------+------------------------------------------------------+
| CANIF           | CAN 接口模块                                         |
+-----------------+------------------------------------------------------+
| CanSm           | CAN 状态管理模块                                     |
+-----------------+------------------------------------------------------+
| ComM            | 通信管理模块                                         |
+-----------------+------------------------------------------------------+
| EcuM            | ECU 状态管理模块                                     |
+-----------------+------------------------------------------------------+
| NM              | 网络管理                                             |
+-----------------+------------------------------------------------------+
| SchM            | 调度程序模块                                         |
+-----------------+------------------------------------------------------+

参考文档
========

[1]参考手册_CanIf.pdf

[2]参考手册_Com.pdf

[3]参考手册_EcuC.pdf

[4]参考手册_CanNm.pdf

[5]参考手册_ComM.pdf

[6]参考手册_NmIf.pdf

协议栈集成
==========

项目交付的内容为：协议栈源码和ORIENTAIS
Studio配置工具。协议栈细分为协议栈的各模块及其对应的配置工具模块。

网络管理栈各配置模块的功能介绍，参见表 网络管理栈各配置模块介绍。

使用协议栈源码和配置工具，进行协议栈的集成的步骤，参见表
协议栈集成的步骤。

.. table:: 表 网络管理栈各配置模块介绍

   +------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+
   | **模块名** |                                                                                  **功能**                                                                                  |                                     说明                                     |
   +------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+
   | Can        | CAN驱动配置。(由MCAL工具导入，详见章节Can模块配置)                                                                                                                         | 报文ID                                                                       |
   +------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+
   | CanIf      | CanIf模块主要处理上层模块与底层驱动的之间Pdu的传递，为上层模块提供统一的接口来管理不同的CAN硬件模块。                                                                      | 动态CanId的计算方式如下：                                                    |
   |            |                                                                                                                                                                            | CanId=(CanIfTxPduCanId&CanIfTxPduCanIdMask)|(metaData&～CanIfRxPduCanIdMask) |
   +------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+
   | EcuC       | 用于辅助配置工具完成配置的模块。主要提供Pdu的定义，其它模块通过关联EcuC中Pdu，相互关联起来。                                                                               | 标准帧                                                                       |
   +------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+
   | Nm         | NmIf模块主要包含两个功能：NmIf模块是ComM与CanNm之间的适配层；网络管理协调功能，协调不同总线channel的ECU节点实现网络的同步睡眠。                                            | 报文长度                                                                     |
   |            |                                                                                                                                                                            |                                                                              |
   +------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+
   | ComM       | ComM模块封装了控制底层的通信服务。通信管理模块从通信请求者那里收集总线通信访问请求，并协调这些请求，主要目的是：为每个Channel设置一个状态机控制一个ECU的多个通信总线通道。 | CanIf模块收到报文后通知CANNM模块                                             |
   +------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+
   | CanSM      | 主要功能是与通信硬件抽象层和系统服务层产生交互，为每一个CAN通信总线定义一个总线相关的状态管理，并为相关的总线提供流控制。                                                  | 关联到对应的Hrh                                                              |
   +------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+
   | CanNm      | 负责实现ECU的状态切换。比如合适进入睡眠、是否保持正常的网络状态等。                                                                                                        | 关联到EcuC中定义的Pdu                                                        |
   +------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+

.. table:: 表 协议栈集成的步骤

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

新建ORIENTAIS Stuido配置工程及模块加载
--------------------------------------

#. 安装ORIENTAIS Studio软件后，双击软件图标打开软件。

   |image1|

   图 配置工程-1

#. 菜单栏File🡪New🡪Project，新建工程。

   |image2|

   图 配置工程-2

#. 在弹出的新建窗口中选择Autosar下的 [BSW Project]，选择Next。

   |image3|

   图 配置工程-3

#. 在弹出的窗口中输入工程名，选择Finish。

   |image4|

   图 配置工程-4

#. 在弹出的窗口中选择Yes。

   |image5|

   图 配置工程-5

#. 选择[Bsw_Builder]，右键单击，选择New ECU Configuration。

   |image6|

   图 配置工程-6

#. 在弹出的窗口中输入ECU名，然后选择Next。

   |image7|

   图 配置工程-7

#. 在弹出的窗口中勾选需添加的模块，点击Finish。

   |image8|

   图 配置工程-8

   |image9|

   图 配置工程-9

#. 新建工程如下所示，步骤⑦中添加的模块已经被加入到工程中。

   |image10|

   图 配置工程-10

模块配置及代码生成
------------------

模块配置
~~~~~~~~

模块的具体配置，取决于具体的项目需求。该协议栈各模块配置项的详细介绍，参见表
协议栈各模块配置参考文档。

.. table:: 表 协议栈各模块配置参考文档

   +----------+--------------------------------------------+----------------+
   | **模块** | **参考文档及其章节**                       | **说明**       |
   +==========+============================================+================+
   | Can      | MCAL对应的Can配置手册                      |                |
   +----------+--------------------------------------------+----------------+
   | CanIf    | 参考手册_CanIf.pdf 章节5                   |                |
   +----------+--------------------------------------------+----------------+
   | EcuC     | 参考手册_EcuC.pdf 章节5                    |                |
   +----------+--------------------------------------------+----------------+
   | ComM     | 参考手册_ComM.pdf 章节5                    |                |
   +----------+--------------------------------------------+----------------+
   | NM       | 参考手册_NmIf.pdf 章节5                    |                |
   +----------+--------------------------------------------+----------------+
   | CanNm    | 参考手册_CanNm.pdf 章节5                   |                |
   +----------+--------------------------------------------+----------------+

配置代码生成
~~~~~~~~~~~~

#. 在ORIENTAIS Stuido主界面左方，选择对应的协议栈，单击右键弹出Validate
   All和Generate All菜单。

   |image11|

   图 模块配置-1

#. 选择Validate
   All对本协议栈各配置选项进行校验，没有错误提示信息即校验通过。若有错误信息，请按照错误提示修改。

#. 选择Generate
   All，生成配置文件。右下角的Console窗口输出生成的配置文件信息。

   |image12|

   图 模块配置-2

#. 将ORIENTAIS Studio切换到Resource模式，即可查看生成的配置文件。

   |image13|

   图 模块配置-3

功能集成
--------

代码集成
~~~~~~~~

协议栈代码包括两部分：项目提供的协议栈源码和ORIENTAIS
Studio配置生成代码。

用户须将协议栈源码和章节（配置代码生成）生成的源代码添加到集成开发工具的对应文件夹。协议栈集成的文件结构，见章节(协议栈调度集成)。

.. note::
   **协议栈集成之前，用户须确保已经有基础工程，且本协议栈相关的其他协议栈能正常工作。**

集成注意事项
~~~~~~~~~~~~

对于集成过程中，协议栈特殊要求和用户经常出现的问题，归类总结形成 表
协议栈集成约束清单。用户需逐一排查表中的约束项，以避免集成问题出现。

.. table:: 表 协议栈集成约束清单

   +----------+----------+---------------------------------------------------------------------------------------------------------+
   | **编号** | **类别** | **约束限制**                                                                                            |
   +==========+==========+=========================================================================================================+
   | **1**    | 中断     | 通信栈有中断、轮询或混合三种工作模式。若选取中断或混合模式，用户需在OS配置对应的中断并填充中断服务API。 |
   +----------+----------+---------------------------------------------------------------------------------------------------------+
   | **2**    | 堆栈     | 用户需确保为任务堆栈和中断堆栈分配足够的堆栈空间。                                                      |
   +----------+----------+---------------------------------------------------------------------------------------------------------+
   | **3**    | 头文件   | - 添加协议栈代码之后，用户需更新集成开发工具中的头文件路径。                                            |
   |          |          |                                                                                                         |
   |          |          | - 调用协议栈API的源文件，需要包含协议栈的头文件。                                                       |
   +----------+----------+---------------------------------------------------------------------------------------------------------+
   | **4**    | 初始化   | 以CAN网络管理为例，网络管理栈的初始化顺序为：Can_Init， CanIf_Init， Nm_Init，                          |
   |          |          | CanSM_Init，ComM_Init，CanNm_Init。                                                                     |
   +----------+----------+---------------------------------------------------------------------------------------------------------+
   | **5**    | 周期函数 | CanNm_MainFunction，Com\_ ComM_MainFunction和CanSM_MainFunction需要被周期性任务函数调用。               |
   +----------+----------+---------------------------------------------------------------------------------------------------------+

集成示例
========

本章节通过普通的CAN网络管理栈为例，向用户展示网络管理栈的集成过程。用户可以据此熟悉网络管理栈配置工具的配置过程，以及如何应用配置工具生成的配置文件。

为让用户更清晰的了解工具的使用，所用的配置均逐一手动完成。用户可以使用工具中的DBC导入功能，快速完成配置。

.. note::
   **本示例不代表用户的实际配置情况，用户需要根据自己的实际需求，决定各个参数的配置。**

集成目标
--------

**CAN报文需求：**

+------------+-------------------+-----------+----------+----------+-------------+----------+
| **报文ID** | **报文**          | **发送**  | **发送** | **报文** | **报文**    | **工作** |
|            |                   |           |          |          |             |          |
|            | **名称**          | **/接收** | **模式** | **周期** | **长度**    | **模式** |
+============+===================+===========+==========+==========+=============+==========+
| 0x405      | CANNM_Tx_Message1 | 发送      | 周期     | 100ms    | 8\ **字节** | 轮询     |
+------------+-------------------+-----------+----------+----------+-------------+----------+
| 0x400      | CANNM_Rx_Message1 | 接收      | NA       | NA       | 8\ **字节** | 轮询     |
+------------+-------------------+-----------+----------+----------+-------------+----------+

模块的配置
----------

新建配置工程及模块加载操作，请参考本文档章节(模块配置及代码生成)。

Can模块配置
~~~~~~~~~~~

本章介绍如何使用EB工具配置Can模块，但是只涉及到与通信栈中报文收发有关系的部分（主要是HardwareObeject），其余配置选项请参考EB工具的帮助手册进行配置。

#. 打开EB工具，新建CAN模块后，在以下路径配置HardwareObject：

   CAN模块🡪CanConfigSet🡪CanHardwareObject。

   根据本次配置示例的目标，需要配置2个HardwareObject，如下图所示：

   |image14|

   图 模块配置-1

   .. note::
      **HardwareObject定义的时候，必须接收报文放在发送报文前面。**

#. 完成EB配置后，生成Can模块的配置文件，替换工程中原有的Can模块的配置文件。

#. 导出EB的配置文件。

#. 将3导出的配置文件，导入到ORIENTAIS Studio中。

..

   导入后工程如下图所示：

   |image15|

   图 模块配置-2

EcuC模块配置
~~~~~~~~~~~~

双击EcuC模块，打开EcuC模块配置界面。

EcucConfigSets配置
^^^^^^^^^^^^^^^^^^

#. 在EcucConfigSets栏目上右键，选择EcucConfigSet，再在EcucConfigSet上右键，选择New🡪EcucPduCollection。

   |image16|

   图 EcucConfigSets设置

   #. PduIdTypeEnum这个参数是定义PDU个数的时用的。因为示例只有2个报文，PDU数不会超过255，选择UINT8和UINT16均可，这里直接使用默认值。

   #. PduLengthTypeEnum这个参数是定义存储数据长度时使用的。因为示例需要配置的报文长度都是8，不会超过255，选择UINT8和UINT16均可，这里直接使用默认值。

#. 在EcucPduCollection上右键，选择Pdu，会生成一个Pdu的配置界面。

   |image17|

   图 EcucPduCollection设置

   可修改PDU命名方便之后配置如：模块名_方向_后缀，CanIf_TxPdu、Com_TxPdu。

#. 这里按照“集成目标”中要求的报文，配置Pdu。

   |image18|

   图 配置Pdu

#. 在MetaDataTypes上右键，选择New MetaDataType会生成一个MetaDataType

   |image19|

   图 配置MetaDataType

   网络管理PDU必要的属性为 PduLength，还需要配置相应的MetaDataType

   #. MetaDataItemLength: 定义MetaData长度，由MetaDataItemType决定。

   #. MetaDataItemType：定义MetaDataItem类型。

      - 这个属性在配置的报文为网络管理发送报文的时候，可以根据实际的需要去配置。一般配置为CAN_ID_32，用于存放CanNm发送报文的节点地址。CanIf会自动根据MetaData中的内容去修改CanNm发送报文的CanId，这会降低配置的工作量(否则修改节点地址后，都需要修改CanIf层中CanNm发送报文的CanId)。

      - 这个属性在配置的报文为网络管理接收报文的时候，可以根据实际的需要去配置。一般配置为CAN_ID_32，用于存放CanNm接收报文的节点地址。CanNm会将MetaData中的内容识别为节点地址，这会降低配置的工作量(否则接收到不同节点发送的网络管理报文后，都需要增加一个PDU，这也要求CanIf层需要将网络管理报文接收邮箱设置为BasicCan)。

   #. PduLength：Pdu长度，根据DBC中的定义设置。

      配置好的MetaDataType如下：

      |image20|

      图 配置好的MetaDataType示意

   配置好的PDU如下：

      |image21|

      图 配置好的Pdu示意

#. 根据步骤3的描述，配置其余报文的Pdu。

   |image22|

   图 配置NM_RxPdu

校验
~~~~

ECUC模块到此配置结束。可以在模块上右键，然后选择校验，查看是否配置有错误。校验后提示窗口没有错误信息，即校验通过。

CanIf模块配置
~~~~~~~~~~~~~

双击CanIf模块，打开CanIf模块的配置界面。

CanIfCtrlDrvCfg配置
^^^^^^^^^^^^^^^^^^^

#. 在CanIfInitCfg下的容器[CanIfInitCfg]上，右边新建一个CanIfInitHohCfg对象。

   |image23|

   图 新建CanIfInitHohCfg对象

#. CanIfCtrlDrvCfg配置

   #. CanIfCtrlDrvCfg_0的配置项CanIfCtrlDrvInitHohConfigRef需要关联到步骤1中创建的对象。

   #. CanIfCtrlDrvNameRef的配置项选Can。

      |image24|

      图 配置CanIfCtrlDrvCfg

#. CanIfCtrlCfg配置

   |image25|

   图 配置CanIfCtrlCfg

CanIfPublicCfg配置
^^^^^^^^^^^^^^^^^^

   |image26|

   图 配置CanIfPublicCfg

CanIfInitCfg配置
^^^^^^^^^^^^^^^^

#. 配置CanIfInitHohCfgs

   CanIfInitHohCfgs下包含2个容器：CanIfHrhCfgs和CanIfHthCfgs。每个发送报文需要一个CanIfHrhCfg，每个接收报文需要一个CanIfHthCfg。因此，本例中需要配置1个接收对象、1个发送对象。

   在新建的容器CanIfInitHohCfg_0上右键新建1个CanIfHrhCfg和1个CanIfHthCfg。

   |image27|

   图 CanIfInitHohCfgs配置第一步

   |image28|

   图 CanIfInitHohCfgs配置第二步

   |image29|

   图 CanIfInitHohCfgs配置第三步

#. 配置CanIfBufferCfgs

   每个发送报文都需要配置一个CanIfBufferCfg，因此本示例需要配置1对象。

   |image30|

   图 配置CanIfBufferCfgs

#. 配置CanIfTxPduCfgs

   每个发送报文都需要配置一个CanIfTxPduCfg，因此本示例需要配置1对象。

   表 CanIfTxPduCfgs说明

   +--------------------------------+-------------------------+-------------------------------------+
   | 参数名                         | 设置值                  | 说明                                |
   +================================+=========================+=====================================+
   | CanIfTxPduCanId                | 0x405                   | CAN ID                              |
   +--------------------------------+-------------------------+-------------------------------------+
   | CanIfTxPduCanIdType            | STANDARD_CAN            | 标准帧                              |
   +--------------------------------+-------------------------+-------------------------------------+
   | CanIfTxPduType                 | DYNAMIC                 | 动态CAN ID                          |
   +--------------------------------+-------------------------+-------------------------------------+
   | CanIfTxPduUserTxConfirmationUL | CAN_NM                  | 报文发送成功确认通知传递给CanNm模块 |
   +--------------------------------+-------------------------+-------------------------------------+
   | CanIfTxPduBufferRef            | CanIfBufferCfg_Nm_TxPdu | 关联到对应Buffer                    |
   +--------------------------------+-------------------------+-------------------------------------+
   | CanIfTxPduRef                  | Nm_TxPdu                | 关联到EcuC中的Pdu                   |
   +--------------------------------+-------------------------+-------------------------------------+

   |image31|

   图 配置CanIfTxPduCfgs

#. 配置CanIfRxPduCfgs

   每个接收报文都需要配置一个CanIfRxPduCfg，因此本示例需要配置1对象。

   .. table:: 表 CanIfRxPduCfgs说明

      +------------------------------+----------------------+------------------------------------------------------------------------------+
      |            参数名            |        设置值        |                                     说明                                     |
      +------------------------------+----------------------+------------------------------------------------------------------------------+
      | CanIfRxPduCanId              | 0x400                | 报文ID                                                                       |
      +------------------------------+----------------------+------------------------------------------------------------------------------+
      | CanIfRxPduCanIdMask          | 0x780                | 动态CanId的计算方式如下：                                                    |
      |                              |                      | CanId=(CanIfTxPduCanId&CanIfTxPduCanIdMask)|(metaData&～CanIfRxPduCanIdMask) |
      +------------------------------+----------------------+------------------------------------------------------------------------------+
      | CanIfRxPduCanIdType          | STANDARD_CAN         | 标准帧                                                                       |
      +------------------------------+----------------------+------------------------------------------------------------------------------+
      | CanIfRxPduDlc                | 8                    | 报文长度                                                                     |
      +------------------------------+----------------------+------------------------------------------------------------------------------+
      | CanIfRxPduUserRxIndicationUL | CAN_NM               | CanIf模块收到报文后通知CANNM模块                                             |
      +------------------------------+----------------------+------------------------------------------------------------------------------+
      | CanIfRxPduHrhIdRef           | CanIfHrhCfg_NM_RxPdu | 关联到对应的Hrh                                                              |
      +------------------------------+----------------------+------------------------------------------------------------------------------+
      | CanIfRxPduRef                | Nm_RxPdu             | 关联到EcuC中定义的Pdu                                                        |
      +------------------------------+----------------------+------------------------------------------------------------------------------+
   
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

   |image32|

   图 配置ComMGeneral

ComMConfigSet配置
^^^^^^^^^^^^^^^^^

#. 配置ComMConfigSet

   由于不使用PNC功能，因此不配置。采取默认配置即可。

   |image33|

   图 配置ComMConfigSet

   该容器下，需要配置的容器有ComMChannels和ComMUsers。ComMChannels主要配置的是总线的类型和ComM函数的调用周期。ComMUsers是用户用于请求通信模式。

#. ComMUsers

   该容器下，已经默认创建了一个User。若有多个通道，可在ComMConfigSet容器上右键创建。每个通道都需要关联一个User。该容器下，保持默认即可。

   |image34|

   图 配置ComMUsers

#. 配置ComMChannels

   该容器下，已经默认创建了一个通道。若有多个通道，可在ComMConfigSet容器上右键创建。此Can网络管理栈DEMO只配置了一个通道。

   |image35|

   图 配置ComMChannels第一步

   该容器下，只需要配置ComMBusType和ComM周期调用函数周期，如下所示：

   |image36|

   图 配置ComMChannels第二步

#. 配置ComMNetworkManagements

   该容器下，已经默认创建了一个ComMNetworkManagement对象。保持默认即可。

   若该通道不是有网络管理功能，请将ComMNmVariant设置成LIGHT。此Autosar
   NM栈DEMO需要配置成FULL。

   |image37|

   图 配置ComMNetworkManagements

#. 配置ComMUserPerChannels

   该容器下，已经默认创建了一个ComMUserPerChannels对象。将对应的User关联到该通道。

   |image38|

   图 配置ComMUserPerChannels

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

   该示例中只有一个通道，因此配置为1。

   |image39|

   图 配置NmGlobalConstants

#. 配置NmGlobalFeatures

   该容器主要配置网络管理的功能，若要开通相应的功能，就勾选相应的配置项。这里，Nm的配置如下：

   |image40|

   图 配置NmGlobalFeatures

#. 配置NmGlobalPropertiess

   保持默认。

NmChannelConfig配置
^^^^^^^^^^^^^^^^^^^

#. 配置NmChannelConfig

   该容器主要配置NmComChannelRef，将ComM配置的通道关联到该模块。

   |image41|

   图 配置NmChannelConfig

#. 配置NmGenericBusNmConfig

   该容器主要配置通道的网络管理的类型。首先创建一个NmGenericBusNmConfig对象。

   |image42|

   图 配置NmGenericBusNmConfig

   |image43|

   图 配置NmGenericBusNmConfig

.. _校验-3:

校验
^^^^

Nm模块到此配置结束。可以在模块上右键，然后选择校验，查看是否配置有错误。校验后提示窗口没有错误信息，即校验通过。

CanNM模块配置
~~~~~~~~~~~~~

CanNmGlobalConfig配置
^^^^^^^^^^^^^^^^^^^^^^

#. 配置CanNmGlobalConfig

   该容器保持默认，CanNM主函数周期设置成5ms。

   |image44|

   图 配置CanNmGlobalConfig

#. 配置CanNmChannelConfig

   该容器的各种配置项，来自于客户需求，例如图例的配置需求为：NM报文快发时间为20ms，快发次数为5次，NM周期报文时间为500ms，NM报文的节点ID是xxD(此处节点ID取决于网络管理的ID号，例如0x405，节点ID为5)，Nm_Repeat模式等待时间为2.1s，Ready
   Sleep状态进入Prepare Bus_Sleep状态时间为2s，Prepare
   Bus_Sleep状态进入Bus_Sleep状态时间为5s。

   |image45|

   图 配置CanNmGlobalConfig

   |image46|

   图 配置CanNmGlobalConfig

#. 配置CanNmRxPdus和CanNmTxPdus

   此容器的Pdu参考映射到EcuC中建立的Pdu当中

   |image47|
   |image48|

   图 配置CanNmGlobalConfig

.. _校验-4:

校验
^^^^

CanNM模块到此配置结束。可以在模块上右键，然后选择校验，查看是否配置有错误。校验后提示窗口没有错误信息，即校验通过。

源代码集成
----------

项目交付给用户的工程结构如下：

   |image49|

- BSW目录，这个目录放置所有基础软件相关代码，除了MCAL、Config文件夹之外，均按bsw源码路径放置

- ASW目录，存放应用代码

- Config目录，存放mcal和bsw生成的动态代码。

- MCAL目录，存放mcal的动态代码

网络管理栈源代码集成步骤如下：

#. 将章节（模块配置）中EB MCAL生成的CAN模块配置文件和ORIENTAIS Studio
   生成的配置文件复制到Config/BSW_Config文件夹中。

#. 将MCAL提供的CAN模块源码和项目提供的协议栈源代码文件复制到BS
   W和MCAL文件夹中。

协议栈调度集成
--------------

通信栈调度集成步骤如下：

#. 协议栈调度集成，需要逐一排查并实现表 协议栈集成约束清单
   所罗列的问题，以避免集成出现差错。

#. 编译链接代码，将生成的elf文件烧写进芯片。

网络管理栈有关的代码，在下方的main.c文件中给出重点标注。

.. note::
   本示例中，网络管理栈初始化的代码和启动通信的代码置于main.c文件，并不代表其他项目同样适用于将其置于main.c文件中。**

.. code-block:: c
    :linenos:

    #include <stdlib.h>
    #include "Std_Types.h"
    #include "Mcu.h"
    #include "Port.h"
    #include "Dio.h"
    #include "Irq.h"
    #include "Gpt.h"
    #include "Gtm.h"
    #include "Adc.h"
    #include "Can_17_MCanP.h"
    #include "CanIf.h"
    #include "ComM_EcuMBswM.h"
    #include "ComM.h"
    # 网络管理栈包含的头文件
    #include "CanSM.h"
    #include "CanNm.h"
    #include "Nm.h"
    #include "CanNm_Internal.h"
    #include "Bsw_Test.h"
    #include "Icu_17_GtmCcu6.h"
    #include "Pwm_17_Gtm.h"
    #include "Spi.h"

    int main(void)
    {
        Mcu_Init(Mcu_ConfigRoot);
        Mcu_InitClock(0);
        while (MCU_PLL_UNLOCKED == Mcu_GetPllStatus())
        {
            /* wait for PLL locked */
        }
        Mcu_DistributePllClock();
        /* IrqGtm_Init */
        IrqGtm_Init();
        /* Port Initialize  */
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
        # 初始化CanIf，Nm，CanSM，ComM，CanNm模块
        Nm_Init(&Nm_Config);
        CanSM_Init(&CanSM_Config);
        ComM_Init(&ComM_Config);
        CanNm_Init(&CanNm_PBConfig);

        # 打开通信
        ComM_RequestComMode(ComMChannel_0, COMM_FULL_COMMUNICATION);
        ComM_CommunicationAllowed(ComMUser_0, TRUE);
        /* infinite loop */
        while (1)
        {
            if (TRUE == Gpt_1msFlag)
            {
                Gpt_1msFlag = FALSE;
                # CanSM和Can底层功能的周期处理函数放在1ms任务中
                CanSM_MainFunction();
                Can_17_MCanP_MainFunction_Read();
                Can_17_MCanP_MainFunction_Write();
                Can_17_MCanP_MainFunction_BusOff();
                Can_17_MCanP_MainFunction_Wakeup();
                # 测试代码：实现网络管理的唤醒
                if(wakeuplag==TRUE)
                {
                    wakeuplag=0;
                    ComM_RequestComMode(0, COMM_FULL_COMMUNICATION); 
                }
            }
            if (TRUE == Gpt_5msFlag)
            {
                Gpt_5msFlag = FALSE;
                # CanNM和ComM功能的周期处理函数放在5ms任务中
                CanNm_MainFunction();
                ComM_MainFunction(0);

                Nm_GetPduData(0,buff);
                if(buff[2]==0x01)
                {
                    # 测试代码：实现网络管理的睡眠，唤醒等功能
                    for(loop = 0x0u; loop < CANNM_DEFAULT_NMPDU_LEN; loop++)
                    {                
                        CanNm_ChRunTime[0].rxPduData[loop]=0;
                    }              
                    ComM_RequestComMode(0, COMM_NO_COMMUNICATION);        
                }
                # 测试代码：实现网络管理的睡眠，唤醒等功能
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
        }
    }

验证结果
--------

根据集成目标，共配置了2个报文，其中1个网络管理发送报文，1个网络管理接收报文。

#. 系统启动后有一个报文发送（CANNM_Tx_Message1），ID
   0x400，周期100ms，初始化值和设置一致

   |image50|

   图 验证结果-1

#. 发送睡眠指令后，过一段时间后，节点会停止发送网络管理报文。如下图：

   |image51|

   图 验证结果-2

#. 发送唤醒指令后，过一段时间后，节点会继续发送网络管理报文。

   |image52|

   图 验证结果-3

.. |image1| image:: /_static/集成手册/集成手册_CANNM/image2.png
   :width: 5.76736in
   :height: 2.9125in


.. |image2| image:: /_static/集成手册/集成手册_CANNM/image3.png
   :width: 5.76736in
   :height: 2.9125in


.. |image3| image:: /_static/集成手册/集成手册_CANNM/image4.png
   :width: 5.76736in
   :height: 2.9125in


.. |image4| image:: /_static/集成手册/集成手册_CANNM/image5.png
   :width: 5.76736in
   :height: 2.9125in


.. |image5| image:: /_static/集成手册/集成手册_CANNM/image6.png
   :width: 5.76736in
   :height: 2.9125in


.. |image6| image:: /_static/集成手册/集成手册_CANNM/image7.png
   :width: 5.76736in
   :height: 2.9125in


.. |image7| image:: /_static/集成手册/集成手册_CANNM/image8.png
   :width: 5.76736in
   :height: 2.9125in


.. |image8| image:: /_static/集成手册/集成手册_CANNM/image9.png
   :width: 5.76736in
   :height: 2.9125in


.. |image9| image:: /_static/集成手册/集成手册_CANNM/image10.png
   :width: 5.76736in
   :height: 2.9125in


.. |image10| image:: /_static/集成手册/集成手册_CANNM/image11.png
   :width: 5.76736in
   :height: 2.9125in


.. |image11| image:: /_static/集成手册/集成手册_CANNM/image12.png
   :width: 5.76736in
   :height: 2.9125in


.. |image12| image:: /_static/集成手册/集成手册_CANNM/image13.png
   :width: 5.76736in
   :height: 2.9125in


.. |image13| image:: /_static/集成手册/集成手册_CANNM/image14.png
   :width: 5.76736in
   :height: 2.9125in


.. |image14| image:: /_static/集成手册/集成手册_CANNM/image15.png
   :width: 5.76736in
   :height: 2.9125in


.. |image15| image:: /_static/集成手册/集成手册_CANNM/image16.png
   :width: 5.76736in
   :height: 2.9825in


.. |image16| image:: /_static/集成手册/集成手册_CANNM/image17.png
   :width: 5.96736in
   :height: 2.9125in


.. |image17| image:: /_static/集成手册/集成手册_CANNM/image18.png
   :width: 5.76736in
   :height: 2.9825in

.. |image18| image:: /_static/集成手册/集成手册_CANNM/image19.png
   :width: 5.76736in
   :height: 2.9125in


.. |image19| image:: /_static/集成手册/集成手册_CANNM/image20.png
   :width: 5.76736in
   :height: 2.9125in


.. |image20| image:: /_static/集成手册/集成手册_CANNM/image21.png
   :width: 5.76736in
   :height: 2.9125in


.. |image21| image:: /_static/集成手册/集成手册_CANNM/image22.png
   :width: 5.76736in
   :height: 2.9125in


.. |image22| image:: /_static/集成手册/集成手册_CANNM/image23.png
   :width: 5.76736in
   :height: 2.9125in


.. |image23| image:: /_static/集成手册/集成手册_CANNM/image24.png
   :width: 5.76736in
   :height: 2.9125in


.. |image24| image:: /_static/集成手册/集成手册_CANNM/image25.png
   :width: 5.76736in
   :height: 2.9125in


.. |image25| image:: /_static/集成手册/集成手册_CANNM/image26.png
   :width: 5.76736in
   :height: 2.9125in


.. |image26| image:: /_static/集成手册/集成手册_CANNM/image27.png
   :width: 5.76736in
   :height: 2.9125in


.. |image27| image:: /_static/集成手册/集成手册_CANNM/image28.png
   :width: 5.76736in
   :height: 2.9125in


.. |image28| image:: /_static/集成手册/集成手册_CANNM/image29.png
   :width: 5.76736in
   :height: 2.9125in


.. |image29| image:: /_static/集成手册/集成手册_CANNM/image30.png
   :width: 5.76736in
   :height: 2.9125in


.. |image30| image:: /_static/集成手册/集成手册_CANNM/image31.png
   :width: 5.76736in
   :height: 2.9125in


.. |image31| image:: /_static/集成手册/集成手册_CANNM/image32.png
   :width: 5.76736in
   :height: 2.9125in


.. |image32| image:: /_static/集成手册/集成手册_CANNM/image33.png
   :width: 5.76736in
   :height: 2.9125in


.. |image33| image:: /_static/集成手册/集成手册_CANNM/image34.png
   :width: 5.76736in
   :height: 2.9125in


.. |image34| image:: /_static/集成手册/集成手册_CANNM/image35.png
   :width: 5.76736in
   :height: 2.9125in


.. |image35| image:: /_static/集成手册/集成手册_CANNM/image36.png
   :width: 5.76736in
   :height: 2.9125in


.. |image36| image:: /_static/集成手册/集成手册_CANNM/image37.png
   :width: 5.76736in
   :height: 2.9125in


.. |image37| image:: /_static/集成手册/集成手册_CANNM/image38.png
   :width: 5.76736in
   :height: 2.9125in


.. |image38| image:: /_static/集成手册/集成手册_CANNM/image39.png
   :width: 5.76736in
   :height: 2.9125in


.. |image39| image:: /_static/集成手册/集成手册_CANNM/image40.png
   :width: 5.76736in
   :height: 2.9125in


.. |image40| image:: /_static/集成手册/集成手册_CANNM/image41.png
   :width: 5.76736in
   :height: 2.9125in


.. |image41| image:: /_static/集成手册/集成手册_CANNM/image42.png
   :width: 5.76736in
   :height: 2.9125in


.. |image42| image:: /_static/集成手册/集成手册_CANNM/image43.png
   :width: 5.76736in
   :height: 2.9125in


.. |image43| image:: /_static/集成手册/集成手册_CANNM/image44.png
   :width: 5.76736in
   :height: 2.9125in


.. |image44| image:: /_static/集成手册/集成手册_CANNM/image45.png
   :width: 5.76736in
   :height: 2.9125in


.. |image45| image:: /_static/集成手册/集成手册_CANNM/image46.png
   :width: 5.76736in
   :height: 2.9125in


.. |image46| image:: /_static/集成手册/集成手册_CANNM/image47.png
   :width: 5.76736in
   :height: 2.9125in


.. |image47| image:: /_static/集成手册/集成手册_CANNM/image48.png
   :width: 5.76736in
   :height: 2.9125in


.. |image48| image:: /_static/集成手册/集成手册_CANNM/image49.png
   :width: 5.76736in
   :height: 2.9125in


.. |image49| image:: /_static/集成手册/集成手册_CANNM/image50.png
   :width: 5.76736in
   :height: 2.9125in


.. |image50| image:: /_static/集成手册/集成手册_CANNM/image51.png
   :width: 6.76736in
   :height: 4.9125in


.. |image51| image:: /_static/集成手册/集成手册_CANNM/image52.png
   :width: 5.76736in
   :height: 4.2125in


.. |image52| image:: /_static/集成手册/集成手册_CANNM/image53.png
   :width: 5.76736in
   :height: 4.2125in