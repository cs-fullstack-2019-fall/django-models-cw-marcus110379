from django.db import models


class Dog(models.Model):
    dogName = models.CharField(max_length=200)
    dogBreed = models.CharField(max_length=200)
    dogColor = models.CharField(max_length=200)
    dogGender = models.CharField(max_length=200)


class newAccount(models.Model):
    username =models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    accountNumber = models.CharField(max_length=100)
    balance= models.DecimalField(max_digits= 10, decimal_places = 3)





# Add a new Account model to your schema. Give it the fields: username, realName, accountNumber, balance. Username should be a username the user uses to log in, the realName should be a user's real name, accountNumber should be the user's account number, and balance is the user's balance.
