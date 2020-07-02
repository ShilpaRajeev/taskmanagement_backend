
from django.conf import settings

from django.db import models
from django.utils import timezone

from .choices import HOMEPAGE_CHOICES, Section


class UserProjectSettings(models.Model):
    """
    This class represents a persistence for
    project user notifications preference.
    """
    project = models.ForeignKey("projects.Project", related_name="user_project_settings", on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="user_project_settings", on_delete=models.CASCADE)
    homepage = models.SmallIntegerField(choices=HOMEPAGE_CHOICES,
                                        default=Section.timeline)

    created_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField()
    _importing = None

    class Meta:
        unique_together = ("project", "user",)
        ordering = ["created_at"]

    def save(self, *args, **kwargs):
        if not self._importing or not self.modified_date:
            self.modified_at = timezone.now()

        return super().save(*args, **kwargs)
