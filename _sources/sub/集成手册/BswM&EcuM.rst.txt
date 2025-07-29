====================
BswM&EcuM
====================


目标
====

该文档描述了系统服务模块BswM&EcuM的集成，旨在让该模块开发实施人员对该模块的应用有粗浅认知。本集成工程含有通信栈，网络管理栈，系统服务栈，通过系统服务栈实现对通信栈报文收发控制，及网络管理栈休眠唤醒和网络模式的请求等简单功能。通信栈及网路管理栈的集成请参照相关文档，本文档不做详细说明。

说明：BswM模块涉及BSW模块很多（包括CAN通信、网络管理、诊断模块；LIN通信、网络管理、诊断模块以及EtherNet通信、网络管理、诊断模块等），配置根据需求可以非常灵活，无固定范式；EcuM模块根据节点功能需求配置也相对灵活。本文档只做入门之用，若要深入请研读AUTOSAR标准。

由于各项目的需求不同，该集成示例不会针对于特定的商业项目做详细讲解。特定商业项目的主要集成问题，将在项目集成特殊说明章节讲述。

缩写词和术语
============

+-----------------+--------------------------------------------------------------------+
| **缩写词/术语** | **描述**                                                           |
+=================+====================================================================+
| **ASW**         | **application software**                                           |
+-----------------+--------------------------------------------------------------------+
| **BSW**         | **Basic Software**                                                 |
+-----------------+--------------------------------------------------------------------+
| **MCAL**        | **Microcontroller Abstract ion Layer**                             |
+-----------------+--------------------------------------------------------------------+
| **CanIf**       | **CAN Interface module**                                           |
+-----------------+--------------------------------------------------------------------+
| **CanSM**       | **CAN State Manager module**                                       |
+-----------------+--------------------------------------------------------------------+
| **ComM**        | **Communication Manager module**                                   |
+-----------------+--------------------------------------------------------------------+
| **EcuM**        | **ECU State Manager module**                                       |
+-----------------+--------------------------------------------------------------------+
| **PduR**        | **PDU Router module**                                              |
+-----------------+--------------------------------------------------------------------+
| **SchM**        | **Scheduler Module**                                               |
+-----------------+--------------------------------------------------------------------+
| **Com**         | **Communication**                                                  |
+-----------------+--------------------------------------------------------------------+
| **CanNm**       | **CAN Network Management**                                         |
+-----------------+--------------------------------------------------------------------+
| **NMIf**        | **Network Management Interface**                                   |
+-----------------+--------------------------------------------------------------------+
| **BswM**        | **Basic Software Mode Manager**                                    |
+-----------------+--------------------------------------------------------------------+
| **EcuM**        | **ECU State Manager**                                              |
+-----------------+--------------------------------------------------------------------+

参考文档
========

[1] AUTOSAR_SWS_BSWModeManager.pdf.

[2] AUTOSAR_SWS_ECUStateManager.pdf.

[3] Autosar R19-11_参考手册_BswM.pdf

[4] Autosar R19-11_参考手册_EcuM.pdf

协议栈集成
==========

普华交付的内容为：协议栈源码和ORIENTAIS Studio配置工具。协议栈细分为协议栈的各模块及其对应的配置工具模块。

系统服务栈各模块的功能介绍，参见表 系统服务栈模块介绍。

使用协议栈源码和配置工具，进行协议栈的集成的步骤，参见表 协议栈集成的步骤。

.. table:: 表 系统服务栈模块介绍

   +------------+------------------------------------------------------------+
   | **模块名** | **功能**                                                   |
   +============+============================================================+
   | EcuM       | 对ECU节点的运行状态进行管理                                |
   +------------+------------------------------------------------------------+
   | BswM       | 对整个BSW软件模块进行管理                                  |
   +------------+------------------------------------------------------------+

