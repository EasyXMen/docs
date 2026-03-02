============
CAN
============

目标
====

本集成手册用于指导客户进行通信栈集成，文档主要包括的内容为：通信栈集成指导。

由于各项目的需求不同，集成示例不会针对于特定的商业项目做详细讲解。

缩写词和术语
============

.. table:: 表

   +-----------------+------------------------------------------------------+
   | **缩写词/术语** | **描述**                                             |
   +=================+======================================================+
   | BSW             | Basic Software 基础软件层                            |
   +-----------------+------------------------------------------------------+
   | BswM            | Basic Software Mode Manager基础软件模式管理器        |
   +-----------------+------------------------------------------------------+
   | MCAL            |   Microcontroller Abstraction Layer 微控制器抽象层   |
   +-----------------+------------------------------------------------------+
   | CANIF           | CAN Interface module CAN接口模块                     |
   +-----------------+------------------------------------------------------+
   | CanSm           | CAN State Manager module CAN状态管理器模块           |
   +-----------------+------------------------------------------------------+
   | ComM            | Communication Manager module通信管理器模块           |
   +-----------------+------------------------------------------------------+
   | EcuM            | ECU State Manager module ECU状态管理器模块           |
   +-----------------+------------------------------------------------------+
   | SchM            | Scheduler Module调度程序模块                         |
   +-----------------+------------------------------------------------------+

参考文档
========

[1]参考手册_CanIf.pdf

[2]参考手册_Com.pdf

[3]参考手册_EcuC.pdf

[4]参考手册_PduR.pdf

[5]参考手册_CanSM.pdf

Can通信栈集成
=============

项目交付的内容为：Can通信栈源码和ORIENTAIS
Studio配置工具。通信栈细分为通信栈的各模块及其对应的配置工具模块。

通信栈各配置模块的功能介绍，参见表 通信栈各配置模块介绍。

使用通信栈源码和配置工具，进行通信栈的集成的步骤，参见表
通信栈集成的步骤。

.. table:: 表 通信栈各配置模块介绍

   +--------+---------------------------------------------------------------------------------------------------------------------------+
   | 模块名 |                                                            功能                                                           |
   +--------+---------------------------------------------------------------------------------------------------------------------------+
   | Can    | CAN驱动配置。(由mcal配置工具导入，详见章节Can模块配置)                                                                    |
   +--------+---------------------------------------------------------------------------------------------------------------------------+
   | CanIf  | CanIf模块主要处理上层模块与底层驱动的之间PDU的传递，为上层模块提供统一的接口来管理不同的CAN硬件模块                       |
   +--------+---------------------------------------------------------------------------------------------------------------------------+
   | EcuC   | 用于辅助配置工具完成配置的模块。主要提供Pdu的定义，其它模块通过关联EcuC中Pdu，相互关联起来。                              |
   +--------+---------------------------------------------------------------------------------------------------------------------------+
   | PduR   | PDU Router主要为通讯接口模块（CANIF）、传输协议模块、诊断通讯管理模块以及通讯模块提供基于I-PDU的路由服务。                |
   +--------+---------------------------------------------------------------------------------------------------------------------------+
   | Com    | COM模块主要提供I-PDU和信号相关管理功能                                                                                    |
   +--------+---------------------------------------------------------------------------------------------------------------------------+
   | CanSM  | 主要功能是与通信硬件抽象层和系统服务层产生交互，为每一个CAN通信总线定义一个总线相关的状态管理，并为相关的总线提供流控制。 |
   +--------+---------------------------------------------------------------------------------------------------------------------------+

.. table:: 表 通信栈集成的步骤

   +----------+----------------------------------------+------------------------------------------------------+
   | **步骤** | **操作**                               | **说明**                                             |
   +==========+========================================+======================================================+
   | 1        | ORIENTAIS                              | 若配置工具已经搭建，则仅需进行通信栈模块的加载操作。 |
   |          | Stuido配置工具工程搭建和通信栈模块加载 |                                                      |
   +----------+----------------------------------------+------------------------------------------------------+
   | 2        | 模块配置及配置文件生成                 | NA                                                   |
   +----------+----------------------------------------+------------------------------------------------------+
   | 3        | 代码集成                               | 现有工程、通信栈源代码和配置生成文件的集成。         |
   +----------+----------------------------------------+------------------------------------------------------+
   | 4        | 验证测试                               | NA                                                   |
   +----------+----------------------------------------+------------------------------------------------------+

.. note::
   **通信栈集成之前，用户须确保已经有基础工程，且本通信栈相关的其他通信栈能正常工作。**

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

#. 在弹出的窗口中加载工程数据。

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

模块的具体配置，取决于具体的项目需求。该通信栈各模块配置项的详细介绍，参见表
通信栈各模块配置参考文档。

.. table:: 表 通信栈各模块配置参考文档

   +----------+---------------------------------------------+--------------+
   | **模块** | **参考文档及其章节**                        | **说明**     |
   +==========+=============================================+==============+
   | Can      | MCAL对应的Can配置手册                       |              |
   +----------+---------------------------------------------+--------------+
   | CanIf    | 参考手册_CanIf.pdf                          |              |
   +----------+---------------------------------------------+--------------+
   | PduR     | 参考手册_PduR.pdf                           |              |
   +----------+---------------------------------------------+--------------+
   | Com      | 参考手册_Com.pdf                            |              |
   +----------+---------------------------------------------+--------------+
   | CanSM    | 参考手册_CanSM.pdf                          |              |
   +----------+---------------------------------------------+--------------+
   | EcuC     | 参考手册_EcuC.pdf                           |              |
   +----------+---------------------------------------------+--------------+
   | ComM     | 参考手册_ComM.pdf                           |              |
   +----------+---------------------------------------------+--------------+

