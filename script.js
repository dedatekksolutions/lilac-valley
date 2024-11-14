// Wait until the DOM content is fully loaded before running the script
document.addEventListener("DOMContentLoaded", async () => {
    let slideIndex = 0; // Initialize the slide index to track the current image in the hero slideshow
    let heroImages = []; // Array to hold the URLs of hero images

    // Helper function to shuffle the array for random image order
    function shuffleArray(array) {
        // Fisher-Yates shuffle algorithm to randomize array order
        for (let i = array.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [array[i], array[j]] = [array[j], array[i]]; // Swap elements
        }
    }

    // Fetch the list of hero images from the server
    try {
        const response = await fetch('http://127.0.0.1:8000/hero-images');
        heroImages = await response.json();

        // Randomize image order by shuffling the array
        if (heroImages.length > 0) {
            shuffleArray(heroImages);

            // Set the initial hero image to a random image from the shuffled array
            document.querySelector('.hero').style.backgroundImage = `url(${heroImages[0]})`;
        }
    } catch (error) {
        console.error("Error fetching hero images:", error); // Log error if fetching fails
    }

    // Function to change the hero background image at regular intervals
    function changeHeroImage() {
        if (heroImages.length > 0) {
            // Move to the next image in the shuffled array, looping back to the start
            slideIndex = (slideIndex + 1) % heroImages.length;
            document.querySelector('.hero').style.backgroundImage = `url(${heroImages[slideIndex]})`;
        }
    }

    // Change the hero image every 5 seconds
    setInterval(changeHeroImage, 5000);
});

//Toggle red boarder to elements
function toggleDebugOutline() {
    document.body.classList.toggle('debug-outline');
}

// Wait until the DOM content is fully loaded before running the gallery script
document.addEventListener("DOMContentLoaded", async () => {
    let currentImage = 0; // Initialize the index for tracking the current image in each gallery
    let galleryImages = []; // Array to hold the URLs of gallery images

    // Fetch the list of gallery images from the server
    try {
        const response = await fetch('http://127.0.0.1:8000/gallery-images');
        galleryImages = await response.json();
    } catch (error) {
        console.error("Error fetching gallery images:", error); // Log error if fetching fails
    }

    // Find all elements with the 'gallery' class to apply the image cycling
    const galleries = document.querySelectorAll('.gallery');
    galleries.forEach(gallery => {
        // Set the initial gallery background image if images are available
        if (galleryImages.length > 0) {
            gallery.style.backgroundImage = `url(${galleryImages[currentImage]})`;
        }

        // Handle click events on the gallery to switch images
        gallery.addEventListener('click', (event) => {
            const galleryWidth = gallery.offsetWidth;

            // Check if click was on the left or right half of the gallery
            if (event.offsetX < galleryWidth / 2) {
                // Left half clicked - show the previous image
                currentImage = (currentImage - 1 + galleryImages.length) % galleryImages.length;
            } else {
                // Right half clicked - show the next image
                currentImage = (currentImage + 1) % galleryImages.length;
            }
            gallery.style.backgroundImage = `url(${galleryImages[currentImage]})`;
        });

        // Prevent the "Book Now" button from triggering the gallery click event
        const bookNowButton = gallery.querySelector('.book-now');
        if (bookNowButton) {
            bookNowButton.addEventListener('click', (event) => {
                event.stopPropagation(); // Stop click event propagation to the gallery
            });
        }
    });

    
    
});


