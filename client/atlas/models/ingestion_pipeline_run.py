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
from pydantic import BaseModel, Field, StrictStr, constr, validator
from atlas.models.pipeline_run_stats import PipelineRunStats

class IngestionPipelineRun(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    id: Optional[constr(strict=True, max_length=24, min_length=24)] = Field(None, alias="_id", description="Unique 24-hexadecimal character string that identifies a Data Lake Pipeline run.")
    backup_frequency_type: Optional[StrictStr] = Field(None, alias="backupFrequencyType", description="Backup schedule interval of the Data Lake Pipeline.")
    created_date: Optional[datetime] = Field(None, alias="createdDate", description="Timestamp that indicates when the pipeline run was created.")
    dataset_name: Optional[StrictStr] = Field(None, alias="datasetName", description="Human-readable label that identifies the dataset that Atlas generates during this pipeline run. You can use this dataset as a `dataSource` in a Federated Database collection.")
    group_id: Optional[constr(strict=True, max_length=24, min_length=24)] = Field(None, alias="groupId", description="Unique 24-hexadecimal character string that identifies the project.")
    last_updated_date: Optional[datetime] = Field(None, alias="lastUpdatedDate", description="Timestamp that indicates the last time that the pipeline run was updated.")
    phase: Optional[StrictStr] = Field(None, description="Processing phase of the Data Lake Pipeline.")
    pipeline_id: Optional[constr(strict=True, max_length=24, min_length=24)] = Field(None, alias="pipelineId", description="Unique 24-hexadecimal character string that identifies a Data Lake Pipeline.")
    snapshot_id: Optional[constr(strict=True, max_length=24, min_length=24)] = Field(None, alias="snapshotId", description="Unique 24-hexadecimal character string that identifies the snapshot of a cluster.")
    state: Optional[StrictStr] = Field(None, description="State of the pipeline run.")
    stats: Optional[PipelineRunStats] = None
    __properties = ["_id", "backupFrequencyType", "createdDate", "datasetName", "groupId", "lastUpdatedDate", "phase", "pipelineId", "snapshotId", "state", "stats"]

    @validator('id')
    def id_validate_regular_expression(cls, v):
        if not re.match(r"^([a-f0-9]{24})$", v):
            raise ValueError(r"must validate the regular expression /^([a-f0-9]{24})$/")
        return v

    @validator('backup_frequency_type')
    def backup_frequency_type_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ('HOURLY', 'DAILY', 'WEEKLY', 'MONTHLY', 'ON_DEMAND'):
            raise ValueError("must validate the enum values ('HOURLY', 'DAILY', 'WEEKLY', 'MONTHLY', 'ON_DEMAND')")
        return v

    @validator('group_id')
    def group_id_validate_regular_expression(cls, v):
        if not re.match(r"^([a-f0-9]{24})$", v):
            raise ValueError(r"must validate the regular expression /^([a-f0-9]{24})$/")
        return v

    @validator('phase')
    def phase_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ('SNAPSHOT', 'EXPORT', 'INGESTION'):
            raise ValueError("must validate the enum values ('SNAPSHOT', 'EXPORT', 'INGESTION')")
        return v

    @validator('pipeline_id')
    def pipeline_id_validate_regular_expression(cls, v):
        if not re.match(r"^([a-f0-9]{24})$", v):
            raise ValueError(r"must validate the regular expression /^([a-f0-9]{24})$/")
        return v

    @validator('snapshot_id')
    def snapshot_id_validate_regular_expression(cls, v):
        if not re.match(r"^([a-f0-9]{24})$", v):
            raise ValueError(r"must validate the regular expression /^([a-f0-9]{24})$/")
        return v

    @validator('state')
    def state_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ('PENDING', 'IN_PROGRESS', 'DONE', 'FAILED', 'DATASET_DELETED'):
            raise ValueError("must validate the enum values ('PENDING', 'IN_PROGRESS', 'DONE', 'FAILED', 'DATASET_DELETED')")
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
    def from_json(cls, json_str: str) -> IngestionPipelineRun:
        """Create an instance of IngestionPipelineRun from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "id",
                            "backup_frequency_type",
                            "created_date",
                            "dataset_name",
                            "group_id",
                            "last_updated_date",
                            "phase",
                            "pipeline_id",
                            "snapshot_id",
                            "state",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of stats
        if self.stats:
            _dict['stats'] = self.stats.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> IngestionPipelineRun:
        """Create an instance of IngestionPipelineRun from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return IngestionPipelineRun.parse_obj(obj)

        _obj = IngestionPipelineRun.parse_obj({
            "id": obj.get("_id"),
            "backup_frequency_type": obj.get("backupFrequencyType"),
            "created_date": obj.get("createdDate"),
            "dataset_name": obj.get("datasetName"),
            "group_id": obj.get("groupId"),
            "last_updated_date": obj.get("lastUpdatedDate"),
            "phase": obj.get("phase"),
            "pipeline_id": obj.get("pipelineId"),
            "snapshot_id": obj.get("snapshotId"),
            "state": obj.get("state"),
            "stats": PipelineRunStats.from_dict(obj.get("stats")) if obj.get("stats") is not None else None
        })
        return _obj