.. table:: 表 协议栈集成的步骤

   +----------+--------------------------------------------------+------------------------------------------------------+
   | **步骤** |                     **操作**                     |                       **说明**                       |
   +----------+--------------------------------------------------+------------------------------------------------------+
   | 1        | ORIENTAIS Stuido配置工具工程搭建和协议栈模块加载 | 若配置工具已经搭建，则仅需进行协议栈模块的加载操作。 |
   +----------+--------------------------------------------------+------------------------------------------------------+
   | 2        | 模块配置及配置文件生成                           | NA                                                   |
   +----------+--------------------------------------------------+------------------------------------------------------+
   | 3        | 代码集成                                         | 现有工程、协议栈源代码和配置生成文件的集成。         |
   +----------+--------------------------------------------------+------------------------------------------------------+
   | 4        | 验证测试                                         | NA                                                   |
   +----------+--------------------------------------------------+------------------------------------------------------+

.. note::
   **协议栈集成之前，用户须确保已经有基础工程，且本协议栈相关的其他协议栈能正常工作。**

新建ORIENTAIS Studio配置工程及模块加载
--------------------------------------

BswM和EcuM的使用非空中楼阁，需要建立在其他模块已经集成的基础上，集成这两个模块只需要在工具添加相应模块进行配置集成即可。

#. 右击如图所示ECU，选择Add Moudle。

   |image1|

   图 新建工程添加新模块-1

#. 勾选EcuM和BswM模块，点击Finish。

   |image2|

   图 新建工程添加新模块-2

#. 出现下图所示模块则为添加成功。

   |image3|

   图 新建工程添加新模块-3

模块配置及生成代码
------------------

模块配置
~~~~~~~~

模块的具体配置，取决于具体的项目需求。

配置代码生成
~~~~~~~~~~~~

#. 在ORIENTAIS Studio主界面左方，选择对应的协议栈，单击右键弹出Validate All和Generate All菜单，也可以单个模块Validate和Generate。

   |image4|
   
   图 Generate All来生成Sys下的所有配置代码

   |image5|
   
   图 针对EcuM进行校验

#. 选择Validate All对本协议栈各配置选项进行校验，没有错误提示信息即校验通过。若有错误信息，请按照错误提示修改。

#. 选择Generate All，生成配置文件。右下角的Console窗口输出生成的配置文件信息。

   |image6|
   
   图 Console窗口的信息

#. 展开工程下config文件夹，即可查看生成的配置文件。

   |image7|
   
   图 config文件夹下的配置文件

功能集成
--------

代码集成
~~~~~~~~

协议栈代码包括两部分：普华提供的协议栈源码和ORIENTAIS Studio配置工具生成的配置代码。

用户须将协议栈源码和章节（配置代码生成）生成的源代码添加到集成开发工具的对应文件夹。协议栈集成的文件结构，见章节（源代码集成）。

.. note::
   **协议栈集成之前，用户须确保已经有基础工程，且本协议栈相关的其他协议栈能正常工作。**

集成注意事项
~~~~~~~~~~~~

对于集成过程中，协议栈特殊要求和用户经常出现的问题，归类总结形成 表 协议栈集成约束清单。用户需逐一排查表中的约束项，以避免集成问题出现。

.. table:: 表 协议栈集成约束清单

   +----------+----------+-------------------------------------------------------------------------------------------------------------+
   | **编号** | **类别** | **约束限制**                                                                                                |
   +==========+==========+=============================================================================================================+
   | **1**    | 头文件   | - 添加协议栈代码之后，用户需更新集成开发工具中的头文件路径。调用协议栈API的源文件，需要包含协议栈的头文件。 |
   +----------+----------+-------------------------------------------------------------------------------------------------------------+
   | **2**    | 初始化   | - 确保EcuM_Init()和EcuM_StartupTwo()两个函数被正确调用                                                      |
   +----------+----------+-------------------------------------------------------------------------------------------------------------+
   | **3**    | 周期函数 | - EcuM_MainFunction()和BswM_MainFunction()需要放到周期任务。                                                |
   +----------+----------+-------------------------------------------------------------------------------------------------------------+

集成示例
========

本章节向用户展示系统服务（EcuM&BswM）栈的集成过程。用户可以据此熟悉系统服务栈配置工具的配置过程，以及如何应用配置工具生成的配置文件。

