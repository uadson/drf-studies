from django_seed import Seed

from basic.models import Course, Exam

seeder = Seed.seeder()
seeder.add_entity(Course, 10)
seeder.add_entity(Exam, 10)

inserted_pks = seeder.execute()