配置代码生成
~~~~~~~~~~~~

#. 在ORIENTAIS Stuido主界面左方，选择对应的通信栈，单击右键弹出Validate
   All和Generate All菜单。

   |image11|

   图 模块配置

#. 选择Validate
   All对本通信栈各配置选项进行校验，没有错误提示信息即校验通过。若有错误信息，请按照错误提示修改。

#. 选择Generate
   All，生成配置文件。右下角的Console窗口输出生成的配置文件信息。

   |image12|

   图 模块配置

#. 将ORIENTAIS Studio切换到Resource模式，即可查看生成的配置文件。

   |image13|

   图 模块配置

功能集成
--------

代码集成
~~~~~~~~

通信栈代码包括两部分：项目提供的通信栈源码和ORIENTAIS
Studio配置生成代码。通信栈集成包括通信栈源码（CAN、CanIf、PduR、ComM、CanSM等）、定时器源码和部分其他模块源码，具体文件见表。

用户须将通信栈源码和章节（配置代码生成）生成的源代码添加到集成开发工具的对应文件夹。通信栈集成的文件结构，见章节（Can通信栈集成）。

表 通信栈源码文件

+-----------------+----------------------------------------------------------------------------------------------------------------------------+-----------------+
| 移库文件夹      | 移库文件                                                                                                                   | 说明            |
+=================+============================================================================================================================+=================+
| ComM            | ComM.c、                                                                                                                   | 通信栈源码      |
|                 |                                                                                                                            |                 |
|                 | ComM.h、                                                                                                                   |                 |
|                 |                                                                                                                            |                 |
|                 | ComM_BusSM.h、                                                                                                             |                 |
|                 |                                                                                                                            |                 |
|                 | ComM_Com.h、                                                                                                               |                 |
|                 |                                                                                                                            |                 |
|                 | ComM_Dcm.h、                                                                                                               |                 |
|                 |                                                                                                                            |                 |
|                 | ComM_EcuMBswM.h、ComM_Internal.c、ComM_Internal.h、ComM_MemMap.h、                                                         |                 |
|                 |                                                                                                                            |                 |
|                 | ComM_Nm.h                                                                                                                  |                 |
+-----------------+----------------------------------------------------------------------------------------------------------------------------+                 |
| CanIf           | CanIf.c、                                                                                                                  |                 |
|                 |                                                                                                                            |                 |
|                 | CanIf.h、                                                                                                                  |                 |
|                 |                                                                                                                            |                 |
|                 | CanIf_Cbk.h、CanIf_MemMap.h、CanIf_Types.h                                                                                 |                 |
+-----------------+----------------------------------------------------------------------------------------------------------------------------+                 |
| CanSM           | CanSM.c、                                                                                                                  |                 |
|                 |                                                                                                                            |                 |
|                 | CanSM.h、                                                                                                                  |                 |
|                 |                                                                                                                            |                 |
|                 | CanSM_BswM.h、                                                                                                             |                 |
|                 |                                                                                                                            |                 |
|                 | CanSM_Cbk.h、                                                                                                              |                 |
|                 |                                                                                                                            |                 |
|                 | CanSM_ComM.h、CanSM_MemMap.h、CanSM_TxTimeoutException.h                                                                   |                 |
+-----------------+----------------------------------------------------------------------------------------------------------------------------+                 |
| PDUR            | PduR_CanIf.h、                                                                                                             |                 |
|                 |                                                                                                                            |                 |
|                 | PduR_Com.h、PduR_Internal.c、PduR_Internal.h、PduR_MemMap.h、PduR_Types.h、                                                |                 |
|                 |                                                                                                                            |                 |
|                 | PduR.c、                                                                                                                   |                 |
|                 |                                                                                                                            |                 |
|                 | PduR.h                                                                                                                     |                 |
+-----------------+----------------------------------------------------------------------------------------------------------------------------+                 |
| Com             | Com.c、                                                                                                                    |                 |
|                 |                                                                                                                            |                 |
|                 | Com.h、                                                                                                                    |                 |
|                 |                                                                                                                            |                 |
|                 | Com_Cbk.h、Com_GwInternal.c、Com_Internal.c、Com_Internal.h、Com_MemMap.h、Com_RxInternal.c、Com_TxInternal.c、Com_Types.h |                 |
+-----------------+----------------------------------------------------------------------------------------------------------------------------+-----------------+
| SchM            | SchM.c、                                                                                                                   | SchM部分源码    |
|                 |                                                                                                                            |                 |
|                 | SchM.h、                                                                                                                   |                 |
|                 |                                                                                                                            |                 |
|                 | SchM_Com.h、                                                                                                               |                 |
|                 |                                                                                                                            |                 |
|                 | SchM_ComM.h、                                                                                                              |                 |
|                 |                                                                                                                            |                 |
|                 | SchM_CanIf.h、                                                                                                             |                 |
|                 |                                                                                                                            |                 |
|                 | SchM_PduR.h、                                                                                                              |                 |
+-----------------+----------------------------------------------------------------------------------------------------------------------------+-----------------+
| BswM            | BswM.c、                                                                                                                   | BswM部分源码    |
|                 |                                                                                                                            |                 |
|                 | BswM.h、                                                                                                                   |                 |
|                 |                                                                                                                            |                 |
|                 | BswM_CanSM.h、                                                                                                             |                 |
|                 |                                                                                                                            |                 |
|                 | BswM_ComM.h、                                                                                                              |                 |
+-----------------+----------------------------------------------------------------------------------------------------------------------------+-----------------+
| EcuM            | EcuM_Types.h、                                                                                                             | EcuM部分源码    |
|                 |                                                                                                                            |                 |
|                 | EcuM.h、                                                                                                                   |                 |
+-----------------+----------------------------------------------------------------------------------------------------------------------------+-----------------+

