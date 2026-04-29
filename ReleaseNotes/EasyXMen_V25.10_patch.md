发布日期：2026年04月29日  
Release date: April 29, 2026  

# 发布说明 Release Note

开源安全车控操作系统小满EasyXMenV25.10-patch（简称“开源小满V25.10-patch”）是普华基础软件基于行业国际标准全面升级的产品版本，包含通信、诊断、网络管理、标定、存储等功能，于2026年4月29日正式发布，发布内容包括全部功能协议栈的源代码，同时提供工具的免费使用安装包以及相关的手册文档，支持的芯片平台包括恩智浦S32K148、英飞凌TC397、瑞萨RH850/U2A16。后续，“开源小满V25.10”将不再维护，用户可根据后文工具申请地址、代码地址及文档地址，申请并体验最新版本。

Open Source Safety Vehicle Control Operating System EasyXMenV25.10-patch ("EasyXMen V25.10-patch") is a comprehensive upgraded product version by iSOFT INFRASTRUCTURE SOFTWARE CO., LTD. based on the international industry standards, including communication, diagnosis, network management, calibration, storage, etc. It will be officially released on April 29, 2026. The released content includes the source code of all functional protocol stacks, and also provides free tool installation packages and relevant manuals and documents. Supported chip platforms include NXP S32K148, Infineon TC397 and Renesas RH850/U2A16. Going forward, "EasyXMen V25.10" will no longer be maintained. Users may apply for and experience the latest version via the tool application address, code repository address, and documentation repository address provided below.

## Bug fixes

本次补丁版本主要聚焦安全车控操作系统功能栈模块的缺陷修复与能力优化，涉及BswM、CanIf、CanNm、CanTp、CanSM、Com、Crypto、Dcm、Dem、DoIP、EcuM、EthTSyn、Fee、IpduM、KeyM、LinIf、LinSM、Nm、OS、SoAd、StbM、TcpIp、UdpNm、XCP 等核心模块。通过本次缺陷修复与优化，显著提升了基础软件平台的运行稳定性和可靠性，可实现用户从 V25.10 基础版本的平滑升级，充分满足车载ECU量产场景的高可靠运行要求。

This patch release focuses primarily on bug fixes and performance optimizations for functional stack modules of the safety vehicle control operating system, covering core modules including BswM, CanIf, CanNm, CanTp, CanSM, Com, Crypto, Dcm, Dem, DoIP, EcuM, EthTSyn, Fee, IpduM, KeyM, LinIf, LinSM, Nm, OS, SoAd, StbM, TcpIp, UdpNm and XCP. These bug fixes and optimizations significantly enhance the operational stability and reliability of the basic software platform, enabling users to perform a smooth upgrade from the V25.10 base version and fully satisfying the high-reliability operation requirements of mass-production scenarios for automotive ECUs.

**BswM模块（BswM module）：**

- 修复BswM初始化SOAD模块宏定义开关不一致，NVM生成BlockId宏定义错误，NM通道ID错误问题；  
It fixes the issues that the macro switches for SOAD module initialization are inconsistent in BswM, that the generated NVM BlockId macro definition is incorrect, and that the NM channel ID is invalid.

**CanIf模块（CanIf module）：**

- 修复CanIfTriggerTransmitSupport宏打开问题；  
It fixes the issue that exceptions occur when the CanIfTriggerTransmitSupport macro is enabled.

**CanNm模块（CanNm module）：**

- 修复const类型指针赋值给指针变量userDataPtr问题；  
It fixes the issue that a const-type pointer is assigned to the pointer variable userDataPtr.

- 修复CanNm_TxConfirmation 补充返回值为 FALSE时逻辑问题；  
It fixes the logical issue when the return value of CanNm_TxConfirmation is set to FALSE;

- CanNm_BusSleepStateHandle上报被动唤醒事件判断条件修正；  
It corrects the judgment condition for passive wake-up event reporting in CanNm_BusSleepStateHandle.

**CanTp模块（CanTp module）：**

- 修复关闭CanTpChangeParameterAp时报错问题；  
It fixes the issue that errors are reported when CanTpChangeParameterAp is disabled.

**CanSM模块（CanSM module）：**