.. note::
   **本示例不代表用户的实际配置情况，用户需要根据自己的实际需求，决定各个参数的配置，另外配置工具有很多其他特性，比如新建条目可以在文件夹上右击、某些情况选中文件夹可以在界面右侧上下移动调整条目顺序等，请自行探索，手册截图上只代表个人习惯方式。**

集成目标
--------

**根据用户策略需求配置BswM和EcuM模块，满足策略需求。本示例实现主要功能：**

#. **通信和网络管理报文的开和关。**

#. **上电主动请求网络。**

#. **被动唤醒本节点。**

模块的配置
----------

模块加载操作，请参考本文档章节（**模块配置及生成代码**）。

EcuM模块配置
~~~~~~~~~~~~~

#. 双击EcuM图标，打开EcuM配置界面。

   |image8|
   
   图 EcuM的配置界面

#. 配置EcuMGeneral界面选项，该界面通常只需要关注Main Function Period（切记要保证该模块Mainfunction放到OS对应周期Task），其他不需要配置。

   |image9|
   
   图 MainFunction的执行时间

#. 配置EcuMConfiguration界面参数，新建下图所示项。

   |image10|
   
   图 配置EcuMConfiguration

#. 配置EcuMCommonConfiguration。

   |image11|
   
   图 配置EcuMCommonConfiguration

#. 配置EcuMDefaultShutdownTarget。

   |image12|
   
   图 配置EcuMDefaultShutdownTarget

#. 配置EcuMDriverInitListOne，特别要注意模块初始化顺序，根据顺序依次进行添加配置。

   |image13|
   
   图 配置EcuMDriverInitListOne – 1

   |image14|
   
   图 配置EcuMDriverInitListOne - 2

   |image15|
   
   图 配置EcuMDriverInitListOne - 3

   |image16|
   
   图 配置EcuMDriverInitListOne - 4

#. 配置EcuMWakeupSource。

   |image17|
   
   图 配置EcuMWakeupSource - 1

   |image18|
   
   图 配置EcuMWakeupSource - 2

#. 配置EcuMSleepMode。

   |image19|
   
   图 配置EcuMSleepMode - 1

   |image20|
   
   图 配置EcuMSleepMode - 2

#. 配置EcuMFlexConfiguration。

   |image21|
   
   图 配置EcuMFlexConfiguration

   |image22|
   
   图 配置EcuC中的Partition

#. 配置EcuMFlexConfiguration下属文件夹下各子项，首先配置EcuMFlexUserConfig，然后配置其他。

   |image23|
   
   图 配置EcuMFlexConfiguration的子项

#. 配置EcuMFlexUserConfig。

   |image24|
   
   图 配置EcuMFlexUserConfig

#. 配置EcuMDriverInitListBswM。

   |image25|
   
   图 配置EcuMDriverInitListBswM - 1

   |image26|
   
   图 配置EcuMDriverInitListBswM - 2

#. 配置EcuMGoDownAllowedUser。

   |image27|
   
   图 配置EcuMGoDownAllowedUser

#. 配置EcuMFlexGeneral。

   |image28|
   
   图 配置EcuMFlexGeneral

#. EcuM模块配置完毕，进行校验生成配置代码，若校验出错，则根据提示信息Check对应配置项，修改之后重新校验生成。

BswM模块配置
~~~~~~~~~~~~

BswM配置和代码调试均比较复杂，此处说明该模块的配置原则，根据原则进行配置可以使条理更加清晰，配置效率提升，配置结果更容易达到预期目标。**该原则就是**：根据软件控制管理需求制定所需Rules（规则），根据Rule衍生出Ruel所需逻辑表达式、所用本模块和其他模块Port（函数接口）以及Rule下要执行的操作行为；根据逻辑表达式衍生出需要判断的条件（Condition），条件有一个或多个；每个Rule对应一个操作行为执行列表，每个执行列表可以挂接一个或者多个操作行为。

#. 双击BswM模块，打开BswM模块的配置界面。

   |image29|
   
   图 打开BswM的配置界面

#. 配置BswMGeneral。

   |image30|
   
   图 配置BswMGeneral

