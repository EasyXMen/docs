============
WDG
============

目标
====

本文档用于指导客户进行WDG集成，文档主要包括的内容为：WDG集成指导、基于普通应用的集成示例讲解、项目集成特殊说明。

通过阅读本文档，用户可以了解代码集成过程，ORIENTAIS配置工具的配置过程，以及如何应用配置工具生成的配置文件。由于各项目的需求不同，集成示例不会针对于特定的商业项目做详细讲解。

缩写词和术语
============

.. table:: 表 缩写词和术语

   +---------------+------------------------------------------------------+
   | 缩写词/术语   | 描述                                                 |
   +===============+======================================================+
   | OS            | Operating System 操作系统                            |
   +---------------+------------------------------------------------------+
   | ECU           | Electronic Control Unit 电控单元                     |
   +---------------+------------------------------------------------------+
   | WDG           | Watchdog 看门狗                                      |
   +---------------+------------------------------------------------------+
   | WdgM          | Watchdog Manager 看门狗管理                          |
   +---------------+------------------------------------------------------+
   | WdgIf         | Watchdog Interface 看门狗接口                        |
   +---------------+------------------------------------------------------+
   | CP            | CheckPoint 监控点                                    |
   +---------------+------------------------------------------------------+
   | SE            | Supervised Entity 监控实体                           |
   +---------------+------------------------------------------------------+

参考文档
========

[1] 参考手册_ORIENTAIS_Studio_WDG.pdf

[2] 参考手册_ORIENTAIS_WDG.pdf

WDG集成
=======

WDG各配置模块的功能介绍，参见表 WDG各配置模块介绍。

使用WDG源码和配置工具，进行WDG的集成的步骤，参见表 WDG集成的步骤。

.. table:: 表 WDG各配置模块介绍

   +---------+------------------------------------------------------------+
   | 模块名  | 功能                                                       |
   +=========+============================================================+
   | Wdg     | wdg驱动配置。                                              |
   +---------+------------------------------------------------------------+
   | WdgIf   | 1.允许WdgM访问多个底层Wdg抽象模块。                        |
   |         |                                                            |
   |         | 2.该模块的API都映射到下层Wdg抽象模块的API。                |
   +---------+------------------------------------------------------------+
   | WdgM    | 1.Watchdog的管理操作，实现各种状态机制管理。               |
   |         |                                                            |
   |         | 2.为用户App提供Watchdog的Api。                             |
   |         |                                                            |
   |         | 3.下发指令给下层WdgIf，并获取其反馈结果。                  |
   +---------+------------------------------------------------------------+

.. table:: 表 WDG集成的步骤

   +------+-------------------------------------+---------------------------------------------------+
   | 步骤 | 操作                                | 说明                                              |
   +======+=====================================+===================================================+
   | 1    | ORIENTAIS                           | 若配置工具已经搭建，则仅需进行WDG模块的加载操作。 |
   |      | Stuido配置工具工程搭建和WDG模块加载 |                                                   |
   +------+-------------------------------------+---------------------------------------------------+
   | 2    | 模块配置及配置文件生成              | NA                                                |
   +------+-------------------------------------+---------------------------------------------------+
   | 3    | 代码集成                            | 现有工程、WDG源代码和配置生成文件的集成。         |
   +------+-------------------------------------+---------------------------------------------------+
   | 4    | 验证测试                            | NA                                                |
   +------+-------------------------------------+---------------------------------------------------+

.. note::
   WDG集成之前，用户须确保已经有基础工程，且WDG相关的其他协议栈能正常工作。

新建ORIENTAIS Stuido配置工程及模块加载
--------------------------------------

#. 安装ORIENTAIS Studio软件后，双击软件图标打开软件。
   |image1|

   图 软件主界面

#. 菜单栏File🡪New🡪Project，新建工程。

   |image2|

   图 新建工程

#. 在弹出的新建窗口中选择Autosar下的 [BSW Project]，选择Next。

   |image3|

   图 新建工程

#. 在弹出的窗口中输入工程名，选择Finish。

   |image4|

   图 新建工程

#. 在弹出的窗口中选择Yes。

   |image5|

   图 完成新建工程

#. 菜单栏File选择[Bsw_Builder]，右键单击，选择New ECU Configuration。

   |image6|

   图 新建ECU

#. 在弹出的窗口中输入ECU名，然后选择Next。

   |image7|

   图 选择芯片平台

#. 在弹出的窗口中勾选需添加的模块，点击Finish。

   |image8|

   图 完成ECU配置

#. 新建工程如下所示，步骤⑧中添加的模块已经被加入到工程中。

   |image9|

   图 工程列表界面

模块配置及生产代码
------------------

模块配置
~~~~~~~~

模块的具体配置，取决于具体的项目需求。该协议栈各模块配置项的详细介绍，参见表
协议栈各模块配置参考文档。

