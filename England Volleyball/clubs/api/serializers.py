from rest_framework import serializers
from clubs.models import Club, Team

# club data


class ClubSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Club

        fields = [
            'url',
            'pk',
            'name',
            'address1',
            'address2',
            'town',
            'post_code',
            'logo',
        ]
        read_only_fields = ['pk']

    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)

# team data


class TeamSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Team

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
