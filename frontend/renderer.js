window.pixel.user((event, data) => {
  var newp = document.createElement('p')
  newp.innerHTML = data['user']
  newp.align = 'left'
  document.getElementById("already").appendChild(newp)
})
window.pixel.pixel((event, data) => {
  var newp = document.createElement('p')
  newp.innerHTML = data['pixel']
  newp.align = 'right'
  document.getElementById("already").appendChild(newp)
})

window.pixel.voiceReceive((event, data) => {
  document.getElementById("voice").innerHTML = data
})
window.roleplay.receiveRole((e, data) => {
  role = document.getElementById('head').innerHTML
  console.log(data['role']);
  document.getElementById('head').innerHTML = role + data['role']
  role = data['role']
  desc=data['desc']

})
window.roleplay.roleplayReceive((e, data) => {
  console.log("hllo from roleplay")
  var messageList = document.getElementById('message-list');
  var newMessage = document.createElement('div');
  newMessage.className = 'bot'
  newMessage.innerHTML = '<strong>' + data['role'] + ':</strong><p> ' + data['response'] + '</p>'
  messageList.appendChild(newMessage)
  
  scrollToBottom()
})
window.chat.receivePixelResponse((e, data) => {
  console.log("hllo ")
  var messageList = document.getElementById('message-list');
  var newMessage = document.createElement('div');
  newMessage.className = 'bot'
  newMessage.innerHTML = '<strong>' + 'Pixel' + ':</strong><p> ' + data['pixel'] + '</p>'
  messageList.appendChild(newMessage)
  if (data['isNews'] == 'yes') {
    newMessage = document.createElement('img')
    newMessage.src =data['imageUrl']
    console.log(data['imageUrl'])
      newMessage.className = 'bot'
    messageList.appendChild(newMessage)
  }
  scrollToBottom()
})