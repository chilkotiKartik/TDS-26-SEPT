// Run in DevTools console on the exam page
[...document.querySelectorAll(".featured.sale")]
  .reduce((sum, el) => sum + Number(el.dataset.discount), 0);
