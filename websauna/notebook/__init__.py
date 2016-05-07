from pyramid.config import Configurator

from websauna.system import Initializer as WSInitializer
from websauna.system.model.utils import attach_models_to_base_from_module
from websauna.utils.autoevent import after, event_source
from websauna.utils.autoevent import bind_events


class AddonInitializer:
    """Configure this addon for websauna.

    * We hook to existing parts of initialization process using ``@after`` aspect advisor

    * For something we don't have a direct join point we just initialize through ``run()``
    """
    def __init__(self, config: Configurator):
        self.config = config

    @after(WSInitializer.configure_admin)
    def configure_admin(self):
        """Setup pyramid_notebook integration."""
        self.config.add_route('admin_shell', '/notebook/admin-shell')
        self.config.add_route('shutdown_notebook', '/notebook/shutdown')
        self.config.add_route('notebook_proxy', '/notebook/*remainder')
        from . import views
        self.config.scan(views)

    def run(self):
        bind_events(self.config.registry.initializer, self)
        from . import subscribers
        self.config.scan(subscribers)


class Initializer(WSInitializer):
    """A demo / test app initializer for testing addon websauna.notebook."""

    def include_addons(self):
        """Include this addon in the configuration."""
        self.config.include("websauna.notebook")


def main(global_config, **settings):
    init = Initializer(global_config)
    init.run()
    return init.make_wsgi_app()


def includeme(config: Configurator):
    """Entry point for Websauna main app to include this addon.

    In the Initializer of your app you should have:

        def include_addons(self):
            # ...
            self.config.include("websauna.notebook")

    """
    addon_init = AddonInitializer(config)
    addon_init.run()