.. table:: 表 协议栈各模块配置参考文档

   +----------+---------------------------------------+-------------------+
   | 模块     | 参考文档及其章节                      | 说明              |
   +==========+=======================================+===================+
   | WdgIf    | Autosar R19-11_参考手册_WdgIf.pdf     |                   |
   +----------+---------------------------------------+-------------------+
   | WdgM     | Autosar R19-11_参考手册_WdgM.pdf      |                   |
   +----------+---------------------------------------+-------------------+

配置代码生成
~~~~~~~~~~~~

#. 在ORIENTAIS Stuido主界面左方，选择对应的协议栈，单击右键弹出Validate
   All和Generate All菜单。

   |image10|

   图 代码生成

#. 选择Validate All对本协议栈各配置选项进行校验，没有错误提示信息即校验通过。若有错误信息，请按照错误提示修改。

#. 选择Generate All，生成配置文件。右下角的Console窗口输出生成的配置文件信息。

   |image11|

   图 代码生成提示界面

#. 将ORIENTAIS Studio切换到Resource模式，即可查看生成的配置文件。

   |image12|

   图 生成的配置文件

功能集成
--------

代码集成
~~~~~~~~

WDG代码包括两部分：项目提供的WDG源码和ORIENTAIS Studio配置生成代码。

用户须将WDG源码和章节（配置代码生成）生成的源代码添加到集成开发工具的对应文件夹。WDG集成的文件结构，见章节（集成示例）。

.. note::
   WDG集成之前，用户须确保已经有基础工程，且WDG相关的其他协议栈能正常工作。

集成注意事项
~~~~~~~~~~~~

对于集成过程中，WDG特殊要求和用户经常出现的问题，归类总结形成表
WDG集成约束清单。用户需逐一排查表中的约束项，以避免集成问题出现。

.. table:: 表 WDG集成约束清单

   +------+------------------+---------------------------------------------------------------------------------------------------------------------------------------+
   | 编号 | 类别             | 约束限制                                                                                                                              |
   +======+==================+=======================================================================================================================================+
   | 1    | 堆栈             | 用户需确保为任务堆栈和中断堆栈分配足够的堆栈空间。                                                                                    |
   +------+------------------+---------------------------------------------------------------------------------------------------------------------------------------+
   | 2    | 头文件           | - 添加协议栈代码之后，用户需更新集成开发工具中的头文件路径。                                                                          |
   |      |                  |                                                                                                                                       |
   |      |                  | - 调用协议栈API的源文件，需要包含协议栈的头文件。                                                                                     |
   +------+------------------+---------------------------------------------------------------------------------------------------------------------------------------+
   | 3    | 初始化           | WDG的初始化顺序为：WdgDriver_Init,WdgM_Init                                                                                           |
   +------+------------------+---------------------------------------------------------------------------------------------------------------------------------------+
   | 4    | 周期函数         | Gtm_IsrTomModule ,WdgM_MainFunction需要被周期性任务函数调用。                                                                         |
   +------+------------------+---------------------------------------------------------------------------------------------------------------------------------------+
   | 5    | Alive监控        | 1. 上电启动OS之后，由于第一个OS周期Task的不确定性，需要在初次执行WdgM_MainFunction之后，才开始执行Alive相关的WdgM_CheckPointReached。 |
   |      |                  |                                                                                                                                       |
   |      |                  | 2. WdgM_SetMode需要在WdgM_MainFunction之后执行，避免两个Mode都使用同一Alive监控的阈值差异造成的错误。                                 |
   +------+------------------+---------------------------------------------------------------------------------------------------------------------------------------+
   | 6    | FirstExpiredSEID | WDGM_FIRST_EXPIRED_SEID和WDGM_FIRST_EXPIRED_INVERSE_SEID各占用RAM空间的16Bytes，应在链接脚本中进行保护，避免其他变量占用该RAM区域。   |
   +------+------------------+---------------------------------------------------------------------------------------------------------------------------------------+
   | 7    | 依赖             | - 硬件依赖                                                                                                                            |
   |      |                  |                                                                                                                                       |
   |      |                  | ..                                                                                                                                    |
   |      |                  |                                                                                                                                       |
   |      |                  |    定时器外设：WDG通过比较到达CP的时间戳监控时间间隔功能。时间戳从定时器外设获取                                                      |
   |      |                  |                                                                                                                                       |
   |      |                  |    看门狗外设：可以是芯片上的看门狗，也可以是外部看门狗，或者两者都有                                                                 |
   |      |                  |                                                                                                                                       |
   |      |                  | - 软件依赖                                                                                                                            |
   |      |                  |                                                                                                                                       |
   |      |                  | ..                                                                                                                                    |
   |      |                  |                                                                                                                                       |
   |      |                  |    OS：提供任务调度周期调用WdgM_MainFunction                                                                                          |
   |      |                  |                                                                                                                                       |
   |      |                  |    提供ISR环境，定期看门狗触发                                                                                                        |
   |      |                  |                                                                                                                                       |
   |      |                  |    定时器：提供时间戳获取函数用于两个CP比较时间跨度                                                                                   |
   |      |                  |                                                                                                                                       |
   |      |                  |    看门狗驱动程序：用于设置模式的函数，设置触发条件的函数，喂狗函数。                                                                 |
   |      |                  |                                                                                                                                       |
   |      |                  |    DEM：DEM错误处理函数，该模块不是强制的。                                                                                           |
   |      |                  |                                                                                                                                       |
   |      |                  |    DET：处理开发过程中的错误，该模块不是强制的。                                                                                      |
   |      |                  |                                                                                                                                       |
   |      |                  |    BswM:调用该模块以重置OS-Application，该模块不是强制的。                                                                            |
   +------+------------------+---------------------------------------------------------------------------------------------------------------------------------------+

