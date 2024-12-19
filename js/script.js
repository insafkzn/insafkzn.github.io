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

// появление формы обратной связи
function togglePopup_obr() {
    const overlay = document.getElementById('popupOverlay__obr');
    overlay.classList.toggle('show');
}

// появление формы кому отправить
function togglePopup() {
  const overlay = document.getElementById('popupOverlay');
  overlay.classList.toggle('show');
}

// скролл
// Template
document.addEventListener("DOMContentLoaded", function () {
    const header = document.querySelector(".header");
    const nav = document.querySelector("nav");
    $(window).on("scroll", function () {
      if ($(this).scrollTop() > 1) {
        nav.style.minHeight = "55px";
        nav.style.backgroundColor = "rgb(240, 240, 240)"
      } else {
        nav.style.minHeight = "70px";
        nav.style.backgroundColor = "white"
      }
    });
});

// раскрытие меню
document.querySelector(".nav-links_link_critism").addEventListener("click", () => {
  document.querySelector(".nav-links_link_critism").classList.toggle("nav-links_link_critism_active");
  document.querySelector(".nav-links__sub").classList.toggle("nav-links__sub_active");
  document.querySelector(".nav-links__submenu").classList.toggle("nav-links__submenu_active");
});

// lazy load

const images = document.querySelectorAll('img');

const options = {
  root: null,
  rootMargin: '0px',
  threshold: 0.1
}

function handleImg(myImg, observer){
  myImg.forEach(myImgSingle => {
    // console.log(myImgSingle.intersectionRatio);
    if(myImgSingle.intersectionRatio > 0){
      loadImage(myImgSingle.target);
    }
  })
}

function loadImage(image){
  image.src = image.getAttribute('data')
}

const observer = new IntersectionObserver(handleImg, options)

images.forEach(img => {
  observer.observe(img)
})
// lazy lozd end