=================
UDSOnCan
=================

目标
====

本集成手册用于指导客户进行诊断栈集成，文档主要包括的内容为：诊断栈集成指导、基于普通应用的集成示例讲解、项目集成特殊说明。

由于各项目的需求不同，集成示例不会针对于特定的项目做详细讲解。

缩写词和术语
============

.. table:: 表 缩写词和术语

   +-----------------+------------------------------------------------------+
   | **缩写词/术语** | **描述**                                             |
   +=================+======================================================+
   | BSW             | Basic Software                                       |
   +-----------------+------------------------------------------------------+
   | MCAL            | Microcontroller Abstraction Layer                    |
   +-----------------+------------------------------------------------------+
   | CanIf           | CAN Interface module                                 |
   +-----------------+------------------------------------------------------+
   | CanSm           | CAN State Manager module                             |
   +-----------------+------------------------------------------------------+
   | ComM            | Communication Manager module                         |
   +-----------------+------------------------------------------------------+
   | PduR            | PDU Router module                                    |
   +-----------------+------------------------------------------------------+
   | Dcm             | Diagnostic Communication Manager                     |
   +-----------------+------------------------------------------------------+
   | Dem             | Diagnostic Event Manager                             |
   +-----------------+------------------------------------------------------+
   | CanTp           | CAN Transport Layer                                  |
   +-----------------+------------------------------------------------------+
   | NvM             | NVRAM Manager                                        |
   +-----------------+------------------------------------------------------+
   | BswM            | Basic Software Mode Manager                          |
   +-----------------+------------------------------------------------------+
   | Rte             | Runtime Environment                                  |
   +-----------------+------------------------------------------------------+
   | iRte            | i-Soft Runtime Environment                           |
   +-----------------+------------------------------------------------------+

参考文档
========

[1]参考手册_CanIf.pdf

[2]参考手册_PduR.pdf

[3]参考手册_CanSM.pdf

[4]参考手册_DCM.pdf

[5]参考手册_Dem.pdf

[6]参考手册_CanTp.pdf

[7]参考手册_EcuC.pdf

[8]参考手册_BswM.pdf

[9]集成手册_BswM&EcuM.pdf

[10]集成手册_OS.pdf

[11]普华基础软件_参考手册_ORIENTAIS SWC Builder_V2_Design使用指南.pdf

[12]普华基础软件_参考手册_ORIENTAIS SWC Builder_V2_Feature使用指南.pdf

[13]普华基础软件_参考手册_ORIENTAIS SWC Builder_V2_Overview使用指南.pdf

[14]普华基础软件_参考手册_ORIENTAIS Configurator_V2_使用指南.pdf

[15]普华基础软件_参考手册_ORIENTAIS Configurator_V2_RTE使用指南.pdf

[16]普华基础软件_参考手册_ORIENTAIS Configurator_V2_iRTE使用指南.pdf

[17]ODX file导入操作说明.docx

诊断栈集成
==========

项目交付的内容为：诊断栈源码和ORIENTAIS
Studio配置工具。诊断栈细分为诊断栈的各模块及其对应的配置工具模块。

.. table:: 表 诊断栈各配置模块介绍

   +------------+------------------------------------------------------------------------------------------------------------------+
   | **模块名** | **功能**                                                                                                         |
   +============+==================================================================================================================+
   | Can        | CAN驱动配置。(由MCAL工具导入)                                                                                    |
   +------------+------------------------------------------------------------------------------------------------------------------+
   | CanIf      | CanIf模块主要处理上层模块与底层驱动的之间PDU的传递，为上层模块提供统一的接口来管理不同的CAN硬件模块              |
   +------------+------------------------------------------------------------------------------------------------------------------+
   | EcuC       | 用于辅助配置工具完成配置的模块。主要提供Pdu的定义，其它模块通过关联EcuC中Pdu，相互关联起来。                     |
   +------------+------------------------------------------------------------------------------------------------------------------+
   | PduR       | PDU Router主要为通讯接口模块（CANIF）、传输协议模块（CAN TP、J1939                                               |
   |            | TP）、诊断通讯管理模块（DCM、J1939DCM）以及通讯模块（COM、LDCOM）以及IPDUM、SECOC等模块提供基于I-PDU的路由服务。 |
   +------------+------------------------------------------------------------------------------------------------------------------+
   | CanTp      | CANTP模块实现依据ISO15765-2标准规范中定义的CAN总线数据在传输层的数据接收发送功能                                 |
   +------------+------------------------------------------------------------------------------------------------------------------+
   | Dcm        | 依据ISO15765-3和ISO14229-1标准描述，实现诊断请求报文的解析，响应(正响应和负响应)与执行                           |
   +------------+------------------------------------------------------------------------------------------------------------------+
   | Dem        | 实现诊断故障的存储与管理功能，提供API接口供其他模块读取DTC和对应的冻结帧数据和扩展数据                           |
   +------------+------------------------------------------------------------------------------------------------------------------+

.. table:: 表 诊断栈集成的步骤

   +----------+----------------------------------------+------------------------------------------------------+
   | **步骤** | **操作**                               | **说明**                                             |
   +==========+========================================+======================================================+
   | 1        | ORIENTAIS                              | 若配置工程已经搭建，则仅需进行诊断栈模块的加载操作。 |
   |          | Stuido配置工具工程搭建和诊断栈模块加载 |                                                      |
   +----------+----------------------------------------+------------------------------------------------------+
   | 2        | 模块配置及配置文件生成                 | 进行基础的诊断栈配置                                 |
   +----------+----------------------------------------+------------------------------------------------------+
   | 3        | 代码集成                               | 现有工程、诊断栈源代码和配置生成文件的集成。         |
   +----------+----------------------------------------+------------------------------------------------------+
   | 4        | 验证测试                               | 用CAN报文监测工具收发诊断报文                        |
   +----------+----------------------------------------+------------------------------------------------------+

.. note::
   **诊断栈集成之前，用户须确保已经有MCAL层可以跑通的基础工程，且诊断栈相关的其他功能栈如通信栈、网络管理栈、NvM栈能正常工作。**

新建ORIENTAIS Stuido配置工程及模块加载
--------------------------------------

