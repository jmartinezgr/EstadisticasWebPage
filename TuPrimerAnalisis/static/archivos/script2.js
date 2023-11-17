// script2.js
document.addEventListener('DOMContentLoaded', function() {
    const dragArea = document.querySelector('.drag_area');
    const hiddenFileInput = document.getElementById('hidden_file_input');
    const header = document.querySelector('.drop_header');
    const textArea = document.querySelector('.textarea');

    dragArea.addEventListener('dragover', (event) => {
        event.preventDefault();
        dragArea.classList.add('active');
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
                textArea.placeholder='Ingresa qué columna o columnas quieres usar, sepáralas por comas y numéralas desde 0';
            } else {
                alert("Archiv No Valido");
            }
        }
    });

    // Función para mostrar el nombre del archivo seleccionado
    function displayFileName(input) {
        const fileNameDisplay = document.getElementById('file-name-display');
        fileNameDisplay.textContent = input.files[0].name;
    }
});