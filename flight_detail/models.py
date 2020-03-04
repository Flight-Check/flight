from django.db import models


class Flightinfo(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    airline = models.CharField(max_length=45, blank=True, null=True)
    destinations = models.CharField(max_length=45, blank=True, null=True)
    flightnumbers = models.TextField(db_column='flightNumbers', blank=True, null=True)  # Field name made lowercase.
    scheduledtime = models.CharField(db_column='scheduledTime', max_length=45, blank=True,
                                     null=True)  # Field name made lowercase.
    estimatedtime = models.CharField(db_column='estimatedTime', max_length=45, blank=True,
                                     null=True)  # Field name made lowercase.
    scheduleddate = models.CharField(db_column='scheduledDate', max_length=45, blank=True,
                                     null=True)  # Field name made lowercase.
    latesttime = models.CharField(db_column='latestTime', max_length=45, blank=True,
                                  null=True)  # Field name made lowercase.
    status = models.CharField(max_length=45, blank=True, null=True)
    statuscolor = models.CharField(db_column='statusColor', max_length=45, blank=True,
                                   null=True)  # Field name made lowercase.
    origin = models.CharField(max_length=45, blank=True, null=True)
    gate = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return self.airline
