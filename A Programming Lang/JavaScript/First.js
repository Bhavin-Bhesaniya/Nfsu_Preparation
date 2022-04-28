/*
<script>

    document.write("Print data on screen\n");
    console.log("Print Data on Console");
    //console Property
    console.info("Information");
    console.time("test");
    console.table(["b", 1, "c", 'd']);//(var.key for )
    console.error("wrong");
    console.warn("warning");
    console.timeEnd("test");
    // console.clear();

    Box property/window :-
    alert("To majamane")
    confirm("are you hacker");
    Unm = prompt("Enter name");
    document.write(Unm);



    Variable:-
    var FirstVar = "bhavin";
    let SecondVar = 10;
    const FixedVar = 10;
    var ConvertVarType = String(SecondVar); / SecondVar.toString();
    Number(Var) / parseInt(var) / parseFloat(var);

    var a = "hi ";          //global variable
    function aa() {
        document.write(a);
        var b = "ya ";      //local variables
        }
    aa();
    document.write(b);



   Operators :-
   arithmatic operators :- +,-,*,/,%,++,--,**
   comparison operators :-==,===,!=,!==,>,<,>=,<=,null/undefined
   logical operators :- && , || , !
   ternary operators :- condtion ? true : false;
  

    
    Datatype :- Dynamic typed language
    primitive :- stack(number,string("",'',new String(construtor)),boolean,null(return object),undefined(create variable without value))
    Reference :- heap (Array,Object,Date(new date()),function,set,map etc..)all return object type / store address
    var ArrayO = ["bhavin", "bhesaniya"];
    var ObjedtYe = {   name1 : "bhavin", surn  : "bhesaniya", };
    document.write(typeof ArrayObj);//show datatypes of var

    
    Numbers :-
    var a = "99";
    var a1 = 99.9978;
    var c = Number(a);
    var c1 = parseInt(a1);
    var c2 = parseFloat(c);
    var c3 = isFinite(a1);
    var c4 = Number.isInteger(a1);
    var c5 = a1.toFixed(2);
    var c6 = a1.toPrecision(3);


    //String Example :- console.log('sum of ${a} and ${b} is ${c}');
    = s.length; //property
    = s.concat(" ",s1);
    = s.charAt(indexNo);
    = s.indexOf(entercharacter);
    = s.lastIndexOf(entercharacter);
    = s.toUpperCase();
    = s.toLowerCase();
    = s.substring(start,end);
    = s.split(" ");     
    = s.trim();
    = s1.localCompare(s2);  //greater return 1
    = s.replace("oldword","new word");
    = s.repeat(value);
    = s.slice(start,end);
    = s.substr();
    = s.includes(value);    // return true / false
    = s.search(value);      // return index no
    = String.fromCharCode("A");
    = s.match(/bh/g);       //return array  
    s.startwith("string");
    s.endwith("string");
    s.charCodeAt(0);
   

    Array :-
    var FirstArray = [10, 20, 30];  //single dimensional
    var ArrayMethod = new Array();
    var MultiDimensionalArray = [ [10, 20, 30], [40, 50, 60] ];
    document.write(FirstArray); 
    // (FirstArray[1]); specific value 

    FirstArray[0] = 10.10;   //Modify Value
    delete FirstArray[2];    //Delete Value


    //Array Methods
    a.sort();   
    a.reverse();
    a.pop();        //Remove last element
    a.shift();      //delete first value
    a.unshift();    //enter at first position
    a.push();       //enter at last position
    = a.concat(Value); 
    = a.join(space);   
    = a.slice(0,1);               //slice array (start,end(-)last)
    a.splice(pos,n); //splice array(start,howmany,new)
    = Array.isArray(a);
    = a.indexOf(10,2);            //(searchitem,startno) -1 if not found
    = a.lastIndexOf(30,2);        //(searchitem,startno) -1 if not found
    = a.includes(10) ;            //search item in array -1 if not found
    = a.some(function);           //check one value return true/false
    = a.each(function);           //check all value return true/false
    = a.find(function);           //check firstvalue
    = a.findIndex(function);      //check firstvalueIndex
    = a.filter(che);              //check value if bigger than compare value or not
    a.toString;
    a.fill(100);                  //fill all values with 100
    a.valueOf();
    a.forEach(function (value, inn))    //print value with index number
    = a.map(test);                      //print array of object
  
    var forIn =
    {
        fName: "bhavin",
        lName: "bhesaniya",
        array: ['bf', 'sh', 'gg'],
        objinobj: {city: 'junagadh' },
        functi: function () { return 55; },
    };
    forIn.foreach(function(item,index)
    {
        console.log(index , " => " + item);
    });
    


    Function :-
    function FunName()      //u can pass arguments  / pass default value also
    {
        //code
        //u can return value
    }
    FunName(); Function call
    function()  //Function without name anonmyous
    { //code }
   
    //ArrowFunction :
    const ArrowFun = (ArgumentHere)=>{ //code };
    ArrowFun();
    ()=>{ }     //Arrow Function without name anonmyous throgh 
  
 

    Condition and loop :-
       if           
       else if
       if else
       //False value by default :- 0,false,"empty string",undefined,null,Nan

       1)for        :- for(initalization; condition; ++/--) { //code }
       2)do..while  :- do( //code )while(condition)
       3)while      :- while(condition) { //code }
       4)for..in    :- 
       5)for..of
       switch..case
       break and continue
      
       //for in example :-  
       for (var key in ObjName) //object name       
       {  document.write('${key} => ${ObjName[key]}');  }
        //when use (for in) we get index & value but when use (for of) loop we directly get value of iterable object
        //for of note travsal object


    Objects :-
    - Looks like a collection of key value pairs
    var objConstrcutor = new Object();
    var Obj ={ fName: "bhavin",
               "id" : 10,
               mov : [ 'bf', 'sh', 'gg' ],
               b   : { city: 'junagadh' },
               dis : function () { return 55; },
               ful : function () { return this.fName + "  " + this.lName; }
            };
    
     //Type of access object value
     console.log(Obj);   //print(Obj)
     Obj.fName;           
     Obj[id];   
     Obj.dis();     //Print object function
     Obj["dis"]();  //Print object function
     Also use for loop
     
     //Modify Value
     Obj.fName = "BHAVIN";

     //Add new property
     Obj["NewPropertyName"] = Value;

     //Delete property
     delete Obj.id;

     //Array of objects
        var d = [
            { Name: 'bhavin', age: 10 },
            { Name: 'bhavine', age: 11 },
            { Name: 'bhavie', age: 12 }];
        
        console.log(d);
        
        for (e = 0; e < d.length; e++) {
            document.write(d[e].Name + "  " + d[e].age + " <br> ");
        }
     
        
    Document Object Model(DOM) :-
    - Platform and language independent model representation of html and xml document
    - Wihtout refresh page and generate dynamic output
    - Define logical structure of the document 
    - All element and attribute are organized in a hierchical tree-like structure
    - Individual part is known as nodes



    Date :-
    Var DateObj = new Date();
    a.setDate(23); /setFullYear(2021); / setMonth(4); / setHours(14); / setSeconds(10); / setMilliseconds(111);
    a.toDateString / getDate / getFullYear() / getMonth / getDate() / getHours / getMinutes() / getSeconds() / getMiliseconds() 


    Event :-
   
    onclick / ondbclick / oncontextmenu / onmouse,enter,out,down,up / 
    key,press,up / onload / onunload / onresize / onscroll
    Add a body tag fire event throgh function






</script>
*/