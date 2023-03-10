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

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, StrictStr, conlist, constr, validator
from atlas.models.cluster_outage_simulation_outage_filter import ClusterOutageSimulationOutageFilter

class ClusterOutageSimulation(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    cluster_name: Optional[constr(strict=True, max_length=64, min_length=1)] = Field(None, alias="clusterName", description="Human-readable label that identifies the cluster that undergoes outage simulation.")
    group_id: Optional[constr(strict=True, max_length=24, min_length=24)] = Field(None, alias="groupId", description="Unique 24-hexadecimal character string that identifies the project that contains the cluster to undergo outage simulation.")
    id: Optional[constr(strict=True, max_length=24, min_length=24)] = Field(None, description="Unique 24-hexadecimal character string that identifies the outage simulation.")
    outage_filters: Optional[conlist(ClusterOutageSimulationOutageFilter, min_items=1)] = Field(None, alias="outageFilters", description="List of settings that specify the type of cluster outage simulation.")
    start_request_date: Optional[datetime] = Field(None, alias="startRequestDate", description="Date and time when MongoDB Cloud started the regional outage simulation.")
    state: Optional[StrictStr] = Field(None, description="Phase of the outage simulation.  | State       | Indication | |-------------|------------| | `START_REQUESTED`    | User has requested cluster outage simulation.| | `STARTING`           | MongoDB Cloud is starting cluster outage simulation.| | `SIMULATING`         | MongoDB Cloud is simulating cluster outage.| | `RECOVERY_REQUESTED` | User has requested recovery from the simulated outage.| | `RECOVERING`         | MongoDB Cloud is recovering the cluster from the simulated outage.| | `COMPLETE`           | MongoDB Cloud has completed the cluster outage simulation.|")
    __properties = ["clusterName", "groupId", "id", "outageFilters", "startRequestDate", "state"]

    @validator('cluster_name')
    def cluster_name_validate_regular_expression(cls, v):
        if not re.match(r"^([a-zA-Z0-9]([a-zA-Z0-9-]){0,21}(?<!-)([\w]{0,42}))$", v):
            raise ValueError(r"must validate the regular expression /^([a-zA-Z0-9]([a-zA-Z0-9-]){0,21}(?<!-)([\w]{0,42}))$/")
        return v

    @validator('group_id')
    def group_id_validate_regular_expression(cls, v):
        if not re.match(r"^([a-f0-9]{24})$", v):
            raise ValueError(r"must validate the regular expression /^([a-f0-9]{24})$/")
        return v

    @validator('id')
    def id_validate_regular_expression(cls, v):
        if not re.match(r"^([a-f0-9]{24})$", v):
            raise ValueError(r"must validate the regular expression /^([a-f0-9]{24})$/")
        return v

    @validator('state')
    def state_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ('START_REQUESTED', 'STARTING', 'SIMULATING', 'RECOVERY_REQUESTED', 'RECOVERING', 'COMPLETE'):
            raise ValueError("must validate the enum values ('START_REQUESTED', 'STARTING', 'SIMULATING', 'RECOVERY_REQUESTED', 'RECOVERING', 'COMPLETE')")
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
    def from_json(cls, json_str: str) -> ClusterOutageSimulation:
        """Create an instance of ClusterOutageSimulation from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "cluster_name",
                            "group_id",
                            "id",
                            "start_request_date",
                            "state",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in outage_filters (list)
        _items = []
        if self.outage_filters:
            for _item in self.outage_filters:
                if _item:
                    _items.append(_item.to_dict())
            _dict['outageFilters'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ClusterOutageSimulation:
        """Create an instance of ClusterOutageSimulation from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return ClusterOutageSimulation.parse_obj(obj)

        _obj = ClusterOutageSimulation.parse_obj({
            "cluster_name": obj.get("clusterName"),
            "group_id": obj.get("groupId"),
            "id": obj.get("id"),
            "outage_filters": [ClusterOutageSimulationOutageFilter.from_dict(_item) for _item in obj.get("outageFilters")] if obj.get("outageFilters") is not None else None,
            "start_request_date": obj.get("startRequestDate"),
            "state": obj.get("state")
        })
        return _obj

