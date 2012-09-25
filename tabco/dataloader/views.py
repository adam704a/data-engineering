# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader, RequestContext
from django.shortcuts import get_object_or_404, render_to_response
from dataloader.models import Order, Purchaser, Item, Merchant, Order


import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)
logging.basicConfig()

def index(request):
	
	if request.method == 'POST':
		save_order(request.FILES['myfile'])

	
	order_list = Order.objects.all()
	t = loader.get_template('dataloader/index.html')
	c = Context({
	        'order_list': order_list,
	})
	return render_to_response('dataloader/index.html', {'order_list': order_list, 'gross_revenue': get_gross_revenue(order_list) }, context_instance=RequestContext(request))
	

def get_gross_revenue(order_list):
	gross_revenue = 0
	for order in order_list:
		order_total = order.quantity * order.item.price
		gross_revenue += order_total
	return gross_revenue
	
def save_order(f):
	for chunk in f.chunks():
			lines = chunk.splitlines()
			lines.pop(0)
			for line in lines:
				entry = line.split('\t')
				
				_purchaser = Purchaser(name=entry[0])
				_purchaser.save()
				
				_item = Item(description=entry[1],price=entry[2])
				_item.save()
				
				_merchant = Merchant(address=entry[4], name=entry[5])
				_merchant.save()
				
				_order = Order(item=_item, merchant=_merchant, purchaser=_purchaser, quantity=entry[3] )
				_order.save()
	
	