===================
CanSM
===================
.. 标题标识符“===”的长度必须要大于其内容的长度，否则会报错，其他标题亦是如此


文档信息(Document Information)
=====================================

版本历史(Version History)
---------------------------------

.. list-table::
   :widths: 10 10 10 10 20
   :header-rows: 1

   * - 日期(Date)
     - 作者(Author)
     - 版本(Version)
     - 状态(Status)
     - 说明(Description)
   * - 2025/3/7
     - xiaojian.liang
     - V0.1
     - 发布(Release)
     - 首次发布(First Release)
   * - 2025/04/04
     - xiaojian.liang
     - V1.0
     - 发布(Release)
     - 正式发布(Official Release)

参考文档(References)
--------------------------------

.. list-table::
   :widths: 10 10 30 10
   :header-rows: 1

   * - 编号(Number)
     - 分类(Classification)
     - 标题(Title)
     - 版本(Version)
   * - 1
     - AUTOSAR
     - AUTOSAR_SWS_CANStateManager.pdf
     - R23-11
   * - 2
     - AUTOSAR
     - AUTOSAR_SWS_COMManager.pdf
     - R23-11
   * - 3
     - AUTOSAR
     - AUTOSAR_SWS_NetworkManagementInterface.pdf
     - R23-11
   * - 4
     - AUTOSAR
     - AUTOSAR_SWS_BSWModeManager.pdf
     - R23-11
   * - 5
     - AUTOSAR
     - AUTOSAR_SWS_CANInterface.pdf
     - R23-11
   * - 6
     - AUTOSAR
     - AUTOSAR_SWS_CANNetworkManagement.pdf
     - R23-11

术语与简写(Terms and Abbreviations)
==========================================


术语(Terms)
-------------------------
   .. :align: center   表格内容居中(Table contents are centered)

None

简写(Abbreviations)
----------------------------

.. list-table::
   :widths: 10 20 30
   :header-rows: 1

   * - 缩写词(Abbreviation)
     - 英文全称(Full English name)
     - 中文解释(Chinese explanation)

   * - CanSM
     - CAN State Manager
     - CAN 状态管理

   * - BswM
     - BSW Mode Manager
     - 基础软件模式管理

   * - EcuM
     - Ecu State Manager
     - Ecu 状态管理

   * - CanIf
     - Can Interface
     - CAN 接口模块

   * - DEM
     - Diagnostic Event Manager
     - 诊断事件处理

   * - DET
     - Default Error Tracer
     - 默认错误检测

   * - EcuM
     - ECU State Manager
     - ECU 状态管理模块

   * - PN
     - Partial Network
     - 部分网络

   * - ComM
     - Com Manager
     - 通讯管理模块

简介(Introduction)
=========================


CanSM 模块负责 CAN 网络的控制流抽象，它使用 CanIf 模块的 API，根据 ComM 模块的模式请求更改已配置的 CAN 网络的通信模式。CAN 控制器模式和 CAN 收发器模式的任何更改将由 CanIf 模块通知 CanSM 模块。根据 CanIf 通知和 CanSM 状态机的状态，CanSM 模块将通知 ComM 和 BswM。

The CanSM module is responsible for the control flow abstraction of the CAN network. It uses the API of the CanIf module to change the communication mode of the configured CAN network according to the mode request from the ComM module. Any changes in the CAN controller mode and CAN transceiver mode will be notified to the CanSM module by the CanIf module. Based on the CanIf notification and the state of the CanSM state machine, the CanSM module will notify ComM and BswM.

.. figure:: ../../../_static/参考手册/CanSM/Layered-Software-Architecture-from-CanSM-point-of-view.png
   :alt: Layered Software Architecture from-CanSM point of view
   :name: Layered-Software-Architecture-from-CanSM-point-of-view
   :align: center

   Layered Software Architecture from-CanSM point of view


功能描述(Functional Description)
====================================
.. 本章节仅描述模块支持的功能大致情况，不宜做细致描述；更加细致的描述在配置章节，结合配置，从集成角度描述

