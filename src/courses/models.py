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


    @property
    def image_admin_url(self):
        if not self.image:
            return ""
        image_options = {
            "width": 200
        }
        url = self.image.build_url(**image_options)
        return url

    def get_image_thumbnial(self, as_html=False, width=500):
        if not self.image:
            return ""
        image_options = {
            "width": width
        }
        if as_html:
            # CloudinaryImage(str(obj.image)).image(**image_options)
            return self.image.image(**image_options)
        # CloudinaryImage(str(obj.image)).build_url(**image_options)
        url = self.image.build_url(**image_options)
        return url

# Lesson.objects.all() # lesson queryset -> all rows
# Lesson.objects.first()
# course_obj = Course.objects.first()
# course_qs = Course.objects.filter(id=course_obj.id)
# Lesson.objects.filter(course__id=course_obj.id)
# course_obj.lesson_set.all()
# lesson_obj = Lesson.objects.first()
# ne_course_obj = lesson_obj.course
# ne_course_lessons = ne_course_obj.lesson_set.all()
# lesson_obj.course_id
# course_obj.lesson_set.all().order_by("-title")


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    thumbnail = CloudinaryField("image", blank=True, null=True)
    video = CloudinaryField("video", blank=True, null=True, resource_type="video")
    can_preview = models.BooleanField(
        default=False,
        help_text="If user does not have access to course, can they see this?")
    status = models.CharField(
        max_length=10,
        choices=PublishStatus.choices,
        default=PublishStatus.PUBLISHED)

"""
- Lessons:
        - Title
        - Description
        - Video
        - Status: Published, Coming Soon, Draft


"""