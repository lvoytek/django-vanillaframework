"""Vanilla Framework management command."""
import os.path

from django.core.management.base import BaseCommand
from django.conf import settings
from pathlib import Path
import urllib.request
from vanillaframework import __version__, config


class Command(BaseCommand):
    """Vanilla Framework management command class."""

    help = "Manage Vanilla Framework install within the Django project."

    def add_arguments(self, parser):
        """Add -- args to the management command."""
        parser.add_argument("-i", "--install", action='store_true', help="Install Vanilla Framework locally")
        parser.add_argument("--css", action='store_true',
                            help="Use the min.css version of Vanilla Framework (no customization)")
        parser.add_argument("--use-version", type=str,
                            help="The version of Vanilla Framework to use, defaults to settings version or newest")
        parser.add_argument("--static-folder", type=str, help="The static folder to put Vanilla Framework in",
                            default=settings.STATIC_ROOT)

    def handle(self, *args, **options):
        """Handle Vanilla Framework management commands."""
        if options["install"]:
            self.handle_install(*args, **options)

    def handle_install(self, *args, **options):
        """Handle Vanilla Framework install command."""
        version_to_get = options["use_version"] if "use_version" in options else config.get_version()

        if "static_folder" not in options:
            print("Error: no static folder provided. Use --static-folder or add a STATIC_ROOT to settings.")
            return

        if options["css"]:
            Path(os.path.join(options["static_folder"], 'css')).mkdir(parents=True, exist_ok=True)
            urllib.request.urlretrieve(config.get_min_css_url(version_to_get), os.path.join(options["static_folder"],
                                                                                            config.get_local_css_path(
                                                                                                version_to_get)))

        if "use_version" in options:
            print("You have downloaded a specific version of Vanilla Framework. To use it, add:")
            print(f"VANILLAFRAMEWORK_VERSION = {version_to_get}")
            print("to your settings file.")

    def get_version(self):
        """Get the django-vanillaframework version."""
        return __version__
