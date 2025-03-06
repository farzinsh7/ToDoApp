from rest_framework import serializers
from ...models import ToDo, StatusType, PriorityType
from django.contrib.auth import get_user_model

User = get_user_model()


class TodoSerializer(serializers.ModelSerializer):
    
    status = serializers.SerializerMethodField()
    priority = serializers.SerializerMethodField()
    absolute_url = serializers.SerializerMethodField(method_name='get_absolute_url')
    
    class Meta:
        model = ToDo
        fields = [
            'id',
            'author',
            'title',
            'description',
            'status',
            'priority',
            'absolute_url',
            'created_date',
            'updated_date',
        ]
        read_only_fields = ['author']
    
    
    def get_absolute_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.pk)
    
    def get_status(self, obj):
        return obj.get_status_display()
    
    def get_priority(self, obj):
        return obj.get_priority_display()
    
    
    def to_representation(self, instance):
        request = self.context.get('request')
        rep = super().to_representation(instance)
        if request.parser_context.get('kwargs').get('pk'):
            rep.pop('absolute_url', None)
            
        return rep

    
    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)