import os

os.environ.get('FACEBOOK')

def site_settings_processor(request):
	context_dictionary = {
		'root_url': 'jpark.pythonanywhere.com',
		'admin_name': 'admin',
		'company_name': 'New Living Pools',
		'company_short': 'New Living Pools',
		'footer_copyright': 'SurgeSite, 2015',
		'logo_file_name': 'images/logo.png',
		'site_email': 'jared@surgesite.com',
		# if email changes, update misc_pages/email.html
		'company_phone_text': '602-919-9766',
		'company_phone_link': '16029199766',
		'company_address': '18615 W. Superior Ave Goodyear Az. 85338',
		'yelp_id': '',
		'google_plus_url': 'https://plus.google.com/u/0/b/101072122455137245100',
		'fb_fan_page_url': 'https://www.facebook.com/azspraypros',
		'fb_app_id': '442602292564761',
		'meta_content': 'West Valley Pool Cleaning, Pool Repair, Tile Cleaning, and Pool Equipment Installation Experts',
		'navbar_link1_name': 'home',
		'navbar_link1_text': 'Home',
		'navbar_link2_name': 'pool_service',
		'navbar_link2_text': 'Weekly Service',
		'navbar_link3_name': 'pool_repair',
		'navbar_link3_text': 'Repairs',
		'navbar_link4_name': 'all_services',
		'navbar_link4_text': 'All Services',
		'navbar_link5_name': 'about',
		'navbar_link5_text': 'About',
		'navbar_link6_name': 'contact',
		'navbar_link6_text': 'Contact',
		'sublink1_name': 'pool_repair',
		'sublink1_text': 'Pool Repair',
		'sublink2_name': 'pool_service',
		'sublink2_text': 'Pool Service',
		'sublink3_name': 'pool_service',
		'sublink3_text': 'Handyman',
	}
	return(context_dictionary)