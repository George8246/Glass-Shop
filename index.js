const video = document.getElementById('video')

Promise.all([
    faceapi.nets.tinyFaceDetector.loadFromUri('/models'),
    faceapi.nets.faceLandmark68Net.loadFromUri('/models'),
    faceapi.nets.faceRecognitionNet.loadFromUri('/models'),
    faceapi.nets.faceExpressionNet.loadFromUri('/models')
]).then(startVideo)

function startVideo() {
    navigator.getUserMedia({
            video: {}
        },
        stream => video.srcObject = stream,
        err => console.error(err)
    )
}

glassImage = new Image();
glassImage.src = 'data/glass5.png';

video.addEventListener('play', () => {
    const canvas = faceapi.createCanvasFromMedia(video)
    document.body.append(canvas)
    const displaySize = {
        width: video.width,
        height: video.height
    }
    faceapi.matchDimensions(canvas, displaySize)
    setInterval(async () => {
        const detections = await faceapi.detectAllFaces(video, new faceapi.TinyFaceDetectorOptions()).withFaceLandmarks()

        let rightEye = detections[0].landmarks.getRightEye()[0];
        let leftEye = detections[0].landmarks.getLeftEye()[0];

        const resizedDetections = faceapi.resizeResults(detections, displaySize)

        // drawRotated(canvas, Math.atan(rightEye.y / rightEye.x));
        // canvas.getContext('2d').clearRect(0, 0, canvas.width, canvas.height);
        // canvas.getContext('2d').drawImage(glassImage, rightEye.x - 50, rightEye.y, rightEye.x - 50 - leftEye.x + 150, 100);
        canvas.getContext('2d').clearRect(0, 0, canvas.width, canvas.height);
        canvas.getContext('2d').save();

        // var degree = Math.atan((leftEye.y - rightEye.y) / (leftEye.x - rightEye.x - 100))// * Math.PI / 180;
        // console.log(degree);

        // canvas.getContext('2d').rotate(degree);
        // canvas.getContext('2d').translate(0, 0);

        var py = Math.sqrt(Math.pow(rightEye.x - leftEye.x + 100, 2) + Math.pow(rightEye.y - leftEye.y, 2));
        canvas.getContext('2d').drawImage(glassImage, rightEye.x - 50, rightEye.y, py, 100);

        canvas.getContext('2d').restore();


    }, 100)
})