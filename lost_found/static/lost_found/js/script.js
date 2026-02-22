function updateFileName(input) {
    const fileNameDisplay = document.getElementById('file-name');
    const previewContainer = document.getElementById('image-preview'); // Dagdagan mo ng div sa HTML
    
    if (input.files && input.files[0]) {
        const reader = new FileReader();
        
        reader.onload = function(e) {
            // Pinapakita yung picture bago i-submit
            previewContainer.innerHTML = `<img src="${e.target.result}" style="max-height: 150px; border-radius: 8px; margin-top: 10px;">`;
        }
        
        reader.readAsDataURL(input.files[0]);
        fileNameDisplay.innerText = "File Selected: " + input.files[0].name;
    }
}
