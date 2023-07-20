from django_seed import Seed

from basic.models.course import Course
from basic.models.exam import Exam

seeder = Seed.seeder()
seeder.add_entity(Course, 10)
seeder.add_entity(Exam, 10)

inserted_pks = seeder.execute()
