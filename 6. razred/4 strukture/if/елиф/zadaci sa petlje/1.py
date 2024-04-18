print("Unesite 3 para brojeva (svaki par u novom redu):")
for i in range(3):
    x1, y1 = map(float, input().split())  # Unosimo prvi par brojeva
    x2, y2 = map(float, input().split())  # Unosimo drugi par brojeva
    parovi.append((x1, y1))
    parovi.append((x2, y2))

print("Uneti parovi su:")
for par in parovi:
    print(par[0], par[1])
