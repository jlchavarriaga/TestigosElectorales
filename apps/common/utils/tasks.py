from importlib import import_module


def get_function(func_name: str):
    module = import_module('config.celery')
    return getattr(module, func_name)


def enqueue_task(task_name: str, *args, **kwargs):
    f = get_function(task_name)
    f.delay(*args, **kwargs)