#. 安装ORIENTAIS Studio软件后，双击软件图标打开软件并设置workspace。

   |image1|

   图 新建工程-1

   菜单栏File🡪New🡪Project，新建工程。

   |image2|

   图 新建工程-2

#. 在弹出的新建窗口中选择Autosar下的 [BSW Project]，选择Next。

   |image3|

   图 新建工程-3

#. 在弹出的窗口中输入工程名，选择Finish。

   |image4|

   图 新建工程-4

#. 选择[Bsw_Builder]，右键单击，选择New ECU Configuration，在弹出的窗口中选择并填写对应的Ecu名称。

   |image5|

   图 新建工程-5

   .. note::
      **可选择的Ecu可能随项目的不同而不同**

#. 选择新建的Ecu，右键单击，选择“Add Module选项”。

   |image6|

   图 新建工程-6

#. 在弹出的选项框中勾选相应模块，点击“Finish”。

   |image7|

   图 新建工程-7

#. 新建工程如下所示，上一步中添加的模块已经被加入到工程中。

   |image8|

   图 新建工程-8

模块配置及生产代码
------------------

模块配置
~~~~~~~~

.. table:: 表 诊断栈各模块配置参考文档

   +----------+--------------------------------------------+----------------+
   | **模块** | **参考文档及其章节**                       | **说明**       |
   +==========+============================================+================+
   | Can      | MCAL对应的Can配置手册                      |                |
   +----------+--------------------------------------------+----------------+
   | CanIf    | 参考手册_CanTp.pdf                         |                |
   +----------+--------------------------------------------+----------------+
   | PduR     | 参考手册_PduR.pdf                          |                |
   +----------+--------------------------------------------+----------------+
   | NvM      | 参考手册_NvM.pdf                           |                |
   +----------+--------------------------------------------+----------------+
   | CanTp    | 参考手册_CanTp.pdf                         |                |
   +----------+--------------------------------------------+----------------+
   | Dcm      | 参考手册_Dcm.pdf                           |                |
   +----------+--------------------------------------------+----------------+
   | Dem      | 参考手册_Dem.pdf                           |                |
   +----------+--------------------------------------------+----------------+

配置代码生成
~~~~~~~~~~~~

#. 在ORIENTAIS Stuido主界面左方，选择对应的诊断栈，单击右键弹出Validate All和Generate All菜单。

   |image9|

   图 配置代码的生成-1

#. 选择Validate All对本诊断栈各配置选项进行校验。

#. 选择Generate All，生成配置文件。右下角的Console窗口输出生成的配置文件信息。

   |image10|

   图 配置代码的生成-2

#. 点击config文件夹，即可查看生成的配置文件。

   |image11|

   图 配置代码的生成-3

功能集成
--------

代码集成
~~~~~~~~

诊断栈代码包括两部分：项目提供的诊断栈源码和ORIENTAIS
Studio配置生成代码。诊断栈集成包括诊断栈源码（CANIF，CANSM，PDUR，CANTP，COMM，DCM，DEM等）、定时器源码和部分其他模块源码，具体文件见表。

用户须将诊断栈源码和章节（配置代码生成）生成的源代码添加到集成开发工具的对应文件夹。诊断栈集成的文件结构，见章节（源代码集成）。

表 诊断栈源码文件