#. 在BswMGeneral下新建BswMUserIncludeFiles并配置。

   |image31|
   
   图 新建BswMUserIncludeFiles

   |image32|
   
   图 配置BswMUserIncludeFiles

#. 配置BswMConfig。

   |image33|
   
   图 配置BswMConfig

#. 配置BswMArbitration下BswMRule。

   |image34|
   
   图 新建Rule

   |image35|
   
   图 配置Rule

#. 配置BswMArbitration下BswMModeRequestPort。

   |image36|
   
   图 新建BswMModeRequestPort

   |image37|
   
   图 配置BswMModeRequestPort - 1

   |image38|
   
   图 配置BswMModeRequestPort - 2

   |image39|
   
   图 配置BswMModeRequestPort - 3

#. 配置上一步Mode通知源的初始值，即RequestPort的未被调用之前的默认通知值。

   |image40|
   
   图 配置Mode的初始值 - 1

   |image41|
   
   图 配置Mode的初始值 - 2

#. 配置BswMArbitration下BswMLogicalExpression。

   |image42|
   
   图 配置BswMLogicalExpression - 1

   |image43|
   
   图 配置BswMLogicalExpression - 2

#. 配置BswMArbitration下BswMModeCondition。

   |image44|
   
   图 新建BswMModeCondition

   |image45|
   
   图 新建BswMModeCondition

   |image46|
   
   图 配置BswMModeCondition - 1

   |image47|
   
   图 配置BswMModeCondition - 2

   |image48|
   
   图 配置BswMModeCondition - 3

   |image49|
   
   图 配置BswMModeCondition - 4

#. 配置EventRequestPort。

   |image50|
   
   图 配置EventRequestPort - 1

   |image51|
   
   图 配置EventRequestPort - 2

   |image52|
   
   图 配置EventRequestPort - 3

#. 配置BswMModeControl下的BswMAction。

   |image53|
   
   图 配置BswMAction - 1

   |image54|
   
   图 配置BswMAction - 2

   |image55|
   
   图 配置BswMAction - 3

#. 配置BswMModeControl下的BswMActionList（注：有的ActionList的Action需要注意执行顺序，需根据需要作出调整，执行顺序为界面呈现的顺序）。

   |image56|
   
   图 配置BswMActionList - 1

   |image57|
   
   图 配置BswMActionList - 2

   |image58|
   
   图 配置BswMActionList - 3

#. BswMRteModeRequestPort的配置。

   |image59|
   
   图 配置BswMRteModeRequestPort – 1

   |image60|
   
   图 配置BswMRteModeRequestPort - 2

#. 配置BswMSwitchPort的配置。

   |image61|
   
   图 配置BswMSwitchPort – 1

   |image62|
   
   图 配置BswMSwitchPort - 2

#. 配置完毕，进行校验生成配置代码，若校验出错，则根据提示信息Check对应配置项，修改之后重新校验生成。

源代码集成
----------

普华交付给用户的工程结构如下：

   |image63|
   
   图 BSW的工程结构图

- Config目录用来存放配置工具生成的配置文件，各模块或各栈建立对应文件夹存放对应模块配置代码。

- BSW目录存放模块相关的源代码，各模块建立对应文件夹存放对应模块源代码。

系统服务栈源代码集成：新建对应的源码文件夹和配置文件文件夹，将对应源码和配置代码放入，然后工程中添加相应头文件路径即可。

协议栈调度集成
--------------

系统服务栈调度集成步骤如下：

#. 协议栈调度集成，需要逐一排查并实现表 协议栈集成约束清单所罗列的问题，以避免集成出现差错。

#. 编译链接代码，将生成的elf文件烧写进芯片。

系统服务栈有关的代码，在下方的main.c文件中给出重点标注。

.. note::
   **本示例仅供参考，并不代表其他项目main.c文件与此完全相同，需要具体项目具体对待。**

