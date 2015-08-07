from django.shortcuts import render
from .forms import TestInstanceForm, GenericTestInstanceForm, DailyPhotonTestInstanceForm, QATestResultForm, FloatValueForm, \
FloatAverageValueForm, TestEquipmentForm, TemperaturePressureForm, UserForm
from django.views.generic.edit import FormView
from django.template import RequestContext, loader
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from wbrc.settings import STATIC_URL

import calendar



# Create your views here.

from .models import Machine, TestInstance, GenericTestInstance, DailyPhotonTestInstance, QATestDefinition, QATestResult,\
QATestAttributeDefinition, QATestAttributeResult, TestEquipment, TemperaturePressure, FloatValue, FloatAverageValue
"""
def login_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        # Correct password, and the user is marked "active"
        auth.login(request, user)
        # Redirect to a success page.
        return HttpResponseRedirect("/account/loggedin/")
    else:
        # Show an error page
        return HttpResponseRedirect("/account/invalid/")
"""
"""
@login_required

def restricted(request):
    return HttpResponse("Since you're logged in, you can see this text!")
"""

#login and logout methods totally plagiarized from How to Tango with Django
def user_login(request):

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
                # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
                # because the request.POST.get('<variable>') returns None, if the value does not exist,
                # while the request.POST['<variable>'] will raise key error exception
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                print "yes we logged in"
                return HttpResponseRedirect('/kitkat/home')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Account is inactive")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'login.html', {})

@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/kiktat/login_form')

def login_form(request):
	return render_to_response('login.html', context_instance=RequestContext(request))

class TestInstanceView(FormView):
	template_name = 'testinstance.html'
	form_class = TestInstanceForm
	#success_url = '/kitkat/latestresults/'

class GenericTestInstanceView(FormView):
	template_name = 'generictestinstance.html'
	form_class = GenericTestInstanceForm
	success_url = '/kitkat/greenfrog/'

class DailyPhotonTestInstanceView(FormView):
	template_name = 'dailyphotontestinstance.html'
	#review = 'first'
	form_class = DailyPhotonTestInstanceForm
	success_url = '/kitkat/greenfrog'
	
def add_testinstance(request):
	str = "Hello Cat wherever you are!"
	print "Hello Cat wherever you are!"
	context = RequestContext(request)
	if request.method == 'POST':
		form = TestInstanceForm(request.POST)
		form.save(commit=True)
	else:
		form = TestInstanceForm()
	if form.is_valid():
		str = str + "okokitisvalid!"
		with open("kitkatlog.txt", "w") as logfile:
			logfile.write(str)
			logfile.write(form.cleaned_data['machine'].machine_name)
			logfile.write(request.read())
#	return render_to_response('latestresults.html', {'form': form}, \
#		context_instance = RequestContext(request)) 
#	return HttpResponseRedirect('/kitkat/latestresults', {'machine_id' : form.cleaned_data['machine'].id})
#	return HttpResponseRedirect('/kitkat/latestresults', args = (request, form.cleaned_data['machine'].id))
#	return HttpResponseRedirect('/kitkat/latestresults(request, %s)' % form.cleaned_data['machine'].id)
		return HttpResponseRedirect('/kitkat/%d/latestresults' % form.cleaned_data['machine'].id)

def add_generictestinstance(request):
	#str = "Hello Cat wherever you are!"
	print "Hello Cat, in add_generictestinstance"
	stri = "Hello Cat, in add_generictestinstance"
	context = RequestContext(request)
	if request.method == 'POST':
		form = GenericTestInstanceForm(request.POST)
#		form.save(commit=True)
	else:
		form = GenericTestInstanceForm()
	if form.is_valid():
		if form.cleaned_data['test_type'] == "Daily Photon Test":
#			upgraded_form = DailyPhotonTestInstanceForm(form)
			stri += "  MATCH!!  "
