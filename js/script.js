document.querySelector(".burger").addEventListener("click", () => {
    document.querySelector(".nav-links").classList.toggle("nav-links__active");
});

const box = document.querySelector(".hamburger-menu");
document.addEventListener('click', (e) => {
    const click = e.composedPath().includes(box);
    if(!click)
        $('.burger').click();
})


