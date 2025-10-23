IOC Functions
--------------------------------------
IOC负责Os-Application之间的通信，特别是跨越核心或存储器保护边界的通信。 其内部功能与操作系统密切相关。IOC 支持 1:1、N:1 和 N:M 通信。同时支持队列和非队列通信。

IOC is responsible for communication between Os-Applications, especially communication across core or memory protection boundaries. Its internal functions are closely related to the operating system. IOC supports 1:1, N:1, and N:M communication. It also supports both queued and non-queued communication.


IocSend_<IocId>[_<SenderId>]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    StatusType IocSend_<IocId>[_<SenderId>] (<Data> IN, [uint16 numberOfBytesIN])

Send data to implement 1:1 or N:1 queue communication between Os-Applications located on the same or different cores.

**Sync/Async**
   FALSE

**Reentrancy**
   This function is generated individually for each sender. A single function is not reentrant (if called from different runnable entities belonging to the same sender), but different functions can be called in parallel.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - IN
     - The data value sent is identified by <IocId>. Parameters are passed by value for primitive data elements and by reference for all other types.
   * - [in]
     - numberOfBytesIN
     - Number of bytes to send (optional generation)

**Return type**
   StatusType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - IOC_E_OK
     - The data has been successfully delivered to the communication service.
   * - IOC_E_LIMIT
     - IOC internal communication buffer is full (scenario: receiver is slower than sender). This error will generate an IOC_E_LOST_DATA override error on the receiver side on the next data reception.
   * - IOC_E_LENGTH
     - <numberOfBytesIN> exceeds the internal buffer or is equal to 0, so no data is sent.

**Example**

.. code::

   - OsIocBufferLength：20
   - OsIocDataProperties：
     - OsIocDataProperties_0：
       - OsIocDataPropertyIndex：0
       - OsIocInitValue：0xFF
       - ArrayLength：Not checked
       - OsIocDataTypeRef：uint32
   - OsIocReceiverProperties：
     - OsIocReceiverProperties_0：
       - OsIocReceiverId：0
       - OsIocReceiverPullCB：ReceiverPullCB_0
       - OsIocReceivingOsApplicationRef：OsApplication_0_core0
   - OsIocSenderProperties：
     - OsIocSenderProperties_0：
       - OsIocSenderId：0
       - OsIocSendingOsApplicationRef：OsApplication_1_Core0


    TASK(Task0)  /* core 0*/ /*OsApplication_1*/ 
    {
    uint32 Sourcedata = 0xAA;
    IocSend_0(Sourcedata);
    }

    TASK(Task0)  /* core 0*/ /*OsApplication_0*/ 
    {
    uint32 desData;
    IocReceive_0(&desData);
    }

.. note::

   - 此接口一般直接由RTE进行调用。

     This interface is generally called directly by the RTE.

   - ORIENTAIS OS支持无RTE时直接调用。

     ORIENTAIS OS supports direct calling without the RTE.


IocWrite_<IocId>[_<SenderId>]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    StatusType IocWrite_<IocId>[_<SenderId>] (<Data> IN, [uint16 numberOfBytesIN])

Send data to implement 1:1 or N:1 non-queue communication between Os-Applications located on the same or different cores.

**Sync/Async**
   FALSE

**Reentrancy**
   This function is generated individually for each sender. A single function is not reentrant (if called from different runnable entities belonging to the same sender), but different functions can be called in parallel.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - IN
     - The data value sent is identified by <IocId>. Parameters are passed by value for primitive data elements and by reference for all other types.
   * - [in]
     - numberOfBytesIN
     - Number of bytes to send (optional generation)

**Return type**
   StatusType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - IOC_E_OK
     - The data has been successfully delivered to the communication service.

**Example**

.. code::

   - OsIocBufferLength：Not checked
   - OsIocDataProperties：
     - OsIocDataProperties_0：
       - OsIocDataPropertyIndex：0
       - OsIocInitValue：0xFF
       - ArrayLength：Not checked
       - OsIocDataTypeRef：uint32
   - OsIocReceiverProperties：
     - OsIocReceiverProperties_0：
       - OsIocReceiverId：0
       - OsIocReceiverPullCB：ReceiverPullCB_0
       - OsIocReceivingOsApplicationRef：OsApplication_0_core0
   - OsIocSenderProperties：
     - OsIocSenderProperties_0：
       - OsIocSenderId：0
       - OsIocSendingOsApplicationRef：OsApplication_1_Core0

    TASK(Task0)  /* core 0*/ /*OsApplication_1*/ 
    {
    uint32 Sourcedata = 0xAA;
    IocWrite_0(Sourcedata);
    }

    TASK(Task0)  /* core 0*/ /*OsApplication_0*/ 
    {
    uint32 desData;
    IocRead_0(&desData);
    }

