let ContentBlocksInfo = document.querySelector('.ContentBlocksInfo');
let ContentBlocksBlock = document.querySelectorAll('.ContentBlocksBlock');
let ContentBlocksInfoClose = document.querySelector('#ContentBlocksInfoClose');

for (var i = 0; i < ContentBlocksBlock.length; i++) {
  ContentBlocksBlock[i].addEventListener('click', function () {
  ContentBlocksInfo.style.display = 'block';
  });
}

ContentBlocksInfoClose.addEventListener('click', function () {
ContentBlocksInfo.style.display = 'none';
});
