from app.infrastructure import PeopleService, WebhookService
from dependency_injector import containers, providers


def setup_dependency_container(app, modules=None, packages=None):
    container = DependencyContainer()
    app.container = container
    app.container.wire(modules=modules, packages=packages)
    return app


class DependencyContainer(containers.DeclarativeContainer):

    config = providers.Configuration()
    wiring_config = containers.WiringConfiguration()

    people_service = providers.Factory(PeopleService)
    webhook_service = providers.Factory(WebhookService)
