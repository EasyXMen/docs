发布日期：2026年04月29日  
Release date: April 29, 2026  

# 发布说明 Release Note

开源安全车控操作系统小满EasyXMenV25.04-patch（简称“开源小满V25.04-patch”）是普华基础软件基于行业国际标准全面升级的产品版本，包含通信、诊断、网络管理、标定、存储等功能，于2026年4月29日正式发布，发布内容包括全部功能协议栈的源代码，同时提供工具的免费使用安装包以及相关的手册文档，支持的芯片平台包括恩智浦S32K148、英飞凌TC397、瑞萨RH850/U2A16。后续，“开源小满V25.04”将不再维护，用户可根据后文工具申请地址、代码地址及文档地址，申请并体验最新版本。

Open Source Safety Vehicle Control Operating System EasyXMenV25.04-patch ("EasyXMen V25.04-patch") is a comprehensive upgraded product version by iSOFT INFRASTRUCTURE SOFTWARE CO., LTD. based on the international industry standards, including communication, diagnosis, network management, calibration, storage, etc. It will be officially released on April 29, 2026. The released content includes the source code of all functional protocol stacks, and also provides free tool installation packages and relevant manuals and documents. Supported chip platforms include NXP S32K148, Infineon TC397 and Renesas RH850/U2A16. Going forward, "EasyXMen V25.04" will no longer be maintained. Users may apply for and experience the latest version via the tool application address, code repository address, and documentation repository address provided below.

# Bug fixes

本次补丁版本主要聚焦安全车控操作系统功能栈模块的缺陷修复与能力优化，涉及 CanIf、CanTp、Com、Dcm、Dem、DoIP、EthIf、LinIf、OS、SoAd、EcuM、WdgM 等数十个核心模块。通过本次缺陷修复与优化，显著提升了基础软件平台的运行稳定性和可靠性，可实现用户从 V25.04 基础版本的平滑升级，充分满足车载ECU量产场景的高可靠运行要求。

This patch release focuses primarily on bug fixes and performance optimizations for functional stack modules of the safety vehicle control operating system, covering dozens of core modules including CanIf, CanTp, Com, Dcm, Dem, DoIP, EthIf, LinIf, OS, SoAd, EcuM and WdgM. These bug fixes and optimizations significantly enhance the operational stability and reliability of the basic software platform, enabling users to perform a smooth upgrade from the V25.04 base version and fully satisfying the high-reliability operation requirements of mass-production scenarios for automotive ECUs.

**CanIf模块（CanIf module）：**  

- 修复未配置对应 TxBuffer 的 Pdu 仍会被 CanIf_TransmitBufferedPdu 函数访问，进而导致 Buffer 数组越界访问的问题。  
It fixes the issue that PDUs with no corresponding TxBuffer configured are still accessed by the CanIf_TransmitBufferedPdu function, resulting in out-of-bounds access to the buffer array.

**CanNm模块（CanNm module）：**

- 修复Repeatmessage请求可能被接受但不处理问题。  
It fixes the issue that Repeatmessage requests may be accepted but not processed.


**CanTp模块（CanTp module）：**

- 修复FF_DL长度有误但未溢出时，响应OVFL流控问题；  
It fixes the issue that an OVFL flow control response is sent when the FF_DL length is incorrect but not overflowed;

- 修复CanTp发送连续帧时，第一帧时间过长大于CS时间问题；  
It fixes the issue that the duration of the first frame exceeds the CS time when CanTp sends consecutive frames;

- 修复当PduLengthType为uint16或者uint8时， FF_DL 存在截断风险的问题；  
It fixes the issue that FF_DL is at risk of truncation when PduLengthType is set to uint16 or uint8;

- 修复 CanTp_ChangeParameter 修改的属性只会生效一次，以及在接收过程中 BS 不固定的问题。  
It fixes the issue that attributes modified by CanTp_ChangeParameter take effect only once and the BS value is unstable during reception.

**Com模块（Com module）：**

- 修复DirectWithoutRepetition型Pdu，无TxConfirmation时被一直请求发送问题；  
It fixes the issue that DirectWithoutRepetition PDUs are continuously requested for transmission when no TxConfirmation is received;

- 修复Com在上一帧发送没有收到底层的TxConfirmation不能再发送报文的问题，同步调整配置工程仅有Tx的情况下编译不过的问题。  
It fixes the issue that Com cannot send messages if no lower-layer TxConfirmation is received for the previous frame transmission, and resolves the issue that the configuration project fails to compile when only Tx is configured.

**ComM模块（ComM module）：**

