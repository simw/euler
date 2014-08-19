"use strict";

var _ = require('underscore');

function generate_primes(nmax) {
    var primes = [2,3];
    var isprime = true;

    for (var i=5; i<nmax; i+=2) {
        isprime = true;
        
        for (var x=0; x<primes.length; x++) {
            if (i % primes[x] == 0) {
                isprime = false; break;
            }
        }

        if (isprime) {
            primes.push(i);
        }
        
        if (i%100000 == 1) {
            console.log("Generate primes up to " + i);
        }
    }
    
    return primes;
}

function largest_prime_factor(n) {
    var primes = generate_primes(n/2);
    
    for (var i=primes.length; i>=0; i--) {
        if (n % primes[i] == 0) {
            return primes[i];
        }
    }
    
    return n;
}
// 600851475143
console.log(largest_prime_factor(100000000));