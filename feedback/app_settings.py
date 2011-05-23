from django.conf import settings

TOP_FEEDBACKS_COUNT = getattr(settings,'TOP_FEEDBACKS_COUNT', 2)
FEEDBACK_SEND_MAIL = getattr(settings,'FEEDBACK_SEND_MAIL', True)
