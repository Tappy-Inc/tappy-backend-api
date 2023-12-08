from django.core.management.base import BaseCommand

# User Domain
from django.contrib.auth.models import User
from domain.user.models.Profile import Profile
from domain.user.models.EducationalBackground import EducationalBackground
from domain.user.models.GovernmentInformation import GovernmentInformation
from domain.user.models.WorkInformation import WorkInformation
from domain.user.models.WorkSchedule import WorkSchedule
from domain.user.models.Document import Document

# System Domain
from domain.system.models.Gender import Gender
from domain.system.models.EmploymentType import EmploymentType
from domain.system.models.JobLevel import JobLevel
from domain.system.models.WorkSetup import WorkSetup
from domain.system.models.Department import Department

# Library: faker
from faker import Faker

class Command(BaseCommand):
    help = 'Create default employment types, job levels, work setups, departments, job positions and genders'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Indicates the number of users to be created')

    def handle(self, *args, **options):

        fake = Faker()

        genders = Gender.objects.filter(gender__in=['Male', 'Female'])
        civil_statuses = ['Single', 'Married', 'Divorced', 'Widowed']
        
        education_types = ['College', 'Highschool', 'Elementary', 'Vocational Course']
        degree_names = [
            'Bachelor\'s in Computer Science', 
            'Master\'s in Business Administration', 
            'Bachelor\'s in Arts', 
            'Master\'s in Science', 
            'PhD in Philosophy',
            'Bachelor\'s in Engineering',
            'Master\'s in Information Technology',
            'Bachelor\'s in Business Administration',
            'Master\'s in Arts',
            'PhD in Computer Science'
        ]
        degree = fake.random_element(elements=degree_names)
        
        
        for _ in range(options['count']):
            username = fake.user_name()
            email = fake.email()
            password = User.objects.make_random_password()
            first_name = fake.first_name()
            last_name = fake.last_name()
            user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
            user.save()

            profile = Profile(
                user=user, 
                bio=fake.text(max_nb_chars=500), 
                location=fake.city(), 
                middle_name=fake.first_name(), 
                gender=fake.random_element(elements=genders), 
                civil_status=fake.random_element(elements=civil_statuses), 
                employee_id=fake.random_int(min=100000, max=999999), 
                birth_date=fake.date_of_birth(),
                manager=None
            )
            profile.save()

            education = EducationalBackground(
                user=user,
                education_type=fake.random_element(elements=education_types),
                school=fake.company(),
                from_year=fake.past_date(),
                to_year=fake.future_date(),
                degree=degree
            )
            education.save()

            government_info = GovernmentInformation(
                user=user,
                sss_no=fake.random_int(min=1000000000, max=9999999999),
                tin=fake.random_int(min=1000000000, max=9999999999),
                philhealth=fake.random_int(min=1000000000, max=9999999999),
                hdmf=fake.random_int(min=1000000000, max=9999999999),
                prc_license_no=fake.random_int(min=1000000000, max=9999999999),
                passport_no=fake.random_int(min=1000000000, max=9999999999),
                tax_status=fake.random_element(elements=['Single', 'Married', 'Head of the Family', 'Widowed']),
                rdo_number=fake.random_int(min=1000, max=9999)
            )
            government_info.save()

            work_info = WorkInformation(
                user=user,
                department=fake.random_element(elements=Department.objects.all()),
                job_level=fake.random_element(elements=JobLevel.objects.all()),
                employment_type=fake.random_element(elements=EmploymentType.objects.all()),
                work_setup=fake.random_element(elements=WorkSetup.objects.all())
            )
            work_info.save()

            days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
            rest_days = fake.random_elements(elements=days_of_week, length=2, unique=True)
            for day in days_of_week:
                work_schedule = WorkSchedule(
                    user=user,
                    day_of_week=day,
                    shift_start=fake.time(),
                    shift_end=fake.time(),
                    is_rest_day=day in rest_days
                )
                work_schedule.save()

            document = Document(
                user=user,
                file_name=fake.file_name(),
                file_type=fake.file_extension(),
                file_source=fake.file_path()
            )
            document.save()

            self.stdout.write(self.style.SUCCESS('Successfully created user "%s"' % username))