+-----------------+---------------------------------+-----------------+
| 移库文件夹      | 移库文件                        | 说明            |
+=================+=================================+=================+
| ComM            | ComM.c                          | 通信栈源码      |
|                 |                                 |                 |
|                 | ComM.h                          |                 |
|                 |                                 |                 |
|                 | ComM_BswM.h                     |                 |
|                 |                                 |                 |
|                 | ComM_BusSM.h                    |                 |
|                 |                                 |                 |
|                 | ComM_Ch.c                       |                 |
|                 |                                 |                 |
|                 | ComM_Ch.h                       |                 |
|                 |                                 |                 |
|                 | ComM_Dcm.h                      |                 |
|                 |                                 |                 |
|                 | ComM_EcuM.h                     |                 |
|                 |                                 |                 |
|                 | ComM_Internal.h                 |                 |
|                 |                                 |                 |
|                 | ComM_MemMap.h                   |                 |
|                 |                                 |                 |
|                 | ComM_Nm.h                       |                 |
|                 |                                 |                 |
|                 | ComM_Pnc.c                      |                 |
|                 |                                 |                 |
|                 | ComM_Pnc.h                      |                 |
|                 |                                 |                 |
|                 | ComM_Types.h                    |                 |
|                 |                                 |                 |
|                 | ComM_Version.h                  |                 |
+-----------------+---------------------------------+                 |
| CanIf           | CanIf.c                         |                 |
|                 |                                 |                 |
|                 | CanIf.h                         |                 |
|                 |                                 |                 |
|                 | CanIf_Can.h                     |                 |
|                 |                                 |                 |
|                 | CanIf_CanTrcv.h                 |                 |
|                 |                                 |                 |
|                 | CanIf_Cbk.h                     |                 |
|                 |                                 |                 |
|                 | CanIf_Internal.c                |                 |
|                 |                                 |                 |
|                 | CanIf_Internal.h                |                 |
|                 |                                 |                 |
|                 | CanIf_MemMap.h                  |                 |
|                 |                                 |                 |
|                 | CanIf_Types.h                   |                 |
+-----------------+---------------------------------+                 |
| CanSM           | CanSM.c                         |                 |
|                 |                                 |                 |
|                 | CanSM.h                         |                 |
|                 |                                 |                 |
|                 | CanSM_BswM.h                    |                 |
|                 |                                 |                 |
|                 | CanSM_Cbk.h                     |                 |
|                 |                                 |                 |
|                 | CanSM_MemMap.h                  |                 |
|                 |                                 |                 |
|                 | CanSM_TxTimeoutException.h      |                 |
+-----------------+---------------------------------+                 |
| PDUR            | PduR.c                          |                 |
|                 |                                 |                 |
|                 | PduR.h                          |                 |
|                 |                                 |                 |
|                 | PduR_Buffer.c                   |                 |
|                 |                                 |                 |
|                 | PduR_Buffer.h                   |                 |
|                 |                                 |                 |
|                 | PduR_Internal.c                 |                 |
|                 |                                 |                 |
|                 | PduR_Internal.h                 |                 |
|                 |                                 |                 |
|                 | PduR_MemMap.h                   |                 |
|                 |                                 |                 |
|                 | PduR_Route.c                    |                 |
|                 |                                 |                 |
|                 | PduR_Route.h                    |                 |
|                 |                                 |                 |
|                 | PduR_Types.h                    |                 |
+-----------------+---------------------------------+                 |
| CanTp           | CanTp.c                         |                 |
|                 |                                 |                 |
|                 | CanTp.h                         |                 |
|                 |                                 |                 |
|                 | CanTp_Cbk.h                     |                 |
|                 |                                 |                 |
|                 | CanTp_Internal.c                |                 |
|                 |                                 |                 |
|                 | CanTp_Internal.h                |                 |
|                 |                                 |                 |
|                 | CanTp_MemMap.h                  |                 |
|                 |                                 |                 |
|                 | CanTp_Types.h                   |                 |
+-----------------+---------------------------------+-----------------+
| BswM            | BswM.c                          | BswM源码        |
|                 |                                 |                 |
|                 | BswM.h                          |                 |
|                 |                                 |                 |
|                 | BswM_AvbAction.c                |                 |
|                 |                                 |                 |
|                 | BswM_Bsw.c                      |                 |
|                 |                                 |                 |
|                 | BswM_Bsw.h                      |                 |
|                 |                                 |                 |
|                 | BswM_CanSM.c                    |                 |
|                 |                                 |                 |
|                 | BswM_CanSM.h                    |                 |
|                 |                                 |                 |
|                 | BswM_ComM.c                     |                 |
|                 |                                 |                 |
|                 | BswM_ComM.h                     |                 |
|                 |                                 |                 |
|                 | BswM_Dcm.c                      |                 |
|                 |                                 |                 |
|                 | BswM_Dcm.h                      |                 |
|                 |                                 |                 |
|                 | BswM_DetCheck.c                 |                 |
|                 |                                 |                 |
|                 | BswM_EcuM.c                     |                 |
|                 |                                 |                 |
|                 | BswM_EcuM.h                     |                 |
|                 |                                 |                 |
|                 | BswM_EthIf.c                    |                 |
|                 |                                 |                 |
|                 | BswM_EthIf.h                    |                 |
|                 |                                 |                 |
|                 | BswM_EthSM.c                    |                 |
|                 |                                 |                 |
|                 | BswM_EthSM.h                    |                 |
|                 |                                 |                 |
|                 | BswM_FrSM.c                     |                 |
|                 |                                 |                 |
|                 | BswM_FrSM.h                     |                 |
|                 |                                 |                 |
|                 | BswM_Internal.h                 |                 |
|                 |                                 |                 |
|                 | BswM_J1939Dcm.c                 |                 |
|                 |                                 |                 |
|                 | BswM_J1939Dcm.h                 |                 |
|                 |                                 |                 |
|                 | BswM_J1939Nm.c                  |                 |
|                 |                                 |                 |
|                 | BswM_J1939Nm.h                  |                 |
|                 |                                 |                 |
|                 | BswM_LinSM.c                    |                 |
|                 |                                 |                 |
|                 | BswM_LinSM.h                    |                 |
|                 |                                 |                 |
|                 | BswM_LinTp.c                    |                 |
|                 |                                 |                 |
|                 | BswM_LinTp.h                    |                 |
|                 |                                 |                 |
|                 | BswM_MemMap.h                   |                 |
|                 |                                 |                 |
|                 | BswM_Nm.c                       |                 |
|                 |                                 |                 |
|                 | BswM_Nm.h                       |                 |
|                 |                                 |                 |
|                 | BswM_NvM.c                      |                 |
|                 |                                 |                 |
|                 | BswM_NvM.h                      |                 |
|                 |                                 |                 |
|                 | BswM_Sd.c                       |                 |
|                 |                                 |                 |
|                 | BswM_Sd.h                       |                 |
|                 |                                 |                 |
|                 | BswM_Swc.c                      |                 |
|                 |                                 |                 |
|                 | BswM_Swc.h                      |                 |
|                 |                                 |                 |
|                 | BswM_TimerControl.c             |                 |
|                 |                                 |                 |
|                 | BswM_Types.h                    |                 |
|                 |                                 |                 |
|                 | BswM_WdgM.c                     |                 |
|                 |                                 |                 |
|                 | BswM_WdgM.h                     |                 |
+-----------------+---------------------------------+-----------------+
| Dcm             | Dcm.c                           | Dcm部分源码     |
|                 |                                 |                 |
|                 | Dcm.h                           |                 |
|                 |                                 |                 |
|                 | DcmDsd.c                        |                 |
|                 |                                 |                 |
|                 | DcmDsl.c                        |                 |
|                 |                                 |                 |
|                 | DcmDsp.c                        |                 |
|                 |                                 |                 |
|                 | Dcm_Cbk.h                       |                 |
|                 |                                 |                 |
|                 | Dcm_Ext.c                       |                 |
|                 |                                 |                 |
|                 | Dcm_Ext.h                       |                 |
|                 |                                 |                 |
|                 | Dcm_Internal.h                  |                 |
|                 |                                 |                 |
|                 | Dcm_MemMap.h                    |                 |
|                 |                                 |                 |
|                 | | Dcm_Types.h                   |                 |
|                 | | Dcm_UDS0x10.c                 |                 |
|                 |                                 |                 |
|                 | Dcm_UDS0x11.c                   |                 |
|                 |                                 |                 |
|                 | Dcm_UDS0x14.c                   |                 |
|                 |                                 |                 |
|                 | Dcm_UDS0x19.c                   |                 |
|                 |                                 |                 |
|                 | Dcm_UDS0x22.c                   |                 |
|                 |                                 |                 |
|                 | Dcm_UDS0x23.c                   |                 |
|                 |                                 |                 |
|                 | Dcm_UDS0x24.c                   |                 |
|                 |                                 |                 |
|                 | Dcm_UDS0x27.c                   |                 |
|                 |                                 |                 |
|                 | Dcm_UDS0x28.c                   |                 |
|                 |                                 |                 |
|                 | Dcm_UDS0x29.c                   |                 |
|                 |                                 |                 |
|                 | Dcm_UDS0x2A.c                   |                 |
|                 |                                 |                 |
|                 | Dcm_UDS0x2C.c                   |                 |
|                 |                                 |                 |
|                 | Dcm_UDS0x2E.c                   |                 |
|                 |                                 |                 |
|                 | Dcm_UDS0x2F.c                   |                 |
|                 |                                 |                 |
|                 | Dcm_UDS0x31.c                   |                 |
|                 |                                 |                 |
|                 | Dcm_UDS0x34.c                   |                 |
|                 |                                 |                 |
|                 | Dcm_UDS0x35.c                   |                 |
|                 |                                 |                 |
|                 | Dcm_UDS0x36.c                   |                 |
|                 |                                 |                 |
|                 | Dcm_UDS0x37.c                   |                 |
|                 |                                 |                 |
|                 | Dcm_UDS0x38.c                   |                 |
|                 |                                 |                 |
|                 | Dcm_UDS0x3D.c                   |                 |
|                 |                                 |                 |
|                 | Dcm_UDS0x3E.c                   |                 |
|                 |                                 |                 |
|                 | Dcm_UDS0x85.c                   |                 |
|                 |                                 |                 |
|                 | Dcm_UDS0x86.c                   |                 |
+-----------------+---------------------------------+-----------------+
| Dem             | Dem.c                           | Dem部分源码     |
|                 |                                 |                 |
|                 | Dem.h                           |                 |
|                 |                                 |                 |
|                 | Dem_CfgTypes.h                  |                 |
|                 |                                 |                 |
|                 | Dem_Dcm.c                       |                 |
|                 |                                 |                 |
|                 | Dem_Dcm.h                       |                 |
|                 |                                 |                 |
|                 | Dem_Ext.c                       |                 |
|                 |                                 |                 |
|                 | Dem_Ext.h                       |                 |
|                 |                                 |                 |
|                 | Dem_Internal.h                  |                 |
|                 |                                 |                 |
|                 | Dem_J1939.c                     |                 |
|                 |                                 |                 |
|                 | Dem_MemMap.h                    |                 |
|                 |                                 |                 |
|                 | Dem_OBD.c                       |                 |
|                 |                                 |                 |
|                 | Dem_SubExt.c                    |                 |
|                 |                                 |                 |
|                 | Dem_Types.h                     |                 |
+-----------------+---------------------------------+-----------------+

