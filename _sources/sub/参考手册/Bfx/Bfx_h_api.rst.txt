
接口描述(Interface Description)
===============================


类型定义(Type Definitions)
---------------------------
.. 如果没有就不存在该章节，或为None

None

      
提供的服务(Services)
-------------------------------

Bfx_SetBit_u8u8
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Bfx_SetBit_u8u8(uint8 *data, uint8 bitPn)

set logical status of input data as '1' at the requested bit position.

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
   * - [inout]
     - data
     - Pointer to input data
   * - [in]
     - bitPn
     - Bit position

**Return type**
   void


Bfx_ClrBit_u8u8
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Bfx_ClrBit_u8u8(uint8 *data, uint8 bitPn)

clear the logical status of the input data to '0' at the requested bit position.

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
   * - [inout]
     - data
     - Pointer to input data
   * - [in]
     - bitPn
     - Bit position

**Return type**
   void


Bfx_GetBit_u8u8_u8
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    boolean Bfx_GetBit_u8u8_u8(uint8 data, uint8 bitPn)

return the logical status of the input data for the requested bit position.

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
     - data
     - input data
   * - [in]
     - bitPn
     - Bit position

**Return type**
   boolean


Bfx_SetBits_u8u8u8u8
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Bfx_SetBits_u8u8u8u8(uint8 *data, uint8 bitStartPn, uint8 bitLn, uint8 status)

set the input data as '1' or '0' as per 'Status' value starting from 'BitStartPn' for the length 'BitLn'.

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
   * - [inout]
     - data
     - Pointer to input data
   * - [in]
     - bitStartPn
     - Start bit position
   * - [in]
     - bitLn
     - Bit field length
   * - [in]
     - status
     - Status value

**Return type**
   void


Bfx_GetBits_u8u8u8_u8
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    uint8 Bfx_GetBits_u8u8u8_u8(uint8 data, uint8 bitStartPn, uint8 bitLn)

return the Bits of the input data starting from 'BitStartPn' for the length of 'BitLn'.

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
     - data
     - input data
   * - [in]
     - bitStartPn
     - Start bit position
   * - [in]
     - bitLn
     - Bit field length

**Return type**
   uint8


Bfx_SetBitMask_u8u8
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Bfx_SetBitMask_u8u8(uint8 *data, uint8 mask)

set the data to logical status '1' as per the corresponding Mask bits when set to value 1 and remaining bits will retain their original values.

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
   * - [inout]
     - data
     - Pointer to input data
   * - [in]
     - mask
     - Mask used to set bits

**Return type**
   void


Bfx_ClrBitMask_u8u8
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Bfx_ClrBitMask_u8u8(uint8 *data, uint8 mask)

clear the logical status to '0' for the input data for all the bit positions as per the mask.

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
   * - [inout]
     - data
     - Pointer to input data
   * - [in]
     - mask
     - mask value

**Return type**
   void


Bfx_TstBitMask_u8u8_u8
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    boolean Bfx_TstBitMask_u8u8_u8(uint8 data, uint8 mask)

return TRUE, if all bits defined in Mask value are set in the input Data value. In all other cases this function shall return FALSE.

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
     - data
     - input data
   * - [in]
     - mask
     - mask value

**Return type**
   boolean


Bfx_TstBitLnMask_u8u8_u8
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    boolean Bfx_TstBitLnMask_u8u8_u8(uint8 data, uint8 mask)

makes a test on the input data and if at least one bit is set as per the mask, then the function shall return TRUE, otherwise it shall return FALSE.

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
     - data
     - data
   * - [in]
     - mask
     - value

**Return type**
   boolean


Bfx_TstParityEven_u8_u8
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    boolean Bfx_TstParityEven_u8_u8(uint8 data)

tests the number of bits set to 1. If this number is even, it shall return TRUE, otherwise it returns FALSE.

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
     - data
     - input data

**Return type**
   boolean


Bfx_ToggleBits_u8
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Bfx_ToggleBits_u8(uint8 *data)

