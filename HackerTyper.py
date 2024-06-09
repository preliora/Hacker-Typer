import os
import keyboard

os.system("title Hacker Typer")

index = 0
current = ""
text = """
function randomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1) + min);
}

function generateGrid() {
    const grid = [];
    for (let i = 0; i < 10; i++) {
        const row = [];
        for (let j = 0; j < 10; j++) {
            row.push(randomInt(1, 100));
        }
        grid.push(row);
    }
    return grid;
}

function displayGrid(grid) {
    for (let i = 0; i < grid.length; i++) {
        let rowStr = "";
        for (let j = 0; j < grid[i].length; j++) {
            rowStr += grid[i][j] + "\t";
        }
        console.log(rowStr);
    }
}

function sumOfGrid(grid) {
    let sum = 0;
    for (let i = 0; i < grid.length; i++) {
        for (let j = 0; j < grid[i].length; j++) {
            sum += grid[i][j];
        }
    }
    return sum;
}

function countEvenNumbers(grid) {
    let count = 0;
    for (let i = 0; i < grid.length; i++) {
        for (let j = 0; j < grid[i].length; j++) {
            if (grid[i][j] % 2 === 0) {
                count++;
            }
        }
    }
    return count;
}

function countOddNumbers(grid) {
    let count = 0;
    for (let i = 0; i < grid.length; i++) {
        for (let j = 0; j < grid[i].length; j++) {
            if (grid[i][j] % 2 !== 0) {
                count++;
            }
        }
    }
    return count;
}

function transposeGrid(grid) {
    const transposedGrid = [];
    for (let i = 0; i < grid[0].length; i++) {
        const row = [];
        for (let j = 0; j < grid.length; j++) {
            row.push(grid[j][i]);
        }
        transposedGrid.push(row);
    }
    return transposedGrid;
}

const grid = generateGrid();
console.log("Original Grid:");
displayGrid(grid);
console.log("Sum of all numbers in the grid:", sumOfGrid(grid));
console.log("Number of even numbers in the grid:", countEvenNumbers(grid));
console.log("Number of odd numbers in the grid:", countOddNumbers(grid));
console.log("Transposed Grid:");
const transposed = transposeGrid(grid);
displayGrid(transposed);

"""

running = True
os.system("color a")

while running:
    keyboard.read_key()
    os.system("cls")
    current += text[index]
    if index == len(text) - 1:
        running = False
    index += 1
    print(current)

os.system("pause")