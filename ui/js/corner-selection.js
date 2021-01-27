let rawVideo;
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

        rawVideo.onclick = ClickedCorner

        document.getElementById('header').classList.remove('hide')
        document.getElementById('initial').classList.add('hide')
        document.getElementById('select-scoreboard').classList.remove('hide')
    })

}

function ResetCorners() {
    cornerIndex = 0
    corners = []
    nextCorner.innerText = cornerIDs[cornerIndex]
    nextCornerBox.classList.remove('hide')
    document.querySelector('#corners-continue-btn').disabled = true;
}

function ClickedCorner(e) {
    if (cornerIndex < 4) {
        let bounds = e.target.getBoundingClientRect()
        const width = bounds.right - bounds.left
        const height = bounds.bottom - bounds.top

        let x = e.clientX - bounds.left
        let y = e.clientY - bounds.top

        x = (x / width) * e.target.videoWidth
        y = (y / height) * e.target.videoHeight

        console.log(`(${x}, ${y})`)

        cornerIndex = cornerIndex + 1
        if (cornerIndex == 4) {
            corners.push([x, y])
            document.querySelector('#corners-continue-btn').disabled = false;
            nextCornerBox.classList.add('hide')
        }
        else {
            corners.push([x, y])
            nextCorner.innerText = cornerIDs[cornerIndex]
        }
    }
    

}

