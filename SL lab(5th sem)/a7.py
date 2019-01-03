def AtomicDictionary():
  d={"B":"Boron","S":"sulphur","He":"Helium"};
  print(d);
  new_sym=input("Enter a symbol: ");
  new_ele=input("Enter Element: ");
  if(new_sym not in d.keys()):
    print("added to dict");
  else:
    print("The key exists and hence value is replaced");
  d[new_sym]=new_ele;
  print(d);
  print("The no. of elements: ",len(d));
  ele=input("enter  a element to check its existance: ");
  if ele not in d.keys():
    print("element not found");
  else:
    print(d[ele]);
