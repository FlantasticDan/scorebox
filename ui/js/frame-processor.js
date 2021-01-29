const io = require('socket.io-client')

const rawCanvas = document.getElementById('raw-canvas')
const distortedVideo = document.getElementById('distorted-source')

let frameInterval
let socket

function startFrameProcessor(dimensions) {

    distortedVideo.width = dimensions.x
    distortedVideo.height = dimensions.y
    // distortedVideo.onload = () => {URL.revokeObjectURL(this.src)}
    document.getElementById('select-scoreboard').classList.add('hide')
    document.getElementById('select-fields').classList.remove('hide')

    rawCanvas.width = rawVideo.videoWidth
    rawCanvas.height = rawVideo.videoHeight

    socket = io(flask)
    console.log(socket)

    socket.on('connect', () => {
        ProcessFrame()
    })

    socket.on('undistort', data => {
        console.log('new frame')
        distortedVideo.src = data
        ProcessFrame()
    })



    // ProcessFrame()

}

function ProcessFrame() {
    rawCanvas.getContext('2d').drawImage(rawVideo, 0, 0, rawCanvas.width, rawCanvas.height)
    rawCanvas.toBlob(blob => {
        blob.arrayBuffer().then(arraybuffer => {
            console.log('sending frame')
            socket.emit('frame', arraybuffer)
            console.log('sent frame')
            // ProcessFrame()
        })
    })

    
}