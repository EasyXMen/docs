===================
E2E
===================
.. 标题标识符“===”的长度必须要大于其内容的长度，否则会报错，其他标题亦是如此


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
     - 首次发布(First release)
   * - 2025/04/04
     - qinmei.chen
     - V1.0
     - 发布(Release)
     - 正式发布(Official release)

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
     - AUTOSAR_SWS_E2ELibrary.pdf
     - R23-11
   * - 2
     - Autosar
     - AUTOSAR_FO_PRS_E2EProtocol.pdf
     - R23-11 


术语与简写(Terms and Abbreviations)
========================================


术语(Terms)
---------------------
   .. :align: center   表格内容居中(Table contents are centered)


.. list-table::
   :widths: 10 40
   :header-rows: 1

   * - 术语 (Term)
     - 解释 (Explanation)

   * - E2E Library
     - 端到端通信保护库的简称 (Abbreviation for End-to-End Communication Protection Library)

   * - Data ID
     - 一个用于唯一标识信息/数据/数据元素的标识符 (An identifier used to uniquely identify information/data/data elements)

   * - Source ID
     - 一个用于唯一标识源信息/数据/数据元素的标识符 (An identifier used to uniquely identify the source of information/data/data elements)

   * - Repetition
     - 信息的重复 (Duplication of information)

   * - Loss
     - 信息的丢失 (Loss of information)

   * - Delay
     - 信息的延迟 (Delay of information)

   * - Insertion
     - 信息的插入(Insertion of information)

   * - Masquerade
     - 伪装(Disguise)     

   * - Incorrect addressing
     - 信息的不正确地址 (Incorrect addressing of information)

   * - Incorrect sequence
     - 信息的不正确序列 (Incorrect sequence of information)

   * - Corruption
     - 信息损坏 (Corruption of information)

   * - Asymmetric information
     - 从一个发送者发送到多个接收者的不对称信息(Asymmetric information sent from one sender to multiple recipients)

   * - Subset
     - 仅由接收方的一部分接受的来自一个发送方的信息(Information from a single sender that is only accepted by a portion of the recipients)

   * - Blocking
     - 阻止对通信通道的访问(Blocking access to the communication channel)

简写(Abbreviations)
----------------------------

.. list-table::
   :widths: 15 20 25
   :header-rows: 1


   * - 简写(Abbreviation)
     - 全称(Full name)
     - 解释(Explanation)

   * - E2E
     - End to End Communication Protection
     - 端到端的通信保护

   * - Data ID
     - Data Identification
     - 一段数据/消息的标识

简介(Introduction)
=============================


E2EL在架构上属于AUTOSAR静态库代码，使用同样属于静态库代码的CRC模块来进行安全数据的保护，E2E XF通过把E2EL的相关算法抽象成用户易操作的配置项和配置界面，并根据用户的属于生成代码，来帮助用户更好的使用E2EL来保护数据。

Architecturally, E2EL belongs to AUTOSAR static library code and uses the CRC module, which is also static library code, to protect safety data. E2E XF abstracts E2EL's related algorithms into user-friendly configuration items and interfaces, and generates code based on user inputs to help users better use E2EL for data protection.

.. figure:: ../../../_static/参考手册/E2E/image2.png
   :alt: E2EL架构图(E2EL Architecture Diagram)
   :name: fig_E2E2
   :align: center

   E2EL架构图 (E2EL Architecture Diagram)



功能描述(Functional Description)
==========================================

特性(Features)
-----------------------

E2EL的各个profile提供了一种可以满足功能安全目标的数据保护机制，各个E2E profile通过不同的算法和API完成以下类型的数据保护机制：

Each E2EL profile provides a data protection mechanism that can meet functional safety goals. Different E2E profiles implement the following types of data protection mechanisms through various algorithms and APIs:

#. 集成CRC库的CRC保护机制；

   CRC protection mechanism integrated with CRC library;

#. 接收端检测接收报文的递增计数器，判断接收数据是否有序递增；

   Incremental counter detection at receiver side to determine if received data is sequentially increasing;

#. 接收端通过检测心跳计数器判断数据是否发生改变；

   Alive counter detection at receiver side to determine if data has changed;

