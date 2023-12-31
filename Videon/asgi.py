"""
ASGI config for Videon project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

from channels.routing import ProtocolTypeRouter, URLRouter

from channels.security.websocket import AllowedHostsOriginValidator

from viddeo.consumers import Videon

from django.urls import path

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Videon.settings')

application = ProtocolTypeRouter({
    'websocket': AllowedHostsOriginValidator(
        URLRouter([
            path('ws/', Videon.as_asgi())
        ])
    )
})
