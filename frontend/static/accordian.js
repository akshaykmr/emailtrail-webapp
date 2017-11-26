function toggleClass(el, className) {
  if (el.classList) {
    el.classList.toggle(className);
  } else {
    var classes = el.className.split(' ');
    var existingIndex = classes.indexOf(className);

    if (existingIndex >= 0)
      classes.splice(existingIndex, 1);
    else
      classes.push(className);

    el.className = classes.join(' ');
  }
}

function configureTrigger(trigger) {
  var toggleSiblingContent = function toggleSiblingContent() {
    toggleClass(trigger.parentNode, 'cbp-ntopen');
  };
  trigger.addEventListener('click', toggleSiblingContent);
}

document.querySelectorAll('.cbp-nttrigger').forEach(configureTrigger);
