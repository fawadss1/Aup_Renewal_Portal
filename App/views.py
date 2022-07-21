from django.contrib import messages
from django.shortcuts import render
from . import models
import datetime

Y = datetime.datetime.now().strftime('%y')


def home(request):
    if request.method == 'POST':
        # degree = request.POST.get('degree')
        program = request.POST.get('program')
        semester = request.POST.get('semester')
        rollNo = request.POST.get('rollNo')
        if not models.Student.objects.filter(Semester__Name=semester, Roll_No=rollNo, Program__Program_Name=program):
            messages.error(request, 'Student Record Not Found')
        else:
            stdData = models.Student.objects.filter(Semester__Name=semester, Roll_No=rollNo,
                                                    Program__Program_Name=program)
            return render(request, 'Home.html', {'StdData': stdData})
    programs = models.Department.objects.all()
    semesters = models.Semester.objects.all()
    return render(request, 'Home.html', {'programs': programs, 'semesters': semesters})


def slip(request, prog, sem, rollNo):
    global feeInWords
    stdData = models.Student.objects.filter(Semester__Name=sem, Roll_No=rollNo,
                                            Program__Program_Name=prog)
    for i in stdData:
        num = i.Semester.Fee
        feeInWords = convert(num)+' Only'
    return render(request, 'Slip.html', {'StdData': stdData, 'year': Y, 'feeInWords': feeInWords})


def convert(num):
    units = (
        "", "One ", "Two ", "Three ", "Four ", "Five ", "Six ", "Seven ", "Eight ", "Nine ", "Ten ", "Eleven ",
        "Twelve ", "Thirteen ", "Fourteen ", "Fifteen ", "Sixteen ", "Seventeen ", "Eighteen ", "Nineteen ")
    tens = ("", "", "Twenty ", "Thirty ", "Forty ", "Fifty ", "Sixty ", "Seventy ", "Eighty ", "Ninety ")
    if num < 0:
        return "Minus " + convert(-num)
    if num < 20:
        return units[num]
    if num < 100:
        return tens[num // 10] + units[int(num % 10)]
    if num < 1000:
        return units[num // 100] + "Hundred " + convert(int(num % 100))
    if num < 1000000:
        return convert(num // 1000) + "Thousand " + convert(int(num % 1000))
    if num < 1000000000:
        return convert(num // 1000000) + "Million " + convert(int(num % 1000000))
    return convert(num // 1000000000) + "Billion " + convert(int(num % 1000000000))
