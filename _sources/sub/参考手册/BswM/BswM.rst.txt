===================
BswM
===================



文档信息（Document Information）
=========================================

版本历史（Version History）
-------------------------------------

.. list-table::
   :widths: 10 10 10 10 20
   :header-rows: 1

   * - 日期（Date）
     - 作者（Author）
     - 版本（Version）
     - 状态（Status）
     - 说明（Description）
   * - 2024/11/20
     - Jian.Jiang
     - V0.1
     - 发布（Release）
     - 首次发布（First release）
   * - 2025/04/04
     - Jian.Jiang
     - V1.0
     - 发布（Release）
     - 正式发布（Official release）

参考文档（Reference Document）
-----------------------------------------------

.. list-table::
   :widths: 10 10 30 10
   :header-rows: 1

   * - 编号（Number）
     - 分类（Classification）
     - 标题（Title）
     - 版本（Version）
   * - 1
     - Autosar
     - AUTOSAR_CP_EXP_ModeManagementGuide.pdf
     - R23-11
   * - 2
     - Autosar
     - AUTOSAR_CP_SRS_ModeManagement.pdf
     - R23-11 
   * - 3
     - Autosar
     - AUTOSAR_CP_SWS_BswModeManager.pdf
     - R23-11
   * - 4
     - Autosar
     - AUTOSAR_CP_SWS_ECUStateManager.pdf
     - R23-11  


术语与简写（Terms and Abbreviations）
============================================


术语（Term）
--------------------
   .. :align: center   表格内容居中

.. list-table::
   :widths: 10 40
   :header-rows: 1

   * - 术语（Term）
     - 解释（Explanation）

   
   * - BSW Mode
     - BSW 模式是一种由 BSW 中的模式管理器控制和标准化的模式。BSW 模式始终是某个 ECU 的本地模式。 
      
       The BSW mode is a mode controlled and standardized by the mode manager in BSW. The BSW mode is always a local mode of a certain ECU.

   * - Mode Manager
     - 模式管理器是一个可以由 BSW 模块（也可以由 SW-C）担任的角色。
       
       The mode manager is a role that can be assumed by a BSW module (or by a SW-C).
     
   * - Mode Request
     - 模式请求是传达给模式管理器的一些信息，请求模式管理器切换到某种模式。
      
       A mode request is some information conveyed to the mode manager, requesting the mode manager to switch to a certain mode.
     
   * - Mode User
     - 模式用户是对模式变化做出反应的实体。
      
       A mode user is an entity that responds to mode changes.


简写（Abbreviation）
------------------------

.. list-table::
   :widths: 10 20 30
   :header-rows: 1


   * - 简写（Abbreviation）
     - 全称（Full name）
     - 解释（Explanation）

   * - BSW
     - Basic Software
     - 基础软件

   * - BswM
     - BSW Mode Manager
     - BSW 模式管理器
  
   * - ECU
     - Electrical Control Unit
     - 电子控制单元

   * - RTE
     - Real Time Environment
     - 运行时环境

简介（Introduction）
===========================


BSW 模式管理器是实现车辆模式管理和应用模式管理概念中驻留在 BSW 中的部分的模块。其职责是根据简单规则仲裁来自应用层 SW-C 或其他 BSW 模块的模式请求，并根据仲裁结果执行操作。
BSW 模式管理器基本功能的操作可描述为两个不同的任务：模式仲裁和模式控制。
模式仲裁部分根据从 SW-C 或其他 BSW 模块收到的模式请求和模式指示的规则仲裁结果启动模式切换。
模式控制部分通过执行包含其他BSW模块的模式切换操作的动作列表来执行模式切换。

The BSW Mode Manager is a module that implements the part of the vehicle mode management and application mode management concepts residing in the BSW. 
Its responsibility is to arbitrate mode requests from application layer SW-Cs or other BSW modules according to simple rules and perform operations based on 
the arbitration results. The operation of the basic functions of the BSW Mode Manager can be described as two distinct tasks: mode arbitration and mode 
control. The mode arbitration part initiates mode switching based on the arbitration results of rules for mode requests and mode indications received from 
SW-Cs or other BSW modules. The mode control part executes mode switching by performing a list of actions that include mode switching operations of other 
BSW modules.

.. figure:: ../../../_static/参考手册/BswM/BswM架构图.png
   :alt: BswM模块层次图
   :name: fig_BswMarch
   :align: center

   BswM架构图
   
   BswM Architecture Diagram


如图 :ref:`fig_BswMarch` 所示，BswM模块处于AUTOSAR架构中的系统服务层，主要服务于其他基础软件模块以及上层RTE。