特性(Features)
-----------------------

.. only:: doc_pbs
  
  变体(Variant)
  ~~~~~~~~~~~~~~~~~~~~~~~
    
  - 支持在不同变体中配置不同的 `CanSMModeRequestRepetitionMax` 和 `CanSMModeRequestRepetitionTime`。
  
    Support configuring different `CanSMModeRequestRepetitionMax` and `CanSMModeRequestRepetitionTime` in different variants.
  
  - 支持相同的 CAN 网络在不同的变体中配置不同的 bus-off 恢复时间参数 `CanSMBorCounterL1ToL2, CanSMBorTimeL1, CanSMBorTimeL2` 和 `CanSMBorTimeTxEnsured`。
  
    Support configuring different bus-off recovery time parameters `CanSMBorCounterL1ToL2`, `CanSMBorTimeL1`, `CanSMBorTimeL2` and `CanSMBorTimeTxEnsured` for the same CAN network in different variants.
  
  - 支持相同的 CAN 网络在不同的变体中的产品错误 `CANSM_E_BUS_OFF` 和 `CANSM_E_MODE_REQUEST_TIMEOUT` 使用不同的 Dem Event。
  
    Support that the product errors `CANSM_E_BUS_OFF` and `CANSM_E_MODE_REQUEST_TIMEOUT` of the same CAN network in different variants use different Dem Events.
  
状态机(State machine)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

CAN 总线的状态管理器 CanSM，负责实现 CAN 网络控制流程的抽象。CanSM 提供 API 以便 ComM 来请求 CAN 网络进行通信模式的切换。ComM 请求切换网络模式的时候，会传递一个参数(用来标识是哪个网络)。对应网络收到这个请求之后，会执行对应的通信模式切换。在网络通信模式切换的过程中，会执行对应的 CAN 外设控制和 PDU 处理。

CanSM, the state manager of the CAN bus, is responsible for implementing the abstraction of CAN network control processes. CanSM provides an API for ComM to request the CAN network to switch communication modes. When ComM requests to switch the network mode, it will pass a parameter (used to identify which network it is). After receiving this request, the corresponding network will execute the corresponding communication mode switch. During the switching of network communication modes, the corresponding CAN peripheral control and PDU processing will be performed.

.. figure:: ../../../_static/参考手册/CanSM/CANSM_BSM.png
   :alt: CANSM_BSM, state machine diagram for one CAN network
   :name: CANSM_BSM
   :align: center

   CANSM_BSM, state machine diagram for one CAN network

上电后，CanSM 会默认处于 CANSM_BSM_S_NOT_INITIALIZED 状态，在经过初始化后，状态将切换至 CANSM_BSM_S_PRE_NOCOM。如果 EcuM 调用 CanSM_StartWakeUpSource 通知 CanSM 唤醒源被启动，那么状态机将切换至 CANSM_BSM_WUVALIDATION 状态。如果接收到 ComM 的 FULL_COMMUNICATION 请求，那么状态机将切换至 CANSM_BSM_S_PRE_FULLCOM 状态。在 CanSM 通知上层 ComM 和 BswM 底层网络已经切换至 FULL_COMMUNICATION，并且调用 CanIf_SetPduMode 更新 PDU 通道状态后，状态机将切换至 CANSM_BSM_S_FULLCOM。

After power-on, CanSM defaults to the CANSM_BSM_S_NOT_INITIALIZED state. After initialization, the state switches to CANSM_BSM_S_PRE_NOCOM. If EcuM calls CanSM_StartWakeUpSource to notify CanSM that the wake-up source has been activated, the state machine switches to the CANSM_BSM_WUVALIDATION state. If a FULL_COMMUNICATION request from ComM is received, the state machine switches to the CANSM_BSM_S_PRE_FULLCOM state. After CanSM notifies the upper-layer ComM and BswM that the underlying network has switched to FULL_COMMUNICATION and calls CanIf_SetPduMode to update the PDU channel state, the state machine switches to CANSM_BSM_S_FULLCOM.

