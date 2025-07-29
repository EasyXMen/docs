============
OBD
============

目标
=====

本集成手册用于指导客户进行OBD诊断栈集成，文档主要包括的内容为：OBD诊断栈集成指导、基于特定应用的集成示例讲解。

由于各项目的需求不同，集成示例不会针对于特定的项目做详细讲解。

缩写词和术语
=============

.. table:: 表

   +---------------+------------------------------------------------------+
   | 缩写词/术语   | 描述                                                 |
   +===============+======================================================+
   | MCAL          | Microcontroller Abstraction Layer微控制器抽象层      |
   +---------------+------------------------------------------------------+
   | CanIf         | CAN Interface module CAN接口                         |
   +---------------+------------------------------------------------------+
   | ComM          | Communication Manager module 通信管理                |
   +---------------+------------------------------------------------------+
   | PduR          | PDU Router module PDU路由                            |
   +---------------+------------------------------------------------------+
   | Dcm           | Diagnostic Communication Manager 诊断通信管理        |
   +---------------+------------------------------------------------------+
   | Dem           | Diagnostic Event Manager 诊断事件管理                |
   +---------------+------------------------------------------------------+
   | CanTp         | CAN Transport Layer CAN传输层                        |
   +---------------+------------------------------------------------------+
   | Rte           | Runtime Environment 运行时环境                       |
   +---------------+------------------------------------------------------+
   | iRte          | i-Soft Runtime Environment 普华基础模块运行时环境    |
   +---------------+------------------------------------------------------+

参考文档
=========

[1]参考手册_CanIf.pdf

[2]参考手册_PduR.pdf

[3]参考手册_CanSM.pdf

[4]参考手册_DCM.pdf

[5]参考手册_Dem.pdf

[6]参考手册_CanTp.pdf

[7]参考手册_EcuC.pdf

[8] 集成手册_UDSonCAN.pdf

[9] 集成手册_CAN.pdf

协议栈集成
===========

项目交付的内容为：协议栈源码和ORIENTAIS
Studio配置工具。协议栈细分为协议栈的各模块及其对应的配置工具模块。

OBD诊断栈各配置模块的功能介绍，参见表 诊断栈各配置模块介绍。

使用协议栈源码和配置工具，进行协议栈的集成的步骤，参见表
协议栈集成的步骤。

.. table:: 表 诊断栈各配置模块介绍

   +---------+----------------------------------------------------------------------------------------------------------------------------+
   | 模块名  | 功能                                                                                                                       |
   +=========+============================================================================================================================+
   | Can     | CAN驱动配置。(由MCAL具导入)                                                                                                |
   +---------+----------------------------------------------------------------------------------------------------------------------------+
   | CanIf   | CanIf 模块主要处理上层模块与底层驱动的之间PDU 的传递，为上                                                                 |
   |         |                                                                                                                            |
   |         | 层模块提供统一的接口来管理不同的CAN 硬件模块                                                                               |
   +---------+----------------------------------------------------------------------------------------------------------------------------+
   | EcuC    | 用于辅助配置工具完成配置的模块。主要提供Pdu的定义，其它模块通过关联EcuC中Pdu，相互关联起来。                               |
   +---------+----------------------------------------------------------------------------------------------------------------------------+
   | PduR    | PDU Router主要为相关模块提供基于I-PDU的路由服务。在诊断栈中，主要是提供CANTP与DCM之间的路由服务                            |
   +---------+----------------------------------------------------------------------------------------------------------------------------+
   | CanTp   | CANTP 模块实现依据ISO15765-2 标准规范中定义的CAN 总线数据在传输层的数据接收发送功能                                        |
   +---------+----------------------------------------------------------------------------------------------------------------------------+
   | DCM     | 依据ISO15765-3和ISO15031-5标准描述，实现诊断请求报文的解析，响应(正响应和负响应)与执行。主要功能有：实现UDS、OBD诊断服务。 |
   +---------+----------------------------------------------------------------------------------------------------------------------------+
   | DEM     | 实现诊断故障的存储与管理功能，提供API 接口供其他模块读取                                                                   |
   |         |                                                                                                                            |
   |         | DTC 和对应的冻结帧数据和扩展数据                                                                                           |
   +---------+----------------------------------------------------------------------------------------------------------------------------+

