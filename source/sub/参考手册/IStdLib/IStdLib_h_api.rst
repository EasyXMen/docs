
接口描述
==========


类型定义（Type Definition）
-----------------------------------

.. 如果没有就不存在该章节，或为None

None

      
提供的服务（Provided Services）
-------------------------------------
IStdLib_MemCpy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void* IStdLib_MemCpy(void *ISTDLIB_RESTRICT dstptr, const void *ISTDLIB_RESTRICT srcptr, uint32 length)

copy from srcptr to dstptr

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
     - dstptr
     - Points to the target array used to store the copied content
   * - [in]
     - srcptr
     - Points to the data source you want to copy
   * - [in]
     - length
     - The number of bytes to be copied

**Return type**
   void *


IStdLib_MemSet
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void* IStdLib_MemSet(void *ISTDLIB_RESTRICT dstptr, int val, uint32 n)

Fill the destination address with val, which is n bytes in length.

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
     - dstptr
     - Points to the target array used to store the copied content
   * - [in]
     - val
     - Fill the value of memory
   * - [in]
     - n
     - The number of bytes to be copied

**Return type**
   void *


IStdLib_MemCmp
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    int IStdLib_MemCmp(const void *ISTDLIB_RESTRICT str1ptr, const void *ISTDLIB_RESTRICT str2ptr, uint32 n)

compare str1ptr and strptr2, which is n bytes in length

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
     - str1ptr
     - Points to the array str1
   * - [in]
     - str2ptr
     - Points to the array str2
   * - [in]
     - n
     - The number of bytes to be compared

**Return type**
   int

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - 0
     - str1ptr is equal to str2ptr
   * - 1
     - other condition.

IStdLib_MemHeapInit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    uint8 IStdLib_MemHeapInit(void *ram, uint32 size)

init heap

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant for different heap. Non reentrant for the same heap.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [inout]
     - ram
     - the whole of memory space
   * - [in]
     - size
     - the size of ram

**Return type**
   uint8

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - ISTDLIB_MEMHEAP_INVALID_PTR
     - the ram is illegal pointer
   * - ISTDLIB_MEMHEAP_INVALID_SIZE
     - unable to manage space larger than 64K or smaller than the size of memheap head
   * - ISTDLIB_MEMHEAP_INVALID_INIT
     - repeated initialization
   * - ISTDLIB_MEMHEAP_INVALID_ALIGN
     - the address of ram is not byte aligned
   * - ISTDLIB_MEMHEAP_OK
     - Function completed successfully

IStdLib_MemHeapMalloc
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void* IStdLib_MemHeapMalloc(void *ram, uint32 size)

malloc block depending on size

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant for different heap. Non reentrant for the same heap.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [inout]
     - ram
     - the whole of memory space
   * - [in]
     - size
     - request size

**Return type**
   void *


IStdLib_MemHeapCalloc
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void* IStdLib_MemHeapCalloc(void *ram, uint32 count, uint32 size)

malloc block depending on size, and fill 0

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant for different heap. Non reentrant for the same heap.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [inout]
     - ram
     - the whole of memory space
   * - [in]
     - count
     - request count
   * - [in]
     - size
     - request size

**Return type**
   void *


IStdLib_MemHeapFree
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    uint8 IStdLib_MemHeapFree(void *ram, const void *ptr)

free block to heap

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant for different heap. Non reentrant for the same heap.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [inout]
     - ram
     - the whole of memory space
   * - [in]
     - ptr
     - memory pointer to be released

**Return type**
   uint8

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - ISTDLIB_MEMHEAP_INVALID_PTR
     - the ram or the pointer is illegal pointer or the pointer is not in valid range
   * - ISTDLIB_MEMHEAP_INVALID_INIT
     - uninitialized
   * - ISTDLIB_MEMHEAP_INVALID_ALIGN
     - the address of ram is not byte aligned
   * - ISTDLIB_MEMHEAP_OK
     - Function completed successfully

IStdLib_MemHeapGetManageSize
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    uint8 IStdLib_MemHeapGetManageSize(const void *ram, uint32 *size)

get the heap size

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
     - ram
     - the whole of memory space
   * - [out]
     - size
     - the manage size

**Return type**
   uint8


IStdLib_MemHeapGetRealMaxSize
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    uint8 IStdLib_MemHeapGetRealMaxSize(const void *ram, uint32 *size)

get the total assignable size

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
     - ram
     - the whole of memory space
   * - [out]
     - size
     - real max size

**Return type**
   uint8


IStdLib_MemHeapGetUsedSize
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    uint8 IStdLib_MemHeapGetUsedSize(const void *ram, uint32 *size)

get the assigned size

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
     - ram
     - the whole of memory space
   * - [out]
     - size
     - used size

**Return type**
   uint8


IStdLib_MemHeapGetCurFreeMaxBlockSize
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    uint8 IStdLib_MemHeapGetCurFreeMaxBlockSize(const void *ram, uint32 *size)

get the max free block size

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
     - ram
     - the whole of memory space
   * - [out]
     - size
     - the max size of block in manage space

**Return type**
   uint8


IStdLib_MemHeapGetMaxMallocSize
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    uint8 IStdLib_MemHeapGetMaxMallocSize(const void *ram, uint32 *size)

get the max assigned size

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
     - ram
     - the whole of memory space
   * - [out]
     - size
     - the max malloc size

**Return type**
   uint8