#			return HttpResponseRedirect('/kitkat/dailyphotontestinstance', \
#			{'machine': form.cleaned_data['machine']})
			upgradedform = DailyPhotonTestInstanceForm(initial={'machine':form.cleaned_data['machine'],\
				'test_type':form.cleaned_data['test_type']})
			return render_to_response('dailyphotontestinstance.html', {'form':upgradedform}, context_instance = context)
#			return HttpResponseRedirect('/kitkat/dailyphotontestinstance', {'form':upgradedform})
			#return HttpResponseRedirect('/kitkat/dailyphotontestinstance', \
			#{'generic_form': form})
		else:
			return HttpResponseRedirect('/kitkat/redfrog')
		stri = stri + str(form.cleaned_data)
	with open("kitkatlog.txt", "w") as logfile:
		logfile.write(stri)

	return render_to_response('generictestinstance.html', context = {'form':form}, context_instance = context)

def add_dailyphotontestinstance(request, review):
#	return HttpResponseRedirect('/kitkat/greenfrog')
	context = RequestContext(request)
	if request.method == 'POST':
		form = DailyPhotonTestInstanceForm(request.POST)	
	else:
		form = DailyPhotonTestInstanceForm()
	if form.is_valid(): 
		#form.test_reading2() 
		if form.test_pass == 0:
#			with open("kitkatlog.txt", "w") as logfile:
#				logfile.write("The test_pass value is 0")
			form.bounds_test()
			return render_to_response('dailyphotontestinstance.html', context = {'form':form}, context_instance = context)
#		else:
#			with open("kitkatlog.txt", "w") as logfile:
#				logfile.write("The test_pass value is non-zero")
#			return HttpResponseRedirect('/kitkat/greenfrog')
		#return render_to_response('dailyphotontestinstance.html', context = {'form':form}, context_instance = context)
#
	else:
		return render_to_response('dailyphotontestinstance.html', context = {'form':form}, context_instance = context)

#	return HttpResponseRedirect('/kitkat/greenfrog')
			
#		str = str + "okokitisvalid!"
#		with open("kitkatlog.txt", "w") as logfile:
#			logfile.write(str)
#			logfile.write(form.cleaned_data['machine'].machine_name)
#	return render_to_response('latestresults.html', {'form': form}, \
#		context_instance = RequestContext(request)) 
#	return HttpResponseRedirect('/kitkat/latestresults', {'machine_id' : form.cleaned_data['machine'].id})
#	return HttpResponseRedirect('/kitkat/latestresults', args = (request, form.cleaned_data['machine'].id))
#	return HttpResponseRedirect('/kitkat/latestresults(request, %s)' % form.cleaned_data['machine'].id)
#		return HttpResponseRedirect('/kitkat/%d/latestresults' % form.cleaned_data['machine'].id)
#		return HttpResonseRedirect('/kitkat/greenfrog')
			
def latestresults(request, machine_id):
		num_recent_show = 20
		num_id = int(machine_id)
		machine_name = Machine.objects.get(id=num_id).machine_name
#		return render(request, 'latestresults.html')
#		return HttpResponse('%d green frogs!  And %d more green frogs.  And many many more happy green frogs hopping!' % (int(machine_id), int(machine_id)))
		latest_test_list = (TestInstance.objects.filter(machine=machine_id)).order_by('-pub_date')[:num_recent_show]
		latest_reading_list = []
		latest_date_list = []
		str_values = []
		for k in range(len(latest_test_list)):
			test_instance = latest_test_list[k]
			latest_reading_list.append(test_instance.reading)
			latest_date_list.append(test_instance.pub_date.date())
			str_values.append(str(test_instance.pub_date.date()) + ":  " + str(test_instance.reading))
		template = loader.get_template('latestresults.html')
		context = RequestContext(request, {'latest_reading_list': latest_reading_list, 'latest_date_list':  latest_date_list, 'str_values': str_values})
		return HttpResponse(template.render(context))

