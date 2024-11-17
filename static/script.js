// Wait until the DOM content is fully loaded before running the script
document.addEventListener("DOMContentLoaded", async () => {
    let slideIndex = 0; // Initialize the slide index to track the current image in the hero slideshow
    let heroImages = []; // Array to hold the URLs of hero images

    // Helper function to shuffle the array for random image order
    function shuffleArray(array) {
        for (let i = array.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [array[i], array[j]] = [array[j], array[i]]; // Swap elements
        }
    }

    // Fetch the list of hero images from the server
    try {
        const response = await fetch('http://127.0.0.1:8000/hero-images');
        heroImages = await response.json();

        if (heroImages.length > 0) {
            shuffleArray(heroImages);
            document.querySelector('.hero').style.backgroundImage = `url("${heroImages[0]}")`;
        }
    } catch (error) {
        console.error("Error fetching hero images:", error);
    }

    // Change the hero image every 5 seconds
    setInterval(() => {
        if (heroImages.length > 0) {
            slideIndex = (slideIndex + 1) % heroImages.length;
            document.querySelector('.hero').style.backgroundImage = `url("${heroImages[slideIndex]}")`;
        }
    }, 5000);
});

// Load gallery images and thumbnails dynamically
document.addEventListener("DOMContentLoaded", async () => {
    let galleryImages = [];

    try {
        const response = await fetch('http://127.0.0.1:8000/gallery-images');
        galleryImages = await response.json();
    } catch (error) {
        console.error("Error fetching gallery images:", error);
        return;
    }

    const mainGallery = document.querySelector('.gallery-main');
    const thumbnailContainer = document.querySelector('.gallery-thumbnails');

    if (galleryImages.length > 0) {
        mainGallery.style.backgroundImage = `url("${galleryImages[0]}")`;

        galleryImages.forEach((imageUrl) => {
            const thumbnail = document.createElement('img');
            thumbnail.src = imageUrl;
            thumbnail.alt = "Thumbnail";
            thumbnail.classList.add('thumbnail-image');

            thumbnail.addEventListener('click', () => {
                mainGallery.style.backgroundImage = `url("${imageUrl}")`;
            });

            thumbnailContainer.appendChild(thumbnail);
        });
    }
});
