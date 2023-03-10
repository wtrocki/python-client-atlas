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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictInt, constr, validator
from atlas.models.link import Link

class SnapshotSchedule(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    cluster_checkpoint_interval_min: StrictInt = Field(..., alias="clusterCheckpointIntervalMin", description="Quantity of time expressed in minutes between successive cluster checkpoints. This parameter applies only to sharded clusters. This number determines the granularity of continuous cloud backups for sharded clusters.")
    cluster_id: constr(strict=True, max_length=24, min_length=24) = Field(..., alias="clusterId", description="Unique 24-hexadecimal digit string that identifies the cluster with the snapshot you want to return.")
    daily_snapshot_retention_days: StrictInt = Field(..., alias="dailySnapshotRetentionDays", description="Quantity of time to keep daily snapshots. MongoDB Cloud expresses this value in days. Set this value to `0` to disable daily snapshot retention.")
    group_id: constr(strict=True, max_length=24, min_length=24) = Field(..., alias="groupId", description="Unique 24-hexadecimal digit string that identifies the project that contains the cluster.")
    links: Optional[List[Link]] = Field(None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    monthly_snapshot_retention_months: StrictInt = Field(..., alias="monthlySnapshotRetentionMonths", description="Number of months that MongoDB Cloud must keep monthly snapshots. Set this value to `0` to disable monthly snapshot retention.")
    point_in_time_window_hours: StrictInt = Field(..., alias="pointInTimeWindowHours", description="Number of hours before the current time from which MongoDB Cloud can create a Continuous Cloud Backup snapshot.")
    snapshot_interval_hours: StrictInt = Field(..., alias="snapshotIntervalHours", description="Number of hours that must elapse before taking another snapshot.")
    snapshot_retention_days: StrictInt = Field(..., alias="snapshotRetentionDays", description="Number of days that MongoDB Cloud must keep recent snapshots.")
    weekly_snapshot_retention_weeks: StrictInt = Field(..., alias="weeklySnapshotRetentionWeeks", description="Number of weeks that MongoDB Cloud must keep weekly snapshots. Set this value to `0` to disable weekly snapshot retention.")
    __properties = ["clusterCheckpointIntervalMin", "clusterId", "dailySnapshotRetentionDays", "groupId", "links", "monthlySnapshotRetentionMonths", "pointInTimeWindowHours", "snapshotIntervalHours", "snapshotRetentionDays", "weeklySnapshotRetentionWeeks"]

    @validator('cluster_checkpoint_interval_min')
    def cluster_checkpoint_interval_min_validate_enum(cls, v):
        if v not in (15, 30, 60):
            raise ValueError("must validate the enum values (15, 30, 60)")
        return v

    @validator('cluster_id')
    def cluster_id_validate_regular_expression(cls, v):
        if not re.match(r"^([a-f0-9]{24})$", v):
            raise ValueError(r"must validate the regular expression /^([a-f0-9]{24})$/")
        return v

    @validator('daily_snapshot_retention_days')
    def daily_snapshot_retention_days_validate_enum(cls, v):
        if v not in (0, 3, 4, 5, 6, 7, 15, 30, 60, 90, 120, 180, 360):
            raise ValueError("must validate the enum values (0, 3, 4, 5, 6, 7, 15, 30, 60, 90, 120, 180, 360)")
        return v

    @validator('group_id')
    def group_id_validate_regular_expression(cls, v):
        if not re.match(r"^([a-f0-9]{24})$", v):
            raise ValueError(r"must validate the regular expression /^([a-f0-9]{24})$/")
        return v

    @validator('monthly_snapshot_retention_months')
    def monthly_snapshot_retention_months_validate_enum(cls, v):
        if v not in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 18, 24, 36):
            raise ValueError("must validate the enum values (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 18, 24, 36)")
        return v

    @validator('snapshot_interval_hours')
    def snapshot_interval_hours_validate_enum(cls, v):
        if v not in (6, 8, 12, 24):
            raise ValueError("must validate the enum values (6, 8, 12, 24)")
        return v

    @validator('snapshot_retention_days')
    def snapshot_retention_days_validate_enum(cls, v):
        if v not in (2, 3, 4, 5):
            raise ValueError("must validate the enum values (2, 3, 4, 5)")
        return v

    @validator('weekly_snapshot_retention_weeks')
    def weekly_snapshot_retention_weeks_validate_enum(cls, v):
        if v not in (0, 1, 2, 3, 4, 5, 6, 7, 8, 12, 16, 20, 24, 52):
            raise ValueError("must validate the enum values (0, 1, 2, 3, 4, 5, 6, 7, 8, 12, 16, 20, 24, 52)")
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
    def from_json(cls, json_str: str) -> SnapshotSchedule:
        """Create an instance of SnapshotSchedule from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "group_id",
                            "links",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in links (list)
        _items = []
        if self.links:
            for _item in self.links:
                if _item:
                    _items.append(_item.to_dict())
            _dict['links'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SnapshotSchedule:
        """Create an instance of SnapshotSchedule from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return SnapshotSchedule.parse_obj(obj)

        _obj = SnapshotSchedule.parse_obj({
            "cluster_checkpoint_interval_min": obj.get("clusterCheckpointIntervalMin"),
            "cluster_id": obj.get("clusterId"),
            "daily_snapshot_retention_days": obj.get("dailySnapshotRetentionDays"),
            "group_id": obj.get("groupId"),
            "links": [Link.from_dict(_item) for _item in obj.get("links")] if obj.get("links") is not None else None,
            "monthly_snapshot_retention_months": obj.get("monthlySnapshotRetentionMonths"),
            "point_in_time_window_hours": obj.get("pointInTimeWindowHours"),
            "snapshot_interval_hours": obj.get("snapshotIntervalHours"),
            "snapshot_retention_days": obj.get("snapshotRetentionDays"),
            "weekly_snapshot_retention_weeks": obj.get("weeklySnapshotRetentionWeeks")
        })
        return _obj