#. 通过特定的ID来区分不同的I-PDU组；

   Specific IDs to distinguish different I-PDU groups;

#. 超时检测机制(接收报文超时和发送确认超时)；

   Timeout detection mechanism (receiver message timeout and sender acknowledgement timeout);

#. E2E profiles的用户需要根据自己的应用场景决定选用哪种类型的E2E profile；

   Users of E2E profiles need to determine which type of E2E profile to use based on their application scenarios;

#. E2E支持的profile有profile1、profile2、profile4、profile4m、profile5、profile6、profile7、profile7m、profile8、profile8m、profile11、profile22、profile44、profile44m。

   E2E supports profiles: profile1, profile2, profile4, profile4m, profile5, profile6, profile7, profile7m, profile8, profile8m, profile11, profile22, profile44, and profile44m.

以下为E2EL各Profile功能介绍。

The following describes the functions of each E2EL Profile.

Profile1
~~~~~~~~~~~~~~~~~~~
 - CRC保护(CRC Protection)

   Profile1使用CRC-8-SAE J1850算法对数据的完整性进行校验。

   Profile1 uses the CRC-8-SAE J1850 algorithm to verify data integrity.

 - DataID

   Profile1通过特定的ID来区分不同的I-PDU组，它分为了四种ID模式。

   Profile1 distinguishes different I-PDU groups through specific IDs, divided into four ID modes.

Both bytes (dataIdMode=0):16位数据ID的两个字节都附加在安全数据上用于CRC计算，但没有显式发送。

Both bytes (dataIdMode=0): Both bytes of the 16-bit Data ID are appended to safety data for CRC calculation but not explicitly transmitted.

ALT bytes (dataIdMode=1)：根据counter的基偶性，来选择高字节还是低字节进行CRC计算。

ALT bytes (dataIdMode=1): Depending on counter parity, either high byte or low byte is selected for CRC calculation.

Low byte only (dataIdMode=2):只有16位数据ID的低字节附加到安全数据进行CRC计算，但不显式发送，高字节设置为0。

Low byte only (dataIdMode=2): Only low byte of 16-bit Data ID is appended to safety data for CRC calculation, not explicitly transmitted, high byte set to 0.

显式传输数据ID nibble (dataIdMode=3): 16位数据ID的两个字节都附加在安全数据上进行CRC计算，但数据ID高字节的低字节显式传输。在这个16位的数据ID中只使用了12位。

Explicit transmission of data ID nibble (dataIdMode=3): Both bytes of 16-bit Data ID are appended to safety data for CRC calculation, but low nibble of high byte is explicitly transmitted. Only 12 bits are used in this 16-bit Data ID.

Profile2
~~~~~~~~~~~~~~~~~~~
 - CRC保护(CRC Protection)

   Profile2使用8bit Polynomial为0x2f的算法对数据的完整性进行校验。

   Profile2 uses an algorithm with 8-bit Polynomial 0x2f to verify data integrity.

 - Sequence counter/alive counter

   4-bit的Sequence counter/alive counter在0-15之间依次递增, 递增计数器用来判断接收数据是否有序递增，心跳计数器用来判断数据是否发生改变。

   A 4-bit Sequence counter/alive counter increments sequentially between 0-15; the sequence counter determines if received data is sequentially increasing, the alive counter detects if data has changed.

 - DataID

   DataID使用特定的ID来区分不同的I-PDU组，Profile2使用了一个预设的DataID列表，并通过Counter的值来选择DataID列表里的特定的DataID。

   DataID uses specific IDs to distinguish different I-PDU groups. Profile2 uses a preset DataID list and selects specific DataIDs from the list based on Counter values.

Profile4
~~~~~~~~~~~~~~~~~~~~~~~~~~~
 - CRC保护(CRC Protection)

   Profile4使用32 bit polynomial为0x1F4ACFB13的算法对数据的完整性进行校验。

   Profile4 uses an algorithm with 32-bit polynomial 0x1F4ACFB13 to verify data integrity.

 - Sequence counter/alive counter

   16-bit的Sequence counter/alive counter, 递增计数器用来判断接收数据是否有序递增，心跳计数器用来判断数据是否发生改变。

   A 16-bit Sequence counter/alive counter; the sequence counter determines if received data is sequentially increasing, the alive counter detects if data has changed.

 - Data Length

   Profile4使用16bit的Data Length来支持动态大小的输入数据。

   Profile4 uses 16-bit Data Length to support dynamic-size input data.

 - DataID

   DataID使用特定的ID来区分不同的I-PDU组，Profile4使用了全局唯一的32bit的DataID进行显式发送。

   DataID uses specific IDs to distinguish different I-PDU groups. Profile4 uses globally unique 32-bit DataID for explicit transmission.

