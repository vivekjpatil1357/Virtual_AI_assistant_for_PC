const { app, BrowserWindow, Menu, ipcMain } = require('electron')
const path = require('path')

function createHomeWindow() {
  mainWindow = new BrowserWindow({
    width: 1150,
    height: 665,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js')
    },
    autoHideMenuBar: true,
  })
  mainWindow.loadFile('index.html')
}
function createChoiceWindow() {
  choiceWindow = new BrowserWindow({
    width: 1150,
    height: 665,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js')
    },
    autoHideMenuBar: true
  })
  choiceWindow.loadFile('choice.html')
}
function createVoiceWindow() {
  voiceWindow = new BrowserWindow({
    width: 1150,
    height: 665,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js')
    },
    // alwaysOnTop: true,
    autoHideMenuBar: true
  })
  voiceWindow.loadFile('voice.html')
}
function createChatWindow() {
  chatWindow = new BrowserWindow({
    width: 445,
    height: 740,
    x: 1050,
    y: 5,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js')
    },
    autoHideMenuBar: true,
    // resizable: false
    alwaysOnTop: true
  })

  chatWindow.loadFile('chat.html')
}
function createRolePlayWindow() {
  rolePlayWindow = new BrowserWindow({
    width: 445,
    height: 710,
    x: 1050,
    y: 5,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js')
    },
    autoHideMenuBar: true,
    // resizable: false
    alwaysOnTop: false
  })

  rolePlayWindow.loadFile('roleplay.html')
}
function createInputRolePlayWindow() {
  inputRolePlayWindow = new BrowserWindow({
    width: 445,
    height: 470,
    x: 1050,
    y: 5,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js')
    },
    autoHideMenuBar: true,
  })
  createRolePlayWindow()
  inputRolePlayWindow.loadFile('input_role.html')
  inputRolePlayWindow.focus()
}

// ###################################################################################################
// Windows ^ above
// ###################################################################################################

