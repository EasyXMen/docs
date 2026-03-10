=================
UDSonLIN
=================

目标
====

本文档旨在通过一个LIN诊断的示例工程的配置，向用户展示协议栈的集成过程。通过阅读本文档，用户可以了解ORIENTAIS配置工具的配置过程，以及如何应用配置工具生成的配置文件。

为了让用户更清晰的了解工具的使用，所用的配置均逐一手动完成。用户在了解了配置的基本过程后，可以快速完成配置。

缩写词和术语
============

.. table:: 表 缩写词和术语

   +-----------------+---------------------------------------------------+
   | **缩写词/术语** |                      **描述**                     |
   +-----------------+---------------------------------------------------+
   | ASW             | Application Software 应用软件                     |
   +-----------------+---------------------------------------------------+
   | BSW             | Basic Software 基础软件                           |
   +-----------------+---------------------------------------------------+
   | MCAL            | Micro Controller Abstraction Layer 微控制器抽象层 |
   +-----------------+---------------------------------------------------+
   | LINIF           | LIN Interface Module LIN接口模块                  |
   +-----------------+---------------------------------------------------+
   | LINTP           | LIN Transport Layer Module LIN传输模块            |
   +-----------------+---------------------------------------------------+
   | ComM            | Communication Manager Module 通信管理模块         |
   +-----------------+---------------------------------------------------+
   | EcuM            | ECU State Manager Module ECU状态管理模块          |
   +-----------------+---------------------------------------------------+
   | PduR            | PDU Router Module PDU路由器模块                   |
   +-----------------+---------------------------------------------------+
   | Dcm             | Diagnostic Communication Manager 诊断通信模块     |
   +-----------------+---------------------------------------------------+
   | Dem             | Diagnostic Event Manager 诊断事件管理模块         |
   +-----------------+---------------------------------------------------+
   | BswM            | Basic Software Mode Manager 基础软件模式管理器    |
   +-----------------+---------------------------------------------------+
   | Rte             | Runtime Environment 运行时环境                    |
   +-----------------+---------------------------------------------------+
   | iRte            | i-Soft Runtime Environment 普华基础模块运行时环境 |
   +-----------------+---------------------------------------------------+

参考文档
========

[1]参考手册_LinIf.pdf

[2]参考手册_PduR.pdf

[3]参考手册_Dcm.pdf

[4]参考手册_Dem.pdf

[5]参考手册\_ UDSonCAN.pdf

协议栈集成
==========

项目交付的内容为：协议栈源码和ORIENTAIS
Studio配置工具。协议栈细分为协议栈的各模块及其对应的配置工具模块。

协议栈各配置模块的功能介绍，参见表 协议栈各配置模块介绍。

使用协议栈源码和配置工具，进行协议栈的集成的步骤，参见表
协议栈集成的步骤。

.. table:: 表 协议栈各配置模块介绍

   +------------+-------------------------------------------------------------------------------------------------------+
   | **模块名** |                                                **功能**                                               |
   +------------+-------------------------------------------------------------------------------------------------------+
   | Lin        | LIN驱动配置。(由EB工具导入，详见章节（Lin模块配置）)                                                  |
   +------------+-------------------------------------------------------------------------------------------------------+
   | LinIf      | LinIf模块主要处理上层模块与底层驱动的之间PDU的传递，为上层模块提供统一的接口来管理不同的LIN硬件模块。 |
   +------------+-------------------------------------------------------------------------------------------------------+
   | EcuC       | 用于辅助配置工具完成配置的模块。主要提供Pdu的定义，其它模块通过关联EcuC中Pdu，相互关联起来。          |
   +------------+-------------------------------------------------------------------------------------------------------+
   | PduR       | PDU Router主要为相关模块提供基于I-PDU的路由服务。在UDSonLIN栈中，主要是提供LinTP与DCM之间的路由服务。 |
   +------------+-------------------------------------------------------------------------------------------------------+
   | Dcm        | 依据ISO15765-3和ISO14229-1标准描述，实现诊断请求报文的解析，响应(正响应和负响应)与执行。              |
   +------------+-------------------------------------------------------------------------------------------------------+
   | Dem        | 实现诊断故障的存储与管理功能，提供API接口供其他模块读取DTC和对应的冻结帧数据和扩展数据。              |
   +------------+-------------------------------------------------------------------------------------------------------+

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

   图 主界面

#. 菜单栏File🡪New🡪Project，新建工程。

   |image2|

   图 新建工程

#. 在弹出的新建窗口中选择Autosar下的 [BSW Project]，选择Next。

   |image3|

   图 新建工程

