from django.template import Context, Template


def test_default_cdn_css_with_version(settings):
    settings.VANILLAFRAMEWORK_VERSION = "3.8.1"
    output = Template(
        """
        {% load vanillaframework_tags %}
        {% vanillaframework_css %}
        """
    ).render(Context({}))

    assert '<link rel="stylesheet" href="https://assets.ubuntu.com/v1/vanilla-framework-version-3.8.1.min.css" />' in output
