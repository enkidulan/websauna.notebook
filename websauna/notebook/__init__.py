from pyramid.config import Configurator

from websauna.system import Initializer
from websauna.system.model.utils import attach_models_to_base_from_module
from websauna.utils.autoevent import after, event_source
from websauna.utils.autoevent import bind_events


class AddonInitializer:
    """Configure this addon for websauna.

    * We hook to existing parts of initialization process using ``@after`` aspect advisor

    * For something we don't have a direct join point we just initialize through ``run()``
    """

    def __init__(self, config:Configurator):
        self.config = config

    @after(Initializer.configure_admin)
    def configure_admin(self):
        """Setup pyramid_notebook integration."""
        """Configure views for your application.

        Let the config scanner to pick ``@simple_route`` definitions from scanned modules.
        Alternative you can call ``config.add_route()`` and ``config.add_view()`` here.
        """
        # We override this method, so that we route home to our home screen, not Websauna default one
        self.config.add_route('admin_shell', '/notebook/admin-shell')
        self.config.add_route('shutdown_notebook', '/notebook/shutdown')
        self.config.add_route('notebook_proxy', '/notebook/*remainder')
        from . import views
        self.config.scan(views)

    def configure_templates(self):
        """Include our package templates folder in Jinja 2 configuration."""
        super(Initializer, self).configure_templates()

        self.config.add_jinja2_search_path('notebook:templates', name='.html', prepend=True)  # HTML templates for pages
        self.config.add_jinja2_search_path('notebook:templates', name='.txt', prepend=True)  # Plain text email templates (if any)
        self.config.add_jinja2_search_path('notebook:templates', name='.xml', prepend=True)  # Sitemap and misc XML files (if any)

    def run(self):

        # This will make sure our initialization hooks are called later
        bind_events(self.config.registry.initializer, self)

        # Run our custom initialization code which does not have a good hook
        # Configure web shell
        # self.configure_admin()


def includeme(config: Configurator):
    """Entry point for Websauna main app to include this addon.

    In the Initializer of your app you should have:

        def include_addons(self):
            # ...
            self.config.include("websauna.notebook")

    """
    addon_init = AddonInitializer(config)
    addon_init.run()

