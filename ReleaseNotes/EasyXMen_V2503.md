发布日期：2025年3月25日

# **发布说明**
开源小满V25.03安全车控操作系统（简称“小满V25.03”）是普华基础软件基于AUTOSAR R19-11标准全面升级的产品版本，包含通信、诊断、网络管理、标定、存储等功能，于2025年3月25日正式发布，发布内容包括全部功能协议栈的源代码，同时提供工具链的免费使用安装包以及相关的手册文档，适用芯片与“小满V24.10”一致，均为恩智浦S32K148。后续V24.10版本的小满产品将不再维护，用户可根据后文工具申请地址、代码地址及文档地址，申请并体验最新版本小满产品。

## **核心亮点**

+ **实现多核多分区功能**

RTE、OS、EcuM、BswM支持多核部署功能，可支撑整个多分区多核系统的初始化、通信、调度；通信栈可按总线支持多核部署，其他BSW模块支持多分区（可信）多核访问，支持在多核上运行。

多核多分区功能的实现，允许将不同的BSW 模块分配到不同的核心或分区，实现不同功能软件代码的隔离并支持多核并行处理，使系统负载均衡，提升整体性能，进一步增强功能安全与信息安全，满足现代汽车电子系统对高性能、高可靠性和高安全性的需求。



+ **RTE重构优化**

基于国际行业标准对RTE进行功能升级优化，基础功能覆盖度大幅提升。本次发布的RTE核心常用功能实现在覆盖度上与国际主流基础软件供应商基本一致，包括通用功能、SR通信、CS通信、模式管理、存储NV、IRV通信、内外部触发、测量标定、独占区保护、PIM等功能，极大程度满足用户通用性需求。



+ **标准规范测试覆盖验证**

参照国际行业标准，基础软件模块包括CAN 通信、 CANFD 通信、 Lin 通信、通信管理、Communication ViaBus、EcuM、诊断服务、时间同步、IPv4、存储栈、RTE、TCP、UDP模块已高通过率完成ATS 基础测试验证；另外TCP/IP、SomeIp模块已基于TC8标准，完成通用性基础功能测试验证。以上标准规范测试的验证，极大地保障了“小满V25.03”功能栈模块的产品质量。

## **重要改进**
除上述多核多分区等功能实现外，还有如下功能迭代：

+ **新增FVM模块**

参照国际行业标准，通过CDD实现基于单一计数器 、基于截取的复合计数器两种新鲜度值构建方案。通过管理新鲜度值，与SecOC模块协同工作，有效防止重放攻击，确保车载网络通信的安全性，进一步保护汽车电子系统的信息安全。

+ **实现诊断UDS 29服务（身份认证服务）**

UDS 29服务是诊断仪和 ECU 之间的身份认证的一种方法，在访问受限数据或执行受限操作时验证客户端的身份，用于保证ECU的数据和软件安全。

参照国际行业标准，在“小满V25.03”基础软件的诊断协议栈中实现并集成UDS 29服务相关功能，并将29服务应用到KeyM模块证书解析、验证功能中，为用户提供更高级别的安全保护机制，进一步满足现代汽车网联化和共享化趋势下的安全需求。

+ **支持TP报文1:N路由**

“小满V25.03”中，PduR模块针对TP报文接收路由和网关路由均支持1:N，并且工具同步实现信号网关和报文网关导入自动生成配置，显著提升了通信灵活性，使汽车电子系统能够更高效地处理数据传输。

+ **支持ORTI调试功能**

“小满V25.03”将ORTI调试功能产品化，支持标准的ORTI文件，支持一系列ORTI标准定义功能，有效分析操作系统的行为，跟踪OS、TASK、CONTEXT、STAC、ALARM、RESOURCE及ISR等的状态并信息显示，还支持劳德巴赫功能，动态显示函数/代码行/模块的执行率、TASK 负载率以及STACK 最大占用率。

ORTI调试功能使开发者可以更方便地分析操作系统的行为，为汽车电子系统的开发和调试提供了更强大的支持。

+ **其他改进**

除上述改进外，“小满V25.03”版本还有一系列BSW功能栈优化，比如Canif、Linif、Frif、Ethif 模块 MCAL driver 实现不同国际标准版本适配，EthIf 模块实现 Switch、vlan 功能等，旨在进一步提升BSW功能栈覆盖度，满足用户使用场景及需求。

## **兼容性说明**
“小满V25.03”版本与“小满V24.10”分别对标不同国际标准版本，在配置方面存在差异，因此，模块配置的Arxml文件在两个版本的BSW Configurator工具中并不相互通用。

## **工具申请地址**
https://register.easyxmen.com/application_pc.html?channel=3

## **代码地址**
https://atomgit.com/easyxmen/XMen

## **文档地址**
 仓库地址：https://atomgit.com/easyxmen/docs

 网页浏览地址：https://easyxmen.atomgit.net/docs/

## **目录结构**

<font style="color:rgb(38,38,38);background-color:rgb(255,255,255);">├── BSWCode                 # 模块静态代码</font>

