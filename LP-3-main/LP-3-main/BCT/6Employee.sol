// SPDX-License-Identifier: MIT
pragma solidity >=0.8.0;

contract EmployeeDetails {
    // Define a structure for employee details
    struct Employee {
        uint256 id;
        string name;
        uint256 salary;
        uint256 joiningDate;
    }

    // Declare a mapping to store employee details by their ID
    mapping(uint256 => Employee) public employees;

    // Function to add an employee's details
    function addEmployee(uint256 _id, string memory _name, uint256 _salary, uint256 _joiningDate) public {
        Employee memory newEmployee = Employee(_id, _name, _salary, _joiningDate);
        employees[_id] = newEmployee;
    }

    // Function to retrieve an employee's details
    function getEmployeeDetails(uint256 _id) public view returns (uint256, string memory, uint256, uint256) {
        Employee memory employee = employees[_id];
        return (employee.id, employee.name, employee.salary, employee.joiningDate);
    }
}
