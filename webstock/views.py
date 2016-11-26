from django.shortcuts import render, redirect
from .models import stocks
from datetime import datetime, timedelta
from yahoo_finance import Share
from django.core import serializers

# Create your views here.

def date_sanitize(date):
	day = date[:2]
	month = date[2:4]
	year = date[4::]
	date_string = '%s-%s-%s' % (year, month, day)
	return date_string

def dbpopulate(comp_name):
	td = datetime.today() - timedelta(days=1)
	ld = td - timedelta(days=9)
	td_string = str(td).split()[0]
	ld_string = str(ld).split()[0]
	comp = Share(comp_name)
	try:
		history = comp.get_historical(ld_string, td_string)
		for h in history:
			stocks.objects.create(symbol = comp_name, date = h['Date'], opening = h['Open'], closing = h['Close'])
		return True
	except:
		return False

def goc(request, comp_name, date):
	date_string = date_sanitize(date)
	if stocks.objects.filter(symbol=comp_name).exists():
		if stocks.objects.filter(date=date_string).exists():
			json_object = serializers.serialize("json", stocks.objects.filter(date=date_string))
			return render(request, 'webstock/goc.html', {'json_object': json_object})
		else:
			stocks.objects.filter(symbol=comp_name).delete()
			return redirect('goc', comp_name=comp_name, date=date)
	else:
		if dbpopulate(comp_name):
			return redirect('goc', comp_name = comp_name, date = date)
		else:
			return render(request, 'webstock/404.html')

def goc_range(request, comp_name, startD, endD):
	startD_string = date_sanitize(startD)
	endD_string = date_sanitize(endD)
	if stocks.objects.filter(symbol=comp_name).exists():
		if stocks.objects.filter(date=endD_string).exists() and stocks.objects.filter(date=startD_string).exists():
			stock_range = stocks.objects.filter(symbol=comp_name).exclude(date__gt=endD_string).filter(date__gte=startD_string)
			context = {'comp_name': comp_name, 'startD_string': startD_string, 'endD_string': endD_string, 'stock_range': stock_range}
			return render(request, 'webstock/goc_range.html', context)
		else:
			stocks.objects.filter(symbol=comp_name).delete()
			return redirect('goc_range', comp_name = comp_name, startD = startD, endD = endD)
	else:
		if dbpopulate(comp_name):
			return redirect('goc_range', comp_name = comp_name, startD = startD, endD = endD)
		else:
			return render(request, 'webstock/404.html')