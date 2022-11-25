from django.template import Context, Template
from django.core.management import call_command
from .util import clean_test_files

css_template = Template(
        """
        {% load vanillaframework_tags %}
        {% vanillaframework_css %}
        """
    )


def test_default_cdn_css_with_version(settings):
    clean_test_files()
    settings.VANILLAFRAMEWORK_VERSION = "3.8.1"
    output = css_template.render(Context({}))

    assert '<link rel="stylesheet" href="https://assets.ubuntu.com/v1/vanilla-framework-version-3.8.1.min.css" />' in output


def test_default_local_css_with_version(settings):
    test_version = "1.0.0"
    call_command("vanillaframework", "-i", "--css", "--use-version", test_version)
    settings.VANILLAFRAMEWORK_VERSION = test_version
    output = css_template.render(Context({}))

    assert f'<link rel="stylesheet" href="/static/css/vanilla-framework-version-{test_version}.min.css" />' in output
    clean_test_files()
