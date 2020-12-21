import helper
import json

def func(x):
    return x + 1


def test_add_Well():
    clinicID = 1
    professionalID = "123456"
    codClient = 1
    practiceID = 1
    reservationDate = "2020-12-18 18:59"
    appointmentDay = "2020-12-26 16:00"
    notified = 0
    cancelled = 0
    finalized = 0
    
    title = "Esto es una prueba"
    description = "Prueba" 

    data = [clinicID,professionalID,codClient,practiceID,reservationDate,appointmentDay,notified,cancelled,finalized,title,description]
    assert json.loads(json.dumps(helper.add_event(data)))["error"] == 0


def test_add_Bad():
    clinicID = None
    professionalID = "123456"
    codClient = 1
    practiceID = 1
    reservationDate = "2020-12-18 18:59"
    appointmentDay = "2020-12-26 16:00"
    notified = 0
    cancelled = 0
    finalized = 0
    
    title = "Esto es una prueba"
    description = "Prueba" 

    data = [clinicID,professionalID,codClient,practiceID,reservationDate,appointmentDay,notified,cancelled,finalized,title,description]
    assert json.loads(json.dumps(helper.add_event(data)))["error"] == 3


def test_getClientEvents_Well():

    clientID = 2

    assert json.loads(json.dumps(helper.get_client_events(clientID)))["error"] == 0


def test_getClientEvents_Bad():

    clientID = 5

    assert json.loads(json.dumps(helper.get_client_events(clientID)))["error"] == 1



def test_update_event_Well():

    appointmentID = 1
    clinicID = 1
    professionalID = "123456"
    codClient = 1
    practiceID = 1
    reservationDate = "2020-11-27 14:59"
    appointmentDay = "2020-11-24 12:00"
    notified = 0
    cancelled = 0
    finalized = 0
    
    title = "Limprieza para los dientes"
    description = "Estan muy sucios"

    data = [appointmentID, clinicID,professionalID,codClient,practiceID,reservationDate,appointmentDay,notified,cancelled,finalized,title,description]

    assert json.loads(json.dumps(helper.update_event(data)))["error"] == 0



def test_update_event_Bad():

    appointmentID = 250
    clinicID = 1
    professionalID = "123456"
    codClient = 1
    practiceID = 1
    reservationDate = "2020-11-27 14:59"
    appointmentDay = "2020-11-24 12:00"
    notified = 0
    cancelled = 0
    finalized = 0
    
    title = "Limprieza para los dientes"
    description = "Estan muy sucios"

    data = [appointmentID, clinicID,professionalID,codClient,practiceID,reservationDate,appointmentDay,notified,cancelled,finalized,title,description]

    assert json.loads(json.dumps(helper.update_event(data)))["error"] == 1




def test_delete_event_Well():

    appointmentID = 1

    data = [appointmentID]

    assert json.loads(json.dumps(helper.delete_event(data)))["error"] == 0



def test_delete_event_Bad():

    appointmentID = 125

    data = [appointmentID]

    assert json.loads(json.dumps(helper.delete_event(data)))["error"] == 1


def test_notify_event_Well():

    appointmentID = 1

    data = [appointmentID]

    assert json.loads(json.dumps(helper.notify_event(data)))["error"] == 0



def test_notify_event_Bad():

    appointmentID = 125

    data = [appointmentID]

    assert json.loads(json.dumps(helper.notify_event(data)))["error"] == 1
    

def test_finalize_event_Well():

    appointmentID = 1

    data = [appointmentID]

    assert json.loads(json.dumps(helper.finalize_event(data)))["error"] == 0



def test_finalize_event_Bad():

    appointmentID = 125

    data = [appointmentID]

    assert json.loads(json.dumps(helper.finalize_event(data)))["error"] == 1



def test_get_professional_events_Well():

    professionalID = "1"

    assert json.loads(json.dumps(helper.get_professional_events(professionalID)))["error"] == 0


