from twilio.rest import Client

# cliente acesso confidencial TWILIO_ACCOUNT_SID and AUTH_TOKEN
client = ' api '

# acesso twilio e acesse api e pegue seu numero
from_whatsapp_number='+*******'
# substitua este número pelo seu próprio número do WhatsApp Messaging
to_whatsapp_number='+*********'

client.messages.create(body='Você vai conseguir!',
                       from_=from_whatsapp_number,
                       to=to_whatsapp_number)
