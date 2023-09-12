from django.db import models

from wagtail.models import Page, ParentalKey, Orderable
from wagtail.admin.panels import FieldPanel, InlinePanel


class HomePage(Page):
    content_panels = Page.content_panels + [
        InlinePanel('gallery_images', label = "Gallery Images"),
    ]

class HomePageGalleryImage(Orderable):
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    heading = models.CharField(blank=True, max_length=250)
    caption = models.CharField(blank=True, max_length=250)
    button_name = models.CharField(blank=True, max_length=20)
    button_url = models.URLField(blank=True, max_length=20)

    panels = [
        FieldPanel('image'),
        FieldPanel('heading'),
        FieldPanel('caption'),
        FieldPanel('button_name'),
        FieldPanel('button_url'),
    ]
