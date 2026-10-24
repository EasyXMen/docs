发布日期：2026年10月24日
Release Date: October 24, 2026

# 发布说明 Release Notes

开源安全车控操作系统小满EasyXMenV26.10（简称“开源小满V26.10”）是普华基础软件基于行业国际标准全面升级的产品版本，包含通信、诊断、网络管理、标定、存储等功能，于2026年10月24日正式发布，发布内容包括全部功能协议栈的源代码，同时提供工具链的安装包以及相关的手册文档，支持的芯片平台包括恩智浦S32K148、英飞凌TC397、瑞萨RH850/U2A16等。后续，“开源小满V25.04、V25.10”将不再维护，用户可根据后文工具及工程申请地址、代码仓地址及文档仓地址，申请并体验最新版本。

EasyXMen V26.10, an open-source operating system designed for safe vehicle control, is a major product upgrade developed by iSOFT Infrastructure Software in accordance with international industry standards. It offers a wide range of functions, including communication, diagnostics, network management, calibration, and storage. Officially released on October 24, 2026, this version includes the complete source code for all functional protocol stacks, along with toolchain installation packages and accompanying manuals and technical documentation. Supported chip platforms include NXP S32K148, Infineon TC397, and Renesas RH850/U2A16, among others. Going forward, EasyXMen V25.04 and V25.10 will no longer be maintained. Users can apply for and explore the latest version through the tool and project application links, source code repository, and documentation repository provided later in this document.

## 核心亮点 Key Highlights

### 多核多分区部署方案全面升级 Comprehensive Upgrade to Multicore and Multi-Partition Deployment

StbM 支持按分区进行服务组件封装，分区划分依赖于时间基的硬件时钟。实现了时间同步服务的按分区隔离，保证各分区时间基准独立且正确，满足多分区时间敏感应用的可靠运行需求。

StbM now supports partition-specific encapsulation of service components, with partition assignments based on the hardware clocks associated with their respective time bases. This enables time synchronization services to be isolated by partition, ensuring that each partition maintains an independent and accurate time reference while meeting the reliability requirements of time-sensitive applications operating across multiple partitions.

看门狗多核实现方案升级为主从方式，多个 MainFunction 主从协同运行。多核看门狗管理职责清晰、协同有序，提升了故障监控的可靠性与灵活性，进一步增强系统的功能安全等级。

The multicore watchdog implementation has been upgraded to a master–slave architecture, with multiple MainFunction instances working together in a coordinated master–slave arrangement. With clearly defined watchdog management responsibilities and coordinated operation across multiple cores, the upgraded architecture improves the reliability and flexibility of fault monitoring, further enhancing the system's functional safety.

### 调试功能升级 Enhanced Debugging Capabilities

构建时由 SystemGenerator 自动生成 ORTI 文件，供配套调试工具读取，可直观显示系统状态、性能、任务状态以及各类 OS 对象。同时支持基于 ORTI 的 Trace 方案，用于任务调度与 Runnable的时序分析。实现与主流调试工具的无缝集成，使时序问题一目了然。

During the build process, SystemGenerator automatically generates ORTI files that can be read by compatible debugging tools, providing intuitive visibility into system status, performance, task states, and various OS objects. An ORTI-based Trace solution is also supported, enabling timing analysis of task scheduling and Runnable execution. This allows seamless integration with mainstream debugging tools, making timing issues easier to identify and analyze.

提供了 Trace 接口预埋供集成扩展，覆盖 RTE API、Runnable 实体、模式切换、SchM API、BSW 可调度实体、COM 通信事件以及 BSW 模块全部外部 API。为深度调试与性能分析提供了标准化接口，降低了二次开发成本，提升了集成灵活性。

Built-in Trace interface hooks are provided to support integration and further extension, covering RTE APIs, Runnable entities, mode switching, SchM APIs, BSW schedulable entities, COM communication events, and all external APIs exposed by BSW modules. These standardized interfaces support in-depth debugging and performance analysis, reduce the cost of secondary development, and provide greater flexibility for system integration.

### 时间同步栈全面升级 Comprehensive Upgrade to the Time Synchronization Stack

