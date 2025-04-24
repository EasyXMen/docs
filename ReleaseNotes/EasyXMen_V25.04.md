发布日期：2025年4月25日  
Release date: April 25, 2025

# **发布说明（Release Note）**

开源安全车控操作系统小满EasyXMenV25.04（简称“开源小满V25.04”）是普华基础软件基于AUTOSAR R19-11标准全面升级的产品版本，包含通信、诊断、网络管理、标定、存储等功能，于2025年4月正式发布，发布内容包括全部功能协议栈的源代码，同时提供工具链的免费使用安装包以及相关的手册文档，支持的芯片平台包括恩智浦S32K148、英飞凌TC397、瑞萨RH850/U2A16，在“开源小满V24.10”基础上增加了2款。后续，“开源小满V24.10”将不再维护，用户可根据后文工具链申请地址、代码地址及文档地址，申请并体验最新版本。
Open Source Safety Vehicle Control Operating System EasyXMen V25.04 ("EasyXMen V25.04") is a comprehensive upgraded product version by iSOFT INFRASTRUCTURE SOFTWARE CO.,LTD. based on the AUTOSAR R19-11 standards, including communication, diagnosis, network management, calibration, storage, etc. It was officially released in April 2025. The released content includes the source code of all the functional protocol stacks, as well as the free toolchain installation package and related manuals and documents, and support chip platforms include NXP S32K148, Infineon TC397, and Renesas RH850/U2A16, with two additional models added based on "EasyXMen V24.10". The "EasyXMen V24.10" will no longer be maintained, and users can apply for and experience the latest version of EasyXMen according to the toolchains application address, code address and document address in the following text.

## **核心亮点（Core highlights）**

+ **实现多核多分区功能（Realization of multi-core and multi-zone functionality）**

RTE、OS、EcuM、BswM支持多核部署功能，可支撑整个多分区多核系统的初始化、通信、调度；通信栈可按总线支持多核部署，其他BSW模块支持多分区（可信）多核访问，支持在多核上运行。  
RTE, OS, EcuM, and BswM support multi-core deployment function, which can support the initialization, communication, and scheduling of the whole multi-zone and multi-core system; the communication stack can support multi-core deployment by bus, and the other BSW modules support multi-zone and (trusted) multi-core access, and support running on multi-core systems.

多核多分区功能的实现，允许将不同的 BSW 模块分配到不同的核心或分区，实现不同功能软件代码的隔离并支持多核并行处理，使系统负载均衡，提升整体性能，进一步增强功能安全与信息安全，满足现代汽车电子系统对高性能、高可靠性和高安全性的需求。  
The realization of multi-core and multi-zone function allows different BSW modules to be assigned to different cores or zones, realizing the isolation of different functional software codes and supporting multi-core parallel processing. This balances the system load, improves the overall performance, further enhances the functional safety and information security, and satisfies the needs of modern automotive electronic systems for high performance, high reliability and high security.

+ **RTE重构优化（Optimization of RTE reconfiguration）**

基于国际行业标准对RTE进行功能升级优化，基础功能覆盖度大幅提升。本次发布的RTE核心常用功能实现在覆盖度上与国际主流基础软件供应商基本一致，包括通用功能、SR通信、CS通信、模式管理、存储NV、IRV通信、内外部触发、测量标定、独占区保护、PIM等功能，极大程度满足用户通用性需求。
Based on the international industry standard, RTE functions are upgraded and optimized, and the coverage of basic functions is greatly improved. The core common functions of RTE released this time are basically the same as those of international mainstream infrastructure software suppliers in terms of coverage, including general functions, SR communication, CS communication, mode management, storage NV, IRV communication, internal and external triggering, measurement calibration, exclusive area protection, PIM and other functions, which greatly satisfy the user's generality needs.

+ **标准规范测试覆盖验证（Standardized specification test and coverage validation）**

参照国际行业标准，基础软件模块包括CAN 通信、CANFD 通信、Lin 通信、通信管理、Communication ViaBus、EcuM、诊断服务、时间同步、IPv4、存储栈、RTE、TCP、UDP模块已高通过率完成ATS 基础测试验证；另外TCP/IP、SomeIp模块已基于TC8标准，完成通用性基础功能测试验证。以上标准规范测试的验证，极大地保障了“开源小满V25.04”功能栈模块的产品质量。
With reference to the international industry standards, the infrastructure software modules including CAN communication, CANFD communication, Lin communication, communication management, Communication ViaBus, EcuM, diagnosis service, time synchronization, IPv4, storage stack, RTE, TCP, and UDP modules have completed the ATS basic test validation with high passing rate. In addition, the TCP/IP, SomeIp modules have completed the generic basic function test validation based on TC8 standard. The validation of the above standardized tests has greatly guaranteed the product quality of "EasyXMen V25.04" function stack modules.

## **重要改进（Important improvements）**

除上述多核多分区等功能实现外，还有如下功能迭代：
In addition to the above implementation of multi-core and multi-zone functions and other functions, there are the following functional iterations:

+ **新增FVM模块（New FVM module）**