集成示例
========

本章节向用户展示WDG的集成过程。用户可以据此熟悉WDG配置工具的配置过程，以及如何应用配置工具生成的配置文件。示例是基于Wdg驱动正常工作之上。

本章节先完成基本WDG配置，使得工程可以编译通过，并实现基础WDG监控，然后根据具体需求服务进行添加或修改。

.. note::
   本示例不代表用户的实际配置情况，用户需要根据自己的实际需求，决定各个参数的配置。

集成目标
--------

通过搭建基础工程，实现简单的Wdg监控功能。具体监控功能如下：

#. Alive supervision -用于监控定期软件的时间。参数配置如表：

   .. table:: 表 Alive监控参数配置

      +----------+-----------------------------------------------+--------------+------------+----------+--------------+--------------+--------------+------------+------------+
      | 监控类型 | 描述                                          | 监控实体个数 | 监控点个数 | 参考周期 | 监控失败门限 | 监控失效门限 | 期望执行次数 | 次数上偏差 | 次数下偏差 |
      +==========+===============================================+==============+============+==========+==============+==============+==============+============+============+
      | Alive    | 监控一次mainfunction周期alive监控点执行的次数 | 1            | 1          | 1        | 0            | 0            | 1            | 0          | 0          |
      | 监控     |                                               |              |            |          |              |              |              |            |            |
      +----------+-----------------------------------------------+--------------+------------+----------+--------------+--------------+--------------+------------+------------+

#. Deadline supervision–用于非周期软件的时间监控。参数配置如表

   .. table:: 表 Deadline监控参数配置

      +----------+--------------------+--------------+------------+----------+--------------+--------------+-------------------+-------------------+
      | 监控类型 | 描述               | 监控实体个数 | 监控点个数 | 参考周期 | 监控失败门限 | 监控失效门限 | 最大时间间隔（S） | 最小时间间隔（S） |
      +==========+====================+==============+============+==========+==============+==============+===================+===================+
      | Deadline | 监控两CP的时间间隔 | 1            | 2          | 1        | 0            | 0            | 0.05              | 0                 |
      |          |                    |              |            |          |              |              |                   |                   |
      | 监控     |                    |              |            |          |              |              |                   |                   |
      +----------+--------------------+--------------+------------+----------+--------------+--------------+-------------------+-------------------+

#. Logical supervision-用于监控执行顺序的正确性。参数配置如表：

   .. table:: 表 Logical监控参数配置

      +-------------+----------------+--------------+------------+----------+--------------+--------------+
      | 监控类型    | 描述           | 监控实体个数 | 监控点个数 | 参考周期 | 监控失败门限 | 监控失效门限 |
      +=============+================+==============+============+==========+==============+==============+
      | Logical     | 监控CP执行顺序 | 1            | 2          | 1        | 0            | 0            |
      |             |                |              |            |          |              |              |
      | 监控        |                |              |            |          |              |              |
      +-------------+----------------+--------------+------------+----------+--------------+--------------+

模块的配置
----------

新建配置工程及模块加载操作，请参考本文档章节（模块配置及生产代码）。生成代码过程请参考章节（模块配置及生产代码）。

导入MCAL的WDG Driver 信息
~~~~~~~~~~~~~~~~~~~~~~~~~

#. 选择如下图所示的 Import Module From Other Arxml选项

   |image13|

   图 导入mcal配置选项

#. 选择Mcal生成的ARXML文件，Supplier选择EB Arxml文件，勾选WDG模块。

   |image14|

   图 导入mcal配置界面

WdgIf配置
~~~~~~~~~

#. 双击WdgIf模块，打开WdgIf模块配置界面。

   |image15|

   图 WdgIf General配置界面

   Dev_Error_Detect: 是否开启对开发过程中错误的检查。

   Version_Info_Api: 是否使能版本检查API函数

#. 添加WdgIfDevice配置，分为WdgIfInternalDevice与WdgIfExternalDevice，可只存在一个或同时存在。添加步骤为：鼠标选中WdgIfInternalDevice—单击右键—New
   WdgIfInternalDevice。详见图。

   |image16|

   图 新添加WdgIfInternalDevice

#. 添加WdgIfDevice后配置界面如图.

   |image17|

   图 WdgIfInternalDevice配置界面

   TriggerConditionFunction：此配置填写Wdg
   Driver中API函数名称。通过这个API可以实现为设定trigger
   counter时设置超时数值(milliseconds)。

   SetModeFunction：此配置填写Wdg
   Driver中API函数名称。通过这个API可以实现在WDGIF_OFF_MODE（0）,
   WDGIF_FAST_MODE（1）以及WDGIF_SLOW_MODE(2).间切换。

   Device Ref：选择对应的底层Watchdog。

