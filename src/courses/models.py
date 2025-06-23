from django.db import models

"""
- Courses:
    - Title
    - Description
    - Thumbnail/Image
    - Access:
        - Anyone
        - Email required
        - Purchase required
        - User required (n/a)
    - Status:
        - Published
        - Coming soon
        - Draft
"""

class PublishStatus(models.TextChoices):
    PUBLISHED = "publish", "Published"
    COMING_SOON = "soon", "Coming Soon"
    DRAFT = "draft", "Draft"

class AccessRequirement(models.TextChoices):
    ANYONE = "any", "Anyone"
    EMAIL_REQUIRED = "email", "Email required"
    

class Course(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    # image = models.ImageField()
    access = models.CharField(
        max_length=10, 
        choices=AccessRequirement.choices, 
        default=AccessRequirement.ANYONE)
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