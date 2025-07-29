====================
TC397 Demo
====================

基本信息（Basic Information）
====================================

简介（Introduction）
--------------------------

本Demo工程集成的AUTOSAR协议栈有CAN通信、诊断、网络管理、存储、看门狗、OS。各个模块均提供了参考的配置示例，旨在指导用户快速熟悉AUTOSAR中各个协议栈的模块的基本配置以及各个模块间的关联关系。

This demo project integrates the AUTOSAR protocol stack, including CAN
communication, diagnostics, network management, storage, watchdog, and
OS. Each module provides reference configuration examples to guide users
in quickly understanding the basic configuration of modules within each
protocol stack in AUTOSAR and their interrelationships.

+---------------------------------------------+------------------------+
| **工程名（Project Name）**                  | **工程类型（Project    |
|                                             | Type）**               |
+---------------------------------------------+------------------------+
| Demo_TC397_V2504_BSW_ConfigProject          | BSW配置工程            |
|                                             |                        |
|                                             | BSW_ConfigProject      |
+---------------------------------------------+------------------------+
| Demo_TC397_V2504_HighTec_V4941_Project      | BSW集成工程            |
|                                             |                        |
|                                             | BSW IntegratedProject  |
+---------------------------------------------+------------------------+

缩略词
------

+--------------------------+-------------------------------------------+
| **缩略语（Acronyms）**   | **中文解释（Chinese explanation）**       |
+==========================+===========================================+
| UDS                      | 统一的诊断服务                            |
+--------------------------+-------------------------------------------+
| CAN                      | 控制器局域网络                            |
+--------------------------+-------------------------------------------+
| NM                       | 网络管理                                  |
+--------------------------+-------------------------------------------+
| CanIf                    | CAN接口模块                               |
+--------------------------+-------------------------------------------+
| CanSm                    | CAN状态管理模块                           |
+--------------------------+-------------------------------------------+
| ComM                     | 通信管理模块                              |
+--------------------------+-------------------------------------------+
| EcuM                     | ECU状态管理模块                           |
+--------------------------+-------------------------------------------+
| NvM                      | 非易失性存储管理                          |
+--------------------------+-------------------------------------------+
| FEE                      | Flash模拟Eep                              |
+--------------------------+-------------------------------------------+
| DCM                      | 诊断通信管理                              |
+--------------------------+-------------------------------------------+
| DEM                      | 诊断事件管理                              |
+--------------------------+-------------------------------------------+
| CANTP                    | CAN传输层                                 |
+--------------------------+-------------------------------------------+
| ComM                     | 通信管理                                  |
+--------------------------+-------------------------------------------+
| WDG                      | 看门狗                                    |
+--------------------------+-------------------------------------------+
| WdgIf                    | 看门狗接口模块                            |
+--------------------------+-------------------------------------------+
| WdgM                     | 看门狗管理模块                            |
+--------------------------+-------------------------------------------+
| E2E                      | (End-to-End)通信安全协议                  |
+--------------------------+-------------------------------------------+
| OS                       | 操作系统                                  |
+--------------------------+-------------------------------------------+

开发环境（Development environment ）
---------------------------------------

+----------------------------+----------------------------------------------+
| **工具描述（Tool           | **名称版本（Name Version）**                 |
| description）**            |                                              |
+----------------------------+----------------------------------------------+
| 编译器&IDE（Compiler&IDE） | Hightec For Tricore V4.9.4.1                 |
+----------------------------+----------------------------------------------+
| EB工具（EB tool）          | EB tresos Studio 26.2.0                      |
+----------------------------+----------------------------------------------+
| MCAL                       | MC-ISAR_AS422_TC3xx \_2.10.0                 |
+----------------------------+----------------------------------------------+
| 硬件开发板（Hardware       | Application Kit TC3X7 V2.0                   |
| development board）        |                                              |
+----------------------------+----------------------------------------------+
| 调试器（Debugger）         | Infineon DAP miniWiggler                     |
+----------------------------+----------------------------------------------+

开发环境获取（\ **Obtaining the development environment**\ ）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

上述开发环境需用户自行获取。

   Users are required to obtain the above development environment on
   their own.

BSW工程目录结构说明（Description of BSW Project Directory Structure）
============================================================================

AUTOSAR 基础软件集成工程的目录结构如下：

The directory structure of the AUTOSAR basic software integration
project is as follows：

|image1|

各文件夹释义：

Explanation of each folder：

ASW：存放应用代码，供客户添加应用代码。

ASW: Stores application code for customers to add application code.

BSW：存放BSW相关代码，包括AUTOSAR各个协议栈源代码和配置、MCAL的源代码和配置、复杂驱动的源代码和配置等。

BSW: Stores BSW-related code, including the source code and
configuration of various AUTOSAR protocol stacks, MCAL, and Complex
Device Drivers.

|image2|

CommonInclude：存放共用的头文件，比如Std_Types.h、Compiler.h、ComStack_Types.h等。

CommonInclude: Stores common header files, such as Std_Types.h,
Compiler.h, ComStack_Types.h, etc.

Communication：存放通信相关的代码，包含Can、Lin、Ethernet、FlexRay等。

Communication: Stores communication-related code, including CAN, LIN,
Ethernet, and FlexRay.

|image3|

Config：存放BSW配置相关的代码，包含BSW的配置、MCAL的配置、CDD的配置等。

Config: Stores configuration files for BSW modules, including BSW, MCAL,
and CDD configurations, etc.

|image4|

Libraries：存放CRC、E2E等通用库代码。

Libraries: Stores reusable software components such as CRC and E2E.

MCAL：存放MCAL各模块的源代码、CanTrcv、LinTrcv、EthPhy、CDD模块源代码。

MCAL: Stores the source code of each module in MCAL, as well as that of
CanTrcv, LinTrcv, EthPhy, and CDD modules.

|image5|

Memory：存放存储相关模块的源代码。

Memory: Stores source code for storage-related modules.

|image6|

SystemServices：存放系统服务相关模块的源代码。

System Services: Stores source code for modules related to system
services.

|image7|

LinkFile：存放链接文件。

LinkFile：Contains linker scripts.

|image8|

协议栈配置说明（Protocol Stack Configuration Instructions）
=================================================================

CAN通信协议栈（CAN communication protocol stack）
----------------------------------------------------

CAN通信协议栈概述（Overview of CAN Communication Protocol Stack）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

CAN通信协议栈涉及到的软件模块主要有CAN、CanIf、PduR、Com、ECUC模块，其中各个模块的主要功能如下表：

The CAN communication protocol stack encompasses the following key
software modules: CAN Driver, CAN Interface (CanIf), Protocol Data Unit
Router (PduR), Communication Manager (Com), and ECU Configuration
(ECUC). Their respective core functionalities are detailed in the
subsequent table

CAN通信栈各配置模块介绍

（Introduction to Configuration Modules of CAN Communication Stack）

