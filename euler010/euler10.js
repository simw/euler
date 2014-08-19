"use strict";

function createArray(len) {
    var arr = (function(n,arr) {
        while (n--) {
            arr[n] = n+1;
        } 
        return arr;
    })(len, []);
    return arr;
}

function removeAllMultiples(n, arr) {
    var max = arr.length;
    var i=2*n;
    
    do {
        arr[i-1]=0;
        i=i+n;
    } while (i<max+1);
    
    return arr;
}

var num = 2000000;
var arr=createArray(num);

var i;
arr[0] = 0;
for (i=2; i<num/2+1; i++) {
    if (arr[i-1] != 0) {
        arr = removeAllMultiples(i,arr);
    }
}

var res = arr.reduce(function(total, value) { return total+value; });

console.log(res);