.. note::
   **诊断栈集成之前，用户须确保已经有基础工程，且本诊断栈相关的其他功能栈能正常工作。**

集成注意事项
~~~~~~~~~~~~

对于集成过程中，诊断栈特殊要求和用户经常出现的问题，归类总结形成 表
诊断栈集成约束清单。用户需逐一排查表中的约束项，以避免集成问题出现。

.. table:: 表 诊断栈诊断栈集成约束清单

   +----------+----------+-------------------------------------------------------------------------------------------------------------+
   | **编号** | **类别** | **约束限制**                                                                                                |
   +==========+==========+=============================================================================================================+
   | **1**    | 中断     | 通信栈有中断、轮询或混合三种工作模式。若选取中断或混合模式，用户需在通信栈配置对应的中断并填充中断服务API。 |
   +----------+----------+-------------------------------------------------------------------------------------------------------------+
   | **2**    | 堆栈     | 用户需确保为任务堆栈和中断堆栈分配足够的堆栈空间。                                                          |
   +----------+----------+-------------------------------------------------------------------------------------------------------------+
   | **3**    | 头文件   | 添加诊断栈代码之后，用户需更新集成开发工具中的头文件路径。调用诊断栈API的源文件，需要包含诊断栈的头文件。   |
   +----------+----------+-------------------------------------------------------------------------------------------------------------+
   | **4**    | 初始化   | 以CAN通信为例，诊断栈的初始化顺序为：Can_Init， CanIf_Init，PduR_Init，CanSM_Init，CanTp_Init，Dcm_Init     |
   +----------+----------+-------------------------------------------------------------------------------------------------------------+
   | **5**    | 周期函数 | Dcm_MainFunction，Dem_MainFunction和CanTp_MainFunction需要被周期性任务函数调用。                            |
   +----------+----------+-------------------------------------------------------------------------------------------------------------+

集成示例
========

本章节通过普通的CAN诊断栈为例，向用户展示诊断栈的集成过程。用户可以据此熟悉诊断栈配置工具的配置过程，以及如何应用配置工具生成的配置文件。

为让用户更清晰的了解工具的使用，所用的配置均逐一手动完成。。

.. note::
   **本示例不代表用户的实际配置情况，用户需要根据自己的实际需求，决定各个参数的配置。**

集成目标
--------

**CAN报文需求：**

.. table:: 表 CAN报文需求

   +------------+------------------+-----------+----------+----------+-------------+----------+
   | **报文ID** | **报文**         | **发送**  | **发送** | **报文** | **报文**    | **工作** |
   |            |                  |           |          |          |             |          |
   |            | **名称**         | **/接收** | **模式** | **周期** | **长度**    | **模式** |
   +============+==================+===========+==========+==========+=============+==========+
   | 0x708      | CAN_DiagReqPhy   | 接收      | 触发     | -        | 8\ **字节** | 中断     |
   +------------+------------------+-----------+----------+----------+-------------+----------+
   | 0x7df      | CAN_DiagReqFun   | 接收      | 触发     | -        | 8\ **字节** | 中断     |
   +------------+------------------+-----------+----------+----------+-------------+----------+
   | 0x709      | CAN_DiagResp     | 发送      | 触发     | -        | 8\ **字节** | 中断     |
   +------------+------------------+-----------+----------+----------+-------------+----------+

模块的配置
----------

新建配置工程及模块加载操作，请参考本文档章节（模块配置及代码生成）。

Can模块配置
~~~~~~~~~~~

配置诊断协议栈之前需要使用MCAL工具配置Can模块，但是只涉及到与诊断栈中报文收发有关系的部分（主要是HardwareObeject），具体配置选项请参考MCAL工具的帮助手册进行配置。

EcuC模块配置
~~~~~~~~~~~~

#. 新建9个PDU，分别用于CanIf、CanTp、Dcm。

   |image12|

   图 EcuC模块配置-1

