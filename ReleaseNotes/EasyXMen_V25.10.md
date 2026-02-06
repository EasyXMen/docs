发布日期：2025年10月25日
Release date: October 25, 2025

# 发布说明 Release Note

开源安全车控操作系统小满EasyXMenV25.10（简称“开源小满V25.10”）是普华基础软件基于行业国际标准全面升级的产品版本，包含通信、诊断、网络管理、标定、存储等功能，于2025年10月24日正式发布。发布内容包括全部功能协议栈的源代码，同时还提供：1.可申请试用的工具ORIENTAIS Configurator for EasyXMen；2.基于瑞萨RH850U2A16、恩智浦S32K148和英飞凌TC397的示例工程；3.相关手册文档。用户可根据后文工具申请地址、代码仓地址及文档仓地址，申请并体验最新版本。2026年1月1日起，“开源小满V25.04”将不再维护，推荐用户下载使用最新版本，V25.04版本相关的配置工程及模块配置Arxml文件升级请见下文“兼容性说明”。**请注意升级工作必须在2025年11月24日之前完成，超过时间节点后V25.10版本的工具不再支持V25.04版本配置工程及模块配置Arxml文件的导入，无法进行升级。**

Open Source Safety Vehicle Control Operating System EasyXMenV25.10 ("EasyXMen V25.10") is a comprehensive upgraded product version by iSOFT INFRASTRUCTURE SOFTWARE CO., LTD. based on the international industry standards, including communication, diagnosis, network management, calibration, storage, etc. It was officially on October 24, 2025. The released content includes the source code of all the functional protocol stacks, as well as: 1. ORIENTAIS Configurator for EasyXMen, a tool that can be applied for trial use; 2. Example projects based on Renesas RH850U2A16, NXP S32K148, and Infineon TC397; and 3. Relevant manuals documents. Users can apply for and experience the latest version of EasyXMen according to the tool request address, code repository address, and documentation repository address in the following text. From January 01, 2026, the "EasyXMen V25.04" will no longer be maintained, and it is recommended that users download and use the latest version. Please refer to the "Compatibility statement" in the following text for the upgrade of configuration project and module configuration Arxml files related to the V25.04 version. **Please note that the upgrade work shall be completed before November 24, 2025. After this time node, tools of the V25.10 version will no longer support V25.04 version configuration projects and the import of module configuration Arxml files, and the upgrade cannot be carried out.**

## 核心亮点 Core highlights

### 多核多分区功能升级 Upgrading of multi-core and multi-zone functionality

基于V25.04版本已支持的多核多分区功能，持续提升BSW功能栈模块支持多核芯片的执行效率，进行多核功能优化升级改造，充分利用硬件的并发特性，降低单核负载率，实现实时性与资源利用率的平衡。开源小满V25.10版本在多核多分区功能在功能栈上大幅扩展，包括存储栈（NvM/ Eep/FlsTst/RamTst）、诊断栈（DEM/DCM/FIM/CanTp）、信息安全（SecOC）、I/O抽象、时间同步（StbM/CanTysn/EthTysn）、网络管理（NM/CanNm/UdpNm/EthSm/CanSm/LinSm）、WDG协议栈（WdgIf/WdgM）在内的功能栈均支持在可信分区上多核多分区部署。多核多分区功能的增强实现，进一步实现更高效的负载均衡和实时响应，提升系统的性能和资源利用率。

Based on the multi-core and multi-zone functionality already supported by the V25.04 version, continuously improve the execution efficiency of BSW functional stack modules supporting multi-core chips, optimize and upgrade the multi-core functionality, fully utilize the concurrent characteristic of hardware, reduce the single-core load rate, and achieve a balance between real-time performance and resource utilization rate. The Open Source EasyXMen V25.10 version greatly expands the multi-core and multi-zone functionality on the functional stacks. The functional stacks, including the storage stack (NvM/ Eep/FlsTst/RamTst), diagnostic stack (DEM/DCM/FIM/CanTp), information security (SecOC), I/O abstraction, time synchronization (Stbm/CanTysn/EthTysn), network management (NM/CanNm/UdpNm/EthSm/CanSm/LinSm), and WDG protocol stack (WdgIf/WdgM), all support multi-core and multi-zone deployment on the trusted zones. The enhanced realization of multi-core and multi–zone function further realizes more efficient load balancing and real-time response, and improves the system performance and resource utilization rate.

