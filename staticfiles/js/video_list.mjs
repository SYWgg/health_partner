console.log("wpqkf")
let cards = document.querySelectorAll("div.ratio");
let masks = document.querySelectorAll("div.mask")
let modalBody = document.querySelector("div.modal-body");
let video_count = 0;
cards.forEach((card, index) => {
    let ratioNode = card;
    let aNode = masks[index].parentNode;

    // 모달의 내용을 해당 동영상으로
    aNode.addEventListener("click", function () {
        var ratioCloneNode = ratioNode.cloneNode(true);

        // modal에 기존 영상이 있을 경우 삭제
        if (video_count >= 1) {
            modalBody.removeChild(modalBody.lastChild);
            modalBody.removeChild(modalBody.lastChild);
        }

        // modal에 새로운 영상 생성
        modalBody.appendChild(ratioCloneNode);

        // 제목, 조회수 등 처리
        let iframeNode = ratioCloneNode.firstChild;

        console.log(iframeNode)

        let videoDetailElement = document.createElement("div");
        let titleElement = document.createTextElement(iframeNode.dataset.title);
        let viewsElement = documnet.createTextElement("조회수 " + iframeNode.dataset.views + "회");
        let tagElement = document.createTextElement("태그: " + iframeNode.dataset.tag);
        videoDetailElement.appendChild(titleElement);
        videoDetailElement.appendChild(viewsElement);
        videoDetailElement.appendChild(tagElement);
        document.body.insertAfter(modalBody.lastChild, videoDetailElement);

        video_count += 1;
    });
})

function insertAfter(referenceNode, newNode) {   
  if (!!referenceNode.nextSibling) {
    referenceNode.parentNode.insertBefore(newNode, referenceNode.nextSibling);
  } else {
    referenceNode.parentNode.appendChild(newNode);
  }  
}