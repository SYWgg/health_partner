let containers = [];
let newDiv;
let interval = 0;
let flag = 0;
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

        // if (interval >= 2) {
        //     interval = 2;
        // } else if ((flag % 3) == 1) {
        //     interval += 1;  
        // }

        // flag += 1;
    }
    console.log("2");
})

console.log("end");

function sleep(ms) {
    return new Promise((r) => setTimeout(r, ms));
}

// container = document.querySelector("div.container");
// newDiv = document.createElement("div");
// newDiv.setAttribute("class", "animate__animated animate__fadeIn");
