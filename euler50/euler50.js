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

function createPrimeArray(max) {
    var arr = createArray(max);

    var i;
    arr[0] = 0;
    for (i=2; i<max/2+1; i++) {
        if (arr[i-1] != 0) {
            arr = removeAllMultiples(i,arr);
        }
    }
    
    arr = arr.filter(function(val) {
        return (val!=0);
    });
    
    return arr;
}

var arr = createPrimeArray(1000);

var sum = 0;
var sums = arr.map(function(val) {
    sum = sum + val;
    return sum;
});



console.log(sums);
