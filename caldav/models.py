from django.db import models
from django.contrib.auth import User

class Event (models.Model):
    start       = models.DateTimeField ()
    end         = models.DateTimeField ()
    allDay      = models.BooleanField (default = False)
    creator     = models.ForeignKey (User, null = True)
    title       = models.CharField (max_length = 50)
    description = models.CharField (max_length = 100, null = True)
    calendar    = models.ForeignKey ("Calendar")
    editable    = models.BooleanField (default = False)

class Calendar (models.Model):
    owner = models.ForeignKey (User, null = True)

# vim: tabstop=4 shiftwidth=4 expandtab
