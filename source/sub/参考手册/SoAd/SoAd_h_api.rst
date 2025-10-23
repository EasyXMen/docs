
SoAd_Init
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void SoAd_Init(const SoAd_ConfigType *SoAdConfigPtr)

Initializes internal and external interfaces and variables of SoAd module.

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
     - SoAdConfigPtr
     - Pointer to the configuration data of the SoAd module.

**Return type**
   void


SoAd_GetVersionInfo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void SoAd_GetVersionInfo(Std_VersionInfoType *versioninfo)

Returns the version information of SoAd module.

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
   * - [out]
     - versioninfo
     - Pointer to where to store the version information of this module.

**Return type**
   void


SoAd_IfRoutingGroupTransmit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType SoAd_IfRoutingGroupTransmit(SoAd_RoutingGroupIdType id)

Triggers the transmission of all If-TxPDUs identified by the parameter id after requesting the data from the related upper layer.

**Sync/Async**
   FALSE

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
     - id
     - routing group identifier indirectly specifying PDUs to be transmitted (after requesting the newest data from the related upper layer).

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - request was successful.
   * - E_NOT_OK
     - request was not successful.

SoAd_IfSpecificRoutingGroupTransmit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType SoAd_IfSpecificRoutingGroupTransmit(SoAd_RoutingGroupIdType id, SoAd_SoConIdType SoConId)

Triggers the transmission of all If-TxPDUs identified by the parameter id on the socket connection specified by SoConId after requesting the data from the related upper layer.

**Sync/Async**
   FALSE

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
     - id
     - routing group identifier indirectly specifying PDUs to be transmitted (after requesting the newest data from the related upper layer).
   * - [in]
     - SoConId
     - socket connection index specifying the socket connection on which the PDUs shall be transmitted.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The request was successful.
   * - E_NOT_OK
     - The request was not successful.

SoAd_GetSoConId
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType SoAd_GetSoConId(PduIdType TxPduId, SoAd_SoConIdType *SoConIdPtr)

Returns socket connection index related to the specified TxPduId.

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
     - TxPduId
     - Transmit PduId specifying the SoAd socket connection for which the socket connection index shall be returned.
   * - [out]
     - SoConIdPtr
     - Pointer to memory receiving the socket connection index asked for.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - request was successful.
   * - E_NOT_OK
     - The request was not successful.

SoAd_OpenSoCon
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType SoAd_OpenSoCon(SoAd_SoConIdType SoConId)

This service opens the socket connection specified by SoConId.

**Sync/Async**
   FALSE

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
     - SoConId
     - socket connection index specifying the socket connection which shall be opened

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The request was successful.
   * - E_NOT_OK
     - The request was not successful.

SoAd_CloseSoCon
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType SoAd_CloseSoCon(SoAd_SoConIdType SoConId, boolean abort)

This service closes the socket connection specified by SoConId.

**Sync/Async**
   FALSE

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
     - SoConId
     - socket connection index specifying the socket connection which shall be closed.
   * - [in]
     - abort
     - TRUE-socket connection will immediately be terminated. FALSE-socket connection will be terminated if no other upper layer is using this socket connection.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The request was successful.
   * - E_NOT_OK
     - The request was not successful.

SoAd_RequestIpAddrAssignment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType SoAd_RequestIpAddrAssignment(SoAd_SoConIdType SoConId, TcpIp_IpAddrAssignmentType Type, const TcpIp_SockAddrType *LocalIpAddrPtr, uint8 Netmask, const TcpIp_SockAddrType *DefaultRouterPtr)

By this API service the local IP address assignment which shall be used for the socket connection specified by SoConId is initiated.

**Sync/Async**
   FALSE

**Reentrancy**
   Reentrant for different SoConIds. Non reentrant for the same SoConId.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - SoConId
     - Socket connection index specifying the socket connection for which the IP address shall be set
   * - [in]
     - Type
     - Type of IP address assignment which shall be initiated.
   * - [in]
     - LocalIpAddrPtr
     - Pointer to structure containing the IP address which shall be assigned to the EthIf controller indirectly specified via SoConId.Note: This parameter is only used in case the parameter Type is set to TCPIP_IPADDR_ASSIGNMENT_STATIC, can be set to NULL_PTR otherwise.
   * - [in]
     - Netmask
     - Network mask of IPv4 address or address prefix of IPv6 address in CIDR Notation. Note: This parameter is only used in case the parameter Type is set to TCPIP_IPADDR_ASSIGNMENT_STATIC.
   * - [in]
     - DefaultRouterPtr
     - Pointer to structure containing the IP address of the default router (gateway) which shall be assigned. Note: This parameter is only used in case the parameter Type is set to TCPIP_IPADDR_ASSIGNMENT_STATIC, can be set to NULL_PTR otherwise.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The request has been accepted.
   * - E_NOT_OK
     - The request has not been accepted.

