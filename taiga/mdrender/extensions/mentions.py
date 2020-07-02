
from django.contrib.auth import get_user_model

from markdown.extensions import Extension
from markdown.inlinepatterns import Pattern
from markdown.util import etree, AtomicString


class MentionsExtension(Extension):
    project = None

    def __init__(self, *args, **kwargs):
        self.project = kwargs.pop("project", None)
        super().__init__(*args, **kwargs)

    def extendMarkdown(self, md):
        MENTION_RE = r"(@)([\w.-]+)"
        mentionsPattern = MentionsPattern(MENTION_RE, project=self.project)
        mentionsPattern.md = md
        md.inlinePatterns.add("mentions", mentionsPattern, "_end")


class MentionsPattern(Pattern):
    project = None

    def __init__(self, pattern, md=None, project=None):
        self.project = project
        super().__init__(pattern, md)

    def handleMatch(self, m):
        username = m.group(3)
        kwargs = {"username": username}
        if self.project is not None:
            kwargs["memberships__project_id"]=self.project.id
        try:
            user = get_user_model().objects.get(**kwargs)
        except get_user_model().DoesNotExist:
            return "@{}".format(username)

        url = "/profile/{}".format(username)

        link_text = "@{}".format(username)

        a = etree.Element('a')
        a.text = AtomicString(link_text)

        a.set('href', url)
        a.set('title', user.get_full_name())
        a.set('class', "mention")

        self.md.extracted_data['mentions'].append(user)

        return a
