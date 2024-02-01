class Calculations{

    add():void{
    let num1:number=2;
    let num2:number=1;
    let addition:number=0;
    addition=num1+num2;
    console.log(addition);
    }
      
    sub():void{
        let num1:number=2;
        let num2:number=1;
        let subtract:number=0;
        subtract=num1-num2;
        console.log(subtract);
        }

        mult():void{
            let num1:number=2;
            let num2:number=1;
            let multiply:number=0;
            multiply=num1*num2;
            console.log(multiply);
            }


            div():void{
                let num1:number=2;
                let num2:number=1;
                let divide:number=0;
                divide=num1/num2;
                console.log(divide);
                }






}
var obj=new Calculations();
obj.add();

var obj=new Calculations();
obj.sub();

var obj=new Calculations();
obj.mult();

var obj=new Calculations();
obj.div();