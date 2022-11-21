let body = document.body
let toggle = document.querySelector('.toggle')
let icon = document.querySelector('.fa-moon')
let iconB = document.querySelector('.dark')

toggle.onclick = () => {
    body.classList.toggle('dark')
    if(body.classList.contains('dark')){
        icon.classList.replace('fa-moon' , 'fa-sun');
    }else{
        icon.classList.replace('fa-sun', 'fa-moon')
    }

}

// function checkIcon(){
//     if(body.classList.contains('dark')){
//         icon.classList.add('fa-moon')
//         icon.classList.remove('fa-sun')
//     }else{
//         icon.classList.add('fa-sun')
//         icon.classList.remove('fa-moon')
//     }
// }

// checkIcon()

// toggle.onclick = () => {
//     body.classList.toggle("dark")
//     setTimeout(()=>{
//         checkIcon()
//     },100)    
// }