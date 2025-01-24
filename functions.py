def GVI(prompt, valid_response): #GVI = Get Valid Input, mechanism for evaluating proper inputs 
    while True:
        user_in = input(prompt).strip().upper()
        if user_in in valid_response:
            return user_in
        else: 
            print(f"No Dummy! That is an Invalid Input!!! Choose from: {', '.join(valid_response)}\n")
