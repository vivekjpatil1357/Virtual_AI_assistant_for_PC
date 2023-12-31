const { contextBridge, ipcRenderer } = require('electron')

contextBridge.exposeInMainWorld('jarvis', {
    start: () => ipcRenderer.send('start'),
    voiceSend: () => ipcRenderer.send('voice'),
    voiceReceive: (callback) => ipcRenderer.on('voice', callback),
    user: (callback) => ipcRenderer.on('user', callback),
    jarvis: (callback) => ipcRenderer.on('jarvis', callback)
})
contextBridge.exposeInMainWorld('choice', {
    sendVoiceChoice: () => ipcRenderer.send('choiceVoice'),
    sendChatChoice: () => ipcRenderer.send('choiceChat'),
    sendRolePlayChoice: () => ipcRenderer.send('choiceRolePlay'),
})