+-----------------+--------------------------------------------------------------------------------------------------+
| **模块名(Module | **功能(Function)**                                                                               |
| name)**         |                                                                                                  |
+-----------------+--------------------------------------------------------------------------------------------------+
| Can             | 主要配置CAN控制器的波特率，CAN报文的收发邮箱。                                                   |
|                 |                                                                                                  |
|                 | Mainly configures the baud rate of the CAN controller and the transmit/receive mailboxes for CAN |
|                 | messages.                                                                                        |
+-----------------+--------------------------------------------------------------------------------------------------+
| CanIf           | CanIf                                                                                            |
|                 | 模块主要处理上层模块与底层驱动的之间PDU的传递，为上层模块提供统一的接口来管理不同的CAN硬件模块。 |
|                 |                                                                                                  |
|                 | The CanIf module primarily handles the transmission of PDUs between upper-level modules and      |
|                 | lower-level drivers, providing upper-level modules with a unified interface to manage different  |
|                 | CAN hardware modules.                                                                            |
+-----------------+--------------------------------------------------------------------------------------------------+
| EcuC            | 用于辅助配置工具完成配置的模块。主要提供Pdu的定义，其它模块通过关联 EcuC中Pdu，相互关联起来。    |
|                 |                                                                                                  |
|                 | This module supports the configuration tool in completing the configuration. It primarily        |
|                 | provides PDU definitions, enabling other modules to establish interconnections by referencing    |
|                 | the PDUs defined in the EcuC module.                                                             |
+-----------------+--------------------------------------------------------------------------------------------------+
| PduR            | PDU Router主要为通讯接口模块（CANIF）、传输协议模块（CAN TP、J1939                               |
|                 | TP）、诊断通讯管理模块（DCM、J1939DCM）以及通讯模块（COM、LDCOM）以及 IPDUM、SECOC等模块提供基于 |
|                 | I-PDU的路由服务。                                                                                |
|                 |                                                                                                  |
|                 | The PDU Router (PduR) primarily provides I-PDU-based routing services for communication          |
|                 | interface modules (e.g., CANIF), transport protocol modules (e.g., CAN TP, J1939 TP), diagnostic |
|                 | communication management modules (e.g., DCM, J1939DCM), communication modules (e.g., COM,        |
|                 | LDCOM), as well as modules like IPDUM and SECOC.                                                 |
+-----------------+--------------------------------------------------------------------------------------------------+
| Com             | COM模块主要提供 I-PDU和信号相关管理功能                                                          |
|                 |                                                                                                  |
|                 | The COM module primarily provides management functions related to I-PDUs (Intermediate Protocol  |
|                 | Data Units) and signals.                                                                         |
+-----------------+--------------------------------------------------------------------------------------------------+

CAN通信协议栈配置功能说明（Description of CAN Communication Protocol Stack Configuration Functions）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

CAN通信协议栈配置的发送报文说明：

Description of Transmitted Messages in CAN Communication Protocol Stack
Configuration:

+------------------------------+-----------+--------------------------------------------------------+
| **报文名(Message Name)**     | **CANID** | **说明(Description)**                                  |
+------------------------------+-----------+--------------------------------------------------------+
| CAN0_Tx_0x300_Cyclic         | 0x300     | 周期报文，周期时间：500ms                              |
|                              |           |                                                        |
|                              |           | 该报文下的信号均配有UB位                               |
|                              |           |                                                        |
|                              |           | Cyclic message transmitted every 500ms. All signals    |
|                              |           | within this message are configured with Update Bits    |
|                              |           | (UB) for validity tracking                             |
+------------------------------+-----------+--------------------------------------------------------+
| CAN0_Tx_0x301_Event          | 0x301     | 事件报文                                               |
|                              |           |                                                        |
|                              |           | Event-triggered message                                |
+------------------------------+-----------+--------------------------------------------------------+
| CAN0_Tx_0x302_Mixed          | 0x302     | 混合报文，正常周期：500ms，触发后连发3帧，周期为：50ms |
|                              |           |                                                        |
|                              |           | Mixed-type message with a nominal cycle of 500ms. When |
|                              |           | triggered, it transmits 3 consecutive frames at 50ms   |
|                              |           | intervals                                              |
+------------------------------+-----------+--------------------------------------------------------+
| CAN0_Tx_0x303_Cyclic_Counter | 0x303     | 周期报文，周期时间：500ms，带RollingCounter            |
|                              |           |                                                        |
|                              |           | Cyclic message with a period of 500ms, equipped with a |
|                              |           | Rolling Counter                                        |
+------------------------------+-----------+--------------------------------------------------------+
| CAN0_Tx_0x350_Cyclic_PN17    | 0x350     | 周期报文，周期时间：100ms                              |
|                              |           |                                                        |
|                              |           | 受PN17控制                                             |
|                              |           |                                                        |
|                              |           | Cyclic message with a period of 100ms, controlled by   |
|                              |           | PN17                                                   |
+------------------------------+-----------+--------------------------------------------------------+
| CAN0_Tx_0x351_Cyclic_PN29    | 0x351     | 周期报文，周期时间：100ms                              |
|                              |           |                                                        |
|                              |           | 受PN29控制                                             |
|                              |           |                                                        |
|                              |           | Cyclic message with a period of 100ms, controlled by   |
|                              |           | PN29                                                   |
+------------------------------+-----------+--------------------------------------------------------+
| CAN0_Tx_0x360_E2E_P01        | 0x360     | 周期报文，周期时间：100ms                              |
|                              |           |                                                        |
|                              |           | E2E报文，DATAID：0x1234                                |
|                              |           |                                                        |
|                              |           | Cyclic message with a period of 100ms. E2E-protected   |
|                              |           | message with DATAID: 0x1234                            |
+------------------------------+-----------+--------------------------------------------------------+

CAN通信协议栈配置的接收报文说明：

Description of Received Messages in CAN Communication Protocol Stack
Configuration:

