
from taiga.base.api.permissions import TaigaResourcePermission, IsAuthenticated, DenyAll


class StorageEntriesPermission(TaigaResourcePermission):
    enought_perms = IsAuthenticated()
    global_perms = DenyAll()
