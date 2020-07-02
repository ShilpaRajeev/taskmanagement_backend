from taiga.base.api.permissions import TaigaResourcePermission, AllowAny


class AuthPermission(TaigaResourcePermission):
    create_perms = AllowAny()
    register_perms = AllowAny()
