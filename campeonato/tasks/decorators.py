from django.shortcuts import redirect

from django.contrib.auth.decorators import login_required
from rolepermissions.checkers import has_role

def grupo_requerido(group_name):
    def decorator(view_func):
        @login_required
        def wrapped_view(request, *args, **kwargs):
            if has_role(request.user, group_name):
                return view_func(request, *args, **kwargs)
            else:
                # Redirecionar para uma página de acesso negado ou realizar alguma outra ação
                return redirect('pagina_de_acesso_negado') 
        return wrapped_view
    return decorator
