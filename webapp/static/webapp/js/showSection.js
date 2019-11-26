const showSection = function(sectionId) {
  const mainSections = document.querySelectorAll("#page-content .content-section");
  const selectedSection = document.querySelector(sectionId);
  mainSections.forEach((section) => {
    const displayStyle = section === selectedSection ? "flex" : "none";
    section.style.display = displayStyle;
  });
}

const setActive = function(linkListId, clickedLinkHref) {
  const linkListDOMElement = document.querySelector(linkListId);
  const linkList = linkListDOMElement.querySelectorAll(linkListId.concat(" li"));
  const clickedLink = linkListDOMElement.querySelector("a[href='{0}']".format(clickedLinkHref));
  linkList.forEach((linkListItem) => {
    linkListItem.classList.remove("active-nav-link");
  })
  clickedLink.parentElement.classList.add("active-nav-link");
}

const checkSection = function(currentUrl) {
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

const unfoldNavTree = function(navbarId, sectionId) {
  const ulSelector = "{0} > ul > li > ul ul".format(navbarId);
  const iconSelector = "{0} > ul > li > ul i".format(navbarId);
  const linkIcons = document.querySelectorAll(iconSelector);
  linkIcons.forEach((icon) => {
    icon.classList.remove("fa-caret-down");
    icon.classList.add("fa-caret-right");
  });

  const navTreeLists = document.querySelectorAll(ulSelector);
  navTreeLists.forEach((treeList) => treeList.style.display = "none");

  const sectionIdArray = sectionId.split('-');
  if (sectionIdArray[0] === "#categorie") {
    let categoryString = "{0}-".format(sectionIdArray[1]);
    for (let i = 2, j = sectionIdArray.length; i < j; i++) {
      categoryString = categoryString.concat(sectionIdArray[i]);
      const categoryLinkSelector = "{0} a[href='#categorie-{1}']".format(navbarId, categoryString);
      const categoryLink = document.querySelector(categoryLinkSelector);
      if (categoryLink.firstElementChild !== null) {
        const linkIconClasses = categoryLink.firstElementChild.classList;
        linkIconClasses.remove("fa-caret-right");
        linkIconClasses.add("fa-caret-down");
        const categoryListSelector = "#category-{0}-options".format(categoryString);
        const categoryList = document.querySelector(categoryListSelector);
        categoryList.style.display = "flex";
        categoryString = categoryString.concat("-");
      }
    }
  }
}

const displaySection = function(navbarId) {
  const currentUrl = location.href.split('#');
  const sectionId = "#".concat(currentUrl[1]);
  checkSection(currentUrl);
  setActive(navbarId, sectionId);
  showSection(sectionId);
}