SoAd_ReleaseIpAddrAssignment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType SoAd_ReleaseIpAddrAssignment(SoAd_SoConIdType SoConId)

By this API service the local IP address assignment used for the socket connection specified by SoConId is released.

**Sync/Async**
   FALSE

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
     - SoConId
     - socket connection index specifying the socket connection for which the IP address shall be released

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The request has been accepted.
   * - E_NOT_OK
     - The request has not been accepted.

SoAd_GetLocalAddr
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType SoAd_GetLocalAddr(SoAd_SoConIdType SoConId, TcpIp_SockAddrType *LocalAddrPtr, uint8 *NetmaskPtr, TcpIp_SockAddrType *DefaultRouterPtr)

Retrieves the local address (IP address and port) actually used for the SoAd socket connection specified by SoConId, the netmask and default router.

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
     - SoConId
     - socket connection index representing the SoAd socket connection for which the actual local IP address shall be obtained.
   * - [inout]
     - LocalAddrPtr
     - Pointer to a struct where the local address (IP address and port) is stored.
   * - [out]
     - NetmaskPtr
     - Pointer to memory where Network mask of IPv4 address or address prefix of IPv6 address in CIDR Notation is stored
   * - [inout]
     - DefaultRouterPtr
     - Pointer to struct where the IP address of the default router (gateway) is stored (struct member "port" is not used and of arbitrary value).

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The request was successful.
   * - E_NOT_OK
     - The request was not successful.

SoAd_GetPhysAddr
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType SoAd_GetPhysAddr(SoAd_SoConIdType SoConId, uint8 *PhysAddrPtr)

Retrieves the physical source address of the EthIf controller used by the SoAd socket connection specified by SoConId.

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
     - SoConId
     - socket connection index representing the SoAd socket connection for which the physical source address of the related EthIf controller shall be obtained.
   * - [out]
     - PhysAddrPtr
     - Pointer to the memory where the physical source address (MAC address) in network byte order is stored.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The request was successful.
   * - E_NOT_OK
     - The request was not successful.

SoAd_GetRemoteAddr
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType SoAd_GetRemoteAddr(SoAd_SoConIdType SoConId, TcpIp_SockAddrType *IpAddrPtr)

Retrieves the remote address (IP address and port) actually used for the SoAd socket connection specified by SoConId.

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
     - SoConId
     - socket connection index representing the SoAd socket connection for which the actually specified remote address shall be obtained.
   * - [out]
     - IpAddrPtr
     - Pointer to a struct where the retrieved remote address (IP address and port) is stored.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The request was successful.
   * - E_NOT_OK
     - The request was not successful.

SoAd_EnableRouting
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType SoAd_EnableRouting(SoAd_RoutingGroupIdType id)

Enables routing of a group of PDUs in the SoAd related to the RoutingGroup specified by parameter id. Routing of PDUs can be either forwarding of PDUs from the upper layer to a TCP or UDP socket of the TCP/IP stack specified by a PduRoute or the other way around specified by a SocketRoute.

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
     - id
     - routing group identifier specifying the routing group to be enabled

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The request was successful.
   * - E_NOT_OK
     - The request was not successful.

SoAd_EnableSpecificRouting
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType SoAd_EnableSpecificRouting(SoAd_RoutingGroupIdType id, SoAd_SoConIdType SoConId)

Enables routing of a group of PDUs in the SoAd related to the RoutingGroup specified by parameter id only on the socket connection identified by SoConId.

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
     - id
     - routing group identifier specifying the routing group to be enabled
   * - [in]
     - SoConId
     - socket connection index specifying the socket connection on which the routing group shall be enabled

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The request was successful.
   * - E_NOT_OK
     - The request was not successful.

