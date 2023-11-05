// SPDX-License-Identifier: MIT
pragma solidity >=0.8.0;

contract Array{
    uint[] public arr;
    uint sum=0;
    //Function to accept array element
    function acceptArray(uint[] memory _arr)public {
        arr=_arr;
    }    
    //Function to display array element
    function display()public view returns(uint[] memory){
        return arr;
    }
    //Function to add array element
    function sumOfArrayEle()public{
        for(uint i=0;i<arr.length;i++){
            sum+=arr[i];
        }
    }
    //Function to display sum of array element
    function sumIs()public view returns(uint){
         return sum;
    }
}