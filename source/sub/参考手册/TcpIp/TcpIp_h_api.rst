
类型定义 Type Definitions
--------------------------------------------------------------------------------
.. 如果没有就不存在该章节，或为None

None


提供的服务 Services
--------------------------------------------------------------------------------
TcpIp_Init
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void TcpIp_Init(const TcpIp_ConfigType *ConfigPtr)

This service initializes the TCP/IP Stack.TcpIp_Init may not block the start-up process for an indefinite amount of time.

**Sync/Async**
   TRUE

**Reentrancy**
   Non reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - ConfigPtr
     - Pointer to the configuration data of the TcpIp module

**Return type**
   void


TcpIp_GetVersionInfo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void TcpIp_GetVersionInfo(Std_VersionInfoType *versioninfo)

Returns the version information.

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


TcpIp_Close
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType TcpIp_Close(TcpIp_SocketIdType SocketId, boolean Abort)

By this API service the TCP/IP stack is requested to close the socket and release all related resources.

**Sync/Async**
   FALSE

**Reentrancy**
   Reentrant for different SocketIds. Non reentrant for the same SocketId.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - SocketId
     - Socket handle identifying the local socket resource.
   * - [in]
     - Abort
     - TRUE: connection will immediately be terminated by sending a RST-Segment and releasing all related resources. FALSE: connection will be terminated after performing a regular connection termination handshake and releasing all related resources.

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

TcpIp_Bind
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType TcpIp_Bind(TcpIp_SocketIdType SocketId, TcpIp_LocalAddrIdType LocalAddrId, uint16 *PortPtr)

By this API service the TCP/IP stack is requested to bind a UDP or TCP socket to a local resource.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant for different SocketIds. Non reentrant for the same SocketId.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - SocketId
     - Socket identifier of the related local socket resource.
   * - [in]
     - LocalAddrId
     - IP address identifier representing the local IP address and EthIf controller to bind the socket to.
   * - [inout]
     - PortPtr
     - Pointer to memory where the local port to which the socket shall be bound is specified. In case the parameter is specified as TCPIP_PORT_ANY, the TCP/IP stack shall choose the local port automatically from the range 49152 to 65535 and shall update the parameter to the chosen value.

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
     - The request has not been accepted (e.g. address in use).

TcpIp_TcpConnect
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType TcpIp_TcpConnect(TcpIp_SocketIdType SocketId, const TcpIp_SockAddrType *RemoteAddrPtr)

By this API service the TCP/IP stack is requested to establish a TCP connection to the configured peer.

**Sync/Async**
   FALSE

**Reentrancy**
   Reentrant for different SocketIds. Non reentrant for the same SocketId.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - SocketId
     - Socket identifier of the related local socket resource.
   * - [in]
     - RemoteAddrPtr
     - IP address and port of the remote host to connect to.

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
     - The request has not been accepted, e.g. connection is already established or no route to destination specified by remoteAddrPtr found.

TcpIp_TcpListen
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType TcpIp_TcpListen(TcpIp_SocketIdType SocketId, uint16 MaxChannels)

By this API service the TCP/IP stack is requested to listen on the TCP socket specified by the socket identifier.

**Sync/Async**
   FALSE

**Reentrancy**
   Reentrant for different SocketIds. Non reentrant for the same SocketId.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - SocketId
     - Socket identifier of the related local socket resource.
   * - [in]
     - MaxChannels
     - Maximum number of new parallel connections established on this listen connection.

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
     - The request has not been accepted, the socket is not configured to be a server socket.

TcpIp_TcpReceived
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType TcpIp_TcpReceived(TcpIp_SocketIdType SocketId, uint32 Length)

By this API service the reception of socket data is confirmed to the TCP/IP stack.

**Sync/Async**
   FALSE

**Reentrancy**
   Reentrant for different SocketIds. Non reentrant for the same SocketId.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - SocketId
     - Socket identifier of the related local socket resource.
   * - [in]
     - Length
     - Number of bytes finally consumed by the upper layer.

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

TcpIp_RequestComMode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType TcpIp_RequestComMode(uint8 CtrlIdx, TcpIp_StateType State)

By this API service the TCP/IP stack is requested to change the TcpIp state of the communication network identified by EthIf controller index.

**Sync/Async**
   FALSE

