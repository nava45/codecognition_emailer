from django.core.mail import EmailMultiAlternatives,EmailMessage


class PropertyBuilder(object):
    def __init__(self, data_as_dict={}):
        self.data = data_as_dict
        for _build in ["self.__class__.%s = '''%s'''"%(k,v) \
                        for k,v in self.data.items()]:
            exec _build
        
    def __str__(self):
        return self.template.format(cc=self)


def substitute_appdata_to_template(template, app_data):
    app_data['template'] = str(template).replace('{{','{').replace('}}','}')
    
    ## How to set propert to the attributes
    #obj = PropertyBuilder(app_data)
    #print str(template).format(cc=obj),"previou sline"
    ###
    
    return str(PropertyBuilder(app_data))


def send(sender, recipients, subject, body, attachments=[]):
    """
    Mail configuration
    django mail or amazon ses statements
    """
    msg = EmailMessage(subject, body, sender, recipients)
    msg.content_subtype = "html"  # Main content is now text/html
    msg.send()


def mail_to(payload):
    """
    payload contains all the necessary data in dictionary format.
    
    *sender sender email address
    *recipients recipeients list of email address
    *subject mail subject string
    *mail_body mail body template
    *app_data mail template data as dict
    
    sample:
    
    payload = {'from':'navaneethan.codecognition.com','to_list':['nava.nmr@gmail.com'],\
            'subject':'A sample mail','body':'Sample body',\
            #app_data dict fields are using in the email configured template
            'template_data_as_dict':{'name':'Narendhiran','project':'hqfeeds','activation_url':''} \
        }
    
    """
    sender = payload.get('from',None)
    recipients = payload.get('to_list',[])
    subject = payload.get('subject',None)
    mail_body = payload.get('body',None)
    app_data = payload.get('template_data_as_dict',None)
    
    if app_data and mail_body and sender and recipients:
        fomatted_body = substitute_appdata_to_template(mail_body, app_data)
        send(sender,recipients,subject,fomatted_body)
    else:
        print "insufficient data in payload"
    
    