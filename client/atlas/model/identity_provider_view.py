# coding: utf-8

"""
    MongoDB Atlas Administration API

    The MongoDB Atlas Administration API allows developers to manage all components in MongoDB Atlas. To learn more, review the [Administration API overview](https://www.mongodb.com/docs/atlas/api/atlas-admin-api/). This OpenAPI specification covers all of the collections with the exception of Alerts, Alert Configurations, and Events. Refer to the [legacy documentation](https://www.mongodb.com/docs/atlas/reference/api-resources/) for the specifications of these resources.  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from atlas import schemas  # noqa: F401


class IdentityProviderView(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "oktaIdpId",
        }
        
        class properties:
            
            
            class oktaIdpId(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 20
                    min_length = 20
                    regex=[{
                        'pattern': r'^([a-f0-9]{20})$',  # noqa: E501
                    }]
            acsUrl = schemas.StrSchema
            
            
            class associatedDomains(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    unique_items = True
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'associatedDomains':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class associatedOrgs(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    unique_items = True
                    
                    @staticmethod
                    def items() -> typing.Type['ConnectedOrgConfigView']:
                        return ConnectedOrgConfigView
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['ConnectedOrgConfigView'], typing.List['ConnectedOrgConfigView']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'associatedOrgs':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ConnectedOrgConfigView':
                    return super().__getitem__(i)
            audienceUri = schemas.StrSchema
            displayName = schemas.StrSchema
            issuerUri = schemas.StrSchema
        
            @staticmethod
            def pemFileInfo() -> typing.Type['PemFileInfoView']:
                return PemFileInfoView
            
            
            class requestBinding(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "HTTP-POST": "POST",
                        "HTTP-REDIRECT": "REDIRECT",
                    }
                
                @schemas.classproperty
                def POST(cls):
                    return cls("HTTP-POST")
                
                @schemas.classproperty
                def REDIRECT(cls):
                    return cls("HTTP-REDIRECT")
            
            
            class responseSignatureAlgorithm(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "SHA-1": "POSITIVE_1",
                        "SHA-256": "POSITIVE_256",
                    }
                
                @schemas.classproperty
                def POSITIVE_1(cls):
                    return cls("SHA-1")
                
                @schemas.classproperty
                def POSITIVE_256(cls):
                    return cls("SHA-256")
            ssoDebugEnabled = schemas.BoolSchema
            ssoUrl = schemas.StrSchema
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "ACTIVE": "ACTIVE",
                        "INACTIVE": "INACTIVE",
                    }
                
                @schemas.classproperty
                def ACTIVE(cls):
                    return cls("ACTIVE")
                
                @schemas.classproperty
                def INACTIVE(cls):
                    return cls("INACTIVE")
            __annotations__ = {
                "oktaIdpId": oktaIdpId,
                "acsUrl": acsUrl,
                "associatedDomains": associatedDomains,
                "associatedOrgs": associatedOrgs,
                "audienceUri": audienceUri,
                "displayName": displayName,
                "issuerUri": issuerUri,
                "pemFileInfo": pemFileInfo,
                "requestBinding": requestBinding,
                "responseSignatureAlgorithm": responseSignatureAlgorithm,
                "ssoDebugEnabled": ssoDebugEnabled,
                "ssoUrl": ssoUrl,
                "status": status,
            }
    
    oktaIdpId: MetaOapg.properties.oktaIdpId
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["oktaIdpId"]) -> MetaOapg.properties.oktaIdpId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["acsUrl"]) -> MetaOapg.properties.acsUrl: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["associatedDomains"]) -> MetaOapg.properties.associatedDomains: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["associatedOrgs"]) -> MetaOapg.properties.associatedOrgs: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["audienceUri"]) -> MetaOapg.properties.audienceUri: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["displayName"]) -> MetaOapg.properties.displayName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["issuerUri"]) -> MetaOapg.properties.issuerUri: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pemFileInfo"]) -> 'PemFileInfoView': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["requestBinding"]) -> MetaOapg.properties.requestBinding: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["responseSignatureAlgorithm"]) -> MetaOapg.properties.responseSignatureAlgorithm: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ssoDebugEnabled"]) -> MetaOapg.properties.ssoDebugEnabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ssoUrl"]) -> MetaOapg.properties.ssoUrl: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["oktaIdpId", "acsUrl", "associatedDomains", "associatedOrgs", "audienceUri", "displayName", "issuerUri", "pemFileInfo", "requestBinding", "responseSignatureAlgorithm", "ssoDebugEnabled", "ssoUrl", "status", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["oktaIdpId"]) -> MetaOapg.properties.oktaIdpId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["acsUrl"]) -> typing.Union[MetaOapg.properties.acsUrl, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["associatedDomains"]) -> typing.Union[MetaOapg.properties.associatedDomains, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["associatedOrgs"]) -> typing.Union[MetaOapg.properties.associatedOrgs, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["audienceUri"]) -> typing.Union[MetaOapg.properties.audienceUri, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["displayName"]) -> typing.Union[MetaOapg.properties.displayName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["issuerUri"]) -> typing.Union[MetaOapg.properties.issuerUri, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pemFileInfo"]) -> typing.Union['PemFileInfoView', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["requestBinding"]) -> typing.Union[MetaOapg.properties.requestBinding, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["responseSignatureAlgorithm"]) -> typing.Union[MetaOapg.properties.responseSignatureAlgorithm, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ssoDebugEnabled"]) -> typing.Union[MetaOapg.properties.ssoDebugEnabled, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ssoUrl"]) -> typing.Union[MetaOapg.properties.ssoUrl, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["oktaIdpId", "acsUrl", "associatedDomains", "associatedOrgs", "audienceUri", "displayName", "issuerUri", "pemFileInfo", "requestBinding", "responseSignatureAlgorithm", "ssoDebugEnabled", "ssoUrl", "status", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        oktaIdpId: typing.Union[MetaOapg.properties.oktaIdpId, str, ],
        acsUrl: typing.Union[MetaOapg.properties.acsUrl, str, schemas.Unset] = schemas.unset,
        associatedDomains: typing.Union[MetaOapg.properties.associatedDomains, list, tuple, schemas.Unset] = schemas.unset,
        associatedOrgs: typing.Union[MetaOapg.properties.associatedOrgs, list, tuple, schemas.Unset] = schemas.unset,
        audienceUri: typing.Union[MetaOapg.properties.audienceUri, str, schemas.Unset] = schemas.unset,
        displayName: typing.Union[MetaOapg.properties.displayName, str, schemas.Unset] = schemas.unset,
        issuerUri: typing.Union[MetaOapg.properties.issuerUri, str, schemas.Unset] = schemas.unset,
        pemFileInfo: typing.Union['PemFileInfoView', schemas.Unset] = schemas.unset,
        requestBinding: typing.Union[MetaOapg.properties.requestBinding, str, schemas.Unset] = schemas.unset,
        responseSignatureAlgorithm: typing.Union[MetaOapg.properties.responseSignatureAlgorithm, str, schemas.Unset] = schemas.unset,
        ssoDebugEnabled: typing.Union[MetaOapg.properties.ssoDebugEnabled, bool, schemas.Unset] = schemas.unset,
        ssoUrl: typing.Union[MetaOapg.properties.ssoUrl, str, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'IdentityProviderView':
        return super().__new__(
            cls,
            *_args,
            oktaIdpId=oktaIdpId,
            acsUrl=acsUrl,
            associatedDomains=associatedDomains,
            associatedOrgs=associatedOrgs,
            audienceUri=audienceUri,
            displayName=displayName,
            issuerUri=issuerUri,
            pemFileInfo=pemFileInfo,
            requestBinding=requestBinding,
            responseSignatureAlgorithm=responseSignatureAlgorithm,
            ssoDebugEnabled=ssoDebugEnabled,
            ssoUrl=ssoUrl,
            status=status,
            _configuration=_configuration,
            **kwargs,
        )

from atlas.model.connected_org_config_view import ConnectedOrgConfigView
from atlas.model.pem_file_info_view import PemFileInfoView
