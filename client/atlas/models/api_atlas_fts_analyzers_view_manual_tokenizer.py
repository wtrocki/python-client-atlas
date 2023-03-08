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
from atlas.models.tokenizeredge_gram import TokenizeredgeGram
from atlas.models.tokenizerkeyword import Tokenizerkeyword
from atlas.models.tokenizern_gram import TokenizernGram
from atlas.models.tokenizerregex_capture_group import TokenizerregexCaptureGroup
from atlas.models.tokenizerregex_split import TokenizerregexSplit
from atlas.models.tokenizerstandard import Tokenizerstandard
from atlas.models.tokenizeruax_url_email import TokenizeruaxUrlEmail
from atlas.models.tokenizerwhitespace import Tokenizerwhitespace
from typing import Any, List
from pydantic import StrictStr, Field

APIATLASFTSANALYZERSVIEWMANUALTOKENIZER_ONE_OF_SCHEMAS = ["TokenizeredgeGram", "Tokenizerkeyword", "TokenizernGram", "TokenizerregexCaptureGroup", "TokenizerregexSplit", "Tokenizerstandard", "TokenizeruaxUrlEmail", "Tokenizerwhitespace"]

class ApiAtlasFTSAnalyzersViewManualTokenizer(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    # data type: TokenizeredgeGram
    oneof_schema_1_validator: Optional[TokenizeredgeGram] = None
    # data type: Tokenizerkeyword
    oneof_schema_2_validator: Optional[Tokenizerkeyword] = None
    # data type: TokenizernGram
    oneof_schema_3_validator: Optional[TokenizernGram] = None
    # data type: TokenizerregexCaptureGroup
    oneof_schema_4_validator: Optional[TokenizerregexCaptureGroup] = None
    # data type: TokenizerregexSplit
    oneof_schema_5_validator: Optional[TokenizerregexSplit] = None
    # data type: Tokenizerstandard
    oneof_schema_6_validator: Optional[Tokenizerstandard] = None
    # data type: TokenizeruaxUrlEmail
    oneof_schema_7_validator: Optional[TokenizeruaxUrlEmail] = None
    # data type: Tokenizerwhitespace
    oneof_schema_8_validator: Optional[Tokenizerwhitespace] = None
    actual_instance: Any
    one_of_schemas: List[str] = Field(APIATLASFTSANALYZERSVIEWMANUALTOKENIZER_ONE_OF_SCHEMAS, const=True)

    class Config:
        validate_assignment = True

    @validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = cls()
        error_messages = []
        match = 0
        # validate data type: TokenizeredgeGram
        if type(v) is not TokenizeredgeGram:
            error_messages.append(f"Error! Input type `{type(v)}` is not `TokenizeredgeGram`")
        else:
            match += 1

        # validate data type: Tokenizerkeyword
        if type(v) is not Tokenizerkeyword:
            error_messages.append(f"Error! Input type `{type(v)}` is not `Tokenizerkeyword`")
        else:
            match += 1

        # validate data type: TokenizernGram
        if type(v) is not TokenizernGram:
            error_messages.append(f"Error! Input type `{type(v)}` is not `TokenizernGram`")
        else:
            match += 1

        # validate data type: TokenizerregexCaptureGroup
        if type(v) is not TokenizerregexCaptureGroup:
            error_messages.append(f"Error! Input type `{type(v)}` is not `TokenizerregexCaptureGroup`")
        else:
            match += 1

        # validate data type: TokenizerregexSplit
        if type(v) is not TokenizerregexSplit:
            error_messages.append(f"Error! Input type `{type(v)}` is not `TokenizerregexSplit`")
        else:
            match += 1

        # validate data type: Tokenizerstandard
        if type(v) is not Tokenizerstandard:
            error_messages.append(f"Error! Input type `{type(v)}` is not `Tokenizerstandard`")
        else:
            match += 1

        # validate data type: TokenizeruaxUrlEmail
        if type(v) is not TokenizeruaxUrlEmail:
            error_messages.append(f"Error! Input type `{type(v)}` is not `TokenizeruaxUrlEmail`")
        else:
            match += 1

        # validate data type: Tokenizerwhitespace
        if type(v) is not Tokenizerwhitespace:
            error_messages.append(f"Error! Input type `{type(v)}` is not `Tokenizerwhitespace`")
        else:
            match += 1

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into ApiAtlasFTSAnalyzersViewManualTokenizer with oneOf schemas: TokenizeredgeGram, Tokenizerkeyword, TokenizernGram, TokenizerregexCaptureGroup, TokenizerregexSplit, Tokenizerstandard, TokenizeruaxUrlEmail, Tokenizerwhitespace. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into ApiAtlasFTSAnalyzersViewManualTokenizer with oneOf schemas: TokenizeredgeGram, Tokenizerkeyword, TokenizernGram, TokenizerregexCaptureGroup, TokenizerregexSplit, Tokenizerstandard, TokenizeruaxUrlEmail, Tokenizerwhitespace. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> ApiAtlasFTSAnalyzersViewManualTokenizer:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> ApiAtlasFTSAnalyzersViewManualTokenizer:
        """Returns the object represented by the json string"""
        instance = cls()
        error_messages = []
        match = 0

        # deserialize data into TokenizeredgeGram
        try:
            instance.actual_instance = TokenizeredgeGram.from_json(json_str)
            match += 1
        except ValidationError as e:
            error_messages.append(str(e))
        # deserialize data into Tokenizerkeyword
        try:
            instance.actual_instance = Tokenizerkeyword.from_json(json_str)
            match += 1
        except ValidationError as e:
            error_messages.append(str(e))
        # deserialize data into TokenizernGram
        try:
            instance.actual_instance = TokenizernGram.from_json(json_str)
            match += 1
        except ValidationError as e:
            error_messages.append(str(e))
        # deserialize data into TokenizerregexCaptureGroup
        try:
            instance.actual_instance = TokenizerregexCaptureGroup.from_json(json_str)
            match += 1
        except ValidationError as e:
            error_messages.append(str(e))
        # deserialize data into TokenizerregexSplit
        try:
            instance.actual_instance = TokenizerregexSplit.from_json(json_str)
            match += 1
        except ValidationError as e:
            error_messages.append(str(e))
        # deserialize data into Tokenizerstandard
        try:
            instance.actual_instance = Tokenizerstandard.from_json(json_str)
            match += 1
        except ValidationError as e:
            error_messages.append(str(e))
        # deserialize data into TokenizeruaxUrlEmail
        try:
            instance.actual_instance = TokenizeruaxUrlEmail.from_json(json_str)
            match += 1
        except ValidationError as e:
            error_messages.append(str(e))
        # deserialize data into Tokenizerwhitespace
        try:
            instance.actual_instance = Tokenizerwhitespace.from_json(json_str)
            match += 1
        except ValidationError as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into ApiAtlasFTSAnalyzersViewManualTokenizer with oneOf schemas: TokenizeredgeGram, Tokenizerkeyword, TokenizernGram, TokenizerregexCaptureGroup, TokenizerregexSplit, Tokenizerstandard, TokenizeruaxUrlEmail, Tokenizerwhitespace. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into ApiAtlasFTSAnalyzersViewManualTokenizer with oneOf schemas: TokenizeredgeGram, Tokenizerkeyword, TokenizernGram, TokenizerregexCaptureGroup, TokenizerregexSplit, Tokenizerstandard, TokenizeruaxUrlEmail, Tokenizerwhitespace. Details: " + ", ".join(error_messages))
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
