def Loops_Lesson():
    math_user_inp=int(input("Pick from these options:\n 1:addition \n 2:subtraction \n 3:multiplication \n 4:division \n 5:modulus\n 6:exponential\n option: "))
    if math_user_inp == 1:
        print("\nAddition in python utilizes the + operator to  add")
        print("Ex:5+22=27")
        print("\nTry it yourself")
        while True:
            print("x+8=15")
            addition_input=int(input("pick the number that would add to 15 to see if it works: "))
            addition_equation= addition_input+8
            if addition_equation != 15:
                print("try again and make sure its a number that adds to 15")
            elif addition_equation == 15:
                print("\nWell done, you have succesfully understood how the addition operator is used!!")
                lesson_learned_option=int(input("\nPick from these options:\n 1:Learn more about the math operators,\n 2:go to the home page,\n 3:Exit the application"))
                learned_option(lesson_learned_option)
                '''if lesson_learned_option == 1:
                    Math_op_Lesson()
                elif lesson_learned_option == 2:
                    home_page()
                elif lesson_learned_option == 3:
                    sys.exit()'''
    
    elif math_user_inp == 2:
        print("\nSubtraction in python utilizes the - operator to subtract")
        print("Ex:13-5=8")
        print("\nTry it yourself")
        while True:
            print("21-x=9")
            subtraction_input=int(input("pick the number that would subtract from 21 to be 9 to see if it works: "))
            subtraction_equation= 21-subtraction_input
            if subtraction_equation != 9:
                print("try again and make sure its a number that subtracts to 9")
            elif subtraction_equation == 9:
                print("\nWell done, you have succesfully understood how the subtraction operator is used!!")
                lesson_learned_option=int(input("\nPick from these options:\n 1:Learn more about the math operators,\n 2:go to the home page,\n 3:Exit the application"))
                if lesson_learned_option == 1:
                    Math_op_Lesson()
                elif lesson_learned_option == 2:
                    home_page()
                elif lesson_learned_option == 3:
                    sys.exit()
        
    
    elif math_user_inp == 3:
        print("\nMultiplication in python utilizes the * operator to multiply")
        print("Ex:6*4=24")
        print("\nTry it yourself")
        while True:
            print("x*7=21")
            multiplication_input=int(input("pick the number that would multiply by 7 to be 21: "))
            multiplication_equation= multiplication_input * 7
            if multiplication_equation != 21:
                print("try again and make sure x is a number that multiplies to 21")
            elif multiplication_equation == 21:
                print("\nWell done, you have succesfully understood how the multiplication operator is used!!")
                lesson_learned_option=int(input("\nPick from these options:\n 1:Learn more about the math operators,\n 2:go to the home page,\n 3:Exit the application"))
                if lesson_learned_option == 1:
                    Math_op_Lesson()
                elif lesson_learned_option == 2:
                    home_page()
                elif lesson_learned_option == 3:
                    sys.exit()      

    elif math_user_inp == 4:
        print("\nDivision in python utilizes the / operator to divide")
        print("Ex:15/5=3")
        print("\nTry it yourself")
        while True:
            print("27/x=9")
            division_input=int(input("pick the number that would divide 27 by x into 9: "))
            division_equation= 27 / division_input 
            if division_equation != 3:
                print("try again and make sure its a number that the number multiplies to 21")
            elif division_equation == 3:
                print("\nWell done, you have succesfully understood how the division operator is used!!")
                lesson_learned_option=int(input("\nPick from these options:\n 1:Learn more about the math operators,\n 2:go to the home page,\n 3:Exit the application"))
                if lesson_learned_option == 1:
                    Math_op_Lesson()
                elif lesson_learned_option == 2:
                    home_page()
                elif lesson_learned_option == 3:
                    sys.exit()

    elif math_user_inp == 5:
        print("\nModulus in python utilizes the %" +  "to find the remainder")
        print("Ex:15%20=5")
        print("\nTry it yourself")
        while True:
            print("12%" + "x=2")
            modulus_input=int(input("pick the number that when divided by x will result in a remainder of 2: "))
            modulus_equation= 12 % modulus_input
            if modulus_equation != 2:
                print("try again and make sure x divides into 12 to get a remainder of 2")
            elif modulus_equation == 2:
                print("\nWell done, you have succesfully understood how the modulus operator is used!!")
                lesson_learned_option=int(input("\nPick from these options:\n 1:Learn more about the math operators,\n 2:go to the home page,\n 3:Exit the application"))
                if lesson_learned_option == 1:
                    Math_op_Lesson()
                elif lesson_learned_option == 2:
                    home_page()
                elif lesson_learned_option == 3:
                    sys.exit()          

    elif math_user_inp == 6:
        print("\nExponential in python utilizes the ** operator to raise the power")
        print("Ex:4**3=64")
        print("\nTry it yourself")
        while True:
            print("3**x=27")
            exponential_input=int(input("pick the number that when raised to the power of x will result in 27: "))
            exponential_equation= 12 % exponential_input
            if exponential_equation != 3:
                print("try again and make sure x can be raised to the power that will yield 27")
            elif exponential_equation == 3:
                print("\nWell done, you have succesfully understood how the exponential operator is used!!")
                lesson_learned_option=int(input("\nPick from these options:\n 1:Learn more about the math operators,\n 2:go to the home page,\n 3:Exit the application"))
                if lesson_learned_option == 1:
                    Math_op_Lesson()
                elif lesson_learned_option == 2:
                    home_page()
                elif lesson_learned_option == 3:
                    sys.exit()

def learned_option(lesson_learned_option):
    if lesson_learned_option == 1:
                    Math_op_Lesson()
                elif lesson_learned_option == 2:
                    home_page()
                elif lesson_learned_option == 3:
                    sys.exit()