As shown in the BswM architecture diagram, the BswM module is located in the system service layer of the AUTOSAR architecture, 
mainly serving other basic software modules and the upper-layer RTE.


功能描述（Functional Description）
========================================

BswM模块主要有如下两个功能：

The BswM module mainly has the following two functions:

1. 模式仲裁：模式仲裁部分根据从 SW-C 或其他 BSW 模块收到的模式请求和模式指示的规则仲裁结果启动模式切换。

   Mode Arbitration: The mode arbitration part initiates mode switching based on the arbitration results of rules for mode requests and mode indications received from SW-Cs or other BSW modules.

2. 模式管理：模式控制部分通过执行包含其他BSW模块的模式切换操作的动作列表来执行模式切换。

   Mode Management: The mode control part executes mode switching by performing a list of actions that include mode switching operations of other BSW modules.
 

特性（Features）
---------------------

模式仲裁（Mode Arbitration）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

BswM 执行的模式仲裁简单且基于规则。用于模式仲裁的规则在 BSW 模式管理器模块的配置中指定。规则由简单的布尔表达式组成，因此模式仲裁预计对运行时的影响较小。

The mode arbitration performed by BswM is simple and rule-based. The rules used for mode arbitration are specified in the configuration of the BSW Mode Manager module. The rules consist of simple boolean expressions, so mode arbitration is expected to have little impact on runtime.

Bsw或SW-C通知BswM进入模式仲裁，可以配置不同的Bsw模块给BswM的通知端口匹配的输入值；这些输入值可以根据具体需求组合成逻辑表达式；逻辑表达式决定了BswM执行的动作列表，动作列表是一系列Bsw或RTE模块操作接口。

Either Bsw or SW-C notifies BswM to enter mode arbitration, and different Bsw modules can be configured to match the input values of BswM's notification ports; these input values can be combined into logical expressions according to specific needs; the logical expressions determine the action list executed by BswM, and the action list is a series of operation interfaces of Bsw or RTE modules.

仲裁规则（Arbitration Rules）
**********************************

规则是由一组模式请求条件组成的逻辑表达式。当输入模式请求和模式指示发生变化时，或在执行 BswM主函数期间，将评估规则。评估结果（True 或 False）用于决定是否执行相应的模式控制操作列表。

A rule is a logical expression composed of a set of mode request conditions. The rule is evaluated when changes occur in the input mode requests and mode indications, or during the execution of the BswM main function. The evaluation result (True or False) is used to determine whether to execute the corresponding list of mode control operations.

仲裁规则的组成（Composition of Arbitration Rules）
*******************************************************

组成模式仲裁规则的逻辑表达式可以使用不同的运算符(AND、OR、XOR、NOT 和 NAND)。表达式中的每个项都对应于一个模式请求条件。如果模式条件引用 **BswMModeRequestPort** ，则该条件将验证请求或指示的模式是否与某个模式相等或不相等。
如果条件引用 **BswMEventRequestPort**，则该条件将验证请求端口是 SET 还是 CLEAR。**BswMEventRequestPort** 事件请求与模式请求的不同之处在于，请求者不向 BswM 发送请求的模式/值，因此，BswM 没有模式条件需要评估。相反，只有事件的接收需要 BswM 进行评估。
当请求者发送/调用事件时，**BswMEventRequestPort** 将处于 SET 状态。然后，BswM 可以通过执行 **BswMClearEventRequest** 操作将 **BswMEventRequestPort** 置于 CLEAR 状态。如图 :ref:`fig_BswM01` 所示具有两个条件的示例。

The logical expressions that make up the mode arbitration rules can use different operators (AND, OR, XOR, NOT, and NAND). Each item in the expression corresponds to a mode request condition. If a mode condition references a **BswMModeRequestPort**, the condition will verify whether the requested or indicated mode is equal or not equal to a certain mode.
If a condition references a **BswMEventRequestPort**, the condition will verify whether the request port is SET or CLEAR. The **BswMEventRequestPort** event request differs from a mode request in that the requester does not send a requested mode/value to BswM, so BswM has no mode condition to evaluate. Instead, only the receipt of the event requires evaluation by BswM.
The **BswMEventRequestPort** will be in the SET state when the requester sends/calls an event. BswM can then place the **BswMEventRequestPort** in the CLEAR state by executing the **BswMEventRequestPort** operation. An example with two conditions is shown in Figure :ref:fig_BswM01.

