var _ = require('underscore');

var sum = function(array) {   
    return array.reduce(function(a,b) { return a+b; }, 0);
}

var fibonacci_generator = function(max_number) {
    var result = [];
    var current_index;
    result.push(1);
    result.push(2);
    current_index = 2;
    
    do {
        result.push(result[current_index-1] + result[current_index-2]);
        current_index++;
    } while (result[current_index-1] < max_number);
    result.pop();
    
    return result;
}

function euler2() {
    var fibs = fibonacci_generator(4e6);
    fibs = fibs.map(function(x) { if (x%2 == 0) { return x; } else { return 0; } });
        
    return sum(fibs);
}

console.log(euler2());