Profile4m
~~~~~~~~~~~~~~~~~~~~~~~~~~~
 - CRC保护 (CRC Protection)

   Profile4使用32 bit polynomial为0x1F4ACFB13的算法对数据的完整性进行校验。

   Profile4 uses an algorithm with 32-bit polynomial 0x1F4ACFB13 to verify data integrity.

 - Sequence counter/alive counter

   16-bit的Sequence counter/alive counter, 递增计数器用来判断接收数据是否有序递增，心跳计数器用来判断数据是否发生改变。

   A 16-bit Sequence counter/alive counter; the sequence counter determines if received data is sequentially increasing, the alive counter detects if data has changed.

 - Data Length

   Profile4使用16bit的Data Length来支持动态大小的输入数据。

   Profile4 uses 16-bit Data Length to support dynamic-size input data.

 - DataID

   DataID使用特定的ID来区分不同的I-PDU组，Profile4使用了全局唯一的32bit的DataID进行显式发送。

   DataID uses specific IDs to distinguish different I-PDU groups. Profile4 uses globally unique 32-bit DataID for explicit transmission.

 - Message Type

   Message Type是用于区分请求和回复信息的2bits值，显式发送。

   Message Type is a 2-bit value used to distinguish between request and reply information, explicitly transmitted.

 - Message Result

   Message Result是用于区分正常回复和错误回复的2bits值，显式发送。

   Message Result is a 2-bit value used to distinguish between normal replies and error replies, explicitly transmitted.

 - Source ID

   Source ID是用于区分不同的源的身份的全局唯一的28bits值，显式发送。

   Source ID is a globally unique 28-bit value used to distinguish identities of different sources, explicitly transmitted.

Profile5
~~~~~~~~~~~~~~~~~~~~~~~~~~~
 - CRC保护(CRC Protection)

   Profile5使用16 bit polynomial为0x1021的算法对数据的完整性进行校验。

   Profile5 uses an algorithm with 16-bit polynomial 0x1021 to verify data integrity.

 - Sequence counter/alive counter

   8-bit的Sequence counter/alive counter, 递增计数器用来判断接收数据是否有序递增，心跳计数器用来判断数据是否发生改变。

   An 8-bit Sequence counter/alive counter; the sequence counter determines if received data is sequentially increasing, the alive counter detects if data has changed.

 - DataID

   DataID使用特定的ID来区分不同的I-PDU组，Profile5使用了全局唯一的16bit的DataID进行隐式发送。

   DataID uses specific IDs to distinguish different I-PDU groups. Profile5 uses globally unique 16-bit DataID for implicit transmission.

Profile6
~~~~~~~~~~~~~~~~~~~~~~~~~~~
 - CRC保护 (CRC Protection)

   Profile6使用16 bit polynomial为0x1021的算法对数据的完整性进行校验。

   Profile6 uses an algorithm with 16-bit polynomial 0x1021 to verify data integrity.

 - Sequence counter/alive counter

   8-bit的Sequence counter/alive counter, 递增计数器用来判断接收数据是否有序递增，心跳计数器用来判断数据是否发生改变。

   An 8-bit Sequence counter/alive counter; the sequence counter determines if received data is sequentially increasing, the alive counter detects if data has changed.

 - DataID

   DataID使用特定的ID来区分不同的I-PDU组，Profile6使用了全局唯一的16bit的DataID进行隐式发送。

   DataID uses specific IDs to distinguish different I-PDU groups. Profile6 uses globally unique 16-bit DataID for implicit transmission.

 - Data Length

   Profile6使用16bit的Data Length来支持动态大小的输入数据。

   Profile6 uses 16-bit Data Length to support dynamic-size input data.