#. 为每个PDU配置length（根据项目不同配置不同的Pdu长度）。

   |image13|

   图 EcuC模块配置-2

   |image14|

   图 EcuC模块配置-3

   .. note::
      **Dcm Pdu长度必须与/Dcm/DcmConfigSet/DcmDsl/DcmDslBuffer里面配置的Dcm Tx、RxBuffer长度一致**

CanIf模块配置
~~~~~~~~~~~~~

#. 新建Hoh。

   |image15|

   图 CanIf模块配置-1

#. 分别新建至少1个接收诊断报文，1个发送诊断报文。

   |image16|

   图 CanIf模块配置-2

#. 分别新建2个接收诊断PDU，1个发送诊断PDU，UL选择CanTp，并选择在EcuC中配置的CanIf对应的PDU。

   |image17|

   图 CanIf模块配置-3

   |image18|

   图 CanIf模块配置-4

   |image19|

   图 CanIf模块配置-5

   |image20|

   图 CanIf模块配置-6

PduR模块配置
~~~~~~~~~~~~

#. 在PduRBswModules中添加CanTp、Dcm。

   |image21|

   图 PduR模块配置-1

#. 添加3个PduRRoutingPath，PduRRouteType配置为TP。

   |image22|

   图 PduR模块配置-2

#. 配置诊断功能寻址请求（FuncReq）、物理寻址请求（PhysReq）、响应（Resp）的路由路径。诊断请求的PduRRoutingPath的PduRSrcPdu选择CanTp对应的PDU，PduRDestPDU选择Dcm对应的PDU。诊断响应的PduRRoutingPath的则相反。

   |image23|

   图 PduR模块配置-3

   |image24|

   图 PduR模块配置-4

CanTp模块配置
~~~~~~~~~~~~~

#. CanTpGeneral的配置如下。

   |image25|

   图 CanTp模块配置-1

#. 添加1个CanTpChannel，CanTpChannelMode配置为FULL_DUPLEX全双工，并添加2个CanTpRxNSdu，1个CanTpTxNSdu，分别对应功能、物理寻址请求及响应。

   |image26|

   图 CanTp模块配置-2

#. 为每个NSdu配置相关参数，并且选择EcuC中对应的CanTp的PDU。

   |image27|

   图 CanTp模块配置-3

   |image28|

   图 CanTp模块配置-4

   |image29|

   图 CanTp模块配置-5

#. 为每个NSdu配置关联的CanIf对应的PDU，注意功能寻址请求NSdu不需要配置发送流控帧的CanTpTxFcNPdu，物理寻址请求需要配置发送流控帧的CanTpTxFcNPdu，响应的NSdu需要配置接收流控帧的CanTpRxFcNPdu，如下图所示。

   |image30|

   图 CanTp模块配置-6

   |image31|

   图 CanTp模块配置-7

   |image32|

   图 CanTp模块配置-8

Dcm模块配置
~~~~~~~~~~~

#. DcmGeneral配置

   |image33|

   图 Dcm模块配置-1

#. 配置DcmDsl，先配置Dcm
   Tx、RxBuffer及其length，需要与EcuC中Dcm对应的Pdu Length的值保持一致。

   |image34|

   图 Dcm模块配置-2

#. 配置DcmDslProtocol，选择Protocol、Buffer、ServiceTable。

   |image35|

   图 Dcm模块配置-3

#. 配置DcmDslMainConnection，选择Dcm通信的ComMChannel，并新建2个DcmDslProtocolRx，1个DcmDslProtocolTx。

   |image36|

   图 Dcm模块配置-4

#. 为每个DcmDslProtocolRx、DcmDslProtocolTx添加Dcm对应的PDU及寻址类型。

   |image37|

   图 Dcm模块配置-5

   |image38|

   图 Dcm模块配置-6

#. 配置DcmDsdServiceTable，添加所需的服务及子服务，及其寻址方式、会话访问限制、安全级访问限制。

   |image39|

   图 Dcm模块配置-7

#. 配置DcmDspSession，SessionLevel与10服务的子服务对应，P2及P2Star时间参数根据需求进行配置。

   |image40|

   图 Dcm模块配置-8

   |image41|

   图 Dcm模块配置-9

#. 配置DcmDspSerurity，SecurityLevel与27服务的子服务对应，如2701、2702对应level1，2705、2706对应level3。

   |image42|

   图 Dcm模块配置-10

#. 配置DcmDspRoutines，其中DcmDspCommonAuthorizationRef配置为每个Routine的会话访问限制与安全级访问限制。

   |image43|

   图 Dcm模块配置-11

#. Routine下的3个容器分别对应3101、3102、3103的子服务功能，可按需求选择配置，并且可在容器中配置子服务的IN/OUT参数类型及长度。

   |image44|

   图 Dcm模块配置-12

#. 配置DcmDspComControl，此项用于配置28服务控制通信的ComM channel。

   |image45|

   图 Dcm模块配置-13

#. 配置DcmDspDidInfos，此项为每个Did配置22服务可读或2E服务可写，以及相关的会话访问限制、安全级访问限制。

   |image46|

   图 Dcm模块配置-14

   |image47|

   图 Dcm模块配置-15

#. 配置DcmDspDatas，为每个Did配置DcmDspDataUsePort、类型、长度（bit为单位），并按需求选择上一步配置的DcmDspDidInfos。

   |image48|

   图 Dcm模块配置-16

#. 配置DcmDspDid，配置Did的DcmDspDidIdentifier及DcmDspDidInfos。

   |image49|

   图 Dcm模块配置-17

#. 配置DcmDspSignal，选择上一步DcmDspDatas中添加的配置。

   |image50|

   图 Dcm模块配置-18

Dem模块配置
~~~~~~~~~~~

#. 根据需求配置DemGeneral，相关配置项的意义可参考AutoSAR标准或Dem参考手册。

   |image51|

   图 Dem模块配置-1

   |image52|

   图 Dem模块配置-2

   |image53|

   图 Dem模块配置-3

#. 配置DemDataElementClass，其中可配置DemInternalDataElement（Dem内部数据）及DemExternalCSDataElement（外部CS接口获取数据）。

   |image54|

   图 Dem模块配置-4

   |image55|

   图 Dem模块配置-5

   |image56|

   图 Dem模块配置-6

