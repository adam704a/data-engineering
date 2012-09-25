# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader, RequestContext
from django.shortcuts import get_object_or_404, render_to_response
from dataloader.models import Order

def index(request):
	order_list = Order.objects.all()[:5]
	t = loader.get_template('dataloader/index.html')
	c = Context({
	        'order_list': order_list,
	})
	return render_to_response('dataloader/index.html', {'orders': order_list }, context_instance=RequestContext(request))