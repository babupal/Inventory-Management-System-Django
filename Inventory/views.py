from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Item,Transaction, Client, Account_Details
from django.shortcuts import render,get_object_or_404
from django import forms
from django.template import RequestContext
from django.core.paginator import Paginator , EmptyPage, PageNotAnInteger
from printing import MyPrint
from io import BytesIO
from datetime import datetime

def index(request):
	items_list=Item.objects.all()
	context={
		'items_list':items_list,	
	}	
	return render(request,'index.html',context)

def home(request):
	items_list=Item.objects.all()
	context={
		'items_list':items_list,	
	}	
	return render(request,'home.html',context)

def details(request,item_id):
	item=get_object_or_404(Item,pk=item_id)
	clients=Client.objects.all()
	return render(request,'details1.html',{'item':item,'clients':clients})

def transitm(request,item_id):
	print("In transitm with request : " + str(request))
	print("            with item_id : " + str(item_id))
	client=Client.objects.get(place=request.POST.get("client"))
	item=Item.objects.get(pk=item_id)
	quantity=request.POST.get("quantity")
	transaction=Transaction(quantity=quantity,item=item,client=client)
	transaction.save()
	activity=request.POST.get("activity")
	print("Activity is " + str(activity))
	transfer_amount=int(quantity) * item.price
	if (activity == 'TRANSFER'):
		print("found transfer")
		prepos="to"
		item.quantity=item.quantity-int(quantity)
		client.balance=client.balance - transfer_amount
	elif (activity == 'RETURN'):
		print("found return")
		prepos="from"
		item.quantity=item.quantity+int(quantity)
		transfer_amount=int(quantity) * item.price
		client.balance=client.balance + transfer_amount
	elif (activity == 'SALE'):
		print("found sale")
		prepos="to"
		item.quantity=item.quantity-int(quantity)
		transfer_amount=int(quantity) * item.price
		client.balance=client.balance - transfer_amount
	elif (activity == 'PURCHASE'):
		print("found purchase")
		prepos="from"
		item.quantity=item.quantity+int(quantity)		
		transfer_amount=int(quantity) * item.price
		client.balance=client.balance + transfer_amount		
	else:
		print("unknown activity")
	item.save()
	client.save()
	account_details=Account_Details(transaction=transaction,debit_amount=transfer_amount,credit_amount=0.00,balance_amount=0.00,client=client,description='debit due to transfer')
	account_details.save()	
	print("Rendering transferitm.html quantity is " + str(quantity))
	return render(request,'trans_result.html',
		{'transaction':transaction,'activity':activity,'quantity':quantity,'item':item,'client':client,'prepos':prepos}
		)

def clients(request):
    print("In Views.py Entering clients request is " + str(request))
    clients_list=Client.objects.all()
    context={
		'clients_list':clients_list,	
	}
    print("rendering clients.html context is " + str(context))
    return render(request,'clients.html',context)

def account_details(request,client_id):
	print("In Views.py Entering account_details request is " + str(request))
	print(".. client_id is " + str(client_id))
	client=Client.objects.get(id=client_id)
	account_details_list=Account_Details.objects.filter(client=client_id)
#	account_details_list=Account_Details.objects.all()
	context={
		'account_details_list':account_details_list,	
	}	
	page = request.GET.get('page',1)
	paginator = Paginator(account_details_list, 5) # Show 10 records per page.
	try:
		acdets = paginator.page(page)
	except PageNotAnInteger:
		acdets = paginator.page(1)
	except EmptyPage:
		acdets = paginator.page(paginator.num_pages)
#	print ("rendering account_details.html context is " + str(context))
#	return render(request,'account_details.html',context)
	return render(request,'account_details.html',{ 'account_details_list': acdets, 'client':client})

# @staff_member_required

def print_users(request):
    # Create the HttpResponse object with the appropriate PDF headers.
	response = HttpResponse(content_type='application/pdf')
	# d = datetime.today().strftime('%Y-%m-%d')
	response['Content-Disposition'] = 'attachment; filename="MyUsers.pdf"'
	#response['Content-Disposition'] = 'inline; filename="{d}.pdf"'

	buffer = BytesIO()

	report = MyPrint(buffer, 'Letter')
	pdf = report.print_users()

	response.write(pdf)
	return response

def print_items(request):
	response = HttpResponse(content_type='application/pdf')
	d = datetime.today().strftime('%Y-%m-%d')
	fname=str(d)
	print(fname)
	#response['Content-Disposition'] = 'attachment; filename="Items as at {d}.pdf"'
	#response['Content-Disposition'] = 'inline; filename="{d}.pdf"'
	response['Content-Disposition'] = 'attachment; filename="{fname}.pdf"'

	buffer = BytesIO()

	report = MyPrint(buffer, 'Letter')
	pdf = report.print_items()

	response.write(pdf)
	return response
