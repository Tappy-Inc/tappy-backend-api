from django.core.management.base import BaseCommand
from domain.system.models.EmploymentType import EmploymentType
from domain.system.models.JobLevel import JobLevel
from domain.system.models.WorkSetup import WorkSetup
from domain.system.models.Department import Department
from domain.system.models.JobPosition import JobPosition

class Command(BaseCommand):
    help = 'Create default employment types, job levels, work setups, departments and job positions'

    def handle(self, *args, **options):
        employment_types = [
            'Probationary',
            'Regular',
            'Consultancy',
            'Project Based',
            'Internship',
            'Part Time'
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
            'Work From Home'
        ]

        for work_setup in work_setups:
            WorkSetup.objects.get_or_create(work_setup=work_setup)
            self.stdout.write(self.style.SUCCESS('Successfully created work setup "%s"' % work_setup))

        departments = [
            'IT Department',
        ]

        for department in departments:
            Department.objects.get_or_create(department_name=department)
            self.stdout.write(self.style.SUCCESS('Successfully created department "%s"' % department))

        job_positions = [
            'Software Engineer',
            'System Analyst',
            'IT Support',
        ]

        for job_position in job_positions:
            JobPosition.objects.get_or_create(position_name=job_position, department=Department.objects.get(department_name='IT Department'))
            self.stdout.write(self.style.SUCCESS('Successfully created job position "%s"' % job_position))