@login_required
def test_view(request):
	resultform = QATestResultForm(request.POST)
	if resultform.is_valid():
		test_def = resultform.cleaned_data['qa_test_def_id']
		attrs = QATestAttributeDefinition.objects.filter(qa_test_def_id=test_def.pk).order_by('form_order')
		attribute_forms = []
		scripts = []
		if test_def.test_name == "Photon Check Calibration":
			scripts.append('script2.js')
		if test_def.test_name == "Daily Photon Test":
			scripts.append('script1.js')
		print scripts

		for attr in attrs:
#			form_ = "form"+attr.form_order
			if attr.attribute_type == "Float Value":
				form = FloatValueForm(prefix = "f"+str(attr.form_order), initial = {'qa_test_attr_def_id': attr}) #want to add test def id as PK here too
				form.set_label(attr.label)
				print form.prefix
				#form.qa_test_attr_def_id = attr #this doesn't work - maybe use a method?
			elif attr.attribute_type == "Float Average Value":
#				print "about to make Float Average Value Form: how did this happen??"
				print len(attrs)
				form = FloatAverageValueForm(prefix = "f"+str(attr.form_order), initial = {'qa_test_attr_def_id': attr}) #want to add test def id as PK here too
				print form.prefix
				#form.qa_test_attr_def_id = attr
				form.set_label(attr.label)
				print form.as_p
			attribute_forms.append(form)
		if test_def.temp_pressure_required:
			form = TemperaturePressureForm(prefix = "ftp")
			attribute_forms.insert(0, form)
		if test_def.test_equip_required:
			form = TestEquipmentForm(prefix = "f_equip")
			attribute_forms.insert(0, form)
		return render_to_response('qa_testforms.html', {'resultform':resultform, 'attribute_forms':attribute_forms, \
			'STATIC_URL':STATIC_URL, 'scripts':scripts}, RequestContext(request) )

def daily_photon_test_view(request):
	formA = QATestResultForm(request.POST)
	if formA.is_valid():
		t = formA.cleaned_data['qa_test_def_id']
		q = QATestAttributeDefinition.objects.filter(qa_test_def_id=t.pk).order_by('-form_order')
#	formB = FloatValueForm(vlabel = "hi!", initial = {'qa_test_attr_def_id': q[0]})
	formB = FloatValueForm(data = {'qa_test_attr_def_id': q[0]})
	formB.set_label(q[0].label)

#	return HttpResponseRedirect("/kitkat/qa_dailyphotontest.html", {'formA': formA, 'formB': formB})
	return render_to_response("qa_dailyphotontest.html", {'formA': formA, 'formB': formB, 'STATIC_URL': STATIC_URL}, RequestContext(request))

def photon_check_calibration_view(request):
#	print "got here"
	formA = QATestResultForm(request.POST)
	if formA.is_valid():
		t = formA.cleaned_data['qa_test_def_id']
		q = QATestAttributeDefinition.objects.filter(qa_test_def_id=t.pk)
	formB = TestEquipmentForm()
	formC = TemperaturePressureForm()
	formD = FloatAverageValueForm(initial = {'qa_test_attr_def_id': q[0]})  #initial doesn't seem to make any difference
	formD.set_label(q[0].label)
	formE = FloatValueForm()
	formE.set_label(q[1].label)
#	print formA.as_p
#	print formB.as_p
	return render_to_response("qa_photoncheckcalibration.html", {'formA': formA, 'formB': formB, 'formC': formC, 'formD': formD, 'formE': formE, 'STATIC_URL': STATIC_URL}, RequestContext(request))
def process_qatestresult(request):
	context = RequestContext(request)
	if request.method == 'POST':
		form = QATestResultForm(request.POST)
		form.save(commit=False)  ##just working on how to get the attribute objects
	else:
		form = QATestResultForm()
	if form.is_valid():
		t = form.cleaned_data['qa_test_def_id']
		q = QATestAttributeDefinition.objects.filter(qa_test_def_id=t.pk)
		for u in q:
			print u
	print str(t)
	if str(t) == "Daily Photon Test":
		return test_view(request)
	elif str(t) == "Photon Check Calibration":
