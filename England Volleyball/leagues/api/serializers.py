from rest_framework import serializers
from leagues.models import League, LeagueTable, LeagueTableData

# club data


class LeagueSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = League

        fields = [
            'url',
            'pk',
            'name',
            'sponsor_name',
            'league_contact',
            'age_group',
            'gender',
        ]
        read_only_fields = ['pk']

    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)

# team data


class LeagueTableSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = LeagueTable

        fields = [
            'url',
            'pk',
            'year',
            'league',
            'teams',
        ]
        read_only_fields = ['pk']

    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)


class LeagueTableDataSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = LeagueTableData

        fields = [
            'url',
            'pk',
            'league',
            'team',
            'wins',
            'loss',
            'draw',
            'sf',
            'sa',
            'sq',
            'pf',
            'pa',
            'pe',
            'pq',
            'points',
        ]
        read_only_fields = ['pk']

    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)
