from django.core.mail import send_mail
from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.
from django.views.generic import DeleteView, UpdateView, ListView

from appgym.models import Registration, Password, Sugesstion, Add_plans
from gymmanage import settings as se

def openadd(request):
    type="openadd"
    # type=request.GET.get("type")
    return render(request,"home.html",{"type":type})

def index(request):
    return render(request,"home.html")

def adlogin(request):
    ema=request.POST.get("email")
    pas=request.POST.get("password")
    # type=request.GET.get("type")
    if ema=="ss" and pas=="sb":
        return render(request,"admin_home.html")

def user(request):
    type="userss"
    # type=request.GET.get("type")
    return render(request,"home.html",{"type":type})

def userlogin(request):
    type="usermesa"
    email=request.POST.get("email")
    pas=request.POST.get("password")
    res = Registration.objects.filter(Email=email,Password=pas)
    if res:
        reg=Registration.objects.get(Email=email)
        # print(reg)
        return render(request,"user_home.html",{"reg":reg,"mess":"registered successfully","type":type})
    else:
        type = 'noulogin'
        return render(request,'home.html',{"mess":"invalid details",'type':type})

def uregister(request):
    type="uregister"
    # type=request.GET.get("type")
    lastid=Registration.objects.all()
    if lastid== None:
        id=1
        return render(request,"home.html",{"type":type,"idno":id})
    else:
        for x in lastid:
            id=x.Idno
            id+=1
        return render(request,"home.html",{"type":type,"idno":id})

def register(request):
    type = 'userss'
    idno = request.POST.get("idno")
    name = request.POST.get("name")
    age = request.POST.get("age")
    contact = request.POST.get("contact")
    email = request.POST.get("email")
    password = request.POST.get("password")
    address = request.POST.get("address")
    re=Registration(Idno=idno,Name=name,Age=age,Contact_no=contact,Email=email,Password=password,Address=address)
    re.save()
    return render(request, "home.html",{'type':type,"re":re})

def addplan(request):
    type=request.GET.get("type")
    return render(request,"admin_home.html",{"type":type})

def viewsuggestions(request):
    type=request.GET.get("type")
    res=Sugesstion.objects.all()
    # print(res)
    return render(request,"admin_home.html",{"type":type,"res":res})
    # model = Sugesstion
    # template_name = 'admin_home.html'
    # context_object_name = 'suggestion'


def payment(request):
    type=request.GET.get("type")
    return render(request,"admin_home.html",{"type":type})

def viewuser(request):
    type=request.GET.get("type")
    res=Registration.objects.all()
    # print(res)
    return render(request,"admin_home.html",{"type":type,"res":res})

def viewplans(request):
    type ='viewplans'
    u = request.GET.get('type')
    email=Registration.objects.get(Email=u)
    res = Add_plans.objects.all()
    return render(request,"user_home.html",{"type":type,'reg':email,'res':res})

def paymentp(request):
    type ="paymentp"
    email=request.GET.get("type")
    res = Registration.objects.get(Email=email)
    return render(request,"user_home.html",{"type":type,'reg':res})

def suggestion(request):
    type = "suggestion"
    email=request.GET.get("type")
    reg=Registration.objects.get(Email=email)
    return render(request,"user_home.html",{"type":type,'email':email,"reg":reg})

def viewprofile(request):
    type = 'viewprofile'
    email=request.GET.get("type")
    print(email)
    reg= Registration.objects.get(Email=email)
    return render(request,'user_home.html',{'reg':reg,'type':type})

def update(request):
    type="update"
    email=request.GET.get("type")
    reg=Registration.objects.get(Email=email)
    return render(request,"user_home.html",{"reg":reg,"type":type})

def updateuser(request):
    type="viewprofile"
    idno=request.POST.get("idno")
    name=request.POST.get("name")
    age=request.POST.get("age")
    contact=request.POST.get("contact")
    email=request.POST.get("email")
    pas=request.POST.get("password")
    address=request.POST.get("address")
    Registration(Name=name,Age=age,Contact_no=contact,Email=email,Password=pas,Idno=idno,Address=address).save()
    ure=Registration.objects.get(Email=email)
    return render(request,"user_home.html",{"type":type,'reg':ure})

def usuggestion(request):
    type="givesuggestion"
    email=request.POST.get("email")
    #print(email)
    sug=request.POST.get("suggestion")
    da=request.POST.get("date")
    reg= Registration.objects.get(Email=email)
    rea=Registration.objects.values("Email").filter(Email=email)
    for x in rea:
        rea=x['Email']
        print(rea)
    ssu=Sugesstion(suggestions=sug,date=da,Email=Registration.objects.get(Email=email))
    #print(ssu)
    ssu.save()
    return render(request,"user_home.html",{"mes":"saved succesfully","reg":reg,"type":type})