.. figure:: ../../../_static/参考手册/BswM/仲裁规则.png
   :alt: BswM仲裁示例图
   :name: fig_BswM01
   :align: center

   仲裁规则
   
   Arbitration Rules

模式控制（Mode Control）
~~~~~~~~~~~~~~~~~~~~~~~~~
BswM 的模式控制部分根据模式仲裁的结果执行所有必要的操作。这是使用操作列表完成的。操作列表是 BswM 在模式仲裁触发时执行的操作的 **有序列表** 。

The mode control part of BswM performs all necessary operations based on the results of mode arbitration. This is accomplished using an operation list. The operation list is an **ordered list** of operations that BswM executes when triggered by mode arbitration.

动作列表中的动作可分为三种类型：

The actions in the action list can be divided into three types:

#. 调用其他 BSW 模块或 RTE; 

   Calling other BSW modules or RTE;

#. 链接到要包含在执行中的其他动作列表。

   Link to other action lists to be included in the execution.

#. 模式仲裁规则。执行相应的动作列表时，将评估这些规则。 

   Mode arbitration rules. These rules are evaluated when the corresponding action list is executed.

如下图 :ref:`fig_BswM02` 所示典型用例：

Typical use cases as shown in the action list below:

.. figure:: ../../../_static/参考手册/BswM/动作列表.png
   :alt: BswM动作列表示例图
   :name: fig_BswM02
   :align: center

   动作列表
   
   Action list

.. only:: doc_pbs

  变体（Variant）
  ~~~~~~~~~~~~~~~
  
  - 支持仲裁执行不同的action list
    
    Supports arbitration to execute different action lists
  
  - 支持不同数量的Rule    
  
    Supports different numbers of Rules
  
  - 支持不同数量的Action   
  
    Supports different numbers of Actions
  
  - 支持部分Action中执行不同的动作  
  
    Supports executing different actions in some Actions.


偏差（Deviation）
-----------------------------

#. BswMModeInitValue变更（Change of BswMModeInitValue）

   因为设计需要，将每个ModeRequestPort都需要配置，提取成按照类别配置，减少参数配置, 所以将配置简化，只需要在BswMModeInitValue中配置。
   
   Due to design requirements, each ModeRequestPort needs to be configured, and it is extracted to be configured by category to reduce parameter configuration. Therefore, the configuration is simplified, and it only needs to be configured in BswMModeInitValue.

#. 动作列表优先级失效（Invalidation of action list priority）

   因为目前设计的值同步执行，不适用于优先级处理， 配置BswMActionListPriority无效。
     
   Because the currently designed value is executed synchronously, it is not suitable for priority processing, and configuring BswMActionListPriority is invalid.

集成（Integration）
=========================

文件列表（File list）
-----------------------

