from django.apps import AppConfig

from django.utils.translation import gettext_lazy as _

class BlogConfig(AppConfig):
    name = "crm.blog"
    verbose_name = _("blog")

    def ready(self):
        try:
            import crm.blog.signals  # noqa F401
        except ImportError:
            pass
