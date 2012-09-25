from django.db import models
		

# My Models
class Item(models.Model):
	description = models.CharField(max_length=128)
	price = models.DecimalField(max_digits=5, decimal_places=2)
	def __unicode__(self):
	        return self.description
	
class Merchant(models.Model):
	name = models.CharField(max_length=128)
	address = models.CharField(max_length=128)
	def __unicode__(self):
	        return self.name

class Purchaser(models.Model):
	name = models.CharField(max_length=128)
	def __unicode__(self):
	        return self.name
	
class Order(models.Model):
	item = models.ForeignKey(Item)
	merchant = models.ForeignKey(Merchant)
	purchaser = models.ForeignKey(Purchaser)
	quantity = models.IntegerField()
	
	


