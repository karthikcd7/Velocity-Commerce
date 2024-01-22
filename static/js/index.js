

drawBoard();

const servers = ["cell-6-4", "cell-4-13", "cell-6-27", "cell-16-23", "cell-20-28", "cell-23-20", 
"cell-19-14", "cell-23-5", "cell-15-7"]; 


const path = []
let selectedCell = null;


function setSource(){
    const cell= document.getElementById(selectedCell)
    cell.style.backgroundColor="green";

}
function isCellDisabled(cellId) {
    return servers.includes(cellId) || path.includes(cellId);
}
function colorServers(servers){
    for (var i = 0; i < servers.length; i++) {
        var cell = document.getElementById(servers[i]);
        cell.textContent = i;
        cell.style.border='2px solid black';
    }

}
colorServers(servers);
colorPath('cell-6-4', 'cell-15-7');
colorPath('cell-4-13', 'cell-15-7');
colorPath('cell-4-13', 'cell-6-27');
colorPath('cell-19-14', 'cell-15-7');
colorPath('cell-19-14', 'cell-4-13');
colorPath('cell-19-14', 'cell-23-5');
colorPath('cell-19-14', 'cell-23-20');
colorPath('cell-23-20', 'cell-20-28');
colorPath('cell-16-23', 'cell-20-28');

function colorXY(cellId) {
    if (isCellDisabled(cellId)) {
      return;
    }
    const cell= document.getElementById(cellId)
    const source= document.getElementById("source")
    source.value=cellId
    if (cell) {
        cell.style.backgroundColor = 'green';
    }
    if (selectedCell) {
        selectedCell.style.backgroundColor = "";
      }
      cell.style.backgroundColor = "green";
      selectedCell = cell;
}

function colorCell(cell) {
    const x = cell.cellIndex + 1;
    const y = cell.parentNode.rowIndex;
    
    colorXY(cell.id)
}

function drawBoard(){
    const numRows = 25; 
    const numCols = 35; 
    const table = document.getElementById("table");
    const thead = document.createElement("thead");
    const headRow = document.createElement("tr");
    thead.appendChild(headRow);
    const emptyHeader = document.createElement("th");
    headRow.appendChild(emptyHeader);
    for (let j = 0; j < numCols; j++) {
        const colHeader = document.createElement("th");
        colHeader.textContent = `${j+1}`;
        headRow.appendChild(colHeader);
    }
    table.appendChild(thead);
    const tbody = document.createElement("tbody");
    for (let i = 1; i <= numRows; i++) {
        const row = document.createElement("tr");
        const rowHeader = document.createElement("th");
        rowHeader.textContent = `${i}`;
        row.appendChild(rowHeader);
        for (let j = 1; j <= numCols; j++) {
            const cell = document.createElement("td");
            cell.setAttribute("id", `cell-${i}-${j}`);
            cell.setAttribute("class", "cell");
            cell.setAttribute("onclick", `colorCell(this)`);
            cell.style.width = "50px";
            row.appendChild(cell);
        }
    tbody.appendChild(row);
    }
    table.appendChild(tbody);
}



function popup(cellId, modelId){
var modal = document.getElementById(modelId);
var span = document.getElementsByClassName("close")[0];
var server = document.getElementById(cellId)
if(server){
    server.onclick = function() {
        modal.style.display = "block";
    }
}
span.onclick = function() {
    modal.style.display = "none";
}
window.onclick = function(event) {
    if (event.target == modal) {
    modal.style.display = "none";
    }
}
}
// popup("cell-2-1","modal-0");
// popup("cell-1-1", "modal-0");

function colorPath(start, end) {
    // get start and end cell objects
    var startCell = document.getElementById(start);
    var endCell = document.getElementById(end);
  
    // get start and end cell coordinates
    var startRow = parseInt(startCell.parentElement.rowIndex);
    var startCol = parseInt(startCell.cellIndex);
    var endRow = parseInt(endCell.parentElement.rowIndex);
    var endCol = parseInt(endCell.cellIndex);
  
    // determine direction of path
    var dirRow = startRow < endRow ? 1 : -1;
    var dirCol = startCol < endCol ? 1 : -1;
  
    // color cells in path
    var row = startRow;
    var col = startCol;
    while (row != endRow || col != endCol) {
      // get current cell object and color it
      var cell = document.getElementById("cell-" + row + "-" + col);
      path.push("cell-" + row + "-" + col)
      cell.style.backgroundColor = "yellow";
  
      // move to next cell
      if (row != endRow) row += dirRow;
      if (col != endCol) col += dirCol;
    }
  
    // color end cell
    endCell.style.backgroundColor = "yellow";
  }


  
  
  