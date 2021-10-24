let containers = [];
let newDiv;
let interval = 0;
containers = document.querySelectorAll("div.container");
containers.forEach(container => {
    newDiv = document.createElement("div");
    if (interval == 0) {
        newDiv.setAttribute("class", "animate__animated animate__fadeIn");
    } else {
        newDiv.setAttribute("class", "animate__animated animate__fadeIn animate__delay-" + interval + "s");

    }
    // newDiv.style.setProperty('--animate-delay', String(interval) + 's');
    if (container.parentNode.tagName != "NAV") {
        console.log("1");
        let childNodes = container.children;

        container.appendChild(newDiv);

        childNodes.forEach(childNode => {
            newDiv.append(childNode);
        })

        if (interval >= 2) {
            interval = 2;
        } else {
            interval += 1;  
        }
        
    }
    console.log("2");
})


// if (containers[0].parentNode == document.getElementsByTagName("nav")[0]) {
//     console.log(Array.isArray(containers));
//     let containersArray = Array.from(containers);   // converts NodeList to Array
//     containersArray.shift();
//     console.log(containersArray);
// }
// containersArray[0].createElement("span");
// containersArray[0].classList.add('animate__animated', 'animate__fadeInUp');
console.log("end");

function sleep(ms) {
    return new Promise((r) => setTimeout(r, ms));
}