<font style="color:rgb(38,38,38);background-color:rgb(255,255,255);">│   ├── CommonInclude       # 共用的头文件</font>

<font style="color:rgb(38,38,38);background-color:rgb(255,255,255);">│   ├── Communication       # 通信模块代码</font>

<font style="color:rgb(38,38,38);background-color:rgb(255,255,255);">│   ├── Crypto              # 加密模块代码</font>

<font style="color:rgb(38,38,38);background-color:rgb(255,255,255);">│   ├── Libraries           # Lib库代码</font>

<font style="color:rgb(38,38,38);background-color:rgb(255,255,255);">│   ├── Memory              # 存储模块代码</font>

<font style="color:rgb(38,38,38);background-color:rgb(255,255,255);">│   └── SystemServices      # 系统服务模块代码</font>

<font style="color:rgb(38,38,38);background-color:rgb(255,255,255);">├── Drivers                 # 板级外设芯片代码</font>

<font style="color:rgb(38,38,38);background-color:rgb(255,255,255);">├── Examples                # 示例工程</font>

<font style="color:rgb(38,38,38);background-color:rgb(255,255,255);">├── RTE                     # RTE代码</font>

<font style="color:rgb(38,38,38);background-color:rgb(255,255,255);">│   └── StaticCode          # RTE 静态代码</font>

<font style="color:rgb(38,38,38);background-color:rgb(255,255,255);">├── RTOS                    # OS 代码</font>

<font style="color:rgb(38,38,38);background-color:rgb(255,255,255);">│   ├── Extend              # OS 扩展代码</font>

<font style="color:rgb(38,38,38);background-color:rgb(255,255,255);">│   ├── Kernel              # OS 内核代码</font>

<font style="color:rgb(38,38,38);background-color:rgb(255,255,255);">│   └── Portable            # OS移植代码</font>

<font style="color:rgb(38,38,38);background-color:rgb(255,255,255);">│       ├── Mcu             # MCU相关的移植代码</font>

<font style="color:rgb(38,38,38);background-color:rgb(255,255,255);">│       └── Processor       # 处理器架构相关移植代码</font>

<font style="color:rgb(38,38,38);background-color:rgb(255,255,255);">└── Test                    # bsw模块测试代码</font>

<font style="color:rgb(38,38,38);background-color:rgb(255,255,255);">└── UT                  # 单元测试代码</font>



+ <font style="color:rgb(36,41,47);background-color:rgb(255,255,255);">补充说明</font>
+ Portable/Mcu 下一个芯片一个目录，比如TC397,S32K148
+ Portable/Processor 一种芯片架构一个目录，比如arm,RISC-V
+ Test/UT 下一个Bsw模块一个目录
+ Drivers 下放置板级外设芯片实现代码，例如 TJA1101
+ Examples 下以一个硬件板型+具体功能组合成目录名，例如S32K148EVB_Q147_Demo
    - 工程对仓库中已有的实现代码进行引用
    - 工程应实现自动化编译
    - 工程的内部目录供参考


<font style="color:rgb(38,38,38);background-color:rgb(255,255,255);"></font><font style="color:rgb(38,38,38);background-color:rgb(255,255,255);">├── MCAL                    # MCAL 静态代码</font>

<font style="color:rgb(38,38,38);background-color:rgb(255,255,255);"></font><font style="color:rgb(38,38,38);background-color:rgb(255,255,255);">├── Asw                     # 应用代码</font>

<font style="color:rgb(38,38,38);background-color:rgb(255,255,255);"></font><font style="color:rgb(38,38,38);background-color:rgb(255,255,255);">|   ├── src                 # 应用源码</font>

<font style="color:rgb(38,38,38);background-color:rgb(255,255,255);"></font><font style="color:rgb(38,38,38);background-color:rgb(255,255,255);">|   └── gen                 # 应用配置生成</font>

<font style="color:rgb(38,38,38);background-color:rgb(255,255,255);"></font><font style="color:rgb(38,38,38);background-color:rgb(255,255,255);">├── PaltformFils            # 编译器等平台相关</font>

<font style="color:rgb(38,38,38);background-color:rgb(255,255,255);"></font><font style="color:rgb(38,38,38);background-color:rgb(255,255,255);">└── ConfigProj              # 配置工程</font>

<font style="color:rgb(38,38,38);background-color:rgb(255,255,255);"></font><font style="color:rgb(38,38,38);background-color:rgb(255,255,255);">├── BswCfgProj          # bsw 配置工程</font>

<font style="color:rgb(38,38,38);background-color:rgb(255,255,255);"></font><font style="color:rgb(38,38,38);background-color:rgb(255,255,255);">    ├── SwcCfgProj          # swc 配置工程</font>

<font style="color:rgb(38,38,38);background-color:rgb(255,255,255);">    └── McalCfgProj         # MCAL 配置工程</font>



## **运行条件**
协议栈静态代码需要结合开发工具进行使用，可通过官方入口进行开发工具链免费申请。各模块配置、工具使用方法，可参考模块用户手册。