**特别说明：** 在其他协议栈如网络管理栈或者通信栈正常运行前提下，添加该两个模块后需要在main.c文件main函数中在所有其他模块初始化之后（while（1）之前）调用EcuM_Init()和EcuM_StartupTwo()函数进行这两个模块的初始化，BswM模块的初始化函数在EcuM_StartupTwo()被调用，读者不需要特别关心。**这里特别说明两种情况：一种是MACL中一些模块和BSW中各模块初始化可以在EcuM模块工具进行配置，此情况下在调用EcuM_Init()函数中会间接调用各模块初始化函数将各模块初始化；另一种是各模块初始化都没有在EcuM模块工具进行配置，那这个时候需要将各模块初始化函数在main函数中按合理顺序进行调用将整个工程正常初始化。**

   |image64|
   
   图 集成调度范例

验证结果
--------

将工程编译通过后，使用劳德巴赫调试工具进行调试，程序成功运行后，使用VehicleSpy观测现象。

#. 指令数据：CanID为0x666的接收报文作为指令载体，Byte1的数据作为指令进行特定处理。

   |image65|
   
   图 指令数据

#. 测试结果——程序上电后根据PowerOn唤醒事件进行主动请求网络，网络管理报文先进行快发然后正常周期发送，通信打开数据周期发送，结果如下图所示

   |image66|
   
   图 测试结果 - 1

#. 测试结果——通过指令进行关发送通信，网络管理报文和通信报文停止发送，结果如下图所示

   |image67|
   
   图 测试结果 - 2

#. 测试结果——通过指令进行开发送通信，网络管理报文和通信报文恢复发送，结果如下图所示

   |image68|
   
   图 测试结果 - 3

#. 测试结果——通过指令请求释放网络，节点进入休眠，ECU到达低功耗运行态，网络管理报文和通信报文停止发送，结果如下图所示

   |image69|
   
   图 测试结果 - 4

#. 测试结果——发送唤醒报文进行唤醒，节点被动唤醒后进入正常运行态一段时间后再次进入休眠，网络管理报文和通信报文停止发送，结果如下图所示**（本示例采用CAN唤醒，不对ID进行过滤）**

   |image70|
   
   图 测试结果 - 5

.. |image1| image:: /_static/集成手册/集成手册_BswM&EcuM/image2.png
   :width: 5.76736in
   :height: 5.05069in

.. |image2| image:: /_static/集成手册/集成手册_BswM&EcuM/image3.png
   :width: 5.76736in
   :height: 5.26736in

.. |image3| image:: /_static/集成手册/集成手册_BswM&EcuM/image4.png
   :width: 5.60417in
   :height: 3.08448in

.. |image4| image:: /_static/集成手册/集成手册_BswM&EcuM/image5.png
   :width: 5.76736in
   :height: 2.9125in

.. |image5| image:: /_static/集成手册/集成手册_BswM&EcuM/image6.png
   :width: 5.76736in
   :height: 4.28403in

.. |image6| image:: /_static/集成手册/集成手册_BswM&EcuM/image7.png
   :width: 5.76736in
   :height: 4.87639in

.. |image7| image:: /_static/集成手册/集成手册_BswM&EcuM/image8.png
   :width: 5.76736in
   :height: 4.35833in

.. |image8| image:: /_static/集成手册/集成手册_BswM&EcuM/image9.png
   :width: 5.76736in
   :height: 2.96736in

.. |image9| image:: /_static/集成手册/集成手册_BswM&EcuM/image10.png
   :width: 5.76736in
   :height: 2.9125in

.. |image10| image:: /_static/集成手册/集成手册_BswM&EcuM/image11.png
   :width: 5.76736in
   :height: 2.9125in

.. |image11| image:: /_static/集成手册/集成手册_BswM&EcuM/image12.png
   :width: 9.38032in
   :height: 5.40834in

.. |image12| image:: /_static/集成手册/集成手册_BswM&EcuM/image13.png
   :width: 5.76736in
   :height: 2.9125in

.. |image13| image:: /_static/集成手册/集成手册_BswM&EcuM/image14.png
   :width: 5.76736in
   :height: 2.9125in

.. |image14| image:: /_static/集成手册/集成手册_BswM&EcuM/image15.png
   :width: 5.76736in
   :height: 2.9125in

.. |image15| image:: /_static/集成手册/集成手册_BswM&EcuM/image16.png
   :width: 5.76736in
   :height: 2.9125in

