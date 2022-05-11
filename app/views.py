import email
from django.shortcuts import render, HttpResponse, redirect
from django.conf import settings
from mailersend import emails
from mailerlite import MailerLiteApi
import math


def index(request):
    return render(request, 'app/index.html')

def thanks(request):
    return render(request, 'app/thanks.html')

def getGroup(request):
    api = MailerLiteApi(settings.MAILERLITE_API_KEY)
    print(api.groups.all(gfilters='Relcanonical'))
    return redirect("thanks")


def submitForm(request):
    if(request.method == "POST"):
        page_count = float(request.POST.get("page_count"))
        current_arpu = float(request.POST.get("current_arpu"))
        first_name = request.POST.get("first_name")
        email_address = request.POST.get("email_address")
        estimated_crawl = math.ceil((float(settings.ROWT_ESTIMATED_CRAWL)/100)*page_count)
        estimated_visits = math.ceil((float(settings.ROWT_ESTIMATED_VISIT)/100)*estimated_crawl)
        estimated_conversions = math.ceil((float(settings.ROWT_ESTIMATED_CONVERSIONS)/100)*estimated_visits)
        rowt = math.ceil(current_arpu*estimated_conversions)

        api_key = settings.MAILERSEND_API_KEY
        api = MailerLiteApi(settings.MAILERLITE_API_KEY)

        mailer = emails.NewEmail(api_key)

        # define an empty dict to populate with mail values
        mail_body = {}

        mail_from = {
            "name": "ROWT, Inc.",
            "email": "founder@rowt.co.uk",
        }

        recipients = [
            {
                "name": first_name,
                "email": email_address,
            }
        ]

        reply_to = [
            {
                "name": "ROWT, Inc.",
                "email": "founder@rowt.co.uk",
            }
        ]

        mailer.set_mail_from(mail_from, mail_body)
        mailer.set_mail_to(recipients, mail_body)
        mailer.set_subject("ROWT Estimate", mail_body)
        content = getHTMLTemplateForMail(page_count, current_arpu, first_name, estimated_crawl, 
        estimated_visits, estimated_conversions, rowt)
        mailer.set_html_content(content, mail_body)
        #mailer.set_plaintext_content("This is the text content", mail_body)
        mailer.set_reply_to(reply_to, mail_body)

        # using print() will also return status code and data
        print(mailer.send(mail_body))
        api.groups.add_single_subscriber(group_id=54475389360145449, subscribers_data={"email": email_address, "name": first_name}, autoresponders=False, resubscribe=False, as_json=False)
    return redirect(settings.ROWT_REDIRECT_URL)

def getHTMLTemplateForMail(page_count, current_arpu, first_name, estimated_crawl, 
        estimated_visits, estimated_conversions, rowt):
        return '''<!DOCTYPE html>
<html
  lang="en"
  xmlns="http://www.w3.org/1999/xhtml"
  xmlns:o="urn:schemas-microsoft-com:office:office"
>
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width,initial-scale=1" />
    <meta name="x-apple-disable-message-reformatting" />
    <title></title>
    <!--[if mso]>
      <style>
        table {
          border-collapse: collapse;
          border-spacing: 0;
          border: none;
          margin: 0;
        }
        div,
        td {
          padding: 0;
        }
        div {
          margin: 0 !important;
        }
      </style>
      <noscript>
        <xml>
          <o:OfficeDocumentSettings>
            <o:PixelsPerInch>96</o:PixelsPerInch>
          </o:OfficeDocumentSettings>
        </xml>
      </noscript>
    <![endif]-->
    <style>
      table,
      td,
      div,
      h1,
      p {
        font-family: Arial, sans-serif;
      }
      @media screen and (max-width: 530px) {
        .unsub {
          display: block;
          padding: 8px;
          margin-top: 14px;
          border-radius: 6px;
          background-color: #555555;
          text-decoration: none !important;
          font-weight: bold;
        }
        .col-lge {
          max-width: 100% !important;
        }
      }
      @media screen and (min-width: 531px) {
        .col-sml {
          max-width: 27% !important;
        }
        .col-lge {
          max-width: 73% !important;
        }
      }
    </style>
  </head>
  <body
    style="
      margin: 0;
      padding: 0;
      word-spacing: normal;
      background-color: #939297;
    "
  >
    <div
      role="article"
      aria-roledescription="email"
      lang="en"
      style="
        text-size-adjust: 100%;
        -webkit-text-size-adjust: 100%;
        -ms-text-size-adjust: 100%;
        background-color: #939297;
      "
    >
      <table
        role="presentation"
        style="width: 100%; border: none; border-spacing: 0"
      >
        <tr>
          <td align="center" style="padding: 0">
            <!--[if mso]>
          <table role="presentation" align="center" style="width:600px;">
          <tr>
          <td>
          <![endif]-->
            <table
              role="presentation"
              style="
                width: 94%;
                max-width: 600px;
                border: none;
                border-spacing: 0;
                text-align: left;
                font-family: Arial, sans-serif;
                font-size: 16px;
                line-height: 22px;
                color: #363636;
              "
            >
              <tr>
                <td style="padding: 30px; background-color: #ffffff">
                  <h1
                    style="
                      margin-top: 0;
                      margin-bottom: 16px;
                      font-size: 26px;
                      line-height: 32px;
                      font-weight: bold;
                      letter-spacing: -0.02em;
                    "
                  >
                    Hi, '''+first_name+'''! 
                  </h1>
                  <p style="margin: 0">
                    Kindly find your ROWT Estimate below: <br /><br />
                    Page Count: '''+str(page_count)+''' <br />
                    Current ARPU: £'''+str(current_arpu)+'''<br />
                    ====================<br />
                    Estimated Crawls: '''+str(estimated_crawl)+'''<br />
                    Estimated Monthy Visits: '''+str(estimated_visits)+'''<br />
                    Estimated Monthly Conversions: '''+str(estimated_conversions)+'''<br />
                    ====================<br />
                    Estimated ROWT: £'''+str(rowt)+'''<br />
                    ====================<br /><br />

                    ROWT is a product of Relcanonical.<br />
                    <a href="https://relcanonical.com/account/request"
                      >Create 400k+ Pages with Dynamic Content in 2s</a
                    >
                    <br /><br />

                    ROWT, Inc.<br />
                  </p>
                </td>
              </tr>
            </table>
            <!--[if mso]>
          </td>
          </tr>
          </table>
          <![endif]-->
          </td>
        </tr>
      </table>
    </div>
  </body>
</html>
'''