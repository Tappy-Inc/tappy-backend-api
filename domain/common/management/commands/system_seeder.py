from django.core.management.base import BaseCommand

# User Domain
from django.contrib.auth.models import User
from domain.user.models.Profile import Profile

# System Domain
from domain.system.models.EmploymentType import EmploymentType
from domain.system.models.JobLevel import JobLevel
from domain.system.models.WorkSetup import WorkSetup
from domain.system.models.Department import Department
from domain.system.models.JobPosition import JobPosition
from domain.system.models.Gender import Gender


class Command(BaseCommand):
    help = 'Create default employment types, job levels, work setups, departments, job positions and genders'

    def handle(self, *args, **options):

        employment_types = [
            'Probationary',
            'Regular',
            'Consultancy',
            'Project Based',
            'Internship',
            'Part Time',
            'Temporary',
            'Contractual',
            'Freelance',
            'Volunteer',
            'Trainee',
            'Apprentice',
            'Seasonal',
            'Commission',
            'Casual'
        ]

        for employment_type in employment_types:
            EmploymentType.objects.get_or_create(employment_type=employment_type)
            self.stdout.write(self.style.SUCCESS('Successfully created employment type "%s"' % employment_type))

        job_levels = [
            'Internship',
            'Associate',
            'Senior Associate',
            'Specialist',
            'Senior Specialist',
            'Officer',
            'Assistant Manager',
            'Manager',
            'Senior Manager',
            'Associate Director',
            'Director',
            'Assistant Vice President',
            'Executive',
            'Vice President',
            'Senior Vice President',
            'C-Level',
            'Others',
        ]

        for job_level in job_levels:
            JobLevel.objects.get_or_create(level=job_level)
            self.stdout.write(self.style.SUCCESS('Successfully created job level "%s"' % job_level))

        work_setups = [
            'Onsite',
            'Hybrid (3D onsite/2D WFH)',
            'Hybrid (2D onsite/3D WFH)',
            'Work From Home',
            'Remote',
            'Flexible',
            'Field Work',
            'Travel Required',
            'Rotational Shift',
            'Fixed Shift',
            'Split Shift',
            'Night Shift',
            'Weekend Shift',
            'Holiday Shift',
            'Overtime Required'
        ]

        for work_setup in work_setups:
            WorkSetup.objects.get_or_create(work_setup=work_setup)
            self.stdout.write(self.style.SUCCESS('Successfully created work setup "%s"' % work_setup))

        departments = [
            'IT Department',
            'Sales Department',
            'Marketing Department',
            'Human Resources Department',
            'Finance Department',
            'Operations Department',
            'Product Department',
            'Customer Service Department',
            'Research and Development Department',
            'Legal Department',
            'Supply Chain Department',
            'Quality Assurance Department',
            'Purchasing Department',
            'Administrative Department',
            'Engineering Department',
            'Production Department',
            'Business Development Department'
        ]

        for department in departments:
            Department.objects.get_or_create(department_name=department)
            self.stdout.write(self.style.SUCCESS('Successfully created department "%s"' % department))

        it_job_positions = [
            'Software Engineer',
            'System Analyst',
            'IT Support',
            'Network Administrator',
            'Database Administrator',
            'IT Project Manager',
            'IT Consultant',
            'IT Technician',
            'IT Director',
            'IT Manager',
            'IT Coordinator',
            'IT Specialist',
            'IT Analyst',
            'IT Operations Manager',
            'IT Security Specialist',
            'IT Service Manager',
            'IT Strategy Manager',
            'IT Systems Manager',
            'IT Test Manager',
            'IT Trainer',
        ]

        sales_job_positions = [
            'Sales Representative',
            'Sales Manager',
            'Sales Analyst',
            'Sales Director',
            'Sales Associate',
            'Sales Consultant',
            'Sales Coordinator',
            'Sales Executive',
            'Sales Support Specialist',
            'Sales Operations Manager',
            'Sales Engineer',
            'Sales Account Manager',
            'Sales and Marketing Manager',
            'Sales Development Representative',
            'Sales Team Leader',
            'Sales Vice President',
            'Sales Specialist',
            'Sales Trainer',
            'Sales Territory Manager',
            'Sales and Service Representative',
        ]

        for job_position in it_job_positions:
            JobPosition.objects.get_or_create(position_name=job_position, department=Department.objects.get(department_name='IT Department'))
            self.stdout.write(self.style.SUCCESS('Successfully created job position "%s"' % job_position))

        for job_position in sales_job_positions:
            JobPosition.objects.get_or_create(position_name=job_position, department=Department.objects.get(department_name='Sales Department'))
            self.stdout.write(self.style.SUCCESS('Successfully created job position "%s"' % job_position))

        genders = [
            'Male',
            'Female',
        ]

        for gender in genders:
            Gender.objects.get_or_create(gender=gender)
            self.stdout.write(self.style.SUCCESS('Successfully created gender "%s"' % gender))

