from django.db import models
from django.core.exceptions import ValidationError

class Accounts(models.Model):
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    account_name = models.CharField(blank=False, null=False, max_length=100)
    account_type = models.CharField(blank=False, null=False, max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=20, blank=True, null=True)
    updated_by = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"Account {self.id}, Balance: ${self.balance}"

    def save(self, *args, **kwargs):
        if self.balance < 0:
            raise ValidationError("Account balance cannot be negative.")
        super(Accounts, self).save(*args, **kwargs)
        
    class Meta:
        db_table = "Accounts"
        verbose_name = "Accounts"
        verbose_name_plural = "Accounts"
        