import Header from "./Modules/Header.js";
new Header();

import Modal from "./Modules/Modal.js";
new Modal();

document.addEventListener('DOMContentLoaded', () => {
    const phoneFields = document.querySelectorAll('[data-field-phone]');
    const maskOptions = {
        mask: '+{7}(000)000-00-00',
    };

    phoneFields.forEach((field) => {
        IMask(field, maskOptions);
    });
});
