# -*- coding: utf-8 -*-
import requests
from meya import Component


class SendGrid(Component):

    def start(self):
        query = self.db.flow.get('query') or \
            self.properties.get('query') or "Message not found"
        url = "https://api.sendgrid.com/v3/mail/send"
        payload = "{\"personalizations\":[{\"to\":[{\"email\":\"john.doe@example.com\",\"name\":\"John Doe\"}],\"subject\":\"Testing Bot Email!\",\"headers\":{\"X-Accept-Language\":\"en\",\"X-Mailer\":\"MeyaBot\"}}],\"from\":{\"email\":\"support@example.com\",\"name\":\"Meya Bot\"},\"subject\":\"Testing Bot Email Subject!\",\"content\":[{\"type\":\"text/html\",\"value\":\""+query+"\"}]}"
        headers = {'authorization': "Bearer <YOUR API KEY>", 'content-type': "application/json"}
        r = requests.post(url, data=payload, headers=headers)
        message = self.create_message(text=r.status_code)
        return self.respond(message=message, action="next")
