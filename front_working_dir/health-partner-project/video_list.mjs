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
      console.log("vi")
      if (modalBody.hasChildNodes()) {
        console.log("zxc");
        modalBody.removeChild(modalBody.lastChild);
      }
      if(modalBody.hasChildNodes())
          modalBody.removeChild(modalBody.lastChild);
      
      console.log(modalBody.hasChildNodes());

      // modal에 새로운 영상 생성
      modalBody.appendChild(ratioCloneNode);

      // 제목, 조회수 등 처리
      let iframeNode = document.getElementsByClassName("modal-body")[0].querySelector("iframe");

      console.log(iframeNode)
      let str = "";

      let videoDetailElement = document.createElement("div");
      // let titleElement = document.createTextNode(iframeNode.getAttribute("data-title"));
      // let titleElement = document.createTextNode(iframeNode.dataset.title);
      document.querySelector(".modal-title").innerHTML = iframeNode.dataset.title;
      let viewsElement = document.createTextNode("조회수 " + iframeNode.dataset.views + "회<br>");
      let tagElement = document.createTextNode("태그: " + iframeNode.dataset.tag + "<br>");
      // videoDetailElement.appendChild(titleElement);
      if (typeof(iframeNode.dataset.tag) == "undefined" || iframeNode.dataset.tag == "") {
        str = "조회수 " + iframeNode.dataset.views + "회<br/>";
      } else {
        str = "조회수 " + iframeNode.dataset.views + "회<br/>" + "태그: " + iframeNode.dataset.tag + "\n";
      }
      videoDetailElement.appendChild(viewsElement);
      videoDetailElement.appendChild(tagElement);
      // modalBody.appendChild(videoDetailElement);
      let strDiv = document.createElement("div");
      strDiv.innerHTML = str;
      document.querySelector(".modal-body").appendChild(strDiv);
      // document.querySelector(".modal-body").innerHTML = str;
      // modalBody.appendChild(str);  

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