# from climate.hum_temp import get_humidity_temperature
from datetime import datetime, time
from .models import Schedule, ScheduleLog, RelayStatus
from climate.models import Exhaust, ClimateValues, ClimateLogs
import time

def schedule_relay(*args):
	print('schedule_relay_job 1')
	gpio_pin = args[1]
	dt = datetime.now()
	end_dt = dt + args[0]
	try:
		relay_status = RelayStatus.objects.get(gpio_pin=gpio_pin)
		relay_status.schedule_status=True
		relay_status.gpio_pin=gpio_pin
		relay_status.save()
	except Exception as e:
		relay_status = RelayStatus()
		relay_status.schedule_status=True
		relay_status.button_status=False
		relay_status.gpio_pin=gpio_pin
		relay_status.save()
		pass
	start_time = datetime.now()
	break_loop = args[2]
	print(relay_status.schedule_status)
	# relay = gpiozero.OutputDevice(int(gpio_pin), active_high=True, initial_value=False)
	while not break_loop:
		try:
			print(f'schedule_relay_job relay {gpio_pin}')

		except Exception as e:
			pass
		relay_status = RelayStatus.objects.get(gpio_pin=gpio_pin)
		if relay_status.schedule_status == 'False':
			break_loop=True
		if end_dt < datetime.now():
			break_loop = True
		time.sleep(3)

	relay_status = RelayStatus.objects.get(gpio_pin=gpio_pin)
	relay_status.schedule_status=False
	relay_status.gpio_pin=gpio_pin
	relay_status.save()
	schedule_log = ScheduleLog()
	convert_to_time=(datetime.min + args[0]).time()
	schedule_log.duration = str(convert_to_time)
	schedule_log.start = start_time
	schedule_log.gpio_pin = gpio_pin
	schedule_log.save()

def relay_14():
	return

def relay_15():
	return

def relay_2():
	return

def relay_3():
	return

def check_climate():
	humidity, fahrenheit, vpd = 0,0,0
	if humidity is not None and fahrenheit is not None:
		humidity = int(humidity)
		# This is were we will check for day time param or night time params
		try:
			ht_day_params = ClimateValues.objects.get(pk=1)
		except Exception as e:
			ht_day_params = ClimateValues()
			ht_day_params.pk=1
			ht_day_params.humidity_value=humidity
			ht_day_params.buffer_value=5
			ht_day_params.temp_value=int(fahrenheit)
			ht_day_params.save()
		try:
			ht_night_params = ClimateValues.objects.get(pk=2)
		except Exception as e:
			ht_night_params = ClimateValues()
			ht_night_params.pk=2
			ht_night_params.humidity_value=humidity
			ht_night_params.buffer_value=5
			ht_night_params.temp_value=int(fahrenheit)
			ht_night_params.start_time=datetime.now().time()
			ht_night_params.end_time=datetime.now().time()
			ht_night_params.save()
		timenow = datetime.now().time()
		if timenow > ht_night_params.start_time and timenow < ht_night_params.end_time:
			ht_params = ClimateValues.objects.get(pk=2)
		else:
			ht_params = ClimateValues.objects.get(pk=1)

		humidity_positive = ht_params.humidity_value+ht_params.buffer_value
		humidity_nagitive = ht_params.humidity_value-ht_params.buffer_value
		temp_params = ht_params.temp_value+ht_params.buffer_value
		print(humidity_positive, temp_params)
		button_job_id = f'button_relay_job_id_3'
		if humidity >= humidity_positive:
			try:
				e = Exhaust.objects.get(pk=2)
				if e.automation_status == 'True':
					if e.status == 'True':
						print('Exhuast arlready running so continue')
					else:
						e.job_id=button_job_id
						e.status=True
						e.save()
						button_relay_job('True',3,button_job_id)
				else:
					e.job_id=button_job_id
					e.status=False
					e.save()
					button_relay_job('False',3,button_job_id)
			except Exception as e:
				pass


		elif int(fahrenheit) >= temp_params:
			try:
				e = Exhaust.objects.get(pk=2)
				if e.status == 'True':
					print('Exhuast arlready running so continue')
				else:
					e.job_id=button_job_id
					e.status=True
					e.save()
					button_relay_job('True',3,button_job_id)
			except Exception as e:
				pass

		else:
			try:
				e = Exhaust.objects.get(pk=2)
				e.job_id=button_job_id
				e.status=False
				e.save()
				button_relay_job('False',3,button_job_id)
			except Exception as e:
				pass

		button_2_job_id = f'button_relay_job_id_2'
		if humidity <= humidity_nagitive:
			try:
				e = Exhaust.objects.get(pk=1)
				if e.status == 'True':
					print('Exhuast arlready running so continue')
				else:
					e.job_id=button_2_job_id
					e.status=True
					e.save()
					button_relay_job('True',2,button_2_job_id)
			except Exception as e:
				pass

		else:
			try:
				e = Exhaust.objects.get(pk=1)
				e.job_id=button_2_job_id
				e.status=False
				e.save()
				button_relay_job('False',2,button_2_job_id)
			except Exception as e:
				pass

	else:
		print('Failed to retrieve data from climate sensor.')

