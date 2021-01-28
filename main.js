const { app, BrowserWindow } = require('electron')
const path = require('path')

function createWindow () {
  const win = new BrowserWindow({
    width: 1800,
    height: 920,
    webPreferences: {
      nodeIntegration: true
    }
  })

  win.removeMenu()
  win.setTitle('ScoreBox')
  win.setResizable(false)
  win.loadFile('index.html')
  win.webContents.openDevTools()
}

app.whenReady().then(createWindow)

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit()
  }
})

app.on('activate', () => {
  if (BrowserWindow.getAllWindows().length === 0) {
    createWindow()
  }
})

let pythonCore = null;
const launchPython = () => {
  let python = path.join(__dirname, 'venv', 'Scripts', 'python.exe')
  let script = path.join(__dirname, 'core', 'main.py')
  console.log(script)
  pythonCore = require('child_process').spawn(python, [script])
}

const killPython = () => {
  pythonCore.kill()
  pythonCore = null
}

app.on('ready', launchPython)
app.on('will-quit', killPython)