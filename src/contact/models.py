from django.db import models

from wagtail.models import Page, ParentalKey
from wagtail.admin.panels import FieldPanel

# Create your models here.
class ContactPage(Page):
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    description = models.TextField(blank=True)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=10)

    content_panels = Page.content_panels + [
        FieldPanel('image'),
        FieldPanel('description'),
        FieldPanel('email'),
        FieldPanel('phone'),
    ]