Profile7
~~~~~~~~~~~~~~~~~~~~~~~~~~~
 - CRC保护 (CRC Protection)

   Profile7使用64 bit polynomial为0x42F0E1EBA9EA3693的算法对数据的完整性进行校验。

   Profile7 uses an algorithm with 64-bit polynomial 0x42F0E1EBA9EA3693 to verify data integrity.

 - Sequence counter/alive counter

   32-bit的Sequence counter/alive counter, 递增计数器用来判断接收数据是否有序递增，心跳计数器用来判断数据是否发生改变。

   A 32-bit Sequence counter/alive counter; the sequence counter determines if received data is sequentially increasing, the alive counter detects if data has changed.

 - DataID

   DataID使用特定的ID来区分不同的I-PDU组，Profile7使用了全局唯一的32bit的DataID进行隐式发送。

   DataID uses specific IDs to distinguish different I-PDU groups. Profile7 uses globally unique 32-bit DataID for implicit transmission.

 - Data Length

   Profile7使用32bit的Data Length来支持动态大小的输入数据。

   Profile7 uses 32-bit Data Length to support dynamic-size input data.

Profile7m
~~~~~~~~~~~~~~~~~~~~~~~~~~~
 - CRC保护(CRC Protection)

   Profile7m使用64 bit polynomial为0x42F0E1EBA9EA3693的算法对数据的完整性进行校验。

   Profile7m uses an algorithm with 64-bit polynomial 0x42F0E1EBA9EA3693 to verify data integrity.

 - Sequence counter/alive counter

   32-bit的Sequence counter/alive counter, 递增计数器用来判断接收数据是否有序递增，心跳计数器用来判断数据是否发生改变。

   A 32-bit Sequence counter/alive counter; the sequence counter determines if received data is sequentially increasing, the alive counter detects if data has changed.

 - DataID

   DataID使用特定的ID来区分不同的I-PDU组，Profile7m使用了全局唯一的32bit的DataID进行隐式发送。

   DataID uses specific IDs to distinguish different I-PDU groups. Profile7m uses globally unique 32-bit DataID for implicit transmission.

 - Data Length

   Profile7m使用32bit的Data Length来支持动态大小的输入数据。

   Profile7m uses 32-bit Data Length to support dynamic-size input data.

 - Message Type

   Message Type是用于区分请求和回复信息的2bits值，显式发送。

   Message Type is a 2-bit value used to distinguish between request and reply information, explicitly transmitted.

 - Message Result

   Message Result是用于区分正常回复和错误回复的2bits值，显式发送。

   Message Result is a 2-bit value used to distinguish between normal replies and error replies, explicitly transmitted.

 - Source ID

   Source ID是用于区分不同的源的身份的全局唯一的28bits值，显式发送。

   Source ID is a globally unique 28-bit value used to distinguish identities of different sources, explicitly transmitted.

Profile8
~~~~~~~~~~~~~~~~~~~~~~~~~~~
 - CRC保护 (CRC Protection)

   Profile8使用32 bit polynomial为0xF4ACFB13的算法对数据的完整性进行校验。

   Profile8 uses an algorithm with 32-bit polynomial 0xF4ACFB13 to verify data integrity.

 - Sequence counter/alive counter

   32-bit的Sequence counter/alive counter, 递增计数器用来判断接收数据是否有序递增，心跳计数器用来判断数据是否发生改变。

   A 32-bit Sequence counter/alive counter; the sequence counter determines if received data is sequentially increasing, the alive counter detects if data has changed.

 - DataID

   DataID使用特定的ID来区分不同的I-PDU组，Profile8使用了全局唯一的32bit的DataID进行显式发送。

   DataID uses specific IDs to distinguish different I-PDU groups. Profile8 uses globally unique 32-bit DataID for explicit transmission.

 - Data Length

   Profile8使用32bit的Data Length来支持动态大小的输入数据。

   Profile8 uses 32-bit Data Length to support dynamic-size input data.

