

function onClickedEstimateSalary() {
  console.log("Estimate Salary button clicked");
  var total_exp = document.getElementById("uitotal_exp");
  var estSalary = document.getElementById("uiEstimatedSalary");

  var url = "http://127.0.0.1:5000/predict_salary"; // Use this if you are NOT using nginx which is first 7 tutorials//
  //var url = "/api/predict_salary";  Use this if  you are using nginx. i.e tutorial 8 and onwards//

  $.post(url, {
      total_exp: parseFloat(total_exp.value),
  },function(data, status) {
      console.log(data.estimated_salary);
      estSalary.innerHTML = "Rupees <h2>" + data.estimated_salary.toString() + "</h2>";
      console.log(status);
  });
}

function onPageLoad() {
    console.log( "document loaded" );
}

window.onload = onPageLoad;
