"use strict";

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
            console.log("Generated primes up to " + i + ", count " + primes.length);
        }
    }
    
    return primes;
}

var res = generate_primes(500000);
console.log(res[0] + " " + res[10000]);
