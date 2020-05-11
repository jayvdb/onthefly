from django.apps import AppConfig
from django.contrib import admin

from onthefly.monkey_patch import patch


class OntheflyConfig(AppConfig):
    name = 'onthefly'
    patched = False

    def ready(self):
        if not self.patched:
            patch()
            self.patched = True

        if hasattr(admin.site, 'register_view'):
            from .admin import AppSettingsView

            admin.site.register_view('onthefly-settings/', 'Onthefly Settings',
                                     view=AppSettingsView.as_view())