.. table:: 表 协议栈集成的步骤

   +------+----------------------------------------+------------------------------------------------------+
   | 步骤 | 操作                                   | 说明                                                 |
   +======+========================================+======================================================+
   | 1    | ORIENTAIS                              | 若配置工具已经搭建，则仅需进行协议栈模块的加载操作。 |
   |      | Stuido配置工具工程搭建和协议栈模块加载 |                                                      |
   +------+----------------------------------------+------------------------------------------------------+
   | 2    | 模块配置及配置文件生成                 | NA                                                   |
   +------+----------------------------------------+------------------------------------------------------+
   | 3    | 代码集成                               | 现有工程、协议栈源代码和配置生成文件的集成。         |
   +------+----------------------------------------+------------------------------------------------------+
   | 4    | 验证测试                               | NA                                                   |
   +------+----------------------------------------+------------------------------------------------------+

.. note::
   **协议栈集成之前，用户须确保已经有基础工程，且本协议栈相关的其他协议栈能正常工作。**

新建ORIENTAIS Stuido配置工程及模块加载
--------------------------------------

安装ORIENTAIS Studio软件后，双击软件图标打开软件。

   |image1|

   图 新建工程

菜单栏File🡪New🡪Project，新建工程。

   |image2|

   图 新建工程

在弹出的新建窗口中选择Autosar下的 [BSW Project]，选择Next。

   |image3|

   图 新建工程

在弹出的窗口中输入工程名，选择Finish。

   |image4|

   图 新建工程

选择[Bsw_Builder]，右键单击，选择New ECU Configuration。

   |image5|

   图 新建工程

在弹出的窗口中输入ECU名，然后选择Next。

   |image6|

   图 选择芯片平台

在弹出的窗口中勾选需添加的模块，点击Finish。

   |image7|

   图 选择模块

新建工程如下所示，步骤0中添加的模块已经被加入到工程中。

   |image8|

   图 工程结构示例

模块配置及生产代码
------------------

模块配置
~~~~~~~~

模块的具体配置，取决于具体的项目需求。OBD诊断栈各模块配置项的详细介绍，参见表
协议栈各模块配置参考文档。

.. table:: 表 协议栈各模块配置参考文档

   +----------------+-----------------------------------------------------+
   | 模块           | 参考文档及其章节                                    |
   +================+=====================================================+
   | Can            | MCAL对应的Can配置手册                               |
   +----------------+-----------------------------------------------------+
   | CanIf          | 参考手册_CanTp.pdf                                  |
   +----------------+-----------------------------------------------------+
   | PduR           | 参考手册_PduR.pdf                                   |
   +----------------+-----------------------------------------------------+
   | NvM            | 参考手册_NvM.pdf                                    |
   +----------------+-----------------------------------------------------+
   | CanTp          | 参考手册_CanTp.pdf                                  |
   +----------------+-----------------------------------------------------+
   | Dcm            | 参考手册_Dcm.pdf                                    |
   +----------------+-----------------------------------------------------+
   | Dem            | 参考手册_Dem.pdf                                    |
   +----------------+-----------------------------------------------------+

配置代码生成
~~~~~~~~~~~~

在ORIENTAIS Stuido主界面左方，选择对应的协议栈，单击右键弹出Validate
All和Generate All菜单。

   |image9|

   图 生成配置

选择Validate
All对本协议栈各配置选项进行校验，没有错误提示信息即校验通过。若有错误信息，请按照错误提示修改。

选择Generate
All，生成配置文件。右下角的Console窗口输出生成的配置文件信息。

   |image10|

   图 生成配置结果