+------------------------------+-----------+----------------------------------------------------------------------------+
| **报文名(Message Name)**     | **CANID** | **说明(Description)**                                                      |
+------------------------------+-----------+----------------------------------------------------------------------------+
| CAN0_Rx_0x200_Cyclic         | 0x200     | 周期报文，周期时间：500ms                                                  |
|                              |           |                                                                            |
|                              |           | 该报文下的信号均配有UB位                                                   |
|                              |           |                                                                            |
|                              |           | Cyclic message with a period of 500ms. All signals under this message are  |
|                              |           | equipped with UB bits                                                      |
+------------------------------+-----------+----------------------------------------------------------------------------+
| CAN0_Rx_0x201_Event          | 0x201     | 事件报文                                                                   |
|                              |           |                                                                            |
|                              |           | Event-triggered message                                                    |
+------------------------------+-----------+----------------------------------------------------------------------------+
| CAN0_Rx_0x202_Mixed          | 0x202     | 混合报文，正常周期：500ms，触发后连发3帧，周期为：50ms，包含信号超时2500ms |
|                              |           |                                                                            |
|                              |           | Mixed-type message with a nominal cycle of 500ms. When triggered, it       |
|                              |           | transmits 3 consecutive frames at 50ms intervals. Signal timeout: 2500ms   |
+------------------------------+-----------+----------------------------------------------------------------------------+
| CAN0_Rx_0x203_Cyclic_Counter | 0x203     | 周期报文，周期时间：500ms，带RollingCounter                                |
|                              |           |                                                                            |
|                              |           | Cyclic message with a period of 500ms, equipped with a Rolling Counter     |
+------------------------------+-----------+----------------------------------------------------------------------------+
| CAN0_Rx_0x250_Cyclic_PN17    | 0x250     | 周期报文，周期时间：100ms                                                  |
|                              |           |                                                                            |
|                              |           | 受PN17控制                                                                 |
|                              |           |                                                                            |
|                              |           | Cyclic message with a period of 100ms, controlled by PN17                  |
+------------------------------+-----------+----------------------------------------------------------------------------+
| CAN0_Rx_0x251_Cyclic_PN29    | 0x251     | 周期报文，周期时间：100ms                                                  |
|                              |           |                                                                            |
|                              |           | 受PN29控制                                                                 |
|                              |           |                                                                            |
|                              |           | Cyclic message with a period of 100ms, controlled by PN29                  |
+------------------------------+-----------+----------------------------------------------------------------------------+
| CAN0_Rx_0x260_E2E_P01        | 0x260     | 周期报文，周期时间：100ms                                                  |
|                              |           |                                                                            |
|                              |           | E2E报文，DATAID：0x1234                                                    |
|                              |           |                                                                            |
|                              |           | Cyclic message with a period of 100ms. E2E-protected message with DATAID:  |
|                              |           | 0x1234                                                                     |
+------------------------------+-----------+----------------------------------------------------------------------------+

CAN网络管理协议栈（CAN网络管理协议栈）
---------------------------------------

CAN网络管理协议栈概述（Overview of CAN Network Management Protocol Stack）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

CAN通信协议栈涉及到的软件模块主要有Can、CanIf、CanSM、EcuC、NM、CanNm、ComM模块，其中各个模块的主要功能如下表：

The software modules involved in the CAN communication protocol stack
mainly include Can, CanIf, CanSM, EcuC, NM, CanNm, and ComM. The main
functions of each module are as shown in the following table:

网络管理栈各配置模块介绍

（Introduction to Configuration Modules of Network Management Stack）

+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **模块名(Module | **功能(Function)**                                                                                                                                                         |
| name)**         |                                                                                                                                                                            |
+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Can             | 主要配置CAN控制器的波特率，CAN报文的收发邮箱。                                                                                                                             |
|                 |                                                                                                                                                                            |
|                 | Mainly configures the baud rate of the CAN controller and the transmit/receive mailboxes for CAN messages.                                                                 |
+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| CanIf           | CanIf模块主要处理上层模块与底层驱动的之间PDU的传递，为上层模块提供统一的接口来管理不同的CAN 硬件模块。                                                                     |
|                 |                                                                                                                                                                            |
|                 | The CanIf module primarily handles the transfer of PDUs between upper-layer modules and lower-layer drivers, and provides a unified interface for upper-layer modules to   |
|                 | manage different CAN hardware modules.                                                                                                                                     |
+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| EcuC            | 用于辅助配置工具完成配置的模块。主要提供Pdu的定义，其它模块通过关联 EcuC中Pdu，相互关联起来。                                                                              |
|                 |                                                                                                                                                                            |
|                 | A module that supports configuration tools in completing configurations. It primarily provides PDU definitions, and other modules are interconnected by associating with   |
|                 | PDUs in EcuC.                                                                                                                                                              |
+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| NM              | Nm模块主要包含两个功能：Nm模块是ComM与CanNm之间的适配层；网络管理协调功能，协调不同总线channel的ECU节点实现网络的同步睡眠。                                                |
|                 |                                                                                                                                                                            |
|                 | The Nm module primarily encompasses two functions: it acts as the adaptation layer between ComM and CanNm; and it provides network management coordination functionality,  |
|                 | which coordinates ECU nodes across different bus channels to achieve synchronous network sleep.                                                                            |
+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ComM            | ComM模块封装了控制底层的通信服务。通信管理模块从通信请求者那里收集总线通信访问请求，并协调这些请求，主要目的是：为每个Channel设置一个状态机控制一个ECU的多个通信总线通道。 |
|                 |                                                                                                                                                                            |
|                 | The ComM module encapsulates the underlying communication services. It collects bus communication access requests from communication requesters, coordinates these         |
|                 | requests, and its primary purpose is to set up a state machine for each Channel to control multiple communication bus channels of an ECU.                                  |
+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| CanSM           | 主要功能是与通信硬件抽象层和系统服务层产生交互，为每一个CAN通信总线定义一个总线相关的状态管理，并为相关的总线提供流控制。                                                  |
|                 |                                                                                                                                                                            |
|                 | The CanSM's primary function is to interact with the Communication Hardware Abstraction Layer and the System Service Layer, implement a bus specific state manager for     |
|                 | each CAN communication bus, and provide flow control for the associated buses.                                                                                             |
+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| CanNM           | 负责实现ECU的状态切换。比如何时进入睡眠、是否保持正常的网络状态等。                                                                                                        |
|                 |                                                                                                                                                                            |
|                 | Responsible for implementing the state transitions of the ECU. For example, when to enter bus sleep mode and whether to maintain a normal communication state.             |
+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

CAN网络管理协议栈配置说明（CAN Network Management Protocol Stack Configuration Specification）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

CAN网络管理的接收报文ID范围为0x500-0x5ff,

CAN网络管理的发送报文ID为0x501

CanNM的主要配置参数如下表所示：

The receive message ID range for CAN network management is 0x500-0x5ff,

The transmit message ID for CAN network management is 0x501

The main configuration parameters of CanNM are as shown in the following
table:

+--------------------------------------+---------------------------------+
| 配置项（Configuration item）         | 配置参数（Configuration         |
|                                      | parameters）                    |
+--------------------------------------+---------------------------------+
| CanNmGlobalPnSupport                 | TRUE                            |
+--------------------------------------+---------------------------------+
| CanNmComUserDataSupport              | TRUE                            |
+--------------------------------------+---------------------------------+
| CanNmMainFunctionPeriod              | 0.005                           |
+--------------------------------------+---------------------------------+
| CanNmPassiveModeEnabled              | FALSE                           |
+--------------------------------------+---------------------------------+
| CanNmPnEiraCalcEnabled               | TRUE                            |
+--------------------------------------+---------------------------------+
| CanNmPnResetTime                     | 2.5S                            |
+--------------------------------------+---------------------------------+
| CanNmActiveWakeupBitEnabled          | TRUE                            |
+--------------------------------------+---------------------------------+
| CanNmCarWakeUpRxEnabled              | FALSE                           |
+--------------------------------------+---------------------------------+
| CanNmImmediateNmCycleTime            | 0.02S                           |
+--------------------------------------+---------------------------------+
| CanNmImmediateNmTransmissions        | 10                              |
+--------------------------------------+---------------------------------+
| CanNmMsgCycleOffset                  | 0.0                             |
+--------------------------------------+---------------------------------+
| CanNmMsgCycleTime                    | 1.0S                            |
+--------------------------------------+---------------------------------+
| CanNmMsgTimeoutTime                  | 0.001S                          |
+--------------------------------------+---------------------------------+
| CanNmNodeId                          | 1                               |
+--------------------------------------+---------------------------------+
| CanNmPduCbvPosition                  | CANNM_PDU_BYTE_1                |
+--------------------------------------+---------------------------------+
| CanNmPduNidPosition                  | CANNM_PDU_BYTE_0                |
+--------------------------------------+---------------------------------+
| CanNmPnEnabled                       | TRUE                            |
+--------------------------------------+---------------------------------+
| CanNmPnHandleMultipleNetworkRequests | FALSE                           |
+--------------------------------------+---------------------------------+
| CanNmRepeatMessageTime               | 3S                              |
+--------------------------------------+---------------------------------+
| CanNmRetryFirstMessageRequest        | FALSE                           |
+--------------------------------------+---------------------------------+
| CanNmTimeoutTime                     | 3.0S                            |
+--------------------------------------+---------------------------------+
| CanNmWaitBusSleepTime                | 1.5S                            |
+--------------------------------------+---------------------------------+
| CanSMBorCounterL1ToL2                | 10                              |
+--------------------------------------+---------------------------------+
| CanSMBorTimeL1                       | 0.1S                            |
+--------------------------------------+---------------------------------+
| CanSMBorTimeL2                       | 1.0S                            |
+--------------------------------------+---------------------------------+
| CanSMBorTimeTxEnsured                | FALSE                           |
+--------------------------------------+---------------------------------+
| CanSMEnableBusOffDelay               | FALSE                           |
+--------------------------------------+---------------------------------+

CAN网络管理协议栈休眠唤醒说明（CAN Network Management Protocol Stack Sleep and Wakeup Specification）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

设置唤醒源主要包含两个为远程唤醒和本地唤醒

Setting the wakeup sources primarily includes two types: remote wakeup
and local wakeup

+-----------------------------------+----------------------------------------+
| 唤醒源(wakeup sources)            | 说明(Description)                      |
+-----------------------------------+----------------------------------------+
| EcuMWakeupSource_CAN              | 被动唤醒，需要检测总线上是否为网管报文 |
|                                   |                                        |
|                                   | Passive wakeup, which requires         |
|                                   | detecting whether the message on the   |
|                                   | bus is a network management message.   |
+-----------------------------------+----------------------------------------+
| EcuMWakeupSource_Local            | 主动唤醒，用户请求后就会立即请求网络   |
|                                   |                                        |
|                                   | Active wakeup, which will immediately  |
|                                   | request the network upon user request. |
+-----------------------------------+----------------------------------------+

在开发板上，ECU一上电主动请求网络，释放网络后ECU休眠时直接调用Mcu_PerformReset进行复位。

On the development board, once powered on, the ECU actively requests
network connectivity. After releasing the network, when the ECU enters
sleep mode, it directly invokes Mcu_PerformReset to perform a reset.

CAN诊断协议栈（CAN diagnostic protocol stack）
-------------------------------------------------

CAN诊断协议栈概述（Overview of CAN Diagnostic Protocol Stack）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


CAN诊断协议栈涉及到的软件模块主要有Can、CanIf、CanTP、EcuC、DCM、DEM模块，其中各个模块的主要功能如下表：

The software modules involved in the CAN diagnostic protocol stack
mainly include Can, CanIf, CanTP, EcuC, DCM, and DEM. The main functions
of each module are as shown in the following table：

诊断栈各配置模块介绍

(Introduction to Each Configuration Module of the Diagnostic Stack)

+---------------------+------------------------------------------------------------------------------------------------------------------+
| 模块名(Module name) | 功能(Function)                                                                                                   |
+---------------------+------------------------------------------------------------------------------------------------------------------+
| Can                 | 主要配置CAN控制器的波特率，CAN报文的收发邮箱。                                                                   |
|                     |                                                                                                                  |
|                     | Mainly configures the baud rate of the CAN controller and the transmit/receive mailboxes for CAN messages.       |
+---------------------+------------------------------------------------------------------------------------------------------------------+
| CanIf               | CanIf模块主要处理上层模块与底层驱动的之间PDU的传递，为上层模块提供统一的接口来管理不同的CAN硬件模块。            |
|                     |                                                                                                                  |
|                     | The CanIf module primarily handles the transfer of PDUs between upper-layer modules and lower-layer drivers, and |
|                     | provides a unified interface for upper-layer modules to manage different CAN hardware modules.                   |
+---------------------+------------------------------------------------------------------------------------------------------------------+
| EcuC                | 用于辅助配置工具完成配置的模块。主要提供Pdu的定义，其它模块通过关联EcuC中Pdu，相互关联起来。                     |
|                     |                                                                                                                  |
|                     | A module that supports configuration tools in completing configurations. It primarily provides PDU definitions,  |
|                     | and other modules are interconnected by associating with PDUs in EcuC.                                           |
+---------------------+------------------------------------------------------------------------------------------------------------------+
| PduR                | PDU Router主要为通讯接口模块（CANIF）、传输协议模块（CAN TP、J1939                                               |
|                     | TP）、诊断通讯管理模块（DCM、J1939DCM）以及通讯模块（COM、LDCOM）以及IPDUM、SECOC等模块提供基于I-PDU的路由服务。 |
|                     |                                                                                                                  |
|                     | The PDU Router primarily provides I-PDU-based routing services for communication interface modules (CANIF),      |
|                     | transport protocol modules (CAN TP, J1939 TP), diagnostic communication management modules (DCM, J1939DCM),      |
|                     | communication modules (COM, LDCOM), as well as modules such as IPDUM and SECOC.                                  |
+---------------------+------------------------------------------------------------------------------------------------------------------+
| CanTp               | CANTP模块实现依据ISO15765-2 标准规范中定义的CAN总线数据在传输层的数据接收发送功能。                              |
|                     |                                                                                                                  |
|                     | The CANTp module implements the data reception and transmission functions at the transport layer for CAN bus     |
|                     | communication as specified in ISO 15765-2.                                                                       |
+---------------------+------------------------------------------------------------------------------------------------------------------+
| Dcm                 | 依据ISO15765-3和ISO14229-1标准描述，实现诊断请求报文的解析，响应(正响应和负响应)与执行。                         |
|                     |                                                                                                                  |
|                     | In compliance with ISO 15765-3 and ISO 14229-1, the implementation enables parsing of diagnostic requests,       |
|                     | generation of positive/negative responses, and execution of corresponding services.                              |
+---------------------+------------------------------------------------------------------------------------------------------------------+
| Dem                 | 实现诊断故障的存储与管理功能，提供API接口供其他模块读取DTC和对应的冻结帧数据和扩展数据。                         |
|                     |                                                                                                                  |
|                     | Implements diagnostic fault storage and management functions, providing APIs for other modules to read DTCs,     |
|                     | corresponding freeze frame data, and extended data.                                                              |
+---------------------+------------------------------------------------------------------------------------------------------------------+