#. 配置扩展数据Extended Data，需要配置DemExtendedDataRecordClass以及DemExtendedDataClass，如下图所示添加相应的配置。

   |image57|

   图 Dem模块配置-7

#. 配置冻结帧Freeze Frame，需要配置DemDidClass、DemFreezeFrameClass、DemFreezeFrameRecNumClass以及DemFreezeFrameRecordClass，如下图所示添加相应的配置。

   |image58|

   图 Dem模块配置-8

   |image59|

   图 Dem模块配置-9

   |image60|

   图 Dem模块配置-10

   |image61|

   图 Dem模块配置-11

#. 配置DemPrimaryMemory，配置Event存储的最大数量，一般与DTC数量保持一致，若DTC数量太大，可考虑采用Displacement策略，减少此存储数量。

   |image62|

   图 Dem模块配置-12

#. 配置DemDTCAttribute，选择上面几步配置中添加的配置项。

   |image63|

   图 Dem模块配置-13

#. 配置DemDebounceCounterBasedClass

   |image64|

   图 Dem模块配置-14

#. 配置DemDebounceTimeBasedClass

   |image65|

   图 Dem模块配置-15

#. 配置DemDTC，添加DTC Value，并选择DemDTCAttribute。

   |image66|

   图 Dem模块配置-16

#. 配置DemEventParameter，选择Event类型、关联的DTC及操作循环等，并可根据需求配置是否添加Debounce以及Debounce Base。

   |image67|

   图 Dem模块配置-17

   |image68|

   图 Dem模块配置-18

BswM模块配置
~~~~~~~~~~~~

BswM模块在系统服务中，详细可参考《集成手册_BswM&EcuM.pdf》文档，以下仅涉及Dcm交互相关。

#. 配置BswMModeRequestPort，新建一个BswMModeRequestPort，并选择BswMRequestProcessing，然后在BswMModeRequestSource新建BswMDcmComModeRequest，并选择对应的BswMDcmComMChannelRef。

   |image69|

   图 BswM模块配置-1

   |image70|

   图 BswM模块配置-2

#. 配置BswMModeCondition，新建一个BswMModeCondition并选择对应的BswMConditionType和BswMConditionMode，然后再选择对应的BswModeCompareValue。

   |image71|

   图 BswM模块配置-3

   |image72|

   图 BswM模块配置-4

#. 配置BswMLogicalExpression，新建一个BswMLogicalExpression并选择BswMLogicalOperator和添加对应的BswMArgumentRef。

   |image73|

   图 BswM模块配置-5

#. 配置BswMAction，若在集成COM模块时，BswM中已配置了则不需要重复配置。若无则新建一个BswMAction，然后在BswMAvailableActions下新建选择BswMPduGroupSwitch，并添加对应的BswMDisabledPduGroupRef或者BswMEnabledPduGroupRef。

   |image74|

   图 BswM模块配置-6

#. 配置BswMActionList，新建一个BswMActionList并选择BswMActionListExecution，在BswMActionListItem下新建一个BswMActionListItem，此处若需要多个Action，则多次新建，然后选择对应的BswMActionListItemRef。

   |image75|

   图 BswM模块配置-7

   |image76|

   图 BswM模块配置-8

#. 配置BswMRule，新建一个BswMRule，选择对应的BswMRuleExpressionRef，BswMRuleFalseActionList或者BswMRuleTrueActionList。

   |image77|

   图 BswM模块配置-9

源代码集成
----------

诊断栈源代码集成步骤如下：

#. 在MCAL工程的基础上，同步章（EcuC模块配置）添加的Can模块配置文件。

#. 从基线中取出章（代码集成）中相关的源代码添加到工程中。

#. 将在章（配置代码生成）中ORIENTAS配置生成的诊断相关配置文件添加到工程中。

#. 添加相关头文件目录。

诊断栈调度集成
--------------

诊断栈调度集成步骤如下：

#. 集成CanTp_Callout.c中CanTp_ResetTime、CanTp_GetTimeSpan函数。

#. 集成Dcm_Callout.c中Dcm_ResetTime、Dcm_GetTimeSpan函数。

CanTp_Callout.c集成源码如下（可以配置TM，mainfunction以及callout接口自行实现，本工程中使用mainfunction实现）：

|image78|

图 调度集成-1

|image79|

图 调度集成-2

Dcm_Callout.c集成源码如下（可以配置TM，mainfunction以及callout接口自行实现，本工程中使用mainfunction实现）：

|image80|

图 调度集成-3

|image81|

图 调度集成-4

3. 诊断栈调度集成，需要逐一排查并实现表  诊断栈集成约束清单
   所罗列的问题，以避免集成出现差错。

4. 编译链接代码，将生成的elf文件烧写进芯片。

使用iRte集成
~~~~~~~~~~~~

在BSW工具中添加iRte模块，然后更新所有bswmd文件，最后同步iRte和OS模块。若需要调整OS
Task堆栈大小，可手动调整。调整OS
Task堆栈大小可参考《集成手册_OS.pdf》文件。

|image82|

图 iRte集成-1

|image83|

图 iRte集成-2

|image84|

图 iRte集成-3

使用Rte集成
~~~~~~~~~~~

在BSW工具中添加Rte模块，然后导入萃取文件，同步萃取文件，更新bswmd文件，最后同步Rte和OS模块。若需要调整OS
Task堆栈大小，可手动调整。调整OS
Task堆栈大小可参考《集成手册_OS.pdf》文件。至于萃取文件来源，可参考SWC工具的相关使用说明文档。

|image85|

图 Rte集成-1

|image86|

图 Rte集成-2

|image87|

图 Rte集成-3

注：更新bswmd文件与同步Rte和OS模块同使用iRte集成中截图一致。

验证结果
--------

根据集成目标，共配置了3个报文，其中2个接收报文分别为诊断物理寻址及诊断功能寻址，1个发送报文为诊断响应。

|image88|

图 验证结果

.. |image1| image:: /_static/集成手册/集成手册_UDSonCAN/image2.png
   :width: 5.76736in
   :height: 3.10347in
.. |image2| image:: /_static/集成手册/集成手册_UDSonCAN/image3.png
   :width: 5.76736in
   :height: 3.10694in
