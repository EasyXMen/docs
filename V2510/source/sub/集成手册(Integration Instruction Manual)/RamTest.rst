================
RamTest
================

目标
====

本文档用于指导客户进行RamTest集成，文档主要包括的内容为：RamTest集成指导、基于普通应用的集成示例讲解、项目集成特殊说明。

通过阅读本文档，用户可以了解代码集成过程，ORIENTAIS配置工具的配置过程，以及如何应用配置工具生成的配置文件。

由于各项目的需求不同，集成示例不会针对于特定的商业项目做详细讲解。

缩写词和术语
============

.. table:: 表 缩写词和术语

   +-----------------+------------------------------------------------------+
   | **缩写词/术语** | **描述**                                             |
   +-----------------+------------------------------------------------------+
   | OS              | Operating System 操作系统                            |
   +-----------------+------------------------------------------------------+
   | ECU             | Electronic Control Unit 电控单元                     |
   +-----------------+------------------------------------------------------+
   | MCU             | Micro Controller Unit 微控制单元                     |
   +-----------------+------------------------------------------------------+
   | Det             | Development Error Tracer 开发错误跟踪器              |
   +-----------------+------------------------------------------------------+
   | RAM             | Random Access Memory 随机访问存储器                  |
   +-----------------+------------------------------------------------------+
   | Dem             | Diagnostic Event Manager 诊断事件管理器              |
   +-----------------+------------------------------------------------------+

参考文档
========

[1] 参考手册_CRC.pdf

RamTest集成
===========

项目交付的内容为：RamTest源码和ORIENTAIS Studio配置工具。

RamTest各配置模块的功能介绍，参见表 RamTest各配置模块介绍。

使用RamTest源码和配置工具，进行RamTest的集成的步骤。

.. table:: 表 RamTest各配置模块介绍

   +------------+------------------------------------------------------------+
   | **模块名** | **功能**                                                   |
   +------------+------------------------------------------------------------+
   | RamTest    | RamTest主要对RAM单元的物理健康状况进行测试                 |
   +------------+------------------------------------------------------------+

.. table:: 表 RamTest集成的步骤

   +----------+-----------------------------------------+-------------------------------------------------------+
   | **步骤** | **操作**                                | **说明**                                              |
   +----------+-----------------------------------------+-------------------------------------------------------+
   | 1        | ORIENTAIS                               | 若配置工具已经搭建，则仅需进行RamTest模块的加载操作。 |
   |          | Stuido配置工具工程搭建和RamTest模块加载 |                                                       |
   +----------+-----------------------------------------+-------------------------------------------------------+
   | 2        | 模块配置及配置文件生成                  | NA                                                    |
   +----------+-----------------------------------------+-------------------------------------------------------+
   | 3        | 代码集成                                | 现有工程、RamTest源代码和配置生成文件的集成。         |
   +----------+-----------------------------------------+-------------------------------------------------------+
   | 4        | 验证测试                                | NA                                                    |
   +----------+-----------------------------------------+-------------------------------------------------------+

.. note::
   **RamTest集成之前，用户须确保已经有基础工程，且相关的其他协议栈能正常工作。**

新建ORIENTAIS Stuido配置工程及模块加载
--------------------------------------

#. 安装ORIENTAIS Studio软件后，双击软件图标打开软件。

   |image1|

   图 软件主界面

#. 菜单栏File🡪New🡪Project，新建工程。

   |image2|

   图 新建工程-1

#. 在弹出的新建窗口中选择Autosar下的 [BSW Project]，选择Next。

   |image3|

   图 新建工程-2

#. 在弹出的窗口中输入工程名，选择Finish。

   |image4|

   图 新建工程-3

#. 在弹出的窗口中选择Yes。

   |image5|

   图 完成新建工程

#. 选择[Bsw_Builder]，右键单击，选择New ECU Configuration。

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

#. 在ORIENTAIS Stuido主界面左方，选择对应的协议栈，单击右键弹出Validate
   All和Generate All菜单。

   |image10|

   图 代码生成

