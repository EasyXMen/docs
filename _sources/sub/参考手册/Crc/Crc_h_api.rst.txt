接口描述（Interface Description）
====================================

类型定义（Type definition）
-------------------------------
.. 如果没有就不存在该章节，或为None

None

      
提供的服务（Provided services）
----------------------------------
Crc_GetVersionInfo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Crc_GetVersionInfo(Std_VersionInfoType *versionInfo)

This service returns the version information of this module.

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
   * - [out]
     - versionInfo
     - Pointer to where to store the version

**Return type**
   void


Crc_CalculateCRC8
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    uint8 Crc_CalculateCRC8(const uint8 *Crc_DataPtr, uint32 Crc_Length, uint8 Crc_StartValue8, boolean Crc_IsFirstCall)

This service makes a CRC8 calculation on Crc_Length data bytes, with SAE J1850 parameters.

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
     - Crc_DataPtr
     - Pointer to start address of data block to be calculated.
   * - [in]
     - Crc_Length
     - Length of data block to be calculated in bytes.
   * - [in]
     - Crc_StartValue8
     - Start value when the algorithm starts.
   * - [in]
     - Crc_IsFirstCall
     - TRUE: First call in a sequence or individual CRC calculation; start from initial value, ignore Crc_StartValue8. FALSE:Subsequent call in a call sequence; Crc_StartValue8 is interpreted to be the return value of the previous function call.

**Return type**
   uint8


Crc_CalculateCRC8H2F
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    uint8 Crc_CalculateCRC8H2F(const uint8 *Crc_DataPtr, uint32 Crc_Length, uint8 Crc_StartValue8H2F, boolean Crc_IsFirstCall)

This service makes a CRC8 calculation with the Polynomial 0x2F on Crc_Length.

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
     - Crc_DataPtr
     - Pointer to start address of data block to be calculated.
   * - [in]
     - Crc_Length
     - Length of data block to be calculated in bytes.
   * - [in]
     - Crc_StartValue8H2F
     - Start value when the algorithm starts.
   * - [in]
     - Crc_IsFirstCall
     - TRUE: First call in a sequence or individual CRC calculation; start from initial value, ignore Crc_StartValue8H2F. FALSE:Subsequent call in a call sequence; Crc_StartValue8H2F is interpreted to be the return value of the previous function call.

**Return type**
   uint8


Crc_CalculateCRC16
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    uint16 Crc_CalculateCRC16(const uint8 *Crc_DataPtr, uint32 Crc_Length, uint16 Crc_StartValue16, boolean Crc_IsFirstCall)

This service makes a CRC16 calculation on Crc_Length data bytes.

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
     - Crc_DataPtr
     - Pointer to start address of data block to be calculated.
   * - [in]
     - Crc_Length
     - Length of data block to be calculated in bytes.
   * - [in]
     - Crc_StartValue16
     - Start value when the algorithm starts.
   * - [in]
     - Crc_IsFirstCall
     - TRUE: First call in a sequence or individual CRC calculation; start from initial value, ignore Crc_StartValue16. FALSE:Subsequent call in a call sequence; Crc_StartValue16 is interpreted to be the return value of the previous function call.

**Return type**
   uint16


Crc_CalculateCRC16ARC
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    uint16 Crc_CalculateCRC16ARC(const uint8 *Crc_DataPtr, uint32 Crc_Length, uint16 Crc_StartValue16, boolean Crc_IsFirstCall)

This service makes a CRC16 calculation on Crc_Length data bytes, using the polynomial 0x8005.

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
     - Crc_DataPtr
     - Pointer to start address of data block to be calculated.
   * - [in]
     - Crc_Length
     - Length of data block to be calculated in bytes.
   * - [in]
     - Crc_StartValue16
     - Start value when the algorithm starts.
   * - [in]
     - Crc_IsFirstCall
     - TRUE: First call in a sequence or individual CRC calculation; start from initial value, ignore Crc_StartValue16. FALSE:Subsequent call in a call sequence; Crc_StartValue16 is interpreted to be the return value of the previous function call.

**Return type**
   uint16


Crc_CalculateCRC32
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    uint32 Crc_CalculateCRC32(const uint8 *Crc_DataPtr, uint32 Crc_Length, uint32 Crc_StartValue32, boolean Crc_IsFirstCall)

This service makes a CRC32 calculation on Crc_Length data bytes.

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
     - Crc_DataPtr
     - Pointer to start address of data block to be calculated.
   * - [in]
     - Crc_Length
     - Length of data block to be calculated in bytes.
   * - [in]
     - Crc_StartValue32
     - Start value when the algorithm starts.
   * - [in]
     - Crc_IsFirstCall
     - TRUE: First call in a sequence or individual CRC calculation; start from initial value, ignore Crc_StartValue32. FALSE:Subsequent call in a call sequence; Crc_StartValue32 is interpreted to be the return value of the previous function call.

**Return type**
   uint32


Crc_CalculateCRC32P4
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    uint32 Crc_CalculateCRC32P4(const uint8 *Crc_DataPtr, uint32 Crc_Length, uint32 Crc_StartValue32, boolean Crc_IsFirstCall)

This service makes a CRC32 calculation on Crc_Length data bytes.

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
     - Crc_DataPtr
     - Pointer to start address of data block to be calculated.
   * - [in]
     - Crc_Length
     - Length of data block to be calculated in bytes.
   * - [in]
     - Crc_StartValue32
     - Start value when the algorithm starts.
   * - [in]
     - Crc_IsFirstCall
     - TRUE: First call in a sequence or individual CRC calculation; start from initial value, ignore Crc_StartValue32. FALSE:Subsequent call in a call sequence; Crc_StartValue32 is interpreted to be the return value of the previous function call.

**Return type**
   uint32


Crc_CalculateCRC64
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    uint64 Crc_CalculateCRC64(const uint8 *Crc_DataPtr, uint64 Crc_Length, uint64 Crc_StartValue64, boolean Crc_IsFirstCall)

This service makes a CRC64 calculation on Crc_Length data bytes.

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
     - Crc_DataPtr
     - Pointer to start address of data block to be calculated.
   * - [in]
     - Crc_Length
     - Length of data block to be calculated in bytes.
   * - [in]
     - Crc_StartValue64
     - Start value when the algorithm starts.
   * - [in]
     - Crc_IsFirstCall
     - TRUE: First call in a sequence or individual CRC calculation; start from initial value, ignore Crc_StartValue64. FALSE:Subsequent call in a call sequence; Crc_StartValue64 is interpreted to be the return value of the previous function call.

**Return type**
   uint64


