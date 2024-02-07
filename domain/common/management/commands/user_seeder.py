from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group

# User Domain
from domain.user.models.Address import Address
from domain.user.models.User import User
from domain.user.models.Document import Document
from domain.user.models.EducationalBackground import EducationalBackground
from domain.user.models.Profile import Profile
from domain.user.models.GovernmentInformation import GovernmentInformation
from domain.user.models.WorkInformation import WorkInformation
from domain.user.models.WorkSchedule import WorkSchedule

# System Domain
from domain.system.models.Department import Department
from domain.system.models.EmploymentType import EmploymentType
from domain.system.models.Gender import Gender
from domain.system.models.JobLevel import JobLevel
from domain.system.models.WorkSetup import WorkSetup


# Library: faker
from faker import Faker

class Command(BaseCommand):
    help = 'Create default employment types, job levels, work setups, departments, job positions, genders and groups'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Indicates the number of users to be created')

    def handle(self, *args, **options):

        fake = Faker()

        # Create groups
        group_names = ['ADMIN', 'HUMAN_RESOURCE', 'EMPLOYEE']
        for group_name in group_names:
            Group.objects.get_or_create(name=group_name)


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
        
        for i in range(options['count']):
            username = f"{fake.user_name()}_{fake.random_int(min=1000, max=9999)}"
            email = fake.email()
            # password = User.objects.make_random_password()
            password = 'Pass@12345'
            first_name = fake.first_name()
            last_name = fake.last_name()
            middle_name = fake.first_name()
            user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name, middle_name=middle_name)
            user.save()

            # Assigning group based on the iteration
            # If it's the first iteration, assign the user to the 'ADMIN' group
            if i == 0:
                username = 'admin'
                group = Group.objects.get(name='ADMIN')
            # If it's the second iteration, assign the user to the 'HUMAN_RESOURCE' group
            elif i == 1:
                username = 'human_resource'
                group = Group.objects.get(name='HUMAN_RESOURCE')
            # For all other iterations, assign the user to the 'EMPLOYEE' group
            elif i == 2:
                username = 'employee'
                group = Group.objects.get(name='EMPLOYEE')
            else:
                group = Group.objects.get(name='EMPLOYEE')
                
            user.groups.add(group)
            user.save()

            address = Address(
                user=user,
                address=fake.address(),
                address_line_2=fake.secondary_address(),
                baranggay=fake.random_element(elements=['Baranggay 1', 'Baranggay 2', 'Baranggay 3']),
                city=fake.city(),
                state=fake.state(),
                postal_code=fake.zipcode(),
                country=fake.country()
            )
            address.save()

            profile = Profile(
                user=user, 
                bio=fake.text(max_nb_chars=500), 
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

            self.stdout.write(self.style.SUCCESS('Successfully created user "%s"' % username))

