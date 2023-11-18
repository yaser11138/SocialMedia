# your_app/templatetags/custom_filters.py
from django import template
from django.utils import timezone
from datetime import datetime

register = template.Library()


@register.filter
def time_passed_since(value):
    now = timezone.now()
    if isinstance(value, datetime):
        difference = now - value
        if difference.days == 0:
            if difference.seconds < 60:
                return f"{difference.seconds} seconds ago"
            elif difference.seconds < 3600:
                minutes = difference.seconds // 60
                return f"{minutes} {'minute' if minutes == 1 else 'minutes'} ago"
            else:
                hours = difference.seconds // 3600
                return f"{hours} {'hour' if hours == 1 else 'hours'} ago"
        else:
            days = difference.days
            return f"{days} {'day' if days == 1 else 'days'} ago"
    return value