.. |image16| image:: /_static/集成手册/集成手册_BswM&EcuM/image17.png
   :width: 5.76736in
   :height: 2.9125in

.. |image17| image:: /_static/集成手册/集成手册_BswM&EcuM/image18.png
   :width: 5.76736in
   :height: 2.9125in

.. |image18| image:: /_static/集成手册/集成手册_BswM&EcuM/image19.png
   :width: 5.76736in
   :height: 2.9125in

.. |image19| image:: /_static/集成手册/集成手册_BswM&EcuM/image20.png
   :width: 5.76736in
   :height: 2.9125in

.. |image20| image:: /_static/集成手册/集成手册_BswM&EcuM/image21.png
   :width: 5.76736in
   :height: 2.9125in

.. |image21| image:: /_static/集成手册/集成手册_BswM&EcuM/image22.png
   :width: 5.76736in
   :height: 2.9125in

.. |image22| image:: /_static/集成手册/集成手册_BswM&EcuM/image23.png
   :width: 5.76736in
   :height: 2.9125in

.. |image23| image:: /_static/集成手册/集成手册_BswM&EcuM/image24.png
   :width: 5.76736in
   :height: 2.9125in

.. |image24| image:: /_static/集成手册/集成手册_BswM&EcuM/image25.png
   :width: 5.76736in
   :height: 2.9125in

.. |image25| image:: /_static/集成手册/集成手册_BswM&EcuM/image26.png
   :width: 5.76736in
   :height: 2.9125in

.. |image26| image:: /_static/集成手册/集成手册_BswM&EcuM/image27.png
   :width: 5.76736in
   :height: 2.9125in

.. |image27| image:: /_static/集成手册/集成手册_BswM&EcuM/image28.png
   :width: 5.76736in
   :height: 2.9125in

.. |image28| image:: /_static/集成手册/集成手册_BswM&EcuM/image29.png
   :width: 5.76736in
   :height: 2.9125in

.. |image29| image:: /_static/集成手册/集成手册_BswM&EcuM/image30.png
   :width: 5.76736in
   :height: 2.9125in

.. |image30| image:: /_static/集成手册/集成手册_BswM&EcuM/image31.png
   :width: 5.76736in
   :height: 2.9125in

.. |image31| image:: /_static/集成手册/集成手册_BswM&EcuM/image32.png
   :width: 5.76736in
   :height: 2.9125in

.. |image32| image:: /_static/集成手册/集成手册_BswM&EcuM/image33.png
   :width: 5.76736in
   :height: 2.9125in

.. |image33| image:: /_static/集成手册/集成手册_BswM&EcuM/image34.png
   :width: 5.76736in
   :height: 2.9125in

.. |image34| image:: /_static/集成手册/集成手册_BswM&EcuM/image35.png
   :width: 5.76736in
   :height: 2.9125in

.. |image35| image:: /_static/集成手册/集成手册_BswM&EcuM/image36.png
   :width: 5.76736in
   :height: 2.9125in

.. |image36| image:: /_static/集成手册/集成手册_BswM&EcuM/image37.png
   :width: 5.76736in
   :height: 2.9125in

.. |image37| image:: /_static/集成手册/集成手册_BswM&EcuM/image38.png
   :width: 5.76736in
   :height: 2.9125in

.. |image38| image:: /_static/集成手册/集成手册_BswM&EcuM/image39.png
   :width: 5.76736in
   :height: 2.9125in

.. |image39| image:: /_static/集成手册/集成手册_BswM&EcuM/image40.png
   :width: 5.76736in
   :height: 2.9125in

.. |image40| image:: /_static/集成手册/集成手册_BswM&EcuM/image41.png
   :width: 5.76736in
   :height: 2.9125in

.. |image41| image:: /_static/集成手册/集成手册_BswM&EcuM/image42.png
   :width: 5.76736in
   :height: 2.9125in

.. |image42| image:: /_static/集成手册/集成手册_BswM&EcuM/image43.png
   :width: 5.76736in
   :height: 2.9125in

