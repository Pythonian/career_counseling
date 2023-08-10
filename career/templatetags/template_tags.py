from django import template

# Create a custom template library instance
register = template.Library()


# Define a custom template filter
@register.filter
def sum_total_scores(scores):
    """
    Custom template filter to calculate the sum of total scores from a list of assessment scores.

    Args:
        scores (list): List of AssessmentScore objects.

    Returns:
        int: Sum of total scores.
    """
    total_score = 0
    for score in scores:
        # Sum up the total scores from each AssessmentScore object
        total_score += score.total_score
    return total_score
