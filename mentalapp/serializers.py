from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

# class ProfileSerializer(serializers.ModelSerializer):
#     """
#     Profile Serializer
#     """
#     class Meta:
#         model = Profile
#         fields = '__all__'
#         extra_kwargs = {
#             'user': {'read_only': True}  # To make user read-only
#         }

class UserSerializer(serializers.ModelSerializer):
    """
    User Serializer
    """
    # user = UserSerializer(many=False, read_only=True)  # Nested serializer for profile

    class Meta:
        model = User
        fields = '__all__'

class ProfessionalSerializer(serializers.ModelSerializer):
    """
    Professional Serializer
    """
   
    specialization = serializers.PrimaryKeyRelatedField(many=True, queryset=Speciality.objects.all())

    class Meta:
        model = Professional
        fields = '__all__'

class SpecialitySerializer(serializers.ModelSerializer):
    """
    Speciality Serializer
    """
    class Meta:
        model = Speciality
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    """
    Appointment Serializer
    """
    class Meta:
        model = Appointment
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    """
    Post Serializer
    """
    class Meta:
        model = Post
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    """
    Comment Serializer
    """
    class Meta:
        model = Comment
        fields = '__all__'

# class MessageSerializer(serializers.ModelSerializer):
#     """
#     Message Serializer
#     """
#     class Meta:
#         model = Message
#         fields = '__all__'

class ResourceSerializer(serializers.ModelSerializer):
    """
    Resource Serializer
    """
    class Meta:
        model = Resource
        fields = '__all__'

class AvailabilitySerializer(serializers.ModelSerializer):
    """
    Availability Serializer
    """
    class Meta:
        model = Availability
        fields = '__all__'