.. note::

   - 此接口一般直接由RTE进行调用。

     This interface is generally called directly by the RTE.

   - ORIENTAIS OS支持无RTE时直接调用。

     ORIENTAIS OS supports direct calling without the RTE.



IocSendGroup_<IocId>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    StatusType IocSendGroup_<IocId> (<Data1> IN1, [uint16 numberOfBytesIN1], <Data2> IN2, [uint16 numberOfBytesIN2], ...)

Send a set of data to implement 1:1 or N:1 queue communication between Os-Applications located on the same or different cores.

**Sync/Async**
   FALSE

**Reentrancy**
   This function is generated individually for each sender. A single function is not reentrant (if called from different runnable entities belonging to the same sender), but different functions can be called in parallel.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - IN
     - The data value sent is identified by <IocId>. Parameters are passed by value for primitive data elements and by reference for all other types.
   * - [in]
     - numberOfBytesIN
     - Number of bytes to send (optional generation)

**Return type**
   StatusType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - IOC_E_OK
     - The data has been successfully delivered to the communication service.
   * - IOC_E_LIMIT
     - The IOC internal communication buffer is full (situation: the receiver is slower than the sender). This error will generate an IOC_E_LOST_DATA override error on the receiver side on the next data reception.
   * - IOC_E_LENGTH
     - <numberOfBytesIN> is outside the internal buffer or equal to 0, so no data will be sent.

**Example**

.. code::

   - OsIocBufferLength：20
   - OsIocDataProperties：
     - OsIocDataProperties_0：
       - OsIocDataPropertyIndex：0
       - OsIocInitValue：0xFF
       - ArrayLength：Not checked
       - OsIocDataTypeRef：uint32
     - OsIocDataProperties_1：
       - OsIocDataPropertyIndex：1
       - OsIocInitValue：Not checked
       - ArrayLength：20
       - OsIocDataTypeRef：uint16
   - OsIocReceiverProperties：
     - OsIocReceiverProperties_0：
       - OsIocReceiverId：0
       - OsIocReceiverPullCB：ReceiverPullCB_0
       - OsIocReceivingOsApplicationRef：OsApplication_0_core0
   - OsIocSenderProperties：
     - OsIocSenderProperties_0：
       - OsIocSenderId：0
       - OsIocSendingOsApplicationRef：OsApplication_1_Core0

    TASK(Task0)  /* core 0*/ /*OsApplication_1*/ 
    {
    uint32 Sourcedata0 = 0xAA;
    uint16 Sourcedata1 = 0xAA;
    IocSendGroup_0(Sourcedata0 ,Sourcedata1);
    }

    TASK(Task0)  /* core 0*/ /*OsApplication_0*/ 
    {
    uint32 desData0;
    uint32 desData1;
    IocReceiveGroup_0(&desData0 ,desData1);
    }

.. note::

   - 此接口一般直接由RTE进行调用。

     This interface is generally called directly by the RTE.

   - ORIENTAIS OS支持无RTE时直接调用。

     ORIENTAIS OS supports direct calling without the RTE.


IocWriteGroup_<IocId>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    StatusType IocWriteGroup_<IocId> (<Data1> IN1, [uint16 numberOfBytesIN1], <Data2> IN2, [uint16 numberOfBytesIN2], ...)

Send a set of data to achieve 1:1 or N:1 non-queue communication between Os-Applications located on the same or different cores.

**Sync/Async**
   FALSE

**Reentrancy**
   This function is generated individually for each sender. A single function is not reentrant (if called from different runnable entities belonging to the same sender), but different functions can be called in parallel.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - IN
     - The data value sent is identified by <IocId>. Parameters are passed by value for primitive data elements and by reference for all other types.
   * - [in]
     - numberOfBytesIN
     - Number of bytes to send (optional generation)

