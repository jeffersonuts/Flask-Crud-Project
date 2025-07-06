document.querySelectorAll(".lightbox").forEach((link) => {
  link.addEventListener("click", function (e) {
    e.preventDefault();

    const overlay = document.createElement("div");
    overlay.classList.add("lightbox-overlay");

    const img = document.createElement("img");
    img.src = this.href;

    overlay.appendChild(img);
    document.body.appendChild(overlay);

    overlay.addEventListener("click", () => {
      overlay.remove();
    });
  });
});
