from vulnerabilities.models import Vulnerability
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render

@api_view(["GET"])
def vulnerabilities_per_year(request):
    data = {}

    vulnerabilities = Vulnerability.objects.all()

    for vuln in vulnerabilities:
        if vuln.vulnerability_id:
            parts = vuln.vulnerability_id.split("-")
            if len(parts) > 1 and parts[1].isdigit():
                year = parts[1]
                data[year] = data.get(year, 0) + 1

    return Response(data)

@api_view(["GET"])
def severity_distribution(request):
    return Response({
        "LOW": 2,
        "MEDIUM": 3,
        "HIGH": 1
    })

def dashboard(request):
    return render(request, "dashboard.html")