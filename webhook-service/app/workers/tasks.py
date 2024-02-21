from app.domain import MAX_RETRY
from celery import Task
from celery.exceptions import MaxRetriesExceededError
from celery.utils.serialization import raise_with_context


class BaseTaskWithRetry(Task):
    """
    A base task class that supports automatic retrying.

    This class extends the `Task` class from the Celery library and adds
    functionality for automatic retrying of tasks in case of exceptions.

    Attributes:
        autoretry_for (tuple): A tuple of exception types for which the task
            should be retried automatically.
        max_retries (int): The maximum number of times the task should be
            retried.
        retry_backoff (bool): Whether to apply exponential backoff when
            retrying the task.
        retry_backoff_max (int): The maximum number of seconds to wait between
            retries when using exponential backoff.
        retry_jitter (bool): Whether to add random jitter to the retry delay.

    Methods:
        retry: Retries the task with the same arguments and options.
    """
    autoretry_for = (Exception,)
    max_retries = MAX_RETRY
    retry_backoff = True
    retry_backoff_max = 600
    retry_jitter = False

    def retry(self, args=None, kwargs=None, exc=None, throw=True,
              eta=None, countdown=None, max_retries=None, **options):
        try:
            return super().retry(
                args, kwargs, None, throw,
                eta, countdown, max_retries,
                **options)
        except MaxRetriesExceededError as e:
            # TODO: Add the message to the dead letter queue
            if exc:
                raise_with_context(exc)
            raise e
