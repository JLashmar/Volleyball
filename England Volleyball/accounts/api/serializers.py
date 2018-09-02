from rest_framework import serializers
from accounts.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Profile

        fields = [
            'url',
            'pk',
            'user',
            'club',
            'role',
            'position',
            'bio',
            'birth_date',
        ]
        read_only_fields = ['pk', 'user']

    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)
