document.addEventListener("DOMContentLoaded", function () {
    var loaderContainer = document.getElementById("loader2");
    var galleryImages = document.querySelectorAll(".gallery img");

    var loadedImagesCount = 0;

    if (galleryImages.length === 0) {
        loaderContainer.style.display = "none"; // Hide the loader immediately if there are no images
    } else {
        galleryImages.forEach(function (image) {
            image.addEventListener("load", function () {
                loadedImagesCount++;
                console.log(loadedImagesCount === galleryImages.length);
                if (loadedImagesCount === galleryImages.length) {
                    loaderContainer.style.display = "none"; // Hide the loader
                }
            });
        });
    }
});