### 新增MemMap功能 New MemMap function

MemMap的主要是用于对工程中的代码、数据 、常量 进行内存映射。引入Memmap 模块对系统中的变量和代码进行配置映射，主要是为了通过合理的字节对齐方式，将数据进行更紧密的排列，以避免内存空间浪费。定义变量的初始化模式，支持特定内存属性的使用。定义代码和常量的位置到Flash空间,提高访问的效率。对代码和数据分配到不同的分区，便于支持内存保护功能。
MemMap is mainly used for memory mapping of codes, data, and constants in projects. The introduction of the Memmap module for configuring and mapping variables and codes in the system is mainly aimed at arranging data more tightly through reasonable byte alignment to avoid wasting memory space. Define the initialization mode of variables and support the use of specific memory properties. Define the location of codes and constants in Flash space to improve the access efficiency. Allocate codes and data to different zones to support the memory protection function.

开源小满V25.10版本已支持通过工具实现内存映射，支持更灵活的配置方式，优化系统执行效率。并生成BSW功能栈模块的MemMap.h和部分链接文件，以减轻集成工作量。MemMap模块会收集工程中所有的SW-ADDR-METHOD和MEMORY-SECTION，并根据配置信息对其进行内存映射，目前支持工具配置、名称推导、默认和手动映射四种方式，优先级为工具配置映射(需配置) > 名称推导映射(需开启) > 默认映射(需关联) = 手动映射(需开启)。MemLayout模块允许通过定义HwMemory，SectionGroup及Section对芯片的内存区域进行管理和划分。同时Section可以被MemMap模块引用，向其提供对于Section的链接语法。

The Open Source EasyXMen V25.10 version now supports realizing memory mapping through tools, supports more flexible configuration methods, and optimizes the system execution efficiency. MemMap.h and some link files for BSW functional stack modules are generated to reduce integration workload. The MemMap module will collect all SW-ADDR-METHOD and MEMORY-SECTION in the project and performs memory mapping based on the configuration information. Currently, it supports tool configuration, name derivation, default, and manual mapping four modes, with a priority of tool configuration mapping (needing to be configured)>name derivation mapping (needing to be enabled)>default mapping (needing to be associated)=manual mapping (needing to be enabled). The MemLayout module allows for management and division of the chip's memory area by defining HwMemory, SectionGroup, and Section. At the same time, Section can be referenced by the MemMap module, to provide it with link grammar for Section.

### 新增E2E Profile保护机制 New E2E Profile protection mechanism

E2E模块的作用是提供数据保护与校验机制， 在数据交互时对数据进行保护与校验， 以防通信链路内故障的影响。E2E保护概念的核心是针对安全相关的数据交换，需要在运行时进行保护，以消除通信链路中可能的失效带来的影响。开源小满V25.10版本在原有基础上新增Profile4m、Profile7m、Profile 8、Profile 8m、Profile 44、Profile 44m保护机制。通过不同的机制组合+参数配置，提供满足适配更多通信场景的保护策略支持。

The function of the E2E module is to provide data protection and verification mechanism, which can protect and verify data during data exchange to prevent the impact of failures in communication link. The core of E2E protection concept is aimed at security related data exchange, and it needs to be protected during operation to eliminate the impact of possible failures in communication link. On the existing basis, the Open Source EasyXMen V25.10 version adds the protection mechanisms for Profile4m, Profile7m, Profile 8, Profile 8m, Profile 44 and Profile 44m. Through combination of different mechanisms and configuration of parameters, it provides protection strategy supports that are suitable for more communication scenarios.

