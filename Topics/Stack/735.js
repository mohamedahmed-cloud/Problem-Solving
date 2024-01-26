"use strict";
function asteroidCollision(asteroids) {
    let stack = [];
    for (let i of asteroids) {
        let flag = true, last = stack.slice(-1)[0];
        while (stack.length > 0 && checkSameSign(last, i) && last >= 0) {
            flag = false;
            last = stack.slice(-1)[0];
            if (Math.abs(last) < Math.abs(i))
                stack.pop();
            else if (Math.abs(last) == Math.abs(i)) {
                stack.pop();
                break;
            }
            else
                break;
            flag = true;
            last = stack.slice(-1)[0];
        }
        if (flag)
            stack.push(i);
    }
    // console.log(stack)
    return stack;
    function checkSameSign(num1, num2) {
        if ((num1 >= 0 && num2 >= 0) || (num1 < 0 && num2 < 0))
            return false;
        return true;
    }
}
;
let asteroids = [-2, -2, 1, -2];
console.log(asteroidCollision(asteroids));
