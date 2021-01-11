function calculateTip() {
  var billAmt = document.getElementById("mealTotal").value;
  var tipAmount = document.getElementById("tippingPercentage").value;
  var numOfPeople = document.getElementById("numberPeople").value;

  if (tipAmount === "another") {
    tipAmount = document.getElementById("tipNum").value/100;
  }

  if (billAmt === "" || tipAmount == 0) {
    alert("Please make sure ALL values are entered");
    return;
  }
  if (numOfPeople === "" || numOfPeople <= 1) {
    numOfPeople = 1;
    document.getElementById("each").style.display = "none";
  } else {
    document.getElementById("each").style.display = "block";
  }
  var total = (billAmt * tipAmount) / numOfPeople;
  total = Math.round(total * 100) / 100;
  total = total.toFixed(2);
  document.getElementById("totalTip").style.display = "block";
  document.getElementById("tip").innerHTML = total;

}
function clearForm() {
  document.getElementById("form").reset();
  document.getElementById("numPeople").value = "";
}

function show(value) {
  if (value == "another") {
    tipNum.style.display='inline-block';
    percentage.style.display='inline-block';
  } 
  else{
    tipNum.style.display='none';
    percentage.style.display='none';
  }
}
document.getElementById("totalTip").style.display = "none";
document.getElementById("each").style.display = "none";
document.getElementById("tipNum").style.display = "none";
document.getElementById("percentage").style.display = "none";
document.getElementById("calculate").onclick = function() {
  calculateTip();

};


document.getElementById("clear").onclick = function() {
  clearForm();
  document.getElementById("totalTip").style.display = "none";
  document.getElementById("each").style.display = "none";
  document.getElementById("tipNum").style.display = "none";
  document.getElementById("percentage").style.display = "none";

};