**Reentrancy**
   Non reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - CtrlIdx
     - EthIf controller index to identify the communication network where the TcpIp state is requested.
   * - [in]
     - State
     - Requested TcpIp state.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Service accepted.
   * - E_NOT_OK
     - Service denied.

TcpIp_RequestIpAddrAssignment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType TcpIp_RequestIpAddrAssignment(TcpIp_LocalAddrIdType LocalAddrId, TcpIp_IpAddrAssignmentType Type, const TcpIp_SockAddrType *LocalIpAddrPtr, uint8 Netmask, const TcpIp_SockAddrType *DefaultRouterPtr)

By this API service the local IP address assignment for the IP address specified by LocalAddrId shall be initiated.

**Sync/Async**
   FALSE

**Reentrancy**
   Non reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - LocalAddrId
     - IP address index specifying the IP address for which an assignment shall be initiated.
   * - [in]
     - Type
     - Type of IP address assignment which shall be initiated.
   * - [in]
     - LocalIpAddrPtr
     - Pointer to structure containing the IP address which shall be assigned to the EthIf controller indirectly specified via LocalAddr Id.
   * - [in]
     - Netmask
     - Network mask of IPv4 address or address prefix of IPv6 address in CIDR Notation.
   * - [in]
     - DefaultRouterPtr
     - Pointer to structure containing the IP address of the default router (gateway) which shall be assigned.

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

TcpIp_ReleaseIpAddrAssignment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType TcpIp_ReleaseIpAddrAssignment(TcpIp_LocalAddrIdType LocalAddrId)

By this API service the local IP address assignment for the IP address specified by LocalAddrId shall be released.

**Sync/Async**
   FALSE

**Reentrancy**
   Non reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - LocalAddrId
     - IP address index specifying the IP address for which an assignment shall be released.

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

TcpIp_ResetIpAssignment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType TcpIp_ResetIpAssignment(void)

Resets all learned IP-addresses to invalid values.

**Sync/Async**
   TRUE

**Reentrancy**
   Non reentrant


**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - success.
   * - E_NOT_OK
     - switch port could not be initialized.

TcpIp_IcmpTransmit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType TcpIp_IcmpTransmit(TcpIp_LocalAddrIdType LocalIpAddrId, const TcpIp_SockAddrType *RemoteAddrPtr, uint8 Ttl, uint8 Type, uint8 Code, uint16 DataLength, const uint8 *DataPtr)

By this API service the TCP/IP stack sends an ICMP message according to the specified parameters.

**Sync/Async**
   TRUE

**Reentrancy**
   Non reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - LocalIpAddrId
     - IP address identifier representing the local IP address and EthIf controller which shall be used for transmission of the ICMP message.
   * - [in]
     - RemoteAddrPtr
     - pointer to struct representing the remote address.
   * - [in]
     - Ttl
     - Time to live value to be used for the ICMP message. If 0 is specified the default value shall be used.
   * - [in]
     - Type
     - type field value to be used in the ICMP message.
   * - [in]
     - Code
     - code field value to be used in the ICMP message.
   * - [in]
     - DataLength
     - length of ICMP message.
   * - [in]
     - DataPtr
     - Pointer to data which shall be sent as ICMP message data

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The ICMP message has been sent successfully.
   * - E_NOT_OK
     - The ICMP message was not sent.

TcpIp_IcmpV6Transmit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType TcpIp_IcmpV6Transmit(TcpIp_LocalAddrIdType LocalIpAddrId, const TcpIp_SockAddrType *RemoteAddrPtr, uint8 HopLimit, uint8 Type, uint8 Code, uint16 DataLength, const uint8 *DataPtr)

By this API service the TCP/IP stack sends an ICMPv6 message according to the specified parameters.

**Sync/Async**
   TRUE

**Reentrancy**
   Non reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - LocalIpAddrId
     - IP address identifier representing the local IP address and EthIf controller which shall be used for transmission of the ICMPv6 message.
   * - [in]
     - RemoteAddrPtr
     - pointer to struct representing the remote address.
   * - [in]
     - HopLimit
     - Hop Limit value to be used for the ICMPv6 message. If 0 is specified the default value shall be used.
   * - [in]
     - Type
     - type field value to be used in the ICMPv6 message.
   * - [in]
     - Code
     - code field value to be used in the ICMPv6 message.
   * - [in]
     - DataLength
     - length of ICMPv6 message.
   * - [in]
     - DataPtr
     - Pointer to data which shall be sent as ICMPv6 message data.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The ICMPv6 message has been sent successfully.
   * - E_NOT_OK
     - The ICMPv6 message was not sent.

