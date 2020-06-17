from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.

class Category(models.Model):
	category=models.CharField(max_length=50)
	def __str__(self):
		return self.category		

class Item(models.Model):
	item_id=models.AutoField(primary_key=True)
	name=models.CharField(max_length=50)
	category=models.ForeignKey(Category,on_delete=models.CASCADE)
	quantity=models.IntegerField(default=0)
	price=models.DecimalField(max_digits=9, decimal_places=2,
                                  blank=True, default=0.00,null=True)
	def total_value(self):
		value = self.price * self.quantity
		return value

	def __str__(self):
		return self.name

class Client(models.Model):
	name=models.CharField(max_length=50,null=True)
	place=models.CharField(max_length=50)
	description=models.CharField(max_length=100)
	balance=models.DecimalField(max_digits=9, decimal_places=2,
                                  blank=True, default=0.00, null=True)

	def __str__(self):
	    return self.place
        
		
	
class Transaction(models.Model):
	trans_id=models.AutoField(primary_key=True)	
	quantity=models.IntegerField()
	time=models.DateTimeField(auto_now=True)
	item=models.ForeignKey(Item,on_delete=models.CASCADE,blank=False,null=False)
	client=models.ForeignKey(Client,on_delete=models.CASCADE,blank=False,null=False)
	def __str__(self):
		return ("%s , %s , %s" % (self.item.name,self.client.name,self.time))

class Account_Details(models.Model):
	transaction=models.ForeignKey(Transaction,on_delete=models.CASCADE,blank=False,null=False)
	debit_amount=models.DecimalField(max_digits=9, decimal_places=2,
                                  blank=True, default=0.00,null=True)
	credit_amount=models.DecimalField(max_digits=9, decimal_places=2,
                                  blank=True, default=0.00,null=True)
	balance_amount=models.DecimalField(max_digits=9, decimal_places=2,
                                  blank=True, default=0.00,null=True)
	time=models.DateTimeField(auto_now=True)
	client=models.ForeignKey(Client,on_delete=models.CASCADE,blank=False,null=False)
	description=models.CharField(max_length=150)

	def __str__(self):
		return ("%s , %s , %s" % (self.client.name,self.transaction.trans_id,self.time))


