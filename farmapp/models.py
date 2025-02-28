from django.db import models

WELL_CHOICES = [
    ('small', 'smallish'),
    ('medium', 'mediumish'),
    ('large', 'largeish'),
]


class Farm(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=256)
    user = models.ManyToManyField('PersonAndRole', related_name='farms')

class GridType(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    row_count = models.IntegerField()
    row_length = models.IntegerField()
    emitter_spacing = models.IntegerField()
    farm = models.ForeignKey('Farm', on_delete=models.CASCADE)

class Grid(models.Model):
    grid_type = models.ForeignKey('GridType', on_delete=models.CASCADE)
    farm = models.ForeignKey('Farm', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    wells = models.ManyToManyField('Well', through='WellDistance')

class WellDistance(models.Model):
    well = models.ForeignKey('Well', on_delete=models.CASCADE)
    grid = models.ForeignKey('Grid', on_delete=models.CASCADE)
    distance = models.DecimalField()

class Well(models.Model):
    farm = models.ForeignKey('Farm', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    depth = models.DecimalField()
    well_type = models.ForeignKey('WellType', on_delete=models.CASCADE)

class WellType(models.Model):
    name = models.CharField(max_length=200, choices=WELL_CHOICES, primary_key=True)
    description = models.CharField(max_length=200)
    price = models.DecimalField()
    diameter = models.DecimalField()
    flow_rate = models.DecimalField()

WELL_CHOICES = [
    ('small', 'smallish'),
    ('medium', 'mediumish'),
    ('large', 'largeish'),
]


class Farm(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=256)
    user = models.ManyToManyField('PersonAndRole', related_name='farms')

class GridType(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    row_count = models.IntegerField()
    row_length = models.IntegerField()
    emitter_spacing = models.IntegerField()
    farm = models.ForeignKey('Farm', on_delete=models.CASCADE)

class Grid(models.Model):
    grid_type = models.ForeignKey('GridType', on_delete=models.CASCADE)
    farm = models.ForeignKey('Farm', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    wells = models.ManyToManyField('Well', through='WellDistance')

class WellDistance(models.Model):
    well = models.ForeignKey('Well', on_delete=models.CASCADE)
    grid = models.ForeignKey('Grid', on_delete=models.CASCADE)
    distance = models.DecimalField()

class Well(models.Model):
    farm = models.ForeignKey('Farm', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    depth = models.DecimalField()
    well_type = models.ForeignKey('WellType', on_delete=models.CASCADE)

class WellType(models.Model):
    name = models.CharField(max_length=200, choices=WELL_CHOICES, primary_key=True)
    description = models.CharField(max_length=200)
    price = models.DecimalField()
    diameter = models.DecimalField()
    flow_rate = models.DecimalField()

