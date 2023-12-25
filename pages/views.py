from django.shortcuts import render

from pages.models import ScrollModel


def homt_page_view(request):
    scrolls = ScrollModel.objects.all().order_by('-pk')[:5]
    context = {
        "scrolls": scrolls
    }
    return render(request,'index.html',context)