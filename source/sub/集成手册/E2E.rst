===================
E2E_集成手册
===================





目标
====

本文档旨在展示对E2EXf、E2EL、CRC三个跟通信安全相关模块的集成过程，让用户了解如何去更好的运用他们。

通过阅读本文档，用户可以了解ORIENTAIS配置工具的配置过程，以及如何应用配置工具生成的配置文件。

为了让用户更清晰的了解工具的使用，所用的配置均逐一手动完成。用户在了解了配置的基本过程后，可以根据通信安全用户手册中对各配置参数的描述和用户的具体应用场景进行举一反三的配置。

缩写词和术语
============

.. table:: 表格 2-1 缩写词和术语

   +---------------+------------------------------------------------------+
   | **\           | **描述**                                             |
   | 缩写词/术语** |                                                      |
   +---------------+------------------------------------------------------+
   | E2EXf         | End to End Transformer 端到端转换器                  |
   +---------------+------------------------------------------------------+
   | E2EL          | End to End library 端到端通讯保护库                  |
   +---------------+------------------------------------------------------+
   | CRC           | End to End library 循环冗余校验                      |
   +---------------+------------------------------------------------------+

参考文档
========

[1]参考手册_E2EL.pdf

[2]参考手册_E2EXf.pdf

协议栈集成
==========

项目交付的内容为：E2E协议栈源码和ORIENTAIS
Configurator配置工具。协议栈细分为协议栈的各模块及其对应的配置工具模块。

E2E协议栈各配置模块的功能介绍，参见表 4‑1 E2E协议栈各配置模块介绍。

使用协议栈源码和配置工具，进行协议栈的集成的步骤，参见表4‑2
E2E协议栈集成的步骤。

.. table:: 表 4-1 E2E协议栈各配置模块介绍

   +----------+-----------------------------------------------------------+
   | **\      | **功能**                                                  |
   | 模块名** |                                                           |
   +----------+-----------------------------------------------------------+
   | CRC      | 循环冗余校验模块                                          |
   +----------+-----------------------------------------------------------+
   | Xfrm     | Xfrm模块根据E2E 保护的数据的<transformerId>以及配置各类型 |
   |          | profile实现E2E保护                                        |
   +----------+-----------------------------------------------------------+

.. table:: 表 4-2 E2E协议栈集成的步骤

   +-----+--------------------------+------------------------------------+
   |**步\| **操作**                 | **说明**                           |
   |骤** |                          |                                    |
   |     |                          |                                    |
   |     |                          |                                    |
   +-----+--------------------------+------------------------------------+
   | 1   | ORIENTAIS                | 若配置工具已经搭建                 |
   |     | Configurator配置工具     | ，则仅需进行协议栈模块的加载操作。 |
   |     | 工程搭建和协议栈模块加载 |                                    |
   +-----+--------------------------+------------------------------------+
   | 2   | 模块配置及配置文件生成   | NA                                 |
   +-----+--------------------------+------------------------------------+
   | 3   | 代码集成                 | 现有工程、                         |
   |     |                          | 协议栈源代码和配置生成文件的集成。 |
   +-----+--------------------------+------------------------------------+
   | 4   | 验证测试                 | NA                                 |
   +-----+--------------------------+------------------------------------+

**注意：协议栈集成之前，用户须确保已经有基础工程，且本协议栈相关的其他协议栈能正常工作。**

新建ORIENTAIS Configurator配置工程及模块加载
-------------------------------------------

#. 安装软件后，双击软件图标打开软件

.. figure:: ../../_static/集成手册/E2E/image1.png
   :width: 5.76042in
   :height: 3.04444in

   图 4-1 新建工程-1

2. 菜单栏File🡪New🡪Project，新建工程

.. figure:: ../../_static/集成手册/E2E/image2.png
   :width: 5.76042in
   :height: 3.19375in

   图 4‑2 新建工程-2

3. 在弹出的新建窗口中选择Autosar下的 [BSW Project]，选择Next

|image1|

图4-3 新建工程-3

4. 在弹出的窗口中输入工程名，选择Finish。

|image2|

图4-4 新建工程-4

在弹出的窗口中选择Yes。

|image3|

图4-5 新建工程-5

5. 在工程的[Bsw_Builder]项目上右键，选择New ECU Configuration

|image4|

图4-6 新建工程-6

6. 在弹出的窗口中输入一个ECU名，选择芯片平台，然后选择Next。

|image5|

图4-7 新建工程-7

7. 在弹出的窗口中勾选需要添加的模块，点击Finish。

|image6|

图4-8 新建工程-8

