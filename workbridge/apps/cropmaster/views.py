from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View, ListView
from . models import Company

# Create your views here.


class CompanyRegistrationView(View):
    def get(self, *args, **kwargs):
        return render(self.request, 'cropmaster/company-res.html')
    def post(self, *args, **kwargs):
        name = self.request.POST.get("name")
        address = self.request.POST.get("address")
        city = self.request.POST.get("city")
        state = self.request.POST.get("state")
        country = self.request.POST.get("country")
        postal_code = self.request.POST.get("postal_code")
        phone_number = self.request.POST.get("phone_number")
        email = self.request.POST.get("email")
        website = self.request.POST.get("website")
        
        sav_obj = Company(name=name, address=address, city=city, state=state,
        country=country, postal_code=postal_code, email=email, website=website)
        sav_obj.save()
        return HttpResponseRedirect("")

class CompanyList(ListView):
    model = Company
    template_name = 'cropmaster/company-res-list.html' 
    context_object_name = 'company_list_context'  
    paginate_by = 1
    