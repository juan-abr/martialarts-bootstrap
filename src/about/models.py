from django.db import models

from wagtail.models import Page, ParentalKey, Orderable
from wagtail.admin.panels import FieldPanel, InlinePanel

# This page explains the program, the training environment, and the style.
class AboutPage(Page):
    content_panels = Page.content_panels + [
        InlinePanel('gallery_images', label="Gallery images"),
    ]

class AboutPageGalleryImage(Orderable):
    page = ParentalKey(AboutPage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    heading = models.CharField(max_length=20)  #To be renamed prefix for clarity
    secondary_heading = models.CharField(max_length=20)
    description = models.TextField()
    
    panels = [
        FieldPanel('image'),
        FieldPanel('heading'),
        FieldPanel('secondary_heading'),
        FieldPanel('description'),
    ]

class InstructorsPage(Page):
    content_panels = Page.content_panels + [
        InlinePanel('gallery_images', label="Gallery images"),
    ]

class InstructorsPageGalleryImage(Orderable):
    page = ParentalKey(InstructorsPage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    position = models.CharField(max_length=20)  #To be renamed prefix for clarity
    name = models.CharField(max_length=20)
    description = models.TextField()
    
    panels = [
        FieldPanel('image'),
        FieldPanel('position'),
        FieldPanel('name'),
        FieldPanel('description'),
    ]