将ORIENTAIS Studio切换到Resource模式，即可查看生成的配置文件。

   |image11|

   图 生成配置工程结构

功能集成
--------

代码集成
~~~~~~~~

诊断栈代码包括两部分：项目提供的诊断栈源码和ORIENTAIS
Studio配置生成代码。诊断栈集成包括诊断栈源码（CANIF，CANSM，PDUR，CANTP，COMM，DCM，DEM等）、定时器源码和部分其他模块源码。

用户须将诊断栈源码和章节（配置代码生成）生成的源代码添加到集成开发工具的对应文件夹。

.. note::
   **诊断栈集成之前，用户须确保已经有通信基础工程，且本诊断栈相关的其他功能栈能正常工作。**

集成注意事项
~~~~~~~~~~~~

对于集成过程中，协议栈特殊要求和用户经常出现的问题，归类总结形成表
协议栈协议栈集成约束清单。用户需逐一排查表中的约束项，以避免集成问题出现。

.. table:: 表 协议栈协议栈集成约束清单

   +------+----------+----------------------------------------------------------------------------------+
   | 编号 | 类别     | 约束限制                                                                         |
   +======+==========+==================================================================================+
   | 1    | 堆栈     | 用户需确保为任务堆栈和中断堆栈分配足够的堆栈空间。                               |
   +------+----------+----------------------------------------------------------------------------------+
   | 2    | 头文件   | 添加协议栈代码之后，用户需更新集成开发工具中的头文件路径。                       |
   |      |          |                                                                                  |
   |      |          | 调用协议栈API的源文件，需要包含协议栈的头文件。                                  |
   +------+----------+----------------------------------------------------------------------------------+
   | 3    | 初始化   | OBD诊断栈的初始化顺序为：Dem_PreInit，CanTp_Init， Dcm_Init，Dem_Init。          |
   +------+----------+----------------------------------------------------------------------------------+
   | 4    | 周期函数 | CanTp_MainFunction，Dcm_MainFunction和Dem_MainFunction需要被周期性任务函数调用。 |
   +------+----------+----------------------------------------------------------------------------------+

集成示例
=========

本章节通过OBD诊断栈为例，向用户展示OBD诊断栈的集成过程。用户可以据此熟悉OBD诊断栈配置工具的配置过程，以及如何应用配置工具生成的配置文件。示例是基于具有正常工作的CAN通信工程之上。

本章节先完成基本OBD配置，使得工程可以编译通过，并实现基础OBD诊断通讯，然后根据具体需求服务进行添加或修改。

.. note::
   **本示例不代表用户的实际配置情况，用户需要根据自己的实际需求，决定各个参数的配置。**

集成目标
--------

通过搭建基础工程，实现OBD诊断基本请求应答功能。使用标准帧CAN0x7df作为请求，标准帧0x709作为响应，同时实现OBD服务01,02,03,07,09的功能。示例网络层时间参数如表
 网络层定时参数（仅 OBD 排放相关诊断要求）

.. table:: 表 网络层定时参数（仅 OBD 排放相关诊断要求）

   +----------+--------------------------+--------------+--------------------+
   | 定时参数 | 描述                     | 超时时间(ms) | 性能要求时间（ms） |
   +==========+==========================+==============+====================+
   | N_As     | 发送方 CAN 报文确认超时  | 25           | -                  |
   +----------+--------------------------+--------------+--------------------+
   | N_Ar     | 接收方 CAN 报文确认超时  | 25           | -                  |
   +----------+--------------------------+--------------+--------------------+
   | N_Bs     | 流控帧传输超时           | 75           | -                  |
   +----------+--------------------------+--------------+--------------------+
   | N_Br     | 流控帧接收端发送等待时间 | -            | <10                |
   +----------+--------------------------+--------------+--------------------+
   | N_Cs     | 连续帧发送时间间隔       | -            | ST*min             |
   +----------+--------------------------+--------------+--------------------+
   | N_Cr     | 连续帧传输超时           | 150 ms       | -                  |
   +----------+--------------------------+--------------+--------------------+

