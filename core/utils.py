# File: core\utils.py
from core.models import Will, Meaning, Knowledge, Wisdom

def calculate_will(user):
    """
    Calculate the will for a user based on their completed tasks or goals.
    This is a placeholder implementation, and you can customize the logic as needed.
    """
    # Example logic to calculate will:
    completed_wills = Will.objects.filter(user=user).count()
    return completed_wills * 10  # Assuming each completed will contributes 10 points

def calculate_meaning(user):
    """
    Calculate the meaning for a user based on their related will entries.
    This is a placeholder implementation, and you can customize the logic as needed.
    """
    # Example logic to calculate meaning:
    completed_meanings = Meaning.objects.filter(will__user=user).count()
    return completed_meanings * 5  # Assuming each completed meaning contributes 5 points

def calculate_knowledge(user):
    """
    Calculate the knowledge for a user based on their related meaning entries.
    This is a placeholder implementation, and you can customize the logic as needed.
    """
    # Example logic to calculate knowledge:
    completed_knowledge = Knowledge.objects.filter(meaning__will__user=user).count()
    return completed_knowledge * 3  # Assuming each completed knowledge entry contributes 3 points

def calculate_wisdom(user):
    """
    Calculate the wisdom for a user based on their related knowledge entries.
    This is a placeholder implementation, and you can customize the logic as needed.
    """
    # Example logic to calculate wisdom:
    completed_wisdom = Wisdom.objects.filter(knowledge__meaning__will__user=user).count()
    return completed_wisdom * 2  # Assuming each completed wisdom entry contributes 2 points
