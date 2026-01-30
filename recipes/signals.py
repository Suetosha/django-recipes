from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver

from .models import Recipe


@receiver(post_delete, sender=Recipe)
def recipe_delete_image_file(sender, instance, **kwargs):
    image = getattr(instance, "image", None)
    if image and image.name:
        image.delete(save=False)


@receiver(pre_save, sender=Recipe)
def recipe_delete_old_image_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return

    try:
        old = sender.objects.get(pk=instance.pk)
    except sender.DoesNotExist:
        return

    old_image = getattr(old, "image", None)
    new_image = getattr(instance, "image", None)

    if old_image and old_image.name and old_image != new_image:
        old_image.delete(save=False)