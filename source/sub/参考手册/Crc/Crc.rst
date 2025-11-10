===================
Crc
===================


文档信息(Document Information)
=======================================

版本历史(Version History)
-----------------------------------

.. list-table::
   :widths: 10 10 10 10 20
   :header-rows: 1

   * - 日期(Date)
     - 作者(Author)
     - 版本(Version)
     - 状态(Status)
     - 说明(Description)
   * - 2024/12/5
     - qinmei.chen
     - V0.1
     - 发布(Release)
     - 首次发布(First Release)
   * - 2025/04/04
     - qinmei.chen
     - V1.0
     - 发布(Release)
     - 正式发布(Official Release)

参考文档(References)
----------------------------------

.. list-table::
   :widths: 10 15 25 10
   :header-rows: 1

   * - 编号(Number)
     - 分类(Classification)
     - 标题(Title)
     - 版本(Version)
   * - 1
     - Autosar
     - AUTOSAR_CP_SWS_CRCLibrary.pdf
     - R23-11


术语与简写(Terms and Abbreviations)
========================================


术语(Terms)
---------------

None


简写(Abbreviations)
---------------------------

.. list-table::
   :widths: 15 20 25
   :header-rows: 1


   * - 简写(Abbreviation)
     - 全称(Full name) 
     - 解释(Explanation)

   * - CRC
     - Cyclic Redundancy Check
     - 循环冗余校验

   * - ALU
     - Arithmetic Logic Unit
     - 算术逻辑单元

简介(Introduction)
============================

CRC模块主要实现了基于输入数据计算一组校验码，以检查数据在传输过程中是否发生了变化或传输错误。

The CRC module primarily implements checksum calculation based on input data to detect data alterations or transmission errors.

假设D是要被校验的数据，已转为n bit的二进制表示。例如

Let D be the data to be verified, converted to an n-bit binary representation. For example:

D = (dn-1, dn-2, dn-3, ..., d1, d0)，其中d0到dn-1是二进制的位数。

D = (dn-1, dn-2, dn-3, ..., d1, d0), where d0 to dn-1 are binary bits.

使用某些规则生成新的二进制序列R，假设k位，r0到rk-1是二进制值0或1。

A new binary sequence R is generated according to specific rules, assumed to be k bits, where r0 to rk-1 are binary values 0 or 1.

冗余码R被附加到原始数据二进制序列上，成为n+k位数据的二进制表示：

The redundant code R is appended to the original data binary sequence, forming an n+k-bit binary representation of the data:

C=(D,R)=(dn-1,dn-2,dn-3,…,d1,d0,rk-1,…,r2,r1,r0,)。

C = (D, R) = (dn-1, dn-2, dn-3, …, d1, d0, rk-1, …, r2, r1, r0).

将C除以k阶多项式，得到(k-1)阶余数r(x)，那么与r(x)对应的二进制码r就是CRC码。

Dividing C by a k-th order polynomial yields a (k-1)-th order remainder r(x), and the binary code r corresponding to r(x) is the CRC code.

被分割的k阶多项式是生成器。

The k-th order polynomial used for division is the generator.

CRCL模块提供三种算法处理机制：

The CRCL module provides three algorithm processing mechanisms:

 - 查表计算方法：速度快，需要占用较大的ROM。

   Look-up table calculation method: Fast but requires large ROM space.

 - 运行时计算方法：速度慢，占用ROM少。
   
   Runtime calculation method: Slow but uses less ROM.

 - 硬件计算方法：快速，但需要硬件支持。

   Hardware calculation method: Fast but requires hardware support.


功能描述(Functional Description)
==========================================


特性(Features)
----------------------

CRC算法简介(Introduction to CRC Algorithms)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
下述是几种标准的CRC校验生成多项式：

The following are several standard CRC generator polynomials:

- CRC 8bit SAE J1850：

 .. centered:: :math:`G(x)=x^8+x^4+x^3+x^2+1`

