# i od 0 do 3 (4 ne obuhvata)
i = range(4)
print(list(i))    # [0, 1, 2, 3]

# ispisuje praznu listu ako je opseg 0 ili negativan
i = range(-4)
print(list(i))    # []

# i from 2 to 4 (5 ne obuhvata)
i = range(2, 5)
print(list(i))    # [2, 3, 4]

# i od -2 to 3 (4 ne obuhvata)
i = range(-2, 4)    
print(list(i))    # [-2, -1, 0, 1, 2, 3]

#  ispisuje praznu listu ako se ne stavi negativan korak
i = range(4, 2) 
print(list(i))    # []

#i od 2 do 10 sa korakom 3 
i = range(2, 10, 3)
print(list(i))    # [2, 5, 8]

# i od 4 to -1 sa korakom -1
i = range(4, -1, -1)    
print(list(i))    # [4, 3, 2, 1, 0]

# i od 1 do 4 sa korakom 1
# range(0, 5, 1) i range(5)
i = range(0, 5, 1) 
print(list(i))    # [0, 1, 2, 3, 4]