模块的配置
----------

新建配置工程及模块加载操作，请参考本文档章节（模块配置及生产代码）。生成代码过程请参考章节（模块配置及生产代码）。

Can模块与CanIf模块配置
~~~~~~~~~~~~~~~~~~~~~~

在CAN模块与CANIF模块中实现用于OBD通信的CAN报文，具体配置方法请参考文档《集成手册_CAN》。

.. table:: 表 OBD协议CAN需求

   +--------------+-------------------------+----------------------------+
   | 报文ID       | 发送/接收               | 报文长度                   |
   +==============+=========================+============================+
   | 0x7df        | 接收                    | 8字节                      |
   +--------------+-------------------------+----------------------------+
   | 0x708        | 接收                    | 8字节                      |
   +--------------+-------------------------+----------------------------+
   | 0x709        | 发送                    | 8字节                      |
   +--------------+-------------------------+----------------------------+

EcuC模块配置
~~~~~~~~~~~~

请参考《集成手册_UDSonCAN.pdf》中的EcuC模块配置。

CanTp模块配置
~~~~~~~~~~~~~

请参考《集成手册_UDSonCAN.pdf》中的CanTp模块配置。

PduR模块配置
~~~~~~~~~~~~

请参考《集成手册_UDSonCAN.pdf》中的PduR模块配置。

DCM模块配置
~~~~~~~~~~~

#. 双击DCM模块，打开DCM模块配置界面。

   |image12|

   图 DCMGeneral

#. DCMGeneral标签页中的参数保持默认即可。

DSD配置
^^^^^^^

#. 新建DcmDsdSidTab，配置DcmDsdSidTabId需与其他服务列表（如UDS）不一同的值。

   |image13|

   图 DcmDsdSidTab

勾选DcmDsdServiceUsed使能服务；

配置需要的OBD服务DcmDsdSidTabServiceId。

   |image14|

   图 DsdService

DSL配置
^^^^^^^

#. DcmDslBuffer中配置两个buffer分别用于发送和接收，配置Dcm
   Tx、RxBuffer及其length，需要与EcuC中Dcm对应的Pdu Length的值保持一致。

   |image15|

   图 DcmDslBuffer

#. 配置OBD的DSLProtocol，实现CANTp与DCM之间的PDU关联。需要修改项如下，若项目无特殊需求，未提到的配置保持默认值即可。

   DcmDslProtocolID选择DCM_OBD_ON_CAN；

   DcmDslProtocolSIDTable选择DcmDsdServiceTable中的OBD服务表；

   DcmDslProtocolRxBufferRef和DcmDslProtocolTxBufferRef关联接收和发送的buffer配置。

   |image16|

   图 DSLProtocol

#. 在上步的DcmDslProtocolRow_OBD中新建配置DcmDslMainConnection，选择Dcm通信的ComMChannel，并新建1个DcmDslProtocolRx，1个DcmDslProtocolTx。

   |image17|

   图 DcmDslMainConnection

#. 为每个DcmDslProtocolRx、DcmDslProtocolTx添加Dcm对应的PDU及寻址类型。

   |image18|

   图 DcmDslProtocolRx

   |image19|

   图 DcmDslProtocolTx

#. 右键新建DcmDslCallbackDCMRequestService。

   |image20|

   图 DcmDslCallbackDCMRequestService

DSP配置
^^^^^^^

本小节配置目的是完成基本OBD诊断通讯和编译通过，具体服务的功能请见本章节后续小节具体服务的描述。此小节目的是建立最小系统配置，未提到的配置保持默认即可，服务的配置将在本章节具体服务小节中介绍。

   |image21|

   图 DSP

添加一个DcmDspPid。选择服务后暂不修改其它内容，内容修改将在章节（Service 0x01）进行。

   |image22|

   图 DcmDspPid

   |image23|

   图 DcmDspPidService

DEM模块配置
~~~~~~~~~~~

