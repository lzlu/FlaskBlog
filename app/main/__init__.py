# -*- coding:utf-8 -*-
from app.models import Permission

__author__ = 'lulizhou'
from flask import Blueprint
main = Blueprint('main', __name__)
from .import views, errors

@main.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)