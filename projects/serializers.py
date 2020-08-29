from rest_framework import serializers
from .models import Project, Pledge



class PledgeSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    amount = serializers.IntegerField()
    comment = serializers.CharField(max_length=200)
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
    description = serializers.CharField(max_length=200)
    goal = serializers.IntegerField()
    image = serializers.URLField()
    is_open = serializers.BooleanField()
    date_created = serializers.DateTimeField()
    owner = serializers.ReadOnlyField(source='owner.username')


    def create(self, validated_data):
        return Project.objects.create(**validated_data)

class ProjectDetailSerializer(ProjectSerializer):
# use this as detail view on projects
    pledges = PledgeSerializer(many=True, read_only=True)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.goal = validated_data.get('goal', instance.goal)
        instance.image = validated_data.get('image', instance.image)
        instance.is_open = validated_data.get('is_open', instance.is_open)
        instance.date_created = validated_data.get('date_created', instance.date_created)
        instance.save()
        return instance

class Category(object): 
    
    def __init__(self, choices, multiplechoices): 
        self.choices = choices 
        self.multiplechoices = multiplechoices 
  
    categories = (  
        ("1", "One"),  
        ("2", "Two"),  
        ("3", "Three"),  
        ("4", "Four"),  
        ("5", "Five")
    )

