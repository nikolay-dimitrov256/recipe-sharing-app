from rest_framework import serializers

from recipeSharingApp.common.models import Like


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['recipe']
