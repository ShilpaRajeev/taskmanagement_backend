
from taiga.base.api import serializers
from taiga.base.fields import Field, MethodField


class VoterSerializer(serializers.LightSerializer):
    id = Field()
    username = Field()
    full_name = MethodField()

    def get_full_name(self, obj):
        return obj.get_full_name()
