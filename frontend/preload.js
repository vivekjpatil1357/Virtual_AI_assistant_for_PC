const { contextBridge, ipcRenderer } = require('electron')

contextBridge.exposeInMainWorld('pixel', {
    start: () => ipcRenderer.send('start'),
    voiceSend: () => ipcRenderer.send('voice'),
    voiceReceive: (callback) => ipcRenderer.on('voice', callback),
    user: (callback) => ipcRenderer.on('user', callback),
    pixel: (callback) => ipcRenderer.on('pixel', callback)
})
contextBridge.exposeInMainWorld('choice', {
    sendVoiceChoice: () => ipcRenderer.send('choiceVoice'),
    sendChatChoice: () => ipcRenderer.send('choiceChat'),
    sendRolePlayChoice: () => ipcRenderer.send('choiceRolePlay'),
})
contextBridge.exposeInMainWorld('chat', {
   sendUserChat:(data)=>ipcRenderer.send('userChat',data),
   receivePixelResponse:(callback)=>ipcRenderer.on('response',callback),
})