在 CANSM_BSM_S_FULLCOM 状 态 中 如 果 接 收 到 ComM 的 SILENT_COMMUNICATION 请求，状态将切换至 CANSM_BSM_S_SILENTCOM，或接收到 ComM 的 NO_COMMUNICATION 请求，状态将切换至 CANSM_BSM_S_PRE_NOCOM。

In the CANSM_BSM_S_FULLCOM state, if a SILENT_COMMUNICATION request from ComM is received, the state switches to CANSM_BSM_S_SILENTCOM; or if a NO_COMMUNICATION request from ComM is received, the state switches to CANSM_BSM_S_PRE_NOCOM.

在CANSM_BSM_S_FULLCOM 状态中如果 CanSM_SetBaudrate 接口被上层调用，需要调用 BswM_CanSM_CurrentState 通知 BSWM 当前状态为 CANSM_BSWM_CHANGE_BAUDRATE，状态机将切换至 CANSM_BSM_S_CHANGE_BAUDRATE。

In the CANSM_BSM_S_FULLCOM state, if the CanSM_SetBaudrate interface is called by the upper layer, BswM_CanSM_CurrentState needs to be invoked to notify BSWM that the current state is CANSM_BSWM_CHANGE_BAUDRATE, and the state machine will switch to CANSM_BSM_S_CHANGE_BAUDRATE.

在 CANSM_BSM_S_CHANGE_BAUDRATE 中进行波特率修改的相关操作，操作结束后根据已有的 ComM 的网络请求状态来决定切换至哪个状态机。

In CANSM_BSM_S_CHANGE_BAUDRATE, perform operations related to baud rate modification. After the operations are completed, determine which state the state machine switches to based on the existing network request status of ComM.

Bus-off 恢复功能 Bus-Off(Recovery Function)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
CanSM 可以配置快恢复时间 CanSMBorTimeL1 和慢恢复时时间 CanSMBorTimeL2，以及经过多少次快恢复切换为慢恢复的次数 CanSMBorCounterL1ToL2。当底层发生 bus-off 时，会调用 CanSM 的 CanSM_ControllerBusOff 函数进行通知。CanSM 会调用 CanIf 的 CanIf_SetControllerMode 函数将控制器状态设置为 CAN_CS_STARTED，当接收到底层调用的 CanSM_ControllerModeIndication 的设置成功的通知后，开始 bus-off 定时器的计时，当 bus-off 快恢复的时间超时后，调用 CanIf_SetPduMode 设置 Pdu 传输状态为 CANIF_ONLINE，当快恢复的次数超过配置参数 CanSMBorCounterL1ToL2 时，将按照慢恢复的时间进行恢复。

CanSM can be configured with a fast recovery time (CanSMBorTimeL1), a slow recovery time (CanSMBorTimeL2), and the number of fast recoveries after which it switches to slow recovery (CanSMBorCounterL1ToL2). When a bus-off occurs at the underlying layer, the CanSM_ControllerBusOff function of CanSM is called for notification. CanSM calls the CanIf_SetControllerMode function of CanIf to set the controller state to CAN_CS_STARTED. After receiving a successful setting notification from the underlying layer via CanSM_ControllerModeIndication, it starts the bus-off timer. When the bus-off fast recovery time times out, CanIf_SetPduMode is called to set the PDU transmission state to CANIF_ONLINE. When the number of fast recoveries exceeds the configured parameter CanSMBorCounterL1ToL2, recovery is performed according to the slow recovery time.

偏差(Deviation)
-------------------------
.. 有序列表示例

None


扩展(Extension)
-------------------------

None


集成(Integration)
=========================

文件列表(File List)
-----------------------------