TcpIp_DhcpReadOption
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType TcpIp_DhcpReadOption(TcpIp_LocalAddrIdType LocalIpAddrId, uint8 Option, uint8 *DataLength, uint8 *DataPtr)

By this API service the TCP/IP stack retrieves DHCP option data identified by parameter option for already received DHCP options.

**Sync/Async**
   TRUE

**Reentrancy**
   Non reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - LocalIpAddrId
     - IP address identifier representing the local IP address and EthIf controller for which the DHCP option shall be read.
   * - [in]
     - Option
     - DHCP option (note: according to IANA DHCP Options).
   * - [inout]
     - DataLength
     - As input parameter, contains the length of the provided data buffer. Will be overwritten with the length of the actual data.
   * - [out]
     - DataPtr
     - Pointer to memory containing DHCP option data.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - requested data retrieved successfully.
   * - E_NOT_OK
     - requested data could not be retrieved.

TcpIp_DhcpV6ReadOption
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType TcpIp_DhcpV6ReadOption(TcpIp_LocalAddrIdType LocalIpAddrId, uint16 Option, uint16 *DataLength, uint8 *DataPtr)

By this API service the TCP/IP stack retrieves DHCPv6 option data identified by parameter option for already received DHCPv6 options.

**Sync/Async**
   TRUE

**Reentrancy**
   Non reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - LocalIpAddrId
     - IP address identifier representing the local IP address and EthIf controller for which the DHCPv6 option shall be read.
   * - [in]
     - Option
     - DHCP option (note: according to IANA DHCP[v6] Options).
   * - [inout]
     - DataLength
     - As input parameter, contains the length of the provided data buffer. Will be overwritten with the length of the actual data.
   * - [out]
     - DataPtr
     - Pointer to memory containing DHCPv6 option data.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - requested data retrieved successfully.
   * - E_NOT_OK
     - requested data could not be retrieved.

TcpIp_DhcpWriteOption
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType TcpIp_DhcpWriteOption(TcpIp_LocalAddrIdType LocalIpAddrId, uint8 Option, uint8 DataLength, const uint8 *DataPtr)

By this API service the TCP/IP stack writes the DHCP option data identified by parameter option.

**Sync/Async**
   TRUE

**Reentrancy**
   Non reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - LocalIpAddrId
     - IP address identifier representing the local IP address and EthIf controller for which the DHCP option shall be written.
   * - [in]
     - Option
     - DHCP option (note: according to IANA DHCP Options).
   * - [in]
     - DataLength
     - length of DHCP option data.
   * - [in]
     - DataPtr
     - Pointer to memory containing DHCP option data

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - no error occured.
   * - E_NOT_OK
     - DHCP option data could not be written.

TcpIp_DhcpV6WriteOption
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType TcpIp_DhcpV6WriteOption(TcpIp_LocalAddrIdType LocalIpAddrId, uint16 Option, uint16 DataLength, const uint8 *DataPtr)

By this API service the TCP/IP stack writes the DHCPv6 option data identified by parameter option.

**Sync/Async**
   TRUE

**Reentrancy**
   Non reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - LocalIpAddrId
     - IP address identifier representing the local IP address and EthIf controller for which the DHCPv6 option shall be written.
   * - [in]
     - Option
     - DHCP option (note: according to IANA DHCP[v6] Options).
   * - [in]
     - DataLength
     - length of DHCPv6 option data.
   * - [in]
     - DataPtr
     - Pointer to memory containing DHCPv6 option data.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - no error occured.
   * - E_NOT_OK
     - DHCPv6 option data could not be written.

TcpIp_ChangeParameter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType TcpIp_ChangeParameter(TcpIp_SocketIdType SocketId, TcpIp_ParamIdType ParameterId, const uint8 *ParameterValue)

