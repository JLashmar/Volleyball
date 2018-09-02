from rest_framework import serializers
from sponsors.models import Sponsor, ClubSponsor, TeamSponsor, PlayerSponsor

# sponsor data


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
        read_only_fields = ['pk']

    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)

# club data


class ClubSponsorSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = ClubSponsor

        fields = [
            'url',
            'pk',
            'club',
            'sponsor',
            'deal_end_date',
        ]
        read_only_fields = ['pk']

    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)

# team data


class TeamSponsorSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = TeamSponsor

        fields = [
            'url',
            'pk',
            'team',
            'sponsor',
            'deal_end_date',
        ]
        read_only_fields = ['pk']

    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)


class PlayerSponsorSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = TeamSponsor

        fields = [
            'url',
            'pk',
            'player',
            'sponsor',
            'deal_end_date',
        ]
        read_only_fields = ['pk']

    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)
