let CreateNewStrategy = document.querySelector('#CreateNewStrategy');

let modal = document.querySelector('.modal');
let Content_FormAddstrategy = document.querySelector('.Content_FormAddstrategy');
CreateNewStrategy.addEventListener('click',function () {
  modal.style.display = "flex";
  Content_FormAddstrategy.style.display="grid";

});

let Content_FormAddstrategy_header_close = document.querySelector('.Content_FormAddstrategy_header_close');

Content_FormAddstrategy_header_close.addEventListener('click',function () {
  modal.style.display = "none";
  Content_FormAddstrategy.style.display="none";

});

let Content_FormAddstrategy_Buttons_style1 = document.querySelector('.Content_FormAddstrategy_Buttons_style1');

Content_FormAddstrategy_Buttons_style1.addEventListener('click',function () {
  modal.style.display = "none";
  Content_FormAddstrategy.style.display="none";

});