def climate_logs():
	humidity, fahrenheit, vpd = 0,0,0
	if humidity is not None and fahrenheit is not None:
		humidity = int(humidity)
		ht_log = ClimateLogs()
		ht_log.humidity = humidity
		ht_log.temp = int(fahrenheit)
		ht_log.vpd = vpd
		ht_log.save()
	else:
		print('Failed to retrieve data from humidity sensor.')

def button_relay_job(status,gpio_pin,button_job_id):
	return

def add_schedule(how_often_day, how_often,schedule_duration,gpio_pin,schedule_job_id):
	print(how_often)
	if gpio_pin == '3':
		triggers = CronTrigger(minute=how_often_day)
		try:
			e = Exhaust.objects.get(pk=1)
			e.status=False
			e.automation_status=False
			e.save()
			e3 = Exhaust.objects.get(pk=2)
			e3.status=False
			e3.automation_status=False
			e3.save()
			button_relay_job('False',2,'button_relay_job_id_2')
			button_relay_job('False',3,'button_relay_job_id_3')
		except Exception as e:
			pass
	else:
		print(type(how_often.hour))
		# triggers = CronTrigger(day_of_week=how_often_day, hour=how_often.hour, minute=how_often.minute)
	# scheduler.add_job(schedule_relay, triggers, args=[schedule_duration,gpio_pin,False], id=schedule_job_id, misfire_grace_time=None, replace_existing=True)
	return

def remove_schedule(schedule_job_id,gpio_pin):
	return
def exhaust_automation():
	return

def schedule_display_inputs(display,gpio_pin):
	count=0
	for d in display:
		print(d)
		duration_hours = d[1]
		duration_minutes = d[2]
		if duration_hours == '0':
			duration_display = f'For {duration_minutes} Minutes'
		elif duration_minutes == '0':
			duration_display = f'For {duration_hours} Hours'
		else:
			duration_display = f'For {duration_hours} Hours {duration_minutes} Minutes'
		try:
			schedule_job_id = d[3]
			set_schedule = Schedule.objects.get(job_id=schedule_job_id)
			set_schedule.duration=duration_display
			set_schedule.schedule_interval=d[0]
			set_schedule.gpio_pin=int(gpio_pin)
			set_schedule.job_id=schedule_job_id
			set_schedule.save()
		except Exception as e:
			try:
				set_schedule = Schedule()
				set_schedule.duration=duration_display
				set_schedule.schedule_interval=d[0]
				set_schedule.gpio_pin=int(gpio_pin)
				set_schedule.job_id=schedule_job_id
				set_schedule.save()
			except Exception as e:
				print(e)
				pass
		count+=1
	return

def start():
	return