CAN诊断协议栈配置说明（CAN Diagnostic Protocol Stack Configuration Instructions）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

CAN诊断协议栈的CANID如下表：

The CAN IDs for the CAN diagnostic protocol stack are listed in the
following table:

+------------------------------------+---------------------------------+
| CANID类型(CANID Type)              | CANID                           |
+------------------------------------+---------------------------------+
| 物理寻址Physical Request CAN ID    | 0x708                           |
+------------------------------------+---------------------------------+
| 功能寻址Functional Request CAN ID  | 0x7DF                           |
+------------------------------------+---------------------------------+
| 物理响应Physical Response CAN ID   | 0x709                           |
+------------------------------------+---------------------------------+

Demo工程中配置的诊断服务有如下表所示：

The diagnostic services configured in the demo project are as shown in
the following table:

|image9|

CAN诊断时间参数如下：

The CAN diagnostic timing parameters are as follows:

+------------------+----------------------------+-------------------+---------------------+-------------------+
| **Application Layer Timing Parameters**                                                                     |
|                                                                                                             |
| **应用层会话管理计时器参数**                                                                                |
+------------------+----------------------------+-------------------+---------------------+-------------------+
|                  | **Symbol**                 | **Min**           | **Max/Timeout**     | **Unit**          |
|                  |                            |                   |                     |                   |
|                  | **符号**                   | **最小值**        | **最大值/超时时间** | **单位**          |
+------------------+----------------------------+-------------------+---------------------+-------------------+
| **ECU            | P2\ :sub:`Server`          | N/A               | 50                  | ms                |
| 电控单元(ECU     |                            |                   |                     |                   |
| Electronic       |                            |                   |                     |                   |
| Control Unit)**  |                            |                   |                     |                   |
|                  +----------------------------+-------------------+---------------------+-------------------+
|                  | P2\*\ :sub:`Server`        | N/A               | 5000                | ms                |
|                  +----------------------------+-------------------+---------------------+-------------------+
|                  | S3\ :sub:`Server`          | N/A               | 5000                | ms                |
+------------------+----------------------------+-------------------+---------------------+-------------------+
|                                                                                                             |
+-------------------------------------------------------------------------------------------------------------+
| **Network Layer Timing Parameters**                                                                         |
|                                                                                                             |
| **网络层定时器参数**                                                                                        |
+------------------+----------------------------+-------------------+---------------------+-------------------+
|                  | **Symbol**                 | **Timeout**       | **Performance       | **Unit**          |
|                  |                            |                   | Requirement**       |                   |
|                  | **符号**                   | **超时时间**      |                     | **单位**          |
|                  |                            |                   | **性能要求**        |                   |
+------------------+----------------------------+-------------------+---------------------+-------------------+
| **ECU            | N_As/N_Ar                  | 70                | ——                  | ms                |
| 电控单元(ECU     |                            |                   |                     |                   |
| Electronic       |                            |                   |                     |                   |
| Control Unit)**  |                            |                   |                     |                   |
|                  +----------------------------+-------------------+---------------------+-------------------+
|                  | N_Bs                       | 150               | ——                  | ms                |
|                  +----------------------------+-------------------+---------------------+-------------------+
|                  | N_Br                       | ——                | < 70                | ms                |
|                  +----------------------------+-------------------+---------------------+-------------------+
|                  | N_Cs                       | ——                | < 150               | ms                |
|                  +----------------------------+-------------------+---------------------+-------------------+
|                  | N_Cr                       | 150               | ——                  | ms                |
+------------------+----------------------------+-------------------+---------------------+-------------------+
|                  |                            |                   |                     |                   |
+------------------+----------------------------+-------------------+---------------------+-------------------+
| **Other parameters**                                                                                        |
|                                                                                                             |
| **其它参数**                                                                                                |
+------------------+----------------------------+-------------------+---------------------+-------------------+
|                  | **Symbol**                 | **Parameter**     | **Value**           | **Unit**          |
|                  |                            |                   |                     |                   |
|                  | **符号**                   | **参数**          | **值**              | **单位**          |
+------------------+----------------------------+-------------------+---------------------+-------------------+
| **ECU电控单元    | BS                         | Block Size        | 0                   | ——                |
| (ECU Electronic  |                            |                   |                     |                   |
| Control Unit)**  |                            |                   |                     |                   |
|                  +----------------------------+-------------------+---------------------+-------------------+
|                  | STmin                      | Minimum           | 10                  | ms                |
|                  |                            | Separation Time   |                     |                   |
|                  +----------------------------+-------------------+---------------------+-------------------+
|                  | Fill bytes(发送数据填充)   | Padding           | 0xAA                | ——                |
|                  +----------------------------+-------------------+---------------------+-------------------+
|                  | 接收填充值检查(Reception   | ON/OFF            | OFF                 | ——                |
|                  | stuffing value check)      |                   |                     |                   |
|                  +----------------------------+-------------------+---------------------+-------------------+
|                  | Fill bytes(接收数据填充)   | Padding           | ——                  | ——                |
|                  +----------------------------+-------------------+---------------------+-------------------+
|                  | 诊断报文长度               | Byze Size         | 8                   | ——                |
|                  | (Diagnostic message        |                   |                     |                   |
|                  | length)                    |                   |                     |                   |
|                  +----------------------------+-------------------+---------------------+-------------------+
|                  | 诊断报文长度检查           | ON/OFF            | ON                  | ——                |
|                  | (Diagnostic message length |                   |                     |                   |
|                  | check)                     |                   |                     |                   |
|                  +----------------------------+-------------------+---------------------+-------------------+
|                  | DCM接收BUFFER最大值Maximum | Byze Size         | 1024                | ——                |
|                  | size of DCM receiving      |                   |                     |                   |
|                  | buffer                     |                   |                     |                   |
|                  +----------------------------+-------------------+---------------------+-------------------+
|                  | DCM发送BUFFER最大值Maximum | Byze Size         | 1024                | ——                |
|                  | size of DCM transmitting   |                   |                     |                   |
|                  | buffer                     |                   |                     |                   |
|                  +----------------------------+-------------------+---------------------+-------------------+
|                  | TP半双工(TP Half-Duplex)                                                                 |
+------------------+------------------------------------------------------------------------------------------+

