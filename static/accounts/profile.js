document.addEventListener("DOMContentLoaded", function() {
            var loaderContainer = document.getElementById("loader2");
            var galleryImages = document.querySelectorAll(".gallery img");
            var loadedImagesCount = 0;

            galleryImages.forEach(function(image) {
                image.addEventListener("load", function() {
                    loadedImagesCount++;
                    if (loadedImagesCount === galleryImages.length) {
                        loaderContainer.style.display = "none"; // Hide the loader
                    }
                });
            });
        });