**Return type**
   StatusType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - IOC_E_OK
     - The data has been successfully delivered to the communication service.
   * - IOC_E_LIMIT
     - The IOC internal communication buffer is full (situation: the receiver is slower than the sender). This error will generate an IOC_E_LOST_DATA override error on the receiver side on the next data reception.
   * - IOC_E_LENGTH
     - <numberOfBytesIN> is outside the internal buffer or equal to 0, so no data will be sent.

**Example**

.. code::

   - OsIocBufferLength：Not checked
   - OsIocDataProperties：
     - OsIocDataProperties_0：
       - OsIocDataPropertyIndex：0
       - OsIocInitValue：0xFF
       - ArrayLength：Not checked
       - OsIocDataTypeRef：uint32
     - OsIocDataProperties_1：
       - OsIocDataPropertyIndex：1
       - OsIocInitValue：Not checked
       - ArrayLength：20
       - OsIocDataTypeRef：uint16
   - OsIocReceiverProperties：
     - OsIocReceiverProperties_0：
       - OsIocReceiverId：0
       - OsIocReceiverPullCB：ReceiverPullCB_0
       - OsIocReceivingOsApplicationRef：OsApplication_0_core0
   - OsIocSenderProperties：
     - OsIocSenderProperties_0：
       - OsIocSenderId：0
       - OsIocSendingOsApplicationRef：OsApplication_1_Core0

    TASK(Task0)  /* core 0*/ /*OsApplication_1*/ 
    {
    uint32 Sourcedata0 = 0xAA;
    uint16 Sourcedata1 = 0xAA;
    IocWriteGroup_0(Sourcedata0 ,Sourcedata1);
    }

    TASK(Task0)  /* core 0*/ /*OsApplication_0*/ 
    {
    uint32 desData0;
    uint32 desData1;
    IocReadGroup_0(&desData0 ,desData1);
    }

.. note::

   - 此接口一般直接由RTE进行调用。

     This interface is generally called directly by the RTE.

   - ORIENTAIS OS支持无RTE时直接调用。

     ORIENTAIS OS supports direct calling without the RTE.


IocReceive_<IocId>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    StatusType IocReceive_<IocId> (<Data> OUT, [uint16* numberOfBytesOUT])

Receive data and implement 1:1 or N:1 queue communication between Os-Applications located on the same or different cores.

**Sync/Async**
   FALSE

**Reentrancy**
   The function is generated individually for each receiver. A single function is not reentrant (if called from different runnable entities belonging to the same receiver), but different functions can be called in parallel.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [out]
     - OUT
     - Receives a data reference for a data element.
   * - [out]
     - numberOfBytesOUT
     - Number of bytes to receive (optional generation)

**Return type**
   StatusType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - IOC_E_OK
     - Data was received successfully.
   * - IOC_E_NO_DATA
     - No data is available for reception.
   * - IOC_E_LOST_DATA
     - This Overlayed Error indicates that the IOC communication service refused an IOCSend request from sender due to an internal buffer overflow. There is no error in the data returned in parameter.

**Example**

.. code::

   - OsIocBufferLength：20
   - OsIocDataProperties：
     - OsIocDataProperties_0：
       - OsIocDataPropertyIndex：0
       - OsIocInitValue：0xFF
       - ArrayLength：Not checked
       - OsIocDataTypeRef：uint32
   - OsIocReceiverProperties：
     - OsIocReceiverProperties_0：
       - OsIocReceiverId：0
       - OsIocReceiverPullCB：ReceiverPullCB_0
       - OsIocReceivingOsApplicationRef：OsApplication_0_core0
   - OsIocSenderProperties：
     - OsIocSenderProperties_0：
       - OsIocSenderId：0
       - OsIocSendingOsApplicationRef：OsApplication_1_Core0

    TASK(Task0)  /* core 0*/ /*OsApplication_1*/ 
    {
    uint32 Sourcedata = 0xAA;
    IocSend_0(Sourcedata);
    }

    TASK(Task0)  /* core 0*/ /*OsApplication_0*/ 
    {
    uint32 desData;
    IocReceive_0(&desData);
    }

.. note::

   - 此接口一般直接由RTE进行调用。

     This interface is generally called directly by the RTE.

   - ORIENTAIS OS支持无RTE时直接调用。

     ORIENTAIS OS supports direct calling without the RTE.


IocRead_<IocId>[_<ReceiverId>]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    StatusType IocRead_<IocId>[_<ReceiverId>] (<Data> OUT, [uint16* numberOfBytesOUT])

