/*
var num1:number=9;
if(num1>0){
    console.log("NUmber is positive")
}else{
    console.log("-ve number")
}
*/


function isLeapYear(year: number): boolean {
    if (year % 4 === 0) {
        // If divisible by 4
        if (year % 100 === 0) {
            // If divisible by 100
            return year % 400 === 0; // Leap year if divisible by 400
        }
        return true; // Leap year if not divisible by 100
    }
    return false; // Not divisible by 4
}

// Example usage
const yearToCheck = 2024;
if (isLeapYear(yearToCheck)) {
    console.log(`${yearToCheck} is a leap year.`);
} else {
    console.log(`${yearToCheck} is not a leap year.`);
}
