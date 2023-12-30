window.jarvis.user((event,data)=>{
  var newp=document.createElement('p')
  newp.innerHTML=data['user']
  newp.align='left'
  document.getElementById("already").appendChild(newp)

})
window.jarvis.jarvis((event,data)=>{
  var newp=document.createElement('p')
  newp.innerHTML=data['jarvis']
  newp.align='right'
  document.getElementById("already").appendChild(newp)
})

window.jarvis.voiceReceive((event,data)=>{
  document.getElementById("voice").innerHTML=data
})