#. 选择Validate
   All对本协议栈各配置选项进行校验，没有错误提示信息即校验通过。若有错误信息，请按照错误提示修改。

#. 选择Generate
   All，生成配置文件。右下角的Console窗口输出生成的配置文件信息。

   |image11|

   图 代码生成提示界面

#. 将ORIENTAIS Studio切换到Resource模式，即可查看生成的配置文件。

   |image12|

   图 生成的配置文件

功能集成
--------

代码集成
~~~~~~~~

RamTest代码包括两部分：项目提供的RamTest源码和ORIENTAIS
Studio配置生成代码。

用户须将RamTest源码和章节（模块配置）生成的源代码添加到集成开发工具的对应文件夹。RamTest集成的文件结构，见章节（RamTstDemEventParameterRefs配置）。

.. note::
   **RamTest集成之前，用户须确保已经有基础工程，且相关的其他协议栈能正常工作。**

集成注意事项
~~~~~~~~~~~~

对于集成过程中，RamTest特殊要求和用户经常出现的问题，归类总结形成。用户需逐一排查表中的约束项，以避免集成问题出现。

.. table:: 表 RamTest集成约束清单

   +----------+----------+--------------------------------------------------------------+
   | **编号** | **类别** | **约束限制**                                                 |
   +----------+----------+--------------------------------------------------------------+
   | **1**    | 堆栈     | 用户需确保为任务堆栈和中断堆栈分配足够的堆栈空间。           |
   +----------+----------+--------------------------------------------------------------+
   | **2**    | 头文件   | - 添加协议栈代码之后，用户需更新集成开发工具中的头文件路径。 |
   |          |          |                                                              |
   |          |          | - 调用协议栈API的源文件，需要包含协议栈的头文件。            |
   +----------+----------+--------------------------------------------------------------+
   | **3**    | 初始化   | RamTest的初始化函数为RamTst_Init                             |
   +----------+----------+--------------------------------------------------------------+
   | **4**    | 周期函数 | 在后台测试时，RamTst_MainFunction需要被周期性任务函数调用。  |
   +----------+----------+--------------------------------------------------------------+
   | **5**    | 前台测试 | 如要进行前台测试，建议在MCU初始化之后进行或下电之前进行。    |
   +----------+----------+--------------------------------------------------------------+
   | **6**    | 软件依赖 | - OS：提供任务调度周期调用RamTst_MainFunction                |
   |          |          |                                                              |
   |          |          | ..                                                           |
   |          |          |                                                              |
   |          |          |    提供ISR环境，定期后台测试                                 |
   |          |          |                                                              |
   |          |          | - DEM：DEM错误处理函数，该模块不是强制的。                   |
   |          |          |                                                              |
   |          |          | - DET：处理开发过程中的错误，该模块不是强制的。              |
   +----------+----------+--------------------------------------------------------------+

集成示例
========

本章节向用户展示RamTest的集成过程。用户可以据此熟悉RamTest配置工具的配置过程，以及如何应用配置工具生成的配置文件。

本章节先完成基本RamTest配置，使得工程可以编译通过，并实现Ram测试，然后根据具体需求服务进行添加或修改。

.. note::
   **本示例不代表用户的实际配置情况，用户需要根据自己的实际需求，决定各个参数的配置。**

集成目标
--------

通过搭建基础工程，实现 RAM 测试功能。具体测试功能如下：

#. 前台测试  
   在前台实现对所配置的 RAM Block 用选定的算法进行全部测试或者部分测试。测试块参数配置如表。  

   .. table:: 表 前台测试测试块参数配置  

      +--------------+-----------------+--------------+------------------------+--------------+------------------+
      | **测试类型** | **起始地址**    | **结束地址** | **测试破坏后的填充值** | **测试策略** | **测试使用方法** |
      +--------------+-----------------+--------------+------------------------+--------------+------------------+
      | 前台测试     | 0x1fff0400      | 0x1fff09ff   | 0                      | 非破坏性     | 前台测试         |
      +--------------+-----------------+--------------+------------------------+--------------+------------------+

