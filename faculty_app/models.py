from datetime import date

from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=150, verbose_name="name")
    chair = models.CharField(
        max_length=255, verbose_name="chair"
    )  # chair of department

    def __str__(self):
        return self.name


class Program(models.Model):
    name = models.CharField(max_length=150, verbose_name="name")
    code = models.CharField(max_length=25, verbose_name="code")
    description = models.TextField(max_length=1000, verbose_name="description")
    coordinator = models.CharField(max_length=150, verbose_name="coordinator")
    coord_number = models.CharField(
        max_length=10, verbose_name="coord_number"
    )  # 0xx-xxx-xxxx
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name="programs",
        verbose_name="department",
    )
    courses = models.TextField(max_length=1000, verbose_name="courses")

    def __str__(self):
        return f"{self.code} {self.name}"


class Teacher(models.Model):
    name = models.CharField(max_length=150, verbose_name="name")
    position = models.CharField(max_length=150, verbose_name="position")
    degree = models.CharField(max_length=150, verbose_name="degree")
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name="teachers",
        verbose_name="department",
    )

    def __str__(self):
        return self.name


class MainPageInfo(models.Model):
    title = models.CharField(
        max_length=150, verbose_name="faculty_name", default="Факультет X"
    )
    description = models.TextField(verbose_name="description")
    general_info = models.TextField(verbose_name="general_info")
    contacts = models.TextField(verbose_name="contacts")

    def __str__(self):
        return "main page"


class ExchangeProgram(models.Model):
    university_name = models.CharField(
        max_length=255, verbose_name="Назва університету"
    )
    country = models.CharField(max_length=255, verbose_name="Країна")
    languages = models.CharField(max_length=255, verbose_name="Мови навчання")
    places = models.IntegerField(verbose_name="Кількість місць")
    deadline = models.DateField(verbose_name="Дедлайн подачі")
    description = models.TextField(verbose_name="Опис", blank=True)

    def __str__(self):
        return self.university

    @property
    def is_active(self):
        return self.deadline >= date.today()