安

安全访问算法配置信息如下：

Configuration information of the security access algorithm is as
follows:

   Mask配置值（Mask Configuration Value）

+-----------------------------------------------------------------------+
| Mask = 0x5555AAAAu                                                    |
+-----------------------------------------------------------------------+

密钥算法（根据Seed计算Key）如下，其中seed为输入的种子。

The key algorithm (calculating the key based on the seed) is as follows,
where 'seed' refers to the input seed.

   安全算法（Security Algorithm）

+-----------------------------------------------------------------------+
| Key = Seed & Mask                                                     |
+-----------------------------------------------------------------------+

.. note::
   最大失败次数为3，达到最大失败次数启动延时时间为10S；连续请求种子错误计数不加1，种子相同，延时时间过后错误计数清零。

   Note: The maximum number of failed attempts is 3; once this limit is
   reached, a 10-second delay is triggered. Consecutive invalid seed
   requests do not increment the error count. If the seed remains
   unchanged, the error count will reset to zero after the delay period
   expires.

DID列表(DID List)：

|image10|

IO DID列表（IO DID List）：

|image11|

RID列表（RID List）：

|image12|

DTC列表（DTC List）：

|image13|

.. note::
   DTC格式：01，ISO 14229；DTC status支持的bit位仅bit7不支持，0x7F；
   DTC format: 01, ISO 14229; DTC status supports all bits except bit 7 (mask: 0x7F);


DTC扩展数据（DTC Extended Data）：

|image14|

DTC快照（DTC Snapshot）：

|image15|

存储协议栈（Memory）
-----------------------

存储协议栈概述（Overview of Memory）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

存储协议栈涉及到的软件模块主要有Flash、FEE、NvM模块，其中各个模块的主要功能如下表：

The software modules involved in the Memory mainly include Flash, FEE,
and NvM modules. The main functions of each module are listed in the
following table:

NvM 各配置模块介绍

(Introduction to each configuration module of NvM)

+-----------------+-------------------------------------------------------------+
| **模块名(Module | **功能(Function)**                                          |
| name)**         |                                                             |
+-----------------+-------------------------------------------------------------+
| Flash           | 提供对Flash的读，写，擦相关操作服务。                       |
|                 |                                                             |
|                 | Provides read, write, and erase services for Flash memory.  |
+-----------------+-------------------------------------------------------------+
| FEE             | 为上层提供虚拟线性地址空间和统一的存储分配方案。            |
|                 |                                                             |
|                 | Provides a virtual linear address space and a unified       |
|                 | memory allocation scheme for upper layers.                  |
+-----------------+-------------------------------------------------------------+
| NvM             | 非易失性数据的存储和管理。                                  |
|                 |                                                             |
|                 | Storage and management of non-volatile data.                |
+-----------------+-------------------------------------------------------------+

存储协议栈配置说明（Memory configuration instructions）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


存储协议栈中主要配置了如下NvMBlock:

The following NvMblocks are mainly configured in the Memory:

+-----------------------------------+---------------------------------------+
| **NvMBlock名(NvMBlock Name)**     | **作用(Function)**                    |
+-----------------------------------+---------------------------------------+
| NvMBlock_ConfigID                 | NvM管理                               |
|                                   |                                       |
|                                   | NvM Management                        |
+-----------------------------------+---------------------------------------+
| NvMBlock_Dem_Data                 | 用来存放Dem的数据                     |
|                                   |                                       |
|                                   | Used to store Dem data                |
+-----------------------------------+---------------------------------------+
| NvMBlock_Dem_Status               | 用来存放Dem的状态                     |
|                                   |                                       |
|                                   | Used to store Dem status              |
+-----------------------------------+---------------------------------------+
| NvMBlock_Dcm                      | 用来存放Dcm的数据（暂未使用）         |
|                                   |                                       |
|                                   | Used to store Dcm data (not used yet) |
+-----------------------------------+---------------------------------------+
| NvMBlock_SecurityLevel01          | 用来存放安全等级1错误计数（暂未使用） |
|                                   |                                       |
|                                   | Used to store Security Level 1 error  |
|                                   | count (not used yet)                  |
+-----------------------------------+---------------------------------------+
| NvMBlock_SecurityLevel02          | 用来存放安全等级2错误计数（暂未使用） |
|                                   |                                       |
|                                   | Used to store Security Level 2 error  |
|                                   | count (not used yet)                  |
+-----------------------------------+---------------------------------------+
| NvMBlock_Did_0xF190               | 用来存放DID 0xF190的数据              |
|                                   |                                       |
|                                   | Used to store data for DID 0xF190     |
+-----------------------------------+---------------------------------------+
| NvMBlock_Did_0xF183               | 用来存放DID 0xF183的数据              |
|                                   |                                       |
|                                   | Used to store data for DID 0xF183     |
+-----------------------------------+---------------------------------------+

看门狗协议栈（Watchdog Protocol Stack）
-------------------------------------------

看门狗协议栈概述（Overview of the Watchdog Protocol Stack）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

看门狗协议栈是一种用于监控和保护系统运行状态的机制。它通过监控软件执行的稳定性和正确性确保了在系统发生故障时能迅速采取恢复措施。

The watchdog stack is a mechanism used to monitor and protect the
system's operating state. It ensures that recovery measures can be
quickly taken in the event of a system failure by monitoring the
stability and correctness of software execution.

Wdg协议栈主要涉及到的模块为Wdg、WdgIf 、WdgM
，其中各个模块的主要功能如下表：

The modules primarily involved in the Wdg Protocol Stack are Wdg, WdgIf,
and WdgM. The main functions of each module are listed in the following
table:

Wdg 看门狗协议栈各配置模块介绍

(Introduction to Each Configuration Module of the Wdg Protocol Stack)

+------------------+-------------------------------------------------------------------------------------------------+
| **模块名（Module | **功能（Function）**                                                                            |
| name）**         |                                                                                                 |
+------------------+-------------------------------------------------------------------------------------------------+
| Wdg              | Wdg 属于MCAL的一部分，用于完成看门狗初始化，模式设置以及喂狗设置等。                            |
|                  |                                                                                                 |
|                  | Wdg is part of MCAL, responsible for watchdog initialization, mode configuration, and watchdog  |
|                  | feeding setup.                                                                                  |
+------------------+-------------------------------------------------------------------------------------------------+
| WdgIf            | WdgIf                                                                                           |
|                  | 模块属于ECU抽象层，能够允许上层WdgM模块来同时处理多个看门狗实体，比如外部看门狗或者内部看门狗。 |
|                  |                                                                                                 |
|                  | The WdgIf module belongs to the ECU Abstraction Layer, enabling the upper-layer WdgM module to  |
|                  | handle multiple watchdog entities simultaneously, such as external watchdogs or internal        |
|                  | watchdogs.                                                                                      |
+------------------+-------------------------------------------------------------------------------------------------+
| WdgM             | WdgM 模块从硬件看门狗实体监控的过程抽象出来完成软件程序执行监控抽象。                           |
|                  |                                                                                                 |
|                  | The WdgM module abstracts the monitoring process of hardware watchdog entities to implement     |
|                  | software execution monitoring abstraction.                                                      |
+------------------+-------------------------------------------------------------------------------------------------+

