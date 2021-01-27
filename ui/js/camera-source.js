navigator.mediaDevices.enumerateDevices()
    .then(devices => {
        let cameraSourceButtons = ''
        devices.forEach(device => {
            if (device.kind == 'videoinput') {
                cameraSourceButtons = `
                ${cameraSourceButtons}
                <button class='ui-text btn camera-source-btn' onclick='SelectCamera(this)' data-deviceid='${device.deviceId}'>
                    ${device.label}
                </button>
                `
            }
        })
        document.getElementById('camera-sources').innerHTML = cameraSourceButtons
    })

function SelectCamera(btn) {
    StartCornerSelection(btn.dataset.deviceid)
}