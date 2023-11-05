// SPDX-License-Identifier: MIT
pragma solidity >=0.4.0;

contract AddSubMulDiv{
    uint public num1;  // Make num1 and num2 public to enable inspection.
    uint public num2;

    constructor(uint _num1, uint _num2) {
        num1 = _num1;
        num2 = _num2;
    }

    function add() public view returns (uint) {
        return num1 + num2;
    }

    function sub() public view returns (uint) {
        require(num1 >= num2, "Subtraction underflow");
        return num1 - num2;
    }

    function mul() public view returns (uint) {
        return num1 * num2;
    }

    function div() public view returns (uint) {
        require(num2 != 0, "Division by zero");
        return num1 / num2;
    }
}