Profile8m
~~~~~~~~~~~~~~~~~~~~~~~~~~~
 - CRC保护 (CRC Protection)

   Profile8m使用32 bit polynomial为0xF4ACFB13的算法对数据的完整性进行校验。

   Profile8m uses an algorithm with 32-bit polynomial 0xF4ACFB13 to verify data integrity.

 - Sequence counter/alive counter

   32-bit的Sequence counter/alive counter, 递增计数器用来判断接收数据是否有序递增，心跳计数器用来判断数据是否发生改变。

   A 32-bit Sequence counter/alive counter; the sequence counter determines if received data is sequentially increasing, the alive counter detects if data has changed.

 - DataID

   DataID使用特定的ID来区分不同的I-PDU组，Profile8m使用了全局唯一的32bit的DataID进行显式发送。

   DataID uses specific IDs to distinguish different I-PDU groups. Profile8m uses globally unique 32-bit DataID for explicit transmission.

 - Data Length

   Profile8m使用32bit的Data Length来支持动态大小的输入数据。

   Profile8m uses 32-bit Data Length to support dynamic-size input data.

 - Message Type

   Message Type是用于区分请求和回复信息的2bits值，显式发送。

   Message Type is a 2-bit value used to distinguish between request and reply information, explicitly transmitted.

 - Message Result

   Message Result是用于区分正常回复和错误回复的2bits值，显式发送。

   Message Result is a 2-bit value used to distinguish between normal replies and error replies, explicitly transmitted.

 - Source ID

   Source ID是用于区分不同的源的身份的全局唯一的28bits值，显式发送。

   Source ID is a globally unique 28-bit value used to distinguish identities of different sources, explicitly transmitted.

Profile11
~~~~~~~~~~~~~~~~~~~~~~~~~~~
 - CRC保护

   Profile11使用CRC-8-SAE J1850的算法对数据的完整性进行校验。

   Profile11 uses the CRC-8-SAE J1850 algorithm to verify data integrity.

 - Sequence counter/alive counter

   4-bit的Sequence counter/alive counter, 递增计数器用来判断接收数据是否有序递增，心跳计数器用来判断数据是否发生改变。

   A 4-bit Sequence counter/alive counter; the sequence counter determines if received data is sequentially increasing, the alive counter detects if data has changed.

 - DataID

   Profile11通过特定的ID来区分不同的I-PDU组，它分为了两种ID模式：

   Profile11 distinguishes different I-PDU groups through specific IDs, divided into two ID modes:

   Both bytes (dataIdMode=0):16位数据ID的两个字节都附加在安全数据上用于CRC计算，但没有显式发送。

   Both bytes (dataIdMode=0): Both bytes of the 16-bit Data ID are appended to safety data for CRC calculation but not explicitly transmitted.

   显式传输数据ID nibble (dataIdMode=3): 16位数据ID的两个字节都附加在安全数据上进行CRC计算，但数据ID高字节的低字节显式传输。在这个16位的数据ID中只使用了12位。

   Explicit transmission of data ID nibble (dataIdMode=3): Both bytes of 16-bit Data ID are appended to safety data for CRC calculation, but low nibble of high byte is explicitly transmitted. Only 12 bits are used in this 16-bit Data ID.

Profile22
~~~~~~~~~~~~~~~~~~~~~~~~~~~
 - CRC保护 (CRC Protection)

   Profile22使用8bit Polynomial为0x2f的算法对数据的完整性进行校验。

   Profile22 uses an algorithm with 8-bit Polynomial 0x2f to verify data integrity.

 - DataID

   DataID使用特定的ID来区分不同的I-PDU组，Profile22使用了一个预设的DataID列表，并通过Counter的值来选择DataID列表里的特定的DataID。

   DataID uses specific IDs to distinguish different I-PDU groups. Profile22 uses a preset DataID list and selects specific DataIDs from the list based on Counter values.

Profile44
~~~~~~~~~~~~~~~~~~~~~~~~~~~
 - CRC保护 (CRC Protection)

   Profile44使用32 bit polynomial为0x1F4ACFB13的算法对数据的完整性进行校验。

   Profile44 uses an algorithm with 32-bit polynomial 0x1F4ACFB13 to verify data integrity.

 - Sequence counter/alive counter

   16-bit的Sequence counter/alive counter, 递增计数器用来判断接收数据是否有序递增，心跳计数器用来判断数据是否发生改变。

   A 16-bit Sequence counter/alive counter; the sequence counter determines if received data is sequentially increasing, the alive counter detects if data has changed.

 - Data Length

   Profile44使用16bit的Data Length来支持动态大小的输入数据。

   Profile44 uses 16-bit Data Length to support dynamic-size input data.

 - DataID

   DataID使用特定的ID来区分不同的I-PDU组，Profile44使用了全局唯一的32bit的DataID进行显式发送。

   DataID uses specific IDs to distinguish different I-PDU groups. Profile44 uses globally unique 32-bit DataID for explicit transmission.