def userviewplans(request):
    type='viewplans'
    email=request.GET.get("type")
    reg=Registration.objects.get(Email=email)
    # print(reg)
    res=Add_plans.objects.all()
    return render(request,"user_home.html",{"type":type,'reg':reg,'res':res})


def admplans(request):
    type = 'plan'
    name=request.POST.get("name")
    description=request.POST.get("description")
    rrp=Add_plans(Name=name,Plan_Description=description)
    rrp.save()
    print(rrp)
    return render(request,"admin_home.html",{"mess":"added succesfully","rrp":rrp,'type':type})


def paymentaf(request):
    type="nopayment"
    email=request.POST.get("email")
    payment=request.POST.get("payment")
    reg=Registration.objects.get(Email=email)
    return render(request,"user_home.html",{"mess":"no payments done","reg":reg,"pay":payment,"type":type})


def back(request):
    type="login"
    return render(request,"user_login.html",{"type":type})


def newregister(request):
    type=request.GET.get("type")
    lastid = Registration.objects.last()
    print(lastid)
    if lastid == None:
        id = 1
    else:
        id = lastid.Idno + 1
    return render(request, "user_login.html", {"type": type, "idno": id})


def confirmdel(request):
    userdel=request.POST.get("d1")
    res=request.POST.get("email")
    # print(res)
    if userdel == "Yes":
        type="user"
        Registration.objects.get(Email=res).delete()
        return render(request,"home.html",{"type":type,"reg":res})
    else:
        type="viewprofile"
        res=Registration.objects.get(Email=res)
        return render(request,"user_home.html",{"type":type,"reg":res})


def delete(request):
    type="del"
    email=request.POST.get("email")
    reg=Registration.objects.get(Email=email)
    return render(request,"user_home.html",{"type":type,"reg":reg})


def adminlogout(request):
    return render(request,"home.html")

def userlogout(request):
    return render(request,"home.html")


def backuser(request):
    return render(request,"home.html")


def deleteuser(request):
    type='del'
    email=request.POST.get("email")
    reg=Registration.objects.get(Email=email)
    return render(request,"user_home.html",{"type":type,"reg":reg})

class adviewplans(ListView):
    model = Add_plans
    template_name = "admin_home.html"
    context_object_name = "view"

class updateplan(UpdateView):
    model = Add_plans
    template_name = "update_plan.html"
    success_url = "/uppie/"
    fields = ["Plan_Description"]

class deleteplan(DeleteView):
    model = Add_plans
    success_url = "/delview/"

# class forgetpass(ListView):
#     model = Registration
#     template_name = "admin_login.html"


def join(request):
    type="paymentp"
    email = request.GET.get("type")
    # payment = request.POST.get("payment")
    try:
        reg = Registration.objects.get(Email=email)
        return render(request,"user_home.html",{"type":type,"email":email,"reg":reg})
    except:
        return render(request,"user_home.html",{"type":type,"email":email})


def previoussuggestions(request):
    email=request.POST.get("type")
    message=request.POST.get("message")
    reg=Registration.objects.get(Email=email)
    reeg=Sugesstion.objects.get(suggestions=message)
    return render(request,"user_home.html",{"reg":reg,"type":type,"reeg":reeg})


# def delsugg(request):
#
#     return None


def viewusersuggestions(request):
    # type ="viewsugg"
    email=request.GET.get("type")
    # print(message)
    reg=Registration.objects.get(Email=email)
    reee=Sugesstion.objects.filter(Email=email)
    if reee:
        type = "viewsugg"
        return render(request,"user_home.html",{"reg":reg,"type":type,"reee":reee,"email":email})
    else:
        type ="suggestion"
        return  render(request,"user_home.html",{"reg":reg,"type":type,"reee":reee,"email":email,"mess":"not valid"})


def goback(request):
    type="suggestion"
    email=request.GET.get("type")
    reg=Registration.objects.get(Email=email)
    return render(request,"user_home.html",{"email":email,"reg":reg,"type":type})


def deleteusersuggestion(request):
    type="delli"
    email=request.POST.get("email")
    suggest=request.POST.get("suggest")
    # print(suggest)
    # print(email)
    reg=Registration.objects.get(Email=email)
    rem=Sugesstion.objects.get(suggestions=suggest)
    return render(request,"user_home.html",{"type":type,"reg":reg,"rem":rem})