#. 后台测试  
   在后台实现对所配置的 RAM Block 分为原子操作，用选定的算法进行全部测试。参数配置如表：  

   .. table:: 表 后台测试测试块参数配置  

      +--------------+-----------------+--------------+------------------------+--------------+------------------+
      | **测试类型** | **起始地址**    | **结束地址** | **测试破坏后的填充值** | **测试策略** | **测试使用方法** |
      +--------------+-----------------+--------------+------------------------+--------------+------------------+
      | 后台测试     | 0x20000000      | 0x200043a7   | 0                      | 非破坏性     | 后台测试         |
      +--------------+-----------------+--------------+------------------------+--------------+------------------+

模块的配置
----------

新建配置工程及模块加载操作，请参考本文档章节（模块配置及生产代码）。生成代码过程请参考章节（模块配置及生产代码）。

RamTstCommon配置
~~~~~~~~~~~~~~~~

在此处进行一些函数是否使用的配置、安全暂存区域和RamTest模块本地变量区域配置。

#. 双击RamTstCommon模块，打开RamTstCommon模块配置界面。

   |image13|

   图 RamTstCommon配置界面

**RamTstAllowApi**\ ：预处理器开关，以禁用/启用API"RamTst_Allow"。

**RamTstChangeNumOfTestedCellsApi**\ ：预处理器开关，以禁用/启用API"
RamTst_ChangeNumberOfTestedCells"。

**RamTstGetTestAlgorithmApi**\ ：预处理器开关，以禁用/启用API"
RamTst_GetTestAlgorithm"。

**RamTstGetTestResultApi**\ ：预处理器开关，以禁用/启用API"
RamTst_GetTestResult"。

**RamTstGetTestResultPerBlockApi**\ ：预处理器开关，以禁用/启用API"
RamTst_GetTestResultPerBlock"。

**RamTstResumeApi**\ ：预处理器开关，以禁用/启用API" RamTst_Resume"。

**RamTstRunFullTestApi：**\ 预处理器开关，以禁用/启用API"
RamTst_RunFullTest"。

**RamTstRunPartialTestApi：**\ 预处理器开关，以禁用/启用API"
RamTst_RunPartialTest"。

**RamTstSelectAlgParamsApi：**\ 预处理器开关，以禁用/启用API"
RamTst_SelectAlgParams"。

**RamTstStopApi：**\ 预处理器开关，以禁用/启用API" RamTst_Stop"。

**RamTstSuspendApi：**\ 预处理器开关，以禁用/启用API" RamTst_Suspend"。

**RamTstVersionInfoApi：**\ 预处理器开关，以禁用/启用API"
RamTst_GetVersionInfo"。

**SelfCheckEnable：**\ 预处理器开关，以禁用/启用自检功能。

**TestCompleteNotificationEnable：**\ 预处理器开关，以禁用/启用测试完成通知。

**TestErrorNotificationEnable：**\ 预处理器开关，以禁用/启用测试失败通知。

**TimOutEnable：**\ 超时开关，以禁用/启用超时功能。

**TimeOutValueFgnd：**\ 前台测试超时时间。

**TimeOutValueBgnd：**\ 后台测试超时时间。

#. RamTst模块本地变量区域配置。分为起始地址和结束地址。

..

   **LocalVarAreaStartAddr**\ ：此配置填写起始地址。

   **LocalVarAreaEndAddr**\ ：此配置填写结束地址。如图5-2.

   |image14|

   图 RamTst模块本地变量区域配置

RamTstAlgorithms配置
~~~~~~~~~~~~~~~~~~~~

此处进行RamTest所使用的测试算法配置。

#. 双击RamTstAlgorithms模块，打开RamTstAlgorithms模块配置界面。

   |image15|

   图 RamTstAlgorithms配置

**RamTstAbrahamTestSelected:** 预处理器开关，以禁用/启用算法Abraham，。

**RamTstCheckerboardTestSelected:**
预处理器开关，以禁用/启用算法Checkerboard。

**RamTstGalpatTestSelected:** 预处理器开关，以禁用/启用算法Galpat。

