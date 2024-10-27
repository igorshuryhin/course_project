from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=100)
    lessons_amount = models.IntegerField(null=True, blank=True)
    duration = models.CharField(max_length=20, null=True)
    description = models.TextField(blank=True, null=True)
    course_price = models.IntegerField()
    start_date = models.DateField(null=True, blank=True, default=None)

    category = models.ForeignKey(Category, null=True, blank=True, related_name="courses", on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
