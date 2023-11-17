// script2.js
const dragArea = document.querySelector('.drag_area');
const hiddenFileInput = document.getElementById('hidden_file_input');
const deleteFileBtn = document.getElementById('delete-file-btn');
const header = document.querySelector('.drop_header')

dragArea.addEventListener('dragover', (event) => {
    event.preventDefault();
    dragArea.classList.add('active');
});

dragArea.addEventListener('dragleave', () => {
    dragArea.classList.remove('active');
    header.textContent = 'Arrastra De nuevo & Cambia tu Archivo' 
});

dragArea.addEventListener('drop', (event) => {
    event.preventDefault();
    dragArea.classList.remove('active');
    
    const files = event.dataTransfer.files;

    if (files.length > 0) {
        const file = files[0];
        const fileType = file.type;

        const validExtensions = ['application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', 'text/csv'];

        if (validExtensions.includes(fileType)) {
            hiddenFileInput.files = files;
            displayFileName(hiddenFileInput);
            deleteFileBtn.style.display = 'inline-block';
        } else {
            alert("XD");
        }
    }
});

deleteFileBtn.addEventListener('click', () => {
    // Restablecer el formulario para eliminar el archivo seleccionado
    document.getElementById('upload-form').reset();
    deleteFileBtn.style.display = 'none';
}); 

// Función para mostrar el nombre del archivo seleccionado
function displayFileName(input) {
    const fileNameDisplay = document.getElementById('file-name-display');
    fileNameDisplay.textContent = input.files[0].name;
}

document.getElementById('submit-btn').addEventListener('click', () => {
    document.getElementById('upload-form').submit();
});

deleteFileBtn.addEventListener('click', () => {
    // Restablecer el formulario para eliminar el archivo seleccionado
    document.getElementById('upload-form').reset();
    deleteFileBtn.style.display = 'none';
});