#		print "here"
#		return photon_check_calibration_view(request)
		return test_view(request)

	#return HttpResponseRedirect('/kitkat/redfrog')

def process_dailyphotontest(request):
	formA = QATestResultForm(request.POST)
	formB = FloatValueForm(request.POST)
	saved_formA = formA.save(commit=True)
	
	saved_formB = formB.save(commit=False)
	saved_formB.qa_test_result_id = QATestResult.objects.get(pk=saved_formA.pk)
	print saved_formA.pk
	saved_formB.qa_test_attr_def_id = QATestAttributeDefinition.objects.filter(qa_test_def_id=saved_formA.qa_test_def_id)[0]
	print QATestAttributeDefinition.objects.filter(qa_test_def_id=saved_formA.qa_test_def_id)[0]
	#q = QATestAttributeDefinition.objects.filter(qa_test_def_id=saved_formA.qa_test_def_id)
	#print q
	#saved_formB.
	#formB.save(commit=True)
	saved_formB.save()
	return HttpResponseRedirect('/kitkat/greenfrog')

def process_photoncheckcalibration(request):
	formA = QATestResultForm(request.POST)
	formB = FloatAverageValueForm(request.POST)
	print formB.as_p
	saved_formA = formA.save(commit=True)	
	saved_formB = formB.save(commit=False)
	saved_formB.qa_test_result_id = QATestResult.objects.get(pk=saved_formA.pk)
	print saved_formA.pk
	saved_formB.qa_test_attr_def_id = QATestAttributeDefinition.objects.filter(qa_test_def_id=saved_formA.qa_test_def_id)[0]
	print QATestAttributeDefinition.objects.filter(qa_test_def_id=saved_formA.qa_test_def_id)[0]
	#q = QATestAttributeDefinition.objects.filter(qa_test_def_id=saved_formA.qa_test_def_id)
	#print q
	#saved_formB.
	#formB.save(commit=True)
	#saved_formB.save()
	print saved_formB.entered_values ######this line is just to check output

	return HttpResponseRedirect('/kitkat/greenfrog')

@login_required
class QATestResultView_generic(FormView):
	template_name = 'qa_test_result.html'
	form_class = QATestResultForm
#	success_url = '/kitkat/greenfrog'

@login_required
def qa_test_initial(request):
	form = QATestResultForm()
	return render_to_response("qa_test_result.html", {'form': form}, RequestContext(request))

def greenfrog(request):  ####devel redirect page
	return render_to_response('greenfrog.html', {'STATIC_URL':STATIC_URL})

def redfrog(request):    ####devel redirect page
	return HttpResponse("I am a red frog")

def process_qa_form(request):
	if request.method == 'POST':
		resultform = QATestResultForm(request.POST)
		resultform.user = request.user
		attribute_forms = []
		saved_resultform = resultform.save(commit=False) #do this to get access to test_def (is this necessary?)
		#if resultform.is_valid():
##get test definition

		test_def = saved_resultform.qa_test_def_id
		print test_def
##testequip, temp-pressure if required
		if test_def.test_equip_required:
			print "test_equip"
			form = TestEquipmentForm(request.POST, prefix  = "f_equip")
			attribute_forms.append(form)
		if test_def.temp_pressure_required:
			print "temp_pressure"
			form = TemperaturePressureForm(request.POST, prefix = "ftp")
			attribute_forms.append(form)
