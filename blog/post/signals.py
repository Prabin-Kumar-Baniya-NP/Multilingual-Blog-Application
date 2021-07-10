from django.dispatch.dispatcher import receiver
from post.models import Post
from django.db.models.signals import pre_save, post_delete
import os


@receiver(pre_save, sender=Post)
def auto_delete_file_on_change(sender, instance,**kwargs):
    """
    Deletes the old image of Post whenever user update the post object image.
    """
    if instance.id is None:
        pass
    else:
        new_instance = instance
        old_instance = Post.objects.get(pk = instance.id)
        if old_instance.image:
            if old_instance.image != new_instance.image:
                if os.path.isfile(old_instance.image.path):
                    os.remove(old_instance.image.path)
        else:
            pass


@receiver(post_delete, sender=Post)
def auto_delete_image_on_post_delete(sender, instance, **kwargs):
    """
    Deletes image of Post when the corresponding post is deleted
    """
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)