**RamTstMarchTestSelected:** 预处理器开关，以禁用/启用算法March。

**RamTstTranspGalpatTestSelected:**
预处理器开关，以禁用/启用算法TranspGalpat。

**RamTstWalkPathTestSelected:** 预处理器开关，以禁用/启用算法WalkPath。

RamTstConfigParams配置
~~~~~~~~~~~~~~~~~~~~~~

此处进行RamTest配置参数的配置。

#. 双击RamTstConfigParams模块，打开RamTstConfigParams模块配置界面。

   |image16|

   图 RamTstConfigParams配置

#. 配置RamTstDefaultAlgParamsId，此处填1；

   **RamTstDefaultAlgParamsId：**\ 默认的测试参数ID配置。

   |image17|

   图 RamTstDefaultAlgParamsId配置

#. 配置RamTstMinNumberOfTestedCells；

   **RamTstMinNumberOfTestedCells：**\ 配置进行测试时最小测试单元字节数。**RamTstMinNumberOfTestedCells**\ ：进行测试时的最小测试单元字节数。
   
   |image18|
   
   图 RamTstMinNumberOfTestedCells配置

#. 配置RamTstTestCompletedNotification；

   **RamTstTestCompletedNotification：**\ 测试完成回调函数，在完成RAM测试时调用。**RamTstTestCompletedNotification**\ ：测试完成回调函数，在完成RAM测试后，没有检测到错误，会调用这个函数。
   
   |image19|
   
   图 RamTstTestCompletedNotification配置

#. 配置RamTstTestErrorNotification；

   **RamTstTestErrorNotification：**\ 测试到错误时的回调函数，在检测到RAM错误时，会调用这个函数。**RamTstTestErrorNotification**\ ：测试到错误时的回调函数，在检测到RAM错误时，会调用这个函数。
   
   |image20|
   
   图 RamTstTestErrorNotification配置

RamTstAlgParams配置
~~~~~~~~~~~~~~~~~~~

   此处进行测试参数的配置。RamTstAlgParams可以配置测试参数相关的参数。可以配置多个测试参数。测试参数的添加步骤为：鼠标选中RamTstAlgParams—单击右键—New—RamTstAlgParams

   |image21|

   图 RamTstAlgParams添加

#. 双击RamTstAlgParams模块，打开RamTstAlgParams模块配置界面。

   |image22|

   图 RamTstAlgParams配置界面

#. 配置RamTstAlgorithm。

   **RamTstAlgorithm：**\ 该测试参数所使用的测试算法。选择MARCH算法。

   |image23|

   图 RamTstAlgorithm配置界面

#. 配置RamTstExtNumberOfTestedCells。

   **RamTstExtNumberOfTestedCells：**\ 这是NUMBER_OF_TESTED_CELLS和MAX_NUMBER_OF_TESTED_CELLS可以达到的单元数的绝对最大值。

   |image24|

   图 RamTstExtNumberOfTestedCells配置界面

#. 配置RamTstMaxNumberOfTestedCells。

   **RamTstMaxNumberOfTestedCells：**\ 可以测试的单元格数的最大值。

   |image25|

   图 RamTstMaxNumberOfTestedCells配置界面

#. 配置RamTstNumberOfTestedCells。

   **RamTstNumberOfTestedCells：**\ 每次测试时所测试的字节数大小，只能为4的倍数。可以在程序中调用API修改。

   |image26|

   图 RamTstNumberOfTestedCells配置界面

测试块配置
~~~~~~~~~~

前台测试测试块配置
^^^^^^^^^^^^^^^^^^

#. 新加测试块添加步骤为：鼠标选中RamTstBlockParams—单击右键—New—RamTstBlockParams

   |image27|

   图 RamTstBlockParams添加

#. 双击RamTstBlockParams模块，打开RamTstBlockParams模块配置界面。

   |image28|

   图RamTstBlockParams配置界面

#. 配置RamTstEndAddress；

   **RamTstEndAddress：**\ 该RAM块的结束地址。此处填写目标块结束地址0x1ffff09ff。

   |image29|

   图 RamTstEndAddress配置界面

