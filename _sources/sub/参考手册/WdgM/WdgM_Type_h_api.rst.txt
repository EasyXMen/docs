
类型定义 Type Definitions
----------------------------------------------------------------------------------------------------------

.. list-table:: 
   :widths: 15 5 20
   :header-rows: 1

   * - Type Name
     - Type
     - Description

   * - WdgM_ConfigType
     - uint16
     - This structure contains all post-build configurable parameters of the Watchdog Manager. A pointer to this structure is passed to the Watchdog Manager initialization function for configuration.
    
   * - WdgM_SupervisedEntityIdType
     - uint16
     - Indicates to the Watchdog Manager that a Checkpoint within a Supervised Entity has been reached.

   * - WdgM_CheckpointIdType
     - uint16
     - This type identifies a Checkpoint in the context of a Supervised Entity for the Watchdog Manager.

   * - WdgM_ModeType
     - uint8
     - This type distinguishes the different modes that were configured for the Watchdog Manager.

   * - WdgM_LocalStatusType
     - uint8
     - This type shall be used for variables that represent the current status of supervision for individual Supervised Entities.

   * - WdgM_GlobalStatusType
     - uint8
     - This type shall be used for variables that represent the global supervision status of the Watchdog Manager module.