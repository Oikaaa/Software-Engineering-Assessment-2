import math
import numpy as np

#-----------------------------------------------------------------------------------------------------------
def degreeToDMS(degree):
    x = degree - math.floor(degree)
    minutes = x * 60
    y = minutes - math.floor(minutes)
    second = y * 60
    return f"{math.floor(degree)}° {math.floor(minutes)}′ {round(second, 2)}′′"

#-----------------------------------------------------------------------------------------------------------
def pythagoras_hy():
    try:
        a = float(input("a side length: "))
        b = float(input("b side length: "))
        c = math.sqrt(a**2 + b**2)
        return c
    except:
        print("Invalid input, please try again.")

def pythagoras_side():
    try:
        a = float(input("a side length: "))
        c = float(input("c side length: "))
        b = math.sqrt(c**2 - a**2)
        return b
    except:
        print("Invalid input, please try again.")

def sine(option = None):
    try:
        option = str(input("What do you want to find? (Angle, Opposite, Hypotenuse)"))
        if option.lower().strip() == "angle":
            o = float(input("Opposite side length: "))
            h = float(input("Hypotenuse side length: "))
            angle = math.degrees(math.asin(o / h))
            convert = str(input("Do you want to convert the angle to DMS(Degree Minutes Second)? Y/N ")).upper().strip()

            if convert == "Y":
                return degreeToDMS(angle)
            else:
                return angle
        elif option.lower().strip() == "opposite":
            angle = float(input("Angle degree: "))
            h = float(input("Hypotenuse side length: "))
            o = math.sin(math.radians(angle)) * h
            return o
        elif option.lower().strip() == "hypotenuse":
            angle = float(input("Angle degree: "))
            o = float(input("Opposite side length: "))
            h = o / math.sin(math.radians(angle))
            return h
        else:
            return "Invalid option or no option has been chosen"
    except:
        print("Invalid input, please try again.")

def cosine():
    try:
        option = str(input("What do you want to find? (Angle, Adjacent, Hypotenuse)"))
        if option.lower().strip() == "angle":
            a = float(input("Adjacent side length: "))
            h = float(input("Hypotenuse side length: "))
            angle = math.degrees(math.acos(a/h))
            convert = str(input("Do you want to convert the angle to DMS(Degree Minutes Second)? Y/N ")).upper().strip()

            if convert == "Y":
                return degreeToDMS(angle)
            else:
                return angle
        elif option.lower().strip() == "adjacent":
            angle = float(input("Angle degree: "))
            h = float(input("Hypotenuse side length: "))
            a = math.cos(math.radians(angle)) * h
            return a
        elif option.lower().strip() == "hypotenuse":
            angle = float(input("Angle degree: "))
            a = float(input("Adjacent side length: "))
            h = a / math.cos(math.radians(angle))
            return h
        else:
            return "Invalid option or no option has been chosen"
    except:
        print("Invalid input, please try again.")

def cosineRule(option = None):
    try:
        option = str(input("What do you want to find? (Angle, Side)"))
        if option.lower().strip() == "side":
            #Find a side
            O = float(input("Angle degree (Opposite angle to the finding angle): "))
            b = float(input("b side length: "))
            c = float(input("c side length: "))
            a = math.sqrt(b**2 + c**2 - 2*b*c*math.cos(math.radians(O)))
            return  a
        elif option.lower().strip() == "angle":
            #Find an angle
            c = float(input("c side length (Opposite side to the finding angle): "))
            a = float(input("a side length: "))
            b = float(input("b side length: "))
            O = math.degrees(math.acos((a**2 + b**2 - c**2)/(2*a*b)))

            convert = str(input("Do you want to convert the angle to DMS(Degree Minutes Second)? Y/N ")).upper()
            if convert == "Y":
                return degreeToDMS(O)
            else:
                return O
        else:
            return "Invalid option or no option has been chosen"
    except:
        print("Invalid input, please try again.")

def sineRule():
    try:
        option = str(input("What do you want to find? (Angle, Side)"))
        if option.lower().strip() == "side":
            #Find a side
            b = float(input("Given side: "))
            B = float(input("Given angle for the side above: "))
            A = float(input("Give angle for the unknown side: "))
            a = b*math.sin(math.radians(A))/math.sin(math.radians(B))
            return a
        elif option.lower().strip() == "angle":
            #Find an angle
            a = float(input("Given side for the unknown angle: "))
            b = float(input("Given side: "))
            B = float(input("Give angle for the side above: "))
            A = math.asin(a*math.sin(B)/b)
            return A
        else:
            return "Invalid option or no option has been chosen"
    except:
        print("Invalid input, please try again.")

def square():
    try:
        l = float(input("Side length: "))
        return l**2
    except:
            print("Invalid input, please try again.")

def rectangle():
    try:
        w = float(input("Width: "))
        l = float(input("Length: "))
        return w*l
    except:
            print("Invalid input, please try again.")

