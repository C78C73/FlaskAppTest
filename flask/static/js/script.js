const button = document.getElementById('testbutton');
const name1 = document.getElementById('inputbox1');
const name2 = document.getElementById('inputbox2');

button.addEventListener('click', () => {
    name2.value = name1.value;
    alert('button was clicked');
})