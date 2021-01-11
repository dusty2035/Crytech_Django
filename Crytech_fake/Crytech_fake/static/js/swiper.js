var slideshow = new Swiper('.swiper-container', {

  autoplay: {
    delay: 6500,
    disableOnInteraction: true,
  },

  loop : true ,

  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },
  keyboard: true,
});