// SPDX-License-Identifier: MIT

pragma solidity ^0.8.13;

contract SimpleStruct {
    struct Simple {
        int a;
        int b;
    }

    struct Complex {
        string x;
        Simple y;
        bool z;
    }

    Simple simple;
    Complex complex;

    function addSimple(Simple memory _simple) public {
        simple = _simple;
    }

    function addComplex(Complex memory _complex) public {
        complex = _complex;
    }

    function seeSimple() public view returns(Simple memory) {
        return simple;
    }

    function seeComplex() public view returns(Complex memory) {
        return complex;
    }

}