### OS新增OSM监控功能 New OSM monitoring function for OS

OSM模块的作用是针对嵌入式操作系统运行状态的实时监控功能，为用户提供系统运行状态的量化数据，支撑性能分析、故障诊断与实时性保障。开源小满V25.10版本已实现支持负载率、调度次数和Event三种类别监控。

The function of the OSM module is to provide real-time monitoring function for the operating status of embedded operating systems, providing users with quantitative data on the system's operating status, and supporting performance analysis, fault diagnosis, and real-time guarantee. The Open Source EasyXMen V25.10 version has realized the support for monitoring the load rate, number of scheduling times, and Event.

负载率监控可支持对CPU负载率、Task负载率、ISR负载率、TaskResponseTime和Os\_InterLockTime信息监控。

The load rate monitoring can support monitoring of CPU load rate, Task load rate, ISR load rate, TaskResponseTime, and Os\_InterLockTime information.

**CPU负载率监控：** 表示CPU在一段时间忙碌处理事务的时间占比，可支持CPU最大负载、最小负载、平均负载的查看。

**CPU load rate monitoring:** Indicates the proportion of time during which the CPU is busy processing transactions during a certain period of time, and can support viewing the maximum load, minimum load, and average load of the CPU.

**Task负载率监控：** 表示CPU在一段时间内运行Task的时间占比，可支持Task最大负载、最小负载、平均负载的查看。

**Task load rate monitoring:** Indicates the proportion of time that the CPU spends running the Task during a certain period of time, and can support viewing the maximum load, minimum load, and average load of the Task.

**ISR负载率监控：** 表示CPU在一段时间内运行ISR的时间占比，可支持ISR最大负载、最小负载、平均负载的查看。

**ISR load rate monitoring:** Indicates the proportion of time that the CPU spends running the ISR during a certain period of time, and can support viewing the maximum load, minimum load, and average load of the ISR.

**TaskResponseTime监控：** 表示任务从开时运行到结束运行的绝对时间，可支持任务响应的最大时间、最小时间、平均时间查看。
**TaskResponseTime monitoring: ** Indicates the absolute time from starting running to stopping running of the task, and can support viewing the maximum, minimum, and average task response time.

**Os\_InterLockTime监控：** 用于Os\_InitOsMonitor接口调用之后，监控所有中断（包括2类中断）或者2类中断的关闭时长。可支持查看最长关中断时间、最近关中断时间的记录情况。

**Os\_InterLockTime monitoring:** Used to monitor the shutdown duration of all interrupts (including Category 2 interrupts) or Category 2 interrupts after calling the Os\_InitOsMonitor interface is called. It can support viewing the records of the longest interrupt shutdown time and the latest interrupt shutdown time.

调度次数监控可支持对Task调度和Isr2调度的信息监控，Task调度监控用于监控从StartOS起至当前时刻，各个Task的总调度次数。sr2调度监控用于监控从StartOS起至当前时刻，各个Isr2的总调度次数。

Monitoring of the number of scheduling times can support information monitoring of Task scheduling and Isr2 scheduling. Task scheduling monitoring is used to monitor the total number of scheduling times of each Task from StartOS to the current time. sr2 scheduling monitoring is used to monitor the total number of scheduling times of each Isr2 from StartOS to the current time.

Event监控可支持对Event实时性和响应率的信息监控，Event实时性监控用于监控从event被触发到task最终响应event的这段时间是否过长，Event响应率监控用于监控是否存在Event响应率过低的场景。

Event monitoring can support Event real-time and response rate information monitoring. Event real-time monitoring is used to monitor whether the duration from the event being triggered to the task finally responding to the event is too long, while Event response rate monitoring is used to monitor whether there are scenarios where the event response rate is too low.

### 功能栈模块重点新增功能 Key new functions of functional stack modules

**SD模块：** 新增支持ServiceGroup功能，用于对服务实例进行分组管理的机制，核心作用是简化服务的发现逻辑、优化网络通信效率，并提升系统对服务的管理能力。