#. 在弹出的窗口中输入工程名，选择Finish。

   |image4|
   
   图 输入工程名

#. 选择[Bsw_Builder]，右键单击，选择New ECU Configuration。

   |image5|

   图 新建ECU

#. 在弹出的窗口中输入ECU名，然后选择Next。

   |image6|

   图 选择MCU

#. 在弹出的窗口中勾选需添加的模块，点击Finish。

   |image7|

   图 选择模块

#. 新建工程如下所示，步骤⑦中添加的模块已经被加入到工程中。

   |image8|

   图 添加模块

模块配置及生产代码
------------------

模块配置
~~~~~~~~

模块的具体配置，取决于具体的项目需求。

.. table:: 表 协议栈各模块配置参考文档

   +----------+----------------------------------------+-------------------+
   | **模块** | **参考文档**                           | **说明**          |
   +==========+========================================+===================+
   | Lin      | MCAL对应的Lin配置手册                  |                   |
   +----------+----------------------------------------+-------------------+
   | LinIf    | 参考手册LinIf.pdf                      |                   |
   +----------+----------------------------------------+-------------------+
   | Dcm      | 参考手册Dcm.pdf                        |                   |
   +----------+----------------------------------------+-------------------+
   | PduR     | 参考手册PduR.pdf                       |                   |
   +----------+----------------------------------------+-------------------+
   | Dem      | 参考手册Dem.pdf                        |                   |
   +----------+----------------------------------------+-------------------+

配置代码生成
~~~~~~~~~~~~

#. 在ORIENTAIS Stuido主界面左方，选择对应的协议栈，单击右键弹出Validate
   All和Generate All菜单。

   |image9|

   图 检验验证

#. 选择Validate All对本协议栈各配置选项进行校验，没有错误提示信息即校验通过。若有错误信息，请按照错误提示修改。

#. 选择Generate All，生成配置文件。右下角的Console窗口输出生成的配置文件信息。

   |image10|

   图 生成配置文件

#. 将ORIENTAIS Studio切换到Resource模式，即可查看生成的配置文件。

   |image11|

   图 配置文件

发功能集成
----------

代码集成 
~~~~~~~~~

协议栈代码包括两部分：项目提供的协议栈源码和ORIENTAIS
Studio配置生成代码。

用户须将协议栈源码和章节（配置代码生成）生成的源代码添加到集成开发工具的对应文件夹。协议栈集成的文件结构，见章节（源代码集成）。

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
   | **4**    | 初始化   | UDSonLIN的初始化顺序为：Lin_Init， LinIf_Init， PduR_Init， LinTp_Init，Dcm \_Init，Dem_PreInit，       |
   |          |          | Dem_Init。                                                                                              |
   +----------+----------+---------------------------------------------------------------------------------------------------------+
   | **5**    | 周期函数 | Dcm_MainFunction，Dem_MainFunction和LinIf_MainFunction需要被周期性任务函数调用。                        |
   +----------+----------+---------------------------------------------------------------------------------------------------------+

集成示例
========

本章节通过普通的LIN诊断栈为例，向用户展示LIN诊断栈的集成过程。用户可以据此熟悉LIN诊断栈配置工具的配置过程，以及如何应用配置工具生成的配置文件。

为让用户更清晰的了解工具的使用，所用的配置均逐一手动完成。工具有配置文件（arxml文件）生成和导入功能，如果有配置好的arxml文件，用户可以使用工具中的arxml文件导入功能，快速完成配置。

.. note::
   **本示例不代表用户的实际配置情况，用户需要根据自己的实际需求，决定各个参数的配置。**

集成目标

集成后的工程为从节点LIN，集成完成后的工程可以进行诊断服务

信号设置如下表所示：

.. table:: 表

   +--------------------------+------------+--------+------------+-------------------------------+
   | **帧名称**               | **帧类型** | **ID** | **Tx\\Rx** | **节点地址**                  |
   +==========================+============+========+============+===============================+
   | **LinIfFrame_MasterReq** | 诊断帧     | 0x3C   | RX         | **物理地址：0x0A              |
   |                          |            |        |            | 功能地址：0x7e**              |
   +--------------------------+------------+--------+------------+-------------------------------+
   | **LinIfFrame_SlaveResp** | 诊断帧     | 0x3D   | TX         | **物理地址：0x0A**            |
   +--------------------------+------------+--------+------------+-------------------------------+

模块的配置
----------

新建配置工程及模块加载操作，请参考本文档章节（模块配置及生产代码）。

Lin模块配置
~~~~~~~~~~~

