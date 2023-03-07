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


class Source(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Document that describes the source of the migration.
    """


    class MetaOapg:
        required = {
            "clusterName",
            "groupId",
            "ssl",
            "managedAuthentication",
        }
        
        class properties:
            clusterName = schemas.StrSchema
            
            
            class groupId(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 24
                    min_length = 24
                    regex=[{
                        'pattern': r'^([a-f0-9]{24})$',  # noqa: E501
                    }]
            managedAuthentication = schemas.BoolSchema
            ssl = schemas.BoolSchema
            caCertificatePath = schemas.StrSchema
            password = schemas.StrSchema
            username = schemas.StrSchema
            __annotations__ = {
                "clusterName": clusterName,
                "groupId": groupId,
                "managedAuthentication": managedAuthentication,
                "ssl": ssl,
                "caCertificatePath": caCertificatePath,
                "password": password,
                "username": username,
            }
    
    clusterName: MetaOapg.properties.clusterName
    groupId: MetaOapg.properties.groupId
    ssl: MetaOapg.properties.ssl
    managedAuthentication: MetaOapg.properties.managedAuthentication
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["clusterName"]) -> MetaOapg.properties.clusterName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["groupId"]) -> MetaOapg.properties.groupId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["managedAuthentication"]) -> MetaOapg.properties.managedAuthentication: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ssl"]) -> MetaOapg.properties.ssl: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["caCertificatePath"]) -> MetaOapg.properties.caCertificatePath: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["password"]) -> MetaOapg.properties.password: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["username"]) -> MetaOapg.properties.username: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["clusterName", "groupId", "managedAuthentication", "ssl", "caCertificatePath", "password", "username", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["clusterName"]) -> MetaOapg.properties.clusterName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["groupId"]) -> MetaOapg.properties.groupId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["managedAuthentication"]) -> MetaOapg.properties.managedAuthentication: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ssl"]) -> MetaOapg.properties.ssl: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["caCertificatePath"]) -> typing.Union[MetaOapg.properties.caCertificatePath, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["password"]) -> typing.Union[MetaOapg.properties.password, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["username"]) -> typing.Union[MetaOapg.properties.username, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["clusterName", "groupId", "managedAuthentication", "ssl", "caCertificatePath", "password", "username", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        clusterName: typing.Union[MetaOapg.properties.clusterName, str, ],
        groupId: typing.Union[MetaOapg.properties.groupId, str, ],
        ssl: typing.Union[MetaOapg.properties.ssl, bool, ],
        managedAuthentication: typing.Union[MetaOapg.properties.managedAuthentication, bool, ],
        caCertificatePath: typing.Union[MetaOapg.properties.caCertificatePath, str, schemas.Unset] = schemas.unset,
        password: typing.Union[MetaOapg.properties.password, str, schemas.Unset] = schemas.unset,
        username: typing.Union[MetaOapg.properties.username, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Source':
        return super().__new__(
            cls,
            *_args,
            clusterName=clusterName,
            groupId=groupId,
            ssl=ssl,
            managedAuthentication=managedAuthentication,
            caCertificatePath=caCertificatePath,
            password=password,
            username=username,
            _configuration=_configuration,
            **kwargs,
        )