看门狗协议栈配置说明（Watchdog Protocol Stack Configuration Instructions）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

看门狗协议栈中配置了一个Alive supervision用于监控定期软件的时间。

An Alive Supervision is configured in the Watchdog Protocol Stack to
monitor the timing of periodic software.

Alive监控参数配置

(Alive Supervision Parameter Configuration)

+----------------+-----------------------------------------------+------------------+--------------+------------+----------------+----------------+----------------+--------------+--------------+
| **监控类型**   | **描述(Description)**                         | **监控实体个数** | **监控点个数 | **参考周期 | **监控失败门限 | **监控失效门限 | **期望执行次数 | **次数上偏差 | **次数下偏差 |
|                |                                               |                  | (Number of   | (Reference | (Supervision   | (Supervision   | (Expected      | (Upper       | (Lower       |
| **(Supervision |                                               | **(Number of     | Supervision  | Cycle      | Failure        | Disable        | Execution      | Deviation of | Deviation of |
| Type)**        |                                               | Supervised       | Points)**    | Time)**    | Threshold)**   | Threshold)**   | Count)**       | Count)**     | Count)**     |
|                |                                               | EntitieS)**      |              |            |                |                |                |              |              |
+----------------+-----------------------------------------------+------------------+--------------+------------+----------------+----------------+----------------+--------------+--------------+
| Alive 监控     | 监控一次mainfunction周期alive监控点执行的次数 | 1                | 1            | 1          | 0              | 0              | 1              | 0            | 0            |
| Alive          | Monitors the execution count of the alive     |                  |              |            |                |                |                |              |              |
| Supervision    | supervision point within one mainfunction     |                  |              |            |                |                |                |              |              |
|                | cycle                                         |                  |              |            |                |                |                |              |              |
+----------------+-----------------------------------------------+------------------+--------------+------------+----------------+----------------+----------------+--------------+--------------+

OS协议栈（OS Protocol Stack）
---------------------------------

OS协议栈概述（Overview of OS Protocol Stack）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

AUTOSAR
OS主要负责任务管理和中断管理功能；实现包括以下模块:Task、Isr、Countor、Alarm、ScheduleTable、Event、Resource等。

The AUTOSAR OS is primarily responsible for task management and
interrupt management functions. It includes the following modules: Task,
Isr (Interrupt Service Routine), Counter, Alarm, ScheduleTable, Event,
Resource, etc.

OS协议栈配置说明（OS protocol stack configuration instructions）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

OsTask配置（OsTask Configuration）

+--------------------------------+--------------+----------------+--------------+---------------------+----------+
| **Name**                       | **Priority** | **Stack        | **Preemptive | **OsTaskAutostart** | **Core** |
|                                |              | Size[4Bytes]** | Poilcy**     |                     |          |
+--------------------------------+--------------+----------------+--------------+---------------------+----------+
| iSoft_Auto_OsTask_10ms_BSW     | 25           | 256            | FULL         | False               | 0        |
+--------------------------------+--------------+----------------+--------------+---------------------+----------+
| iSoft_Auto_OsTask_5ms_BSW      | 25           | 256            | FULL         | False               | 0        |
+--------------------------------+--------------+----------------+--------------+---------------------+----------+
| iSoft_Auto_OsTask_1ms_BSW      | 25           | 256            | FULL         | False               | 0        |
+--------------------------------+--------------+----------------+--------------+---------------------+----------+
| iSoft_Auto_DEFAULT_OsTask_Init | 63           | 1024           | NON          | True                | 0        |
+--------------------------------+--------------+----------------+--------------+---------------------+----------+
| iSoft_Auto_OsTask_100ms        | 1            | 256            | FULL         | False               | 0        |
+--------------------------------+--------------+----------------+--------------+---------------------+----------+
| OsTask_100ms_c1                | 1            | 256            | FULL         | False               | 1        |
+--------------------------------+--------------+----------------+--------------+---------------------+----------+
| OsTask_100ms_c2                | 1            | 256            | FULL         | False               | 2        |
+--------------------------------+--------------+----------------+--------------+---------------------+----------+
| OsTask_100ms_c3                | 1            | 256            | FULL         | False               | 3        |
+--------------------------------+--------------+----------------+--------------+---------------------+----------+
| OsTask_100ms_c4                | 1            | 256            | FULL         | False               | 4        |
+--------------------------------+--------------+----------------+--------------+---------------------+----------+
| OsTask_100ms_c5                | 1            | 256            | FULL         | False               | 5        |
+--------------------------------+--------------+----------------+--------------+---------------------+----------+

OsIsr配置（OsIsr Configuration）

+-------------+--------------+----------------+--------------+----------+----------+
| **Name**    | **Category** | **Stack        | **Priority** | **Nested | **Core** |
|             |              | Size[4Bytes]** |              | Enable** |          |
+-------------+--------------+----------------+--------------+----------+----------+
| CAN0_INT0   | GATEGORY_2   | 512            | 18           | False    | 0        |
+-------------+--------------+----------------+--------------+----------+----------+
| CAN0_INT1   | GATEGORY_2   | 512            | 19           | False    | 0        |
+-------------+--------------+----------------+--------------+----------+----------+
| CAN0_INT2   | GATEGORY_2   | 512            | 20           | False    | 0        |
+-------------+--------------+----------------+--------------+----------+----------+
| CAN0_INT3   | GATEGORY_2   | 512            | 21           | False    | 0        |
+-------------+--------------+----------------+--------------+----------+----------+
| CAN0_INT4   | GATEGORY_2   | 128            | 22           | False    | 0        |
+-------------+--------------+----------------+--------------+----------+----------+
| CAN0_INT5   | GATEGORY_2   | 128            | 23           | False    | 0        |
+-------------+--------------+----------------+--------------+----------+----------+
| CAN0_INT6   | GATEGORY_2   | 128            | 24           | False    | 0        |
+-------------+--------------+----------------+--------------+----------+----------+
| CAN0_INT7   | GATEGORY_2   | 128            | 25           | False    | 0        |
+-------------+--------------+----------------+--------------+----------+----------+
| GTM_TOM0_0  | GATEGORY_2   | 128            | 8            | False    | 0        |
+-------------+--------------+----------------+--------------+----------+----------+
| GTM_TIM1_5  | GATEGORY_2   | 128            | 33           | False    | 0        |
+-------------+--------------+----------------+--------------+----------+----------+

OsAlarm配置（OsAlarm Configuration）

