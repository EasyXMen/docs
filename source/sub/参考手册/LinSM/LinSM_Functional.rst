功能描述 Functional Description
==========================================================

特性 Features
--------------------------------------------------------------------------------------------------

LIN网络的状态管理功能 State Management Function of LIN Network
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
LinSM模块的功能主要体现在对Lin通道的网络管理功能，LinSM根据上层对Lin通道的通信状态请求，对该通道进行相应的休眠或唤醒操作。同时，LinSM内部为每个通道维护独立的状态机记录该通道的通信模式，根据当前的通信模式体现休眠唤醒操作成功与否。

The function of the LinSM module is mainly reflected in the network management of Lin channels. According to the upper layer's request for the communication state of the Lin channel, LinSM performs corresponding sleep or wakeup operations on the channel. At the same time, LinSM internally maintains an independent state machine for each channel to record the communication mode of the channel, and reflects the success or failure of the sleep and wakeup operations according to the current communication mode.

按照状态机流转顺序主要功能为：

According to the sequence of state machine transitions, the main functions are:

1.LinSM模块上电后处于非初始化状态，初始化后记录各通道状态为 **LINSM_NO_COM** 状态，即无通信

1.The LinSM module is in an uninitialized state after power-on. After initialization, the state of each channel is recorded as **LINSM_NO_COM** state, that is, no communication.

2.当上层请求 **COMM_FULL_COMMUNICATION** 时，相应Lin通道启动Wake up流程，唤醒成功则记录该通道为 **LINSM_FULL_COM** 状态，即启动通信

2.When the upper layer requests **COMM_FULL_COMMUNICATION**, the corresponding Lin channel starts the Wake up process. If the wakeup is successful, the channel is recorded as **LINSM_FULL_COM** state, that is, communication is started.

3.当上层请求 **COMM_NO_COMMUNICATION** 时，相应Lin通道启动Goto Sleep流程，休眠成功则记录该通道为 **LINSM_NO_COM** 状态

3.When the upper layer requests **COMM_NO_COMMUNICATION**, the corresponding Lin channel starts the Goto Sleep process. If the sleep is successful, the channel is recorded as **LINSM_NO_COM** state.

除上描述外，LinSM不受理其他类型的通信状态请求

Except as described above, LinSM does not accept other types of communication state requests.

Wake up
****************************
当LinSM模块初始化后，且Lin通道处于LINSM_NO_COM，上层调用LinSM_RequestComMode()向某通道请求COMM_FULL_COMMUNICATION，LinSM立即将该请求通过LinIf_Wakeup()函数转发到LinIf模块，LinIf_Wakeup()的返回值都将直接返回给上层调用者。

After the LinSM module is initialized and the Lin channel is in LINSM_NO_COM, the upper layer calls LinSM_RequestComMode() to request COMM_FULL_COMMUNICATION for a certain channel. LinSM immediately forwards the request to the LinIf module through the LinIf_Wakeup() function. The return value of LinIf_Wakeup() will be directly returned to the upper-layer caller.

只有当LinIf_Wakeup()返回E_OK则对该通道启动 **Wake up** 进程：

The **Wake up** process for the channel is started only when LinIf_Wakeup() returns E_OK:

加载 `唤醒超时计时器` ，计时器数值根据配置决定

Load the `wakeup timeout timer`, the timer value is determined according to the configuration.

加载 `唤醒重试计数器` ，计数器数值根据配置决定

Load the `wakeup retry counter`, the counter value is determined according to the configuration.

进程结束：

End of process:

1.LinSM_WakeupConfirmation()函数被回调

1.The LinSM_WakeupConfirmation() function is called back.

1.1入参success为TRUE时，表示该通道唤醒成功，记录该通道通信状态为LINSM_FULL_COM，且子状态为 **LINSM_RUN_COMMUNICATION**。
   
1.1When the input parameter success is TRUE, it indicates that the channel wakeup is successful. The communication state of the channel is recorded as LINSM_FULL_COM, and the sub-state is **LINSM_RUN_COMMUNICATION**.

1.2入参success为FALSE时，表示该通道唤醒失败，维持当前状态为LINSM_NO_COM
   
1.2When the input parameter success is FALSE, it indicates that the channel wakeup failed, and the current state remains LINSM_NO_COM.