配置诊断协议栈之前需要使用 MCAL 工具配置 Lin
模块，但是只涉及到与诊断栈中报文收发有关系的部分（主要是
HardwareObeject）。该集成示例为从节点LIN，需要将LIN配置为从节点。具体配置选项请参考
MCAL工具的参考手册进行配置。

EcuC模块配置
~~~~~~~~~~~~

#. 双击EcuC模块，打开EcuC模块配置界面。

   |image12|

   图 EcuC配置

#. 在EcucConfigSets栏目上右键，选择EcucConfigSet。再在EcucConfigSet上右键，选择New🡪EcucPduCollection。

   |image13|

   图 EcucConfigSet

   ·PduLengthTypeEnum
   选择UINT16（这个参数是定义存储数据长度时使用的变量的长度，示例选择UINT16，若配置的报文长度都是8，不会超过255，选择UINT8即可）

#. 在EcucPduCollection上右键，选择Pdu，会生成一个Pdu的配置界面。

   |image14|

   图 新建Pdu

   这里按照发送和接收，可以将Pdu名字改为报文的名字。LIN诊断需要配置6个Pdu，分别用于LinTp、Dcm。

   |image14|

   图 配置Pdu

#. 为每个 Pdu 配置 Length（根据项目不同配置不同的 Pdu 长度）。

   |image15|\ |image16|

   图 配置Pdu的Length

.. note::
   Dcm Pdu 长度必须与/Dcm/DcmConfigSet/DcmDsl/DcmDslBuffer 里面配置的
   Dcm Tx、RxBuffer长度一致。

LinIf模块配置
~~~~~~~~~~~~~

#. 双击LinIf模块，打开LinIf模块的配置界面。

   |image17|

   图 LinIf配置

#. LinIfGeneral标签页使能LinIfTpSupported选项。

#. 在LinIfGlobalConfig标签页下依次打开LinIfGlobalConfigs
   ->LinIfGlobalConfig
   ->LinIfChannel_1->LinIfFrames新建LinFrame用于诊断请求。

   |image18|

   图 新建LinFrame

#. 然后右击LinIfChannel_1新建LinFrame用于诊断响应。

   |image19|

   图 新建响应报文

#. 双击LinTp模块，进入LinTp配置页面，LinTpGeneral配置界面不需要配置

   |image20|

   图 LinTpGeneral配置界面

#. 选择LinTpGlobalConfig标签，LinTpGlobalConfig->LinTpChannelConfigs新建一个LinTpChannelConfig。再关联对应的ComMChannel。

   |image21|

   图 关联Channel

#. 选择LinTpRxNSdus新建物理地址的Sdu，根据需求配置对应的Ncr，NAD关联对应的ComMChannel

   |image22|

   图 新建物理地址Sdu

#. 选择LinTpRxNSdus新建功能地址的Sdu，根据需求配置对应的Ncr，NAD关联对应的ComMChannel。

   |image23|

   图 新建功能地址Sdu

#. 选择LinTpTxNSdus新建响应的Sdu，根据需求配置对应的Nas，Ncs，NAD，关联对应的LinChannel和ComMChannel。

   |image24|

   图 新建响应Sdu

PduR模块配置
~~~~~~~~~~~~

#. 双击PduR模块，打开PduR模块的配置界面。在PduRBswModules中添加Dcm和LinTp。

   |image25|

   图 PduR模块配置

#. 打开PduRRoutingTables标签页，添加3个PduRRoutingPath。

   |image26|

   图 添加PduRRoutingPath

#. 配置诊断功能寻址请求（FuncReq）、物理寻址请求（PhysReq）、响应（Resp）的路由路径。诊断请求的PduRRoutingPath的PduRSrcPdu选择LinTp对应的PDU，PduRDestPDU选择Dcm对应的PDU。诊断响应的PduRRoutingPath的则相反。

   |image27|

   图 配置物理寻址路由

   |image28|

   图 配置功能寻址路由

   |image29|

   图 配置响应路由

Dcm模块配置
~~~~~~~~~~~

Dcm模块配置可参考《集成手册_UDSonLIN.pdf》中Dcm的配置，Lin的诊断配置只需修改DcmDsl模块：

添加对应的Lin诊断的buffer：

|image30|

图 DCM配置-DCMConfigSets

添加DcmDslProtocol:

|image31|

图 DCM配置-DCMConfigSets

Dem模块配置
~~~~~~~~~~~

请参考《集成手册_UDSonLIN.pdf》中的Dem配置。

BswM模块配置
~~~~~~~~~~~~

请参考《集成手册_UDSonLIN.pdf》中的BswM配置。

