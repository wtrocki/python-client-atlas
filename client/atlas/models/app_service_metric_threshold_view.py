# coding: utf-8

"""
    MongoDB Atlas Administration API

    The MongoDB Atlas Administration API allows developers to manage all components in MongoDB Atlas. To learn more, review the [Administration API overview](https://www.mongodb.com/docs/atlas/api/atlas-admin-api/). This OpenAPI specification covers all of the collections with the exception of Alerts, Alert Configurations, and Events. Refer to the [legacy documentation](https://www.mongodb.com/docs/atlas/reference/api-resources/) for the specifications of these resources.  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import annotations
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401

from typing import Any, List, Optional
from pydantic import BaseModel, Field, StrictStr, ValidationError, validator
from atlas.models.data_metric_threshold_view import DataMetricThresholdView
from atlas.models.raw_metric_threshold_view import RawMetricThresholdView
from atlas.models.time_metric_threshold_view import TimeMetricThresholdView
from typing import Any, List
from pydantic import StrictStr, Field

APPSERVICEMETRICTHRESHOLDVIEW_ONE_OF_SCHEMAS = ["DataMetricThresholdView", "RawMetricThresholdView", "TimeMetricThresholdView"]

class AppServiceMetricThresholdView(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    # data type: RawMetricThresholdView
    oneof_schema_1_validator: Optional[RawMetricThresholdView] = None
    # data type: TimeMetricThresholdView
    oneof_schema_2_validator: Optional[TimeMetricThresholdView] = None
    # data type: DataMetricThresholdView
    oneof_schema_3_validator: Optional[DataMetricThresholdView] = None
    actual_instance: Any
    one_of_schemas: List[str] = Field(APPSERVICEMETRICTHRESHOLDVIEW_ONE_OF_SCHEMAS, const=True)

    class Config:
        validate_assignment = True

    discriminator_value_class_map = {
    }

    @validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = cls()
        error_messages = []
        match = 0
        # validate data type: RawMetricThresholdView
        if type(v) is not RawMetricThresholdView:
            error_messages.append(f"Error! Input type `{type(v)}` is not `RawMetricThresholdView`")
        else:
            match += 1

        # validate data type: TimeMetricThresholdView
        if type(v) is not TimeMetricThresholdView:
            error_messages.append(f"Error! Input type `{type(v)}` is not `TimeMetricThresholdView`")
        else:
            match += 1

        # validate data type: DataMetricThresholdView
        if type(v) is not DataMetricThresholdView:
            error_messages.append(f"Error! Input type `{type(v)}` is not `DataMetricThresholdView`")
        else:
            match += 1

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into AppServiceMetricThresholdView with oneOf schemas: DataMetricThresholdView, RawMetricThresholdView, TimeMetricThresholdView. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into AppServiceMetricThresholdView with oneOf schemas: DataMetricThresholdView, RawMetricThresholdView, TimeMetricThresholdView. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> AppServiceMetricThresholdView:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> AppServiceMetricThresholdView:
        """Returns the object represented by the json string"""
        instance = cls()
        error_messages = []
        match = 0

        # use oneOf discriminator to lookup the data type
        _data_type = json.loads(json_str).get("metricName")
        if not _data_type:
            raise ValueError("Failed to lookup data type from the field `metricName` in the input.")

        # check if data type is `DataMetricThresholdView`
        if _data_type == "DataMetricThresholdView":
            instance.actual_instance = DataMetricThresholdView.from_json(json_str)
            return instance

        # check if data type is `RawMetricThresholdView`
        if _data_type == "REALM_AUTH_LOGIN_FAIL":
            instance.actual_instance = RawMetricThresholdView.from_json(json_str)
            return instance

        # check if data type is `TimeMetricThresholdView`
        if _data_type == "REALM_ENDPOINTS_COMPUTE_MS":
            instance.actual_instance = TimeMetricThresholdView.from_json(json_str)
            return instance

        # check if data type is `DataMetricThresholdView`
        if _data_type == "REALM_ENDPOINTS_EGRESS_BYTES":
            instance.actual_instance = DataMetricThresholdView.from_json(json_str)
            return instance

        # check if data type is `RawMetricThresholdView`
        if _data_type == "REALM_ENDPOINTS_FAILED_REQUESTS":
            instance.actual_instance = RawMetricThresholdView.from_json(json_str)
            return instance

        # check if data type is `TimeMetricThresholdView`
        if _data_type == "REALM_ENDPOINTS_RESPONSE_MS":
            instance.actual_instance = TimeMetricThresholdView.from_json(json_str)
            return instance

        # check if data type is `TimeMetricThresholdView`
        if _data_type == "REALM_GQL_COMPUTE_MS":
            instance.actual_instance = TimeMetricThresholdView.from_json(json_str)
            return instance

        # check if data type is `DataMetricThresholdView`
        if _data_type == "REALM_GQL_EGRESS_BYTES":
            instance.actual_instance = DataMetricThresholdView.from_json(json_str)
            return instance

        # check if data type is `RawMetricThresholdView`
        if _data_type == "REALM_GQL_FAILED_REQUESTS":
            instance.actual_instance = RawMetricThresholdView.from_json(json_str)
            return instance

        # check if data type is `TimeMetricThresholdView`
        if _data_type == "REALM_GQL_RESPONSE_MS":
            instance.actual_instance = TimeMetricThresholdView.from_json(json_str)
            return instance

        # check if data type is `TimeMetricThresholdView`
        if _data_type == "REALM_OVERALL_COMPUTE_MS":
            instance.actual_instance = TimeMetricThresholdView.from_json(json_str)
            return instance

        # check if data type is `DataMetricThresholdView`
        if _data_type == "REALM_OVERALL_EGRESS_BYTES":
            instance.actual_instance = DataMetricThresholdView.from_json(json_str)
            return instance

        # check if data type is `RawMetricThresholdView`
        if _data_type == "REALM_OVERALL_FAILED_REQUESTS":
            instance.actual_instance = RawMetricThresholdView.from_json(json_str)
            return instance

        # check if data type is `RawMetricThresholdView`
        if _data_type == "REALM_SDKFNS_FAILED_REQUESTS":
            instance.actual_instance = RawMetricThresholdView.from_json(json_str)
            return instance

        # check if data type is `TimeMetricThresholdView`
        if _data_type == "REALM_SDK_FNS_RESPONSE_MS":
            instance.actual_instance = TimeMetricThresholdView.from_json(json_str)
            return instance

        # check if data type is `TimeMetricThresholdView`
        if _data_type == "REALM_SDK_FUNCTIONS_COMPUTE_MS":
            instance.actual_instance = TimeMetricThresholdView.from_json(json_str)
            return instance

        # check if data type is `DataMetricThresholdView`
        if _data_type == "REALM_SDK_FUNCTIONS_EGRESS_BYTES":
            instance.actual_instance = DataMetricThresholdView.from_json(json_str)
            return instance

        # check if data type is `TimeMetricThresholdView`
        if _data_type == "REALM_SDK_MQL_COMPUTE_MS":
            instance.actual_instance = TimeMetricThresholdView.from_json(json_str)
            return instance

        # check if data type is `DataMetricThresholdView`
        if _data_type == "REALM_SDK_MQL_EGRESS_BYTES":
            instance.actual_instance = DataMetricThresholdView.from_json(json_str)
            return instance

        # check if data type is `TimeMetricThresholdView`
        if _data_type == "REALM_SDK_MQL_RESPONSE_MS":
            instance.actual_instance = TimeMetricThresholdView.from_json(json_str)
            return instance

        # check if data type is `TimeMetricThresholdView`
        if _data_type == "REALM_SYNC_CURRENT_OPLOG_LAG_MS_SUM":
            instance.actual_instance = TimeMetricThresholdView.from_json(json_str)
            return instance

        # check if data type is `DataMetricThresholdView`
        if _data_type == "REALM_SYNC_EGRESS_BYTES":
            instance.actual_instance = DataMetricThresholdView.from_json(json_str)
            return instance

        # check if data type is `RawMetricThresholdView`
        if _data_type == "REALM_SYNC_NUM_UNSYNCABLE_DOCS_PERCENT":
            instance.actual_instance = RawMetricThresholdView.from_json(json_str)
            return instance

        # check if data type is `TimeMetricThresholdView`
        if _data_type == "REALM_TRIGGERS_COMPUTE_MS":
            instance.actual_instance = TimeMetricThresholdView.from_json(json_str)
            return instance

        # check if data type is `TimeMetricThresholdView`
        if _data_type == "REALM_TRIGGERS_CURRENT_OPLOG_LAG_MS_SUM":
            instance.actual_instance = TimeMetricThresholdView.from_json(json_str)
            return instance

        # check if data type is `DataMetricThresholdView`
        if _data_type == "REALM_TRIGGERS_EGRESS_BYTES":
            instance.actual_instance = DataMetricThresholdView.from_json(json_str)
            return instance

        # check if data type is `RawMetricThresholdView`
        if _data_type == "REALM_TRIGGERS_FAILED_REQUESTS":
            instance.actual_instance = RawMetricThresholdView.from_json(json_str)
            return instance

        # check if data type is `TimeMetricThresholdView`
        if _data_type == "REALM_TRIGGERS_RESPONSE_MS":
            instance.actual_instance = TimeMetricThresholdView.from_json(json_str)
            return instance

        # check if data type is `RawMetricThresholdView`
        if _data_type == "RawMetricThresholdView":
            instance.actual_instance = RawMetricThresholdView.from_json(json_str)
            return instance

        # check if data type is `TimeMetricThresholdView`
        if _data_type == "TimeMetricThresholdView":
            instance.actual_instance = TimeMetricThresholdView.from_json(json_str)
            return instance

        # deserialize data into RawMetricThresholdView
        try:
            instance.actual_instance = RawMetricThresholdView.from_json(json_str)
            match += 1
        except ValidationError as e:
            error_messages.append(str(e))
        # deserialize data into TimeMetricThresholdView
        try:
            instance.actual_instance = TimeMetricThresholdView.from_json(json_str)
            match += 1
        except ValidationError as e:
            error_messages.append(str(e))
        # deserialize data into DataMetricThresholdView
        try:
            instance.actual_instance = DataMetricThresholdView.from_json(json_str)
            match += 1
        except ValidationError as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into AppServiceMetricThresholdView with oneOf schemas: DataMetricThresholdView, RawMetricThresholdView, TimeMetricThresholdView. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into AppServiceMetricThresholdView with oneOf schemas: DataMetricThresholdView, RawMetricThresholdView, TimeMetricThresholdView. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is not None:
            return self.actual_instance.to_json()
        else:
            return "null"

    def to_dict(self) -> dict:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is not None:
            return self.actual_instance.to_dict()
        else:
            return dict()

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.dict())

