from django import template
from ..config import get_min_css_url
from ..util import has_local_css

register = template.Library()


@register.inclusion_tag('vanillaframework/tags/css.html')
def vanillaframework_css():
    """Build the css tag for using Vanilla Framework with Django templates."""
    return {
        'is_local': has_local_css(),
        'vanilla_css_path': None if has_local_css() else get_min_css_url()
    }
