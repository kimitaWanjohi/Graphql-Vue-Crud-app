from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Cpu(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Laptop(models.Model):
    name = models.CharField(max_length=100)
    ram = models.CharField(max_length=100, choices=(
        ('1 Gb', '1 Gb'),
        ('2 Gb', '2 Gb'),
        ('4 Gb', '4 Gb'),
        ('8 Gb', '8 Gb'),
        ('16 Gb', '16 Gb'),
        ('32 Gb', '32 Gb'),
        ('64 Gb', '64 Gb')
    ))
    company = models.ForeignKey(Company, related_name='laptop_made', on_delete=models.CASCADE)
    cpu = models.ForeignKey(Cpu, related_name='laptops', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

