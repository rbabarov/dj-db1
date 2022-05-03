from django.db import models
from django.template.defaultfilters import slugify


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    #id = models.ForeignKey()
    name = models.CharField(max_length=254, null=True)
    price = models.DecimalField(max_digits=7,decimal_places=0)
    image = models.ImageField(upload_to=None)
    release_date = models.DateField(null=True)
    lte_exists = models.BooleanField(default=False)
    slug = models.SlugField(max_length=254, null=True, unique=True)

    def get_slug(self):
        self.slug = slugify(self.name)