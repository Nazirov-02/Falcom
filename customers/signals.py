from django.dispatch import receiver
from django.db.models.signals import post_save,post_delete
from django.core.mail import EmailMessage
from customers.models import Customers
from accounts.models import User

@receiver(post_save, sender=Customers)
def create_customer(sender, instance, created, **kwargs):
    if created:
        print(f'Signal triggered for customer: {instance.name}')
        users = User.objects.all()
        email_of_user = [user.email for user in users if user.email]
        if email_of_user:
            email = EmailMessage(
                subject='Customer Saved',
                body=f'{instance.name} successfully saved',
                to=email_of_user,
            )
            email.send(fail_silently=False)


@receiver(post_delete, sender=Customers)
def delete_customer(sender, instance, **kwargs):
    print(f'Signal triggered for customer deletion: {instance.name}')
    users = User.objects.all()
    email_of_user = [user.email for user in users if user.email]
    if email_of_user:
        email = EmailMessage(
            subject='Customer Deleted',
            body=f'{instance.name} has been deleted.',
            to=email_of_user,
        )
        email.send(fail_silently=False)


from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import EmailMessage
from customers.models import Customers
from accounts.models import User


@receiver(post_save, sender=Customers)
def update_customer(sender, instance, created, **kwargs):
    if not created:
        print(f'Customer updated: {instance.name}')

        users = User.objects.all()
        email_of_user = [user.email for user in users if user.email]

        if email_of_user:
            email = EmailMessage(
                subject='Customer Updated',
                body=f'The customer "{instance.name}" has been updated successfully.\n\n'
                     f'Updated details:\n'
                     f'Name: {instance.name}\n'
                     f'Email: {instance.email}\n'
                     f'Address: {instance.address}\n'
                     f'Phone: {instance.phone}\n\n'
                     f'Updated by system automatically.',
                to=email_of_user,
            )
            email.send(fail_silently=False)
            print(f'Email notification sent to: {email_of_user}')

