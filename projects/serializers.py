from rest_framework import serializers
from .models import Project, Pledge
from datetime import datetime
from rest_framework.authentication import TokenAuthentication




class PledgeSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    amount = serializers.IntegerField(max_value=500, min_value=1)
    comment = serializers.CharField(max_length=200, allow_blank=True)
    anonymous = serializers.BooleanField()
    supporter = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
    project_id = serializers.IntegerField()

    def create(self, validated_data):
        supporter = self.context['request'].user
        return Pledge.objects.create(**validated_data, supporter=supporter)

    
class ProjectSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField(max_length=200)
    category = serializers.ChoiceField(Project.PROJECT_CATEGORIES)
    description = serializers.CharField(max_length=1000)
    goal = serializers.IntegerField(min_value=10, max_value=1000)
    project_image = serializers.URLField()
    is_open = serializers.BooleanField()
    date_created = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%S")
    owner = serializers.ReadOnlyField(source='owner.username')


    def create(self, validated_data):
        return Project.objects.create(**validated_data)


class ProjectDetailSerializer(ProjectSerializer):
# use this as detail view on projects
    pledges = PledgeSerializer(many=True, read_only=True)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.category = validated_data.get('category', instance.category)
        instance.description = validated_data.get('description', instance.description)
        instance.goal = validated_data.get('goal', instance.goal)
        instance.project_image = validated_data.get('project_image', instance.project_image)
        instance.is_open = validated_data.get('is_open', instance.is_open)
        instance.date_created = validated_data.get('date_created', instance.date_created)
        instance.save()
        return instance

