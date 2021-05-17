def get_input(prompt="", type_to_return=str, retry=True):
    try:
        return type_to_return(input(prompt + " "))
    except Exception as error:
        print(error)
        if retry:
            get_input(prompt, type_to_return, retry)
        else:
            raise error