def triangle():
    try:
        h = float(input("Height: "))
        b = float(input("Base: "))
        return h*b*0.5
    except:
            print("Invalid input, please try again.")

def trapezoid():
    try:
        a = float(input("a side: "))
        b = float(input("b side: "))
        h = float(input("Height: "))
        return ((a+b)*h)/2
    except:
            print("Invalid input, please try again.")

def parallelogram():
    try:
        h = float(input("Height: "))
        b = float(input("Base: "))
    except:
            print("Invalid input, please try again.")
    return h * b

def circle():
    try:
        r = float(input("Radius: "))
        return math.pi * r**2
    except:
            print("Invalid input, please try again.")

def linear():
    try:
        print("y = mx + c")
        m = float(input("m value: "))
        c = float(input("c value: "))
        return f"Gradient: {m} \n Y-Intercept {c} \n X-intercept {-c/m}"
    except:
            print("Invalid input, please try again.")

def quadratic():
    try:
        print("y = ax^2 + bx + c")
        a = float(input("a value: "))
        b = float(input("b value: "))
        c = float(input("c value: "))
        concave = None

        if a > 0 :
            concave = "up"
        elif a < 0:
            concave = "down"
        else:
            print("Seems like this is a linear function \n "
                "--------------------------------------------")
            return linear()

        x1 = (-b + math.sqrt(b**2 - 4*a*c))/2*a
        x2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / 2 * a

        vertex_x = -b/2*a
        vertex_y = a*vertex_x**2 + b*vertex_x**2 + c
        return f"The graph has a concave {concave} Y-Intercept {c} \n X-intercept {x1} and {x2} \n Vertex: ({vertex_x},{vertex_y})"
    except:
            print("Invalid input, please try again.")
    
def factorise_quadratic():
    try:
        print("y = ax^2 + bx + c")
        a = float(input("a value: "))
        b = float(input("b value: "))
        c = float(input("c value: "))

        if a == 0:
            print("Seems like this is a linear function \n "
                "--------------------------------------------")
            return linear()

        x1 = (-b + math.sqrt(b**2 - 4*a*c))/2*a
        x2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
        return f"Result: {"" if a == 0 else a}(x {"+" if x1 > 0 else "-"} {abs(x1)})(x {"+" if x2 > 0 else "-"} {abs(x2)})"
    except:
        print("Invalid input, please try again.")

def simultaneous_linear_equation():
    try:
        print("Equation 1: ax + by = c")
        a1 = float(input("a1 value: "))
        b1 = float(input("b1 value: "))
        c1 = float(input("c1 value: "))

        print("Equation 2: ax + by = c")
        a2 = float(input("a2 value: "))
        b2 = float(input("b2 value: "))
        c2 = float(input("c2 value: "))

        coefficients = np.array([[a1, b1],[a2, b2]])
        dependants = np.array([c1, c2])

        solution = np.linalg.solve(coefficients, dependants)
        return f"(They will cross each other at: {float(solution[0])}, {float(solution[1])})"
    except:
        print("Invalid input, please try again.")

#-----------------------------------------------------------------------------------------------------------
list = {
    1: pythagoras_hy,
    2: pythagoras_side,
    3: sine,
    4: cosine,
    5: sineRule,
    6: cosineRule,
    7: square,
    8: rectangle,
    9: triangle,
    10: trapezoid,
    11: parallelogram,
    12: circle,
    13: linear,
    14: quadratic,
    15: factorise_quadratic,
    16: simultaneous_linear_equation,
}

print("\\\\\\\\\\ ||   ||  || \\\\\\\\\\ \n"
      "\\\\\\\\\\ ||   ||  || \\\\\\\\\\ \n"
      "\\\\\\\\\\ ||===||  || \\\\\\\\\\ \n"
      "\\\\\\\\\\ ||   ||  || \\\\\\\\\\ \n"
      "\\\\\\\\\\ ||   ||  || \\\\\\\\\\ \n"
      "Welcome to The Math Calculator Software, please select an option from the list that you need help with. \n"
      "-------------Right Triangle------------- \n"
      "1. Hypotenuse using Pythagoras \n"
      "2. Side using Pythagoras\n"
      "3. Sine \n"
      "4. Cosine \n"
      "5. Sine Rule \n"
      "6. Cosine Rule \n"
      "-------------Area------------- \n"
      "7. Square  \n"
      "8. Rectangle \n"
      "9. Triangle \n"
      "10. Trapezoid \n"
      "11. Parallelogram \n"
      "12. Circle \n"
      "-------------Function------------- \n"
      "13. Linear (y = mx + c)\n"
      "14. Quadratic (y = ax^2 + bx + c) \n"
      "15. Factorise quadratic equation \n"
      "16. Simultaneous Linear Equation"
      )

while True:
    choice = int(input("Choose your function: "))

    if choice > len(list) or choice < 1:
        print("Invalid option")
    else:
        print(list[choice]())
        print("-------------------")