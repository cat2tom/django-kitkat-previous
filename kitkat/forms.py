from django import forms
from django.contrib.auth.models import User
from .models import TestInstance, Machine, GenericTestInstance, DailyPhotonTestInstance, TEST_TYPE_CHOICES, \
	daily_photon_test_upper_bound, daily_photon_test_lower_bound, QATestDefinition, Electrometer, IonChamber, QATestResult, \
	QATestAttributeResult, FloatValue, FloatAverageValue, TestEquipment, TemperaturePressure, QATestAttributeDefinition

#####tango
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
"""
#no need for user profile - only if we want to store additional info
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')
"""
#####/tango


class TestInstanceForm(forms.ModelForm):
	reading = forms.FloatField()
	machine = forms.ModelChoiceField(queryset=Machine.objects.all())
#	pub_date = forms.DateTimeField()
	
	class Meta:
		model = TestInstance
		fields = ('machine', 'reading')
#		fields = ('machine', 'reading', 'pub_date')
		#excludes = ()

class GenericTestInstanceForm(forms.ModelForm):
	machine = forms.ModelChoiceField(queryset=Machine.objects.all())
	test_type = forms.ChoiceField(choices=TEST_TYPE_CHOICES)

	class Meta:
		model = GenericTestInstance
		fields = ('machine', 'test_type')

class DailyPhotonTestInstanceForm(GenericTestInstanceForm):
	reading = forms.FloatField()
	test_pass = 0
	
	class Meta:
		model = DailyPhotonTestInstance
		fields = ('machine', 'test_type', 'reading',)

	def 	bounds_test(self):
		if self.cleaned_data['reading'] <= daily_photon_test_upper_bound and self.cleaned_data['reading'] >= daily_photon_test_lower_bound:
			self.test_pass = 1
		else:
			self.test_pass = -1

"""
	def test_pass_defined(self):
		return not (self.test_pass == None)
	def test_reading(self):
		return self.reading <= daily_photon_test_upper_bound and self.reading >= daily_photon_test_lower_bound
	def test_reading2(self):
		return self.cleaned_data['reading'] <= daily_photon_test_upper_bound and self.cleaned_data['reading'] >= daily_photon_test_lower_bound
"""	
#		fields = '__all__'
#		exclude = ('machine', 'test_type')

"""
	def 	bounds_test2(self):
		if self.reading <= daily_photon_test_upper_bound and self.reading >= daily_photon_test_lower_bound:
			self.test_pass = 1
		else:
			self.test_pass = -1 
"""

class QATestResultForm(forms.ModelForm):
	qa_test_def_id=forms.ModelChoiceField(queryset=QATestDefinition.objects.all(), label = "QA Test Type")
	machine_id = forms.ModelChoiceField(queryset=Machine.objects.all())
#	electrometer_id = forms.ModelChoiceField(queryset=Electrometer.objects.all(), required = False)
#	ionchamber_id = forms.ModelChoiceField(queryset=IonChamber.objects.all(), required = False)

	class Meta:
		model = QATestResult
#		fields = ('qa_test_def_id', 'machine_id', 'electrometer_id', 'ionchamber_id')
		fields = ('qa_test_def_id', 'machine_id')

class QATestAttributeResultForm(forms.ModelForm):
	qa_test_attr_def_id = forms.ModelChoiceField(queryset = QATestAttributeDefinition.objects.all(), widget = forms.HiddenInput())
	qa_test_result_id = None # also automatic
	class Meta:
		model = QATestAttributeResult
		fields = ('qa_test_attr_def_id',)

class FloatValueForm(QATestAttributeResultForm):
#	vlabel = "Placeholder"
	print "in float value form"
	value = forms.FloatField()
	class Meta:
		model = FloatValue
		fields = ('value',)

	"""		def __init__(self, vlabel=None, *args, **kwargs):
			print "made it to the custom initiation method"
#			vlabel = kwargs.pop('vlabel', None)
			super(FloatValueForm, self).__init__(*args, **kwargs)
			if vlabel:
				self.fields['value'].label=vlabel"""

	def set_label(self, vlabel):
		self.fields['value'].label = vlabel

class FloatAverageValueForm(QATestAttributeResultForm):
#	entered_values = forms.CharField(label="Output check readings")  #THIS SHOULD NOT HAVE A LABEL!!
	entered_values = forms.CharField(widget=forms.Textarea(attrs={'cols': 10, 'rows': 5}))

#	mean_value = forms.FloatField(widget=forms.HiddenInput) #this needs to be calculated
	mean_value = forms.FloatField(label="Mean")

	def set_label(self, vlabel):
		self.fields['entered_values'].label = vlabel


	class Meta:
		model = FloatAverageValue
		fields = ('entered_values', 'mean_value')

class TestEquipmentForm(forms.ModelForm):
	qa_test_result_id = None # also automatic
	electrometer = forms.ModelChoiceField(queryset=Electrometer.objects.all(), required = True) #we should require this
	ionchamber = forms.ModelChoiceField(label="Ion Chamber", queryset=IonChamber.objects.all(), required = True)
	
	class Meta:
		model = TestEquipment
		fields = ('electrometer', 'ionchamber')

class TemperaturePressureForm(forms.ModelForm):
	qa_test_result_id = None # also automatic
	temperature = forms.FloatField()
	pressure = forms.FloatField()
	
	class Meta:
		model = TemperaturePressure
		fields = ('temperature', 'pressure')
