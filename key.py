from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools 

SCOPES = 'https://www.googleapis.com/auth/calendar'
CLIENT_SECRET = 'client_secret.json'
#flow = IntsalledAppFlow.flow_from_client_secrets_file("client_secret.json", scopes=scopes)
#flow.run_console()
#pickle.dump(credentials, open("token.pkl","wb"))
#credentials = pickle.load(open("token.pkl","rb"))
#service = build("calendar", "v3",credentials=credentials)
#result = service. calendarList().list().execute()




store = file.Storage('storage.json')
credz = store.get()
if not credz or credz.invalid:
	flow = client.flow_from_clientsecrets(CLIENT_SECRET, SCOPES)
	credz = tools.run(flow, store)

SERVICE = build("calendar","v3", VERSION, http=credz.authorize(Http()))


    