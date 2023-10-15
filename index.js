function calculate() {
    let a = parseInt(document.getElementById("a").value);
    let b = parseInt(document.getElementById("b").value);
    let result = a + b;
    if (isNaN(result)) {
        result = "please enter numbers";
    }
    document.getElementById("result").innerHTML = "Result: " + result;
}