- 修复CanSM代码CanSM_ValidateNetworkParition函数入参错误问题；  
It fixes the issue that the input parameter of the CanSM_ValidateNetworkParition function in the CanSM module is incorrect.

**Com模块（CanSM module）：**

- 修复COM-event报文使用Com_TriggerIPDUSend周期发送，断开CAN设备再连接，该报文无法继续发送问题；  
It fixes the issue that COM-event messages sent periodically using Com_TriggerIPDUSend fail to resume transmission after the CAN device is disconnected and reconnected.

**Crypto模块（Crypto module）：**

- 修复Hash算法olen溢出风险，更新返回值长度，在bufferlen不足时截断返回数据,解决ripemd160生成结果错误问题  
It fixes the overflow risk of the olen in Hash algorithms, updates the return value length, truncates the returned data when the bufferlen is insufficient, and resolves the issue of incorrect ripemd160 results;

- 修复aes不同工作模式下都没有返回正确计算结果长度问题；  
It fixes the issue that the correct calculation result length is not returned for aes in different operation modes;

- 修复配置HMAC-SHA256进trap问题；  
It fixes the issue that a trap is triggered when HMAC-SHA256 is configured;

- 修复RSA-OEAP-SHA1算法执行失败问题；  
It fixes the issue that the RSA-OEAP-SHA1 algorithm fails to execute;

- 修复VerifyHmac resultLength找不到的问题；  
It fixes the issue that resultLength cannot be found in VerifyHmac;

- 修复3DES没有密钥输入问题；  
It fixes the issue that no key is input for 3DES.

**Dcm模块（Dcm module）：**

- 修复请求2A 01 时发送周期错误问题；  
It fixes the issue that the transmission period is incorrect for 2A 01 requests;

- 修复服务的正响应抑制配置支持问题；  
It fixes the issue of configuration support for positive response suppression;

- 修复DCM正响应抑制问题；  
It fixes the issue of positive response suppression in DCM;

- 修复动态长度DID长度校验错误；  
It fixes the issue of incorrect length verification for dynamic-length DIDs;

- 修复在1904,1906服务中，无效的DTCSnapshotRecordNumber/DTCExtDataRecordNumber也会正响应问题；  
It fixes the issue that positive responses are returned for invalid DTCSnapshotRecordNumber/DTCExtDataRecordNumber in services 1904 and 1906;

- 修复请求编程会话DcmDspSessionForBoot=DCM_SYS_BOOT下未执行复位和boot跳转时没有响应NRC10问题；  
It fixes the issue that NRC10 is not returned when no reset or boot jump is performed under DCM_SYS_BOOT with DcmDspSessionForBoot configured during a programming session request;

- 修复UDS85服务使能ControlOptionRecord，请求的GroupOfDTC不正确回复NRC22问题；  
It fixes the issue that NRC22 is incorrectly returned for an invalid GroupOfDTC when ControlOptionRecord is enabled in UDS service 85;

- 修复未配置DCM_DDDID_CHECK_SOURCE且配置了2A和2C服务时编译报错问题；  
It fixes the issue that compilation errors occur when services 2A and 2C are configured without DCM_DDDID_CHECK_SOURCE;

- 修复在已经激活IO控制时，切换到默认会话下没有执行恢复ECU控制问题；  
It fixes the issue that ECU control is not restored in the default session when IO control is activated;

- 修复DoIP发送公告的时候VIN/GID同步失败，Dcm_GetVin接口返回值错误问题；  
It fixes the issue that VIN/GID synchronization fails and the return value of the Dcm_GetVin interface is incorrect when DoIP sends announcement messages;

- 修复2A和2c相关问题,2A增加读取PDID；  
It fixes issues related to services 2A and 2C, and adds support for PDID reading in service 2A;

- 修复当DID配置从nvm读取时，当nvm返回notok时，应回复NRC22问题；  
It fixes the issue that NRC22 is not returned when NVM returns notok while reading DID configuration from NVM;

- 修复DCM中28服务和22服务处理异常问题；  
It fixes the issue of abnormal processing of services 28 and 22 in DCM;

- 修复2A服务请求的PDID为动态DID，但该动态DID未被定义时，期望DCM恢复7F 2A 31,但反馈正响应问题；  
It fixes the issue that DCM returns a positive response instead of the expected 7F 2A 31 when the requested PDID in service 2A is an undefined dynamic DID.

