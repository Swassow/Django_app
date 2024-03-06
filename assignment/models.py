from django.db import models

# Create your models here.
class Func(models.Model):
    name =models.CharField(max_length=100)

class company(models.Model):
    name =models.CharField(max_length=100)

class employee(models.Model):
    name =models.CharField(max_length=100)
    email =models.CharField(max_length=100)
    company_id = models.ForeignKey(company, on_delete=models.CASCADE)

class device(models.Model):
    device_name =models.CharField(max_length=100)
    device_condition =models.CharField(max_length=255)
    occupied=models.IntegerField(default=-2)
    company_id = models.ForeignKey(company, on_delete=models.CASCADE)
    check_out_date=models.DateTimeField(null=True, blank=True)
    returned_date=models.DateTimeField(null=True, blank=True)


class deviceLog(models.Model):
    employee_id=models.ForeignKey(employee, on_delete=models.CASCADE)
    company_id=models.ForeignKey(company, on_delete=models.CASCADE)
    device_id=models.ForeignKey(device, on_delete=models.CASCADE,default=1)
    check_out_condition=models.CharField(max_length=100)
    returned_condition=models.CharField(null=True, blank=True,max_length=100)
    check_out_date=models.DateTimeField(null=True, blank=True)
    returned_date=models.DateTimeField(null=True, blank=True)
