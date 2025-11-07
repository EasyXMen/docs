Peripheral(Functions)
--------------------------------------

在某些MCU架构中，存在内存映射的硬件寄存器(外设区域)，这些寄存器只能在特定模式(例如特权模式)下访问。只要任务/中断服务例程(Tasks/ISRs)具有完全的硬件访问权限，它们就可以直接访问这些寄存器。如果操作系统使用了内存保护，那么非受信任的操作系统应用程序的任务/中断服务例程不能直接访问这些寄存器，因为这会被操作系统识别为内存违规。

In some MCU architectures, memory-mapped hardware registers (peripheral areas) exist that are accessible only in specific modes (e.g., privileged mode). As long as tasks/interrupt service routines (Tasks/ISRs) have full hardware access rights, they can directly access these registers. If the operating system employs memory protection, tasks/ISRs of untrusted OS-Applications cannot access these registers directly, as this is recognized by the OS as a memory violation.

外设访问的接口被划分为8位、16位和32位。为了简化表达，ReadPeripheral<x>代表ReadPeripheral8、ReadPeripheral16、ReadPeripheral32。WritePeripheral<x>代表WritePeripheral8、WritePeripheral16、WritePeripheral32。ModifyPeripheral<x>代表ModifyPeripheral8、ModifyPeripheral16、ModifyPeripheral32。

Peripheral access interfaces are categorized into 8-bit, 16-bit, and 32-bit types. For simplicity, ReadPeripheral<x> denotes ReadPeripheral8, ReadPeripheral16, and ReadPeripheral32; WritePeripheral<x> denotes WritePeripheral8, WritePeripheral16, and WritePeripheral32; and ModifyPeripheral<x> denotes ModifyPeripheral8, ModifyPeripheral16, and ModifyPeripheral32.


ReadPeripheral<x>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    StatusType ReadPeripheral8(AreaIdType Area, const uint8 *Address, uint8 *ReadValue)

    StatusType ReadPeripheral16(AreaIdType Area, const uint16 *Address, uint16 *ReadValue)
    
    StatusType ReadPeripheral32(AreaIdType Area, const uint32 *Address, uint32 *ReadValue)

This service returns the content of a given memory location (<Address>).

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - Area
     - hardware peripheral area reference
   * - [in]
     - Address
     - memory address, which will be read
   * - [out]
     - ReadValue
     - Returned value

**Return type**
   StatusType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - No error
   * - E_OS_ID
     - Area id is out of range (EXTENDED status)
   * - E_OS_VALUE
     - Address does not belong to given Area (EXTENDED status)
   * - E_OS_CALLEVEL
     - Wrong call context of the API function (EXTENDED status)
   * - E_OS_ACCESS
     - The calling task or ISR is not allowed to access the given


WritePeripheral<x>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    StatusType WritePeripheral8(AreaIdType Area, uint8 *Address, uint8 WriteValue)

    StatusType WritePeripheral16(AreaIdType Area, uint16 *Address, uint16 WriteValue)

    StatusType WritePeripheral32(AreaIdType Area, uint32 *Address, uint32 WriteValue)

This service writes theto a given memory location (<memory address>).

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - Area
     - hardware peripheral area reference
   * - [in]
     - Address
     - memory address, which will be writed
   * - [in]
     - WriteValue
     - write value

**Return type**
   StatusType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - No error
   * - E_OS_ID
     - Area id is out of range (EXTENDED status)
   * - E_OS_VALUE
     - Address does not belong to given Area (EXTENDED status)
   * - E_OS_CALLEVEL
     - Wrong call context of the API function (EXTENDED status)
   * - E_OS_ACCESS
     - The calling task or ISR is not allowed to access the given


ModifyPeripheral<x>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    StatusType ModifyPeripheral8(AreaIdType Area, uint8 *Address, uint8 Clearmask, uint8 Setmask)

    StatusType ModifyPeripheral16(AreaIdType Area, uint16 *Address, uint16 Clearmask, uint16 Setmask)

    StatusType ModifyPeripheral32(AreaIdType Area, uint32 *Address, uint32 Clearmask, uint32 Setmask)
    
    This service modifies a given memory location (<memory address>) with the formula: *<Address> = ((*<Address> & <clearmask>) | <setmask>)

This service modifies a given memory location (<memory address>).

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - Area
     - hardware peripheral area reference
   * - [in]
     - Address
     - memory address, which will be modified
   * - [in]
     - Clearmask
     - memory address will be modified by a bit-AND
   * - [in]
     - Setmask
     - memory address will be modified by a bit-OR

**Return type**
   StatusType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - No error
   * - E_OS_ID
     - Area id is out of range (EXTENDED status)
   * - E_OS_VALUE
     - Address does not belong to given Area (EXTENDED status)
   * - E_OS_CALLEVEL
     - Wrong call context of the API function (EXTENDED status)
   * - E_OS_ACCESS
     - The calling task or ISR is not allowed to access the given

**Example**

.. code::

    Spinlock_0:LockMethod:LOCK_NOTHING
    AccessingApplication: App0,App1
    App0:  Core: 0
    TaskInit: Priority:1, Preemptive Policy:FULL, Autostart:True

    TASK(Task0)  /* core 1*/
    {
      uint8* Address8 = REG_XXX1;
      uint8 ReadValue8 = 0;
      uint16* Address16 = REG_XXX2;
      uint16 ModifyValue16 = 165;
      uint32* Address32 = REG_XXX3;
    StatusType  status;
      
      status = ReadPeripheral8 (OsPeripheral_0, Address8, &ReadValue8);
      ......
      status = WritePeripheral16 (OsPeripheral_0, Address16, ModifyValue16);
      ......
      status = ModifyPeripheral32 (OsPeripheral_0, Address32, 0xff, 0xab);
      ......
    }