.. note::
   **通信栈集成之前，用户须确保已经有基础工程，且本通信栈相关的其他通信栈能正常工作。**

集成注意事项
~~~~~~~~~~~~

对于集成过程中，通信栈特殊要求和用户经常出现的问题，归类总结形成 表
通信栈集成约束清单。用户需逐一排查表中的约束项，以避免集成问题出现。

.. table:: 表 通信栈集成约束清单

   +----------+----------+-------------------------------------------------------------------------------------------------------------+
   | **编号** | **类别** | **约束限制**                                                                                                |
   +==========+==========+=============================================================================================================+
   | **1**    | 中断     | 通信栈有中断、轮询或混合三种工作模式。若选取中断或混合模式，用户需在通信栈配置对应的中断并填充中断服务API。 |
   +----------+----------+-------------------------------------------------------------------------------------------------------------+
   | **2**    | 堆栈     | 用户需确保为任务堆栈和中断堆栈分配足够的堆栈空间。                                                          |
   +----------+----------+-------------------------------------------------------------------------------------------------------------+
   | **3**    | 头文件   | - 添加通信栈代码之后，用户需更新集成开发工具中的头文件路径。                                                |
   |          |          |                                                                                                             |
   |          |          | - 调用通信栈API的源文件，需要包含通信栈的头文件。                                                           |
   +----------+----------+-------------------------------------------------------------------------------------------------------------+
   | **4**    | 初始化   | 以CAN通信为例，通信栈的初始化顺序为：Can_Init， CanIf_Init， PduR_Init， Com_Init，CanSM_Init。             |
   +----------+----------+-------------------------------------------------------------------------------------------------------------+
   | **5**    | 周期函数 | Com_MainFunctionRx，Com_MainFunctionRouteSignals和Com_MainFunctionTx需要被周期性任务函数调用。              |
   +----------+----------+-------------------------------------------------------------------------------------------------------------+

集成示例
========

本章节通过普通的CAN通信栈为例，向用户展示通信栈的集成过程。用户可以据此熟悉通信栈配置工具的配置过程，以及如何应用配置工具生成的配置文件。

为让用户更清晰的了解工具的使用，所用的配置均逐一手动完成。用户可以使用工具中的DBC导入功能，快速完成配置。DBC导入功能不属于本文档介绍范畴，具体操作请参照《参考手册_ORIENTAIS
Studio_使用指南.pdf》的导入DBC文件章节。

.. note::
   **本示例不代表用户的实际配置情况，用户需要根据自己的实际需求，决定各个参数的配置。**

集成目标
--------

**CAN报文需求：**

.. table:: 表

   +------------+------------------+-----------+----------+----------+-------------+----------+
   | **报文ID** | **报文**         | **发送**  | **发送** | **报文** | **报文**    | **工作** |
   |            |                  |           |          |          |             |          |
   |            | **名称**         | **/接收** | **模式** | **周期** | **长度**    | **模式** |
   +============+==================+===========+==========+==========+=============+==========+
   | 0x100      | CAN_Tx_Message1  | 发送      | 周期     | 50ms     | 8\ **字节** | 轮询     |
   +------------+------------------+-----------+----------+----------+-------------+----------+
   | 0x105      | CAN_Tx_Message2  | 发送      | 触发     | -        | 8\ **字节** | 轮询     |
   +------------+------------------+-----------+----------+----------+-------------+----------+
   | 0x120      | CAN_Rx_Message1  | 接收      | NA       | 100ms    | 8\ **字节** | 轮询     |
   +------------+------------------+-----------+----------+----------+-------------+----------+
   | 0x125      | CAN_Rx_Message2  | 接收      | NA       | -        | 8\ **字节** | 轮询     |
   +------------+------------------+-----------+----------+----------+-------------+----------+

**CAN报文信号需求：**

- CAN_Tx_Message1(0x100)包含的信号

   |image14|

   图 集成示例-1

- CAN_Tx_Message2(0x105) 包含的信号

   |image15|

   图 集成示例-2

- CAN_Rx_Message1(0x120) 包含的信号

   |image16|

   图 集成示例-3

- CAN_Rx_Message1(0x125) 包含的信号

   |image17|

   图 集成示例-4

模块的配置
----------

新建配置工程及模块加载操作，请参考本文档章节（模块配置及代码生成）。

Can模块配置
~~~~~~~~~~~