- 修复连续调用ComM_RequestComMode请求通道COMM_NO_COMMUNICATION时出现异常问题。  
It fixes the issue that an exception occurs when ComM_RequestComMode is called continuously to request COMM_NO_COMMUNICATION for a channel.

**Crypto模块（Crypto module）：**

- 修复随机数生成不变化问题。  
It fixes the issue that generated random numbers remain unchanged.

**Dcm模块（Dcm module）：**

- 添加 Pdu 功能寻址长度检查，修复给 ECU 发送 64 字节以太网功能寻址 SF 时 ECU 不路由的问题；  
It adds a length check for PDU functional addressing, and fixes the issue that the ECU does not route when receiving 64-byte Ethernet functional addressing SFs;

- 修复跨核中断中调用Rte_Call导致死锁问题；  
It fixes the issue that a deadlock occurs due to the invocation of Rte_Call in cross-core interrupts;

- 修复Dcm的发送请求会在多核情况下出现意外多次调用问题；  
It fixes the issue that Dcm transmission requests are unexpectedly called multiple times in multi-core scenarios;

- 修复当 DcmDslDiagRespMaxNumRespPend 配置为 0 时，代码仍允许持续发送 78 响应而非禁止发送的问题；  
It fixes the issue that the code still allows continuous 78 responses instead of prohibiting transmission when DcmDslDiagRespMaxNumRespPend is configured as 0;

- 修复Dcm_SetProgConditions接口原型错误问题；  
It fixes the issue that the interface prototype of Dcm_SetProgConditions is incorrect;

- 修复2E服务写入动态长度DID时功能异常及工具生成问题；  
It fixes the issue of functional abnormality and tool generation errors when writing dynamic-length DIDs through the 2E service;

- 修复使用可变参数，可变参数长度计算错误问题。  
It fixes the issue that the length of variable arguments is calculated incorrectly when variable arguments are used.

**Dem模块（Dem module）：**

- 修复当DEM_ENABLE_SOFT_FILTER_OF_PASS开启的时候，缺少过滤条件问题；  
It fixes the issue that filter conditions are missing when DEM_ENABLE_SOFT_FILTER_OF_PASS is enabled;

- 修复处理读扩展数据读取异常问题；  
It fixes the issue that an exception occurs during extended data reading processing;

- 修复Dem模块PermanentMemory和内部数据的处理问题；  
It fixes the issue of abnormal processing of PermanentMemory and internal data in the Dem module;

- 删除NvM模块冗余块恢复使用的Ram区，优化Ram使用。增加一个OBD事件用于0A服务测试；  
It removes the redundant RAM area used for block recovery in the NvM module to optimize RAM usage; It adds an OBD event for 0A service testing;

- 调整结构体定义，修改计算NvM的size需求。  
It adjusts structure definitions and modifies the size calculation logic for NvM.

**DoIP模块（DoIP module）：**

- 修复路由激活报文中 Protocol Version 为 FF 默认值时可正常激活的问题；  
It fixes the issue that normal routing activation is allowed when the Protocol Version in routing activation messages is set to the default value FF;

- 修复路由激活后，ECU 发送 Alive Check Response 导致后续任何 DoIP 请求无响应的问题。  
It fixes the issue that the ECU sends an Alive Check Response after routing activation, resulting in no response to any subsequent DoIP requests.

**Dlt模块（Dlt module）：**

- 修复Dlt未使能StbM计时时编译报错问题。  
It fixes the issue that a compilation error occurs when StbM timing is not enabled in Dlt.

**E2E模块（E2E module）：**

- 修复 Xfrm 模块中配置 dataIdMode 为 NOTUSED 后，E2E_P01CheckDataIDMode 无法通过检测的问题。  
It fixes the issue that E2E_P01CheckDataIDMode fails to pass detection after dataIdMode is configured as NOTUSED in the Xfrm module.

**EcuM模块（EcuM module）：**

- 修复 EcuM AlarmClock 相关接口找不到返回值的问题；  
It fixes the issue that return values are missing for EcuM AlarmClock-related interfaces;

- 修复 EcuM_AbortWakeupAlarm 缺少 ECUM_E_NOT_ACTIVE 返回值的问题；  
It fixes the issue that the ECUM_E_NOT_ACTIVE return value is missing in EcuM_AbortWakeupAlarm;

- 修复单核 modehandling 失效问题。  
It fixes the issue that single-core modehandling is invalid.

**EthIf模块（EthIf module）：**

- 修复VALN情况下，首次调用EthIf_SetControllerMode且传入的CtrlIdx大于0时，向EthSM通知时的CtrlIdx错误的问题；  
It fixes the issue that an incorrect CtrlIdx is reported to EthSM when EthIf_SetControllerMode is called for the first time with a CtrlIdx greater than 0 in VALN scenarios.