Receive data to implement 1:1 or N:1 non-queue communication between Os-Applications located on the same or different cores.

**Sync/Async**
   FALSE

**Reentrancy**
   The function is generated individually for each receiver. A single function is not reentrant (if called from different runnable entities belonging to the same receiver), but different functions can be called in parallel.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [out]
     - OUT
     - Receives a data reference for a data element.
   * - [out]
     - numberOfBytesOUT
     - Number of bytes to receive (optional generation)

**Return type**
   StatusType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - IOC_E_OK
     - Data was received successfully.

**Example**

.. code::

   - OsIocBufferLength：Not checked
   - OsIocDataProperties：
     - OsIocDataProperties_0：
       - OsIocDataPropertyIndex：0
       - OsIocInitValue：0xFF
       - ArrayLength：Not checked
       - OsIocDataTypeRef：uint32
   - OsIocReceiverProperties：
     - OsIocReceiverProperties_0：
       - OsIocReceiverId：0
       - OsIocReceiverPullCB：ReceiverPullCB_0
       - OsIocReceivingOsApplicationRef：OsApplication_0_core0
   - OsIocSenderProperties：
     - OsIocSenderProperties_0：
       - OsIocSenderId：0
       - OsIocSendingOsApplicationRef：OsApplication_1_Core0

    TASK(Task0)  /* core 0*/ /*OsApplication_1*/ 
    {
    uint32 Sourcedata = 0xAA;
    IocWrite_0(Sourcedata);
    }

    TASK(Task0)  /* core 0*/ /*OsApplication_0*/ 
    {
    uint32 desData;
    IocRead_0(&desData);
    }

.. note::

   - 此接口一般直接由RTE进行调用。

     This interface is generally called directly by the RTE.

   - ORIENTAIS OS支持无RTE时直接调用。

     ORIENTAIS OS supports direct calling without the RTE.


IocReceiveGroup_<IocId>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    StatusType IocReceiveGroup_<IocId> (<Data1> OUT1, [uint16* numberOfBytesOUT1], <Data2> OUT2, [uint16* numberOfBytesOUT2], ...)

Receive a set of data to implement 1:1 or N:1 queue communication between Os-Applications located on the same or different cores.

**Sync/Async**
   FALSE

**Reentrancy**
   The function is generated individually for each receiver. A single function is not reentrant (if called from different runnable entities belonging to the same receiver), but different functions can be called in parallel.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [out]
     - OUT
     - Receives a data reference for a data element.
   * - [out]
     - numberOfBytesOUT
     - Number of bytes to receive (optional generation)

**Return type**
   StatusType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - IOC_E_OK
     - Data was received successfully.
   * - IOC_E_NO_DATA
     - No data is available for reception.
   * - IOC_E_LOST_DATA
     - This Overlayed Error indicates that the IOC communication service refused an IOCSend request from sender due to an internal buffer overflow. There is no error in the data returned in parameter.

**Example**

.. code::

   - OsIocBufferLength：20
   - OsIocDataProperties：
     - OsIocDataProperties_0：
       - OsIocDataPropertyIndex：0
       - OsIocInitValue：0xFF
       - ArrayLength：Not checked
       - OsIocDataTypeRef：uint32
     - OsIocDataProperties_1：
       - OsIocDataPropertyIndex：1
       - OsIocInitValue：Not checked
       - ArrayLength：20
       - OsIocDataTypeRef：uint16
   - OsIocReceiverProperties：
     - OsIocReceiverProperties_0：
       - OsIocReceiverId：0
       - OsIocReceiverPullCB：ReceiverPullCB_0
       - OsIocReceivingOsApplicationRef：OsApplication_0_core0
   - OsIocSenderProperties：
     - OsIocSenderProperties_0：
       - OsIocSenderId：0
       - OsIocSendingOsApplicationRef：OsApplication_1_Core0

    TASK(Task0)  /* core 0*/ /*OsApplication_1*/ 
    {
    uint32 Sourcedata0 = 0xAA;
    uint16 Sourcedata1 = 0xAA;
    IocSendGroup_0(Sourcedata0 ,Sourcedata1);
    }

    TASK(Task0)  /* core 0*/ /*OsApplication_0*/ 
    {
    uint32 desData0;
    uint32 desData1;
    IocReceiveGroup_0(&desData0 ,desData1);
    }

