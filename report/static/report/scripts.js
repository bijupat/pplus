(function () {
  document.querySelectorAll(".editrateinput").forEach(function (input) {
    input.onkeyup = function () {
      //console.log(document.querySelector('#datesubmit'))
      id = input.dataset.invkey;
      //console.log(id);
      //console.log(document.querySelectorAll("[data-invkey ="+id+"]"));
      //alert("editrateclicked for " + input.dataset.testname)
      document
        .querySelectorAll("[data-invkey=" + id + "]")
        .forEach(function (but) {
          but.disabled = false;
        });
    };
  });

  if (document.getElementById("addpayment")) {
    document
      .getElementById("addpayment")
      .addEventListener("change", function () {
        //console.log(document.querySelector('#datesubmit'))
        //alert("datechanged")
        document.querySelector("#addpaysubmit").disabled = false;
      });

    // on selecting date the submit button activated from disabled
    document
      .getElementById("addeditdiscountinput")
      .addEventListener("change", function () {
        //console.log(document.querySelector('#datesubmit'))
        //alert("datechanged")
        document.querySelector("#addeditdiscountsubmit").disabled = false;
      });
  }
})();
