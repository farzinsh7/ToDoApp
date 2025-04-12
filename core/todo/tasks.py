from celery import shared_task


@shared_task
def delete_done_tasks():
    from .models import ToDo, StatusType

    deleted, _ = ToDo.objects.filter(status=StatusType.done.value).delete()
    print(f"{deleted} done tasks deleted.")