#. WdgIf模块到此配置结束。可以在模块上右键，然后选择校验，查看是否配置有错误。校验后提示窗口没有错误信息，即校验通过。

WdgM模块配置
~~~~~~~~~~~~

#. 双击WdgM模块，打开WdgM模块配置界面。

   |image18|

   图 WdgM System Setting配置

   WdgMDemStoppedSupervisionReport：是否需要将错误信息报告给Dem模块。

   WdgMDevErrorDetect:
   打开或关闭错误追踪（Det）功能。若开启，一旦检测到配置出错，则代码停留在故障出错位置。量产用代码，需关闭该配置。

   WdgMImmediateReset: 使能/失能在Global status Stopped状态时立即复位。

   WdgMOffModeEnabled: 是否允许Watchdog Driver配置为Off Mode模式。true:
   允许 “OffMode”, false: 不允许“OffMode”。

   WdgMVersionInfoApi：预处理器开关，用于启用/禁用API
   WdgM_GetVersionInfo的存在。用于删除不需要的代码段。

   Address For
   FIRST_EXPIRED_SEID：FIRST_EXPIRED_SEID存储地址。存储在此区域的数据必须不会因热启动而擦除或复位。

   Address For
   FIRST_EXPIRED_INVERSE_SEID：FIRST_EXPIRED_INVERSE_SEID存储地址。存储在此区域的数据必须不会因热启动而擦除或复位。

#. WdgMSupervisedEntitys添加如图。

   |image19|

   图 添加WdgMSupervisedEntity或WdgMWatchdog

#. WdgMCheckpoint添加如图。

   |image20|

   图 添加新WdgMCheckpoint或WdgMInternalTransition

#. WdgMSupervisedEntitys配置界面如图。

   |image21|

   图 WdgMSupervisedEntity配置界面

   Supervised Entity Id：此参数应该包含一个唯一的SEID。

   Internal Transition Id：外部逻辑监控ID。

   OS Application
   Ref：该SE属于哪个Application。用于SE故障时的部分代码重启。

   Internal Checkpoint Initial Ref：该SE的Internal Logical
   supervision的初始Checkpoint。

   WdgMInternalCheckpoint FinalRef：该SE的Internal Logical
   supervision的最终Checkpoint

#. WdgMInternalTransition配置界面如图。

   |image22|

   图 WdgMInternalTransition配置界面

   Internal Transition Dest
   Ref：InternalLogicalSupervision中的某执行段的目的CP。

   Internal Transition Source
   Ref：InternalLogicalSupervision中的某执行段的起始CP

#. WdgMWatchdog配置界面如图。

   |image23|

   图 WdgMWatchdog配置界面

   Watchdog Name：该参数包含Watchdog硬件实例的命名。

   Watchdog Device Ref：该参数应包含看门狗实例的符号名称。

#. WdgMConfigSet配置界面如图。

   |image24|

   图 WdgMConfigSet中Initial Mode配置界面

   Initial Mode：看门狗管理器初始化后所处的模式。

#. WdgMDemEventParamenterRef添加。

   WdgMDemEventParamenterRef添加步骤为：鼠标选中WdgMConfigSet—单击右键—New—WdgMDemEventParamenterRefs。用来关联Dem模块的DTC详见。

   |image25|

   图 添加新WdgMDemEventParamenterRefs或WdgMMode

#. WdgMDemEventParamenterRefs配置界面如图。

   |image26|

   图 WdgMDemEventParamenterRefs配置界面

#. 添加WdgMMode配置项步骤。鼠标选中WdgMMode—单击右键—New—WdgMAliveSupervisoin。详见图。

   |image27|

   图 新加WdgMAliveSupervision

   或WdgMDeadlineSupervisionWdgM

   或ExternalLogicalSupervision

   或 WdgMLocalStatusParams或 WdgMTrigger

   .. note::
      在增加或删除WdgMAliveSupervision后，若其它WdgMAliveSupervision
      ID会发生变化，务必单击打开会发生变化的WdgMAliveSupervision，以保证其ID能正确更新。

#. WdgMAliveSupervision配置界面如图5-16。

   |image28|

   图 WdgMAliveSupervision配置界面

   Expected Alive Indications：期望该CP在SupervisionReferenceCycle的Main
   Function中，出现的次数

   Max Margin：Expected Alive Indications与实际情况的最大允许偏差。

   Min Margin：Expected Alive Indications与实际情况的最小允许偏差。

   Supervision Reference
   Cycle：该AliveSupervision执行多少个MainFuncation周期

   Alive Supervision Checkpoint Ref：该AliveSupervision监控的检查点

