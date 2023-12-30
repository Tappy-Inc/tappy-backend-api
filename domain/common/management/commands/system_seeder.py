from django.core.management.base import BaseCommand

# System Domain
from domain.system.models.EmploymentType import EmploymentType
from domain.system.models.JobLevel import JobLevel
from domain.system.models.WorkSetup import WorkSetup
from domain.system.models.Department import Department
from domain.system.models.JobPosition import JobPosition
from domain.system.models.Gender import Gender
from domain.system.models.CompanyInformation import CompanyInformation

# Mailer Domain
from domain.mailer.models.Template import Template
from domain.mailer.models.FromEmail import FromEmail

class Command(BaseCommand):
    help = 'Create default employment types, job levels, work setups, departments, job positions, genders, company information, templates and from emails'

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

        company_information = [
            {
                'company_name': 'Tappy Inc.',
                'address': 'BGC, Taguig',
                'number': '+639062131607',
                'company_size': 100,
                'industry': 'Software Development'
            },
        ]

        for company in company_information:
            CompanyInformation.objects.get_or_create(**company)
            self.stdout.write(self.style.SUCCESS('Successfully created company information "%s"' % company['company_name']))

        from_emails = [
            {
                'name': 'Tappy Inc.',
                'email': 'info@tappy.com.ph'
            },
        ]

        for from_email in from_emails:
            FromEmail.objects.get_or_create(**from_email)
            self.stdout.write(self.style.SUCCESS('Successfully created from email "%s"' % from_email['email']))

        templates = [
            {
                'from_email': FromEmail.objects.get(id=1),
                'name': 'welcome_email',
                'subject': 'Welcome to Tappy Inc.',
                'body': 'Welcome to Tappy Inc. We are glad to have you with us.'
            },
        ]

        for template in templates:
            Template.objects.get_or_create(**template)
            self.stdout.write(self.style.SUCCESS('Successfully created template "%s"' % template['name']))