有多种工具可以用于配置mcal，本章介绍如何使用EB工具配置Can模块，但是只涉及到与通信栈中报文收发有关系的部分（主要是HardwareObeject），其余配置选项请参考EB工具的帮助手册进行配置。

#. 打开EB工具，新建CAN模块后，在以下路径配置HardwareObject：

CAN模块🡪CanConfigSet🡪CanHardwareObject。

根据本次配置示例的目标，需要配置4个HardwareObject，如下图所示：

   |image18|

   图 模块配置-1

.. note::
   **HardwareObject定义的时候，必须接收报文放在发送报文前面。**

#. 完成EB配置后，生成Can模块的配置文件，替换工程中原有的Can模块的配置文件。

#. 导出EB的配置文件。

#. 将3导出的配置文件，导入到ORIENTAIS Studio中。

..

   导入后工程如下图所示：

   |image19|

   图 模块配置-2


#. 双击CanIf模块，打开CanIf模块的配置界面。

   |image20|

   图 模块配置-3

#. CanIfDispatchCfg、CanIfPrivateCfg、CanIfPublicCfg、CanIfTrcvDrvCfg标签页均保持默认值，不需要配置。

#. 在CanIfInitCfg标签页下的容器[CanIfInitCfg]上，右边新建一个CanIfInitHohCfg对象。

   |image21|

   图 模块配置-4

#. CanIfCtrlDrvCfg配置：

   #. [CanIfCtrlDrvCfg_0]的配置项CanIfCtrlDrvInitHohConfigRef需要关联到步骤3中创建的HOH对象。

   #. [CanIfCtrlDrvNameRef]的配置项选MCAL->Can中配置的名称。

   |image22|

   图 模块配置-5

#. CanIfCtrlCfg配置：

   #. 将默认生成的[CanIfCtrlCfg_0]名字改为[CanIfCtrlCfg_Controller0]。

   #. 参数CanIfCtrlCanCtrlRef，选择CanController_0。

   |image23|

   图 模块配置-6

   可点击CanIfInitCfg后再右边新建CanIfBufferCfg、CanIfInitHohCfg、CanIfRxPduCfg、CanIfTxPduCfg；也可以在容器[CanIfInitCfg]上右键，在弹窗中选择新建的配置。
      
      |image24|
      
      图 模块配置-7

#. 新建一个CanIfInitHohCfg，再在新建的容器[CanIfInitHohCfg_0]上右键新建2个CanIfHrhCfg和2个CanIfHthCfg。然后将新建的容器改为有意义的名字。

   #. 每个发送报文需要一个CanIfHthCfg，每个接收报文需要一个CanIfHrhCfg。

   |image25|

   图 模块配置-8

#. 配置CanIfHrhCfg_Rx_Message1和CanIfHrhCfg_Rx_Message2。

   |image26|

   图 模块配置-9

   |image27|

   图 模块配置-10

#. 配置CanIfHthCfg_Tx_Message1和CanIfHthCfg_Tx_Message2。

   |image28|

   图 模块配置-11

   |image29|

   图 模块配置-12

#. 新建2个CanIfBufferCfg，并修改名字。每个发送报文需要建立一个CanIfBufferCfg。

   |image30|

   图 模块配置-13

   |image31|

   图 模块配置-14

#. 新建1个CanIfRxPduCfg，并修改名字。每个接收报文需要在CanIf中配置对应的CanIfRxPduCfg。报文CAN_Rx_Message1对应的CanIfRxPduCfg参数配置如下：

   .. table:: 表

      +------------------------------+-------------------------+---------------------------------------------------+
      | 参数名                       | 设置值                  | 说明                                              |
      +==============================+=========================+===================================================+
      | CanIfRxPduCanId              | 0x120                   | 报文ID（参照DBC）                                 |
      +------------------------------+-------------------------+---------------------------------------------------+
      | CanIfRxPduCanIdType          | STANDARD_CAN            | 帧类型：标准帧                                    |
      +------------------------------+-------------------------+---------------------------------------------------+
      | CanIfRxPduDlc                | 8                       | 报文长度 （参照DBC）                              |
      +------------------------------+-------------------------+---------------------------------------------------+
      | CanIfRxPduUserRxIndicationUL | PDUR                    | CanIf模块收到报文后通知PduR模块                   |
      +------------------------------+-------------------------+---------------------------------------------------+
      | CanIfRxPduHrhIdRef           | CanIfHrhCfg_Rx_Message1 | 关联到对应的Hrh（本章节步骤⑧创建）                |
      +------------------------------+-------------------------+---------------------------------------------------+
      | CanIfRxPduRef                | CAN_Rx_Message1         | 关联到EcuC中定义的pdu,此处命名规则为XXX（报文名） |
      +------------------------------+-------------------------+---------------------------------------------------+

   |image32|

   图 模块配置-15

   用同样的方法配置CanIfRxPduCfg_Rx_Message2：

      |image33|

      图 模块配置-16

