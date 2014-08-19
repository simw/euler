'use strict';

function createArray() {
    var arr = (function(n,arr) {
        while (n--) {
            arr[n] = n+1;
        } 
        return arr;
    })(100, []);
    return arr;
}

function getResult() {
    var arr = createArray();
    
    var arrSquare = arr.map(function(value) {
        return value * value;
    });
    
    var res1 = arrSquare.reduce(function(total, value) {
        return total + value;
    });
    
    var res2 = arr.reduce(function(total, value) {
        return total + value;
    });
    res2 = res2*res2;
    
    return [res1, res2];
}

var res = getResult();
console.log(res);
console.log(res[1]-res[0]);