
类型定义 Type Definitions
-----------------------------------------------------------------------------------

.. list-table:: 
   :widths: 15 5 20
   :header-rows: 1

   * - Type Name
     - Type
     - Description

   * - SecOC_SameBufferPduCollectionType
     - struct SecOC_SameBufferPduCollectionTag
     - Define SecOC Buffer configuration that may be used by a collection of Pdus.

   * - SecOC_ReceptionOverflowStrategyType
     - enum SecOC_ReceptionOverflowStrategyTag
     - Define strategy for handling PDUs when the received buffer overflows.

   * - SecOC_VeriStatusPropModeType
     - enum SecOC_VeriStatusPropModeTag
     - Define which authentication state is passed to the SWC.

   * - SecOC_PduType
     - enum SecOC_PduTag
     - Define the type of API.

   * - SecOC_CryptoProcessingType
     - enum SecOC_CryptoProcessingTag
     - Define the encryption and decryption process, synchronous or asynchronous.

   * - SecOC_CsmPrimitivesType
     - enum SecOC_CsmPrimitivesTag
     - Define the Csm primitive, MAC or SIGNATURE.

   * - SecOC_CsmJobType
     - struct SecOC_CsmJobTag
     - Define information about the Csm job.

   * - SecOC_RxSecuredPduType
     - struct SecOC_RxSecuredPduTag
     - Define the Pdu that is received by the SecOC module from the PduR.

   * - SecOC_RxAuthenticPduType
     - struct SecOC_RxAuthenticPduTag
     - Define the Authentic Pdu that is received by the SecOC module from the PduR.

   * - SecOC_RxCryptographicPduType
     - struct SecOC_RxCryptographicPduTag
     - Define the Cryptographic Pdu that is received by the SecOC module from the PduR.

   * - SecOC_UseMessageLinkType
     - struct SecOC_UseMessageLinkTag
     - Define information about the message linker.SecOC links an Authentic I-Pdu and Cryptographic I-Pdu together by repeating a specific part (Message Linker) of the Authentic I-Pdu in the Cryptographic I-Pdu.

   * - SecOC_QueueInfoType
     - struct SecOC_QueueInfoTag
     - Define information about the queue where PDUs reside.

   * - SecOC_RxPduProcessingType
     - struct SecOC_RxPduProcessingTag
     - Define the processing information of the Rx Pdu.

   * - SecOC_TxPduProcessingType
     - struct SecOC_TxPduProcessingTag
     - Define the processing information of the Tx Pdu.

   * - SecOC_RxSecuredPduCollectionType
     - struct SecOC_RxSecuredPduCollectionTag
     - When Secured I-Pdu is received in Authentic I-Pdu and CryptoGraphic I-Pdu, specify all information of this Secured I-Pdu.

   * - SecOC_RxSecuredPduLayerType
     - struct SecOC_RxSecuredPduLayerTag
     - Define information about the two types of Rx Secured I-PDUs.

   * - SecOC_RxPduSecuredAreaType
     - struct SecOC_RxPduSecuredAreaTag
     - Define an area in the Authentic I-Pdu that will be the input to the Authenticator verification algorithm.

   * - SecOC_RxAuthenticPduLayerType
     - struct SecOC_RxAuthenticPduLayerTag
     - Define the Pdu that is received by the SecOC module from the PduR.

   * - SecOC_PbRxPduProcessingType
     - struct SecOC_PbRxPduProcessingTag
     - Define the information at the post-build phase to configure the RxPdus to be verified by the SecOC module.

   * - SecOC_TxSecuredPduType
     - struct SecOC_TxSecuredPduTag
     - Define one Pdu that is transmitted by the SecOC module to the PduR after the Mac was generated.

   * - SecOC_TxAuthenticPduType
     - struct SecOC_TxAuthenticPduTag
     - Define the Pdu (that is transmitted by the SecOC module to the PduR) which contains the Secured I-Pdu Header and the Authentic I-Pdu.

   * - SecOC_TxCryptographicPduType
     - struct SecOC_TxCryptographicPduTag
     - Define the Cryptographic Pdu that is transmitted.

   * - SecOC_TxSecuredPduCollectionType
     - struct SecOC_TxSecuredPduCollectionTag
     - Define the Pdu that is transmitted by the SecOC module to the PduR after the Mac was generated.Two separate Pdus are transmitted to the PduR:Authentic I-Pdu and Cryptographic I-Pdu.

   * - SecOC_TxSecuredPduLayerType
     - struct SecOC_TxSecuredPduLayerTag
     - Define the Pdu that is transmitted by the SecOC module to the PduR after the Mac was generated.

   * - SecOC_TxPduSecuredAreaType
     - struct SecOC_TxPduSecuredAreaTag
     - Define an area in the Authentic I-Pdu that will be the input to the Authenticator generation algorithm.

   * - SecOC_TxAuthenticPduLayerType
     - struct SecOC_TxAuthenticPduLayerTag
     - Define the Pdu that is transmitted by the SecOC module to the PduR after the Mac was verified.

   * - SecOC_PbTxPduProcessingType
     - struct SecOC_PbTxPduProcessingTag
     - Define the information at the post-build phase to configure the TxPdus to be secured by the SecOC module.

   * - SecOC_PbConfigType
     - struct SecOC_PbConfigTag
     - Define configuration information at the post-build phase for the SecOC module.

   * - SecOC_ReceptionOverflowStrategyTag
     - enum
     - Define strategy for handling PDUs when the received buffer overflows.

   * - SecOC_VeriStatusPropModeTag
     - enum
     - Define which authentication state is passed to the SWC.

   * - SecOC_PduTag
     - enum
     - Define the type of API.

   * - SecOC_CryptoProcessingTag
     - enum
     - Define the encryption and decryption process, synchronous or asynchronous.

   * - SecOC_CsmPrimitivesTag
     - enum
     - Define the Csm primitive, MAC or SIGNATURE.


