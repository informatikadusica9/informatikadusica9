def m_u_km (m):
  return (m//1000, m%1000)


m = int(input("Unesi metre: "))

(km, m) = m_u_km(m)
print(  "km=", km,  "m = ", m)
