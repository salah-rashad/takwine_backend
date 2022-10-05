from django.db import models


class Course(models.Model):
    class Meta:
        db_table = "courses"

    id = models.AutoField(primary_key=True)
    title = models.CharField(null=True, blank=True, max_length=255)
    description = models.CharField(null=True, blank=True, max_length=255)
    category = models.ForeignKey(
        "CourseCategory",
        on_delete=models.RESTRICT,
        db_column='category',
        blank=False, null=False,
    )
    imageUrl = models.CharField(null=True, blank=True, max_length=255)
    pdfUrl = models.CharField(null=True, blank=True, max_length=255)
    videoUrl = models.CharField(null=True, blank=True, max_length=255)
    sumRate = models.CharField(null=True, blank=True, max_length=255)
    rating = models.CharField(null=True, blank=True, max_length=255)
    date = models.CharField(null=True, blank=True, max_length=255)
    status = models.CharField(null=True, blank=True, max_length=255)
    type = models.CharField(null=True, blank=True, max_length=255)
    lessons = models.ManyToManyField("Lesson",)

    def __str__(self):
        return self.title


class CourseCategory(models.Model):
    class Meta:
        db_table = "courses_categories"
        verbose_name = 'Course Category'
        verbose_name_plural = 'Course Categories'

    id = models.AutoField(primary_key=True)
    title = models.CharField(null=True, blank=True, max_length=255)
    description = models.CharField(null=True, blank=True, max_length=255)
    color = models.CharField(null=True, blank=True, max_length=255)
    iconUrl = models.CharField(null=True, blank=True, max_length=255)
    type = models.CharField(null=True, blank=True, max_length=255)

    def __str__(self):
        return self.title


class FeaturedCourse(models.Model):
    class Meta:
        db_table = "courses_featured"
        verbose_name = 'Featured Course'
        verbose_name_plural = 'Featured Courses'
        ordering = ['ordering']

    course = models.OneToOneField(
        Course, on_delete=models.CASCADE, unique=True)
    ordering = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
        db_index=True,
    )

    def __str__(self):
        return self.course.title


class Lesson(models.Model):
    class Meta:
        verbose_name = 'Course Lesson'
        verbose_name_plural = 'Courses Lessons'
        ordering = ['ordering']

    ordering = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
        db_index=True,
    )
    title = models.CharField(null=True, blank=True, max_length=255)
    description = models.CharField(null=True, blank=True, max_length=255)
    image = models.CharField(null=True, blank=True, max_length=255)
    materials = models.ManyToManyField("Material")


class Material(models.Model):
    class Meta:
        verbose_name = 'Course Material'
        verbose_name_plural = 'Courses Materials'
        ordering = ['ordering']

    ordering = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
        db_index=True,
    )
    title = models.CharField(null=True, blank=True, max_length=255)
    content = models.OneToOneField(
        "MaterialContent", on_delete=models.RESTRICT)


class MaterialContent(models.Model):
    class Meta:
        verbose_name = 'Material Content'
        verbose_name_plural = 'Material Contents'

    components = models.ManyToManyField("MaterialComponent")
    attachments = models.ManyToManyField("MaterialAttachment")


COMPONENT_TYPE_CHOICES = (
    ("text", "Text"),
    ("image", "Image"),
    ("video", "Video"),
)


class MaterialComponent(models.Model):
    class Meta:
        verbose_name = 'Material Component'
        verbose_name_plural = 'Material Components'
        ordering = ['ordering']

    ordering = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
        db_index=True,
    )
    type = models.CharField(choices=COMPONENT_TYPE_CHOICES,
                            blank=False,
                            null=False,
                            default=COMPONENT_TYPE_CHOICES[0][0],
                            max_length=50,
                            )
    data = models.CharField(null=True, blank=True, max_length=550)


class MaterialAttachment(models.Model):
    class Meta:
        verbose_name = 'Material Attachment'
        verbose_name_plural = 'Material Attachments'
        ordering = ['ordering']

    ordering = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
        db_index=True,
    )

    name = models.CharField(null=True, blank=True, max_length=255)
    date = models.DateTimeField(auto_now_add=True)