#. 配置RamTstStartAddress；

   **RamTstStartAddress：**\ 该RAM块的起始地址。此处填写目标块起始地址0x1ffff0400。

   |image30|

   图 RamTstStartAddress配置界面

#. 配置RamTstFillPattern；

   **RamTstFillPattern**\ ：进行破坏性的测试时，测试结束后，填入RAM的填充值。此处填写0。

   |image31|

   图 RamTstFillPattern配置界面

#. 配置RamTstTestPolicy；

   **RamTstTestPolicy：**\ 该RAM块的测试策略，破坏性还是非破坏性。此

   处配置为非破坏性（RAMTEST_NON_DESTRUCTIVE）。

   |image32|

   图 RamTstTestPolicy配置界面

#. 配置BlockTestUseMethod；

   **BlockTestUseMethod：**\ 该RAM块所使用的测试方法，前台测试还是后台测试等。此处配置为前台测试（BLOCK_TEST_USED_METHOD_FO REGROUN D）。

   |image33|

   图 BlockTestUseMethod配置界面

后台测试测试块配置
^^^^^^^^^^^^^^^^^^

#. 新加测试块添加步骤为：鼠标选中RamTstBlockParams—单击右键—New—RamTstBlockParams

   |image34|

   图 RamTstBlockParams添加

#. 双击RamTstBlockParams模块，打开RamTstBlockParams模块配置界面。

   |image35|

   图 RamTstBlockParams配置界面

#. 配置RamTstEndAddress；

   **RamTstEndAddress：**\ 该RAM块的结束地址。此处填写目标块结束地址0x200043a7。

   |image36|

   图 RamTstEndAddress配置界面

#. 配置RamTstStartAddress；

   **RamTstStartAddress：**\ 该RAM块的起始地址。此处填写目标块起始地址0x20000000。

   |image37|

   图 RamTstStartAddress配置界面

#. 配置RamTstFillPattern；

   **RamTstFillPattern：**\ 进行破坏性的测试时，测试结束后，填入RAM的填充值。此处填写0。

   |image38|

   图 RamTstFillPattern配置界面

#. 配置RamTstTestPolicy；

   **RamTstTestPolicy：**\ 该RAM块的测试策略，破坏性还是非破坏性。此处配置为非破坏性（RAMTEST_NON_DESTRUCTIVE）。

   |image39|

   图 RamTstTestPolicy配置界面

#. 配置BlockTestUseMethod；

   **BlockTestUseMethod：**\ 该RAM块所使用的测试方法，前台测试还是后台测试等。此处配置为后台测试（BLOCK_TEST_USED_METHOD_BA CKGROUND）。

   |image40|

   图 BlockTestUseMethod配置界面

RamTstDemEventParameterRefs配置
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. 添加RamTstDemEventParameterRefs，鼠标选中RamTstDemEventParameterRefs—单击右键—New—RamTstDemEventParameterRefs。

   |image41|

   图 RamTstDemEventParameterRefs添加

#. 双击RamTstAlgParams模块，打开RamTstAlgParams模块配置界面。

   |image42|

   图 RamTstDemEventParameterRefs配置界面

#. 配置RAMTST_MAIN_RAM_FAILURE，将RAMTST_MAIN_RAM_FAILURE勾选上，并从下拉框中选择对应的Dem配置项。

   |image43|

   图 RAMTST_MAIN_RAM_FAILURE配置界面

#. 配置RAMTST_PART_RAM_FAILURE，将RAMTST_PART_RAM_FAILURE勾选上，并从下拉框中选择对应的Dem配置项。

   |image44|

   图 RAMTST_PART_RAM_FAILURE配置界面

#. 配置RAMTST_RUNFL_RAM_FAILURE，将RAMTST_RUNFL_RAM_FAILURE勾选上，并从下拉框中选择对应的Dem配置项。

   |image45|

   图 RAMTST_RUNFL_RAM_FAILURE配置界面

源代码集成
----------