#. 新建2个CanIfTxPduCfg，并修改名字。每个接收报文需要在CanIf中配置对应的CanIfTxPduCfg。报文CAN_Tx_Message1对应的CanIfTxPduCfg参数配置如下：

   .. table:: 表

      +--------------------------------+-------------------------+------------------------------------+
      | 参数名                         | 设置值                  | 说明                               |
      +================================+=========================+====================================+
      | CanIfTxPduCanId                | 0x100                   | CAN ID                             |
      +--------------------------------+-------------------------+------------------------------------+
      | CanIfTxPduCanIdType            | STANDARD_CAN            | 帧类型：标准帧                     |
      +--------------------------------+-------------------------+------------------------------------+
      | CanIfTxPduType                 | STATIC                  | 静态CAN ID                         |
      +--------------------------------+-------------------------+------------------------------------+
      | CanIfTxPduUserTxConfirmationUL | PDUR                    | 报文发送成功确认通知传递给PDUR模块 |
      +--------------------------------+-------------------------+------------------------------------+
      | CanIfTxPduBufferRef            | CanIfHthCfg_Tx_Message1 | 关联到对应HtH                      |
      +--------------------------------+-------------------------+------------------------------------+
      | CanIfTxPduRef                  | CAN_Tx_Message1         | 关联到EcuC中的Pdu                  |
      +--------------------------------+-------------------------+------------------------------------+

   |image34|

   图 模块配置-17

   用同样的方法配置CanIfTxPduCfg_Tx_Message2：

      |image35|

      图 模块配置-18

#. 校验配置，无错误信息，即配置完成。

EcuC模块配置
~~~~~~~~~~~~

#. 双击EcuC模块，打开EcuC模块的配置界面。

   |image36|

   图 EcuC配置-1

#. 右击EcucConfigSets新建EcucConfigSet，右击EcucConfigSet新建EcucPduCollections，右击EcucPduCollections新建EcucPduCollection，右击EcucPduCollections新建MetaDataTypes和Pdus，MetaDataTypes保持默认。

#. 新建8个Pdu并修改名字，配置报文方向和报文长度。

   .. note::

      此处配置pdu为两组，命名需要分开，方便后续配置需要使用。推荐规则为Com_XXX和XXX两种(XXX代表报文名)。

   |image37|

   图 EcuC配置-2

#. 其他页面保持默认即可。

Com模块配置
~~~~~~~~~~~

以下是层级关系修改后的完整rst文档：

Com模块配置
~~~~~~~~~~~

#. 双击Com模块，打开Com模块的配置界面。

   |image38|

   图 Com配置-1

#. ComSupportedIPduGroups填写数目，且与ComIPduGroup数量保持一致，其他配置选择默认。

   |image39|

   图 Com配置-2

#. 选择ComConfig页面配置，新建目标数量的ComIPdu、ComIPduGroup、ComSignal并修改名称：

   发送ComIPdu的属性配置如图。

   接收ComIPdu的属性配置ComIPduDirection为RECEIVE和ComIPduGroupRef新建选择ComIPduGroup_Rx。

   |image40|

   图 Com配置-3

#. 选中ComIPdu，配置发送ComIPdu的属性配置如图：

   接收ComIPdu的属性配置ComIPduDirection为RECEIVE和ComIPduGroupRef新建选择ComIPduGroup_Rx。

   .. note::
         ComPduIdRef选择Com_XX的相应报文，此处对应EcuC的配置；
         ComIPduSignalRef需要新建选择该报文所包含的所有信号；

   |image41|

   图 Com配置-4

   |image42|

   图 Com配置-5

#. 在发送IPDU新建ComTxIPdu，配置ComMinimumDelayTime为0.005s，其他保持默认：

   #. 在接收IPDU中不需要新建ComTxIPdu。

   |image43|

   图 Com配置-6

#. 在发送ComTxIPdu新建ComTxModeTrue，按照需求选择ComTxModeMode为周期、事件或者混合型发送模式此处为周期型发送，ComTxModeNumberOfRepetitions、ComTxModeRepetitionPeriod、ComTxModeTimeOffset和ComTxModeTimePeriod按照不同发送模式配置具体请参照需求设置。

   |image44|

   图 Com配置-7

#. 选定信号后设置ComBitPosition、ComBitSize、ComSignalEndianness、ComSignalInitValue、ComSignalType和ComTransferProperty等参数。ComTransferProperty的配置，需要考虑与IPDU发送模式相配合从而实现相应的发送类型，此处为周期报文选择PENDING。

   |image45|

   图 Com配置-8

#. ComTimeBase配置保持默认。

   |image46|

   图 Com配置-9

PduR模块配置
~~~~~~~~~~~~

#. 双击PduR模块，打开PduR模块的配置界面，PduRGeneral保持默认配置。

   |image47|

   图 PduR配置-1

#. 打开PduRBswModules新建PduRBswModules_CanIf和PduRBswModules_Com，PduRBswModuleRef分别选择CanIf和Com，其他配置保持默认。

   |image48|

   图 PduR配置-2

#. 打开PduRRoutingTables新建一个PduRRoutingTable，再PduRRoutingTable中新建PduRRoutingPath如图。

   |image49|

   图 PduR配置-3

#. 找到并选中PduRDestPdu，配置右边PduRDestPduRef。

   .. note:: 
    接收报文 PduRSrcPduRef 选择 XXX（此处对应 EcuC 的配置）；  
    发送报文 PduRDestPduRef 选择 Com_XXX（此处对应 EcuC 的配置）；

   如下图为发送报文配置目标pdu。

   |image50|

   图 PduR配置-4

