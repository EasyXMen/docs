
TcpIp_GetSocket
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType TcpIp_GetSocket(TcpIp_DomainType Domain, TcpIp_ProtocolType Protocol, #if(1u< TCPIP_SOCKETOWNER_NUMBER) uint8 socketOwnerId, #endif TcpIp_SocketIdType *SocketIdPtr)

By this API service the TCP/IP stack is requested to allocate a new socket. Note: Each accepted incoming TCP connection also allocates a socket resource.

**Sync/Async**
   Synchronous

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

