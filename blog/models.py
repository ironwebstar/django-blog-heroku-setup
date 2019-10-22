from django.db import models
from django.utils.safestring import mark_safe
# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(null=True, blank=True, upload_to='blog/%Y/%m/%d')
    published = models.BooleanField(default=True, null=False, blank=False)

    def __str__(self):
        """A string representation of the model."""
        return self.title

    def image_tag(self):
        if self.image:
            return mark_safe('<img src="%s" style="width: 150px; height:150px;" />' % self.image.url)
        else:
            return 'No Image Found'

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True