#. WdgMDeadlineSupervisoin添加及配置界面介绍。添加步骤为：鼠标选中WdgMMode—单击右键—New—WdgMDeadlineSupervisoin。默认情况，无该配置项。详见图。

   |image29|

   图 WdgMDeadlineSupervision配置界面

   .. note::
      在增加或删除WdgMDeadlineSupervisoin后，若其它WdgMDeadlineSupervisoin
      ID会发生变化，务必单击打开会发生变化的WdgMDeadlineSupervisoin，以保证其ID能正确更新。

   Deadline Max：Deadline监控两个Checkpoint直接的最大时间间隔单位：s。

   Deadline Min：Deadline监控两个Checkpoint直接的最小时间间隔单位：s。

   Deadline Start Ref：Deadline监控的起始Checkpoint。

   Deadline Stop Ref：Deadline监控的结束Checkpoint。

#. WdgMExternalTransition添加步骤及配置项介绍。

   WdgMExternalLogicalSupervisoin添加步骤为：鼠标选中WdgMMode—单击右键—New—WdgMExternalLogicalSupervisoin。

   右键单击WdgMExternalLogicalSupervisoin_xx —New—ExternalTransition。。

   鼠标选中WdgMExternalLogicalSupervisoin_xx —鼠标移到右方窗口的InitialRef
   或 StopRef—单击右键—Add Reference—下拉选择Checkpoint。

   配置描述如图。

   |image30|
   |image31|

   图 添加WdgMExternalTranstion

   External Transition Source
   Ref：ExternalLogicalSupervision中的某执行段的目的CP。

   Deadline Stop Ref：ExternalLogicalSupervision中的某执行段的结束CP

#. WdgMLocalStatusParams添加步骤及介绍

   鼠标选中WdgMMode—单击右键—New—WdgMLocalStatusParams。配置界面如图5-19。

   |image32|

   图 WdgMLocalStatusParams配置界面

   Failed Alive Supervision Ref Cycle Tol：Alive
   Supervision出现故障时，能接受的故障次数。达到故障次数时，Local
   Status的状态从Failed切换到Expired。

   Local Status Supervision Entity Ref：选择当前Mode，被使用的Supervision
   Entity。

#. WdgMTrigger添加步骤及配置项介绍

   鼠标选中WdgMMode—单击右键—New—WdgMTrigger。配置项介绍如图5-20。

   |image33|

   图 WdgMTrigger配置界面

   Trigger Condition
   Value：该参数应包含传递给该看门狗WdgIf_SetTriggerCondition的值。单位: ms

   Watchdog Mode：当前Trigger，对应Trigger Watchdog
   Ref底层的Watchdog的工作模式。

   rigger Watchdog Ref：当前Trigger对应的底层Watchdog。

#. WdgM模块到此配置结束。可以在模块上右键，然后选择校验，查看是否配置有错误。校验后提示窗口没有错误信息，即校验通过。

配置Alive Supervision
~~~~~~~~~~~~~~~~~~~~~

#. 添加Wdg驱动头文件。内部WDG不需要添加。

   |image34|

   图 添加WDG驱动文件界面

#. 新建WdgIfInternalDevice。

   |image35|

   图 新建WdgIfInternalDevice

#. 添加驱动接口函数。

   |image36|

   图 添加驱动接口函数

#. 配置Address for FIRST_EXPIRED_SEID和Address for
   FIRST_EXPIRED_INVERSE_SEID。

   |image37|

   图 配置SEID

#. WdgMGenerals->New,新建一个WdgMSupervisedEntity和一个WdgMWatchd og。

   |image38|

   图 配置watchdog

#. 配置Supervised Entity Id工具默认值为1。

   |image39|

   图 配置Supervised Entity ID

#. 配置WdgMWatchdog_1。

   |image40|

   图 配置WdgMWatchdog_0

#. WdgMConfigSet->New->WdgMMode。

   |image41|

   图 配置WdgMMode

#. Expired Supervision Cycle Tol配置为0。

   |image42|

   图 配置Expired Supervision Cycle Tol

#. WdgMMode_0->New，新建WdgMAliveSupervision和WdgLocalStatusParams。

   |image43|

   图 新建WdgMAliveSupervision和WdgLocalStatusParams

#. 选择本地状态监控实体参考监控实体0.监控失败门限配置为0。

   |image44|

   图 配置监控失败门限

#. 配置Alive监控相关参数。

   |image45|

   图 配置Alive监控参数

#. 设置触发值为100，看门狗模式为FAST模式。

   |image46|

   图 配置看门狗模式

#. 选择初始化模式为WdgMMode_1。

   |image47|

   图 配置初始看门狗模式

   代码修改如下：

   这是Alive supervision的一个例子。函数WdgM_MainFunction()在50ms任务中执行，函数WdgM_CheckpointReached在50ms任务中执行，因此每执行WdgM_MainFunction()时，WdgM_CheckpointReached中的期望指示是1次。

.. code-block:: c
   :linenos:

   /*OsTask_50ms:Core0(CPU0),Type = BASIC,Priority = 3*/
   TASK(OsTask_50ms)
   {
       WdgM_CheckpointReached(1,0);
       
       /*WdgM_MainFunction() call cycle to check the result of the WdgM module*/
       WdgM_MainFunction();
       
       if (E_OK != TerminateTask())
       {
           while (1)
           {
               /* dead loop */
           }
       }
   }

