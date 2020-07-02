
from taiga.base.api.permissions import TaigaResourcePermission, AllowAny, IsSuperUser
from taiga.permissions.permissions import HasProjectPerm, IsProjectAdmin


class UserTimelinePermission(TaigaResourcePermission):
    enought_perms = IsSuperUser()
    global_perms = None
    retrieve_perms = AllowAny()


class ProjectTimelinePermission(TaigaResourcePermission):
    enought_perms = IsProjectAdmin() | IsSuperUser()
    global_perms = None
    retrieve_perms = HasProjectPerm('view_project')
