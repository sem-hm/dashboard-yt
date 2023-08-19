from django.db import models

# Create your models here.
class Bank(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.name
    
    def __repr__(self) -> str:
        return f'Model Bank: {self.name}'


class CreditRegister(models.Model):
    currency_choices = [
        (1, 'Moneda extranjera'),
        (2, 'Moneda nacional'),
        (3, 'UDIS'),
    ]
    currency = models.PositiveSmallIntegerField(
        choices=currency_choices,
        default=2
    )

    credit_status_choices = [
        (1, 'Vencido'),
        (2, 'Vigente'),
    ]
    credit_status = models.PositiveSmallIntegerField(
        choices=credit_status_choices,
        default=2
    )
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    total = models.FloatField(default=0.0)
    date = models.DateField(auto_now_add=True)
    def __str__(self) -> str:
        return f'{self.get_currency_display()} - {self.get_credit_status_display()} - {self.bank.name} - ${self.total}'
    
    def __repr__(self) -> str:
        return f'Model CreditRegister: {self.get_currency_display()} {self.get_credit_status_display()} {self.bank.name} ${self.total}'
