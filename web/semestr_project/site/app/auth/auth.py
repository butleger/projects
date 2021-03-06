from flask import Blueprint, render_template, abort, request
from auth.controllers import HomeController, LoginController, \
                    CreateArticleController, LogOutController, \
                    CreateUserController


auth = Blueprint("auth", __name__)

@auth.route('/create_user', methods=['GET', 'POST'])
def create_user_wrapper():
    return CreateUserController.get_response()


@auth.route('/home')
def home_wrapper():
    return HomeController.get_response()


@auth.route('/login', methods=['GET', 'POST'])
def login_wrapper():
    return LoginController.get_response()


@auth.route('/create_article', methods=['GET', 'POST'])
def create_article_wrapper():
    return CreateArticleController.get_response()


@auth.route('/logout')
def logout_wrapper():
    return LogOutController.get_response()

