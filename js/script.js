// раскрытие меню
document.querySelector(".burger").addEventListener("click", () => {
    document.querySelector(".nav-links").classList.toggle("nav-links__active");
});

// нажатие на любую другую точку не связанную с меню, она будет закрываться 
const box = document.querySelector(".hamburger-menu");
document.addEventListener('click', (e) => {
    const click = e.composedPath().includes(box);
    const navLinks = document.querySelector(".nav-links");
    if(!click && navLinks.classList.contains("nav-links__active"))
        $('.burger').click();
})

// появление формы кому отправить
function togglePopup() {
    const overlay = document.getElementById('popupOverlay');
    overlay.classList.toggle('show');
}

// скролл
// Template
// document.addEventListener("DOMContentLoaded", function () {
//     const header = document.querySelector(".header");
//     $(window).on("scroll", function () {
//       if ($(this).scrollTop() > 1) {
//         header.classList.add("header__scroll");
//       } else if (
//         $(this).scrollTop() < 1 ){
//         header.classList.remove("header__scroll");
//       }
//     });
// });