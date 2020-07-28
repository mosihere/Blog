from django.db import models

# Create your models here.

# Tip --> Slug is something like details of a urls
# for example mosihere/articles/what-is-linux
# for a long text we should use TextField()
class Articles(models.Model):
    title = models.CharField(max_length = 100)
    slug = models.SlugField()
    # Slug mostly use for a tags / for example when we click on a link it will check slug and go for it
    main_text = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    image = models.ImageField(default='default.jpg', blank=True)

    # TODO: add Author

# We add this function to change Article Objects name into real name.
# use title as Article Name
    def __str__(self):
        return self.title


# This method used to only show first 50 characters of a article
    def snippet(self):
        return self.main_text[:50] + ' ...'
