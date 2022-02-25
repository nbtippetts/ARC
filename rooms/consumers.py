import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class ClimateConsumer(WebsocketConsumer):
	def connect(self):
		self.room_group_name = 'climate_data'
		async_to_sync(self.channel_layer.group_add)(
			self.room_group_name,
			self.channel_name
		)

		self.accept()


	def receive(self, text_data):
		text_data_json = json.loads(text_data)
		message = text_data_json['data']
		room_id = text_data_json['room_id']

		async_to_sync(self.channel_layer.group_send)(
			self.room_group_name,
			{
				'type':'chat_message',
				'message':message,
				'room_id': room_id
			}
		)

	def chat_message(self, event):
		message = event['message']
		room_id = event['room_id']

		self.send(text_data=json.dumps({
			'type':'room',
			'room_id':room_id,
			'message':message
		}))