"use strict";

/*
 * Largest palindrome that is product of 2 three digit numbers
 * 
 * Minimum 10,000 (100^2); maximum 998,001 (999^2)
 * 
 * 
 * 
 * 
 */

function isPalindrome(num) {
    var str = '' + num;
    var res = true;
    for (var i=0; i<str.length/2; i=i+1) {
        if (str[i] !== str[str.length-i-1]) {
            res = false;
            break;
        }
    }
    
    return res;
}

function isPalindrome2(str) {
    str = '' + str;
    
    return (str.length <=1) || 
        ((str[0] === str[str.length-1]) && isPalindrome2(str.splice(1,str.length-2)));
}

function findPalindromes(min, max) {
    var list = [];
    
    for (var i=max; i>=min; i--) {
        for (var j=max; j>=i; j--) {
            if (isPalindrome(i*j)) {
                list.push([i*j, i, j]);
                //return [i*j, i, j];
            }
        }
    }
    list.sort(function(a,b) { return (b[0]-a[0]); });
    return list.slice(0,20);
}

//console.log(isPalindrome(99999));
//console.log(isPalindrome2(99999));
console.log(findPalindromes(100,999));