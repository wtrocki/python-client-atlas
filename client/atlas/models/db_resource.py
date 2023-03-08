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



from pydantic import BaseModel, Field, StrictBool, StrictStr

class DBResource(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    cluster: StrictBool = Field(..., description="Flag that indicates whether to grant the action on the cluster resource. If `true`, MongoDB Cloud ignores the **actions.resources.collection** and **actions.resources.db** parameters.")
    collection: StrictStr = Field(..., description="Human-readable label that identifies the collection on which you grant the action to one MongoDB user. If you don't set this parameter, you grant the action to all collections in the database specified in the **actions.resources.db** parameter. If you set `\"actions.resources.cluster\" : true`, MongoDB Cloud ignores this parameter.")
    db: StrictStr = Field(..., description="Human-readable label that identifies the database on which you grant the action to one MongoDB user. If you set `\"actions.resources.cluster\" : true`, MongoDB Cloud ignores this parameter.")
    __properties = ["cluster", "collection", "db"]

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
    def from_json(cls, json_str: str) -> DBResource:
        """Create an instance of DBResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DBResource:
        """Create an instance of DBResource from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return DBResource.parse_obj(obj)

        _obj = DBResource.parse_obj({
            "cluster": obj.get("cluster"),
            "collection": obj.get("collection"),
            "db": obj.get("db")
        })
        return _obj