配置Deadline Supervision
~~~~~~~~~~~~~~~~~~~~~~~~

#. 添加Wdg驱动头文件。

   |image34|

   图 添加Wdg驱动头文件

#. 新建WdgIfInternalDevice。

   |image35|

   图 新建WdgIfInternalDevice

#. 添加驱动接口函数。

   |image36|

   图 添加驱动接口函数

#. 配置Address for FIRST_EXPIRED_SEID和Address for FIRST_EXPIRED_INVERSE_SEID。

   |image37|
   
   图 配置SEID

#. WdgMGenerals->New,新建一个WdgMSupervisedEntity和一个WdgMWatchdog。

   |image38|

   图 新建WdgMSupervisedEntity和WdgMWatchdog

#. 配置Supervised Entity Id 工具默认生成为1。

   |image48|
   
   图 配置Supervised Entity Id

#. WdgSupervisedEntity_0->New,添加WdgMCheckPoint。

   |image49|
   
   图 添加WdgMCheckPoint

#. 配置WdgMWatchdog_0。

   |image50|

   图 配置WdgMWatchdog

#. WdgMConfigSet->New->WdgMMode。

   |image51|

   图 新建WdgMMode

#. Expired Supervision Cycle Tol配置为0。

   |image52|

   图 配置Expired Supervision Cycle Tol

#. WdgMMode_1->New，新建WdgMDeadLineSupervision和WdgLocalStatusParams。

   |image53|

   图 新建WdgMDeadLineSupervision和WdgLocalStatusParams

#. 选择本地状态监控实体参考监控实体0.监控失败门限配置为0。

   |image54|

   图 配置监控失败门限

#. 配置Deadline监控相关参数。

   |image55|

   图 配置Deadline监控相关参数

#. 设置触发值为100，看门狗模式为FAST模式。

   |image56|
   
   图 配置看门狗模式

#. 选择初始化模式为WdgMMode_1。

   |image47|

   图 配置看门狗初始模式

   .. note::
      #. 在同一个DeadLine supervision的配置中，start ref和stop ref配置为同一个checkpoint。
      
      #. 在Deadline的配置中，如果配置checkpoint形成链路的情况下，同一个checkpoint不能用做多个Deadline的start ref。

   代码修改如下：

   这是Deadline supervision的一个例子。WdgMDeadlineMax = 0.05，WdgMDeadlineMin = 0，表示两个CP之间的时间不超过50ms。

   .. code-block:: c
      :linenos:

      /* OsTask_50ms: Core0(CPU0), Type = BASIC, Priority = 3 */
      TASK(OsTask_50ms)
      {
          /* please insert your code here ... */
          static unsigned int counter = 0; 

          if (0 == counter)
          {
              counter = 1;
              WdgM_CheckpointReached(1, 0);  // 第一个检查点（CP0）
          }
          else
          {
              counter = 0;
              WdgM_CheckpointReached(1, 1);  // 第二个检查点（CP1）
              WdgM_MainFunction();           // 执行WDG周期监控
          }

          if (E_OK != TerminateTask())
          {
              while (1) { /* dead loop */ }
          }
      }

配置Logical Supervision
~~~~~~~~~~~~~~~~~~~~~~~

#. 添加Wdg驱动头文件。

   |image34|

   图 添加Wdg驱动头文件

#. 新建WdgIfInternalDevice。

   |image35|

   图 新建WdgIfInternalDevice

#. 添加驱动接口函数。

   |image36|

   图 添加驱动接口函数

#. 配置Address for FIRST_EXPIRED_SEID和Address for FIRST_EXPIRED_INVERSE_SEID。

   |image37|

   图 配置SEID

#. WdgMGenerals->New,新建一个WdgMSupervisedEntity和一个WdgMWatchdog。

   |image38|

   图 新建WdgMSupervisedEntity和WdgMWatchdog

#. WdgSupervisedEntity_0->New,添加WdgMCheckPoint和WdgMInternalTransmition。

   |image49|

   图 添加WdgMCheckPoint和WdgMInternalTransmition

#. 配置Supervised Entity Id 为大于0的值，该例程配置为1。设置初始化监控点为SE0CP0,结束监控点为SE0CP1。

   |image58|

   图 配置监控点

#. 设置WdgInternalTransmision起始为SE0CP0，终止为SE0CP1。

   |image59|

   图 配置WdgInternalTransmision

#. 配置WdgMWatchdog_0。

   |image60|

   图 配置WdgMWatchdog

#. WdgMConfigSet->New->WdgMMode。

   |image61|

   图 新建WdgMMode

#. Expired Supervision Cycle Tol配置为0。

   |image62|

   图 配置Expired Supervision Cycle Tol

#. WdgMMode_0->New，新建WdgLocalStatusParams。

   |image63|

   图 新建WdgLocalStatusParams

#. 选择本地状态监控实体参考监控实体0.监控失败门限配置为0。

   |image64|

   图 配置监控失败门限