Stbm模块支持直接从 CAN 控制器获取硬件级时间戳，提升时间采集的底层精度与响应实时性。新增时间值 NvM 持久化存储功能，系统下电时自动将当前时间存储至 NvM 模块，上电后自动加载恢复，避免系统重启后出现时间回退问题。新增 Time Validation 时间校验能力，全程监控时间同步链路中各模块的数据传递状态，二是对时钟速率校正的计算结果进行有效性校验，过滤异常偏差值，保障时间同步的准确性与稳定性。新增备份时钟机制，在主时钟失效的异常场景下，可自动切换至备份时钟推算当前时间，保障全局时间基准的连续性与可用性。新增 Eth disciplinedClock 支持，支持由驱动层 / 硬件侧自主维护本地时间；新增支持时间基克隆能力，支持对现有时间基的完整上下文进行克隆，生成独立的全新时间基，可应用于时间有效性验证、反向时间同步等业务场景。新增安全时间同步机制，为时间同步全流程提供类 SecOC 级别的安全防护，保障同步报文的完整性与真实性，防范时间同步过程被篡改攻击。

The StbM module now supports direct acquisition of hardware-level timestamps from CAN controllers, improving the underlying accuracy of time acquisition and real-time responsiveness. A new NvM-based persistent time storage feature automatically saves the current time to the NvM module when the system powers down and restores the stored time upon power-up, preventing time rollback after a system restart. A new Time Validation capability continuously monitors the status of data transfers between modules throughout the time synchronization chain. It also validates the results of clock rate correction calculations, filtering out abnormal deviations to ensure accurate and stable time synchronization. A new backup clock mechanism enables the system to automatically switch to a backup clock if the primary clock fails, allowing the current time to be calculated using the backup clock and ensuring the continuity and availability of the global time reference. Support for Eth disciplinedClock has been added, allowing the driver layer or hardware to maintain local time independently. A new time base cloning capability also enables the complete context of an existing time base to be replicated, creating a new and independent time base. This capability can be applied in scenarios such as time validity verification and reverse time synchronization. A new secure time synchronization mechanism provides SecOC-like security protection throughout the entire time synchronization process, ensuring the integrity and authenticity of synchronization messages and protecting against tampering attacks during time synchronization.

CanTSyn 覆盖 CAN 域，支持 CAN 硬件时间戳、安全时间同步以及时间基准类型可配置；EthTSyn 覆盖以太网域，支持安全时间同步，并与 StbM 联动作为以太网域的时间基准。两者结合实现了对 CAN 与以太网双域的时间同步覆盖，为跨域时间敏感应用提供了统一、可靠的时间基准支撑。可按需配置时间源、依托硬件时钟提升同步精度,并通过TLS、SecOC保护同步报文,规避时间报文篡改风险,助力整车的时序安全合规。

CanTSyn provides time synchronization for the CAN domain, supporting CAN hardware timestamps, secure time synchronization, and configurable time base types. EthTSyn covers the Ethernet domain, supports secure time synchronization, and works in conjunction with StbM to establish the time reference for the Ethernet domain. Together, CanTSyn and EthTSyn provide comprehensive time synchronization coverage across both CAN and Ethernet domains, establishing a unified and reliable time reference for time-sensitive applications operating across these domains. Time sources can be configured as needed, with hardware clocks improving synchronization accuracy and TLS and SecOC protecting synchronization messages against tampering, helping ensure compliance with vehicle-level timing and security requirements.

### 存储栈能力升级 Enhanced Storage Stack Capabilities

针对域控制器关键数据存储安全与高速内存访问需求，本版本对存储栈架构进行全面升级，新增 MemAcc与 BndM模块，BndM 模块与 Dcm模块协同工作，支持面向诊断场景的大块 NvData写入。数据直接从 Flash 读取，无需构建 RAM 镜像。并采用A/B分区切换完成更新。使得诊断刷写大块数据不再占用宝贵的 RAM 资源，显著降低内存开销。A/B 分区切换机制在更新过程中保障掉电安全，避免写入中断导致的数据损坏。

To meet the requirements for secure storage of critical data and high-speed memory access in domain controllers, this release introduces a comprehensive upgrade to the storage stack architecture, including two new modules: MemAcc and BndM. The BndM module works in conjunction with the Dcm module to support large-block NvData writes for diagnostic applications. Data is read directly from Flash, eliminating the need to create a RAM image. Updates are performed through A/B partition switching. As a result, diagnostic flashing of large data blocks no longer consumes valuable RAM resources, significantly reducing memory overhead. The A/B partition switching mechanism provides power-loss protection during updates, preventing data corruption if a write operation is interrupted.

MemAcc 模块与底层 Mem 驱动协同，向上承接 Fee、Ea、BndM 的块式读、写、擦除请求，向下统一调度 Mem 驱动。实现按 AddressArea 对同一存储器件的并发访问进行读写互斥与作业排队管理。统一了存储访问入口，使多客户端并发访问互不冲突，提升了存储系统的稳定性与协作效率。