项目交付给用户的工程结构如下：

   |image46|

   图 工程结构图

- Config目录，这个目录用来存放配置工具生成的配置文件，RamTest有关的配置文件放在BSW_Config文件夹中。

- BSW目录，存放模块相关的源代码。可以看到BSW目录下各个文件夹下是各个模块的源代码。

RamTest源代码集成步骤如下：

#. 将章节（模块的配置）中ORIENTAIS Studio生成的配置文件复制到BSW_Config文件夹中。

#. 将项目提供的协议栈源代码文件复制到BSW/Memory/RamTst文件夹中。

在集成时，需要在链接文件里面将RAM进行分区规划。划分为存放RamTst模块本地变量区域、被测RAM区域。将RAMTEST自身数据放在RamTst模块本地变量区域，和被测区域分开。并将栈区（OS启动之前自身的堆栈）与其他区域分开。如下图所示：

   |image47|

   图 Ram区域划分图

用户须确保各分配的RAM区域不会被其他变量使用。

链接文件修改如下所示：

   |image48|

   图 Ram区域划分图

   |image49|

   图 RamTst使用的变量放到RAM区域

同时，需要在MemMap.h文件里面启用内存管理，如下所示：

   |image50|

   图 MemMap使用

RamTest调度集成
---------------

RamTest调度集成步骤如下：

#. RamTest调度集成，需要逐一排查并实现所罗列的问题，以避免集成出现差错。

#. 编译链接代码，将生成的elf文件烧写进芯片。

初始化和前台测试代码如下。

.. note::
   **本示例中，RamTst协议栈初始化的代码和启动通信的代码置于EcuM_Callout_Stubs.c文件，并不代表其他项目同样适用于将其置于EcuM_Callout_Stubs.c文件中。**


.. code-block:: c
   :linenos:
   :emphasize-lines: 2-3

   #include "Fls.h"
   // RamTest协议栈相关模块头文件
   #include "RamTst.h"

   // 定义EcuM_AL_DriverInitOne任务
   TASK(EcuM_AL_DriverInitOne)
   {
       RamTst_Init(&RamTstConfigRoot);  // 初始化RamTest模块，传入配置参数
       RamTst_RunFullTest();            // 执行完整的RAM测试

       // 获取测试结果
       RamTst_TestResultType RamTstResult = RamTst_GetTestResult();
   }

验证结果
--------

验证前台测试
~~~~~~~~~~~~

将工程编译通过后，使用调试工具进行调试，当执行RamTst_RunFullTest()后，再调用RamTst_GetTestResult()获取结果，编译下载仿真时，在获取结果后打断点，可以看见返回测试结果为OK。

验证后台测试
~~~~~~~~~~~~

将工程编译通过后，使用调试工具进行调试，周期调用RamTst_MainFunction()，编译下载仿真时，当后台测试完成时，会调用RamTst_TestCompletedNotification()回调函数，在回调函数里面再调用RamTst_GetTestResult()获取结果，可以看见返回测试结果为OK。

.. |image1| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_RamTest/image2.png
   :width: 5.76736in
   :height: 3.2125in


.. |image2| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_RamTest/image3.png
   :width: 5.76736in
   :height: 3.2125in


.. |image3| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_RamTest/image4.png
   :width: 5.76736in
   :height: 4.5125in


.. |image4| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_RamTest/image5.png
   :width: 5.76736in
   :height: 3.8125in


.. |image5| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_RamTest/image6.png
   :width: 5.76736in
   :height: 3.2125in


.. |image6| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_RamTest/image7.png
   :width: 5.76736in
   :height: 3.2125in


.. |image7| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_RamTest/image8.png
   :width: 5.76736in
   :height: 6.0125in


.. |image8| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_RamTest/image9.png
   :width: 5.76736in
   :height: 4.5125in


.. |image9| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_RamTest/image10.png
   :width: 5.76736in
   :height: 3.2125in


.. |image10| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_RamTest/image11.png
   :width: 5.76736in
   :height: 6.0125in


.. |image11| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_RamTest/image12.png
   :width: 5.76736in
   :height: 3.2125in


