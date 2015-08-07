from django.db import models
from django.contrib.auth.models import User

# Create your models here.

###CONSTANTS:
#Machine
serial_number_max_length = 50
machine_name_max_length = 20

#GenericTestInstance
test_type_max_length = 20
TEST_TYPE_CHOICES = [('', '-------'), ('Daily Photon Test', 'Daily Photon Test'), ('Other Test', 'Other Test')]
#TEST_TYPE_CHOICES = [('Daily Photon Test', 'Daily Photon Test'), ('Other Test', 'Other Test')]

#DailyPhotonTestInstance
daily_photon_test_upper_bound = 197.5
daily_photon_test_lower_bound = 186.0

#Electrometer
electrometer_name_max_length = 20

##new since report
qa_test_name_max_length = 50
ATTR_TYPE_CHOICES = [('', '-------'), ('Bool Value', 'Bool Value'), ('Float Value', 'Float Value'), ('Float Average Value', 'Float Average Value'),\
 ('Calc Bool Value', 'Calc Bool Value'), ('Calc Float Value', 'Calc Float Value')]

class Machine(models.Model):
	#serial_number = models.CharField(max_length=serial_number_max_length)
	machine_name = models.CharField(max_length=machine_name_max_length)
	def __str__(self):
		return self.machine_name
		
class TestInstance(models.Model):
	reading = models.FloatField() #FloatField or DecimalField?  Not finalised
	pub_date = models.DateTimeField(auto_now_add=True)
	machine = models.ForeignKey(Machine)

class GenericTestInstance(models.Model):
 	pub_date = models.DateTimeField(auto_now_add=True)
	machine = models.ForeignKey(Machine)
	#we want user here as well
	test_type = models.CharField(max_length = test_type_max_length, choices = TEST_TYPE_CHOICES)
   
class DailyPhotonTestInstance(GenericTestInstance):
	#generic_test = models.ForeignKey(GenericTestInstance)
	reading = models.FloatField()
#	test_pass = models.BooleanField()  #######reeeally did not want to put this in, trying to make pass/fail display work
	
	def _within_bounds(self):
		if self.reading >= lower_bound and self.reading <= upper_bound:
			return True
		else:
			return False


class Electrometer(models.Model):
	electrometer_name = models.CharField(max_length = electrometer_name_max_length)
	def __str__(self):
		return self.electrometer_name
"""
class PhotonCheckCalibration(GenericTestInstance):
	electrometer = models.ForeignKey(Electrometer)
"""
#The whole ion chamber logic below is based on my having no understanding of the functional relationship
#between "val 2" and the expected readings at 6MV and 18MV, hopefully I can improve this!
class IonChamber(models.Model):
	val1 = models.IntegerField(default=0) #temporary field name
	val2 = models.IntegerField(default=0) #temporary field name
	expected_reading_6MV = models.FloatField(default=0) #potential to calculate from "val2"?
	expected_reading_18MV = models.FloatField(default=0)
	def __str__(self):
		return str(self.val1) + '/' + str(self.val2)
		
class QAFloatComponent(models.Model):
	num = models.FloatField()

#########post report models:

class QATestDefinition(models.Model):
	test_name = models.CharField(max_length = qa_test_name_max_length)
	frequency = models.CharField(max_length = 20) #magic number
	test_equip_required = models.BooleanField()
	temp_pressure_required = models.BooleanField()
	def __str__(self):
		return self.test_name

	#need def of which machines test can refer to
	#need which Electrometers, Ion Chambers can be selected depending on which machine

class QATestAttributeDefinition(models.Model):
	qa_test_def_id = models.ForeignKey(QATestDefinition)
	label = models.CharField(max_length=30) #magic number
	attribute_type = models.CharField(max_length=30, choices = ATTR_TYPE_CHOICES)
	form_order = models.SmallIntegerField()
	def __str__(self):
		return self.label

class QATestResult(models.Model):
	qa_test_def_id = models.ForeignKey(QATestDefinition)
	pub_date = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(User)
	machine_id = models.ForeignKey(Machine)
#	electrometer_id = models.ForeignKey(Electrometer, blank=True, null=True)
#	ionchamber_id = models.ForeignKey(IonChamber, blank=True, null=True)

	def __str__(self):
		return str(self.qa_test_def_id) +" "+ str(self.machine_id) +" "+ "%d/%d/%d %d:%d" % \
	(self.pub_date.day, self.pub_date.month, self.pub_date.year, self.pub_date.hour, self.pub_date.minute)
#+ " test type " + str(self.qa_test_def_id)

class TestEquipment(models.Model):
	qa_test_result_id = models.ForeignKey(QATestResult)
	electrometer = models.ForeignKey(Electrometer, blank=True, null=True)
	ionchamber = models.ForeignKey(IonChamber, blank=True, null=True)

class TemperaturePressure(models.Model):
	qa_test_result_id = models.ForeignKey(QATestResult)
	temperature = models.FloatField()
	pressure = models.FloatField()	
#	def __str__(self):
#		return "

class QATestAttributeResult(models.Model):
	qa_test_result_id = models.ForeignKey(QATestResult)
	qa_test_attr_def_id = models.ForeignKey(QATestAttributeDefinition)

class BoolValue(QATestAttributeResult):
	value = models.BooleanField()
	
class FloatValue(QATestAttributeResult):
	value = models.FloatField()

class FloatAverageValue(QATestAttributeResult):
	entered_values = models.CharField(max_length=100) #magic number
	mean_value = models.FloatField()  #calculated, how, oh how

class CalcBoolValue(QATestAttributeResult):
	value = models.BooleanField()

class CalcFloatValue(QATestAttributeResult):
	value = models.FloatField()
	