**SD module:** It adds the support for the ServiceGroup function, which is a mechanism for grouping management of service instances with the core functions of simplifying the discovery logic of services, optimizing the network communication efficiency, and enhancing the system's service management capability.

**EthIf模块：** 新增支持Switch模式切换功能，并实现支持Switch相关的接口，满足支持通过EthIf转发给Switch。

**EthIf module:** It adds the support for the function of Switch mode switching, and supports Switch related interfaces, meeting the requirement of forwarding to Switch through EthIf.

**SoAd模块：** 新增支持SoAd\_IsConnectionReady接口，可实现查询 SoAd 管理的特定通信连接是否处于就绪状态，为上层模块提供连接可用性的判断依据。

**SoAd module:** It adds the support for the SoAd\_IsConnectionReady interface, which can query whether the specific communication connection for SoAd management is in a ready state, providing a basis for determining the connection availability of upper modules.

**TcpIp模块：** 新增支持TcpIp\_IsConnectionReady和TcpIp\_GetCtrlIdx接口，TcpIp\_IsConnectionReady接口为上层提供TCP 连接可用性的直接判断，避免无效数据传输，提升通信效率。TcpIp\_GetCtrlIdx接口通过CtrlIdx桥接 TcpIp和 EthIf，支撑灵活的控制器管理。

**TcpIp module:** It adds the support for the TcpIp\_IsConnectionReady and TcpIp\_GetCtrlIdx interfaces. The TcpIp_IsConnectionReady interface provides direct determination of TCP connection availability for the upper layer, avoiding invalid data transmission and improving communication efficiency. The TcpIp\_GetCtrlIdx interface bridges TcpIp and EthIf through CtrlIdx, supporting flexible controller management.

**ComM模块：** 新增ComM\_RequestComMode功能，实现支持COMM\_FULL\_COMMUNICATION\_WITH\_WAKEUP\_REQUEST请求，用于向下层请求网络上的wake up。

**ComM module:** It adds the ComM_RequestComMode function, which supports the COMM\_FULL\_COMMUNICATION\_WITH\_WAKEUP_REQUEST request, used to request wake up on the network from the lower layer.

**EthSM模块：** 新增EthSM\_RequestComMode功能，实现支持 COMM\_SILENT\_COMMUNICATION 请求。

**EthSM module:** It adds the EthSM\_RequestComMode function, which supports the COMM\_SILENT\_COMMUNICATION request.

**NmIf模块：** 新增BswM\_Nm\_StateChangeNotification，支持Nm状态变化通知到BswM。

**NmIf module:** It adds the BswM\_Nm\_StateChangeNotification, which supports notifying the Nm status changes to BswM.

**ComM, Nm, CanNm, UdpNm模块：** 实现PNC功能升级，在模块间使用直接传递 PNC Bit-Vector 代替使用 UserData 和 ComSignal 传递。

**ComM, Nm, CanNm, and UdpNm modules:** It implements PNC function upgrading, and uses direct transmission of PNC Bit-Vector between modules, instead of UserData and ComSignal transmission.

**XCP模块：** 新增支持Resume模式，用于上电快速上传DAQ，新增支持STIM，用于Master传输数据到Slave。

**XCP module:** It adds the support for Resume mode, used for quickly uploading DAQ upon power on, and added the support for STIM for transferring data from Master to Slave.

**Dcm模块：** 新增支持ModeRule功能，可以根据读取模式决定是否执行服务/DID/RID等实现模式检测；UDS 0x11新增04、05子服务，同步增加配置项；新增支持动态DID信息存储功能，以支撑诊断工具对车辆动态状态的查询需求；新增P4Timer功能，可支持服务/子服务/RID级别的配置。

**Dcm module:** It adds the support for the ModeRule function, which can determine whether to execute services/DID/RID based on the read mode to implement mode detection; UDS 0x11 adds sub-services 04 and 05, and synchronously adds configuration items; it adds the support for dynamic DID information storage function to meet the query requirements of diagnostic tools for vehicle dynamic status; it adds P4Timer function, which can support service/sub-service/RID-level configuration.

