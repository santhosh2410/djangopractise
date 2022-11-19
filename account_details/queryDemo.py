from .models import *

#Returns all customers from customer table
customers = Customer.objects.all()

#Returns first customer in table
firstCustomer = Customer.objects.first()

#Returns last customer in table
lastCustomer = Customer.objects.last()

#Returns single customer by name
customerByName = Customer.objects.get(name='akshaya')

#***(5)Returns single customer by name
customerById = Customer.objects.get(id=4)

#Returns all orders related to customer (firstCustomer variable set above)
firstCustomer.order_set.all()

#Returns orders customer name: (Query parent model values)
order = Order.objects.first() 
parentName = order.customer.name

#Returns products from products table with value of "Pickle" in category attribute
products = Product.objects.filter(category="Pickle")

#Order/Sort Objects by id
leastToGreatest = Product.objects.all().order_by('id') 
greatestToLeast = Product.objects.all().order_by('-id') 


# Returns all products with tag of "Fryum": (Query Many to Many Fields)
productsFiltered = Product.objects.filter(tags__name="Fryum")


#Returns the total count for number of time a "Potato Chips" was ordered by the first customer
FryumOrders = firstCustomer.order_set.filter(product__name="potato chips").count()

#Returns total count for each product orderd
allOrders = {}

for order in firstCustomer.order_set.all():
	if order.product.name in allOrders:
		allOrders[order.product.name] += 1
	else:
		allOrders[order.product.name] = 1



#RELATED SET EXAMPLE
class ParentModel(models.Model):
	name = models.CharField(max_length=200, null=True)

class ChildModel(models.Model):
	parent = models.ForeignKey(Customer)
	name = models.CharField(max_length=200, null=True)

parent = ParentModel.objects.first()
#Returns all child models related to parent
parent.childmodel_set.all()