DEMGeneral配置
^^^^^^^^^^^^^^

#. 如图所示添加配置集。添加Dataelement,GeneralOBD,Indicator。

   |image24|

   图 DEMGeneral

#. 在DemGeneral->DemOBDSupport配置为DEM_OBD_MASTER。同时DemGeneral->DemEventMemorySet->DemMILIndicatorRef关联一个DemIndicator。

   DemGeneral->DemEventMemorySet->DemTypeOfDTCSupported选择DEM_DTC_TRANSLATION_ISO15031_6。

   DemGeneral->DemClearDTCLimitation选择DEM_ALL_SUPPORTED_DTCS。

   若无明确需求，其它配置可保持默认即可。

   |image25|

   |image26|

   |image27|

   图 DemGeneral

   新建CSDataElement在DemGeneralOBD中关联。

   |image28|

   图 DemGeneralOBD

DEMConfig配置
^^^^^^^^^^^^^

配置DemDTCAttributes，关联DemMemoryDestinationRef到DemPrimaryMemory。关联DemFreezeFrameRecNumClassRef。其它配置先保持默认配置。

#. 新建DTCAttribute用于OBD的DTC。

   |image29|

   图6 DTCAttribute

#. 添加一个DemDTC，设置DemDtcValue，关联DemDTCAttributesRef，并关联DemOBDDTCRef。

   |image30|

   图 DemDTC

#. 配置DemEventParameter：

   #. 勾选DemEventAvailable；

   #. 关联DemOperationCycleRef

   #. DemEventKind选择SWC

   #. DemDTCRef关联步骤②配置的DTC

   #. 修改DemEventKind为DEM_EVENT_KIND_SWC

      |image31|

      图 DemEventParameter

Service 0x01 
~~~~~~~~~~~~~

#. 在DcmDsp中添加DcmDspPid，根据需求确定PID。在PidIdentifier填写PID，在DcmDspPidService选择01服务，在DcmDspPidSize中填写其数据长度：

   DcmDspPidIdentifier：配置PID

   DcmDspPidService：选择使用此PID的服务

   DcmDspPidSize：设置数据大小

   DcmDspPidUsed：使能此PID

   |image32|

   图 DcmDspPid

#. 配置DcmDspPidData建立service1的配置

   |image33|

   图 DcmDspPidService

#. DcmDspPidDataUsePort一般选择USE_DATA_SYNCH_FNC或者USE_DATA_SYNCH_CLENT_SERVER，协议栈会从DcmDspPidDataReadFnc中获取数据，并设置DcmDspPidDataType。

   |image34|

   图 DcmDspPidDataUsePort

#. 根据DcmDspPidDataReadFnc配置构造获取PID数据的函数。示例如下：

Service 0x02 
~~~~~~~~~~~~~

#. 添加DemExternalCSDataElementClass用于获取PID数据

   |image35|

   图 DemExternalCSDataElementClass

#. 配置DemPidClass中DemPidIdentifier，并关联步骤1中DemExternalCSDataElementClass

   |image36|

   图 DemPidClass

   |image37|

   图 DemPidClass

#. DCM新建配置一个用于Service02的DcmDspPidData

   |image38|

   图 DcmDspPidData

#. DcmDspPidData关联步骤2中DemPidClass。

   |image39|

   图 DcmDspPidData

#. DemDTCAttributes_OBD中不能有其它协议的FreezeFrame。

   |image40|

   图 DemDTCAttributes

Service 0x03 / 07 
~~~~~~~~~~~~~~~~~~

#. 在DcmDsdServiceTable中添加03和07服务；

#. （0x0A服务选用）在DemGeneral中DemEventMemorySet下DemPermanentMemorys添加DemPermanentMemory用于0x0A服务。根据需求将DemGeneral中DemEventMemorySet的DemMaxNumberEventEntryPermanent配置为非0值。

   |image41|

   图 DcmDsdServiceTable

   |image42|

   图 DemGeneral

