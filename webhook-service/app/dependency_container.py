from app.infrastructure import WebhookService
from dependency_injector import containers, providers


def setup_dependency_container(modules=None, packages=None):
    container = DependencyContainer()
    container.wire(modules=modules, packages=packages)


class DependencyContainer(containers.DeclarativeContainer):
    """
    Container for managing dependencies in the application.
    """

    config = providers.Configuration()
    wiring_config = containers.WiringConfiguration()

    webhook_service = providers.Factory(WebhookService)