1.3无论入参结果，LinSM都要回调ComM_BusSM_ModeIndication()和BswM_LinSM_CurrentState()传递该通道当状态
   
1.3Regardless of the input parameter result, LinSM shall call back ComM_BusSM_ModeIndication() and BswM_LinSM_CurrentState() to transmit the current state of the channel.

2.`唤醒超时计时器` 超时，则 `唤醒重试计数器` 减一，重置 `唤醒超时计时器` 且再调用LinIf_Wakeup()，当 `唤醒重试计数器` 减至0时：

2.When the `wakeup timeout timer` expires, the `wakeup retry counter` is decremented by 1, the `wakeup timeout timer` is reset, and LinIf_Wakeup() is called again. When the `wakeup retry counter` is decremented to 0:

2.1调用Det_ReportRuntimeError上报错误码  LINSM_E_CONFIRMATION_TIMEOUT
   
2.2Call Det_ReportRuntimeError to report the error code LINSM_E_CONFIRMATION_TIMEOUT. 

2.3当通道类型为MASTER时：可继续为该通道调用LinIf_Wakeup()
   
2.3When the channel type is MASTER: LinIf_Wakeup() can continue to be called for the channel.

2.4当通道类型为SLAVE时：加载silence-after-wakeup计时器，进入静默状态，该计时器超时后重启Wake up进程
   
2.4When the channel type is SLAVE: Load the silence-after-wakeup timer, enter the silent state, and restart the Wake up process after the timer expires.

Goto Sleep
****************************
当LinSM模块初始化后，且Lin通道处于LINSM_FULL_COM，上层调用LinSM_RequestComMode()向某通道请求COMM_NO_COMMUNICATION。

After the LinSM module is initialized and the LIN channel is in LINSM_FULL_COM, the upper layer calls LinSM_RequestComMode() to request COMM_NO_COMMUNICATION for a certain channel.

1.对于MASTER类型的Lin通道：LinSM立即将该请求通过LinIf_GotoSleep()函数转发到LinIf模块，LinIf_GotoSleep()的返回值都将直接返回给上层调用者，当LinIf_GotoSleep()返回E_OK则对该通道启动 **Goto Sleep** 进程。

1.For LIN channels of MASTER type: LinSM immediately forwards the request to the LinIf module through the LinIf_GotoSleep() function. The return value of LinIf_GotoSleep() will be directly returned to the upper-layer caller. When LinIf_GotoSleep() returns E_OK, the **Goto Sleep** process for the channel is started.

2.对于SLAVE类型的Lin通道：LinSM为该通道记录该状态请求，直接返回E_OK。当LinIf检测到总线睡眠时，LinIf对该通道被调用LinSM_GotoSleepIndication()，此时调用LinIf_GotoSleep()且返回E_OK则对该通道启动 **Goto Sleep** 进程。

2.For LIN channels of SLAVE type: LinSM records the state request for the channel and directly returns E_OK. When LinIf detects that the bus is sleeping, LinIf calls LinSM_GotoSleepIndication() for the channel. At this time, calling LinIf_GotoSleep() and returning E_OK starts the **Goto Sleep** process for the channel.

Goto Sleep进程启动时，记录该通道状态为LINSM_FULL_COM下的子状态 **LINSM_GOTO_SLEEP**

When the Goto Sleep process starts, the state of the channel is recorded as the sub-state **LINSM_GOTO_SLEEP** under LINSM_FULL_COM.

进程结束：

End of process:

1.上层对已经启动Goto Sleep进程的通道的状态请求不变时，LinSM维持该通道处于LINSM_GOTO_SLEEP状态，直到LinSM_GotoSleepConfirmation()被回调，记录该通道状态为LINSM_NO_COM且回调ComM_BusSM_ModeIndication()和BswM_LinSM_CurrentState()传递该通道当状态

1.When the state request of the upper layer for the channel that has started the Goto Sleep process remains unchanged, LinSM maintains the channel in the LINSM_GOTO_SLEEP state until LinSM_GotoSleepConfirmation() is called back. Then, the state of the channel is recorded as LINSM_NO_COM, and ComM_BusSM_ModeIndication() and BswM_LinSM_CurrentState() are called back to transmit the current state of the channel.


