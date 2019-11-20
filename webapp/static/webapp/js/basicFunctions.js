// String format function.
if (!String.prototype.format) {
  String.prototype.format = function() {
    var args = arguments;
    return this.replace(/{(\d+)}/g, function(match, number) {
      return typeof args[number] != 'undefined'
        ? args[number]
        : match
      ;
    });
  };
}

const getStorageValueOrDefault = function(key, defaultval) {
  let value = localStorage.getItem(key);
  (value === null) ? value = defaultval : value = JSON.parse(value);

  return value;
}

const setStorageValue = function(key, val) {
  localStorage.setItem(key, JSON.stringify(val));
}

const foldWindow = function(windowId) {
  const foldableWindow = document.querySelector(windowId);
  const displayStyle = foldableWindow.style.display === "flex" ? "none" : "flex";
  foldableWindow.style.display = displayStyle;

  return displayStyle;
}

const showTab = function(clickedButton, buttonsClass, activeTabId, tabWindowsClass) {
  const activeTab = document.querySelector(activeTabId);
  const tabList = document.querySelectorAll(tabWindowsClass);
  const buttonsList = document.querySelectorAll(buttonsClass);

  tabList.forEach((tab) => tab.style.display = "none");
  buttonsList.forEach((button) => button.classList.remove("active"));

  clickedButton.classList.add("active");
  activeTab.style.display = "flex";
}

const foldSuggestionWindow = function(button, windowId) {
  const icon = button.querySelector("i");
  const iconClasses = icon.classList;
  if (iconClasses.contains("fa-caret-right")) {
    iconClasses.remove("fa-caret-right");
    iconClasses.add("fa-caret-down");
  }
  else {
    iconClasses.remove("fa-caret-down");
    iconClasses.add("fa-caret-right");
  }
  foldWindow(windowId);
}

const filterSharedTeachers = function() {
  const sharedTeacherForm = document.querySelector("#share-options > nav");
  const teacherList = document.querySelectorAll("#teacher-overview li");
  const sharedTeacherList = document.querySelectorAll("#teacher-overview .shared");
  const unsharedTeacherList = document.querySelectorAll("#teacher-overview .unshared");
  const textFilter = sharedTeacherForm.querySelector("#teachernav");
  const checkShared = sharedTeacherForm.querySelector("#showshared");
  const checkUnshared = sharedTeacherForm.querySelector("#showunshared");

  teacherList.forEach((teacher) => teacher.style.display = "none");
  if (checkShared.checked) {
    sharedTeacherList.forEach((teacher) => teacher.style.display = "flex");
  }
  if (checkUnshared.checked) {
    unsharedTeacherList.forEach((teacher) => teacher.style.display = "flex");
  }
  if (textFilter.value.length > 0) {
    const searchPattern = new RegExp(textFilter.value.toLowerCase());
    teacherList.forEach((teacher) => {
      if (!searchPattern.test(teacher.innerText.toLowerCase())) {
        teacher.style.display = "none";
      }
    });
  }
}

const filterSharedProfiles = function() {
  const studentName = document.querySelector("#studentname");
  const studentId = document.querySelector("#studentid");
  const studentList = document.querySelectorAll("#student-overview li");

  studentList.forEach((student) => student.style.display = "flex");

  if (studentName.value.length > 0) {
    const nameSearchPattern = new RegExp(studentName.value.toLowerCase());
    studentList.forEach((student) => {
      const nameData = student.querySelector(".name-data");
      if (!nameSearchPattern.test(nameData.innerText.toLowerCase())) {
        student.style.display = "none";
      }
    });
  }

  if (studentId.value.length > 0) {
    const idSearchPattern = new RegExp(studentId.value.toLowerCase());
    studentList.forEach((student) => {
      const idData = student.querySelector(".id-data");
      if (!idSearchPattern.test(idData.innerText.toLowerCase())) {
        student.style.display = "none";
      }
    });
  }
}