The MemAcc module works with the underlying Mem drivers, accepting block-based read, write, and erase requests from Fee, Ea, and BndM while centrally scheduling operations across the Mem drivers. It provides read/write mutual exclusion and job queue management for concurrent access to the same storage device on a per-AddressArea basis. This establishes a unified entry point for storage access, preventing conflicts between concurrent requests from multiple clients and improving the stability and coordination efficiency of the storage system.

### 国密算法支持 Support for Chinese Cryptographic Algorithms

面向智能网联汽车的合规与自主可控要求，以国密算法为核心，构建了从 ECU 到车云的全链路安全能力，具体包括三类算法：

To meet the compliance and technological independence requirements of intelligent connected vehicles, the solution establishes end-to-end security capabilities extending from ECUs to the vehicle cloud, built around Chinese SM cryptographic algorithms. These capabilities encompass three types of algorithms:

SM2（非对称算法）：支持非对称加密、数字签名与密钥交换，用于身份认证、证书验签和安全密钥协商，防止身份伪造；

SM2 (Asymmetric Cryptographic Algorithm): Supports asymmetric encryption, digital signatures, and key exchange for identity authentication, certificate signature verification, and secure key negotiation, helping prevent identity spoofing;

SM3（密码杂凑算法）：支持杂凑、HMAC 与消息摘要，用于固件和数据完整性校验，防篡改、防重放；

SM3 (Cryptographic Hash Algorithm): Supports hashing, HMAC, and message digest generation for firmware and data integrity verification, providing protection against tampering and replay attacks;

SM4（分组对称加密算法）：支持敏感数据加密、安全通信与固件加密，保障机密性。

SM4 (Symmetric Block Cipher): Supports sensitive data encryption, secure communications, and firmware encryption to ensure confidentiality.

在集成层面，国密算法与现有 Crypto 框架采用统一接口，使用户在国产化项目中能够低成本迁移集成，显著提升国产化项目的集成效率。

At the integration level, the Chinese SM cryptographic algorithms use a unified interface with the existing Crypto framework, enabling users to migrate and integrate these algorithms into projects requiring domestically developed technologies at a lower cost, significantly improving integration efficiency.

## 功能栈模块变更 Functional Stack Module Updates

**CanTp模块**：修复发送状态切换慢导致丢失ACK的问题；STMIN在换算基础上增加1周期，防止未达STMIN发送CF的问题。

**CanTp Module**: Fixed an issue where slow transmission state transitions caused ACKs to be missed; added one cycle to the converted STMIN value to prevent Consecutive Frames (CFs) from being transmitted before the required minimum separation time has elapsed.

**Dcm模块**：修复22服务的DID使用NvM情况下的错误处理；修复2F服务在切换安全级情况下的问题；修复19 02 00情况下的错误处理；修复36服务，86服务的错误处理；修复周期传输在会话切换后不停止的问题。

**Dcm Module**: Fixed error handling issues when DIDs used by Service 22 rely on NvM; resolved an issue with Service 2F when switching security levels; corrected error handling for Service 19 02 00 and Services 36 and 86; and fixed an issue where periodic transmission continued after a diagnostic session change.

**Dem模块**：支持计时去抖较大门限值情况下的低分辨率处理；修复冻结帧处理问题。

**Dem Module**: Added support for low-resolution processing when large threshold values are configured for time-based debouncing; fixed an issue with freeze-frame data handling.

**Det模块**：防止多次重入处理机制修改。

**Det Module**: Updated the reentrancy handling mechanism to prevent repeated reentrant calls.

**Fee模块**：断电保护，修复初始化无效数据处理问题。

**Fee Module**: Improved power-loss protection and fixed an issue with invalid data handling during initialization.

**Nvm模块**：修复写跳过功能在Crc值相同情况下未执行跳过的问题；修复队列处理问题。

**NvM Module**: Fixed an issue where the write-skip function failed to skip write operations when CRC values matched; resolved an issue with queue handling.

**Xcp模块**：修复高负载极限情况下DAQ上传数据一致性问题。

**Xcp Module**: Fixed a data consistency issue affecting DAQ data uploads under extreme high-load conditions.

**Com模块**：接收IPdu长度超过预期时，支持截断后继续处理。

**Com Module**: Added support for truncating received I-PDUs that exceed the expected length and continuing processing.

**PduR模块**：支持TP报文1：n的发送功能。

**PduR Module**: Added support for one-to-many (1:n) transmission of TP messages.

**ComM模块**：用户通信模式通知移至主函数周期执行，解决中断上下文调用问题；支持用户通信模式通知到SWC的失败后重试。