Profile44m
~~~~~~~~~~~~~~~~~~~~~~~~~~~
 - CRC保护 (CRC Protection)

   Profile44m使用32 bit polynomial为0x1F4ACFB13的算法对数据的完整性进行校验。

   Profile44m uses an algorithm with 32-bit polynomial 0x1F4ACFB13 to verify data integrity.

 - Sequence counter/alive counter

   16-bit的Sequence counter/alive counter, 递增计数器用来判断接收数据是否有序递增，心跳计数器用来判断数据是否发生改变。

   A 16-bit Sequence counter/alive counter; the sequence counter determines if received data is sequentially increasing, the alive counter detects if data has changed.

 - Data Length

   Profile44m使用16bit的Data Length来支持动态大小的输入数据。

   Profile44m uses 16-bit Data Length to support dynamic-size input data.

 - DataID

   DataID使用特定的ID来区分不同的I-PDU组，Profile44m使用了全局唯一的32bit的DataID进行显式发送。

   DataID uses specific IDs to distinguish different I-PDU groups. Profile44m uses globally unique 32-bit DataID for explicit transmission.

 - Message Type

   Message Type是用于区分请求和回复信息的2bits值，显式发送。

   Message Type is a 2-bit value used to distinguish between request and reply information, explicitly transmitted.

 - Message Result

   Message Result是用于区分正常回复和错误回复的2bits值，显式发送。

   Message Result is a 2-bit value used to distinguish between normal replies and error replies, explicitly transmitted.

 - Source ID

   Source ID是用于区分不同的源的身份的全局唯一的28bits值，显式发送。

   Source ID is a globally unique 28-bit value used to distinguish identities of different sources, explicitly transmitted.

偏差(Deviation)
------------------
.. 有序列表示例

#. E2E Wrapper未实现(E2E Wrapper is not implemented)
   
   因为我们E2E的调用均通过RTE的transformer进行实现

   Because our E2E calls are all implemented through the RTE transformer

#. forward未实现(forward is not implemented)

   因为暂无需求
   
   Because there is currently no requirement

扩展(Extensions)
-----------------------------------------
None

集成(Integration)
============================

文件列表(File List)
-------------------------------

