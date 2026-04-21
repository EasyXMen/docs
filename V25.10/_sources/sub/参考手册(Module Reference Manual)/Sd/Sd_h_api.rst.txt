.. include:: Sd_Type_h_api.rst

Sd模块接口描述 Descriptions of Sd Module Interface
--------------------------------------------------------------------------------------------
.. 如果没有就不存在该章节，或为None

Sd_Init
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Sd_Init(const Sd_ConfigType *ConfigPtr)

Initializes the Service Discovery.

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
     - ConfigPtr
     - Pointer to a selected configuration structure.

**Return type**
   void


Sd_GetVersionInfo
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Sd_GetVersionInfo(Std_VersionInfoType *versioninfo)

Returns the version information of this module.

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


Sd_ServerServiceSetState
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Sd_ServerServiceSetState(uint16 SdServerServiceHandleId, Sd_ServerServiceSetStateType ServerServiceState)

This API function is used by the BswM to set the Server Service Instance state.

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
     - SdServerServiceHandleId
     - ID to identify the Server Service Instance.
   * - [in]
     - ServerServiceState
     - The state the Server Service Instance shall be set to.

**Return type**
   Std_ReturnType


Sd_ClientServiceSetState
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Sd_ClientServiceSetState(uint16 ClientServiceHandleId, Sd_ClientServiceSetStateType ClientServiceState)

This API function is used by the BswM to set the Client Service Instance state.

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
     - ClientServiceHandleId
     - ID to identify the Client Service Instance.
   * - [in]
     - ClientServiceState
     - The state the Client Service Instance shall be set to.

**Return type**
   Std_ReturnType


Sd_ServiceGroupStart
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Sd_ServiceGroupStart(Sd_ServiceGroupIdType ServiceGroupId)

Starts a preconfigured SdServiceGroup.

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
     - ServiceGroupId
     - Id of SdServiceGroup to be started

**Return type**
   void


Sd_ServiceGroupStop
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Sd_ServiceGroupStop(Sd_ServiceGroupIdType ServiceGroupId)

Stops a preconfigured SdServiceGroup.

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
     - ServiceGroupId
     - Id of SdServiceGroup to be stopped

**Return type**
   void


Sd_ConsumedEventGroupSetState
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType Sd_ConsumedEventGroupSetState(uint16 SdConsumedEventGroupHandleId, Sd_ConsumedEventGroupSetStateType ConsumedEventGroupState)

This API function is used by the BswM to set the requested state of the EventGroupStatus.

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
     - SdConsumedEventGroupHandleId
     - ID to identify the Consumed Eventgroup.
   * - [in]
     - ConsumedEventGroupState
     - The state the EventGroup shall be set to.

**Return type**
   Std_ReturnType


Sd_LocalIpAddrAssignmentChg
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Sd_LocalIpAddrAssignmentChg(SoAd_SoConIdType SoConId, TcpIp_IpAddrStateType State)

This function gets called by the SoAd if an IP address assignment related to a socket connection changes (i.e. new address assigned or assigned address becomes invalid).

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant for different SoConIds.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - SoConId
     - socket connection index specifying the socket connection where the IP address assigment has changed.
   * - [in]
     - State
     - state of IP address assignment.

**Return type**
   void


Sd_SoConModeChg
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Sd_SoConModeChg(SoAd_SoConIdType SoConId, SoAd_SoConModeType Mode)

Notification about a SoAd socket connection state change, e.g. socket connection gets online.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant for different SoConIds.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - SoConId
     - socket connection index specifying the socket connection where the IP address assigment has changed.
   * - [in]
     - Mode
     - new mode.

**Return type**
   void


Sd_RxIndication
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void Sd_RxIndication(PduIdType RxPduId, const PduInfoType *PduInfoPtr)

Indication of a received I-PDU from a lower layer communication interface module.

**Sync/Async**
   TRUE

**Reentrancy**
   Reentrant for different SoConIds.

**Parameters**

.. list-table::
   :widths: 5 10 30
   :header-rows: 1

   * - Dir
     - Name
     - Description
   * - [in]
     - RxPduId
     - ID of the received I-PDU.
   * - [in]
     - PduInfoPtr
     - Contains the length (SduLength) of the received I-PDU and a pointer to a buffer (SduDataPtr) containing the I-PDU.

**Return type**
   void
