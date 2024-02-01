var Calculations = /** @class */ (function () {
    function Calculations() {
    }
    Calculations.prototype.add = function () {
        var num1 = 2;
        var num2 = 1;
        var addition = 0;
        addition = num1 + num2;
        console.log(addition);
    };
    Calculations.prototype.sub = function () {
        var num1 = 2;
        var num2 = 1;
        var subtract = 0;
        subtract = num1 - num2;
        console.log(subtract);
    };
    Calculations.prototype.mult = function () {
        var num1 = 2;
        var num2 = 1;
        var multiply = 0;
        multiply = num1 * num2;
        console.log(multiply);
    };
    Calculations.prototype.div = function () {
        var num1 = 2;
        var num2 = 1;
        var divide = 0;
        divide = num1 / num2;
        console.log(divide);
    };
    return Calculations;
}());
var obj = new Calculations();
obj.add();
var obj = new Calculations();
obj.sub();
var obj = new Calculations();
obj.mult();
var obj = new Calculations();
obj.div();
