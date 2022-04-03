
//=========================================================================
let ContentBlocksInfo1 = document.querySelector('#ContentBlocksInfo1');
let ContentBlocksBlock1 = document.querySelector('#ContentBlocksBlock1');
let ContentBlocksInfoClose1 = document.querySelector('#ContentBlocksInfoClose1');

ContentBlocksBlock1.addEventListener('click', function () {
ContentBlocksInfo1.style.display = 'block';
});
ContentBlocksInfoClose1.addEventListener('click', function () {
ContentBlocksInfo1.style.display = 'none';
});
//=========================================================================
let ContentBlocksInfo2 = document.querySelector('#ContentBlocksInfo2');
let ContentBlocksBlock2 = document.querySelector('#ContentBlocksBlock2');
let ContentBlocksInfoClose2 = document.querySelector('#ContentBlocksInfoClose2');

ContentBlocksBlock2.addEventListener('click', function () {
ContentBlocksInfo2.style.display = 'block';
});
ContentBlocksInfoClose2.addEventListener('click', function () {
ContentBlocksInfo2.style.display = 'none';
});
//=========================================================================
let ContentBlocksInfo3 = document.querySelector('#ContentBlocksInfo3');
let ContentBlocksBlock3 = document.querySelector('#ContentBlocksBlock3');
let ContentBlocksInfoClose3 = document.querySelector('#ContentBlocksInfoClose3');

ContentBlocksBlock3.addEventListener('click', function () {
ContentBlocksInfo3.style.display = 'block';
});
ContentBlocksInfoClose3.addEventListener('click', function () {
ContentBlocksInfo3.style.display = 'none';
});
//=========================================================================
let range1 = document.querySelector('#range1');
let slider1Input = document.querySelector('#slider1Input');

range1.addEventListener('change', function () {
slider1Input.value = range1.value;
});
slider1Input.addEventListener('change', function () {
range1.value = slider1Input.value;
});
//=========================================================================
let range2 = document.querySelector('#range2');
let slider2Input = document.querySelector('#slider2Input');

range2.addEventListener('change', function () {
slider2Input.value = range2.value;
});
slider1Input.addEventListener('change', function () {
range2.value = slider1Input.value;
});
//=========================================================================
//=========================================================================
let range3 = document.querySelector('#range3');
let slider3Input = document.querySelector('#slider3Input');

range3.addEventListener('change', function () {
slider3Input.value = range3.value;
});
slider3Input.addEventListener('change', function () {
range3.value = slider3Input.value;
});
//=========================================================================
//=========================================================================
let range4 = document.querySelector('#range4');
let slider4Input = document.querySelector('#slider4Input');

range4.addEventListener('change', function () {
slider4Input.value = range4.value;
});
slider4Input.addEventListener('change', function () {
range4.value = slider4Input.value;
});
//=========================================================================
//=========================================================================
let range5 = document.querySelector('#range5');
let slider5Input = document.querySelector('#slider5Input');

range5.addEventListener('change', function () {
slider5Input.value = range5.value;
});
slider5Input.addEventListener('change', function () {
range5.value = slider5Input.value;
});
//=========================================================================

let ContentBlocksSetting = document.querySelector('.ContentBlocksSetting');
let ContentBlocksInfoClose = document.querySelector('#ContentBlocksInfoClose');

let ContentBlocksInfoButton1 = document.querySelector('#ContentBlocksInfoButton1');
let ContentBlocksInfoButton2 = document.querySelector('#ContentBlocksInfoButton2');
let ContentBlocksInfoButton3 = document.querySelector('#ContentBlocksInfoButton3');

let NameStrategiesShow1 = document.querySelector('#NameStrategiesShow1');
let NameStrategiesShow2 = document.querySelector('#NameStrategiesShow2');
let NameStrategiesShow3 = document.querySelector('#NameStrategiesShow3');

let hidden = document.querySelector('#hidden');

let ContentBlocksSettingShow = document.querySelector('#ContentBlocksSettingShow');

ContentBlocksInfoClose.addEventListener('click', function () {
  ContentBlocksSetting.style.display = 'none';
  ContentBlocksInfo2.style.display = 'none';
});
//------------------------------------------------------------------
ContentBlocksInfoButton1.addEventListener('click', function () {
  ContentBlocksInfo2.style.display = 'none';
  ContentBlocksInfo1.style.display = 'none';
  ContentBlocksInfo3.style.display = 'none';

  ContentBlocksSetting.style.display = 'block';
ContentBlocksSettingShow.innerHTML = NameStrategiesShow1.innerHTML;
hidden.value = NameStrategiesShow1.innerHTML;
});
//------------------------------------------------------------------
ContentBlocksInfoButton2.addEventListener('click', function () {
  ContentBlocksInfo2.style.display = 'none';
  ContentBlocksInfo1.style.display = 'none';
  ContentBlocksInfo3.style.display = 'none';

  ContentBlocksSetting.style.display = 'block';
ContentBlocksSettingShow.innerHTML = NameStrategiesShow2.innerHTML;
hidden.value = NameStrategiesShow2.innerHTML;
});

ContentBlocksInfoButton3.addEventListener('click', function () {
  ContentBlocksInfo2.style.display = 'none';
  ContentBlocksInfo1.style.display = 'none';
  ContentBlocksInfo3.style.display = 'none';

  ContentBlocksSetting.style.display = 'block';
ContentBlocksSettingShow.innerHTML = NameStrategiesShow3.innerHTML;
hidden.value = NameStrategiesShow3.innerHTML;
});
