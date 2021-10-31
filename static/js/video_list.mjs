let cards = document.querySelectorAll("div.ratio");
let masks = document.querySelectorAll("div.mask")
let modalBody = document.querySelector("div.modal-body");
let video_count = 0;
cards.forEach((card, index) => {
    let ratioNode = card;
    let iframeNode = ratioNode.children;
    let aNode = masks[index].parentNode;

    // 모달의 내용을 해당 동영상으로
    aNode.addEventListener("click", function () {
        var ratioCloneNode = ratioNode.cloneNode(true);
        if (video_count >= 1) {
            modalBody.removeChild(modalBody.lastChild);
        }
        modalBody.appendChild(ratioCloneNode);
        video_count += 1;
    });
})