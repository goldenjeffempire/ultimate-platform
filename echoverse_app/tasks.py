from django_q.tasks import schedule
from .views import check_abandoned_carts
from celery import shared_task
import requests
from django.utils import timezone
from .models import SocialMediaPost


# Schedule the task to run every hour
schedule('echoverse_app.views.check_abandoned_carts', minutes=60)

# Post to Social Media
@shared_task
def post_to_social_media(post_id):
    post = SocialMediaPost.objects.get(id=post_id)

    if post.scheduled_time > timezone.now():
        return "Not yet time to post."

    if post.platform == 'Facebook':
        api_url = "https://graph.facebook.com/v12.0/me/feed"
        payload = {'message': post.content, 'access_token': 'YOUR_FACEBOOK_ACCESS_TOKEN'}
    elif post.platform == 'Twitter':
        api_url = "https://api.twitter.com/2/tweets"
        payload = {'status': post.content}
    elif post.platform == 'LinkedIn':
        api_url = "https://api.linkedin.com/v2/shares"
        payload = {'content': {'text': post.content}, 'visibility': {'code': 'PUBLIC'}}
    else:
        return "Unsupported platform"

    response = requests.post(api_url, json=payload)

    if response.status_code == 200:
        post.posted = True
        post.save()
        return f"Posted successfully on {post.platform}"
    else:
        return f"Failed to post on {post.platform}"
