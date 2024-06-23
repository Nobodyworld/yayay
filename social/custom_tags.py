from django import template
from django.utils import timezone

register = template.Library()

@register.simple_tag
def button_label(action, user_role=None):
    """
    Returns a button label based on the action and user role.
    
    Parameters:
    - action (str): The action for which the label is needed.
    - user_role (str, optional): The role of the user, to provide specific labels for roles.
    
    Returns:
    - str: The appropriate label for the button.
    """
    labels = {
        'submit': 'Submit',
        'delete': 'Delete',
        'confirm': 'Confirm',
    }
    special_labels = {
        ('delete', 'admin'): 'Permanently Delete',
    }
    return special_labels.get((action, user_role), labels.get(action, 'Click'))

@register.simple_tag
def format_date(date):
    """
    Formats a datetime object to a string in a local timezone format.
    
    Parameters:
    - date (datetime): The date to format.
    
    Returns:
    - str: The formatted date string.
    """
    return timezone.localtime(date).strftime('%Y-%m-%d %H:%M')

@register.simple_tag(takes_context=True)
def display_for_role(context, role_required):
    """
    Determines if content should be displayed for a user's role based on the template context.
    
    Parameters:
    - context (dict): The template context containing the request object.
    - role_required (str): The required role to display the content.
    
    Returns:
    - bool: True if the user's role matches the required role, False otherwise.
    """
    user = context['request'].user
    return user.is_authenticated and user.role == role_required

@register.simple_tag
def summarize_data(data):
    """
    Summarizes a list of dictionaries by providing the count of items and the maximum 'value' found.
    
    Parameters:
    - data (list): The data to summarize.
    
    Returns:
    - dict: A dictionary containing the count of items and the maximum 'value'.
    """
    try:
        return {
            'count': len(data),
            'max_value': max(item['value'] for item in data if 'value' in item),
        }
    except ValueError:
        return {'count': len(data), 'max_value': None}

@register.simple_tag
def embed_twitter_post(post_id):
    """
    Generates HTML for embedding a Twitter post.
    
    Parameters:
    - post_id (str): The Twitter post ID to embed.
    
    Returns:
    - str: HTML content for embedding the Twitter post.
    """
    return (f'<blockquote class="twitter-tweet">'
            f'<a href="https://twitter.com/user/status/{post_id}"></a>'
            '</blockquote><script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>')

@register.simple_tag
def css_class_for_status(status):
    """
    Returns a CSS class based on the status of an item.
    
    Parameters:
    - status (str): The status to evaluate.
    
    Returns:
    - str: The corresponding CSS class.
    """
    return {
        'new': 'bg-success',
        'pending': 'bg-warning',
        'closed': 'bg-secondary',
    }.get(status, 'bg-primary')

@register.filter
def replace_value(value, arg):
    """
    Replaces underscores with spaces in a string and capitalizes the first letter.
    
    Parameters:
    - value (str): The original string.
    - arg (unused): Unused parameter, present for compatibility with Django filter function signature.
    
    Returns:
    - str: The transformed string.
    """
    return value.replace("_", " ").capitalize()
