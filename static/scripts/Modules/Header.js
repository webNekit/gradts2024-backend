class Header {
    selectors = {
        root: '[data-header]', // Главный элемент шапки
        overlay: '[data-overlay-menu]',
        toglerButton: '[data-burger-menu]',
    }

    stateClasses = {
        isActive: 'is-active',
        isLock: 'is-lock',
        isScroll: 'is-scroll', // Класс для подчеркивания
    }

    bindEvents() {
        this.toglerButtonElement.addEventListener("click", this.onToglerButtonClick);
        window.addEventListener("scroll", this.onScroll); // Слушаем событие прокрутки
    }

    onToglerButtonClick = () => {
        this.toglerButtonElement.classList.toggle(this.stateClasses.isActive);
        this.overlayElement.classList.toggle(this.stateClasses.isActive);
        document.documentElement.classList.toggle(this.stateClasses.isLock);
    }

    onScroll = () => {
        const scrollThreshold = 50; // Порог скролла в пикселях
        if (window.scrollY > scrollThreshold) {
            this.rootElement.classList.add(this.stateClasses.isScroll);
        } else {
            this.rootElement.classList.remove(this.stateClasses.isScroll);
        }
    }

    constructor() {
        this.rootElement = document.querySelector(this.selectors.root);
        this.overlayElement = document.querySelector(this.selectors.overlay);
        this.toglerButtonElement = document.querySelector(this.selectors.toglerButton);
        this.bindEvents();
    }
}

export default Header;
