function auto_height(elem) {  /* javascript */
  console.log(elem.style.min_height)
    repeated = elem.value.split('\n').length - 1;
    elem.style.height = (40 + 23 * repeated).toString() + 'px';
}