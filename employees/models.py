from django.db import models

# Create your models here.


class Job(models.Model):
    """Должности"""
    name = models.CharField("Должность", max_length=15)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Должность"
        verbose_name_plural = "Должность"


class Employee(models.Model):
    """Сотрудники"""
    first_name = models.CharField("Имя", max_length=15)
    middle_name = models.CharField("Отчество", max_length=15)
    last_name = models.CharField("Фамилия", max_length=15)
    job_title = models.ForeignKey(Job, verbose_name="Должность", related_name="job", on_delete=models.CASCADE)
    employment_date = models.DateField("Прием на работу")
    salary = models.PositiveIntegerField("Зарплата", default=0)
    chief = models.ForeignKey("self", on_delete=models.CASCADE, default=None, null=True, blank=True)

    def __str__(self):
        return self.last_name+" "+self.first_name+" "+self.middle_name

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудник"
