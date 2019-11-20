const foldWindowAndSave = function(localStorageKey, windowId) {
  const displayStyle = foldWindow(windowId);
  const localStorageValue = getStorageValueOrDefault(localStorageKey, {});
  localStorageValue[windowId] = displayStyle;
  setStorageValue(localStorageKey, localStorageValue);
}

const displaySavedFoldWindows = function(localStorageKey) {
  const savedWindows = getStorageValueOrDefault(localStorageKey, {});
  for (windowId in savedWindows) {
    const foldDOMElement = document.querySelector(windowId);
    foldDOMElement.style.display = savedWindows[windowId];
  }
}

const setFoldWindow = function(localStorageKey, windowId, displayValue) {
  const savedWindows = getStorageValueOrDefault(localStorageKey, {});
  savedWindows[windowId] = displayValue;
  setStorageValue(localStorageKey, savedWindows);
}

const setSingleFoldWindowVisible = function(localStorageKey, visibleWindowId, windowIdSpecifier="", displayParentCategory=true, displayGrandparentCategory=true) {
  const savedWindows = getStorageValueOrDefault(localStorageKey, {});
  const visibleParentCategoryWindowId = visibleWindowId.slice(0, -2).concat(windowIdSpecifier);
  const visibleGrandparentCategoryWindowId = visibleWindowId.slice(0, -4).concat(windowIdSpecifier);
  const specifiedVisibleWindowId = visibleWindowId.concat(windowIdSpecifier);

  for (windowId in savedWindows) {
    setFoldWindow(localStorageKey, windowId, "none");
  }
  if (displayParentCategory) {
    setFoldWindow(localStorageKey, visibleParentCategoryWindowId, "flex");
  }
  if (displayGrandparentCategory) {
    setFoldWindow(localStorageKey, visibleGrandparentCategoryWindowId, "flex");
  }
  setFoldWindow(localStorageKey, specifiedVisibleWindowId, "flex");
}
