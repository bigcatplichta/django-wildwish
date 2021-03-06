from app.settings import SENDGRID_API_KEY
from decouple import config
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# Use SendGrid Dynamic Templates (https://mc.sendgrid.com/dynamic-templates)

SG = SendGridAPIClient(SENDGRID_API_KEY)

def send_msg(message):
    try:
        response = SG.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.body)
        
# obj is donation.animal, or any object that returns a queryset of images with obj.images.all()
def get_img_array(obj):
    imgs = []
    for i in obj.images.all():
        imgs.append({'url': i.upload.url})
        
    return (imgs)   

# Argument is 'Donation' object from 'animals' app
def send_recpt(donation):
    message = Mail(
        from_email = 'roar@wildheart.foundation',
        to_emails = donation.email,
        # subject = f'Your Donation to {donation.wish.animal.name}',
        # html_content = '<strong>Hey thanks for donating.</strong>'
    )
    
    message.dynamic_template_data = {
        'subject': f'Your Donation to {donation.wish.animal.name}',
        'name': donation.first_name,
        'wish_id': donation.wish.id,
        'animal_id': donation.wish.animal.id,
        'animal_name': donation.wish.animal.name,
        'animal_av_url': get_img_array(donation.wish.animal)[0]['url'],
        'images': get_img_array(donation.wish.animal),
        'wish_url': f'http://dev.wildwish.com/#/wishes/{donation.wish.id}'
    }
    
    message.template_id = 'd-397bbaeafd9e4933934aa42d1826d7fc'

    send_msg(message)
        

def send_wish_imgs(donation):
    print(f'Images from {donation.wish.animal.name}\'s wish have been emailed.')
        
    message = Mail(
        from_email = 'roar@wildheart.foundation',
        to_emails = donation.email,
        # subject = f'Your Donation to {donation.wish.animal.name}',
        # html_content = '<strong>Hey thanks for donating.</strong>'
    )
    
    # How to handle substitutions for multiple name list?
    message.dynamic_template_data = {
        'subject': f'Thanks to you, {donation.wish.animal.name} got their wish',
        'name': donation.first_name,
        'animal_name': donation.wish.animal.name
    }
    
    # SG template name: Wish Image Update
    message.template_id = 'd-6bcd2497b984421da06081c03982f718'

    send_msg(message)    