from user.views.register import register
from user.views.login import login

menu_dict = {
    "name": "Laboratory Main Menu",
    "description": "Group 3 laboratory project",
    "children": [
        {
            "name": "Register/Login",
            "description": "FREE to registration",
            "children": [{
                "name": "Register",
                "description": "FREE to registration",
                "function": register,

            },
                {
                    "name": "Login",
                    "description": "you need login to access",
                    "function": login,

                }, ]

        },

        {
            "name": "Patients List",
            "description": "show list of patients",
            "children": []
        },
        {
            "name": "New test",
            "description": "Test list",
            "children": [{
                "name": "Corona Test",
                "description": "corona test",
                "children": []
            }]

        }

    ]
}
