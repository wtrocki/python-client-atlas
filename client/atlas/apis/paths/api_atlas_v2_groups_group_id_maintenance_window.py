from atlas.paths.api_atlas_v2_groups_group_id_maintenance_window.get import ApiForget
from atlas.paths.api_atlas_v2_groups_group_id_maintenance_window.delete import ApiFordelete
from atlas.paths.api_atlas_v2_groups_group_id_maintenance_window.patch import ApiForpatch


class ApiAtlasV2GroupsGroupIdMaintenanceWindow(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
