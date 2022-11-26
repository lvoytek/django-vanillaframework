"""Django settings file interaction for determining Vanilla Framework middleware settings."""
import os.path
from pathlib import Path
from django.conf import settings
from .util import get_latest_release_version


def get_version():
    """
    Get the version of Vanilla Framework to use.

    If no version is provided in settings, use the latest available.
    """
    version = getattr(settings, "VANILLAFRAMEWORK_VERSION", None)

    if version is None:
        version = get_latest_release_version()

    return version if version is not None else "3.8.2"


def get_min_css_url(ver=None):
    """
    Get the min.css CDN URL for the provided version of Vanilla Framework.

    If a custom URL or version is provided, use that instead.
    """
    return getattr(settings, "VANILLAFRAMEWORK_MIN_CSS_URL",
                   f"https://assets.ubuntu.com/v1/vanilla-framework-version-{ver if ver else get_version()}.min.css")


def get_local_css_path(ver=None):
    """Get the static file path of the local copy of Vanilla Framework."""
    return getattr(settings, "VANILLAFRAMEWORK_CSS_PATH",
                   f"css/vanilla-framework-version-{ver if ver else get_version()}.min.css")


def get_local_sass_path():
    """Get the static file path of the custom sass file that includes Vanilla Framework."""
    return getattr(settings, "VANILLAFRAMEWORK_PATH", "vanillaframework.scss")


def has_local_css():
    """Check if there is a local copy of Vanilla Framework in the correct location and return True if so."""
    css = os.path.join(settings.STATIC_ROOT, get_local_css_path()) if hasattr(settings,
                                                                              "STATIC_ROOT") else get_local_css_path()
    return Path(css).is_file()
