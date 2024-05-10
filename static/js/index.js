// Check if window was scrolled or not
window.onscroll = function () {
    let topButton = document.getElementById("scroll-to-top");
    if (document.body.scrollTop > 30 || document.documentElement.scrollTop > 30) {
        topButton.classList.add("active");
    } else {
        topButton.classList.remove("active");
    }
}

// GO to top of the page when click
function goTop() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}