**Dem模块（Dem module）：**

- 添加memoryIndex的无效索引值判断；  
It adds the judgment for invalid index values of memoryIndex;

- 修复处理未配置冻结帧编译报错问题；  
It fixes the issue that compilation errors occur when processing unconfigured freeze frames;

- 更新Dem_GetSizeOfExtendedDataRecordSelection函数处理逻辑；  
It updates the processing logic of the Dem_GetSizeOfExtendedDataRecordSelection function;

- 更新faile cycle counter的处理逻辑；  
It updates the processing logic of the faile cycle counter.

**DoIP模块（DoIP module）：**

- 修复激活路由后，当ECU发送未知的payload此时会回正确的NACK，但之后的任何类型的DoIP请求都无响应问题；  
It fixes the issue that the ECU returns a correct NACK for an unknown payload after routing activation but fails to respond to any subsequent DoIP requests;

- 修复DoIP队列发送问题回归的临界区不配套问题；  
It fixes the issue that mismatched critical sections occur due to regression in DoIP queue transmission.

**EcuM模块（EcuM module）：**

- 将SleepMode设置为非必配项；  
It sets SleepMode as a non-mandatory configuration item;

- 修复EcuMDriverRestartList不生成问题，修复CoreId映射问题，修复初始化Pb结构体可能出现重名的问题；修复timer状态未清除的问题；  
It fixes the issues that the EcuMDriverRestartList is not generated, that the CoreId mapping is incorrect, that duplicate names may exist in the initialized Pb structure, and that the timer state is not cleared;

- 修改获取时间的临时变量为克隆变量；  
It replaces the temporary variable for time acquisition with a clone variable;

- 修复EcuM唤醒源验证完成后未停止Timer的问题；  
It fixes the issue that the timer is not stopped after EcuM wake-up source verification is completed.

**EthTSyn模块（EthTSyn module）：**

- 修正EthTSyn模块的Module Id问题；  
It fixes the issue that the Module Id of the EthTSyn module is incorrect.

**Fee模块（Fee module）：**

- 修复更新换页后复位，数据不一致问题；  
It fixes the issue of data inconsistency after a reset following page replacement.

**IpduM模块（IpduM module）：**

- 修复TxReqest中UnusedDefaultValue会作为信号初始值的问题；  
It fixes the issue that UnusedDefaultValue in TxRequest is used as the initial signal value.

**KeyM模块（KeyM module）：**

- 修复证书签名验签时tbs长度不对导致校验失败问题；  
It fixes the issue that certificate signature verification fails due to an incorrect tbs length.

**LinIf模块（LinIf module）：**

- 修复 LinTp 接收到 SID 为 0x7F 且第 4 字节为 0x78 的 SRF 应答帧时，在 P2Max 定时器到期前再次接收到 LinTp 发送请求可能导致 PduR 路由功能卡死的问题；  
It fixes the issue that repeated LinTp transmission requests received before the P2Max timer expires may cause PduR routing to freeze when LinTp receives an SRF response frame with SID 0x7F and the fourth byte 0x78;

- 修复 LinTp 模块在物理请求的发送阶段未结束时，连续发送两次功能寻址请求导致功能寻址无法发送的问题；  
It fixes the issue that functional addressing fails to be sent when two consecutive functional addressing requests are sent before the physical request transmission phase of the LinTp module is completed;

- 修复 LINTP 进入 P2MAX 阶段后，无持续 3D 报文外发导致从节点无法响应数据的问题；  
It fixes the issue that slave nodes cannot respond with data due to the absence of continuous 3D messages after LINTP enters the P2MAX phase;

- 修复 LinIf 模块的主节点未被配置为对应通道的 LinTp 节点时，仍会调用 LinTp_HandleTimers，进而导致通道 ID 为 0 的 LinTp 主节点定时器计时精度异常的问题；  
It fixes the issue that LinTp_HandleTimers is still called when the master node of the LinIf module is not configured as the LinTp node of the corresponding channel, leading to abnormal timing accuracy of the LinTp master node with channel ID 0.

**LinSM模块（LinSM module）：**