源代码集成
----------

诊断栈源代码集成步骤如下：

#. 在 MCAL 工程的基础上，同步章添加的 Lin 模块配置文件。

#. 从基线中取出章（代码集成）中相关的源代码添加到工程中。

#. 将在章（模块配置）中 ORIENTAS 配置生成的诊断相关配置文件添加到工程中。

#. 添加相关头文件目录。

协议栈调度集成
--------------

诊断栈调度集成步骤如下：

#. 诊断栈调度集成，需要逐一排查并实现表
   诊断栈集成约束清单所罗列的问题，以避免集成出现差错。

#. 编译链接代码，将生成的elf文件烧写进芯片。

使用iRte集成
~~~~~~~~~~~~

请参考《集成手册_UDSonLIN.pdf》中的使用iRte集成。

使用Rte集成
~~~~~~~~~~~

请参考《集成手册_UDSonLIN.pdf》中的使用Rte集成。

验证结果
--------

根据集成目标，共配置了3个报文，其中2个接收报文分别为诊断物理寻址及诊断功能寻址，1个发送报文为诊断响应。

   |image32|

   图 验证结果

.. |image1| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_UDSonLIN/image2.png
   :width: 5.76736in
   :height: 3.10347in
.. |image2| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_UDSonLIN/image3.png
   :width: 5.76736in
   :height: 3.10694in
.. |image3| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_UDSonLIN/image4.png
   :width: 3.79528in
   :height: 3.62205in
.. |image4| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_UDSonLIN/image5.png
   :width: 3.8072in
   :height: 2.92887in
.. |image5| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_UDSonLIN/image6.png
   :width: 3.82677in
   :height: 3.51969in
.. |image6| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_UDSonLIN/image7.png
   :width: 5.76736in
   :height: 3.10694in
.. |image7| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_UDSonLIN/image8.png
   :width: 4.96934in
   :height: 8.30117in
.. |image8| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_UDSonLIN/image9.png
   :width: 5.76736in
   :height: 3.10347in
.. |image9| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_UDSonLIN/image10.png
   :width: 5.76736in
   :height: 3.10694in
.. |image10| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_UDSonLIN/image11.png
   :width: 5.76736in
   :height: 3.10347in
.. |image11| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_UDSonLIN/image12.png
   :width: 5.76736in
   :height: 3.10347in
.. |image12| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_UDSonLIN/image13.png
   :width: 5.76736in
   :height: 2.60694in
.. |image13| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_UDSonLIN/image14.png
   :width: 5.76736in
   :height: 2.60694in
.. |image14| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_UDSonLIN/image15.png
   :width: 5.76736in
   :height: 2.60694in
.. |image15| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_UDSonLIN/image16.png
   :width: 5.76736in
   :height: 2.61111in
.. |image16| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_UDSonLIN/image17.png
   :width: 5.76736in
   :height: 2.60694in
.. |image17| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_UDSonLIN/image18.png
   :width: 5.76736in
   :height: 2.60694in
.. |image18| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_UDSonLIN/image19.png
   :width: 5.76736in
   :height: 2.60694in
.. |image19| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_UDSonLIN/image20.png
   :width: 5.76736in
   :height: 2.60694in
.. |image20| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_UDSonLIN/image21.png
   :width: 5.76736in
   :height: 2.60694in
.. |image21| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_UDSonLIN/image22.png
   :width: 5.76736in
   :height: 2.60694in
.. |image22| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_UDSonLIN/image23.png
   :width: 5.76736in
   :height: 2.60694in
.. |image23| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_UDSonLIN/image24.png
   :width: 5.76736in
   :height: 2.60694in
.. |image24| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_UDSonLIN/image25.png
   :width: 5.76736in
   :height: 2.60694in
.. |image25| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_UDSonLIN/image26.png
   :width: 5.76736in
   :height: 2.60694in
.. |image26| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_UDSonLIN/image27.png
   :width: 5.76736in
   :height: 2.60694in
.. |image27| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_UDSonLIN/image28.png
   :width: 5.76736in
   :height: 2.60694in
.. |image28| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_UDSonLIN/image29.png
   :width: 5.76736in
   :height: 2.60694in
.. |image29| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_UDSonLIN/image30.png
   :width: 5.76736in
   :height: 2.60694in
.. |image30| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_UDSonLIN/image31.png
   :width: 5.76736in
   :height: 2.60694in
.. |image31| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_UDSonLIN/image32.png
   :width: 5.76736in
   :height: 2.60694in
.. |image32| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_UDSonLIN/image33.png
   :width: 5.76736in
   :height: 2.60694in