function get(){
 var sentence=document.getElementById("text1").value;
 var array1=sentence.match(/\w[a-z]{0,}/gi);
 var result=array1[0];
 for(var i=1;i<array1.length;i++)
  {
    if(result.length<array1[i].length)
      result=array1[i];
  }
 var l=result.length;
 document.getElementById("res1").value=result;
 document.getElementById("res2").value=l;
}
