const emailIn = document.querySelector("#email")
const senhaIn = document.querySelector("#senha")
const entrarButton = document.querySelector("#btnEntrar")
const form = querySelector("#form")


entrarButton.addEventListener("click", (e) => {

    e.preventDefault
    if (emailIn.value == "") {
        alert("Insira um email!")
        
    }

    if (senhaIn.value == "") {
        alert("Insira uma senha!")
        
    }

    form.submit()

})