.. |image3| image:: /_static/集成手册/集成手册_UDSonCAN/image4.png
   :width: 3.79528in
   :height: 3.62205in
.. |image4| image:: /_static/集成手册/集成手册_UDSonCAN/image5.png
   :width: 3.8072in
   :height: 2.92887in
.. |image5| image:: /_static/集成手册/集成手册_UDSonCAN/image6.png
   :width: 3.82677in
   :height: 3.51969in
.. |image6| image:: /_static/集成手册/集成手册_UDSonCAN/image7.png
   :width: 5.76736in
   :height: 3.10694in
.. |image7| image:: /_static/集成手册/集成手册_UDSonCAN/image8.png
   :width: 4.96934in
   :height: 8.30117in
.. |image8| image:: /_static/集成手册/集成手册_UDSonCAN/image9.png
   :width: 5.76736in
   :height: 3.10347in
.. |image9| image:: /_static/集成手册/集成手册_UDSonCAN/image10.png
   :width: 5.76736in
   :height: 3.10694in
.. |image10| image:: /_static/集成手册/集成手册_UDSonCAN/image11.png
   :width: 5.76736in
   :height: 3.10347in
.. |image11| image:: /_static/集成手册/集成手册_UDSonCAN/image12.png
   :width: 5.76736in
   :height: 3.10347in
.. |image12| image:: /_static/集成手册/集成手册_UDSonCAN/image13.png
   :width: 5.76736in
   :height: 2.60694in
.. |image13| image:: /_static/集成手册/集成手册_UDSonCAN/image14.png
   :width: 5.76736in
   :height: 2.60694in
.. |image14| image:: /_static/集成手册/集成手册_UDSonCAN/image15.png
   :width: 5.76736in
   :height: 2.60694in
.. |image15| image:: /_static/集成手册/集成手册_UDSonCAN/image16.png
   :width: 5.76736in
   :height: 2.61111in
.. |image16| image:: /_static/集成手册/集成手册_UDSonCAN/image17.png
   :width: 5.76736in
   :height: 2.60694in
.. |image17| image:: /_static/集成手册/集成手册_UDSonCAN/image18.png
   :width: 5.76736in
   :height: 2.60694in
.. |image18| image:: /_static/集成手册/集成手册_UDSonCAN/image19.png
   :width: 5.76736in
   :height: 2.60694in
.. |image19| image:: /_static/集成手册/集成手册_UDSonCAN/image20.png
   :width: 5.76736in
   :height: 2.60694in
.. |image20| image:: /_static/集成手册/集成手册_UDSonCAN/image21.png
   :width: 5.76736in
   :height: 2.60694in
.. |image21| image:: /_static/集成手册/集成手册_UDSonCAN/image22.png
   :width: 5.76736in
   :height: 2.60694in
.. |image22| image:: /_static/集成手册/集成手册_UDSonCAN/image23.png
   :width: 5.76736in
   :height: 2.60694in
.. |image23| image:: /_static/集成手册/集成手册_UDSonCAN/image24.png
   :width: 5.76736in
   :height: 2.60694in
.. |image24| image:: /_static/集成手册/集成手册_UDSonCAN/image25.png
   :width: 5.76736in
   :height: 2.60694in
.. |image25| image:: /_static/集成手册/集成手册_UDSonCAN/image26.png
   :width: 5.76736in
   :height: 2.60694in
.. |image26| image:: /_static/集成手册/集成手册_UDSonCAN/image27.png
   :width: 5.76736in
   :height: 2.60694in
.. |image27| image:: /_static/集成手册/集成手册_UDSonCAN/image28.png
   :width: 5.76736in
   :height: 2.60694in
.. |image28| image:: /_static/集成手册/集成手册_UDSonCAN/image29.png
   :width: 5.76736in
   :height: 2.60694in
.. |image29| image:: /_static/集成手册/集成手册_UDSonCAN/image30.png
   :width: 5.76736in
   :height: 2.60694in
.. |image30| image:: /_static/集成手册/集成手册_UDSonCAN/image31.png
   :width: 5.76736in
   :height: 2.60694in
.. |image31| image:: /_static/集成手册/集成手册_UDSonCAN/image32.png
   :width: 5.76736in
   :height: 2.60694in
.. |image32| image:: /_static/集成手册/集成手册_UDSonCAN/image33.png
   :width: 5.76736in
   :height: 2.60694in
.. |image33| image:: /_static/集成手册/集成手册_UDSonCAN/image34.png
   :width: 5.76736in
   :height: 2.60694in
.. |image34| image:: /_static/集成手册/集成手册_UDSonCAN/image35.png
   :width: 5.76736in
   :height: 2.60694in
.. |image35| image:: /_static/集成手册/集成手册_UDSonCAN/image36.png
   :width: 5.76736in
   :height: 2.60694in
.. |image36| image:: /_static/集成手册/集成手册_UDSonCAN/image37.png
   :width: 5.76736in
   :height: 2.60694in
.. |image37| image:: /_static/集成手册/集成手册_UDSonCAN/image38.png
   :width: 5.76736in
   :height: 2.60694in
.. |image38| image:: /_static/集成手册/集成手册_UDSonCAN/image39.png
   :width: 5.76736in
   :height: 2.60694in
.. |image39| image:: /_static/集成手册/集成手册_UDSonCAN/image40.png
   :width: 5.76736in
   :height: 2.60694in
.. |image40| image:: /_static/集成手册/集成手册_UDSonCAN/image41.png
   :width: 5.76736in
   :height: 2.60694in
.. |image41| image:: /_static/集成手册/集成手册_UDSonCAN/image42.png
   :width: 5.76736in
   :height: 2.60694in
.. |image42| image:: /_static/集成手册/集成手册_UDSonCAN/image43.png
   :width: 5.76736in
   :height: 2.60694in
.. |image43| image:: /_static/集成手册/集成手册_UDSonCAN/image44.png
   :width: 5.76736in
   :height: 2.60694in
.. |image44| image:: /_static/集成手册/集成手册_UDSonCAN/image45.png
   :width: 5.76736in
   :height: 2.60694in
.. |image45| image:: /_static/集成手册/集成手册_UDSonCAN/image46.png
   :width: 5.76736in
   :height: 2.60694in
