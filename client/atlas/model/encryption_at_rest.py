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


class EncryptionAtRest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def awsKms() -> typing.Type['AWSKMS']:
                return AWSKMS
        
            @staticmethod
            def azureKeyVault() -> typing.Type['AzureKeyVault']:
                return AzureKeyVault
        
            @staticmethod
            def googleCloudKms() -> typing.Type['GoogleCloudKMS']:
                return GoogleCloudKMS
            __annotations__ = {
                "awsKms": awsKms,
                "azureKeyVault": azureKeyVault,
                "googleCloudKms": googleCloudKms,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["awsKms"]) -> 'AWSKMS': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["azureKeyVault"]) -> 'AzureKeyVault': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["googleCloudKms"]) -> 'GoogleCloudKMS': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["awsKms", "azureKeyVault", "googleCloudKms", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["awsKms"]) -> typing.Union['AWSKMS', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["azureKeyVault"]) -> typing.Union['AzureKeyVault', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["googleCloudKms"]) -> typing.Union['GoogleCloudKMS', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["awsKms", "azureKeyVault", "googleCloudKms", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        awsKms: typing.Union['AWSKMS', schemas.Unset] = schemas.unset,
        azureKeyVault: typing.Union['AzureKeyVault', schemas.Unset] = schemas.unset,
        googleCloudKms: typing.Union['GoogleCloudKMS', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EncryptionAtRest':
        return super().__new__(
            cls,
            *_args,
            awsKms=awsKms,
            azureKeyVault=azureKeyVault,
            googleCloudKms=googleCloudKms,
            _configuration=_configuration,
            **kwargs,
        )

from atlas.model.awskms import AWSKMS
from atlas.model.azure_key_vault import AzureKeyVault
from atlas.model.google_cloud_kms import GoogleCloudKMS
