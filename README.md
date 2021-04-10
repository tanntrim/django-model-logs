# django-model-logs

###Log_Mixin :
Its a django mixin when used in django auto save the changes being done with the value of the column.

To make it work need to follow these steps :

1. We are using middleware named 'get_user_middleware' to get the name of current user being used in log.
So we need to declare the middleware in setting files with path to the files as
```
'#Middleware_#Path.RequestMiddleware'
``` 

Note: You are free to move the middleware file to your desire location and import the required module in log_mixin with updated directory location :

```
from #Middleware_#Path import get_request
```
