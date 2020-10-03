from controllers.signin import Signin
from controllers.login import Login
from controllers.appointment import Appointment

client = {
    "signin":"/signin","view_func_signin":Signin.as_view("app_signin"),
    "login":"/login", "view_func_login":Login.as_view('app_login'),
}

appointment = {
    "appointment":"/appointment", "view_func_appointment":Appointment.as_view('app_appointment'),
}