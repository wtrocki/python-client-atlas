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


class ApiMeasurementsGeneralViewAtlas(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            databaseName = schemas.StrSchema
            end = schemas.DateTimeSchema
            
            
            class granularity(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "PT1M": "PT1M",
                        "PT5M": "PT5M",
                        "PT1H": "PT1H",
                        "P1D": "P1D",
                    }
                
                @schemas.classproperty
                def PT1M(cls):
                    return cls("PT1M")
                
                @schemas.classproperty
                def PT5M(cls):
                    return cls("PT5M")
                
                @schemas.classproperty
                def PT1H(cls):
                    return cls("PT1H")
                
                @schemas.classproperty
                def P1D(cls):
                    return cls("P1D")
            
            
            class groupId(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 24
                    min_length = 24
                    regex=[{
                        'pattern': r'^([a-f0-9]{24})$',  # noqa: E501
                    }]
            
            
            class hostId(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    regex=[{
                        'pattern': r'^([0-9]{1,3}\.){3}[0-9]{1,3}|([0-9a-f]{1,4}\:){7}([0-9a-f]{1,4})|(([a-z0-9]+\.){1,10}[a-z]+)?(\:[0-9]{4,5})$',  # noqa: E501
                    }]
            
            
            class links(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['LinkAtlas']:
                        return LinkAtlas
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['LinkAtlas'], typing.List['LinkAtlas']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'links':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'LinkAtlas':
                    return super().__getitem__(i)
            
            
            class measurements(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ApiMeasurementViewAtlas']:
                        return ApiMeasurementViewAtlas
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['ApiMeasurementViewAtlas'], typing.List['ApiMeasurementViewAtlas']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'measurements':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ApiMeasurementViewAtlas':
                    return super().__getitem__(i)
            partitionName = schemas.StrSchema
            
            
            class processId(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    regex=[{
                        'pattern': r'^([0-9]{1,3}\.){3}[0-9]{1,3}|([0-9a-f]{1,4}\:){7}([0-9a-f]{1,4})|(([a-z0-9]+\.){1,10}[a-z]+)?(\:[0-9]{4,5})$',  # noqa: E501
                    }]
            start = schemas.DateTimeSchema
            __annotations__ = {
                "databaseName": databaseName,
                "end": end,
                "granularity": granularity,
                "groupId": groupId,
                "hostId": hostId,
                "links": links,
                "measurements": measurements,
                "partitionName": partitionName,
                "processId": processId,
                "start": start,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["databaseName"]) -> MetaOapg.properties.databaseName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["end"]) -> MetaOapg.properties.end: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["granularity"]) -> MetaOapg.properties.granularity: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["groupId"]) -> MetaOapg.properties.groupId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hostId"]) -> MetaOapg.properties.hostId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["links"]) -> MetaOapg.properties.links: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["measurements"]) -> MetaOapg.properties.measurements: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["partitionName"]) -> MetaOapg.properties.partitionName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["processId"]) -> MetaOapg.properties.processId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["start"]) -> MetaOapg.properties.start: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["databaseName", "end", "granularity", "groupId", "hostId", "links", "measurements", "partitionName", "processId", "start", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["databaseName"]) -> typing.Union[MetaOapg.properties.databaseName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["end"]) -> typing.Union[MetaOapg.properties.end, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["granularity"]) -> typing.Union[MetaOapg.properties.granularity, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["groupId"]) -> typing.Union[MetaOapg.properties.groupId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hostId"]) -> typing.Union[MetaOapg.properties.hostId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["links"]) -> typing.Union[MetaOapg.properties.links, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["measurements"]) -> typing.Union[MetaOapg.properties.measurements, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["partitionName"]) -> typing.Union[MetaOapg.properties.partitionName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["processId"]) -> typing.Union[MetaOapg.properties.processId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["start"]) -> typing.Union[MetaOapg.properties.start, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["databaseName", "end", "granularity", "groupId", "hostId", "links", "measurements", "partitionName", "processId", "start", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        databaseName: typing.Union[MetaOapg.properties.databaseName, str, schemas.Unset] = schemas.unset,
        end: typing.Union[MetaOapg.properties.end, str, datetime, schemas.Unset] = schemas.unset,
        granularity: typing.Union[MetaOapg.properties.granularity, str, schemas.Unset] = schemas.unset,
        groupId: typing.Union[MetaOapg.properties.groupId, str, schemas.Unset] = schemas.unset,
        hostId: typing.Union[MetaOapg.properties.hostId, str, schemas.Unset] = schemas.unset,
        links: typing.Union[MetaOapg.properties.links, list, tuple, schemas.Unset] = schemas.unset,
        measurements: typing.Union[MetaOapg.properties.measurements, list, tuple, schemas.Unset] = schemas.unset,
        partitionName: typing.Union[MetaOapg.properties.partitionName, str, schemas.Unset] = schemas.unset,
        processId: typing.Union[MetaOapg.properties.processId, str, schemas.Unset] = schemas.unset,
        start: typing.Union[MetaOapg.properties.start, str, datetime, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ApiMeasurementsGeneralViewAtlas':
        return super().__new__(
            cls,
            *_args,
            databaseName=databaseName,
            end=end,
            granularity=granularity,
            groupId=groupId,
            hostId=hostId,
            links=links,
            measurements=measurements,
            partitionName=partitionName,
            processId=processId,
            start=start,
            _configuration=_configuration,
            **kwargs,
        )

from atlas.model.api_measurement_view_atlas import ApiMeasurementViewAtlas
from atlas.model.link_atlas import LinkAtlas