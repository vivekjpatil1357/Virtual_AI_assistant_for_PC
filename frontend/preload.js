const { contextBridge, ipcRenderer } = require('electron')

contextBridge.exposeInMainWorld('pixel', {
    start: () => ipcRenderer.send('start'),
    stop: () => ipcRenderer.send('stop'),
    voiceSend: () => ipcRenderer.send('voice'),
    voiceReceive: (callback) => ipcRenderer.on('voice', callback),
    user: (callback) => ipcRenderer.on('user', callback),
    pixel: (callback) => ipcRenderer.on('pixel', callback),
    backFromVoice:()=>ipcRenderer.send('backFromVoice')
})
contextBridge.exposeInMainWorld('choice', {
    sendVoiceChoice: () => ipcRenderer.send('choiceVoice'),
    sendChatChoice: () => ipcRenderer.send('choiceChat'),
    sendRolePlayChoice: () => ipcRenderer.send('choiceRolePlay'),
    backFromChoice:()=>ipcRenderer.send('backFromChoice')
})
contextBridge.exposeInMainWorld('chat', {
    sendUserChat: (data) => ipcRenderer.send('userChat', data),
    receivePixelResponse: (callback) => ipcRenderer.on('response', callback),
    backFromChat:()=>ipcRenderer.send('backFromChat')
})
contextBridge.exposeInMainWorld('roleplay', {
    sendRole: (data) => ipcRenderer.send('sendRole', data),
    receiveRole:(callback)=>ipcRenderer.on('receiveRole',callback),
    roleplaySend:(data)=>ipcRenderer.send('roleplaySend',data),
    roleplayReceive:(callback)=>ipcRenderer.on('roleplayReceive',callback)
})