// from data.js
var tableData = data;
// YOUR CODE HERE!
console.log(tableData);
// YOUR CODE HERE!
var tbody = d3.select('tbody');
// Refactor to use Arrow Functions!
tableData.forEach((sheepleReport) => {
    var row = tbody.append('tr');
    Object.values(sheepleReport).forEach(value => {
        var cell = row.append('td');
        cell.text(value);
    });
});
// Select the button
var button = d3.select('#filter-btn');
button.on('click', function() {
    alert('you clicked a button ');
    // Select the input element and get the raw HTML nodeß
    var inputElement = d3.select('#datetime');
    // Get the value property of the input element
    var inputValue = inputElement.property('value');
    //alert('you clicked a button');
    var cityValue = d3.select('#city').property("value");
    d3.select("tbody").selectAll("tr").remove()
    //ad some logic to avoid null filtering
    let filterData = tableData;
    if (inputValue !== ""){
    filterData = tableData.filter(uforow =>uforow.datetime ===inputValue);
    }
    if (cityValue !== ""){
    filterData = filterData.filter(UFO_row => UFO_row.city === cityValue);
    }
    console.log(filterData);
    filterData.forEach((sheepleReport) => {
        var row = tbody.append('tr');
        Object.values(sheepleReport).forEach(value => {
            var cell = row.append('td');
            cell.text(value);
        });
    });
});