**Dem模块：** 新增支持多客户端功能，支持配置多个client，允许不同客户端并发访问Dem数据；支持多存储功能，可实现配置多个primary和userdef存储；支持多分区功能，可配置事件在不同的分区，在卫星分区的错误报告后会汇总到主分区进行处理。

**Dem module:** It adds the support for the multi-client function, which supports configuring multiple clients, and allows different clients to access Dem data concurrently; it supports multi-storage function, and can configure multiple primary and userdef storage; it supports multi-zone function, and can allocate events in different zones, and after errors are reported from satellite zone, they will be gathered in the main zone for processing.

**Fim模块：** 新增支持多分区功能，支持FID在不同的分区，只能在对应分区获取FID状态；新增支持轮询处理功能，支持轮询异步或同步获取结果。

**Fim module:** It adds the support for the multi-zone function, which supports allocating FID in different zones, and FID status can only be obtained in the corresponding zone; it adds the polling processing function, supporting asynchronous or synchronous polling to obtain results.

**CanTp模块：** 新增支持多分区功能，支持R(T)xNSdu分属于不同的分区,CanTp只能处理来自当前分区的NSdu的接收与发送；新增CanTpDemEventParameterRefs配置，支持当发生超时错误、SN错误、流控状态为Overflow等事件时向Dem报告故障。

**CanTp module:** It adds the support for the multi-zone function, supporting R(T)xNSdu belonging to different zones, and CanTp can only handle the receiving and transmission of NSdu from the current zone; it adds CanTpDemEventParameterRefs configuration, supporting reporting faults to Dem when timeout errors, SN errors, flow control status Overflow, or other events occur.

**Det模块：** 新增支持ErrorHook和Callout接口，以供BSW或SWC模块进行调用，用于通知开发错误、通知运行错误、通知瞬间故障被产生。

**Det module:** It adds support for ErrorHook and Callout interfaces, which can be called by BSW or SWC modules to notify the generation of development errors, runtime errors, and instantaneous faults.

**Nvm模块：** 新增支持多分区功能，支持不同分区的block请求，并通过主函数统一处理；新增支持加解密功能，调用CSM的加解密服务，对关键数据进行保护处理；新增支持解压缩的配置，并调用对应的 callout 接口；新增支持调用FirstInitAll接口，用于在ECU首次运行或非易失性存储器被清空后使用，以确保NVRAM Block中的数据处于正确的初始状态。

**Nvm module:** It adds the support for the multi-zone function, which supports block requests of different zones, and processes them uniformly through the main function; it adds the support for encryption and decryption functions, used to call the CSM's encryption and decryption services to protect critical data; it adds the support for decompression configuration, and can call the corresponding callback interface; it adds the support for calling the FirstInitAll interface, which is used after the ECU is run for the first time or the non-volatile memory is cleared, in order to ensure that the data in the NVRAM Block is in the correct initial state.

**Fee、Ea模块：** 新增FeeMinimumReadPageSize、EaMinimumReadPageSize功能，在请求读任务时，若请求的长度没有与最小读取长度对齐，则不请求读任务。FEE新增Cluster功能，一个 Bank 可以被划分为多个 Cluster，每个 Cluster 由若干个连续的 Virtual Page 组成，通过在 Cluster 内部轮换使用不同的 Virtual Page 来执行写操作，避免对 Flash 的单一区域频繁擦写，实现磨损均衡延长 Flash 寿命。同时，通过将不同特性（如更新频率、数据大小）的 Block 配置到不同的 Cluster，实现差异化的存储管理策略。