+-----------------------------+-------------------------+----------------+------------+------------+------------+------+----------+
| **Name**                    | **Set Event**                            | **Set Event Task**                   | **Core**        |
+-----------------------------+------------------------------------------+--------------------------------------+-----------------+
| iSoft_Auto_OsAlarm_10ms_BSW | iSoft_Auto_OsEvent_10ms_BSW              | iSoft_Auto_OsTask_10ms_BSW           | 0               |
+-----------------------------+------------------------------------------+--------------------------------------+-----------------+
| iSoft_Auto_OsAlarm_5ms_BSW  | iSoft_Auto_OsEvent_5ms_BSW               | iSoft_Auto_OsTask_5ms_BSW            | 0               |
+-----------------------------+------------------------------------------+--------------------------------------+-----------------+
| iSoft_Auto_OsAlarm_1ms_BSW  | iSoft_Auto_OsEvent_1ms_BSW               | iSoft_Auto_OsTask_1ms_BSW            | 0               |
+-----------------------------+-------------------------+----------------+------------+------------+------------+------+----------+
| **Name**                    | **Activate Task**       | **OsAlarmAutostart**        | **Start    | **Cycle Time**    | **Core** |
|                             |                         |                             | Time**     |                   |          |
+-----------------------------+-------------------------+-----------------------------+------------+-------------------+----------+
| iSoft_Auto_OsAlarm_100ms    | iSoft_Auto_OsTask_100ms | True                        | 100        | 100               | 0        |
+-----------------------------+-------------------------+-----------------------------+------------+-------------------+----------+
| OsAlarm_100ms_c1            | OsTask_100ms_c1         | True                        | 0          | 100               | 1        |
+-----------------------------+-------------------------+-----------------------------+------------+-------------------+----------+
| OsAlarm_100ms_c2            | OsTask_100ms_c2         | True                        | 0          | 100               | 2        |
+-----------------------------+-------------------------+-----------------------------+------------+-------------------+----------+
| OsAlarm_100ms_c3            | OsTask_100ms_c3         | True                        | 0          | 100               | 3        |
+-----------------------------+-------------------------+-----------------------------+------------+-------------------+----------+
| OsAlarm_100ms_c4            | OsTask_100ms_c4         | True                        | 0          | 100               | 4        |
+-----------------------------+-------------------------+-----------------------------+------------+-------------------+----------+
| OsAlarm_100ms_c5            | OsTask_100ms_c5         | True                        | 0          | 100               | 5        |
+-----------------------------+-------------------------+-----------------------------+------------+-------------------+----------+

工程验证（Project Verification）
======================================

编译及下载（Compile and Download）
--------------------------------------

将BSW工程导入IDE后点击Build Project即可编译工程。

After importing the BSW project into the IDE, click 'Build Project' to
compile the project.

|image16|

编译通过后点击Debug下载工程。（根据使用的调试器配置）

After the compilation passes, click Debug to download the project.
(According to the configured debugger in use)

|image17|


OS任务（OS Task）
-------------------

工程中执行的OS任务在

Demo_TC397_V2504_HighTec_V4941_Project
\\BSW\\Config\\BSW_Config\\RTE\\SchM路径下的Rte.c文件中，用户可以自行在相关的任务中添加自己需要实现的功能。

The OS tasks executed in the project are located in the Rte.c file in
the following
path:Demo_TC397_V2504_HighTec_V4941_Project\\BSW\\Config\\BSW_Config\\RTE\\SchM,
Users can add their own required functions to the relevant tasks.

|image18|


工程运行验证（Engineering Operational Validation）
------------------------------------------------------


正确连接开发板并成功下载运行后，使用通信测试验证工具接收板子发出的报文，可以收到如下报文。

After properly connecting the development board and successfully
downloading and running [the project], use the communication test and
verification tool to receive the messages sent by the board, The
following messages are expected.

|image19|

.. |image1| image:: /_static/工程说明/小满TC397示例工程说明（中英文修改版0718）/image1.png
   :width: 5.78568in
   :height: 2.53428in
.. |image2| image:: /_static/工程说明/小满TC397示例工程说明（中英文修改版0718）/image2.png
   :width: 5.77794in
   :height: 2.0483in
.. |image3| image:: /_static/工程说明/小满TC397示例工程说明（中英文修改版0718）/image3.png
   :width: 5.49716in
   :height: 0.85396in
.. |image4| image:: /_static/工程说明/小满TC397示例工程说明（中英文修改版0718）/image4.png
   :width: 5.57044in
   :height: 0.78933in
.. |image5| image:: /_static/工程说明/小满TC397示例工程说明（中英文修改版0718）/image5.png
   :width: 5.56434in
   :height: 3.96572in
.. |image6| image:: /_static/工程说明/小满TC397示例工程说明（中英文修改版0718）/image6.png
   :width: 5.3282in
   :height: 0.86762in
.. |image7| image:: /_static/工程说明/小满TC397示例工程说明（中英文修改版0718）/image7.png
   :width: 5.33763in
   :height: 1.96725in
.. |image8| image:: /_static/工程说明/小满TC397示例工程说明（中英文修改版0718）/image8.png
   :width: 5.3788in
   :height: 1.22908in
.. |image9| image:: /_static/工程说明/小满TC397示例工程说明（中英文修改版0718）/image9.png
   :width: 6.74167in
   :height: 7.26667in
.. |image10| image:: /_static/工程说明/小满TC397示例工程说明（中英文修改版0718）/image10.png
   :width: 6.59167in
   :height: 3.96806in
.. |image11| image:: /_static/工程说明/小满TC397示例工程说明（中英文修改版0718）/image11.png
   :width: 6.64097in
   :height: 2.79097in
.. |image12| image:: /_static/工程说明/小满TC397示例工程说明（中英文修改版0718）/image12.png
   :width: 6.69722in
   :height: 1.58472in
.. |image13| image:: /_static/工程说明/小满TC397示例工程说明（中英文修改版0718）/image13.png
   :width: 6.77222in
   :height: 3.52917in
.. |image14| image:: /_static/工程说明/小满TC397示例工程说明（中英文修改版0718）/image14.png
   :width: 7.25833in
   :height: 1.36111in
.. |image15| image:: /_static/工程说明/小满TC397示例工程说明（中英文修改版0718）/image15.png
   :width: 7.03194in
   :height: 2.23819in
.. |image16| image:: /_static/工程说明/小满TC397示例工程说明（中英文修改版0718）/image16.png
   :width: 6.45717in
   :height: 2.17976in
.. |image17| image:: /_static/工程说明/小满TC397示例工程说明（中英文修改版0718）/image17.png
   :width: 5.76757in
   :height: 3.49295in
.. |image18| image:: /_static/工程说明/小满TC397示例工程说明（中英文修改版0718）/image18.png
   :width: 5.71287in
   :height: 4.78728in
.. |image19| image:: /_static/工程说明/小满TC397示例工程说明（中英文修改版0718）/image19.png
   :width: 6.77153in
   :height: 1.82847in
