let isLoading = false;
let nextPage = 2; // Assuming you start with page 2, change this if necessary

let imageContainer = document.querySelector("#content-section");
let doc = document.querySelector("main");// Removed .container here
console.log(imageContainer, doc);

doc.addEventListener("scroll", (event) => {
    alert(`Document scroll event fired!`);
});