#. 找到并选中PduRSrcPdu，配置右边PduRSrcPduRef。

.. note:: 
    接收报文 PduRSrcPduRef 选择 XXX（此处对应 EcuC 的配置）；  
    发送报文 PduRDestPduRef 选择 Com_XXX（此处对应 EcuC 的配置）；

如下图为发送报文配置源pdu。

   |image51|

   图 PduR配置-5

CanSM模块配置
~~~~~~~~~~~~~

#. 找到并选中CanSMManagerNetwork，配置右边CanSMComMNetworkHandleRef此配置与ComM模块关联。

   |image52|

   图 CanSMp配置-1

#. 找到并选中CanSMController，配置右边CanSMControllerId此配置与CanIf模块关联。

   |image53|

   图 CanSMp配置-2

ComM模块配置
~~~~~~~~~~~~

#. 找到并添加ComMUser

   |image54|

   图 ComM模块配置-1

#. 修改ComMChannel，配置右边ComMBusType为COMM_BUS_TYPE_CAN

   |image55|

   图 ComM模块配置-2

#. 找到ComMNetworkManagement配置，ComMNmVariant设置为NONE

   |image56|

   图 ComM模块配置-3

#. 找到ComMUserPreChannels配置，将之前配置的user关联到channel

   |image57|

   图 ComM模块配置-4

源代码集成
----------

项目交付给用户的工程结构如下：

   |image58|

   图 交付工程

- BSW目录，这个目录放置所有基础软件相关代码，除了MCAL、Config文件夹之外，均按bsw源码路径放置

- ASW目录，存放应用代码

- Config目录，存放mcal和bsw生成的动态代码

- MCAL目录，存放mcal的静态代码

通信栈源代码集成步骤如下：

#. 将章节（模块的配置）中EB MCAL生成的CAN模块配置文件和ORIENTAIS Studio
   生成的配置文件复制到Config/BSW_Config文件夹中。

#. 将MCAL提供的CAN模块源码和项目提供的通信栈源代码文件复制到BS
   W和MCAL文件夹中。

通信栈调度集成
--------------

通信栈调度集成步骤如下：

#. 通信栈调度集成，需要逐一排查并实现表 通信栈集成约束清单
   所罗列的问题，以避免集成出现差错。

#. 编译链接代码，将生成的elf文件烧写进芯片。

通信栈有关的代码，在下方的main.c文件中给出重点标注。

.. note::
   本示例中，通信栈初始化的代码和启动通信的代码置于main.c文件，并不代表其他项目同样适用于将其置于main.c文件中。

.. code-block:: c
   :linenos:
   :emphasize-lines: 5-10, 25-29, 32-36, 39-40, 53-54, 57, 63-64, 67-87

    #include <machine/wdtcon.h>
    #include "Mcu.h"
    #include "Port.h"
    #通信栈相关模块头文件
    #include "Can_17_MCanP.h"
    #include "CanIf.h"
    #include "Com.h"
    #include "PduR.h"
    #include "ComM.h"
    #include "CanSM.h"
    #include "ComM_EcuMBswM.h"

    int main(void)
    {
    /*Initialize ECUM Module*/
    EcuM_Init(&EcuM_ConfigAlternative[0]);

    /*Initialize FlsLoader*/
    FlsLoader_Init(NULL_PTR);

    /*Dem module Pre_Init*/
    Dem_PreInit();

    #初始化Can，CanIf，PduR，Com，CanSM模块
    Can_17_MCanP_Init(&Can_17_MCanP_ConfigRoot[0]);
    CanIf_Init(&CanIf_InitCfgSet);
    PduR_Init(&PduR_PBConfigData);
    Com_Init(&Com_PBConfigData);
    CanSM_Init(&CanSM_Config);

    #使能接收，发送组，打开超时监控
    Com_IpduGroupVector ipduGroupVector;
    Com_SetIpduGroup(ipduGroupVector, ComIPduGroup_CAN_Rx,TRUE);
    Com_SetIpduGroup(ipduGroupVector, ComIPduGroup_CAN_Tx,TRUE);
    Com_ReceptionDMControl(ipduGroupVector); 
    Com_IpduGroupControl(ipduGroupVector,TRUE);

    #打开通信
    ComM_RequestComMode(ComMChannel_0, COMM_FULL_COMMUNICATION);
    ComM_CommunicationAllowed(ComMUser_0, TRUE);

    Gpt_EnableNotification(GptConf_GptChannel_Gpt_1ms);
    Gpt_StartTimer(GptConf_GptChannel_Gpt_1ms, 100000);

    /* infinite loop */
    while (1)
    {
        if(Gpt_5msFlag == TRUE)
        {
        /* please insert your code here... */
        uint64 u8_test = 0;
        #CanSM和ComM的周期处理函数放在5ms任务中
        CanSM_MainFunction();
        ComM_MainFunction_ComMChannel_0();

        #获取ComM的状态，FULL_COMMNNICATION状态时，进行Com通信
        ComM_GetCurrentComMode(ComMUser_0,&can_BusMode);
        ComM_ModeType can_BusMode = COMM_NO_COMMUNICATION;

        if (COMM_FULL_COMMUNICATION == can_BusMode)
        {
            #Com模块接收和信号路由周期处理函数
            Com_MainFunctionRx();
            Com_MainFunctionRouteSignals();
            /* Test Code */
            #测试代码：将接收到的报文用发送报文转发出来
            if (TRUE == CAN_Rx_Message1_Signal1_Recevive_Flag)
            {
                CAN_Rx_Message1_Signal1_Recevive_Flag = FALSE;
                Com_ReceiveSignal(CAN_Rx_Message1_Signal1,&u8_ComTest);
                Com_SendSignal(CAN_Tx_Message1_Signal1,&u8_ComTest);
                Com_ReceiveSignal(CAN_Rx_Message1_Signal2,&u8_ComTest); 
                Com_SendSignal(CAN_Tx_Message1_Signal2,&u8_ComTest);
                Com_ReceiveSignal(CAN_Rx_Message1_Signal3,&u8_ComTest);
                #测试代码：将接收到的报文用发送报文转发出来
                Com_SendSignal(CAN_Tx_Message1_Signal3,&u8_ComTest);
                Com_ReceiveSignal(CAN_Rx_Message1_Signal4,&u8_ComTest);
                Com_SendSignal(CAN_Tx_Message1_Signal4,&u8_ComTest);
            }
            if (TRUE == CAN_Rx_Message2_Signal1_Recevive_Flag)
            {
                CAN_Rx_Message2_Signal1_Recevive_Flag = FALSE;
                Com_ReceiveSignal(CAN_Rx_Message2_Signal1,&u8_ComTest);
                Com_SendSignal(CAN_Tx_Message2_Signal1,&u8_ComTest);
            }
            #Com模块发送周期处理函数
            Com_MainFunctionTx();
        }
        }
        return 0;
    }
    }

