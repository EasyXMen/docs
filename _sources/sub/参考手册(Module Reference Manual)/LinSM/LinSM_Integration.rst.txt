集成 Integration
========================================

文件列表 File List
--------------------------------------------------------------------

静态文件 Static Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - 文件(File)
     - 描述(Description)
   
   * - LinSM.c
     - 模块源文件(Module source file)

   * - LinSM.h
     - 模块头文件(Module header file)

   * - LinSM_Internal.h
     - 模块内部头文件(Module internal header file)

动态文件 Dynamic Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - 文件(File)
     - 描述(Description)
   
   * - LinSM_Cfg.c
     - 配置源文件(Configuration source file)

   * - LinSM_Cfg.h
     - 配置头文件(Configuration header file)


错误处理 Error Handling
------------------------------------------------------------------------

开发错误 Development Errors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. list-table:: 
   :widths: 20 10 30
   :header-rows: 1

   * - Error code
     - Value[hex]
     - Description

   * - LINSM_E_UNINIT
     - 0x00
     - Referenced network does not exist (identification is out of range)

   * - LINSM_E_NONEXISTENT_NETWORK
     - 0x20
     - API called without initialization of LinSM

   * - LINSM_E_PARAMETER
     - 0x30
     - Referenced network does not exist (identification is out of range)

   * - LINSM_E_PARAM_POINTER
     - 0x40
     - API service called with invalid pointer

   * - LINSM_E_INIT_FAILED
     - 0x50
     - Init function failed

   * - LINSM_E_PARTITION
     - 0x60
     - API service called in wrong partition

   * - LINSM_E_PARTITION_UNINIT
     - 0x70
     - API called without initialization of channel partition

运行时错误 Runtime Errors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. list-table:: 
   :widths: 20 10 30
   :header-rows: 1

   * - Error code
     - Value[hex]
     - API called without initialization of LinSM

   * - LINSM_E_CONFIRMATION_TIMEOUT
     - 0x00
     - Timeout of the callbacks from LinIf