By this API service the TCP/IP stack is requested to change a parameter of a socket. E.g. the Nagle algorithm may be controlled by this API.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant for different SocketIds. Non reentrant for the same SocketId.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - SocketId
     - Socket identifier of the related local socket resource.
   * - [in]
     - ParameterId
     - Identifier of the parameter to be changed.
   * - [in]
     - ParameterValue
     - Pointer to memory containing the new parameter value.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - The parameter has been changed successfully.
   * - E_NOT_OK
     - The parameter could not be changed.

TcpIp_GetIpAddr
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType TcpIp_GetIpAddr(TcpIp_LocalAddrIdType LocalAddrId, TcpIp_SockAddrType *IpAddrPtr, uint8 *NetmaskPtr, TcpIp_SockAddrType *DefaultRouterPtr)

Obtains the local IP address actually used by LocalAddrId, the netmask and default router.

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
     - LocalAddrId
     - Local address identifier referring to the local IP address which shall be obtained.
   * - [inout]
     - IpAddrPtr
     - Pointer to a struct where the IP address shall be stored. The struct member domain shall be set to the desired TcpIp_Domain Type and it shall be ensured that the struct is large enough to store an address of the selected type (INET or INET6). Struct members not related to the IP address are of arbitrary value and shall not be used.
   * - [out]
     - NetmaskPtr
     - Pointer to memory where Network mask of IPv4 address or address prefix of IPv6 address in CIDR Notation is stored.
   * - [inout]
     - DefaultRouterPtr
     - Pointer to struct where the IP address of the default router (gateway) is stored (struct member "port" is not used and of arbitrary value). The struct must be of the same type and size as IpAddrPtr.

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
     - The request was not successful, e.g. domain in Ip AddrPtr and the local domain type do not match.

TcpIp_GetPhysAddr
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType TcpIp_GetPhysAddr(TcpIp_LocalAddrIdType LocalAddrId, uint8 *PhysAddrPtr)

Obtains the physical source address used by the EthIf controller implicitly specified via Local AddrId.

**Sync/Async**
   TRUE

**Reentrancy**
   Non reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - LocalAddrId
     - Local address identifier implicitely specifing the EthIf controller for which the physical address shall be obtained.
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
     - The request was not successful, e.g. no unique Ctrl specified via IpAddrId.

TcpIp_GetRemotePhysAddr
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    TcpIp_ReturnType TcpIp_GetRemotePhysAddr(uint8 CtrlIdx, const TcpIp_SockAddrType *IpAddrPtr, uint8 *PhysAddrPtr, boolean initRes)

TcpIp_GetRemotePhysAddr queries the IP/physical address translation table specified by Ctrl Idx and returns the physical address related to the IP address specified by IpAddrPtr. In case no physical address can be retrieved and parameter initRes is TRUE, address resolution for the specified IP address is initiated on the local network.

**Sync/Async**
   TRUE

**Reentrancy**
   Non reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - CtrlIdx
     - EthIf controller index to identify the related ARP/NDP table.
   * - [in]
     - IpAddrPtr
     - specifies the IP address for which the physical address shall be retrieved.
   * - [out]
     - PhysAddrPtr
     - Pointer to the memory where the physical address (MAC address) related to the specified IP address is stored in network byte order.
   * - [in]
     - initRes
     - specifies if the address resolution shall be initiated (TRUE) or not (FALSE) in case the physical address related to the specified IP address is currently unknown.

**Return type**
    TcpIp_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - TCPIP_E_OK
     - specified IP address resolved, physical address provided via PhysAddrPtr.
   * - TCPIP_E_PHYS_ADDR_MISS
     - physical address currently unknown (address resolution initiated if initRes set to TRUE).

TcpIp_GetCtrlIdx
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType TcpIp_GetCtrlIdx(TcpIp_LocalAddrIdType LocalAddrId, uint8 *CtrlIdxPtr)

TcpIp_GetCtrlIdx returns the index of the controller related to LocalAddrId.

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
     - LocalAddrId
     - Local address identifier implicitely specifing the EthIf controller that shall be returned.
   * - [out]
     - CtrlIdxPtr
     - Pointer to the memory where the index of the controller related to LocalAddrId is stored.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - the request was successful.
   * - E_NOT_OK
     - the request was not successful.

TcpIp_GetArpCacheEntries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType TcpIp_GetArpCacheEntries(uint8 ctrlIdx, uint32 *numberOfElements, TcpIp_ArpCacheEntryType *entryListPtr)

