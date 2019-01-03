function isNum(str1,str2)
{
  n1=Math.floor(Number(str1));
  n2=Math.floor(Number(str2));
  return String(n1) === str1 && n1>=0 && String(n2) === str2 && n2>=0;
}

function getResult()
{
  var isadd=document.getElementById("add1").checked;
  var issub=document.getElementById("sub1").checked;
  var ismul=document.getElementById("mul1").checked;
  var isdiv=document.getElementById("div1").checked;
  var result=0;
  var n1=document.getElementById("no1").value;
   var n2=document.getElementById("no2").value;
 if(isNum(n1,n2))
  {
    if(isadd)
     result=n1-(-n2);
    else if(issub)
     result=n1-n2;
    else if(ismul)
     result=n1*n2;
    else if(isdiv && n2>0)
     result=n1/n2;
    else
      alert("Divide by zero error");
 }
 else
   alert("enter a valid number");
document.getElementById("res").value=result;
}
   
