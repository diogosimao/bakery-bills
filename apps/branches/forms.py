from django import forms
from django.template import Template
from material import Layout


class BranchForm(forms.Form):
    description = forms.CharField()
    address = forms.CharField()
    city = forms.CharField()
    state = forms.CharField()

    layout = Layout('description', 'address', 'city', 'state',)

    template = Template("""
    {% form %}
        {% part form.description prefix %}<i class="material-icons prefix">domain</i>{% endpart %}
        {% part form.address prefix %}<i class="material-icons prefix">home</i>{% endpart %}
        {% part form.city prefix %}<i class="material-icons prefix">map</i>{% endpart %}
        {% part form.state prefix %}<i class="material-icons prefix">map</i>{% endpart %}
    {% endform %}
    """)

    buttons = Template("""
        <button class="btn btn-primary pull-right" type="submit">Add branch</button>
    """)

    title = "Add branch"

    action = Template("{{view.form_action}}")

