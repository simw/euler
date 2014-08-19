var _ = require('underscore');

var sum = function(array) {   
    return array.reduce(function(a,b) { return a+b; }, 0);
}

function is_divisible(x) {
    if (x%3 == 0 || x%5 == 0) {
        return x;
    } else {
        return 0;
    }
}

function euler1() {
    var nmax = 1000;
    
    var ns = _.range(1, nmax);
    ns = ns.map(is_divisible);
        
    return sum(ns);
}

console.log(euler1());