toggles all the bits of data (1's Complement Data).

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
   * - [inout]
     - data
     - Pointer to input data

**Return type**
   void


Bfx_ToggleBitMask_u8u8
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Bfx_ToggleBitMask_u8u8(uint8 *data, uint8 mask)

toggles the bits of data when the corresponding bit of the mask is enabled and set to 1.

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
   * - [inout]
     - data
     - Pointer to input data
   * - [in]
     - mask
     - mask value

**Return type**
   void


Bfx_ShiftBitRt_u8u8
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Bfx_ShiftBitRt_u8u8(uint8 *data, uint8 shiftCnt)

shift data to the right by ShiftCnt. The most significant bit (left-most bit) is replaced by a '0' bit and the least significant bit (right-most bit) is discarded for every single bit shift cycle.

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
   * - [inout]
     - data
     - Pointer to input data
   * - [in]
     - shiftCnt
     - Shift right count

**Return type**
   void


Bfx_ShiftBitLt_u8u8
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Bfx_ShiftBitLt_u8u8(uint8 *data, uint8 shiftCnt)

shift data to the left by ShiftCnt. The least significant bit (right-most bit) is replaced by a '0' bit and the most significant bit (left-most bit) is discarded for every single bit shift cycle.

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
   * - [inout]
     - data
     - Pointer to input data
   * - [in]
     - shiftCnt
     - Shift right count

**Return type**
   void


Bfx_RotBitRt_u8u8
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Bfx_RotBitRt_u8u8(uint8 *data, uint8 shiftCnt)

rotate data to the right by ShiftCnt. The least significant bit is rotated to the most significant bit location for every single bit shift cycle.

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
   * - [inout]
     - data
     - Pointer to input data
   * - [in]
     - shiftCnt
     - Shift count

**Return type**
   void


Bfx_RotBitLt_u8u8
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Bfx_RotBitLt_u8u8(uint8 *data, uint8 shiftCnt)

rotate data to the left by ShiftCnt. The most significant bit is rotated to the least significant bit location for every single bit shift cycle.

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
   * - [inout]
     - data
     - Pointer to input data
   * - [in]
     - shiftCnt
     - Shift count

**Return type**
   void


Bfx_CopyBit_u8u8u8u8
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Bfx_CopyBit_u8u8u8u8(uint8 *destData, uint8 destPn, uint8 srcData, uint8 srcPn)

copy a bit from source data from bit position to destination data at bit position.

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
   * - [inout]
     - destData
     - Pointer to destination data
   * - [in]
     - destPn
     - Destination position
   * - [in]
     - srcData
     - Source data
   * - [in]
     - srcPn
     - Source position

**Return type**
   void


Bfx_PutBits_u8u8u8u8
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Bfx_PutBits_u8u8u8u8(uint8 *data, uint8 bitStartPn, uint8 bitLn, uint8 pattern)

put bits as mentioned in Pattern to the input Data from the specified bit position.

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
   * - [inout]
     - data
     - Pointer to input data
   * - [in]
     - bitStartPn
     - Start bit position
   * - [in]
     - bitLn
     - Bit field length
   * - [in]
     - pattern
     - Pattern to be set

**Return type**
   void


Bfx_PutBitsMask_u8u8u8
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Bfx_PutBitsMask_u8u8u8(uint8 *data, uint8 pattern, uint8 mask)

put all bits defined in Pattern and for which the corresponding Mask bit is set to 1 in the input Data.

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
   * - [inout]
     - data
     - Pointer to input data
   * - [in]
     - pattern
     - Pattern to be set
   * - [in]
     - mask
     - mask value

**Return type**
   void


Bfx_PutBit_u8u8u8
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Bfx_PutBit_u8u8u8(uint8 *data, uint8 bitPn, boolean status)

update the bit specified by BitPn of input data as '1' or '0' as per 'Status' value.

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
   * - [inout]
     - data
     - Pointer to input data
   * - [in]
     - bitPn
     - Bit position
   * - [in]
     - status
     - status value

**Return type**
   void


Bfx_ShiftBitSat_s8s8_s8
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    sint8 Bfx_ShiftBitSat_s8s8_s8(sint8 ShiftCnt, uint8 *data)

Arithmetic shift with saturation.

**Sync/Async**
   FALSE

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
     - ShiftCnt
     - Shift count
   * - [inout]
     - data
     - input data

**Return type**
   sint8


Bfx_ShiftBitSat_u8s8_u8
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    uint8 Bfx_ShiftBitSat_u8s8_u8(sint8 ShiftCnt, uint8 *data)

Arithmetic shift with saturation.

**Sync/Async**
   FALSE

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
     - ShiftCnt
     - Shift count
   * - [inout]
     - data
     - Pointer to input data

**Return type**
   uint8


Bfx_CountLeadingSigns_s8
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    uint8 Bfx_CountLeadingSigns_s8(sint8 data)

Count the number of consecutive bits which have the same value as most significant bit in Data,starting with bit at position msb minus one. Put the result in Data. It is the number of leading sign bits minus one, giving the number of redundant sign bits in Data.

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
     - data
     - input data

**Return type**
   uint8


Bfx_CountLeadingOnes_u8
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    uint8 Bfx_CountLeadingOnes_u8(uint8 data)

Count the number of consecutive ones in Data starting with the most significant bit and return the result.

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
     - data
     - input data

**Return type**
   uint8


Bfx_CountLeadingZeros_u8
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    uint8 Bfx_CountLeadingZeros_u8(uint8 data)

Count the number of consecutive zeros in Data starting with the most significant bit and return the result.

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
     - data
     - input data

**Return type**
   uint8


Bfx_SetBit_u16u8
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Bfx_SetBit_u16u8(uint16 *data, uint8 bitPn)

set logical status of input data as '1' at the requested bit position.

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
   * - [inout]
     - data
     - Pointer to input data
   * - [in]
     - bitPn
     - Bit position

**Return type**
   void


Bfx_ClrBit_u16u8
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Bfx_ClrBit_u16u8(uint16 *data, uint8 bitPn)

clear the logical status of the input data to '0' at the requested bit position.

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
   * - [inout]
     - data
     - Pointer to input data
   * - [in]
     - bitPn
     - Bit position

**Return type**
   void


Bfx_GetBit_u16u8_u8
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    boolean Bfx_GetBit_u16u8_u8(uint16 data, uint8 bitPn)

return the logical status of the input data for the requested bit position.

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
     - data
     - input data
   * - [in]
     - bitPn
     - Bit position

**Return type**
   boolean


Bfx_SetBits_u16u8u8u8
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Bfx_SetBits_u16u8u8u8(uint16 *data, uint8 bitStartPn, uint8 bitLn, uint8 status)

set the input data as '1' or '0' as per 'Status' value starting from 'BitStartPn' for the length 'BitLn'.

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
   * - [inout]
     - data
     - Pointer to input data
   * - [in]
     - bitStartPn
     - Start bit position
   * - [in]
     - bitLn
     - Bit field length
   * - [in]
     - status
     - Status value

**Return type**
   void


Bfx_GetBits_u16u8u8_u16
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    uint16 Bfx_GetBits_u16u8u8_u16(uint16 data, uint8 bitStartPn, uint8 bitLn)

return the Bits of the input data starting from 'BitStartPn' for the length of 'BitLn'.

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
     - data
     - input data
   * - [in]
     - bitStartPn
     - Start bit position
   * - [in]
     - bitLn
     - Bit field length

**Return type**
   uint16


Bfx_SetBitMask_u16u16
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Bfx_SetBitMask_u16u16(uint16 *data, uint16 mask)

set the data to logical status '1' as per the corresponding Mask bits when set to value 1 and remaining bits will retain their original values.

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
   * - [inout]
     - data
     - Pointer to input data
   * - [in]
     - mask
     - Mask used to set bits

**Return type**
   void


Bfx_ClrBitMask_u16u16
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Bfx_ClrBitMask_u16u16(uint16 *data, uint16 mask)

clear the logical status to '0' for the input data for all the bit positions as per the mask.

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
   * - [inout]
     - data
     - Pointer to input data
   * - [in]
     - mask
     - mask value

**Return type**
   void


Bfx_TstBitMask_u16u16_u8
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    boolean Bfx_TstBitMask_u16u16_u8(uint16 data, uint16 mask)

return TRUE, if all bits defined in Mask value are set in the input Data value. In all other cases this function shall return FALSE.

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
     - data
     - input data
   * - [in]
     - mask
     - mask value

**Return type**
   boolean


Bfx_TstBitLnMask_u16u16_u8
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    boolean Bfx_TstBitLnMask_u16u16_u8(uint16 data, uint16 mask)

makes a test on the input data and if at least one bit is set as per the mask, then the function shall return TRUE, otherwise it shall return FALSE.

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
     - data
     - data
   * - [in]
     - mask
     - value

**Return type**
   boolean


Bfx_TstParityEven_u16_u8
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    boolean Bfx_TstParityEven_u16_u8(uint16 data)

tests the number of bits set to 1. If this number is even, it shall return TRUE, otherwise it returns FALSE.

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
     - data
     - input data

**Return type**
   boolean


Bfx_ToggleBits_u16
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Bfx_ToggleBits_u16(uint16 *data)

toggles all the bits of data (1's Complement Data).

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
   * - [inout]
     - data
     - Pointer to input data

**Return type**
   void


Bfx_ToggleBitMask_u16u16
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Bfx_ToggleBitMask_u16u16(uint16 *data, uint16 mask)

toggles the bits of data when the corresponding bit of the mask is enabled and set to 1.

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
   * - [inout]
     - data
     - Pointer to input data
   * - [in]
     - mask
     - mask value

**Return type**
   void


Bfx_ShiftBitRt_u16u8
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Bfx_ShiftBitRt_u16u8(uint16 *data, uint8 shiftCnt)

shift data to the right by ShiftCnt. The most significant bit (left-most bit) is replaced by a '0' bit and the least significant bit (right-most bit) is discarded for every single bit shift cycle.

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
   * - [inout]
     - data
     - Pointer to input data
   * - [in]
     - shiftCnt
     - Shift right count

**Return type**
   void


Bfx_ShiftBitLt_u16u8
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Bfx_ShiftBitLt_u16u8(uint16 *data, uint8 shiftCnt)

shift data to the left by ShiftCnt. The least significant bit (right-most bit) is replaced by a '0' bit and the most significant bit (left-most bit) is discarded for every single bit shift cycle.

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
   * - [inout]
     - data
     - Pointer to input data
   * - [in]
     - shiftCnt
     - Shift right count

**Return type**
   void


Bfx_RotBitRt_u16u8
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Bfx_RotBitRt_u16u8(uint16 *data, uint8 shiftCnt)

rotate data to the right by ShiftCnt. The least significant bit is rotated to the most significant bit location for every single bit shift cycle.

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
   * - [inout]
     - data
     - Pointer to input data
   * - [in]
     - shiftCnt
     - Shift count

**Return type**
   void


Bfx_RotBitLt_u16u8
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Bfx_RotBitLt_u16u8(uint16 *data, uint8 shiftCnt)

rotate data to the left by ShiftCnt. The most significant bit is rotated to the least significant bit location for every single bit shift cycle.

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
   * - [inout]
     - data
     - Pointer to input data
   * - [in]
     - shiftCnt
     - Shift count

**Return type**
   void


Bfx_CopyBit_u16u8u16u8
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Bfx_CopyBit_u16u8u16u8(uint16 *destData, uint8 destPn, uint16 srcData, uint8 srcPn)

copy a bit from source data from bit position to destination data at bit position.

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
   * - [inout]
     - destData
     - Pointer to destination data
   * - [in]
     - destPn
     - Destination position
   * - [in]
     - srcData
     - Source data
   * - [in]
     - srcPn
     - Source position

**Return type**
   void


Bfx_PutBits_u16u8u8u16
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Bfx_PutBits_u16u8u8u16(uint16 *data, uint8 bitStartPn, uint8 bitLn, uint16 pattern)

put bits as mentioned in Pattern to the input Data from the specified bit position.

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
   * - [inout]
     - data
     - Pointer to input data
   * - [in]
     - bitStartPn
     - Start bit position
   * - [in]
     - bitLn
     - Bit field length
   * - [in]
     - pattern
     - Pattern to be set

**Return type**
   void


Bfx_PutBitsMask_u16u16u16
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Bfx_PutBitsMask_u16u16u16(uint16 *data, uint16 pattern, uint16 mask)

put all bits defined in Pattern and for which the corresponding Mask bit is set to 1 in the input Data.

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
   * - [inout]
     - data
     - Pointer to input data
   * - [in]
     - pattern
     - Pattern to be set
   * - [in]
     - mask
     - mask value

**Return type**
   void


Bfx_PutBit_u16u8u8
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Bfx_PutBit_u16u8u8(uint16 *data, uint8 bitPn, boolean status)

update the bit specified by BitPn of input data as '1' or '0' as per 'Status' value.

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
   * - [inout]
     - data
     - Pointer to input data
   * - [in]
     - bitPn
     - Bit position
   * - [in]
     - status
     - status value

**Return type**
   void


Bfx_ShiftBitSat_s16s8_s16
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    sint16 Bfx_ShiftBitSat_s16s8_s16(sint8 ShiftCnt, uint16 *data)

Arithmetic shift with saturation.

**Sync/Async**
   FALSE

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
     - ShiftCnt
     - Shift count
   * - [inout]
     - data
     - input data

**Return type**
   sint16


Bfx_ShiftBitSat_u16s8_u16
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    uint16 Bfx_ShiftBitSat_u16s8_u16(sint8 ShiftCnt, uint16 *data)

Arithmetic shift with saturation.

**Sync/Async**
   FALSE

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
     - ShiftCnt
     - Shift count
   * - [inout]
     - data
     - Pointer to input data

**Return type**
   uint16


Bfx_CountLeadingSigns_s16
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    uint8 Bfx_CountLeadingSigns_s16(sint16 data)

Count the number of consecutive bits which have the same value as most significant bit in Data,starting with bit at position msb minus one. Put the result in Data. It is the number of leading sign bits minus one, giving the number of redundant sign bits in Data.

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
     - data
     - input data

**Return type**
   uint8


Bfx_CountLeadingOnes_u16
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    uint8 Bfx_CountLeadingOnes_u16(uint16 data)

Count the number of consecutive ones in Data starting with the most significant bit and return the result.

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
     - data
     - input data

**Return type**
   uint8


Bfx_CountLeadingZeros_u16
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    uint8 Bfx_CountLeadingZeros_u16(uint16 data)

Count the number of consecutive zeros in Data starting with the most significant bit and return the result.

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
     - data
     - input data

**Return type**
   uint8


Bfx_SetBit_u32u8
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Bfx_SetBit_u32u8(uint32 *data, uint8 bitPn)

set logical status of input data as '1' at the requested bit position.

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
   * - [inout]
     - data
     - Pointer to input data
   * - [in]
     - bitPn
     - Bit position

**Return type**
   void


Bfx_ClrBit_u32u8
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Bfx_ClrBit_u32u8(uint32 *data, uint8 bitPn)

clear the logical status of the input data to '0' at the requested bit position.

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
   * - [inout]
     - data
     - Pointer to input data
   * - [in]
     - bitPn
     - Bit position

**Return type**
   void


Bfx_GetBit_u32u8_u8
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    boolean Bfx_GetBit_u32u8_u8(uint32 data, uint8 bitPn)

return the logical status of the input data for the requested bit position.

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
     - data
     - input data
   * - [in]
     - bitPn
     - Bit position

**Return type**
   boolean


Bfx_SetBits_u32u8u8u8
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Bfx_SetBits_u32u8u8u8(uint32 *data, uint8 bitStartPn, uint8 bitLn, uint8 status)

set the input data as '1' or '0' as per 'Status' value starting from 'BitStartPn' for the length 'BitLn'.

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
   * - [inout]
     - data
     - Pointer to input data
   * - [in]
     - bitStartPn
     - Start bit position
   * - [in]
     - bitLn
     - Bit field length
   * - [in]
     - status
     - Status value

**Return type**
   void


Bfx_GetBits_u32u8u8_u32
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    uint32 Bfx_GetBits_u32u8u8_u32(uint32 data, uint8 bitStartPn, uint8 bitLn)

return the Bits of the input data starting from 'BitStartPn' for the length of 'BitLn'.

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
     - data
     - input data
   * - [in]
     - bitStartPn
     - Start bit position
   * - [in]
     - bitLn
     - Bit field length

**Return type**
   uint32


Bfx_SetBitMask_u32u32
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Bfx_SetBitMask_u32u32(uint32 *data, uint32 mask)

set the data to logical status '1' as per the corresponding Mask bits when set to value 1 and remaining bits will retain their original values.

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
   * - [inout]
     - data
     - Pointer to input data
   * - [in]
     - mask
     - Mask used to set bits

**Return type**
   void


Bfx_ClrBitMask_u32u32
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Bfx_ClrBitMask_u32u32(uint32 *data, uint32 mask)

clear the logical status to '0' for the input data for all the bit positions as per the mask.

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
   * - [inout]
     - data
     - Pointer to input data
   * - [in]
     - mask
     - mask value

**Return type**
   void


Bfx_TstBitMask_u32u32_u8
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    boolean Bfx_TstBitMask_u32u32_u8(uint32 data, uint32 mask)

return TRUE, if all bits defined in Mask value are set in the input Data value. In all other cases this function shall return FALSE.

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
     - data
     - input data
   * - [in]
     - mask
     - mask value

**Return type**
   boolean


Bfx_TstBitLnMask_u32u32_u8
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    boolean Bfx_TstBitLnMask_u32u32_u8(uint32 data, uint32 mask)

makes a test on the input data and if at least one bit is set as per the mask, then the function shall return TRUE, otherwise it shall return FALSE.

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
     - data
     - data
   * - [in]
     - mask
     - value

**Return type**
   boolean


Bfx_TstParityEven_u32_u8
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    boolean Bfx_TstParityEven_u32_u8(uint32 data)

tests the number of bits set to 1. If this number is even, it shall return TRUE, otherwise it returns FALSE.

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
     - data
     - input data

**Return type**
   boolean


Bfx_ToggleBits_u32
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Bfx_ToggleBits_u32(uint32 *data)

toggles all the bits of data (1's Complement Data).

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
   * - [inout]
     - data
     - Pointer to input data

**Return type**
   void


Bfx_ToggleBitMask_u32u32
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Bfx_ToggleBitMask_u32u32(uint32 *data, uint32 mask)

toggles the bits of data when the corresponding bit of the mask is enabled and set to 1.

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
   * - [inout]
     - data
     - Pointer to input data
   * - [in]
     - mask
     - mask value

**Return type**
   void


Bfx_ShiftBitRt_u32u8
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Bfx_ShiftBitRt_u32u8(uint32 *data, uint8 shiftCnt)

shift data to the right by ShiftCnt. The most significant bit (left-most bit) is replaced by a '0' bit and the least significant bit (right-most bit) is discarded for every single bit shift cycle.

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
   * - [inout]
     - data
     - Pointer to input data
   * - [in]
     - shiftCnt
     - Shift right count

**Return type**
   void


Bfx_ShiftBitLt_u32u8
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Bfx_ShiftBitLt_u32u8(uint32 *data, uint8 shiftCnt)

shift data to the left by ShiftCnt. The least significant bit (right-most bit) is replaced by a '0' bit and the most significant bit (left-most bit) is discarded for every single bit shift cycle.

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
   * - [inout]
     - data
     - Pointer to input data
   * - [in]
     - shiftCnt
     - Shift right count

**Return type**
   void


Bfx_RotBitRt_u32u8
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Bfx_RotBitRt_u32u8(uint32 *data, uint8 shiftCnt)

rotate data to the right by ShiftCnt. The least significant bit is rotated to the most significant bit location for every single bit shift cycle.

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
   * - [inout]
     - data
     - Pointer to input data
   * - [in]
     - shiftCnt
     - Shift count

**Return type**
   void


Bfx_RotBitLt_u32u8
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Bfx_RotBitLt_u32u8(uint32 *data, uint8 shiftCnt)

rotate data to the left by ShiftCnt. The most significant bit is rotated to the least significant bit location for every single bit shift cycle.

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
   * - [inout]
     - data
     - Pointer to input data
   * - [in]
     - shiftCnt
     - Shift count

**Return type**
   void


Bfx_CopyBit_u32u8u32u8
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Bfx_CopyBit_u32u8u32u8(uint32 *destData, uint8 destPn, uint32 srcData, uint8 srcPn)

copy a bit from source data from bit position to destination data at bit position.

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
   * - [inout]
     - destData
     - Pointer to destination data
   * - [in]
     - destPn
     - Destination position
   * - [in]
     - srcData
     - Source data
   * - [in]
     - srcPn
     - Source position

**Return type**
   void


Bfx_PutBits_u32u8u8u32
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Bfx_PutBits_u32u8u8u32(uint32 *data, uint8 bitStartPn, uint8 bitLn, uint32 pattern)

put bits as mentioned in Pattern to the input Data from the specified bit position.

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
   * - [inout]
     - data
     - Pointer to input data
   * - [in]
     - bitStartPn
     - Start bit position
   * - [in]
     - bitLn
     - Bit field length
   * - [in]
     - pattern
     - Pattern to be set

**Return type**
   void


Bfx_PutBitsMask_u32u32u32
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Bfx_PutBitsMask_u32u32u32(uint32 *data, uint32 pattern, uint32 mask)

put all bits defined in Pattern and for which the corresponding Mask bit is set to 1 in the input Data.

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
   * - [inout]
     - data
     - Pointer to input data
   * - [in]
     - pattern
     - Pattern to be set
   * - [in]
     - mask
     - mask value

**Return type**
   void


Bfx_PutBit_u32u8u8
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Bfx_PutBit_u32u8u8(uint32 *data, uint8 bitPn, boolean status)

update the bit specified by BitPn of input data as '1' or '0' as per 'Status' value.

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
   * - [inout]
     - data
     - Pointer to input data
   * - [in]
     - bitPn
     - Bit position
   * - [in]
     - status
     - status value

**Return type**
   void


Bfx_ShiftBitSat_s32s8_s32
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    sint32 Bfx_ShiftBitSat_s32s8_s32(sint8 ShiftCnt, uint32 *data)

Arithmetic shift with saturation.

**Sync/Async**
   FALSE

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
     - ShiftCnt
     - Shift count
   * - [inout]
     - data
     - input data

**Return type**
   sint32


Bfx_ShiftBitSat_u32s8_u32
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    uint32 Bfx_ShiftBitSat_u32s8_u32(sint8 ShiftCnt, uint32 *data)

Arithmetic shift with saturation.

**Sync/Async**
   FALSE

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
     - ShiftCnt
     - Shift count
   * - [inout]
     - data
     - Pointer to input data

**Return type**
   uint32


Bfx_CountLeadingSigns_s32
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    uint8 Bfx_CountLeadingSigns_s32(sint32 data)

Count the number of consecutive bits which have the same value as most significant bit in Data,starting with bit at position msb minus one. Put the result in Data. It is the number of leading sign bits minus one, giving the number of redundant sign bits in Data.

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
     - data
     - input data

**Return type**
   uint8


Bfx_CountLeadingOnes_u32
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    uint8 Bfx_CountLeadingOnes_u32(uint32 data)

Count the number of consecutive ones in Data starting with the most significant bit and return the result.

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
     - data
     - input data

**Return type**
   uint8


Bfx_CountLeadingZeros_u32
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    uint8 Bfx_CountLeadingZeros_u32(uint32 data)

Count the number of consecutive zeros in Data starting with the most significant bit and return the result.

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
     - data
     - input data

**Return type**
   uint8


Bfx_SetBit_u64u8
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Bfx_SetBit_u64u8(uint64 *data, uint8 bitPn)

set logical status of input data as '1' at the requested bit position.

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
   * - [inout]
     - data
     - Pointer to input data
   * - [in]
     - bitPn
     - Bit position

**Return type**
   void


Bfx_ClrBit_u64u8
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Bfx_ClrBit_u64u8(uint64 *data, uint8 bitPn)

clear the logical status of the input data to '0' at the requested bit position.

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
   * - [inout]
     - data
     - Pointer to input data
   * - [in]
     - bitPn
     - Bit position

**Return type**
   void


Bfx_GetBit_u64u8_u8
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    boolean Bfx_GetBit_u64u8_u8(uint64 data, uint8 bitPn)

return the logical status of the input data for the requested bit position.

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
     - data
     - input data
   * - [in]
     - bitPn
     - Bit position

**Return type**
   boolean


Bfx_SetBits_u64u8u8u8
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Bfx_SetBits_u64u8u8u8(uint64 *data, uint8 bitStartPn, uint8 bitLn, uint8 status)

set the input data as '1' or '0' as per 'Status' value starting from 'BitStartPn' for the length 'BitLn'.

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
   * - [inout]
     - data
     - Pointer to input data
   * - [in]
     - bitStartPn
     - Start bit position
   * - [in]
     - bitLn
     - Bit field length
   * - [in]
     - status
     - Status value

**Return type**
   void


Bfx_GetBits_u64u8u8_u64
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    uint64 Bfx_GetBits_u64u8u8_u64(uint64 data, uint8 bitStartPn, uint8 bitLn)

return the Bits of the input data starting from 'BitStartPn' for the length of 'BitLn'.

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
     - data
     - input data
   * - [in]
     - bitStartPn
     - Start bit position
   * - [in]
     - bitLn
     - Bit field length

**Return type**
   uint64


Bfx_SetBitMask_u64u64
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Bfx_SetBitMask_u64u64(uint64 *data, uint64 mask)

set the data to logical status '1' as per the corresponding Mask bits when set to value 1 and remaining bits will retain their original values.

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
   * - [inout]
     - data
     - Pointer to input data
   * - [in]
     - mask
     - Mask used to set bits

**Return type**
   void


Bfx_ClrBitMask_u64u64
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Bfx_ClrBitMask_u64u64(uint64 *data, uint64 mask)

clear the logical status to '0' for the input data for all the bit positions as per the mask.

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
   * - [inout]
     - data
     - Pointer to input data
   * - [in]
     - mask
     - mask value

**Return type**
   void


Bfx_TstBitMask_u64u64_u8
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    boolean Bfx_TstBitMask_u64u64_u8(uint64 data, uint64 mask)

return TRUE, if all bits defined in Mask value are set in the input Data value. In all other cases this function shall return FALSE.

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
     - data
     - input data
   * - [in]
     - mask
     - mask value

**Return type**
   boolean


Bfx_TstBitLnMask_u64u64_u8
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    boolean Bfx_TstBitLnMask_u64u64_u8(uint64 data, uint64 mask)

makes a test on the input data and if at least one bit is set as per the mask, then the function shall return TRUE, otherwise it shall return FALSE.

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
     - data
     - data
   * - [in]
     - mask
     - value

**Return type**
   boolean


Bfx_TstParityEven_u64_u8
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    boolean Bfx_TstParityEven_u64_u8(uint64 data)

tests the number of bits set to 1. If this number is even, it shall return TRUE, otherwise it returns FALSE.

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
     - data
     - input data

**Return type**
   boolean


Bfx_ToggleBits_u64
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Bfx_ToggleBits_u64(uint64 *data)

toggles all the bits of data (1's Complement Data).

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
   * - [inout]
     - data
     - Pointer to input data

**Return type**
   void


Bfx_ToggleBitMask_u64u64
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Bfx_ToggleBitMask_u64u64(uint64 *data, uint64 mask)

toggles the bits of data when the corresponding bit of the mask is enabled and set to 1.

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
   * - [inout]
     - data
     - Pointer to input data
   * - [in]
     - mask
     - mask value

**Return type**
   void


Bfx_ShiftBitRt_u64u8
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Bfx_ShiftBitRt_u64u8(uint64 *data, uint8 shiftCnt)

shift data to the right by ShiftCnt. The most significant bit (left-most bit) is replaced by a '0' bit and the least significant bit (right-most bit) is discarded for every single bit shift cycle.

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
   * - [inout]
     - data
     - Pointer to input data
   * - [in]
     - shiftCnt
     - Shift right count

**Return type**
   void


Bfx_ShiftBitLt_u64u8
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Bfx_ShiftBitLt_u64u8(uint64 *data, uint8 shiftCnt)

shift data to the left by ShiftCnt. The least significant bit (right-most bit) is replaced by a '0' bit and the most significant bit (left-most bit) is discarded for every single bit shift cycle.

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
   * - [inout]
     - data
     - Pointer to input data
   * - [in]
     - shiftCnt
     - Shift right count

**Return type**
   void


Bfx_RotBitRt_u64u8
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Bfx_RotBitRt_u64u8(uint64 *data, uint8 shiftCnt)

rotate data to the right by ShiftCnt. The least significant bit is rotated to the most significant bit location for every single bit shift cycle.

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
   * - [inout]
     - data
     - Pointer to input data
   * - [in]
     - shiftCnt
     - Shift count

**Return type**
   void


Bfx_RotBitLt_u64u8
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Bfx_RotBitLt_u64u8(uint64 *data, uint8 shiftCnt)

rotate data to the left by ShiftCnt. The most significant bit is rotated to the least significant bit location for every single bit shift cycle.

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
   * - [inout]
     - data
     - Pointer to input data
   * - [in]
     - shiftCnt
     - Shift count

**Return type**
   void


Bfx_CopyBit_u64u8u64u8
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Bfx_CopyBit_u64u8u64u8(uint64 *destData, uint8 destPn, uint64 srcData, uint8 srcPn)

copy a bit from source data from bit position to destination data at bit position.

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
   * - [inout]
     - destData
     - Pointer to destination data
   * - [in]
     - destPn
     - Destination position
   * - [in]
     - srcData
     - Source data
   * - [in]
     - srcPn
     - Source position

**Return type**
   void


Bfx_PutBits_u64u8u8u64
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Bfx_PutBits_u64u8u8u64(uint64 *data, uint8 bitStartPn, uint8 bitLn, uint64 pattern)

put bits as mentioned in Pattern to the input Data from the specified bit position.

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
   * - [inout]
     - data
     - Pointer to input data
   * - [in]
     - bitStartPn
     - Start bit position
   * - [in]
     - bitLn
     - Bit field length
   * - [in]
     - pattern
     - Pattern to be set

**Return type**
   void


Bfx_PutBitsMask_u64u64u64
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Bfx_PutBitsMask_u64u64u64(uint64 *data, uint64 pattern, uint64 mask)

put all bits defined in Pattern and for which the corresponding Mask bit is set to 1 in the input Data.

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
   * - [inout]
     - data
     - Pointer to input data
   * - [in]
     - pattern
     - Pattern to be set
   * - [in]
     - mask
     - mask value

**Return type**
   void


Bfx_PutBit_u64u8u8
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Bfx_PutBit_u64u8u8(uint64 *data, uint8 bitPn, boolean status)

update the bit specified by BitPn of input data as '1' or '0' as per 'Status' value.

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
   * - [inout]
     - data
     - Pointer to input data
   * - [in]
     - bitPn
     - Bit position
   * - [in]
     - status
     - status value

**Return type**
   void


Bfx_ShiftBitSat_s64s8_s64
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    sint64 Bfx_ShiftBitSat_s64s8_s64(sint8 ShiftCnt, uint64 *data)

Arithmetic shift with saturation.

**Sync/Async**
   FALSE

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
     - ShiftCnt
     - Shift count
   * - [inout]
     - data
     - input data

**Return type**
   sint64


Bfx_ShiftBitSat_u64s8_u64
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    uint64 Bfx_ShiftBitSat_u64s8_u64(sint8 ShiftCnt, uint64 *data)

Arithmetic shift with saturation.

**Sync/Async**
   FALSE

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
     - ShiftCnt
     - Shift count
   * - [inout]
     - data
     - Pointer to input data

**Return type**
   uint64


Bfx_CountLeadingSigns_s64
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    uint8 Bfx_CountLeadingSigns_s64(sint64 data)

Count the number of consecutive bits which have the same value as most significant bit in Data,starting with bit at position msb minus one. Put the result in Data. It is the number of leading sign bits minus one, giving the number of redundant sign bits in Data.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - data
     - input data

**Return type**
   uint8


Bfx_CountLeadingOnes_u64
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    uint8 Bfx_CountLeadingOnes_u64(uint64 data)

Count the number of consecutive ones in Data starting with the most significant bit and return the result.

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
     - data
     - input data

**Return type**
   uint8


Bfx_CountLeadingZeros_u64
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    uint8 Bfx_CountLeadingZeros_u64(uint64 data)

Count the number of consecutive zeros in Data starting with the most significant bit and return the result.

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
     - data
     - input data

**Return type**
   uint8


Bfx_GetVersionInfo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Bfx_GetVersionInfo(Std_VersionInfoType *versionInfo)

Returns the version information of this library.

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
     - version information

**Return type**
   void


