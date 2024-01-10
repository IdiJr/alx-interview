# 0x05. N Queens
This project contains a sample interview task.
The N queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard.
![](https://static.dw.com/image/55872075_604.webp)

In this task, we're expected to a program that provides every possible solution to the N queens problem. One solution per line, the solutions should not be printed in any order and only `sys` module can be imported.

## Tasks
* 0. N queens
- Usage: `nqueens N`
    If the user called the program with the wrong number of arguments, print `Usage:` `nqueens N`, followed by a new line, and exit with the status `1`
- where N must be an integer greater or equal to `4`
    If N is not an integer, print `N must be a number`, followed by a new line, and exit with the status `1`
    If N is smaller than `4`, print `N must be at least 4`, followed by a new line, and exit with the status 1
- The program should print every possible solution to the problem
    One solution per line
    Format: see example
    You don’t have to print the solutions in a specific order
- You are only allowed to import the `sys` module