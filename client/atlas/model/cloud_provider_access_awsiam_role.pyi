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


class CloudProviderAccessAWSIAMRole(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Details that describe the features linked to the Amazon Web Services (AWS) Identity and Access Management (IAM) role.
    """


    class MetaOapg:
        required = {
            "providerName",
        }
        
        class properties:
            
            
            class providerName(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def AWS(cls):
                    return cls("AWS")
            
            
            class atlasAWSAccountArn(
                schemas.StrSchema
            ):
                pass
            atlasAssumedRoleExternalId = schemas.UUIDSchema
            authorizedDate = schemas.DateTimeSchema
            createdDate = schemas.DateTimeSchema
            
            
            class featureUsages(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['CloudProviderAccessFeatureUsage']:
                        return CloudProviderAccessFeatureUsage
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['CloudProviderAccessFeatureUsage'], typing.List['CloudProviderAccessFeatureUsage']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'featureUsages':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'CloudProviderAccessFeatureUsage':
                    return super().__getitem__(i)
            
            
            class iamAssumedRoleArn(
                schemas.StrSchema
            ):
                pass
            
            
            class roleId(
                schemas.StrSchema
            ):
                pass
            __annotations__ = {
                "providerName": providerName,
                "atlasAWSAccountArn": atlasAWSAccountArn,
                "atlasAssumedRoleExternalId": atlasAssumedRoleExternalId,
                "authorizedDate": authorizedDate,
                "createdDate": createdDate,
                "featureUsages": featureUsages,
                "iamAssumedRoleArn": iamAssumedRoleArn,
                "roleId": roleId,
            }
    
    providerName: MetaOapg.properties.providerName
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["providerName"]) -> MetaOapg.properties.providerName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["atlasAWSAccountArn"]) -> MetaOapg.properties.atlasAWSAccountArn: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["atlasAssumedRoleExternalId"]) -> MetaOapg.properties.atlasAssumedRoleExternalId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["authorizedDate"]) -> MetaOapg.properties.authorizedDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["createdDate"]) -> MetaOapg.properties.createdDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["featureUsages"]) -> MetaOapg.properties.featureUsages: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["iamAssumedRoleArn"]) -> MetaOapg.properties.iamAssumedRoleArn: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["roleId"]) -> MetaOapg.properties.roleId: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["providerName", "atlasAWSAccountArn", "atlasAssumedRoleExternalId", "authorizedDate", "createdDate", "featureUsages", "iamAssumedRoleArn", "roleId", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["providerName"]) -> MetaOapg.properties.providerName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["atlasAWSAccountArn"]) -> typing.Union[MetaOapg.properties.atlasAWSAccountArn, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["atlasAssumedRoleExternalId"]) -> typing.Union[MetaOapg.properties.atlasAssumedRoleExternalId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["authorizedDate"]) -> typing.Union[MetaOapg.properties.authorizedDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["createdDate"]) -> typing.Union[MetaOapg.properties.createdDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["featureUsages"]) -> typing.Union[MetaOapg.properties.featureUsages, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["iamAssumedRoleArn"]) -> typing.Union[MetaOapg.properties.iamAssumedRoleArn, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["roleId"]) -> typing.Union[MetaOapg.properties.roleId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["providerName", "atlasAWSAccountArn", "atlasAssumedRoleExternalId", "authorizedDate", "createdDate", "featureUsages", "iamAssumedRoleArn", "roleId", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        providerName: typing.Union[MetaOapg.properties.providerName, str, ],
        atlasAWSAccountArn: typing.Union[MetaOapg.properties.atlasAWSAccountArn, str, schemas.Unset] = schemas.unset,
        atlasAssumedRoleExternalId: typing.Union[MetaOapg.properties.atlasAssumedRoleExternalId, str, uuid.UUID, schemas.Unset] = schemas.unset,
        authorizedDate: typing.Union[MetaOapg.properties.authorizedDate, str, datetime, schemas.Unset] = schemas.unset,
        createdDate: typing.Union[MetaOapg.properties.createdDate, str, datetime, schemas.Unset] = schemas.unset,
        featureUsages: typing.Union[MetaOapg.properties.featureUsages, list, tuple, schemas.Unset] = schemas.unset,
        iamAssumedRoleArn: typing.Union[MetaOapg.properties.iamAssumedRoleArn, str, schemas.Unset] = schemas.unset,
        roleId: typing.Union[MetaOapg.properties.roleId, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CloudProviderAccessAWSIAMRole':
        return super().__new__(
            cls,
            *_args,
            providerName=providerName,
            atlasAWSAccountArn=atlasAWSAccountArn,
            atlasAssumedRoleExternalId=atlasAssumedRoleExternalId,
            authorizedDate=authorizedDate,
            createdDate=createdDate,
            featureUsages=featureUsages,
            iamAssumedRoleArn=iamAssumedRoleArn,
            roleId=roleId,
            _configuration=_configuration,
            **kwargs,
        )

from atlas.model.cloud_provider_access_feature_usage import CloudProviderAccessFeatureUsage