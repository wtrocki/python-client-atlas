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


class CreateGCPEndpointGroupRequest(
    schemas.ComposedBase,
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Group of Private Endpoint settings.
    """


    class MetaOapg:
        
        
        class all_of_1(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                
                class properties:
                    endpointGroupName = schemas.StrSchema
                    
                    
                    class endpoints(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            @staticmethod
                            def items() -> typing.Type['CreateGCPForwardingRuleRequest']:
                                return CreateGCPForwardingRuleRequest
                    
                        def __new__(
                            cls,
                            _arg: typing.Union[typing.Tuple['CreateGCPForwardingRuleRequest'], typing.List['CreateGCPForwardingRuleRequest']],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'endpoints':
                            return super().__new__(
                                cls,
                                _arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> 'CreateGCPForwardingRuleRequest':
                            return super().__getitem__(i)
                    
                    
                    class gcpProjectId(
                        schemas.StrSchema
                    ):
                        pass
                    __annotations__ = {
                        "endpointGroupName": endpointGroupName,
                        "endpoints": endpoints,
                        "gcpProjectId": gcpProjectId,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["endpointGroupName"]) -> MetaOapg.properties.endpointGroupName: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["endpoints"]) -> MetaOapg.properties.endpoints: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["gcpProjectId"]) -> MetaOapg.properties.gcpProjectId: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["endpointGroupName", "endpoints", "gcpProjectId", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["endpointGroupName"]) -> typing.Union[MetaOapg.properties.endpointGroupName, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["endpoints"]) -> typing.Union[MetaOapg.properties.endpoints, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["gcpProjectId"]) -> typing.Union[MetaOapg.properties.gcpProjectId, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["endpointGroupName", "endpoints", "gcpProjectId", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *_args: typing.Union[dict, frozendict.frozendict, ],
                endpointGroupName: typing.Union[MetaOapg.properties.endpointGroupName, str, schemas.Unset] = schemas.unset,
                endpoints: typing.Union[MetaOapg.properties.endpoints, list, tuple, schemas.Unset] = schemas.unset,
                gcpProjectId: typing.Union[MetaOapg.properties.gcpProjectId, str, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_1':
                return super().__new__(
                    cls,
                    *_args,
                    endpointGroupName=endpointGroupName,
                    endpoints=endpoints,
                    gcpProjectId=gcpProjectId,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        @classmethod
        @functools.lru_cache()
        def all_of(cls):
            # we need this here to make our import statements work
            # we must store _composed_schemas in here so the code is only run
            # when we invoke this method. If we kept this at the class
            # level we would get an error because the class level
            # code would be run when this module is imported, and these composed
            # classes don't exist yet because their module has not finished
            # loading
            return [
                CreateEndpointRequest,
                cls.all_of_1,
            ]


    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CreateGCPEndpointGroupRequest':
        return super().__new__(
            cls,
            *_args,
            _configuration=_configuration,
            **kwargs,
        )

from atlas.model.create_endpoint_request import CreateEndpointRequest
from atlas.model.create_gcp_forwarding_rule_request import CreateGCPForwardingRuleRequest
