const rawCanvas = document.getElementById('raw-canvas')
const distortedVideo = document.getElementById('distorted-source')

let frameInterval

function startFrameProcessor(dimensions) {

    distortedVideo.width = dimensions.x
    distortedVideo.height = dimensions.y
    // distortedVideo.onload = () => {URL.revokeObjectURL(this.src)}
    document.getElementById('select-scoreboard').classList.add('hide')
    document.getElementById('select-fields').classList.remove('hide')

    rawCanvas.width = rawVideo.videoWidth
    rawCanvas.height = rawVideo.videoHeight

    ProcessFrame()

}

function ProcessFrame() {
    rawCanvas.getContext('2d').drawImage(rawVideo, 0, 0, rawCanvas.width, rawCanvas.height)
    rawCanvas.toBlob(blob => {
        blob.arrayBuffer().then(arraybuffer => {
            fetch(`${flask}/frame`, {
                method: 'POST',
                cache: 'no-cache',
                body: arraybuffer
            }).then(res => {
                res.blob().then(img => {
                    distortedVideo.src = URL.createObjectURL(img)
                    // setTimeout(ProcessFrame, 55)
                    ProcessFrame()
                })
            })
        })
    })

    
}