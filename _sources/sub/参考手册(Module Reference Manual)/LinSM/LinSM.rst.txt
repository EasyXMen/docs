===================
LinSM
===================



文档信息 Document Information
============================================================

版本历史 Version History
--------------------------------------------------------------------------------------------------------

.. list-table::
   :widths: 10 10 10 10 20
   :header-rows: 1

   * - 日期(Date)
     - 作者(Author)
     - 版本(Version)
     - 状态(Status)
     - 说明(Description)

   * - 2024/11/15
     - caihong.liu
     - V0.1
     - 发布(Release)
     - 首次发布(First release)

   * - 2025/04/04
     - caihong.liu
     - V1.0
     - 发布(Release)
     - 正式发布(Official release)

参考文档 References
--------------------------------------------------------------------------------------------------------

.. list-table::
   :widths: 10 10 30 10
   :header-rows: 1

   * - 编号(Number)
     - 分类(Classification)
     - 标题(Title)
     - 版本(Version)
   * - 1
     - Autosar
     - AUTOSAR_CP_SWS_LINStateManager.pdf
     - R23-11
   * - 2
     - Autosar
     - AUTOSAR_SWS_LINInterface.pdf
     - R23-11
   * - 3
     - Autosar
     - AUTOSAR_CP_SWS_COMManager.pdf
     - R23-11

术语与简写 Terms and Abbreviations
====================================================================


术语 Terms
--------------------------------------------------------------------------------------------------------


.. list-table::
   :widths: 10 40
   :header-rows: 1

   * - 术语(Terms)
     - 解释(Explanation)

   * - MASTER Node
     - LIN总线拓扑结构中的唯一主机节点，同时支持主机任务和从机任务(The unique master node in the LIN bus topology, which supports both master tasks and slave tasks)

   * - SLAVE Node
     - LIN总线拓扑结构中的从机节点，从机节点只支持从机任务(The slave node in the LIN bus topology, which only supports slave tasks)

   * - Schedule Table
     - 规定总线上帧的传输次序以及各帧在总线上的传输时间的配置(A configuration that specifies the transmission order of frames on the bus and the transmission time of each frame on the bus)


简写 Abbreviations
--------------------------------------------------------------------------------------------------------

.. list-table::
   :widths: 10 20 30
   :header-rows: 1


   * - 简写(Abbreviation)
     - 全称(Full name)
     - 解释(Explanation)

   * - LIN
     - Local Interconnect Network
     - 局部互联网络

   * - LinIf
     - LIN Interface
     - 局部互联网络接口

   * - LinSM
     - LIN State Manager
     - 局部互联网络状态管理

   * - BswM
     - BSW Mode Manager
     - 基础软件模式管理

   * - ComM
     - Communication Manager
     - 通信管理

简介 Introduction
==================================

本文档是AUTOSAR R23-11的LIN State Manager模块参考手册。手册描述AUTOSAR规范的LinSM模块相关功能、API、配置，旨在指导使用LinSM模块的用户能够清晰地了解如何去使用LinSM模块。

This document is the reference manual for the LIN State Manager module of AUTOSAR R23-11. The manual describes the functions, APIs, and configurations related to the LinSM module specified in the AUTOSAR standard, aiming to guide users who use the LinSM module to clearly understand how to use the LinSM module.
    
如下图 :ref:`fig_LinStack_arch` 所示，LinSM模块的下层是Lin Interface，上层是ComM，BswM等。其主要职责是控制Lin总线的控制流。主要功能包括以下三点：

As shown in Figure :ref:`fig_LinStack_arch` below, the lower layer of the LinSM module is the Lin Interface, and the upper layers include ComM, BswM, etc. Its main responsibility is to control the control flow of the LIN bus. The main functions include the following three points:
    
1.根据上层的请求切换到相应的调度表

1.Switch to the corresponding schedule table according to the request from the upper layer

2.根据上层的请求对LIN通道处理Go-to-sleep或wake-up流程

2.Process the Go-to-sleep or wake-up process for the LIN channel according to the request from the upper layer

3.当LIN通道状态切换到新状态时通知上层模块

3.Notify the upper-layer modules when the LIN channel state switches to a new state

.. figure:: ../../../_static/参考手册/LinSM/AutosarLINStack.png
   :alt: LIN通信栈架构图 (LIN Communication Stack Architecture Diagram)
   :name: fig_LinStack_arch
   :align: center

   AUTOSAR BSW software architecture - LIN stack scope.

.. 功能描述章节
.. include:: LinSM_Functional.rst

.. 集成描述章节
.. include:: LinSM_Integration.rst

.. 引用接口描述。来自于code->doxygen->latex->rst
.. 引用接口描述。 From code->doxygen->latex->rst
.. include:: LinSM_api.rst
 
.. 引用配置描述章节
.. include:: LinSM_Configuration.rst