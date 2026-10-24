
类型定义 Type Definitions
----------------------------------------
.. 如果没有就不存在该章节，或为None

.. list-table:: 
   :widths: 15 5 20
   :header-rows: 1

   * - Type Name
     - Type
     - Description

   * - Sd_ServerServiceSetStateType
     - enum Sd_ServerServiceSetStateTypeTag
     - This type defines the Server states that are reported to the SD using the expected API Sd_ServerServiceSetState.

   * - Sd_ClientServiceSetStateType
     - enum Sd_ClientServiceSetStateTypeTag
     - This type defines the Client states that are reported to the BswM using the expected API Sd_ClientServiceSetState.

   * - Sd_ConsumedEventGroupSetStateType
     - enum Sd_ConsumedEventGroupSetStateTypeTag
     - This type defines the subscription policy by consumed EventGroup for the Client Service.

   * - Sd_ClientServiceCurrentStateType
     - enum Sd_ClientServiceCurrentStateTypeTag
     - This type defines the modes to indicate the current mode request of a Client Service.

   * - Sd_ConsumedEventGroupCurrentStateType
     - enum Sd_ConsumedEventGroupCurrentStateTypeTag
     - This type defines the subscription policy by consumed EventGroup for the Client Service.

   * - Sd_EventHandlerCurrentStateType
     - enum Sd_EventHandlerCurrentStateTypeTag
     - This type defines the subscription policy by EventHandler for the Server Service.

   * - Sd_VersionDrivenFindBehavior
     - enum Sd_VersionDrivenFindBehaviorTag
     - This type defines the version-driven find behavior for the Service Discovery.

   * - Sd_ServiceGroupIdType
     - uint16
     - Service Group ID.

   * - Sd_ConfigOptionStringType
     - uint8 *
     - Type for a zero-terminated string of configuration options.

   * - Sd_HandlerIdMapType
     - uint16
     - Type for a handler ID map.

   * - SdCapabilityRecordMatchCalloutType
     - boolean*
     - SdCapabilityRecordMatchCallout type.

   * - Sd_ClientTimerType
     - struct Sd_ClientTimerTypeTag
     - This container specifies all timers used by the Service Discovery module for Client Services.

   * - Sd_CapabilityRecordType
     - struct Sd_CapabilityRecordTypeTag
     - Sd uses capability records to store arbitrary name/value pairs conveying additional information about the named service.

   * - Sd_SoAdSoConGroupType
     - struct Sd_SoAdSoConGroupTypeTag
     - Reference SoAdSocketConnectionGroup.

   * - Sd_SoAdRoutingGroupType
     - struct Sd_SoAdRoutingGroupTypeTag
     - Structure for soad routing group.

   * - Sd_ConsumedEventGroupType
     - struct Sd_ConsumedEventGroupTypeTag
     - This container specifies all parameters for consumed event groups.

   * - Sd_ConsumedMethodsType
     - struct Sd_ConsumedMethodsTypeTag
     - Container element for representing the data path for accessing the server methods.

   * - SdBlocklistedMinorVersionsType
     - uint32
     - Type to define the blocklisted minor versions.

   * - Sd_BlocklistedVersionType
     - struct Sd_SdBlocklistedVersionTag
     - Structure for SD blocklisted versions.

   * - Sd_ClientServiceType
     - struct Sd_ClientServiceTypeTag
     - This container specifies all parameters used by Client services.

   * - Sd_DemEventParameterType
     - struct Sd_DemEventParameterTypeTag
     - Dem Event Parameter.

   * - Sd_InstanceDemEventParameterRefsType
     - struct Sd_InstanceDemEventParameterRefsTypeTag
     - Container for the references to DemEventParameter elements which shall be invoked using the API Dem_ReportErrorStatus API in case the corresponding error occurs.

   * - Sd_InstanceMulticastRxPduType
     - struct Sd_InstanceMulticastRxPduTypeTag
     - This container specifies the received PDU.

   * - Sd_InstanceTxPduType
     - struct Sd_InstanceTxPduTypeTag
     - This container specifies the transmitted PDU.

   * - Sd_InstanceUnicastRxPduType
     - struct Sd_InstanceUnicastRxPduTypeTag
     - This container specifies the received PDU.

   * - Sd_ServerTimerType
     - struct Sd_ServerTimerTypeTag
     - This container specifies all timers used by the Service Discovery module for Server Services.

   * - Sd_SoAdSoConType
     - struct Sd_SoAdSoConTypeTag
     - Configuration of soad socket connection.

   * - Sd_ServiceGroupType
     - struct Sd_ServiceGroupTypeTag
     - This container specifies all parameters used by Service Groups.

   * - Sd_EventHandlerMulticastType
     - struct Sd_EventHandlerMulticastTypeTag
     - The subcontainer including the Routing Group for Activation of Events sent over Multicast.

   * - Sd_EventHandlerTcpType
     - struct Sd_EventHandlerTcpTypeTag
     - The subcontainer including the Routing Groups for Activation and Trigger Transmit for Events sent over TCP.

   * - Sd_EventHandlerUdpType
     - struct Sd_EventHandlerUdpTypeTag
     - The subcontainer including the Routing Groups for Activation and Trigger Transmit for Events sent over UDP.

   * - Sd_EventHandlerType
     - struct Sd_EventHandlerTypeTag
     - Container Element for representing an EventGroup as part of the Service Instance.

   * - Sd_ProvidedMethodsType
     - struct Sd_ProvidedMethodsTypeTag
     - Container element for representing the needed elements of the data path for the methods provided by the service.

   * - Sd_ServerServiceType
     - struct Sd_ServerServiceTypeTag
     - This container specifies all parameters used by Server services.

   * - Sd_InstanceType
     - struct Sd_InstanceTypeTag
     - This container represents an instance of the SD.

   * - Sd_RxPduIdSoConIdMapType
     - struct Sd_RxPduIdSoConIdMapTypeTag
     - Mapping between RxPduId and SoConId.

   * - Sd_ConfigType
     - struct Sd_ConfigTypeTag
     - This container contains the configuration parameters and sub containers of the AUTOSAR Service Discovery module.

   * - Sd_ServerServiceSetStateTypeTag
     - enum
     - This type defines the Server states that are reported to the SD using the expected API Sd_ServerServiceSetState.

   * - Sd_ClientServiceSetStateTypeTag
     - enum
     - This type defines the Client states that are reported to the BswM using the expected API Sd_ClientServiceSetState.

   * - Sd_ConsumedEventGroupSetStateTypeTag
     - enum
     - This type defines the subscription policy by consumed EventGroup for the Client Service.

   * - Sd_ClientServiceCurrentStateTypeTag
     - enum
     - This type defines the modes to indicate the current mode request of a Client Service.

   * - Sd_ConsumedEventGroupCurrentStateTypeTag
     - enum
     - This type defines the subscription policy by consumed EventGroup for the Client Service.

   * - Sd_EventHandlerCurrentStateTypeTag
     - enum
     - This type defines the subscription policy by EventHandler for the Server Service.

   * - Sd_VersionDrivenFindBehaviorTag
     - enum
     - This type defines the version-driven find behavior for the Service Discovery.
