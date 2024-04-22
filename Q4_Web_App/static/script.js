document.addEventListener('DOMContentLoaded', function() {
    const canvas = document.getElementById('canvas');
    const video = document.getElementById('video');
    const ctx = canvas.getContext('2d');
    let drawing = false;
    let xStart, yStart;

    canvas.width = video.clientWidth;
    canvas.height = video.clientHeight;

    video.addEventListener('mousedown', function(e) {
        drawing = true;
        xStart = e.offsetX;
        yStart = e.offsetY;
    });

    video.addEventListener('mousemove', function(e) {
        if (!drawing) return;
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        ctx.beginPath();
        ctx.rect(xStart, yStart, e.offsetX - xStart, e.offsetY - yStart);
        ctx.strokeStyle = 'green';
        ctx.stroke();
    });

    video.addEventListener('mouseup', function(e) {
        drawing = false;
        fetch('/calculate_dimensions', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                xStart: xStart,
                yStart: yStart,
                xEnd: e.offsetX,
                yEnd: e.offsetY
            })
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('dimensions').innerText = `Width: ${data.width.toFixed(2)} mm, Height: ${data.height.toFixed(2)} mm`;
        });
    });
});
