# coding: utf-8

"""
    MongoDB Atlas Administration API

    The MongoDB Atlas Administration API allows developers to manage all components in MongoDB Atlas. To learn more, review the [Administration API overview](https://www.mongodb.com/docs/atlas/api/atlas-admin-api/). This OpenAPI specification covers all of the collections with the exception of Alerts, Alert Configurations, and Events. Refer to the [legacy documentation](https://www.mongodb.com/docs/atlas/reference/api-resources/) for the specifications of these resources.  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr, conlist, constr, validator
from atlas.models.criteria_view import CriteriaView
from atlas.models.online_archive_schedule import OnlineArchiveSchedule
from atlas.models.partition_field_view import PartitionFieldView

class OnlineArchive(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    id: Optional[constr(strict=True, max_length=24, min_length=24)] = Field(None, alias="_id", description="Unique 24-hexadecimal digit string that identifies the online archive.")
    cluster_name: Optional[constr(strict=True, max_length=64, min_length=1)] = Field(None, alias="clusterName", description="Human-readable label that identifies the cluster that contains the collection for which you want to create an online archive.")
    coll_name: Optional[StrictStr] = Field(None, alias="collName", description="Human-readable label that identifies the collection for which you created the online archive.")
    collection_type: Optional[StrictStr] = Field('STANDARD', alias="collectionType", description="Classification of MongoDB database collection that you want to return.  If you set this parameter to `TIMESERIES`, set `\"criteria.type\" : \"date\"` and `\"criteria.dateFormat\" : \"ISODATE\"`.")
    criteria: CriteriaView = ...
    db_name: Optional[StrictStr] = Field(None, alias="dbName", description="Human-readable label of the database that contains the collection that contains the online archive.")
    group_id: Optional[constr(strict=True, max_length=24, min_length=24)] = Field(None, alias="groupId", description="Unique 24-hexadecimal digit string that identifies the project that contains the specified cluster. The specified cluster contains the collection for which to create the online archive.")
    partition_fields: Optional[conlist(PartitionFieldView, min_items=1)] = Field(None, alias="partitionFields", description="List that contains document parameters to use to logically divide data within a collection. Partitions provide a coarse level of filtering of the underlying collection data. To divide your data, specify up to two parameters that you frequently query. Any queries that don't use these parameters result in a full collection scan of all archived documents. This takes more time and increase your costs.")
    schedule: Optional[OnlineArchiveSchedule] = None
    state: Optional[StrictStr] = Field(None, description="Phase of the process to create this online archive when you made this request.  | State       | Indication | |-------------|------------| | `PENDING`   | MongoDB Cloud has queued documents for archive. Archiving hasn't started. | | `ARCHIVING` | MongoDB Cloud started archiving documents that meet the archival criteria. | | `IDLE`      | MongoDB Cloud waits to start the next archival job. | | `PAUSING`   | Someone chose to stop archiving. MongoDB Cloud finishes the running archival job then changes the state to `PAUSED` when that job completes. | | `PAUSED`    | MongoDB Cloud has stopped archiving. Archived documents can be queried. The specified archiving operation on the active cluster cannot archive additional documents. You can resume archiving for paused archives at any time. | | `ORPHANED`  | Someone has deleted the collection associated with an active or paused archive. MongoDB Cloud doesn't delete the archived data. You must manually delete the online archives associated with the deleted collection. | | `DELETED`   | Someone has deleted the archive was deleted. When someone deletes an online archive, MongoDB Cloud removes all associated archived documents from the cloud object storage. |")
    __properties = ["_id", "clusterName", "collName", "collectionType", "criteria", "dbName", "groupId", "partitionFields", "schedule", "state"]

    @validator('id')
    def id_validate_regular_expression(cls, v):
        if not re.match(r"^([a-f0-9]{24})$", v):
            raise ValueError(r"must validate the regular expression /^([a-f0-9]{24})$/")
        return v

    @validator('cluster_name')
    def cluster_name_validate_regular_expression(cls, v):
        if not re.match(r"^([a-zA-Z0-9]([a-zA-Z0-9-]){0,21}(?<!-)([\w]{0,42}))$", v):
            raise ValueError(r"must validate the regular expression /^([a-zA-Z0-9]([a-zA-Z0-9-]){0,21}(?<!-)([\w]{0,42}))$/")
        return v

    @validator('collection_type')
    def collection_type_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ('TIMESERIES', 'STANDARD'):
            raise ValueError("must validate the enum values ('TIMESERIES', 'STANDARD')")
        return v

    @validator('group_id')
    def group_id_validate_regular_expression(cls, v):
        if not re.match(r"^([a-f0-9]{24})$", v):
            raise ValueError(r"must validate the regular expression /^([a-f0-9]{24})$/")
        return v

    @validator('state')
    def state_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ('PENDING', 'ACTIVE', 'PAUSING', 'PAUSED', 'DELETED', 'ORPHANED'):
            raise ValueError("must validate the enum values ('PENDING', 'ACTIVE', 'PAUSING', 'PAUSED', 'DELETED', 'ORPHANED')")
        return v

    class Config:
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> OnlineArchive:
        """Create an instance of OnlineArchive from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "id",
                            "cluster_name",
                            "group_id",
                            "state",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of criteria
        if self.criteria:
            _dict['criteria'] = self.criteria.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in partition_fields (list)
        _items = []
        if self.partition_fields:
            for _item in self.partition_fields:
                if _item:
                    _items.append(_item.to_dict())
            _dict['partitionFields'] = _items
        # override the default output from pydantic by calling `to_dict()` of schedule
        if self.schedule:
            _dict['schedule'] = self.schedule.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OnlineArchive:
        """Create an instance of OnlineArchive from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return OnlineArchive.parse_obj(obj)

        _obj = OnlineArchive.parse_obj({
            "id": obj.get("_id"),
            "cluster_name": obj.get("clusterName"),
            "coll_name": obj.get("collName"),
            "collection_type": obj.get("collectionType") if obj.get("collectionType") is not None else 'STANDARD',
            "criteria": CriteriaView.from_dict(obj.get("criteria")) if obj.get("criteria") is not None else None,
            "db_name": obj.get("dbName"),
            "group_id": obj.get("groupId"),
            "partition_fields": [PartitionFieldView.from_dict(_item) for _item in obj.get("partitionFields")] if obj.get("partitionFields") is not None else None,
            "schedule": OnlineArchiveSchedule.from_dict(obj.get("schedule")) if obj.get("schedule") is not None else None,
            "state": obj.get("state")
        })
        return _obj

