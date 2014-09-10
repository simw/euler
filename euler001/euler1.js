
function is_multiple(num, divs) {
    'use strict';
    for (var i=0; i<divs.length; i++) {
        if (num % divs[i] === 0) {
            return true;
        }
    }
    return false;
}

function euler1(nmax, divs) {
    'use strict';
    var total = 0;

    for (var i=1; i<nmax; i++) {
        if (is_multiple(i, divs)) {
            total = total + i;
        }
    }

    return total;
}

console.log(euler1(1000, [3, 5]));
