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


// нажатие на любую другую точку не связанную с меню, она будет закрываться 

// document.addEventListener('mouseover', (e) => {
//   const sub_link = document.querySelector(".nav-links_link_sub");
//   const navLinks = document.querySelector(".nav-links__submenu");
  
//   // Проверяем, наведен ли курсор на подменю или ссылку "О фонде"
//   const isHoveringSubLink = e.composedPath().includes(sub_link);
//   const isHoveringNavLinks = e.composedPath().includes(navLinks);
//   // console.log(isHoveringSubLink)
//   // console.log(isHoveringNavLinks)
//   if (isHoveringSubLink || isHoveringNavLinks) {
//     document.getElementById('submenu').style.display = 'flex';
//   } else {
//     document.getElementById('submenu').style.display = 'none';
//   }
// });

// const sub_link = document.querySelector(".nav-links_link_sub");
// const navLinks = document.querySelector(".nav-links__submenu");

// sub_link.addEventListener('onmouseover', function(){
//   document.querySelector(".nav-links__submenu").style.display = 'flex';
// })
// navLinks.addEventListener('onmouseover', function(){
//   document.getElementById('.nav-links__submenu').style.display = 'flex';
// })


// function showSubmenu() { 
//   document.getElementById('submenu').style.display = 'flex'; 
// } 
// function hideSubmenu() { 
//   document.getElementById('submenu').style.display = 'none'; 
// }

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