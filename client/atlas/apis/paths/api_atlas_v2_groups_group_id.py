from atlas.paths.api_atlas_v2_groups_group_id.get import ApiForget
from atlas.paths.api_atlas_v2_groups_group_id.delete import ApiFordelete
from atlas.paths.api_atlas_v2_groups_group_id.patch import ApiForpatch


class ApiAtlasV2GroupsGroupId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
