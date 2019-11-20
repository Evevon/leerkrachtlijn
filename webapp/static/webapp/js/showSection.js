const setActive = function(linkListId, clickedLink) {
  const linkList = document.querySelectorAll(linkListId.concat(" li"));
  linkList.forEach((linkListItem) => {
    linkListItem.classList.remove("active-nav-link");
  })
  clickedLink.parentElement.classList.add("active-nav-link");
}

const showSection = function(sectionId) {
  const mainSections = document.querySelectorAll("#page-content .content-section");
  const selectedSection = document.querySelector(sectionId);
  mainSections.forEach((section) => {
    const displayStyle = section === selectedSection ? "flex" : "none";
    section.style.display = displayStyle;
  });
}

const checkSection = function() {
  const currentUrl = location.href.split('#');
  const pagebody = document.querySelector("body");
  pagebody.classList.remove("orange-theme");
  pagebody.classList.remove("green-theme");
  pagebody.classList.remove("red-theme");
  pagebody.classList.remove("blue-theme");

  if (!document.getElementById(currentUrl[1])) {
    location.assign(currentUrl[0].concat("#overzicht"));
    pagebody.classList.add("orange-theme");
    showSection("#overzicht");
  }
  else if (currentUrl[1] === "dimensie-1" || currentUrl[1].includes("categorie-1")) {
    pagebody.classList.add("blue-theme");
    showSection("#".concat(currentUrl[1]));
  }
  else if (currentUrl[1] === "dimensie-2" || currentUrl[1].includes("categorie-2")){
    pagebody.classList.add("green-theme");
    showSection("#".concat(currentUrl[1]));
  }
  else if (currentUrl[1] === "dimensie-3" || currentUrl[1].includes("categorie-3")) {
    pagebody.classList.add("red-theme");
    showSection("#".concat(currentUrl[1]));
  }
  else {
    pagebody.classList.add("orange-theme");
    showSection("#".concat(currentUrl[1]));
  }
}

const setActiveOnWindowLoad = function(navbarId) {
  const currentUrl = location.href.split('#');
  const anchorLink = currentUrl[1] === undefined ? "overzicht" : currentUrl[1];
  const selector = "{0} a[href='#{1}']".format(navbarId, anchorLink);
  const activeLink = document.querySelector(selector);
  setActive(navbarId, activeLink);
}

window.onhashchange = function() {
  checkSection();
}

window.onload = function() {
  checkSection();
}
