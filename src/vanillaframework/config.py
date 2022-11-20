from django.conf import settings


def get_version():
    """
    Get the version of Vanilla Framework to use.
    If no version is provided in settings, use the latest available.
    """
    return getattr(settings, "VANILLAFRAMEWORK_VERSION", "3.8.1")


def get_min_css_url():
    """
    Get the min.css CDN URL for the provided version of Vanilla Framework.
    If a custom URL is provided, use that instead.
    """
    return getattr(settings, "VANILLAFRAMEWORK_MIN_CSS_URL",
                   f"https://assets.ubuntu.com/v1/vanilla-framework-version-{get_version()}.min.css")
