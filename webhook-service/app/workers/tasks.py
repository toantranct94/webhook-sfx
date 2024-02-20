from celery import Task
from app.domain import MAX_RETRY
from celery.exceptions import MaxRetriesExceededError
from celery.utils.serialization import raise_with_context


class BaseTaskWithRetry(Task):
    autoretry_for = (Exception,)
    max_retries = MAX_RETRY
    retry_backoff = True
    retry_backoff_max = 600
    retry_jitter = False

    def retry(self, args=None, kwargs=None, exc=None, throw=True,
              eta=None, countdown=None, max_retries=None, **options):
        try:
            # don't pass the original exception here, since doing that will cause
            # celery to _not_ throw MaxRetriesExceededError
            return super().retry(args, kwargs, None, throw, eta, countdown, max_retries, **options)
        except MaxRetriesExceededError as e:
            # do your stuff here
            # you could call a method that you implement in other subclasses to easily reuse this logic

            # finally, mimic the original celery behaviour by raising the exception,
            # or the MaxRetriesExceededError if no exception was given
            if exc:
                raise_with_context(exc)
            raise e