静态文件（Static files）
~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - 文件（File）
     - 描述（Description）
   
   * - BswM.h
     - LC配置数据类型，以及通用API的声明
      
       LC configuration data types and declarations of general APIs

   * - BswM_Bsw.h
     - 内部与SchM交互的API声明
      
       API declarations for internal interaction with SchM

   * - BswM_CanSM.h
     - BswM与CanSM模块交互API声明
      
       API declarations for interaction between BswM and CanSM modules

   * - BswM_ComM.h
     - BswM与ComM模块交互API声明
      
       API declarations for interaction between BswM and ComM modules

   * - BswM_Dcm.h
     - BswM与Dcm模块交互API声明
      
       API declarations for interaction between BswM and Dcm modules

   * - BswM_EcuM.h
     - BswM与EcuM模块交互API声明
      
       API declarations for interaction between BswM and EcuM modules

   * - BswM_EthIf.h
     - BswM与EthIf模块交互API声明
      
       API declarations for interaction between BswM and EthIf modules

   * - BswM_EthSM.h
     - BswM与EthSM模块交互API声明
      
       API declarations for interaction between BswM and EthSM modules

   * - BswM_FrSM.h
     - BswM与FrSM模块交互API声明
      
       API declarations for interaction between BswM and FrSM modules

   * - BswM_Internal.h
     - BswM中PC配置数据结构类型定义以及内部函数声明
      
       Type definition of PC configuration data structure and declaration of internal functions in BswM

   * - BswM_J1939Dcm.h
     - BswM与J1939Dcm模块交互API声明
      
       API declarations for interaction between BswM and J1939Dcm modules

   * - BswM_J1939Nm.h
     - BswM与J1939Nm模块交互API声明
      
       API declarations for interaction between BswM and J1939Nm modules

   * - BswM_LinSM.h
     - BswM与LinSM模块交互API声明
      
       API declarations for interaction between BswM and LinSM modules

   * - BswM_LinTp.h
     - BswM与LinTp模块交互API声明
      
       API declarations for interaction between BswM and LinTp modules

   * - BswM_MemMap.h
     - BswM所有变量、函数用到的MemMap机制包含头文件
      
       The MemMap mechanism used by all variables and functions in BswM includes header files

   * - BswM_Nm.h
     - BswM与Nm模块交互API声明
      
       API declarations for interaction between BswM and Nm modules

   * - BswM_NvM.h
     - BswM与NvM模块交互API声明
      
       API declarations for interaction between BswM and NvM modules

   * - BswM_Sd.h
     - BswM与Sd模块交互API声明
      
       API declarations for interaction between BswM and Sd modules

   * - BswM_SoAd.h
     - BswM与SoAd模块交互API声明
      
       API declarations for interaction between BswM and SoAd modules

   * - BswM_Swc.h
     - BswM与Rte交互的API声明
      
       API declarations for interaction between BswM and Rte

   * - BswM_Types.h
     - BswM定义的通用数据类型
      
       Common data types defined by BswM

   * - BswM.c
     - BswM模块提供的API（不与其他模块交互），以及内部函数等
      
       APIs provided by the BswM module (that do not interact with other modules), as well as internal functions, etc.

   * - BswM_Bsw.c
     - 与基础软件的模式通知的API实现
      
       API implementation for mode notification with basic software

   * - BswM_CanSM.c
     - BswM与CanSM模块交互的API实现
      
       Implementation of API for interaction between BswM and CanSM modules
       
   * - BswM_ComM.c
     - BswM与ComM模块交互的API实现
      
       Implementation of API for interaction between BswM and ComM modules

   * - BswM_Dcm.c
     - BswM与Dcm模块交互的API实现
      
       Implementation of API for interaction between BswM and Dcm modules

   * - BswM_DetCheck.c
     - BswM内部的Det函数实现
      
       Implementation of the Det function inside BswM

   * - BswM_EcuM.c
     - BswM与EcuM模块交互的API实现
      
       Implementation of API for interaction between BswM and EcuM modules

   * - BswM_EthIf.c
     - BswM与EthIf模块交互的API实现
      
       Implementation of API for interaction between BswM and EthIf modules

   * - BswM_EthSM.c
     - BswM与EthSM模块交互的API实现
      
       Implementation of API for interaction between BswM and EthSM modules

   * - BswM_FrSM.c
     - BswM与FrSM模块交互API实现
      
       Implementation of API for interaction between BswM and FrSM modules

   * - BswM_J1939Dcm.c
     - BswM与J1939Dcm模块交互API实现
      
       Implementation of API for interaction between BswM and J1939Dcm modules

   * - BswM_J1939Nm.c
     - BswM与J1939Nm模块交互API实现
      
       Implementation of API for interaction between BswM and J1939Nm modules

   * - BswM_LinSM.c
     - BswM与LinSM模块交互API实现
      
       Implementation of API for interaction between BswM and LinSM modules

   * - BswM_LinTp.c
     - BswM与LinTp模块交互API实现
      
       Implementation of API for interaction between BswM and LinTp modules  

   * - BswM_Nm.c
     - BswM与Nm模块交互API实现
      
       Implementation of API for interaction between BswM and Nm modules

   * - BswM_NvM.c
     - BswM与NvM模块交互API实现
      
       Implementation of API for interaction between BswM and NvM modules

   * - BswM_Sd.c
     - BswM与Sd模块交互API实现
      
       Implementation of API for interaction between BswM and Sd modules

   * - BswM_SoAd.c
     - BswM与SoAd模块交互API实现
      
       Implementation of API for interaction between BswM and SoAd modules

   * - BswM_Swc.c
     - BSWM与Rte模块交互API实现
      
       Implementation of API for interaction between BSWM and Rte modules

   * - BswM_TimerControl.c
     - BswM中timer control相关API实现
      
       Implementation of timer control related APIs in BswM

动态文件（Dynamic file）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - 文件（File）
     - 描述（Description）
   
   * - BswM_Cfg.c
     - BswM中所有PC配置数据
      
       All PC configuration data in BswM

   * - BswM_Cfg.h
     - BswM中所有PC配置宏定义以及包含的头文件
      
       All PC configuration macro definitions and included header files in BswM

   * - BswM_LCfg.c
     - BswM中所有Link time配置内部Api实现
      
       Implementation of all Link time configuration internal APIs in BswM

   * - BswM_Lcfg.h
     - BswM中所有Link time配置数据声明以及宏定义
      
       All Link time configuration data declarations and macro definitions in BswM

   * - BswM_Lcfg_{name}.c
     - BswM中所有Link time配置数据
      
       All Link time configuration data in BswM

   * - SchM_BswM.h
     - 定义BswM_MainFunction函数声明，以及某些关键区域保护机制
      
       Define the function declaration of BswM_MainFunction, as well as some key area protection mechanisms


