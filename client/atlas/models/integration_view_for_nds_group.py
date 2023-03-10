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
from atlas.models.api_datadog_view import ApiDatadogView
from atlas.models.api_microsoft_teams_view import ApiMicrosoftTeamsView
from atlas.models.api_new_relic_view import ApiNewRelicView
from atlas.models.api_ops_genie_view import ApiOpsGenieView
from atlas.models.api_pager_duty_view import ApiPagerDutyView
from atlas.models.api_prometheus_view import ApiPrometheusView
from atlas.models.api_slack_view import ApiSlackView
from atlas.models.api_victor_ops_view import ApiVictorOpsView
from atlas.models.api_webhook_view import ApiWebhookView
from typing import Any, List
from pydantic import StrictStr, Field

INTEGRATIONVIEWFORNDSGROUP_ONE_OF_SCHEMAS = ["ApiDatadogView", "ApiMicrosoftTeamsView", "ApiNewRelicView", "ApiOpsGenieView", "ApiPagerDutyView", "ApiPrometheusView", "ApiSlackView", "ApiVictorOpsView", "ApiWebhookView"]

class IntegrationViewForNdsGroup(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    # data type: ApiDatadogView
    oneof_schema_1_validator: Optional[ApiDatadogView] = None
    # data type: ApiMicrosoftTeamsView
    oneof_schema_2_validator: Optional[ApiMicrosoftTeamsView] = None
    # data type: ApiNewRelicView
    oneof_schema_3_validator: Optional[ApiNewRelicView] = None
    # data type: ApiOpsGenieView
    oneof_schema_4_validator: Optional[ApiOpsGenieView] = None
    # data type: ApiPagerDutyView
    oneof_schema_5_validator: Optional[ApiPagerDutyView] = None
    # data type: ApiPrometheusView
    oneof_schema_6_validator: Optional[ApiPrometheusView] = None
    # data type: ApiSlackView
    oneof_schema_7_validator: Optional[ApiSlackView] = None
    # data type: ApiVictorOpsView
    oneof_schema_8_validator: Optional[ApiVictorOpsView] = None
    # data type: ApiWebhookView
    oneof_schema_9_validator: Optional[ApiWebhookView] = None
    actual_instance: Any
    one_of_schemas: List[str] = Field(INTEGRATIONVIEWFORNDSGROUP_ONE_OF_SCHEMAS, const=True)

    class Config:
        validate_assignment = True

    @validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = cls()
        error_messages = []
        match = 0
        # validate data type: ApiDatadogView
        if type(v) is not ApiDatadogView:
            error_messages.append(f"Error! Input type `{type(v)}` is not `ApiDatadogView`")
        else:
            match += 1

        # validate data type: ApiMicrosoftTeamsView
        if type(v) is not ApiMicrosoftTeamsView:
            error_messages.append(f"Error! Input type `{type(v)}` is not `ApiMicrosoftTeamsView`")
        else:
            match += 1

        # validate data type: ApiNewRelicView
        if type(v) is not ApiNewRelicView:
            error_messages.append(f"Error! Input type `{type(v)}` is not `ApiNewRelicView`")
        else:
            match += 1

        # validate data type: ApiOpsGenieView
        if type(v) is not ApiOpsGenieView:
            error_messages.append(f"Error! Input type `{type(v)}` is not `ApiOpsGenieView`")
        else:
            match += 1

        # validate data type: ApiPagerDutyView
        if type(v) is not ApiPagerDutyView:
            error_messages.append(f"Error! Input type `{type(v)}` is not `ApiPagerDutyView`")
        else:
            match += 1

        # validate data type: ApiPrometheusView
        if type(v) is not ApiPrometheusView:
            error_messages.append(f"Error! Input type `{type(v)}` is not `ApiPrometheusView`")
        else:
            match += 1

        # validate data type: ApiSlackView
        if type(v) is not ApiSlackView:
            error_messages.append(f"Error! Input type `{type(v)}` is not `ApiSlackView`")
        else:
            match += 1

        # validate data type: ApiVictorOpsView
        if type(v) is not ApiVictorOpsView:
            error_messages.append(f"Error! Input type `{type(v)}` is not `ApiVictorOpsView`")
        else:
            match += 1

        # validate data type: ApiWebhookView
        if type(v) is not ApiWebhookView:
            error_messages.append(f"Error! Input type `{type(v)}` is not `ApiWebhookView`")
        else:
            match += 1

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into IntegrationViewForNdsGroup with oneOf schemas: ApiDatadogView, ApiMicrosoftTeamsView, ApiNewRelicView, ApiOpsGenieView, ApiPagerDutyView, ApiPrometheusView, ApiSlackView, ApiVictorOpsView, ApiWebhookView. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into IntegrationViewForNdsGroup with oneOf schemas: ApiDatadogView, ApiMicrosoftTeamsView, ApiNewRelicView, ApiOpsGenieView, ApiPagerDutyView, ApiPrometheusView, ApiSlackView, ApiVictorOpsView, ApiWebhookView. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> IntegrationViewForNdsGroup:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> IntegrationViewForNdsGroup:
        """Returns the object represented by the json string"""
        instance = cls()
        error_messages = []
        match = 0

        # deserialize data into ApiDatadogView
        try:
            instance.actual_instance = ApiDatadogView.from_json(json_str)
            match += 1
        except ValidationError as e:
            error_messages.append(str(e))
        # deserialize data into ApiMicrosoftTeamsView
        try:
            instance.actual_instance = ApiMicrosoftTeamsView.from_json(json_str)
            match += 1
        except ValidationError as e:
            error_messages.append(str(e))
        # deserialize data into ApiNewRelicView
        try:
            instance.actual_instance = ApiNewRelicView.from_json(json_str)
            match += 1
        except ValidationError as e:
            error_messages.append(str(e))
        # deserialize data into ApiOpsGenieView
        try:
            instance.actual_instance = ApiOpsGenieView.from_json(json_str)
            match += 1
        except ValidationError as e:
            error_messages.append(str(e))
        # deserialize data into ApiPagerDutyView
        try:
            instance.actual_instance = ApiPagerDutyView.from_json(json_str)
            match += 1
        except ValidationError as e:
            error_messages.append(str(e))
        # deserialize data into ApiPrometheusView
        try:
            instance.actual_instance = ApiPrometheusView.from_json(json_str)
            match += 1
        except ValidationError as e:
            error_messages.append(str(e))
        # deserialize data into ApiSlackView
        try:
            instance.actual_instance = ApiSlackView.from_json(json_str)
            match += 1
        except ValidationError as e:
            error_messages.append(str(e))
        # deserialize data into ApiVictorOpsView
        try:
            instance.actual_instance = ApiVictorOpsView.from_json(json_str)
            match += 1
        except ValidationError as e:
            error_messages.append(str(e))
        # deserialize data into ApiWebhookView
        try:
            instance.actual_instance = ApiWebhookView.from_json(json_str)
            match += 1
        except ValidationError as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into IntegrationViewForNdsGroup with oneOf schemas: ApiDatadogView, ApiMicrosoftTeamsView, ApiNewRelicView, ApiOpsGenieView, ApiPagerDutyView, ApiPrometheusView, ApiSlackView, ApiVictorOpsView, ApiWebhookView. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into IntegrationViewForNdsGroup with oneOf schemas: ApiDatadogView, ApiMicrosoftTeamsView, ApiNewRelicView, ApiOpsGenieView, ApiPagerDutyView, ApiPrometheusView, ApiSlackView, ApiVictorOpsView, ApiWebhookView. Details: " + ", ".join(error_messages))
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

