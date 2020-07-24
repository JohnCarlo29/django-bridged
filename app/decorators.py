from django.shortcuts import redirect


def guest(function):
    def wrap(request, *ars, **kwargs):
        if request.user is not None and request.user.is_authenticated:
            return redirect('/home/')
    return wrap
