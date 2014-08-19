'use strict';

function checkFactors(n) {
    var nums = [20,19,18,17,16,15,14,13,12,11];
    
    var divisible = true;
    for (var i=0; i<nums.length; i++) {
        if (n % nums[i] != 0) {
            divisible = false;
            break;
        }
    }
    
    return divisible;
}

function findNumber() {
    var i=0, found=false;
    do {
        i=i+1;
        found = checkFactors(i*20);        
    } while (!found);
    
    return i*20;
}

console.log(findNumber());