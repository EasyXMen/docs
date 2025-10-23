

SoAd_RxIndication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void SoAd_RxIndication(TcpIp_SocketIdType SocketId, const TcpIp_SockAddrType *RemoteAddrPtr, uint8 *BufPtr, uint16 Length)

The TCP/IP stack calls this primitive after the reception of data on a socket. The socket identifier along with configuration information determines which module is to be called.

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
     - RemoteAddrPtr
     - Pointer to memory containing IP address and port of the
   * - [in]
     - BufPtr
     - Pointer to the received data
   * - [in]
     - Length
     - Data length of the received TCP segment or UDP datagram

**Return type**
    void


SoAd_CopyTxData
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    BufReq_ReturnType SoAd_CopyTxData(TcpIp_SocketIdType SocketId, uint8 *BufPtr, uint16 BufLength)

This service requests to copy data for transmission to the buffer indicated. This call is triggered by TcpIp_Transmit(). Note: The call to <Up>_CopyTxData() may happen in the context of TcpIp_Transmit()

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant for different SocketIds. Non reentrant for the same SocketId

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - SocketId
     - Socket identifier of the related local socket resource
   * - [in]
     - BufPtr
     - Pointer to buffer for transmission data
   * - [in]
     - BufLength
     - Length of provided data buffer

**Return type**
   BufReq_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - BUFREQ_OK
     - Data has been copied to the transmit buffer completely as requested
   * - BUFREQ_E_NOT_OK
     - Data has not been copied. Request failed

SoAd_TxConfirmation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void SoAd_TxConfirmation(TcpIp_SocketIdType SocketId, uint16 Length)

The TCP/IP stack calls this function after the data has been acknowledged by the peer for TCP. Caveats: The upper layer might not be able to determine exactly which data bytes have been confirmed.

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
     - Length
     - Number of transmitted data bytes.

**Return type**
   void


SoAd_TcpAccepted
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType SoAd_TcpAccepted(TcpIp_SocketIdType SocketId, TcpIp_SocketIdType SocketIdConnected, const TcpIp_SockAddrType *RemoteAddrPtr)

This service gets called if the stack put a socket into the listen mode before (as server) and a peer connected to it (as client).In detail: The TCP/IP stack calls this function after a socket was set into the listen state with TcpIp_TcpListen() and a TCP connection is requested by the peer.

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
     - SocketId
     - Socket identifier of the related local socket resource which has been used at TcpIp_Bind()
   * - [in]
     - SocketIdConnected
     - Socket identifier of the local socket resource used for the established connection
   * - [in]
     - RemoteAddrPtr
     - IP address and port of the remote host

**Return type**
   Std_ReturnType

**Return values**

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - Name
     - Description
   * - E_OK
     - upper layer accepts the established connection
   * - E_NOT_OK
     - upper layer refuses the established

SoAd_TcpConnected
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void SoAd_TcpConnected(TcpIp_SocketIdType SocketId)

This service gets called if the stack initiated a TCP connection before (as client) and the peer (the server) acknowledged the connection set up.In detail:The TCP/IP stack calls this function after a socket was requested to connect with TcpIp_TcpConnect() and a TCP connection is confirmed by the peer.The parameter value of SocketId equals the SocketId value of the preceding TcpIp_TcpConnect() call.

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
     - SocketId
     - Socket identifier of the related local socket resource

**Return type**
   void


SoAd_TcpIpEvent
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void SoAd_TcpIpEvent(TcpIp_SocketIdType SocketId, TcpIp_EventType Event)

This service gets called if the stack encounters a condition described by the values in Event.

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
     - SocketId
     - Socket identifier of the related local socket resource
   * - [in]
     - Event
     - This parameter contains a description of the event just encountered

**Return type**
   void


SoAd_LocalIpAddrAssignmentChg
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void SoAd_LocalIpAddrAssignmentChg(TcpIp_LocalAddrIdType IpAddrId, TcpIp_IpAddrStateType State)

This service gets called by the TCP/IP stack if an IP address assignment changes (i.e. new address assigned or assigned address becomes invalid).

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
     - IpAddrId
     - IP address Identifier, representing an IP address specified in the TcpIp module configuration (e.g. static IPv4 address on EthIf controller 0)
   * - [in]
     - State
     - state of IP address assignment

**Return type**
   void


