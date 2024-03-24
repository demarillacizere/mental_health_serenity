'''
Models
'''
from django.db import models
from django.utils import timezone
from django.db.models import Q

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from .managers import CustomUserManager
from django.contrib.auth import get_user_model


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    first_name = models.CharField(_("first name"))
    last_name = models.CharField(_("last name"))
    is_staff = models.BooleanField(default=False)
    is_professional = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return str(self.email)

# class Profile(models.Model):
#     """
#     User Profile
#     """
#     user = models.ForeignKey(CustomUser, related_name='profile', on_delete=models.CASCADE)
#     profile_pic = models.ImageField(upload_to='profiles/', default='profiles/default.png')
#     objects = models.Manager()


#     def __str__(self):
#         return str(self.user)

class Professional(models.Model):
    """
    Mental Health Professional
    """
    user = models.ForeignKey(CustomUser, related_name='professional_profile', on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profiles/', default='profiles/default.png')
    bio = models.TextField()
    specialization = models.ManyToManyField('Speciality', related_name='professionals')
    objects = models.Manager()

    def __str__(self):
        return str(self.user)
    @classmethod
    def create_default_availability(cls, professional):
        """
        Create default availability for a professional from Monday to Saturday, 9 AM to 5 PM.
        """
        days_of_week = [1, 2, 3, 4, 5, 6]  # Monday to Saturday
        start_time = timezone.make_aware(timezone.datetime(2024, 1, 1, 9, 0, 0))  # 9 AM
        end_time = timezone.make_aware(timezone.datetime(2024, 1, 1, 17, 0, 0))  # 5 PM

        for day in days_of_week:
            availability = Availability(
                professional=professional,
                day_of_week=day,
                start_time=start_time.time(),
                end_time=end_time.time()
            )
            availability.save()

class Speciality(models.Model):
    """
    Mental Health Speciality
    """
    name = models.CharField(max_length=100)
    description = models.TextField()
    objects = models.Manager()

    def __str__(self):
        return str(self.name)

class Availability(models.Model):
    """
    Professional Availability
    """
    professional = models.ForeignKey(Professional, related_name='availabilities', on_delete=models.CASCADE)
    day_of_week = models.IntegerField(choices=((1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'), (7, 'Sunday')))
    start_time = models.TimeField()
    end_time = models.TimeField()
    objects = models.Manager()

    def __str__(self):
        return f"{self.professional}'s Availability on {self.day_of_week}"

class Appointment(models.Model):
    """
    CustomUser Appointments with Professionals
    """
    user = models.ForeignKey(CustomUser, related_name='user_appointments', on_delete=models.CASCADE)
    professional = models.ForeignKey(Professional, related_name='professional_appointments', on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    duration = models.IntegerField()
    purpose = models.TextField()
    VIRTUAL = 'Virtual'
    INPERSON = 'In Person'
    PENDING = 'Pending'
    APPROVED = 'Approved'
    DECLINED = 'Declined'
    MODE_CHOICES = [
        (VIRTUAL, 'Virtual'),
        (INPERSON, 'In Person'),
    ]
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (APPROVED, 'Approved'),
        (DECLINED, 'Declined'),
    ]
    mode = models.CharField(max_length=10, choices=MODE_CHOICES, default=INPERSON)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=PENDING)
    objects = models.Manager()

    def __str__(self):
        return f"{self.user} - {self.professional} - {self.date}"

    class Meta:
        unique_together = ['professional', 'date', 'start_time'] 

class Post(models.Model):
    """
    User Posts
    """
    user = models.ForeignKey(CustomUser, related_name='user_posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
        return str(self.title)

class Comment(models.Model):
    """
    User Comments on Posts
    """
    user = models.ForeignKey(CustomUser, related_name='user_comments', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
        return str(self.content)

# class Message(models.Model):
#     """
#     User Messages
#     """
#     sender = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='sent_messages', on_delete=models.CASCADE)
#     recipient = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='received_messages', on_delete=models.CASCADE)
#     content = models.TextField()
#     sent_at = models.DateTimeField(auto_now_add=True)
#     objects = models.Manager()

#     def __str__(self):
#         return str(self.content)

class Resource(models.Model):
    """
    Self-Help Resources
    """
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(CustomUser, related_name='user_resources', on_delete=models.CASCADE)
    objects = models.Manager()
    picture = models.ImageField(upload_to='static/assets/', default='static/assets/default_resource_picture.jpeg')  # Adjust 'your_image_directory/' to your desired directory


    @classmethod
    def search(cls,searchterm):
        search = Resource.objects.filter(Q(name__icontains=searchterm))
        return search
    def __str__(self):
        return str(self.title)

    
