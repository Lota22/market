let signup = document.form
let username = document.form.username
let fname = document.form.firstname
let lname = document.form.lastname
let email = document.form.email
let state = document.form.state
let phone = document.form.phone
let address = document.form.address
let password = document.form.password

let validate = () =>{
    if(username.value.length <=0){
        alert('Supply username');
        username.focus()
        return form();
    }

    if(fname.value.length <=0){
        alert('Supply first name');
        fname.focus()
        return form();
    }

    if(lname.value.length <=0){
        alert('Supply last name');
        lname.focus()
        return form();
    }
    if(email.value.length <=0){
        alert('Supply email');
        email.focus()
        return form();
    }
    if(state.value.length <=0){
        alert('Supply State');
        state.focus()
        return form();
    }
    if(phone.value.length <=0){
        alert('Supply phone number');
        phone.focus()
        return form();
    }
    if(address.value.length <=0){
        alert('Supply address');
        address.focus()
        return form();
    }
    if(password.value.length <=0){
        alert('Supply Password');
        password.focus()
        return form();
    }

    
}