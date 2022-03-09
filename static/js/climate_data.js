let url = `ws://${window.location.host}/ws/socket-server/`

const climateSocket = new WebSocket(url)

climateSocket.onmessage = function (e) {
  let data = JSON.parse(e.data)
  console.log('Data:', data)

  if (data.type === 'room') {
    let co2 = document.getElementById('CO2-' + data.room_id)
	let humidity = document.getElementById('Humidity-' + data.room_id)
	  let temperature = document.getElementById('Exhaust-' + data.room_id)

	  co2.innerText = `${data.message.co2}`
	  humidity.innerText = `${data.message.humidity}`
	  temperature.innerText = `${data.message.temperature}`

  }
}
