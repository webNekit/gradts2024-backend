class Modal {
    selectors = {
        button: '[data-callback-button]', // Кнопки открытия модального окна
        modal: '[data-callback-modal]', // Само модальное окно
        close: '[data-callback-close]', // Кнопка закрытия модального окна
    };

    stateClasses = {
        isActive: 'is-active',
        isLock: 'off-scroll',
    };

    constructor() {
        // Находим все кнопки для открытия модальных окон
        this.buttons = document.querySelectorAll(this.selectors.button);
        // Находим модальное окно
        this.modal = document.querySelector(this.selectors.modal);

        if (!this.modal) {
            console.error('Модальное окно не найдено.');
            return;
        }

        // Привязываем события
        this.bindEvents();
    }

    bindEvents() {
        // Вешаем обработчик на каждую кнопку открытия модального окна
        this.buttons.forEach((button) => {
            button.addEventListener('click', this.openModal);
        });

        // Вешаем обработчик на кнопку закрытия
        const closeButton = this.modal.querySelector(this.selectors.close);
        if (closeButton) {
            closeButton.addEventListener('click', this.closeModal);
        }

        // Закрытие модального окна по клику на overlay
        this.modal.addEventListener('click', (event) => {
            if (event.target === this.modal) {
                this.closeModal();
            }
        });
    }

    openModal = () => {
        this.modal.classList.add(this.stateClasses.isActive);
        document.documentElement.classList.add(this.stateClasses.isLock);
    };

    closeModal = () => {
        this.modal.classList.remove(this.stateClasses.isActive);
        document.documentElement.classList.remove(this.stateClasses.isLock);
    };
}

export default Modal;
