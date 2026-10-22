
类型定义
--------
.. 如果没有就不存在该章节，或为None

.. list-table:: 
   :widths: 15 5 20
   :header-rows: 1

   * - Type Name
     - Type
     - Description

   * - StbM_ClockGptConfigType
     - struct
     - 

   * - StbM_ClockOsConfigType
     - struct
     - 


      
提供的服务
-----------
StbM_ClockPreInit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void StbM_ClockPreInit(void)



**Sync/Async**
   

**Reentrancy**
   


**Return type**
   void


StbM_ClockGptInit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void StbM_ClockGptInit(uint8 channelIdx)



**Sync/Async**
   

**Reentrancy**
   

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - 
     - channelIdx
     - 

**Return type**
   void


StbM_ClockGptGetCurrentTime
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void StbM_ClockGptGetCurrentTime(uint8 channelIdx, uint64 *timePtr)



**Sync/Async**
   

**Reentrancy**
   

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - 
     - channelIdx
     - 
   * - 
     - timePtr
     - 

**Return type**
   void


StbM_ClockOsGetCurrentTime
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void StbM_ClockOsGetCurrentTime(uint8 counterIdx, uint64 *timePtr)



**Sync/Async**
   

**Reentrancy**
   

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - 
     - counterIdx
     - 
   * - 
     - timePtr
     - 

**Return type**
   void