**ComM Module**: Moved user communication mode notifications to periodic execution within the main function, resolving issues caused by calls made in interrupt context; added retry support when communication mode notifications to SWCs fail.

**RTE模块**：新增VFB Tracing功能，支持添加各Trace事件，多Trace Client定义；新增CS通信MetaData传递及ClientIdDefinition功能，支持模型ClientIdDefinition，可自定义配置ClientId；新增异步模式切换；新增Xcp 标定数据单独映射内存段（SwAddrMethod）；新增支持LdCom_TransmitTrigger回调函数的生成，以及TriggerTransmit功能的实现；新增SR通信、Trigger、模式管理PRPort支持；实现Rte.c进行文件拆分，将Rte.c的代码按SwcType及分区进行拆分，回调函数使用单独的.c文件；E2E算法的兼容实现，新增配置文件支持PROFILE_08、PROFILE_44、PROFILE_04m、PROFILE_07m、PROFILE_08m、PROFILE_44m；ComXf 支持可选信号序列化，可对信号组（SignalGroup）内的独立信号单独执行序列化操作。

**RTE Module**: Added VFB Tracing functionality, supporting the addition of various Trace events and the definition of multiple Trace Clients; added MetaData transfer and ClientIdDefinition functionality for client-server (CS) communication, including support for model-defined ClientIdDefinition and customizable ClientId configuration; added asynchronous mode switching; added support for mapping Xcp calibration data to a dedicated memory section (SwAddrMethod); added support for generating the LdCom_TransmitTrigger callback function and implementing TriggerTransmit functionality; added support for sender-receiver (SR) communication, Trigger functionality, and mode-management PRPorts; implemented the splitting of Rte.c into separate files based on SwcType and partition, with callback functions placed in dedicated .c files; implemented compatibility support for E2E algorithms, with configuration file support added for PROFILE_08, PROFILE_44, PROFILE_04m, PROFILE_07m, PROFILE_08m, and PROFILE_44m; and added support for optional signal serialization in ComXf, allowing individual signals within a SignalGroup to be serialized independently.

**OS模块**：新增支持Barrier同步机制，允许User、RTE使用该功能进行核间同步（初始化、运行时同步等）；新增堆栈共享功能，任务可以同一片内存区域作为堆栈；新增故障管理功能，发生异常时的错误收集和输出；新增可配置内存保护功能，支持可调整区域的内存保护，更灵活的分区权限规则。

**OS Module**: Added support for the Barrier synchronization mechanism, enabling users and the RTE to perform inter-core synchronization during initialization, runtime, and other scenarios; introduced stack-sharing functionality, allowing multiple tasks to share the same memory region for their stacks; added fault management capabilities to collect and report errors when exceptions occur; and introduced configurable memory protection, supporting memory protection for adjustable regions and more flexible partition access permission rules.

## 工具及工程申请地址 Tool and Project Application Links

- [开源小满开发平台](https://easyxmen.com/welcome.html?channel=3)：面向全球 OEM、Tier1 及行业伙伴，提供专业工程化支撑，助力缩短开发周期、降低开发成本，加速向量产平滑过渡。（内含BSW及SWC工具、代码及配置工程等）  
   [EasyXMen Development Platform](https://easyxmen.com/welcome.html?channel=3): Designed for OEMs, Tier 1 suppliers, and industry partners worldwide, the platform provides professional engineering support to help shorten development cycles, reduce development costs, and accelerate a smooth transition to mass production. (Includes BSW and SWC tools, source code projects, configuration projects, and other resources.)

- [开源小满学习版](https://easyxmen.com/welcome_rm.html?channel=3)：推荐场景为个人学习、院校/机构教学、初步功能评估。如需用于实际项目，建议申请[开源小满开发平台](https://easyxmen.com/welcome.html?channel=3)。（内含BSW工具、代码及配置工程等）  
   [EasyXMen Learning Edition](https://easyxmen.com/welcome_rm.html?channel=3): Recommended for individual learning, teaching at educational institutions and training organizations, and preliminary functional evaluation. For use in actual development projects, users are advised to apply for access to the [EasyXMen Development Platform](https://easyxmen.com/welcome.html?channel=3). (Includes BSW tools, source code projects, configuration projects, and other resources.)

## 代码仓地址 Source Code Repository

https://atomgit.com/easyxmen/XMen

## 文档仓地址 Documentation Repository
https://atomgit.com/easyxmen/docs

- 快速预览（Quick Preview）：https://easyxmen.atomgit.com/