**IStdLib模块（IStdLib module）：**

- 修复usedsize在开辟清除时大小不一致的问题；  
It fixes the issue that the usedsize is inconsistent during memory allocation and deallocation.

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

- 修复 LinSlave 通道状态机若无 LinMaster 支持则卡死无法休眠的问题；  
It fixes the issue that the LinSlave channel state machine freezes and cannot enter sleep mode without LinMaster support;

- 增加配置项 LinSMOverwritePendingScheduleRequest；  
It adds the configuration item LinSMOverwritePendingScheduleRequest.

**Nvm模块（NvM module）：**

- 删除NvM模块冗余块恢复使用的Ram区，优化Ram使用；  
It removes the redundant RAM area used for block recovery in the NvM module to optimize RAM usage.

**OS模块（OS module）：**

- 修复同步IOC回调被打断后AppId被篡改的问题；  
It fixes the issue that the AppId is tampered with after a synchronous IOC callback is interrupted;

- 工具删除shell功能后同步修改内核；  
It synchronizes kernel modifications after the shell function is removed from the tool.

**PduR模块（PduR module）：**

- 修复由于 PduR_DestinationRouteStatus 状态转换落后于 CopyTxData 调用，导致以太网获取不到数据进而使网关断开连接的问题；  
It fixes the issue that the Ethernet gateway disconnects due to unavailable data caused by the delayed state transition of PduR_DestinationRouteStatus relative to the call of CopyTxData.

**Sd模块（Sd module）：**

- 修复服务器在短时间内收到多个针对自身的订阅报文时，无法向先订阅的客户端发送初始事件的问题；  
It fixes the issue that the server fails to send initial events to earlier subscribed clients when receiving multiple subscription messages targeting itself within a short period;

- 修复服务器检查到客户端重启后，错误地将该客户端订阅服务下的所有事件订阅者全部删除的问题；  
It fixes the issue that the server incorrectly deletes all event subscribers under the subscribed service for a client after detecting the client’s restart.

**SoAd模块（SoAd module）：**

- 修复NPdu功能发送错误数据的问题；  
It fixes the issue that incorrect data is sent in NPdu functions;

- 修复SoAd_PduBuffer在存入8字节数据的情况下，buffer的指针更新异常问题；  
It fixes the issue that the pointer of SoAd_PduBuffer is updated abnormally when 8-byte data is stored;

- 修复 SoAd_CopyTxData 中调用 TpTxConfirmation 被包在临界区的问题，以及释放远端地址标识未修改的问题；  
It fixes the issues that the call of TpTxConfirmation in SoAd_CopyTxData is wrapped in a critical section and that the issue that the remote address identifier is not modified upon release.

- 修改 IF 类型的拷贝发送数据逻辑；  
It modifies the data copy and transmission logic for IF types.

**TcpIp模块（TcpIp module）：**

- 修复启用IP_FORCE_FLAG_DF标志位后，checksum计算错误的问题；  
It fixes the issue that the checksum is calculated incorrectly after the IP_FORCE_FLAG_DF flag is enabled.

**Tm模块（Tm module）：**

- 修复100us32bit和1ms32bit接口开关宏定义不同步的问题；  
It fixes the issue that the switch macro definitions for 100us32bit and 1ms32bit interfaces are out of sync.

**UdpNm模块（UdpNm module）：**

- 修复const类型指针赋值给指针变量userDataPtr问题；  
It fixes the issue that a const-type pointer is assigned to the pointer variable userDataPtr.

**WdgM模块（WdgM module）：**

- 修复WdgM逻辑计算不正确的问题，增加多MainFunction支持，修复段映射错误问题；  
It fixes the issue that the WdgM logic calculation is incorrect, adds support for multiple MainFunction calls, and fixes the issue that segment mapping errors occur.


## 兼容性说明 Compatibility statement

“开源小满V25.04_patch”属于“开源小满V25.04”Bug迭代修复版本，遵循同一国际标准版本，在配置方面，模块配置的Arxml文件在两个版本的BSW Configurator工具中可以相互通用。

"EasyXMen V25.04_patch" is an iterative bug fix release of EasyXMen V25.04, based on the same international standard. In terms of configuration, module configuration ARXML files are fully interchangeable between the BSW Configurator tools of the two versions.

## 工具申请地址 Tool application Address

https://register.easyxmen.com/welcome.html?channel=3

## 代码仓地址 Code Repository Address

https://atomgit.com/easyxmen/XMen

## 文档仓地址 Documentation Repository Address

https://atomgit.com/easyxmen/docs

- 快速预览（Instant view the page at）：https://easyxmen.atomgit.com/index.html