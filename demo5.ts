
/*
var num1:number =5;
var fac:number=1;

while(num1>=1){
    fac=fac*num1
    num1--;
}
console.log("The factorial is "+fac);

////////////////////////////////////////////////////////////////////////
var num1:number=5;
var num2:number=1;
while(num2<11){
    console.log(num1*num2);
    num2++;
}
//////////////////////////////////////////////////////////////////////////

var n:number=10;
do{
    console.log(n);
    n--;
}while(n>=0)


/////////////////////////////////////////////////////////////////
var num1:number=1;
do{
    if(num1%2==0){
        console.log(num1);
        num1++;
    }
    else{
        num1++;
    }
}while(num1<101)

////////////////////////////////////////////////////////////////////////
var num:number=5;
var i:number;
var fac=1;
for(i=num;i>=1;i--)
{
    fac*=i;
}
console.log(fac);

/////////////////////////////////////////////////////////////////////////////

var j:any;
var n:any="abc"

for(j in n){
    console.log(n[j]);
}

/////////////////////////////////////////////////////////////////////////
var a1:number=1;
var i:number;
for(i=0;i<50;i++){
    if(i!=20){
        console.log(i);
    }
    else{
        break;
    }
}
////////////////////////////////////////////////////////////////////////////////
class Pradip1 {
    static pradip(num: number, name: string, mail_id?: string) {
        console.log("ID:" + num);
        console.log("Name:" + name);
        if (mail_id) {
            console.log("Email id:" + mail_id);
        }
    }
}

Pradip1.pradip(64, "Pradip");

//////////////////////////////////////////////////////////////////////////
// Function to add two numbers
function add(a: number, b: number)
  {
    return a + b;
  }
  console.log("Sum:", add(3, 7));


function addnum(...nums:number[])
{
    var i;
    var sum:number=0;
    for(i=0;i<nums.length;i++){
        sum=sum+nums[i];
    }
    console.log("Sum of the numbers is "+sum);

}

addnum(1,2,3,4);


///////////////////////////////////////////////////////////////////////////////
function cal(price:number,rate:number=0.50){
    var dis=price*rate;
    console.log("Discount amount is:" +dis);
}
cal(10);
cal(1000,0.30);

*********************************************************************************


var msg=function(){
    return "Hello World";
}
console.log(msg());

***************************************************************************

var str2:string="Hello World";
console.log(str2.length);
*****************************************************************************
*/

