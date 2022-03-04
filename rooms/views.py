import json
from django.shortcuts import render, redirect
from datetime import datetime, date
from django.contrib.auth.decorators import login_required
import requests
# Create your views here.
def get_all_rooms(request):
	# url = "http://127.0.0.1:5000/rooms"
	url = "http://10.42.0.1:5000/rooms"
	rooms_response = requests.get(url)
	if rooms_response.status_code == 409:
		context = {
			'get_all_rooms': [],
			'room_id':1,
			'get_ip': []
		}
		return render(request, 'rooms.html',context)
	# url = f"http://127.0.0.1:5000/all_ips"
	url = f"http://10.42.0.1:5000/all_ips"
	ip_response = requests.get(url)
	if ip_response.status_code == 200:
		context = {
			'get_all_rooms': rooms_response.json(),
			'room_id':len(rooms_response.json()),
			'get_ip': ip_response.json()
		}
	else:
		context = {
			'get_all_rooms': rooms_response.json(),
			'room_id':len(rooms_response.json()),
			'get_ip': []
		}
	return render(request, 'rooms.html',context)
def get_room(request,room_id):
	# url = f"http://127.0.0.1:5000/room/{room_id}"
	url = f"http://10.42.0.1:5000/room/{room_id}"
	response = requests.get(url)
	res = response.json()
	climate_ips={}
	climate_check=['Exhaust','Humidity','CO2']
	climate_schedule_ips=[]
	climate_schedule_check=['Light','Water']
	for ip in res['ip']:
		if ip['name'] in climate_check:
			climate_ips[ip['name']]=ip
		if ip['name'] in climate_schedule_check:
			climate_schedule_ips.append(ip)

	context = {
		'get_room': response.json(),
		'valid_climate_ips': climate_ips,
		'valid_climate_schedule_ips': climate_schedule_ips
	}
	return render(request, 'room.html',context)
def put_room(request):
	if request.method == 'POST':
		# url = f'http://127.0.0.1:5000/rooms'
		url = f'http://10.42.0.1:5000/rooms'
		response = requests.get(url)
		if response.status_code==200:
			room = response.json()
			print(room[-1]['id'])
			room_id=room[-1]['id']+1
		else:
			room_id=1
		# url = f'http://127.0.0.1:5000/room/{room_id}'
		url = f'http://10.42.0.1:5000/room/{room_id}'
		name = request.POST['name']
		payload={'name': name}
		response = requests.put(url, data=payload)
		print(response.json())
		context = {
			'put_room': response.json()
		}
		return redirect('/rooms', context)

def patch_room(request,room_id):
	if request.method == 'POST':
		# url = f'http://127.0.0.1:5000/room/{room_id}'
		url = f'http://10.42.0.1:5000/room/{room_id}'
		name = request.POST['name']
		payload={'name': name}
		response = requests.patch(url, data=payload)
		print(response.json())
		context = {
			'patch_room': response.json()
		}
		return redirect('/rooms', context)

def delete_room(request,room_id):
	# url = f"http://127.0.0.1:5000/room/{room_id}"
	url = f"http://10.42.0.1:5000/room/{room_id}"
	response = requests.delete(url)
	print(response.status_code)
	return redirect('/rooms')

def delete_ip(request,room_id,ip_id):
	# url = f'http://127.0.0.1:5000/room/{room_id}/ip/{ip_id}'
	url = f'http://10.42.0.1:5000/room/{room_id}/ip/{ip_id}'
	response = requests.delete(url)
	print(response.status_code)
	return redirect('/rooms')



def put_ip(request, ip_id):
	if request.method == 'POST':
		room_id=request.POST['room_id']
		name='unassigned'
		ip=request.POST['ip']
		# url = f'http://127.0.0.1:5000/room/{room_id}/ip/{ip_id}'
		url = f'http://10.42.0.1:5000/room/{room_id}/ip/{ip_id}'
		payload={'IP':ip, 'name': name, 'room_id': room_id}
		response = requests.patch(url, data=payload)
		print(response.json())
		context = {
			'put_room': response.json()
		}
		return redirect('/rooms', context)

def get_schedule(request, room_id):
	# url = f"http://127.0.0.1:5000/room/{room_id}/relayschedule"
	url = f"http://10.42.0.1:5000/room/{room_id}/relayschedule"
	response = requests.get(url)
	# url = f"http://127.0.0.1:5000/room/{room_id}/ips"
	url = f"http://10.42.0.1:5000/room/{room_id}/ips"
	ip_response = requests.get(url)
	context = {
		'get_schedule': response.json(),
		'get_ips': ip_response.json()
	}
	return render(request, 'schedule.html',context)
