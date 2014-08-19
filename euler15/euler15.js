'use strict';

var cached = {};

function countRoutes(x,y,n) {
    var res1, res2;
    if (cached[x+"-"+y]) {
        return cached[x+"-"+y];
    } else if (cached[y+"-"+x]) {
        return cached[y+"-"+x];
    } else {
        if (x==n && y==n) {
            cached[x+"-"+y] = 1;
            return 1;
        } else if (x==n) {
            res1 = countRoutes(x,y+1,n);
            cached[x+"-"+y]=res1;
            return res1;
        } else if (y==n) {
            res1 = countRoutes(x+1,y,n);
            cached[x+"-"+y]=res1;
            return res1;
        } else {
            res1 = countRoutes(x+1,y,n);
            res2 = countRoutes(x,y+1,n);
            cached[x+"-"+y]=res1+res2;
            return res1+res2;
        }
    }
}

function findRoutes(n) {
    var routes = 0;
    var choices = [[0,0]];
    
    // x = left / right, y = up / down
    var x, y, start;
    do {
        start = choices.pop();
        x = start[0], y = start[1];
        do {
            if (x===n) {
                // On the right edge, can't continue right
                y=y+1;
            } else if (y===n) {
                // On the bottom edge, can't continue down
                x=x+1;
            } else {
                // Somewhere in the middle
                // Choose to go right, but add the down choice to explore later
                choices.push([x,y+1]);
                x=x+1;
            }
        } while (x < n || y < n);
        routes=routes+1;
    } while (choices.length > 0);
    
    return routes;
}

console.log(findRoutes(10));
console.log(countRoutes(0,0,20));