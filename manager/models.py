from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Entry(models.Model):
    word = models.CharField(max_length=300, unique=True)
    slug = models.SlugField(blank = True, unique = True)
    definition = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    
    search_count = models.IntegerField(default= 0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'entries'

    def __str__(self):
        return self.word
    
    def get_absolute_url(self):
        return reverse('manager:entry-detail', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.id or not self.slug:
            self.slug = slugify(self.word)
        super(Entry, self).save(*args, **kwargs)