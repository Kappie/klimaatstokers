from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.dateparse import parse_date
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
from django.template.defaultfilters import date as local_date
from easy_thumbnails.files import get_thumbnailer
import datetime

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=600)
    body_text  = MarkdownxField()
    pub_date = models.DateTimeField('date published', default=datetime.datetime.now()) 
    leader_image = models.ImageField(null=True)
    leader_text = models.TextField(null=True)
    # This is e.g. my-nice-title when title is My Nice Title, and is used in the post url.
    slug = models.SlugField(null=False, unique=True)       
    authors = models.ManyToManyField(User, related_name='author')

    def to_html(self):
        return markdownify(self.body_text)

    def date_string(self):
        day = local_date(self.pub_date, "j")
        month = local_date(self.pub_date, "F")
        year = local_date(self.pub_date, "Y")

        return "%s %s %s" % (day, month, year)

    def authors_string(self):
        author_names = [author.get_full_name() for author in self.authors.all()]
        if len(author_names) == 1:
            return author_names[0]
        else:
            result = ", ".join(author_names[:-1])
            result += " en %s" % author_names[-1]
            return result

    def get_thumbnail(self):
        options = {'size': (360, 240), 'crop': 'smart'}
        thumb_url = get_thumbnailer(self.leader_image).get_thumbnail(options).url
        return thumb_url

    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title
     