.. |image12| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_RamTest/image13.png
   :width: 5.76736in
   :height: 3.2125in


.. |image13| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_RamTest/image14.png
   :width: 5.76736in
   :height: 3.2125in


.. |image14| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_RamTest/image15.png
   :width: 5.76736in
   :height: 3.2125in


.. |image15| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_RamTest/image16.png
   :width: 5.76736in
   :height: 3.2125in


.. |image16| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_RamTest/image17.png
   :width: 5.76736in
   :height: 3.2125in


.. |image17| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_RamTest/image18.png
   :width: 5.76736in
   :height: 3.2125in


.. |image18| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_RamTest/image19.png
   :width: 5.76736in
   :height: 3.2125in


.. |image19| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_RamTest/image20.png
   :width: 5.76736in
   :height: 4.3125in


.. |image20| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_RamTest/image21.png
   :width: 5.76736in
   :height: 3.2125in


.. |image21| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_RamTest/image22.png
   :width: 4.76736in
   :height: 3.9125in


.. |image22| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_RamTest/image23.png
   :width: 5.76736in
   :height: 3.2125in


.. |image23| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_RamTest/image24.png
   :width: 5.26736in
   :height: 4.2125in


.. |image24| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_RamTest/image25.png
   :width: 5.76736in
   :height: 4.2125in


.. |image25| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_RamTest/image26.png
   :width: 5.76736in
   :height: 4.2125in


.. |image26| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_RamTest/image27.png
   :width: 5.76736in
   :height: 3.9125in


.. |image27| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_RamTest/image28.png
   :width: 5.76736in
   :height: 3.9125in


.. |image28| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_RamTest/image29.png
   :width: 5.76736in
   :height: 3.2125in


.. |image29| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_RamTest/image30.png
   :width: 5.76736in
   :height: 3.2125in


.. |image30| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_RamTest/image31.png
   :width: 5.76736in
   :height: 3.2125in


.. |image31| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_RamTest/image32.png
   :width: 5.76736in
   :height: 3.2125in


.. |image32| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_RamTest/image33.png
   :width: 5.76736in
   :height: 3.2125in


.. |image33| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_RamTest/image34.png
   :width: 5.76736in
   :height: 3.9125in


.. |image34| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_RamTest/image35.png
   :width: 5.76736in
   :height: 4.5125in


.. |image35| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_RamTest/image36.png
   :width: 5.76736in
   :height: 3.3125in


.. |image36| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_RamTest/image37.png
   :width: 5.76736in
   :height: 3.9125in


.. |image37| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_RamTest/image38.png
   :width: 5.76736in
   :height: 3.9125in


.. |image38| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_RamTest/image39.png
   :width: 5.26736in
   :height: 3.2125in


.. |image39| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_RamTest/image40.png
   :width: 5.76736in
   :height: 3.2125in


.. |image40| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_RamTest/image41.png
   :width: 5.76736in
   :height: 3.2125in


.. |image41| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_RamTest/image42.png
   :width: 5.76736in
   :height: 3.2125in


.. |image42| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_RamTest/image43.png
   :width: 5.76736in
   :height: 3.2125in


.. |image43| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_RamTest/image44.png
   :width: 5.76736in
   :height: 3.2125in


.. |image44| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_RamTest/image45.png
   :width: 5.76736in
   :height: 3.2125in


.. |image45| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_RamTest/image46.png
   :width: 5.76736in
   :height: 3.2125in


.. |image46| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_RamTest/image47.png
   :width: 5.76736in
   :height: 3.2125in


.. |image47| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_RamTest/image48.png
   :width: 4.86736in
   :height: 6.2125in


.. |image48| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_RamTest/image49.png
   :width: 5.06736in
   :height: 6.2125in


.. |image49| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_RamTest/image50.png
   :width: 5.36736in
   :height: 3.4125in


.. |image50| image:: /_static/集成手册(Integration_Instruction_Manual)/集成手册_RamTest/image51.png
   :width: 5.76736in
   :height: 6.2125in