Copies entries from the physical address cache of the IPv4 instance that is active on the EthIf controller specified by ctrlIdx into a user provided buffer. The function will copy all or numberOf Elements into the output list. If input value of numberOfElements is 0 the function will not copy any data but only return the number of valid entries in the cache. EntryListPtr may be NULL_PTR in this case.

**Sync/Async**
   TRUE

**Reentrancy**
   Non reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - ctrlIdx
     - EthIf controller index to identify the related ARP table.
   * - [inout]
     - numberOfElements
     - In: Maximum number of entries that can be stored in output entry ListPtr. Out: Number of entries written to output entryListPtr (Number of all entries in the cache if input value is 0).
   * - [out]
     - entryListPtr
     - Pointer to memory where the list of cache entries shall be stored.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - physical address cache could be read.
   * - E_NOT_OK
     - physical address cache could not be read (i.e. no IPv4 instance active on this controller).

TcpIp_GetNdpCacheEntries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType TcpIp_GetNdpCacheEntries(uint8 ctrlIdx, uint32 *numberOfElements, TcpIp_NdpCacheEntryType *entryListPtr)

Copies entries from the physical address cache of the IPv6 instance that is active on the EthIf controller specified by ctrlIdx into a user provided buffer. The function will copy all or numberOf Elements into the output list. If input value of numberOfElements is 0 the function will not copy any data but only return the number of valid entries in the cache. EntryListPtr may be NULL_PTR in this case.

**Sync/Async**
   TRUE

**Reentrancy**
   Non reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - ctrlIdx
     - EthIf controller index to identify the related NDP table.
   * - [inout]
     - numberOfElements
     - In: Maximum number of entries that can be stored in output entry ListPtr. Out: Number of entries written to output entryListPtr (Number of all entries in the cache if input value is 0).
   * - [out]
     - entryListPtr
     - Pointer to memory where the list of cache entries shall be stored.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - physical address cache could be read.
   * - E_NOT_OK
     - physical address cache could not be read (i.e. no IPv6 instance active on this controller).

TcpIp_GetAndResetMeasurementData
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType TcpIp_GetAndResetMeasurementData(TcpIp_MeasurementIdxType MeasurementIdx, boolean MeasurementResetNeeded, uint32 *MeasurementDataPtr)

Allows to read and reset detailed measurement data for diagnostic purposes. Get all MeasurementIdx's at once is not supported. TCPIP_MEAS_ALL shall only be used to reset all MeasurementIdx's at once. A NULL_PTR shall be provided for MeasurementDataPtr in this case.

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
     - MeasurementIdx
     - Data index of measurement data
   * - [in]
     - MeasurementResetNeeded
     - Flag to trigger a reset of the measurement data
   * - [out]
     - MeasurementDataPtr
     - Reference to data buffer, where to copy measurement data

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - successful.
   * - E_NOT_OK
     - failed.

TcpIp_IsConnectionReady
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    TcpIp_ReturnType TcpIp_IsConnectionReady(TcpIp_SocketIdType SocketId, const TcpIp_SockAddrType *RemoteAddrPtr)

API allows to check if a communication over this socket is possible for a dedicated remote address. It includes that the socket is bound, a physical address is available for the requested remote address and if a security association is configured that a secured connection is already established.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant for different SocketIds. Non reentrant for the same SocketId.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - SocketId
     - Socket handle identifying the local socket resource.
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
     - SocketId is ready for communication.
   * - TCPIP_E_NOT_OK
     - Request was rejected.
   * - TCPIP_E_PENDING
     - Connection establishment in progress.

TcpIp_UdpTransmit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType TcpIp_UdpTransmit(TcpIp_SocketIdType SocketId, const uint8 *DataPtr, const TcpIp_SockAddrType *RemoteAddrPtr, uint16 TotalLength)

This service transmits data via UDP to a remote node. The transmission of the data is immediately performed with this function call by forwarding it to EthIf.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant for different SocketIds. Non reentrant for the same SocketId.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - SocketId
     - Socket identifier of the related local socket resource.
   * - [in]
     - DataPtr
     - Pointer to a linear buffer of TotalLength bytes containing the data to be transmitted. In case DataPtr is a NULL_PTR, TcpIp shall retrieve data from upper layer via callback <Up>_CopyTxData().
   * - [in]
     - RemoteAddrPtr
     - IP address and port of the remote host to transmit to.
   * - [in]
     - TotalLength
     - indicates the payload size of the UDP datagram.

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - Request to transmit the UDP message has been accepted.
   * - E_NOT_OK
     - UDP message could not be sent because of a permanent error, e.g. message is too long.