8. 新建完成依次展开小三角，可以看到步骤⑦中添加的模块已经被加入到工程
   中，说明工程新建完成。

|image7|

图4-9 新建工程-9


模块配置及代码生成
------------------

模块配置
~~~~~~~~

模块的具体配置，取决于具体的项目需求。该协议栈各模块配置项的详细介绍。

.. table:: 表 4‑3 协议栈各模块配置参考文档

   +--------+----------------------------------------+-------------------+
   | **\    | **参考文档**                           | **说明**          |
   | 模块** |                                        |                   |
   +--------+----------------------------------------+-------------------+
   | Can    | MCAL对应的Can配置手册                  |                   |
   +--------+----------------------------------------+-------------------+
   | CanIf  | CAN通信.pdf                            |                   |
   +--------+----------------------------------------+-------------------+
   | EcuC   | CAN通信.pdf                            |                   |
   +--------+----------------------------------------+-------------------+
   | Xfrm   | 参考手册_E2EL.pdf                      |                   |
   |        |                                        |                   |
   |        | 参考手册_E2EXf.pdf                     |                   |
   +--------+----------------------------------------+-------------------+

配置代码生成
~~~~~~~~~~~~

#. 在ORIENTAIS
   Configurator主界面左方，选择对应的协议栈，单击右键弹出Validate
   All和Generate All菜单。

|image8|

图4-10 配置代码的生成-1

2. 选择Validate
   All对本协议栈各配置选项进行校验，没有错误提示信息即校验通过。若有错误信息，请按照错误提示修改。

3. 选择Generate
   All，生成配置文件。右下角的Console窗口输出生成的配置文件信息。

|image9|

图4-11 配置代码的生成-2

4. 在工程config文件夹，可查看生成的配置文件。

|image10|

图4-12 配置代码的生成-3

功能集成
--------

代码集成
~~~~~~~~

协议栈代码包括两部分：项目提供的协议栈源码和ORIENTAIS
Configurator配置生成代码。

用户须将协议栈源码和章节4.2.2生成的源代码添加到集成开发工具的对应文件夹。

**注意：协议栈集成之前，用户须确保已经有基础工程，且本协议栈相关的其他协议栈能正常工作。**

集成注意事项
~~~~~~~~~~~~

对于集成过程中，协议栈特殊要求和用户经常出现的问题，归类总结形成 表
4‑4协议栈集成约束清单。用户需逐一排查表中的约束项，以避免集成问题出现。

表 4‑4 E2E协议栈集成约束清单

+-----+---------+-----------------------------------------------------+
|**编\| **类别**| **约束限制**                                        |
|号** |         |                                                     |
|     |         |                                                     |
|     |         |                                                     |
+-----+---------+-----------------------------------------------------+
| 1   | 头文件  | 添加协议\                                           |
|     |         | 栈代码之后，用户需更新集成开发工具中的头文件路径。  |
|     |         |                                                     |
|     |         | 调用协议栈API的源文件，需要包含协议栈的头文件。     |
+-----+---------+-----------------------------------------------------+
| 2   | 初始化  | E2EXf_Init函数进行初始化。                          |
+-----+---------+-----------------------------------------------------+
| 3   | 接\     | 根据需求对被保护数据直接调用E2Exf中的接口。         |
|     | 口调用  |                                                     |
+-----+---------+-----------------------------------------------------+

集成示例
========

本章节向用户展示E2E协议栈的集成过程。用户可以据此熟悉E2E协议栈配置工具的配置过程，以及如何应用配置工具生成的配置文件。

集成目标
--------

集成完成后模拟发送端和接收端，可以实现正确在发送端对数据进行保护以及在接收端对数据进行校验。

模块的配置
----------

新建配置工程及模块加载操作，请参考本文档4.2章节。

CRC模块配置
~~~~~~~~~~~

本小节介绍CRC模块配置，该模块配置主要用来开关各种CRC算法以及各种算法的计算模式。

#. 双击图中Crc项，打开配置界面，如下图：

|image11|

图5-1 CRC配置界面

2. 勾选所有CRC算法，相应模式选择CRC_RUNTIME或者CRC_TABLE（剩余一种暂不支持）。

|image12|

图5-2 CRC配置界面

3. 点击保存按钮，右击Crc项点击Validate选项进行校验，校验无错误即为配置

成功。

|image13|

图5-3 CRC配置校验及生成

Xfrm模块中E2Exfrm配置
~~~~~~~~~~~~~~~~~~~~

#. 双击Xfrm项，打开Xfrm模块配置界面。新建一个E2EXfrmGeneral容器。