#. 设置触发值为100，看门狗模式为FAST模式。

   |image65|

   图 配置看门狗模式

#. 选择初始化模式为WdgMMode_1。

   |image47|

   图 配置看门狗初始模式

   代码修改如下：

   这是Internal logical supervision的一个例子。这两个CP属于同一监控实体。CP必须以正确的顺序执行。


   .. code-block:: c
      :linenos:

      /* OsTask_50ms: Core0(CPU0), Type = BASIC, Priority = 3 */
      TASK(OsTask_50ms)
      {
          /* please insert your code here ... */
          static unsigned int counter = 0; 

          if (0 == counter)
          {
              counter = 1;
              WdgM_CheckpointReached(3, 0);  // 第一个检查点（CP0），需先执行
          }

          if (1 == counter)
          {
              WdgM_CheckpointReached(3, 1);  // 第二个检查点（CP1），需后执行
              WdgM_MainFunction();           // 执行WDG周期监控，检查执行顺序
              counter = 0;
          }

          if (E_OK != TerminateTask())
          {
              while (1) { /* dead loop */ }
          }
      }

WDG调度集成
-----------

WDG调度集成步骤如下：

#. WDG调度集成，需要逐一排查并实现表
   WDG集成约束清单所罗列的问题，以避免集成出现差错。

#. 编译链接代码，将生成的elf文件烧写进芯片。

.. note::
   本示例中，WDG初始化的代码置于OsTaskInit，并不代表其他项目同样适用于将其置于OsTaskInit中。

初始化代码如下：

.. code-block:: c
   :linenos:

   TASK(OsTask_Init)
   {
       Dem_PreInit();
       Dem_Init(&DemPbCfg);
       Gtm_Init(&Gtm_ConfigRoot[0]);
       Smu_Init(&Smu_ConfigRoot[0]);
       Wdg_17_Scu_Init(&Wdg_ConfigRoot[0]);
       
       WdgM_Init(&WdgMConfigRoot[0]);
   }

监控代码根据不同的解控实例，监控点放置位置，WdgM_MainFunction放置位置，请参考章节（WdgM模块配置、配置Alive Supervision、配置Deadline Supervision）

验证结果
--------

验证Alive Supervision
~~~~~~~~~~~~~~~~~~~~~

将工程编译通过后，使用PE调试工具进行调试，当屏蔽WdgM_CheckpointReached(1,0)后，编译下载仿真时，在编译环境中观察到发生复位。

当不屏蔽WdgM_CheckpointReached(1,0)后，观测点配置如章节（WdgM模块配置）,编译下载仿真时，在编译环境中观察未发生复位。

验证Deadline Supervision
~~~~~~~~~~~~~~~~~~~~~~~~

将工程编译通过后，使用PE调试工具进行调试，当WdgM_CheckpointReached(1,0)和WdgM_CheckpointReached(1,1)时间间隔不为50ms时，编译下载仿真时，在编译环境中观察到发生复位。

当两观测点时间间隔为50ms,
即观测点配置如章节（配置Alive Supervision）,编译下载仿真时，在编译环境中观察未发生复位。

验证Logical Supervision
~~~~~~~~~~~~~~~~~~~~~~~

将工程编译通过后，使用PE调试工具进行调试，当执行两次WdgM_CheckpointReached(1,0)，不执行WdgM_CheckpointReached(1,1)，然后执行WdgM_MainFunction检查时，编译下载仿真时，在编译环境中观察到发生复位。

当观测点配置如章节（配置Deadline Supervision）,编译下载仿真时，在编译环境中观察未发生复位。

.. |image1| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_WDG/image2.png
   :width: 5.76736in
   :height: 3.10347in
.. |image2| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_WDG/image3.png
   :width: 5.76736in
   :height: 3.10694in
.. |image3| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_WDG/image4.png
   :width: 3.79528in
   :height: 3.62205in
.. |image4| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_WDG/image5.png
   :width: 3.8072in
   :height: 2.92887in
.. |image5| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_WDG/image6.png
   :width: 3.82677in
   :height: 2.51969in
.. |image6| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_WDG/image7.png
   :width: 4.76736in
   :height: 3.10694in
.. |image7| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_WDG/image8.png
   :width: 4.96934in
   :height: 4.30117in
.. |image8| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_WDG/image9.png
   :width: 5.76736in
   :height: 6.10347in
.. |image9| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_WDG/image10.png
   :width: 4.76736in
   :height: 2.80694in
.. |image10| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_WDG/image11.png
   :width: 5.76736in
   :height: 3.10347in
.. |image11| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_WDG/image12.png
   :width: 5.76736in
   :height: 3.10347in
.. |image12| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_WDG/image13.png
   :width: 5.76736in
   :height: 2.60694in
.. |image13| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_WDG/image14.png
   :width: 5.76736in
   :height: 4.60694in
.. |image14| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_WDG/image15.png
   :width: 5.76736in
   :height: 3.60694in
.. |image15| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_WDG/image16.png
   :width: 5.26736in
   :height: 3.61111in
