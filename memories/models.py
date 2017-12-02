from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# class MyUser(User):
#     sign_in_times = models.PositiveIntegerField(default=0)
#
#     def sign_in():
#         sign_in_times += 1
#
#     def is_sign_in_continuity():
#         last_login_day = self.last_login.strftime("%d")
#         now_day = timezone.now.strftime("%d")
#         if now_day - last_login_day == 1:
#             sign_in_times += 1
#         else:
#             sign_in_times = 0

class MyUser(User):
    introduction = models.TextField()


class Memory(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    author = models.CharField(max_length=10, null=True)
    post_time = models.DateTimeField(default=timezone.now, null=True)
    def post(self):
        self.save()
