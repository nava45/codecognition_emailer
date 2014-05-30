codecognition_emailer
=====================

Email Template Configuration Utility

Open your settings.py

add

	EMAIL_HOST_USER = '' #Add the google username
	EMAIL_HOST_PASSWORD = '' #Add the password 
	
To Run the server:
python manage.py runserver



To check in shell:
python manage.py shell

	>>>from emailer.models import *
	>>>from emailer.email import *
	>>>template = str(MailTemplate.objects.all()[0].body)
	>>>payload = {'from':'navaneethan.codecognition.com','to_list':['nava.nmr@gmail.com'],\
            'subject':'A sample activation mail','body':template,\
          	'template_data_as_dict':{'name':'Narendhiran','project':'hqfeeds','activation_url':''} \
        }
	 #app_data dict fields are using in the email configured template

Here 'template_data_as_dict' is a dictionary which should contain all the fields in Email Pre-Configured Template as keys.

	>>>mail_to(payload)