.. note::

   - 此接口一般直接由RTE进行调用。

     This interface is generally called directly by the RTE.

   - ORIENTAIS OS支持无RTE时直接调用。

     ORIENTAIS OS supports direct calling without the RTE.


IocReadGroup_<IocId>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    StatusType IocReadGroup_<IocId> (<Data1> OUT1, [uint16* numberOfBytesOUT1], <Data2> OUT2, [uint16* numberOfBytesOUT2], ...)

Receives a set of data to implement 1:1 or N:1 non-queue communication between Os-Applications located on the same or different cores.

**Sync/Async**
   FALSE

**Reentrancy**
   The function is generated individually for each receiver. A single function is not reentrant (if called from different runnable entities belonging to the same receiver), but different functions can be called in parallel.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [out]
     - OUT
     - Receives a data reference for a data element.
   * - [out]
     - numberOfBytesOUT
     - Number of bytes to receive (optional generation)

**Return type**
   StatusType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - IOC_E_OK
     - Data was received successfully.

**Example**

.. code::

   - OsIocBufferLength：Not checked
   - OsIocDataProperties：
     - OsIocDataProperties_0：
       - OsIocDataPropertyIndex：0
       - OsIocInitValue：0xFF
       - ArrayLength：Not checked
       - OsIocDataTypeRef：uint32
     - OsIocDataProperties_1：
       - OsIocDataPropertyIndex：1
       - OsIocInitValue：Not checked
       - ArrayLength：20
       - OsIocDataTypeRef：uint16
   - OsIocReceiverProperties：
     - OsIocReceiverProperties_0：
       - OsIocReceiverId：0
       - OsIocReceiverPullCB：ReceiverPullCB_0
       - OsIocReceivingOsApplicationRef：OsApplication_0_core0
   - OsIocSenderProperties：
     - OsIocSenderProperties_0：
       - OsIocSenderId：0
       - OsIocSendingOsApplicationRef：OsApplication_1_Core0

    TASK(Task0)  /* core 0*/ /*OsApplication_1*/ 
    {
    uint32 Sourcedata0 = 0xAA;
    uint16 Sourcedata1 = 0xAA;
    IocWriteGroup_0(Sourcedata0 ,Sourcedata1);
    }

    TASK(Task0)  /* core 0*/ /*OsApplication_0*/ 
    {
    uint32 desData0;
    uint32 desData1;
    IocReadGroup_0(&desData0 ,desData1);
    }

.. note::

   - 此接口一般直接由RTE进行调用。

     This interface is generally called directly by the RTE.

   - ORIENTAIS OS支持无RTE时直接调用。

     ORIENTAIS OS supports direct calling without the RTE.



IocEmptyQueue_<IocId>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    StatusType IocEmptyQueue_<IocId> (void)

If the <IocId> in the function name identifies queued communication, this interface can be called to delete the contents of the IOC internal communication queue.

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant

**Return type**
   StatusType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - IOC_E_OK
     - The queue contents were successfully deleted.

**Example**

.. code::

   - OsIocBufferLength：20
   - OsIocDataProperties：
     - OsIocDataProperties_0：
       - OsIocDataPropertyIndex：0
       - OsIocInitValue：0xFF
       - ArrayLength：Not checked
       - OsIocDataTypeRef：uint32
   - OsIocReceiverProperties：
     - OsIocReceiverProperties_0：
       - OsIocReceiverId：0
       - OsIocReceiverPullCB：ReceiverPullCB_0
       - OsIocReceivingOsApplicationRef：OsApplication_0_core0
   - OsIocSenderProperties：
     - OsIocSenderProperties_0：
       - OsIocSenderId：0
       - OsIocSendingOsApplicationRef：OsApplication_1_Core0

    TASK(Task0)  /* core 0*/ /*OsApplication_1*/ 
    {
    uint32 Sourcedata = 0xAA;
    IocSend_0(Sourcedata);
    IocEmptyQueue_0();
    }

    TASK(Task0)  /* core 0*/ /*OsApplication_0*/ 
    {
    uint32 desData;
    IocReceive_0(&desData);
    }

.. note::

   - 此接口一般直接由RTE进行调用。

     This interface is generally called directly by the RTE.

   - ORIENTAIS OS支持无RTE时直接调用。

     ORIENTAIS OS supports direct calling without the RTE.





