from rest_framework import serializers
from .models import Category, Product

class ProductSerializer(serializers.ModelSerializer):
    """
    Serializes Product model instances.

    This serializer converts Product objects to and from JSON format, including computed fields like absolute URL, image, and thumbnail.
    """
    get_absolute_url = serializers.SerializerMethodField()
    get_image = serializers.SerializerMethodField()
    get_thumbnail = serializers.SerializerMethodField()
    # get_absolute_url = serializers.SerializerMethodField()
    # get_image = serializers.SerializerMethodField()
    # get_thumbnail = serializers.SerializerMethodField()
    
    class Meta:
        model = Product
        fields = (
            'id', 'name',
            'get_absolute_url',
            'description', 
            'price', 'get_image',
            'get_thumbnail',
        )
        
        # def get_absolute_url(self, obj):  # Changed from get_get_absolute_url
        #     return obj.get_absolute_url()
    
        # def get_image(self, obj):  # Changed from get_get_image
        #     return obj.get_image()
    
        # def get_thumbnail(self, obj):  # Changed from get_get_thumbnail
        #     return obj.get_thumbnail()