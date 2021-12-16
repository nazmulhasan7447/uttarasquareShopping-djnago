const pop_up_close_btn = document.querySelector('.close_pop_up_box');
const main_pop_up_box = document.querySelector('.main-pop-box');
console.log(pop_up_close_btn);
window.onload = () => {
    main_pop_up_box.style.visibility = 'visible';
}

pop_up_close_btn.onclick = () =>{
    main_pop_up_box.style.visibility = 'hidden';
}
