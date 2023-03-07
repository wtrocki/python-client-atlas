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


class Collation(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    One or more settings that specify language-specific rules to compare strings within this index.
    """


    class MetaOapg:
        required = {
            "locale",
        }
        
        class properties:
            
            
            class locale(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "af": "AF",
                        "sq": "SQ",
                        "am": "AM",
                        "ar": "AR",
                        "hy": "HY",
                        "as": "AS",
                        "az": "AZ",
                        "bn": "BN",
                        "be": "BE",
                        "bs": "BS",
                        "bs_Cyrl": "BS_CYRL",
                        "bg": "BG",
                        "my": "MY",
                        "ca": "CA",
                        "chr": "CHR",
                        "zh": "ZH",
                        "zh_Hant": "ZH_HANT",
                        "hr": "HR",
                        "cs": "CS",
                        "da": "DA",
                        "nl": "NL",
                        "dz": "DZ",
                        "en": "EN",
                        "en_US": "EN_US",
                        "en_US_POSIX": "EN_US_POSIX",
                        "eo": "EO",
                        "et": "ET",
                        "ee": "EE",
                        "fo": "FO",
                        "fil": "FIL",
                        "fi_FI": "FI_FI",
                        "fr": "FR",
                        "fr_CA": "FR_CA",
                        "gl": "GL",
                        "ka": "KA",
                        "de": "DE",
                        "de_AT": "DE_AT",
                        "el": "EL",
                        "gu": "GU",
                        "ha": "HA",
                        "haw": "HAW",
                        "he": "HE",
                        "hi": "HI",
                        "hu": "HU",
                        "is": "IS",
                        "ig": "IG",
                        "smn": "SMN",
                        "id": "ID",
                        "ga": "GA",
                        "it": "IT",
                        "ja": "JA",
                        "kl": "KL",
                        "kn": "KN",
                        "kk": "KK",
                        "km": "KM",
                        "kok": "KOK",
                        "ko": "KO",
                        "ky": "KY",
                        "lk": "LK",
                        "lo": "LO",
                        "lv": "LV",
                        "li": "LI",
                        "lt": "LT",
                        "dsb": "DSB",
                        "lb": "LB",
                        "mk": "MK",
                        "ms": "MS",
                        "ml": "ML",
                        "mt": "MT",
                        "mr": "MR",
                        "mn": "MN",
                        "ne": "NE",
                        "se": "SE",
                        "nb": "NB",
                        "nn": "NN",
                        "or": "OR",
                        "om": "OM",
                        "ps": "PS",
                        "fa": "FA",
                        "fa_AF": "FA_AF",
                        "pl": "PL",
                        "pt": "PT",
                        "pa": "PA",
                        "ro": "RO",
                        "ru": "RU",
                        "sr": "SR",
                        "sr_Latn": "SR_LATN",
                        "si": "SI",
                        "sk": "SK",
                        "sl": "SL",
                        "es": "ES",
                        "sw": "SW",
                        "sv": "SV",
                        "ta": "TA",
                        "te": "TE",
                        "th": "TH",
                        "bo": "BO",
                        "to": "TO",
                        "tr": "TR",
                        "uk": "UK",
                        "hsb": "HSB",
                        "ur": "UR",
                        "ug": "UG",
                        "vi": "VI",
                        "wae": "WAE",
                        "cy": "CY",
                        "yi": "YI",
                        "yo": "YO",
                        "zu": "ZU",
                    }
                
                @schemas.classproperty
                def AF(cls):
                    return cls("af")
                
                @schemas.classproperty
                def SQ(cls):
                    return cls("sq")
                
                @schemas.classproperty
                def AM(cls):
                    return cls("am")
                
                @schemas.classproperty
                def AR(cls):
                    return cls("ar")
                
                @schemas.classproperty
                def HY(cls):
                    return cls("hy")
                
                @schemas.classproperty
                def AS(cls):
                    return cls("as")
                
                @schemas.classproperty
                def AZ(cls):
                    return cls("az")
                
                @schemas.classproperty
                def BN(cls):
                    return cls("bn")
                
                @schemas.classproperty
                def BE(cls):
                    return cls("be")
                
                @schemas.classproperty
                def BS(cls):
                    return cls("bs")
                
                @schemas.classproperty
                def BS_CYRL(cls):
                    return cls("bs_Cyrl")
                
                @schemas.classproperty
                def BG(cls):
                    return cls("bg")
                
                @schemas.classproperty
                def MY(cls):
                    return cls("my")
                
                @schemas.classproperty
                def CA(cls):
                    return cls("ca")
                
                @schemas.classproperty
                def CHR(cls):
                    return cls("chr")
                
                @schemas.classproperty
                def ZH(cls):
                    return cls("zh")
                
                @schemas.classproperty
                def ZH_HANT(cls):
                    return cls("zh_Hant")
                
                @schemas.classproperty
                def HR(cls):
                    return cls("hr")
                
                @schemas.classproperty
                def CS(cls):
                    return cls("cs")
                
                @schemas.classproperty
                def DA(cls):
                    return cls("da")
                
                @schemas.classproperty
                def NL(cls):
                    return cls("nl")
                
                @schemas.classproperty
                def DZ(cls):
                    return cls("dz")
                
                @schemas.classproperty
                def EN(cls):
                    return cls("en")
                
                @schemas.classproperty
                def EN_US(cls):
                    return cls("en_US")
                
                @schemas.classproperty
                def EN_US_POSIX(cls):
                    return cls("en_US_POSIX")
                
                @schemas.classproperty
                def EO(cls):
                    return cls("eo")
                
                @schemas.classproperty
                def ET(cls):
                    return cls("et")
                
                @schemas.classproperty
                def EE(cls):
                    return cls("ee")
                
                @schemas.classproperty
                def FO(cls):
                    return cls("fo")
                
                @schemas.classproperty
                def FIL(cls):
                    return cls("fil")
                
                @schemas.classproperty
                def FI_FI(cls):
                    return cls("fi_FI")
                
                @schemas.classproperty
                def FR(cls):
                    return cls("fr")
                
                @schemas.classproperty
                def FR_CA(cls):
                    return cls("fr_CA")
                
                @schemas.classproperty
                def GL(cls):
                    return cls("gl")
                
                @schemas.classproperty
                def KA(cls):
                    return cls("ka")
                
                @schemas.classproperty
                def DE(cls):
                    return cls("de")
                
                @schemas.classproperty
                def DE_AT(cls):
                    return cls("de_AT")
                
                @schemas.classproperty
                def EL(cls):
                    return cls("el")
                
                @schemas.classproperty
                def GU(cls):
                    return cls("gu")
                
                @schemas.classproperty
                def HA(cls):
                    return cls("ha")
                
                @schemas.classproperty
                def HAW(cls):
                    return cls("haw")
                
                @schemas.classproperty
                def HE(cls):
                    return cls("he")
                
                @schemas.classproperty
                def HI(cls):
                    return cls("hi")
                
                @schemas.classproperty
                def HU(cls):
                    return cls("hu")
                
                @schemas.classproperty
                def IS(cls):
                    return cls("is")
                
                @schemas.classproperty
                def IG(cls):
                    return cls("ig")
                
                @schemas.classproperty
                def SMN(cls):
                    return cls("smn")
                
                @schemas.classproperty
                def ID(cls):
                    return cls("id")
                
                @schemas.classproperty
                def GA(cls):
                    return cls("ga")
                
                @schemas.classproperty
                def IT(cls):
                    return cls("it")
                
                @schemas.classproperty
                def JA(cls):
                    return cls("ja")
                
                @schemas.classproperty
                def KL(cls):
                    return cls("kl")
                
                @schemas.classproperty
                def KN(cls):
                    return cls("kn")
                
                @schemas.classproperty
                def KK(cls):
                    return cls("kk")
                
                @schemas.classproperty
                def KM(cls):
                    return cls("km")
                
                @schemas.classproperty
                def KOK(cls):
                    return cls("kok")
                
                @schemas.classproperty
                def KO(cls):
                    return cls("ko")
                
                @schemas.classproperty
                def KY(cls):
                    return cls("ky")
                
                @schemas.classproperty
                def LK(cls):
                    return cls("lk")
                
                @schemas.classproperty
                def LO(cls):
                    return cls("lo")
                
                @schemas.classproperty
                def LV(cls):
                    return cls("lv")
                
                @schemas.classproperty
                def LI(cls):
                    return cls("li")
                
                @schemas.classproperty
                def LT(cls):
                    return cls("lt")
                
                @schemas.classproperty
                def DSB(cls):
                    return cls("dsb")
                
                @schemas.classproperty
                def LB(cls):
                    return cls("lb")
                
                @schemas.classproperty
                def MK(cls):
                    return cls("mk")
                
                @schemas.classproperty
                def MS(cls):
                    return cls("ms")
                
                @schemas.classproperty
                def ML(cls):
                    return cls("ml")
                
                @schemas.classproperty
                def MT(cls):
                    return cls("mt")
                
                @schemas.classproperty
                def MR(cls):
                    return cls("mr")
                
                @schemas.classproperty
                def MN(cls):
                    return cls("mn")
                
                @schemas.classproperty
                def NE(cls):
                    return cls("ne")
                
                @schemas.classproperty
                def SE(cls):
                    return cls("se")
                
                @schemas.classproperty
                def NB(cls):
                    return cls("nb")
                
                @schemas.classproperty
                def NN(cls):
                    return cls("nn")
                
                @schemas.classproperty
                def OR(cls):
                    return cls("or")
                
                @schemas.classproperty
                def OM(cls):
                    return cls("om")
                
                @schemas.classproperty
                def PS(cls):
                    return cls("ps")
                
                @schemas.classproperty
                def FA(cls):
                    return cls("fa")
                
                @schemas.classproperty
                def FA_AF(cls):
                    return cls("fa_AF")
                
                @schemas.classproperty
                def PL(cls):
                    return cls("pl")
                
                @schemas.classproperty
                def PT(cls):
                    return cls("pt")
                
                @schemas.classproperty
                def PA(cls):
                    return cls("pa")
                
                @schemas.classproperty
                def RO(cls):
                    return cls("ro")
                
                @schemas.classproperty
                def RU(cls):
                    return cls("ru")
                
                @schemas.classproperty
                def SR(cls):
                    return cls("sr")
                
                @schemas.classproperty
                def SR_LATN(cls):
                    return cls("sr_Latn")
                
                @schemas.classproperty
                def SI(cls):
                    return cls("si")
                
                @schemas.classproperty
                def SK(cls):
                    return cls("sk")
                
                @schemas.classproperty
                def SL(cls):
                    return cls("sl")
                
                @schemas.classproperty
                def ES(cls):
                    return cls("es")
                
                @schemas.classproperty
                def SW(cls):
                    return cls("sw")
                
                @schemas.classproperty
                def SV(cls):
                    return cls("sv")
                
                @schemas.classproperty
                def TA(cls):
                    return cls("ta")
                
                @schemas.classproperty
                def TE(cls):
                    return cls("te")
                
                @schemas.classproperty
                def TH(cls):
                    return cls("th")
                
                @schemas.classproperty
                def BO(cls):
                    return cls("bo")
                
                @schemas.classproperty
                def TO(cls):
                    return cls("to")
                
                @schemas.classproperty
                def TR(cls):
                    return cls("tr")
                
                @schemas.classproperty
                def UK(cls):
                    return cls("uk")
                
                @schemas.classproperty
                def HSB(cls):
                    return cls("hsb")
                
                @schemas.classproperty
                def UR(cls):
                    return cls("ur")
                
                @schemas.classproperty
                def UG(cls):
                    return cls("ug")
                
                @schemas.classproperty
                def VI(cls):
                    return cls("vi")
                
                @schemas.classproperty
                def WAE(cls):
                    return cls("wae")
                
                @schemas.classproperty
                def CY(cls):
                    return cls("cy")
                
                @schemas.classproperty
                def YI(cls):
                    return cls("yi")
                
                @schemas.classproperty
                def YO(cls):
                    return cls("yo")
                
                @schemas.classproperty
                def ZU(cls):
                    return cls("zu")
            
            
            class alternate(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "non-ignorable": "NONIGNORABLE",
                        "shifted": "SHIFTED",
                    }
                
                @schemas.classproperty
                def NONIGNORABLE(cls):
                    return cls("non-ignorable")
                
                @schemas.classproperty
                def SHIFTED(cls):
                    return cls("shifted")
            backwards = schemas.BoolSchema
            
            
            class caseFirst(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "lower": "LOWER",
                        "false": "FALSE",
                        "upper": "UPPER",
                    }
                
                @schemas.classproperty
                def LOWER(cls):
                    return cls("lower")
                
                @schemas.classproperty
                def FALSE(cls):
                    return cls("false")
                
                @schemas.classproperty
                def UPPER(cls):
                    return cls("upper")
            caseLevel = schemas.BoolSchema
            
            
            class maxVariable(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "punct": "PUNCT",
                        "space": "SPACE",
                    }
                
                @schemas.classproperty
                def PUNCT(cls):
                    return cls("punct")
                
                @schemas.classproperty
                def SPACE(cls):
                    return cls("space")
            normalization = schemas.BoolSchema
            numericOrdering = schemas.BoolSchema
            
            
            class strength(
                schemas.Int32Schema
            ):
            
            
                class MetaOapg:
                    format = 'int32'
                    inclusive_maximum = 5
                    inclusive_minimum = 1
            __annotations__ = {
                "locale": locale,
                "alternate": alternate,
                "backwards": backwards,
                "caseFirst": caseFirst,
                "caseLevel": caseLevel,
                "maxVariable": maxVariable,
                "normalization": normalization,
                "numericOrdering": numericOrdering,
                "strength": strength,
            }
    
    locale: MetaOapg.properties.locale
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["locale"]) -> MetaOapg.properties.locale: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["alternate"]) -> MetaOapg.properties.alternate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["backwards"]) -> MetaOapg.properties.backwards: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["caseFirst"]) -> MetaOapg.properties.caseFirst: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["caseLevel"]) -> MetaOapg.properties.caseLevel: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maxVariable"]) -> MetaOapg.properties.maxVariable: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["normalization"]) -> MetaOapg.properties.normalization: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["numericOrdering"]) -> MetaOapg.properties.numericOrdering: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["strength"]) -> MetaOapg.properties.strength: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["locale", "alternate", "backwards", "caseFirst", "caseLevel", "maxVariable", "normalization", "numericOrdering", "strength", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["locale"]) -> MetaOapg.properties.locale: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["alternate"]) -> typing.Union[MetaOapg.properties.alternate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["backwards"]) -> typing.Union[MetaOapg.properties.backwards, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["caseFirst"]) -> typing.Union[MetaOapg.properties.caseFirst, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["caseLevel"]) -> typing.Union[MetaOapg.properties.caseLevel, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maxVariable"]) -> typing.Union[MetaOapg.properties.maxVariable, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["normalization"]) -> typing.Union[MetaOapg.properties.normalization, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["numericOrdering"]) -> typing.Union[MetaOapg.properties.numericOrdering, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["strength"]) -> typing.Union[MetaOapg.properties.strength, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["locale", "alternate", "backwards", "caseFirst", "caseLevel", "maxVariable", "normalization", "numericOrdering", "strength", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        locale: typing.Union[MetaOapg.properties.locale, str, ],
        alternate: typing.Union[MetaOapg.properties.alternate, str, schemas.Unset] = schemas.unset,
        backwards: typing.Union[MetaOapg.properties.backwards, bool, schemas.Unset] = schemas.unset,
        caseFirst: typing.Union[MetaOapg.properties.caseFirst, str, schemas.Unset] = schemas.unset,
        caseLevel: typing.Union[MetaOapg.properties.caseLevel, bool, schemas.Unset] = schemas.unset,
        maxVariable: typing.Union[MetaOapg.properties.maxVariable, str, schemas.Unset] = schemas.unset,
        normalization: typing.Union[MetaOapg.properties.normalization, bool, schemas.Unset] = schemas.unset,
        numericOrdering: typing.Union[MetaOapg.properties.numericOrdering, bool, schemas.Unset] = schemas.unset,
        strength: typing.Union[MetaOapg.properties.strength, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Collation':
        return super().__new__(
            cls,
            *_args,
            locale=locale,
            alternate=alternate,
            backwards=backwards,
            caseFirst=caseFirst,
            caseLevel=caseLevel,
            maxVariable=maxVariable,
            normalization=normalization,
            numericOrdering=numericOrdering,
            strength=strength,
            _configuration=_configuration,
            **kwargs,
        )
