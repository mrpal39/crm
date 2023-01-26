from django.apps import AppConfig

from django.utils.translation import gettext_lazy as _

class DashboardConfig(AppConfig):
    # name = ''
    name = "crm.dashboard"
    verbose_name = _("dashboard")

    def ready(self):
        try:
            import crm.dashboard.signals  # noqa F401
        except ImportError:
            pass