静态文件(Static Files)
~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - 文件(File)
     - 描述(Description)
   
   * - E2E_P01.c
     - E2E Profile1算法库源文件(Source file of E2E Profile1 algorithm library)
       
   * - E2E_P01.h
     - E2E Profile1算法库头文件(Header file of E2E Profile1 algorithm library)
       
   * - E2E_P02.c
     - E2E Profile2算法库源文件(Source file of E2E Profile2 algorithm library)
       
   * - E2E_P02.h
     - E2E Profile2算法库头文件(Header file of E2E Profile2 algorithm library)
       
   * - E2E_P04.c
     - E2E Profile4算法库源文件(Source file of E2E Profile4 algorithm library)
       
   * - E2E_P04.h
     - E2E Profile4算法库头文件(Header file of E2E Profile4 algorithm library)
       
   * - E2E_P04m.c
     - E2E Profile4m算法库源文件(Source file of E2E Profile4m algorithm library)
       
   * - E2E_P04m.h
     - E2E Profile4m算法库头文件(Header file of E2E Profile4m algorithm library)

   * - E2E_P05.c
     - E2E Profile5算法库源文件(Source file of E2E Profile5 algorithm library)
       
   * - E2E_P05.h
     - E2E Profile5算法库头文件(Header file of E2E Profile5 algorithm library)
       
   * - E2E_P06.c
     - E2E Profile6算法库源文件(Source file of E2E Profile6 algorithm library)
       
   * - E2E_P06.h
     - E2E Profile6算法库头文件(Header file of E2E Profile6 algorithm library)
       
   * - E2E_P07.c
     - E2E Profile7算法库源文件(Source file of E2E Profile7 algorithm library)
       
   * - E2E_P07.h
     - E2E Profile7算法库头文件(Header file of E2E Profile7 algorithm library)
       
   * - E2E_P07m.c
     - E2E Profile7m算法库源文件(Source file of E2E Profile7m algorithm library)
       
   * - E2E_P07m.h
     - E2E Profile7m算法库头文件(Header file of E2E Profile7m algorithm library)
       
   * - E2E_P08.c
     - E2E Profile8算法库源文件(Source file of E2E Profile8 algorithm library)
       
   * - E2E_P08.h
     - E2E Profile8算法库头文件(Header file of E2E Profile8 algorithm library)

   * - E2E_P08m.c
     - E2E Profile8m算法库源文件(Source file of E2E Profile8m algorithm library)
       
   * - E2E_P08m.h
     - E2E Profile8m算法库头文件(Header file of E2E Profile8m algorithm library)
       
   * - E2E_P11.c
     - E2E Profile11算法库源文件(Source file of E2E Profile11 algorithm library)
       
   * - E2E_P11.h
     - E2E Profile11算法库头文件(Header file of E2E Profile11 algorithm library)
       
   * - E2E_P22.c
     - E2E Profile22算法库源文件(Source file of E2E Profile22 algorithm library)
       
   * - E2E_P22.h
     - E2E Profile22算法库头文件(Header file of E2E Profile22 algorithm library)
       
   * - E2E_P44.c
     - E2E Profile44算法库源文件(Source file of E2E Profile44 algorithm library)
       
   * - E2E_P44.h
     - E2E Profile44算法库头文件(Header file of E2E Profile44 algorithm library)
       
   * - E2E_P44m.c
     - E2E Profile44m算法库源文件(Source file of E2E Profile44m algorithm library)
       
   * - E2E_P44m.h
     - E2E Profile44m算法库头文件(Header file of E2E Profile44m algorithm library)
       
   * - E2E.c
     - E2E状态机管理(E2E state machine management)
       
   * - E2E.h
     - E2E的共有头文件(Common header file of E2E)

.. figure:: ../../../_static/参考手册/E2E/image3.png
   :alt: E2EL组件文件交互关系图(E2EL Component Files Interaction Diagram)
   :name: fig_E2E1
   :align: center

   E2EL组件文件交互关系图 (E2EL Component Files Interaction Diagram)


动态文件(Dynamic Files)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
None

错误处理(Error Handling)
--------------------------------

开发错误(Development Errors)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
None

产品错误(Product Errors)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
None

运行时错误(Runtime Errors)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. list-table:: 
   :widths: 20 10 30
   :header-rows: 1

   * - Error code
     - Value[hex]
     - Description

   * - E2E_E_INPUTERR_NULL
     - 0x13
     - At least one pointer parameter is a NULL pointer

   * - E2E_E_INPUTERR_WRONG
     - 0x17
     - At least one input parameter is erroneous, e.g. out of range

   * - E2E_E_INTERR
     - 0x19
     - An internal library error has occurred (e.g. error detected by program flow monitoring, violated invariant or postcondition)

   * - E2E_E_WRONGSTATE
     - 0x1A
     - Function executed in wrong state



.. 引用接口描述。来自于code->doxygen->latex->rst
.. include:: E2E_h_api.rst
.. include:: E2E_P01_h_api.rst
.. include:: E2E_P02_h_api.rst
.. include:: E2E_P04_h_api.rst
.. include:: E2E_P04m_h_api.rst
.. include:: E2E_P05_h_api.rst
.. include:: E2E_P06_h_api.rst
.. include:: E2E_P07_h_api.rst
.. include:: E2E_P07m_h_api.rst
.. include:: E2E_P08_h_api.rst
.. include:: E2E_P08m_h_api.rst
.. include:: E2E_P11_h_api.rst
.. include:: E2E_P22_h_api.rst
.. include:: E2E_P44_h_api.rst
.. include:: E2E_P44m_h_api.rst

配置(Configuration)
===============================
None

