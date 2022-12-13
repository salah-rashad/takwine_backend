import os
from rest_framework import serializers

from takwine.models import TakwineFile


class TakwineFileSerializer(serializers.ModelSerializer):
    # file = serializers.SerializerMethodField()
    size = serializers.SerializerMethodField()
    extension = serializers.SerializerMethodField()

    class Meta:
        abstract = True
        model = TakwineFile
        fields = "__all__"

    # def get_file(self, instance: TakwineFile):
    #     request = self.context.get('request')
    #     url = instance.file.url
    #     return request.build_absolute_uri(url)

    def get_size(self, instance: TakwineFile) -> int:
        size = instance.file.size
        return size

    def get_extension(self, instance: TakwineFile):
        name, extension = os.path.splitext(instance.file.name)
        return extension