验证结果
--------

根据集成目标，共配置了4个报文，其中1个周期发送报文，1个触发发送报文，还有2个与发送报文信号配置一致的接收报文。

#. 系统启动后有一个报文发送（CAN_Tx_Message1），ID
   0x100，周期50ms，初始化值和设置一致

   |image59|

   图 验证结果-1

#. 本地发送一帧ID为0x120的报文(CAN_Rx_Message1)后，发送报文0x100(CAN_Tx_Message1)的值发生变化

   |image60|

   图 验证结果-2

#. 本地发送一帧ID为0x125的报文（CAN_Rx_Message2）后，开发板发送一帧ID为0x105的报文（CAN_Tx_Message2）

   |image61|

   图 验证结果-3

.. |image1| image:: /_static/集成手册/集成手册_CAN/image2.png
   :width: 5.76736in
   :height: 2.9125in


.. |image2| image:: /_static/集成手册/集成手册_CAN/image3.png
   :width: 5.76736in
   :height: 2.9125in


.. |image3| image:: /_static/集成手册/集成手册_CAN/image4.png
   :width: 5.76736in
   :height: 2.9125in


.. |image4| image:: /_static/集成手册/集成手册_CAN/image5.png
   :width: 5.76736in
   :height: 2.9125in


.. |image5| image:: /_static/集成手册/集成手册_CAN/image6.png
   :width: 5.76736in
   :height: 2.9125in


.. |image6| image:: /_static/集成手册/集成手册_CAN/image7.png
   :width: 5.76736in
   :height: 2.9125in


.. |image7| image:: /_static/集成手册/集成手册_CAN/image8.png
   :width: 5.76736in
   :height: 2.9125in


.. |image8| image:: /_static/集成手册/集成手册_CAN/image9.png
   :width: 5.76736in
   :height: 2.9125in


.. |image9| image:: /_static/集成手册/集成手册_CAN/image10.png
   :width: 5.76736in
   :height: 2.9125in


.. |image10| image:: /_static/集成手册/集成手册_CAN/image11.png
   :width: 5.76736in
   :height: 2.9125in


.. |image11| image:: /_static/集成手册/集成手册_CAN/image12.png
   :width: 5.76736in
   :height: 2.9125in


.. |image12| image:: /_static/集成手册/集成手册_CAN/image13.png
   :width: 5.76736in
   :height: 2.9125in


.. |image13| image:: /_static/集成手册/集成手册_CAN/image14.png
   :width: 5.76736in
   :height: 2.9125in


.. |image14| image:: /_static/集成手册/集成手册_CAN/image15.png
   :width: 7.76736in
   :height: 2.9125in


.. |image15| image:: /_static/集成手册/集成手册_CAN/image16.png
   :width: 9.76736in
   :height: 1.4825in


.. |image16| image:: /_static/集成手册/集成手册_CAN/image17.png
   :width: 6.96736in
   :height: 2.9125in


.. |image17| image:: /_static/集成手册/集成手册_CAN/image18.png
   :width: 9.76736in
   :height: 1.4825in

.. |image18| image:: /_static/集成手册/集成手册_CAN/image19.png
   :width: 5.76736in
   :height: 2.9125in


.. |image19| image:: /_static/集成手册/集成手册_CAN/image20.png
   :width: 5.76736in
   :height: 2.9125in


.. |image20| image:: /_static/集成手册/集成手册_CAN/image21.png
   :width: 5.76736in
   :height: 2.9125in


.. |image21| image:: /_static/集成手册/集成手册_CAN/image22.png
   :width: 5.76736in
   :height: 2.9125in


.. |image22| image:: /_static/集成手册/集成手册_CAN/image23.png
   :width: 5.76736in
   :height: 2.9125in