#. 添加DemOBDDTC并配置DemDtcValue

   |image43|

   图 DemOBDDTC

#. （0x0A服务选用）DemMemoryDestinationRef选择DemPermanentMemory。

   |image44|

   图 DemDTCAttributes

#. 添加DemDTC并配置，根据需求选择DemDTCAttributes。

   |image45|

   图 DemDTC_P014300

#. 添加DemEventParameter，勾选DemEventAvailable；关联DemDTCRef；选择DemOperationCycleRef。

   |image46|

   图 DemEventParameter

Service 0x09
~~~~~~~~~~~~

在DcmDsdServiceTable中添加0x09的OBD服务列表

   |image47|

   图 DcmDsdServiceTable

在DSP中添加DcmDspVehInfo，配置DcmDspVehInfoInfoType，此处以INFOTYPE 0x02
(VIN)为例，填写为0x02。

   |image48|

   图 DcmDspVehInfo

在DcmDspVehInfo中添加DcmDspVehInfoData，配置获取Vehicle
information的函数名称
DcmDspVehInfoDataReadFnc或可直接勾选DcmDspVehInfoDataUsePort，并根据需求配置数据的大小DcmDspVehInfoDataSize为17字节。

   |image49|

   图 DcmDspVehInfoData

在Rte_Dcm.c中将数据传入 DcmDspVehInfoDataReadFnc配置的函数.

   |image50|

   图 测试示例程序

源代码集成
----------

诊断栈源代码集成步骤如下：

#. 在MCAL工程的基础上，同步章（Can模块与CanIf模块配置）添加的Can模块配置文件。

#. 从基线中取出章（代码集成）中相关的源代码添加到工程中。

#. 将在章（配置代码生成）中ORIENTAS配置生成的诊断相关配置文件添加到工程中。

#. 添加相关头文件目录。

协议栈调度集成
--------------

请参考《集成手册_UDSonCAN.pdf》中的诊断栈调度集成。

.. note::
   **工程中涉及故障检测是需要自己实现，以下验证结果是人为添加测试代码调用Dem_SetEventStatus函数。**

验证结果
--------

验证Service 0x01
~~~~~~~~~~~~~~~~

#. 通过CAN工具向ECU发送01服务请求报文：

CANID：0x7df

请求内容：02 01 00 AA AA AA AA AA

期望结果：收到CANID0x709响应报文06 41 00 80 00 00 00 AA

#. 通过CAN工具向ECU发送01服务请求报文：

   CANID：0x7df

   请求内容：02 01 01 AA AA AA AA AA

   期望结果：收到CANID0x709响应，内容与章节（Service 0x01）接口填写的数据内容一致，报文为06
   41 01 01 02 03 04 AA

   |image51|

   图 验证结果01

验证Service 0x02
~~~~~~~~~~~~~~~~

#. 通过CAN工具向ECU发送02服务请求报文：

   CANID：0x7df

   请求内容：03 02 00 00 AA AA AA AA

   期望结果：收到CANID0x709响应报文07 42 00 00 00 10 00 00

#. 通过CAN工具向ECU发送02服务请求报文：

   CANID：0x7df

   请求内容：03 02 0C 00 AA AA AA AA

   期望结果：收到CANID0x709响应报文05 42 0C 00 11 22 AA AA

   |image52|

   图 验证02服务功能

验证0x03 / 07
~~~~~~~~~~~~~

#. 通过CAN工具向ECU发送03服务请求报文：

   CANID：0x7df

   请求内容：01 03 AA AA AA AA AA AA

   期望结果：收到CANID0x709响应报文04 43 01 01 43 AA AA AA

#. 通过CAN工具向ECU发送07服务请求报文：

   CANID：0x7df

   请求内容：01 07 AA AA AA AA AA AA

   期望结果：收到CANID0x709响应报文04 47 01 43 AA AA AA

   |image53|

   图 03&07验证结果

验证Service 0x09
~~~~~~~~~~~~~~~~

