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


class DiskBackupSnapshotSchedule(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            autoExportEnabled = schemas.BoolSchema
            
            
            class clusterId(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 24
                    min_length = 24
                    regex=[{
                        'pattern': r'^([a-f0-9]{24})$',  # noqa: E501
                    }]
            
            
            class clusterName(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 64
                    min_length = 1
                    regex=[{
                        'pattern': r'^([a-zA-Z0-9]([a-zA-Z0-9-]){0,21}(?<!-)([\w]{0,42}))$',  # noqa: E501
                    }]
            
            
            class copySettings(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['DiskBackupCopySetting']:
                        return DiskBackupCopySetting
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['DiskBackupCopySetting'], typing.List['DiskBackupCopySetting']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'copySettings':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'DiskBackupCopySetting':
                    return super().__getitem__(i)
            
            
            class deleteCopiedBackups(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ApiDeleteCopiedBackupsView']:
                        return ApiDeleteCopiedBackupsView
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['ApiDeleteCopiedBackupsView'], typing.List['ApiDeleteCopiedBackupsView']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'deleteCopiedBackups':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ApiDeleteCopiedBackupsView':
                    return super().__getitem__(i)
        
            @staticmethod
            def export() -> typing.Type['AutoExportPolicyView']:
                return AutoExportPolicyView
            
            
            class links(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Link']:
                        return Link
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['Link'], typing.List['Link']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'links':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Link':
                    return super().__getitem__(i)
            nextSnapshot = schemas.DateTimeSchema
            
            
            class policies(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    max_items = 1
                    
                    @staticmethod
                    def items() -> typing.Type['ApiPolicyView']:
                        return ApiPolicyView
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['ApiPolicyView'], typing.List['ApiPolicyView']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'policies':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ApiPolicyView':
                    return super().__getitem__(i)
            referenceHourOfDay = schemas.Int32Schema
            referenceMinuteOfHour = schemas.Int32Schema
            restoreWindowDays = schemas.Int32Schema
            updateSnapshots = schemas.BoolSchema
            useOrgAndGroupNamesInExportPrefix = schemas.BoolSchema
            __annotations__ = {
                "autoExportEnabled": autoExportEnabled,
                "clusterId": clusterId,
                "clusterName": clusterName,
                "copySettings": copySettings,
                "deleteCopiedBackups": deleteCopiedBackups,
                "export": export,
                "links": links,
                "nextSnapshot": nextSnapshot,
                "policies": policies,
                "referenceHourOfDay": referenceHourOfDay,
                "referenceMinuteOfHour": referenceMinuteOfHour,
                "restoreWindowDays": restoreWindowDays,
                "updateSnapshots": updateSnapshots,
                "useOrgAndGroupNamesInExportPrefix": useOrgAndGroupNamesInExportPrefix,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["autoExportEnabled"]) -> MetaOapg.properties.autoExportEnabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["clusterId"]) -> MetaOapg.properties.clusterId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["clusterName"]) -> MetaOapg.properties.clusterName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["copySettings"]) -> MetaOapg.properties.copySettings: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["deleteCopiedBackups"]) -> MetaOapg.properties.deleteCopiedBackups: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["export"]) -> 'AutoExportPolicyView': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["links"]) -> MetaOapg.properties.links: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nextSnapshot"]) -> MetaOapg.properties.nextSnapshot: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["policies"]) -> MetaOapg.properties.policies: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["referenceHourOfDay"]) -> MetaOapg.properties.referenceHourOfDay: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["referenceMinuteOfHour"]) -> MetaOapg.properties.referenceMinuteOfHour: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["restoreWindowDays"]) -> MetaOapg.properties.restoreWindowDays: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updateSnapshots"]) -> MetaOapg.properties.updateSnapshots: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["useOrgAndGroupNamesInExportPrefix"]) -> MetaOapg.properties.useOrgAndGroupNamesInExportPrefix: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["autoExportEnabled", "clusterId", "clusterName", "copySettings", "deleteCopiedBackups", "export", "links", "nextSnapshot", "policies", "referenceHourOfDay", "referenceMinuteOfHour", "restoreWindowDays", "updateSnapshots", "useOrgAndGroupNamesInExportPrefix", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["autoExportEnabled"]) -> typing.Union[MetaOapg.properties.autoExportEnabled, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["clusterId"]) -> typing.Union[MetaOapg.properties.clusterId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["clusterName"]) -> typing.Union[MetaOapg.properties.clusterName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["copySettings"]) -> typing.Union[MetaOapg.properties.copySettings, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["deleteCopiedBackups"]) -> typing.Union[MetaOapg.properties.deleteCopiedBackups, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["export"]) -> typing.Union['AutoExportPolicyView', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["links"]) -> typing.Union[MetaOapg.properties.links, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nextSnapshot"]) -> typing.Union[MetaOapg.properties.nextSnapshot, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["policies"]) -> typing.Union[MetaOapg.properties.policies, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["referenceHourOfDay"]) -> typing.Union[MetaOapg.properties.referenceHourOfDay, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["referenceMinuteOfHour"]) -> typing.Union[MetaOapg.properties.referenceMinuteOfHour, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["restoreWindowDays"]) -> typing.Union[MetaOapg.properties.restoreWindowDays, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updateSnapshots"]) -> typing.Union[MetaOapg.properties.updateSnapshots, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["useOrgAndGroupNamesInExportPrefix"]) -> typing.Union[MetaOapg.properties.useOrgAndGroupNamesInExportPrefix, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["autoExportEnabled", "clusterId", "clusterName", "copySettings", "deleteCopiedBackups", "export", "links", "nextSnapshot", "policies", "referenceHourOfDay", "referenceMinuteOfHour", "restoreWindowDays", "updateSnapshots", "useOrgAndGroupNamesInExportPrefix", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        autoExportEnabled: typing.Union[MetaOapg.properties.autoExportEnabled, bool, schemas.Unset] = schemas.unset,
        clusterId: typing.Union[MetaOapg.properties.clusterId, str, schemas.Unset] = schemas.unset,
        clusterName: typing.Union[MetaOapg.properties.clusterName, str, schemas.Unset] = schemas.unset,
        copySettings: typing.Union[MetaOapg.properties.copySettings, list, tuple, schemas.Unset] = schemas.unset,
        deleteCopiedBackups: typing.Union[MetaOapg.properties.deleteCopiedBackups, list, tuple, schemas.Unset] = schemas.unset,
        export: typing.Union['AutoExportPolicyView', schemas.Unset] = schemas.unset,
        links: typing.Union[MetaOapg.properties.links, list, tuple, schemas.Unset] = schemas.unset,
        nextSnapshot: typing.Union[MetaOapg.properties.nextSnapshot, str, datetime, schemas.Unset] = schemas.unset,
        policies: typing.Union[MetaOapg.properties.policies, list, tuple, schemas.Unset] = schemas.unset,
        referenceHourOfDay: typing.Union[MetaOapg.properties.referenceHourOfDay, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        referenceMinuteOfHour: typing.Union[MetaOapg.properties.referenceMinuteOfHour, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        restoreWindowDays: typing.Union[MetaOapg.properties.restoreWindowDays, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        updateSnapshots: typing.Union[MetaOapg.properties.updateSnapshots, bool, schemas.Unset] = schemas.unset,
        useOrgAndGroupNamesInExportPrefix: typing.Union[MetaOapg.properties.useOrgAndGroupNamesInExportPrefix, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DiskBackupSnapshotSchedule':
        return super().__new__(
            cls,
            *_args,
            autoExportEnabled=autoExportEnabled,
            clusterId=clusterId,
            clusterName=clusterName,
            copySettings=copySettings,
            deleteCopiedBackups=deleteCopiedBackups,
            export=export,
            links=links,
            nextSnapshot=nextSnapshot,
            policies=policies,
            referenceHourOfDay=referenceHourOfDay,
            referenceMinuteOfHour=referenceMinuteOfHour,
            restoreWindowDays=restoreWindowDays,
            updateSnapshots=updateSnapshots,
            useOrgAndGroupNamesInExportPrefix=useOrgAndGroupNamesInExportPrefix,
            _configuration=_configuration,
            **kwargs,
        )

from atlas.model.api_delete_copied_backups_view import ApiDeleteCopiedBackupsView
from atlas.model.api_policy_view import ApiPolicyView
from atlas.model.auto_export_policy_view import AutoExportPolicyView
from atlas.model.disk_backup_copy_setting import DiskBackupCopySetting
from atlas.model.link import Link
