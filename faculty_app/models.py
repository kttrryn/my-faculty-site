from django.db import models


class Department(models.Model):
    id = models.IntegerField(verbose_name="id")
    name = models.CharField(max_length=150, verbose_name="name")
    chair = models.CharField(max_length=255, verbose_name="chair")  # chair of department

    def __str__(self):
        return self.name


class Program(models.Model):
    id = models.IntegerField(verbose_name="id")
    name = models.CharField(max_length=150, verbose_name="name")
    code = models.CharField(max_length=25, verbose_name="code")
    description = models.TextField(max_length=500, verbose_name="description")
    coordinator = models.CharField(max_length=150, verbose_name="coordinator")
    coord_number = models.CharField(max_length=10, verbose_name="coord_number")  # 0xx-xxx-xxxx
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name='programs',
        verbose_name='department'
    )
    courses = models.TextField(max_length=1000, verbose_name="description")

    def __str__(self):
        return f"{self.code} {self.name}"


class Teacher(models.Model):
    id = models.IntegerField(verbose_name="id")
    name = models.CharField(max_length=150, verbose_name="name")
    position = models.CharField(max_length=150, verbose_name="position")
    degree = models.CharField(max_length=150, verbose_name="degree")
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name='teachers',
        verbose_name='department'
    )

    def __str__(self):
        return self.name
