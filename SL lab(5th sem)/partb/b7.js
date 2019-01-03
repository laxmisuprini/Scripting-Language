window.onload=function()
{
  var vehdetails=[
  {
   "name":"Car",
   "model":"Maruthi",
   "price":75000,
   "year":1997
  },
   {
   "name":"Bike",
   "model":"pulsar",
   "price":55000,
   "year":2014
  },
  {
   "name":"Cycle",
   "model":"Herculus",
   "price":5500,
   "year":2017
  }];

vehdetails.forEach(function(item,index)
 {
   listEle=document.createElement("th")
   listEle.id=item.model
   listEle.innerHTML=item.name
   document.getElementById("menu").appendChild(listEle)
 })

vehdetails.forEach(mouseOverHandler);
function mouseOverHandler(item,index)
{
  var ele=document.getElementById(item.model);
  ele.onmouseover=function()
 {
   var details=item;
   if(details!=null)
  {
    document.getElementById("data-table").removeAttribute("hidden");
    document.getElementById("name").innerHTML=details.name;
    document.getElementById("model").innerHTML=details.model;
    document.getElementById("price").innerHTML=details.price;
    document.getElementById("year").innerHTML=details.year;
 }
}
}
} 

