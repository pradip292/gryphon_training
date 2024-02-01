var global_num=12 //global variable

class Numbers{
    num_val=13; //class varible
    static sval=10; //static field

    storeNum():void{
        var local_num=14; //local varible
    }
}

console.log("Global num:"+ global_num)
console.log(Numbers.sval) // static variable
var obj =new Numbers();
console.log("Global num:"+obj.num_val)