TcpIp_TcpTransmit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType TcpIp_TcpTransmit(TcpIp_SocketIdType SocketId, const uint8 *DataPtr, uint32 AvailableLength, boolean ForceRetrieve)

This service requests transmission of data via TCP to a remote node.The transmission of the data is decoupled.

**Sync/Async**
   FALSE

**Reentrancy**
   Reentrant for different SocketIds. Non reentrant for the same SocketId.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - SocketId
     - Socket identifier of the related local socket resource.
   * - [in]
     - DataPtr
     - Pointer to a linear buffer of AvailableLength bytes containing the data to be transmitted. In case DataPtr is a NULL_PTR, TcpIp shall retrieve data from upper layer via callback <Up>_CopyTx Data().
   * - [in]
     - AvailableLength
     - Available data for transmission in bytes.
   * - [in]
     - ForceRetrieve
     - This parameter is only valid if DataPtr is a NULL_PTR. Indicates how the TCP/IP stack retrieves data from upper layer if DataPtr is a NULL_PTR. TRUE: the whole data indicated by availableLength shall be retrieved from the upper layer via one or multiple <Up>_ CopyTxData() calls within the context of this transmit function. FALSE: The TCP/IP stack may retrieve up to availableLength data from the upper layer. It is allowed to retrieve less than availableLength bytes.

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
     - The request has not been accepted, e.g. due to a lack of buffer space or the socket is not connected.

TcpIp_RxIndication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void TcpIp_RxIndication(uint8 CtrlIdx, Eth_FrameType FrameType, boolean IsBroadcast, const uint8 *PhysAddrPtr, const uint8 *DataPtr, uint16 LenByte)

By this API service the TCP/IP stack gets an indication and the data of a received frame.

**Sync/Async**
   TRUE

**Reentrancy**
   Non reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - CtrlIdx
     - Index of the EthIf controller.
   * - [in]
     - FrameType
     - frame type of received Ethernet frame.
   * - [in]
     - IsBroadcast
     - parameter to indicate a broadcast frame.
   * - [in]
     - PhysAddrPtr
     - pointer to Physical source address (MAC address in network byte order) of received Ethernet frame.
   * - [in]
     - DataPtr
     - Pointer to payload of the received Ethernet frame (i.e. Ethernet header is not provided).
   * - [in]
     - LenByte
     - Length of received data.

**Return type**
   void


TcpIp_MainFunction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void TcpIp_MainFunction(ApplicationType partitionIndex)

Schedules the TCP/IP stack.(Entry point for scheduling)

**Sync/Async**
   TRUE

**Reentrancy**
   Non reentrant

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - partitionIndex
     - Index of partition.

**Return type**
   void


TcpIp_MainFunction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void TcpIp_MainFunction(void)

Schedules the TCP/IP stack.(Entry point for scheduling)

**Sync/Async**
   TRUE

**Reentrancy**
   Non reentrant


**Return type**
   void


TcpIp_GetSocket
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType TcpIp_GetSocket(TcpIp_DomainType Domain, TcpIp_ProtocolType Protocol, #if(1u< TCPIP_SOCKETOWNER_NUMBER) uint8 socketOwnerId, #endif TcpIp_SocketIdType *SocketIdPtr)

By this API service the TCP/IP stack is requested to allocate a new socket. Note: Each accepted incoming TCP connection also allocates a socket resource.

**Sync/Async**
   TRUE

**Reentrancy**
   TRUE

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - Domain
     - IP address family.
   * - [in]
     - Protocol
     - Socket protocol as sub-family of parameter type.
   * - [in]
     - socketOwnerId
     - TcpIpSocketOwnerId
   * - [out]
     - SocketIdPtr
     - Pointer to socket identifier representing the requested socket. This socket identifier must be provided for all further API calls which requires a SocketId. Note: SocketIdPtr is only valid if return value is E_OK.

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
     - The request has not been accepted: no free socket.

