from django.db import models

class Invs(models.Model):
    instance_id = models.CharField(max_length=30)
    instance_type = models.CharField(max_length=30)
    ami_id = models.CharField(max_length=30)
    instance_status = models.CharField(max_length=30)
    availability_zone = models.CharField(max_length=30)
    public_ip = models.CharField(max_length=30)
    private_ip = models.CharField(max_length=30)
    instance_keypair = models.CharField(max_length=30)
    dns_public = models.CharField(max_length=30)
    dns_private = models.CharField(max_length=30)

    def __str__(self):
        return str.name
