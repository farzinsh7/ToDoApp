from django.core.management.base import BaseCommand
from faker import Faker
from accounts.models import User
from ...models import ToDo, StatusType, PriorityType


class Command(BaseCommand):
    help = "Inserting Dummy Data by Faker"

    def handle(self, *args, **options):
        fake = Faker()

        # Create a fake user
        user = User.objects.create_user(
            email=fake.email(),
            password=fake.password(),
        )

        # Create 5 completed tasks
        for _ in range(5):
            task = ToDo.objects.create(
                author=user,
                title=fake.sentence(nb_words=6),
                description=fake.paragraph(),
                status=StatusType.done,
                priority=fake.random_element(
                    elements=[PriorityType.low, PriorityType.medium, PriorityType.high]
                ),
            )
            self.stdout.write(self.style.SUCCESS(f"Created task: {task.title}"))
