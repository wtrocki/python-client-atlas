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


class ApiNewRelicView(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Details to integrate one New Relic account with one MongoDB Cloud project.

***IMPORTANT**: Effective Wednesday, June 16th, 2021, New Relic no longer supports the plugin-based integration with MongoDB. We do not recommend that you sign up for the plugin-based integration.

To learn more, see the <a href="https://discuss.newrelic.com/t/new-relic-plugin-eol-wednesday-june-16th-2021/127267" target="_blank">New Relic Plugin EOL Statement</a>. Consider configuring an alternative monitoring integration before June 16th to maintain visibility into your MongoDB deployments.
    """


    class MetaOapg:
        required = {
            "accountId",
            "licenseKey",
            "writeToken",
            "readToken",
        }
        
        class properties:
            
            
            class accountId(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 40
                    min_length = 40
                    regex=[{
                        'pattern': r'^([0-9a-f]){40}$',  # noqa: E501
                    }]
            
            
            class licenseKey(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 40
                    min_length = 40
                    regex=[{
                        'pattern': r'^([0-9a-f]){40}$',  # noqa: E501
                    }]
            readToken = schemas.StrSchema
            writeToken = schemas.StrSchema
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "NEW_RELIC": "NEW_RELIC",
                    }
                
                @schemas.classproperty
                def NEW_RELIC(cls):
                    return cls("NEW_RELIC")
            __annotations__ = {
                "accountId": accountId,
                "licenseKey": licenseKey,
                "readToken": readToken,
                "writeToken": writeToken,
                "type": type,
            }
    
    accountId: MetaOapg.properties.accountId
    licenseKey: MetaOapg.properties.licenseKey
    writeToken: MetaOapg.properties.writeToken
    readToken: MetaOapg.properties.readToken
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accountId"]) -> MetaOapg.properties.accountId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["licenseKey"]) -> MetaOapg.properties.licenseKey: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["readToken"]) -> MetaOapg.properties.readToken: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["writeToken"]) -> MetaOapg.properties.writeToken: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["accountId", "licenseKey", "readToken", "writeToken", "type", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accountId"]) -> MetaOapg.properties.accountId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["licenseKey"]) -> MetaOapg.properties.licenseKey: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["readToken"]) -> MetaOapg.properties.readToken: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["writeToken"]) -> MetaOapg.properties.writeToken: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["accountId", "licenseKey", "readToken", "writeToken", "type", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        accountId: typing.Union[MetaOapg.properties.accountId, str, ],
        licenseKey: typing.Union[MetaOapg.properties.licenseKey, str, ],
        writeToken: typing.Union[MetaOapg.properties.writeToken, str, ],
        readToken: typing.Union[MetaOapg.properties.readToken, str, ],
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ApiNewRelicView':
        return super().__new__(
            cls,
            *_args,
            accountId=accountId,
            licenseKey=licenseKey,
            writeToken=writeToken,
            readToken=readToken,
            type=type,
            _configuration=_configuration,
            **kwargs,
        )
