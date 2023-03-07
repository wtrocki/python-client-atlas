<a name="__pageTop"></a>
# atlas.apis.tags.mongo_db_cloud_users_api.MongoDBCloudUsersApi

All URIs are relative to *https://cloud.mongodb.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user**](#create_user) | **post** /api/atlas/v2/users | Create One MongoDB Cloud User
[**get_user**](#get_user) | **get** /api/atlas/v2/users/{userId} | Return One MongoDB Cloud User using Its ID
[**get_user_by_username**](#get_user_by_username) | **get** /api/atlas/v2/users/byName/{userName} | Return One MongoDB Cloud User using Their Username

# **create_user**
<a name="create_user"></a>
> ApiAppUserView create_user(api_app_user_view)

Create One MongoDB Cloud User

Creates one MongoDB Cloud user account. A MongoDB Cloud user account only grants access to the MongoDB Cloud application. To grant database access, create a database user. To use this resource, the requesting API Key can have any role. This resource doesn't require the API Key to have an Access List.

### Example

```python
import atlas
from atlas.apis.tags import mongo_db_cloud_users_api
from atlas.model.api_error import ApiError
from atlas.model.api_app_user_view import ApiAppUserView
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.mongodb.com
# See configuration.py for a list of all supported configuration parameters.
configuration = atlas.Configuration(
    host = "https://cloud.mongodb.com"
)

# Enter a context with an instance of the API client
with atlas.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mongo_db_cloud_users_api.MongoDBCloudUsersApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
    }
    body = ApiAppUserView(
        country="AE",
        created_at="1970-01-01T00:00:00.00Z",
        email_address="email_address_example",
        first_name="first_name_example",
        id="32b6e34b3d91647abb20e7b8",
        last_auth="1970-01-01T00:00:00.00Z",
        last_name="last_name_example",
        links=[
            Link(
                href="https://cloud.mongodb.com/api/atlas",
                rel="self",
            )
        ],
        mobile_number="\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\1\ssssssssssssssssssssssssssssssss\sssssssssssssssssssssss900\sssssssssssssssssssssssss\.\sssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss217\sssssssssssssssssssss0962",
        password="password_example",
        roles=[
            ApiRoleAssignmentView(
                group_id="32b6e34b3d91647abb20e7b8",
                org_id="32b6e34b3d91647abb20e7b8",
                role_name="ORG_OWNER",
            )
        ],
        team_ids=[
            "32b6e34b3d91647abb20e7b8"
        ],
        username="username_example",
    )
    try:
        # Create One MongoDB Cloud User
        api_response = api_instance.create_user(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling MongoDBCloudUsersApi->create_user: %s\n" % e)

    # example passing only optional values
    query_params = {
        'envelope': False,
        'pretty': False,
    }
    body = ApiAppUserView(
        country="AE",
        created_at="1970-01-01T00:00:00.00Z",
        email_address="email_address_example",
        first_name="first_name_example",
        id="32b6e34b3d91647abb20e7b8",
        last_auth="1970-01-01T00:00:00.00Z",
        last_name="last_name_example",
        links=[
            Link(
                href="https://cloud.mongodb.com/api/atlas",
                rel="self",
            )
        ],
        mobile_number="\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\1\ssssssssssssssssssssssssssssssss\sssssssssssssssssssssss900\sssssssssssssssssssssssss\.\sssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss217\sssssssssssssssssssss0962",
        password="password_example",
        roles=[
            ApiRoleAssignmentView(
                group_id="32b6e34b3d91647abb20e7b8",
                org_id="32b6e34b3d91647abb20e7b8",
                role_name="ORG_OWNER",
            )
        ],
        team_ids=[
            "32b6e34b3d91647abb20e7b8"
        ],
        username="username_example",
    )
    try:
        # Create One MongoDB Cloud User
        api_response = api_instance.create_user(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling MongoDBCloudUsersApi->create_user: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
query_params | RequestQueryParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/vnd.atlas.2023-01-01+json', 'application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiAppUserView**](../../models/ApiAppUserView.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
envelope | EnvelopeSchema | | optional
pretty | PrettySchema | | optional


# EnvelopeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

# PrettySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_user.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#create_user.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#create_user.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#create_user.ApiResponseFor500) | Internal Server Error

#### create_user.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndAtlas20230101json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndAtlas20230101json
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiAppUserView**](../../models/ApiAppUserView.md) |  | 


#### create_user.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### create_user.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### create_user.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_user**
<a name="get_user"></a>
> ApiAppUserView get_user(user_id)

Return One MongoDB Cloud User using Its ID

Returns the details for one MongoDB Cloud user account with the specified unique identifier for the user. To use this resource, the requesting API Key can have any role. This resource doesn't require the API Key to have an Access List.

### Example

```python
import atlas
from atlas.apis.tags import mongo_db_cloud_users_api
from atlas.model.api_error import ApiError
from atlas.model.api_app_user_view import ApiAppUserView
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.mongodb.com
# See configuration.py for a list of all supported configuration parameters.
configuration = atlas.Configuration(
    host = "https://cloud.mongodb.com"
)

# Enter a context with an instance of the API client
with atlas.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mongo_db_cloud_users_api.MongoDBCloudUsersApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'userId': "bf325375e030fccba0091731",
    }
    query_params = {
    }
    try:
        # Return One MongoDB Cloud User using Its ID
        api_response = api_instance.get_user(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling MongoDBCloudUsersApi->get_user: %s\n" % e)

    # example passing only optional values
    path_params = {
        'userId': "bf325375e030fccba0091731",
    }
    query_params = {
        'envelope': False,
        'pretty': False,
    }
    try:
        # Return One MongoDB Cloud User using Its ID
        api_response = api_instance.get_user(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling MongoDBCloudUsersApi->get_user: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/vnd.atlas.2023-01-01+json', 'application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
envelope | EnvelopeSchema | | optional
pretty | PrettySchema | | optional


# EnvelopeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

# PrettySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
userId | UserIdSchema | | 

# UserIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_user.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#get_user.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#get_user.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#get_user.ApiResponseFor500) | Internal Server Error

#### get_user.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndAtlas20230101json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndAtlas20230101json
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiAppUserView**](../../models/ApiAppUserView.md) |  | 


#### get_user.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### get_user.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### get_user.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_user_by_username**
<a name="get_user_by_username"></a>
> ApiAppUserView get_user_by_username(user_name)

Return One MongoDB Cloud User using Their Username

Returns the details for one MongoDB Cloud user account with the specified username. To use this resource, the requesting API Key can have any role. This resource doesn't require the API Key to have an Access List.

### Example

```python
import atlas
from atlas.apis.tags import mongo_db_cloud_users_api
from atlas.model.api_error import ApiError
from atlas.model.api_app_user_view import ApiAppUserView
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.mongodb.com
# See configuration.py for a list of all supported configuration parameters.
configuration = atlas.Configuration(
    host = "https://cloud.mongodb.com"
)

# Enter a context with an instance of the API client
with atlas.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mongo_db_cloud_users_api.MongoDBCloudUsersApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'userName': "`.^^3i-5kga^8p^#m&_u~gwru'!0_ak${ha{-6|433`8-i&+'*puq-ugn~?pr64#2j*+-2^2e.$%6pbt%hk|v!5e?r$7|af0ebm5rc56tr/-g.m%*4niwjg{13sm+-|mu5|vy{e*b#b9+d%mxpbxi+k'{=/nl_8{#!$43^d`o2!'^-~l8.+!``y*~$?-h{zmt}?&t7i/s~vr{s{8k+*d{8/l=sdiw$`y}p66_kr&fk#dzf26w^re_=raqkq?7z1#.y#2ega/vp/%4jh&2e=u4`%v8+f`foz?2qqflj~jpq7?w?*_q4*63e$gl73+}mo6x0.mk4!s^0#rw2#z.w_0`'//?6wu8^^$-svhwhf!817%=j~d#zv^0s/._a`&u^it-{x+{1j|gat-'j&x72'0uq_v_q+th{|b6n*g.&-0dh{29cu9_##l4m+r+q66f4-cvknicn88tf`zwre??qu32*'gcisb+8zk5}}j.}fd!0^z02#{/'=9u6qan*+f{*h8z9}.s*4pxc5es6%aj+|mf&_l'=k4s{~*hp0b~v7+i`^^f_z44u'+sww.ty!c3~{#2cy^q7=9te/cky}~uxl}p3l8etvrn}psi$7t3'}5t4m8`p4=k{+%6%kfdjgs26y*'~.35b8|4+4ef#5sixdef`-z~q3-57u&lkyd$09n`mu6s7nk9ga{kqaw'mnvayk1%%.4!{1r5*/kh-}79zn2~p4c/3u|t~*zk1uknz%gku*_v8`%x9e'#_py}m=zo~k1y!t?&{{vejznv'^qrfqlu4a./7jg-#raf24q-#92yetd|l#i9y!jw|fn_/=od{`nsr'^y$one%0nny|ie|g?ms6b|'^?{%.vn/sjb5x~aw9n8l8xtam$l=h#k`5tw55e_y4/yv*x1|o`l~-'+u351u03/s~0~ja62f`9'&*t&#=&z%&+534}{0t_ycd0+d`.g=#is+ys=ryguq=&h-!}d/k^7`i4hs9r'1%=-sx*?!c{4&+u-*$?$_'%wmq3}1_k$vx|x!0r*7~tm#sp+'!$#qnh+m.{&_b{=u+-m8d}lkxa?yz_^lx8e{o?dlw|q6z'9y=yormjxh+{ns|}z`+z._v$4{yaml`c.!!`sh?o6ie}w.g=um1^9-03``yri%osg|0d'ufrpu1/!$h6oc23a*be++|g|po{|`+5=$kyz9?6w.qtkztia`'b3el-wu&4r$tr1-?zm=355.%9|a/*mv0q&x_zjp^}|cr&+1dezr$hb7`iez+gegb~0v*'6p12m_slv`m?tbdda.*d|ao~z3818h8l#v$=3t/g5&%f7`ze2}5457.{j*-&zq#6ua1$~|49+|=%l&2*xs!fuek3gvz0mwwb+837qz-b.95q?ai*u1w%&`~xd*zk$me3vji!2hv8`8=^ytc1d~lhv$`wr&#3b/^jw5vi1jy?+l.v5i!yxujdcnm*'6c=33zgk-x&781q!h2g-es7f/p~m$r+zcmxxf-x|4x#'$xet$d&b=m|+}'oc1n$0wl0_=au+a#.y0mscj?{7^r`bw-jdfg'=/rfx/4/^!p%|5--9hb-w11sy#406=~-4=28a$.8$6s=#b|y}x=.lhfcu/y^#3'7-1'cs4g3r~?qwk4h!hxj%w%~3qh~z/y7y9'd%s2='z?{5s2.u6|'ybq-th8pzpsf.&q/zf0+n`_kj/_#?z%%7``a441u18vpq{-bp?dz%5az`h+f.r${k*l0}c`6%63=a'vo2a38shrgx5n~&bj84mrnn8pcw1i_+nym?lw429'&mc|0*q!e/m_sqn.`*4%u_y_|k!y*v}|*`ivz~x*~nvcah/5dzk/rt0`lkujsd$+5v_xc8s.|oifm_t??8/196qubao3?w/7r!4r45_{t-ym&xp07.yx/'{$q8{fq^-kk%&p9j&e7yqjg*`g}b1{i_v*r!&k1#+e}g`d9d8?5#%t5ve4}bpxk=+4q.{v_/z!huc2iv*tbg.~l8!8%%&hqw-g~mlrc!v7t-hk0=oxc+%30%6yp8=0v3|8_.cs#w6=j66f2.+8`oc+3s2'!-gfx2rz.4-'~aer.o!w=g3vs3%p~i|'_uo5m-la~i1/|4o$d6`{.gp3o7ovi0$o}o|4l-{~-096p/_z5e3*g.1#~fs01!|j5rt_v#dq'0&!wm5dw?_^i6lfwp9l=w8{$5~#p+*-85wjphw!n38!va'z0p8q'4&1g64!2'p}kn=4dc.{721$?9}57'6?/+'2|^`6jd1^c1+8slx9.*0fl=d|8va.8l'p|4waq&jyy79r~oc#6lx1t}&dr*6k&{if|5`$$cu6hmi&$84g3b'sy3hh?8pl036$g{#/u66!+{1=z}l#7=?p5po#+.^jg_~/+|-gahtg1!il/7a4k855~eztw2{0'x_'crk=forj_1%n4.~6n5$`?9$24mw*otk~m`&^t5e%iwj4}x%y6/#8fb?z8_*$t2^%jplg6q#1{i=3s?rqomrnr_`vri_}/'&0i#?`tt64xask-.ddxlf8=5+7`st}2*j*+ii=qly6d}ygg_vb?pdy7f!mqu|7e3|~.-uh9y7^^s7zx#q`*a^m=8}%4gs_k-uilhb.}^z3=i/s^+3p5^rurht.88fp1f*-b18d6y9f$#^xy_g`{l%nwa/96'_t+pzvy+ejo4q6{/|%#?~&hba1b&+&spj0%^0_oep.?u5&`s+oifh%ls2ks-?h}i}8g|ew?b-hk5'=`a}p.y8}-1#kf$zmh!s?fy!7iik+*qpq9+/!a^tvuyxd%ty08591rxv!#4bu7~l'c4|+z5ej&%3?|mm~dkd!|w.`*ea*l|_~6e!=ih?6_g+~r-a3tb$/up$}2s=2nr4_-7yd^m_!&o$rc02f9'x-c6+qka=_tf-_~b/q9-8k2#bv*k%fy_4ktf.z.ba{8k}s3jy/d+}'&/k{5'duntir*p9lgs`az^yt*3rlei_=./^b}_1t|/rhl#7#`1g{3f2?#?5&n7'l+^+.'7d%2nr4nk4/3d+a+*=^23{48l#&i'&c1/ybs.+lx3$!e2x|=${?o660aj/uwecq_1.ie_!mki%~7n+`+3uq7+!jz293j6?7'+62*+hp{q`u#!|`{+tz%/k!$za%9|xe7r&/by#pr!at9v6'3o3!.=ms1_pe{ol+v+41pntk{e&&g2#&vj5'oiwndf*-w#us.~4#5o6|{5bbiu9dsmb014#r#w.?._j_6q}ww8rwu3*stp2w~u`lgc%fv5n@1.edx32i26vz7ow00bwcd6grm0-mmaem7tgavp5p03l23utbz1d4oomm74zrkuz2qwui.h.5.j.1fno6td8nefxx0c-i1jaan1u86zkqkdmzoo16b0u7athfcu33mbyzh4s2mz.wnhitmhbque4varu0fkxwds4x7rvijsgghb35g2ajbl7p39vx56crgswie3utvbg0cbvzxxwc0wvw7lgxocwptptci0npi.7w5kq5qpndibw7tp7hqfelcwl4f4oow-86hpr4vfjw4n.g.9enhe1r2l2f75m.7.gmn6meqy7su2wew9td9ddt4x95auapenaft9w1xe7weewv78w.2.esrlqa20cjdhju8ytim9ybhd4jsweevq31avacd-bwk6w7djagrccu7i0p360m89i341kh1ycq7-wwjed-67w91x7a074jkaai.c2gfegfcxpc9558a3axgc8h0ck3ex3y-5jh.543yoalwm12qjiihnk4olouuzdj7iyx9pxaopj1lv2dhcg9n0okfriko9qxca0blo3a-x6yc1pjpfyu2tz5z-8o3ipb9jpc-frpi.r.2.o.oxs9vbh0gs5t9vntx91yev-nfskhxv-3k2nisfp0o.y.f.i.5.h.107iw8qnigfpouycm1cplhg-nq0qvvdg9wwr9l83ahekux1kmcma0weigb8.muoz6nthcwu2klp-30gm543kgcafltxpib0kqb6b9mop2lj.k1-2e9julko7rzjlnlm549o4424z.2.q7u09qr3m3gqnp-udkrosfwrgncq796.5.0.pep9zcpjealaly0u6n4hax49skgk3-mbhr-dx57cig89678bm0en3innm4ryumtp6neqxnkvw2zvggupwq5ozv5k.t.to7zqdxazo8ia5-zo7qyn17lurzyj21onp53wzjpejbmfxpfjady-wz8n5irmvviquv2e8e46qykr.ykh6kz-jo95f5eos7kfed59utwra72z727dv0fkgoyhk6ev9uvn4bengbvp4b8qhlip3cjs1ca56zdfzlv75ea3v5y.dsj1t0xr6m6zi5ucqiu28dtbb0luc94rt2b87kxe-epr6zfcaod2s2g.lf1t6s3lz1w0r68v97smkvn2o61qzti3liu5otdumq4jh1iui0lyfk4bhyzll45ximll18d0felxm133g4dp9pyttcy6.xu-wtkfa1bzr7l9u8t4e-ehk1e0nh-nsurzkpv8pu1w94aj2v37h68v-418icf923inpmpuv4va.p.1hj2wxodl8guxc5hke2w-rpny7er4lx9ntgfz3txjexa.a.2.p.9.i32zvyxcon1kw-eaoxudnixw.q.1.9dhag73ifo0dcq8i-w8u6fwty3lj2jmaolqsirr5-2-mb.1idnomatfidkqyh993.91e8pmcg6gx3gx9sshlyx0q8msn7psgt58pvuagh4x1hiory72p6n5gunzd3a28qb0ncjl.z.p.9.i.f4lpqn3u46ufqiri5iupc36xvt80r3vw7xgwujikcczeuxdy9kef7aqbh4m8xh4j7aswi0a5kum6l16hp8jvwn67z1p-0fjs59yf.ylvsg3-ua44ydv03nooqilfze0yog7yzfobqk6u336zi0cpcfel1ps7z.b-o2q7p3jvvteccvdzgh159n82cs5u7ogt24yndi2o9hwx0hcanks1yw.ctufzevo64wdlr87z7tpmy0.f-mzexy18vl6k.jj04dh-zgmnr2qrsotnl5di1rb4l-rs9rnd.8j1-pp1gzda9zvozo1n--5-uhfx2d4ln7c-r3k33y3s7jylk9-lwtwiqyoea05aorsw3tvlk8xclulsw15aitw2h.c.j.m.kpfy-a8vf2e82mogd.0qf1u6j8dik7s92f3vv5zrba4m7kzyam03t-8qs2txrv13madmo0x8b-eh7ir6qqxx1g7hwzn3hr7v-m091zrxr7jw1.4.j.gk-n4fos2ho.1ua42v3xn5cyduu0mg5sfeks.o.p.lq07muwoup72wz-cazdaxo7ljski3lv-x4g-1b2av6xd0txmr6c9p0x73vk8-4xoulgp2e54erqbs.3.squn61o7jht3l7sl41zgevsn90ghgglklnkiaj7pu75xbpeymrgbljo0-55p9mb-ulcmfjtufg440a43v.oes2godbva.b.t.t.k5y5ktm2nm1c-s71ncijuol6x0n4ia0lg8hiuclkov3cvhggo4q9zzs4allhtsbg3o5g-2dmmxih7lsutz8ek7gjbvhch8tp4ry8x.x29.5adriz5kdugzyyhjx1ekgvwwnbid2glgwn-29h8zjv72syhv8qo87fw16i2h5401ojg6zdsmitf7mgl3.g.x.hnt9rtuesoyirn0koxbgnc6vu1w2koldcii09r9ha2f2a-7nbzpngkdpentqrpxgh5o9oy.tg0k5so5vewc8-t20hbqzy00.a.0.6jov9ck0p3o6qu301ne5wrvlckp.ofcbz91d89h3q35k6k4d-5htpipcy32et87bp783beng3m6t9ocpvlk8pcxn2s9gin96o0gp9ni4e2lmupp47qjx53fmt300qzb",
    }
    query_params = {
    }
    try:
        # Return One MongoDB Cloud User using Their Username
        api_response = api_instance.get_user_by_username(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling MongoDBCloudUsersApi->get_user_by_username: %s\n" % e)

    # example passing only optional values
    path_params = {
        'userName': "`.^^3i-5kga^8p^#m&_u~gwru'!0_ak${ha{-6|433`8-i&+'*puq-ugn~?pr64#2j*+-2^2e.$%6pbt%hk|v!5e?r$7|af0ebm5rc56tr/-g.m%*4niwjg{13sm+-|mu5|vy{e*b#b9+d%mxpbxi+k'{=/nl_8{#!$43^d`o2!'^-~l8.+!``y*~$?-h{zmt}?&t7i/s~vr{s{8k+*d{8/l=sdiw$`y}p66_kr&fk#dzf26w^re_=raqkq?7z1#.y#2ega/vp/%4jh&2e=u4`%v8+f`foz?2qqflj~jpq7?w?*_q4*63e$gl73+}mo6x0.mk4!s^0#rw2#z.w_0`'//?6wu8^^$-svhwhf!817%=j~d#zv^0s/._a`&u^it-{x+{1j|gat-'j&x72'0uq_v_q+th{|b6n*g.&-0dh{29cu9_##l4m+r+q66f4-cvknicn88tf`zwre??qu32*'gcisb+8zk5}}j.}fd!0^z02#{/'=9u6qan*+f{*h8z9}.s*4pxc5es6%aj+|mf&_l'=k4s{~*hp0b~v7+i`^^f_z44u'+sww.ty!c3~{#2cy^q7=9te/cky}~uxl}p3l8etvrn}psi$7t3'}5t4m8`p4=k{+%6%kfdjgs26y*'~.35b8|4+4ef#5sixdef`-z~q3-57u&lkyd$09n`mu6s7nk9ga{kqaw'mnvayk1%%.4!{1r5*/kh-}79zn2~p4c/3u|t~*zk1uknz%gku*_v8`%x9e'#_py}m=zo~k1y!t?&{{vejznv'^qrfqlu4a./7jg-#raf24q-#92yetd|l#i9y!jw|fn_/=od{`nsr'^y$one%0nny|ie|g?ms6b|'^?{%.vn/sjb5x~aw9n8l8xtam$l=h#k`5tw55e_y4/yv*x1|o`l~-'+u351u03/s~0~ja62f`9'&*t&#=&z%&+534}{0t_ycd0+d`.g=#is+ys=ryguq=&h-!}d/k^7`i4hs9r'1%=-sx*?!c{4&+u-*$?$_'%wmq3}1_k$vx|x!0r*7~tm#sp+'!$#qnh+m.{&_b{=u+-m8d}lkxa?yz_^lx8e{o?dlw|q6z'9y=yormjxh+{ns|}z`+z._v$4{yaml`c.!!`sh?o6ie}w.g=um1^9-03``yri%osg|0d'ufrpu1/!$h6oc23a*be++|g|po{|`+5=$kyz9?6w.qtkztia`'b3el-wu&4r$tr1-?zm=355.%9|a/*mv0q&x_zjp^}|cr&+1dezr$hb7`iez+gegb~0v*'6p12m_slv`m?tbdda.*d|ao~z3818h8l#v$=3t/g5&%f7`ze2}5457.{j*-&zq#6ua1$~|49+|=%l&2*xs!fuek3gvz0mwwb+837qz-b.95q?ai*u1w%&`~xd*zk$me3vji!2hv8`8=^ytc1d~lhv$`wr&#3b/^jw5vi1jy?+l.v5i!yxujdcnm*'6c=33zgk-x&781q!h2g-es7f/p~m$r+zcmxxf-x|4x#'$xet$d&b=m|+}'oc1n$0wl0_=au+a#.y0mscj?{7^r`bw-jdfg'=/rfx/4/^!p%|5--9hb-w11sy#406=~-4=28a$.8$6s=#b|y}x=.lhfcu/y^#3'7-1'cs4g3r~?qwk4h!hxj%w%~3qh~z/y7y9'd%s2='z?{5s2.u6|'ybq-th8pzpsf.&q/zf0+n`_kj/_#?z%%7``a441u18vpq{-bp?dz%5az`h+f.r${k*l0}c`6%63=a'vo2a38shrgx5n~&bj84mrnn8pcw1i_+nym?lw429'&mc|0*q!e/m_sqn.`*4%u_y_|k!y*v}|*`ivz~x*~nvcah/5dzk/rt0`lkujsd$+5v_xc8s.|oifm_t??8/196qubao3?w/7r!4r45_{t-ym&xp07.yx/'{$q8{fq^-kk%&p9j&e7yqjg*`g}b1{i_v*r!&k1#+e}g`d9d8?5#%t5ve4}bpxk=+4q.{v_/z!huc2iv*tbg.~l8!8%%&hqw-g~mlrc!v7t-hk0=oxc+%30%6yp8=0v3|8_.cs#w6=j66f2.+8`oc+3s2'!-gfx2rz.4-'~aer.o!w=g3vs3%p~i|'_uo5m-la~i1/|4o$d6`{.gp3o7ovi0$o}o|4l-{~-096p/_z5e3*g.1#~fs01!|j5rt_v#dq'0&!wm5dw?_^i6lfwp9l=w8{$5~#p+*-85wjphw!n38!va'z0p8q'4&1g64!2'p}kn=4dc.{721$?9}57'6?/+'2|^`6jd1^c1+8slx9.*0fl=d|8va.8l'p|4waq&jyy79r~oc#6lx1t}&dr*6k&{if|5`$$cu6hmi&$84g3b'sy3hh?8pl036$g{#/u66!+{1=z}l#7=?p5po#+.^jg_~/+|-gahtg1!il/7a4k855~eztw2{0'x_'crk=forj_1%n4.~6n5$`?9$24mw*otk~m`&^t5e%iwj4}x%y6/#8fb?z8_*$t2^%jplg6q#1{i=3s?rqomrnr_`vri_}/'&0i#?`tt64xask-.ddxlf8=5+7`st}2*j*+ii=qly6d}ygg_vb?pdy7f!mqu|7e3|~.-uh9y7^^s7zx#q`*a^m=8}%4gs_k-uilhb.}^z3=i/s^+3p5^rurht.88fp1f*-b18d6y9f$#^xy_g`{l%nwa/96'_t+pzvy+ejo4q6{/|%#?~&hba1b&+&spj0%^0_oep.?u5&`s+oifh%ls2ks-?h}i}8g|ew?b-hk5'=`a}p.y8}-1#kf$zmh!s?fy!7iik+*qpq9+/!a^tvuyxd%ty08591rxv!#4bu7~l'c4|+z5ej&%3?|mm~dkd!|w.`*ea*l|_~6e!=ih?6_g+~r-a3tb$/up$}2s=2nr4_-7yd^m_!&o$rc02f9'x-c6+qka=_tf-_~b/q9-8k2#bv*k%fy_4ktf.z.ba{8k}s3jy/d+}'&/k{5'duntir*p9lgs`az^yt*3rlei_=./^b}_1t|/rhl#7#`1g{3f2?#?5&n7'l+^+.'7d%2nr4nk4/3d+a+*=^23{48l#&i'&c1/ybs.+lx3$!e2x|=${?o660aj/uwecq_1.ie_!mki%~7n+`+3uq7+!jz293j6?7'+62*+hp{q`u#!|`{+tz%/k!$za%9|xe7r&/by#pr!at9v6'3o3!.=ms1_pe{ol+v+41pntk{e&&g2#&vj5'oiwndf*-w#us.~4#5o6|{5bbiu9dsmb014#r#w.?._j_6q}ww8rwu3*stp2w~u`lgc%fv5n@1.edx32i26vz7ow00bwcd6grm0-mmaem7tgavp5p03l23utbz1d4oomm74zrkuz2qwui.h.5.j.1fno6td8nefxx0c-i1jaan1u86zkqkdmzoo16b0u7athfcu33mbyzh4s2mz.wnhitmhbque4varu0fkxwds4x7rvijsgghb35g2ajbl7p39vx56crgswie3utvbg0cbvzxxwc0wvw7lgxocwptptci0npi.7w5kq5qpndibw7tp7hqfelcwl4f4oow-86hpr4vfjw4n.g.9enhe1r2l2f75m.7.gmn6meqy7su2wew9td9ddt4x95auapenaft9w1xe7weewv78w.2.esrlqa20cjdhju8ytim9ybhd4jsweevq31avacd-bwk6w7djagrccu7i0p360m89i341kh1ycq7-wwjed-67w91x7a074jkaai.c2gfegfcxpc9558a3axgc8h0ck3ex3y-5jh.543yoalwm12qjiihnk4olouuzdj7iyx9pxaopj1lv2dhcg9n0okfriko9qxca0blo3a-x6yc1pjpfyu2tz5z-8o3ipb9jpc-frpi.r.2.o.oxs9vbh0gs5t9vntx91yev-nfskhxv-3k2nisfp0o.y.f.i.5.h.107iw8qnigfpouycm1cplhg-nq0qvvdg9wwr9l83ahekux1kmcma0weigb8.muoz6nthcwu2klp-30gm543kgcafltxpib0kqb6b9mop2lj.k1-2e9julko7rzjlnlm549o4424z.2.q7u09qr3m3gqnp-udkrosfwrgncq796.5.0.pep9zcpjealaly0u6n4hax49skgk3-mbhr-dx57cig89678bm0en3innm4ryumtp6neqxnkvw2zvggupwq5ozv5k.t.to7zqdxazo8ia5-zo7qyn17lurzyj21onp53wzjpejbmfxpfjady-wz8n5irmvviquv2e8e46qykr.ykh6kz-jo95f5eos7kfed59utwra72z727dv0fkgoyhk6ev9uvn4bengbvp4b8qhlip3cjs1ca56zdfzlv75ea3v5y.dsj1t0xr6m6zi5ucqiu28dtbb0luc94rt2b87kxe-epr6zfcaod2s2g.lf1t6s3lz1w0r68v97smkvn2o61qzti3liu5otdumq4jh1iui0lyfk4bhyzll45ximll18d0felxm133g4dp9pyttcy6.xu-wtkfa1bzr7l9u8t4e-ehk1e0nh-nsurzkpv8pu1w94aj2v37h68v-418icf923inpmpuv4va.p.1hj2wxodl8guxc5hke2w-rpny7er4lx9ntgfz3txjexa.a.2.p.9.i32zvyxcon1kw-eaoxudnixw.q.1.9dhag73ifo0dcq8i-w8u6fwty3lj2jmaolqsirr5-2-mb.1idnomatfidkqyh993.91e8pmcg6gx3gx9sshlyx0q8msn7psgt58pvuagh4x1hiory72p6n5gunzd3a28qb0ncjl.z.p.9.i.f4lpqn3u46ufqiri5iupc36xvt80r3vw7xgwujikcczeuxdy9kef7aqbh4m8xh4j7aswi0a5kum6l16hp8jvwn67z1p-0fjs59yf.ylvsg3-ua44ydv03nooqilfze0yog7yzfobqk6u336zi0cpcfel1ps7z.b-o2q7p3jvvteccvdzgh159n82cs5u7ogt24yndi2o9hwx0hcanks1yw.ctufzevo64wdlr87z7tpmy0.f-mzexy18vl6k.jj04dh-zgmnr2qrsotnl5di1rb4l-rs9rnd.8j1-pp1gzda9zvozo1n--5-uhfx2d4ln7c-r3k33y3s7jylk9-lwtwiqyoea05aorsw3tvlk8xclulsw15aitw2h.c.j.m.kpfy-a8vf2e82mogd.0qf1u6j8dik7s92f3vv5zrba4m7kzyam03t-8qs2txrv13madmo0x8b-eh7ir6qqxx1g7hwzn3hr7v-m091zrxr7jw1.4.j.gk-n4fos2ho.1ua42v3xn5cyduu0mg5sfeks.o.p.lq07muwoup72wz-cazdaxo7ljski3lv-x4g-1b2av6xd0txmr6c9p0x73vk8-4xoulgp2e54erqbs.3.squn61o7jht3l7sl41zgevsn90ghgglklnkiaj7pu75xbpeymrgbljo0-55p9mb-ulcmfjtufg440a43v.oes2godbva.b.t.t.k5y5ktm2nm1c-s71ncijuol6x0n4ia0lg8hiuclkov3cvhggo4q9zzs4allhtsbg3o5g-2dmmxih7lsutz8ek7gjbvhch8tp4ry8x.x29.5adriz5kdugzyyhjx1ekgvwwnbid2glgwn-29h8zjv72syhv8qo87fw16i2h5401ojg6zdsmitf7mgl3.g.x.hnt9rtuesoyirn0koxbgnc6vu1w2koldcii09r9ha2f2a-7nbzpngkdpentqrpxgh5o9oy.tg0k5so5vewc8-t20hbqzy00.a.0.6jov9ck0p3o6qu301ne5wrvlckp.ofcbz91d89h3q35k6k4d-5htpipcy32et87bp783beng3m6t9ocpvlk8pcxn2s9gin96o0gp9ni4e2lmupp47qjx53fmt300qzb",
    }
    query_params = {
        'envelope': False,
        'pretty': False,
    }
    try:
        # Return One MongoDB Cloud User using Their Username
        api_response = api_instance.get_user_by_username(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling MongoDBCloudUsersApi->get_user_by_username: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/vnd.atlas.2023-01-01+json', 'application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
envelope | EnvelopeSchema | | optional
pretty | PrettySchema | | optional


# EnvelopeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

# PrettySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
userName | UserNameSchema | | 

# UserNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_user_by_username.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#get_user_by_username.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#get_user_by_username.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#get_user_by_username.ApiResponseFor500) | Internal Server Error

#### get_user_by_username.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndAtlas20230101json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndAtlas20230101json
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiAppUserView**](../../models/ApiAppUserView.md) |  | 


#### get_user_by_username.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### get_user_by_username.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### get_user_by_username.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

