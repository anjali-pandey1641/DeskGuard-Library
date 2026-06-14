let typing = false;

document.querySelectorAll("input").forEach(input => {

    input.addEventListener("focus", () => {
        typing = true;
    });

    input.addEventListener("blur", () => {
        typing = false;
    });

});

setInterval(() => {

    if (!typing) {
        location.reload();
    }

}, 5000);