参照国际行业标准，通过CDD实现基于单一计数器 、基于截取的复合计数器两种新鲜度值构建方案。通过管理新鲜度值，与SecOC模块协同工作，有效防止重放攻击，确保车载网络通信的安全性，进一步保护汽车电子系统的信息安全。
With reference to international industry standards, CDD realizes two fresh degree value construction schemes based on single counter and interception-based composite counter. By managing the fresh degree value and working with the SecOC module, it effectively prevents replay attacks, ensures safety of in-vehicle network communication, and further protects the information safety of the automotive electronic system.

+ **实现诊断UDS 29服务（身份认证服务）（Realization of UDS 29 diagnosis service (authentication service)）**

UDS 29服务是诊断仪和 ECU 之间的身份认证的一种方法，在访问受限数据或执行受限操作时验证客户端的身份，用于保证ECU的数据和软件安全。
The UDS 29 service is a method of authentication between the diagnostic instrument and the ECU, verifying the identity of the client when accessing restricted data or performing restricted operations, and is used to ensure safety of the ECU's data and software.

参照国际行业标准，在“开源小满V25.04”基础软件的诊断协议栈中实现并集成UDS 29服务相关功能，并将29服务应用到KeyM模块证书解析、验证功能中，为用户提供更高级别的安全保护机制，进一步满足现代汽车网联化和共享化趋势下的安全需求。
With reference to the international industry standards, the UDS 29 service has been implemented and integrated  into the diagnosis protocol stack of "EasyXMen V25.04" infrastructure software, and been applied to the certificate analysis and validation functions of the KeyM module, so as to provide users with a higher level of safety protection mechanism, and further to meet the safety requirements of modern automobiles under the trend of network connectivity and sharing.

+ **支持TP报文1:N路由（Support for TP message 1:N routing）**

“开源小满V25.04”中，PduR模块针对TP报文接收路由和网关路由均支持1:N，并且工具同步实现信号网关和报文网关导入自动生成配置，显著提升了通信灵活性，使汽车电子系统能够更高效地处理数据传输。
In "EasyXMen V25.04", the PduR module supports 1:N for both TP message receiving routes and gateway routes, and the tool synchronizes the signal gateway and message gateway import to automatically generate configurations, which significantly improves the communication flexibility and enables the automotive electronic system to more efficiently deal with data transmission.

+ **支持ORTI调试功能（Support for ORTI debugging functions）**

“开源小满V25.04”将ORTI调试功能产品化，支持标准的ORTI文件，支持一系列ORTI标准定义功能，有效分析操作系统的行为，跟踪OS、TASK、CONTEXT、STAC、ALARM、RESOURCE及ISR等的状态并信息显示，还支持劳德巴赫功能，动态显示函数/代码行/模块的执行率、TASK 负载率以及STACK 最大占用率。
"EasyXMen V25.04" productizes ORTI debugging functions, supports standard ORTI files and a series of ORTI standard definition functions, effectively analyzes the behavior of the operating system, traces the status and information display of OS, TASK, CONTEXT, STAC, ALARM, RESOURCE, and ISR, etc. It also supports the  Laudenbach function, which dynamically displays the execution rate of functions/code lines/modules, TASK load rate, and STACK maximum occupancy rate.

ORTI调试功能使开发者可以更方便地分析操作系统的行为，为汽车电子系统的开发和调试提供了更强大的支持。
The ORTI debugging function makes it easier for developers to analyze the behavior of the operating system, providing stronger support for the development and debugging of automotive electronic systems.

+ **其他改进（Other improvements）**

除上述改进外，“开源小满V25.04”版本还有一系列BSW功能栈优化，比如Canif、Linif、Ethif 模块 MCAL driver 实现不同国际标准版本适配，EthIf 模块实现 Switch、vlan 功能等，旨在进一步提升BSW功能栈覆盖度，满足用户使用场景及需求。
In addition to the above improvements, "EasyXMen V25.04" version also has a series of BSW function stack optimization, such as Canif, Linif, Ethif module. MCAL driver adapts to different international standard versions, EthIf module implements Switch, vlan function, etc., which aims to further improve the coverage of BSW function stack to meet the user's usage scenarios and requirements. 

## **兼容性说明（Compatibility statement）**

“开源小满V25.04”与“开源小满V24.10”分别对标不同国际标准版本，在配置方面存在差异，因此，模块配置的Arxml文件在两个版本的BSW Configurator工具中并不相互通用。
"EasyXMen V25.04" and "EasyXMen V24.10" are benchmarked against different international standard versions, and there are differences in the configuration. Therefore, the Arxml file for module configuration is not common between the two versions of BSW Configurator tool.

## **工具链申请地址（Toolchains request address）**

https://register.easyxmen.com/application_pc.html?channel=3

## **代码地址（Code address）**

https://atomgit.com/easyxmen/XMen

## **文档地址（Documentation address）**

+ 仓库地址（Repository address）：https://atomgit.com/easyxmen/docs 

+ 网页浏览地址（View the page at）：https://easyxmen.atomgit.net/docs/