|image14|

图5-4 Xfrm模块配置界面

|image15|

图5-5 E2EXfrmGeneral容器配置

2. 点击界面上TransformationSet项，展开小三角，右击TransformationSet_0新建

TransformationTechnology。（注：为了对应E2EL中的2个profile，示例中新

建2个，如下图）

|image16|

图5-6 TransformationSet界面

|image17|

图5-7 新建TransformationTechnology容器

3. 展开小三角，点击TransformationTechnology_0,出现下图界面，该界面参数值

保持默认值。

|image18|

图5-8 TransformationTechnology容器配置

4. 点击EndToEndTransformationDescription，配置该项，界面如图，图中标注出

需要修改名字，该界面首先配置profileName（对应不同的profile，进而对应

不同的CRC算法），然后根据该项和用户需求配置其他参数，profileBehavior

保持默认。

|image19|

图5-9 EndToEndTransformationDescription配置

5. 展开小三角，点击BufferProperty，配置该项，其他保持默认。（\ **特别提醒：**

**该处HeaderLength的值为传输数据中所占的位，所以在COM模块配置信号**

**的时候一定要留有该Header的空间，不同的profile该值有所不同，需要特别**

**注意**\ ）

|image20|

图5-10 BufferProperty配置

6. 若有其他EndToEndTransformationDescription，配置跟上面类似

7. 点击界面下方E2Exfrm配置该项，先配置EndToEndTransformationIsignalProps，该项数量要与上文中配置的EndToEndTransformationDescription数量一致，做到一对一；然后配置E2Etransformer项，该项数量也要跟EndToEndTransformationIsignalProps或者EndToEndTransformationDescription一致，做到一对一；添加需要的数量的EndToEndTransformationIsignalProps和E2Etransformer，如下图

|image21|

图5-11 EndToEndTransformationIsignalProps和E2Etransformer关联

8. 详细配置EndToEndTransformationIsignalProps，先配置最后一项Transformer

项，根据选择的TransformationTechnology也即profile，根据集成手册中描述

对上面几项可配参数进行配置。\ **（特别提醒：该项目以**\ TransformationTechnol

ogy\ **的profile为profile01为例）**

|image22|

图5-12 EndToEndTransformationIsignalProps配置

9. 按需求新建E2Etransformer，并详细配置各E2Etransformer，然后将E2Eisigna

lProp与EndToEndTransformationIsignalProps关联，如图

|image23|

图5-13 E2Etransformer配置

10. 在TransformationSet中关联对应的TransformChains。

|image24|

图5-14 E2Etransformer关联

11. 点击保存按钮，右击Xfrm项点击Validate选项进行校验，校验无错误即为配

..

   置成功。

|image25|

图5-15 Xfrm配置校验及生成

5.3源代码集成
-------------

项目交付给用户的工程结构如下：

|image26|

图5-16 工程结构目录

-  BSW目录，存放模块相关的源代码和配置代码。可以看到Source目录下各个文件夹下是各个模块的源代码。

-  BSW下的Config->BSW_Config目录，用于存放配置工具生成的配置文件

E2E协议栈源代码集成步骤如下：

#. 将ORIENTAIS Configurator生成的配置文件放到Config的文件夹；

#. 将普华提供的协议栈源代码文件放在src目录。

#. 添加新增加的模块的代码头文件路径到工程设置中

协议栈调度集成
-------------

E2E协议栈调度集成步骤如下：

#. 协议栈调度集成，需要逐一排查并实现表
   4‑4协议栈集成约束清单所罗列的问题，以避免集成出现差错。

#. 编译链接代码，将生成的elf文件烧写进芯片。

E2E协议栈有关的代码，在下方的main.c文件中给出重点标注。

**注意 :
本示例中，E2E协议栈初始化的代码和启动通信的代码置于EcuM_Callout_Stubs.c文件，并不代表其他项目同样适用于将其置于EcuM_Callout_Stubs.c文件中。**

#include "E2E.h"

#include "Rte_E2EXf.h"

#include "Crc.h"

FUNC(void, ECUM_AL_DRIVERINITBSWM_0_CODE)

EcuM_AL_DriverInitBswM(uint8 drvInitIdx)