def test_get_professional_events_Bad():

    professionalID = "12"

    assert json.loads(json.dumps(helper.get_professional_events(professionalID)))["error"] == 1



def test_get_professional_events_byClinic_Well():

    clinicID = 1
    professionalID = "1"

    assert json.loads(json.dumps(helper.get_professional_events_byClinic(clinicID,professionalID)))["error"] == 0


def test_get_professional_events_byClinic_Bad():

    clinicID = 1
    professionalID = "12"

    assert json.loads(json.dumps(helper.get_professional_events_byClinic(clinicID,professionalID)))["error"] == 1


def test_get_professional_events_byClinic_Bad2():

    clinicID = 12
    professionalID = "1"

    assert json.loads(json.dumps(helper.get_professional_events_byClinic(clinicID,professionalID)))["error"] == 1




def test_get_professional_events_not_cancelled_Well():

    clinicID = 1
    professionalID = "1"

    assert json.loads(json.dumps(helper.get_professional_events_not_cancelled(clinicID,professionalID)))["error"] == 0


def test_get_professional_events_not_cancelled_Bad():

    clinicID = 1
    professionalID = "12"

    assert json.loads(json.dumps(helper.get_professional_events_not_cancelled(clinicID,professionalID)))["error"] == 1


def test_get_professional_events_not_cancelled_Bad2():

    clinicID = 12
    professionalID = "1"

    assert json.loads(json.dumps(helper.get_professional_events_not_cancelled(clinicID,professionalID)))["error"] == 1



def test_get_client_events_Well():

    clientID = 2

    assert json.loads(json.dumps(helper.get_client_events(clientID)))["error"] == 0


def test_get_client_events_Bad():

    clientID = 12

    assert json.loads(json.dumps(helper.get_client_events(clientID)))["error"] == 1





def test_get_professional_day_events_Well():

    clinicID = 1
    professionalID = "123456"
    beginDate = "2020-12-26 00:00"
    finishDate = "2020-12-26 23:59"
    data = [clinicID,professionalID,beginDate,finishDate]


    assert json.loads(json.dumps(helper.get_professional_day_events(data)))["error"] == 0


def test_get_professional_day_events_Bad():

    clinicID = 1
    professionalID = "123456"
    beginDate = "2020-11-18 00:00"
    finishDate = "2020-11-18 23:59"
    data = [clinicID,professionalID,beginDate,finishDate]


    assert json.loads(json.dumps(helper.get_professional_day_events(data)))["error"] == 1



def test_get_professional_schedule_Well():

    clinicID = 1
    professionalID = "1"


    assert json.loads(json.dumps(helper.get_professional_schedule(clinicID,professionalID)))["error"] == 0


def test_get_professional_schedule_Bad():

    clinicID = 1
    professionalID ="123"


    assert json.loads(json.dumps(helper.get_professional_schedule(clinicID,professionalID)))["error"] == 1



def test_get_professional_schedule_Bad2():

    clinicID = 12
    professionalID ="1"


    assert json.loads(json.dumps(helper.get_professional_schedule(clinicID,professionalID)))["error"] == 1



def test_get_professional_day_schedule_Well():

    clinicID = 1
    professionalID = "1"
    date = 1
    data = [clinicID,professionalID,date]


    assert json.loads(json.dumps(helper.get_professional_day_schedule(data)))["error"] == 0


def test_get_professional_day_schedule_Bad():

    clinicID = 1
    professionalID = "1"
    date = 4
    data = [clinicID,professionalID,date]


    assert json.loads(json.dumps(helper.get_professional_day_schedule(data)))["error"] == 1



    
def test_get_client_pending_events_Well():

    clientID = 1


    assert json.loads(json.dumps(helper.get_client_pending_events(clientID)))["error"] == 0


def test_get_client_pending_events_Bad():

    clientID = 3


    assert json.loads(json.dumps(helper.get_client_pending_events(clientID)))["error"] == 1



def test_get_specialities_Well():

    assert json.loads(json.dumps(helper.get_specialities()))["error"] == 0


