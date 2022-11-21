let change = document.querySelector('.show')
let cyber = document.querySelector('.grab')

change.addEventListener("click", () =>{
    change.classList.toggle('shower')
    if(cyber.type ==='password'){
        cyber.type = 'text';
    }else{
        cyber.type ='password';
    }
})