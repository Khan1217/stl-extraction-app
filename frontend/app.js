const input_btn = document.getElementById("input-btn")
input_btn.addEventListener("change",inputHandler)
const surface_area = document.getElementById("surface-area");
const results_block = document.getElementById("results-block");
const volume = document.getElementById("volume");
const length = document.getElementById("length");
const width = document.getElementById("width");
const height = document.getElementById("height");
const length_cylinder = document.getElementById("length-cylinder");
const diameter_cylinder = document.getElementById("diameter-cylinder");


const backend_url = "http://127.0.0.1:5000/stl_file"

async function inputHandler(event){
    const file = event.target.files[0];
    const response = await fetch(backend_url, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/octet-stream'
        },
        body: file
      })
    const data = await response.json()
    surface_area.innerHTML = data.surface_area.toFixed(2)
    volume.innerHTML = data.volume.toFixed(2)
    length.innerHTML = data.length.toFixed(2)
    width.innerHTML = data.width.toFixed(2)
    height.innerHTML = data.height.toFixed(2)
    length_cylinder.innerHTML = data.length_of_cylinder.toFixed(2)
    diameter_cylinder.innerHTML = data.diameter_of_cylinder.toFixed(2);
    results_block.style.display = "block"
}

