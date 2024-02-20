from dependency_injector import containers, providers
from infrastructure import PeopleService, QueueService, WebhookService


def setup_dependency_container(app, modules=None, packages=None):
    container = DependencyContainer()
    app.container = container
    app.container.wire(modules=modules, packages=packages)
    return app


class DependencyContainer(containers.DeclarativeContainer):
    """
    Container for managing dependencies in the application.
    """

    config = providers.Configuration()
    wiring_config = containers.WiringConfiguration()

    people_service = providers.Factory(PeopleService)
    queue_service = providers.Singleton(QueueService)
    webhook_service = providers.Factory(WebhookService)