- 增加LinSlave在唤醒状态无法休眠条件；  
It adds the condition that prevents LinSlave from entering sleep mode in the wake-up state.

**Nm模块（Nm module）：**

- 修复Nm_InnerClusterType只能保存8个通道的状态的的问题；  
It fixes the issue that Nm_InnerClusterType can only store the status of 8 channels;

- 修复Nm_RepeatMessageIndication和Nm_TxTimeoutException应由用户实现，定义不应放在源码中的问题；  
It fixes the issue that Nm_RepeatMessageIndication and Nm_TxTimeoutException, which shall be implemented by the user, are incorrectly defined in the source code;

- 修复Nm_StateType中NM_STATE_OFFLINE值与Autosar规范不同问题；  
It fixes the issue that the value of NM_STATE_OFFLINE in Nm_StateType is inconsistent with the Autosar specification.

**OS模块（OS module）：**

- 修复开启ErrorHook后，OSError_Save_ShutDownOs编译报错问题；  
It fixes the issue that compilation errors occur in OSError_Save_ShutDownOs after ErrorHook is enabled.

**SoAd模块（SoAd module）：**

- 修复对接收buffer读写位置不一致的问题；  
It fixes the issue that the read and write positions of the receive buffer are inconsistent;

- 修复覆盖率测试SoAd_GetBestMatchAlgorithmSoCon和SoAd_IfSpecificRoutingGroupTransmit无法全覆盖的问题；  
It fixes the issue that full coverage cannot be achieved for SoAd_GetBestMatchAlgorithmSoCon and SoAd_IfSpecificRoutingGroupTransmit in coverage testing;

- 修复SoAd_IfTransmit,SoAd_IfRoutingGroupTransmit和SoAd_IfSpecificRoutingGroupTransmit问题；对于TP接收关闭连接时更新TCP窗口；  
It fixes the issues in SoAd_IfTransmit, SoAd_IfRoutingGroupTransmit and SoAd_IfSpecificRoutingGroupTransmit, and updates the TCP window when closing a connection for TP reception;

- 修复SoAd_CopyTxData中调用TpTxConfimatin是包在临界区的问题和释放远端地址标识未修改的问题；  
It fixes the issues that the call of TpTxConfirmation in SoAd_CopyTxData is wrapped in a critical section and that the remote address identifier is not modified upon release.

**StbM模块（StbM module）：**

- 修复StbM_MeasurementType 依赖以太网栈提供的Eth_RateDevationType的问题；  
It fixes the issue that StbM_MeasurementType depends on the Eth_RateDevationType provided by the Ethernet stack.

**TcpIp模块（TcpIp module）：**

- 修复全局状态变量读取问题；  
It fixes the issue with reading global state variables.

**UdpNm模块（UdpNm module）：**

- 修复若被动唤醒时，就第一帧NM报文中CBV的repeatmessagebit置1时，会进入repeat状态2次问题；  
It fixes the issue that the repeat state is entered twice when the repeatmessagebit of the CBV in the first NM frame is set to 1 during passive wake-up.

**XCP模块（XCP module）：**

- 修复Xcp_KeyHandler的以太网包计数问题；  
It fixes the issue that the Ethernet packet count of Xcp_KeyHandler is incorrect;

- 修复XCPOnEth中Xcp_SoAdTxConfirmation缺少参数问题；  
It fixes the issue that parameters are missing in Xcp_SoAdTxConfirmation for XCPOnEth.

## 兼容性说明 Compatibility statement

“开源小满V25.10_patch”属于“开源小满V25.10”Bug迭代修复版本，遵循同一国际标准版本，在配置方面，模块配置的Arxml文件在两个版本的BSW Configurator工具中可以相互通用。

"EasyXMen V25.10_patch" is an iterative bug fix release of EasyXMen V25.10, based on the same international standard. In terms of configuration, module configuration ARXML files are fully interchangeable between the BSW Configurator tools of the two versions.

## 工具申请地址 Tool application Address

https://register.easyxmen.com/welcome.html?channel=3

## 代码仓地址 Code Repository Address

https://atomgit.com/easyxmen/XMen

## 文档仓地址 Documentation Repository Address

https://atomgit.com/easyxmen/docs

- 快速预览（Instant view the page at）：https://easyxmen.atomgit.com/V25.10/index.html
