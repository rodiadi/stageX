from django.shortcuts import render

from staging.calculator import stage_colon



def home(request):

    return render(
        request,
        "colon/home.html"
    )



def staging(request):

    result = None


    if request.method == "POST":


        T = request.POST.get("T")

        N = request.POST.get("N")

        M = request.POST.get("M")



        result = stage_colon(
            T,
            N,
            M
        )


    return render(
        request,
        "colon/staging.html",
        {
            "result": result
        }
    )