静态文件(Static Files)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - 文件(File)
     - 描述(Description)

   * - CanSM.h
     - CanSM 模块头文件，通过加载该头文件访问 CanSM 公开的函数和数据类型(CanSM module header file, through which the public functions and data types of CanSM can be accessed by including this header file)

   * - CanSM_CanIf.h
     - CanSM 模块提供给 CanIf、CanNm 模块使用的函数(The CanSM module provides functions for the CanIf and CanNm modules to use)

   * - CanSM.c
     - CanSM 模块实现源文件，各 API 实现在该文件中(CanSM module implementation source file, where all API implementations are contained)

动态文件(Dynamic Files)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - 文件(File)
     - 描述(Description)

   * - CanSM_Cfg.h
     - 用于定义 CanSM 模块预编译时用到的非 PB 宏(Used to define non-PB macros used by the CanSM module during precompilation)

   * - CanSM_PBcfg.h
     - 用于定义 CanSM 模块预编译时用到的 PB 宏和数据类型定义(Used to define PB macros and data type used by the CanSM module during precompilation)

   * - CanSM_Cfg.c
     - 配置参数源文件，包含各个非 PB 配置项的定义(Configuration parameter source file, containing definitions of various non-PB configuration items)

   * - CanSM_PBcfg.c
     - 配置参数源文件，包含各个 PB 配置项的定义(Configuration parameter source file, containing definitions of various PB configuration items)

   * - CanSM_MemMap.h
     - CanSM 模块函数和变量存储位置定义文件(File for defining the storage locations of CanSM module functions and variables)


错误处理(Error Handling)
----------------------------

开发错误(Development Errors)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. list-table::
   :widths: 20 10 30
   :header-rows: 1

   * - Error code
     - Value[hex]
     - Description

   * - CANSM_E_UNINIT
     - 0x01
     - API service used without module initialization

   * - CANSM_E_PARAM_POINTER
     - 0x02
     - API service called with wrong pointer

   * - CANSM_E_INVALID_NETWORK_HANDLE
     - 0x03
     - API service called with wrong parameter

   * - CANSM_E_PARAM_CONTROLLER
     - 0x04
     - API service called with wrong parameter

   * - CANSM_E_PARAM_TRANSCEIVER
     - 0x05
     - API service called with wrong parameter

   * - CANSM_E_INVALID_PARTITION_CONTEXT
     - 0x06
     - API service called on wrong partition context

   * - CANSM_E_ALREADY_INITIALIZED
     - 0x07
     - Init API service called if CanSM is already initialized

   * - CANSM_E_NOT_IN_NO_COM
     - 0x0B
     - DeInit API service called when not all CAN networks are in state CANSM_NO_COMMUNICATION


产品错误(Product Errors)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. list-table::
   :widths: 10 20
   :header-rows: 1

   * - Error code
     - Description

   * - CANSM_E_BUS_OFF
     - The bus-off recovery state machine of a CAN network has detected a certain amount of sequential bus-offs without successful recovery


运行时错误(Runtime Errors)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. list-table::
   :widths: 20 10 30
   :header-rows: 1

   * - Error code
     - Value[hex]
     - Description

   * - CANSM_E_MODE_REQUEST_TIMEOUT
     - 0x0A
     - Mode request for a network failed more often than allowed by configuration


接口描述(Interface Description)
======================================

.. 目前能够自动生成的有类型定义，普通函数，回调函数。
.. 有些模块的API来自多个头文件，需要自行裁剪合并
.. 引用接口描述。来自于code->doxygen->xml->rst
.. include:: CanSM_h_api.rst
.. include:: CanSM_CanIf_h_api.rst

配置函数(Configuration Function)
---------------------------------------
.. 可选的章节，根据模块实际情况确定
.. 格式同提供的服务


CanSM_MainFunction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. code::

   void CanSM_MainFunction_<CanSMNetwork.ShortName>(void)

Scheduled function of the CanSM.

**Sync/Async**
   Synchronous

**Reentrancy**
   Non Reentrant

**Return type**
   void


依赖的服务(Dependent Services)
------------------------------------

