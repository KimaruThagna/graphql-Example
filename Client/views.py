from django.shortcuts import render

def home(request):

    return (render(request,'graphql/index.html',{"form":myForm}))