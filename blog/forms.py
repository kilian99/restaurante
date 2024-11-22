from django import forms
from .models import Post, Reserva, Mesa

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['nombre_cliente', 'email_cliente', 'telefono_cliente', 'fecha', 'hora', 'mesa', 'num_personas', 'comentarios']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'hora': forms.TimeInput(attrs={'type': 'time'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'fecha' in self.data and 'hora' in self.data:
            fecha = self.data.get('fecha')
            hora = self.data.get('hora')
            mesas_ocupadas = Reserva.objects.filter(fecha=fecha, hora=hora).values_list('mesa_id', flat=True)
            self.fields['mesa'].queryset = Mesa.objects.exclude(id__in=mesas_ocupadas)