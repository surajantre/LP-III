// SPDX-License-Identifier: MIT
pragma solidity >=0.8.0;

contract PassStudentMarks{
    uint[10] public marks;

    function acceptMarks(uint[] memory _marks) public {
        //require(_marks.length == 10, "Array size must be 10");

        uint i = 0;
        do {
            require(_marks[i] >40, "WE accept marks of only pass students");
            require(_marks[i] <=100, "Accept only valid marks");
            marks[i] = _marks[i];
            i++;
        } while (i < _marks.length);
    }
    //Function to get the marks
    function getMarks() public view returns (uint[10] memory) {
        return marks;
    }
}
