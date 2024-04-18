def s_u_h (s):
  return (s//3600 ,s%3600//60, s%60 )
s = int(input("Unesi sekunde: "))  
(h , m , s ) = s_u_h (s)
print(  "sati=", h, "h,", "min = ", m, "min,", "sec=", s, "s")
