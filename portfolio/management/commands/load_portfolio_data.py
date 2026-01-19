from django.core.management.base import BaseCommand
from portfolio.models import Profile, SkillCategory, Skill, Experience, Education, Project

class Command(BaseCommand):
    help = 'Load initial portfolio data for Hamzah Ahmed Faea'

    def handle(self, *args, **kwargs):
        # 1. Profile
        profile, created = Profile.objects.get_or_create(
            name="Hamzah Ahmed Faea",
            defaults={
                "role": "Software Engineer (Full-Stack & Backend Specialist)",
                "tagline": "Building complex, bilingual, and reliable web systems.",
                "bio": "Full-stack software engineer with strong expertise in backend architecture. Detail-oriented problem-solver experienced in building, testing, and maintaining complex applications, including responsive, bilingual interfaces and integrated booking systems.",
                "github": "https://github.com/Hamzah712",
                "linkedin": "https://linkedin.com/in/hamzahfaea",
                "email": "hamzah.faea@gmail.com",
                "location": "Islamabad, Pakistan",
            }
        )
        if not created:
            profile.role = "Software Engineer (Full-Stack & Backend Specialist)"
            profile.tagline = "Building complex, bilingual, and reliable web systems."
            profile.bio = "Full-stack software engineer with strong expertise in backend architecture. Detail-oriented problem-solver experienced in building, testing, and maintaining complex applications, including responsive, bilingual interfaces and integrated booking systems."
            profile.github = "https://github.com/Hamzah712"
            profile.linkedin = "https://linkedin.com/in/hamzahfaea"
            profile.email = "hamzah.faea@gmail.com"
            profile.location = "Islamabad, Pakistan"
            profile.save()

        # 2. Skill Categories & Skills
        skills_data = {
            "Languages": [("C#", 90), ("JavaScript", 85), ("Java", 80), ("C++", 75), ("HTML", 95), ("CSS", 90)],
            "Databases": [("SQL Server", 85), ("PostgreSQL", 80), ("MySQL", 80)],
            "Frameworks": [("ASP.NET Core", 90), ("React", 60), ("Django", 70)],
            "Tools": [("Git", 90), ("Docker", 75), ("Postman", 85), ("VS Code", 95)],
        }

        for cat_name, skills in skills_data.items():
            category, _ = SkillCategory.objects.get_or_create(name=cat_name)
            for skill_name, proficiency in skills:
                Skill.objects.get_or_create(category=category, name=skill_name, defaults={"proficiency": proficiency})

        # 3. Experience
        Experience.objects.get_or_create(
            role="Freelance Software Developer",
            company="Nozol Chalets",
            defaults={
                "tech_stack": "ASP.NET 8 MVC, EF Core, SQL Server, Razor Pages",
                "start_date": "2023",
                "end_date": "Present",
                "achievements": "Built a full-stack reservation system handling 80+ monthly bookings.\nImplemented iCal synchronization with Booking.com.\nCreated a bilingual (Arabic/English) interface with SMS/WhatsApp integration.",
                "order": 1
            }
        )

        # 4. Education
        Education.objects.get_or_create(
            degree="BS in Software Engineering",
            institution="International Islamic University Islamabad",
            defaults={
                "duration": "2021–2025",
                "order": 1
            }
        )

        # 5. Projects (Sample if needed, but user didn't specify specific projects other than the context)
        Project.objects.get_or_create(
            title="Nozol Chalets Reservation System",
            defaults={
                "description": "A full-stack reservation system with iCal synchronization and bilingual support.",
                "tech_stack": "ASP.NET 8 MVC, SQL Server, iCal",
                "link": "https://nozolchalets.com", # Placeholder
                "order": 1
            }
        )

        self.stdout.write(self.style.SUCCESS("Successfully loaded Hamzah's portfolio data."))
