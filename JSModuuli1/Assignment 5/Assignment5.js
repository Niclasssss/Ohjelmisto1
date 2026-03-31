const vuosi = Number(prompt('Anna vuosi.'))

if (vuosi % 4 == 0 && (vuosi % 100 != 0 || vuosi % 400 == 0)) {
     document.querySelector('#vuosi').innerHTML = vuosi + ' on karkausvuosi.';
} else {
    document.querySelector('#vuosi').innerHTML = vuosi + ' ei ole karkausvuosi.';
}