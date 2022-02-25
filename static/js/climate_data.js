let url = `ws://${window.location.host}/ws/socket-server/`

const climateSocket = new WebSocket(url)

climateSocket.onmessage = function (e) {
  let data = JSON.parse(e.data)
  console.log('Data:', data)

  if (data.type === 'room') {
    let messages = document.getElementById('climate-data-' + data.room_id)

    messages.innerText = `CO2: ${data.message.co2} Humidity: ${data.message.humidity} Temperature: ${data.message.temperature}`

  }
}