.. |image23| image:: /_static/集成手册/集成手册_CAN/image24.png
   :width: 5.76736in
   :height: 2.9125in


.. |image24| image:: /_static/集成手册/集成手册_CAN/image25.png
   :width: 5.76736in
   :height: 2.9125in


.. |image25| image:: /_static/集成手册/集成手册_CAN/image26.png
   :width: 5.76736in
   :height: 2.9125in


.. |image26| image:: /_static/集成手册/集成手册_CAN/image27.png
   :width: 5.76736in
   :height: 2.9125in


.. |image27| image:: /_static/集成手册/集成手册_CAN/image28.png
   :width: 5.76736in
   :height: 2.9125in


.. |image28| image:: /_static/集成手册/集成手册_CAN/image29.png
   :width: 5.76736in
   :height: 2.9125in


.. |image29| image:: /_static/集成手册/集成手册_CAN/image30.png
   :width: 5.76736in
   :height: 2.9125in


.. |image30| image:: /_static/集成手册/集成手册_CAN/image31.png
   :width: 5.76736in
   :height: 2.9125in


.. |image31| image:: /_static/集成手册/集成手册_CAN/image32.png
   :width: 5.76736in
   :height: 2.9125in


.. |image32| image:: /_static/集成手册/集成手册_CAN/image33.png
   :width: 5.76736in
   :height: 2.9125in


.. |image33| image:: /_static/集成手册/集成手册_CAN/image34.png
   :width: 5.76736in
   :height: 2.9125in


.. |image34| image:: /_static/集成手册/集成手册_CAN/image35.png
   :width: 5.76736in
   :height: 2.9125in


.. |image35| image:: /_static/集成手册/集成手册_CAN/image36.png
   :width: 5.76736in
   :height: 2.9125in


.. |image36| image:: /_static/集成手册/集成手册_CAN/image37.png
   :width: 5.76736in
   :height: 2.9125in


.. |image37| image:: /_static/集成手册/集成手册_CAN/image38.png
   :width: 5.76736in
   :height: 2.9125in


.. |image38| image:: /_static/集成手册/集成手册_CAN/image39.png
   :width: 5.76736in
   :height: 2.9125in


.. |image39| image:: /_static/集成手册/集成手册_CAN/image40.png
   :width: 5.76736in
   :height: 2.9125in


.. |image40| image:: /_static/集成手册/集成手册_CAN/image41.png
   :width: 5.76736in
   :height: 2.9125in


.. |image41| image:: /_static/集成手册/集成手册_CAN/image42.png
   :width: 5.76736in
   :height: 2.9125in


.. |image42| image:: /_static/集成手册/集成手册_CAN/image43.png
   :width: 5.76736in
   :height: 2.9125in


.. |image43| image:: /_static/集成手册/集成手册_CAN/image44.png
   :width: 5.76736in
   :height: 2.9125in


.. |image44| image:: /_static/集成手册/集成手册_CAN/image45.png
   :width: 5.76736in
   :height: 2.9125in


.. |image45| image:: /_static/集成手册/集成手册_CAN/image46.png
   :width: 5.76736in
   :height: 2.9125in


.. |image46| image:: /_static/集成手册/集成手册_CAN/image47.png
   :width: 5.76736in
   :height: 2.9125in


.. |image47| image:: /_static/集成手册/集成手册_CAN/image48.png
   :width: 5.76736in
   :height: 2.9125in


.. |image48| image:: /_static/集成手册/集成手册_CAN/image49.png
   :width: 5.76736in
   :height: 2.9125in


.. |image49| image:: /_static/集成手册/集成手册_CAN/image50.png
   :width: 5.76736in
   :height: 2.9125in


.. |image50| image:: /_static/集成手册/集成手册_CAN/image51.png
   :width: 5.76736in
   :height: 2.9125in


.. |image51| image:: /_static/集成手册/集成手册_CAN/image52.png
   :width: 5.76736in
   :height: 2.9125in


.. |image52| image:: /_static/集成手册/集成手册_CAN/image53.png
   :width: 5.76736in
   :height: 2.9125in


.. |image53| image:: /_static/集成手册/集成手册_CAN/image54.png
   :width: 5.76736in
   :height: 2.9125in


.. |image54| image:: /_static/集成手册/集成手册_CAN/image55.png
   :width: 5.76736in
   :height: 2.9125in


.. |image55| image:: /_static/集成手册/集成手册_CAN/image56.png
   :width: 5.76736in
   :height: 2.9125in


.. |image56| image:: /_static/集成手册/集成手册_CAN/image57.png
   :width: 5.76736in
   :height: 2.9125in


.. |image57| image:: /_static/集成手册/集成手册_CAN/image58.png
   :width: 5.76736in
   :height: 2.9125in


.. |image58| image:: /_static/集成手册/集成手册_CAN/image59.png
   :width: 5.76736in
   :height: 2.9125in


.. |image59| image:: /_static/集成手册/集成手册_CAN/image60.png
   :width: 5.76736in
   :height: 2.9125in


.. |image60| image:: /_static/集成手册/集成手册_CAN/image61.png
   :width: 5.76736in
   :height: 2.9125in


.. |image61| image:: /_static/集成手册/集成手册_CAN/image62.png
   :width: 5.76736in
   :height: 2.9125in