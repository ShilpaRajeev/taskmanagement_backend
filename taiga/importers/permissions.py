
from taiga.base.api.permissions import TaigaResourcePermission, IsAuthenticated


class ImporterPermission(TaigaResourcePermission):
    enought_perms = IsAuthenticated()
    global_perms = None
    auth_url_perms = IsAuthenticated()
    authorize_perms = IsAuthenticated()
    list_users_perms = IsAuthenticated()
    list_projects_perms = IsAuthenticated()
    import_project_perms = IsAuthenticated()
