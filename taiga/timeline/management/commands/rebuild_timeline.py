
from django.core.management.base import BaseCommand
from django.test.utils import override_settings

from taiga.timeline.models import Timeline
from taiga.timeline.rebuilder import rebuild_timeline

from optparse import make_option


class Command(BaseCommand):
    help = 'Regenerate project timeline'

    def add_arguments(self, parser):
        parser.add_argument('--purge',
                            action='store_true',
                            dest='purge',
                            default=False,
                            help='Purge existing timelines')
        parser.add_argument('--initial_date',
                            action='store',
                            dest='initial_date',
                            default=None,
                            help='Initial date for timeline generation')
        parser.add_argument('--final_date',
                            action='store',
                            dest='final_date',
                            default=None,
                            help='Final date for timeline generation')
        parser.add_argument('--project',
                            action='store',
                            dest='project',
                            default=None,
                            help='Selected project id for timeline generation')

    @override_settings(DEBUG=False)
    def handle(self, *args, **options):
        if options["purge"] == True:
            Timeline.objects.all().delete()

        rebuild_timeline(options["initial_date"], options["final_date"], options["project"])