错误处理（Error handling）
--------------------------------

开发错误（Development errors）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. list-table:: 
   :widths: 20 10 30
   :header-rows: 1

   * - Error code
     - Value[hex]
     - Description

   * - BSWM_E_UNINIT
     - 0x01
     - A service was called prior to initialization

   * - BSWM_E_NULL_POINTER
     - 0x02
     - A null pointer was passed as an argument

   * - BSWM_E_PARAM_INVALID
     - 0x03
     - A parameter was invalid (unspecific)

   * - BSWM_E_REQ_USER_OUT_OF_RANGE
     - 0x04
     - A requesting user was out of range

   * - BSWM_E_REQ_MODE_OUT_OF_RANGE
     - 0x05
     - A requested mode was out of range

   * - BSWM_E_PARAM_CONFIG
     - 0x06
     - The provided configuration is inconsistent

   * - BSWM_E_PARAM_POINTER
     - 0x07
     - A parameter pointer was invalid

   * - BSWM_E_INIT_FAILED
     - 0x08
     - Invalid configuration set selection


运行时错误（Runtime error）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. list-table:: 
   :widths: 20 10 30
   :header-rows: 1

   * - Error code
     - Value[hex]
     - Description

   * - BSWM_API_ID_DO_ACTION_LIST（服务函数ID）（Service function ID）
     - 通过配置BswMReportFailRuntimeErrorId决定

       Determined by configuring BswMReportFailRuntimeErrorId  

     - Invalid configuration set selection

.. include:: BswM_api.rst

配置（configuration）
=============================

基础配置说明（Basic Configuration Instructions）
-------------------------------------------------------

仲裁规则配置（Arbitration rule configuration）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
首先要明确要做什么，比如：控制灯，我们知道了要控制灯，那么需要知道灯的逻辑状态（打开，关闭），
还需要知道在什么状态下打开，什么状态下关闭。我们知道这些条件后我们就能够组成一套规则。在BswM
中通过配置来完成这一套规则的构建。基本步骤如下：

First, it is necessary to clarify what needs to be done. For example, if we want to control a light, we need to know the logical states of the light (on, off), as well as under what conditions it should be turned on and under what conditions it should be turned off. Once we know these conditions, we can form a set of rules. In BswM, the construction of this set of rules is completed through configuration. The basic steps are as follows:

1. 创建一个Rule，Rule名称为：BswM_Rule_XXX，其中Rule为规则名称，比如：BswM_Rule_LedOnOff。
 
   Create a Rule with the name: BswM_Rule_XXX, where "Rule" is the rule name, for example: BswM_Rule_LedOnOff.

2. 在该Rule中配置选择仲裁条件以及执行的动作， 条件为真是执行什么动作，条件为假时执行什么动作。

   In this Rule, configure the selection of arbitration conditions and the actions to be executed, including what action to perform when the condition is true and what action to perform when the condition is false.

   - 通过配置BswMRuleInitState来设置Rule的初始值，

     Set the initial value of the Rule by configuring BswMRuleInitState,

   - 通过配置BswMRuleExpressionRef选择Rule的仲裁条件，

     Select the arbitration condition of the Rule by configuring BswMRuleExpressionRef,

   - 通过配置BswMRuleFalseActionList选择Rule的仲裁结果为假时执行的动作，

     Select the actions to be executed when the arbitration result of the Rule is false by configuring BswMRuleFalseActionList,

   - 通过配置BswMRuleTrueActionList选择Rule的仲裁结果为真时执行的动作。

     Select the actions to be executed when the arbitration result of the Rule is true by configuring BswMRuleTrueActionList.

.. figure:: ../../../_static/参考手册/BswM/RuleConfig.png
   :alt: Rule configuration
   :name: fig_BswM03
   :align: center

   RuleConfig


- 1: 名称
- 2: 规则初始状态
- 3: 仲裁条件
- 4: 条件为假执行的动作
- 5: 条件为真执行的动作

