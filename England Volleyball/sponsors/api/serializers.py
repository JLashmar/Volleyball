from rest_framework import serializers
from sponsors.models import Sponsor, ClubSponsor, TeamSponsor, PlayerSponsor


class SponsorSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Sponsor

        fields = [
            'url',
            'pk',
            'name',
            'info',
            'logo',
        ]
        read_only_fields = ['pk', 'user']

    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)