- CRC 8bit based on 0x2F:

 .. centered:: :math:`G(x)=x^8+x^5+x^3+x^2+x+1`

- CRC 16bit CCITT-FALSE:

 .. centered:: :math:`G(x)=x^{16}+x^{12}+x^5+1`

- CRC 16bit based on 0x8005:

 .. centered:: :math:`G(x)=x^{16}+x^{15}+x^2+1`

- CRC 32bit Ethernet IEEE-802.3:

 .. centered:: :math:`G(x)=x^{32}+x^{26}+x^{23}+x^{22}+x^{16}+x^{12}+x^{11}+x^{10}+x^8+x^7+x^5+x^4+x^2+x+1`

- CRC 32bit based on 0xF4ACFB13:

 .. centered:: :math:`G(x)=x^{32}+x^{31}+x^{30}+x^{29}+x^{28}+x^{25}+x^{23}+x^{21}+x^{19}+x^{18}+x^{15}+x^{14}+x^{13}+x^{12}+x^{11}+x^9+x^8+x^4+x+1`

- CRC 64bit ECMA:

 .. math::
  \begin{align}
  G(x) = &x^{64}+x^{62}+x^{57}+x^{55}+x^{54}+x^{53}+x^{52}+x^{47}+x^{46}+x^{40}+x^{39}+x^{38} \\
  &+ x^{37}+x^{35}+x^{33}+x^{32}+x^{31}+x^{29}+x^{27}+x^{24}+x^{23}+x^{22}+x^{21}+x^{19} \\
  &+x^{17}+x^{13}+x^{12}+x^{10}+x^9+x^7+x^4+x+1
  \end{align}

CRC校验的原理就是将需要校验的数据与按规则产生的数据进行异或运算，得到的余数即为校验值。进行异或的方式与实际数据传输时，高位先传还是低位先传有关，若异或从数据的高位开始，为顺序异或，若异或从数据的低位开始，则为反序异或，两种异或方式，即使对应同一个生成多项式，计算出来的结果也不相同。

The principle of CRC verification involves performing XOR operations between the data to be verified and data generated according to specific rules, with the resulting remainder serving as the checksum value. The XOR method depends on the data transmission order: starting from the high bit is forward XOR, while starting from the low bit is reverse XOR. These two XOR methods produce different results even with the same generator polynomial.

​Forward XOR (顺序异或)​: Processing starts from the ​most significant bit (MSB)​​ of the data.

​Reverse XOR (反序异或)​: Processing starts from the ​least significant bit (LSB)​​ of the data.

Even with the ​same generator polynomial​, these two methods yield ​different results​ due to opposing computational directions

CRC标准参数模型(CRC Standard Parameter Model)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
CRC8、CRC16、CRC32、CRC64所要用到的标准参数如下：

The standard parameters required for CRC8, CRC16, CRC32, and CRC64 are as follows:

.. list-table::
   :widths: 10 10
   :header-rows: 1

   * - 参数名(Parameter Name)
     - 解释(Explanation)

   * - CRC宽度(CRC Width)
     - CRC计算结果的宽度(Result data width of CRC calculation)

   * - 多项式(Polynomial)
     - 用于CRC算法的生成多项式(Generator polynomial used for CRC algorithm)

   * - 初始值(Initial Value)
     - CRC算法开始时寄存器初始化的预置值(Preset value for register initialization at CRC algorithm start)

   * - 输入数据反转(Input Data Reverse)
     - 定义了在参与CRC计算之前，每个输入字节是否需要进行位反转(Defines whether each input byte needs bit reversal before CRC calculation)

   * - 输出数据反转(Output Data Reverse)
     - 定义了CRC计算结果是否需要按位反转(Defines whether CRC result needs bit reversal)

   * - 异或值(XOR Value)
     - 该值将与寄存器中的最终值进行运算，再将异或结果作为返回值(Value XORed with final register value before returning as checksum)

   * - 检查值(Check Value)
     - 这是作为验证CRC算法的一种较弱的方法，当输入ASCII字符串"123456789"时，该值作为校验值(Weak validation method for CRC algorithm; serves as check value when input is ASCII string "123456789")

