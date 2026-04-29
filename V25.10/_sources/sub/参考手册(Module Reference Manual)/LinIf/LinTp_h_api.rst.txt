LinTp_Init
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void LinTp_Init(const LinTp_ConfigType *ConfigPtr)

Initializes the LIN Transport Layer.

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
     - Pointer to the LIN Transport Protocol configuration

**Return type**
   void


LinTp_Transmit
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType LinTp_Transmit(PduIdType LinTpTxSduId, const PduInfoType *LinTpTxInfoPtr)

Requests the transfer of segmented data.

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
     - LinTpTxSduId
     - This parameter contains the unique identifier of the N-SDU to be transmitted
   * - [in]
     - LinTpTxInfoPtr
     - A pointer to a structure with N-SDU related data

**Return type**
   Std_ReturnType


LinTp_GetVersionInfo
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    static inline void LinTp_GetVersionInfo(Std_VersionInfoType *versionInfo)

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
   * - 
     - versionInfo
     - 

**Return type**
   void


LinTp_Shutdown
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    void LinTp_Shutdown(void)

Shutdowns the LIN TP.

**Sync/Async**
   TRUE

**Reentrancy**
   Non Reentrant


**Return type**
   void


LinTp_ChangeParameter
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    Std_ReturnType LinTp_ChangeParameter(PduIdType id, TPParameterType parameter, uint16 value)

A dummy method introduced for interface compatibility.

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
     - Identifier of the received N-SDU on which the reception parameter has to be changed.
   * - [in]
     - parameter
     - The selected parameter that the request shall change (STmin).
   * - [in]
     - value
     - The new value of the parameter.

**Return type**
   Std_ReturnType
