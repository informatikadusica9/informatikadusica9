def kilometri_u_metre(m):
    return (m // 1000, m % 1000)


(km, m) = kilometri_u_metre (2553)
print(2553, "m = ", km, "km i", m, "m")

