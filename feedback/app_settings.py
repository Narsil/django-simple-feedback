from django.conf import settings

TOP_FEEDBACKS_COUNT = getattr(settings, 'TOP_FEEDBACKS_COUNT', 2)
FEEDBACK_SEND_MAIL = getattr(settings, 'FEEDBACK_SEND_MAIL', True)
FEEDBACK_SUBJECT = getattr(settings,
    'FEEDBACK_SUBJECT',
    '[feedback] on %(path)s')
FEEDBACK_BODY = getattr(settings,
    'FEEDBACK_BODY',
    '%(feedback)s')
FEEDBACK_FROM = getattr(settings,'FEEDBACK_FROM', 'feedback@example.com')
managers_emails = map(lambda x:x[1], getattr(settings, 'MANAGERS', []))
FEEDBACK_TO = getattr(settings,'FEEDBACK_TO', managers_emails)