.. |image16| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_WDG/image17.png
   :width: 5.36736in
   :height: 3.60694in
.. |image17| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_WDG/image18.png
   :width: 5.76736in
   :height: 2.60694in
.. |image18| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_WDG/image19.png
   :width: 5.76736in
   :height: 2.60694in
.. |image19| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_WDG/image20.png
   :width: 5.76736in
   :height: 3.60694in
.. |image20| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_WDG/image21.png
   :width: 5.76736in
   :height: 3.60694in
.. |image21| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_WDG/image22.png
   :width: 5.76736in
   :height: 2.60694in
.. |image22| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_WDG/image23.png
   :width: 5.76736in
   :height: 2.60694in
.. |image23| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_WDG/image24.png
   :width: 5.76736in
   :height: 2.60694in
.. |image24| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_WDG/image25.png
   :width: 5.76736in
   :height: 2.60694in
.. |image25| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_WDG/image26.png
   :width: 5.76736in
   :height: 2.60694in
.. |image26| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_WDG/image27.png
   :width: 5.76736in
   :height: 2.60694in
.. |image27| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_WDG/image28.png
   :width: 5.76736in
   :height: 2.60694in
.. |image28| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_WDG/image29.png
   :width: 5.76736in
   :height: 2.60694in
.. |image29| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_WDG/image30.png
   :width: 5.76736in
   :height: 2.60694in
.. |image30| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_WDG/image31.png
   :width: 5.76736in
   :height: 2.60694in
.. |image31| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_WDG/image32.png
   :width: 5.76736in
   :height: 2.60694in
.. |image32| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_WDG/image33.png
   :width: 5.76736in
   :height: 2.60694in
.. |image33| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_WDG/image34.png
   :width: 5.76736in
   :height: 2.60694in
.. |image34| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_WDG/image35.png
   :width: 5.36736in
   :height: 4.60694in
.. |image35| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_WDG/image36.png
   :width: 5.36736in
   :height: 4.10694in
.. |image36| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_WDG/image37.png
   :width: 5.76736in
   :height: 2.60694in
.. |image37| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_WDG/image38.png
   :width: 7.36736in
   :height: 3.20694in
.. |image38| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_WDG/image39.png
   :width: 5.76736in
   :height: 4.10694in
.. |image39| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_WDG/image40.png
   :width: 5.76736in
   :height: 2.60694in
.. |image40| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_WDG/image41.png
   :width: 5.76736in
   :height: 2.60694in
.. |image41| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_WDG/image42.png
   :width: 5.76736in
   :height: 4.60694in
.. |image42| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_WDG/image43.png
   :width: 5.76736in
   :height: 4.60694in
.. |image43| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_WDG/image44.png
   :width: 5.76736in
   :height: 3.90694in
.. |image44| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_WDG/image45.png
   :width: 5.76736in
   :height: 2.60694in
.. |image45| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_WDG/image46.png
   :width: 5.76736in
   :height: 4.20694in
.. |image46| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_WDG/image47.png
   :width: 5.76736in
   :height: 2.60694in
.. |image47| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_WDG/image48.png
   :width: 5.76736in
   :height: 4.40694in
.. |image48| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_WDG/image49.png
   :width: 5.76736in
   :height: 2.60694in
.. |image49| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_WDG/image50.png
   :width: 5.76736in
   :height: 4.60694in
.. |image50| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_WDG/image51.png
   :width: 5.76736in
   :height: 2.60694in
.. |image51| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_WDG/image52.png
   :width: 5.76736in
   :height: 4.47917in
.. |image52| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_WDG/image53.png
   :width: 5.76736in
   :height: 2.47917in
.. |image53| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_WDG/image54.png
   :width: 5.76736in
   :height: 4.47917in
.. |image54| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_WDG/image55.png
   :width: 5.76736in
   :height: 2.47917in
.. |image55| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_WDG/image56.png
   :width: 5.76736in
   :height: 2.47917in
.. |image56| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_WDG/image57.png
   :width: 5.76736in
   :height: 4.17917in
.. |image57| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_WDG/image58.png
   :width: 5.76736in
   :height: 2.47917in
.. |image58| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_WDG/image59.png
   :width: 5.76736in
   :height: 4.47917in
.. |image59| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_WDG/image60.png
   :width: 5.76736in
   :height: 2.47917in
.. |image60| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_WDG/image61.png
   :width: 5.76736in
   :height: 2.47917in
.. |image61| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_WDG/image62.png
   :width: 5.76736in
   :height: 4.47917in
.. |image62| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_WDG/image63.png
   :width: 5.76736in
   :height: 4.47917in
.. |image63| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_WDG/image64.png
   :width: 5.76736in
   :height: 4.47917in
.. |image64| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_WDG/image65.png
   :width: 5.76736in
   :height: 4.47917in
.. |image65| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_WDG/image66.png
   :width: 5.76736in
   :height: 4.17917in
.. |image66| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_WDG/image67.png
   :width: 5.76736in
   :height: 3.47917in
