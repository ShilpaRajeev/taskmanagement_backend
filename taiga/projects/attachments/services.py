
from django.apps import apps
from django.conf import settings

from taiga.base.utils.thumbnails import get_thumbnail_url, get_thumbnail


def get_attachment_by_id(project_id, attachment_id):
    model_cls = apps.get_model("attachments", "Attachment")
    try:
        obj = model_cls.objects.select_related("content_type").get(id=attachment_id)
    except model_cls.DoesNotExist:
        return None

    if not obj.content_object or obj.content_object.project_id != project_id:
        return None

    return obj


def get_timeline_image_thumbnail_name(attachment):
    if attachment.attached_file:
        thumbnail = get_thumbnail(attachment.attached_file, settings.THN_ATTACHMENT_TIMELINE)
        return thumbnail.name if thumbnail else None
    return None


def get_card_image_thumbnail_url(attachment):
    if attachment.attached_file:
        return get_thumbnail_url(attachment.attached_file, settings.THN_ATTACHMENT_CARD)
    return None


def get_attachment_image_preview_url(attachment):
    if attachment.attached_file:
        return get_thumbnail_url(attachment.attached_file, settings.THN_ATTACHMENT_PREVIEW)
    return None


def url_is_an_attachment(url: str, base=None) -> "Union[str, None]":
    if not url:
        return None
    return url if url.startswith(base or settings.MEDIA_URL) else None