.. |image46| image:: /_static/集成手册/集成手册_UDSonCAN/image47.png
   :width: 5.76736in
   :height: 2.60694in
.. |image47| image:: /_static/集成手册/集成手册_UDSonCAN/image48.png
   :width: 5.76736in
   :height: 2.60694in
.. |image48| image:: /_static/集成手册/集成手册_UDSonCAN/image49.png
   :width: 5.76736in
   :height: 2.60694in
.. |image49| image:: /_static/集成手册/集成手册_UDSonCAN/image50.png
   :width: 5.76736in
   :height: 2.60694in
.. |image50| image:: /_static/集成手册/集成手册_UDSonCAN/image51.png
   :width: 5.76736in
   :height: 2.60694in
.. |image51| image:: /_static/集成手册/集成手册_UDSonCAN/image52.png
   :width: 5.76736in
   :height: 2.47917in
.. |image52| image:: /_static/集成手册/集成手册_UDSonCAN/image53.png
   :width: 5.76736in
   :height: 2.47917in
.. |image53| image:: /_static/集成手册/集成手册_UDSonCAN/image54.png
   :width: 5.76736in
   :height: 2.47917in
.. |image54| image:: /_static/集成手册/集成手册_UDSonCAN/image55.png
   :width: 5.76736in
   :height: 2.47917in
.. |image55| image:: /_static/集成手册/集成手册_UDSonCAN/image56.png
   :width: 5.76736in
   :height: 2.47917in
.. |image56| image:: /_static/集成手册/集成手册_UDSonCAN/image57.png
   :width: 5.76736in
   :height: 2.47917in
.. |image57| image:: /_static/集成手册/集成手册_UDSonCAN/image58.png
   :width: 5.76736in
   :height: 2.47917in
.. |image58| image:: /_static/集成手册/集成手册_UDSonCAN/image59.png
   :width: 5.76736in
   :height: 2.47917in
.. |image59| image:: /_static/集成手册/集成手册_UDSonCAN/image60.png
   :width: 5.76736in
   :height: 2.47917in
.. |image60| image:: /_static/集成手册/集成手册_UDSonCAN/image61.png
   :width: 5.76736in
   :height: 2.47917in
.. |image61| image:: /_static/集成手册/集成手册_UDSonCAN/image62.png
   :width: 5.76736in
   :height: 2.47917in
.. |image62| image:: /_static/集成手册/集成手册_UDSonCAN/image63.png
   :width: 5.76736in
   :height: 2.47917in
.. |image63| image:: /_static/集成手册/集成手册_UDSonCAN/image64.png
   :width: 5.76736in
   :height: 2.47917in
.. |image64| image:: /_static/集成手册/集成手册_UDSonCAN/image65.png
   :width: 5.76736in
   :height: 2.47917in
.. |image65| image:: /_static/集成手册/集成手册_UDSonCAN/image66.png
   :width: 5.76736in
   :height: 2.47917in
.. |image66| image:: /_static/集成手册/集成手册_UDSonCAN/image67.png
   :width: 5.76736in
   :height: 2.47917in
.. |image67| image:: /_static/集成手册/集成手册_UDSonCAN/image68.png
   :width: 5.76736in
   :height: 2.47917in
.. |image68| image:: /_static/集成手册/集成手册_UDSonCAN/image69.png
   :width: 5.76736in
   :height: 2.47917in
.. |image69| image:: /_static/集成手册/集成手册_UDSonCAN/image70.png
   :width: 5.76736in
   :height: 2.47917in
.. |image70| image:: /_static/集成手册/集成手册_UDSonCAN/image71.png
   :width: 5.76736in
   :height: 2.47917in
.. |image71| image:: /_static/集成手册/集成手册_UDSonCAN/image72.png
   :width: 5.76736in
   :height: 2.47917in
.. |image72| image:: /_static/集成手册/集成手册_UDSonCAN/image73.png
   :width: 5.76736in
   :height: 2.47917in
.. |image73| image:: /_static/集成手册/集成手册_UDSonCAN/image74.png
   :width: 5.76736in
   :height: 2.47917in
.. |image74| image:: /_static/集成手册/集成手册_UDSonCAN/image75.png
   :width: 5.76736in
   :height: 2.47917in
.. |image75| image:: /_static/集成手册/集成手册_UDSonCAN/image76.png
   :width: 5.76736in
   :height: 2.47917in
.. |image76| image:: /_static/集成手册/集成手册_UDSonCAN/image77.png
   :width: 5.76736in
   :height: 2.47917in
.. |image77| image:: /_static/集成手册/集成手册_UDSonCAN/image78.png
   :width: 5.76736in
   :height: 2.47917in
.. |image78| image:: /_static/集成手册/集成手册_UDSonCAN/image79.png
   :width: 5.76736in
   :height: 2.47917in
.. |image79| image:: /_static/集成手册/集成手册_UDSonCAN/image80.png
   :width: 5.76736in
   :height: 2.44792in
.. |image80| image:: /_static/集成手册/集成手册_UDSonCAN/image81.png
   :width: 5.76736in
   :height: 2.47917in
.. |image81| image:: /_static/集成手册/集成手册_UDSonCAN/image82.png
   :width: 5.76736in
   :height: 2.44792in
.. |image82| image:: /_static/集成手册/集成手册_UDSonCAN/image83.png
   :width: 3.65527in
   :height: 3.34776in
.. |image83| image:: /_static/集成手册/集成手册_UDSonCAN/image84.png
   :width: 5.76736in
   :height: 3.10694in
.. |image84| image:: /_static/集成手册/集成手册_UDSonCAN/image85.png
   :width: 5.76736in
   :height: 3.10694in
.. |image85| image:: /_static/集成手册/集成手册_UDSonCAN/image86.png
   :width: 3.61114in
   :height: 3.30733in
.. |image86| image:: /_static/集成手册/集成手册_UDSonCAN/image87.png
   :width: 5.76736in
   :height: 3.10694in
.. |image87| image:: /_static/集成手册/集成手册_UDSonCAN/image88.png
   :width: 5.76736in
   :height: 2.47917in
.. |image88| image:: /_static/集成手册/集成手册_UDSonCAN/image89.png
   :width: 5.76736in
   :height: 5.51319in
