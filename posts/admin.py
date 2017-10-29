from django.contrib import admin

from django.apps import apps
import sys

for myModel in apps.get_models():
    try:
        AdminModel = getattr(sys.modules[__name__], (myModel.__name__ + 'Admin'))
        admin.site.register(myModel, AdminModel)
    except Exception:
        try:
            admin.site.register(myModel)
        except admin.sites.AlreadyRegistered:
            pass
