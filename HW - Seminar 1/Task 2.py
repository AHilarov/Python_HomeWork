# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# для всех значений предика

for x in range(2):
    for y in range(2):
        for z in range(2):
            if not(x or y or z)== (not(x) and not(y) and not(z)):
                print (x,y,z)

# ((x ∧ ¬y) ≡ (z ∨ ¬w)) → (x ∧ z).
# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 # if not(not(not(x and not (y)) == (z or not (w))) or (x and z)):
#                     if not(((x and not(y)) == (z or not(w))) <= (x and z)):
#                         print (x,y,z, w)