3. 然后在BswMLogicalExpression配置相应的逻辑表达式。

   Then configure the corresponding logical expression in BswMLogicalExpression.

   - 通过配置BswMLogicalOperator决定逻辑表达式的运算符，

     The operator of the logical expression is determined by configuring BswMLogicalOperator,

   - 通过配置BswMArgumentRef选择逻辑表达式的运算对象。

     The operand of the logical expression is selected by configuring BswMArgumentRef.

.. figure:: ../../../_static/参考手册/BswM/LogicalExpression.png
   :alt: LogicalExpression configuration
   :name: fig_BswM04
   :align: center

   LogicalExpression

- 1: 逻辑表达式的名称
- 2: 逻辑运算符
- 3: 等式或者其他逻辑表达式，由运算符决定可配置的数量

4. 在BswMModeCondition为BswMLogicalExpression配置等式：
  
   Configure the equation for BswMModeCondition as BswMLogicalExpression:
     
   - 通过配置BswMConditionType选择等式两边比较类型，（对于 BSWM_EQUALS 和 BSWM_EQUALS_NOT，通过 BswMConditionMode 引用的 BswMModeRequestPort端口与在BswMConditionValue中配置的值进行相等或不相等的比较。对于 BSWM_EVENT_IS_SET 和 BSWM_EVENT_IS_CLEARED，通过 BswMConditionMode 引用的 BswMEventRequestPort 端口被检查是否已设置或清除（未设置）。
     
     Select the comparison type of both sides of the equation by configuring BswMConditionType. (For BSWM_EQUALS and BSWM_EQUALS_NOT, the BswMModeRequestPort referenced by BswMConditionMode is compared for equality or inequality with the value configured in BswMConditionValue. For BSWM_EVENT_IS_SET and BSWM_EVENT_IS_CLEARED, the BswMEventRequestPort referenced by BswMConditionMode is checked to see if it is set or cleared (not set).
   
   - 通过配置BswMConditionMode选择等式左边的对象，

     Select the object on the left side of the equation by configuring BswMConditionMode,

   .. figure:: ../../../_static/参考手册/BswM/ModeConditionLeft.png
    :alt: condition configuration
    :name: fig_BswM05
    :align: center

    ModeConditionLeft

- 1: 等式两边比较类型
- 2: 等式左边的对象，引用BswMModeRequestPort或BswMEventRequest

  

   - 通过配置BswMBswMode下的BswMBswRequestedMode或BswModeCompareValue选择等式右边的值。

     The value on the right side of the equation is selected by configuring BswMBswRequestedMode or BswModeCompareValue under BswMBswMode.

   .. figure:: ../../../_static/参考手册/BswM/ModeConditionRight.png
    :alt: 比较模式配置
    :name: fig_BswM06
    :align: center

    ModeConditionRight

- 1: 条件等式右值

   .. caution:: 注意
      
      BswMConditionModey引用的 BswMModeRequestPort的 BswMModeRequestSource为BswMBswModeNotification 或 BswMSwcModeNotification 或 
      BswMSwcModeRequest时，BswMConditionValue配置为BswMModeDeclaration；
      
      When the BswMModeRequestSource of the BswMModeRequestPort referenced by BswMConditionMode is BswMBswModeNotification, BswMSwcModeNotification, or BswMSwcModeRequest, BswMConditionValue is configured as BswMModeDeclaration;

      BswMConditionModey引用的 BswMModeRequestPort的 BswMModeRequestSource为BswMGenericRequest 或 BswMJ1939DcmBroadcastStatus时，
      BswMConditionValue配置为BswMBswMode下的BswMBswRequestedMode，由用户自定义； 
      
      When the BswMModeRequestSource of the BswMModeRequestPort referenced by BswMConditionMode is BswMGenericRequest or BswMJ1939DcmBroadcastStatus, BswMConditionValue is configured as BswMBswRequestedMode under BswMBswMode, which is customized by the user;

      BswMConditionModey引用的 BswMModeRequestPort的 BswMModeRequestSource为其他类型时，BswMConditionValue配置为BswMBswMode下BswModeCompareValue
      下拉框来选择。
      
      When the BswMModeRequestSource of the BswMModeRequestPort referenced by BswMConditionMode is of other types, BswMConditionValue is configured by selecting from the BswModeCompareValue drop-down box under BswMBswMode.


5. 配置条件的等式的左值，可以是BswMEventRequestPort或者BswMModeRequestPort

   The left value of the equation for configuring conditions can be BswMEventRequestPort or BswMModeRequestPort.

   - 通过配置BswMRequestProcessing决定模式请求的处理方式（延迟或立即）。

     The processing method of mode requests (delayed or immediate) is determined by configuring BswMRequestProcessing.

   - 通过配置BswMRequestSource选择模式请求的来源。BswMEventRequestPort如图 :ref:`fig_BswM07` 所示，BswMModeRequestPort如图 :ref:`fig_BswM08` 所示。

     The source of the mode request is selected by configuring BswMRequestSource. The BswMEventRequestPort is shown in Figure BswMEventRequestSource, and the BswMModeRequestPort is shown in Figure ModeRequestSource.
     
     .. figure:: ../../../_static/参考手册/BswM/BswMEventRequestSource.png
      :alt: Event request source configuration
      :name: fig_BswM07
      :align: center

      BswMEventRequestSource

     .. figure:: ../../../_static/参考手册/BswM/ModeRequestSource.png
      :alt: Mode request source configuration
      :name: fig_BswM08
      :align: center

      ModeRequestSource

     .. important::

      当使用非标准请求的条件时，可以通过配置BswMGenericRequest实现一些非标条件。

      When using conditions for non-standard requests, some non-standard conditions can be implemented by configuring BswMGenericRequest.

6. 配置执行的动作列表，在工具中配置BswMModeControl->BswMActionList(被BswMRule使用)

   Configure the list of actions to be executed. In the tool, configure BswMModeControl->BswMActionList (used by BswMRule)

   - 通过配置BswMActionListExecution选择动作类型（触发执行或条件执行）。

     Select the action type (trigger execution or conditional execution) by configuring BswMActionListExecution.

     .. figure:: ../../../_static/参考手册/BswM/ActionList.png
        :alt: Action List configuration
        :name: fig_BswM09
        :align: center

        ActionList
  
  - 1: actionList的执行类型
  - 2: 优先级

   - 通过配置BswMActionListItem选择动作列表中执行的动作。

     The actions to be executed in the action list are selected by configuring BswMActionListItem

     .. figure:: ../../../_static/参考手册/BswM/ActionListItem.png
        :alt: Action List Item configuration
        :name: fig_BswM10
        :align: center

        ActionListItem

  - 1: 中断执行
  - 2: 执行顺序
  - 3: 执行过程中报Detld
  - 4: 执行的动作，可以是action、其他actionList、Rule
  
7. 配置执行动作（Configure execution actions）

   - 通过配置BswMAction->BswMAvailableActions选择执行的动作。

     Select the action to be executed by configuring BswMAction->BswMAvailableActions

     .. figure:: ../../../_static/参考手册/BswM/Action.png
      :alt: Action configuration
      :name: fig_BswM11
      :align: center

      Action

   .. important::

      当非标准提供的功能需要被执行时，可以通过配置BswMUserCallout（只支持无参数函数）来执行用户非标代码。

      When functions not provided as standard need to be executed, user non-standard code can be executed by configuring BswMUserCallout (only parameterless functions are supported)
    

多核多分区配置说明（Configuration Instructions for Multi-Core and Multi-Partition）
-------------------------------------------------------------------------------------------

BswM存在于每个分区中，每个分区有单独的BswMConfig实例，在多分区系统中，用户需要配置多个BswMConfig实例。
每个BswM实例是相互隔离的，需要通过Rte或者用户自定义的全局变量将BswM实例的配置信息传递给其他BswM实例。
如下图配置多分区：

BswM exists in each partition, and each partition has a separate BswMConfig instance. In a multi-partition system, users need to configure multiple BswMConfig instances.
Each BswM instance is isolated from each other, and the configuration information of the BswM instance needs to be passed to other BswM instances through Rte or user-defined global variables.
Configure multiple partitions as shown in the following figure:

 .. figure:: ../../../_static/参考手册/BswM/MultiPartition.png
   :alt: MultiPartition
   :name: fig_BswM12
   :align: center

   MultiPartition

- 1: 为每一个分区创建一个BswMConfig
- 2: 为对应的BswMConfig分配分区信息

与SWC交互配置说明（Configuration Instructions for Interaction with SWC）
----------------------------------------------------------------------------------

BswM提供模式管理和模式请求两种方式来与SWC或其他基础软件模块进行交互，BswM既可以作为模式用户也可以作为模式提供者。

BswM provides two ways, namely mode management and mode request, to interact with SWC or other basic software modules. BswM can act as both a mode user and a mode provider.

 .. figure:: ../../../_static/参考手册/BswM/ModeCtrl.png
   :alt: Mode Control
   :name: fig_BswM13
   :align: center

   ModeCtrl

如下图所示应用程序 SW-C 的端口如何连接到 BSW 模式管理器的服务端口。应用程序模式管理器 SW-C 具有模式
请求端口和模式切换 R 端口（名为 modeNotificationPort，以区别于模式切换 P 端口）。第一个端口用于请求其
应用程序模式的更改，后者用于在 BswM 执行模式更改时接收通知。应用程序模式管理器的模式请求端口（modeRequest 
Port0）连接到 BSW 模式管理器的相应模式请求端口。

As shown in the following figure, how the ports of the application SW-C are connected to the service ports of the BSW Mode Manager. The application mode manager SW-C has a mode request port and a mode switch R port (named modeNotificationPort to distinguish it from the mode switch P port). The first port is used to request a change in its application mode, and the latter is used to receive notifications when the BswM executes a mode change. The mode request port (modeRequest Port0) of the application mode manager is connected to the corresponding mode request port of the BSW Mode Manager.

 .. figure:: ../../../_static/参考手册/BswM/ModeManager.png
   :alt: Mode Management
   :name: fig_BswM14
   :align: center

   ModeManager


模式切换与模式通知（Mode Switching and Mode Notification）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. 模式通知（Mode Notification）

   - 通过配置BswMConfig->BswMArbitration->BswMModeRequestPort->BswMModeRequestSource-> **BswMBswModeNotification** 来与其他基础软件模块进行模式管理，BswMBswModeNotification引用其他模块描述文件中的模式声明组原型。
      
     Mode management with other basic software modules is performed by configuring BswMConfig->BswMArbitration-> BswMModeRequestPort->BswMModeRequestSource-> **BswMBswModeNotification** . BswMBswModeNotification references the mode declaration group prototype in the description files of other modules.
   
   - 通过配置BswMConfig->BswMArbitration->BswMModeRequestPort->BswMModeRequestSource-> **BswMSwcModeNotification** 来接收来自SWC的模式切换通知, BswMSwcModeNotificationModeDeclarationGroupPrototypeRef引用萃取文件中的模式声明组原型。
      
     Notifications of mode switching from SWC are received by configuring BswMConfig->BswMArbitration->BswMModeRequestPort-> BswMModeRequestSource-> **BswMSwcModeNotification** . BswMSwcModeNotificationModeDeclarationGroupPrototypeRef references the mode declaration group prototype in the extraction file.

2. 模式切换（Mode Switching）

   - 首先配置BswMSwitchPort（BswMModeControl->BswMSwitchPort）创建模式切换P端口
      
     First, configure BswMSwitchPort (BswMModeControl->BswMSwitchPort) to create a mode switch P port.
   
   - 与SWC交互需要配置BswMRteSwitch(BswMModeControl->BswMAction->BswMAvailableActions-> **BswMRteSwitch** )来执行模式切换
      
     To interact with SWC, it is necessary to configure BswMRteSwitch (BswMModeControl->BswMAction->BswMAvailableActions-> **BswMRteSwitch** ) to perform mode switching.
   
   - 与基础软件交互需要配置BswMSchMSwitch(BswMModeControl->BswMAction->BswMAvailableActions-> **BswMSchMSwitch** )来执行模式切换
      
     To interact with basic software, it is necessary to configure BswMSchMSwitch (BswMModeControl->BswMAction-> BswMAvailableActions-> **BswMSchMSwitch** ) to perform mode switching.

模式请求（Mode Request）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

模式请求基于Sender-Receiver通信进行模式控制的。
   
Mode requests are based on Sender-Receiver communication for mode control.

1. BswM作为请求方（BswM acts as the requester）

   - 首先配置BswMRteModeRequestPort（BswMModeControl->BswMRteModeRequestPort）创建SR通信P端口

     First, configure BswMRteModeRequestPort (BswMModeControl->BswMRteModeRequestPort) to create an SR communication P port

   - 然后配置BswMRteModeRequest(BswMModeControl->BswMAction->BswMAvailableActions->BswMRteModeRequest)发出模式切换请求

     Then configure BswMRteModeRequest (BswMModeControl->BswMAction->BswMAvailableActions->BswMRteModeRequest) to send a mode switch request

2. BswM作为被请求方（BswM acts as the requested party）

   - 通过配置BswMSwcModeRequest（BswMConfig->BswMArbitration->BswMModeRequestPort->BswMModeRequestSource-> BswMSwcModeRequest）接收模式切换请求

     Receive mode switch requests by configuring BswMSwcModeRequest (BswMConfig->BswMArbitration->BswMModeRequestPort-> BswMModeRequestSource->BswMSwcModeRequest)

