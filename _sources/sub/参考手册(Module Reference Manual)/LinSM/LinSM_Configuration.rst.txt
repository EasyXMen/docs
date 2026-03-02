配置 Configuration
====================================

唤醒超时计时器 Wakeup Timeout Timer
------------------------------------------------------------------------------------------------------------------

Lin通道在启动Wake up进程时需要加载的超时计时器以及重试计数器根据配置决定超时计时器各通道间独立配置，配置项位于LinSMChannel/LinSMConfirmationTimeout。该配置参数为浮点型，范围大小为[0 ..INF]，单位为秒。计时器在周期性调度函数LinSM_MainFunction()中递减，所以建议实际值为主函数运行周期的整数倍。当该值配置为0时意为永不会触发超时。

The timeout timer and retry counter that the Lin channel needs to load when starting the Wake up process are determined by configuration.The timeout timer is configured independently for each channel, and the configuration item is located at LinSMChannel/LinSMConfirmationTimeout. This configuration parameter is of floating-point type, with a range of [0 .. INF] in seconds. The timer decrements in the periodic scheduling function LinSM_MainFunction(), so it is recommended that the actual value be an integer multiple of the main function running period. When this value is configured as 0, it means that the timeout will never be triggered.

1.LinSMConfirmationTimeout配置截图：(单位：s，参数值要大于唤醒命令在Lin通道上的传播时间)

1.Screenshot of LinSMConfirmationTimeout configuration: (Unit: s, the parameter value must be greater than the propagation time of the wakeup command on the Lin channel)

.. figure:: ../../../_static/参考手册/LinSM/LinSMConfirmationTimeout.png
   :alt: LinSMConfirmationTimeout的图片 (Image of LinSMConfirmationTimeout)
   :align: center

   fig_LinSMConfirmationTimeout

- LinSMMainProcessingPeriod配置截图：(单位：s)
- Screenshot of LinSMMainProcessingPeriod configuration: (Unit: s)

.. figure:: ../../../_static/参考手册/LinSM/LinSMMainProcessingPeriod.png
   :alt: LinSMMainProcessingPeriod的图片 (Image of LinSMMainProcessingPeriod)
   :align: center

   fig_LinSMMainProcessingPeriod

唤醒失败重试次数由全局性配置LinSMConfigSet/LinSMModeRequestRepetitionMax决定

The number of wakeup failure retries is determined by the global configuration LinSMConfigSet/LinSMModeRequestRepetitionMax.

1.LinSMModeRequestRepetitionMax配置截图：

1.Screenshot of LinSMModeRequestRepetitionMax configuration:

.. figure:: ../../../_static/参考手册/LinSM/LinSMModeRequestRepetitionMax.png
   :alt: LinSMModeRequestRepetitionMax的图片 (Image of LinSMModeRequestRepetitionMax)
   :align: center

   fig_LinSMModeRequestRepetitionMax

调度表配置 Schedule Table Configuration
------------------------------------------------------------------------------------------------------------------

调度表配置位于各通道的配置下子容器：LinSMChannel/LinSMSchedule，调度表配置以及相应函数功能仅支持MASTER节点，使用调度表配置需要先将通道类型LinSMChannel/LinSMNodeType配置为MASTER

The schedule table configuration is located in the sub-container under the configuration of each channel: LinSMChannel/LinSMSchedule. The schedule table configuration and corresponding function features only support MASTER nodes. To use the schedule table configuration, the channel type (LinSMChannel/LinSMNodeType) must first be configured as MASTER.

1.LinSMNodeType配置截图：(下拉框选择配置参数)

1.Screenshot of LinSMNodeType configuration: (Select configuration parameters from the drop-down box)

.. figure:: ../../../_static/参考手册/LinSM/LinSMNodeType.png
   :alt: LinSMNodeType的图片 (Image of LinSMNodeType)
   :align: center

   fig_LinSMNodeType

LinSMChannel/LinSMSchedule容器中，LinSMScheduleIndex依次递增自动配置，供以BswM请求调度表切换使用，范围[0 ..255]; LinSMScheduleIndexRef引用LinIf模块LinIfScheduleTable配置。

In the LinSMChannel/LinSMSchedule container, LinSMScheduleIndex is automatically configured in increasing order and is used for BswM to request schedule table switching, with a range of [0 .. 255]; LinSMScheduleIndexRef references the LinIf module's LinIfScheduleTable configuration.

1.LinSMSchedule配置截图

1.Screenshot of LinSMSchedule configuration

.. figure:: ../../../_static/参考手册/LinSM/LinSMSchedule.png
   :alt: LinSMSchedule的图片 (Image of LinSMSchedule)
   :align: center

   fig_LinSMSchedule

1.LinSMScheduleIndexRef引用的来源：LinIfScheduleTable

1.Source referenced by LinSMScheduleIndexRef: LinIfScheduleTable

.. figure:: ../../../_static/参考手册/LinSM/LinIfScheduleTable.png
   :alt: LinIfScheduleTable的图片 (Image of LinIfScheduleTable)
   :align: center

   fig_LinIfScheduleTable