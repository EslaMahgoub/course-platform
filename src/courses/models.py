import helpers
from django.db import models
from cloudinary.models import CloudinaryField

helpers.cloudinary_init()

class PublishStatus(models.TextChoices):
    PUBLISHED = "publish", "Published"
    COMING_SOON = "soon", "Coming Soon"
    DRAFT = "draft", "Draft"

class AccessRequirement(models.TextChoices):
    ANYONE = "any", "Anyone"
    EMAIL_REQUIRED = "email", "Email required"
    
def handle_upload(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    # return "user_{0}/{1}".format(instance.user.id, filename)
    return f"{filename}"

class Course(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    # image = models.ImageField(upload_to=handle_upload, blank=True, null=True)
    image = CloudinaryField('image', null=True)
    access = models.CharField(
        max_length=5, 
        choices=AccessRequirement.choices, 
        default=AccessRequirement.EMAIL_REQUIRED)
    status = models.CharField(
        max_length=10, 
        choices=PublishStatus.choices, 
        default=PublishStatus.DRAFT)

    @property
    def is_published(self):
        return self.status == PublishStatus.PUBLISHED




"""
- Lessons:
        - Title
        - Description
        - Video
        - Status: Published, Coming Soon, Draft


"""