.. |image43| image:: /_static/集成手册/集成手册_BswM&EcuM/image44.png
   :width: 5.76736in
   :height: 2.9125in

.. |image44| image:: /_static/集成手册/集成手册_BswM&EcuM/image45.png
   :width: 5.76736in
   :height: 2.9125in

.. |image45| image:: /_static/集成手册/集成手册_BswM&EcuM/image46.png
   :width: 5.76736in
   :height: 2.9125in

.. |image46| image:: /_static/集成手册/集成手册_BswM&EcuM/image47.png
   :width: 5.76736in
   :height: 2.9125in

.. |image47| image:: /_static/集成手册/集成手册_BswM&EcuM/image48.png
   :width: 5.76736in
   :height: 2.9125in

.. |image48| image:: /_static/集成手册/集成手册_BswM&EcuM/image49.png
   :width: 5.76736in
   :height: 2.9125in

.. |image49| image:: /_static/集成手册/集成手册_BswM&EcuM/image50.png
   :width: 5.76736in
   :height: 2.9125in

.. |image50| image:: /_static/集成手册/集成手册_BswM&EcuM/image51.png
   :width: 5.76736in
   :height: 2.9125in

.. |image51| image:: /_static/集成手册/集成手册_BswM&EcuM/image52.png
   :width: 5.76736in
   :height: 2.9125in

.. |image52| image:: /_static/集成手册/集成手册_BswM&EcuM/image53.png
   :width: 5.76736in
   :height: 2.9125in

.. |image53| image:: /_static/集成手册/集成手册_BswM&EcuM/image54.png
   :width: 5.76736in
   :height: 2.9125in

.. |image54| image:: /_static/集成手册/集成手册_BswM&EcuM/image55.png
   :width: 5.76736in
   :height: 2.9125in

.. |image55| image:: /_static/集成手册/集成手册_BswM&EcuM/image56.png
   :width: 5.76736in
   :height: 2.9125in

.. |image56| image:: /_static/集成手册/集成手册_BswM&EcuM/image57.png
   :width: 5.76736in
   :height: 2.9125in

.. |image57| image:: /_static/集成手册/集成手册_BswM&EcuM/image58.png
   :width: 5.76736in
   :height: 2.9125in

.. |image58| image:: /_static/集成手册/集成手册_BswM&EcuM/image59.png
   :width: 5.76736in
   :height: 2.9125in

.. |image59| image:: /_static/集成手册/集成手册_BswM&EcuM/image60.png
   :width: 5.76736in
   :height: 2.9125in

.. |image60| image:: /_static/集成手册/集成手册_BswM&EcuM/image61.png
   :width: 5.76736in
   :height: 2.9125in

.. |image61| image:: /_static/集成手册/集成手册_BswM&EcuM/image62.png
   :width: 5.76736in
   :height: 2.9125in

.. |image62| image:: /_static/集成手册/集成手册_BswM&EcuM/image63.png
   :width: 5.76736in
   :height: 2.9125in

.. |image63| image:: /_static/集成手册/集成手册_BswM&EcuM/image64.png
   :width: 5.76736in
   :height: 2.9125in

.. |image64| image:: /_static/集成手册/集成手册_BswM&EcuM/image65.png
   :width: 5.44375in
   :height: 11.69236in

.. |image65| image:: /_static/集成手册/集成手册_BswM&EcuM/image66.png
   :width: 5.76736in
   :height: 2.9125in

.. |image66| image:: /_static/集成手册/集成手册_BswM&EcuM/image67.png
   :width: 5.44375in
   :height: 9.69236in

.. |image67| image:: /_static/集成手册/集成手册_BswM&EcuM/image68.png
   :width: 5.76736in
   :height: 2.9125in

.. |image68| image:: /_static/集成手册/集成手册_BswM&EcuM/image69.png
   :width: 5.44375in
   :height: 9.69236in

.. |image69| image:: /_static/集成手册/集成手册_BswM&EcuM/image70.png
   :width: 5.63472in
   :height: 8.76111in

.. |image70| image:: /_static/集成手册/集成手册_BswM&EcuM/image71.png
   :width: 5.76736in
   :height: 7.79861in