#. 通过CAN工具向ECU发送09服务请求报文：

   CANID：0x7df

   请求内容：02 09 00 AA AA AA AA AA

   期望结果：收到CANID0x709响应报文06 49 00 40 00 00 00 AA

#. 通过CAN工具向ECU发送09服务请求报文：

   CANID：0x7df

   请求内容：02 09 02 AA AA AA AA AA

   期望结果：收到CANID0x709响应，内容与章节（Service 0x09）填写的数据内容一致。

   |image54|

   图 验证结果09

.. |image1| image:: /_static/集成手册/集成手册_OBD/image2.png
   :width: 5.76736in
   :height: 3.2125in


.. |image2| image:: /_static/集成手册/集成手册_OBD/image3.png
   :width: 5.76736in
   :height: 3.2125in


.. |image3| image:: /_static/集成手册/集成手册_OBD/image4.png
   :width: 5.76736in
   :height: 3.2125in


.. |image4| image:: /_static/集成手册/集成手册_OBD/image5.png
   :width: 5.76736in
   :height: 3.2125in


.. |image5| image:: /_static/集成手册/集成手册_OBD/image6.png
   :width: 5.76736in
   :height: 3.2125in


.. |image6| image:: /_static/集成手册/集成手册_OBD/image7.png
   :width: 5.76736in
   :height: 3.2125in


.. |image7| image:: /_static/集成手册/集成手册_OBD/image8.png
   :width: 5.76736in
   :height: 6.0125in


.. |image8| image:: /_static/集成手册/集成手册_OBD/image9.png
   :width: 5.76736in
   :height: 3.2125in


.. |image9| image:: /_static/集成手册/集成手册_OBD/image10.png
   :width: 5.76736in
   :height: 3.2125in


.. |image10| image:: /_static/集成手册/集成手册_OBD/image11.png
   :width: 5.76736in
   :height: 3.2125in


.. |image11| image:: /_static/集成手册/集成手册_OBD/image12.png
   :width: 5.76736in
   :height: 3.2125in


.. |image12| image:: /_static/集成手册/集成手册_OBD/image13.png
   :width: 5.76736in
   :height: 3.2125in


.. |image13| image:: /_static/集成手册/集成手册_OBD/image14.png
   :width: 5.76736in
   :height: 3.2125in


.. |image14| image:: /_static/集成手册/集成手册_OBD/image15.png
   :width: 5.76736in
   :height: 3.2125in


.. |image15| image:: /_static/集成手册/集成手册_OBD/image16.png
   :width: 5.76736in
   :height: 3.2125in


.. |image16| image:: /_static/集成手册/集成手册_OBD/image17.png
   :width: 5.76736in
   :height: 3.2125in


.. |image17| image:: /_static/集成手册/集成手册_OBD/image18.png
   :width: 5.76736in
   :height: 3.2125in


.. |image18| image:: /_static/集成手册/集成手册_OBD/image19.png
   :width: 5.76736in
   :height: 3.2125in


.. |image19| image:: /_static/集成手册/集成手册_OBD/image20.png
   :width: 5.76736in
   :height: 4.3125in


.. |image20| image:: /_static/集成手册/集成手册_OBD/image21.png
   :width: 5.76736in
   :height: 3.2125in


.. |image21| image:: /_static/集成手册/集成手册_OBD/image22.png
   :width: 4.76736in
   :height: 3.9125in


.. |image22| image:: /_static/集成手册/集成手册_OBD/image23.png
   :width: 5.76736in
   :height: 3.2125in


.. |image23| image:: /_static/集成手册/集成手册_OBD/image24.png
   :width: 5.76736in
   :height: 4.9125in


.. |image24| image:: /_static/集成手册/集成手册_OBD/image25.png
   :width: 5.76736in
   :height: 4.2125in


.. |image25| image:: /_static/集成手册/集成手册_OBD/image26.png
   :width: 5.76736in
   :height: 4.2125in


