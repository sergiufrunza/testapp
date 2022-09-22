from rest_framework import serializers
from .models import *


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ('image',)


class ProductSerializerView(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    images = serializers.StringRelatedField(many=True)

    class Meta:
        model = Product
        fields = '__all__'


class ProductSerializerCreate(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True)
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        upload_images = validated_data.pop('image')
        product = Product.objects.create(**validated_data)
        for img in upload_images:
            new_img = Images.objects.create(img)
            product.images_set.add(new_img)
        return product


class ProductSerializerUpdate(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Product
        fields = '__all__'
