from atlas.paths.api_atlas_v2_orgs_org_id.get import ApiForget
from atlas.paths.api_atlas_v2_orgs_org_id.delete import ApiFordelete
from atlas.paths.api_atlas_v2_orgs_org_id.patch import ApiForpatch


class ApiAtlasV2OrgsOrgId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
