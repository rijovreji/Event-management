from django import forms
from .models import Booking

class Dateinput(forms.DateInput):
    input_type = 'date'

class BookingForms(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

        widgets = {
            'booking_date': Dateinput(),   # FIXED
        }

        labels = {
            'cust_Name': "Customer Name:",
            'cust_Phn': "Customer Phone:",
            'booking_date': "Booking Date:",
            'Name': "Event Name:",
        }


        # cust_Name = models.CharField(max_length=55, null=True, blank=True)
        # cust_Phn = models.IntegerField(null=True, blank=True)
        # Name = models.ForeignKey(Event, on_delete=models.CASCADE)
        # Booking_Date = models.DateField()
        # Booking_on = models.DateField(auto_now=True)