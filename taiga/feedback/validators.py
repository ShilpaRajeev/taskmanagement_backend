
from taiga.base.api import validators

from . import models


class FeedbackEntryValidator(validators.ModelValidator):
    class Meta:
        model = models.FeedbackEntry
