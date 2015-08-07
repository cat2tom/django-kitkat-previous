from django.conf.urls import url
from django.contrib.auth.views import login, logout
from django.contrib.auth.decorators import login_required


from . import forms
from . import views

urlpatterns = [
	url(r'^home/+$', views.home, name = 'home'),
	url(r'^testinstance/+$', views.TestInstanceView.as_view(), name='testinstance'),
	url(r'^generictestinstance/+$', views.GenericTestInstanceView.as_view(), name='generictestinstance'),
	url(r'^dailyphotontestinstance/+$', views.DailyPhotonTestInstanceView.as_view(), name='dailyphotontestinstance'),
	url(r'^(?P<machine_id>[0-9]+)/latestresults/+$', views.latestresults, name='latestresults'),
    url(r'^add_testinstance/+$', views.add_testinstance, name='add_testinstance'), # NEW MAPPING!
    url(r'^add_generictestinstance/+$', views.add_generictestinstance, name='add_generictestinstance'), # NEW MAPPING!
    url(r'^add_dailyphotontestinstance/(?P<review>\w+)/?$', views.add_dailyphotontestinstance, name='add_dailyphotontestinstance'), # NEW MAPPING!
	url(r'^greenfrog/+$', views.greenfrog, name='greenfrog'),
	url(r'^redfrog/+$', views.redfrog, name='redfrog'),
#	url(r'^qa_test_result/+', login_required(views.QATestResultView_generic.as_view()), name='qa_test_result'),
	url(r'^qa_test_result/+', views.qa_test_initial, name='qa_test_result'),
    url(r'^process_qatestresult/+$', views.process_qatestresult, name='process_qatestresult'), # NEW MAPPING!
    url(r'^process_dailyphotontest/+$', views.process_dailyphotontest, name = 'process_dailyphotontest'),
    url(r'^process_photoncheckcalibration/+$', views.process_photoncheckcalibration, name = 'process_photoncheckcalibration'),
    url(r'^user_login/$', views.user_login, name='user_login'),
    url(r'^login_form/$', views.login_form, name='login_form'),
    url(r'^process_qa_form/$', views.process_qa_form, name='process_qa_form'),
	url(r'^(?P<test_result_id>[0-9]+)/display_entry/+$', views.display_entry, name = 'display_entry'),
	url(r'^(?P<qa_test_def>[0-9]+)/(?P<machine>[0-9]+)/past_results/+$', views.past_results, name = 'past_results'),
    url(r'^user_logout/$', views.user_login, name='user_logout'),
    url(r'^recent_results_daily_photon_output_test/$', views.recent_results_daily_photon_output_test, name='recent_results_daily_photon_output_test'),

#	url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'admin/login.html'}),
 #   url(r'^accounts/logout/$', 'django.contrib.auth.views.logout'),

]

# 	url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name = 'results'),