强制接口(Mandatory Interfaces)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. 可选的章节，根据模块实际情况确定

.. list-table::
   :widths: 10 5 30
   :header-rows: 1

   * - API Function
     - Header File
     - Description

   * - BswM_CanSM_CurrentState
     - BswM_CanSM.h
     - Function called by CanSM to indicate its current state.

   * - CanIf_CheckTrcvWakeFlag
     - CanIf.h
     - Requests the CanIf module to check the Wake flag of the designated CAN transceiver.

   * - CanIf_ClearTrcvWufFlag
     - CanIf.h
     - Requests the CanIf module to clear the WUF flag of the designated CAN transceiver.

   * - CanIf_GetPduMode
     - CanIf.h
     - This service reports the current mode of a requested PDU channel.

   * - CanIf_GetTxConfirmationState
     - CanIf.h
     - This service reports, if any TX confirmation has been done for the whole CAN controller since thelast CAN controller start.

   * - CanIf_SetControllerMode
     - CanIf.h
     - This service calls the corresponding CAN Driver service for changing of the CAN controller mode.

   * - CanIf_SetPduMode
     - CanIf.h
     - This service sets the requested mode at the L-PDUs of a predefined logical PDU channel.

   * - CanIf_SetTrcvMode
     - CanIf.h
     - This service changes the operation mode of the tansceiver TransceiverId, via calling the corresponding CAN Transceiver Driver service.

   * - CanNm_ConfirmPnAvailability
     - CanNm.h
     - Enables the PN filter functionality on the indicated NM channel. Availability: The API is only available if CanNmGlobalPnSupport is TRUE.

   * - ComM_BusSM_ModeIndication
     - ComM.h
     - Indication of the actual bus mode by the corresponding Bus State Manager. ComM shall propagate the indicated state to the users with means of the RTE and BswM.

   * - Dem_SetEventStatus
     - Dem.h
     - Called by SW-Cs or BSW modules to report monitor status information to the Dem. BSW modules calling Dem_SetEventStatus can safely ignore the return value. This API will be available only if ({Dem/DemConfigSet/DemEventParameter/DemEventReportingType} == STANDARD_REPORTING)

   * - Det_ReportRuntimeError
     - Det.h
     - Service to report runtime errors. If a callout has been configured then this callout shall be called.

可选接口(Optional Interfaces)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. 可选的章节，根据模块实际情况确定
.. 格式同强制接口

.. list-table::
   :widths: 10 5 30
   :header-rows: 1

   * - API Function
     - Header File
     - Description

   * - CanIf_SetBaudrate
     - CanIf.h
     - This service shall set the baud rate configuration of the CAN controller. Depending on necessary baud rate modifications the controller might have to reset.

   * - Det_ReportError
     - Det.h
     - Service to report development errors.


配置接口Configuration(Interfaces)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. 可选的章节，根据模块实际情况确定
.. 格式同强制接口

.. list-table::
   :widths: 10 5 30
   :header-rows: 1

   * - API Function
     - Header File
     - Description

   * - void <User_GetBusOffDelay>(NetworkHandleType network, uint8* delayCyclesPtr)
     - Configuration parameter CanSM/CanSMGeneral/CanSMGetBusOffDelayHeader
     - This callout function returns the number of CanSM base cycles to wait additionally to L1/L2 after a BusOff occurred.


配置 configuration
===========================

因 CanSM 依赖 CanNM 接口 CanNm_ConfirmPnAvailability，所以需要确保 CanNM 在 CanSM 之前初始化，这通常是在 EcuMDriverInitListBswM 中配置的。

Since CanSM depends on the CanNM interface CanNm_ConfirmPnAvailability, CanNM must be initialized before CanSM. This is usually configured in EcuMDriverInitListBswM.

.. figure:: ../../../_static/参考手册/CanSM/EcuMDriverInitListBswM.png
   :name: EcuMDriverInitListBswM
   :align: center

   EcuMDriverInitListBswM