#now get attributes from test definition.  Wish there were an easier way
		attrs = QATestAttributeDefinition.objects.filter(qa_test_def_id=test_def).order_by('form_order')
		print attrs
		for attr in attrs:
			print "attrs"
			if attr.attribute_type == "Float Value":
				form = FloatValueForm(request.POST, prefix = "f"+str(attr.form_order)) 
				#form.set_label(attr.label)
			elif attr.attribute_type == "Float Average Value":
				form = FloatAverageValueForm(request.POST, prefix = "f"+str(attr.form_order)) #want to add test def id as PK here too
				#form.set_label(attr.label)
			attribute_forms.append(form)
		all_valid = True
		counter = 1
		for form in attribute_forms:
			if not form.is_valid():
				print "form "+str(counter)+" does not validate"
				counter+=1
				all_valid = False
			else:
				print "form "+str(counter)+" DOES validate"
				#print "the attribute is defined as " +str(form.cleaned_data['qa_test_attr_def_id'])
				#print form.cleaned_data['qa_test_attr_def_id'].attribute_type
				counter+=1

		if not resultform.is_valid():
			all_valid = False
		print "The result form is valid? " + str(resultform.is_valid())
		print "all_valid is " + str(all_valid)
		if not all_valid:
			scripts = []
			if test_def.test_name == "Photon Check Calibration":
				scripts.append('script2.js')
			if test_def.test_name == "Daily Photon Test":
				scripts.append('script1.js')
			return render_to_response('qa_testforms.html', {'resultform':resultform, 'attribute_forms':attribute_forms, \
			'STATIC_URL':STATIC_URL, 'scripts':scripts}, RequestContext(request) )
		if all_valid:
		#save everything!
			saved_resultform.user = request.user
			saved_resultform.save()
			for form in attribute_forms:
				saved_form = form.save(commit=False)
				saved_form.qa_test_result_id = saved_resultform
				#if hasattr(saved_form, 'qa_test_attr_def_id'):
					#print "has attribute"
				if isinstance(saved_form, QATestAttributeResult):
					print "is instance"
					saved_form.qa_test_attr_def_id = form.cleaned_data['qa_test_attr_def_id']  #No idea why I had to add this to make it validate
				#print "do we still have a test attr def id? " + str(saved_form.qa_test_attr_def_id_id)
				saved_form.save()
			#resultform.save(commit=True)
			#return HttpResponse('placeholder')
			return HttpResponseRedirect("/kitkat/%d/display_entry" % saved_resultform.pk  )
			
			#while more_attrs:
				
				
				
				
				
	return HttpResponse('placeholder')


@login_required
def home(request):
#	return HttpResponseRedirect("/kitkat/home.html")
	template = loader.get_template('home.html')
	linklabel = "Record QA event"
	link = '/kitkat/qa_test_result'
	context = RequestContext(request, {'linklabel': linklabel, 'link': link})
	return HttpResponse(template.render(context))
"""
def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	template = loader.get_template('polls/index.html')
	context = RequestContext(request, {'latest_question_list': latest_question_list })
	return HttpResponse(template.render(context))
"""

@login_required
def display_entry(request, test_result_id):
	print test_result_id
	Result = QATestResult.objects.get(pk=test_result_id)
	Testequip = TestEquipment.objects.filter(qa_test_result_id=Result)
	TempPressure = TemperaturePressure.objects.filter(qa_test_result_id=Result)
	attributes = QATestAttributeResult.objects.filter(qa_test_result_id=Result)
	attributes = sorted(attributes, key = lambda attr: attr.qa_test_attr_def_id.form_order)
	response = HttpResponse()
	response.write("<p>%s : %s</p>" % ("Date", Result.pub_date) )
	response.write("<p>%s : %s</p>" % ("User", Result.user) )
	response.write("<p>%s : %s</p>" % ("QA test", str(Result.qa_test_def_id)) )
	response.write("<p>%s : %s</p>" % ("Machine", str(Result.machine_id)) )
	if not len(Testequip) == 0:
		response.write("<p>%s : %s</p>" % ("Electrometer", str(Testequip[0].electrometer)) )
		response.write("<p>%s : %s</p>" % ("Ion Chamber", str(Testequip[0].ionchamber)) )
	if not len(TempPressure) == 0:
		response.write("<p>%s : %.2f</p>" % ("Temperature", TempPressure[0].temperature) )
		response.write("<p>%s : %.2f</p>" % ("Pressure", TempPressure[0].pressure) )
	for attribute in attributes:
#		print attribute.qa_test_attr_def_id
		if attribute.qa_test_attr_def_id.attribute_type == "Float Value":
			if isinstance(attribute, FloatValue):
				print "is instance"
			floatvalue = FloatValue.objects.get(pk=attribute.pk)
			response.write("<p>%s : %.2f</p>" % (floatvalue.qa_test_attr_def_id.label, floatvalue.value) )
		if attribute.qa_test_attr_def_id.attribute_type == "Float Average Value":
			floataveragevalue = FloatAverageValue.objects.get(pk=attribute.pk)
			response.write("<p>%s : %s</p>" % (floataveragevalue.qa_test_attr_def_id.label, floataveragevalue.entered_values) )
			response.write("<p>%s : %.2f</p>" % ("Mean", floataveragevalue.mean_value) )
	response.write("<p><a href=\'/kitkat/home\'>Home</a></p>")
	response.write("<p><a href=\'/kitkat/%d/%d/past_results\'>Past entries for %s on %s</a></p>" % \
		(Result.qa_test_def_id.pk, Result.machine_id.pk, str(Result.qa_test_def_id), str(Result.machine_id) ) )
	return response

@login_required
def past_results	(request, qa_test_def, machine):
	machine = int(machine)
	qa_test_def = int(qa_test_def)
	result_set = QATestResult.objects.all()
	print "the result set is this big: %d" % len(result_set)
	if machine != 0:
		result_set = result_set.filter(machine_id=machine)
	print "the result set is this big: %d" % len(result_set)
	if qa_test_def != 0:
		result_set = result_set.filter(qa_test_def_id=qa_test_def)
	print "the result set is this big: %d" % len(result_set)
	result_set = result_set.order_by('-pub_date')
	response = HttpResponse()
	for result in result_set:
		response.write("<p><a href=\'/kitkat/%d/display_entry\'>%s</a></p>" % (result.pk, str(result)) )
	response.write("<a href=\'/kitkat/home\'>Home</a>")
	return response

@login_required
def recent_results_daily_photon_output_test(request):
	#print "got to the results method"
	num_recent = 5
	recent_readings = []
	reading_times = []
	if request.method == 'GET':
		machine_name = request.GET['machine_name']
	#print "flag 1"
	#machine_name = request.POST['machine_name']
	#result_set = QATestResult.objects.filter(machine_id=).order_by('-pubdate')[0:5][::-1]
	test_def = QATestDefinition.objects.get(test_name="Daily Photon Test")
	#print "flag 2"
	result_set = QATestResult.objects.filter(qa_test_def_id=test_def)
	#print result_set
	#print "flag 3"
	machine = Machine.objects.get(machine_name=machine_name)
	result_set = result_set.filter(machine_id=machine).order_by('-pub_date')
	#print len(result_set)
	for i in range(num_recent):
		attr = FloatValue.objects.filter(qa_test_result_id=result_set[i].pk)
		print len(attr)
		if(len(attr) == 1):
			recent_readings.append(attr[0].value)
			reading_times.append(calendar.timegm(result_set[i].pub_date.timetuple()) * 1000)
	#print recent_readings
	#print "flag 4"
	data = str(reading_times[0]) + " " + str(recent_readings[0])
	for i in range(1, len(recent_readings)):
		data +="/" + str(reading_times[i]) + " " + str(recent_readings[i])
#	reading_times_string = str(reading_times[0])
#	for i in range(1, len(reading_times)):
#		reading_times_string +=" " + str(reading_times[i])
#	data = recent_readings_string + "/" + reading_times_string

	return HttpResponse(data)
	#return HttpResponse("helo")
	