def put_schedule(request, room_id):
	if request.method == 'POST':
		# url = f'http://127.0.0.1:5000/relayschedule'
		url = f'http://10.42.0.1:5000/relayschedule'
		response = requests.get(url)
		relayschedule = response.json()
		if relayschedule:
			print(relayschedule[-1]['climate_schedule_id'])
			relayschedule_id=relayschedule[-1]['climate_schedule_id']+1
		else:
			relayschedule_id=1
		# url = f'http://127.0.0.1:5000/room/{room_id}/relayschedule/{relayschedule_id}'
		url = f'http://10.42.0.1:5000/room/{room_id}/relayschedule/{relayschedule_id}'
		ip_data = request.POST['ip'].split('|')
		ip_id = ip_data[0]
		name = ip_data[1]
		start = request.POST['start_time']
		end = request.POST['end_time']
		how_often = request.POST['how_often']
		payload={'name': name,'start_time': start.replace('T', ' '), 'end_time': end.replace('T', ' '), 'how_often': how_often, 'ip_id':ip_id}
		response = requests.put(url, data=payload)
		print(response.json())
		return redirect(f'/rooms/get_room/{room_id}')
def patch_schedule(request, room_id, climate_schedule_id):
	if request.method == 'POST':
		# url = f"http://127.0.0.1:5000/room/{room_id}/relayschedule/{climate_schedule_id}"
		url = f"http://10.42.0.1:5000/room/{room_id}/relayschedule/{climate_schedule_id}"
		# name = request.POST['name']
		start = request.POST['start_time']
		end = request.POST['end_time']
		how_often = request.POST['how_often']
		ip_id=1
		payload={'start_time': start.replace('T', ' '), 'end_time': end.replace('T', ' '), 'how_often': how_often, 'ip_id':ip_id}
		response = requests.patch(url, data=payload)
		print(response.status_code)
		# context = {
		# 	'put_schedule': response.text
		# }
		return redirect(f'/rooms/get_room/{room_id}')

def delete_schedule(request,room_id, climate_schedule_id):
	if request.method == 'POST':
		# url = f"http://127.0.0.1:5000/room/{room_id}/relayschedule/{climate_schedule_id}"
		url = f"http://10.42.0.1:5000/room/{room_id}/relayschedule/{climate_schedule_id}"
		response = requests.delete(url)
		print(response.text)
		context = {
			'delete_schedule': response.text
		}
		return redirect(f'/rooms/get_room/{room_id}', context)

def get_climate(request, room_id):
	# url = f"http://127.0.0.1:5000/room/{room_id}/climate"
	url = f"http://10.42.0.1:5000/room/{room_id}/climate"
	response = requests.get(url)
	# url = f"http://127.0.0.1:5000/room/{room_id}/ips"
	url = f"http://10.42.0.1:5000/room/{room_id}/ips"
	ip_response = requests.get(url)
	context = {
		'get_climate': response.json(),
		'get_ips': ip_response.json()
	}
	return render(request, 'climate.html',context)
def put_climate(request, room_id):
	if request.method == 'POST':
		# url = f'http://127.0.0.1:5000/room/{room_id}/climate'
		url = f'http://10.42.0.1:5000/room/{room_id}/climate'
		response = requests.get(url)
		climate = response.json()
		if climate:
			print(climate[-1]['climate_id'])
			climate_id=climate[-1]['climate_id']+1
		else:
			climate_id=1
		# url = f'http://127.0.0.1:5000/room/{room_id}/climate/{climate_id}'
		url = f'http://10.42.0.1:5000/room/{room_id}/climate/{climate_id}'
		payload = {
			'name':request.POST['name'],
			'co2_parameters':request.POST['co2_parameters'],
			'humidity_parameters':request.POST['humidity_parameters'],
			'temperature_parameters':request.POST['temperature_parameters'],
			'co2_relay_ip':request.POST['co2_ip'],
			'humidity_relay_ip':request.POST['humidity_ip'],
			'exhaust_relay_ip':request.POST['exhaust_ip'],
		}
		response = requests.put(url, data=payload)
		print(response.json())
		return redirect(f'/rooms/get_room/{room_id}')
def patch_climate(request, room_id, climate_id):
	if request.method == 'POST':
		# url = f"http://127.0.0.1:5000/room/{room_id}/climate/{climate_id}"
		url = f"http://10.42.0.1:5000/room/{room_id}/climate/{climate_id}"
		payload = {
			'name':request.POST['name'],
			'co2_parameters':request.POST['co2_parameters'],
			'humidity_parameters':request.POST['humidity_parameters'],
			'temperature_parameters':request.POST['temperature_parameters'],
			'co2_relay_ip':request.POST['co2_ip'],
			'humidity_relay_ip':request.POST['humidity_ip'],
			'exhaust_relay_ip':request.POST['exhaust_ip'],
		}
		response = requests.patch(url, data=payload)
		print(response.status_code)
		return redirect(f'/rooms/get_room/{room_id}')

def delete_climate(request,room_id, climate_id):
	if request.method == 'POST':
		# url = f"http://127.0.0.1:5000/room/{room_id}/climate/{climate_id}"
		url = f"http://10.42.0.1:5000/room/{room_id}/climate/{climate_id}"
		response = requests.delete(url)
		print(response.text)
		context = {
			'delete_schedule': response.text
		}
		return redirect(f'/rooms/get_room/{room_id}', context)

def relay_control(request, room_id):
	if request.method == 'POST':
		# url = f"http://127.0.0.1:5000//relay_control"
		url = f"http://10.42.0.1:5000/room/{room_id}/climate"
		payload={'ip': request.POST['ip'],'state': request.POST['state']}
		response = requests.get(url,params=payload)
		print(response.status_code)
	return redirect(f'/rooms/get_room/{room_id}')