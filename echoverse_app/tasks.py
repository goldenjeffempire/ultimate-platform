from django_q.tasks import schedule
from .views import check_abandoned_carts

# Schedule the task to run every hour
schedule('echoverse_app.views.check_abandoned_carts', minutes=60)