调度表切换功能 Schedule Table Switching Function
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
调度表切换功能仅支持MASTER类型Lin通道，且主动请求切换时该通道必须已处于唤醒状态，即 **LINSM_FULL_COM** 状态

The schedule table switching function only supports MASTER-type Lin channels, and when actively requesting switching, the channel must be in the wakeup state, i.e., **LINSM_FULL_COM** state.

请求切换调度表：

Request to switch the schedule table:

1.BswM通过调用LinSM_ScheduleRequest()发送调度表切换请求，LinSM通过调用LinIf_ScheduleRequest()将该请求传递到LinIf。LinIf_ScheduleRequest()返回E_NOT_OK时，LinSM将当前调度表作为入参调用BswM_LinSM_CurrentSchedule()

1.BswM sends a schedule table switching request by calling LinSM_ScheduleRequest(). LinSM transmits the request to LinIf by calling LinIf_ScheduleRequest(). When LinIf_ScheduleRequest() returns E_NOT_OK, LinSM calls BswM_LinSM_CurrentSchedule() with the current schedule table as the input parameter.

调度表切换指示：

Schedule table switching indication:

1.LinIf切换调度表时，将回调LinSM_ScheduleRequestConfirmation()，LinSM记录该通道当前的调度表，并将当前调度表作为入参调用BswM_LinSM_CurrentSchedule()

1.When LinIf switches the schedule table, it will call back LinSM_ScheduleRequestConfirmation(). LinSM records the current schedule table of the channel and calls BswM_LinSM_CurrentSchedule() with the current schedule table as the input parameter.

.. attention::

   LinIf具有自动切换调度表的机制，即请求切换调度表与调度表切换指示并非一一对应，LinSM_ScheduleRequestConfirmation()被回调时不一定是因为调用过LinSM_ScheduleRequest()

   LinIf has a mechanism for automatically switching schedule tables, that is, the request to switch the schedule table does not correspond one-to-one with the schedule table switching indication. LinSM_ScheduleRequestConfirmation() may be called back not necessarily because LinSM_ScheduleRequest() has been called.

.. only:: doc_pbs

   多变体支持 Multi-variant Support
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   LinSM 支持在不同变体中：

   LinSM supports in different variants:

   1.支持配置不同的调度表
   
   1.Supports configuring different schedule tables.
   
   2.支持配置不同唤醒失败重试次数
   
   2.Supports configuring different numbers of wakeup failure retries.

偏差 Deviation
----------------------------------

1.移除ComM_BusSM_BusSleepMode()回调

1.Remove the ComM_BusSM_BusSleepMode() callback.

1.1因为Autosar在LinSM文档描述：当SLAVE通道被调用LinSM_GotoSleepIndication()且该通道请求的通信类型为COMM_NO_COMMUNICATION，则调用LinIf_GotoSleep()且返回E_OK时回调ComM_BusSM_BusSleepMode()。而在ComM文档中描述：Lin_Slave通道配置项ComMNmVariant应为SLAVE_ACTIVE，对于此种配置的通道只有当ComM_BusSM_BusSleepMode()被回调时对该通道请求COMM_NO_COMMUNICATION。两者描述冲突
   
1.1Because AUTOSAR describes in the LinSM document: When the SLAVE channel is called LinSM_GotoSleepIndication() and the communication type requested by the channel is COMM_NO_COMMUNICATION, ComM_BusSM_BusSleepMode() is called back when LinIf_GotoSleep() is called and returns E_OK. However, the ComM document describes: The configuration item ComMNmVariant for the Lin_Slave channel should be SLAVE_ACTIVE. For channels with such configuration, COMM_NO_COMMUNICATION is requested for the channel only when ComM_BusSM_BusSleepMode() is called back. The two descriptions conflict.

1.2所以LinSM中移除ComM_BusSM_BusSleepMode()回调，ComM将Lin_Slave通道配置项ComMNmVariant修改为LIGHT
   
1.2Therefore, the ComM_BusSM_BusSleepMode() callback is removed from LinSM, and ComM modifies the configuration item ComMNmVariant of the Lin_Slave channel to LIGHT.

扩展 Extension
----------------------------------
None