{

     P2CONST(EcuM_GenBSWPbCfgType, AUTOMATIC, CANIF_APPL_DATA) pbCfg =
EcuM_ConfigPtr->modulePBCfg;

    if (EcuMDriverInitListBswM_0 == drvInitIdx)

    {

       Dem_PreInit();

        Fee_Init(NULL_PTR);

        CanIf_Init(pbCfg->canIfPbCfg);

        CanSM_Init(pbCfg->canSmPbCfg);

        CanNm_Init(pbCfg->canNmPbCfg);

        Nm_Init(NULL_PTR);

        PduR_Init(pbCfg->pduRPbCfg);

        Com_Init(pbCfg->comPbCfg);

        ComM_Init(pbCfg->comMPbCfg);

        CanTp_Init(pbCfg->canTpPbCfg);

        NvM_Init(NULL_PTR);

        Dcm_Init(pbCfg->dcmPbCfg);

        E2EXf_Init(&E2EXf_Config);

    }

    /\*Enter in RUN after initialized all BSW mode.*/

    EcuMRunData.State = ECUM_STATE_RUN;

}

4. 根据需求对被保护数据直接调用E2Exf中接口即可：例如要发送6个字节的数据，选用profile1进行保护，发送端调用\ **E2EXf_Transformation_0**\ ()进行保护；接收端调用\ **E2EXf_Inv_Transformation_0**\ ()进行检查，该函数名来源于下图中名称添加前缀所得，每一个会生成这样的一对保护和检查函数用于收发端，不可混用，具体使用详情请参照工程中相关代码及《参考手册_E2EXf.pdf》。

.. |image1| image:: ../../_static/集成手册/E2E/image3.png
   :width: 4.26042in
   :height: 4.05208in
.. |image2| image:: ../../_static/集成手册/E2E/image4.png
   :width: 4.625in
   :height: 3.88542in
.. |image3| image:: ../../_static/集成手册/E2E/image5.png
   :width: 4.05208in
   :height: 1.89583in
.. |image4| image:: ../../_static/集成手册/E2E/image6.png
   :width: 4.30208in
   :height: 1.97917in
.. |image5| image:: ../../_static/集成手册/E2E/image7.png
   :width: 3.72917in
   :height: 3.53125in
.. |image6| image:: ../../_static/集成手册/E2E/image8.png
   :width: 5.125in
   :height: 4.82292in
.. |image7| image:: ../../_static/集成手册/E2E/image9.png
   :width: 5.42708in
   :height: 2.64583in
.. |image8| image:: ../../_static/集成手册/E2E/image10.png
   :width: 3.65625in
   :height: 3.5625in
.. |image9| image:: ../../_static/集成手册/E2E/image10.png
   :width: 3.47917in
   :height: 2.27083in
.. |image10| image:: ../../_static/集成手册/E2E/image11.png
   :width: 5.375in
   :height: 3.96875in
.. |image11| image:: ../../_static/集成手册/E2E/image12.png
   :width: 5.15625in
   :height: 3.625in
.. |image12| image:: ../../_static/集成手册/E2E/image13.png
   :width: 5.77083in
   :height: 3.78125in
.. |image13| image:: ../../_static/集成手册/E2E/image14.png
   :width: 5.76042in
   :height: 3.41667in
.. |image14| image:: ../../_static/集成手册/E2E/image15.png
   :width: 5.77083in
   :height: 2.84375in
.. |image15| image:: ../../_static/集成手册/E2E/image16.png
   :width: 5.77083in
   :height: 3.01042in
.. |image16| image:: ../../_static/集成手册/E2E/image17.png
   :width: 5.77083in
   :height: 3.53125in
.. |image17| image:: ../../_static/集成手册/E2E/image18.png
   :width: 5.76042in
   :height: 3.78125in
.. |image18| image:: ../../_static/集成手册/E2E/image19.png
   :width: 5.76042in
   :height: 2.875in
.. |image19| image:: ../../_static/集成手册/E2E/image20.png
   :width: 5.76042in
   :height: 2.38542in
.. |image20| image:: ../../_static/集成手册/E2E/image21.png
   :width: 5.76042in
   :height: 2.38542in
.. |image21| image:: ../../_static/集成手册/E2E/image22.png
   :width: 5.76042in
   :height: 2.38542in
.. |image22| image:: ../../_static/集成手册/E2E/image23.png
   :width: 5.76042in
   :height: 2.38542in
.. |image23| image:: ../../_static/集成手册/E2E/image24.png
   :width: 5.76042in
   :height: 2.38542in
.. |image24| image:: ../../_static/集成手册/E2E/image25.png
   :width: 5.76042in
   :height: 2.38542in
.. |image25| image:: ../../_static/集成手册/E2E/image26.png
   :width: 5.77083in
   :height: 3.4375in
.. |image26| image:: ../../_static/集成手册/E2E/image27.png
   :width: 2.80208in
   :height: 2.97917in
