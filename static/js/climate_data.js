let url = `ws://${window.location.host}/ws/socket-server/`

const climateSocket = new WebSocket(url)

climateSocket.onmessage = function (e) {
	let data = JSON.parse(e.data)
	console.log('Data:', data)

	if (data.type === 'room') {
		try {
			let co2 = document.getElementById('CO2-' + data.room_id)
			co2.innerText = `CO2: ${data.message.co2}`
		} catch (e) { }
		try {
			let humidity = document.getElementById('Humidity-' + data.room_id)
			humidity.innerText = `Humidity: ${data.message.humidity}%`
		} catch (e) { }
		try {
			let temperature = document.getElementById('Exhaust-' + data.room_id)
			temperature.innerText = `Temperature: ${data.message.temperature}\u2109`
		} catch (e) { }
	}
}
