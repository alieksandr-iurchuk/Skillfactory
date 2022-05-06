from django import template


register = template.Library()

TEXTET_SYMBOLS = {
   'кино': '***',
   'блин': '***',
}

# Регистрируем наш фильтр под именем currency, чтоб Django понимал,
# что это именно фильтр для шаблонов, а не простая функция.
@register.filter(name='censor')
def replase(value, str='блин'):
   postfix = TEXTET_SYMBOLS[str]

   """
   value: значение, к которому нужно применить фильтр
   """

   return f'{value}{postfix}'