SoAd_DisableRouting
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType SoAd_DisableRouting(SoAd_RoutingGroupIdType id)

Disables routing of a group of PDUs in the SoAd related to the RoutingGroup specified by parameter id. Routing of PDUs can be either forwarding of PDUs from the upper layer to a TCP or UDP socket of the TCP/IP stack specified by a PduRoute or the other way around specified by a SocketRoute.

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
     - id
     - routing group identifier specifying the routing group to be disabled

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The request was successful.
   * - E_NOT_OK
     - The request was not successful.

SoAd_DisableSpecificRouting
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType SoAd_DisableSpecificRouting(SoAd_RoutingGroupIdType id, SoAd_SoConIdType SoConId)

Disables routing of a group of PDUs in the SoAd related to the RoutingGroup specified by parameter id only on the socket connection identified by SoConId.

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
     - id
     - routing group identifier specifying the routing group to be disabled
   * - [in]
     - SoConId
     - socket connection index specifying the socket connection on which the routing group shall be disabled

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The request was successful.
   * - E_NOT_OK
     - The request was not successful.

SoAd_SetRemoteAddr
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType SoAd_SetRemoteAddr(SoAd_SoConIdType SoConId, const TcpIp_SockAddrType *RemoteAddrPtr)

By this API service the remote address (IP address and port) of the specified socket connection shall be set.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant for different SoConIds. Non reentrant for the same SoConId.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - SoConId
     - socket connection index specifying the socket connection for which the remote address shall be set
   * - [in]
     - RemoteAddrPtr
     - Struct containint the IP address and port to be set.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The request has been accepted.
   * - E_NOT_OK
     - The request has not been accepted.

SoAd_SetUniqueRemoteAddr
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType SoAd_SetUniqueRemoteAddr(SoAd_SoConIdType SoConId, const TcpIp_SockAddrType *RemoteAddrPtr, SoAd_SoConIdType *AssignedSoConIdPtr)

This API service shall either return the socket connection index of the SoAdSocketConnection Group where the specified remote address (IP address and port) is set or assign the remote address to an unused socket connection from the same SoAdSocketConnectionGroup.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant for different SoConIds. Non reentrant for the same SoConId.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - SoConId
     - Index of any socket connection that is part of the SoAdSocket ConnectionGroup.
   * - [in]
     - RemoteAddrPtr
     - Pointer to the structure containing the requested remote IP address and port.
   * - [out]
     - AssignedSoConIdPtr
     - Pointer to the SoAd_SoConIdType where the index of the socket connection configured with the remote address (RemoteAddrPtr) shall be stored.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The request has been accepted.
   * - E_NOT_OK
     - The request was rejected, AssignedSoConIdPtr remains unchanged.

SoAd_ReleaseRemoteAddr
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void SoAd_ReleaseRemoteAddr(SoAd_SoConIdType SoConId)

By this API service the remote address (IP address and port) of the specified socket connection shall be released, i.e. set back to the configured remote address setting.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant for different SoConIds. Non reentrant for the same SoConId.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - SoConId
     - Index of the socket connection for which the remote address shall be released.

**Return type**
   void

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The request has been accepted.
   * - E_NOT_OK
     - The request was rejected, AssignedSoConIdPtr remains unchanged.

SoAd_TpChangeParameter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType SoAd_TpChangeParameter(PduIdType id, TPParameterType parameter, uint16 value)

Request to change a specific transport protocol parameter (e.g. block size).

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
     - id
     - Identification of the PDU which the parameter change shall affect.
   * - [in]
     - parameter
     - ID of the parameter that shall be changed.
   * - [in]
     - value
     - The new value of the parameter.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The parameter was changed successfully.
   * - E_NOT_OK
     - The parameter change was rejected.

SoAd_ReadDhcpHostNameOption
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType SoAd_ReadDhcpHostNameOption(SoAd_SoConIdType SoConId, uint8 *length, uint8 *data)