.. |image26| image:: /_static/集成手册/集成手册_OBD/image27.png
   :width: 5.76736in
   :height: 3.9125in


.. |image27| image:: /_static/集成手册/集成手册_OBD/image28.png
   :width: 5.76736in
   :height: 3.9125in


.. |image28| image:: /_static/集成手册/集成手册_OBD/image29.png
   :width: 5.76736in
   :height: 3.2125in


.. |image29| image:: /_static/集成手册/集成手册_OBD/image30.png
   :width: 5.76736in
   :height: 3.2125in


.. |image30| image:: /_static/集成手册/集成手册_OBD/image31.png
   :width: 5.76736in
   :height: 3.2125in


.. |image31| image:: /_static/集成手册/集成手册_OBD/image32.png
   :width: 5.76736in
   :height: 3.2125in


.. |image32| image:: /_static/集成手册/集成手册_OBD/image33.png
   :width: 5.76736in
   :height: 3.2125in


.. |image33| image:: /_static/集成手册/集成手册_OBD/image34.png
   :width: 5.76736in
   :height: 3.9125in


.. |image34| image:: /_static/集成手册/集成手册_OBD/image35.png
   :width: 5.76736in
   :height: 4.5125in


.. |image35| image:: /_static/集成手册/集成手册_OBD/image36.png
   :width: 5.76736in
   :height: 3.3125in


.. |image36| image:: /_static/集成手册/集成手册_OBD/image37.png
   :width: 5.76736in
   :height: 3.9125in


.. |image37| image:: /_static/集成手册/集成手册_OBD/image38.png
   :width: 5.76736in
   :height: 3.9125in


.. |image38| image:: /_static/集成手册/集成手册_OBD/image39.png
   :width: 5.26736in
   :height: 3.2125in


.. |image39| image:: /_static/集成手册/集成手册_OBD/image40.png
   :width: 5.76736in
   :height: 3.2125in


.. |image40| image:: /_static/集成手册/集成手册_OBD/image41.png
   :width: 5.76736in
   :height: 3.2125in


.. |image41| image:: /_static/集成手册/集成手册_OBD/image42.png
   :width: 5.76736in
   :height: 3.2125in


.. |image42| image:: /_static/集成手册/集成手册_OBD/image43.png
   :width: 5.76736in
   :height: 3.2125in


.. |image43| image:: /_static/集成手册/集成手册_OBD/image44.png
   :width: 5.76736in
   :height: 3.2125in


.. |image44| image:: /_static/集成手册/集成手册_OBD/image45.png
   :width: 5.76736in
   :height: 3.2125in


.. |image45| image:: /_static/集成手册/集成手册_OBD/image46.png
   :width: 5.76736in
   :height: 3.2125in


.. |image46| image:: /_static/集成手册/集成手册_OBD/image47.png
   :width: 5.76736in
   :height: 3.2125in


.. |image47| image:: /_static/集成手册/集成手册_OBD/image48.png
   :width: 5.76736in
   :height: 3.2125in


.. |image48| image:: /_static/集成手册/集成手册_OBD/image49.png
   :width: 5.76736in
   :height: 3.2125in


.. |image49| image:: /_static/集成手册/集成手册_OBD/image50.png
   :width: 5.36736in
   :height: 3.4125in


.. |image50| image:: /_static/集成手册/集成手册_OBD/image51.png
   :width: 5.76736in
   :height: 3.2125in


.. |image51| image:: /_static/集成手册/集成手册_OBD/image52.png
   :width: 5.76736in
   :height: 3.2125in


.. |image52| image:: /_static/集成手册/集成手册_OBD/image53.png
   :width: 5.76736in
   :height: 3.2125in


.. |image53| image:: /_static/集成手册/集成手册_OBD/image54.png
   :width: 4.46736in
   :height: 2.1125in

.. |image54| image:: /_static/集成手册/集成手册_OBD/image55.png
   :width: 4.46736in
   :height: 2.1125in