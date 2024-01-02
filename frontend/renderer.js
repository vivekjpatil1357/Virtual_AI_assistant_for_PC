window.pixel.user((event,data)=>{
  var newp=document.createElement('p')
  newp.innerHTML=data['user']
  newp.align='left'
  document.getElementById("already").appendChild(newp)

})
window.pixel.pixel((event,data)=>{
  var newp=document.createElement('p')
  newp.innerHTML=data['pixel']
  newp.align='right'
  document.getElementById("already").appendChild(newp)
})

window.pixel.voiceReceive((event,data)=>{
  document.getElementById("voice").innerHTML=data
})

window.chat.receivePixelResponse((e,data)=>{
  console.log("hllo")
  var messageList = document.getElementById('message-list');
  var newMessage = document.createElement('div');
  newMessage.className='bot'
  newMessage.innerHTML = '<strong>' + 'Pixel' + ':</strong><p> ' + data['pixel'] + '</p>'
  messageList.appendChild(newMessage)
  scrollToBottom()

  // '<strong>' + 'Pixel'+ ':</strong><p> ' + data['pixel'] + '</p>';
})