By this API service an upper layer of the SoAd can read the currently configured hostname, i.e. FQDN option in the DHCP submodule of the TCP/IP stack.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant for different SoConIds. Non reentrant for the same SoConId.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - SoConId
     - socket connection index specifying the socket connection for which the hostname shall be read.
   * - [in]
     - length
     - As input parameter, contains the length of the provided data buffer. Will be overwritten with the length of the actual data.
   * - [in]
     - data
     - Pointer to provided memory buffer the hostname, i.e. the Fully Qualified Domain Name (FQDN) according to IETF RFC 4702/IETF RFC 4704 will be copied to.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The request has been accepted.
   * - E_NOT_OK
     - The request has not been accepted.

SoAd_WriteDhcpHostNameOption
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType SoAd_WriteDhcpHostNameOption(SoAd_SoConIdType SoConId, uint8 length, const uint8 *data)

By this API service an upper layer of the SoAd can set the hostname, i.e. FQDN option in the DHCP submodule of the TCP/IP stack.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant for different SoConIds. Non reentrant for the same SoConId.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - SoConId
     - socket connection index specifying the socket connection for which the hostname shall be changed
   * - [in]
     - length
     - Length of hostname to be set.
   * - [in]
     - data
     - Pointer to memory containing the hostname, i.e. the Fully Qualified Domain Name (FQDN) according to IETF RFC 4702/IETF RFC 4704.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The request has been accepted.
   * - E_NOT_OK
     - The request has not been accepted.

SoAd_GetSoConMode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void SoAd_GetSoConMode(SoAd_SoConIdType SoConId, SoAd_SoConModeType *ModePtr)

Returns current state of the socket connection specified by SoConId.

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
     - SoConId
     - socket connection index specifying the socket connection for which the state shall be returned.
   * - [out]
     - ModePtr
     - Pointer to memory where the socket connection state shall be stored.

**Return type**
   void


SoAd_IfTransmit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType SoAd_IfTransmit(PduIdType TxPduId, const PduInfoType *PduInfoPtr)

Requests transmission of a PDU.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant for different SoConIds. Non reentrant for the same SoConId.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - TxPduId
     - Identifier of the PDU to be transmitted
   * - [in]
     - PduInfoPtr
     - Length of and pointer to the PDU data and pointer to MetaData.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Transmit request has been accepted.
   * - E_NOT_OK
     - Transmit request has not been accepted.

SoAd_TpTransmit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType SoAd_TpTransmit(PduIdType TxPduId, const PduInfoType *PduInfoPtr)

Requests transmission of a PDU.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant for different SoConIds. Non reentrant for the same SoConId.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - TxPduId
     - Identifier of the PDU to be transmitted
   * - [in]
     - PduInfoPtr
     - Length of and pointer to the PDU data and pointer to MetaData.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Transmit request has been accepted.
   * - E_NOT_OK
     - Transmit request has not been accepted.

SoAd_TpCancelReceive
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType SoAd_TpCancelReceive(PduIdType RxPduId)

Requests cancellation of an ongoing reception of a PDU in a lower layer transport protocol module.

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
     - RxPduId
     - Identification of the PDU to be cancelled.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Cancellation was executed successfully by the destination module.
   * - E_NOT_OK
     - Cancellation was rejected by the destination module.

SoAd_TpCancelTransmit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType SoAd_TpCancelTransmit(PduIdType TxPduId)

Requests cancellation of an ongoing transmission of a PDU in a lower layer communication module.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant for different PduIds. Non reentrant for the same PduId.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - TxPduId
     - Identification of the PDU to be cancelled.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Cancellation was executed successfully by the destination module.
   * - E_NOT_OK
     - Cancellation was rejected by the destination module.

SoAd_IsConnectionReady
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    TcpIp_ReturnType SoAd_IsConnectionReady(SoAd_SoConIdType SoConId, const TcpIp_SockAddrType *RemoteAddrPtr)

API allows to check if a communication over this socket connection is possible for a dedicated remote address. It includes that the socket connection is bound to a socket, a physical address is available for the requested remote address and if a security association is configured that a ecured connection is already established.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant for different SoConIds. Non reentrant for the same SoConId.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - SoConId
     - Socket connection index specifying the socket connection for the request.
   * - [in]
     - RemoteAddrPtr
     - Pointer to the structure containing the requested remote IP address and port.

**Return type**
   TcpIp_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - TCPIP_E_OK
     - Connection is ready for communication.
   * - TCPIP_E_NOT_OK
     - Request was rejected.
   * - TCPIP_E_PENDING
     - Connection establishment in progress.

