from django.utils import timezone
from django.shortcuts import redirect
from django.urls import reverse
from users.models import User


class SubscriptionRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            profile = request.user.profile
            subscription_end_date = profile.subscription_end_date
            if not subscription_end_date or subscription_end_date < timezone.now():
                allowed_paths = [
                    reverse('subscribe'),  # Adjust 'subscribe' to your subscription view name
                    reverse('logout'),
                ]
                if request.user.role in [User.Role.LAWYER, User.Role.NOTARY]:
                    if request.path not in allowed_paths and not request.path.startswith('/admin/'):
                        return redirect('subscribe')
        response = self.get_response(request)
        return response