CRC功能实现(CRC Function Implementation)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
CRC功能实现分为三种方式：直接计算法、查表法、硬件实现法，分别对应配置项CrcxMode中的取值CRC_RUNTIME、CRC_TABLE和CRC_HARDWARE ，x代表CRC位宽，可为8、8H2F、16、16ARC、32、32P4、64。

CRC function implementation is divided into three methods: direct calculation, look-up table, and hardware implementation, corresponding to the values CRC_RUNTIME, CRC_TABLE, and CRC_HARDWARE in configuration item CrcxMode respectively. Here, "x" represents CRC bit width, which can be 8, 8H2F, 16, 16ARC, 32, 32P4, or 64.

集成(Integration)
===============================

文件列表(File List)
-------------------------------

静态文件(Static Files)
~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - 文件(File)
     - 描述(Description)

   * - Crc.h
     - CRC模块头文件，包含了API函数的扩展声明并定义了端口的数据结构(CRC module header file containing extended API function declarations and port data structure definitions)

   * - Crc.c
     - CRC模块源文件，包含了API函数的实现(CRC module source file containing API function implementations)

   * - Crc_MemMap.h
     - CRC的内存映射定义(CRC memory mapping definition)

动态文件(Dynamic Files)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - 文件(File)
     - 描述(Description)
   
   * - Crc_cfg.h
     - 定义CRC模块预编译时用到的配置参数(Defines configuration parameters used during CRC module pre-compilation)

错误处理(Error Handling)
--------------------------------
None

.. 引用接口描述。来自于code->doxygen->latex->rst
.. include:: Crc_h_api.rst

配置(Configuration)
============================

Crc8Mode
----------------------
开启Crc8的支持，可选方法包括CRC_TABLE、CRC_RUNTIME和CRC_HARDWARE

Enables Crc8 support; optional methods include CRC_TABLE, CRC_RUNTIME, and CRC_HARDWARE

Crc8H2FMode
----------------------
开启Crc8H2F的支持，可选方法包括CRC_TABLE、CRC_RUNTIME和CRC_HARDWARE

Enables Crc8H2F support; optional methods include CRC_TABLE, CRC_RUNTIME, and CRC_HARDWARE

Crc16Mode
----------------------
开启Crc16的支持，可选方法包括CRC_TABLE、CRC_RUNTIME和CRC_HARDWARE

Enables Crc16 support; optional methods include CRC_TABLE, CRC_RUNTIME, and CRC_HARDWARE

Crc16ARCMode
----------------------
开启Crc16ARC的支持，可选方法包括CRC_TABLE、CRC_RUNTIME和CRC_HARDWARE

Enables Crc16ARC support; optional methods include CRC_TABLE, CRC_RUNTIME, and CRC_HARDWARE

Crc32Mode
----------------------
开启Crc32的支持，可选方法包括CRC_TABLE、CRC_RUNTIME和CRC_HARDWARE

Enables Crc32 support; optional methods include CRC_TABLE, CRC_RUNTIME, and CRC_HARDWARE

Crc32P4Mode
----------------------
开启Crc32P4的支持，可选方法包括CRC_TABLE、CRC_RUNTIME和CRC_HARDWARE

Enables Crc32P4 support; optional methods include CRC_TABLE, CRC_RUNTIME, and CRC_HARDWARE

Crc64Mode
----------------------
开启Crc64的支持，可选方法包括CRC_TABLE、CRC_RUNTIME和CRC_HARDWARE

Enables Crc64 support; optional methods include CRC_TABLE, CRC_RUNTIME, and CRC_HARDWARE

.. figure:: ../../../_static/参考手册/Crc/CRC容器配置图.png
   :alt: CRC容器配置图 (CRC Container Configuration Diagram)
   :name: fig_event-handler
   :align: center

   CRC容器配置图 (CRC Container Configuration Diagram)

