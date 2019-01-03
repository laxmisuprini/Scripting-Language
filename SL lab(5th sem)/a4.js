function isNum(str)
{
 var n=Math.floor(Number(str));
 return String(n) === str && n>0;
}

function get1()
{
 var no=document.getElementById("no").value;
 var result=0;
 if(isNum(no))
  {
    result=no*2;
  }
 else
  alert("Enter a valid number");
 document.getElementById("res").value=result;
}


function get2()
{
 var no=document.getElementById("no").value;
 var result=0;
 if(isNum(no))
  {
    result=no*no;
  }
 else
  alert("Enter a valid number");
 document.getElementById("res").value=result;
}
