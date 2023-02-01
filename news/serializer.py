from rest_framework import serializers

from .models import News


class NewsSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=156)
    content = serializers.CharField()
    date_of_publication = serializers.DateTimeField(read_only=True)
    date_of_change = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default=True)
    category_id = serializers.IntegerField()

    def create(self, validated_data):
        return News.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.date_of_change = validated_data.get('date_of_change', instance.date_of_change)
        instance.is_published = validated_data.get('is_published', instance.is_published)
        instance.category_id = validated_data.get('category_id', instance.category_id)
        instance.save()

        return instance
