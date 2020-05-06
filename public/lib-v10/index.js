function cardGen(file) {
    const id = file.name.replace(".", "_");
    return `<div class="card">
    <div class="title" id="${id}">${file.name} <a href="#${id}">#</a></div>
    <div class="cardContent">${marked(file.content, { headerIds: false })}</div>
</div>`;
}

function scrollToHash() {
    const requestedId = window.location.hash;
    if (requestedId[1]) {
        const element = document.querySelector(requestedId);
        if (element) {
            element.scrollIntoView();
        }
    }
}

async function main() {
    const data = await fetch(LIB_PATH + "data.json").then((v) => v.json());
    const finalContent = data.map(cardGen).join("");
    document.querySelector(".content").innerHTML = finalContent;
    Prism.highlightAll();
    scrollToHash();
}
main();
