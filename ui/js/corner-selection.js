let rawVideo;
let cornerCanvas;
let videoStream;
let nextCorner;
let nextCornerBox;

const cornerIDs = [
    'Top Left',
    'Top Right',
    'Bottom Right',
    'Bottom Left'
]

let corners = []
let cornerIndex = 0

function StartCornerSelection(deviceId) {
    
    rawVideo = document.getElementById('raw-source')
    nextCorner = document.getElementById('next-corner-id')
    nextCornerBox = document.getElementById('next-corner')
    cornerCanvas = document.getElementById('corner-canvas')

    navigator.mediaDevices.getUserMedia({
        video: {
            deviceId: deviceId,
            width: 1920,
            height: 1080
        }
    })
    .then(stream => {
        videoStream = stream
        rawVideo.srcObject = stream
        rawVideo.play()

        document.getElementById('header').classList.remove('hide')
        document.getElementById('initial').classList.add('hide')
        document.getElementById('select-scoreboard').classList.remove('hide')

        setTimeout(() => {
            cornerCanvas.onclick = ClickedCorner
            const bounding = rawVideo.getBoundingClientRect()
            console.log(bounding)
            cornerCanvas.width = bounding.width
            cornerCanvas.height = bounding.height
        }, 100)

    })

}

function ResetCorners() {
    cornerIndex = 0
    corners = []
    lastCorner = undefined
    nextCorner.innerText = cornerIDs[cornerIndex]
    nextCornerBox.classList.remove('hide')
    document.querySelector('#corners-continue-btn').disabled = true;

    let context = cornerCanvas.getContext('2d')
    context.clearRect(0, 0, cornerCanvas.width, cornerCanvas.height)
}

let lastCorner;
let firstCorner;

function ClickedCorner(e) {
    if (cornerIndex < 4) {
        let bounds = rawVideo.getBoundingClientRect()
        const width = bounds.right - bounds.left
        const height = bounds.bottom - bounds.top

        let x = e.clientX - bounds.left
        let y = e.clientY - bounds.top

        if (lastCorner != undefined) {
            DrawCornersLine(x, y)
        }
        else {
            firstCorner = {x: x, y: y}
        }
        lastCorner = {x: x, y: y}

        x = (x / width) * rawVideo.videoWidth
        y = (y / height) * rawVideo.videoHeight

        console.log(`(${x}, ${y})`)

        cornerIndex = cornerIndex + 1
        if (cornerIndex == 4) {
            corners.push([x, y])
            document.querySelector('#corners-continue-btn').disabled = false;
            nextCornerBox.classList.add('hide')
            DrawCornersLine(firstCorner.x, firstCorner.y)
        }
        else {
            corners.push([x, y])
            nextCorner.innerText = cornerIDs[cornerIndex]
        }
    }
}

function DrawCornersLine(x, y) {
    let context = cornerCanvas.getContext('2d')

    context.lineWidth = 5
    context.lineCap = 'square'

    context.beginPath()
    context.moveTo(lastCorner.x, lastCorner.y)
    context.lineTo(x, y)

    context.strokeStyle = '#2962ff'
    context.stroke()
}

function CornersContinue(btn) {
    btn.disabled = true
    payload = {
        corner_pin: corners,
        width: rawVideo.videoWidth,
        height: rawVideo.videoHeight
    }
    fetch(`${flask}/cornerpin`, {
        method: 'POST',
        cache: 'no-cache',
        body: JSON.stringify(payload)
    }).then(res => {
        res.json().then(data => {
            startFrameProcessor(data)
        })
    })
}