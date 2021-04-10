from datetime import datetime
from django.contrib.postgres.fields.jsonb import JSONField as JSONBField
from django.db import models


class LogMixin(models.Model):
    log = JSONBField(default=list, null=True, blank=True)
    def save(self, *args, **kwargs):
        """

        Args:
            *args:
            **kwargs:

        Returns: runs Super Save Function

        """
        # Getting Old Value of the current row With The primary key
        old = eval(self.__class__.__name__).objects.get(pk=self.pk)
        for key, value in old.__dict__.items():
            # Validating The attributes whose values had changed
            if value not in self.__dict__.values() and key != '_state' and key != 'log':
                # Appending the changed field ,values ,datetime and user in json format into log
                '''
                TO get the logged in username have created middleware  
                Returning The user object and getting Username from the object
                '''
                self.log.append({'field': key, 'from': value, 'to': self.__dict__.get(key),
                                 'at': datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),
                                 'by': get_request().user.username})
                print('mixin method')
        return super(LogMixin, self).save(*args, **kwargs)
