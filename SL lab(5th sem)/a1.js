function isNum(str)
{
  var n=Math.floor(Number(str));
  return String(n) === str && n>0;
}

function getResult()
{
  var n=document.getElementById("no").value;
   var result=0;
  if(isNum(n))
   {
      if(n%3==0 && n%7==0)
        result="Divisible by both 3 and 7";
      else if(n%3==0)
        result="Divisible by 3";
      else if(n%7==0)
        result="Divisible by 7";
      else
        result="Neither divisible by 3 nor 7";
  }
 else
   alert("Enter a valid number");

document.getElementById("res").value=result;

}
