from board.models import User

from django.shortcuts import render
from django.views.generic import UpdateView


class ConfirmUser(UpdateView):
    model = User
    context_object_name = 'confirm_user'

    def post(self, request, *args, **kwargs):
        if 'code' in request.POST:
            user = User.objects.filter(code=request.POST['code'])
            if user.exists():
                user.update(is_active=True)
                user.update(code=None)
            else:
                return render(self.request, 'sign/invalid_code.html')
            return render(self.request, 'sign/account_activated.html')