**Fee and Ea modules:** It adds the FeeMinimumReadPageSize and EaMinimumReadPageSize functions, and when requesting a read task, if the request length is not aligned with the minimum read length, the read task will not be requested. FEE adds the Cluster function, which allows a Bank to be divided into multiple Clusters, each consisting of several consecutive Virtual Pages, and by rotating the use of different Virtual Pages within a Cluster to perform write operations, it avoids frequent erasures to a single area of Flash, and achieves wear balance to extend the Flash’s lifespan. Meanwhile, by configuring blocks with different characteristics such as update frequency and data size into different clusters, differentiated storage management strategies can be implemented.

**BswM模块：** 新增BswM 多核多服务组件支持，优化 BswM Action 执行逻辑，提高执行效率、降低代码资源消耗。

**BswM module:** It adds the support for BswM multi-core and multi-service components, optimizing the BswM Action execution logic, improving the execution efficiency, and reducing the code resource consumption.

**RTE：** 新增支持Runnable激活偏移功能，可通过配置OsScheduleTable实现；模式管理ModeManager及ModeUser新增支持不可信分区部署功能；新增支持独占区检测功能，当阻塞式Rte API被RTE独占区包裹时，API直接返回，避免中断时间过长；新增ECU间CS通信支持MetaData传递功能；RTE第二配置界面Runnable拖拽时，可根据Runnable属性自动关联OsTask、OsEvent，创建OsAlarm，配置RteOsInteraction等配置。

**RTE:** It adds the support for Runnable activation offset function, which can be achieved by configuring OsScheduleTable; the mode management ModeManager and ModeUser adds the support for deploying untrusted zones; it adds the support for exclusive zone detection function, and when the blocking Rte API is wrapped by an RTE exclusive zone, the API will return directly to avoid too long interruption time; it adds the support for MetaData transmission function for CS communication between ECU; when dragging and dropping Runnable on the second configuration interface of RTE, it can automatically associate OsTask and OsEvent, create OsAlarm, and configure RteOsInteraction according to the Runnable properties.

## 兼容性说明 Compatibility statement

“开源小满V25.10”比“开源小满V25.04”的工具模块定义文件版本更高，两版工具在配置方面存在差异，推荐用户试用新版本的工具。V25.10版本的工具，在打开升级器开关情况下（方法参见<ORIENTAIS\_Configurator\_User\_Manual\_for\_EasyXMen\_V25.10.pdf> 4.5升级器章节），可以导入V25.04版本创建的配置工程，导入后需逐个模块点击打开并进行保存，然后执行校验、生成等操作。模块配置Arxml文件同理，在V25.10版工具导入V25.04版工具生成的模块配置Arxml文件后，需要点击导入模块并进行保存，再执行校验、生成等操作。

The tool module definition file version of "Open Source EasyXMen V25.10" is higher than that of "Open Source EasyXMen V25.04", and there are differences in the configuration. It is recommended that users try the new version of the tool. The tools of V25.10 version can import configuration projects created in the V25.04 version when the upgrader switch is turned on (see <ORIENTAIS\_Configurator\_User\_Manual\_for\_EasyXMen\_V25.10.pdf> 4.5 Upgrader for the methods). After importing, users need to click on each module to open and save them, and then perform verification, generation, and other operations. The module configuration Arxml file is the same. After importing the module configuration Arxml file generated by the V25.04 version tool into the V25.10 version tool, users need to click on the Import Module and save it, and then perform verification, generation, and other operations.

注意：升级工作必须在2025年11月24日之前完成，超过时间节点后V25.10版本的工具不再支持V25.04版本配置工程及模块配置Arxml文件的导入，导致无法升级。

Please note that the upgrade work shall be completed before November 24, 2025. After this time node, tools of the V25.10 version will no longer support V25.04 version configuration projects and the import of module configuration Arxml files, and the upgrade cannot be carried out.



## 工具申请地址 Tool application Address

https://register.easyxmen.com/welcome.html?channel=3

## 代码仓地址 Code Repository Address

https://atomgit.com/easyxmen/XMen

## 文档仓地址 Documentation Repository Address

https://atomgit.com/easyxmen/docs

* 快速预览(Instant view the page at)：https://easyxmen.atomgit.net/docs/
