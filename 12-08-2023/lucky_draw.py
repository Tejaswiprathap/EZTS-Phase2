'''lucky draw   colors:red,black,white,green
numbers:1,2,3,4   shapes:spade,club,diamond,heart
(black,4,spade) wins lucky draw'''

print("=====WELCOME TO THE LUCKY DRAW=====")
colors=['red','black','white','green']
numbers=['1','2','3','4']
shapes=['spade','diamond','heart','club']
print(colors)
print(numbers)
print(shapes)
a=input("Choose a color: ")
b=input("Choose a number: ")
c=input("Choose a shape: ")
if a=='black' and b=='4' and c=='spade':
    print("CONGRATULATIONS,YOU WON THE LUCKY DRAW")
elif a=='red' and b=='3' and c=='spade':
    print("CONGRATULATIONS,YOU WON THE LUCKY DRAW")
else:
    print("BETTER LUCK NEXT TIME")
