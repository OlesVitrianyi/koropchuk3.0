from .forms import *

menu = [{'title': 'Про сайт', 'url_name': 'about'},
        {'title': 'Додати статтю', 'url_name': 'add_page'},
        {'title': "Зворотній зв'язок", 'url_name': 'contact'},
        {'title': 'Увійти', 'url_name': 'login'}
]


class DataMixin:
        def get_user_context(self, **kwargs):
                context = kwargs
                #cats = Category.objects.all()
                context['menu'] = menu
                #context['cats'] = cats
                if 'cat_selected' not in context:
                        context['cat_selected'] = 0
                return context