def conuserdel(request):
    userdel = request.POST.get("r1")
    email=request.POST.get("email")
    res = request.POST.get("suggestions")
    # print(res)
    # print(res)
    if userdel == "Yes":
        type = "suggestion"
        reg = Registration.objects.get(Email=email)
        Sugesstion.objects.get(suggestions=res).delete()
        return render(request, "user_home.html", {"type": type, "reg": reg})

    else:
        type ="suggestion"
        reg=Registration.objects.get(Email=email)
        # print(reg)
        return  render(request,"user_home.html",{"type":type,"reg":reg})

# # class deletevsugg(DeleteView):
#     model = View_suggestion
# #     success_url = "/delusugg/"

def aboutus(request):
    type="aboutgym"
    return render(request,"home.html",{"type":type})


def home(request):
    # type="homiie"
    return render(request,"home.html",{"message":"welcome"})


def showuserlogin(request):
    type='userss'
    return render(request,"home.html",{"type":type})

def deleteaduser(request):
    type="viewuser"
    email=request.POST.get("email")
    print(email)
    Registration.objects.get(Email=email).delete()
    res=Registration.objects.all()
    print(res)
    return render(request,"admin_home.html",{"type":type,"res":res})


# def confirmaddel(request):
#     type="mess"
#     condel=request.POST.get("y1")
#     res=request.POST.get("email")
#     print(res)
#     if condel == "Yes":
#         type="viewuser"
#         Registration.objects.get(Email=res).delete()
#         return render(request,"admin_home.html",{"type":type,"res":res,"mess":"deleted","type":type1})
#     else:
#         type="viewuser"
#         res=Registration.objects.get(Email=res)
#         return render(request,"admin_home.html",{"type":type,"res":res})

def viewuserupdate(request):
    type="userup"
    email=request.GET.get("type")
    reg=Registration.objects.get(Email=email)
    return render(request,"admin_home.html",{"reg":reg,"type":type})


def updateuadd(request):
    type ="viewuser"
    idno=request.POST.get("idno")
    name=request.POST.get("name")
    age=request.POST.get("age")
    contact=request.POST.get("contact")
    email=request.POST.get("email")
    password=request.POST.get("password")
    address=request.POST.get("address")
    Registration(Idno=idno,Name=name,Age=age,Contact_no=contact,Email=email,Password=password,Address=address).save()
    reg=Registration.objects.all()
    print(reg)
    return render(request,"admin_home.html",{"type":type,"res":reg})


def forgetpassword(request):
    type="forgotpasswprd"
    return render(request,"home.html",{"type":type})
#
# def SendPassword(request):
#     email=request.POST.get('email')
#     try:
#         reg=Registration.objects.get(Email=email)
#         if reg:
#             email1=reg.Email
#             password=reg.Password
#             finalpassword=str(password)
#             Subject="Forgot Password Details"
#             Message="Your Password Is"+password
#             print(Subject,Message)
#             sendemail=EmailMessage(Subject,Message,se.EMAIL_HOST_USER,email1)
#             sendemail.send(True)
#             return render(request,"home.html",{"type":"forgotpasswprd","fpmessage":"Password is sended to your Mail Id","finalpassword":finalpassword})
#     except:
#         return render(request, "home.html",{"type": "forgotpasswprd", "fpmessage": "Invalid Mail"})
# def getpassword(request):
#     email=request.POST.get("email")
#     res=Registration.objects.get(Email=email)
#     print(res.Email)
#     if res:
#         pa=Password.objects.filter(email=res.Email)
#         print(pa.email)
#         if pa:
#             type = 'userss'
#             send_mail("password",pa.password,se.EMAIL_HOST_USER,{res.Email})
#             Registration.objects.filter(Email=res.Email).update(Password=pa.password)
#             return render(request,"home.html",{"reg":res,"type":type})
#     else:
#         type= "usermesa"
#         return render(request,"home.html",{"type":type})


def getpass(request):
    email = request.POST.get("email")
    res = Registration.objects.get(Email=email)
    print(res.Email)
    if res:
        pa = Password.objects.get(email=res.Email)
        print(pa)
        print(pa.password)
        if pa:
            type = 'userss'
            send_mail("userforgetpassword",pa.password, se.EMAIL_HOST_USER,[res.Email])
            Registration.objects.filter(Email=res.Email).update(Password=pa.password)
            return render(request, "home.html", {"reg": res, "type": type})
    else:
        type = "usermesa"
        return render(request, "home.html", {"type": type})