async function requestSay(data, tosend) {           //pass text, will speak and call fetchVoiceData
  console.log("going to say :" + data)
  if (tosend) {
    voiceWindow.webContents.send('pixel', {
      'pixel': data
    })
  }
  var dataToSend = { 'text': data, }
  await fetch('http://127.0.0.1:1000/say', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(dataToSend),
  }).then((r) => r.json())
    .then((data) => {
      // console.log(data['h'])
      fetchVoiceData()
    }).catch(error => {
      console.log(error);
    });
}
async function fetchResponse(data, isvoice) {  //pass query and bool for if it is for voice or chat, will search in AI for result
  console.log("fetch response called")
  var dataToSend = { 'query': data, }
  await fetch('http://127.0.0.1:1000/ai', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(dataToSend),
  }).then((r) => r.json())
    .then((data) => {
      console.log(data['response'])
      if (isvoice) {
        voiceWindow.webContents.send('pixel', {
          'pixel': data['response']
        })
        requestSay(data['response'], false)
      }
      else {

        console.log("sending to Frontend")
        // console.log(data['response'].indexOf("the report of "))

        // else {
        chatWindow.webContents.send('response', {
          'pixel': data['response'],

        })
        // }
      }
    }).catch(error => {
      console.log(error);
    });
}
async function fetchVoiceData() {   //will cause to call mainLogic for voice module
  console.log("fetching new data")
  var res = await fetch('http://127.0.0.1:1000/start/voice'
  ).then(res => res.json())
    .then((data) => {
      voiceWindow.webContents.send('user', {
        'user': data['query']
      })
      console.log(data['isExit'])
      if (data['isExit'] == "No") {
        console.log(data['query'])
        callTofetchResponse = async () => await fetchResponse(data['query'], true)
        callTorequestSay = async () => await requestSay(data['response'], true)
        if (data['isAi'] == 'yes')
          callTofetchResponse()
        else
          callTorequestSay()
        console.log("fetchecd")
      }
    }).catch(error => {
      console.error('Fetch error:', error.message);
   });
}
async function fetchChatData(text) { //will cause to call mainLogic for chat module
  console.log("fetching chat new data")
  dataToSend = { 'text': text };
  var res = await fetch('http://127.0.0.1:1000/start/chat',
    {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(dataToSend),
    }).then(res => res.json())
    .then((data) => {

      console.log(data['response'])

      callTofetchResponse = async () => await fetchResponse(data['query'], false)
      callTorequestSay = async () => await requestSay(data['response'])
      if (data['isAi'] == 'yes')
        callTofetchResponse()
      else {
        console.log("sending to Frontend")
        if (data['response'].indexOf("the report of ") == 0) {
          chatWindow.webContents.send('response', {
            'pixel': data['response'],
            'isNews': 'yes',
            'imageUrl': data['imageUrl']
          })
        }
        else {
          chatWindow.webContents.send('response', {
            'pixel': data['response'],
            'isNews': 'no',
          })
        }
      }

      // callTorequestSay()
      console.log("fetchecd")
      // }
    }).catch(error => {
      console.error('Fetch error:', error.message);
    });
}
// ###################################################################################################
// Fetch Functions ^ above
// ###################################################################################################
ipcMain.on('roleplaySend', (e,data) => {
  dataToSend = data
  
  fetch('http://127.0.0.1:1000/roleplay',{ 
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(dataToSend),
  }).then((r) => r.json())
  .then((data) => {
    rolePlayWindow.webContents.send('roleplayReceive', {
      'response': data['response'],
      'role': data['role']      
    })

  }).catch(error => {
    console.log(error);
  });
})
ipcMain.on('choiceVoice', () => { // in choice when choosed as Voice,will open voice page
  createVoiceWindow()
  choiceWindow.close()
})
ipcMain.on('choiceChat', () => {  // in choice when choosed as Chat will open chat page
  createChatWindow()
  choiceWindow.close()
})
ipcMain.on('stop', () => {
  fetch('http://127.0.0.1:1000/stop')
  .catch((e) => {
    
  })
  const { spawn } = require('child_process');
  console.log("stop processss!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
  
  const pythonProcess = spawn('python', ['C:\\Users\\vivek\\OneDrive\\Desktop\\prj\\backend\\app.py'], {
    shell: false,
    detached: true,
    stdio: 'ignore',
  });
  // voiceWindow.focus();
  
  
  
})
ipcMain.on('choiceRolePlay', () => {    // in choice when choosed as Roleplay, will open Roleplay page
  console.log('role play choosed')
  createInputRolePlayWindow()
  choiceWindow.close()
})
ipcMain.on('sendRole', (e, data) => {  
  inputRolePlayWindow.close()
  console.log(data)
  rolePlayWindow.webContents.send('receiveRole', {
    'role': data['role'],
    'desc':data['desc']
  })
})
ipcMain.on('start', () => {       // when clicked on start on first page, it will redirect to second page
  console.log('from main start')
  createChoiceWindow();
  mainWindow.close();
  
})
ipcMain.on('voice', async (e) => {  //after choosing voice in choice , when "start voice chat" button clicked it will open Mic
  await fetchVoiceData()
})
ipcMain.on('userChat', async (e, data) => {      //after choosing chat in choice ,  it will open ChatBox
  await fetchChatData(data);
})
ipcMain.on('backFromChat', () => {
  console.log("back from chat")
  createChoiceWindow()
  chatWindow.close()
})
ipcMain.on('backFromVoice', () => {
  console.log("back from voice")
  createChoiceWindow()
  voiceWindow.close()
})
ipcMain.on('backFromChoice', () => {
  console.log("back from Choice")
  createHomeWindow()
  choiceWindow.close()
})
app.whenReady().then(() => {
  createHomeWindow()
  app.on('activate', function () {
    if (BrowserWindow.getAllWindows().length === 0) createHomeWindow()
  })
})
app.on('window-all-closed', function () {
  if (process.platform !== 'darwin') app.quit()
})
// ###################################################################################################
// ON commands (Event Handling) ^ above
// ###################################################################################################