def test_get_practices_Well():

    assert json.loads(json.dumps(helper.get_practices()))["error"] == 0





    
def test_get_practices_by_specialities_Well():

    specialityID = 3


    assert json.loads(json.dumps(helper.get_practices_by_specialities(specialityID)))["error"] == 0


def test_get_practices_by_specialities_Bad():

    specialityID = 2


    assert json.loads(json.dumps(helper.get_practices_by_specialities(specialityID)))["error"] == 1


def test_get_professionals_Well():

    assert json.loads(json.dumps(helper.get_professionals()))["error"] == 0


def test_get_clients_Well():

    assert json.loads(json.dumps(helper.get_clients()))["error"] == 0



def test_get_professionals_by_specialities_Well():

    specialityID = 3


    assert json.loads(json.dumps(helper.get_professionals_by_specialities(specialityID)))["error"] == 0


def test_get_professionals_by_specialities_Bad():

    specialityID = 2


    assert json.loads(json.dumps(helper.get_professionals_by_specialities(specialityID)))["error"] == 1



def test_get_clinics_Well():

    assert json.loads(json.dumps(helper.get_clinics()))["error"] == 0



def test_get_professionals_clinics_Well():

    professionalID = "1"


    assert json.loads(json.dumps(helper.get_professionals_clinics(professionalID)))["error"] == 0


def test_get_professionals_clinics_Bad():

    professionalID = "9874"


    assert json.loads(json.dumps(helper.get_professionals_clinics(professionalID)))["error"] == 1




def test_login_Well():

    email = "dios@gmail.com"
    password = "admin"


    assert json.loads(json.dumps(helper.login(email, password)))["error"] == 0


def test_login_Bad():

    email = "dios@gmail.com"
    password = "entrar"


    assert json.loads(json.dumps(helper.login(email, password)))["error"] == 1



def test_login_Bad2():

    email = "jesus@gmail.com"
    password = "admin"


    assert json.loads(json.dumps(helper.login(email, password)))["error"] == 1




def test_isProfessional_Well():

    userID = 3

    error = json.loads(json.dumps(helper.isProfessional(userID)))["error"]
    isProf = json.loads(json.dumps(helper.isProfessional(userID)))["status"]["isProfessional"]

    assert  error == 0 

    assert  isProf == True


def test_isProfessional_Bad():

    userID = 1

    error = json.loads(json.dumps(helper.isProfessional(userID)))["error"]
    isProf = json.loads(json.dumps(helper.isProfessional(userID)))["status"]["isProfessional"]

    assert  error == 0 

    assert  isProf == False


def test_isClient_Well():

    userID = 1

    error = json.loads(json.dumps(helper.isClient(userID)))["error"]
    isClient = json.loads(json.dumps(helper.isClient(userID)))["status"]["isClient"]

    assert  error == 0 

    assert  isClient == True


def test_isClient_Bad():

    userID = 3

    error = json.loads(json.dumps(helper.isClient(userID)))["error"]
    isClient = json.loads(json.dumps(helper.isClient(userID)))["status"]["isClient"]

    assert  error == 0 

    assert  isClient == False




def test_get_user_data_Well():

    userID = 1


    assert json.loads(json.dumps(helper.get_user_data(userID)))["error"] == 0


def test_get_user_data_Bad():

    userID = 1235


    assert json.loads(json.dumps(helper.get_user_data(userID)))["error"] == 1



def test_edit_user_Well():

    userID = 1
    nombre = "Butros Asis"
    dni = "41695105"
    email = "butros.asis@gmail.com"
    telefono = "3548431878"

    data = [userID, nombre, dni, email, telefono]


    assert json.loads(json.dumps(helper.edit_user(data)))["error"] == 0


def test_edit_user_Bad():

    userID = 1222
    nombre = "Butros"
    dni = "41695105"
    email = "butros.asis@gmail.com"
    telefono = "3548431878"

    data = [userID, nombre, dni, email, telefono]


    assert json.loads(json.dumps(helper.edit_user(data)))["error"] == 1

