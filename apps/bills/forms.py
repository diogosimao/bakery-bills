from django import forms
from django.template import Template
from material import Layout

from apps.bills.models import Bill
from apps.branches.models import Branch


class BillForm(forms.Form):
    description = forms.CharField()
    debit = forms.DecimalField()
    due_date = forms.DateField()
    branch = forms.ModelChoiceField(queryset=Branch.objects.all(), to_field_name="slug")

    layout = Layout('description', 'debit', 'due_date', 'branch',)

    template = Template("""
    {% form %}
        {% part form.description prefix %}<i class="material-icons prefix">description</i>{% endpart %}
        {% part form.debit prefix %}<i class="material-icons prefix">attach_money</i>{% endpart %}
        {% part form.due_date prefix %}<i class="material-icons prefix">date_range</i>{% endpart %}
        {% part form.branch prefix %}<i class="material-icons prefix">domain</i>{% endpart %}
    {% endform %}
    {% if messages %}
      <ul class="messages">
        {% for message in messages %}
          <li class="{{ message.tags }}">{{ message }}</li>
        {% endfor %}
      </ul>
    {% endif %}
    """)

    buttons = Template("""
        <button class="btn btn-primary pull-right" type="submit">Add bill</button>
    """)

    title = "Add bill"

    action = Template("{{view.form_action}}")


class PaymentForm(forms.Form):
    payment_date = forms.DateField()
    bill = forms.ModelChoiceField(
        queryset=Bill.objects.select_related('payments').filter(payments__isnull=True), to_field_name="slug")

    layout = Layout('payment_date', 'bill',)

    template = Template("""
    {% form %}
        {% part form.payment_date prefix %}<i class="material-icons prefix">date_range</i></i>{% endpart %}
        {% part form.bill prefix %}<i class="material-icons prefix">receipt</i>{% endpart %}
    {% endform %}
    {% if messages %}
      <ul class="messages">
        {% for message in messages %}
          <li class="{{ message.tags }}">{{ message }}</li>
        {% endfor %}
      </ul>
    {% endif %}
    """)

    buttons = Template("""
        <button class="btn btn-primary pull-right" type="submit">Register payment</button>
    """)

    title = "Register Payment"

    action = Template("{{ view.form_action }}")

