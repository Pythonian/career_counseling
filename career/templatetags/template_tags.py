from django import template

register = template.Library()


@register.filter
def sum_total_scores(scores):
    total_score = 0
    for score in scores:
        total_score += score.total_score
    return total_score
