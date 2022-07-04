import django

django.setup()
from random import randint

from django_seed import Seed
from employees.models import Employee, Job

seeder = Seed.seeder('ru_RU')
seeder.add_entity(Employee, 50000, {
    'job_title': lambda x: Job.objects.order_by('?').first(),
    # 'chief': lambda x: x.job_title < Employee.job_title,
    'first_name': lambda x: seeder.faker.first_name(),
    'middle_name': lambda x: seeder.faker.last_name(),
    'last_name': lambda x: seeder.faker.last_name(),
    'employment_date': lambda x: seeder.faker.date_object(),
    'salary': lambda x: randint(10_000, 400_000),
})
inserted_pks = seeder.execute()
